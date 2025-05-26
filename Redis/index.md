# Redis 知识

## 基本概念

Redis :  Remote Dictionary Server 远程字典服务 这是他的名字
单线程模式: Redis 是单线程处理客户端请求, 使用多路复用 epoll 来实现的,如果epoll中出现多个客户端请求,他会将请求放入自己管理的aeEventLoop
        aeEventLoop中封装了epoll. 可以在不同的操作系统上使用不同的I/O多路复用机制

    
## 运行
1. 有两种方式在一个安装了redis的机器上启动,一种是后台启动:
    ```
    brew services start redis
    ```
    另外一种是前台启动,就是你在控制台可以看到输出:
    ```
    /opt/homebrew/opt/redis/bin/redis-server /opt/homebrew/etc/redis.conf
    ```
2. 进入控制台
    ```
    redis-cli #进入命令行
    ```

3. 重启:
    ```
    redis-server /path/to/redis.conf
    ```
## Redis 支持远程连接
在redis.conf中修改
1. 绑定地址, 关掉保护模式
    ```
    bind 0.0.0.0 #绑定IP, 本地IP和远程IP
    protected-mode no #关掉保护模式
    ```
2. 打开认证:
    ```
    # redis.conf
    requirepass your_password
    ```

3. 客户端连接的时候:
    ```
    redis-cli -h your_server_ip -a your_password
    ```

4. 可以使用图形版的客户端
    https://redis.io/ 自己去下载

5. 可以使用Docker 去生成Redis的服务instance,这样更容易维护

## 数据库
Redis 可以支持多个数据库:
    SELECT 0 #这是默认数据库,当你登录上来就是在这个数据库了
    SELECT 1 #切换到数据库1
Redis支持多个逻辑数据库, 默认值是16 (编号:0 ~ 15), 都在内存中.如果你要持久化这个数据库,就
需要shell中执行:
```
dump.rdb
```
所有的逻辑数据库(0~15)都会保存在一个RDB文件中.

一般情况来说,redis只是一个内存数据库缓存,不会存储在文件中,如果你需要将数据保留到文件中的话,可以采用持久化的方法:
1. RDB (Redis Database 快照) 默认是开启的
他会在每个间隔时间自动保存到磁盘, dump.rdb文件中, 在redis.conf里面有配置,
```conf
dbfilename dump.rdb #可以换成其他文件
dir /opt/homebrew/var/db/redis/ #可以换成其他地址
```
2. AOF (Append Only File) 日志文件,可以配置开启, 他默认是关闭的, 你可以打开:
```conf
appendonly yes
appendfsync everysec # 每秒写盘一次

```
所以关于数据库存盘的推荐:
| 配置项       | 是否丢数据       | 推荐情况         |
| --------- | ----------- | ------------ |
| 无持久化      | ✅ 完全丢失      | 仅限缓存、不重要数据   |
| RDB（默认）   | ⚠️ 丢最近几分钟   | 普通场景够用       |
| AOF       | ❌ 最多丢 1 秒以内 | 高可用写入、高可靠性场景 |
| RDB + AOF | ❌✅ 两者结合最安全  | 推荐生产环境开启     |

一个非常重要的: 任何时候redis的数据都不能分开保存,都会只保存在dump.rdb中.

## Redis 管理中的基本命令:
1. 连接管理的命令:
    ```
    AUTH password：进行身份验证。

    PING：测试连接是否仍然有效。

    SELECT index：切换到指定的数据库。

    QUIT：关闭连接。
    ```
2. 服务器管理的命令:
    ```
    INFO：获取服务器信息和统计数据。

    CONFIG GET parameter：获取配置参数的值。

    CONFIG SET parameter value：设置配置参数的值。

    SAVE：同步保存数据到磁盘。

    BGSAVE：异步保存数据到磁盘。,不会卡在命令行

    SHUTDOWN：关闭服务器。
    ```
3. 发布/订阅 命令 (TODO:之后要理解什么是发布,订阅)
    ```
    PUBLISH channel message：向频道发送消息。

    SUBSCRIBE channel：订阅频道。

    UNSUBSCRIBE channel：取消订阅频道。
    ```


