# Generated by Django 2.0.10 on 2019-02-26 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datamodel', '0088_resultaattype_brondatum_archiefprocedure_procestermijn'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resultaattype',
            old_name='omschrijving_generiek',
            new_name='resultaattypeomschrijving',
        ),
    ]