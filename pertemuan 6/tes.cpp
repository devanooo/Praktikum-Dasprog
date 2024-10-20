#include <iostream>

using namespace std;


void rekursif(int x){
    if(x<0){
        return rekursif(x - 1);
    }
    else{
        x = 1;
    }
}
int main(){
    int x;
    rekursif(x);
    cin >> x;
}