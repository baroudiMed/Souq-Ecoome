# Generated by Django 3.0.7 on 2020-06-23 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart_shopping', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='profil',
            new_name='profile',
        ),
    ]
