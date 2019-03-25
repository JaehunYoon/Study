#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
 
int main() {
     
    pid_t childPid;
    int i;
     
    childPid = fork();
     
    if(childPid > 0) {  // 부모 프로세스
        printf("부모 PID : %ld, pid : %d\n",(long)getpid(), childPid);
        sleep(2);
        printf("부모 종료\n");
        exit(0);
    }
    else if(childPid == 0){  // 자식 코드
        printf("자식 시작\n");
         
        for(i=0;i<10;i++) {
            printf("자식 PID : %ld 부모 PID : %ld\n",(long)getpid(), (long)getppid());
            sleep(1);
        }
         
        printf("자식 종료\n");
        exit(0);
    }
    else {  // fork 실패
        perror("fork Fail! \n");
        return -1;
    }
     
    return 0;
}