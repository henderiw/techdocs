# wireguard in cilium

- 5.6 kernel includes wireguard
- no key management
  - you generate a private key and derive a public key
  - distribute the public key
  - peer: public key + IP is the key
  - UDP protocol between peers for handshake
- No encryption offload in HW accelerators -> less performat these days against IPSEC
- No L2 header

client - eth0 - lxc0 - wg0 - eth0

flow:
- netlink create a new device cilium-wg0
- private key + derived public key
- K8s ciliumNode annotation with public key