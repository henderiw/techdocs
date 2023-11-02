# oran architecture

[O-RAN.WG1.OAD-R003-v10.00.pages](https://orandownloadsweb.azurewebsites.net/specifications)

Building blocks
- SMO (Non-RT RIC)
- O-Cloud
- O-RAN NF(s) incl Near-RT RIC, O-CU-CP, O-CU-UP, O-DU, O-RU, O-ENB
- O-RU (real time component)

Interfaces:
- O1: SMO <-> ORAN NF
- O2: SMO <-> OCloud
- A1: SMO Non-RT RIC <-> Near-RT RIC
- Open Fronthaul M-Plane

O-RAN NF Interfaces
- Y1: Near-RT RIC -> analytics consumers
- NG: O-RAN NF(s) - NG Core
- E2: Non-RT RC <-> O-RAN NF
- E1: O-CU-UP <-> O-CU-DP
3GPP interfaces:
- F1-c: fronthaul CP
- F1-u: fronthaul DP
- X2-c: O-CU-CP
- Xn-c: O-CU-CP
- NG-c: O-CU-CP
- X2-u: O-CU-UP
- Xn-u: O-CU-UP
- NG-u: O-CU-UP

SMO:
- FCAPS
    - Observability
        - PM
        - FM
        - Trace
    - Config Management
    - heartbeat
    - File Management
    - PNF discovery
    - PNF SW Mgmt

FOCOM - O2 IMS
NFO - O2 DMS

