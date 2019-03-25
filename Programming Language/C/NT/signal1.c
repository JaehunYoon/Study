#include <stdio.h>
#include <unistd.h>
#include <signal.h>

void sig_handler(int signo);

int main(int argc, char **argv) {
    int i = 0;
    signal(SIGINT, SIG_IGN);
    while(1) {
        printf("%d\n", i);
        sleep(2);
        i++;
    }
}

void sig_handler(int signo) {
    printf("I Received SIGINT(%d)\n", SIGINT);
}