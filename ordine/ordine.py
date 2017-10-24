# -*- coding: utf-8-*-
import os, sys

# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")
import csv
import pandas as pd

input_file = 'dailyshop di Chen luca.xlsx'

barcode_table = pd.read_csv('barcode.txt')
# print barcode_table
Esempio_ordine = pd.read_csv('_Esempio_ordine.txt',sep=';')
print Esempio_ordine.keys()

input_df = pd.read_excel(input_file)
output_df = input_df
barcode_title = unicode('商品条码', "utf8", errors="ignore")
# print input_df[barcode_title]


Esempio_ordine_new = pd.DataFrame(data=None,columns=Esempio_ordine.columns)

Esempio_ordine_new['cod_articolo'] = input_df[barcode_title]


for index, row in Esempio_ordine_new.iterrows():
    print index
    row['cod_articolo'] = 1

print Esempio_ordine_new