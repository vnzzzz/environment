FROM golang:1.17.8

# apt
RUN apt update \
    && apt install -y vim git

# install go tools
RUN go get github.com/uudashr/gopkgs/v2/cmd/gopkgs \
    github.com/ramya-rao-a/go-outline \
    github.com/nsf/gocode \
    github.com/acroca/go-symbols \
    github.com/fatih/gomodifytags \
    github.com/josharian/impl \
    github.com/haya14busa/goplay/cmd/goplay \
    github.com/go-delve/delve/cmd/dlv \
    golang.org/x/lint/golint \
    golang.org/x/tools/gopls

RUN mkdir /go/src/work
WORKDIR /go/src/work
