all:
	virtualenv ../venv
	. ../venv/bin/activate
	pip install --break-system-packages pytest pylint pycodestyle flake8

test:
	. ../venv/bin/activate
	pytest

check:
	pylint py_strings.py
	pycodestyle --ignore=E203 py_strings.py
	flake8 --ignore E203,F401,F403,F405 .
