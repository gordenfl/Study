# C/C++ 中的冷门知识

1.2[a] 与 a[2] 等价

```C
int a[] = {10, 20, 30};
std::cout << 2[a] << std::endl;  // 输出 30
```

2.main 函数可以没有返回值（在某些情况下合法）

```C
int main() {
    std::cout << "Hello\n";
    // 没有 return 0;
}
```

3.使用逗号运算符 ,

```C
int a = (1, 2, 3);  // a = 3
```

4.自增/自减陷阱

```C
int i = 0;
i = i++;  // i 仍然是 0
```

5.sizeof 和数组退化

```C
int a[] = {1, 2, 3, 4};
int* p = a;

sizeof(a);  // 4 * sizeof(int) == 16
sizeof(p);  // 通常是 4 或 8（指针大小），不是数组大小
```

6.函数指针数组

```C
void f1() { std::cout << "f1\n"; }
void f2() { std::cout << "f2\n"; }

void (*funcs[])() = {f1, f2};
funcs[1]();  // 调用 f2
```

7.字符串字面量是 const char*

```C
char* s = "hello";  // ⚠️ C++ 中非法（从 C++11 起）
```

8.true == 1，但 true + true 也合法

```C
bool b = true;
std::cout << b + b << std::endl;  // 输出 2
```

9.逗号与 for 循环

```C
for (int i = 0, j = 10; i < j; i++, j--) {
    std::cout << i << " " << j << "\n";
}
```

10.nullptr 与 NULL

```C
void f(int);
void f(char*);

f(0);       // 调用 f(int)
f(NULL);    // 可能还是 f(int)，因为 NULL 通常是 0
f(nullptr); // 调用 f(char*)，C++11 引入的空指针类型
```

