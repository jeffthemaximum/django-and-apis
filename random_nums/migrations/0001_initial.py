# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Random_Num',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField()),
                ('count', models.IntegerField(default=0)),
                ('total_count', models.IntegerField(default=0)),
                ('frequency', models.DecimalField(max_digits=11, decimal_places=10)),
            ],
        ),
    ]
