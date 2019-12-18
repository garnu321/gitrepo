/*
 * zliczanie.cpp
*/

#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
	int a;
    int b = 0;
    int c = 0;
    cout << "Podaj liczbę: ";
    cin >> a;
    while (a != 0) {
        if (a % 5 == 0) {
            b = b + 1;
        }
        if (a % 7 == 0) {
            c = c + 1;
        }
        cout << "Podaj liczbę: ";
        cin >> a;
    }
    cout << "Podzielnych przez 5: " << b << endl;
    cout << "Podzielnych przez 7: " << c << endl;
    
	return 0;
}

