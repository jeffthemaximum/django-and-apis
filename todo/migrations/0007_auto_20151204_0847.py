# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_auto_20151203_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='shared_user',
            field=models.ManyToManyField(related_name='shared_users', null=True, to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
