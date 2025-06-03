# Bitmap 

How Bitmap works? What's the implementation of Bitmap?

## implementation of Bitmap

1. Bitmap is a String in Redis. It's a byte array.
    The max size of this bits array is 512Mb. String is the same.
    each byte is 8bit. So max size Bitmap in logic is 512Mb*8 = 2**32 bit.

2. how to position the bit
    if you give an offset, Redis, will do the next:
    * byte_index = offset/8
    * bit_index = offset%8
    then Redis change the data[byte_index]'s bit_index bit to the value you set 0 or 1

3. Extend the space
    if you give a position is exceed the position this Bitmap has. Redis will extend this bitmap to what you need.

    ```bash
    SetBit mybitmap 1000000 1
    ```

    Redis will auto extend this mybitmap to 1000000+ but all the extend has a limitation of 512Mb

4. BitCount
    Iterating over the byte array, count all the bit's 1 and return the result out.