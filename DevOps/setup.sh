#!/bin/bash

# Usage: This script is used to setup the environment in the server

sudo yum update -y
sudo yum install python3-pip -y
sudo yum install git -y
sudo yum install screen -y

pip install virtualenv
virtualenv myenv
source myenv/bin/activate

git clone https://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@github.com/D-Arenas/Project-1-analitica.git
cd Project-1-analitica/despliegue

pip install -r requirements.txt
screen -S dashboard_session -d -m python app.py
