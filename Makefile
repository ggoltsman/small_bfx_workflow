snpEff:
	wget https://snpeff.blob.core.windows.net/versions/snpEff_latest_core.zip &&\
		unzip snpEff_latest_core.zip && rm snpEff_latest_core.zip

install: snpEff
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_unittests.py

lint:
	pylint --disable=C,unspecified-encoding workflow.py modules.py

format:
	black *.py

all: snpEff install test lint format

clean:
	rm -rf snpEff
