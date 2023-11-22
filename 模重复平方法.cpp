#include <iostream>
using namespace std;

// 计算 (x * y) % p 的函数
int multiplyMod(int x, int y, int p) {
	return (x % p * y % p) % p;
}

// 模重复平方法
int powerMod(int base, int exponent, int modulus) {
	int result = 1; // 初始化结果
	base = base % modulus; // 如果 base >= modulus，更新它
	if (base == 0)
		return 0; // 如果 base 是 0，返回 0
	while (exponent > 0) {
		// 通过位与运算判断奇偶性。如果指数是奇数，将 base 乘以结果
		if (exponent & 1)
			result = multiplyMod(result, base, modulus);
		// 指数减半
		exponent = exponent >> 1;
		// 执行平方
		base = multiplyMod(base, base, modulus);
	}
	return result;
}

int main() {
	int base, exponent, modulus;
	cout << "Enter base, exponent and modulus..." << endl;
	cin >> base >> exponent >> modulus;
	cout << "Result of " << base << "^" << exponent << " mod " << modulus << " is " << powerMod(base, exponent, modulus) << endl;
	return 0;
}