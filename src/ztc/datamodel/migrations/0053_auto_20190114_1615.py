# Generated by Django 2.0.9 on 2019-01-14 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("datamodel", "0052_auto_20190114_1614")]

    operations = [
        migrations.RenameField(
            model_name="zaaktype", old_name="trefwoord", new_name="trefwoorden"
        )
    ]
