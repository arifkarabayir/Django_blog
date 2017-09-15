# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-12 20:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20170811_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcomment', models.TextField(default='')),
                ('subcomment_owner', models.CharField(max_length=30)),
                ('comment_date', models.DateTimeField(verbose_name='date commented')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='subcomment',
            name='parent_comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Comment'),
        ),
        migrations.AddField(
            model_name='subcomment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Post'),
        ),
    ]