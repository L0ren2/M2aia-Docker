# install ubuntu version that is compatible with M2aia
ARG version=20.04
FROM ubuntu:${version}
LABEL m2aia.docker="Base"
# refrain from interactive questions
ARG DEBIAN_FRONTEND=noninteractive
# install additional packages
RUN apt update && apt upgrade -y

