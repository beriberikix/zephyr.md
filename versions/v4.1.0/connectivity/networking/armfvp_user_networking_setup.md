---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/connectivity/networking/armfvp_user_networking_setup.html
original_path: connectivity/networking/armfvp_user_networking_setup.html
---

# Networking with Arm FVP User Mode

This page is intended to serve as a starting point for anyone interested in
using Arm FVP user mode networking with Zephyr.

## [Introduction](#id1)

User mode networking emulates a built-in IP router and DHCP server, and routes
TCP and UDP traffic between the guest and host. It uses the user mode socket
layer of the host to communicate with other hosts. This allows the use of
a significant number of IP network services without requiring administrative
privileges, or the installation of a separate driver on the host on which
the model is running.

By default, Arm FVP uses the `172.20.51.0/24` network and runs a gateway at
`172.20.51.254`. This gateway also functions as a DHCP server for the GOS,
allowing it to be automatically assigned with an IP address `172.20.51.1`.

More details about Arm FVP user mode networking can be obtained from here:
[https://developer.arm.com/documentation/100964/latest/Introduction-to-Fast-Models/User-mode-networking](https://developer.arm.com/documentation/100964/latest/Introduction-to-Fast-Models/User-mode-networking)

## [Using Arm FVP User Mode Networking with Zephyr](#id2)

Arm FVP user mode networking can be enabled in any applications and it doesn’t
need any configurations on the host system. This feature has been enabled in
DHCPv4 client sample.
See [DHCPv4 client](../../samples/net/dhcpv4_client/README.md#dhcpv4-client "Start a DHCPv4 client to obtain an IPv4 address from a DHCPv4 server.") sample application.

## [Limitations](#id3)

- You can use TCP and UDP over IP, but not ICMP (ping).
- User mode networking does not support forwarding UDP ports on the host to
  the model.
- You can only use DHCP within the private network.
- You can only make inward connections by mapping TCP ports on the host to
  the model. This is common to all implementations that provide host
  connectivity using NAT.
- Operations that require privileged source ports, for example NFS in its
  default configuration, do not work.
- If setup fails, or the parameter syntax is incorrect, there is no error
  reporting.
