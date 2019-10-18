# Generated by Django 2.2.2 on 2019-09-27 10:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='glossary_entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lemma_it', models.CharField(blank=True, max_length=256, null=True)),
                ('Lemma_ch', models.CharField(blank=True, max_length=256, null=True)),
                ('Acronimo_it', models.CharField(blank=True, max_length=25, null=True)),
                ('Acronimo_ch', models.CharField(blank=True, max_length=25, null=True)),
                ('Definizione_it', models.TextField(blank=True, null=True)),
                ('Definizione_ch', models.TextField(blank=True, null=True)),
                ('Ambito_riferimento_it', models.CharField(blank=True, max_length=256, null=True)),
                ('Ambito_riferimento_ch', models.CharField(blank=True, max_length=256, null=True)),
                ('Autore_definizione_it', models.CharField(blank=True, max_length=256, null=True)),
                ('Autore_definizione_ch', models.CharField(blank=True, max_length=256, null=True)),
                ('Posizione_definizione_it', models.CharField(blank=True, max_length=256, null=True)),
                ('Posizione_definizione_ch', models.CharField(blank=True, max_length=256, null=True)),
                ('Url_definizione_it', models.URLField(blank=True, max_length=400, null=True)),
                ('Url_definizione_ch', models.URLField(blank=True, max_length=400, null=True)),
                ('Titolo_documento_fonte_it', models.CharField(blank=True, max_length=256, null=True)),
                ('Titolo_documento_fonte_ch', models.CharField(blank=True, max_length=256, null=True)),
                ('Autore_documento_fonte_it', models.CharField(blank=True, max_length=256, null=True)),
                ('Autore_documento_fonte_ch', models.CharField(blank=True, max_length=256, null=True)),
                ('Host_documento_fonte_it', models.CharField(blank=True, max_length=256, null=True)),
                ('Host_documento_fonte_ch', models.CharField(blank=True, max_length=256, null=True)),
                ('Url_documento_fonte_it', models.URLField(blank=True, max_length=400, null=True)),
                ('Url_documento_fonte_ch', models.URLField(blank=True, max_length=400, null=True)),
                ('Data_inserimento_entry', models.DateField(default=datetime.date(2019, 9, 27))),
                ('Id_statico_entry', models.CharField(default='ITCH00000', max_length=256)),
                ('Admin_approval_switch', models.CharField(choices=[('show', 'show'), ('hide', 'hide')], default=('hide', 'hide'), max_length=30)),
            ],
            options={
                'ordering': ['Admin_approval_switch', 'Lemma_it', 'Lemma_ch', 'Id_statico_entry'],
            },
        ),
    ]