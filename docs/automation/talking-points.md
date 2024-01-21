#

## Title:

- making networks consumable
- making network sexy

## Talking points

- lots of point solutions
- specialization versus generalization -> house culture (not invented by me)
    - don't specialize the common layer
    - why have a special common layer RBAC/PKI/etc etc
- open + extendable
    - people
    - code generation
- time to market
    - code generation
    - decoupled
    - easy to extend/customize
- footprint -> small + big -> microservices
- declaritive/intent driven -> focus on what not how
- devops/ ci-cd
- rollback/ backup and restore
- fullfilment + assurance -> many solution only for config (no state, fault, assurance)
- source of truth

## Kubernetes

- Open source/community of 1000(s) people
- KRM
- schema: validation/mutation
- extendable:
    - controllers/operators/fnAAS/api-server/...
    - do 1 thing
- huge ecosystem

## Finished good/framework

Missing:
- YANG
- Versioned datastore
- Assurance/Health
- Easy to use/Easy to consume
    - Intent definition
    - Assurance definition
    - UI definition

## Automation

- every layer matters
- simplicity scales -> DO 1 THING
- isolation
- lego blocks -> reusable components
- orchestration -> connect multiple lego blocks
- choreography versus workflow
- build versus buy

## cloud is in the air

- Cloud is everywhere: hyperscalers, 5G, cloudnative; sd-wan
    - workloads are more dynamic
    - hyperscalers
    - No cloud w/o a network
    - Operational model is different
    - My journey
    - Aspects relevant for automation
- Automation aspects: (patterns)
    - automation is a product: Buy, Build or Extend
        - Lifecycle is critical
        - How to make the effort to maintain and update small
        - code generation
        - use an open eco-system
    - Consumable by everyone: small, extendable, etc
    - No fear, No compromise -> TRUST
    - Declarative/Intent: not just config but also does it work and ideally a UI
    - Data Modeling
    - Data driven
    - Collaboration, change control: Devops/
    - Divide and concur: do 1 thing and 1 thing well
    - Avoid blast radius
    - Is networking a snowflake -> specialization versus generalization
- Now what?
    - I looked at kubernetes and it turns out it has a lot of attributes we can leverage, so why not use it.
    - Very extenssive Schema definition with validation/mutation hooks
    - Controller paradim, Event driven design and a huge eco-system
    - Introduce Nephio
    - Introduce SDC
    - Introduce kform
    - assurance
- Misconseptions:
    - No we dont have to run the controls by IT, you can have your own dedicated cluster
    - k8s upgrades -> LTS
    - are we tied to go?
        - no python controllers

## macro thoughts

- what is happening
    - network is super critical - any service over IP
    - is networking perceived sexy enough; how do we attract new talent; 
    - overlay is winning


First, although i work for Nokia this talk is about my personal experience and journey of building a network automation system for the community. The talk will give an introduction on my jorney of network automation, it will focus on a number of critical aspects I believe are important to make network automation consumable and sexy. It explains a journey how to use Kubernetes as a network automation platform, the extensions we added, etc. the talk will also present some open source projects related to this talk. e.g. Nephio and others that will be open source soon.The talk will focus on automation, orchestration, observability and closed loop + even the ease of consumption and extensions.

While working for Nokia, this presentation delves into my personal journey developing a community-based network automation system atop Kubernetes. I'll explore the motivations, objectives, and implementation details, including specific extensions tailored for network automation. The talk introduces open-source projects like Nephio, Porch, and Sdc, emphasizing the importance of automation, orchestration, observability, closed-loop processes, and user-friendly consumption/extensibility (low code, no code). Additionally, a live demo will showcase fundamental aspects of the system to the audience.

Despite being employed by a vendor(Nokia) this talk is about my journey. I will share my journey of developing a community based network automation system on top of kubernetes. I'll discuss the why, the what and the how + the extensions we made especially for network automation. The talk introduces open-source projects, such as Nephio, Porch, Sdc, etc, and highlights the significance of automation, orchestration, observability, closed-loop processes, and user-friendly consumption/extandability (aka low code no code). On top a demo will be shown to the audience to see things in real.