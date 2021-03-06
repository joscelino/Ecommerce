# Generated by Django 2.2.15 on 2020-09-03 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('costumer', '0007_auto_20200903_0922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='costumeraddress',
            name='costumer',
        ),
        migrations.RemoveField(
            model_name='costumeraddress',
            name='id',
        ),
        migrations.AddField(
            model_name='costumeraddress',
            name='costumer_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='costumer.Costumer'),
            preserve_default=False,
        ),
    ]
