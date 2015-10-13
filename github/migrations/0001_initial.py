# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=64)),
                ('reponame', models.CharField(max_length=64)),
                ('stars', models.IntegerField(default=0)),
                ('watchers', models.IntegerField(default=0)),
                ('forks', models.IntegerField(default=0)),
            ],
        ),
    ]
