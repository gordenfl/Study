# Bloom Filter

What is Bloom Filter?

This is a way to store a lot of boolean value. such like  "oneqiong" is exist in the bloom filter or not?
The common way is to set a dict data = {} then set 'oneqiong' = True, then we test if 'oneqiong' key is in the key or not.
this way needs a lot of memory and disk to finish all the function.

Bloom Filter is help for this. how does it work?

## Bloom Filter size

Each bloom Filter will have a size, the size means how many of the bit this bloom filter will have. Bit not byte.
For example :
    if you need 100,000 bloom filter, you just need 12Kb.
    if you does not use bit, it will take your 100,000 * 28 = 2.8 Mb.

## Hash

Each bloom filter need an hash function to help generate the index of the bits. and Bloom Filter will set this bits into 1.

## Set

Get Hash value from Hash function, it's an index of size. That means there will be some value will have the same value, it is the hash collision, it will cause some result is error, but most of that will be correct.

## Test 'word'

This test is means that whether the 'word' has been set. just using the same hash function to get the index to rest it the bit is 1 or 0, 1 means that value exist. 0 means that value does not exist.

## Code

This code is implement the BloomFilter, it just depend on the library bitarray, bitarray is a library to help set and get the some bit is 1 or 0, help user to test about that.

```py
import hashlib
from bitarray import bitarray

class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size  # 位数组长度
        self.hash_count = hash_count  # 哈希函数数量
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def _hashes(self, item):
        """
        生成 k 个哈希值。
        """
        hash_list = []
        for i in range(self.hash_count):
            hash_result = hashlib.sha256((item + str(i)).encode()).hexdigest()
            hash_int = int(hash_result, 16)
            hash_list.append(hash_int % self.size)
        return hash_list

    def add(self, item):
        """
        添加元素到布隆过滤器。
        """
        for hash_val in self._hashes(item):
            self.bit_array[hash_val] = 1

    def __contains__(self, item):
        """
        检查元素是否在过滤器中。
        """
        return all(self.bit_array[hash_val] for hash_val in self._hashes(item))


# 测试布隆过滤器
bf = BloomFilter(size=5000, hash_count=7)
items = ["apple", "banana", "orange"]
for item in items:
    bf.add(item)

# 检查是否存在
test_items = ["apple", "banana", "grape", "lemon"]
for item in test_items:
    if item in bf:
        print(f"'{item}' might be in the set.")
    else:
        print(f"'{item}' is definitely not in the set.")

```
