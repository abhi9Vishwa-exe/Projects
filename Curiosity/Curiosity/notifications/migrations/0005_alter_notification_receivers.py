# Generated by Django 4.0.3 on 2022-03-19 07:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notifications', '0004_remove_notification_contenta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='receivers',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
