# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', blank=True, to='forums.Comment', null=True)),
                ('poster', models.ForeignKey(to='members.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('headline', models.CharField(max_length=256)),
                ('text', models.TextField()),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('forum', models.ForeignKey(to='forums.Forum')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='thread',
            field=models.ForeignKey(to='forums.Thread'),
        ),
    ]
