# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-05 11:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='\u6807\u9898')),
                ('content', models.TextField(verbose_name='\u6b63\u6587')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('last_modified_time', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('status', models.CharField(choices=[('d', 'Draft'), ('p', 'Published')], max_length=1, verbose_name='\u6587\u7ae0\u72b6\u6001')),
                ('abstract', models.CharField(blank=True, help_text='\u53ef\u9009\uff0c\u5982\u82e5\u4e3a\u7a7a\u5c06\u6458\u9009\u6b63\u6587\u524d60\u4e2a\u5b57\u7b26', max_length=60, null=True, verbose_name='\u6458\u8981')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='\u6d4f\u89c8\u91cf')),
                ('likes', models.PositiveIntegerField(default=0, verbose_name='\u70b9\u8d5e\u6570')),
                ('topped', models.BooleanField(default=False, verbose_name='\u7f6e\u9876')),
            ],
            options={
                'ordering': ['-last_modified_time'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='\u7c7b\u540d')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('last_modified_time', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Category', verbose_name='\u5206\u7c7b'),
        ),
    ]
