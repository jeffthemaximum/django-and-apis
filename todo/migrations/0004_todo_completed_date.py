# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_todo_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='completed_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
