---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/networking/api/vlan.html
original_path: connectivity/networking/api/vlan.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Virtual LAN (VLAN) Support

## [Overview](#id1)

[Virtual LAN](https://wikipedia.org/wiki/Virtual_LAN) (VLAN) is a
partitioned and isolated computer network at the data link layer
(OSI layer 2). For ethernet network this refers to
[IEEE 802.1Q](https://en.wikipedia.org/wiki/IEEE_802.1Q)

In Zephyr, each individual VLAN is modeled as a virtual network interface.
This means that there is an ethernet network interface that corresponds to
a real physical ethernet port in the system. A virtual network interface is
created for each VLAN, and this virtual network interface connects to the
real network interface. This is similar to how Linux implements VLANs. The
*eth0* is the real network interface and *vlan0* is a virtual network interface
that is run on top of *eth0*.

VLAN support must be enabled at compile time by setting option
[`CONFIG_NET_VLAN`](../../../kconfig.md#CONFIG_NET_VLAN "CONFIG_NET_VLAN") and [`CONFIG_NET_VLAN_COUNT`](../../../kconfig.md#CONFIG_NET_VLAN_COUNT "CONFIG_NET_VLAN_COUNT") to reflect how
many network interfaces there will be in the system. For example, if there is
one network interface without VLAN support, and two with VLAN support, the
[`CONFIG_NET_VLAN_COUNT`](../../../kconfig.md#CONFIG_NET_VLAN_COUNT "CONFIG_NET_VLAN_COUNT") option should be set to 3.

Even if VLAN is enabled in a `prj.conf` file, the VLAN needs to be
activated at runtime by the application. The VLAN API provides a
[`net_eth_vlan_enable()`](ethernet.md#c.net_eth_vlan_enable "net_eth_vlan_enable") function to do that. The application needs
to give the network interface and desired VLAN tag as a parameter to that
function. The VLAN tagging for a given network interface can be disabled by a
[`net_eth_vlan_disable()`](ethernet.md#c.net_eth_vlan_disable "net_eth_vlan_disable") function. The application needs to configure
the VLAN network interface itself, such as setting the IP address, etc.

See also the [VLAN sample application](../../../samples/net/vlan/README.md#vlan "Setup two virtual LAN networks and use net-shell to view the networks' settings.") for API usage
example. The source code for that sample application can be found at
[samples/net/vlan](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/vlan).

The net-shell module contains *net vlan add* and *net vlan del* commands
that can be used to enable or disable VLAN tags for a given network interface.

See the [IEEE 802.1Q spec](https://ieeexplore.ieee.org/document/6991462/) for more information about ethernet VLANs.

## [API Reference](#id2)

Related code samples

[Virtual LAN](../../../samples/net/vlan/README.md#vlan "Setup two virtual LAN networks and use net-shell to view the networks' settings.")
:   Setup two virtual LAN networks and use net-shell to view the networks' settings.

*group* vlan\_api
:   VLAN definitions and helpers.

    Defines

    NET\_VLAN\_TAG\_UNSPEC
    :   Unspecified VLAN tag value.

    Functions

    static inline uint16\_t net\_eth\_vlan\_get\_vid(uint16\_t tci)
    :   Get VLAN identifier from TCI.

        Parameters:
        :   - **tci** – VLAN tag control information.

        Returns:
        :   VLAN identifier.

    static inline uint8\_t net\_eth\_vlan\_get\_dei(uint16\_t tci)
    :   Get Drop Eligible Indicator from TCI.

        Parameters:
        :   - **tci** – VLAN tag control information.

        Returns:
        :   Drop eligible indicator.

    static inline uint8\_t net\_eth\_vlan\_get\_pcp(uint16\_t tci)
    :   Get Priority Code Point from TCI.

        Parameters:
        :   - **tci** – VLAN tag control information.

        Returns:
        :   Priority code point.

    static inline uint16\_t net\_eth\_vlan\_set\_vid(uint16\_t tci, uint16\_t vid)
    :   Set VLAN identifier to TCI.

        Parameters:
        :   - **tci** – VLAN tag control information.
            - **vid** – VLAN identifier.

        Returns:
        :   New TCI value.

    static inline uint16\_t net\_eth\_vlan\_set\_dei(uint16\_t tci, bool dei)
    :   Set Drop Eligible Indicator to TCI.

        Parameters:
        :   - **tci** – VLAN tag control information.
            - **dei** – Drop eligible indicator.

        Returns:
        :   New TCI value.

    static inline uint16\_t net\_eth\_vlan\_set\_pcp(uint16\_t tci, uint8\_t pcp)
    :   Set Priority Code Point to TCI.

        Parameters:
        :   - **tci** – VLAN tag control information.
            - **pcp** – Priority code point.

        Returns:
        :   New TCI value.
