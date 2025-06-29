# Linux Memory Management

This document will explain how Linux OS manage their memory not only for user space, but also for kernel.

## Core Memory management

1. Virtual memory to Physic memory mapping

2. Alloc of memory and release 

3. Memory protect and 隔离

4. Management of Cache, Page, Swap

### Virtual Memory management

What is Virtual Memory? Each process has it's own address manage and it will have the it's own memory address, we called Virtual Memory.
This Virtual memory need to mapping to an physic memory for each process. So the system need to manage about the memory mapping.

Virtual Memory has been divided to small pages for each memory, on page always be 4Kb (x86-64bits system) or even huge size of that.
Physic memory also be divided into small pages. it called Page Frame.

There is another area called memory table. It managed all the memory page mapping to the virtual memory Table. Virtual memory will only  



[Back to Index](./Basic%20Constructure%20of%20Linux.md)