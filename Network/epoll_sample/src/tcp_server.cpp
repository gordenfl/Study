#include "tcp_server.hpp"

#include <errno.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/epoll.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#include <string>
#include <iostream>
#include <set>
using std::string;
using std::set;
using std::cout;
using std::endl;
TcpServer::TcpServer(const string ip, const size_t port) {
    _ip = ip;
    _port = port;
    _addr = {};
}

void TcpServer::set_nonblocking(int fd) {
    int flag = fcntl(fd, F_GETFL, 0);
    fcntl(fd, F_SETFL, flag | O_NONBLOCK);
}
bool TcpServer::init()
{
    _listen_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (_listen_fd < 0) {
        perror("socket create faild");
        return false;
    }

    //address can be reuseable
    int opt = 1;
    setsockopt(_listen_fd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));

    _addr.sin_family = AF_INET;
    _addr.sin_port = htons(_port);
    _addr.sin_addr.s_addr = INADDR_ANY;

    if (bind(_listen_fd, (sockaddr *)&_addr, sizeof(_addr)) < 0) {
        perror("socket bind error");
        return false;
    }

    if (listen(_listen_fd, SOMAXCONN) < 0) {
        perror("listen error");
        return false;
    }

    this->set_nonblocking(_listen_fd);

    _epoll_fd = epoll_create1(0);

    epoll_event ev = {};
    ev.events = EPOLLIN;
    ev.data.fd = _listen_fd;
    epoll_ctl(_epoll_fd, EPOLL_CTL_ADD, _listen_fd, &ev);

    cout << "Chat Server Starting at Port: " << _port << "..."<< endl;
    return true;
}
bool TcpServer::new_client() {
    sockaddr_in cli_addr;
    socklen_t cli_len = sizeof(cli_addr);
    int client_fd = accept(_listen_fd, (sockaddr *)&cli_addr, &cli_len);
    if (client_fd < 0 ) {
        return false;
    }

    set_nonblocking(client_fd);

    epoll_event client_ev = {};
    client_ev.events = EPOLLIN | EPOLLET; 
    client_ev.data.fd = client_fd;
    epoll_ctl(_epoll_fd, EPOLL_CTL_ADD, client_fd, &client_ev);

    _client_fds.insert(client_fd);
    return true;
}

bool TcpServer::start() {
    if (false == init()) {
        return false;
    }

    while (true) {
        int nfds = epoll_wait(_epoll_fd, _events, MAX_EVENTS, -1);
        for (int i = 0; i < nfds; ++i) {
            int fd = _events[i].data.fd;
            if (fd == _listen_fd) {
                if (false  == new_client()) {
                    continue;
                }
                cout << "New Client: " << fd << endl;
            } else {
                recv_client(_events[i]);
            }
        }
    }
    return true;
}

void TcpServer::recv_client(epoll_event &event) {
    _data_size = 0;
    int client_fd = event.data.fd;
    bool closed = false;
    while (true) {
        int n = read(client_fd, _buff+_data_size, BUFF_SIZE-_data_size);
        if (n > 0) {
            _data_size += n;
        } else if (n == 0) {
            closed = true;
            break;
        } else { // n <0, error happend
            if (errno == EAGAIN || errno == EWOULDBLOCK) {
                break;
            }
            closed = true;
            break;
        }
    }

    if (closed == true) {
        cout << "Client " << client_fd << " disconnected. \n" << endl;
        close(client_fd);
        epoll_ctl(_epoll_fd, EPOLL_CTL_DEL, client_fd, nullptr);
        return;
    }

    broadcast(event);
}

void TcpServer::broadcast(epoll_event &event) {
    for (auto client_fd : _client_fds) {
        if (client_fd == event.data.fd) {
            continue;
        }
        write(client_fd, _buff, _data_size);
    }
}