# BeamStreamProcessing

`kubectl exec -it $pod_name -- bash`

`kubectl get pv`

`kubectl get pvc`

`kubectl logs zookeepeer-0`

`kubectl describe svc kafka`

`kubectl get pods kafka-766f598bf9-h7h8s -o wide`

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

 /var/lib/kafka/data/
 
kafka-topics --bootstrap-server 192.168.49.2:30003 --describe --topic yyy
 
kubectl cp kafka-0:/var/lib/kafka /home/yauheni/kafka

kafka-console-consumer --bootstrap-server 192.168.49.2:30003 --topic test

docker exec -i -t 78a6fbac7acf /bin/bash

./spark-submit --master spark://0.0.0.0:7077 --name spark-stream --class com.stream.EvenNumberFilter  local:///stream_2.13-0.1.0-SNAPSHOT.jar

[//]: # (./spark-submit --master spark://spark-master:7077 --name spark-stream --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.3 /opt/spark/process.py)

./spark-submit --master spark://spark-master:7077 --name spark-stream --packages org.apache.spark:spark-streaming-kafka-0-10_2.12:3.4.3 /opt/spark/process.py

./spark-submit --master spark://spark-master:7077 --name spark-stream --packages org.apache.spark:spark-streaming-kafka-0-10_2.12:3.4.3,org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.3 /opt/spark/process.py

minikube image load apache-spark:3.4.3
kubectl delete deployment spark-master
kubectl delete deployment spark-worker

minikube addons enable ingress

docker builder prune
docker system df

minikube addons enable ingress

# Clean

sudo du -sh /var/lib/docker/

docker system prune --all --force --volumes

minikube ssh

