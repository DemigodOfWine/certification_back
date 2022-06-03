# Generated by Django 3.2.4 on 2021-06-30 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cap_server', '0003_rename_date_certification_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certification',
            name='assembled',
            field=models.BooleanField(choices=[(True, 'Да'), (False, 'Нет')], default=True, null=True, verbose_name='В сборке'),
        ),
    ]
