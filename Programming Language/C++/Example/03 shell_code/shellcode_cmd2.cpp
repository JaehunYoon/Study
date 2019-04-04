#include <stdio.h>
#include <tchar.h>
#include <Windows.h>

int _tmain(int argc, _TCHAR* argv[]) {
	__asm {
		// cmd
		xor ebx, ebx
		mov [ebp-4], ebx
		mov  byte ptr[ebp - 4], 63h
		mov  byte ptr[ebp - 3], 6Dh
		mov  byte ptr[ebp - 2], 64h
		// call WinExec('cmd', SW_SHOW)
		push  5
		lea  eax, [ebp - 4]
		push  eax
		mov  eax, 0x74b23a30
		call  eax
		// call ExitProcess(1)
		push  1
		mov  eax, 0x74ae3a20
		call  eax
	}

	return 0;
}