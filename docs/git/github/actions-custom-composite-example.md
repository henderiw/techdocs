# action composite

- you need to install a go environment before you can use it
- input need logic in action.yaml file
- allows to run go binaries 
    - process input params
    - download binary (based on version from input + arch/os)
    - run the binary and provide the output


## action.yaml file

need to install go
need to map input variables

```yaml
name: 'KformPackage Action'
description: 'KformPackage Action, a release automation tool for kform providers and modules using oci artifacts'
author: 'kform'

inputs:
  sourcePkgDir:
    description: 'Directory from which the package is sourced'
    default: config
    required: false
  targetPkgRegistryHostname:
    description: 'Hostname of the container registry e.g. ghcr.io where the oci artifact image is stored'
    required: true
  targetPkgNamespace:
    description: 'Name of the oci artifact package namespace, defaults to the owner/organization of the repository'
    required: false
  targetPkgName:
    description: 'Name of the oci artifact package (module or provider), defaults to the name of the repository'
    required: false
outputs:
  artifacts:
    description: 'Build result artifacts'

runs:
  using: composite
  steps:
  - run: go run main.go
    shell: bash
    env:
      INPUT_SRC_PKG_DIR: ${{ inputs.sourcePkgDir }}
      INPUT_TARGET_PKG_REGISTRY_HOSTNAME: ${{ inputs.targetPkgRegistryHostname }}
      INPUT_TARGET_PKG_NAMESPACE: ${{ inputs.targetPkgNamespace }}
      INPUT_TARGET_PKG_NAME: ${{ inputs.targetPkgName }}
```