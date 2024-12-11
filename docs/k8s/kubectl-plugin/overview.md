# kubectl plugin

Extends the kubectl command line tool for repetitive tasks

## how it is known

using your system PATH and a naming convention

kubectl-<command> e.g. kubectl-wim

kubectl wim -h

## install via krew

kubectl krew index add kcp-dev https://github.com/kcp-dev/krew-index.git
kubectl krew install kcp-dev/kcp
kubectl krew install kcp-dev/ws
kubectl krew install kcp-dev/create-workspace 

github repo -> https://github.com/kcp-dev/krew-index.git

directory plugins
- kcp.yaml
- ws.yaml
- create-workspace.yaml

```yaml
apiVersion: krew.googlecontainertools.github.com/v1alpha2
kind: Plugin
metadata:
  name: kcp
spec:
  version: v0.26.0
  platforms:
    - bin: bin/kubectl-kcp.exe
      uri: https://github.com/kcp-dev/kcp/releases/download/v0.26.0/kubectl-kcp-plugin_0.26.0_windows_arm64.tar.gz
      sha256: 753780ca53fb979a1667947f19beb1f184923be353b55788d2c4c63e9db95336
      selector:
        matchLabels:
          os: windows
          arch: arm64
    - bin: bin/kubectl-kcp.exe
      uri: https://github.com/kcp-dev/kcp/releases/download/v0.26.0/kubectl-kcp-plugin_0.26.0_windows_amd64.tar.gz
      sha256: 5bb0d68355ef25821b5970ab76fe451ef21eff32f04e7e0ad9a826d86714643f
      selector:
        matchLabels:
          os: windows
          arch: amd64
    - bin: bin/kubectl-kcp
      uri: https://github.com/kcp-dev/kcp/releases/download/v0.26.0/kubectl-kcp-plugin_0.26.0_linux_arm64.tar.gz
      sha256: 2a1bd876b373e58714c15af8259e0e7c8ca4caf63500204b62f8ca3ef530c1c1
      selector:
        matchLabels:
          os: linux
          arch: arm64
    - bin: bin/kubectl-kcp
      uri: https://github.com/kcp-dev/kcp/releases/download/v0.26.0/kubectl-kcp-plugin_0.26.0_linux_amd64.tar.gz
      sha256: 0a5712b7317bda9215bc8700254d942073f3ec1ce5d8ab739549dd3e51608b6c
      selector:
        matchLabels:
          os: linux
          arch: amd64
    - bin: bin/kubectl-kcp
      uri: https://github.com/kcp-dev/kcp/releases/download/v0.26.0/kubectl-kcp-plugin_0.26.0_darwin_arm64.tar.gz
      sha256: cd3265c0460868db0a2acc29e5c2d0542de2f9fd9899976a91938d30b17e7dc5
      selector:
        matchLabels:
          os: darwin
          arch: arm64
    - bin: bin/kubectl-kcp
      uri: https://github.com/kcp-dev/kcp/releases/download/v0.26.0/kubectl-kcp-plugin_0.26.0_darwin_amd64.tar.gz
      sha256: 9819fce2e60fa29319fd2121bb8134af67102596603a4db2ec8b4447a58faa58
      selector:
        matchLabels:
          os: darwin
          arch: amd64
  shortDescription: KCP cli plugin for kubectl.
  homepage: https://kcp.io/
  description: |
    KCP cli plugin for kubectl. Enables you to work with KCP.
```

## go example

```go
package main

import (
	"fmt"
	"log"
	"os"

	"github.com/spf13/cobra"
	"k8s.io/client-go/kubernetes"
	"k8s.io/client-go/rest"
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
)

func main() {
	// Root command
	var rootCmd = &cobra.Command{
		Use:   "kubectl-myplugin",
		Short: "A custom kubectl plugin to list Kubernetes pods",
		Long: `kubectl-myplugin is a kubectl plugin that allows you to list pods
in a specific Kubernetes namespace.`,
	}

	// Flags and variables
	var namespace string

	// Add subcommand for listing pods
	var listPodsCmd = &cobra.Command{
		Use:   "list",
		Short: "List pods in the specified namespace",
		Run: func(cmd *cobra.Command, args []string) {
			// Call the function to list pods
			listPods(namespace)
		},
	}

	// Attach namespace flag to the list command
	listPodsCmd.Flags().StringVarP(&namespace, "namespace", "n", "default", "The namespace to list pods from (default: 'default')")

	// Add subcommands to the root command
	rootCmd.AddCommand(listPodsCmd)

	// Execute the root command
	if err := rootCmd.Execute(); err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
}

func listPods(namespace string) {
	// Create Kubernetes client configuration
	config, err := rest.InClusterConfig()
	if err != nil {
		// If not running inside a cluster, try kubeconfig
		log.Fatalf("Failed to load Kubernetes configuration: %v", err)
	}

	clientset, err := kubernetes.NewForConfig(config)
	if err != nil {
		log.Fatalf("Failed to create Kubernetes client: %v", err)
	}

	// Retrieve pods in the specified namespace
	pods, err := clientset.CoreV1().Pods(namespace).List(metav1.ListOptions{})
	if err != nil {
		log.Fatalf("Failed to list pods in namespace %s: %v", namespace, err)
	}

	// Print the pod names
	fmt.Printf("Pods in namespace %s:\n", namespace)
	if len(pods.Items) == 0 {
		fmt.Println("No pods found.")
	} else {
		for _, pod := range pods.Items {
			fmt.Println(pod.Name)
		}
	}
}
```