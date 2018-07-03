# Generated by Django 2.0.5 on 2018-07-03 22:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GILTI', '0002_auto_20180624_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='US_Rate',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='client',
            name='exp_alloc',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='client',
            name='year_end',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
    ]
