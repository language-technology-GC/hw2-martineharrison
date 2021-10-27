# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 18:15:56 2021

@author: andre
"""
import re
import jiwer 

with open("predictions.txt", encoding = 'UTF-8') as predictions:
    new_list = [line for line in predictions]
    del new_list[:7]
    target_regex = re.compile("\AT\-\d+")
    hypothesis_regex = re.compile("\AH\-\d+")
    targets_list = list(filter(target_regex.match, new_list))
    hypotheses_list = list(filter(hypothesis_regex.match, new_list))
   
    split_targets = []
    for item in targets_list:
        split_targets.append(re.split(r'\t+', item))
    for item in split_targets:
        del item[:1]
    joined_targets = [''.join(item) for item in split_targets]
    stripped_targets = jiwer.RemoveWhiteSpace()(joined_targets)
    
    split_hypotheses = []
    for item in hypotheses_list:
        split_hypotheses.append(re.split(r'\t+', item))
    for item in split_hypotheses:
         del item[:2]
    joined_hypotheses = [''.join(item) for item in split_hypotheses]
    stripped_hypotheses = jiwer.RemoveWhiteSpace()(joined_hypotheses)
    
    wer_output =  open("wer_output.txt", 'w')
    wer = 100 * (jiwer.wer(stripped_targets, stripped_hypotheses))
    wer_output.write('Word error rate for Icelandic grapheme-to-phoneme engine: ' + str(round(wer)))
    wer_output.close()
    
    
    