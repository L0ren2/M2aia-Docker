# M2aia-Docker
This is used as a way to execute external Modules for M2aia. 

As long as there is a suited Docker Container, the language the module is written in does not matter. 

It is expected, that the modules will write their output into the m2aia-share directory. 

## Prerequisites
- Working installation of `docker`

- User that is part of the `docker` group

## Configuration
Currently, to use the CLI, you will have to configure the `Makefile` in this directory. 
For this, open the `Makefile` using your favourite editor. 
Then modify the variable `THIS-DIR` to point to the current directory (the directory where this `README.md` and the `Makefile` are located), since docker does not allow relative paths. 

That's it! 

You can now use all programs inside that docker container. 

## Run the CLI
There are two ways supported: 

 - From within M2aia
 - Headless, without M2aia itself

### Within M2aia
M2aia can be built with the plugin `org.mitk.modules.docker.external` which adds a view named `External Docker Modules`. 
In this view you can specify the name of any external module. as long as that module is in its corresponding directory and M2aia can find it, it will be executed. 
M2aia will signal that the module has finished, so that the data can be processed further. 
TODO ^^'

### Headless
For running in headless mode, please just run the `make` command in this directory. 
There are four different options: `make base`, `make python`, `make r` and `make all`
Base is just a base image from which all other containers are constructed. 
It can not run anything but binary files and shell scripts. 
Python is for running python files and R can be used for running R-scripts. 
You can get a command prompt inside a container by executing `docker run -it --name=m2aia-container-[base | python | r] --mount "type=bind,source=$(THIS-DIR)/m2aia-share,destination=/m2aia-share" m2aia-docker-[base | python | r] bash`, depending on which of the available containers you want to run. 
Inside the `m2aia-container` you can find a directory named `/m2aia-share` which is mapped to the `$(THIS-DIR)/m2aia-share` directory. 
The `$(THIS-DIR)/m2aia-share` directory is used for storing the outputs of CLI-Modules on the Host. 
M2aia should be able to read the files in the `$(THIS-DIR)/m2aia-share` directory. 

