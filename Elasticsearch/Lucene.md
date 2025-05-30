# Lucene Construction and Inner Workings(构造和内部工作原理)

Lucene composed with :

* Document: document is a basic item in search engine. like a line in RDS
* Field: Lucene need to description the document not only use the document content, but also they need the document ID, document public_date, etc. Field, meas type of these data.

    | id | title| content | public_date | from | datetime |
    |----|----|----|----|----|----|

    document is one line in that table, document1, document2 ...

* Index: inverted Index, for search
* Analyzer: will analysis the text based are Tokenization and Normalization
* TokenStream: The result of Stream Participle(分词). Through a group of filter.
* Query: Query item,
* Scorer: make the score of the document and the keyword
* Directory: Storage of the index file. (it can be disk, or memory)
* IndexWriter: Write index, include add, update, delete
* IndexReader/IndexSearch: read the index, search index.

1. How to create Lucene Index

    The core part of Lucene is inverted index. just build word map to document:

    * first step is analysis text and word segmentation(分词)

        * get the fields from the document
        * analyzer will analysis each field of the document
            * Tokenizer: will separate all the words from the document
            * Filter will remote some words, such like: the, a, then, where etc.
        * Finally this step will get Tokens, Positions

    * build inverted index
        * Posting List (倒排表)

            ```css
            term1 → { docID: [position1, position2, ...], docFreq, tf }
            term2 → { docID: [position1, position2, ...], docFreq, tf }
            ```

            it includes Term(词),, DocId, Position, Term Frequency(TF), Document Frequency (DF: means how many document include this word)

            all these info will store in index file. such as: .tim, .doc, .pos, .fdx, .fdt

    * format of the index file
        Lucene store all these index to file system with high efficient way. It use a rate compress way, and block storage way.
        * .tis/.tip index of words 
        * .frq words frequency
        * .prx position of of words
        * .fdx/fdt: document attribute info

        then save all the info to storage or memory with "Directory"

2. Lucene Searching process

    * Analysis query info such as: "java code of the Search Engine"
        it will break into [ java, code, search, engine ]
    * Execute Search
        * IndexSearcher will query all the Index
        * Find all the docID
        * Score each document with algorithm(BM25, TF-IDF).

    * Return the result with the reverse order of Score.

3. Segment in Index
    Segment is a unit part of Index, each index have several Index, because the data will be very huge. It will have a lot of Index, so one file can not store all the Index in the search engine. Index has been divide into small pieces for manage. One of small piece of Index is Segment.

    Each search, all segment will be search, and they will be merge automatic to promote efficient and reduce the disk fragmentation.

Here I give you the flow chart in Chinese, easy to understand.

```css
  [ 文档(Document) ]
        ↓
    [ 分词器(Analyzer) ]
        ↓
  [ 倒排索引(Inverted Index) ]
        ↓
[ 索引文件存储(Directory) ]
        ↓
[ 查询(Query) ]
        ↓
[ 搜索器(IndexSearcher) ]
        ↓
[ 相关性打分(Scorer) ]
        ↓
  [ 排序后的结果 ]

```