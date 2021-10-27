# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 15:22:22 2021

@author: andre
"""
not_read_entire_file = True
with open("ice_test.tsv", encoding = "utf8") as test: 
    graphemes =  open("test.ice.g", 'wb')
    for item in test:
      first_column = [row.split()[0] for row in test]
      spaced = [" ".join(item) for item in first_column]
      stringed = '\n'.join(spaced)
      re_encoded = stringed.encode('utf-8')
      graphemes.write(re_encoded)
      if test == '':
         not_read_entire_file = False
         graphemes.close()