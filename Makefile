.PHONY: format
format:
	poetry run isort ./src ./tests
	poetry run black ./src ./tests

.PHONY: lint
lint: AUTOFLAKE_OPTIONS := --remove-unused-variables --remove-all-unused-imports
lint: format
	poetry run autoflake . $(AUTOFLAKE_OPTIONS)

.PHONY: tests
tests:
	poetry run python -m pytest --cache-clear ./tests/*

.PHONY: packages
packages:
	poetry install


.PHONY: run
run:
	poetry run uvicorn src_new.app:main_app --port=8000 --reload
