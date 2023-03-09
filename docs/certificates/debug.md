# debug

curl -v -k https://mtls-server-service.proxy.svc.cluster.local:8888 --cert /certs/tls.crt --key /certs/tls.key --cacert /certs/ca.crt

curl -v -k https://mtls-server-service.proxy.svc.cluster.local:8888

openssl s_client -showcerts -connect mtls-server-service.proxy.svc.cluster.local:8888 </dev/null