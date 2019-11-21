#!/usr/bin/env python
# -*- coding: utf-8 -*-



def main(args):
    stop = int(input("Podaj liczbę końcową: " ))
    if stop > 1: 
        
        for i in range(0, stop+1): 
            print(i*i)
    else:
        print("Podaj liczbę większą od 0!")    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
