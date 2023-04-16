package mine

import (
	"fmt"
	"runtime"
)

func MyFmt() {
	pc, _, _, _ := runtime.Caller(0)
	fmt.Printf("---- %s ----\n", runtime.FuncForPC(pc).Name())

	// println
	fmt.Println("Hello, Golang")
	fmt.Println("this", "is", "a", "pen")

	// printf
	fmt.Printf("number=%d \n", 5)

	// print
	print("Hello World \n")
	println("Hello World")
}
