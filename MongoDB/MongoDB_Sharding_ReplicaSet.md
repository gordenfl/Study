# MongoDB Sharding and Replica Set

## MongoDB Sharding

What's MongoDB Sharding?
Sharding can separate data to difference group then send different group to different Server.
It always used to huge data collection management
Implement Scale-out
Support high concurrent and huge storage application

* sharding with the shard key. There are several way: Range, Hash, Zone-based
* all data distribute to different instance of MongoDB
* Scheduling all different client, with mongos to locate the data
* Provide distribute Storage and Query, promote the Capacity and Performance

All these struct fit for provide large-scale Application such as: Social Network, E-Commercial, Log Platform when the single performance does match requirements.

```sh
            ┌───────────────┐
            │   mongos      │
            └─────┬─────────┘
                  │
     ┌────────────┼─────────────┐
 ┌───▼───┐    ┌───▼───┐    ┌───▼───┐
 │Shard1 │    │Shard2 │    │Shard3 │
 └───────┘    └───────┘    └───────┘
      │           │            │
      │     (Replica Sets)     │
 ┌────────┐  ┌────────┐   ┌────────┐
 │ Config │  │ Config │   │ Config │
 │ Server │  │ Server │   │ Server │
 └────────┘  └────────┘   └────────┘

```

Let's make a Sharding:

1. Shard Node: Each shard alway be a Replica Set
2. Config: at least we need 3 instance to Config
3. Mongo router: this module will accept user's request, then distribute to Shard instance
4. Start Sharding:

    ```shell
    sh.enableSharding("mydb")
    ```

5. Choose Shard from all the Sharding by itself

    ```shell
    sh.shardCollection("mydb.user", { user_id: 1}) # it will 
    ```

### Key Point

1. the Most important is how to design the sharding logic
2. Don't do the transaction in different shards
3. mongos can make some Replica Set itself

## MongoDB Replica Set

MongoDB Replica provide the high availability architecture.

* A group of MongoDB node, one Primary and multi Secondary
* Secondary node Sync data automatically from Primary node.
* System can switch Primary node while old Primary broken, it's called Failover
* Support Read Preference (read from replica), Separate Read and Write.
* Maybe the whole of Replica is a Shard for Sharding.!!!!!

### Step to start an replica

1. Multi-MongoDB instance
    in this case, we just run different instance in one machine:

    ```shell
    mongod --replSet "rs0" --port 20202 --dbpath /data/db1 --bind_ip localhost --fork --logpath /data/db1/mongod.log

    mongod --replSet "rs0" --port 20203 --dbpath /data/db1 --bind_ip localhost --fork --logpath /data/db1/mongod.log

    mongod --replSet "rs0" --port 20204 --dbpath /data/db1 --bind_ip localhost --fork --logpath /data/db1/mongod.log

    mongod --replSet "rs0" --port 20205 --dbpath /data/db1 --bind_ip localhost --fork --logpath /data/db1/mongod.log
    ```

    Value of --replSet must be the same.

2. Connection to the First instance of mongod, initial the Replica Set
    enter the mongo shell:

    ```shell
    mongo --port 20202
    ```

    initial Replica Set with:

    ```shell
        rs.initial(
            {
                _id: "rs0",
                members: [
                    {_id: 0, host: "localhost:20202"},
                    {_id: 1, host: "localhost:20203"},
                    {_id: 2, host: "localhost:20204"},
                    {_id: 3, host: "localhost:20205"},
                ]
            }
        )
    ```

3. Replica Set Status check

    ```shell
    rs.status()
    ```

    you will get, primary node, secondary node, Sync process and heartbeat.

4. Connection to Replica Set

    ```CPP
    mongodb://localhost:20202, localhost:20203, localhost:20204, localhost:20205/?replicaSet=rs0
    ```

    while Primary down, the client can switch to new Primary as well.

### Principle of Replica Set

1. Primary accept all the write request
2. Secondary sync all the data from Primary (Op log + Data copy)
3. If Primary die, System will promote one of Secondary into Primary automatically
4. You can config Read Preference let all the read request send to Secondary

### Hidden Node

It's very important for a system who using MongoDB. Hidden Node can backup all the data from Primary. but it does not provide service outside. It can only be an backup of the Primary.

How can you set a node to Hidden Node

```shell
mongo --port 20202
cfg = rs.conf()
cfg.members[2].priority = 0   # do not in the chosen list, Primary can't set priority to 2
cfg.members[2].hidden = true # Hidden 
rs.reconfig(cfg) $refresh the config

cfg.members[2].slaveDelay = 3600  # default delay 1 hour data 
```
