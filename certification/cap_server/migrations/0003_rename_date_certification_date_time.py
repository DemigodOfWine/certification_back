# Generated by Django 3.2.4 on 2021-06-30 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cap_server', '0002_certification_assembled'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certification',
            old_name='date',
            new_name='date_time',
        ),
    ]
