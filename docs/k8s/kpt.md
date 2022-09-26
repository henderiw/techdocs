# kpt

package cebtric tool chain that enables WYSIWYG

WYSIWYG => what you see is what you get

## introduction

- deploy config and policies consistently (GITOPS)
- version controlled deploy process
  - typically we dont have an undo
  - track changes like document control

## why

impertative:
- easier to use and adopt
- difficult to use and scale -> lack of reusibility & automation

IaaC: (terraform/helm)
- more power and control (templating, DSL, general program languages) -> manual hman authoring and editing
- ARTISINAL AUTOMATION

Code like presentation:
- values.yml -> EXCESSIVE PARAMETERIZATION

UI: new approach needed

Config as Data
- KRM data model
- package: config data -> source of truth
- seperate code that acts on config -> functions
- abstract storage

## components

- kpt cli:
  - supports package, function operations and deployment
- function SDKs:
  - support for go, typescript and starlark (python alike)
- function catalog:
  - off the shelf tested functions
- package orchestrator (porch):
  - control plane for CRUD operation on packages
  - evaluates functions on package data
  - Support OCI and Git
- config sync:
  - build on top of git-sync and kustomize
- backstage ui plugin
  - demo WYSIWYG experience

         +------------
UI <---> |           |
         |  PORCH    |
KPT <--> |           |
         +-----------+
             Repo
               |
         +-----+------+
      config sync    config sync


## PORCH API

- package revision:
  - packageName
  - Revision
  - RepositoryName
  - Parent
  - Lifecycle
  - Tasks (Init, Clone, Merge, Edit, Eval)

- package revision resources
  - PackageName
  - Revision
  - RepositoryName
  - Resources

- function
  - image
  - repository ref
  - functionType (validate/mutate)
  - functionConfig (typeMeta [kind/apiversion], required fields)
  - KeyWords
  - Description
  - Documentation URL