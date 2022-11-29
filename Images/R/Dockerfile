# use m2aia-docker-base as base image
FROM m2aia/docker:base
LABEL m2aia.docker="R"
# refrain from interactive questions
ARG DEBIAN_FRONTEND=noninteractive
# install additional packages
RUN apt update && apt upgrade -y && apt install -y r-base

