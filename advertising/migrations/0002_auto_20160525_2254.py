# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-25 22:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('advertising', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertising',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='advertising',
            name='url',
        ),
        migrations.AddField(
            model_name='imageadvertising',
            name='title',
            field=models.CharField(default=datetime.datetime(2016, 5, 25, 22, 54, 19, 37213, tzinfo=utc), max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='imageadvertising',
            name='url',
            field=models.URLField(default=datetime.datetime(2016, 5, 25, 22, 54, 24, 25020, tzinfo=utc), max_length=450),
            preserve_default=False,
        ),
    ]
