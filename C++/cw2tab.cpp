/*
 * cw2tab.cpp

 */


#include <iostream>
#include <iomanip>
using namespace std;

void wypelnij(int tb[][10], int w, int k, int n) {
    srand(time(NULL));
    for(int i=0; i<w; i++) {
        for(int j=0; j<k; j++) {
            tb[i][j] = rand() % (n + 1);    
            cout << i << "," << j << " " << tb[i][j] << endl;
        
        }
    }
    
}

void sumujW(int tb[][10], int w, int k) {
    int sumaW = 0;
    for(int i=0; i<w; i++) {
        for(int j=0; j<k; j++) {
            cout << setw(4) << tb[i][j];
            sumaW += tb[i][j];
        }
        cout << setw(6) << sumaW << endl;
        
    }
} 

void sumujK(int tb[][10], int w, int k) {
    int sumaK = 0;
    for(int i=0; i<w; i++) {
        for(int j=0; j<k; j++) {
            cout << setw(4) << tb[i][j];
            sumaK += tb[j][i];
        }
        cout << setw(6) << sumaK << endl;
        
    }
} 


int main(int argc, char **argv)
{
    int n = 0;
    cout << "Podaj wartość maksymalną: ";
    cin >> n;
    int w = 5;
    int k = 10; 
    int tb[w][10];
	wypelnij(tb, w, k, n);
    sumujW(tb, w, k);
    sumujK(tb, w, k);
	return 0;
}

