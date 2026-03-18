---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/networking/api/dhcpv4.html
original_path: connectivity/networking/api/dhcpv4.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# DHCPv4

## [Overview](#id1)

The Dynamic Host Configuration Protocol (DHCP) is a network management protocol
used on IPv4 networks. A DHCPv4 server dynamically assigns an IPv4 address
and other network configuration parameters to each device on a network so they
can communicate with other IP networks.
See this
[DHCP Wikipedia article](https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol)
for a detailed overview of how DHCP works.

Note that Zephyr supports both DHCPv4 client and server functionality.

## [Sample usage](#id2)

See [DHCPv4 client](../../../samples/net/dhcpv4_client/README.md#dhcpv4-client "Start a DHCPv4 client to obtain an IPv4 address from a DHCPv4 server.") sample application for details.

## [API Reference](#id3)

Related code samples

[DHCPv4 client](../../../samples/net/dhcpv4_client/README.md#dhcpv4-client "Start a DHCPv4 client to obtain an IPv4 address from a DHCPv4 server.")
:   Start a DHCPv4 client to obtain an IPv4 address from a DHCPv4 server.

*group* DHCPv4
:   DHCPv4.

    Typedefs

    typedef void (\*net\_dhcpv4\_option\_callback\_handler\_t)(struct net\_dhcpv4\_option\_callback \*cb, size\_t length, enum [net\_dhcpv4\_msg\_type](#c.net_dhcpv4_msg_type) msg\_type, struct [net\_if](net_if.md#c.net_if "net_if") \*iface)
    :   Define the application callback handler function signature.

        Note: cb pointer can be used to retrieve private data through [CONTAINER\_OF()](../../../kernel/util/index.md#group__sys-util_1gac5bc561d1bfd1bf68877fe577779bd2f) if original struct net\_dhcpv4\_option\_callback is stored in another private structure.

        Param cb:
        :   Original struct net\_dhcpv4\_option\_callback owning this handler

        Param length:
        :   The length of data returned by the server. If this is greater than cb->max\_length, only cb->max\_length bytes will be available in cb->data

        Param msg\_type:
        :   Type of DHCP message that triggered the callback

        Param iface:
        :   The interface on which the DHCP message was received

    Enums

    enum net\_dhcpv4\_msg\_type
    :   DHCPv4 message types.

        These enumerations represent RFC2131 defined msy type codes, hence they should not be renumbered.

        Additions, removald and reorders in this definition must be reflected within corresponding changes to net\_dhcpv4\_msg\_type\_name.

        *Values:*

        enumerator NET\_DHCPV4\_MSG\_TYPE\_DISCOVER = 1
        :   Discover message.

        enumerator NET\_DHCPV4\_MSG\_TYPE\_OFFER = 2
        :   Offer message.

        enumerator NET\_DHCPV4\_MSG\_TYPE\_REQUEST = 3
        :   Request message.

        enumerator NET\_DHCPV4\_MSG\_TYPE\_DECLINE = 4
        :   Decline message.

        enumerator NET\_DHCPV4\_MSG\_TYPE\_ACK = 5
        :   Acknowledge message.

        enumerator NET\_DHCPV4\_MSG\_TYPE\_NAK = 6
        :   Negative acknowledge message.

        enumerator NET\_DHCPV4\_MSG\_TYPE\_RELEASE = 7
        :   Release message.

        enumerator NET\_DHCPV4\_MSG\_TYPE\_INFORM = 8
        :   Inform message.

    Functions

    static inline void net\_dhcpv4\_init\_option\_callback(struct net\_dhcpv4\_option\_callback \*callback, [net\_dhcpv4\_option\_callback\_handler\_t](#c.net_dhcpv4_option_callback_handler_t) handler, uint8\_t option, void \*data, size\_t max\_length)
    :   Helper to initialize a struct net\_dhcpv4\_option\_callback properly.

        Parameters:
        :   - **callback** – A valid Application’s callback structure pointer.
            - **handler** – A valid handler function pointer.
            - **option** – The DHCP option the callback responds to.
            - **data** – A pointer to a buffer for max\_length bytes.
            - **max\_length** – The maximum length of the data returned.

    int net\_dhcpv4\_add\_option\_callback(struct net\_dhcpv4\_option\_callback \*cb)
    :   Add an application callback.

        Parameters:
        :   - **cb** – A valid application’s callback structure pointer.

        Returns:
        :   0 if successful, negative errno code on failure.

    int net\_dhcpv4\_remove\_option\_callback(struct net\_dhcpv4\_option\_callback \*cb)
    :   Remove an application callback.

        Parameters:
        :   - **cb** – A valid application’s callback structure pointer.

        Returns:
        :   0 if successful, negative errno code on failure.

    static inline void net\_dhcpv4\_init\_option\_vendor\_callback(struct net\_dhcpv4\_option\_callback \*callback, [net\_dhcpv4\_option\_callback\_handler\_t](#c.net_dhcpv4_option_callback_handler_t) handler, uint8\_t option, void \*data, size\_t max\_length)
    :   Helper to initialize a struct net\_dhcpv4\_option\_callback for encapsulated vendor-specific options properly.

        Parameters:
        :   - **callback** – A valid Application’s callback structure pointer.
            - **handler** – A valid handler function pointer.
            - **option** – The DHCP encapsulated vendor-specific option the callback responds to.
            - **data** – A pointer to a buffer for max\_length bytes.
            - **max\_length** – The maximum length of the data returned.

    int net\_dhcpv4\_add\_option\_vendor\_callback(struct net\_dhcpv4\_option\_callback \*cb)
    :   Add an application callback for encapsulated vendor-specific options.

        Parameters:
        :   - **cb** – A valid application’s callback structure pointer.

        Returns:
        :   0 if successful, negative errno code on failure.

    int net\_dhcpv4\_remove\_option\_vendor\_callback(struct net\_dhcpv4\_option\_callback \*cb)
    :   Remove an application callback for encapsulated vendor-specific options.

        Parameters:
        :   - **cb** – A valid application’s callback structure pointer.

        Returns:
        :   0 if successful, negative errno code on failure.

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
