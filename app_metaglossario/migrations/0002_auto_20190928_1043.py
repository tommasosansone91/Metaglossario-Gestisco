# Generated by Django 2.2.2 on 2019-09-28 08:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_metaglossario', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='glossary_entry',
            options={'ordering': ['Admin_approval_switch', 'Lemma', 'Id_statico_entry']},
        ),
        migrations.RenameField(
            model_name='glossary_entry',
            old_name='Acronimo_ch',
            new_name='Acronimo',
        ),
        migrations.RenameField(
            model_name='glossary_entry',
            old_name='Ambito_riferimento_ch',
            new_name='Ambito_riferimento',
        ),
        migrations.RenameField(
            model_name='glossary_entry',
            old_name='Ambito_riferimento_it',
            new_name='Autore_definizione',
        ),
        migrations.RenameField(
            model_name='glossary_entry',
            old_name='Autore_definizione_ch',
            new_name='Autore_documento_fonte',
        ),
        migrations.RenameField(
            model_name='glossary_entry',
            old_name='Definizione_ch',
            new_name='Definizione',
        ),
        migrations.RenameField(
            model_name='glossary_entry',
            old_name='Autore_definizione_it',
            new_name='Host_documento_fonte',
        ),
        migrations.RenameField(
            model_name='glossary_entry',
            old_name='Autore_documento_fonte_ch',
            new_name='Lemma',
        ),
        migrations.RenameField(
            model_name='glossary_entry',
            old_name='Autore_documento_fonte_it',
            new_name='Posizione_definizione',
        ),
        migrations.RenameField(
            model_name='glossary_entry',
            old_name='Host_documento_fonte_ch',
            new_name='Titolo_documento_fonte',
        ),
        migrations.RenameField(
            model_name='glossary_entry',
            old_name='Url_definizione_ch',
            new_name='Url_definizione',
        ),
        migrations.RenameField(
            model_name='glossary_entry',
            old_name='Url_definizione_it',
            new_name='Url_documento_fonte',
        ),
        migrations.RemoveField(
            model_name='glossary_entry',
            name='Acronimo_it',
        ),
        migrations.RemoveField(
            model_name='glossary_entry',
            name='Definizione_it',
        ),
        migrations.RemoveField(
            model_name='glossary_entry',
            name='Host_documento_fonte_it',
        ),
        migrations.RemoveField(
            model_name='glossary_entry',
            name='Lemma_ch',
        ),
        migrations.RemoveField(
            model_name='glossary_entry',
            name='Lemma_it',
        ),
        migrations.RemoveField(
            model_name='glossary_entry',
            name='Posizione_definizione_ch',
        ),
        migrations.RemoveField(
            model_name='glossary_entry',
            name='Posizione_definizione_it',
        ),
        migrations.RemoveField(
            model_name='glossary_entry',
            name='Titolo_documento_fonte_ch',
        ),
        migrations.RemoveField(
            model_name='glossary_entry',
            name='Titolo_documento_fonte_it',
        ),
        migrations.RemoveField(
            model_name='glossary_entry',
            name='Url_documento_fonte_ch',
        ),
        migrations.RemoveField(
            model_name='glossary_entry',
            name='Url_documento_fonte_it',
        ),
        migrations.AlterField(
            model_name='glossary_entry',
            name='Data_inserimento_entry',
            field=models.DateField(default=datetime.date(2019, 9, 28)),
        ),
    ]
