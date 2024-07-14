# quantum routing

Routing in Quantum networks

bipartite entanglement

protocols:
- heralded entanglement
- swapping

goal:
- max # entanglements
    -> routing -> paths, distributed way/sdn way, static/dyanmic
        - proactive: calculation before the entanglement happens
        - reactive routing: path computation is reactive on the virtual topology
            - latency constraints, we loose entanglements
        - virtual routing
        - opportunistic routing: hop by hop

    -> forwarding -> how does the quantum information moves around
        - fideltity: active versus passive
        - path recovery: in q things always fails
        - swapping operations:
            - path is a repeater chain
            - approaches:
                - synchronous: all swap at the same time, works well when all works well
                - asynchronous: local entanglement are ok
                - opportunistic: repeaters swap asap

- other routing considerations
    - path computation algorithms
        - dijkstra
        - path search on grph
        - greedy alg
        - linear programs
        - AI based
    - fidelty support
        - passive vs active
        - purify than swap
        - choice of purification
    - path recovery
        - handle decoherence


open questons
- optimal topology
- 3rd generations
- coupling between routing and forwarding
- dataplane overhead analysis
- lack of robust failure recovery
- interoperability of hetergenous links/hw