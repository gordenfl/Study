#pragma once

#include "define.hpp"

#include <string>
#include <vector>
#include <set>

#include <netinet/in.h>
#include <sys/socket.h>
#include <sys/event.h>
#include <arpa/inet.h>

class TcpServer{
public:
TcpServer();
void startServer();
bool init();
bool new_client();
void set_nonblocking(int);
void recv_client(int);

void broadcast(int, int);

private:

int _listen_fd, _kq;

struct sockaddr_in _addr;

char _buffer[BUFF_SIZE];
struct kevent _evList[MAX_EVENTS];
size_t _data_size;

std::set<int> _clients;

};