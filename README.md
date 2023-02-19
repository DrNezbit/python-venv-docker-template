# python-venv-docker-template

This is a simple template for creating a docker and docker-compose stack for development of python scripts or applications.  

Add your needed requirements to requirements.txt, replace code in "main.py" with your own and run "docker-compose up".  Container will be built to run your code. Feel free to change code and simply start container again.  If any requirements are added to requirements.txt after initial build the image will need to be rebuilt with "docker-compose up -build" or removed to be rebuilt
