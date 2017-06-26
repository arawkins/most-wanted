# Feature Request System

This is a small demo feature request system.
You can find an instance of it running online at (insert url here)

## How to run

There are a couple of different ways you can get this app up and running.

### Using docker
```
docker run -d -p 5000:5000 arawkins/most-wanted:latest
```
You should find the app running at http://localhost:5000

### Using python 3
The following instructions assume a working python 3 development environment, inlcuding pip.
You may want to [set up a virtualenv](http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/) before running the following commands.
```
pip3 install -r requirements.txt
python3 create_db.py
python3 main.py
```
You should find the app running at http://localhost:5000
