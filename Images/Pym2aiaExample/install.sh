#!/bin/sh
pip install git+https://github.com/m2aia/pym2aia.git
git clone https://github.com/m2aia/pym2aia-examples
cd /pym2aia-examples/
git submodule update --recursive --init
pip install -r /pym2aia-examples/requirements.txt