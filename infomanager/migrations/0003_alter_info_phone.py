# Generated by Django 3.2.3 on 2021-05-29 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infomanager', '0002_alter_info_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='phone',
            field=models.IntegerField(max_length=11, unique=True),
        ),
    ]
