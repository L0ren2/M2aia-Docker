THIS-DIR=/home/maia/Documents/maia/Docker/Images# without trailing / ; do not remove the # character after the path (dont introduce whitespace in the path)
BASE-DIR=$(THIS-DIR)/Base# 
PYTHON-DIR=$(THIS-DIR)/Python#
R-DIR=$(THIS-DIR)/R#
R-EXAMPLE-DIR=$(THIS-DIR)/RExample#
PYM2AIA-DIR=$(THIS-DIR)/Pym2aia#
PYM2AIA-EXAMPLE-DIR=$(THIS-DIR)/Pym2aiaExample#
PYM2AIA-VOLCANO-DIR=$(THIS-DIR)/Pym2aiaVolcanoPlot#

base:
	docker build $(BASE-DIR) -t m2aia/docker:base
	@echo "Successfully built base image!"

python: base
	docker build $(PYTHON-DIR) -t m2aia/docker:python
	@echo "Successfully built python image!"

r: base
	docker build $(R-DIR) -t m2aia/docker:r
	@echo "Successfully built R image!"

r-example: r
	docker build $(R-EXAMPLE-DIR) -t m2aia/docker:r-example
	@echo "Successfully built R-Example image!"

pym2aia: python
	docker build $(PYM2AIA-DIR) -t m2aia/docker:pym2aia
	@echo "Successfully built Pym2aia image!"

pym2aia-example: pym2aia
	docker build $(PYM2AIA-EXAMPLE-DIR) -t m2aia/docker:pym2aia-example
	@echo "Successfully built Pym2aiaExample image!"

pym2aia-volcano: pym2aia
	docker build $(PYM2AIA-VOLCANO-DIR) -t m2aia/docker:pym2aia-volcano-plot
	@echo "Successfully built Pym2aiaVolcano image!"

all: base r python pym2aia pym2aia-volcano # dont build examples

