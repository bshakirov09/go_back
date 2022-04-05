# Generated by Django 4.0.2 on 2022-03-17 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('explore', '0003_tag_explore_is_main_explore_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='explore',
            name='is_main',
        ),
        migrations.RemoveField(
            model_name='explore',
            name='tag',
        ),
        migrations.CreateModel(
            name='ExploreTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('modified_datetime', models.DateTimeField(auto_now=True)),
                ('explore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='explore.explore')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='explore.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
