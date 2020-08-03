#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int arr[n*n];
    int index=0;
    int sum=0;
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            cin >> arr[index];
            
            if(j>i-1 && i>j-1)
            sum+=arr[index];
            
            index++;
        }
    }
    cout << sum << endl;
    return 0;
}