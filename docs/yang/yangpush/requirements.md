# yang push

server implementation
- dial out design
    - netconf sends a packet on port 6643 and this triggers a SSH dial-in session
    - gnmi: dial out (first)
- you get a packet and need to find the relation to the ip -> vendor/version/schema

# simulated yang server

- create an on-change event handler: data is updated at x intervals
- sends gnmi and netconf data