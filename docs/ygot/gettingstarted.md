## install generator:

git clone https://github.com/openconfig/ygot

go build -o $GOBIN/generator generator/generator.go 


$YANGBASE/combined
YGOT_PKG = ygotsrl
YGOT_OUT = pkgsrlygot/SRL_ygot.go

generator -output_file=pkg/$YGOT_PKG/$YGOT_PKG.go -package_name=$YGOT_PKG -generate_fakeroot -fakeroot_name device -path=$YANGBASE/combined/ -typedef_enum_with_defmod -shorten_enum_leaf_names -exclude_state -generate_simple_unions -generate_append -generate_delete -generate_getters -generate_populate_defaults $YANGBASE/combined/

### example
export YANGBASE=/Users/henderiw/Documents/codeprojects/yndd/yang-models/
export YGOT_PKG=ygotnddp
mkdir -p pkg/$YGOT_PKG

generator -output_file=pkg/$YGOT_PKG/$YGOT_PKG.go -package_name=$YGOT_PKG -generate_fakeroot -fakeroot_name device -path=$YANGBASE/combined/ -typedef_enum_with_defmod -shorten_enum_leaf_names -exclude_state -generate_simple_unions -generate_append -generate_delete -generate_getters -generate_populate_defaults $YANGBASE/combined/*.yang
