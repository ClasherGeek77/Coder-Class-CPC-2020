#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    int modulo = a%b;
    switch(modulo) {
        case 0: 
            cout << "Hore ^_^" <<endl;
            break;
        default:
            cout << "Kecewa :(" <<endl;
            break;
    }
    return 0;
}