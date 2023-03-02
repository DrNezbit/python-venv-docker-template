# python-venv-docker-template

This is a simple template for creating a docker image and docker compose stack for development of python scripts or applications.  

## Setup
Start by installing docker if not installed already (Portainer is also recommended but not required). Next add your needed requirements to requirements.txt, replace code in "main.py" with your own and run "docker compose up" (add "-d" to run in background).  Container will be built to run your code. Feel free to change code and simply start container again.  If any requirements are added to requirements.txt after initial build the image will need to be rebuilt.

## Docker Install
https://docs.docker.com/get-docker/

## Portainer Setup
https://docs.portainer.io/start/install/server/docker
