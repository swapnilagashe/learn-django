# Generated by Django 5.0.2 on 2024-04-16 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0002_rename_name_menu_item_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='rating',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]
