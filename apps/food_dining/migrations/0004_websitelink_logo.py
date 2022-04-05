# Generated by Django 4.0.2 on 2022-03-15 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0002_file_is_main_file_ordering'),
        ('food_dining', '0003_remove_bakery_food_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='websitelink',
            name='logo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='file.file'),
            preserve_default=False,
        ),
    ]
