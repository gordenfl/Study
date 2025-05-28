#include "tcp_server.hpp"

#include<string>
using std::string;
TcpServer::TcpServer(const string ip, const size_t port) {
    _ip = ip;
    _port = port;
}

void TcpServer::Start() {
    //int socket


}