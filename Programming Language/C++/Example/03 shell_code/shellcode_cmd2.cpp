#include <stdio.h>
#include <tchar.h>

int _tmain(int argc, _TCHAR* argv[]) {
    __asm {
        // cmd
        mov  byte ptr [ebp-4], 63h
        mov  byte ptr [ebp-3], 6Dh
        mov  byte ptr [ebp-2], 64h
        mov  byte ptr [ebp-1], 0
        // call WinExec('cmd', SW_SHOW)
        push  5
        lea  eax, [ebp-4]
        push  eax
        mov  eax, 0x769D3A30
        call  eax
        // call ExitProcess(1)
        push  1
        mov  eax, 0x76993A20
        call  eax
    }

    return 0;
}