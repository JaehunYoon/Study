#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <sys/socket.h>

#define BUFF_SIZE 1024

int main(int argc, char **argv) {
    int client_socket;
    struct sockaddr_in server_addr;
    char buff[BUFF_SIZE + 5];

    client_socket = socket(PF_INET, SOCK_STREAM, 5);

    if (client_socket == -1) {
        printf("client socket 생성 실패\n");
        exit(-1);
    }

    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(4000);
    server_addr.sin_addr.s_addr = inet_addr("127.0.0.1");

    if (connect(client_socket, (struct sockaddr*)&server_addr, sizeof(server_addr)) == -1) {
        printf("접속 실패\n");
        exit(-1);
    }

    send(client_socket, argv[1], strlen(argv[1])+1, 0);
    recv(client_socket, buff, BUFF_SIZE, 0);
    printf("%s\n", buff);
    close(client_socket);

    return 0;
}