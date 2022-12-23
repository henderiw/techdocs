# jq examples

## conditions

- conditional expressions
  - ==
  - !=
  - >
  - >=
  - <=
  - <
- boolean operators: and, or, not
- if-then-else

### with length 

expression:

```
expression: $discoveryRuleNames | length != 0
expression: $parentTemplateNames | length != 0
```

```
input:
[]

result:
0
```

```
input:
["ss-tmpl2"]
result:
0
```

- length should always be applied to a list
- need a conditional expression

## build a slice

expression:

```
$topoDef | .spec.properties.templates | select((. | length) > 0) | .[].templateRef.name
-> from the last pipe
-> the input is an object
-> the last expression takes the template reference name within the list and builds a list, since the object contains a list
$topoDef | .spec.properties.templates | select((. | length) > 0) | .[] | [.templateRef.name]
-> from the last pipe
-> the input is an object looping over a list
-> we take the template reference name from it and with the [] we put it in a list

```

```
input:
{"apiVersion":"topo.yndd.io/v1alpha1","kind":"Definition","metadata":{"annotations":{"kubectl.kubernetes.io/last-applied-configuration":"{\"apiVersion\":\"topo.yndd.io/v1alpha1\",\"kind\":\"Definition\",\"metadata\":{\"annotations\":{},\"name\":\"fabric2\",\"namespace\":\"default\"},\"spec\":{\"properties\":{\"location\":{\"latitude\":\"a\",\"longitude\":\"b\"},\"templates\":[{\"templateRef\":{\"name\":\"ss-tmpl2\"}}]}}}\n"},"creationTimestamp":"2022-12-20T07:15:17Z","generation":1,"managedFields":[{"apiVersion":"topo.yndd.io/v1alpha1","fieldsType":"FieldsV1","fieldsV1":{"f:metadata":{"f:annotations":{".":{},"f:kubectl.kubernetes.io/last-applied-configuration":{}}},"f:spec":{".":{},"f:properties":{".":{},"f:location":{".":{},"f:latitude":{},"f:longitude":{}},"f:templates":{}}}},"manager":"kubectl-client-side-apply","operation":"Update","time":"2022-12-20T07:15:17Z"}],"name":"fabric2","namespace":"default","resourceVersion":"1618178","uid":"917c4a18-0adb-4443-ba28-22a322bc19bc"},"spec":{"properties":{"location":{"latitude":"a","longitude":"b"},"templates":[{"digitalTwin":false,"templateRef":{"name":"ss-tmpl2"}}]}}}

result:

[
  "ss-tmpl2"
]
```

## build a map

```
expression: .spec.properties.templates[] |  {(.templateRef.name): .templateRef.namespace}
```

```
input:
{"apiVersion":"topo.yndd.io/v1alpha1","kind":"Definition","metadata":{"annotations":{"kubectl.kubernetes.io/last-applied-configuration":"{\"apiVersion\":\"topo.yndd.io/v1alpha1\",\"kind\":\"Definition\",\"metadata\":{\"annotations\":{},\"name\":\"fabric2\",\"namespace\":\"default\"},\"spec\":{\"properties\":{\"location\":{\"latitude\":\"a\",\"longitude\":\"b\"},\"templates\":[{\"templateRef\":{\"name\":\"ss-tmpl2\"}}]}}}\n"},"creationTimestamp":"2022-12-20T07:15:17Z","generation":1,"managedFields":[{"apiVersion":"topo.yndd.io/v1alpha1","fieldsType":"FieldsV1","fieldsV1":{"f:metadata":{"f:annotations":{".":{},"f:kubectl.kubernetes.io/last-applied-configuration":{}}},"f:spec":{".":{},"f:properties":{".":{},"f:location":{".":{},"f:latitude":{},"f:longitude":{}},"f:templates":{}}}},"manager":"kubectl-client-side-apply","operation":"Update","time":"2022-12-20T07:15:17Z"}],"name":"fabric2","namespace":"default","resourceVersion":"1618178","uid":"917c4a18-0adb-4443-ba28-22a322bc19bc"},"spec":{"properties":{"location":{"latitude":"a","longitude":"b"},"templates":[{"digitalTwin":false,"templateRef":{"name":"ss-tmpl2"}}]}}}

result:

{
  "ss-tmpl2": null
}
```

```
expression: 

```

