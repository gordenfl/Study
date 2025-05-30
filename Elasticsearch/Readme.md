# Elastic Search 

## What is ES?

Elasticsearch later, we call it ES.
What can ES do? 

* Distribution search and analysis function. It's fit for massive data analysis and search.
* Realtime: the data can be searched while it just write into system.
* Easy to Extend: Horizontal, just add new node, can provide more service ability
* Data model: support complex queries, such as full-text search, aggregation, sorting, filtering
* Integrate with other platform. easy to integrate with other platform such as Logstash, Kibana. It' an ELK Stack with log analysis, monitoring.

## Deep with ES

ES is based on Apache Lucene distribute search engine. it can learn it with several aspect.

1. Core Concept

    * Document: basic unit for the ES, all the data store with JSON, like a line of data table in RDS
    * Index: inverted Index, for search
    * Field: Each document will generate several Field it's a Key pair.

        ```json
        {
            id:XXX,
            title: "this job is good",
            content: "XXXXXXXXXXXXXXXXXXXX,xxxxxxxxxx,xxxxx,x,x,x,xxxx",
            publish_date: "10/10/2022 12:01:11",
            from: "http://www.163.com/news/xxxkskskjfkdkd",
            datetime: "05/01/2025 10:12:32",
        }
        ```

        each attribute of this json is called field.

    * Node: One ES instant in ES cluster
    * Shard: Index will divide into Primary shards, distribute into different nodes. each replica will have the shards.

2. Data Write In (Build Index)

    * Index request sent by client. (eg. HTTP POST request)
    * Distribute each request to target Primary Shard
    * Primary shard will be analysis and generate Word Entries, gen build the inverted index.
    * Primary shard will write into Translog (Data persistence), This will add to in-Memory buffer
    * Automatic refresh the buffer. save all the data to Storage
    * After that, all the data will be sync to replica instance

3. Searching process

    * Receive request sent by Client (eg. GET/index/_search?q=Keyword)
    * manager node will distribute the request to some node
    * node will make search logic then return the result (result include the document and score)
    * manager will collect all the result, merge + order(by score)+ page. after that return it back to client

4. Core Technology

    * invert index : key1, key2, key3 ... => document
    * merge small segment into large segment (what is segment, late we will explain)
    * core logic is in [Lucene](./Lucene.md)

5. Distribute framework

    * each ES service is composed with multi node.
    * each Node will save one or multi segments
    * each Node have the segment are different with other Node
    * One time search, it will cause all the Node's segments to read and search data, return back to master, then return to user.

6. NTR(near Realtime)

    * ES  is almost realtime while you save the data into, you can get the result from searching.
    * ES refresh: ES will make document in the memory change to a searchable segment.
    * ES will refresh data through refresh_interval, how refresh words? below:
        * Document write into the Lucene Cache
        * At the same time, it will write into transLog (transaction, and for recover)
        * Begin refresh, generate a new segment file from the new Document
        * the segment is opened for search, let all the data change to searchable

7. Integrations

    * Logstash: gether all the log from different platform
    * Beats: data collector
