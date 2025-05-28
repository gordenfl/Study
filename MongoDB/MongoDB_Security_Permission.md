# MongoDB Security

There are several Security Functions in MongoDB:

1. Authentication
    Use the User Authentication with  SHA-1/SHA-256, LDAP, x509 Cert, Kerberos.

    With SHA-X user's password+SALT will get the Hash value, compare with User's Hash Value in Database to make the Authentication.
    SALT is a random value while create user generated.

    Default MongoDB does not have Authentication step, you need to initial that:

    ```shell
    use admin
    db.createUser(
        {
            user: "admin"
            pwd: "password of admin",
            roles:[ {role: "root", db: "admin"}] #here we give root a role of root, there are different role defined in MongoDb, I will list below.
        }
    )
    ```

    You can initial authentication using:

    ```shell
    mongod --auth --bind_ip x.x.x.x
    ```

    or set in the config file:

    ```shell
    security:
        authorization: enable
    ```

    for the LDAP, x509 Cert, Kerberos, it's all the Enterprise Authentication method. Here I will not give more detail description.

2. Authorization
    Different User will have different permission according it's role, these are the role of in the MongoDB:

    * 📘 数据库用户角色（Database User Roles）

        | 角色名      | 作用域       | 描述                                       |
        |-------------|--------------|--------------------------------------------|
        | read        | 指定数据库   | 允许只读访问数据库。包括集合查询和索引查看。|
        | readWrite   | 指定数据库   | 允许对数据库进行读写操作。                |

        ---

    * *🛠 数据库管理角色（Database Administration Roles）

        | 角色名      | 作用域       | 描述                                             |
        |-------------|--------------|--------------------------------------------------|
        | dbAdmin     | 指定数据库   | 管理数据库，如索引、统计、查看模式等。         |
        | dbOwner     | 指定数据库   | 拥有对数据库的完全控制权限（包括管理用户和角色）。|
        | userAdmin   | 指定数据库   | 管理当前数据库的用户和角色，不包括数据访问权限。|

        ---

    * 🌐 集群管理角色（Cluster Administration Roles）

        | 角色名          | 作用域     | 描述                                                       |
        |------------------|------------|------------------------------------------------------------|
        | clusterAdmin      | admin 库   | 拥有对整个集群的管理权限。                                |
        | clusterManager    | admin 库   | 管理和监控集群，但不能设置安全策略或管理用户。            |
        | clusterMonitor    | admin 库   | 查看集群状态和性能监控信息。                              |
        | hostManager       | admin 库   | 执行服务器相关的管理操作，如查看日志、诊断。              |

        ---

    * 🔄 备份与恢复角色（Backup and Restore Roles）

        | 角色名     | 作用域     | 描述                                                      |
        |------------|------------|-----------------------------------------------------------|
        | backup     | admin 库   | 允许执行备份操作，包括读取所有数据库及其元数据。          |
        | restore    | admin 库   | 允许将数据恢复到数据库中，包括插入集合、索引等。          |

        ---

    * 🔐 用户管理角色（User Administration Roles）

        | 角色名                | 作用域     | 描述                                                  |
        |------------------------|------------|-------------------------------------------------------|
        | userAdminAnyDatabase   | admin 库   | 管理任意数据库的用户和角色。                         |
        | readAnyDatabase        | admin 库   | 只读访问所有数据库。                                 |
        | readWriteAnyDatabase   | admin 库   | 对所有数据库有读写权限。                             |
        | dbAdminAnyDatabase     | admin 库   | 管理所有数据库（不含读写权限）。                     |
        | root                   | admin 库   | 拥有所有权限，包括对所有数据库和操作的完全控制。     |

        ---

    * ⚙️ 内部系统角色（Internal System Roles）

        > ⚠️ 这些角色仅供 MongoDB 系统内部使用，不应直接赋予用户。

        | 角色名     | 作用域     | 描述                                               |
        |------------|------------|----------------------------------------------------|
        | __system   | 所有数据库 | 内部使用角色，MongoDB 启动和系统任务使用。        |
        | __backup   | admin 库   | 内部备份流程使用。                                |
        | __restore  | admin 库   | 内部恢复流程使用。                                |

3. TLS/SSL transportation
    Why?
    Communication with Client and Server will be attach. sometime the data will be stolen. How can we avoid that happen?
    TLS and SSL can help us to achieve that.MongoDb support Self Signed Certification. You can generate CA with follow step

    * Generate Root CA

        ```bash
            openssl genrsa -out ca.key 4096
            openssl req -x509 -new -nodes -key ca.key -sha256 -days 365 -out ca.crt
        ```

    * Generate Server Private key and CSR(Certification Request)

        ```shell
        openssl genrsa -out mongo.key 4096
        openssl req -new -key mongo.key -out mongo.csr
        ```

    * Issue a server certificate with CA

        ```shell
        openssl x509 -req -in mongo.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out mongo.crt -days 365 -sha256
        ```

    * Merge Certificate file and private key into a PEM file (because MongoDB need PEM). If you want Two-way authentication, Client should do the same thing.

        ```shell
        cat mongo.key mongo.crt > mongo.pem
        ```

    * Open TLS/SSL Config
        Modify MongoDB Config file (mongod.conf) or add into startup command:

        ```yaml
        net:
            tls:
                mode: requireTLS     #This part maybe requireTLS/allowTLS/preferTLS/disabled
                certificateKeyFile: /path/to/mongo.pem
                CAFile: /path/to/ca.crt
                allowConnectionsWithoutCertificates: false
        ```

        or in the command line:

        ```shell
        mongod --tlsMode requireTLS \
            --tlsCertificateKeyFile /path/to/mongo.pem \
            --tlsCAFile /path/to/ca.crt
        ```

    * Client connection
        Client (mongo shell or driver), must use TLS/SSL to connection:

        ```shell
        mongo --host your.mongodb.host \
            --tls \
            --tlsCAFile /path/to/ca.crt \
            --tlsCertificateKeyFile /path/to/client.pem \
            --tlsAllowInvalidHostnames  # (Test Env only)
        ```

4. Encrypted Storage (At Rest)静态

    | Encrypted Type                                   | Instruction                              |
    | -------------------------------------- | ------------------------------- |
    | **Encrypted Storage Engine**     | Data in disk encrypt  |
    | **Field Level Encryption, FLE** | client send data to server, server only storage, does not know what the data means to, client read it then decrypt |
    | **Backup Encrypt**                               |  Encrypt the backup data         |

    * MongoDB enterprise version has WriedTiger engine support Storage encrypt
    * AES-256 Encrypt, Manage all the key with Master Key
    * Key management with integration KMIP : Key management interoperability protocol
    * storage encrypt transparent for up layer

5. Network Permission Control
    IP white list control and network control.
    MongoDB have the IP white list define
  
    and you can also using Linux iptable to control the network permission

    ```yaml
    net:
        bindIp: 127.0.0.1,192.168.1.100,10.0.0.5
    ```

    or when mongod start:

    ```shell
    mongod --bind_ip 127.0.0.1,192.168.1.100,10.0.0.5
    ```

    avoid to use 0.0.0.0 , except all the control under the firewall.

6. Audit Logging
    It's on the MongoDB Enterprise version. when mongodb start, some argument can be set to open this function:

    ```shell
    mongod --audioDestination file --auditFormat JSON --auditPath /var/log/mongo_audio.log
    ```

    with this function you can filter some log and only log the key event such like authCheck, createCollection, dropCollection createIndex, dropIndex, insert, update, delete, addUser, removeUser, updateUser, grantRole, revokeRole etc.
