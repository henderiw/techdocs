# cel

- validation is critical, but can be hard
    - immutable field
    - cross field checks
    - mutually exclusive
- we need a validation webhook -> this is adding complicity to development, operational complexity (mis-configure, latency added, etc)
- answer: CEL (common expression language)

## examples

no for/while/...
- use comprehension "marcos(s)"
    - all()
    - exists()
    - exists.one()
    - map()
    - filter()
no if/else
- use the ternary operator
    - <condition> ? <ifTrue> : <ifFalse>


[cel spec](https://github.com/google/cel-spec)
[k8s cel](https://kubernetes.io/docs/reference/using-api/cel/)

## CRD validation rules

x-kubernetes-validations:
- rule: "self.replicas <= se;f.maxReplicas"

oldSelf -> helps in transition rules

messageExpression

## CRD conversion with CEL

-> next goal -> KEP available
