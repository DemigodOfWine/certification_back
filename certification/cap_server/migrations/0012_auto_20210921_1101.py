# Generated by Django 3.2.4 on 2021-09-21 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cap_server', '0011_base_acoustic_insulation_line'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings1560',
            name='tvg_K3',
            field=models.BooleanField(choices=[(True, 'on'), (False, 'off')], default=False, verbose_name='3 каскад'),
        ),
        migrations.AddField(
            model_name='settings1560',
            name='tvg_atten',
            field=models.BooleanField(choices=[(True, 'on'), (False, 'off')], default=False, verbose_name='Аттенюатор'),
        ),
    ]