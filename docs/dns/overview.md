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
CNAME: A CNAME, or Canonical Name, used to alias one domain to another. It is often used to create an alias or nickname for a domain's canonical (official) hostname
    - example: alias.example.com. IN CNAME canonical.example.com.
    - It's important to note that CNAME records introduce an additional DNS lookup, which may impact performance
TXT: A TXT record (Text record) is a type of DNS (Domain Name System) record used to associate arbitrary text with a domain. TXT records are often used to store machine-readable information, but they can also be used for various purposes, including verification and validation mechanisms.
    - example: example.com. IN TXT "This is some text information."
        example.com: The domain to which the TXT record belongs.
        IN: The class of the record (Internet class).
        TXT: The type of the record (TXT).
        "This is some text information.": The text information associated with the domain.
MX: An MX (Mail Exchange) record is a type of DNS (Domain Name System) record that specifies the mail servers responsible for receiving email messages on behalf of a domain. 
    - example: example.com. IN MX priority mail-server.example.com.
        example.com: The domain for which the MX record is configured.
        IN: The class of the record (Internet class).
        MX: The type of the record (MX).
        priority: A positive integer indicating the priority of the mail server. Lower values have higher priority.
        mail-server.example.com: The domain name of the mail server.
    A domain can have multiple MX records, each with its own priority and mail server. This allows for redundancy and load balancing. If the mail server with the highest priority is unreachable, the next lower priority server is attempted.
        example.com. IN MX 10 mail-server1.example.com.
        example.com. IN MX 20 mail-server2.example.com.
SOA: A SOA (Start of Authority) record is a type of DNS (Domain Name System) record that contains administrative information about a domain. The SOA record is fundamental to the structure of a DNS zone and provides essential details about the domain, including the primary authoritative DNS server, the email of the domain administrator, domain serial number, timers for refreshing the zone, and other metadata.
    - example
        ```
        example.com. IN SOA primary-ns.example.com. admin.example.com. (
                        serial-number
                        refresh
                        retry
                        expire
                        minimum-ttl
                    )
        ```
        example.com: The domain for which the SOA record is configured.
        IN: The class of the record (Internet class).
        SOA: The type of the record (SOA).
        primary-ns.example.com: The domain name of the primary authoritative DNS server.
        admin.example.com: The email address of the domain administrator or technical contact.
        serial-number: A version number that is incremented each time the zone data is modified.
        refresh, retry, expire, minimum-ttl: Timers controlling zone maintenance.
NS: An NS (Name Server) record is a type of DNS (Domain Name System) record used to delegate a subdomain or specify authoritative DNS servers for a domain. NS records indicate which DNS servers are responsible for handling queries related to a specific domain or subdomain.
    - example.com. IN NS ns1.example.com.
        example.com: The domain for which the NS record is configured.
        IN: The class of the record (Internet class).
        NS: The type of the record (NS).
        ns1.example.com: The domain name of an authoritative DNS server for the specified domain.
    multiple NS records:
        example.com. IN NS ns1.example.com.
        example.com. IN NS ns2.example.com.

        In this example, the NS records indicate that ns1.example.com and ns2.example.com are authoritative DNS servers for the example.com domain. DNS queries for subdomains or other information related to example.com are directed to these authoritative servers.

## other

AXFR, or "Full Zone Transfer," is a mechanism in DNS that allows a secondary DNS server to transfer a full copy of a DNS zone from a primary DNS server. This mechanism is commonly used in a master-slave DNS server setup, where one server (the primary) maintains the authoritative copy of the DNS zone, and one or more other servers (the secondaries) replicate the zone information through zone transfers.

