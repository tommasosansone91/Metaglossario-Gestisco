# all'inizio questo lo posso fare come amministratore

from .models import glossary_entry
from .models import glossary_file

import pandas as pd

df = pd.read_excel (r'Path where the Excel file is stored\File name.xlsx') #for an earlier version of Excel, you may need to use the file extension of 'xls'
print (df)



def import_withtimes(request):
    print "Copia degli elementi dal modello dei file caricati (Glossary_file) al modello della terminologia (Glossary_entry)"
    po_cache = list()
    # The list() constructor returns a mutable sequence list of elements. If no parameters are passed, it creates an empty list. If iterable is passed as parameter, it creates a list of elements in the iterable.
    for item in glossary_file.objects.all():

        if item.po_number in po_cache:
            continue

        withtimes = Model2.objects.filter(planning_order=item.po_number)
        for wi in withtimes:
            po_cache.append(wi.planning_order)
            item.wms = wi.wms_order
            item.status = wi.shipment_status
            item.aging = wi.status_date
            item.carrier = wi.service_level
            item.add_date = wi.order_add_date
            item.asn_validation = wi.asn_sent_time
            item.docs_add_date = wi.docs_received_time
            item.save()


