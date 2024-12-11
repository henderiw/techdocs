# common artifact manager

- each app has its own configuration
    - operation Type -> GUI -> create operation
    - workflow -> GUI -> create workflows
    - adaptor -> Host -> bash

Now with CAM
    - UI - install artifact bundle
    - k8s controller: kube API server
        - deployers
        - CRD
        - dependency management
        - deployed using DR (disaster recovery)
        - Ease of use VS Code plugin

Basic Unit
    - artifact metadata
        - files: YAML, JSON, ZIP, script
        - dependency
        - checksum

Artifact bundle
    - Artifact

Is this OCI based, artifact repository?

Deployers: install in specific language of choice
    - short lived kubernetes jobs
    - can be written in any language
    - implemented as a job runner

Applications:
- MDM telemtry mappings
- MDM resync mappings
- NFMP resync
- YANG to YANG
- Device admin operations
- telemtry
- WFM
- MDM
- NSP ACT
- Service fullfilment

build using JAVA using spring framework