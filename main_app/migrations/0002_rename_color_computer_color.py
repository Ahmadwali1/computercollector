# Generated by Django 4.2.7 on 2023-12-02 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='computer',
            old_name='Color',
            new_name='color',
        ),
    ]
