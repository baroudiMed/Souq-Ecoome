# Generated by Django 3.0.7 on 2020-06-19 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_delete_product_accessories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Accessories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PACCAlternatives', models.ManyToManyField(related_name='accessories_product', to='product.Product')),
                ('PACCProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mainAccessory_product', to='product.Product')),
            ],
            options={
                'verbose_name': 'Product Accessory',
                'verbose_name_plural': 'Product Accessories',
            },
        ),
    ]
