# Generated by Django 3.2.25 on 2024-07-13 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20240713_0438'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='Ingredient',
            new_name='ingredients',
        ),
    ]
