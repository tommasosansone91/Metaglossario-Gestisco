# Generated by Django 2.2.2 on 2020-02-07 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_metaglossario', '0051_auto_20200205_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acquired_terminology',
            name='Id_statico_entry',
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='prepared_terminology',
            name='Id_statico_entry',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]
