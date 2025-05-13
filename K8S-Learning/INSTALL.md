# How to Install Minikube in Mac OS

```
brew install minikube
minikube start --driver=docker
```

virtualbox：使用 VirtualBox 虚拟机。
hyperkit：macOS 上的轻量级虚拟化工具。
hyperv：Windows 上的 Hyper-V 虚拟化平台。
kvm2：Linux 上的 KVM 虚拟化。
none：直接在主机上安装 Kubernetes 组件（通常用于 Linux）。
都可以是用，只是我们现在选择的是docker 所以 --driver=docker