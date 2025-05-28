#include <iostream>
#include <thread>
#include <cstring>
#include <unistd.h>
#include <netinet/in.h>
#include <arpa/inet.h>


constexpr int PORT = 8899;
constexpr int BUFF_SIZE = 1024*10;
using std::string;
using std::cout;
using std::endl;
using std::flush;

void recv_thread(int sock) {
    char buff[BUFF_SIZE];
    while (true) {
        int len = read(sock, buff, sizeof(buff) - 1);
        if (len>0) {
            buff[len] = '\0';
            std::cout << "fd(" <<sock<<"): "<< buff << std::endl << std::flush;
        } else if (len == 0) {
            std::cout << "\n Server closed connection \n";
            exit(0);
        }
    }
}
int main() {
    int sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock < 0) {
        perror("socket create failed");
        return -1;
    }

    sockaddr_in serv_addr = {};
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(PORT);
    inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr);

    if (connect(sock, (sockaddr*)&serv_addr, sizeof(serv_addr))<0) {
        perror("connect server failed");
        return -1;
    }

    std::cout << "Connected to server. Type Message:" << endl;
    std::thread(recv_thread, sock).detach();

    std::string input;
    while (std::getline(std::cin, input)) {
        write(sock, input.c_str(), input.size());
    }

    close(sock);
}

