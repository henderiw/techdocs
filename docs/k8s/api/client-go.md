# client go

[client-go](https://github.com/kubernetes/client-go)

executes REST verbs
- CREATE, GET, LIST, UPDATE, DELETE, PATCH, WATCH


## kubernetes API types

[kubernetes api types](https://github.com/kubernetes/api)

core api types

## api machinery

[kubernetes api machinery](https://github.com/kubernetes/apimachinery)

contains many generic API types
- ObjectMeta
- TypeMeta
- GetOptions
- ListOptions

## creating a client

```go
// gets a rest config
// outside the cluster we use by default ~/.kube/config

// `/var/run/secrets/kubernetes.io/serviceaccount
config, err := clientcmd.BuildConfigFromFlags("", kubeconfig)
// 
clientset, err := kubernetes.NewFromConfig(config)
```

```go
// inside the cluster you get a kubeconfig via serviceaccounts 
config, err := rest.InClusterConfig()
// uses protobug iso jspn which is the default
config.ContentType = "application/vnd.kubernetes.protobuf"
config.UserAgent = "tbd"
```

```go
pod, err := clientset.CoreV1().Pods("book").Get("example", metav1.GetOptions{})
```

## versioning

1. the client has to match the version the server supports
2. apimachinary features CreateOptions, GetOptions, etc -> get new features

[https://github.com/kubernetes/client-go](compatibility)

api versions

- v1alpha1, v1alpha2, v1alpha3
    - might go away or change any time w/o backward compatibility
    - data might get dropped or become inaccessible
    - often disabled by the admin
- v1beta1, v1beta2, v2beta1
    - coexist at least one version with the stable version
    - try not to change w/o incompatibility
    - will not be dropped or become inaccessible
    - often enabled in clusters
- v1, v2, v3
    - they will stay
    - compatible

objects are stored in etcd in a specific version -> storage version


## kubernetes objects in go

### runtime.Object

```go
type Object interface {
    // Get or Set GVK
    GetObjectKind() schema.ObjectKind 
    // copy the object
    DeepCopyObject() Object
}

type ObjectKind interface {
    SetGroupversionKind(kind GroupVersionKind)
    GroupVersionKind() GroupVersionKind
}
```

### TypeMeta

-> the client does not return apiversion and kind
-> this gets added by the serializer through the scheme

### Objectmeta

- metadata
    - name
    - namespace
    - uid
    - resourceVersion -> optimistic concurrency
    - creationTimestamp
    - deletionTimestamp
    - labels
    - annotations
    - ...

### spec/status

## ClientSets

a clientset gives access to clients for multiple API groups and resources

every clientset gives also access to the discovery client

## status subresource

- extra http endpoint suffixed with /status

```go
// spec 
"/apis/apps/v1beta1/namespaces/ns/deployments/name"
// status
"/apis/apps/v1beta1/namespaces/ns/deployments/name/status"
```

## deletecollection

delete multiple objects of a namespace at once
or labelSelector/fieldSelector

## watches

```go
type Interface interface {
    Stop()
    ResultChan() <- chan Event
}
```

eventType
- ADDED
- MODIFIED
- DELETED
- ERROR

## informers and caches

watch verb/interface -> events
- in memory caching and fast, indexed lookups by name and other properties

watch event -> Informer (store) -> Lister (get, list, )
                                -> Informer (event handler)


informers
- take care of error handling
    - relist
    - resync timer
- shared informer factory (shared load per GVR) per resource a single informer
- can be constrained to namespaces
- 


```go
clientset, err := kubernetes.NewFromConfig(config)
informerFactory := informers.NewSharedInformerFactory(clientset, time.Second * 30)
podInformer := informerFactory.Core(),V1().Pods()
podInformer.Informer().AddEventHandler(cache.ResourceHandlerFuncs{
    AddFunc: func(new any),
    UpdateFunc: func(old, new any),
    DeleteFunc: func(obj any),
})
informerFactory.Start(wait.NeverStop)
informerFactory.WaitForCacheSync(wait.NeverStop)
pod, err := podInformer.Lister().Pods("programming.kubernetes").Get("client.go)
```

updates are handled using watch events and will trigger the event handlers

## work queue

[work queue](https://github.com/kubernetes/client-go/tree/master/util/workqueue)


```go
type Interface interfac{
    Add(item any)
    Len() int
    Get(item any, shutdown bool)
    Done(item any)
    Shutdown()
    ShuttingDown()
}
```

api machinery
- kinds
- resources
- REST mapping: mapping GVR to GVK
    -> discovery REST mapping
- Scheme
    -> maps go types to GVK
    -> registers the golang types, but also defaulters and conversions

golang type --(scheme)--> GVK --(RESTMapper)--> GVR --(client) --> HTTP


http://bit.ly/2ZA6dWH