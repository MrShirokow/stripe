# Generated by Django 4.1 on 2022-11-23 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stripe_payment', '0003_alter_product_options_alter_product_price'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Item',
        ),
    ]
