#include "tcp_server.hpp"

#include<iostream>
using std::cout;
using std::endl;

int main() {
    cout<< "Hello" << endl;
    TcpServer a;
    a.startServer();
}