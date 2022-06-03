# Generated by Django 3.2.4 on 2021-06-29 15:33

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('echo_pulse_delay', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=10, null=True, verbose_name='Задержка сигнала, мкс')),
                ('capacity', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=10, null=True, verbose_name='Емкость, пФ')),
                ('afc_maximum_s_rel', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=10, null=True, verbose_name='Коэффициент двойного преобразования (не менее), дБ')),
                ('echo_pulse_duration', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=10, null=True, verbose_name='Длительность сигнала, мкс')),
                ('afc_frequency_maximum', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=10, null=True, verbose_name='Частота максимума АЧХ, кГц')),
                ('lower_afc_frequency', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=10, null=True, verbose_name='Нижняя граничная частота АЧХ, кГц')),
                ('upper_afc_frequency', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=10, null=True, verbose_name='Верхняя граничная частота АЧХ, кГц')),
                ('operating_frequency', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=10, null=True, verbose_name='Рабочая частота, кГц')),
                ('relative_transmission_bandwidth', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=10, null=True, verbose_name='Относительная полоса АЧХ, %')),
                ('afc_maximum_s_rel_first_half_wave', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=10, null=True, verbose_name='Коэффициент двойного преобразования по первой полуволне (не менее), дБ')),
                ('leading_front_duration', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=10, null=True, verbose_name='Длительность фронта первой полуволны, мкс')),
                ('first_half_wave_duration', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=10, null=True, verbose_name='Длительность первой полуволны, мкс')),
                ('afc_frequency_maximum_first_wave', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=10, null=True, verbose_name='Частота максимума АЧХ по первому периоду, кГц')),
                ('date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата внесения записи')),
                ('last_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Последние изменение')),
                ('comment', models.TextField(blank=True, max_length=500, null=True, verbose_name='Комментарий')),
                ('special_properties', models.CharField(blank=True, max_length=200, null=True, verbose_name='Особые свойства')),
                ('apyas', models.CharField(default=None, max_length=16, null=True, verbose_name='АПЯС')),
                ('control_line', models.PositiveIntegerField(default=None, null=True, verbose_name='Канал контроля')),
                ('maximum_excitation_pulse_voltage', models.DecimalField(decimal_places=1, default=None, max_digits=5, null=True, verbose_name='Максимальная амплитуда возбуждения, В')),
                ('wave_type', models.CharField(choices=[('sh', 'Поперечные'), ('l', 'Продольные')], max_length=2, null=True, verbose_name='Основной тип возбуждаемых волн')),
                ('damper', models.BooleanField(choices=[(True, 'Есть'), (False, 'Нет')], default=False, null=True, verbose_name='Демпфер')),
                ('phase', models.BooleanField(choices=[(True, 'Положительная'), (False, 'Отрицательная')], default=False, null=True, verbose_name='Первая полуволна')),
                ('height', models.DecimalField(decimal_places=2, default=None, max_digits=4, null=True, verbose_name='Высота, мм')),
                ('diameter', models.DecimalField(decimal_places=2, default=None, max_digits=4, null=True, verbose_name='Диаметр, мм')),
                ('weight', models.DecimalField(decimal_places=2, default=None, max_digits=4, null=True, verbose_name='Масса, г')),
                ('connector', models.CharField(default=None, max_length=16, null=True, verbose_name='Тип разъема')),
                ('temp_down', models.DecimalField(decimal_places=2, default=None, max_digits=4, null=True, verbose_name='Нижний диапазон рабочей температуры, С')),
                ('temp_up', models.DecimalField(decimal_places=2, default=None, max_digits=4, null=True, verbose_name='Верхний диапазон рабочей температуры, С')),
            ],
            options={
                'verbose_name': 'Базовые характеристики',
                'verbose_name_plural': 'Базовые характеристики',
                'db_table': 'dpc_base',
            },
            managers=[
                ('manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=10, unique=True, verbose_name='Модель')),
                ('photo', models.ImageField(null=True, upload_to='dpc/img/')),
                ('form_certificate', models.IntegerField(choices=[(1, 'Демпфированные'), (2, 'Не демпфированные')], null=True, verbose_name='Форма паспорта')),
                ('intended_use_rus', models.TextField(blank=True, default=None, max_length=500, null=True, verbose_name='Назначение')),
                ('intended_use_eng', models.TextField(blank=True, default=None, max_length=500, null=True, verbose_name='Назначение')),
                ('application', models.TextField(blank=True, default=None, max_length=500, null=True, verbose_name='Применение')),
                ('status', models.CharField(choices=[('С', 'Капсула'), ('S', 'Преобразователь')], max_length=2, null=True, verbose_name='Вид изделия')),
                ('model_b', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cap_server.model', verbose_name='Базовая капсула')),
            ],
            options={
                'verbose_name': 'Модели преобразователей',
                'verbose_name_plural': 'Модели преобразователей',
                'db_table': 'dpc_model',
            },
            managers=[
                ('manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Settings1560',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_signal', models.DecimalField(decimal_places=1, default=None, max_digits=5, verbose_name='Начало сигнала, мкс')),
                ('end_signal', models.DecimalField(decimal_places=1, default=None, max_digits=5, verbose_name='Конец сигнала, мкс')),
                ('end_draw_signal', models.DecimalField(decimal_places=1, default=None, max_digits=5, verbose_name='Конец отрисовки сигнала, мкс')),
                ('gain_raw', models.CharField(choices=[('0 0 0', '0/0/0'), ('0 0 1', '0/0/1'), ('0 1 0', '0/1/0'), ('1 0 0', '1/0/0'), ('0 1 1', '0/1/1'), ('1 0 1', '1/0/1'), ('1 1 0', '1/1/0'), ('1 1 1', '1/1/1')], max_length=6, verbose_name='GAIN RAW(аттенюатора/3 каскад/2 каскад)')),
                ('tvg_mod', models.CharField(choices=[('ON', 'ON'), ('BYPASS', 'BYPASS')], max_length=6, verbose_name='TVG MODE')),
                ('tvg_bypass', models.DecimalField(decimal_places=1, default=None, max_digits=5, verbose_name='Усиление, дБ')),
                ('source_sync', models.CharField(choices=[('CTP', 'CTP'), ('SENSOR', 'SENSOR'), ('INTERNAL', 'INTERNAL')], max_length=20, verbose_name='Источник синхронизации')),
                ('accumulation', models.PositiveIntegerField(verbose_name='Источник синхронизации')),
                ('filter_index', models.IntegerField(choices=[(0, '10 kHz'), (1, '20 kHz'), (2, '40 kHz'), (3, 'BYPASS')], default=None, verbose_name='Форма паспорта')),
                ('ascan_lenght', models.PositiveIntegerField(verbose_name='Длина вектора ASCAN')),
                ('constant_delay', models.PositiveIntegerField(verbose_name='Интервал постоянной задержки начала зондирования')),
                ('random_delay', models.PositiveIntegerField(verbose_name='Диапазон значений случайной задержки начала зондирования')),
                ('sampling_frequency', models.PositiveIntegerField(verbose_name='Частота квантования, МГц')),
                ('zonder_frequency', models.PositiveIntegerField(verbose_name='Частота зондера, Гц')),
                ('zonder_periods', models.DecimalField(decimal_places=1, default=None, max_digits=5, verbose_name='Число периодов зондера')),
                ('zonder_amplitude', models.IntegerField(choices=[(50, '50'), (100, '100'), (200, '200')], default=None, verbose_name='Амплитуда зондера, В')),
                ('zonder_enable', models.CharField(choices=[('ON', 'ON'), ('OFF', 'OFF')], max_length=3, verbose_name='ZONDER ENABLE')),
                ('zonder_reverse_polarity', models.CharField(choices=[('ON', 'ON'), ('OFF', 'OFF')], max_length=3, verbose_name='Реверсирование полярности')),
                ('zonder_mode', models.CharField(choices=[('COMBINED', 'COMBINED'), ('SPLIT', 'SPLIT')], max_length=10, verbose_name='ZONDER_MODE')),
                ('damp_duration', models.PositiveIntegerField(verbose_name='Интервал дампирования')),
                ('emu_data', models.IntegerField(choices=[(0, 'OFF'), (1, 'ON')], default=None, verbose_name='Эмуляция данных')),
                ('echo_pulse_delay_receiver', models.DecimalField(decimal_places=2, default=None, max_digits=4, null=True, verbose_name='Задержка приемного тракта, мкс')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cap_server.model', verbose_name='Модель')),
            ],
            options={
                'verbose_name': 'Настройки А1560',
                'verbose_name_plural': 'Настройки А1560',
                'db_table': 'dpc_settings1560',
            },
        ),
        migrations.CreateModel(
            name='Ranges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('echo_pulse_delay', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=10, null=True, verbose_name='Задержка сигнала, мкс')),
                ('capacity', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=10, null=True, verbose_name='Емкость, пФ')),
                ('afc_maximum_s_rel', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=10, null=True, verbose_name='Коэффициент двойного преобразования (не менее), дБ')),
                ('echo_pulse_duration', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=10, null=True, verbose_name='Длительность сигнала, мкс')),
                ('afc_frequency_maximum', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=10, null=True, verbose_name='Частота максимума АЧХ, кГц')),
                ('lower_afc_frequency', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=10, null=True, verbose_name='Нижняя граничная частота АЧХ, кГц')),
                ('upper_afc_frequency', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=10, null=True, verbose_name='Верхняя граничная частота АЧХ, кГц')),
                ('operating_frequency', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=10, null=True, verbose_name='Рабочая частота, кГц')),
                ('relative_transmission_bandwidth', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=10, null=True, verbose_name='Относительная полоса АЧХ, %')),
                ('afc_maximum_s_rel_first_half_wave', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=10, null=True, verbose_name='Коэффициент двойного преобразования по первой полуволне (не менее), дБ')),
                ('leading_front_duration', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=10, null=True, verbose_name='Длительность фронта первой полуволны, мкс')),
                ('first_half_wave_duration', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=10, null=True, verbose_name='Длительность первой полуволны, мкс')),
                ('afc_frequency_maximum_first_wave', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=10, null=True, verbose_name='Частота максимума АЧХ по первому периоду, кГц')),
                ('date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата внесения записи')),
                ('last_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Последние изменение')),
                ('comment', models.TextField(blank=True, max_length=500, null=True, verbose_name='Комментарий')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cap_server.model', verbose_name='Модель')),
            ],
            options={
                'verbose_name': 'Допуски',
                'verbose_name_plural': 'Допуски',
                'db_table': 'dpc_ranges',
            },
            managers=[
                ('manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Operators',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_rus', models.CharField(blank=True, max_length=150, null=True)),
                ('name_eng', models.CharField(blank=True, max_length=150, null=True)),
                ('status', models.BooleanField(choices=[(True, 'Да'), (False, 'Нет')], default=None, verbose_name='Выходной контроль')),
                ('login', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Оператор',
                'verbose_name_plural': 'Операторы',
                'db_table': 'dpc_operators',
            },
            managers=[
                ('manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Controllers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_rus', models.CharField(blank=True, max_length=150, null=True)),
                ('name_eng', models.CharField(blank=True, max_length=150, null=True)),
                ('status', models.BooleanField(choices=[(True, 'Да'), (False, 'Нет')], default=None, verbose_name='Выходной контроль')),
                ('login', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Контролер',
                'verbose_name_plural': 'Контролеры',
                'db_table': 'dpc_controller',
            },
            managers=[
                ('manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('echo_pulse_delay', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=10, null=True, verbose_name='Задержка сигнала, мкс')),
                ('capacity', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=10, null=True, verbose_name='Емкость, пФ')),
                ('afc_maximum_s_rel', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=10, null=True, verbose_name='Коэффициент двойного преобразования (не менее), дБ')),
                ('echo_pulse_duration', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=10, null=True, verbose_name='Длительность сигнала, мкс')),
                ('afc_frequency_maximum', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=10, null=True, verbose_name='Частота максимума АЧХ, кГц')),
                ('lower_afc_frequency', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=10, null=True, verbose_name='Нижняя граничная частота АЧХ, кГц')),
                ('upper_afc_frequency', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=10, null=True, verbose_name='Верхняя граничная частота АЧХ, кГц')),
                ('operating_frequency', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=10, null=True, verbose_name='Рабочая частота, кГц')),
                ('relative_transmission_bandwidth', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=10, null=True, verbose_name='Относительная полоса АЧХ, %')),
                ('afc_maximum_s_rel_first_half_wave', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=10, null=True, verbose_name='Коэффициент двойного преобразования по первой полуволне (не менее), дБ')),
                ('leading_front_duration', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=10, null=True, verbose_name='Длительность фронта первой полуволны, мкс')),
                ('first_half_wave_duration', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=10, null=True, verbose_name='Длительность первой полуволны, мкс')),
                ('afc_frequency_maximum_first_wave', models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=10, null=True, verbose_name='Частота максимума АЧХ по первому периоду, кГц')),
                ('serial_number', models.CharField(max_length=16)),
                ('temp', models.DecimalField(decimal_places=2, default=None, max_digits=4, null=True, verbose_name='Температура, С')),
                ('humid', models.DecimalField(decimal_places=2, default=None, max_digits=4, null=True, verbose_name='Влажность, отн.')),
                ('verification_stage', models.IntegerField(choices=[(0, 'Первичная'), (1, 'Вторичная')], default=None, verbose_name='Этап контроля')),
                ('comment', models.TextField(blank=True, max_length=500, null=True, verbose_name='Комментарий')),
                ('date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата внесения записи')),
                ('result', models.BooleanField(choices=[(True, 'Да'), (False, 'Нет')], default=False, null=True, verbose_name='Результат')),
                ('ascan', django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=10, default=None, max_digits=15, null=True), default=None, size=None)),
                ('dmg', models.BooleanField(choices=[(True, 'Да'), (False, 'Нет')], default=False, null=True, verbose_name='Списание')),
                ('serial_number_b', models.CharField(blank=True, default=None, max_length=16, null=True, verbose_name='Базовый серийный номер')),
                ('phase_wave', models.BooleanField(choices=[(True, 'Да'), (False, 'Нет')], default=True, null=True, verbose_name='Фаза первой полуволны')),
                ('base', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='base', to='cap_server.base', verbose_name='Базовые х-ки')),
                ('controller', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='controller', to='cap_server.controllers', verbose_name='Контроллер')),
                ('model', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='model_certification', to='cap_server.model', verbose_name='Модель')),
                ('operator', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='operator', to='cap_server.operators', verbose_name='Оператор')),
                ('ranges', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ranges', to='cap_server.ranges', verbose_name='Допуски')),
                ('settings', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='settings', to='cap_server.settings1560', verbose_name='Настройки А1560')),
            ],
            options={
                'verbose_name': 'Результаты паспортизации',
                'verbose_name_plural': 'Результаты паспортизации',
                'db_table': 'dpc_certification',
            },
            managers=[
                ('manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='base',
            name='model',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='model_base', to='cap_server.model', verbose_name='Модель'),
        ),
    ]
