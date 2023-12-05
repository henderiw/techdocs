# api extension server

kaas: kube-apiserver
caas: customer-apiserver

why?
- offload kaas -> caas
- special subresource (approve/proxy) -> caas
- etcd storage -> caas

[youtube api-server cncf](https://www.youtube.com/watch?v=M6KjCHWIpgA)

[sample apiserver](https://github.com/kubernetes/sample-apiserver)

[api-server-builder](https://github.com/kubernetes-sigs/apiserver-builder-alpha)
[apiserver concepts](https://github.com/kubernetes-sigs/apiserver-builder-alpha/blob/master/docs/concepts/README.md)

[apiserver builder](https://github.com/kubernetes-sigs/apiserver-builder-alpha/blob/master/docs/tools_user_guide.md)

## api-server builder


init project

go mod init github.com/henderiw/api-aggregated-server

install apiserver-builder

go install sigs.k8s.io/apiserver-builder-alpha/cmd/apiserver-boot

apiserver-boot init repo example.com

## rest.Storage

In the Kubernetes API server codebase, rest.Storage is an interface used for providing storage and CRUD (Create, Read, Update, Delete) operations for a specific Kubernetes resource. It's part of the RESTful storage interface used in the Kubernetes API machinery.

```go
package rest

import (
	"context"
	"k8s.io/apimachinery/pkg/runtime"
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
)

// Storage is an interface for providing storage operations for a specific resource.
type Storage interface {
	// Create creates a new object in the storage.
	Create(ctx context.Context, obj runtime.Object, createValidation metav1.Object) (runtime.Object, error)

	// Update updates an existing object in the storage.
	Update(ctx context.Context, obj runtime.Object, createValidation, updateValidation metav1.Object, forceAllowCreate bool) (runtime.Object, bool, error)

	// Delete deletes an object from the storage.
	Delete(ctx context.Context, name string, deleteValidation metav1.Object, options *metav1.DeleteOptions) (runtime.Object, bool, error)

	// Get retrieves an object from the storage by name.
	Get(ctx context.Context, name string, options metav1.GetOptions) (runtime.Object, error)

	// List lists objects in the storage.
	List(ctx context.Context, options metav1.ListOptions, allowWatchBookmarks bool) (runtime.Object, error)

	// Watch watches changes to objects in the storage.
	Watch(ctx context.Context, options metav1.ListOptions) (watch.Interface, error)
}
```

## rest.TableConvertor

The ConvertToTable method is responsible for taking an object representing structured data and converting it into a table format. The Table returned by this method is then used for displaying information, often in the context of command-line tools or other interfaces where a tabular layout is more readable.

```go
package rest

// TableConverter is an interface for converting structured data to a tabular format.
type TableConverter interface {
	// ConvertToTable converts structured data to a tabular format.
	ConvertToTable(obj interface{}) (Table, error)
}
```