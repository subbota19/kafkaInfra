# kafkaInfra

This project provides a Kubernetes deployment for Apache Kafka and Zookeeper using StatefulSet, ensuring stable network
identities and persistent storage, allows for easy scaling by adding more brokers as needed.

## Key Features

* StatefulSet for Kafka: Enables broker scaling (standard Deployment creates pods with random names).
* Bootstrap Service: Acts as an entry point for external clients to connect to the Kafka cluster, and traffic will be
  routed to the appropriate broker (production solution can use Load Balancer).
* Headless Service: Facilitates direct broker discovery within the cluster (without fixed IPs).

Each Kafka broker is accessible via its own DNS name:

`kafka-0.kafka.default.svc.cluster.local`
`kafka-1.kafka.default.svc.cluster.local`
`kafka-2.kafka.default.svc.cluster.local`

* NodePort Services: Expose brokers externally for communication.

# Run Kubernetes cluster on minikube

`minikube status`

If output looks like this:

* Type: Control Plane
* Host: Stopped
* Kubelet: Stopped
* Apiserver: Stopped
* Kubeconfig: Stopped

you have to start minikub:

`minikube start`

For releasing Zookeeper and Kafka services run the following steps:

`kubectl apply -f minikub/statefulset/services/zookeeper.yaml`

`kubectl apply -f minikub/statefulset/services/kafka-0.yaml`

`kubectl apply -f minikub/statefulset/services/kafka-1.yaml`

`kubectl apply -f minikub/statefulset/services/kafka-2.yaml`

`kubectl apply -f minikub/statefulset/services/headless-service.yaml`

`kubectl apply -f minikub/statefulset/services/bootstrap.yaml`

and for deployment:

`kubectl apply -f minikub/statefulset/deployment/kafka`

`kubectl apply -f minikub/statefulset/deployment/zookeeper.yaml`

JUST USEFUL COMMANDS:

`kubectl exec -it $pod_name -- bash`

`kubectl get pv`

`kubectl get pvc`

`kubectl logs zookeepeer-0`

`kubectl describe svc kafka`

`kubectl get pods kafka-766f598bf9-h7h8s -o wide`

/var/lib/kafka/data/

# Spark

./spark-submit --master spark://0.0.0.0:7077 --name spark-stream --class com.stream.EvenNumberFilter local:
///stream_2.13-0.1.0-SNAPSHOT.jar

./spark-submit --master spark://spark-master:7077 --name spark-stream --packages org.apache.spark:
spark-streaming-kafka-0-10_2.12:3.4.3 /opt/spark/process.py

./spark-submit --master spark://spark-master:7077 --name spark-stream --packages org.apache.spark:
spark-streaming-kafka-0-10_2.12:3.4.3,org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.3 /opt/spark/process.py

minikube addons enable ingress

# Clean

sudo du -sh /var/lib/docker/

docker system prune --all --force --volumes

# Kafka scripts

kafka-run-class kafka.tools.GetOffsetShell --bootstrap-server 192.168.49.2:30003 --topic benchmark_fault --time -1

kafka-configs --bootstrap-server 192.168.49.2:30003 --topic benchmark_fault --describe --all

kafka-consumer-groups --bootstrap-server 192.168.49.2:30003 --topic benchmark_fault --list

kafka-console-consumer --bootstrap-server 192.168.49.2:30
003 --topic benchmark_fault --property print.key=true --property key.separator=": "

kafka-console-consumer --bootstrap-server 192.168.49.2:30003 \
--topic benchmark_fault \
--property print.key=true \
--property key.separator=": " \
--property print.timestamp=true \
--property print.offset=true \
--group my-consumer-group

kafka-console-producer --bootstrap-server 192.168.49.2:30003 --topic benchmark_fault