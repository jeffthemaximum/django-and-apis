# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ip', '0002_auto_20151123_1103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ip',
            name='provider_details',
        ),
    ]
