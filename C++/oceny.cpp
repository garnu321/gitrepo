/*
 * oceny.cpp

 */


#include <iostream>
using namespace std;
int main(int argc, char **argv)
{
 float ocena, oceny, suma, srednia;
    suma = 0;
    cout << "Podaj liczbe ocen:";
    cin >> oceny;
    while (oceny < 1) {
        cout << "Podaj liczbę ocen:";
        cin >> oceny;
    }
    for(int i = 0; i < oceny; i = i + 1) {
        cout << "Podaj ocenę:";
        cin >> ocena;
        while (ocena < 1 or ocena > 6) {
            cout << "Błędna ocena! Podaj poprawną: ";
            cin >> ocena;
            
        }
        suma = suma + ocena;
    }
    srednia = suma / oceny;
    cout << "Twoja średnia wynosi: ";
    cout << srednia;

	return 0;
}

