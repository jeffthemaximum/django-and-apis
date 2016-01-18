# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urls', '0004_auto_20160102_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='hits',
            field=models.IntegerField(default=0),
        ),
    ]
