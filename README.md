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

For releasing Zookeeper and Kafka run the following steps:

`kubectl apply -f kub/networks/network-policy.yaml`

`kubectl apply -f kub/networks/zookeeper-service.yaml`

`kubectl apply -f kub/networks/kafka-service.yaml`

`kubectl apply -f kub/deployment/zookeeper-deployment`

`kubectl apply -f kub/deployment/kafka-deployment.yaml`

 /var/lib/kafka/data/
 
 kafka-topics --bootstrap-server 192.168.49.2:30003 --describe --topic yyy
 
kubectl cp kafka-0:/var/lib/kafka /home/yauheni/kafka

kafka-console-consumer --bootstrap-server 192.168.49.2:30003 --topic test
