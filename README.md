# Feature Request System

This is a small demo feature request system.
You can find an instance of it [running online here](http://mostwanted-env.us-west-2.elasticbeanstalk.com/)

## How to run

There are a couple of different ways you can get this app up and running.

### Using Docker
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
