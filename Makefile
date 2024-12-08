.DEFAULT_GOAL := all

# Define variables for the arguments
COMPOSE_SERVICE :=

all:
	@echo "Please check Makefile"
kafka-deployment:
	kubectl apply -f minikub/statefulset/deployment/kafka.yaml
	kubectl apply -f minikub/statefulset/deployment/zookeeper.yaml

kafka-delete-deployment:
	kubectl delete -f minikub/statefulset/deployment/kafka.yaml
	kubectl delete -f minikub/statefulset/deployment/zookeeper.yaml

kafka-services:
	kubectl apply -f minikub/statefulset/services/zookeeper.yaml
	kubectl apply -f minikub/statefulset/services/kafka-0.yaml
	kubectl apply -f minikub/statefulset/services/kafka-1.yaml
	kubectl apply -f minikub/statefulset/services/kafka-2.yaml
	kubectl apply -f minikub/statefulset/services/headless-service.yaml
	kubectl apply -f minikub/statefulset/services/bootstrap.yaml

kafka-delete-services:
	kubectl delete -f minikub/statefulset/services/zookeeper.yaml
	kubectl delete -f minikub/statefulset/services/kafka-0.yaml
	kubectl delete -f minikub/statefulset/services/kafka-1.yaml
	kubectl delete -f minikub/statefulset/services/kafka-2.yaml
	kubectl delete -f minikub/statefulset/services/headless-service.yaml
	kubectl delete -f minikub/statefulset/services/bootstrap.yaml

spark-ingress:
	kubectl apply -f minikub/deployment/ingress/spark.yaml
spark-deployment:
	kubectl apply -f minikub/deployment/deployment/spark-master.yaml
	kubectl apply -f minikub/deployment/deployment/spark-worker.yaml
spark-services:
	kubectl apply -f minikub/deployment/services/spark-master.yaml
	kubectl apply -f minikub/deployment/services/spark-worker.yaml
spark-build:
	docker build -t apache-spark:3.4.3 -f docker/spark/Dockerfile .
