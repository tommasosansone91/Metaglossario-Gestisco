# Generated by Django 2.2.2 on 2019-11-25 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_metaglossario', '0023_delete_displaying_terminology'),
    ]

    operations = [
        migrations.CreateModel(
            name='model_is_Titolo_documento_fonte_of',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_soggetto', models.CharField(max_length=25)),
                ('ID_oggetto', models.CharField(max_length=25)),
            ],
            options={
                'ordering': ['ID_soggetto', 'ID_oggetto'],
            },
        ),
    ]
