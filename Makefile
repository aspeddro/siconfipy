NAME=siconfipy

installdev:
	pip install --user --no-use-pep517 -e .

uninstall:
	pip uninstall $(NAME) --yes

install:
	pip install .

installtest:
	pip uninstall $(NAME)
	pip install --index-url https://test.pypi.org/simple/ $(NAME)

clean:
	rm -rf dist 
	rm -rf build 
	rm -rf siconfipy.egg-info

format:
	black .

check:
	twine check dist/*

datasets:
	python utils/build_datasets.py

build:
	python setup.py sdist

testpublish: clean build format
	twine upload --repository testpypi dist/*

installtest:
	pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple siconfipy

publish: clean build format
	twine upload dist/*