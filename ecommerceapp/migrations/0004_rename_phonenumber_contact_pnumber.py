# Generated by Django 4.2.3 on 2023-09-13 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0003_orders_orderupdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='phonenumber',
            new_name='pnumber',
        ),
    ]