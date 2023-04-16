package mine

import (
	"fmt"
	"runtime"
)

func MyControl() {
	pc, _, _, _ := runtime.Caller(0)
	fmt.Printf("---- %s ----\n", runtime.FuncForPC(pc).Name())

	// for
	for i := 0; i < 10; i++ {
		fmt.Println(i)
	}

	// if
	x := 1
	if x == 1 {
		fmt.Println("x is 1")
	} else if x == 2 {
		fmt.Println("x is 2")
	}

	// 簡易分付きif
	if x, y := 1, 2; x < y {
		fmt.Printf("x(%d) is less thane y(%d)\n", x, y)
	}

	// break
	i := 0
	for {
		fmt.Println(i)
		i++
		if i == 10 {
			break
		}
	}

	// 条件付きfor
	j := 0
	for j < 5 {
		fmt.Println(j)
		j++
	}

	// continue
	for i := 0; i < 5; i++ {
		if i%2 == 1 {
			continue
		}
		fmt.Println(i)
		i++
	}

	// 範囲節
	fruits := [3]string{"Apple", "Banana", "Cherry"}
	for i, s := range fruits {
		fmt.Printf("fruits[%d]=%s\n", i, s)
	}

	// 文字列型とrange
	for i, r := range "ABC" {
		fmt.Printf("[%d] -> %d\n", i, r)
	}

	// switch
	for n := 0; n < 6; n++ {
		switch n {
		case 1, 2:
			fmt.Println("1 or 2")
		case 3, 4:
			fmt.Println("3 or 4")
		default:
			fmt.Println("unkonwn")
		}
	}

	// 変数を局所的に使う
	switch n := 2; n {
	case 1, 3, 5, 7, 9:
		fmt.Printf("%d is odd\n", n)
	default:
		fmt.Printf("%d is even\n", n)
	}

	// 式を伴うcase
	m := 4
	switch {
	case m > 0 && m < 3:
		fmt.Println("0 < n < 3")
	case m > 3 && m < 6:
		fmt.Println("3 < m < 6")
	}

	// intarface型
	anything(1)
	anything(3.14)
	anything("test")
	anything([...]int{1, 2, 3, 4, 5})

	// goto
	goto_test()

	// ラベル付き文
LOOP:
	for {
		for {
			for {
				fmt.Println("start")
				break LOOP
			}
		}
	}

	// defer
	runDefer()

	// ゴルーチン
	go fmt.Println("goroutine")
	fmt.Printf("CPU:%d\n", runtime.NumCPU())
	fmt.Printf("Goroutine:%d\n", runtime.NumGoroutine())
	fmt.Printf("Version:%s\n", runtime.Version())

}

func anything(a interface{}) {
	fmt.Println(a)
}

func goto_test() {
	fmt.Println("A")
	goto L
	// fmt.Println("B")
L:
	fmt.Println("C")
}

func runDefer() {
	defer fmt.Println("defer")
	fmt.Println("done")
}
