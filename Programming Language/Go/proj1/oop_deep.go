package main

import "fmt"

/*
              Animal(interface)
			  /    \
            /       \
	     Dog	    Cat
*/


type Animal interface {
	Speak() string
	getTType() string
}

type Cat struct {
	Name string
	Color string
	Age int
	TType string
}
func (cat Cat) Speak() string {
	return "miao"
}

func (cat *Cat) getColor() string {
	return cat.Color
}
func (cat Cat) getTType() string {
	return cat.TType
}

type Dog struct {
	Name string
	Size int
	Age int
	TType string
}

func (dog Dog) Speak() string {
	return "wang"
}
func (dog *Dog) getSize() int {
	return dog.Size
}
func (dog Dog) getTType() string {
	return dog.TType
}


func GetSound(animal Animal) {
	fmt.Println("the", animal.getTType() ,"sound like", animal.Speak())
}

func testOOPDeep() {
	cat := Cat{Name:"cat1", Color:"white", Age:10, TType:"cat"}
	dog := Dog{Name:"mento", Size:10, Age:14, TType:"dog"}
	GetSound(cat)
	GetSound(dog)
}

