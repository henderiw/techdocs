## multiple clusters

kubectl config delete-cluster kind-ndd
kubectl config delete-context kind-ndd

cp ~/.kube/config ~/.kube/config.bak && KUBECONFIG=~/.kube/config:/tmp/newconfig kubectl config view --flatten > /tmp/config && mv /tmp/config ~/.kube/config

