# Generated by Django 5.0.1 on 2024-03-13 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_product_categories_customer_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='percentage',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='price_and_quantity_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='selling_price',
            field=models.IntegerField(),
        ),
    ]
