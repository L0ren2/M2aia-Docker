# use m2aia-docker-base as base image
FROM m2aia/docker:r
LABEL m2aia.docker="R-Example"
# refrain from interactive questions
ARG DEBIAN_FRONTEND=noninteractive
# install additional packages
RUN apt update && apt upgrade -y && apt install -y r-base-core \
libfftw3-3 \
libfftw3-dev \
libtiff5-dev \
libcurl4-openssl-dev \
curl

COPY ./install.R /install.R

# install older version of locfit package
RUN curl https://cran.r-project.org/src/contrib/Archive/locfit/locfit_1.1-11.tar.gz --output /tmp/locfit_1.1-11.tar.gz && \
cd /tmp/ && \
tar -xvf locfit_1.1-11.tar.gz && \
echo 'exportPattern(" . ")' > locfit/NAMESPACE && \
tar -zcf locfit.tar.gz locfit && \
mkdir -p /usr/local/lib/R/site-library/locfit && \
mv locfit.tar.gz /usr/local/lib/R/site-library/ && \
R CMD INSTALL -l locfit /usr/local/lib/R/site-library/locfit.tar.gz && \
Rscript /install.R

#finally copy comandline module
COPY ./cli-module.R /cli-module.R
