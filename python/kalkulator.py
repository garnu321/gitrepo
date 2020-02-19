#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kalkulator.py

wynik = 0

def pobierzLiczbe():
    x = int(input("Podaj liczbę: "))
    return x
    
def dodaj(x1, x2):
    global wynik
    wynik = x1 + x2 
    
    
def odejmij(x1, x2):
    global wynik
    wynik = x1 - x2
   
 
def pomnoz(x1, x2):
    global wynik
    wynik = x1 * x2
    
   
def podziel(x1, x2):
    global wynik
    wynik = x1 / x2             
       
    
def drukuj():
    print(wynik)
    
def main(args):
    operacja = input("Jakie działanie chcesz wykonać?(*, /, +, -): ")
    x1 = pobierzLiczbe()
    x2 = pobierzLiczbe()    
    if operacja == "+":
        dodaj(x1, x2)
    elif operacja == "-":
        odejmij(x1, x2) 
    elif operacja == "*":
        pomnoz(x1, x2)
    elif operacja == "/":
        podziel(x1, x2)                 
    else:
        print("Błedny znak działania!") 
    drukuj()      
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
