# kubernetes

projects
- armada
- karmada
- yunikorn
- kserve
- kueue
- volcano
- kubeflow
- k8sgpt

open areas:
- multi-clutser scheduling
- model monitoring
- feature store
- responsible AI
- LLM intgeration

Talks:
- PrediBase:
    - GPU availability: A100/H100
    - GPU cost: $3/5 per hour
    - Privacy (training data and model should stay local)

    Why multi-cluster service mesh (with istio)
    Serverless inference (cost/traffic)
    - dataplane per VPC (hosts the LLM)
            - keda controller/keda proxy for autoscaling
                1. proxy gets a request and asks the keda controller for scling
            - LLM service + LLM deployment and LLM PODs
                - LLM POD: 8min to download (1 pod per node)
                    - 8 min to download container
                    - 16 min to load weigths
        - predibase control plane
    Cold starts are difficult:
        - 150G on disk: 70B
        part 1: container mirror (spegel)
        part 2: weigth downloads
            - local cache (init container) - per VPC model cache
            - S3 CRT client - multi-threade downloads
    Application
        LORA/LORAX for finetuning (subset of weigths)
        dynamically load weigths at inference times

    Questions:
    - scale
        - container images: 8
        - models: any model from hugging face (LLAMA2/Mistral)

CoreWeave
- no hypervisor layer
- GPU optimized stack
- katalyst:
    - CRD/Operators
    - Kubebuilder
    - vcluster Pro (40M)
        - shared workload cluster
        - dedicated workload node

Kueue: batch systems in production: multi-tenancy and fungibility (infra)
- batch systems
- why job queuing? training ( lots of jobs, limited resources)
- goal: max utilization of scarce resources (accelerators)
    - 2-level hierarchy for fair sharing and borrowing
    - priority based ordering and preemption

GPU utilization ik k8s with virtual kubelet
- virtual kubelet: tranlsates k8s CP events to external resource APIs
- enable scheduling ()

Cohere:
- OCI artifacts (ORAS)
    - focus on non-image artifacts (ORAS)
    - binpacking into layers
- Provision GPU accross clouds
- small scale versus large scale
issue
    - NVIDEA drivers
    - NVIDEA Device plugin
    - DCGM exporter
    -> goal GPU operator
issue 5: inconsistent identifiers:
    - device name fetched through NVML is inconsistent across clouds
    - lack of common node labels
    -> goal node/GPU feature discovery
issue 6: node upgrades are bound to fail
    - balance 
    - blue/green is ideal but GOU costs
    - solution: node pool, taint and set max nodes to 1 for the old pool
issue 7: autoscaling LLM(s) is challenging
    - autoscaler had hardcoded avlues
    - back off delays can lead to long scale up times
    - what metric to use?
        - global queue based on batches running
    


try:
- Weavescope
- firefly (adobe)
- 
