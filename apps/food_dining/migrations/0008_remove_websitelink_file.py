# Generated by Django 4.0.2 on 2022-03-16 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_dining', '0007_alter_bakery_latitude_alter_bakery_longitude_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='websitelink',
            name='file',
        ),
    ]