#include <Windows.h>
#include <stdio.h>
#include <tchar.h>

int _tmain(int argc, _TCHAR* argv[]) {
    if (argc < 3) {
        printf("\n # Get Function Address v1.0 by DSM #");
        printf("Usage : %s [dll] [proc]", argv[0]);
        return -1;
    }

    HMODULE hmodule = LoadLibrary(argv[1]);

    if (hmodule == NULL) {
        printf("dll 로드 실패\n");
        exit(1);
    }

    PVOID pvoid = GetProcAddress(hmodule, argv[2]);

    if (pvoid == NULL) {
        printf("함수 로드 실패\n");
        exit(1);
    }

    printf("addr : %p\n", pvoid);
    return 0;
}