# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-07 11:28
from __future__ import unicode_literals

from django.db import migrations, models
import storage.models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0002_item_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='item_icon',
        ),
        migrations.AddField(
            model_name='item',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=storage.models.upload_image_location, width_field='width_field'),
        ),
        migrations.AddField(
            model_name='item',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
    ]