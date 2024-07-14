# infiniband

## terminology

HCA: Host channel adaptor (connects directly to the memory)
TCA: 
RAS: Reliability, Availability and Serviciability
LRH: local route header
VL: Virtual Links -> QoS
SL: service level -> QoS


IBTA is responsible for maintaining and enhancing the specification

## introduction

1. amdahl-law -> baclance between CPU performance, memory BW and I/O performance
2. moore's law -> double performance every 18 months
3. I/O is gouverned by mechanical and electrical limitations

Bus architectures (PCI) -> dictate the mechanical connections of a computer system and network interface cards and semiconductors.
- early 90's
- from 32 bit/sec with 33Mhz to 64 bit/sec with 66Mhz -> 133 MHz
- great for home or business users ona PC, but servers get constrained

Infiniband:
- 4X links
- deployed as PCI HCA(s) Host channel adaptors -> PCI-X is a bottleneck
    -> 20Gb/s pr 2,5 GB/sec
- a switched based I/O interconnect
- low pin count serial architecture
- copper (17m), fibre (km)
- QoS and RAS (reliability, availability and serviciability)

## markets

- IPC:
    - switched
    - multi-path
    - subnet manager
    - multicast

## bus architectures

technology     | switches | bus
   :-:         |    :-:   |    :-:    | 
topology       | switched | shared bus
pin count      | low      | high
endpoints      | many     | few
signal length  | km       | inches
reliability    | yes      | no
scalability    | yes      | no
fault tolerant | yes      | no

pci:
- 64 bit -> 90 pins

infiniband:
- can operate at a reduced power level compared to ethernet


# technical overview

physical layer
- 1X, 4X, 12X
- each link is a 4 wire serial differential connection (2 wires in each direction) -> 2,5 Gbps full duplex with raw BW of 2.0 Gb/sec 8b/10b encoded
- fiber and copper connectors defined
link layer
- link encoding: packets
    - mgmt packets:  (link config and maintenance; device information such as virtual lane support)
    - data packets: 4K bytes of payload
- subnet routing (LID): switching
    - 16 bit LocalID (LID) assigned by the subnet manager
    - LRH: local route header present in all packaets
    - QoS: virtual lanes (VLs) 15 standard VLs
        VL15: highest priority - management
        VL0: lowest priority
        SL: service level
        SL to VL mapping
- MAC: 
    - flow control- . credit based flow control (per VL) - destination grants credits to a sender
    - data integrity: VCRC (variant CRC) and Invariant CRC
        - VCRC 16 bit - all field of the packet and recalculated hop by hop
        - ICRC = end2end integrity

network layer
- inter subnet routing: used when packet traverse a subnet
    -> require a GRH: 128bit IPv6 address
transport layer
- responsible for in order packet delivery, partitioning, channel multiplexing and transport services (reliable connection, reliable datagram, unreliable connection, unreliable datagram, raw datagram)
- IBA operation
- SAR: segmentation and reassembly
    - BTH: base transport header
        -> contains the destination queu pair and seq nbr
        -> receiver 
- message QP

## infiniband elements

            CPU
             |
system mem - system controller
             |
             HCA
             |
    TCA - IB switch - TCA
             |
             TCA

HCA: host channel adaptor
- supports all verbs
TCA: target channel adaptor
- provides connection to an I/O device
switch
router
subnet manager (SM)
- method 1: subnet management
    - LID assignment
    - Sl to VL mapping
    - Link bringup and tear down
    - link failover
    - QP0 is handling this using VL15
    - SMP: subnet management packets (sumps) - unreliable datagrams
- method 2: general services: GSI
    - chassis management
    - oob I/O operations
    - GSI packets (gumps) - use VL15, QP1

support VIA (Virtual interface architecture)
- distributed messaging technology

