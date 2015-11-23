# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ip', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ip',
            old_name='location',
            new_name='city',
        ),
        migrations.AddField(
            model_name='ip',
            name='country',
            field=models.CharField(default='USA', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ip',
            name='isp_provider',
            field=models.CharField(default='TWC', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ip',
            name='organization',
            field=models.CharField(default='IAL', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ip',
            name='provider_details',
            field=models.CharField(default='Time warner cable', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ip',
            name='state',
            field=models.CharField(default='NY', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ip',
            name='zip',
            field=models.CharField(default='10025', max_length=100),
            preserve_default=False,
        ),
    ]
