# kpt cli ndd-core example

create github project yndd/blueprint

mkdir basecore

kpt pkg init basecore --description "kpt package for provisioning ndd core"

kpt fn eval --type mutator --keywords image --image set-namespace:v0.4.1 --fn-config package-context.yaml