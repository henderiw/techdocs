## options

2 important considerations
- is it N:1 or 1:1 senders to receivers
    - N:1 -> multiple senders via 1 single channel to a receiver
    - 1:1 -> 1 sender to 1 receiver via a dedicated channel
- how to signal done and who closes the channel
    - in N:1 it has to be the receiver and the done signaling is done using a dedicated message
    - in 1:1 the sender can close the channel but we have to be careful of blocking and memory leaks

1. 1:1 mode

Approach is good when you are a server with memory storage
single sender with singler receiver

e.g. kubernetes watch is like this
https://github.com/henderiw-k8s-lcnc/discovery/blob/18da59164f7286ae97c49d8ae71509a20c5103d5/registrator/k8s.go#L210


watch.Interface
```golang
type Interface interface {
    // Stop stops watching. Will close the channel returned by ResultChan(). Releases
    // any resources used by the watch.
    Stop()

    // ResultChan returns a chan which will receive all the events. If an error occurs
    // or Stop() is called, the implementation will close this channel and
    // release any resources used by the watch.
    ResultChan() <-chan Event
}
```

as a client you do this -> watcher

process the information from the channel

```golang
    // get the channel
    wi, err := r.clientset.CoordinationV1().Leases(r.namespace).Watch(ctx, metav1.ListOptions{
		LabelSelector: validSelector,
		Watch:         true,
	})
	if err != nil {
		r.l.Error(err, "failed to create watch")
		time.Sleep(defaultWaitTime)
		goto WATCH
	}
	for {
		select {
		case _, ok := <-wi.ResultChan():
			if !ok {
				return
			}
			sr := &ServiceResponse{
				ServiceName: serviceName,
			}
			if opts.RetriveServices {
				sr.ServiceInstances, sr.Err = r.Query(ctx, serviceName, tags)
			}
			ch <- sr
		}
	}
```

2. the client supplies the channel

e.g. in a registration service, more like an event proxy

example https://github.com/yndd/provider-controller/blob/26a4be09840821a0935d32945214a2c76042d9a5/pkg/watcher/watcher.go#L89

client supplies a channel in a watch that is started as a goroutine

client side

```golang
ch := make(chan *registrator.ServiceResponse)
	for _, pod := range cc.Spec.Pods {
		w.log.Debug("podInfo", "pod", pod)
		for _, serviceInfo := range cc.GetServicesInfoByKind(pod.Kind) {
			w.log.Debug("serviceInfo", "serviceInfo", serviceInfo)
			go w.registrator.WatchCh(ctx, serviceInfo.ServiceName, []string{}, ch)
		}
	}

	for {
		select {
		case <-ctx.Done():
			w.registrator.StopWatch("")
			return
		case serviceResp, ok := <-ch:
			if !ok {
				// someone closed the channel so we cannot continue
				w.registrator.StopWatch("")
				return
			}
			if serviceResp.Err != nil {
				// when an error is returned we stop and restart all watches again
				w.registrator.StopWatch("")
				goto START
			}
			if serviceResp != nil {
				for _, ch := range w.eventCh {
					ch <- event.GenericEvent{
						Object: &pkgmetav1.ControllerConfig{
							ObjectMeta: metav1.ObjectMeta{Name: cc.Name, Namespace: cc.Namespace},
						},
					}
				}
			}
		}
	}
```

server side

```golang
func (r *k8sRegistrator) WatchCh(ctx context.Context, serviceName string, tags []string, opts WatchOptions, ch chan *ServiceResponse) {
	r.l.WithValues("serviceName", serviceName)
	wi, ok := r.watches[serviceName]
	if ok && wi != nil {
		wi.Stop()
	}
	validSelector, _ := buildSelector(serviceName, tags)
WATCH:
	wi, err := r.clientset.CoordinationV1().Leases(r.namespace).Watch(ctx, metav1.ListOptions{
		LabelSelector: validSelector,
		Watch:         true,
	})
	if err != nil {
		r.l.Error(err, "failed to create watch")
		time.Sleep(defaultWaitTime)
		goto WATCH
	}
	for {
		select {
		case _, ok := <-wi.ResultChan():
			if !ok {
				return
			}
			sr := &ServiceResponse{
				ServiceName: serviceName,
			}
			if opts.RetriveServices {
				sr.ServiceInstances, sr.Err = r.Query(ctx, serviceName, tags)
			}
			ch <- sr
		}
	}
}

func (r *k8sRegistrator) StopWatch(serviceName string) {
	r.m.Lock()
	defer r.m.Unlock()
	wi, ok := r.watches[serviceName]
	if ok && wi != nil {
		wi.Stop()
	}
	delete(r.watches, serviceName)
}

```