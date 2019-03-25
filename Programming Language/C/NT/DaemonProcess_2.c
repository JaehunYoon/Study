 #include <sys/types.h>
 #include <sys/stat.h>
 #include <stdio.h>
 #include <fcntl.h>

 int main()
 {

     int pid_rtn;
     pid_rtn = fork();
     printf("pid_rtn = [%d] \n", pid_rtn); // 자식프로세스 생성.

     //1. fork()로 자식프로세스 생성.
     if(pid_rtn < 0)  //fork() 오류시 종료.
     {
  printf("fork 오류... : return is [%d] \n", pid_rtn );
      perror("fork error : ");
  exit(0);
     } else if (pid_rtn > 0){ // 부모프로세스를 종료.
         printf("자식프로세스 : [%d] - 부모프로세스 : [%d] \n", pid_rtn, getpid() );
  exit(0);
     } else if(pid_rtn == 0) { // fork() 성공.
      printf("자식프로세스 : [%d]\n", getpid() );
  //pause();
     }
  
     //2.세션생성.
     setsid();

     //3.상대경로 명시.
     chdir("/");

     int cnt = 0;
     //4.데몬으로 돌릴 프로그램명시.
     while(1) {
  printf("카운트 증가=[%d] \n", cnt++ );
  sleep(10);   // 10초간격으로.
     }
 }