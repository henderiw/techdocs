# Transport (UET)

## SES (Semantic Sublayer)

- Deals with messages:
    - Segementing message into packets for PDS transmission
    - Reassembling packets from PDS
    - Generating response for every PDS Request

## PDS (Packet Delivery Subsystem)

- Reliability
    - packet delivery (reliable/unreliable) and ordering (ordered/unordered)
        - Delivery modes:
            - RUD: reliable unordered delivery
            - ROD: reliable orderd delivery
            - RUDI: reliable unordered delivery idempodent
            - UUD: unreliable, unordered delivery
    - selective retransmit
- Congestion Management
    - tx rate control
    - adaptive routing

- Deals with packets (known message boundaries)
- PDS Messages:
    - PDS Request
    - PDS Ack
- PDS:
    - PDS provides a connectionless interface to SES, but dynamically establishes connections referred to as PDC(s)
    - PDS also provides connectionless reliable delivery for idempotent operations
- Congestion management services:
    - Monitoring telemetry (network and endpoint congestion: latency, ECN and packet trimming)
    - Carries congestion state
    - Generates signals to control transmission chararcteristics of PDS connections.
        - outstanding data (windown size)
        - rate at which data is transmitted
    - multipath
    - CCC: congestion control context

Delivery modes


|                 | ROD | RUD | RUDI | UUD |
| :-              | :-  | :-  | :-   | :-  |
| dynamic PDC     | Y   |  Y  |  N   |  N  |

RUD:
- pkt is delivered one and in order to the SES
- deleiver pkts in the order they arrive from the network
- Seq number

ROD:
- pkt is delivered one and in order to the SES
- 2 options:
    - Go-Back-N: seq nbr for ordering
        - single network path
    - Reorder buffer at the target:
        - ROD can be implemented as RUD using adaptive path selection and selective ACKs
        - PDS knows the target capabilities

RUDI:
- pkt is delivered at least once to the SES
- goal multiple RMA Writes/Reads and than the barrier
- If Congestion management is used can be done in the same traffic class, otherwise a different traffic class is needed
- no replay protection -> need to be added in the application

UUD:
- if the same traffic class Congestion management must be enabled

## Congestion Mnagement

[simulation code](https://github.com/mhandley/uec-transport-simulation-code)

## trimming:

helps congestion management
2 indications for congestions
1. ECN
2. trimmed packets -> 100/128 bytes -> returned back to the source

Send with a new DSCP + update total length

## ReadRequest improvement

- Now: (High Efficiency Read is not good)
    - 16K read with a 4K MTU would need to send 4 ReadRequest/ReadResp
    - Handled by the semantic layer ()
- Options for improvement:
    - implement Read as Write by Target (High efficiency Write is available)
        - ReadReq does not contain the info needed to form a WriteRequest at Target -> missing info for the initiator (PidonFEP, Index, Match Bits)
        - New Opcode needed
    - One Read Request per MTU
        - Do not require support for REMOTE_READ completion counters -> no need for state tracking if this is not required

discussion:
- now: read is initiator driven
- REMOTE_READ completion counters (target) -> completion queue/counters in libfabric