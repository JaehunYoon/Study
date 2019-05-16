#include <Windows.h>
#include <tchar.h>

int _tmain(int argc, _TCHAR* argv[]) {
    char cmd[4] = {'c', 'm', 'd', '\x0'};
    WinExec(cmd, SW_SHOW);
    ExitProcess(1);
}