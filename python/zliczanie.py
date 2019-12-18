#!/usr/bin/env python
# -*- coding: utf-8 -*-
#



def main(args):
    b = 0
    c = 0
    a = int(input("Podaj liczbę: "))
    while a != 0:
        if a % 5 == 0: 
            b = b + 1
        if a % 7 == 0: 
            c = c + 1   
        a = int(input("Podaj liczbę: "))      
    print("Podzielnych przez 5:", b)    
    print("Podzielnych przez 7:", c)   
    return 0
    
       

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
