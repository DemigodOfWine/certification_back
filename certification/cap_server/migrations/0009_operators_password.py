# Generated by Django 3.2.4 on 2021-09-03 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cap_server', '0008_auto_20210901_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='operators',
            name='password',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]