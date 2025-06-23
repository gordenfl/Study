# Server/Back-end engineer knowledge checklist

---

## 🔧 1. Programming Languages & Toolchain

### Essential Languages

* **Go**, **Rust**, **Java**, **Python**, **C#**, **Node.js** (choose based on stack): Master at least one language’s syntax, standard library, concurrency model, and performance tuning.

### Toolchain

* **Build tools** (e.g., Make, Go Modules, Gradle, CMake)
* **Debuggers** (gdb, delve), **profilers** (pprof, perf)
* **Static analysis / Lint tools**
* **Unit testing frameworks / Mocking libraries**

---

## 🧠 2. Computer Science Fundamentals

### Data Structures & Algorithms

* Common structures: arrays, linked lists, stacks, queues, hash tables, skip lists, heaps, trees, graphs
* Algorithms: sorting, searching, dynamic programming, graph algorithms, greedy strategies
* Practical systems: LRU cache, inverted indices, Top‑K algorithms, Bloom filters

### Operating Systems

* Processes vs threads, memory management, file systems, I/O models (epoll/kqueue)
* System calls, context switching, deadlocks, scheduling algorithms
* mmap, zero-copy techniques, cache coherence, page cache

### Networking

* Protocols: TCP / UDP / QUIC / HTTP/HTTPS / WebSocket
* TCP handshake & teardown, Nagle’s algorithm, congestion control
* DNS, CDN, load balancing, Keep‑Alive, long-lived connections
* Socket programming, connection pooling, protocol serialization (e.g., Protobuf)

---

## 🏗️ 3. Backend Core Concepts

### Network Communication

* RESTful API design, gRPC, WebSocket, GraphQL
* Multi-protocol support (TCP/UDP/HTTP), cross-language encoding (e.g., Protobuf)

### Databases

* Relational: MySQL, PostgreSQL (transactions, indexing, query tuning, lock mechanisms)
* NoSQL: Redis, MongoDB, Cassandra
* Schema design, normalization, horizontal scaling (sharding), middleware (e.g., Sharding‑JDBC, TiDB)

### Caching Systems

* Advanced Redis: ZSet, Bitmap, HyperLogLog, Lua scripting, pipelining
* Cache coherence patterns: Cache-Aside, Write-Through, Write-Back
* Cache issues: stampede, avalanche, penetration

### Message Queues

* Kafka, RabbitMQ, NATS, Redis Streams
* Asynchronous processing, burst handling, retry policies, ordering guarantees

### Storage Systems

* Object Storage: MinIO, Amazon S3
* File systems, block storage, embedded KV stores: RocksDB, LevelDB

### Security & Authentication

* HTTPS/TLS, JWT, OAuth2, encryption/decryption
* Data masking, role-based access control (RBAC), audit/audit logs

---

## ⚙️ 4. High Performance & Distributed Systems

### Concurrency & Async Programming

* Go’s goroutines, Java thread pools, Rust’s async/await
* Locking primitives: mutexes, CAS (compare-and-swap), spinlocks, read-write locks, semaphores

### High-Concurrency Architecture

* Connection/thread management, load distribution
* Rate limiting (token bucket, leaky bucket), circuit breakers, graceful degradation

### Distributed Systems Fundamentals

* CAP theorem, consensus protocols: Paxos, Raft, Gossip
* Distributed transactions: Two-Phase Commit (2PC), SAGA, TCC
* Consistent hashing, service discovery: Zookeeper, Etcd

### Distributed Architecture Patterns

* Monolith vs microservices
* API Gateway, sidecar pattern (e.g., Istio)
* Layer 4/7 load balancers: Nginx, Envoy, HAProxy

---

## 📊 5. Monitoring & Operations

### Logging

* Log aggregation: ELK stack, Loki
* Structured logging, JSON format, trace IDs

### Metrics & Observability

* Prometheus + Grafana, OpenTelemetry, Jaeger (distributed tracing)
* Core metrics: QPS, latency, GC, memory usage

### DevOps & Automation

* Container platforms: Docker, Docker Compose, Kubernetes (K8s)
* CI/CD tools: Jenkins, GitHub Actions, ArgoCD

---

## 📦 6. Deployment & Engineering Practices

### Version Control

* Git workflows: GitFlow, trunk-based development
* Branch/tags/releases management

### Containers & Deployment

* Image building, config management, environment separation
* CI/CD pipelines, test automation, deployment automation

### Resilience & Observability

* Health probes, circuit breaker patterns, slow-request profiling, alerting/monitoring rules

---

## 🧩 7. Domain Modeling & Design Patterns

### Architectural Styles

* DDD (Domain-Driven Design)
* CQRS, Event Sourcing
* Clean Architecture, Hexagonal (Ports & Adapters) Architecture

### Coding Best Practices

* SOLID principles, classic design patterns (Factory, Strategy, Observer, etc.)
* Middleware abstraction, modular design, interface-driven code

---

## 🎮 (Optional) Game Server Development Addendum

* AOI (Area of Interest) systems, spatial partitioning (e.g., Grid, Quadtree)
* Real-time sync models: state-sync, command-sync
* UDP networking, frame sync, tick-rate management
* Scripting support (Lua, Python), data-driven architecture
* Scene management, finite state machines, frame processor design

