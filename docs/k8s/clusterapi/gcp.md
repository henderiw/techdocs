# gcp cluster api

[info](https://github.com/kubernetes-sigs/cluster-api-provider-gcp/blob/main/docs/book/src/topics/prerequisites.md)

export GCP_REGION=europe-west1
export GCP_PROJECT=srlinux
# Make sure to use same kubernetes version here as building the GCE image
export KUBERNETES_VERSION=1.23.12
export GCP_CONTROL_PLANE_MACHINE_TYPE=n1-standard-2
export GCP_NODE_MACHINE_TYPE=n1-standard-2
export GCP_NETWORK_NAME=default
export CLUSTER_NAME=capi-cluster

gcloud compute networks list --project="${GCP_PROJECT}"
gcloud compute networks describe "${GCP_NETWORK_NAME}" --project="${GCP_PROJECT}"
gcloud compute firewall-rules list --project "$GCP_PROJECT"
gcloud compute routers create "${CLUSTER_NAME}-myrouter" --project="${GCP_PROJECT}" --region="${GCP_REGION}" --network="default"
gcloud compute routers nats create "${CLUSTER_NAME}-mynat" --project="${GCP_PROJECT}" --router-region="${GCP_REGION}" --router="${CLUSTER_NAME}-myrouter" --nat-all-subnet-ip-ranges --auto-allocate-nat-external-ips

## build image


vi ~/.ssh/config

Host 35.195.187.170
  HostName 35.195.187.170
  HostKeyAlgorithms=+ssh-rsa

Host 34.78.166.215
  HostName 34.78.166.215
  HostKeyAlgorithms=+ssh-rsa

# Export the GCP project id you want to build images in.
export GCP_PROJECT_ID=srlinux

# Export the path to the service account credentials created in the step above.
export GOOGLE_APPLICATION_CREDENTIALS="/Users/henderiw/Downloads/srlinux-a50051d117f3.json"

# Clone the image builder repository if you haven't already.
git clone https://github.com/kubernetes-sigs/image-builder.git image-builder

# Change directory to images/capi within the image builder repository
cd image-builder/images/capi

# Run the Make target to generate GCE images.
make build-gce-ubuntu-2004

# Check that you can see the published images.
gcloud compute images list --project ${GCP_PROJECT_ID} --no-standard-images --filter="family:capi-ubuntu-1804-k8s"

# Export the IMAGE_ID from the above
export IMAGE_ID="projects/${GCP_PROJECT_ID}/global/images/<image-name>"