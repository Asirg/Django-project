# Generated by Django 5.1.6 on 2025-02-18 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='descripion',
            new_name='description',
        ),
    ]
