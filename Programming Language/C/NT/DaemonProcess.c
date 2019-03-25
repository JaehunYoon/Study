#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

int main()
{
    int pid;
    int i;

    i = 1000;
    pid = fork();
    if (pid == -1)
    {
        perror("fork error ");
        exit(0);
    }
    // chile process
    else if (pid == 0)
    {
        printf("my parent id is %d\n", getpid());
        close(0);
        close(1);
        close(2);
        setsid();
        while(1)
        {
            printf("-->%d\n", i);
            i++;
            sleep(1);
        }
    }
    // 부모프로세스가 실행시키는 코드
    else
    {
        printf("my child PID is [%d]\n", pid);
        sleep(1);
        printf("i'm going now \n");
        exit(0);
    }
}