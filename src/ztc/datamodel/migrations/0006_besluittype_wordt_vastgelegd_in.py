# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamodel', '0005_auto_20171129_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='besluittype',
            name='wordt_vastgelegd_in',
            field=models.ManyToManyField(blank=True, help_text='Het INFORMATIEOBJECTTYPE van informatieobjecten waarin besluiten van dit BESLUITTYPE worden vastgelegd.', null=True, to='datamodel.InformatieObjectType'),
        ),
    ]
