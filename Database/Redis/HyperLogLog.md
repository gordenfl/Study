# HyperLogLog Type

If a data's type is HyperLogLog, that means the data not only store in the database but also it can be record the unique quantity.

Let's give an Example for that:

```bash
# create a visitors_day1
127.0.0.1:6379> PFADD visitors_day1 user1 user2 user3
(integer) 1

#create visitors_day2
127.0.0.1:6379> PFADD visitors_day2 user3 user4 user5
(integer) 1

# merger two days HyperLogLog to visitors_total
127.0.0.1:6379> PFMERGE visitors_total visitors_day1 visitors_day2
OK

# Count how many data in this key "visitor_total" 
127.0.0.1:6379> PFCOUNT visitors_total
(integer) 5
```

OK, let's analysis the core logic of the HyperLogLog type.

HyperLogLog: 是基于桶来存储数据的,如果一个数据的加入不会导致桶的数量变化返回值就会是0.这就是为什么我们在
```bash
127.0.0.1:6379> PFADD visitors user2 user5
(integer) 0 
```
的时候虽然user2 出现过,但是user5 没有出现过,依然返回的是0. 让我们来分析一下这个bucket是个什么玩意儿.

1. At first, we will get all Hash value of each element
    while we execute "PFADD visitors user5", Redis will get hash value of "user5" (redis use MurmurHash), this hash value is a binary with fixed length. for example: 64bit

    ```scss
        MurmurHash(user5) => "010010100011..." with length of 64 
    ```

2. Bucket values:
    This process logic is put different value into different bucket, which bucket id is the prefix X bits of the hash value such as Hash[:X+1]
    If we have 2**24 buckets, prefix 14 bit of Hash value will be the bucket id. we will put the value into that bucket.

3. Prefix 0:
    later, 64-X bit value will be used to calc the Sparsity(稀疏度).
    we just get the Leading Zeros(LZ), such as:
    
    ```makefile
    Hash[X:64] is "0001011010101..."
    ```

    so the LZ is 3, because it has 3 zero from the beginning. if Prefix 0 is larger,that means the number is more sparse (更加稀疏).

4. Cardinality Estimation Principle 基数估算原理
    if a new Hash value's prefix 0 is larger then the max prefix 0 value. It should update the max cardinality
    if a new Hash value's prefix 0 is smaller or equal the max prefix 0 value, The max cardinality will not be changed.

    only the max prefix 0 value has been changed while we using PFADD. it will return 1 else return 0.
    That's why we PFADD visitors user2 user5, it just return 0.

| 阶段      | 动作                    |
| ------- | --------------------- |
| 元素 → 哈希 | 对元素进行哈希，生成 64 位二进制哈希值 |
| 分桶      | 哈希前 N 位决定元素落在哪个桶      |
| 前导零统计   | 哈希后续位统计连续前导零数         |
| 更新桶     | 如果前导零数比原记录大，则更新       |
| 基数估算    | 汇总所有桶的最大前导零数量，估算基数    |

That's why it sometime we can only get return value 0 while we add new value into the HyperLogLog.
