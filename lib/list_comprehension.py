#!/usr/bin/env python3

def return_evens(num_list):
    '''Return even numbers from a list'''
    return [num for num in num_list if num % 2 == 0]
    

def make_exclamation(sentence_list):
    '''Return list of sentences with exclamation marks'''
    return [sentence + '!' for sentence in sentence_list if sentence]