## 关于Redis字段类型
| 类型          | 命令示例                   | 用途举例                 |
| ------------ | ---------------------- | -------------------- |
| String      | `SET key value`        | 缓存用户信息、计数器           |
| List        | `LPUSH key value`      | 消息队列、任务队列            |
| Set         | `SADD key value`       | 标签集合、唯一性集合           |
| Hash        | `HSET key field value` | 用户属性（如 user:1\:name） |
| ZSet              | `ZADD key score value` | 排行榜、延迟队列             |
| Stream (TODO)     | `XADD`、`XREAD`         | 日志收集、事件流（Redis 5.0+） |
| Bitmap (TODO)     | `SETBIT`、`GETBIT`      | 用户签到、活跃统计            |
| HyperLogLog(TODO) | `PFADD`、`PFCOUNT`      | 基数估计（去重统计）           |
| GEO (TODO)        | `GEOADD`、`GEORADIUS`   | 地理位置服务（LBS）          |

1. String类型:  
    ```
    SET key value：设置键的字符串值。
    GET key：获取键的值。
    INCR key / DECR key：将键的整数值增加或减少。
    APPEND key value：在键的值后追加字符串。
    MGET key1 key2 ...：获取多个键的值。
    ```
2. List 类型:
    ```
    LPUSH key value：将值插入列表头部。
    RPUSH key value：将值插入列表尾部。
    LPOP key / RPOP key：移除并返回列表的头部或尾部元素。
    LRANGE key start stop：获取列表指定范围的元素。
    LLEN key：获取列表长度。
    ```

3. Set类型:  是一个无序的不重复的字符串集合, 他常用的命令如下:
    ```
    SADD key value1 value2      # 添加元素（可多个）
    SREM key value              # 删除元素
    SISMEMBER key value         # 判断是否存在
    SMEMBERS key                # 获取所有元素
    SCARD key                   # 集合元素个数
    SUNION key1 key2            # 并集
    SINTER key1 key2            # 交集
    SDIFF key1 key2             # 差集
    ```
4. Hash类型:  比如Hash里面可以包含多个Key value 对,但是这个value里面是不能是一个Hash类型的, 就是一般意义上的HashTable,但是不能嵌套而已.
    ```
    HSET key field value：设置哈希表字段的值。
    HGET key field：获取哈希表字段的值。
    HDEL key field：删除哈希表字段。
    HGETALL key：获取哈希表中的所有字段和值。
    HMSET key field1 value1 field2 value2 ...：设置多个字段的值。
    ```

5. ZSet类型: (有序集合/Sorted Set), 这个set中的元素也是唯一的, 但是每一个元素带有一个分数,这个类型会自动按照分数来排序 他的实现看[这里](./ZSet.md)
    添加数据:

    ```bash
    ZADD leaderboard 100 user1 200 user2
    ```

    ```txt
    | Member | Score |
    | ------ | ----- |
    | user1  | 100   |
    | user2  | 200   |
    ```

    正序排列:

    ```bash
    ZRANGE leaderboard 0 -1 WITHSCORES
    ```

    ```txt
    | Member | Score |
    | ------ | ----- |
    | user1  | 100   |
    | user2  | 200   |
    ```

    倒序排列:

    ```bash
    ZREVRANGE leaderboard 0 -1 WITHSCORES
    ```

    | 排名 | 用户    | 分数  |
    | -- | ----- | --- |
    | 1  | user2 | 200 |
    | 2  | user1 | 100 |

6. BitMap类型: 他是通过bit的方式来存储和处理数据,非常适合表示大量二进制状态,比如:是/否, 开/关, 存在/不存在等等
    * 添加Bitmap (SETBIT)

    ```redis
    SETBIT key offset 1
    ```

    key:代表的是bitMap的键
    offset:表示第几位 (可以理解为用户ID或者索引)
    1: 设置为1, 表示存在,或者有效

    ```bash
    SETBIT user:active 12323 1
    ```

    代表ID 为 12323 的user:active 为 1

    * 修改Bitmap (SETBIT)
    和添加一样,只要key值是一样的就能够修改

    ```bash
    SETBIT user:active 12323 0
    ```

    这样就可以将原来设置12323 user:active 的 1 该成 0

    * 删除Bitmap (DEL)
    因为Bitmap只是表示一种状态,有或者无, 那么你要删除有两种意图,就是设置成无,直接用SETBIT 设置成0 就可以了,另外一个,你连整个key都不想要,就用这种方法:

    ```bash
        DEL key
    ```

    * BitCount 统计1的数量

    ```bash
    BITCOUNT key
    ```