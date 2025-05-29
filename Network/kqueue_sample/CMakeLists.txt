cmake_minimum_required(VERSION 3.16)
project(epoll_demo)

set(CMAKE_CXX_STANDARD 17)
include_directories(include)

add_executable(server src/main.cpp src/tcp_server.cpp)
add_executable(client src/tcp_client.cpp)