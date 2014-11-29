# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_comments', '0003_auto_20141129_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='is_public',
            field=models.BooleanField(default=True, help_text='Uncheck this box to make the comment effectively disappear from the site.', db_index=True, verbose_name='is public'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='is_removed',
            field=models.BooleanField(default=False, help_text='Check this box if the comment is inappropriate. A "This comment has been removed" message will be displayed instead.', db_index=True, verbose_name='is removed'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='submit_date',
            field=models.DateTimeField(default=None, verbose_name='date/time submitted', db_index=True),
            preserve_default=True,
        ),
    ]
