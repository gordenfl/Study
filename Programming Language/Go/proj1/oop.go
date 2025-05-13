package main

import "fmt"

type Person struct {
	Name string
	Age  int
}

func (person *Person) Greet() {
	fmt.Println("Person's name is ", person.Name, " age of this person is ", person.Age)
}

func(person *Person) getName() string {
	return person.Name
}

func (person *Person) getAge() int {
	return person.Age
}

func (person *Person) setAge(age int) {
	person.Age = age
}

func (person *Person) isOlder(other Person) bool {
	return person.getAge() > other.getAge()
}

func testOOP() {
	fmt.Println("OOP Test ==============================")
	gordon := Person{Name:"Gordon", Age:44}
	gordon.Greet()

	fmt.Println("Object name is", gordon.getName(), "age is", gordon.getAge())

	oneqiong := Person{Name:"oneqiong", Age:42}
	fmt.Println("oneqiong is older then gordon: ", oneqiong.isOlder(gordon))

	gordon.setAge(39)
	fmt.Println("oneqiong is older then gordon: ", oneqiong.isOlder(gordon))
}

