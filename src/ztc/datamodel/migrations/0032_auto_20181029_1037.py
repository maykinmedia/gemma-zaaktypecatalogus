# Generated by Django 2.0.8 on 2018-10-29 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamodel', '0031_auto_20180911_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='besluittype',
            name='publicatietekst',
            field=models.TextField(blank=True, help_text='De generieke tekst van de publicatie van BESLUITen van dit BESLUITTYPE', verbose_name='publicatietekst'),
        ),
        migrations.AlterField(
            model_name='besluittype',
            name='toelichting',
            field=models.TextField(blank=True, help_text='Een eventuele toelichting op dit BESLUITTYPE.', verbose_name='toelichting'),
        ),
    ]
