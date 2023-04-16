package mine

import (
	"fmt"
	"runtime"
)

func MyConst() {
	pc, _, _, _ := runtime.Caller(0)
	fmt.Printf("---- %s ----\n", runtime.FuncForPC(pc).Name())

	const x = 1
	fmt.Println(x)

	const (
		x2 = 2
		x3 = 3
		x4 = 4
	)
	fmt.Println(x2, x3, x4)

	// 値の省略
	const (
		x5 = 1
		x6
		x7
		x8 = "test"
		x9
	)
	fmt.Println(x5, x6, x7, x8, x9)

	// 式
	const (
		x10 = 1
		x11 = 2
		x12 = x10 + x11
	)
	fmt.Println(x10, x11, x12)
	fmt.Printf("%T\n", x10)

	// iota
	const (
		A = iota
		B = iota
		C = iota
	)
	fmt.Println(A, B, C)

	// iota again
	// iotaは一つのconstごと
	const (
		D = iota
		E
		F
	)
	fmt.Println(D, E, F)
}
