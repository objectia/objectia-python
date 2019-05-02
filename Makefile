.PHONY: test install requirements deploy release-test
test:
	pytest -v

release-test:
	python3 setup.py sdist bdist_wheel upload -r pypitest

deploy:
	python3 setup.py sdist bdist_wheel upload

install: requirements

requirements: .requirements.txt

.requirements.txt: requirements.txt
	pip install --upgrade pip setuptools
	pip install -r requirements.txt
	pip freeze > .requirements.txt