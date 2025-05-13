package main

import "fmt"

// create a struct
// 有一点跟 C 不同的，大部分是一样的注意 , 在最后一行也需要逗号
// 有个问题 struct 是传值的，但是 struct 里面包含一个 map 的时候传递值还是引用？？？？
// struct 可以添加函数，格式是 func (b Bill) func_name(argument) 函数中是用 b 作为实例来编写函数， 就像 C++ 中的 this， Python 中的 self 一样



type bill struct {
	name string
	total float32
	items map[string]float32
	time string
}
func (b *bill) format() string {
	ret := "Bill Information:\n"
	var total float32 = 0.0
	for k, v := range b.items {
		ret+=fmt.Sprintf("item name: %v, price:%v \n", k, v)
		total+=v
	}
	ret += fmt.Sprintf("total:%v", total)
	return ret
}
//使用指针来代替 self 的方法
// 使用 func (b bill) func (b *bill) 都可以，但是前面一种是复制一份 结构体来做事情，后面一种是直接传入原来的结构体
// func (b, *bill) 不需要做任何改动

func (b *bill) testFunc() string {
	fmt.Println((*b).format())
	return "finished of test Func"
}

func buildBill(name string, items map[string]float32, total float32, time string) bill {
	return bill {
		name:name,
		items:items,
		total:total,
		time:time,
	}
}
func testStruct() {
	fmt.Println("Struct Test =====================")
	bt := buildBill("AAAAA", map[string]float32{"A":32.4, "BBB":434.4,}, 3234.223, "3334535-234-32")

	fmt.Println(bt.format())
	
	fmt.Println(bt.testFunc())
}