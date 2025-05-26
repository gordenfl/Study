# TOP K

What is Top-K?
Top-K: is an operation can choose Top k optimize result from a collection according some condition such like score, rate, similarity. The K means how many record you need to get.

## Where to Use Top-K

1. Search engine
    * always search engine will return the result for one search not all the result it has. It just return the top-k value, and the Top-K value is most related with the question.
2. Suggestion System
    * E-commerce system always need the result of some goods have the most related items with the item user watching.
3. Machine Learning/Deep Learning
4. Graph Search, and Path planning

## Way to implement

1. Sort all data and get top k value (O(nlgn))
2. Heap, if heap size < k, push into Heap, if size>=K, pop the top value then push into Heap (O(N lgK))
3. Quick Select(Quick Sort): select one value as the middle value, if left value more than K then keep search in the left side. if left side value is less then K, find K-left_size value in the right side. O(N)
4. Distribute/ Stream logic
    * all the machine get Top-K
    * add all collection together select Top-K
    * it's stream, just using MinHeap
