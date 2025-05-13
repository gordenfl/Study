package main

import "fmt"

/*
            Animal_Interface

              Animal(struct)
			  /    \
            /       \
	     Dog	    Cat

still need to using interface define the common function, then different subclass pass as the interface to be call the common interface

BaseClass only help to implement the same function. do not have other function.
*/
type OOP_Animal_Interface interface {
	getTType() string
}

type OOP_Animal struct {
	Name string
	Size int
	TType string
}
func (oop_animal OOP_Animal) getTType() string {
	return oop_animal.TType
}



type OOP_Dog struct {
	OOP_Animal
}
func (dog OOP_Dog) getName() string {
	return dog.Name
}

func (dog OOP_Dog) getSize() int {
	return dog.Size
}



type OOP_Cat struct {
	OOP_Animal
}

func (cat OOP_Cat) getName() string {
	return cat.Name
}
func (cat OOP_Cat) getSize() int {
	return cat.Size
}


func GetAnimalInfo(animal OOP_Animal_Interface) {
	fmt.Println("This Animal is a type of ", animal.getTType())
}

func testOOPBaseClass() {
	dog := OOP_Dog{OOP_Animal{Name:"dog1", Size:10, TType:"dog"}}
	GetAnimalInfo(dog)
}