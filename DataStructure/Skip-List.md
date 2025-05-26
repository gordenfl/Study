# Skip-List

What is Skip-List?
It's a advanced data struct.

Based on Linked List: 

```
|---------------------------------------------------------------------->|
|-------------------------------------------------------------->|------>|
|------------------------------>|------------------------------>|------>|
|-------------->|-------------->|-------------->|-------------->|------>|
|------>|------>|------>|------>|------>|------>|------>|------>|------>|
|       |       |       |       |       |       |       |       |       |
N1->N2->N3->N4->N5->N6->N7->N8->N9->NA->NB->NC->ND->NE->NF->NG->NH->Ni->NJ
```

At first all the node in the list should be ordered. Skip List will have max level const for that. not log(n) level

After that, through the max_level  repeat, the logic can find the node.

For the Time:
Search : Average case: O(log n)
Insert : Average case: O(log n)
Delete : Average case: O(log n)

Space:
each node has store the multi forward pointers, the Space should be O(n)

```py
import random

MAX_LEVEL = 4

class Node:
    def __init__(self, value, level):
        self.value = value
        self.forward = [None] * (level + 1)

class SkipList:
    def __init__(self):
        self.head = Node(None, MAX_LEVEL)
        self.level = 0

    def randomLevel(self):
        lvl = 0
        while random.random() < 0.5 and lvl < MAX_LEVEL:
            lvl += 1
        return lvl

    def search(self, value):
        current = self.head
        for i in reversed(range(self.level + 1)):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
        current = current.forward[0]
        return current and current.value == value

    def insert(self, value):
        update = [None] * (MAX_LEVEL + 1)
        current = self.head
        for i in reversed(range(self.level + 1)):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current

        lvl = self.randomLevel()
        if lvl > self.level:
            for i in range(self.level + 1, lvl + 1):
                update[i] = self.head
            self.level = lvl

        newNode = Node(value, lvl)
        for i in range(lvl + 1):
            newNode.forward[i] = update[i].forward[i]
            update[i].forward[i] = newNode

    def delete(self, value):
        update = [None] * (MAX_LEVEL + 1)
        current = self.head
        for i in reversed(range(self.level + 1)):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current

        target = current.forward[0]
        if target and target.value == value:
            for i in range(self.level + 1):
                if update[i].forward[i] != target:
                    break
                update[i].forward[i] = target.forward[i]
            # Adjust level if needed
            while self.level > 0 and self.head.forward[self.level] is None:
                self.level -= 1
            print(f"Deleted {value}")
        else:
            print(f"Value {value} not found!")

    def display(self):
        print("\nSkip List Levels:")
        for i in reversed(range(self.level + 1)):
            current = self.head.forward[i]
            print(f"Level {i}: ", end="")
            while current:
                print(current.value, end=" -> ")
                current = current.forward[i]
            print("None")

# Example usage
if __name__ == "__main__":
    sl = SkipList()
    for val in [3, 6, 7, 9, 12, 19, 17]:
        sl.insert(val)

    sl.display()

    print("\nDeleting 9...")
    sl.delete(9)
    sl.display()

    print("\nDeleting 3...")
    sl.delete(3)
    sl.display()

    print("\nTrying to delete 20...")
    sl.delete(6)
    sl.display()

```
