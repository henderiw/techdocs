# action javascript/typescript

- native way to implement actions
- node/js is by default installed in the runner, no extra elements required
- input comes native using the context
- allows to run go binaries 
    - process input params
    - download binary (based on version from input + arch/os)
    - run the binary and provide the output


[blog: actions in go](https://full-stack.blend.com/how-we-write-github-actions-in-go.html)
[typescript template](https://github.com/actions/typescript-action)
[javascript example](https://nils-braun.medium.com/writing-a-github-action-in-typescript-from-scratch-3bbd6f92a6cc)
[goreleaser-example](https://github.com/goreleaser/goreleaser-action/)

[github variables](https://docs.github.com/en/actions/learn-github-actions/variables#default-environment-variables)

## important note

run npm run package or run all to ensure the system is in sync

```
npm run package  
npm run all
```

## action.yaml

defines:
- metadata
- input/output of an action
- runs -> uses node and the index.ts or index.js file

```yaml
name: 'kformpkg-action'
description: 'kformpkg-action, a release automation tool for kform providers and modules using oci artifacts'
author: 'kform'

inputs:
  kformVersion:
    description: 'kform version'
    default: 'latest'
    required: false
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
  using: 'node20'
  main: 'dist/index.js'
```