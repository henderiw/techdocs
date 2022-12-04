# cdk8s

- generates k8s yaml
- written in any language
- cdk8s apps are structured as a tree of constructs
  - root of the tree is an App
  - user defines charts
    - charts are composed of any constructs and eventually k8s resources
  - each chart is rendered ina seperate manifest (yaml file)

## building blocks

constructs:
  - enable composition, abstract strongly types api-types
  - share them through package managers
  - test and version them

chart:
  - container that synthesizes a single k8s manifest (1 or a set of yaml files)
  - namespace and labels can be defined recursively
  
apiObject:
  - represnets an entry in the l8s manifest

dependecies:
  - service.addDependency(namesapce) -> adds a dependency to the namespace for service
    - uses ordering in the manifest to deal with this
  - appChart.addDependency(namespaceChart) -> add a dependency between charts
    - uses names of the manifest 0000 for the first one, 0001 for the second, etc

escape Hatch:
  - jsonPatch

helm chart:

include:
  - includes an existing manifest in the chart

testing:
  - test utilities
  - Testing.app()
  - Testing.chart()
  - Testing.synth(chart)

