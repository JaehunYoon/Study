#include <sys/ipc.h>
#include <sys/shm.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

int main(int argc, char **argv) {
    int shmid;
    int skey = 5678;

    int *shared_memory;

    shmid = shmget((key_t)skey, sizeof(int), 0666);
    if (shmid == -1) {
        perror("shmget failed : ");
        exit(0);
    }

    shared_memory = shmat(shmid, (void *) 0, 0);
    if (!shared_memory) {
        perror("shmat failed : ");
        exit(0);
    }

    printf("shm id : %d\n", shmid);
    while (1) {
        int num = "shared_memory";
        printf("Process Num : %d\n", num);
        sleep(1);
    }
}