# cel in k8s api

mailing list:
- kubernetes-sig-api-machinery@googlegroups.com
- wg-sig-api-machinery-cel-dev-external
slack #sig-api-machinery-cel-dev

[cel conversion](https://github.com/kubernetes/enhancements/issues/3945)
[cel in native types declaritive validation](https://kubernetes.io/docs/reference/access-authn-authz/validating-admission-policy/)
[cel for admission control](https://github.com/kubernetes/enhancements/blob/master/keps/sig-api-machinery/3488-cel-admission-control/README.md)

- type checked
- cost checked

variables:
- self
- oldself: -> used for transiationing rules like immutability

rules
- rule: "!has(self.foo) || self.startsWith("kube")"
- message
// +kubebuilder:validation:XValidation:rule="!has(self.interfaceName || self == oldSelf",message="Value is immutable"

future:
- validation rules
- mutating rules also called transition rules (self/oldSelf)
- version conversion
- policy agent (kuberbetes/cel-admission-webhook)
    - policy author (care about correctness and extensibility)
    - cluster administrator ()
    - failure policy
    - authz check