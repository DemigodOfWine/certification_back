# Generated by Django 3.2.4 on 2021-09-29 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cap_server', '0014_alter_settings1560_accumulation'),
    ]

    operations = [
        migrations.AddField(
            model_name='operators',
            name='verification_level',
            field=models.IntegerField(blank=True, choices=[(0, 'Первичный контроль'), (1, 'Контроль качества')], default=None, null=True, verbose_name='Этап контроля'),
        ),
    ]
