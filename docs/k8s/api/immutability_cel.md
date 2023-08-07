# enforce immutability

[crd immutability with cel](https://kubernetes.io/blog/2022/09/29/enforce-immutability-using-cel/#:~:text=To%20enforce%20a%20field%27s%20immutability,value)%20%7C%20has(self.)

## immutable after first modification

// +kubebuilder:validation:XValidation:rule="!has(oldSelf.value) || has(self.value)", message="Value is required once set"
type ImmutableSinceFirstWrite struct {
   metav1.TypeMeta   `json:",inline"`
   metav1.ObjectMeta `json:"metadata,omitempty"`

   // +kubebuilder:validation:Optional
   // +kubebuilder:validation:XValidation:rule="self == oldSelf",message="Value is immutable"
   // +kubebuilder:validation:MaxLength=512
   Value string `json:"value"`
}

## Immutability upon object creation 

the difference is that the validation is Required

// +kubebuilder:validation:XValidation:rule="!has(oldSelf.value) || has(self.value)", message="Value is required once set"
type ImmutableSinceFirstWrite struct {
   metav1.TypeMeta   `json:",inline"`
   metav1.ObjectMeta `json:"metadata,omitempty"`

   // +kubebuilder:validation:Optional
   // +kubebuilder:validation:XValidation:rule="self == oldSelf",message="Value is immutable"
   // +kubebuilder:validation:MaxLength=512
   Value string `json:"value"`
}

// +kubebuilder:validation:XValidation:rule="!has(oldSelf.values) || has(self.values)", message="Value is required once set"