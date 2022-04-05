# Generated by Django 4.0.2 on 2022-03-15 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_dining', '0002_bakery_city_bakery_country_foodservice_city_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bakery',
            name='food_type',
        ),
        migrations.RemoveField(
            model_name='bakery',
            name='service_options',
        ),
        migrations.RemoveField(
            model_name='foodservice',
            name='food_type',
        ),
        migrations.RemoveField(
            model_name='foodservice',
            name='service_options',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='food_type',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='service_options',
        ),
        migrations.RemoveField(
            model_name='supermarket',
            name='food_type',
        ),
        migrations.RemoveField(
            model_name='supermarket',
            name='service_options',
        ),
        migrations.RemoveField(
            model_name='takeout',
            name='food_type',
        ),
        migrations.RemoveField(
            model_name='takeout',
            name='service_options',
        ),
        migrations.AlterField(
            model_name='bakery',
            name='facebook_url',
            field=models.CharField(max_length=355, null=True),
        ),
        migrations.AlterField(
            model_name='bakery',
            name='instagram_url',
            field=models.CharField(max_length=355, null=True),
        ),
        migrations.AlterField(
            model_name='bakery',
            name='twitter_url',
            field=models.CharField(max_length=355, null=True),
        ),
        migrations.AlterField(
            model_name='foodservice',
            name='facebook_url',
            field=models.CharField(max_length=355, null=True),
        ),
        migrations.AlterField(
            model_name='foodservice',
            name='instagram_url',
            field=models.CharField(max_length=355, null=True),
        ),
        migrations.AlterField(
            model_name='foodservice',
            name='twitter_url',
            field=models.CharField(max_length=355, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='facebook_url',
            field=models.CharField(max_length=355, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='instagram_url',
            field=models.CharField(max_length=355, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='twitter_url',
            field=models.CharField(max_length=355, null=True),
        ),
        migrations.AlterField(
            model_name='supermarket',
            name='facebook_url',
            field=models.CharField(max_length=355, null=True),
        ),
        migrations.AlterField(
            model_name='supermarket',
            name='instagram_url',
            field=models.CharField(max_length=355, null=True),
        ),
        migrations.AlterField(
            model_name='supermarket',
            name='twitter_url',
            field=models.CharField(max_length=355, null=True),
        ),
        migrations.AlterField(
            model_name='takeout',
            name='facebook_url',
            field=models.CharField(max_length=355, null=True),
        ),
        migrations.AlterField(
            model_name='takeout',
            name='instagram_url',
            field=models.CharField(max_length=355, null=True),
        ),
        migrations.AlterField(
            model_name='takeout',
            name='twitter_url',
            field=models.CharField(max_length=355, null=True),
        ),
    ]