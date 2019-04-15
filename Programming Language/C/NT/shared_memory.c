#include <sys/ipc.h>
#include <sys/shm.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

int main(int argc, char **argv) {
    int shmid;
    void *shared_memory = (void *) 0;
    FILE *fp;
    char buff[1024];
    int skey = 5678;

    int *process_num;
    int local_num;

    // 공유메모리 공간을 만든다.
    shmid = shmget((key_t)skey, sizeof(int), 0666|IPC_CREAT);
    if (shmid == -1) {
        perror("shmget failed : ");
        exit(0);
    }

    // ipcs(s) 를 이용해서 확인하기 위함.
    printf("Key %x\n", skey);

    // 공유메모리를 맵핑한다.
    shared_memory = shmat(shmid, (void *) 0, 0);
    if (!shared_memory) {
        perror("shmat failed : ");
        exit(0);
    }

    process_num = (int *)shared_memory;

    for (;;) {
        local num = 0;
        
    }
}