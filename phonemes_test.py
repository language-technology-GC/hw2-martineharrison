# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 16:22:02 2021

@author: andre
"""
import csv

not_read_entire_file = True
with open("ice_test.tsv", encoding = 'utf8') as test:
    phonemes =  open("test.ice.p", 'wb')
    test_list = list(csv.reader(test, delimiter="\t", quotechar='"'))
    second_column = []
    for item in test_list:
        second_column.append(item[1])
    stringed = '\n'.join(second_column)
    re_encoded = stringed.encode('utf-8')
    phonemes.write(re_encoded)
    if test == '':
      not_read_entire_file = False
      phonemes.close()