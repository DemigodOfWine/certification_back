# Generated by Django 3.2.8 on 2021-11-26 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tomography_ann', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aaadata',
            options={'verbose_name': 'Сырой сигнал', 'verbose_name_plural': 'Сырой сигнал'},
        ),
        migrations.AddField(
            model_name='aaadata',
            name='data',
            field=models.JSONField(null=True),
        ),
    ]
