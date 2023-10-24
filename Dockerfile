FROM ubuntu:latest
LABEL authors="ivtik"

ENTRYPOINT ["top", "-b"]