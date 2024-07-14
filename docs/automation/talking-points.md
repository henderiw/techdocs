#

## Title:

- making networks consumable
- making network sexy
- are we building a snowflake

## Talking points

- lots of point solutions
- specialization versus generalization -> house culture (not invented by me)
    - don't specialize the common layer
    - why have a special common layer RBAC/PKI/etc etc
- need to think about it as a system/product
- structured api
    - validate
    - defaults
    - mutation
    - transform
    - dependencies
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
    - operational taks
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
    - Networks become more complex and we are asked to do more with less
    - Change is continuous
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


## ip assembly

1. Sketch the current situation
    - We operate networks mostly by human (finger defined)
    - Budgets are tight and we are asked to do more and more
    - Dealing with Change is a fact
2. We have done an outstanding job in in solving a distributed routing protocol problem, but we havent don’t a good job in making our networks consumable (thinking of a picture of IETF where when we preseting routing protocol extensions you see 100 people on the mic, wheras aa YANG model gets no attention)
3. Introduce the Automation Maturity Model (does this exist?)
    a. extreme -> FDN finger defined, where individual humans control
    b. Middle: not sure what to call this
    c. autonomous: where the network is operated in a collaborative approach where machine execute most of the work or give insights

    -> manual, recommendation, autonomous
4. need to think through this a bit more  on this section -> idea is to give insight how to go from 3a to 3c
    a. e.g. here we could present a picture of a person being on call all the time (which is 3a
    b. towards a world where a machine detects something and collaboratively people get asked on the next step based on suggestions a machine provides
5. Conclusion: is the status quo an option? You decide (as everybody should reflect where they want to be

## the journey towards the maturity level

- a system or a product we have to maintain
- a structured API at every layer 
    -> codeGen/validation/mutation/dependency mgmt
    -> a well defined schema that is extendable and consumable
- every layer matters : no fear
- a set of lego blocks (bots) that seamlessly operate (microservices)
    - Declarative 
    - Config
    - State
    - UI
- collaborative system
- the automation system itself should be consumable


0. twoards the maturity model
1. look at the landscape
automation landscape
- IaaC/Config Managements
- Home grown systems
- Vendor solutions
- System Integration

-> look at cloud and sdwan (managed services), keys of kingdom are taken away from us

2. look at the requirements
- consumable by everyone: DIY/DNY/DSY
- lifecycle - need to be maintainable/suuportable extendable
- structured API w/o fear (as vendors we make it very hard)
- declaritive, config + state, UI
    - drain the network
- does it work
- microservices
- Query engine to reason with and i consumable
- Collaboration
- Digital Twin
3. Why build a snowflake - leverage the systems out there?
- Use kubernetes
- large ecosystem
- model of apps where people can collaborate and compete
- Nephio

Need to find a good angle to close


Autocon: -> making network automation consumable

Kubernetes outline:

- Introduction:
    - We all have constraints; always asked to do more within the constraints we have -> automation is the answer
- Automation
    - Should be treated like a product - minimizing the effort to maintain its lifecycle is critical.
    - Should be consumable/predictable and trustable leveraging a collaborative approach
    - ...
- Now what?
    - Kubernetes as a system is the biggest and largest automation and orchestration system out there, leveraged in many industries. Why is network special that it should not leverage this?
        - Open Source
        - Very extendable
        - Huge ecosystem
        - Declarative
        - Collabrative: Gitops
        - Huge knowledge base
- To Help in this journey Nokia want to help train and educate people to leverage Kubernetes as the automation platform for network automation
    -> launch Kubenet