# MongoDB's Index

What is MongoDB Index?
This is for the data search, and promote the efficient of search process.

Like RDS, the index just using B+ tree, and all the data will connected in linked list. if you want to search with some condition, B+ tree can easy to get the result.

How does MongoDB Index working?
MongoDB does not using B+ Tree for the index. it use B Tree and other data struct to store all the index data.
Different kinds of index will have different data struct.

MongoDB Index: it stores KEY and document's ADDRESS where the document stored.

## Type of Index

1. Single Field Index
    this index just base on only one field:

    ```javascript
    db.mydb.createIndex({username: 1}) //1 means increase order, -1 means decrease order
    db.mydb.createIndex({age: -1})
    ```

    The basic data struct it use is B-Tree

2. Composite Index
    this index based on multi-field

    ```javascript
    db.mydb.createIndex({username: 1, age: -1}) 
    ```

    The basic data struct it use is B-Tree as well

3. Unique Index
    this attribute in the document must be identify unique

    ```javascript
    db.mydb.createIndex({ email: 1 }, { unique: True })
    ```

    The basic data struct it use is B-Tree as well

4. Hash Index
    Hash process is performed on the field values, which is suitable for uniform distribution and efficient equal value query. later we will learn deep about the Hash Index

    ```js
        db.mydb.createIndex({address: "hashed"}) 
    ```

    The basic data struct it use is Hash Table

5. GEO Index
    support the geography search, such like near by a point.

    ```js
        db.mydb.createIndex({location: "2d"})
        db.mydb.createIndex({location: "2dsphere"})
    ```

    2d index use data struct is grid-based B Tree. map the position (x, y) in to a grid panel, suck like B Tree node
    2dsphere index use GeoJSON coordinate. Make the map struct inside. The search method just using spherical geometry

6. TTL Index (Time-To-Live Index)
    TTL means time to live. This index only on the some attribute with Time. and if the time is timeout, the document will be delete automatically
    * Automatic clear timeout data
    * shrimp the space
    * always using on the session, log, cache etc.

    ```CPP
    db.sessions.createIndex(
        {createdAt: 1}, // the index value will be 1 at the data add to document
        {expireAfterSeconds: 3600} // the data will be delete while the data has stay in the document over the 3600 second time.
    )
    ```

    TTL Index also using B-Tree as the basic data struct.

7. Partial Index

    Easy to understand, this kind of index only build on the document fit for the requirement

    ```CPP
    db.users.createIndex(
        {age: 1},
        {partitalFilterExpression: {age: {$gle:18}}}
    ) // this Index only build on the data  age large or equal 18 in the document of users 
    ```

    It always using B-Tree as the basic data struct.

    additionally, this partial index alway used with TTL Index, to keep TTL data will be index not all the data be index

    ```CPP
    db.sessions.createIndex({
        {lastActiveAt: 1},
        {
            expireAfterSeconds:3600,
            partialFilterExpression: {isActive: true}
        }
    }) // only the data will exist 1 hours of isActive is True sessions
    // if the isActive does not true, it will not be delete
    ```

## Use Index and Optimize

1. View Collection's Index

    ```js
    db.mydb.getIndexes()
    ```

2. Delete

    ```js
    db.mydb.dropIndex("indexname")
    ```

3. Force to use index while in Find

    ```js
    db.mydb.find({age: 13}).hint({age: 1})
    // find({age: 13}) is search the data which age equal 13
    // and hint is force mongodb to use the age's increase index
    ```

4. Choose Index and covered Query
    Covered Query means return the field of query not return whole document. Because if you need the other field in the document, MongoDB need to load whole collection then get it.

    ```js
    db.mydb.createIndex({username: 1, email: 1})
    db.mydb.find({ username: "gordon"}, { username: 1, email: 1, _id: 0}) //TODO:what does _id:0 means to?
    ```

## Notice about Index

1. if you have a lot of index, when you add or delete or udpate data, it will bring a lot of cost.
2. multi-index order: such as {username: 1, age: -1} or {age: -1, username: 1, }
3. Big index will occupy more memory, it will bring negative effect.
4. Avoid "index failed": the query conditions do not match the index design. The index will not be used. bring low efficient.

## Hash Index

Hash Index is an single field index. This index will hash this value of this filed. put the Hash Value in the B Tree. This B Tree can only support the  equal compare.

| Feature         | Introduce                       |
| ---------- | ------------------------ |
| 🌟 Hash distribute     | Index value is Hash value, so It is average distribution|
| 🔍 Only support equal Search  | `find({ field: value })` |
| ❌ No Range Query  | Can not using `$gt`、`$lt` etc.       |
| 🚀 Promote Average Overload | reduce one point overload                |
| 📏 Only one Field   | Only can build on one field               |


## Under layer

1. MurmurHash to get Hash value
2. index value with hash value  point to the document address
3. Hash index using B tree
