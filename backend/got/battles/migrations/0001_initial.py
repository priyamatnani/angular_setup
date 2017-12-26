# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-23 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BattleSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='', max_length=200)),
                ('year', models.IntegerField(null=True)),
                ('battle_number', models.IntegerField()),
                ('attacker_king', models.TextField(default='', max_length=200)),
                ('defender_king', models.TextField(default='', max_length=200)),
                ('attacker_1', models.TextField(default='', max_length=200, null=True)),
                ('attacker_2', models.TextField(default='', max_length=200, null=True)),
                ('attacker_3', models.TextField(default='', max_length=200, null=True)),
                ('attacker_4', models.TextField(default='', max_length=200, null=True)),
                ('defender_1', models.TextField(default='', max_length=200, null=True)),
                ('defender_2', models.TextField(default='', max_length=200, null=True)),
                ('defender_3', models.TextField(default='', max_length=200, null=True)),
                ('defender_4', models.TextField(default='', max_length=200, null=True)),
                ('attacker_outcome', models.TextField(max_length=20)),
                ('battle_type', models.TextField(max_length=20)),
                ('major_death', models.BooleanField()),
                ('major_capture', models.BooleanField()),
                ('attacker_size', models.IntegerField()),
                ('defender_size', models.IntegerField()),
                ('attacker_commander', models.TextField(default='', max_length=200, null=True)),
                ('defender_commander', models.TextField(default='', max_length=200, null=True)),
                ('summer', models.BooleanField()),
                ('location', models.TextField(default='', max_length=200)),
                ('region', models.TextField(default='', max_length=200)),
                ('note', models.TextField(default='', max_length=5000, null=True)),
            ],
        ),
    ]