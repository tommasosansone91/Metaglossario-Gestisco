# Generated by Django 2.2.2 on 2019-11-13 17:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_metaglossario', '0014_auto_20191112_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acquired_terminology',
            name='Data_inserimento_entry',
            field=models.DateField(default=datetime.date(2019, 11, 13)),
        ),
        migrations.AlterField(
            model_name='glossary_entry',
            name='Data_inserimento_entry',
            field=models.DateField(default=datetime.date(2019, 11, 13)),
        ),
        migrations.AlterField(
            model_name='glossary_file',
            name='Data_inserimento_glossary',
            field=models.DateField(default=datetime.date(2019, 11, 13)),
        ),
        migrations.AlterField(
            model_name='prepared_terminology',
            name='Data_inserimento_entry',
            field=models.DateField(default=datetime.date(2019, 11, 13)),
        ),
    ]