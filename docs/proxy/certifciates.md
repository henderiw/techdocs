# certificate architecture

install certmanager

```bash
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.11.0/cert-manager.yaml
```

```bash
kubectl create ns proxy
```

```bash
cat <<EOF | kubectl create -f -
apiVersion: cert-manager.io/v1
kind: Issuer
metadata:
  name: proxy-issuer
  namespace: proxy
spec:
  selfSigned: {}
EOF
```

```bash
cat <<EOF | kubectl apply -f -
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: root-certificate
  namespace: proxy
spec:
  isCA: true
  secretName: root-certificate
  commonName: "Root Certificate"
  privateKey:
    algorithm: RSA
    size: 4096
    encoding: PKCS8
  issuerRef:
    name: proxy-issuer
    kind: Issuer
EOF
```

```bash
cat <<EOF | kubectl apply -f -
apiVersion: cert-manager.io/v1
kind: Issuer
metadata:
  name: root-issuer
  namespace: proxy
spec:
  ca:
    secretName: root-certificate
EOF
```

certificate for the controller

```bash
cat <<EOF | kubectl apply -f -
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: server-certificate
  namespace: proxy
spec:
  secretName: server-certificate
  privateKey:
    algorithm: RSA
    encoding: PKCS8
    size: 4096
  commonName: "server"
  usages:
    - server auth
    - key encipherment
    - digital signature
  issuerRef:
    name: root-issuer
    kind: Issuer
  dnsNames:
  - mtls-server-service.proxy.svc.cluster.local
EOF
```

```bash
cat <<EOF | kubectl apply -f -
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: client-certificate
  namespace: proxy
spec:
  secretName: client-certificate
  privateKey:
    algorithm: RSA
    encoding: PKCS8
    size: 4096
  commonName: "client"
  usages:
    - client auth
    - key encipherment
    - digital signature
  issuerRef:
    name: root-issuer
    kind: Issuer
EOF
```


- root
- subCA

alternative

- root
- subCA1
- subCA2
