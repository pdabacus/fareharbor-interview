#!/bin/sh
export PYENV_ROOT=/home/pavan/Desktop/fareharbor-dayal/.pyenv
if ! [ -d ../.pyenv/shims ]; then
    pyenv install 3.8.11
fi
pyenv local 3.8.11
eval "$(pyenv init -)"
if ! [ -f ../.pyenv/versions/3.8.11/bin/django-admin ]; then
    pip install -r requirements.txt
fi
export FAREHARBOR_ENV=1
