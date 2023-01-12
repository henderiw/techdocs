

gcloud artifacts repositories list
gcloud artifacts repositories list


gcloud auth configure-docker europe-docker.pkg.dev

docker tag nind europe-docker.pkg.dev/srlinux/eu.gcr.io/nind:latest
docker push europe-docker.pkg.dev/srlinux/eu.gcr.io/nind:latest