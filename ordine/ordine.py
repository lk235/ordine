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
for index, row in input_df.iterrows():
    if
