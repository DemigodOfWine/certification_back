# Generated by Django 3.2.4 on 2021-09-01 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cap_server', '0007_operators_courses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operators',
            name='courses',
        ),
        migrations.AddField(
            model_name='operators',
            name='controlers_of_operator',
            field=models.ManyToManyField(to='cap_server.Controllers', verbose_name='Контролеры'),
        ),
    ]
