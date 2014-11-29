# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_comments', '0002_auto_20141129_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='object_pk',
            field=models.TextField(verbose_name='object ID', db_index=True),
            preserve_default=True,
        ),
    ]
