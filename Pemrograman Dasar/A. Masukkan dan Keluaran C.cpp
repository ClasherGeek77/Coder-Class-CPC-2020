#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    float a, b, c, d, e, f;
    cin >> a >> b >> c >> d >> e >> f;
    cout << fixed;
    cout << setprecision(9);
    cout << (a+b+c+d+e+f)/6.0 <<endl;
    return 0;
}