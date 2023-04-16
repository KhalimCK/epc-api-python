init:
	pip install -r requirements/prod.txt

test:
	pip install -r requirements/test.txt
	pytest --cov-report term-missing --cov=api tests/
