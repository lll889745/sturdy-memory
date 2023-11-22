#include <iostream>
using namespace std;

int power(int a, int i, int p){ // a^i mod p
    int result = 1;
    a %= p;
    while(i > 0){
        if(i & 1)
            result = (result * a) % p;
        a = (a * a) % p;
        i >>= 1;
    }
    return result;
}

int ord(int a, int p){
    for(int i = 1; i < p; i++){
        if((p-1) % i != 0) // i不是p-1的因数
            continue;
        if(power(a, i, p) == 1)
            return i;
    }
    return -1;
}

int main(){
    int a, p;
    cout << "Enter a and p: " << endl;
    cin >> a >> p;
    cout << "ord " << p << "(" << a << ")=" << ord(a, p) << endl;
}