# Generated by Django 3.1.1 on 2020-09-11 06:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20200911_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 11, 6, 23, 0, 295967, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 11, 6, 23, 0, 294970, tzinfo=utc)),
        ),
    ]
