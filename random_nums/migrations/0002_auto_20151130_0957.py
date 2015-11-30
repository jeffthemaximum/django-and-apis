# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('random_nums', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='random_num',
            name='count',
            field=models.IntegerField(default=1),
        ),
    ]
