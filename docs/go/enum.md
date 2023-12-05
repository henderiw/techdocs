```golang
type EventType int

const (
	Added EventType = iota
	Modified
	Deleted
)

func (r EventType) String() string {
	return [...]string{"Added", "Modified", "Deleted"}[r]
}
```