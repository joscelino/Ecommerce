# Generated by Django 2.2.15 on 2020-08-26 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20200826_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='short_description',
            field=models.TextField(max_length=50, verbose_name='Short description'),
        ),
    ]
