.DEFAULT_GOAL := all

# Define variables for the arguments
COMPOSE_SERVICE :=

all:
	@echo "Please check Makefile"
kafka-deployment:
	kubectl apply -f minikub/statefulset/deployment/kafka.yaml
	kubectl apply -f minikub/statefulset/deployment/zookeeper.yaml
kafka-services:
	kubectl apply -f minikub/statefulset/services/zookeeper.yaml
	kubectl apply -f minikub/statefulset/services/kafka-0.yaml
	kubectl apply -f minikub/statefulset/services/kafka-1.yaml
	kubectl apply -f minikub/statefulset/services/kafka-2.yaml
	kubectl apply -f minikub/statefulset/services/headless-service.yaml
	kubectl apply -f minikub/statefulset/services/bootstrap.yaml
spark-build:
	docker build -t apache-spark:3.4.0 -f docker/spark/Dockerfile .
docker-compose-up:
	docker compose up
docker-compose-build:
	docker compose build
docker-compose-down:
	docker compose down --volumes
docker-compose-start:
	docker compose start $(COMPOSE_SERVICE)
docker-compose-stop:
	docker compose stop
