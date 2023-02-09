# fn-runner architecture

## porch

## fn-runner deployment

apiVersion: apps/v1
kind: Deployment
metadata:
  annotations:
    config.k8s.io/owning-inventory: 43f64117017bae04c0c4b805f2bebed6a68ac51e-1669891207669472095
    deployment.kubernetes.io/revision: "1"
    internal.kpt.dev/upstream-identifier: apps|Deployment|porch-system|function-runner
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"apps/v1","kind":"Deployment","metadata":{"annotations":{"config.k8s.io/owning-inventory":"43f64117017bae04c0c4b805f2bebed6a68ac51e-1669891207669472095","internal.kpt.dev/upstream-identifier":"apps|Deployment|porch-system|function-runner"},"name":"function-runner","namespace":"porch-system"},"spec":{"replicas":2,"selector":{"matchLabels":{"app":"function-runner"}},"template":{"metadata":{"labels":{"app":"function-runner"}},"spec":{"containers":[{"command":["/server","--config=/config.yaml","--functions=/functions","--pod-namespace=porch-fn-system"],"env":[{"name":"WRAPPER_SERVER_IMAGE","value":"gcr.io/kpt-dev/porch-wrapper-server:v0.0.12"}],"image":"gcr.io/kpt-dev/porch-function-runner:v0.0.12","imagePullPolicy":"IfNotPresent","name":"function-runner","ports":[{"containerPort":9445}],"readinessProbe":{"exec":{"command":["/grpc-health-probe","-addr","localhost:9445"]}},"resources":{"requests":{"cpu":"125m","memory":"64Mi"}},"volumeMounts":[{"mountPath":"/pod-cache-config","name":"pod-cache-config-volume"}]}],"serviceAccountName":"porch-fn-runner","volumes":[{"configMap":{"name":"pod-cache-config"},"name":"pod-cache-config-volume"}]}}}}
  creationTimestamp: "2023-01-28T08:47:38Z"
  generation: 1
  name: function-runner
  namespace: porch-system
  resourceVersion: "1607"
  uid: d3dcc972-00a8-45a0-ac7d-db269994d737
spec:
  progressDeadlineSeconds: 600
  replicas: 2
  revisionHistoryLimit: 10
  selector:
    matchLabels:
      app: function-runner
  strategy:
    rollingUpdate:
      maxSurge: 25%
      maxUnavailable: 25%
    type: RollingUpdate
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: function-runner
    spec:
      containers:
      - command:
        - /server
        - --config=/config.yaml
        - --functions=/functions
        - --pod-namespace=porch-fn-system
        env:
        - name: WRAPPER_SERVER_IMAGE
          value: gcr.io/kpt-dev/porch-wrapper-server:v0.0.12
        image: gcr.io/kpt-dev/porch-function-runner:v0.0.12
        imagePullPolicy: IfNotPresent
        name: function-runner
        ports:
        - containerPort: 9445
          protocol: TCP
        readinessProbe:
          exec:
            command:
            - /grpc-health-probe
            - -addr
            - localhost:9445
          failureThreshold: 3
          periodSeconds: 10
          successThreshold: 1
          timeoutSeconds: 1
        resources:
          requests:
            cpu: 125m
            memory: 64Mi
        terminationMessagePath: /dev/termination-log
        terminationMessagePolicy: File
        volumeMounts:
        - mountPath: /pod-cache-config
          name: pod-cache-config-volume
      dnsPolicy: ClusterFirst
      restartPolicy: Always
      schedulerName: default-scheduler
      securityContext: {}
      serviceAccount: porch-fn-runner
      serviceAccountName: porch-fn-runner
      terminationGracePeriodSeconds: 30
      volumes:
      - configMap:
          defaultMode: 420
          name: pod-cache-config
        name: pod-cache-config-volume
