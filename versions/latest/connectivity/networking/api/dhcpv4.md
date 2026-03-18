---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/networking/api/dhcpv4.html
original_path: connectivity/networking/api/dhcpv4.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# DHCPv4

## [Overview](#id1)

The Dynamic Host Configuration Protocol (DHCP) is a network management protocol
used on IPv4 networks. A DHCPv4 server dynamically assigns an IPv4 address
and other network configuration parameters to each device on a network so they
can communicate with other IP networks.
See this
[DHCP Wikipedia article](https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol)
for a detailed overview of how DHCP works.

Note that Zephyr only supports DHCP client functionality.

## [Sample usage](#id2)

See [DHCPv4 client](../../../samples/net/dhcpv4_client/README.md#dhcpv4-client "Start a DHCPv4 client to obtain an IPv4 address from a DHCPv4 server.") sample application for details.

## [API Reference](#id3)

Related code samples

[DHCPv4 client](../../../samples/net/dhcpv4_client/README.md#dhcpv4-client "Start a DHCPv4 client to obtain an IPv4 address from a DHCPv4 server.")
:   Start a DHCPv4 client to obtain an IPv4 address from a DHCPv4 server.

*group* dhcpv4
:   DHCPv4.

    Enums

    enum net\_dhcpv4\_msg\_type
    :   DHCPv4 message types.

        These enumerations represent RFC2131 defined msy type codes, hence they should not be renumbered.

        Additions, removald and reorders in this definition must be reflected within corresponding changes to net\_dhcpv4\_msg\_type\_name.

        *Values:*

        enumerator NET\_DHCPV4\_MSG\_TYPE\_DISCOVER = 1

        enumerator NET\_DHCPV4\_MSG\_TYPE\_OFFER = 2

        enumerator NET\_DHCPV4\_MSG\_TYPE\_REQUEST = 3

        enumerator NET\_DHCPV4\_MSG\_TYPE\_DECLINE = 4

        enumerator NET\_DHCPV4\_MSG\_TYPE\_ACK = 5

        enumerator NET\_DHCPV4\_MSG\_TYPE\_NAK = 6

        enumerator NET\_DHCPV4\_MSG\_TYPE\_RELEASE = 7

        enumerator NET\_DHCPV4\_MSG\_TYPE\_INFORM = 8

    Functions

    void net\_dhcpv4\_start(struct [net\_if](net_if.md#c.net_if "net_if") \*iface)
    :   Start DHCPv4 client on an iface.

        Start DHCPv4 client on a given interface. DHCPv4 client will start negotiation for IPv4 address. Once the negotiation is success IPv4 address details will be added to interface.

        Parameters:
        :   - **iface** – A valid pointer on an interface

    void net\_dhcpv4\_stop(struct [net\_if](net_if.md#c.net_if "net_if") \*iface)
    :   Stop DHCPv4 client on an iface.

        Stop DHCPv4 client on a given interface. DHCPv4 client will remove all configuration obtained from a DHCP server from the interface and stop any further negotiation with the server.

        Parameters:
        :   - **iface** – A valid pointer on an interface

    void net\_dhcpv4\_restart(struct [net\_if](net_if.md#c.net_if "net_if") \*iface)
    :   Restart DHCPv4 client on an iface.

        Restart DHCPv4 client on a given interface. DHCPv4 client will restart the state machine without any of the initial delays used in start.

        Parameters:
        :   - **iface** – A valid pointer on an interface

    const char \*net\_dhcpv4\_msg\_type\_name(enum [net\_dhcpv4\_msg\_type](#c.net_dhcpv4_msg_type) msg\_type)
    :   Return a text representation of the msg\_type.

        Parameters:
        :   - **msg\_type** – The msg\_type to be converted to text

        Returns:
        :   A text representation of msg\_type
