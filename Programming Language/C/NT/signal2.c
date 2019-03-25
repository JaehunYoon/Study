#include <stdio.h>
#include <signal.h>

struct sigaction act_new;
struct sigaction act_old;

void sigint_handler(int signo) {
    printf("Ctrl + c 키를 누르셨죠!\n");
    printf("다시 입력 시 종료됩니다.\n");
    sigaction(SIGINT, &act_old, NULL);
}

int main(void) {
    act_new.sa_handler = sigint_handler;
    sigemptyset(&act_new.sa_mask);

    sigaction(SIGINT, &act_new, &act_old);
    while(1) {
        printf("test ttt ttt\n");
        sleep(1);
    }
}