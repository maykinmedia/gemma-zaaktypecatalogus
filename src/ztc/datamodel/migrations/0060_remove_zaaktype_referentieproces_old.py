# Generated by Django 2.0.9 on 2019-01-15 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("datamodel", "0059_migrate_referentieproces_data")]

    operations = [
        migrations.RemoveField(model_name="zaaktype", name="referentieproces_old")
    ]
