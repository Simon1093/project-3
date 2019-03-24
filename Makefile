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

unit: up
	docker-compose exec -T web pytest tests/unit/

integration: up
	docker-compose exec -T web pytest tests/integration/

test: up
	docker-compose exec -T web pytest tests/unit/
	docker-compose exec -T web pytest tests/integration/
