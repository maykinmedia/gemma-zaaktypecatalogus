# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-06-18 08:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("datamodel", "0010_auto_20180618_1042")]

    operations = [
        migrations.AlterField(
            model_name="statustype",
            name="is_van",
            field=models.ForeignKey(
                help_text="Het ZAAKTYPE van ZAAKen waarin STATUSsen van dit STATUSTYPE bereikt kunnen worden.",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="statustypen",
                to="datamodel.ZaakType",
                verbose_name="is van",
            ),
        )
    ]
