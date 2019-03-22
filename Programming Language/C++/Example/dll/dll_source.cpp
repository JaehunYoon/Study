#include <iostream>
using namespace std;

__declspec(dllexport) int mycal_plus(int a, int b) {
	int c = a + b;
	cout << "dll mycal_plus() "<< a << " + " << b << " = " << c << endl;
	return c;
}
