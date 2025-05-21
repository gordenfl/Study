# System Design Interview

These Documents are the node for the reading the book of "System Design Interview"

## Include

From the basic concept and include some system design example, step by step from easy to hard. give people a growing up environment.
Hope read this book can bring some upgrade for this ability

## Chapter 01

### General Info

Easy system, to build a system from easy to hard. start from a easy website product's framework.

<img src=image01.avif>

Explain the DNS and HTTP request and response, then rend on the browser include different kinds of device.

Mark the step in the diagram let people know what is the logic flowing.

Add Database into our system to support. What kind of database we need. It's depend what kinds of services we need provide.

1. RDS
    MYSQL, Oracle, PostgreSQL, using database, table, transaction, store procedure etc.

2. NonSQL
    Amazon DynamoDB, MongoDB, Redis, HBase, Neo4j. all these database store data as the key-value store.

RDS can face to the a lot of problem solution. sometime the requirement need low latency and no-structured data need to be manage or just need serialize or un-serializer of data, just using Json, XML, Yaml etc.
If you need store huge data, you can use NoSQL is better to RDS.

### Database Extend

Vertical Scaling vs Horizontal Scaling
Vertical Scaling has a limitation of hardware.
Horizontal Scaling can works for almost every system. then Load balance is best way to using all these.

### Load balance

The load balancer evenly distributes incoming traffic to the web server defined in the load balancing set.

<img src=image02.avif>

## Database replication

Mast and Slaves mode can be used almost MDB, all the data store in the Master, the slaver rsync the data from Master to provide the query service.
All the data insert, update, delete should execute on the master server.

<img src=image03.avif>

一个从库突然挂了,让所有的读写都指向主库,然后立即启动一个新的从库,分担读的任务
如果主库突然挂了,可以马上提升从库为主库,然后让其他从库follow 这个新的主库

TODO: 多主复制,循环复制,可以帮助提升提升从库为主库时候数据丢失问题~~~~~~~

<img src=image04.jpeg>


## 缓存

简言之:临时存储的地方.

解决穿透缓存: 一个网页在加载的时候,直接去问cache, cache要做的工作就是,先看自己这里是否有(布隆过滤器或缓存空值),如果没有就去对应的服务上去抓,抓到以后就放在自己这里,然后返回给访问者.

不仅仅缓存存在的数据,不存在的数据也缓存,这样会进一步的减轻服务器的压力.但是缓存一定要有一个timeout 的属性. 这个解决缓存穿透问题

解决缓存击穿: 当一个数据缓存失效的某一个瞬间,有大量的请求访问这个数据打到服务器上,让服务器挂掉,这样会让服务器挂掉.这个时候每个访问缓存的时候,针对这个值要做一个互斥锁,让互斥锁解决大量的请求同时进入数据库层,而停留在缓存层.当在互斥锁等待超时的时候,依然返回旧数据,这样可以保证系统的高可用.这个问题可以

解决缓存雪崩: 当每个数据在缓存中存在一个Timeout, 有大量的数据在同一个时间Timeout,会导致大量的访问到后台系统,这样会让系统挂掉. 可以让这个缓存的时间在一个范围内随机产生, 热点数据一致不过期,只有当逻辑设置其过期后才过期.

Important Principle:

1. When should we use cache: data was visited frequent but few modify.
2. Timeout Policy: easy to understand
3. Sync Policy: keep the data is the same between cache and application
4. Reduce Fault: skip SPOF (Single Point of Failure). use multi cache server for one cache service. or one cache have limit warning.

5. Eviction strategy(驱逐策略): LRU, LFU strategy with different situation.


## CDN

CND just for the static content distribute with different region, content.
Almost the content is Picture, video, HTML, CSS Javascript.
If some content has hight visit, please generate into the static content, push to CDN. Control it timeout by your own logic.

CDN have geography part, it can make your service have better user experience globally.

<img src=image05.jpeg>

* Factors to Consider: 
    * Cost
    * Cache Time(not too long and not too short) 
    * If the CND has some error, you need find the solution for the request 
    * Invalid the resource or have some version control for each group of resource

## Stateless Web

Move all the status data (Session, tmp user data), move to the whole system. almost store in the NoSQL db. you can add new instance for each part of the server, Loadbalance, CDN.

<img src=image06.jpeg>


## Data Center

manage multi-datacenter, distribute different user with different location, to the data center near by. you can use geoDNS.

all the data center will share one NoSQL database as the session storage.



## Message Queue

Let your system have some async worker. data transfer should use Message Queue. There is a producer and consumer.
it wil reduce the dependency of each module your product. 

<img src=image07.jpeg>

## Log, Automation

Log: is important part, most the error log, you should put all the error log together for manager to see. all the log transfer can using Message Queue.

## Database Extend

as the system extend, the database extend also have two ways:

Vertical: promote the machine's CPU, Disk, Memory,....
Horizontal:user multi-instance running on different physics server to support the service.

1. Data Sharding
The strategy is very important for the Data Sharding:
    * sing an ID mod by the count of server, each server will store the same size of data.
    * Denormalization: it's more complex writing here. you can see the detail from ChatGPT, and several way to let query using less table make data replicate.

# Totally Of This:

Millions user system need to keep extend and change the structure.

* Keep Stateless Web
* Have Redundancy in each level
* Cache data as many as possible
* Support Multi Data center
* CDN Host the static data
* Extend the Data layer with Shading
* Separate Service to multi single service
* Monitoring system data with automation tools





