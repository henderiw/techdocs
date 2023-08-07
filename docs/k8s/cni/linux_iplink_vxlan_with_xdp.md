# Host 1 – VETH11 (NS) – VETH12 (HOST) | VETH21 (NS) – VETH22 (HOST)
 
# Host 1 - VXLAN
sudo ip link add vxlan100 type vxlan id 100 dstport 4789 local 10.210.21.227 remote 10.210.21.228 nolearning
sudo ip link add vxlan101 type vxlan id 101 dstport 4789 local 10.210.21.227 remote 10.210.21.228 nolearning
sudo ip link set vxlan100 mtu 5000
sudo ip link set vxlan100 up
sudo ip link set vxlan101 mtu 5000
sudo ip link set vxlan101 up
 
# Host 1 – XDP: input.yaml
links:
    veth12: vxlan100
    veth22: vxlan101
 
$ docker run --net host -v$(pwd):/xc --privileged networkop/xdp-xconnect -conf /xc/input.yaml
 
# Host 1 - Bonding
sudo ip netns exec clab-alpine01-linux ip link add bond0 type bond mode 802.3ad lacp_rate fast miimon 100
sudo ip netns exec clab-alpine01-linux ip link set veth11 down
sudo ip netns exec clab-alpine01-linux ip link set veth21 down
sudo ip netns exec clab-alpine01-linux ip link set dev veth11 master bond0
sudo ip netns exec clab-alpine01-linux ip link set dev veth21 master bond0
sudo ip netns exec clab-alpine01-linux ip link set veth11 up
sudo ip netns exec clab-alpine01-linux ip link set veth21 up
sudo ip netns exec clab-alpine01-linux ip link set bond0 up
sudo ip netns exec clab-alpine01-linux ip addr add 192.168.0.11/24 dev bond0
 
# Host 2 – VETH11 (NS) – VETH12 (HOST) | VETH21 (NS) – VETH22 (HOST)
 
# Host 2 - VXLAN
sudo ip link add vxlan100 type vxlan id 100 dstport 4789 local 10.210.21.228 remote 10.210.21.227 nolearning
sudo ip link add vxlan101 type vxlan id 101 dstport 4789 local 10.210.21.228 remote 10.210.21.227 nolearning
sudo ip link set vxlan100 mtu 5000
sudo ip link set vxlan100 up
sudo ip link set vxlan101 mtu 5000
sudo ip link set vxlan101 up
 
# Host 2 – XDP: input.yaml
links:
    veth12: vxlan100
    veth22: vxlan101
 
$ docker run --net host -v$(pwd):/xc --privileged networkop/xdp-xconnect -conf /xc/input.yaml
 
# Host 2 - Bonding
sudo ip netns exec clab-alpine01-linux ip link add bond0 type bond mode 802.3ad lacp_rate fast miimon 100
sudo ip netns exec clab-alpine01-linux ip link set veth11 down
sudo ip netns exec clab-alpine01-linux ip link set veth21 down
sudo ip netns exec clab-alpine01-linux ip link set dev veth11 master bond0
sudo ip netns exec clab-alpine01-linux ip link set dev veth21 master bond0
sudo ip netns exec clab-alpine01-linux ip link set veth11 up
sudo ip netns exec clab-alpine01-linux ip link set veth21 up
sudo ip netns exec clab-alpine01-linux ip link set bond0 up
sudo ip netns exec clab-alpine01-linux ip addr add 192.168.0.21/24 dev bond0