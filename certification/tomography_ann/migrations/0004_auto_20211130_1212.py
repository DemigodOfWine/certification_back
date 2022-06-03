# Generated by Django 3.2.8 on 2021-11-30 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tomography_ann', '0003_auto_20211130_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aaadata',
            name='addload',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='aaadata',
            name='alimax',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='aaadata',
            name='alimin',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='aaadata',
            name='amaxC',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='aaadata',
            name='amaxD',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='aaadata',
            name='balance',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='aaadata',
            name='dydsize',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='aaadata',
            name='poroglvl',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='aaadata',
            name='stpY',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='aaadata',
            name='wa',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='aaadata',
            name='xm',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='aaadata',
            name='ym',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='aaadata',
            name='zm',
            field=models.IntegerField(null=True),
        ),
    ]