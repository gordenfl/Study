# Kubernetes 基本知识

## 应用的部署

    1. 直接部署: 抢占资源,互相影响,
    2. 虚拟机部署: 过于繁琐,开销很大
    3. 容器化部署: 通过 容器来实现文件系统,网络,CPU, 内存,磁盘,进程, 用户控件的隔离

## 容器化部署的选择

    1. Docker
    2. Podman
    3. Buildah
    4. CRI-O
    5. LXC/LXD
    6. Rancher
    7. Wasmtime

## 容器的属性

容器的生命周期会很短,通常我们的网络地址会有很大的变化,这样,我们就可以docker中自定义网络,端口映射就可以做到. CPU我们也可以自己完成限制, K8S 让我们的容器很多问题进行修复.

## K8S能做什么

    1. 自我修复:如果发现一个Docker instance 出现问题,可以直接通过docker image 进行修复.
    2. 弹性伸缩: 自动负载调整进行服务的
    3. 自动部署,回滚: 如果我image出现更新,他会自动根据image 把所有宿主机中的docker instance 进行更新,就是删掉之前的docker instance 重新创建
    4. 服务发现和和负载均衡
    5. 极米和配置管理: mysql , tomcat, apache 的配置星系,K8S 能够在一个地方管理他
    6. 存储编排:
    7. 批处理

## 与K8S对应的平台

    1. Apache Mesos : docker 之前就发布了,分布式系统调度,多节点(Linux操作系统), 公国Zookeeper 来使用服务注册, 服务发现功能等等, 他是面向服务器来管理,而不是容器
    2. Docker Swarm : Docker开发的调度框架, Docker Swarm 与Docker 之间有好的服务区控制,但是现在Docker 已经处于停滞状态, Docker 自己也不用了
    3. K8S : Google 之前内部的Borg系统改进,而且开源了发布出来,收到市场的欢迎. 他可以是哟个Label, Pod的概念来讲容器划分成逻辑单元.Pod是协同Co-located容器的集合, 这些容器被共同部署和调度.形成了一个大型的服务.这对于Docker Swarm 和Apache Mesos 有了非常大的改进,和易用性提升.

## K8S 组成部分

    1. K8S 要求最少有一个Master 节点和一个Node 节点才能够正常运行. Master节点可以与Node 节点在同一台物理机
    2. K8S Master 组件
        etcd :
        kube-controller-manager : 所有K8S任务处理的接口都在这里
        cloud-controller-manager:
        kube-scheduler: 
    3. K8S Node 组件
        kubelet
        kube-proxy
        container runtime
    4. K8S 附加组件
        ...
    5. kubectl 命令行,控制台
    6. K8S可视化界面

### 控制面板组件

    1. etcd
    2. kube-apiserver
    3. kube-co
### 节点组件
### 附加组件

## K8S 的分层架构

### 生态系统
### 接口层
### 应用层
### 管理层
### 核心层