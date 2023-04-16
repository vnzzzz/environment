#!/bin/bash

poetry new src --name code

(cd src; poetry config --local virtualenvs.path ".venv"; poetry config --local virtualenvs.in-project true )
(cd src; poetry add flake8 black) 