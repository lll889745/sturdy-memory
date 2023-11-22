#include <iostream>
using namespace std;

// 欧几里得算法：两个整数的最大公约数等于其中较小数和两数相除余数的最大公约数
// 核心点：gcd(a, b) = gcd(b, a % b)；a * a_rev = 1 (mod m)
int gcd(int a, int b) { // a为较大数，b为较小数
	while (b != 0) {
		int temp = a % b;
		a = b;
		b = temp;
	}
	return a;
}

bool isPrime(int a, int b) { // 判断a和b是否互质
	return gcd(a, b) == 1;
}

int main() {
	int a, m;
	while(1){
	cout << "Type in a and m..." << endl;
	cin >> a >> m;
	if (!isPrime(a, m)) { // a和m不互质
		cout << "No";
		return 0;
	}
	// 遍历1 ~ m − 1的整数 a_rev，寻找满足(a × a_rev) % m = 1的数
	for (int a_rev = 1; a_rev < m; a_rev++) {
		if ((a * a_rev) % m == 1) { // a * a_rev = 1 (mod m)
			cout << "Yes" << endl;
			cout << a_rev << endl;
		}
	}
	}
	return 0;
}
//717 619369