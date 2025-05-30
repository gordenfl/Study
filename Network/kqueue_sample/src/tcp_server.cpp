
#include "tcp_server.hpp"

#include <iostream>
#include <fcntl.h> 
#include <unistd.h> 
#include "define.hpp"

using std::cout;
using std::endl;

TcpServer::TcpServer() {
    _addr = {};
    _kq = 0;
    _listen_fd = 0;
}

void TcpServer::startServer() {
    if (!init()) {
        return;
    }

    while(true) {
        int nenv = kevent(_kq, nullptr, 0, _evList, MAX_EVENTS, nullptr);
        for (int i = 0; i < nenv; ++i) {
            int fd = _evList[i].ident;

            if (fd == _listen_fd) {// new connection
                if(!new_client()) {
                    continue;
                }
            } else if (_evList[i].filter == EVFILT_READ) {
                recv_client(fd);
            }
        }
    }
}

bool TcpServer::init() {
    _listen_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (_listen_fd < 0) {
        perror("create socket error");
        return false;
    }

    int opt = 1;
    setsockopt(_listen_fd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));

    _addr.sin_family = AF_INET;
    _addr.sin_port = htons(PORT);
    _addr.sin_addr.s_addr = INADDR_ANY;

    if (bind(_listen_fd, (sockaddr*)&_addr, sizeof(_addr)) < 0) {
        perror("socket bind error");
        return false;
    }

    if(listen(_listen_fd, SOMAXCONN) < 0) {
        perror("listen error");
        return false;
    }

    set_nonblocking(_listen_fd);

    // create kqueue
    _kq = kqueue();
    if (_kq == -1) {
        perror("kqueue create error");
        return false;
    }

    struct kevent evSet;
    EV_SET(&evSet, _listen_fd, EVFILT_READ, EV_ADD, 0, 0, nullptr);
    kevent(_kq, &evSet, 1, nullptr, 0, nullptr);

    std::cout << "Server (kqueue) running ...." << endl;
    return true;
}

bool TcpServer::new_client() {
    sockaddr_in cli_addr{};
    socklen_t cli_len = sizeof(cli_addr);
    int client_fd = accept(_listen_fd, (sockaddr *)&cli_addr, &cli_len);
    if (client_fd < 0) {
        return false;
    }

    set_nonblocking(client_fd);
    struct kevent client_ev;
    EV_SET(&client_ev, client_fd, EVFILT_READ, EV_ADD, 0, 0, nullptr);
    kevent(_kq, &client_ev, 1, nullptr, 0, nullptr);

    _clients.insert(client_fd);
    std::cout << "New Client connected fd:" << client_fd << endl;

    return true;
}

void TcpServer::set_nonblocking(int fd) {
    int flag = fcntl(fd, F_GETFL, 0);
    fcntl(fd, F_SETFL, flag|O_NONBLOCK);
}

void TcpServer::recv_client(int fd) {
    char buffer[BUFF_SIZE];
    int len = read(fd, buffer, BUFF_SIZE);
    if (len <= 0) {//client close connection
        std::cout << "Client fd: " << fd << "disconnected" << std::endl;
        close(fd);
        _clients.erase(fd);

        struct kevent ev;
        EV_SET(&ev, fd, EVFILT_READ, EV_DELETE, 0, 0, nullptr);
        kevent(_kq, &ev, 1, nullptr, 0, nullptr);
    } else {
        std::string msg(buffer, len);
        broadcast(msg, fd);
    }
}

void TcpServer::broadcast(std::string& msg, int fd) {
    for (int client_fd: _clients) { 
        if (client_fd != fd) {
            ssize_t sent = write(client_fd, msg.c_str(), msg.size());
            if (sent < 0) {
                perror("send data error");
            }
        }
    }
}