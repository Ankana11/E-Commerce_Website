# Generated by Django 4.2.3 on 2023-09-16 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0004_rename_phonenumber_contact_pnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]