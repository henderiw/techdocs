K3S uses SQLLIGHT storage

K3S_KUBECONFIG_MODE="644" sh -s -

curl -sfL https://get.k3s.io | K3S_KUBECONFIG_MODE="644" \
INSTALL_K3S_EXEC='--flannel-backend=none   --no-flannel' sh -s - \
  --disable-network-policy \
  --disable "servicelb" \
  --disable "traefik" \
  --disable "metrics-server"

sudo cat /etc/rancher/k3s/k3s.yaml > ~/.kube/config



kubectl create -f https://raw.githubusercontent.com/cilium/cilium/v1.12/install/kubernetes/quick-install.yaml


curl -sfL https://get.k3s.io | K3S_KUBECONFIG_MODE="644" \
INSTALL_K3S_EXEC='--flannel-backend=none   --no-flannel' sh -s - \
  --disable "metrics-server"


# install with cilium

curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC='--flannel-backend=none --disable-network-policy' K3S_KUBECONFIG_MODE="644" sh -

export KUBECONFIG=/etc/rancher/k3s/k3s.yaml

CILIUM_CLI_VERSION=$(curl -s https://raw.githubusercontent.com/cilium/cilium-cli/master/stable.txt)
CLI_ARCH=amd64
if [ "$(uname -m)" = "aarch64" ]; then CLI_ARCH=arm64; fi
curl -L --fail --remote-name-all https://github.com/cilium/cilium-cli/releases/download/${CILIUM_CLI_VERSION}/cilium-linux-${CLI_ARCH}.tar.gz{,.sha256sum}
sha256sum --check cilium-linux-${CLI_ARCH}.tar.gz.sha256sum
sudo tar xzvfC cilium-linux-${CLI_ARCH}.tar.gz /usr/local/bin
rm cilium-linux-${CLI_ARCH}.tar.gz{,.sha256sum}
cilium install





curl -s "https://gist.githubusercontent.com/lizrice/107e492b82f386da8883e9d1a385c0b2/raw/d615888ce6e135fba78a57f8ebc575a9dca921bf/ctfapp.yaml" -o ctfapp.yaml
kubectl create -f ctfapp.yaml

apt-get install -y linux-tools-$(uname -r)

