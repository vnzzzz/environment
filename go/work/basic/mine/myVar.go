package mine

import (
	"fmt"
	"runtime"
)

/* パッケージ変数 */
var n = 100

func MyVar() {
	pc, _, _, _ := runtime.Caller(0)
	fmt.Printf("---- %s ----\n", runtime.FuncForPC(pc).Name())

	/* using package var */
	n = n + 1
	fmt.Printf("n=%d\n", n)
}
