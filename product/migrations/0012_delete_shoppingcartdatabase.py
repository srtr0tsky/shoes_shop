# Generated by Django 4.1.7 on 2023-02-27 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_alter_shoppingcartdatabase_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ShoppingCartDatabase',
        ),
    ]
