# k8s api overview

[api overview](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md)

[api extension server](https://pkg.go.dev/sigs.k8s.io/apiserver-runtime)

[api k8s repo explanation](https://iximiuz.com/en/posts/kubernetes-api-go-types-and-common-machinery/)

[extend kubectl with plugins](https://kubernetes.io/docs/tasks/extend-kubectl/kubectl-plugins/)

[cloud provider](https://github.com/kubernetes?utf8=✓&q=cloud-provider&type=&language=)

[cloud provider manager](https://kubernetes.io/docs/tasks/administer-cluster/developing-cloud-controller-manager/)

[cni](https://github.com/containernetworking/cni)
[device plugin](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/)
[csi](https://github.com/container-storage-interface/spec/blob/master/spec.md)
[cri](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-node/container-runtime-interface.md)

[dynamic admission control](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/)

[authentication](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#webhook-token-authentication)

control loop:
- read the state of the resources -> event driven
- change the state of child resources
- update the status of the resource
- repeat

architecture:
- informers
- [work queues](https://pkg.go.dev/k8s.io/client-go/util/workqueue)

[k8s mechanism](https://dominik-tornow.medium.com/the-mechanics-of-kubernetes-ac8112eaa302)
[level triggering](https://hackernoon.com/level-triggering-and-reconciliation-in-kubernetes-1f17fe30333d)
[optimistic concurrency]()
-> using resource version (when you update you check the resource version and if it changed the update fails)
-> perfect fir for level based systems

[google borg](https://research.google/pubs/large-scale-cluster-management-at-google-with-borg/)

[operators](https://www.redhat.com/en/blog/introducing-operators-putting-operational-knowledge-into-software)
[operators talk](https://www.youtube.com/watch?v=6Csf0g9BTr4)


Master:
- API Server
    - HTTP API: JSON/protobuf
    - HTTP verbs [json patch](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/update-api-object-kubectl-patch/#use-a-json-merge-patch-to-update-a-deployment)
    - API reference
        - kind
        - group
        - version
        - resource
        - subresources
    - GVR <-> GVK => RESTmapping
    - HandlerChain [apiserver/pkg/server/config.go](https://github.com/kubernetes/kubernetes/blob/66674f549626cc41f04e475d2c0e865116c4cd40/staging/src/k8s.io/apiserver/pkg/server/config.go#L543)
        - Mux [hndler](https://github.com/kubernetes/kubernetes/blob/66674f549626cc41f04e475d2c0e865116c4cd40/staging/src/k8s.io/apiserver/pkg/server/handler.go#L42:6)
        - [handler per api group](https://github.com/kubernetes/kubernetes/blob/66674f549626cc41f04e475d2c0e865116c4cd40/staging/src/k8s.io/apiserver/pkg/endpoints/groupversion.go#L99)
        - [register handler](https://github.com/kubernetes/kubernetes/blob/66674f549626cc41f04e475d2c0e865116c4cd40/staging/src/k8s.io/apiserver/pkg/endpoints/installer.go#L183)
        - hanlderchain
            - WithPanicRecovery(): recovery and log panics 
                [code](https://github.com/kubernetes/kubernetes/blob/76e9089d0ee657faf6603876dfe077df94b19f51/staging/src/k8s.io/apiserver/pkg/server/filters/wrap.go#L29)
            - WithRequestInfo(): ataches the requestinfo to the context
                [code](https://github.com/kubernetes/kubernetes/blob/7f23a743e8c23ac6489340bbb34fa6f1d392db9d/staging/src/k8s.io/apiserver/pkg/endpoints/filters/requestinfo.go#L28)
            - WithWaitGroup(): adds all long running requests to a waitgroup -> graceful shutdown
                [code](https://github.com/kubernetes/kubernetes/blob/d902351c991a68fa76de9935a485afeb1f780c11/staging/src/k8s.io/apiserver/pkg/server/filters/waitgroup.go#L47)
            - WithTimeoutForNonLongRunningRequests(): timees out non log running requests
                [code](https://github.com/kubernetes/kubernetes/blob/d902351c991a68fa76de9935a485afeb1f780c11/staging/src/k8s.io/apiserver/pkg/server/filters/timeout.go#L37)
            - WIthCORS(): provides a CORS implementation
                [code](https://github.com/kubernetes/kubernetes/blob/d902351c991a68fa76de9935a485afeb1f780c11/staging/src/k8s.io/apiserver/pkg/server/filters/cors.go#L36)
            - WithAuthentication(): attempts to auth a request to a human/machine and stores the user info in the provided context.
                [code](https://github.com/kubernetes/kubernetes/blob/d902351c991a68fa76de9935a485afeb1f780c11/staging/src/k8s.io/apiserver/pkg/endpoints/filters/authentication.go#L42)
            - WithAudit(): audit logging info (IP, etc)
                [code](https://github.com/kubernetes/kubernetes/blob/016e9d5c06089774c6286fd825302cbae661a446/staging/src/k8s.io/apiserver/pkg/admission/audit.go#L40)
            - WithImpersonation(): handles user impersonation by checking requests that attempt to change the user (like sudo)
                [code](https://github.com/kubernetes/kubernetes/blob/a3ccea9d8743f2ff82e41b6c2af6dc2c41dc7b10/staging/src/k8s.io/apiserver/pkg/endpoints/filters/impersonation.go#L41)
            - WithMaxInflightLimit(): limits the # of inflight requests
                [code](https://github.com/kubernetes/kubernetes/blob/24643fd1163857a507e40f4bceb303c5b44d2d8f/staging/src/k8s.io/apiserver/pkg/server/filters/maxinflight.go#L97)
            - WithAuthorization(): checks permissions -> RBAC handlers
                [code](https://github.com/kubernetes/kubernetes/blob/a3ccea9d8743f2ff82e41b6c2af6dc2c41dc7b10/staging/src/k8s.io/apiserver/pkg/endpoints/filters/authorization.go#L45)
        - after the handlerchain is passed
            - /, /version, /apis, /healtz are directly handled (nonRESTful apis)
            -  request for RESTFul resources go through admissions chain
                - mutation or validation chains with webhooks
                - first phase: mutation
                - 2nd phase is for validation
- Controller Manager
- Scheduler



http://bit.ly/2WWlcxk