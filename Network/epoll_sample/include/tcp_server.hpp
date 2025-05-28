#include <string>
#include <vector>

#include <netinet/in.h>
#include <sys/socket.h>
#include <sys/epoll.h>

#define MAX_EVENTS  1024*10
class TcpServer {
public:
    TcpServer(const std::string ip, const size_t port);
    void Start();
private:
    std::string _ip;
    size_t _port;
    std::vector<int> _fds;
    struct sockaddr_in addr;
    struct epoll_event ev, events[MAX_EVENTS];
};