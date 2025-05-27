# MongoDB Aggregation

What is Aggregation?
In MongoDB, Aggregation is a kind of operation for the data, such as transfer, statistic. It is very strong ability for MongoDB. Such like GROUP BY, HAVING, SUM, AVG, JOIN in SQL.

In MongoDB, the Aggregation can :

* GROUP the document, SUM, AVERAGE, COUNT
* Project fields and calculate new fields (what is Project field, late I will tell you)
* Support multi-segment process, make a complex "Data Stream"

## Core Concept of Aggregation Pipeline

MongoDB aggregation based on Pipeline model. It will get the final result through pass the document to different kind of STAGE follow the specific order. e.g: Filter, Group By, Order

* Basic syntax

    ```js
    db.collection.aggregate(
        [
            {stage1}, 
            {stage2}, 
            {stage3}, 
            {....}, 
        ]
    )
    ```

* Common STAGEs

    | Stage         | Function                     | Example                                                                                            |
    | ---------- | ---------------------- | --------------------------------------------------------------------------------------------- |
    | `$match`   | Filter（like `WHERE`）         | `{ $match: { age: { $gte: 18 } } }`                                                           |
    | `$group`   | Group and Aggregate calc（like `GROUP BY`） | `{ $group: { _id: "$city", total: { $sum: 1 } } }`                                            |
    | `$sort`    | Order（like `ORDER BY`）      | `{ $sort: { total: -1 } }`                                                                    |
    | `$project` | Project（Select Field or create new field）         | `{ $project: { name: 1, age: 1, year: { $year: "$birthday" } } }`                             |
    | `$limit`   | limit the result （like `LIMIT`）      | `{ $limit: 10 }`                                                                              |
    | `$skip`    | Skip the count（like `OFFSET`）     | `{ $skip: 5 }`                                                                                |
    | `$lookup`  | Join the table（like SQL `JOIN`）    | `{ $lookup: { from: "orders", localField: "userId", foreignField: "userId", as: "orders" } }` |
    | `$unwind`  | Split Array to multi line              | `{ $unwind: "$tags" }`                                                                        |
    | `$count`   | Statistic Count                   | `{ $count: "total" }`                                                                         |

  * \$match : how to use it:
    $match is like find. it always in the head of pipeline.

    ```js
    {
        $match: {
            <Conditions>
        }
    }
    ```

    Example:

    ```js
    db.users.aggregate(
        [
            {
                $match: { address: "New York"} //search the address is NewYork's records
            }
        ]
    )
    ```

    ```js
    db.users.aggregate([
        {$match: { age: {$gt:30} } } // search age is larger than 30
    ])
    ```

    ```js
    db.users.aggregate([
        {$match: {age: {$gt:20, $lt:40}}} // the age is larger then 20 but less then 40
    ])
    ```

    ```js
    db.user.aggregate([
        {$match: {
            gender: "M", 
            age: {$gt:20, $lt:40}
        }} // male AND age between 20 to 40
    ]) 
    ``` 

    ```js
    db.user.aggregate([
        {$match: {
            $or:{
                gender: "M",
                age: {$gt:20, $lt:40}
            }
        }} // this is using OR condition, means gender is M or age is between 20 and 40
    ])
    ```

    ```js
    db.user.aggregate{[
        {$match: {
            $or: [
                {$and: [{gender:'M'}, {age:{$gt:20, $lt:40}}]},
                {$and: [{gender:'F'}, {age:{$gt:22, $lt:30}}]},
            ]
        }}// this is OR AND composed together to query something.
    ]}
    ```



  * \$sort : how to use it:
    $sort such like ORDER BY in SQL. It can deal with the attribute type include : number, string, datetime, Nested field(嵌套字段, such like: address.city)

    the basic syntax like:

    ```js
    {
        $sort: {<Field1>: <Direction>, <Field2>: <Direction>, ....}
    }
    ```

    About the Direction: 
    * 1 means to up, from small to large
    * -1 is reversed

    Example:

    ```js
    db.users.aggregate([
        {$sort: {age: 1}} // that means sort the data on age from small to large
    ])
    ```

    ```js
    db.users.aggregate([
        {$sort: {age: 1, name: -1}} 
    ])// that means sort the data on age from small to large and name from large to small
    ```

    ```js
    db.users.aggregate([
        {$match: {gender: 'M', age: {$gt: 20} } }, 
        {$sort: {age: 1} }, 
    ])//combine with match and sorted with age from small to large
    
    ```    

  * \$group : how to use it:
    group is help you group all the data get COUNT, SUM, AVERAGE etc. The basic syntax is :

    ```js
    {
        $group: {
            _id: <the key group by>,
            <New Attr>: { <OP>: <Express> },
            <New Attr>: { <OP>: <Express> },
            ...
        }
    }
    ```

    be careful, There is an <OP> here. There are several OP in the $group express. Let's see what are they:

    | OP         | Function                  |
    | ----------- | ------------------- |
    | `$sum`      | Sum（can use to make count with: `$sum: 1`） |
    | `$avg`      | Average                 |
    | `$max`      | Max Value                 |
    | `$min`      | Min Value                 |
    | `$push`     | Collect the field data in this group, it is an array, without unique  |
    | `$addToSet` | Collect the field data in this group, it is an array, unique    |
    | `$first`    | Get First record of this group （the order depend on the pipeline）  |
    | `$last`     | Get Last record of this group          |

    Example:

    ```js
    db.users.aggregate( [
        {
            $group: {
                _id: "$address", //Group by address
                totalUsers: { $sum: 1 } //How many record each address
            }
        }
    ])
    ```

    ```js
    db.users.aggregate (
        [
            $group: {
                _id: "$address", // Group by address
                avgAge: { $avg: "$age"},  // the average age in this group
                maxAge: { $max: "$age"}, // the max age in this group
                minAge: { $min: "$age"}, // the min age in this group
            }
        ]
    )
    ```

    ```js
    db.users.aggregate ( 
        [
            $group: {
                _id: {gender: "$gender", address: "$address"} // group by gender and address
                count: {$sum : 1} //count how many record in this group
            }
        ]
    )
    ```

    ```js
    db.users.aggregate ( 
        [
            $group: {
                _id: {address: "$address"} // group by address     
                name_list: {$push : "$name"} // display all the name in each address
            }
        ]
    )
    ```

  * \$project means to:
    $project such like SELECT A, B, C in SQL

    Assume we have data in document:

    ```js
    { "_id": 1, "name": "Gordon", "age": 44, "score": 80}, 
    { "_id": 2, "name": "Oneqiong", "age": 42, "score": 90}, 
    ```

    we execute this query:

    ```js
        db.user.aggregate(
            [
                {$project: { name: 1, score: 1, _id: 0}}
            ]
        )
    ```

    we will get the result:

    ```js
        {
            {"name": "Gordon", "score": 80},
            {"name": "Oneqiong", "score": 90}
        }
    ```

    There is an other function of $project which is add new attribute:

    ```js
        db.user.aggregate(
            [
                {$project: {name: 1, score: 1, passed: { $gte: ["$score", 60]}}}
            ]
        )
        
    ```

    That means we add new attribute "passed", that logic is to test whether it $score is great or equal to 60, if yes, return True else return False. So we will get the result:

    ```js
        {
            {"name": "Gordon", "score": 80, "passed": true},
            {"name": "Oneqiong", "score": 90, "passed": true}
        }
    ```

  * $unwind means to: extend an array, what is that means? let's see the example

    ```js
        {"_id": 1, "name": "Gordon", "place": ["Novato", "San Rafael", "Irvine"]}
    ```

    if we use $unwind to this document

    ```js
    db.users.aggregate (
        [$unwind: "$place"]
    )
    ```

    it will becomes:

    ```js
        {"_id": 1, "name": "Gordon", "place": "Novato"},
        {"_id": 1, "name": "Gordon", "place": "San Rafael"},
        {"_id": 1, "name": "Gordon", "place": "Irvine"},
    ```

## Summary of Aggregation:

    All the aggregation is what we need make data some change or combine all the data