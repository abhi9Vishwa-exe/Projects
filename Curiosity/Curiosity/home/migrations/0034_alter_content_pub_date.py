# Generated by Django 3.2.6 on 2022-04-03 09:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_alter_content_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 3, 15, 0, 29, 513518), verbose_name='date published'),
        ),
    ]
