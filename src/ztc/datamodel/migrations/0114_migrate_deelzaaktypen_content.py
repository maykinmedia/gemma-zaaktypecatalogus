# Generated by Django 2.2.4 on 2019-10-28 14:38

from django.db import migrations


def forwards(apps, _):
    ZaakType = apps.get_model("datamodel.ZaakType")

    for zaaktype in ZaakType.objects.prefetch_related("is_deelzaaktype_van"):
        for hoofdzaaktype in zaaktype.is_deelzaaktype_van.all():
            hoofdzaaktype.deelzaaktypen.add(zaaktype)


def backwards(apps, _):
    ZaakType = apps.get_model("datamodel.ZaakType")

    for zaaktype in ZaakType.objects.prefetch_related("deelzaaktypen"):
        for deelzaaktype in zaaktype.deelzaaktypen.all():
            deelzaaktype.is_deelzaaktype_van.add(zaaktype)


class Migration(migrations.Migration):

    dependencies = [("datamodel", "0113_zaaktype_deelzaaktypen")]

    operations = [migrations.RunPython(forwards, backwards)]