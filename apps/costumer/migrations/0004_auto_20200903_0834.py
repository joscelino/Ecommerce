# Generated by Django 2.2.15 on 2020-09-03 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('costumer', '0003_auto_20200826_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costumer',
            name='age',
            field=models.IntegerField(verbose_name='Age'),
        ),
    ]