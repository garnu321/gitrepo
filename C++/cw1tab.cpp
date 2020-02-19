/*

 */


#include <iostream>
using namespace std;

void pobierzLiczby(int t[], int n) {
    for (int i = 0; i < n; i++) {
        cout << "Podaj liczby: ";
        cin >> t[i]; 
        
        
    }
}

void drukuj(int t[], int n) {
    for (int i = 0; i < n; i++) {
         cout << t[i] << " ";
        
    }
    cout << endl;
}

void sumujTab(int t[], int n)
    


int main(int argc, char **argv) {
    int n = 5;
    int tablica1[n]; 
    int tablica2[n];
    pobierzLiczby(tablica1, n);
    pobierzLiczby(tablica2, n);
    drukuj(tablica1, n);
    drukuj(tablica2, n);
    int s1 = sumujTab(tablica1, n);
    int s2 = sumujTab(tablica2, n);
    
   
    
	
	return 0;
}

