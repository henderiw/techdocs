package kfserver1

import (
	"github.com/henderiw-nephio/k8sform/kform-plugin/kfprotov1"
	"github.com/henderiw-nephio/k8sform/plugin"
	"google.golang.org/grpc"
)

// Kerraform

const (
	grpcMaxMessageSize = 256 << 20
)

type ServeOpt interface {
	ApplyServeOpt(*ServeConfig) error
}

type serveConfigFunc func(*ServeConfig) error

func (s serveConfigFunc) ApplyServeOpt(in *ServeConfig) error {
	return s(in)
}

type ServeConfig struct{}

func Serve(name string, serverFactory func() kfprotov1.ProviderServer, opts ...ServeOpt) error {
	conf := ServeConfig{}
	for _, opt := range opts {
		err := opt.ApplyServeOpt(&conf)
		if err != nil {
			return err
		}
	}

	serveConfig := &plugin.ServeConfig{
		VersionedPlugins: map[int]plugin.PluginSet{
			1: {"provider": &GRPCProviderPlugin{
				Name:         name,
				Opts:         opts,
				GRPCProvider: serverFactory,
			}},
		},
		GRPCServer: func(opts []grpc.ServerOption) *grpc.Server {
			opts = append(opts, grpc.MaxRecvMsgSize(grpcMaxMessageSize))
			opts = append(opts, grpc.MaxSendMsgSize(grpcMaxMessageSize))

			return grpc.NewServer(opts...)
		},
	}

	go plugin.Serve(serveConfig)

	return nil
}