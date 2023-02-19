import os,sys,logging

logging.basicConfig(
    stream=sys.stdout,
    format="%(levelname)s - %(asctime)s \n%(message)s",
    datefmt='%m/%d/%Y %I:%M:%S %p%z',
    level=logging.INFO)
   
logging.info(" Hello World!")

pwd=os.popen("pwd").read()
logging.info("Current working directory is: %s",pwd)

cnts=os.popen("ls").read()
logging.info("Contents of %s %s",pwd,cnts)

pkgs=os.popen("pip freeze").read()
logging.info("installed pip packages are: \n%s \n-------------------------",pkgs)

logging.info("This is a Python script running in a venv inside of \n\
a docker container as part of a docker-compose stack \n \
\nThis file will be ran on container start.  \n\
- Add needed requirements to requirements.txt \n\
- Rebuild container (docker-compose up -build) \n\
- Replace this file with what you would like to run")
