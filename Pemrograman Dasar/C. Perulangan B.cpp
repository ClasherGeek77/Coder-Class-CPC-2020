#include <iostream>
using namespace std;

int main() {
    int a, b, c, x, z;
    cin >> a >> b >> c >> x;
    z =  (a*x + b) % c;
    int i=1;
    while(z!=x){
        z =  (a*z + b) % c;
        i++;
    }
    cout << i << endl;
    return 0;
}