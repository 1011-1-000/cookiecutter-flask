.PHONY: clean system-packages python-packages install tests run all

# the head of the command should be the tab not the space


clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete
	rm -rf ./tmp
	rm -rf ./db
	rm -rf ./log
	rm -rf ./migrations

init:
	mkdir db/
	mkdir log/
	flask db init
	flask db migrate
	flask db upgrade

python-packages:
	pip install -r requirements.txt

install: python-packages

tests:
	flask test

run_dev:
	flask run

run_prod:
	supervisord -c supervisord.conf

all: clean install init tests run_dev