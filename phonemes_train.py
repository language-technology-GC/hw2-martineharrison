# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 14:02:48 2021

@author: andre
"""
import csv

not_read_entire_file = True
with open("ice_train.tsv", encoding = 'utf8') as training:
    phonemes =  open("train.ice.p", 'wb')
    training_list = list(csv.reader(training, delimiter="\t", quotechar='"'))
    second_column = []
    for item in training_list:
        second_column.append(item[1])
    stringed = '\n'.join(second_column)
    re_encoded = stringed.encode('utf-8')
    phonemes.write(re_encoded)
    if training == '':
      not_read_entire_file = False
      phonemes.close()
  
