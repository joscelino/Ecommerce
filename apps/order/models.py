from django.db import models
from django.contrib.auth.models import User


class Base(models.Model):

    """  Order database registration control """
    registration = models.DateField('Registration data', auto_now_add=True)
    modification = models.DateField('Modification data', auto_now=True)
    active = models.BooleanField('Active', default=True)

    class Meta:
        abstract = True


class Order(Base):

    """ Order database fields """
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    total = models.FloatField()
    status = models.CharField(
        default='R',
        max_length=1,
        choices=(
            ('A', 'Approved'),
            ('R', 'Registered'),
            ('C', 'Canceled'),
            ('I', 'In approval'),
            ('T', 'In transport'),
            ('D', 'Delivered'),
        )
    )

    def __str__(self):
        return f'Order number: {self.id}'


class ItemOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.CharField(max_length=60)
    product_id = models.PositiveIntegerField()
    variation = models.CharField(max_length=50)
    variation_id = models.PositiveIntegerField()
    price = models.FloatField()
    promotional_price = models.FloatField(default=0)
    image = models.CharField(max_length=2000)

    def __str__(self):
        return f'{self.order}'

    class Meta:
        verbose_name = 'Order item'
        verbose_name_plural = 'Order items'
