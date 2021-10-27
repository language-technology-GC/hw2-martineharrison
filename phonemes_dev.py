# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 15:18:52 2021

@author: andre
"""
import csv

not_read_entire_file = True
with open("ice_dev.tsv", encoding = 'utf8') as dev:
    phonemes =  open("dev.ice.p", 'wb')
    dev_list = list(csv.reader(dev, delimiter="\t", quotechar='"'))
    second_column = []
    for item in dev_list:
        second_column.append(item[1])
    stringed = '\n'.join(second_column)
    re_encoded = stringed.encode('utf-8')
    phonemes.write(re_encoded)
    if dev == '':
      not_read_entire_file = False
      phonemes.close()