#include <unistd.h>
#include <stdlib.h>
#include <signal.h>

void sig_handler(int signo) {
    printf("SIGINT\n");
}

// 쓰레드 함수
void *t_function(void *data) {
    char a[100000];
    int num = *((int *)data);
    printf("Thread Start\n");
    sleep(5);
    printf("Thread end\n");

    return (void*)&num;
}

int main() {
    pthread_t p_thread;
    int thr_id;
    int status;
    int a = 100;

    printf("Before Thread\n");
    thr_id = pthread_create(&p_thread, NULL, t_function, (void *)&a);
    if (thr_id < 0) {
        perror("thread create error : ");
        exit(0);
    }
    signal(SIGINT, (void *)sig_handler);

    pthread_detach(p_thread); // pthread_join 을 사용하면 blocking 이 되기 때문에 쓰레드를 분리.
    pause();
    printf("end of Process\n");

    return 0;
}