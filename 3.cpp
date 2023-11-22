#include <iostream>
using namespace std;

int findRev(int a, int m) {
    for (int a_rev = 1; a_rev < m; a_rev++)
        if ((a * a_rev) % m == 1)
            return a_rev;
    return -1;
}
int main(){
    int n, x = 0, m_sum = 1;
    cout << "Enter n: " << endl;
    cin >> n;
    int m[n], b[n], M[n], M_rev[n];
    cout << "Enter m: " << endl;
    for (int i = 0; i < n; i++){
        cin >> m[i];
        m_sum *= m[i];
    }
    cout << "Enter b: " << endl;
    for (int i = 0; i < n; i++)
        cin >> b[i];
    for (int i = 0; i < n; i++){
        M[i] = m_sum / m[i];
        M_rev[i] = findRev(M[i], m[i]);
        x += b[i] * M[i] * M_rev[i];
    }
    cout << "x≡" << x % m_sum << "(mod " << m_sum << ")" << endl;
    return 0;
}
