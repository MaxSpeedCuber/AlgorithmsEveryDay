install:
	pip install poetry && \
	poetry install

start:
	poetry run python AlgorithmsEveryDay/main.py
