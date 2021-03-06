# Generated by Django 2.2.2 on 2020-02-05 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_metaglossario', '0049_auto_20200205_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acquired_terminology',
            name='Acronimo_ch',
            field=models.CharField(blank=True, default=None, max_length=25),
        ),
        migrations.AlterField(
            model_name='acquired_terminology',
            name='Acronimo_it',
            field=models.CharField(blank=True, default=None, max_length=25),
        ),
        migrations.AlterField(
            model_name='acquired_terminology',
            name='Ambito_riferimento_ch',
            field=models.CharField(blank=True, default=None, max_length=256),
        ),
        migrations.AlterField(
            model_name='acquired_terminology',
            name='Ambito_riferimento_it',
            field=models.CharField(blank=True, default=None, max_length=256),
        ),
        migrations.AlterField(
            model_name='acquired_terminology',
            name='Autore_definizione_ch',
            field=models.TextField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='acquired_terminology',
            name='Autore_definizione_it',
            field=models.TextField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='acquired_terminology',
            name='Autore_documento_fonte_ch',
            field=models.TextField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='acquired_terminology',
            name='Autore_documento_fonte_it',
            field=models.TextField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='acquired_terminology',
            name='Commento_entry',
            field=models.TextField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='acquired_terminology',
            name='Definizione_ch',
            field=models.TextField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='acquired_terminology',
            name='Definizione_it',
            field=models.TextField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='acquired_terminology',
            name='Host_documento_fonte_ch',
            field=models.TextField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='acquired_terminology',
            name='Host_documento_fonte_it',
            field=models.TextField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='acquired_terminology',
            name='Lemma_ch',
            field=models.CharField(blank=True, default=None, max_length=256),
        ),
        migrations.AlterField(
            model_name='acquired_terminology',
            name='Lemma_it',
            field=models.CharField(blank=True, default=None, max_length=256),
        ),
        migrations.AlterField(
            model_name='acquired_terminology',
            name='Posizione_definizione_ch',
            field=models.TextField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='acquired_terminology',
            name='Posizione_definizione_it',
            field=models.TextField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='acquired_terminology',
            name='Titolo_documento_fonte_ch',
            field=models.TextField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='acquired_terminology',
            name='Titolo_documento_fonte_it',
            field=models.TextField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='acquired_terminology',
            name='Url_definizione_ch',
            field=models.URLField(blank=True, default=None, max_length=400),
        ),
        migrations.AlterField(
            model_name='acquired_terminology',
            name='Url_definizione_it',
            field=models.URLField(blank=True, default=None, max_length=400),
        ),
        migrations.AlterField(
            model_name='acquired_terminology',
            name='Url_documento_fonte_ch',
            field=models.URLField(blank=True, default=None, max_length=400),
        ),
        migrations.AlterField(
            model_name='acquired_terminology',
            name='Url_documento_fonte_it',
            field=models.URLField(blank=True, default=None, max_length=400),
        ),
    ]
