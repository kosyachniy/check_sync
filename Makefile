PYTHON := env/bin/python

setup:
	python3 -m venv env

setup-tests:
	make setup
	$(PYTHON) -m pip install -r tests/requirements.txt

test-linter:
	find . -type f -name '*.py' \
	| grep -vE 'env/' \
	| grep -vE 'tests/' \
	| xargs $(PYTHON) -m pylint -f text \
		--rcfile=tests/.pylintrc \
		--msg-template='{path}:{line}:{column}: [{symbol}] {msg}'

test-unit:
	$(PYTHON) -m pytest -s tests/

test:
	make test-linter
	make test-unit

clear:
	rm -rf env/
	rm -rf __pycache__/
	rm -rf **/__pycache__/
	rm -rf .pytest_cache/
