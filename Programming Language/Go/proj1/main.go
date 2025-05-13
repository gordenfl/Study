package main

import (
	"fmt"
	"sort"
	"strings"
	// ...existing code...
)

func testVar() {
	fmt.Println("Var Test =====================")
	name := "Gordon"
	n:="TBD"
	var t = 134
	fmt.Println(name, n, t)
	name ="VVVV"
	n = "AAAAA"
	t = 3456
	fmt.Println(name, n, t)
}
func testInts() {
	fmt.Println("Ints Test =====================")
	// int int8 int 16 int32 int64 float as well
	var age int8 = -128

	age = 122
	height:=12
	height=111
	fmt.Println(age, height)

	//format of string
	fmt.Printf("ASDFASDFASFD %v asdfasdfasdf %v adfasdfasdf\n", 33, 42)
	fmt.Printf("ASDFASDFASFD %q asdfasdfasdf %q adfasdfasdf\n", "33", "Gordon")
	fmt.Printf("ASDFASDFASFD %T asdfasdfasdf %T adfasdfasdf\n", 33, "Gordon")
	fmt.Printf("ASDFASDFASFD %0.4f asdfasdfasdf %T adfasdfasdf\n", 33.99, "Gordon")
	fmt.Printf("ASDFASDFASFD %s asdfasdfasdf %s adfasdfasdf\n", "33.99", "Gordon")
	fmt.Printf("ASDFASDFASFD %v asdfasdfasdf %v adfasdfasdf\n", "33.99", "Gordon")//auto matic get the type of variable
	var str = fmt.Sprintf("ASDFASDFASFD %s asdfasdfasdf %s adfasdfasdf", "33.99", "Gordon")//auto matic get the type of variable
	fmt.Println(str, "====")
}

func testArray(){
	// //Arrays
	fmt.Println("Arrayy Test =====================")
	var ages1 [3]int = [3]int {23,24,57}
	fmt.Println(ages1, len(ages1))
	var args2 = [3]int {23,24,57}
	fmt.Println(args2, len(args2))
	var args3 = [3]string {"23","24","57"}
	fmt.Println(args3, len(args3))
	var scores = []int{1,2,3,4,5,6}
	fmt.Println(scores, len(scores))
	scores = append(scores, 88)
	fmt.Println(scores, len(scores))

	
}
func testArrayRange() {
	// //slice ranges
	fmt.Println("ArrayyRange Test =====================")
	var args4 = []string {"23","24","57"} // must [] not [3]
	args4 = append(args4, "gordon")
	fmt.Println(args4, len(args4))
	newargs :=args4[1:4]
	fmt.Println(newargs, args4[2:], args4[:2] ,len(newargs))
}
func testString() {
	fmt.Println("String Test =====================")
	//Strings  IMPORTANT: the ReplaceAll will not change the source data in the variable!!!! it will create a new variable
	data := "Hello Gordon and Ken"
	fmt.Println(strings.Contains(data, "Gordon"))
	fmt.Println(strings.ReplaceAll(data, "Gordon", "Bing"))
	fmt.Println(strings.Index(data, "Gordon"))

	fmt.Println(strings.Split(data, " ")[2])
}
func testSort() {
	fmt.Println("Sort Test =====================")
	// sort IMPORTANT the sort will change the source data of your variable
	data := []int {3,4,2,5,1,6,78,9,2,3,4,5}
	sort.Ints(data)
	fmt.Println(data)
}

func testForloop() {
	fmt.Println("ForLoop Test =====================")
	// for loop, IMPORTANT: all the value in the loop are the copy of the data  not the same data
	x := 0
	for x < 5 { //like while
		fmt.Println(x)
		x++
	}

	for i := 0; i < 5; i++ { //like for
		fmt.Println(i)
	}

	names := []string{"ABCC", "DEEE", "FFAS", "DF", "ASD", "F", "ASDF", "ASDF", "ASDF"}
	for i := 0; i < len(names); i++ {
		fmt.Println(names[i])
	}

	for index, value := range names {
		fmt.Println(index, value)
	}
}

func testBooleanType() {
	fmt.Println("BooleanType Test =====================")
	//Boolean
	age := 45
	fmt.Println(age < 50)

	if age >= 50 {
		fmt.Println("asdfasfdaf")
	} else if age > 20 {
		fmt.Println("AAAAAAAAAAAAAA")
	} else {
		fmt.Println("VVVVVVVVVVVVV")
	}

	names := []string{"ABCC", "DEEE", "FFAS", "DF", "ASD", "F", "ASDF", "ASDF", "ASDF"}
	for i, v := range names {
		if i == 1 {
			fmt.Println(i, v)
			continue
			//break // or using break as c++ or other language
		}
		fmt.Println(i, v, "aaaaa")
	}
}

//start OOP in Go, most important


func main() {
	// fmt.Println("Hello World!")
	//testOopDeep()	
	fmt.Println("Hello World!")
	saySomething("Gordon", A)
	saySomething("Gordon", B)
	fr, sr := getInts("AAAA")
	fmt.Println(fr+1, sr+1)

	testVar()
	testInts()
	testArray()
	testArrayRange()
	testString()
	testSort()
	testForloop()
	testBooleanType()
	testMap()
	testPoint()
	testStruct()

	testOOP()
	testOOPDeep()
	testOOPBaseClass()
}
