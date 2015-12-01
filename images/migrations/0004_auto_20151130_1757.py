# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_auto_20151130_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.FileField(upload_to=b'documents/%Y/%m/%d'),
        ),
    ]
