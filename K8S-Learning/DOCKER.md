# Docker 相关知识

## Dockerfile 是什么？

1. FROM : 在dockerfile 里面可以定义一个基础镜像
```
FROM ubuntu:20.04
```

2. RUN :安装软件和依赖,例如安装软件包配置系统环境等要执行的命令行
```
RUN apt-get update && apt-get install -y python3
```

3. COPY或ADD :复制文件,指令将本地文件添加到镜像中
```dockerfile
COPY /home/gordenfl/app /app
#这里的COPY命令是将 /home/gordenfl/app 目录 复制到镜像中的/app 根目录下面的app目录
```

4. ENV: 这只环境变量,提供容器运行时候使用
```dockerfile
ENV APP_NAME=product
ENV APP_PORT=8080
```
这样设定以后,程序中可以使用这些环境变量
```Py
import os
name = os.getenv("APP_NAME")
port = os.getenv("APP_PORT")
```
也可以在运行docker的时候 -e 设定这些环境变量
```shell
docker run -e APP_NAME=product -e APP_PORT=8080 your_image
```

5. CMD 或 ENTRYPOINT 指令指定容器启动时候执行的命令
```dockerfile
CMD ["python", "app.py", "arg1", "arg2"]
```
ENTRYPOINT 适用于固定主参数, 如果参数中有修改的部分,可以用CMD来定义.

6. WORKDIR :设定容器的执行目录
```dockerfile
WORKDIR /app
```

7. EXPOSE: 暴露端口, 指令生命容器运行的时候监听的端口
```dockerfile
EXPOSE 80
EXPOSE 443
```

然后执行:
```shell
docker run -p 8080:80 -p 8443:443
```
这是将主机的8080 绑定容器的80端口, 注意的8443绑定容器的443 端口

8. HEALTHCHECK: 定义容器的健康检查机制,可能会用到CMD
```dockerfile
HEALTHCHECK --interval=30s --timeout=10s CMD curl -f http://localhost:8080/health || exit 1
```
这句话定的就是每30秒定义执行一次CMD中的curl命令,因为用了 -f参数表示如果HTTP响应为400或者更高, curl将返回非0 的退出状态码.否则就会执行exit 1 返回1 给外面
一般来说: 
- 退出码0: 表示容器健康
- 退出码1: 表示容器不健康
- 其他非零退出码被定位不确定状态,Docker可能无法正确识别
这里的||exit 1 用来不管curl返回的错误值是什么都按照 1 来返回.只有当curl命令返回0 的时候整条命令才会返回0

9. ONBUILD: 当这个镜像被其他镜像当做FROM的时候
会执行这个指令.比如我写了一个Dockerfile, 里面的FROM 用的是ubuntu:20.04, 当我在执行,我这个Dockerfile去构建一个images的时候, ubuntu:20.04 这个镜像中的ONBUILD就会被执行
<br>

10. USER: 这个设置表示在做CMD的时候以哪个用户作为执行者
<br>

11. RUN: 在构建镜像的时候执行的,CMD会在镜像启动的时候执行
比如你希望在镜像构建的时候安装相对应的软件和fetch一些已经有的第三方库,就需要用到这个指令,这个非常重要,不要轻视他
```dockerfile
RUN apt-get update && apt-get install -y python3
```

12. LABEL: 定义元数据
```dockerfile
LABEL author="gordenfl@gmail.com"
LABEL released="10/10/2023"
```

13. VOLUME: 挂载点,用于持久化数据
```dockerfile
VOLUME ["/app/data"]
```
这个挂载点可以定义多个,这里只会定义挂载点而已,就是在docker instance内部的路径,文件写入的时候具体写在宿主机的什么位置必须要在创建完了instance并且启动的时候通过-v或者--mount参数指定
```shell
docker run -d -v /home/gordenfl/data:/app/data my-image
```
docker instance里写入/app/data的数据,实际上是存放在外部宿主机的/home/gordenfl/data 目录中的

14. ARG 定义构建参数,可以在构件式传入:
```dockerfile
ARG NODE_VERSION=18 
FROM node:${NODE_VERSION}
```
这里设置的ARG的默认值是18 在
```shell
docker build -t my-node-app .
```
他会使用默认值,如果你指定了NODE_VERSION就会使用你指定的值:
```shell
docker build --build-arg NODE_VERSION=20 -t my-node=app .
```
这样就是node:20 了


## Dockerfile写完了我们来使用它

在包含Dockerfile 的目录中执行:
```shell
docker build -t image_name .
```
这样就会在Docker Image中生成一个叫做image_name的镜像,这个镜像构造全部按照目录中的Dockerfile来实现

然后执行:
```shell
docker images
```
来查看镜像是否已经生成.(一般来说没有出错就一定会生成一个叫做 image_name的镜像)
然后我们就可以使用镜像来创建容器了:
```shell
docker run -d -p 8080:80 --name my_image_name image_name
```
-d 代表后台运行daemon
-p 就是前面说的端口映射
--name 就是给这个容器起一个名字
image_name 就是用的前面我们制作好的镜像


## Docker Compose : 多容易编排
一般来说一个Docker 的容易只做一件事情,但是我们很多的项目不仅仅只有一个事情就能完成,比如一个网站没需要网站服务器,需要缓存,需要数据库,需要文件系统,需要接口等等部分,这些部分共同组成了我们这个系统,所以如果我们每一部分都要写一个Dockerfile,这些Dockerfile如何编排,就是一个问题,Docker Compose就是帮我们解决这个问题的.

Docker Compose 主要是通过一个YAML语言的文件来配置的,配置好了以后我们就可以通过这个yml文件一次性生成我们想要的. 他主要解决以下问题:
1. 服务定义: 通过 docker-compose.yml 文件定义多个服务的镜像,环境变量,端口映射,卷挂载,网络配置等等
2. 统一管理: 使用简单的命令,比如 docker-compose up 和 docker-compose down 来启动和停止整个应用栈
3. 环境隔离: 每个compose项目都有独立的网络和卷,避免了不同项目之间的冲突
4. 可移植性: 只要我们写好我们的程序,完全可以确保生产环境和测试环境已经开发环境中的一致性


举个例子 docker-compose.yml
```yml
version: '3.9'
services:
    web:
        build: .
        ports:
            - "8000:8000"
        volumes:
            - .:/code
        depends_on:
            - db
    db:
        image: mysql:5.4
        environment:
            MYSQL_PASSWORD: abcdefg

```
1. 依赖管理
这样的一个compose 文件定义了两个服务 一个是web, 一个是db,每个服务可以指定构建方式,镜像,端口,卷,环境变量等等, 应用级别的项目会更加复杂. 其中 depends_on: 是一个依赖关系,这就可能会产生循环依赖,需要改进,通过 healthcheck: 来取代depends_on:
```yml
  db:
    image: postgres:13
    environment:
      POSTGRES_PASSWORD: example
    healthcheck:
      test: ["CMD", "pg_isready", "-U", "postgres"]
      interval: 10s
      timeout: 5s
      retries: 5 
```
就是在db中执行healthcheck来检查,而不用depends_on来做.

2. 网络配置
当运行docker-compose up 的时候,Docker Compose 会自动创建一个默认的桥接网络,他默认的名字叫做default.
你可以通过一下命令查到网络列表:
```shell
docker network ls
```



