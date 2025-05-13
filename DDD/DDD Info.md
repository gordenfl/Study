# Domain-Drive Design
首先这是我第一次听说这种面试,感觉自己之前很SB

基础的知识包括:
    基本知识: 负载均衡, 缓存,数据库, CAP, 分布式一致性, 容灾
        关于:
            数据系统的基础方面: 可靠性,可维护性,可伸缩性, 数据模型和查询语言
            数据存储引擎的内部,研究数据库如何在磁盘上摆放数据库,存储引擎对于负载进行优化的方法
            几种数据编码进行比较,

    游戏后端对于:
        AOI, 状态同步,选择TCP/UDP协议的标准,游戏匹配, 可扩展房间服务器架构方面



## 首先知道什么是 Domain-Driven Design
```
┌───────────────────────┐
│    Presentation Layer │  ← 用户接口（如 API、CLI）
└────────▲──────────────┘
         │
┌────────┴──────────────┐
│  Application Layer    │  ← 协调任务流，不含业务逻辑
└────────▲──────────────┘
         │
┌────────┴──────────────┐
│      Domain Layer     │  ← 核心业务模型和规则（Entity、VO、Service、Aggregate）
└────────▲──────────────┘
         │
┌────────┴──────────────┐
│  Infrastructure Layer │  ← 数据库、网络、文件、第三方服务等技术细节
└───────────────────────┘
```


## 我所理解的DDD (domain driven design)

1. 数据类型分为DAO, DTO, 
    DAO: 是用来作为数据库存储的对象,在数据库存储使用
    DTO: 是用来作为数据传递时候的对象,在Application 逻辑参数的一种类型
2. 接口直接调用Application中定义的 Service 类型来进入逻辑
3. Application 的每个逻辑需要的参数就是前面说的DTO, 拿到DTO后,这里的Application 调用Domain中的数据类型,进行逻辑,如果Application中有各种复杂的逻辑,可以在此完成
4. Domain: 定义的是纯粹的物理模型,一个一个的class, 并不包含任何数据库或者其他依赖的,保持完整独立
5. infrastructure 才是最终实现读写文件,读取,写入数据库的操作

## 我们在看看在游戏设计中如何使用DDD

1. Domain 实体: Entity, Scene, Monster, Player, Item, Skill, Quest, Task, Domain是可以独立存在的不依赖任何东西
2. Presentation Layer  就是给一个简单的接口,协议调用的接口,就是过去的c_XXXXXX s_XXXXXX 函数的调用,这部分是放在服务器引擎中C去实现的,所以每个module在游戏中都是有一个init的函数去绑定协议.
3. Application: 实现实际的游戏逻辑, 包括实体之间的互相复杂的逻辑放在这里, 这里的逻辑需要用到Domain的实体,和一些infrastructure 提供的接口(用于存盘, 数据库,网络等等)
4. infrastructure: 就是实现Application中需要完成对Domain和Application结果与外部,比如数据库,磁盘,网络等行为都放在这里实现,提供统一的接口给Application
我靠这不就是我们之前做游戏时候的框架么?

## 大话3 我理解的
UserObj, Item, Grocery, Scene, 等等都是Domain.
AOI, Fight, NpcChat, NpcMenu, Task, 副本, 等等都是Application.
引擎中的网络,写盘, 计费那边的接口, 等等都是 Infrastructure.

引擎中的网络部分不会主动调用Presentation, 这部分的逻辑,比如客户端发来的消息,需要服务器端处理,这个时候infrastructure 收到网络包,是通过之前已经初始化好的回调函数去让Presentation layer去处理代码

说白了DDD就是大话3服务器端引擎的工作原理.


