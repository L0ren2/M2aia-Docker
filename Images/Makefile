THIS-DIR=/home/maia/Documents/maia/Docker/Images# without trailing / ; do not remove the # character after the path (dont introduce whitespace in the path)
BASE-DIR=$(THIS-DIR)/Base# 
PYTHON-DIR=$(THIS-DIR)/Python#
R-DIR=$(THIS-DIR)/R#
PYM2AIA-DIR=$(THIS-DIR)/Pym2aia#

base:
	docker build $(BASE-DIR) -t m2aia/docker:base
	@echo "Successfully built base image!"

python: base
	docker build $(PYTHON-DIR) -t m2aia/docker:python
	@echo "Successfully built python image!"

r: base
	docker build $(R-DIR) -t m2aia/docker:r
	@echo "Successfully built R image!"

pym2aia: python
	docker build $(PYM2AIA-DIR) -t m2aia/docker:pym2aia
	@echo "Successfully built Pym2aia image!"

all: pym2aia python r
