# meshnet

interconnect pods via p2p links using a predefined topology

[meshnet repo](https://github.com/networkop/meshnet-cni)

options:
- veth: used to connect pods on the same node
- vxlan or grpc: used to connect pods on different hosts
- macvlan: used to connect to external resources

## architecture

- datastore: a k8s native etcd backend cluster storing topology information and runtime pod metadata (e.g. pod IP address and NetNS)
- meshnet: a CNI binary responsible for pod's network configuration
- meshnetd: a daemon responsible for communication with k8s and vxlan (or grpc) link configuration updates

## cni configuration

```json
root@kne-control-plane:/etc/cni/net.d# cat 00-meshnet.conflist
{
	"cniVersion": "0.3.0",
	"name": "kindnet",
	"plugins": [
		{
			"bridge": "kind-br",
			"hairpinMode": true,
			"ipMasq": false,
			"ipam": {
				"dataDir": "/run/cni-ipam-state",
				"ranges": [
					[
						{
							"subnet": "10.244.0.0/24"
						}
					]
				],
				"type": "host-local"
			},
			"isDefaultGateway": true,
			"isGateway": true,
			"type": "bridge"
		},
		{
			"capabilities": {
				"portMappings": true
			},
			"type": "portmap"
		},
		{
			"name": "meshnet",
			"type": "meshnet",
			"ipam": {},
			"dns": {}
		}
	]
}
```

## daemonset kne example

default grpc port: 51111

k get -n meshnet daemonsets.apps meshnet -o yaml

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  annotations:
    deprecated.daemonset.template.generation: "1"
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"apps/v1","kind":"DaemonSet","metadata":{"annotations":{},"labels":{"app":"meshnet","k8s-app":"meshnet"},"name":"meshnet","namespace":"meshnet"},"spec":{"selector":{"matchLabels":{"app":"meshnet","name":"meshnet"}},"template":{"metadata":{"labels":{"app":"meshnet","name":"meshnet"}},"spec":{"containers":[{"command":["./entrypoint.sh"],"env":[{"name":"HOST_IP","valueFrom":{"fieldRef":{"fieldPath":"status.hostIP"}}},{"name":"INTER_NODE_LINK_TYPE","value":"GRPC"},{"name":"NODE_NAME","valueFrom":{"fieldRef":{"fieldPath":"spec.nodeName"}}},{"name":"POD_NAME","valueFrom":{"fieldRef":{"fieldPath":"metadata.name"}}},{"name":"POD_NAMESPACE","valueFrom":{"fieldRef":{"fieldPath":"metadata.namespace"}}}],"image":"us-west1-docker.pkg.dev/kne-external/kne/networkop/meshnet:v0.3.2","imagePullPolicy":"IfNotPresent","name":"meshnet","resources":{"limits":{"memory":"10G"},"requests":{"cpu":"200m","memory":"1G"}},"securityContext":{"privileged":true},"volumeMounts":[{"mountPath":"/etc/cni/net.d","name":"cni-cfg"},{"mountPath":"/opt/cni/bin","name":"cni-bin"},{"mountPath":"/var/run/netns","mountPropagation":"Bidirectional","name":"var-run-netns"}]}],"hostIPC":true,"hostNetwork":true,"hostPID":true,"nodeSelector":{"beta.kubernetes.io/arch":"amd64"},"serviceAccountName":"meshnet","terminationGracePeriodSeconds":30,"tolerations":[{"effect":"NoSchedule","operator":"Exists"}],"volumes":[{"hostPath":{"path":"/opt/cni/bin"},"name":"cni-bin"},{"hostPath":{"path":"/etc/cni/net.d"},"name":"cni-cfg"},{"hostPath":{"path":"/var/run/netns"},"name":"var-run-netns"}]}}}}
  creationTimestamp: "2023-07-02T13:42:59Z"
  generation: 1
  labels:
    app: meshnet
    k8s-app: meshnet
    manager: kubectl-client-side-apply
    operation: Update
    time: "2023-07-02T13:42:59Z"
  - apiVersion: apps/v1
    manager: kube-controller-manager
    operation: Update
    subresource: status
    time: "2023-07-02T13:43:19Z"
  name: meshnet
  namespace: meshnet
  resourceVersion: "676"
  uid: 3804ed4d-e523-4f01-8f27-d55c5c8c88ca
