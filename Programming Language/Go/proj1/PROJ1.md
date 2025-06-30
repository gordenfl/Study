# Proj1 project

this project include all basic function include syntax and function basic information.

## How does Go run.

Go is not a script language. It's compiled language such like C, C++, Fortran, C#, Java. But it's different with Java and C#, all Java and C# code will compile and generate bytecode, then the bytecode running on the Language Virtual Machine. So C# and Java does not the pure Compiled language absolutely.

OK, As the C, C++, Fortran, If you want to run the code you write, you need to compile the code and link them together generate a binary executable file. then run that executable file, you can run the logic what you write.

How does Go code became the executable file:

1. First step --- Analysis code and generate AST(Abstract Syntax Tree), then this AST will convert to inner node struct for the next step. (If you want know more detail about the node struct. TODO: here, we can learn more detail).
2. Middle step --- SSA IR (Single Static Assignment). From the node last step generated, compiler will transfer all the Node into SSA, all these binary code all the cross platforms. SSA step make some optimize such like (const, remove the dead code).
3. Last step --- Generate machine code from the SSA which generated last step. Go just generate all machine code directly without middle file such like: .o (C++). All these files are all in the memory not write into disk.
4. Compile and Link --- The machine code will be passed to inner compiler(汇编器), then Go linker(链接器) will static linked all the dependency together such like: Go runtime, GC(garbage collection). At last it will generate executable file.
5. In Go you can using "go build" to generate executable file locally(default name is directory name current or you can Specifying a filename with -o), using "go install" you can install the executable file into $GOBIN folder, for the global call

```txt
.go 源文件
     ↓ 语法分析 → AST
                   ↓
              AST → Node（Middle Data）
                   ↓
              Node → SSA IR → SSA (Optimization)
                   ↓
             SSA → (Machine code for different platform)
                   ↓
             Compile & Link → Executable Files
```

```shell
go -c functions.f90     # generate functions.o 和 functions.mod
go -save-temps -c main.f90  # generate main.mod、main.o、main.fi（if there are some preprocessing[预处理]）、main.s
go main.o functions.o -o program  # link and output program
```

## Go and Dynamic Library

Does Go support shared library? the answer is : YES but it's only called by C
You can use ```-buildmode=c-shared``` or ```-buildmode=c-archive``` this arguments will let Go to generate shared library only for C. and It will generate the ```.h``` and ```.so```

Go does not have dynamic library. 

## Plugin in Go (from Go 1.8)

Go 1.8 later, it add function called ```-buildmode=plugin``` with this argument you can compile the code into a ```.so```, but this ```.so``` can only be called by Go, can not called by C.

```cmd
go build -buildmode=plugin -o myplugin.so myplugin.go
```

When I want to use this plugin.so, I need to using function call like ``` plugin.Open, and plug.Lookup to call the function in that library

```go
package main

import (
	"fmt"
	"log"
	"plugin"
)
func main() {
	// Open plugin file 打开插件
	plug, err := plugin.Open("myplugin.so")
	if err != nil {
		log.Fatal(err)
	}

	// Search the symbol in the plugin maybe an function or variable
    // 查找插件中的符号（函数或变量）
	sym, err := plug.Lookup("MyFunction")
}
```

if you want know more deep of the C and Go interactive. There are some more knowledge such like RPC, or using IPC between two process. I will explain here. 

## Advantage of Go

1. Once compile: it's more efficient then other language
2. All the compile occurred in the memory. Faster!
3. Simple command line: ```go build``` that's OK easy to remember. all the Cross platform are defined inner or env variable.

## Coding

Please read the code in this folder, you will know how to write the simple Go code. just for getting started. It's include:

variable define

package

import

data type

for loop

printer

function define

struct

class based on struct

OOP

OOP deeper: Interface, Inherit(it does not support multiple inheritance, but you can use a struct include two or more type to merge different class instance together)
