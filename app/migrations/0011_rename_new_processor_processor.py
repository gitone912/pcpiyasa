# Generated by Django 4.1.6 on 2023-02-17 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_product_added_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='new_processor',
            new_name='processor',
        ),
    ]