spec:
  revisionHistoryLimit: 10
  selector:
    matchLabels:
      app: meshnet
      name: meshnet
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: meshnet
        name: meshnet
    spec:
      containers:
      - command:
        - ./entrypoint.sh
        env:
        - name: HOST_IP
          valueFrom:
            fieldRef:
              apiVersion: v1
              fieldPath: status.hostIP
        - name: INTER_NODE_LINK_TYPE
          value: GRPC
        - name: NODE_NAME
          valueFrom:
            fieldRef:
              apiVersion: v1
              fieldPath: spec.nodeName
        - name: POD_NAME
          valueFrom:
            fieldRef:
              apiVersion: v1
              fieldPath: metadata.name
        - name: POD_NAMESPACE
          valueFrom:
            fieldRef:
              apiVersion: v1
              fieldPath: metadata.namespace
        image: us-west1-docker.pkg.dev/kne-external/kne/networkop/meshnet:v0.3.2
        imagePullPolicy: IfNotPresent
        name: meshnet
        resources:
          limits:
            memory: 10G
          requests:
            cpu: 200m
            memory: 1G
        securityContext:
          privileged: true
        terminationMessagePath: /dev/termination-log
        terminationMessagePolicy: File
        volumeMounts:
        - mountPath: /etc/cni/net.d
          name: cni-cfg
        - mountPath: /opt/cni/bin
          name: cni-bin
        - mountPath: /var/run/netns
          mountPropagation: Bidirectional
          name: var-run-netns
      dnsPolicy: ClusterFirst
      hostIPC: true
      hostNetwork: true
      hostPID: true
      nodeSelector:
        beta.kubernetes.io/arch: amd64
      restartPolicy: Always
      schedulerName: default-scheduler
      securityContext: {}
      serviceAccount: meshnet
      serviceAccountName: meshnet
      terminationGracePeriodSeconds: 30
      tolerations:
      - effect: NoSchedule
        operator: Exists
      volumes:
      - hostPath:
          path: /opt/cni/bin
          type: ""
        name: cni-bin
      - hostPath:
          path: /etc/cni/net.d
          type: ""
        name: cni-cfg
      - hostPath:
          path: /var/run/netns
          type: ""
        name: var-run-netns
  updateStrategy:
    rollingUpdate:
      maxSurge: 0
      maxUnavailable: 1
    type: RollingUpdate
status:
  currentNumberScheduled: 1
  desiredNumberScheduled: 1
  numberAvailable: 1
  numberMisscheduled: 0
  numberReady: 1
  observedGeneration: 1
  updatedNumberScheduled: 1
```

## topology crd example

2 node srl cluster

```yaml
k describe topologies.networkop.co.uk -A
Name:         srl1
Namespace:    2-srl-ixr3dl
Labels:       <none>
Annotations:  <none>
API Version:  networkop.co.uk/v1beta1
Kind:         Topology
Metadata:
  Creation Timestamp:  2023-07-02T13:46:00Z
  Generation:          1
  Managed Fields:
    API Version:  networkop.co.uk/v1beta1
    Fields Type:  FieldsV1
    fieldsV1:
      f:spec:
        .:
        f:links:
    Manager:      kne
    Operation:    Update
    Time:         2023-07-02T13:46:00Z
    API Version:  networkop.co.uk/v1beta1
    Fields Type:  FieldsV1
    fieldsV1:
      f:status:
        .:
        f:container_id:
        f:net_ns:
        f:skipped:
        f:src_ip:
    Manager:         meshnetd
    Operation:       Update
    Subresource:     status
    Time:            2023-07-02T13:46:00Z
  Resource Version:  1421
  UID:               abac5ee0-bb93-4c1b-9eba-a50d3c1f24e4
Spec:
  Links:
    local_intf:  e1-1
    local_ip:
    peer_intf:   e1-1
    peer_ip:
    peer_pod:    srl2
    UID:         0
Status:
  container_id:  5fb4410fd068df026c85f7c3bf4b51cabbe2dd7d2e8d991ff43771a697edc0e8
  net_ns:        /var/run/netns/cni-d99c3faa-4740-86a9-0eff-fcfbb6b5f099
  Skipped:
    link_id:   0
    pod_name:  srl2
  src_ip:      172.20.0.3
Events:        <none>


Name:         srl2
Namespace:    2-srl-ixr3dl
Labels:       <none>
Annotations:  <none>
API Version:  networkop.co.uk/v1beta1
Kind:         Topology
Metadata:
  Creation Timestamp:  2023-07-02T13:46:00Z
  Generation:          1
  Managed Fields:
    API Version:  networkop.co.uk/v1beta1
    Fields Type:  FieldsV1
    fieldsV1:
      f:spec:
        .:
        f:links:
    Manager:      kne
    Operation:    Update
    Time:         2023-07-02T13:46:00Z
    API Version:  networkop.co.uk/v1beta1
    Fields Type:  FieldsV1
    fieldsV1:
      f:status:
        .:
        f:container_id:
        f:net_ns:
        f:src_ip:
    Manager:         meshnetd
    Operation:       Update
    Subresource:     status
    Time:            2023-07-02T13:46:01Z
  Resource Version:  1425
  UID:               f13d35a2-7fd7-4382-b84f-fb29183d0340
Spec:
  Links:
    local_intf:  e1-1
    local_ip:
    peer_intf:   e1-1
    peer_ip:
    peer_pod:    srl1
    UID:         0
Status:
  container_id:  418575e3d02a328722a595558fea29ecdf835dcdacbe786d875a31dcad35e3ea
  net_ns:        /var/run/netns/cni-204bbcb4-7c16-1904-4a66-5b3374b9acd8
  src_ip:        172.20.0.3
Events:          <none>
```

