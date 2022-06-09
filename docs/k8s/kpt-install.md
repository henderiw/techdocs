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


## repository registration with github or oci

```
- create git repo -> https://github.com/henderiw/blueprints.git
- create personal access token for porch to authenticate to git (repo access rights)
```

commands:
- kpt alpha repo register <repo>
  - local commands
    - branch: default is main branch
    - deployment: tags the repository as a deployment repo
    - description
    - directory: directory within the repo where packages are found (default is root)
    - name: (default last segment of the name of the repo)
    - repo-basic-username: basic authentication to a repo
    - repo-basic-password: basic authentication to a repo
- kpt alpha repo unregister <repo>
- kpt alpha repo get <repo>

Example

```
GITHUB_USERNAME=
GITHUB_TOKEN=
kpt alpha repo register \
  --namespace default \
  --repo-basic-username=${GITHUB_USERNAME} \
  --repo-basic-password=${GITHUB_TOKEN} \
  https://github.com/${GITHUB_USERNAME}/blueprints.git
kpt alpha repo get
kpt alpha repo unregister blueprints --namespace default
```

## package discovery and introspection

kpt alpha rpkg 
    ->  interact with packages managed by porch
    -> r stands for remote

output:
- LATEST: indictes the latest revision
- LIFECYCLE: published, draft or proposed

Name are represnted as hash since the name convention of K8s/KRM does not satisfy

commands:
- kpt alpha rpkg get -> list package revisions in registered repos
- kpt alpha rpkg pull -> read the package resources/pull the content of the package resources

## authoring packages

- kpt alpha rpkg init <package-name>: -> initializes a new package revision in the target repository
  - local commands:
    - directory:
    - ref: branch, tag or SHA
    - repository:
    - revision:
    - strategy: resource-merge, fast-forward, force-delete-replace (default: resource-merge)
- kpt alpha rpkg clone: -> create a clone of an existing package revision; Creates a clone of a source package in the target repository.
- kpt alpha rpkg copy: -> create a new package revision from an existing one; Creates a copy of a source package in the target repository to start creation of a new revision of the package; can be used to create a new revision of an existing package. It is a means to modifying an already published package revision.
- kpt alpha rpkg push: Pushes package resources into a remote package
- kpt alpha rpkg del -> delete a package revision

## lifecycle and approval

- kpt alpha rpkg propose:
- kpt alpha rpkg approve: -> approve a proposal to publish a package revision
- kpt alpha rpkg reject:

## deploy

- kpt alpha sync create: Creates a sync of a package in the deployment cluster.
- kpt alpha sync del: 
- kpt alpha sync get