# install

export IMAGE_SERVICE_ENDPOINT=unix:///var/run/containerd/containerd.sock
export CONTAINER_RUNTIME_ENDPOINT=unix:///var/run/containerd/containerd.sock
VERSION="v1.26.0" # check latest version in /releases page
wget https://github.com/kubernetes-sigs/cri-tools/releases/download/$VERSION/crictl-$VERSION-linux-amd64.tar.gz
tar zxvf crictl-$VERSION-linux-amd64.tar.gz -C /usr/local/bin
rm -f crictl-$VERSION-linux-amd64.tar.gz

```bash
crictl ps
```