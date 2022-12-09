FROM m2aia/m2aia:latest-build as M2aiaBinaries
FROM m2aia/docker:python
LABEL m2aia.docker="Pym2aia"
ARG DEBIAN_FRONTEND=noninteractive 

RUN apt-get update -q -y && apt-get upgrade -q -y
RUN apt-get install -q -y --no-install-recommends \
    libglu1-mesa-dev \
    libgomp1 \
    libopenslide-dev \
    python3 \
    python3-pip \
	python3-scipy \
	python3-mne
RUN pip install wget \
numpy==1.23.5 \
python-dateutil==2.8.2 \
matplotlib==3.5.0 \
seaborn \
seaborn_image \
tensorflow \
umap-learn \
torch \
torchvision \
efficientnet_pytorch

RUN pip install https://github.com/m2aia/pym2aia/releases/download/v0.2.6/pym2aia-0.2.6-py3-none-linux_x86_64.whl

