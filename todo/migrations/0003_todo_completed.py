# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_shared_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
