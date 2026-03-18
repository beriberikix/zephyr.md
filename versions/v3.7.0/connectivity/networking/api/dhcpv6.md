---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/networking/api/dhcpv6.html
original_path: connectivity/networking/api/dhcpv6.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# DHCPv6

## [Overview](#id1)

The Dynamic Host Configuration Protocol (DHCP) for IPv6 is a network management protocol
used on IPv6 based networks. A DHCPv6 server dynamically assigns an IPv6 address
and other network configuration parameters to each device on a network so they
can communicate with other IP networks.
See this
[DHCPv6 Wikipedia article](https://en.wikipedia.org/wiki/DHCPv6)
for a detailed overview of how DHCPv6 works.

Note that Zephyr only supports DHCPv6 client functionality.

## [API Reference](#id2)

*group* DHCPv6
:   DHCPv6.

    Functions

    void net\_dhcpv6\_start(struct [net\_if](net_if.md#c.net_if "net_if") \*iface, struct [net\_dhcpv6\_params](#c.net_dhcpv6_params) \*params)
    :   Start DHCPv6 client on an iface.

        Start DHCPv6 client on a given interface. DHCPv6 client will start negotiation for IPv6 address and/or prefix, depending on the configuration. Once the negotiation is complete, IPv6 address/prefix details will be added to the interface.

        Parameters:
        :   - **iface** – A valid pointer to a network interface
            - **params** – DHCPv6 client configuration parameters.

    void net\_dhcpv6\_stop(struct [net\_if](net_if.md#c.net_if "net_if") \*iface)
    :   Stop DHCPv6 client on an iface.

        Stop DHCPv6 client on a given interface. DHCPv6 client will remove all configuration obtained from a DHCP server from the interface and stop any further negotiation with the server.

        Parameters:
        :   - **iface** – A valid pointer to a network interface

    void net\_dhcpv6\_restart(struct [net\_if](net_if.md#c.net_if "net_if") \*iface)
    :   Restart DHCPv6 client on an iface.

        Restart DHCPv6 client on a given interface. DHCPv6 client will restart the state machine without any of the initial delays.

        Parameters:
        :   - **iface** – A valid pointer to a network interface

    struct net\_dhcpv6\_params
    :   *#include <dhcpv6.h>*

        DHCPv6 client configuration parameters.

        Public Members

        bool request\_addr
        :   Request IPv6 address.

        bool request\_prefix
        :   Request IPv6 prefix.
