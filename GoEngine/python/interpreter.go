package python

import (
	"fmt"
	"log"
	"path/filepath"
	"runtime"

	python3 "github.com/DataDog/go-python3"
)

func Init() {
	if !python3.Py_IsInitialized() {
		python3.Py_Initialize()
	}

	// 设置 PYTHONPATH（添加你的脚本目录）
	_, filename, _, _ := runtime.Caller(0)
	scriptDir := filepath.Join(filepath.Dir(filename), "..", "logic")
	sysPath := python3.PySys_GetObject("path")
	pyScriptPath := python3.PyUnicode_FromString(scriptDir)
	python3.PyList_Append(sysPath, pyScriptPath)

	fmt.Println("Python initialized. Script path:", scriptDir)
}

func Finalize() {
	python3.Py_Finalize()
}

func CallUserMove(uid string, x, y int) {
	moduleName := python3.PyUnicode_FromString("user_logic")
	module := python3.PyImport_Import(moduleName)
	if module == nil {
		log.Println("Failed to import user_logic")
		python3.PyErr_Print()
		return
	}

	fn := module.GetAttrString("on_user_move")
	if fn == nil || !python3.PyCallable_Check(fn) {
		log.Println("Function on_user_move not found or not callable")
		python3.PyErr_Print()
		return
	}

	args := python3.PyTuple_New(3)
	python3.PyTuple_SetItem(args, 0, python3.PyUnicode_FromString(uid))
	python3.PyTuple_SetItem(args, 1, python3.PyLong_FromGoInt(x))
	python3.PyTuple_SetItem(args, 2, python3.PyLong_FromGoInt(y))

	result := fn.CallObject(args)
	if result == nil {
		log.Println("Call to on_user_movvim e failed")
		python3.PyErr_Print()
	}
}
