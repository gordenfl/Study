# Mongodb Index deep

## How many type of Index MongoDb has?

1. Single Field Index
2. Composite Index
3. Unique Index
4. Hash Index
5. GEO Index
6. TTL Index
7. Partial Index

## How to implement these indexes

1. Single Field Index & Composite Index & Unique Index & TTL Index (Time to live index, 过时间删除)
    It just using B+ tree, all the leaves are sorted store in a double link list. and Each leaves point to an json PATH, while FIND need return all teh data, from leaves to find the whole of data in JSON collections.

2. Hash Index
    It just using Hash Battle to implement the Hash value to record

    * Hash function: MongoDB using Hash function calc the HASH value
    * according the HASH value decide the Hash bottle ID
    * each HASH value point to the resource position

3. GEO Index
    It just using two ways to implement it. 2D index and 2d sphere implement all about that.
    MongoDB using sphere index to make module of the ball , then do some calc according the sphere

4. TTL Index
    It all using B+ Tree implement, but the while the leaves are expired, the leaves will remove from the b+ tree, it's called lazy deletion. so TTL also need to according the time period to find the record through B+ tree, then delete all the node's data.
    MonboDB has a command called:

    ```shell
    compact
    ```

    It can shrink the space of all the index. remove all the leaves has already useless.

