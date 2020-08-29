from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError

import re
from utils.cpfvalidator import cpf_validator


class Base(models.Model):

    """  Costumer database registration control """
    registration = models.DateField('Registration data', auto_now_add=True)
    modification = models.DateField('Modification data', auto_now=True)
    active = models.BooleanField('Active', default=True)

    class Meta:
        abstract = True


class Costumer(Base):
    """ Costumer database fields """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(verbose_name='Age')
    birth_date = models.DateField(verbose_name='Birth date')
    cpf = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return f'{self.user}'

    def clean(self):
        error_messages = {}
        if not cpf_validator(self.cpf):
            error_messages['cpf']: 'Please, type a valid cpf.'

        if self.age > 120:
            error_messages['age']: 'Please, check the age.'

        if error_messages:
            raise ValidationError(error_messages)


class CostumerAddress(models.Model):
    """ Costumer address database fields"""
    costumer = models.ForeignKey(Costumer, on_delete=models.CASCADE)
    address = models.CharField(verbose_name='Street', max_length=50)
    number = models.CharField(verbose_name='number', max_length=5)
    adjunct_address = models.CharField(verbose_name='Adjunct address', max_length=30)
    district = models.CharField(verbose_name='District', max_length=30)
    zip_code = models.CharField(verbose_name='Zip code', max_length=8)
    city = models.CharField(verbose_name='City', max_length=30)
    state = models.CharField(
        verbose_name='state',
        max_length=2,
        default='SP',
        choices=(
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
        )
    )

    def clean(self):
        error_messages = {}
        if re.search(r'[^0-9]', self.zip_code) or len(self.zip_code) < 8:
            error_messages['zip_code']: 'Please, type a valid zip code.'

        if error_messages:
            raise ValidationError(error_messages)

    def __str__(self):
        return self.address
