# dns overview

/etc/resolv.conf

tld: top level domain (e.g. .com)
root servers


host (www.google.com) -> resolver <-> (www.google.com)                    -> root server
                                      not authoritive try com. at <ip(s)> <- root server
                                  <-> (www.google.com)                           -> tld server
                                      not authoritive try google.com. at <ip(s)> <- tld server
                                  <-> (www.google.com)                           -> google nameserver
                                      142.250.114.99  <- google nameserver

caching/TTL to indicate how long it can be cached

[root server url](https://www.iana.org/domains/root/servers)

## dns records

A: ipv4 record
AAAA: ipv6 record
NXDOMAIN: non existing domain
SRV: identifies the location of a specific service or protocol within a domain
    - example: _sip._tcp.example.com. IN SRV 10 5 5060 sipserver.example.com.
        - service: _sip
        - protocol: _tcp
        - name: example.com (domain name)
        - priority: 10 (lower values indicate higher priority)
        - weight: 5 (distribute load for records with the same priority)
        - port: 5060 (port the sip server is listening on)
        - target: hostname of the server that provides the SIP service.
    - usage: query _sip._tcp.example.com
PTR: used in reverse DNS lookups (map ip to domain name)
    - example: 25.168.192.in-addr.arpa. IN PTR mail.example.com.
        - ip address: 25.168.192
        - in-addr.arpa.
        - PTR: record type
        - domain name: mail.example.com.