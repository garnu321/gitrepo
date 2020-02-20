#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  NWD1.py



def main(args):
    a = int(input("Podaj 1 liczbę: "))
    b = int(input("Podaj 2 liczbę: "))
    licznik = 0
    while a != b:
        licznik += 1
        if a > b: 
            a = a - b
        else: 
            b = b - a
    print ("NWD tych liczb wynosi:", a) 
    print (licznik)   
  
           
            
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
