## alpjne

apk add iproute2

for the ip link utility add a namespace in /run/netns

mkdir /run/netns
ln -s /proc/17257/ns/net /run/netns/leaf1

in reality vea and veb should be random names

ip link add vea type veth peer name veb

ip link set vea netns leaf1
ip netns exec leaf1 ip link set vea name e1-1
ip netns exec leaf1 ip link set e1-1 up

ip link set veb netns leaf1
ip netns exec leaf1 ip link set veb name e1-2
ip netns exec leaf1 ip link set e1-2 up

ip netns exec leaf1 ip link