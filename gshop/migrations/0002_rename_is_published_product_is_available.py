# Generated by Django 4.0.4 on 2022-05-27 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gshop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='is_published',
            new_name='is_available',
        ),
    ]
