#include <iostream>
#include <vector>
#include <cmath>
#include <numeric>
using namespace std;

bool is_prime(int n) { // 爱拉托斯散筛法
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    for (int i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) return false;
    }
    return true;
}

vector<int> prime_factors(int n) { // 分解质因数
    vector<int> factors;
    while (n % 2 == 0) { // 先把2全部除掉
        n /= 2;
    }
    for (int i = 3; i <= sqrt(n); i += 2) { // 从3开始，每次加2
        while (n % i == 0) {
            if (factors.empty() || factors.back() != i) {
                factors.push_back(i);
            }
            n /= i;
        }
    }
    if (n > 2) { // 如果最后剩下一个大于2的数，那么一定是质数
        factors.push_back(n);
    }
    return factors;
}

int pow_mod(int base, int exponent, int mod) { // 快速幂取模
    int result = 1;
    base %= mod;
    while (exponent > 0) {
        if (exponent & 1) {
            result = (long long)result * base % mod;
        }
        exponent >>= 1;
        base = (long long)base * base % mod;
    }
    return result;
}

bool is_primitive_root(int g, int p) { // 判断g是否是p的原根
    vector<int> factors = prime_factors(p - 1); // 分解p-1的质因数
    for (int factor : factors) {
        if (pow_mod(g, (p - 1) / factor, p) == 1) { // 如果g^((p-1)/factor) mod p != 1，那么g就是p的原根
            return false;
        }
    }
    return true;
}

int find_primitive_root(int p) { // 寻找p的第一个原根g1
    for (int g = 2; g < p; ++g) {
        if (is_primitive_root(g, p)) {
            return g;
        }
    }
    return -1;
}

int euler_phi(int n) { // 欧拉函数
    if(is_prime(n)) return n - 1;
    int result = n;
    for (int i = 2; i * i <= n; ++i) {
        if (n % i == 0) {
            while (n % i == 0) {
                n /= i;
            }
            result -= result / i;
        }
    }
    if (n > 1) result -= result / n;
    return result;
}

vector<int> find_primitive_roots(int p) { // 寻找p的所有原根：g1^di，其中di是p-1的简化剩余系（模p-1的余数）
    int g = find_primitive_root(p);
    int phi = euler_phi(p - 1);
    vector<int> roots;
    for (int k = 1; k < p; ++k) {
        if (gcd(k, p - 1) == 1) { // k和p-1互质，属于简化剩余系
            roots.push_back(pow_mod(g, k, p));
        }
    }
    return roots;
}

int main() {
    int p;
    cout << "Enter an odd prime number: ";
    cin >> p;

    if (!is_prime(p) || p % 2 == 0) {
        cout << p << " is not an odd prime number." << endl;
        return 1;
    }

    vector<int> primitive_roots = find_primitive_roots(p);
    cout << "Primitive roots modulo " << p << ": ";
    for (int root : primitive_roots) {
        cout << root << " ";
    }
    cout << endl;

    return 0;
}