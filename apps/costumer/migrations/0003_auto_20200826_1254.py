# Generated by Django 2.2.15 on 2020-08-26 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costumer', '0002_auto_20200825_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costumer',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]