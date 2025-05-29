#include <iostream>

#include <thread>
#include <cstring>
#include <unistd.h>

#include <arpa/inet.h>
#include <netinet/in.h>
#include <sys/socket.h>


const char * SERVER_IP = "127.0.0.1";
constexpr int PORT = 8888;
constexpr int MAX_EVENTS = 1024*10;
constexpr int BUFF_SIZE = 1024*10;

using std::cout;
using std::endl;

void receiver_message(int sockfd) {
    char buf[BUFF_SIZE];
    memset(buf, 0, BUFF_SIZE);
    while (true) {
        int len = read(sockfd, buf, BUFF_SIZE-1);
        if (len > 0) {
            buf[len] += '\0';
            std::cout << "[Message]: " << buf << std::flush;
        } else if (len == 0) {
            std::cout << "Server closed connection" << endl;
            close(sockfd);
            exit(0);
        } else {
            perror (" Read error occur");
            break;
        }
    }
}

int main() {
    int sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) {
        perror("socket create error");
        return -1;
    }

    sockaddr_in server_addr{};
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(PORT);

    inet_pton(AF_INET, SERVER_IP, &server_addr.sin_addr);

    if(connect(sockfd, (sockaddr*)&server_addr, sizeof(server_addr)) < 0) {
        perror("create connection error");
        return -1;
    }

    std::cout << "Connected to chat server at " << SERVER_IP << ":" << PORT << endl;
    std::cout << "Type Message and press Enter to send." << endl;

    std::thread receiver(receiver_message, sockfd);
    receiver.detach();

    std::string input;
    while (true) {
        std::getline(std::cin, input);
        if (input == "/quit") {
            break;
        }
        
        input += "\n";

        write(sockfd, input.c_str(), input.size());
    }

    close(sockfd);
    std::cout << "Disconnected!!" << endl;
    return 0;
}