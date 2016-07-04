# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('level', models.IntegerField(default=1)),
                ('adjustment_level', models.IntegerField(default=1)),
                ('mythic_tier', models.IntegerField(default=0)),
                ('description', models.TextField()),
                ('dm_notes', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
