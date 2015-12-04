# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20151201_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='shared_user',
            field=models.ManyToManyField(related_name='shared_users', null=True, to='friendship.Friend', blank=True),
        ),
    ]
