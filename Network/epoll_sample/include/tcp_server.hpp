#pragma once

#include <string>
#include <vector>
#include <set>

#include <netinet/in.h>
#include <sys/socket.h>
#include <sys/epoll.h>

#define MAX_EVENTS  1024*10
#define BUFF_SIZE   1024*10

class TcpServer {
public:
    TcpServer(const std::string ip, const size_t port);
    bool start();
    bool new_client();
    bool init();
    void set_nonblocking(int);
    void recv_client(epoll_event &event);

    void broadcast(epoll_event &event);

private:
    std::string _ip;
    size_t _port;

    int _listen_fd;
    struct sockaddr_in _addr;
    int _epoll_fd;
    epoll_event _events[MAX_EVENTS];
    char _buff[BUFF_SIZE];
    size_t _data_size;
    std::set<int> _client_fds;
};