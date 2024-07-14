# KEP

[3rd party resources](https://github.com/kubernetes/design-proposals-archive/blob/main/api-machinery/thirdpartyresources.md)

code location
- kubernetes/staging/src/k8s.io/apiextensions-apiserver

## architecture

- dedicated apiserver (api-extension server)
    - owns the CRD api and is implemented as a dedicated APIserver
    - etcd part prefix: /registry/apiextensions.kubernetes.io
    - controllers:
        - namingController (status controller): 
            - checks the already approved 
            - validate names (singular, plural, shortnames, kind, listkind)
            - setConditions -> 
                - type=NamesAccepted
                - type=Established condition
        - establishingController
            - only act if names are accepted
            - set established condition
        - apiApprovalController
            - looks at annotation and dependent on the setting it will set conditions
            - Not needed: use for kubernetes api(s)
        - nonStructuralSchemaController
            - controller that handles unstructured schema
        - finalizingController
            - handles deletes -> checkes the delete timestamp; 
        - openapiv3: 
            - upon start 
                - openAPIV3Service is initialized (see below)
                - buildV3Spec (for each version of the crd name)
                - 
            - openAPIV3Service ???? (jnitialized when this controller starts)
                - DeleteGroupVersion -> uses the full api path (apis/<group>/<version>)
                - UpdateGroupVersion -> uses the full api path (apis/<group>/<version>)
    apiserver:
        - stores crd
        - delegationHandler
        - versionDiscoveryHandler
        - groupDiscoveryHandler
        - crdHandler
            uses:   
                - versionDiscoveryHandler
                - groupDiscoveryHandler
                - crd informers
                - delegate: http handler -> not found
                - crd options getter
                - admission control
                - establishingController
                - auth resolver
                - static openapi spec (crd open api spec)
            - ServeHTTP
                - based on url a different handler is called
                    - non resource request url
                        - /apis/<group>/<version> -> versionDiscoveryHandler
                        - /apis/<group> -> groupDiscoveryHandler
                        - other -> delegate NotFound (404)
                    - resource req url
                        - check crd exists
                            - if not or error -> return 404 or internal error
                        - chek namespacedScoped or not or nor served
                            - delegate NotFound (404)
                        - check if status is not established/namesaccepted/terminatin
                            - delegate NotFound (404)
                        - getOrCreateServingInfoFor -> returns the storage information (either build or returned from storage)
                            - what happens when building the storage layer
                                - get scope/storages
                                    // Scope/Storages per version.
                                    requestScopes := map[string]*handlers.RequestScope{}
                                    storages := map[string]customresource.CustomResourceStorage{}
                                    statusScopes := map[string]*handlers.RequestScope{}
                                    scaleScopes := map[string]*handlers.RequestScope{}
                                    deprecated := map[string]bool{}
                                    warnings := map[string][]string{}
                                    structuralSchemas := map[string]*structuralschema.Structural{}
                                - map key -> is versionName e.g. v1alpha1, v1beta1, v1, etc
                                - build the relevant resources
                            - returns crdInfo
                                - if not found or error -> return 404
                                - if not served -> return 404
                                - if depreciated -> add warning to return
                                - build handler
                                    - subresources (status/scale/other)
                                    -> serveResource
                                    -> serveStatus
                                    -> serveScale
            - serveResource
                - handles: get, list, watch, create, update, patch, delete, deleteCollection
            - serveStatus
                - handles get, update, patch
            - serveScale
                - handles get, update, patch
            - createCustomResourceDefinition
            - updateCustomResourceDefinition
            - removeStorage_locked
                - called from create/updateCustomResourceDefinition
                - removeStorage_locked removes the cached storage with the given uid as key from the storage map. This function updates r.customStorage with the cleaned-up storageMap and tears down the old storage.
            - removeDeadStorage
            - tearDown
            - destroy
            - GetCustomResourceListerCollectionDeleter
            - getOrCreateServingInfoFor


        
