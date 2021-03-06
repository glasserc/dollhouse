# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessory',
            name='accessory_lpos',
            field=models.CharField(max_length=10, default='100px'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='accessory',
            name='accessory_tops',
            field=models.CharField(max_length=10, default='100px'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doll',
            name='doll_lpos',
            field=models.CharField(max_length=10, default='100px'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doll',
            name='doll_tpos',
            field=models.CharField(max_length=10, default='100px'),
            preserve_default=False,
        ),
    ]
