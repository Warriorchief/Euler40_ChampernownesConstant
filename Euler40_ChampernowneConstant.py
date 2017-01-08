#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 11:58:51 2017

@author: christophergreen
Champernowne's constant
Problem 40
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

def assemble():
    champ= "1234567891011121314151617181920"
    i=21;
    while len(champ)<1000001:
        champ+=str(i);
        i+=1
    return champ;

champ=assemble();



print(int(champ[0])*int(champ[9])*int(champ[99])*int(champ[999])*int(champ[9999])*int(champ[99999])*int(champ[999999])); #-->210 CORRECT