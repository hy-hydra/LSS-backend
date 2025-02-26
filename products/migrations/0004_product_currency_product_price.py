# Generated by Django 4.2.5 on 2023-10-17 21:09

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_source_url_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='currency',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=10, null=True),
        ),
    ]
