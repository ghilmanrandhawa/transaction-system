# Generated by Django 4.0 on 2021-12-21 07:04

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('number', models.IntegerField()),
                ('balance', models.DecimalField(decimal_places=2, max_digits=22)),
            ],
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=22)),
                ('created', models.DateTimeField(default=datetime.datetime(2021, 12, 21, 7, 4, 6, 138717, tzinfo=utc))),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banks.account')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banks.branch')),
            ],
        ),
    ]
