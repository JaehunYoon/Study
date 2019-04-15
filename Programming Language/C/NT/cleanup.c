#include <pthread.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

// cleanup handler
void cleanup(void *arg) {
    printf("Thread Clean up\n");
    free(arg);
}

void *t_function(void *data) {
    static int retval = 999;
    int count = *((int *)data);
    int i = 0;

    char *mydata;
    mydata = (char *)malloc(1000);

    pthread_cleanup_push(cleanup, (void *)mydata);

    while (1) {
        // i 값이 3 이 되면 '현재 쓰레드' 종료
        if (i == count) {
            // 반환값 설정
            pthread_exit((void *)&retval);
        }

        printf("Thread Running... %d : data=%d\n", i, count);
        i++;
        sleep(1);
    }

    pthread_cleanup_pop(0);
}

int main() {
    pthread_t p_thread;
    int thr_id;
    void *tret = NULL;
    int count = 3;

    // 쓰레드 생성, count 값을 쓰레드 함수에 넘겨줌
    thr_id = pthread_create(&p_thread, NULL, t_function, (void *)&count);
    if (thr_id < 0) {
        perror("thread create error : ");
        exit(0);
    }
    pthread_join(p_thread, &tret);

    // pthread_exit 의 반납값 출력
    printf("thread exit code %d\n", *((int*)tret));

    return 0;
}