# Generated by Django 3.2.3 on 2021-06-02 11:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infomanager', '0005_alter_info_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
