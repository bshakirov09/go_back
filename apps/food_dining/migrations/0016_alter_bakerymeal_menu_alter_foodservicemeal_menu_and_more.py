# Generated by Django 4.0.2 on 2022-03-28 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_dining', '0015_rename_food_service_supermarketmenu_supermarket_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bakerymeal',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_dining.bakerymenu'),
        ),
        migrations.AlterField(
            model_name='foodservicemeal',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_dining.foodservicemenu'),
        ),
        migrations.AlterField(
            model_name='restaurantmeal',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_dining.restaurant'),
        ),
        migrations.AlterField(
            model_name='supermarketmeal',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_dining.supermarketmenu'),
        ),
        migrations.AlterField(
            model_name='takeoutmeal',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_dining.takeoutmenu'),
        ),
    ]
