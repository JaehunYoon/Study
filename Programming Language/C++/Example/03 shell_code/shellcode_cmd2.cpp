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

		// kernel32.dll base address 구함
		mov  eax, fs:[eax+0x30] // Get a pointer to the PEB
		mov  eax, [eax+0xc] // Get PEB -> LDR (PEB_LDR_DATA)
		mov  eax, [eax+0x14] // Get PEB -> LDR.InMemoryOrderModuleList (.exe InMemyroOrderModuleList)
		mov  ebx, [eax] // Get the next entry (2nd entry) (ntdll.dll InMemoryOrderLinks)
		mov  ebx, [ebx] // kernel32.dll InMemoryOrderLinks
		mov  ebx, [ebx+0x10] // Get the 3rd entries base address (kernel32.dll) (ebx = kernel32.dll base address)
		
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