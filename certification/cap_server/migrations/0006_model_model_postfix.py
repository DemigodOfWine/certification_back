# Generated by Django 3.2.4 on 2021-08-23 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cap_server', '0005_alter_settings1560_filter_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='model',
            name='model_postfix',
            field=models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name='Постфикс'),
        ),
    ]