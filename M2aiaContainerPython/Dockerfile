# user m2aia-docker-base image
FROM m2aia-docker-base
# refrain from interactive questions
ARG DEBIAN_FRONTEND=noninteractive
# install additional packages
RUN apt update && apt upgrade -y && apt install -y python3
COPY ./bin /bin

