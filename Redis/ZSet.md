# ZSet Type

This article just explain how ZSet works. What's the function in programming.

ZSet is a very important data type in Redis. Many ranking system are all using ZSet to implement the function.

## Zset can be used with:

1. Ranking System
    each ZSet can only support one Ranking system, if you want have many Ranking system , please use many ZSet with different attribute with the score

2. Time Order
    using Time with the score make a Time order

3. Order with self defined Weight
    calc score with self define method

4. Deduplication + Order
    ZSet composed with Skip-List, this data struct can easy to find position you want. You can easy to add new score+member into ZSet and keep all the data sorted with score.

5. Page data with Hight efficiency
    ZRANGE & ZRANGEBYSCORE pagesize the data of ZSet.

## ZSet compose

1. Skip List: please see [here](../DataStructure/Skip-List.md)
the skip list order is based on score, each List node include the member data.

2. Hash Table
ZSet is compose not only with SkipList but also include a Hash table. The hash is: member: score, it keeps all members are unique. Except that function, Hash table has another function is identify position member's position in the order.
If there is not Hash Table, if we want to find what is member's order, we need go through all List to find that.
