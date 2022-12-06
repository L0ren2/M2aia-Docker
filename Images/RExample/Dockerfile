# use m2aia-docker-base as base image
FROM m2aia/docker:r
LABEL m2aia.docker="R-Example"

RUN apt update && apt upgrade -y && apt install -y r-base-core \
libfftw3-3 \
libfftw3-dev \
libtiff5-dev \
libcurl4-openssl-dev \
curl

COPY ./install.R /install.R
RUN Rscript /install.R

COPY ./cli-module.R /cli-module.R
