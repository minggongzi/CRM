# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-09 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('url_type', models.SmallIntegerField(choices=[(0, 'absolute'), (1, 'dynamic')], default=0)),
                ('url_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.ManyToManyField(blank=True, to='crm.Role'),
        ),
        migrations.AlterUniqueTogether(
            name='menus',
            unique_together=set([('name', 'url_name')]),
        ),
        migrations.AddField(
            model_name='role',
            name='menus',
            field=models.ManyToManyField(blank=True, to='crm.Menus'),
        ),
    ]
