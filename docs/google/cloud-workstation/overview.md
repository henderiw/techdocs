# CLoud workstations

## overview

- managed dev environment (built-in securoty and preconfigured/customizable dev environments)
  - access via IDE
  - access via SSH

Workstation clusters:
- created by admin
- in a region attached to a VPC

Workstation configuration (templates)
- Tooling
- Machine specs: VM type/Storage
- Permissions: IAM access management for other devs

Persistent storage:
- run on ephemiral compute engine VM(s) -> deleted when WStation is stopped

DNS hostname

Config updates through restarts

Customized images can be provided

## architecture

- workstation cluster
  - controller (manages the lifecycle of VM instances + other workstation resources
    - uses the compute engine API to manage the lifecycle of resources
  - gateway (network ingress and egress) - DNS <workstation-ID>.<clusterid>.cloudworkstations.dev
  - vpc
    - private service connect: connect cloud workstationcontroller and your VPC
    - workstation:
      - PD: persistent disk -> /home
      - VM:
        - VM gateway
        - Container

## access the workstation

web based

https://workstation-henderiw.cluster-uyzaxmmfljddawt5f7fyllgmuc.cloudworkstations.dev
https://3000-workstation-henderiw.cluster-uyzaxmmfljddawt5f7fyllgmuc.cloudworkstations.dev

[url-port forward](]https://cloud.google.com/workstations/docs/use-port-forwarding)


gcloud beta workstations start-tcp-tunnel \
    --project=PROJECT_ID \
    --region=REGION \
    --cluster=CLUSTER_NAME \
    --config=CONFIG_NAME \
    --local-host-port=:7007 WORKSTATION 7007


gcloud beta workstations start-tcp-tunnel \
  --project=srlinux \
  --cluster=cluster--henderiw \
  --config=nind \
  --region=europe-west1 \
  --local-host-port=:2222 workstation-henderiw 22

ssh -p 2222 \
  -o "UserKnownHostsFile=/dev/null" \
  -o "StrictHostKeyChecking=no" \
  user@localhost