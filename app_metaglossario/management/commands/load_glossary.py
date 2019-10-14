# per ora non funziona

# myapp/management/commands/load_glossary.py
from django.core.management.base import BaseCommand, CommandError
import csv

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('csv_file', nargs='+', type=str)

    def handle(self, *args, **options):
        for csv_file in options['csv_file']:
            dataReader = csv.reader(open(csv_file), delimiter=',', quotechar='"')
            for row in dataReader:
                
                Lemma=row[0],
                Acronimo=row[1],
                Definizione=row[2],
                Ambito_riferimento=row[3],
                Autore_definizione=row[4],
                Posizione_definizione=row[5],
                Url_definizione=row[6],
                Titolo_documento_fonte=row[7],
                Autore_documento_fonte=row[8],
                Host_documento_fonte=row[9],
                Url_documento_fonte=row[10],
                Commento_entry=row[11],
                Data_inserimento_entry=row[12],
                Id_statico_entry=row[13],
                
                # etc...
                self.stdout.write(
                    'Created glossary entry'
                #     'Created glossary entry {} {}'.format(emp.Lemma, emp.Id_statico_entry)
                )

# You would then call this with:
# ./manage.py import_csv --csvfile "/home/<name>/webapps/<name2>/employees.csv"


#       python ./manage.py load_glossary csv_file "D:\Files Tommaso\Politecnico\Lavoro polimi\Algoritmi metaglossario Python\traformazioni di prova per il Metaglossario\dati_prova.csv"