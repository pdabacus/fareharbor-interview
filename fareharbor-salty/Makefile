#
# Makefile for Fareharbor Salty Django API
#

.PHONY: all init vars run
all: init run

init:
ifndef FAREHARBOR_ENV
$(error set shell with `source shellinit.sh`)
endif

vars: init
	@echo "PYENV_ROOT $(PYENV_ROOT)"
	@echo "python $(shell which python)"

run: init
	python manage.py runserver
