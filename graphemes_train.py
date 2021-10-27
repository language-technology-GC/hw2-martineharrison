# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 18:55:45 2021

@author: andre
"""
not_read_entire_file = True
with open("ice_train.tsv", encoding = "utf8") as training: 
    graphemes =  open("train.ice.g", 'wb')
    for item in training:
      first_column = [row.split()[0] for row in training]
      spaced = [" ".join(item) for item in first_column]
      stringed = '\n'.join(spaced)
      re_encoded = stringed.encode('utf-8')
      graphemes.write(re_encoded)
      if training == '':
         not_read_entire_file = False
         graphemes.close()