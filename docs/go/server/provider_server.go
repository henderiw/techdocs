package kfserver1

import (
	"sync"

	"github.com/henderiw-nephio/k8sform/kform-plugin/kfprotov1"
	"github.com/henderiw-nephio/k8sform/kform-plugin/kfprotov1/kfplugin1"
)

// New converts a kfprotov1.ProviderServer into a server capable of handling
// kform protocol requests and issuing responses using the gRPC types.
func New(name string, serve kfprotov1.ProviderServer, opts ...ServeOpt) kfplugin1.ProviderServer {
}

type server struct {
	pserver kfprotov1.ProviderServer
	kfplugin1.UnimplementedProviderServer

	stopMu sync.Mutex
	stopCh chan struct{}

	name string

	// protocolDataDir is a directory to store raw protocol data files for
	// debugging purposes.
	protocolDataDir string

	// protocolVersion is the protocol version for the server.
	protocolVersion string
}
