# Generated by Django 4.0 on 2021-12-21 08:20

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('banks', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 21, 8, 19, 53, 156096, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='account',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='created_accounts', to='users.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 21, 8, 19, 53, 156104, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='account',
            name='modified_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='modified_accounts', to='users.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bank',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 21, 8, 19, 53, 155431, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='bank',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='created_banks', to='users.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bank',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 21, 8, 19, 53, 155450, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='bank',
            name='modified_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='modified_banks', to='users.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='branch',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 21, 8, 19, 53, 155794, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='branch',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='created_branches', to='users.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='branch',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 21, 8, 19, 53, 155804, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='branch',
            name='modified_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='modified_branches', to='users.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='created_transactions', to='users.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 21, 8, 19, 53, 156445, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='transaction',
            name='modified_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='modified_transactions', to='users.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Accounts', to='banks.branch'),
        ),
        migrations.AlterField(
            model_name='account',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Accounts', to='users.user'),
        ),
        migrations.AlterField(
            model_name='branch',
            name='bank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='banks.bank'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 21, 8, 19, 53, 156425, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='users.user'),
        ),
    ]