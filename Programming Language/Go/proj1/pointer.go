package main

import "fmt"

//&var is get address of a variable
//*var is get value of a pointer
//传参跟 C 一样&在 type 前面    &int &bool

func print_r(p_name *string) {
	fmt.Println(*p_name)
	*p_name = "BBBBB"
}
func testPoint() {
	fmt.Println("Point Test =====================")
	m:= "AAAAAAA"
	print_r(&m)
	fmt.Println(m)
}