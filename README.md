## 🔧 1. Programming Languages & Toolchain

### Essential Languages

* **Go / Rust / C#** – Achieve proficiency in at least one: syntax, standard library, concurrency models, and performance tuning.

### Toolchain

* **Build tools** (e.g., Go Modules, Gradle)
* **Debugging** (delve, pprof, perf)
* **Static analysis / Linting tools**
* **Unit testing frameworks / Mocking libraries**

---

## 🧠 2. Computer Science Fundamentals

### Operating Systems

* **Memory management**
* **System calls, context switching, scheduling algorithms**
* **Zero-copy, cache coherence, page cache**

### Computer Networking

* **Nagle’s algorithm**, **congestion control mechanisms**
* **Load balancing**, **HTTP Keep‑Alive**, **persistent connections**

---

## 🏗️ 3. Backend Core Concepts

### Network Communication

* **gRPC**, **GraphQL**

### Caching Systems

* Cache consistency patterns: **Cache-Aside**, **Write-Through**, **Write-Back**

### Message Queues

* **RabbitMQ**, **NATS**
* Asynchronous processing, **burst smoothing**, retry strategies, **ordering guarantees**

### Storage Systems

* **Object storage** (e.g., MinIO)
* **Key-Value storage** (e.g., RocksDB, LevelDB)

### Security & Authentication

* **Data masking**, **audit logging**

---

## ⚙️ 4. High Performance & Distributed Systems

### Concurrency & Asynchronous Programming

* **Go’s goroutine model**, Rust’s **async/await**
* **Compare-and-swap (CAS)**

### High-Concurrency Design

* Connection management, thread models, load balancing
* **Rate limiting** (token bucket, leaky bucket), **circuit breaking**, **graceful degradation**

### Distributed Systems Fundamentals

* Consensus protocols: **Paxos**, **Raft**, **Gossip protocols**
* Distributed transactions: **2‑Phase Commit (2PC)**, **SAGA**, **TCC**
* **Consistent hashing**, service registration & discovery (e.g., **Etcd**)

### Distributed Architecture Practices

* **Service decomposition**, **API Gateway**, **Sidecar architecture** (e.g., Istio)
* Load balancers: **Nginx**, **Envoy**, **HAProxy**

---

## 📊 5. Monitoring & Operations

### Logging Systems

* Log collection: **ELK**, **Loki**
* Structured logging, trace IDs

### Performance Monitoring

* **Prometheus** + **Grafana**, **OpenTelemetry**, **Jaeger**
* Metrics: QPS, response time, GC stats, memory usage

### Operations Automation

* **Docker Compose**, **ArgoCD**

---

## 📦 6. Deployment & Engineering Practices

### Version Control

* Git workflows (**GitFlow**, trunk-based development)
* Branching strategies, Tag/Release management

### Containerization & Deployment

* Image building, configuration management, DevOps pipelines with CI/CD

### Observability & Resilience

* Health checks, circuit breakers, slow‑request profiling, alerting rules

---

## 🧩 7. Domain Modeling & Design Patterns

### Architectural Patterns

* **CQRS**, **Event Sourcing**
* **Clean Architecture**, **Hexagonal (Ports & Adapters) Architecture**

### Coding Best Practices

* **SOLID principles**
* Middleware abstractions, modular design, interface-driven development

---

## 🎮 (Optional) Game Server Development Addendum

* **Space partitioning** (Grid, Quadtree)
* Real-time sync (state sync / command sync)
* **Frame synchronization**, **tick-rate** design
* Data-driven design
* **Frame processor** architecture
