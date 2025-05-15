// logic/init.go
package logic

import (
	"GoEngine/python"
)

func InitPython() {
	// currently done in python.Initialize(), can later extend if needed
	python.CallUserMove("user1", 10, 20)
}
