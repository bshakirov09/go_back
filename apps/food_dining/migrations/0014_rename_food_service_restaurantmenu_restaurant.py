# Generated by Django 4.0.2 on 2022-03-18 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_dining', '0013_takeoutmenu_takeoutmeal_supermarketmenu_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurantmenu',
            old_name='food_service',
            new_name='restaurant',
        ),
    ]
