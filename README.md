
# Python auto generated bank_crabi microservice
[![Build Status](https://travis-ci.org/reivaj05/bank_crabi.svg?branch=master)](https://travis-ci.org/reivaj05/bank_crabi) [![codecov](https://codecov.io/gh/reivaj05/bank_crabi/branch/master/graph/badge.svg)](https://codecov.io/gh/reivaj05/bank_crabi) [![docker](https://img.shields.io/badge/docker-image-blue.svg)](https://hub.docker.com/r/javiersv05/bank_crabi/)

## How to run

 - Export variables needed in the container.

```
source scripts/env_vars/develop.sh
```

 - Launch postgres container
```
docker-compose up -d db
```
 - Lauch application container
```
docker-compose up -d crabi
```
 - Run example script
```
python scripts/example.py
```
 - Check logs
```
docker logs bank_crabi_crabi_1
```

# Endpoints

 - [accounts](http://localhost:8000/api/v0.1/bank/accounts/)
 - [transfers](http://localhost:8000/api/v0.1/bank/transfers/)
 - [deposits](http://localhost:8000/api/v0.1/bank/deposits/)
 - [authorizations](http://localhost:8000/api/v0.1/bank/authorizations/)
 - [transactions](http://localhost:8000/api/v0.1/bank/transactions/)
 - [captures](http://localhost:8000/api/v0.1/bank/captures/)
 - [login](http://localhost:8000/rest-auth/login/)

To login:
```
{
	"username": "admin@crabi.com",
	"email": "admin@crabi.com",
	"password": "password"
}
```
# TODOS

 - Add better validation os business rules
 - Add permission for business rules
 - Add tests
 - Improve design

Check [micro-gen](https://github.com/reivaj05/micro-gen) for more information.