```
[{"apiVersion":"topo.yndd.io/v1alpha1","kind":"Template","metadata":{"annotations":{"kubectl.kubernetes.io/last-applied-configuration":"{\"apiVersion\":\"topo.yndd.io/v1alpha1\",\"kind\":\"Template\",\"metadata\":{\"annotations\":{},\"name\":\"bl-tmpl1\",\"namespace\":\"default\"},\"spec\":{\"properties\":{\"fabric\":{\"borderLeaf\":{\"num\":2,\"vendorInfo\":[{\"platform\":\"IXR-D3\",\"vendorType\":\"nokiaSRL\"}]},\"pod\":[{\"templateRef\":{\"name\":\"pod-type1\"}},{\"templateRef\":{\"name\":\"pod-type1\"}}],\"settings\":{\"maxSpinesPerPod\":2,\"maxUplinksTier2ToTier1\":2,\"maxUplinksTier3ToTier2\":2}}}}}\n"},"creationTimestamp":"2022-12-20T05:56:19Z","generation":1,"managedFields":[{"apiVersion":"topo.yndd.io/v1alpha1","fieldsType":"FieldsV1","fieldsV1":{"f:metadata":{"f:annotations":{".":{},"f:kubectl.kubernetes.io/last-applied-configuration":{}}},"f:spec":{".":{},"f:properties":{".":{},"f:fabric":{".":{},"f:borderLeaf":{".":{},"f:multiHoming":{},"f:num":{},"f:vendorInfo":{}},"f:pod":{},"f:settings":{".":{},"f:maxSpinesPerPod":{},"f:maxUplinksTier2ToTier1":{},"f:maxUplinksTier3ToTier2":{}}}}}},"manager":"kubectl-client-side-apply","operation":"Update","time":"2022-12-20T05:56:19Z"}],"name":"bl-tmpl1","namespace":"default","resourceVersion":"1603717","uid":"438f50f6-0029-4cd3-9316-ea051ac750bf"},"spec":{"properties":{"fabric":{"borderLeaf":{"multiHoming":0,"num":2,"vendorInfo":[{"platform":"IXR-D3","vendorType":"nokiaSRL"}]},"pod":[{"templateRef":{"name":"pod-type1"}},{"templateRef":{"name":"pod-type1"}}],"settings":{"maxSpinesPerPod":2,"maxUplinksTier2ToTier1":2,"maxUplinksTier3ToTier2":2}}}}},{"apiVersion":"topo.yndd.io/v1alpha1","kind":"Template","metadata":{"annotations":{"kubectl.kubernetes.io/last-applied-configuration":"{\"apiVersion\":\"topo.yndd.io/v1alpha1\",\"kind\":\"Template\",\"metadata\":{\"annotations\":{},\"name\":\"pod-type1\",\"namespace\":\"default\"},\"spec\":{\"properties\":{\"fabric\":{\"pod\":[{\"tier2\":{\"num\":2,\"uplinkPerNode\":2,\"vendorInfo\":[{\"platform\":\"IXR-D3\",\"vendorType\":\"nokiaSRL\"}]},\"tier3\":{\"num\":4,\"uplinkPerNode\":2,\"vendorInfo\":[{\"platform\":\"IXR-D3\",\"vendorType\":\"nokiaSRL\"}]}}]}}}}\n"},"creationTimestamp":"2022-12-20T05:56:24Z","generation":1,"managedFields":[{"apiVersion":"topo.yndd.io/v1alpha1","fieldsType":"FieldsV1","fieldsV1":{"f:metadata":{"f:annotations":{".":{},"f:kubectl.kubernetes.io/last-applied-configuration":{}}},"f:spec":{".":{},"f:properties":{".":{},"f:fabric":{".":{},"f:pod":{}}}}},"manager":"kubectl-client-side-apply","operation":"Update","time":"2022-12-20T05:56:24Z"}],"name":"pod-type1","namespace":"default","resourceVersion":"1603731","uid":"a37deecf-e37f-40ec-bb7d-94685df95ae2"},"spec":{"properties":{"fabric":{"pod":[{"tier2":{"multiHoming":0,"num":2,"uplinkPerNode":2,"vendorInfo":[{"platform":"IXR-D3","vendorType":"nokiaSRL"}]},"tier3":{"multiHoming":0,"num":4,"uplinkPerNode":2,"vendorInfo":[{"platform":"IXR-D3","vendorType":"nokiaSRL"}]}}]}}}},{"apiVersion":"topo.yndd.io/v1alpha1","kind":"Template","metadata":{"annotations":{"kubectl.kubernetes.io/last-applied-configuration":"{\"apiVersion\":\"topo.yndd.io/v1alpha1\",\"kind\":\"Template\",\"metadata\":{\"annotations\":{},\"name\":\"ss-tmpl1\",\"namespace\":\"default\"},\"spec\":{\"properties\":{\"fabric\":{\"pod\":[{\"num\":1,\"tier2\":{\"num\":2,\"uplinkPerNode\":4,\"vendorInfo\":[{\"platform\":\"IXR-D3\",\"vendorType\":\"nokiaSRL\"}]},\"tier3\":{\"num\":4,\"uplinkPerNode\":2,\"vendorInfo\":[{\"platform\":\"IXR-D3\",\"vendorType\":\"nokiaSRL\"}]}}],\"settings\":{\"maxUplinksTier2ToTier1\":4,\"maxUplinksTier3ToTier2\":4},\"tier1\":{\"num\":2,\"vendorInfo\":[{\"platform\":\"IXR-D3\",\"vendorType\":\"nokiaSRL\"}]}}}}}\n"},"creationTimestamp":"2022-12-20T05:56:31Z","generation":1,"managedFields":[{"apiVersion":"topo.yndd.io/v1alpha1","fieldsType":"FieldsV1","fieldsV1":{"f:metadata":{"f:annotations":{".":{},"f:kubectl.kubernetes.io/last-applied-configuration":{}}},"f:spec":{".":{},"f:properties":{".":{},"f:fabric":{".":{},"f:pod":{},"f:settings":{".":{},"f:maxSpinesPerPod":{},"f:maxUplinksTier2ToTier1":{},"f:maxUplinksTier3ToTier2":{}},"f:tier1":{".":{},"f:multiHoming":{},"f:num":{},"f:vendorInfo":{}}}}}},"manager":"kubectl-client-side-apply","operation":"Update","time":"2022-12-20T05:56:31Z"}],"name":"ss-tmpl1","namespace":"default","resourceVersion":"1603756","uid":"c26710c1-2d1a-4f79-baa8-835c6ecca003"},"spec":{"properties":{"fabric":{"pod":[{"num":1,"tier2":{"multiHoming":0,"num":2,"uplinkPerNode":4,"vendorInfo":[{"platform":"IXR-D3","vendorType":"nokiaSRL"}]},"tier3":{"multiHoming":0,"num":4,"uplinkPerNode":2,"vendorInfo":[{"platform":"IXR-D3","vendorType":"nokiaSRL"}]}}],"settings":{"maxSpinesPerPod":2,"maxUplinksTier2ToTier1":4,"maxUplinksTier3ToTier2":4},"tier1":{"multiHoming":0,"num":2,"vendorInfo":[{"platform":"IXR-D3","vendorType":"nokiaSRL"}]}}}}},{"apiVersion":"topo.yndd.io/v1alpha1","kind":"Template","metadata":{"annotations":{"kubectl.kubernetes.io/last-applied-configuration":"{\"apiVersion\":\"topo.yndd.io/v1alpha1\",\"kind\":\"Template\",\"metadata\":{\"annotations\":{},\"name\":\"ss-tmpl2\",\"namespace\":\"default\"},\"spec\":{\"properties\":{\"fabric\":{\"pod\":[{\"num\":4,\"tier2\":{\"num\":2,\"uplinkPerNode\":1,\"vendorInfo\":[{\"platform\":\"IXR-D3\",\"vendorType\":\"nokiaSRL\"}]},\"tier3\":{\"num\":4,\"uplinkPerNode\":1,\"vendorInfo\":[{\"platform\":\"IXR-D3\",\"vendorType\":\"nokiaSRL\"}]}},{\"templateRef\":{\"name\":\"pod-type1\"}},{\"templateRef\":{\"name\":\"pod-type1\"}},{\"templateRef\":{\"name\":\"pod-type1\"}},{\"templateRef\":{\"name\":\"pod-type1\"}},{\"templateRef\":{\"name\":\"pod-type1\"}},{\"templateRef\":{\"name\":\"pod-type1\"}}],\"settings\":{\"maxUplinksTier2ToTier1\":4,\"maxUplinksTier3ToTier2\":4},\"tier1\":{\"num\":2,\"vendorInfo\":[{\"platform\":\"IXR-D3\",\"vendorType\":\"nokiaSRL\"}]}}}}}\n"},"creationTimestamp":"2022-12-20T05:56:34Z","generation":1,"managedFields":[{"apiVersion":"topo.yndd.io/v1alpha1","fieldsType":"FieldsV1","fieldsV1":{"f:metadata":{"f:annotations":{".":{},"f:kubectl.kubernetes.io/last-applied-configuration":{}}},"f:spec":{".":{},"f:properties":{".":{},"f:fabric":{".":{},"f:pod":{},"f:settings":{".":{},"f:maxSpinesPerPod":{},"f:maxUplinksTier2ToTier1":{},"f:maxUplinksTier3ToTier2":{}},"f:tier1":{".":{},"f:multiHoming":{},"f:num":{},"f:vendorInfo":{}}}}}},"manager":"kubectl-client-side-apply","operation":"Update","time":"2022-12-20T05:56:34Z"}],"name":"ss-tmpl2","namespace":"default","resourceVersion":"1603769","uid":"731651c6-029d-4788-b8b7-c70f1c860f93"},"spec":{"properties":{"fabric":{"pod":[{"num":4,"tier2":{"multiHoming":0,"num":2,"uplinkPerNode":1,"vendorInfo":[{"platform":"IXR-D3","vendorType":"nokiaSRL"}]},"tier3":{"multiHoming":0,"num":4,"uplinkPerNode":1,"vendorInfo":[{"platform":"IXR-D3","vendorType":"nokiaSRL"}]}},{"templateRef":{"name":"pod-type1"}},{"templateRef":{"name":"pod-type1"}},{"templateRef":{"name":"pod-type1"}},{"templateRef":{"name":"pod-type1"}},{"templateRef":{"name":"pod-type1"}},{"templateRef":{"name":"pod-type1"}}],"settings":{"maxSpinesPerPod":2,"maxUplinksTier2ToTier1":4,"maxUplinksTier3ToTier2":4},"tier1":{"multiHoming":0,"num":2,"vendorInfo":[{"platform":"IXR-D3","vendorType":"nokiaSRL"}]}}}}}]
```