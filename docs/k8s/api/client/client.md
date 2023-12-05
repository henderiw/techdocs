# different clients


[dynamic client blog1](https://caiorcferreira.github.io/post/the-kubernetes-dynamic-client/)

[dynamic client blog2](https://ymmt2005.hatenablog.com/entry/2020/04/14/An_example_of_using_dynamic_client_of_k8s.io/client-go)

```
func newClient() (dynamic.Interface, error) {
	config, err := rest.InClusterConfig()
	if err != nil {
		return nil, err
	}

	dynClient, err := dynamic.NewForConfig(config)
	if err != nil {
		return nil, err
	}

	return dynClient, nil
}
```

list resources

```
var monboDBResource = schema.GroupVersionResource{Group: "mongodbcommunity.mongodb.com", Version: "v1", Resource: "mongodbcommunity"}

func ListMongoDB(ctx context.Context, client dynamic.Interface, namespace string) ([]unstructured.Unstructured, error)  {
	// GET /apis/mongodbcommunity.mongodb.com/v1/namespaces/{namespace}/mongodbcommunity/
	list, err := client.Resource(monboDBResource).Namespace(namespace).List(ctx, metav1.ListOptions{})
	if err != nil {
		return nil, err
	}

	return list.Items, nil
}
```

