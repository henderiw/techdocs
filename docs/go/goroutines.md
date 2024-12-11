## ways to block iso select

```go
	<-ctx.Done()
	log.Info("informers stopped...")
	r.cancel()
```

```go

		for range ctx.Done() {
		}
```
