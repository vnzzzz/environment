package mine

import (
	"errors"
	"fmt"
	"runtime"
)

func MyFunction() {
	pc, _, _, _ := runtime.Caller(0)
	fmt.Printf("---- %s ----\n", runtime.FuncForPC(pc).Name())

	// 関数の利用
	fmt.Println(plus(1, 2))

	hello()

	q, r := div(19, 7)
	fmt.Printf("商=%d 剰余=%d\n", q, r)

	// 戻り値の破棄
	_, r_ := div(19, 7)
	fmt.Println(r_)

	// エラーハンドリング
	q2, r2, err := div2(19, 0)
	switch err {
	case ErrDivError1:
		fmt.Println(err)
	default:
		fmt.Printf("商=%d 剰余=%d\n", q2, r2)
	}

	q3, r3, err := div2(19, 7)
	switch err {
	case ErrDivError1:
		fmt.Println(err)
	default:
		fmt.Printf("商=%d 剰余=%d\n", q3, r3)
	}

	// 無名関数
	f := func(x, y int) int { return x + y }
	fmt.Printf("無名関数の実行結果:%d\n", f(2, 3))

	// 無名関数の型
	fmt.Printf("%T\n", f)
	fmt.Printf("%T\n", f(2, 3))

	// 関数を返す関数の実行
	f2 := returnFunc()
	f2()
	returnFunc()() //そのまま実行できる

	// 関数を引数に取る関数の実行
	callFunction(func() {
		fmt.Println("I am a function")
	})

	//「引数に文字列を取り、戻り値に文字列を返す関数」を戻り値にする関数 の実行
	f3 := later()
	fmt.Println(f3("Golang"))
	fmt.Println(f3("is"))
	fmt.Println(f3("awesome!"))

	// クロージャによるジェネレータの利用
	ints := integers()
	fmt.Println(ints())
	fmt.Println(ints())
	fmt.Println(ints())

	otherInts := integers()
	fmt.Println(otherInts())

}

// 関数定義
func plus(x, y int) int {
	return x + y
}

// 戻り値のない関数
func hello() {
	fmt.Println("Hello, World!")
}

// 複数の戻り値
func div(a, b int) (int, int) {
	q := a / b
	r := a % b
	return q, r
}

// エラー処理
var ErrDivError1 = errors.New("0除算エラー") //エラーインスタンスの作成

func div2(a, b int) (int, int, error) {
	switch b {
	case 0:
		return 0, 0, ErrDivError1
	default:
		q := a / b
		r := a % b
		return q, r, nil
	}
}

// 関数を返す関数
func returnFunc() func() {
	return func() {
		fmt.Printf("I am a function\n")
	}
}

// 関数を引数に取る関数
func callFunction(f func()) {
	f()
}

//「引数に文字列を取り、戻り値に文字列を返す関数」を戻り値にする関数
func later() func(string) string {
	// 1つ前に与えられた文字列を保存するための変数
	var store string
	// 「引数に文字列を取り、文字列を返す関数」を返す
	return func(next string) string {
		s := store
		store = next
		return s
	}
}

// クロージャによるジェネレータの実装
func integers() func() int {
	i := 0
	return func() int {
		i += 1
		return i
	}
}
