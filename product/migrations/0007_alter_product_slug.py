# Generated by Django 4.1.7 on 2023-02-24 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
