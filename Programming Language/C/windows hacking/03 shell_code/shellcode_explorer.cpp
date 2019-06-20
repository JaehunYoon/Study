#include <stdio.h>
#include <tchar.h>
#include <Windows.h>

int _tmain(int argc, _TCHAR* argv[]) {
	__asm {
		// explorer
		mov  byte ptr[ebp - 33], 65h
		mov  byte ptr[ebp - 32], 78h
		mov  byte ptr[ebp - 31], 70h
		mov  byte ptr[ebp - 30], 6Ch
		mov  byte ptr[ebp - 29], 6Fh
		mov  byte ptr[ebp - 28], 72h
		mov  byte ptr[ebp - 27], 65h
		mov  byte ptr[ebp - 26], 72h
		mov  byte ptr[ebp - 25], 2Eh
		mov  byte ptr[ebp - 24], 65h
		mov  byte ptr[ebp - 23], 78h
		mov  byte ptr[ebp - 22], 65h
		mov  byte ptr[ebp - 21], 20h
		mov  byte ptr[ebp - 20], 63h
		mov  byte ptr[ebp - 19], 3Ah
		mov  byte ptr[ebp - 18], 5Ch
		mov  byte ptr[ebp - 17], 77h
		mov  byte ptr[ebp - 16], 69h
		mov  byte ptr[ebp - 15], 6Eh
		mov  byte ptr[ebp - 14], 64h
		mov  byte ptr[ebp - 13], 6Fh
		mov  byte ptr[ebp - 12], 77h
		mov  byte ptr[ebp - 11], 73h
		mov  byte ptr[ebp - 10], 5Ch
		mov  byte ptr[ebp - 9], 73h
		mov  byte ptr[ebp - 8], 79h
		mov  byte ptr[ebp - 7], 73h
		mov  byte ptr[ebp - 6], 74h
		mov  byte ptr[ebp - 5], 65h
		mov  byte ptr[ebp - 4], 6Dh
		mov  byte ptr[ebp - 3], 33h
		mov  byte ptr[ebp - 2], 32h
		mov  byte ptr[ebp - 1], 0h

		// call WinExec(code, SW_SHOW)
		push  5
		lea  eax, [ebp - 33]
		push  eax
		mov  eax, 0x73BE3A10
		call  eax
		// call ExitProcess(1)
		push  1
		mov  eax, 0x73BE3A20
		call  eax
	}

	return 0;
}