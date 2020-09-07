#include <iostream>
#include<string> 
#include <string.h>
using namespace std;
string arr;
string arrB;
int n,m;
bool cekDigitSpesial(string res){
    for(int i=0; i<n; i++){
        size_t found = res.find(arr[i]); 
        if (not (found != string::npos)) 
        return false; //tidak ketemu
    }
    return true;
}
bool cekDigitTidakSpesial(string res, int nt){
    
    for(int i=0; i<nt; i++){
        size_t found = res.find(arrB[i]); 
        if (found != string::npos) //ketemu
        return true; //ketemu
    }
    return false;
}

bool cekMod(int ires){
    for (int i = 0; i < n; i++) { 
        int ia = arr[i]-'0';
		if (ia !=0 &&ires % ia != 0) 
			return false; 
	} 
	return true; 
}

int main() {
    int ires;
    cin >> n >> m;
    
    for(int i=0; i<n; i++){
        cin >> arr[i];

    }
    if('1'!=arr[0]&&'1'!=arr[1]&&'1'!=arr[2]&&'1'!=arr[3]&&'1'!=arr[4]&&'1'!=arr[5]&&'1'!=arr[6]&&'1'!=arr[7]&&'1'!=arr[8]&&'1'!=arr[9]){
        arrB+='1';
    }
    if('2'!=arr[0]&&'2'!=arr[1]&&'2'!=arr[2]&&'2'!=arr[3]&&'2'!=arr[4]&&'2'!=arr[5]&&'2'!=arr[6]&&'2'!=arr[7]&&'2'!=arr[8]&&'2'!=arr[9]){
        arrB+='2';
    }
    if('3'!=arr[0]&&'3'!=arr[1]&&'3'!=arr[2]&&'3'!=arr[3]&&'3'!=arr[4]&&'3'!=arr[5]&&'3'!=arr[6]&&'3'!=arr[7]&&'3'!=arr[8]&&'3'!=arr[9]){
        arrB+='3';
    }
    if('4'!=arr[0]&&'4'!=arr[1]&&'4'!=arr[2]&&'4'!=arr[3]&&'4'!=arr[4]&&'4'!=arr[5]&&'4'!=arr[6]&&'4'!=arr[7]&&'4'!=arr[8]&&'4'!=arr[9]){
        arrB+='4';
    }
    if('5'!=arr[0]&&'5'!=arr[1]&&'5'!=arr[2]&&'5'!=arr[3]&&'5'!=arr[4]&&'5'!=arr[5]&&'5'!=arr[6]&&'5'!=arr[7]&&'5'!=arr[8]&&'5'!=arr[9]){
        arrB+='5';
    }
    if('6'!=arr[0]&&'6'!=arr[1]&&'6'!=arr[2]&&'6'!=arr[3]&&'6'!=arr[4]&&'6'!=arr[5]&&'6'!=arr[6]&&'6'!=arr[7]&&'6'!=arr[8]&&'6'!=arr[9]){
        arrB+='6';
    }
    if('7'!=arr[0]&&'7'!=arr[1]&&'7'!=arr[2]&&'7'!=arr[3]&&'7'!=arr[4]&&'7'!=arr[5]&&'7'!=arr[6]&&'7'!=arr[7]&&'7'!=arr[8]&&'7'!=arr[9]){
        arrB+='7';
    }
    if('8'!=arr[0]&&'8'!=arr[1]&&'8'!=arr[2]&&'8'!=arr[3]&&'8'!=arr[4]&&'8'!=arr[5]&&'8'!=arr[6]&&'8'!=arr[7]&&'8'!=arr[8]&&'8'!=arr[9]){
        arrB+='8';
    }
    if('9'!=arr[0]&&'9'!=arr[1]&&'9'!=arr[2]&&'9'!=arr[3]&&'9'!=arr[4]&&'9'!=arr[5]&&'9'!=arr[6]&&'9'!=arr[7]&&'9'!=arr[8]&&'9'!=arr[9]){
        arrB+='9';
    }
    
    int nt = 0; 
    while (arrB[nt]) 
        {nt++;}
    int i = 1;
    bool x=false; //tidak ada karakter spesial
    bool y=true; //ada karakter tidak spesial
    while(ires <= 1000000){
        ires = m*i;
        string res= to_string(ires); 
        x=cekDigitSpesial(res);
        y=cekDigitTidakSpesial(res, nt);
       bool def = cekMod(ires);
        
        if(x and !y){
            break;
        }
        i++;
    }
    if(ires>1000000){
        cout << -1 << endl;
    }else
    cout << ires <<endl;
    return 0;
}