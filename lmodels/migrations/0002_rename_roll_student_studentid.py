# Generated by Django 5.0.4 on 2024-05-14 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lmodels', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='roll',
            new_name='studentid',
        ),
    ]
