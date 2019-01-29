# Generated by Django 2.0.9 on 2019-01-08 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamodel', '0042_auto_20190108_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zaaktype',
            name='onderwerp',
            field=models.CharField(help_text="Het onderwerp van ZAAKen van dit ZAAKTYPE. In veel gevallen nauw gerelateerd aan de product- of dienstnaam uit de Producten- en Dienstencatalogus (PDC). Bijvoorbeeld: 'Evenementenvergunning', 'Geboorte', 'Klacht'. Zie ook het IOB model op https://www.gemmaonline.nl/index.php/Imztc_2.1/doc/attribuutsoort/zaaktype.onderwerp", max_length=80, verbose_name='onderwerp'),
        ),
    ]