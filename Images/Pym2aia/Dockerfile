FROM m2aia/m2aia:latest-build as M2aiaBinaries
FROM m2aia/docker:python
LABEL m2aia.docker="Pym2aia"
#RUN mkdir -p /opt/packages
#COPY --from=M2aiaBinaries /opt/packages/m2aia.tar.gz /opt/packages/

RUN DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get -y install tzdata
RUN apt-get update && apt-get install -y -q --no-install-recommends \
    python3-venv \
    git \
    libglu1-mesa-dev \
    libtiff5-dev \
    libopenslide-dev 
    #qtbase5-dev \
    #qtscript5-dev \
    #libqt5svg5-dev \
    #libqt5opengl5-dev \
    #libqt5xmlpatterns5-dev \
    #qtwebengine5-dev \
    #qttools5-dev \
    #libqt5charts5-dev \
    #libqt5x11extras5-dev \
    #qtxmlpatterns5-dev-tools \
    #libqt5webengine-data \    

#RUN pip install tomli pyparsing packaging iniconfig exceptiongroup attrs pluggy pytest SimpleITK numpy

# m2aia/m2aia:latest-build containes the latest M2aia installer and required dependencies
#RUN mkdir -p /opt/m2aia
# we extract all files to this location
#RUN tar -xvf /opt/packages/m2aia.tar.gz -C /opt/m2aia --strip-components=1


# promote the required library path
#ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/m2aia/bin
#ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/m2aia/bin/MitkCore

#RUN git clone https://github.com/m2aia/pym2aia /opt/pym2aia
#RUN pip install git+https://github.com/m2aia/pym2aia.git
RUN pip install https://github.com/m2aia/pym2aia