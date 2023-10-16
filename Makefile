all:
	python3 src/main.py

init:
	python3 src/init.py

install-deb:
	sudo apt update
	sudo apt install gcc g++ python3 \
	python3-pip libssl-dev libboost-all-dev \
	git build-essential cmake libuv1-dev libssl-dev libhwloc-dev -y

reinit:
	python3 src/reinit.py
