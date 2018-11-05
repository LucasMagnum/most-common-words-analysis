run:
	python run.py 100

setup:
	pip install -r requirements.txt

test:
	python -m unittest discover tests
