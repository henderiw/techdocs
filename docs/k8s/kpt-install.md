# install kpt

## cli

## porch

### install gcloud

https://cloud.google.com/sdk/docs/install

### install gke cluster

gcloud config set project srlinux

gcloud container clusters create-auto --region europe-west1 porch-dev

gcloud container clusters create --region europe-west1 porch-dev

gcloud container clusters get-credentials --region europe-west1 porch-dev

### install porch

download the bundle
https://github.com/GoogleContainerTools/kpt/releases

mkdir porch-install
tar xzf deployment-blueprint.tar.gz -C porch-install
kubectl apply -f porch-install

## install config sync

download the bundle
https://github.com/GoogleContainerTools/kpt-config-sync/releases

mkdir config-sync
tar -xzf deployment-blueprint.tar.gz -C config-sync
kubectl apply -f config-sync

## ui

in tmp directory

git clone https://github.com/GoogleContainerTools/kpt-backstage-plugins.git
cd kpt-backstage-plugins
docker build --target backstage-app-local --tag kpt-backstage-plugins .

docker run -v ~/.kube/config:/root/.kube/config -v ~/.config/gcloud:/root/.config/gcloud -p 7007:7007 kpt-backstage-plugins

## example nginx

in tmp directory

kpt pkg get https://github.com/GoogleContainerTools/kpt/package-examples/nginx@v0.9
