# Generated by Django 4.0.5 on 2022-07-01 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserDetail',
            new_name='User',
        ),
    ]
