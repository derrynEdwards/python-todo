setup:
	python3 -m venv ~/.todo

install:
	source ~/.todo/bin/activate &&\
		pip install --upgrade pip &&\
		pip install -r requirements.txt

start:
	source ~/.todo/bin/activate &&\
		python web.py

all: setup install start