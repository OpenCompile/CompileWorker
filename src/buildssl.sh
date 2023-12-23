#!/bin/bash

cd Repos/openssl
./config -static
make -j$(nproc)
sudo make install
