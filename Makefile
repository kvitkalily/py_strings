.PHONY: all

all: setup test check

setup: requirements.txt
	virtualenv ../venv
	../venv/bin/pip install -r requirements.txt

test: ../venv/bin/pip
	../venv/bin/pytest

check:
	../venv/bin/pylint py_strings.py
	../venv/bin/pycodestyle --ignore=E203 py_strings.py
	../venv/bin/flake8 --ignore E203,F401,F403,F405 .

clean:
	rm -rf __pycache__
