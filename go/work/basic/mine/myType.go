package mine

import (
	"fmt"
	"math"
	"runtime"
)

func MyType() {
	pc, _, _, _ := runtime.Caller(0)
	fmt.Printf("---- %s ----\n", runtime.FuncForPC(pc).Name())

	// 型宣言
	n := 5
	/*
		下のような書き方もできる
		var n int
		n = 5
	*/
	var (
		x, y int
		z    string
	)
	x, y, z = 1, 2, "test"
	fmt.Println(n, x, y, z)

	// 型推論
	i := 1
	b := true
	f := 3.14
	s := "abc"
	fmt.Println(i, b, f, s)

	// 論理値型
	b1 := true
	fmt.Println("b1", b1)

	// 数値型 キャスト
	n_int := 1
	n_i64 := int64(n_int)
	n_uint := uint(n_int)
	n_byte := byte(n_int)
	n_u32 := uint32(n_int)
	fmt.Printf("int型:%d int64型:%d uint型:%d uint32型:%d byte型:%d \n", n_int, n_i64, n_uint, n_u32, n_byte)

	fmt.Printf("f:%f int(f):%d\n", f, int(f))

	// オーバーフロー
	n_over := 256
	n_byte_over := byte(n_over)
	fmt.Printf("overflowしたbyte: %d \n", n_byte_over)

	// 補数
	by1 := byte(255)
	by2 := by1 + byte(255)
	println(by2)

	// ラップアラウンド
	ui_1 := uint32(400000000)
	ui_2 := uint32(4000000000)
	sum := ui_1 + ui_2
	fmt.Printf("%d + %d = %d\n", ui_1, ui_2, sum)

	// ラップアラウンド対策
	fmt.Printf("uint32 max value = %d\n", math.MaxUint32)
	doSomething(1, 1)
	doSomething(ui_1, ui_2)

	// 浮動小数点
	fmt.Printf("float max value = %f\n", math.MaxFloat32)
	fmt.Printf("float min value = %f\n", math.SmallestNonzeroFloat32)

	// 特殊な演算
	zero := 0.0
	pinf := 1.0 / zero
	ninf := -1.0 / zero
	fmt.Println(pinf, ninf)

	// rune型
	r := '松'
	fmt.Printf("%v\n", r)

	// sting型
	s1 := "文字列"
	fmt.Printf("%v\n", s1)

	// RAW文字列
	s2 := `
	GOの
	RAW文字列リテラル
	`
	fmt.Printf("%v\n", s2)

	// 配列型
	fmt.Printf("%v \n", [5]int{1, 2, 3, 4, 5})
	fmt.Printf("%v \n", [5]int{})
	fmt.Printf("%v \n", [...]int{1, 2, 3})
	a := [5]int{1, 2, 3, 4, 5}
	a[2] = 100
	fmt.Printf("%v \n", a)

}

func doSomething(a, b uint32) bool {
	// オーバーフロー確認用の関数
	if (math.MaxUint32 - a) < b {
		fmt.Printf("%d + %d はオーバーフローします\n", a, b)
		return false
	} else {
		fmt.Printf("%d + %d = %d (オーバーフローしません)\n", a, b, a+b)
		return true
	}
}
