#include <iostream>
using namespace std;

int main() {
    int a, b, x, y;
    cin >> a >> b >> x >> y;
    while(true){
    if (x>y)
    break;
    else{
        cout << x << endl;
        x = a*x + b;
    }
    }
    return 0;
}