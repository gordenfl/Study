package main

import "fmt"

func testMap() {
	fmt.Println("Map Test =====================")	
	// Map how to define a map in go  !IMPORTANT
	// pass value's type are: string, int, bool, float, array, struct 
	// pass ref's type are: Slice, Map, function
	data := map[string]int32{
		"age":    23,
		"height": 123,
		"weight": 246,
		"ticket": 23,
		"price":  13,
	}
	
	updateData(data)
	for k, v := range data {
		fmt.Println(k, v)
	}
}

func updateData(data map[string]int32) {
	data["age"] = 23434
}

