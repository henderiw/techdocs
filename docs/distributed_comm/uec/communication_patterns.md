# communciation patterns

challenge in HPC -> wildcard is needed

## rendezvous operations

Processes coordinate to exchange messages or data. A rendezvous operation typically involves two distinct phases: 

- matching phase:
    - The processes agree on specific criteria or conditions that need to be met for the communication to occur.
    - Specifying tags/message sizes
- data transfer phase.
    - Exchange of information between the participating processes according to the agreed-upon criteria

Rendezvous operations are often used in collective communication patterns where multiple processes collaborate to perform a collective task. Examples of collective communication operations that may involve rendezvous include `barrier synchronization`, `gather`, `scatter`, and `reduce` operations.

Examples `MPI_Send` and `MPI_Recv`

Initiator:
- SEND completion
- READ completion

Target:
- MSG completion

## deferrable send

