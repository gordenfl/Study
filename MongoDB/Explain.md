# Explain

What's Explain? This action let MongoDB to test about your command, give you a result about your command's efficient description. such like 'desc' in MySQL.

## Basic Usage of explain

```js
db.collection.find({age:25}).explain()

db.collection.aggregate([
    {$match: {age:25}},
    {$group: {_id: "$city", count: {$sum: 1} } }
]).explain()
```

* Mode of explain

1. queryPlanner (default): it will give the query plan only
2. executionStates: it will give you statistic info about this query, include document count, time etc. each step
3. allPlansExecution: it will give you all detail info about the query.

```js
db.collection.find({age:25}).explain("executionStats")
```

## Output of Explain

1. Does not have Index. Query will scan all the document

    ```js
    "stage": "COLLSCAN",
    "totalDocsExamined": 100000,
    "nReturned": 5
    ```

2. Query with Index IXSCAN

    ```js
    "stage" : "IXSCAN",
    "indexName": "age_1",
    "totalKeyExamined": 100,
    "totoDocs Examined": 100
    ```

3. Result of allPlansExecution

    ```CPP
    "allPlansExecution": [
        { "plan": {...}, "executionStats": {...} },
        { "plan": {...}, "executionStats": {...}},
        { "plan": {...}, "executionStats": {...}}
    ] //it give us 3 way to execute this SQL, and each one's status.
    ```

    it is very useful for people to optimize the query logic


## The inner logic about explain

1. Generate the execute plan for the Command you send according with the Command you send and the Index you have
2. Execute the Command as "Test Run". It will not faced on all document. It just executed on a few document, until it get the result about this query. After that, the Test Run will stop.
3. Generate the WiningPlan according the tim, document/index etc in the last step.
4. Return the detail info about the explain
(if you choose the executionState mode, MongoDB will execute all the query, then statistic all the result.
 if you choose the queryPlaner mode, MongoDB only analysis. It will not execute any query)
