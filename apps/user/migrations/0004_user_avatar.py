# Generated by Django 4.0.2 on 2022-03-03 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0001_initial'),
        ('user', '0003_verifyemail'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='avatars', to='file.file'),
        ),
    ]
