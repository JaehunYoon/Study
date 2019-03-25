#include <unistd.h>
#include <string.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <signal.h>

void zombie_handler()
{
    int status;
    int spid;
    spid = wait(&status);
    printf("자식프로세스 wait 성공 \n");
    printf("================================\n");
    printf("PID         : %d\n", spid);
    printf("Exit Value  : %d\n", WEXITSTATUS(status));
    printf("Exit Stat   : %d\n", WIFEXITED(status));
}

int main()
{
    int pid;
    int status;
    int spid;
    int i;

    // SIGCHLD에 대해서 시그널핸들러를 설치한다.  
    signal(SIGCHLD, (void *)zombie_handler);
    for (i = 0; i < 3; i++)
    {
        pid = fork();
        int random_value = (random()%5)+3;
        if (pid == 0)
        {
            // 랜덤하게 기다린후 종료한다. 
            // 랜덤값을 리턴한다. 
            printf("I will be back %d %d\n", random_value, getpid());
            sleep(random_value);
            return random_value;
        }
    }
    getchar();
}