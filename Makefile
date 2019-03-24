include .env
include ./deploy/.env


ENV=local

use_secrets:
	cp ./secrets/$(ENV)/.env ./deploy/

down:
	docker-compose down

build: use_secrets
	docker-compose build

up: down build
	docker-compose up -d
