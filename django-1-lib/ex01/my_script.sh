#!/bin/bash

pip --version | cut -d' ' -f2

python3 -m venv local_lib
. local_lib/bin/activate
pip install --log path.log --force-reinstall git+https://github.com/jaraco/path.git
if [[ $? -eq 0 ]]
then
	python3 my_program.py 
fi