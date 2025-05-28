#include <iostream>
#include "tcp_server.hpp"
using std::cout;
using std::endl;;
int main() {
    int port = 12345;  // 服务器监听的端口

    // 创建服务器对象，传入监听的端口号
    //ChatServer server(port);

    // 启动服务器
    TcpServer server("127.0.0.1", 8899);
    server.start();

    return 0;
}