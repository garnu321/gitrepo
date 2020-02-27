#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  NWD2.py



def main(args):
    a = int(input("Podaj 1 liczbę: "))
    b = int(input("Podaj 2 liczbę: "))
    licznik = 0
    while a > 0:
        licznik += 1
        a %= b
        b -= a 
        
    print ("NWD tych liczb wynosi:", b) 
    print (licznik)   
  
           
            
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
