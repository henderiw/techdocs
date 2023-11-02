package kfserver1

import (
	"context"
	"errors"

	"github.com/henderiw-nephio/k8sform/kform-plugin/kfprotov1"
	"github.com/henderiw-nephio/k8sform/kform-plugin/kfprotov1/kfplugin1"
	"github.com/henderiw-nephio/k8sform/plugin"
	"google.golang.org/grpc"
)

// GRPCProviderPlugin is an implementation of the
// github.com/hashicorp/go-plugin#Plugin and
// github.com/hashicorp/go-plugin#GRPCPlugin interfaces, indicating how to
// serve tfprotov5.ProviderServers as gRPC plugins for go-plugin.
type GRPCProviderPlugin struct {
	GRPCProvider func() kfprotov1.ProviderServer
	Opts         []ServeOpt
	Name         string
}

// GRPCServer registers the gRPC provider server with the gRPC server that
// go-plugin is standing up.
func (p *GRPCProviderPlugin) GRPCServer(broker *plugin.GRPCBroker, s *grpc.Server) error {
	kfplugin1.RegisterProviderServer(s, New(p.Name, p.GRPCProvider(), p.Opts...))
	return nil
}

// Not implemented
func (p *GRPCProviderPlugin) GRPCClient(ctx context.Context, broker *plugin.GRPCBroker, c *grpc.ClientConn) (interface{}, error) {
	return nil, errors.New("kform-plugin-go only implements gRPC servers")
}
