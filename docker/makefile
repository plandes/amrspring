##@meta {desc: 'build and deployment for docker projects', date: '2024-02-17'}


## Build system
#
#
# type of project
PROJ_TYPE=		docker


## Project
#
DOCKER_IMG_NAME=	springserv
DOCKER_USER=		plandes
DOCKER_UP_DEPS=		mkdata


## Includes
#
include ../zenbuild/main.mk


## Targets
#
.PHONY:			mkdata
mkdata:
			mkdir -p data
