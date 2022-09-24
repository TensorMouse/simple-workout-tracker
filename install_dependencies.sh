#!/bin/bash

echo "Installing virtualenv and creating virtual environment"
pip install virtualenv
virtualenv venv
echo "Installing dependencies to virtual environment" 
./venv/bin/pip install -r requirements.txt
