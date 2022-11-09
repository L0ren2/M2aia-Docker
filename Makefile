THIS-DIR=/home/maia/Documents/maia/Docker# without trailing / ; do not remove the # character after the path (dont introduce whitespace in the path)
BASE-DIR=$(THIS-DIR)/M2aiaContainer# 
PYTHON-DIR=$(THIS-DIR)/M2aiaContainerPython#
R-DIR=$(THIS-DIR)/M2aiaContainerR#

base:
	docker build $(BASE-DIR) -t m2aia-docker-base
	@echo "Successfully built base image!"
	@echo Run 'docker run -it --name=m2aia-container-base --mount "type=bind,source=$(THIS-DIR)/m2aia-share,destination=/m2aia-share" m2aia-docker-base bash' to get an interactive prompt.

python: base
	docker build $(PYTHON-DIR) -t m2aia-docker-python
	@echo "Successfully built python image!"
	@echo Run 'docker run -it --name=m2aia-container-python --mount "type=bind,source=$(THIS-DIR)/m2aia-share,destination=/m2aia-share" m2aia-docker-python bash' to get an interactive prompt.

r: base
	docker build $(R-DIR) -t m2aia-docker-r
	@echo "Successfully built R image!"
	@echo Run 'docker run -it --name=m2aia-container-r --mount "type=bind,source=$(THIS-DIR)/m2aia-share,destination=/m2aia-share" m2aia-docker-r bash' to get an interactive prompt.

all: python r
