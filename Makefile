all:
	@python3 src/main.py

setup:
	pip3 install -r requirements.txt

install-deb:
	sudo apt install gcc g++ python3 \
	python3-pip libssl-dev libboost-all-dev \
	git

reinit:
	python3 src/reinit.py