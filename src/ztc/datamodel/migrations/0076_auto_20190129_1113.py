# Generated by Django 2.0.9 on 2019-01-29 10:13

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("datamodel", "0075_auto_20190129_1103")]

    operations = [
        migrations.AlterField(
            model_name="zaaktype",
            name="producten_of_diensten",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.URLField(
                    max_length=1000, verbose_name="URL naar product/dienst"
                ),
                help_text="Het product of de dienst die door ZAAKen van dit ZAAKTYPE wordt voortgebracht.",
                size=None,
            ),
        )
    ]
