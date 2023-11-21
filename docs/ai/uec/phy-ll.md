Chairs:
- Cathy Huang
- Adee Ran

Cisco: Adee Ran
HPE: Robert Alverson, Keith Underwood, Robert Alverson
Juniper: David Ofelt, ariel Cohen
Salience Labs: Andrew Garrett
Keysight: andy Moorwood, Venkat Pullela
Cornelis Networks: Charles Archer, Tomas Maj
Spirent: Ed Nakamoto, Keivan Chang, Lee Wheat, Matt Philpott
Broadcom: Eugene Opsasnick, Mohan Kalhunte
AMD: Gordon Brebner, J. Metz, Vipin Jain
Marvell: Kapil Shrikhande, Rani zemach
Intel: Mark Debbage, Nayan Suther, Nirjan Vaidya, Kent Lusted
Enfabrica: Shimon Muller
Synopsis: Tony Mantione
Oracle: Jacob Uecker

Tosten Hoefler
Jai Kumar
John Marshall
Chao Zang
Mike Li
Rob Craig
Craig Carlson
Charles Seifert
Uri Elzur

Agenda:
- 802.3dj update (Kent Lusted (Intel))
    electrical
        - 2 package approach: class A and class B
        - adaopted CR host
    optical PMDs
        - FECo mode -> host, module is transparent
        - FECi mode: RSS44 + helper FEC -> host, module is adding
        low latency and low power
        
        - 500m: FECo -> asked for 250m
        - 2 km: FECi
    [spec](https://www.ieee802.org/3/ad_hoc/ngrates/public/23_11/zhuang_nea_01_231114.pdf)
- spec review: (Adee Ran (Cisco))
    - draft 0.5
    - 3 stages: received/responses/
    - Nov 22 Ballot close dat
    - Dec 20: draft 0.7

Link Layer: Robert Alverson (HPE)
- Packer Rate improvement
    - Header optimizations: improve efficiency for small packets
    - min pkt size -> eth = 64 bytes
    - min size assumption:
    discussions
    - min cache line is 256 bytes
    - PRI is optional feature; LLR bit is compression is used or not
    - compression is optional
    - PRI options
        1. global enablement
        2. per link enablement (LLDP TLV) -> switch involvement
        3. per endpoint enablement (preferred) -> all switches need to be capable)
        4. subnet based
        - alternative is a fabric manager
        - libfabric -> when connection is established (use transport to control link layer) -> should be more widely usable
        - goal: unicast only
    - optimization possibilities:
        - replace ETH/IP header with an optimized header
             fields to be optimized
                ETH:
                    IPG: Yes
                    Preamble/LLR: NO
                    SMAC/DMAC: compressed address (24 bit for src/dst)
                        -> how do we manage these bits
                        -> more multi-rail architectures (32 bit is recommended)
                    EthType: Yes
                IP:
                    Version: Yes
                    IHL: yes
                    DSCP/ECN: No
                    length: ??? -> Yes is consensus
                    Fragmentaton: yes
                    TTL: Yes -> Should not be removed (e.g. dragonfly)
                    Protocol: 4 bit might be enough
                    Hdr Chksum: yes -> rely on ETh CRC
                    Src/Dst IP: compressed address
                Data Payload
                CRC
            25% gain -> this is ideal scenario; so is it worth the complexity
            IF (infiniband) is more efficient (50% more efficient)
            256bytes cache line for GPU(s) -> GPU(s) pack multiple cache lines together
            HPC -> values this feature

