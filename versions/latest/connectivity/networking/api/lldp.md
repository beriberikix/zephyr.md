---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/networking/api/lldp.html
original_path: connectivity/networking/api/lldp.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Link Layer Discovery Protocol

## [Overview](#id1)

The Link Layer Discovery Protocol (LLDP) is a vendor-neutral link layer
protocol used by network devices for advertising their identity, capabilities,
and neighbors on a wired Ethernet network.

For more information, see this
[LLDP Wikipedia article](https://en.wikipedia.org/wiki/Link_Layer_Discovery_Protocol).

## [API Reference](#id2)

Related code samples

[Link Layer Discovery Protocol (LLDP)](../../../samples/net/lldp/README.md#lldp "Enable LLDP support and setup VLANs.")
:   Enable LLDP support and setup VLANs.

*group* lldp
:   LLDP definitions and helpers.

    Defines

    net\_lldp\_set\_lldpdu(iface)
    :   Set LLDP protocol data unit (LLDPDU) for the network interface.

        Parameters:
        :   - **iface** – Network interface

        Returns:
        :   <0 if error, index in lldp array if iface is found there

    net\_lldp\_unset\_lldpdu(iface)
    :   Unset LLDP protocol data unit (LLDPDU) for the network interface.

        Parameters:
        :   - **iface** – Network interface

    Typedefs

    typedef enum [net\_verdict](net_core.md#c.net_verdict "net_verdict") (\*net\_lldp\_recv\_cb\_t)(struct [net\_if](net_if.md#c.net_if "net_if") \*iface, struct [net\_pkt](net_pkt.md#c.net_pkt "net_pkt") \*pkt)
    :   LLDP Receive packet callback.

        Callback gets called upon receiving packet. It is responsible for freeing packet or indicating to the stack that it needs to free packet by returning correct [net\_verdict](net_core.md#group__net__core_1ga8e5393f3bdd85491f221324e637c3896).

        Returns:

        - NET\_DROP, if packet was invalid, rejected or we want the stack to free it. In this case the core stack will free the packet.
        - NET\_OK, if the packet was accepted, in this case the ownership of the [net\_pkt](net_pkt.md#structnet__pkt) goes to callback and core network stack will forget it.

    Enums

    enum net\_lldp\_tlv\_type
    :   TLV Types.

        Please refer to table 8-1 from IEEE 802.1AB standard.

        *Values:*

        enumerator LLDP\_TLV\_END\_LLDPDU = 0
        :   End Of LLDPDU (optional).

        enumerator LLDP\_TLV\_CHASSIS\_ID = 1
        :   Chassis ID (mandatory).

        enumerator LLDP\_TLV\_PORT\_ID = 2
        :   Port ID (mandatory).

        enumerator LLDP\_TLV\_TTL = 3
        :   Time To Live (mandatory).

        enumerator LLDP\_TLV\_PORT\_DESC = 4
        :   Port Description (optional).

        enumerator LLDP\_TLV\_SYSTEM\_NAME = 5
        :   System Name (optional).

        enumerator LLDP\_TLV\_SYSTEM\_DESC = 6
        :   System Description (optional).

        enumerator LLDP\_TLV\_SYSTEM\_CAPABILITIES = 7
        :   System Capability (optional).

        enumerator LLDP\_TLV\_MANAGEMENT\_ADDR = 8
        :   Management Address (optional).

        enumerator LLDP\_TLV\_ORG\_SPECIFIC = 127
        :   Org specific TLVs (optional).

    Functions

    int net\_lldp\_config(struct [net\_if](net_if.md#c.net_if "net_if") \*iface, const struct [net\_lldpdu](#c.net_lldpdu) \*lldpdu)
    :   Set the LLDP data unit for a network interface.

        Parameters:
        :   - **iface** – Network interface
            - **lldpdu** – LLDP data unit struct

        Returns:
        :   0 if ok, <0 if error

    int net\_lldp\_config\_optional(struct [net\_if](net_if.md#c.net_if "net_if") \*iface, const uint8\_t \*tlv, size\_t len)
    :   Set the Optional LLDP TLVs for a network interface.

        Parameters:
        :   - **iface** – Network interface
            - **tlv** – LLDP optional TLVs following mandatory part
            - **len** – Length of the optional TLVs

        Returns:
        :   0 if ok, <0 if error

    void net\_lldp\_init(void)
    :   Initialize LLDP engine.

    int net\_lldp\_register\_callback(struct [net\_if](net_if.md#c.net_if "net_if") \*iface, [net\_lldp\_recv\_cb\_t](#c.net_lldp_recv_cb_t) cb)
    :   Register LLDP Rx callback function.

        Parameters:
        :   - **iface** – Network interface
            - **cb** – Callback function

        Returns:
        :   0 if ok, < 0 if error

    enum [net\_verdict](net_core.md#c.net_verdict "net_verdict") net\_lldp\_recv(struct [net\_if](net_if.md#c.net_if "net_if") \*iface, struct [net\_pkt](net_pkt.md#c.net_pkt "net_pkt") \*pkt)
    :   Parse LLDP packet.

        Parameters:
        :   - **iface** – Network interface
            - **pkt** – Network packet

        Returns:
        :   Return the policy for network buffer

    struct net\_lldp\_chassis\_tlv
    :   *#include <lldp.h>*

        Chassis ID TLV, see chapter 8.5.2 in IEEE 802.1AB.

        Public Members

        uint16\_t type\_length
        :   7 bits for type, 9 bits for length

        uint8\_t subtype
        :   ID subtype.

        uint8\_t value[NET\_LLDP\_CHASSIS\_ID\_VALUE\_LEN]
        :   Chassis ID value.

    struct net\_lldp\_port\_tlv
    :   *#include <lldp.h>*

        Port ID TLV, see chapter 8.5.3 in IEEE 802.1AB.

        Public Members

        uint16\_t type\_length
        :   7 bits for type, 9 bits for length

        uint8\_t subtype
        :   ID subtype.

        uint8\_t value[NET\_LLDP\_PORT\_ID\_VALUE\_LEN]
        :   Port ID value.

    struct net\_lldp\_time\_to\_live\_tlv
    :   *#include <lldp.h>*

        Time To Live TLV, see chapter 8.5.4 in IEEE 802.1AB.

        Public Members

        uint16\_t type\_length
        :   7 bits for type, 9 bits for length

        uint16\_t ttl
        :   Time To Live (TTL) value.

    struct net\_lldpdu
    :   *#include <lldp.h>*

        LLDP Data Unit (LLDPDU) shall contain the following ordered TLVs as stated in “8.2 LLDPDU format” from the IEEE 802.1AB.

        Public Members

        struct [net\_lldp\_chassis\_tlv](#c.net_lldp_chassis_tlv) chassis\_id
        :   Mandatory Chassis TLV.

        struct [net\_lldp\_port\_tlv](#c.net_lldp_port_tlv) port\_id
        :   Mandatory Port TLV.

        struct [net\_lldp\_time\_to\_live\_tlv](#c.net_lldp_time_to_live_tlv) ttl
        :   Mandatory TTL TLV.
