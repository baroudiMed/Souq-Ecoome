# Generated by Django 3.0.7 on 2020-06-20 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_product_prdescountprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PDRISBestSeller',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='PDRISNew',
            field=models.BooleanField(default=True),
        ),
    ]
