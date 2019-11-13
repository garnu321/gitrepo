#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sumuj_parzyste():
    suma = 0
    for i in range(0, 100, 2):
        # liczba = int(input("Podaj liczbę: "))
        suma = suma + i
        print(suma)


def main(args):
    sumuj_parzyste()
   
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
