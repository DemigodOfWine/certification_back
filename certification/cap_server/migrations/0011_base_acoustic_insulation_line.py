# Generated by Django 3.2.4 on 2021-09-09 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cap_server', '0010_auto_20210909_0831'),
    ]

    operations = [
        migrations.AddField(
            model_name='base',
            name='acoustic_insulation_line',
            field=models.PositiveIntegerField(default=None, null=True, verbose_name='Канал акустической изоляции'),
        ),
    ]