# Generated by Django 4.2.6 on 2023-10-10 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('phone_number', models.CharField(max_length=255, verbose_name='Номер телефона')),
            ],
            options={
                'verbose_name': 'Работник',
                'verbose_name_plural': 'Работники',
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_check.employee', verbose_name='Сотрудник')),
            ],
            options={
                'verbose_name': 'Торговая точка',
                'verbose_name_plural': 'Торговые точки',
            },
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')),
                ('latitude', models.FloatField(verbose_name='Ширина')),
                ('longitude', models.FloatField(verbose_name='Долгота')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_check.store', verbose_name='Торговая точка')),
            ],
        ),
    ]
