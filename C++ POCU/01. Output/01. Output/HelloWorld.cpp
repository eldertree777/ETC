#include <iostream>

using namespace std;


namespace hello {
	void printHello() {
		cout << "Hello World" << endl;
	}
}

int main() {
	hello::printHello();

	// 16���� ���
	int number = 10;
	cout << showbase << hex << number << endl;
}