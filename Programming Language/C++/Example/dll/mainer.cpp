__declspec(dllimport) int mycal_plus(int, int);

int main() {
	int a = 20;
	int b = 90;
	int c = mycal_plus(a, b);
	
	return 0;
}
