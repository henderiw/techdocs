# cloudran

## terminology

- cloudRAN or vRAN
- open RAN
- O-RAN
- OpenRAN

## goals

- avoid HW lockin
- volumes

overall dedicated HW solution are typically more cost effective
-> RAN NIC is what Nokia pushes to overcome this challenge
-> RAN NIC is eCPRI now, no RoE

How big is this market based on the above?
- Verizon is pushing to go to cloud RAN, Ericsson is also dragging their feet
- Samsung is full cloud RAN in Verizon

## cell site GW

### distributed cloud ran

- CPRI: conversion is vendor specific -> ORAN is the standard solution

32 port box
    21 AP port to radio total
    - eCPRI: 6-9 ports could be 50G
    - 1G is for legacy BBU
    - vDU with RAN NIC -> QSFP56DD (CPRI and eCPRI natively) -> acting as 100G QSFP28
      - 2-3 ran nic cards?
      - 2x10G Management
    - vCu
    - backhaul: 25G/ QSFP28 uplink

GNSS HW capable

### centralized cloud ran

like SAS24

no GNSS, clock is connected to TOR or anyhaul aggregation switch
