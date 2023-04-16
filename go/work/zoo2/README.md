# memo

プロジェクトルート（ここでの`zoo`）でvscode remote containerを開かないと、importでエラーが出るので注意

```bash

# add module
go mod init zoo

# run
go run main.go app.go 

# build
go build
go build *.go

# test
go test -v

# package test
go test -v ./animals

```
