packages?=src

format:
	ruff format $(packages)
	ruff check --fix $(packages)

mypy:
	mypy $(packages)

check: format mypy
