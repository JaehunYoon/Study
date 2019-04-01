#include <stdio.h>
#include <unistd.h>
#include <pthread.h>

void* threadFunc(void *data) {
    int i;
    int me = *((int *)data);

    for (i = 0; i < 10; i++) {
        printf("%d - Got %d\n", me, i);
        sleep(1);
    }
}

int main() {
    int thr_id;
    pthread_t p_thread[3];
    int status;
    int a = 1;
    int b = 2;
    int c = 3;

    thr_id = pthread_create(&p_thread[0], NULL, threadFunc, (void *)&a);
    thr_id = pthread_create(&p_thread[1], NULL, threadFunc, (void *)&a);
    thr_id = pthread_create(&p_thread[2], NULL, threadFunc, (void *)&a);

    pthread_join(p_thread[0], (void **) &status);
    pthread_join(p_thread[1], (void **) &status);
    pthread_join(p_thread[2], (void **) &status);

    printf("programming is end\n");
    return 0;
}