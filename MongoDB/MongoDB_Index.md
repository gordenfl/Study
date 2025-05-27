# MongoDB's Index

What is MongoDB Index?
This is for the data search, and promote the efficient of search process.

Like RDS, the index just using B+ tree, and all the data will connected in linked list. if you want to search with some condition, B+ tree can easy to get the result.

How does MongoDB Index working?
MongoDB does not using B+ Tree for the index. it use B Tree to store all the index data.
Each query, mongoDB can find target document in index B-Tree. Don't need to go through all collection.

MongoDB Index: it stores KEY and document's ADDRESS where the document stored.

## Type of Index

1. Single Field Index
    this index just base on only one field:

    ```javascript
    db.mydb.createIndex({username: 1}) //1 means increase order, -1 means decrease order
    db.mydb.createIndex({age: -1})
    ```

2. Composite Index
    this index based on multi-field

    ```javascript
    db.mydb.createIndex({username: 1, age: -1}) 
    ```

3. Unique Index
    this attribute in the document must be identify unique

    ```javascript
    db.mydb.createIndex({ email: 1 }, { unique: True })
    ```

4. Hash Index
    Hash process is performed on the field values, which is suitable for uniform distribution and efficient equal value query. later we will learn deep about the Hash Index

    ```js
        db.mydb.createIndex({address: "hashed"}) 
    ```

5. GEO Index
    support the geography search, such like near by a point.

    ```js
        db.mydb.createIndex({location: "2dsphere"})
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
