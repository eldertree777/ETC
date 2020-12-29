#include <iostream>

using namespace std;


namespace hello {
	void printHello() {
		cout << "Hello World" << endl;
	}
}

int main() {
	hello::printHello();

	// 16진수 출력
	int number = 10;
	cout << showbase << hex << number << endl;
}