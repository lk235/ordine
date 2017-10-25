# -*- coding: utf-8-*-
import os, sys

# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")
import csv
import pandas as pd
from datetime import datetime

def replace_dot(s):
    s = s.replace('.',':') + ':00'
    # time_result = datetime.strptime(s, "%d/%m/%Y %H:%M:%S")
    # print time_result
    return s
    # return s.replace('.',':') + ':00'

input_file = 'dailyshop di Chen luca.xlsx'

barcode_table = pd.read_csv('barcode.txt')
# print barcode_table
Esempio_ordine = pd.read_csv('_Esempio_ordine.txt',sep=';')
print Esempio_ordine.keys()

input_df = pd.read_excel(input_file,index_col=None)
output_df = input_df
barcode_title = unicode('商品条码', "utf8", errors="ignore")
order_date_title = unicode('订单时间', "utf8", errors="ignore")
# print input_df[barcode_title]


Esempio_ordine_new = pd.DataFrame(data=None,columns=Esempio_ordine.columns)

Esempio_ordine_new['cod_articolo'] = input_df[barcode_title]

index_len = len(Esempio_ordine_new.index)
Esempio_ordine_new['version'] = ['1.0']*index_len
Esempio_ordine_new['ID_cliente'] = ['4E4B484E434D']* index_len
Esempio_ordine_new['codice_cliente'] = ['013428'] * index_len
Esempio_ordine_new['barcode'] = input_df[barcode_title]
# Esempio_ordine_new['nr_ordine'] =
Esempio_ordine_new['data_ordine'] = input_df[order_date_title]
Esempio_ordine_new['data_ordine'] = Esempio_ordine_new['data_ordine'].apply(replace_dot)
Esempio_ordine_new['destmerce_denominazione'] = ['Punto Vendita / Utente finale'] * index_len
Esempio_ordine_new['destmerce_indirizzo'] = ['Via delle cosmee,1'] * index_len
Esempio_ordine_new['destmerce_localita'] = ['ROMA'] * index_len
Esempio_ordine_new['destmerce_provincia'] = ['RM'] * index_len
Esempio_ordine_new['destmerce_cap'] = ['00134'] * index_len
Esempio_ordine_new['destmerce_telefono'] = ['3271388371'] * index_len
Esempio_ordine_new['note_spedizione'] = ['chiuso domenica'] * index_len
Esempio_ordine_new['comunicazioni_interne'] = ['spedire catalogo. grazie'] * index_len
Esempio_ordine_new = pd.merge(Esempio_ordine_new,barcode_table,on='barcode',how='left')
Esempio_ordine_new = Esempio_ordine_new[Esempio_ordine_new['cod_articolo1'].notnull()]
Esempio_ordine_new['cod_articolo'] = Esempio_ordine_new['cod_articolo1']
Esempio_ordine_new = Esempio_ordine_new.drop('cod_articolo1', axis=1)
Esempio_ordine_new = Esempio_ordine_new.drop('barcode', axis=1)
# Esempio_ordine_new['nr_riga'] =
# Esempio_ordine_new['totale_righe'] =
for index, row in Esempio_ordine_new.iterrows():
    print index
    row['cod_articolo'] = 00000000000

print Esempio_ordine_new.index
# Esempio_ordine_new['data_ordine'].astype('datetime64[ns]')
# Esempio_ordine_new['data_ordine'] = pd.to_datetime(Esempio_ordine_new['data_ordine'],format="%d/%m/%Y %H:%M:%S")
# print Esempio_ordine_new['data_ordine']
# print Esempio_ordine_new['cod_articolo']

# test =  pd.to_datetime(['08/10/2017'])
# tm = pd.Timestamp('24/10/2017')
# print tm
# # tm.map(lambda tm: tm.strftime('%d-%m-%Y'))
# tm1 =  tm.strftime("%d/%m/%y %H:%M:%S")
# print type(tm1)

# tm2 =  datetime.strptime('23/9/2017 00:00:00',"%d/%m/%Y %H:%M:%S")
# print tm2
# print type(tm2)
# dt = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
# print dt

Esempio_ordine_new.to_csv('test.csv',sep=':')

