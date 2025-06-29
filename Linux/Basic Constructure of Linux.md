# Basic Structure of Linux OS

## Basic structure

```
    +----------------------+
    |     应用程序层         | ==> all the app you run is a process running in Application layer
    +----------------------+
    |     系统调用接口       | ==> Linux Core interface <<Unix 环境高级编程>
    +----------------------j
    |       内核空间        | ==> This does not an process, 
    |  +---------------+   | ==> you can see this just one process manage all the thing 
    |  | 进程管理子系统  |   | ==> include: process mgr, memory mgr, file system , network stack, driver
    |  | 内存管理子系统  |   |
    |  | 文件系统       |   |
    |  | 网络协议栈     |   |
    |  | 驱动程序       |   |
    |  +----------------+  |
    +----------------------+
    |      硬件层           |
    +----------------------+
```

| 命令                  | 含义          |
| ------------------- | ----------- |
| `top`               | 查看进程管理      |
| `free`              | 查看内存使用情况    |
| `lsmod`, `modprobe` | 查看/加载模块（驱动） |
| `strace ./a.out`    | 跟踪系统调用      |
| `dmesg`             | 查看内核日志      |


## Process Management

[Process Management](./ProcessManagement.md)

### Memory Management

[Memory Management](./memory_mange.md)

## File System

[File System](./FileSystem.md)

## Networking Stack

[Networking Stack](./NetworkingStack.md)

## Device Drivers

[Device Driver](./DeviceDriver.md)










