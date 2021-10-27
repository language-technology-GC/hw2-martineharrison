# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 14:58:35 2021

@author: andre
"""
not_read_entire_file = True
with open("ice_dev.tsv", encoding = "utf8") as dev: 
    graphemes =  open("dev.ice.g", 'wb')
    for item in dev:
      first_column = [row.split()[0] for row in dev]
      spaced = [" ".join(item) for item in first_column]
      stringed = '\n'.join(spaced)
      re_encoded = stringed.encode('utf-8')
      graphemes.write(re_encoded)
      if dev == '':
         not_read_entire_file = False
         graphemes.close()