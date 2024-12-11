# automation stack

- Take a step back and look at the components/building blocks for automation
- Declarative approach: what not how or you dont want to look at the indidual changes but you mange the change on what you want to achieve
    -> e.g. kubernetes 
- In essence focus on what iso how
- From abstraction to provider specific configuration

terminology and architecture:
- preparation/orchestration phase:
    - intent - BL - generate artifacts specific to 
    - context - in which this intent is relevant
    - resource/ abstract - derived resources (apis, etc etc)
- actuation: take the what and try to ensure the desired state
    - gitops
    - transactional
    - monitor health


Preparation phase:
- build with is easy to maintain
- script, workflows, etc
- avoid NXM problem -> vendor abstraction (resource data model), avoid duplication


Solutions:
- Data Model, Generating Pipeline, A Serving infrastructure
    - Resource input
    - Generate
    - Validation data model, CI pipeline
    - Staging environment
- parameterization
- abstract with SRE config
- pets versus cattle -> continuous enforcement

SOT:
- data accuracy and integrity
- reference
- immutable and consistent

## introduction

Title: Kubenet: A Framework for Declarative Network Automation

Introduction

In the rapidly evolving landscape of technology, automation stands as a critical force driving efficiency, accuracy, and scalability. Understanding the foundational principles and architecture of automation is indispensable. This blog introduces the framework adopted at Kubenet for network automation, emphasizing a declarative approach where the focus is on defining “what” needs to be achieved, rather than the “how.”

1: Clarifying Terminology in Network Automation

Grasping the right terminology is crucial, as network automation involves multiple components and layers of technology. Below, we clarify the key terms used at Kubenet:

- Resource: Defines the objectives and encapsulates your requirements. Resources vary widely and include:
	•	Abstract Resources: High-level definitions that abstract from specific implementations to enhance flexibility across environments.
	•	Identity and Inventory Resources: Also known as inventory resources, these define the environmental context, such as network topology and IP pools, essential for setting network configurations.
	•	Internal Resources: Controlled internally, these resources focus on derived outcomes crucial for efficient automation.
	•	External Resources: Depending on external systems’ data models and protocols, these may include:
	•	Provider-Specific Resources: Tailored to specific hardware or software from vendors, meeting specific technological needs.
- Consumer: Any user or system that utilizes the resource, ranging from organizational departments to external systems interacting with the network.
- Provider: The entity that implements and manages resources, ensuring that the actual network state aligns with the desired state.
- Runtime: The actual environment where the network service is implemented, whether physical, virtual, or containerized.
- Actuator: A specialized provider that engages with the runtime to enforce the desired resource states, aligning the intended and actual states and addressing deviations.

At Kubenet, we leverage KRM and construct resources using OpenAPI and YANG data modeling, facilitating interactions with various internal and external systems.

2: Automation Building Blocks

Understanding the conceptual behavior aimed for in our automation framework is crucial. Essentially, a consumer defines a desire, and producers generate the derived artifacts. These artifacts, once curated and validated, are managed by actuators to ensure alignment between the desired and actual states. Kubenet employs a decomposable system approach, differentiating the preparation/orchestration phase from the actuation phase due to their unique operational focuses.

- Preparation/Orchestration Phase:
    - This phase involves transforming defined desires into actionable configuration artifacts.
	•	    Some transformations may be straightforward, while others require in-depth planning and complex process understanding. At Kubenet, our goal is to develop a system that is both extendable and easy to maintain.
	•	    In networking, these transformations can be complex; for example, a network resource at Kubenet might transform into device-specific configurations using network topology and design resources, possibly expanding into multiple resources depending on the network’s size.
    - Ideally you want to perform these transformation/generation in a controlled environment. Creating a candidate, iterating over a candidate, validation the candidate before handing to the serving area and actuation phase.

- Actuation Phase:
	•	The automation system then implements the desired state across the network as defined by the resources.
        - Multiple devices are typically involved in this phase that in many cases need to be actuated in harmony.
        - Interacting with various external systems implementing different data models.
	•	Continuous monitoring and dynamic adjustments are crucial, ensuring the network remains reflective of the desired state and quickly adapts to any operational changes or discrepancies.
    - 

Both phases leverage a version control system to allow for rollback and revision control of the network resources.

What do you think? any comments are welcome?

Feel free to reply here, or send me a message on LinkedIn.


# the automation stack

- desired config
- actual state
- policy (enforcing mode)

- preparation phase
    - change management
        - validate change, define pre/post checks, etc
        - validation to a certain extend
        - phase from design
        - examples: change a vlan, change a network device, upgrade NOS (for security, etc)
    - lifecycle
    - steps in defining a change
        - What is the change?
            - instantiation an already defined resource with new parameters
                -> business logic should not change
            - define a new service with business logic -> additional pipeline  
        - Validate the result
            - Validate the result syntactically against a schema (dry-run in sdc)
            - Visualize diff on the network devices (check what changes between running and new desired)
            - Validate on a digital twin
        - Define the pre/post checks -> executed in conjunction with the actuation layer
- actuation phase
    - only layer that interact with the network devices (several components)
        - implements the actual changes 
        - policy for enforcement
    - implements the change:
        - transaction
        - progressive rollout
        - 
    - get state from the network 
        -> to perform post checks
- observation phase



Kubenet Update: Expanding and Enhancing Network Automation

As we move beyond the initial phase of proving that Kubernetes can effectively handle network automation, Kubenet is now transitioning to a more open and user-friendly platform. Here’s what we’ve accomplished and where we’re heading:
	•	Enhanced Business Logic Capabilities: Kubenet now supports Python, Jinja templates, and Go templates, simplifying the way users can write and implement your business logic.
	•	Decoupled Architecture: We’ve successfully decoupled Kubenet from the dependency on a Kubernetes cluster facilitated by Choreo (https://choreo-docs.kform.dev), enhancing flexibility.
	•	Refined Data Model: The abstract data model has been split and decomposed, making it easier for users to extend and modify it to fit their specific needs. (https://github.com/kubenet-dev/apis)
	•	Version Control Integration: To foster collaboration and streamline workflows, we’ve integrated a version control backend. This integration supports both development and production environments, ensuring that changes are tracked and managed effectively.
	•	Advanced Configuration Validation: Kubenet has integrated SDC (https://docs.sdcio.dev) with offline YANG config validation, improving the reliability and correctness of network configurations.
	•	Python Prototyping for CRDs: We are currently prototyping the use of Pydantic to enable writing of Custom Resource Definitions (CRDs) in Python, aiming to make the development process more accessible and powerful. (https://github.com/kform-dev/pydantic-crd-model-example)

We will explore this in #autocon workshop this week.