status:
  availableReplicas: 2
  conditions:
  - lastTransitionTime: "2023-01-28T08:49:00Z"
    lastUpdateTime: "2023-01-28T08:49:00Z"
    message: Deployment has minimum availability.
    reason: MinimumReplicasAvailable
    status: "True"
    type: Available
  - lastTransitionTime: "2023-01-28T08:47:38Z"
    lastUpdateTime: "2023-01-28T08:49:00Z"
    message: ReplicaSet "function-runner-786689f6bd" has successfully progressed.
    reason: NewReplicaSetAvailable
    status: "True"
    type: Progressing
  observedGeneration: 1
  readyReplicas: 2
  replicas: 2
  updatedReplicas: 2

## function upf-ipam pod

apiVersion: v1
kind: Pod
metadata:
  annotations:
    cluster-autoscaler.kubernetes.io/safe-to-evict: "true"
    fn.kpt.dev/reclaim-after: "1675579115"
  creationTimestamp: "2023-01-28T09:01:58Z"
  generateName: nephio-upf-ipam-fn-814d2165-
  labels:
    fn.kpt.dev/image: nephio-upf-ipam-fn-814d2165
  name: nephio-upf-ipam-fn-814d2165-nkq8p
  namespace: porch-fn-system
  resourceVersion: "2971708"
  uid: 2db1c39a-c3ab-4212-ac2b-858e5e3cd798
spec:
  containers:
  - command:
    - /wrapper-server-tools/wrapper-server
    - --port
    - "9446"
    - --
    - function
    image: gcr.io/jbelamaric-public/nephio-upf-ipam-fn:latest
    imagePullPolicy: Always
    name: function
    readinessProbe:
      exec:
        command:
        - /wrapper-server-tools/grpc-health-probe
        - -addr
        - localhost:9446
      failureThreshold: 3
      periodSeconds: 10
      successThreshold: 1
      timeoutSeconds: 1
    resources: {}
    terminationMessagePath: /dev/termination-log
    terminationMessagePolicy: File
    volumeMounts:
    - mountPath: /wrapper-server-tools
      name: wrapper-server-tools
    - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
      name: kube-api-access-7zchd
      readOnly: true
  dnsPolicy: ClusterFirst
  enableServiceLinks: true
  initContainers:
  - command:
    - cp
    - -a
    - /wrapper-server/.
    - /wrapper-server-tools
    image: gcr.io/kpt-dev/porch-wrapper-server:v0.0.12
    imagePullPolicy: IfNotPresent
    name: copy-wrapper-server
    resources: {}
    terminationMessagePath: /dev/termination-log
    terminationMessagePolicy: File
    volumeMounts:
    - mountPath: /wrapper-server-tools
      name: wrapper-server-tools
    - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
      name: kube-api-access-7zchd
      readOnly: true
  nodeName: mgmt-control-plane
  preemptionPolicy: PreemptLowerPriority
  priority: 0
  restartPolicy: Always
  schedulerName: default-scheduler
  securityContext: {}
  serviceAccount: default
  serviceAccountName: default
  terminationGracePeriodSeconds: 30
  tolerations:
  - effect: NoExecute
    key: node.kubernetes.io/not-ready
    operator: Exists
    tolerationSeconds: 300
  - effect: NoExecute
    key: node.kubernetes.io/unreachable
    operator: Exists
    tolerationSeconds: 300
  volumes:
  - emptyDir: {}
    name: wrapper-server-tools
  - name: kube-api-access-7zchd
    projected:
      defaultMode: 420
      sources:
      - serviceAccountToken:
          expirationSeconds: 3607
          path: token
      - configMap:
          items:
          - key: ca.crt
            path: ca.crt
          name: kube-root-ca.crt
      - downwardAPI:
          items:
          - fieldRef:
              apiVersion: v1
              fieldPath: metadata.namespace
            path: namespace

## config file

