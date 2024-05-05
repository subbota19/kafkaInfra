# BeamStreamProcessing

`kubectl exec -it $pod_name -- bash`

`kubectl get pv`

`kubectl get pvc`

`kubectl logs zookeepeer-0`

`kubectl describe svc kafka`

`kubectl get pods kafka-766f598bf9-h7h8s -o wide`

# Run Kubernetes cluster on minikub

`minikub status`

If output looks like this:

* Type: Control Plane
* Host: Stopped
* Kubelet: Stopped
* Apiserver: Stopped
* Kubeconfig: Stopped

you have to start minikub:

`minikub start`

For releasing Zookeeper and Kafka services run the following steps:

`kubectl apply -f minikub/statefulset/services/zookeeper.yaml`

`kubectl apply -f minikub/statefulset/services/kafka-0.yaml`

`kubectl apply -f minikub/statefulset/services/kafka-1.yaml`

`kubectl apply -f minikub/statefulset/services/kafka-2.yaml`

`kubectl apply -f minikub/statefulset/services/headless-service.yaml`

`kubectl apply -f minikub/statefulset/services/bootstrap.yaml`

and for deployment:

`kubectl apply -f minikub/statefulset/deployment/kafka`

`kubectl apply -f minikub/statefulset/zookeeper.yaml`

 /var/lib/kafka/data/
 
kafka-topics --bootstrap-server 192.168.49.2:30003 --describe --topic yyy
 
kubectl cp kafka-0:/var/lib/kafka /home/yauheni/kafka

kafka-console-consumer --bootstrap-server 192.168.49.2:30003 --topic test
