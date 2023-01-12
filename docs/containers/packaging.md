# packaging

## VM

packer tries to generalize this but:
- every cloud is a bit different: different builder for gcp, aws, vbox, etc
- when using docker it is very different again

## container images

Work on bare metal, VM(s), etc

option1: clone environment -> build the image locally
-> docker preferred approach


option2: we provide an image for people to consume (everything is installed)
-> issue is the image is heavy (big)
-> docker or packer (given option1 docker seems to be the better approach)
  -> packer make it generic between containers and VMs but this is not relevant

## google workstation

uses docker in docker

[workstation images](https://cloud.google.com/workstations/docs/customize-container-images)

-> entry point is /google/scripts/entrypoint.sh

executes a number of scripts from

/etc/workstation-startup.d/ 


