# Generated by Django 4.0.2 on 2022-03-18 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_dining', '0014_rename_food_service_restaurantmenu_restaurant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantmeal',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='food_dining.restaurantmenu'),
        ),
    ]
