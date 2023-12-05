# kpt cli xample

WARNING: need to use SSH key

## init git

```
gh auth login

gh repo create blueprint --public
gh repo create deployment --public

GITHUB_USER=henderiw
BLUEPRINT_REPO=git@github.com:${GITHUB_USER}/blueprint.git
DEPLOYMENT_REPO=git@github.com:${GITHUB_USER}/deployment.git

git clone ${BLUEPRINT_REPO}
git clone ${DEPLOYMENT_REPO}

cd blueprint
```

## init a package

create a directory

```
mkdir basens
```

Lets initialize the package

```
henderiw@henderiookpro16 blueprint % kpt pkg init basens --description "kpt package for provisioning namespace"
writing basens/Kptfile
writing basens/README.md
writing basens/package-context.yaml
```

Examine the package content

```
henderiw@henderiookpro16 blueprint % kpt pkg tree basens
Package "basens"
├── [Kptfile]  Kptfile basens
└── [package-context.yaml]  ConfigMap kptfile.kpt.dev
```

this creates 3 files:
- kptfile -> file for the kpt file
  - name: basens
  - annotations: config.kubernetes.io/local-config: "true"
- package-context.yml: file for the function config
  - name: kptfile.kpt.dev
  - annotations: config.kubernetes.io/local-config: "true"

## adding resources

```
cd basens
```

Create a Namespace resource using the script with the --dry-run option

```
kube-gen.sh namespace example > namespace.yaml
```

```
kpt fn eval --type mutator --keywords namespace --image set-namespace:v0.4.1 --fn-config package-context.yaml


henderiw@henderiookpro16 basens % kpt fn eval --type mutator --keywords namespace --image set-namespace:v0.4.1 --fn-config package-context.yaml
[RUNNING] "gcr.io/kpt-fn/set-namespace:v0.4.1"
[PASS] "gcr.io/kpt-fn/set-namespace:v0.4.1" in 4.2s
  Results:
    [info]: all namespaces are already "example". no value changed
```

```
kpt fn eval -i set-namespace:v0.4.1 --fn-config package-context.yaml --save -t mutator
```

```
henderiw@henderiookpro16 basens % kpt fn eval -i set-namespace:v0.4.1 --fn-config package-context.yaml --save -t mutator
[RUNNING] "gcr.io/kpt-fn/set-namespace:v0.4.1"
[PASS] "gcr.io/kpt-fn/set-namespace:v0.4.1" in 1s
  Results:
    [info]: all namespaces are already "example". no value changed
Added "gcr.io/kpt-fn/set-namespace:v0.4.1" as mutator in the Kptfile
```

Kpt file
```
apiVersion: kpt.dev/v1
kind: Kptfile
metadata:
  name: basens
  annotations:
    config.kubernetes.io/local-config: "true"
info:
  description: kpt package for provisioning namespace
pipeline:
  mutators:
    - image: gcr.io/kpt-fn/set-namespace:v0.4.1
      configPath: package-context.yaml
```

## permissions

create rolebinding in the repo

```
kube-gen.sh rolebinding app-admin --clusterrole=app-admin --group=example.admin@bigco.com > rolebinding.yaml
```

```
henderiw@henderiookpro16 basens % cat rolebinding.yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: app-admin
  namespace: example
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: app-admin
subjects:
- apiGroup: rbac.authorization.k8s.io
  kind: Group
  name: example.admin@bigco.com
```

1. get the value of package name from configmap in `package-context.yaml`
and use it to update the name of the entry in subjects section of app-admin

```
cat > update-rolebinding.yaml << EOF

apiVersion: fn.kpt.dev/v1alpha1
kind: ApplyReplacements
metadata:
  name: update-rolebinding
  annotations:
    config.kubernetes.io/local-config: "true"
replacements:
- source:
    kind: ConfigMap
    name: kptfile.kpt.dev
    fieldPath: data.name
  targets:
  - select:
      name: app-admin
      kind: RoleBinding
    fieldPaths:
    - subjects.[kind=Group].name
    options:
      delimiter: '.'
      index: 0
EOF
```

the following command adds apply-replacement in the package rendering workflow

```
kpt fn eval -i apply-replacements:v0.1.1 --fn-config update-rolebinding.yaml --save -t mutator
```

## Quota

```
kube-gen.sh quota default --hard=cpu=40,memory=40G > resourcequota.yaml
```

## Publishing the package

```
cd .. && git add basens && git commit -am "initial pkg"

git push origin main

git tag basens/v0 && git push origin basens/v0
```

## consuming the package

cd ../deployment

kpt pkg get ${BLUEPRINT_REPO}/basens/@v0 backend --for-deployment

```
Package "backend":
Fetching git@github.com:henderiw/blueprint@v0
From github.com:henderiw/blueprint
 * tag               basens/v0  -> FETCH_HEAD
Adding package "basens".

Fetched 1 package(s).

Customizing package for deployment.
[RUNNING] "builtins/gen-pkg-context"
[PASS] "builtins/gen-pkg-context" in 0s
  Results:
    [info]: generated package context

Customized package for deployment.
```

```
kpt fn render backend
```

```
git add backend && git commit -am "initial pkg for deployment"
```