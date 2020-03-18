clean:
	@rm -rf @rm -fr */__pycache__
	@rm -fr build dist .eggs .pytest_cache

dev_install:
	@pip3 install -r requirements.txt

test:
	@py.test tests/

lint:
	@flake8 --ignore=E731,W503,W605 src/*.py *.py
