package main

import (
	"fmt"
)

// function type define
// type function func(string) string

func saySomething(name string, fe func(string) string) {
	s := fe(name)
	fmt.Println(s)
}

func A(name string) string {
	return "AAAA " + name
}

func B(name string) string {
	return "BBBB " + name
}

////////////////////////////////////////////////////
// default function define
/*
func function(f int32 ,t string) {
	fmt.Println("function is called")
	fmt.Println(f, t)
}
*/

////////////////////////////////////////////////////
// function return multiply values
func getInts(n string) (int32, int32) {
	return 23,34
}

////////////////////////////////////////////////////
