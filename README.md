client_list
===========

## Dependencies

Some Common System dependencies are the following

*Python 2.7.3 (available via apt in debian "wheezy") or 2.7.5+ (in ubuntu 13.10)

*wget 1.13+ (older versions could not connect to PyPi via HTTPS)

*pip 1.1 (available via apt in debian wheezy as python-pip)

*git

*libbz2-dev

*libffi-dev

*libicu-dev

*libjpeg-dev

*libpython-dev

## Install

* Get the repository from github.
	1. `git@github.com:AdrielVelazquez/client_list.git`

* Create the local DB and virtualenv
    1. `make install`

## Run Server

. ./bin/activate && python server.py

## Configurations

Configs can be altered with

`export CLIENT_CONFIG= <server_home_dir>/location/of/config-prod.py`

## Tests

`make test`

## Endpoints

The endpoint accepts the id in the url

`/api/client/<client-id>`

The endpoint returns a json

{"client": client.name, "Exists": client.exists}
