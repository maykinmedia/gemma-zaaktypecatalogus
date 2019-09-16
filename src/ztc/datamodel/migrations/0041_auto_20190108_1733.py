# Generated by Django 2.0.9 on 2019-01-08 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("datamodel", "0040_auto_20190108_1723")]

    operations = [
        migrations.AlterField(
            model_name="zaaktype",
            name="indicatie_intern_of_extern",
            field=models.CharField(
                choices=[("Intern", "intern"), ("Extern", "extern")],
                help_text="Een aanduiding waarmee onderscheid wordt gemaakt tussen ZAAKTYPEn die Intern respectievelijk Extern geïnitieerd worden. Indien van beide sprake kan zijn, dan prevaleert de externe initiatie.",
                max_length=6,
                verbose_name="indicatie intern of extern",
            ),
        )
    ]
