cmake_minimum_required(VERSION 3.16)
project(epoll_demo LANGUAGES CXX)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
option(BUILD_SHARED_LIBS "Build shared libraries" OFF)

add_executable(epoll_demo src/main.cpp)
target_compile_features(epoll_demo PRIVATE cxx_std_17)

install(TARGETS epoll_demo)