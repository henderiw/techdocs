# Network automation: lets think about a change or a group of changes we want to apply

An important aspect in network automation is change management and how it relates to the runtime. I like to think of a change in the following way:

- A change is the difference between the current desired state and the previous desrired state. It is determinsitic with a given input the output is determinsitic. Typically changes are atomic or better short in lifecycle. You can also plan and determine when to execute them. So a change is a change in the input when going from a current desired state to a new desrited 


- A runtime on the other hand is undeterminsitic and events can occur at various points in time and is less controllable

As such the notion of a runtime if important and i like to think of a change to the runtime as 



Wheras when i think about a change, a change is determinsitic

A runtime is 

This why in automation we need to distinguish between the intent which is static and determinsitic and the runtime which is 


In network automation we need to distinguish between the runtime, the actual network that does is serving the client from the intent. We also call this the desired state versus the actual state.

One of the reason for distinguishing between them and particulelry 


###

Change versus Runtime in Network Automation
An important aspect of network automation is understanding the relationship between change management and the runtime environment. I like to conceptualize these concepts in the following ways:

Change Management

A change represents the difference between the new desired state and the actual desired state. It is deterministic: given a specific input, the output is predictable. Ideally, changes are atomic, meaning they are small and short-lived. They can be planned and executed at specific times. Essentially, a change involves updating the input to transition from the current desired state to a new desired state.

Runtime Environment

In contrast, runtime operations are non-deterministic. Events can occur at various points in time and are less controllable. The runtime environment is dynamic and reactive, responding to real-time conditions and events that may not be predictable.
Therefore, understanding the concept of runtime is crucial. I like to think of changes to the runtime as part of an ongoing, adaptive process, rather than discrete, planned events.

While changes are deterministic and planned, runtime operations are dynamic and responsive. This distinction is important in network automation because it helps separate the intent, which is static and deterministic, from the runtime, which is dynamic and variable.

In network automation, it's essential to distinguish between the runtime (the actual network serving the client) and the intent (the desired state of the network). This distinction is often referred to as the desired state versus the actual state.

One of the key reasons for distinguishing between them is that while the intent remains fixed and serves as a guiding principle, the runtime environment must adapt to real-world conditions and events. This separation allows for more effective management and automation of network operations, ensuring that the network can respond to changing conditions while still striving to meet the desired state.