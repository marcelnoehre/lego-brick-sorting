#!/bin/bash

sudo apt update && sudo apt upgrade -y
sudo apt install -y git python3-pip
git clone https://github.com/DexterInd/GrovePi.git
cd GrovePi/Software/Python
sudo apt install -y python3-picamera2 python3-opencv
pip3 install -r requirements.txt