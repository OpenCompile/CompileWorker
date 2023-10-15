#!/bin/bash

cd Repos/openssl
git checkout OpenSSL_1_1_0-stable
./config -static
make -j$(nproc)
sudo make install
