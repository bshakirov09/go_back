# Generated by Django 4.0.2 on 2022-03-18 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_dining', '0014_rename_food_service_restaurantmenu_restaurant'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supermarketmenu',
            old_name='food_service',
            new_name='supermarket',
        ),
        migrations.RenameField(
            model_name='takeoutmenu',
            old_name='food_service',
            new_name='take_out',
        ),
    ]