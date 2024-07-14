# pluralize

"github.com/gobuffalo/flect"

```go
// Validate checks the Resource values to make sure they are valid.
func (r *Resource) Validate() error {
	if len(r.Kind) == 0 {
		return fmt.Errorf("kind cannot be empty")
	}

	if len(r.Resource) == 0 {
		r.Resource = flect.Pluralize(strings.ToLower(r.Kind))
	}

	if r.Kind != flect.Pascalize(r.Kind) {
		return fmt.Errorf("kind must be CamelCase (expected %s was %s)", flect.Pascalize(r.Kind), r.Kind)
	}

	return nil
}
```