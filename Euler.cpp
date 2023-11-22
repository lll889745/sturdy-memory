#include <iostream>
#include <cmath>
using namespace std;

// phi(n) 定义为小于等于 n 的正整数中与 n 互质的数的个数。
// 我们通过枚举 n 的所有质因数，然后根据欧拉函数的公式计算出 phi(n) 的值。
// 核心点：n = p1^k1 * p2^k2 * ... * pk^k；phi(n) = n * (1 - 1/p1) * (1 - 1/p2) * ... * (1 - 1/pk)
int phi(int n) {
	int result = n;
	for (int i = 2; i * i <= n; ++i) { // 在2 ~ sqrt(n)之间枚举质因数
	// i * i <= n is faster than i <= sqrt(n)
		if (n % i == 0) { // i is a prime factor of n
			// 对于任意正整数 n，其质因数分解可以表示为 n = p1^k1 * p2^k2 * ... * pk^k
			while (n % i == 0) { // 所以我们希望将n中的pi全部除掉
				n /= i;
			}
			result -= result / i; // phi(n) = n * (1 - 1/p1) * (1 - 1/p2) * ... * (1 - 1/pk)
		}
	}
	if (n > 1) { // n 是质数，因为对于质数而言前面的判断条件不成立
		result -= result / n;
		// result--;
	}
	return result;
}

int main() {
	int n;
	cout << "Type in an integer..." << endl;
	cin >> n;
	cout << "Phi(" << n << ") = " << phi(n);
	return 0;
}
