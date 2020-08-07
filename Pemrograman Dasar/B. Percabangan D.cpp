#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    int sisi[3];
    cin >> sisi[0] >> sisi[1] >> sisi[2];
    int n = sizeof(sisi)/sizeof(sisi[0]); 
    sort(sisi, sisi+n); 
    if(sisi[0]<sisi[1]<sisi[2] && sisi[0]+sisi[1]>sisi[2])
    cout << "segitiga" << endl;
    else
    cout << "bukan segitiga" << endl;
    return 0;
}