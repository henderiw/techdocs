#

  //--machine-type=n2d-standard-16 \
  // --min-cpu-platform="Intel Haswell" \

gcloud compute instances create playground2 \
  --enable-nested-virtualization \
  --zone=europe-west1-b \
  --machine-type=n2-standard-16
  --image-family=ubuntu-2204-lts \
  --image-project=ubuntu-os-cloud \
  --boot-disk-size=256GB \
  --boot-disk-type=pd-standard

grep -cw vmx /proc/cpuinfo

gcloud compute instances delete playground2 


gcloud resource-manager org-policies \
  describe constraints/compute.disableNestedVirtualization \
  --project=srlinux --effective


gcloud resource-manager org-policies \
  disable-enforce compute.disableNestedVirtualization \
  --project=srlinux



gcloud compute instances export playground \
  --destination=playground.yaml \
  --zone=europe-west1-b

gcloud compute instances update-from-file playground \
  --source=playground.yaml \
  --most-disruptive-allowed-action=RESTART \
  --zone=europe-west1-b

gcloud resource-manager org-policies describe constraints/compute.disableNestedVirtualization --project srlinux --effective