# Amazon System Design Prepare

## unknown knowledge points

1. N-Tiered Architecture
    layer by layer. such like MyBank.NET: Presentation Layer(表现层), Business layer(业务逻辑层), Data Access Layer(数据层), Integration Layer(集成层).
    Best part:
    * Reduce the dependence of each layer.
    * Decoupling: each layer does not dependency.
    * Extension: easy for the extension for each layer
    * Maintainable: easy to maintain, upgrade etc.

2. SOA Architecture
    like microservice, but all the module are separated like microservice but it has more function and logic in each module. it will based on the same technology, not like microservice can using different tech stack. each service can be developed and deployed itself.
    Different program language platform can transfer data each other with interface.
    Alway one Sub System can be independent. not one function. it's different with microservice.

    shortcoming:缺点
    How to deal with the Transactions with different modules
    How to deal with error and service found.
    As the module become more and more, It will become complex of version control, dependency etc.

3. Microservice
    for free, each service separated can have itself tech stack. implement by itself. does not have dependency with other microservice, provide the sRPC, HTTP, TCP interface to transfer data each other.
    the most loose dependency for the system design.

    It's most low dependency structure of a huge product. Easy to extend, and add new function. it can support different tech stack. each small function can be a microservice.

    对于一个大功能中的每一个部分都可以做一个微服务来实现,这些微服务之间的通信可以用数据库,kafka, tcp, gRPC 等方法.


## schedule process management  调度过程管理

1. Distributed Schedule
    Composed with Components. all the Components are distributed. Composed with distribute, execute, monitoring and failure deal logic.
    Always it's managed by (Kubernetes CronJob), or (Amazon CloudWatch Event + Lambda function).

2. Priority manage
    Different kinds of task will have different priority to deal with. Always using Kafka and AWS SQS to deal with.
    Periodic tasks can be managed by the CronJobs

3. Task Priority Strategy
    Resource limitation management
    Error Tolerance: retry count, max retry-count, interval management.
    Task dependency management

4. Resource management:
    K8S to management the resource, keep all the execute high efficiency.
    AWS EKS, ECS, to management resource according the performance.

5. Monitoring and Warning
    Use AWS CloudWatch
    Collect all the result of execute in distribute system together then make a error report.

6. Retry policy
    Different kinds of retry logic for different kinds of task.
    Warning the error while all error occur after the retry.
    CI/CD import auto rollback the logic to previous version
    Database backup and recover

## Interview Process

1. make sure all the requirements with detail
2. Structure of whole System
3. Data Structure
4. API (REST: GET, POST, PUT, DELETE)
5. Structure of System (diagram: microservice, include each function and DB, LB etc.)