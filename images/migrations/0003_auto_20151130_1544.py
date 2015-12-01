# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_image_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='author',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='image',
            name='file_name',
        ),
        migrations.AlterField(
            model_name='image',
            name='token',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