apiVersion: v1
data:
  pod-cache-config.yaml: |
    gcr.io/kpt-fn/apply-replacements:v0.1.1: 30m
    gcr.io/kpt-fn/apply-setters:v0.2.0: 30m
    gcr.io/kpt-fn/create-setters:v0.1.0: 30m
    gcr.io/kpt-fn/ensure-name-substring:v0.2.0: 30m
    gcr.io/kpt-fn/gatekeeper:v0.2.1: 30m
    gcr.io/kpt-fn/kubeval:v0.2.0: 30m
    gcr.io/kpt-fn/search-replace:v0.2.0: 30m
    gcr.io/kpt-fn/set-annotations:v0.1.4: 30m
    gcr.io/kpt-fn/set-enforcement-action:v0.1.0: 30m
    gcr.io/kpt-fn/set-image:v0.1.1: 30m
    gcr.io/kpt-fn/set-labels:v0.1.5: 30m
    gcr.io/kpt-fn/set-namespace:v0.4.1: 30m
    gcr.io/kpt-fn/starlark:v0.4.3: 30m
    gcr.io/kpt-fn/upsert-resource:v0.2.0: 30m
    gcr.io/kpt-fn/enable-gcp-services:v0.1.0: 30m
    gcr.io/kpt-fn/export-terraform:v0.1.0: 30m
    gcr.io/kpt-fn/generate-folders:v0.1.1: 30m
    gcr.io/kpt-fn/remove-local-config-resources:v0.1.0: 30m
    gcr.io/kpt-fn/set-project-id:v0.2.0: 30m
kind: ConfigMap
metadata:
  annotations:
    config.k8s.io/owning-inventory: 43f64117017bae04c0c4b805f2bebed6a68ac51e-1669891207669472095
    internal.kpt.dev/upstream-identifier: '|ConfigMap|porch-system|pod-cache-config'
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"v1","data":{"pod-cache-config.yaml":"gcr.io/kpt-fn/apply-replacements:v0.1.1: 30m\ngcr.io/kpt-fn/apply-setters:v0.2.0: 30m\ngcr.io/kpt-fn/create-setters:v0.1.0: 30m\ngcr.io/kpt-fn/ensure-name-substring:v0.2.0: 30m\ngcr.io/kpt-fn/gatekeeper:v0.2.1: 30m\ngcr.io/kpt-fn/kubeval:v0.2.0: 30m\ngcr.io/kpt-fn/search-replace:v0.2.0: 30m\ngcr.io/kpt-fn/set-annotations:v0.1.4: 30m\ngcr.io/kpt-fn/set-enforcement-action:v0.1.0: 30m\ngcr.io/kpt-fn/set-image:v0.1.1: 30m\ngcr.io/kpt-fn/set-labels:v0.1.5: 30m\ngcr.io/kpt-fn/set-namespace:v0.4.1: 30m\ngcr.io/kpt-fn/starlark:v0.4.3: 30m\ngcr.io/kpt-fn/upsert-resource:v0.2.0: 30m\ngcr.io/kpt-fn/enable-gcp-services:v0.1.0: 30m\ngcr.io/kpt-fn/export-terraform:v0.1.0: 30m\ngcr.io/kpt-fn/generate-folders:v0.1.1: 30m\ngcr.io/kpt-fn/remove-local-config-resources:v0.1.0: 30m\ngcr.io/kpt-fn/set-project-id:v0.2.0: 30m\n"},"kind":"ConfigMap","metadata":{"annotations":{"config.k8s.io/owning-inventory":"43f64117017bae04c0c4b805f2bebed6a68ac51e-1669891207669472095","internal.kpt.dev/upstream-identifier":"|ConfigMap|porch-system|pod-cache-config"},"name":"pod-cache-config","namespace":"porch-system"}}
  creationTimestamp: "2023-01-28T08:47:37Z"
  name: pod-cache-config
  namespace: porch-system
  resourceVersion: "784"
  uid: 72c7ec7a-e182-4c6c-aa82-31dee5eb23f3