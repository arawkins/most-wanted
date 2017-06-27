# Feature Request System

This is a small demo feature request system.
You can find an instance of it [running online here](http://mostwanted-env.us-west-2.elasticbeanstalk.com/)

## How to run

There are a couple of different ways you can get this app up and running.

### Using Docker
This app is available as a [docker image on docker hub](https://hub.docker.com/r/arawkins/most-wanted/).
```
docker run -d -p 5000:5000 arawkins/most-wanted:latest
```
You should find the app running at http://localhost:5000

### Using Python 3
The following instructions assume a working python 3 development environment, including pip.
You may want to [set up a virtualenv](http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/) before running the following commands.
```
pip3 install -r requirements.txt
python3 create_db.py
python3 main.py
```
You should find the app running at http://localhost:5000

### Using AWS Elastic Beanstalk
You can quickly deploy this app to AWS Elasic Beanstalk as a single container docker application. When setting up your application, provide the Dockerrun.aws.json file to AWS as the source of your application version. It will pull the image from docker hub and start the application for you.
