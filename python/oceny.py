#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  oceny.py
def pobierzOceny():
    oceny = []
    ocena = int(input("Podaj ocenę: "))
    while ocena > 0:
        if ocena < 7:
            oceny.append(ocena)
        else:
            print("Błędna ocena!") 
        ocena = int(input("Podaj ocenę: "))    
    return oceny


def LiczSrednia(oceny):
    print(sum(oceny) / len(oceny))
        
            


def main(args):
    oceny = pobierzOceny()
    LiczSrednia(oceny)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
