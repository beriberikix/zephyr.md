---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/connectivity/networking/api/net_if.html
original_path: connectivity/networking/api/net_if.html
---

# Network Interface

## [Overview](#id1)

The network interface is a nexus that ties the network device drivers
and the upper part of the network stack together. All the sent and received
data is transferred via a network interface. The network interfaces cannot be
created at runtime. A special linker section will contain information about them
and that section is populated at linking time.

Network interfaces are created by `NET_DEVICE_INIT()` macro.
For Ethernet network, a macro called `ETH_NET_DEVICE_INIT()` should be used
instead as it will create VLAN interfaces automatically if
[`CONFIG_NET_VLAN`](../../../kconfig.md#CONFIG_NET_VLAN "CONFIG_NET_VLAN") is enabled. These macros are typically used in
network device driver source code.

The network interface can be turned ON by calling `net_if_up()` and OFF
by calling `net_if_down()`. When the device is powered ON, the network
interface is also turned ON by default.

The network interfaces can be referenced either by a `struct net_if *`
pointer or by a network interface index. The network interface can be
resolved from its index by calling `net_if_get_by_index()` and from interface
pointer by calling `net_if_get_by_iface()`.

The IP address for network devices must be set for them to be connectable.
In a typical dynamic network environment, IP addresses are set automatically
by DHCPv4, for example. If needed though, the application can set a device’s
IP address manually. See the API documentation below for functions such as
`net_if_ipv4_addr_add()` that do that.

The `net_if_get_default()` returns a *default* network interface. What
this default interface means can be configured via options like
[`CONFIG_NET_DEFAULT_IF_FIRST`](../../../kconfig.md#CONFIG_NET_DEFAULT_IF_FIRST "CONFIG_NET_DEFAULT_IF_FIRST") and
[`CONFIG_NET_DEFAULT_IF_ETHERNET`](../../../kconfig.md#CONFIG_NET_DEFAULT_IF_ETHERNET "CONFIG_NET_DEFAULT_IF_ETHERNET").
See Kconfig file [subsys/net/ip/Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig) what options are available for
selecting the default network interface.

The transmitted and received network packets can be classified via a network
packet priority. This is typically done in Ethernet networks when virtual LANs
(VLANs) are used. Higher priority packets can be sent or received earlier than
lower priority packets. The traffic class setup can be configured by
[`CONFIG_NET_TC_TX_COUNT`](../../../kconfig.md#CONFIG_NET_TC_TX_COUNT "CONFIG_NET_TC_TX_COUNT") and [`CONFIG_NET_TC_RX_COUNT`](../../../kconfig.md#CONFIG_NET_TC_RX_COUNT "CONFIG_NET_TC_RX_COUNT") options.

If the [`CONFIG_NET_PROMISCUOUS_MODE`](../../../kconfig.md#CONFIG_NET_PROMISCUOUS_MODE "CONFIG_NET_PROMISCUOUS_MODE") is enabled and if the underlying
network technology supports promiscuous mode, then it is possible to receive
all the network packets that the network device driver is able to receive.
See [Promiscuous Mode](promiscuous.md#promiscuous-interface) API for more details.

## [Network interface state management](#id2)

Zephyr distinguishes between two interface states: administrative state and
operational state, as described in RFC 2863. The administrative state indicate
whether an interface is turned ON or OFF. This state is represented by
[`NET_IF_UP`](../../../doxygen/html/group__net__if.md#ggae691e5537917ffce27ad0db82c730371ab0ab7393d643354c46c3437d74c15840) flag and is controlled by the application. It can be
changed by calling [`net_if_up()`](../../../doxygen/html/group__net__if.md#ga02644cc623fc7a8878c17d54984e4210) or [`net_if_down()`](../../../doxygen/html/group__net__if.md#ga2187650062d6139b9f4b81745a206803) functions.
Network drivers or L2 implementations should not change administrative state on
their own.

Bringing an interface up however not always means that the interface is ready to
transmit packets. Because of that, operational state, which represents the
internal interface status, was implemented. The operational state is updated
whenever one of the following conditions take place:

> - The interface is brought up/down by the application (administrative state
>   changes).
> - The interface is notified by the driver/L2 that PHY status has changed.
> - The interface is notified by the driver/L2 that it joined/left a network.

The PHY status is represented with [`NET_IF_LOWER_UP`](../../../doxygen/html/group__net__if.md#ggae691e5537917ffce27ad0db82c730371ab1a529826bad6b4bcd04185372f97d6d) flag and can
be changed with [`net_if_carrier_on()`](../../../doxygen/html/group__net__if.md#ga35e5db3a631ac9039f14d86e59fc0dcc) and [`net_if_carrier_off()`](../../../doxygen/html/group__net__if.md#ga6839941422a88c1f707ab70ea34df323). By
default, the flag is set on a newly initialized interface. An example of an
event that changes the carrier state is Ethernet cable being plugged in or out.

The network association status is represented with [`NET_IF_DORMANT`](../../../doxygen/html/group__net__if.md#ggae691e5537917ffce27ad0db82c730371a7dd1db72a37b1fbc4c4491ce1c75238d)
flag and can be changed with [`net_if_dormant_on()`](../../../doxygen/html/group__net__if.md#ga89a3374d4bb116460a7b7c50a750b593) and
[`net_if_dormant_off()`](../../../doxygen/html/group__net__if.md#ga1c31fac887d944ac0a16aad70e889496). By default, the flag is cleared on a newly
initialized interface. An example of an event that changes the dormant state is
a Wi-Fi driver successfully connecting to an access point. In this scenario,
driver should set the dormant state to ON during initialization, and once it
detects that it connected to a Wi-Fi network, the dormant state should be set
to OFF.

The operational state of an interface is updated as follows:

> - `!net_if_is_admin_up()`
>
>   Interface is in [`NET_IF_OPER_DOWN`](../../../doxygen/html/group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9adb20a95215310c420f8dae7e17a2f367).
> - `net_if_is_admin_up() && !net_if_is_carrier_ok()`
>
>   Interface is in [`NET_IF_OPER_DOWN`](../../../doxygen/html/group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9adb20a95215310c420f8dae7e17a2f367) or
>   [`NET_IF_OPER_LOWERLAYERDOWN`](../../../doxygen/html/group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9ae7e9b8b12ae618a5ee1483dee916aab4) if the interface is stacked
>   (virtual).
> - `net_if_is_admin_up() && net_if_is_carrier_ok() && net_if_is_dormant()`
>
>   Interface is in [`NET_IF_OPER_DORMANT`](../../../doxygen/html/group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a5cbe2aa27a444444d4acf122113d430d).
> - `net_if_is_admin_up() && net_if_is_carrier_ok() && !net_if_is_dormant()`
>
>   Interface is in [`NET_IF_OPER_UP`](../../../doxygen/html/group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a6b99bfc28d831292029761d74209ee03).

Only after an interface enters [`NET_IF_OPER_UP`](../../../doxygen/html/group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a6b99bfc28d831292029761d74209ee03) state the
[`NET_IF_RUNNING`](../../../doxygen/html/group__net__if.md#ggae691e5537917ffce27ad0db82c730371add3e2ecdcd5de3154f9bd2836428a25a) flag is set on the interface indicating that the
interface is ready to be used by the application.

## [API Reference](#id3)

[Network Interface abstraction layer](../../../doxygen/html/group__net__if.md)

Related code samples

- [IPv4 autoconf client](../../../samples/net/ipv4_autoconf/README.md#ipv4-autoconf "Perform IPv4 autoconfiguration and self-assign a random IPv4 address")Perform IPv4 autoconfiguration and self-assign a random IPv4 address
- [Network management socket](../../../samples/net/sockets/net_mgmt/README.md#sockets-net-mgmt "Listen to network management events using a network management socket.")Listen to network management events using a network management socket.
- [Telnet console](../../../samples/net/telnet/README.md#telnet-console "Access Zephyr shell over telnet.")Access Zephyr shell over telnet.
- [Virtual LAN](../../../samples/net/vlan/README.md#vlan "Setup two virtual LAN networks and use net-shell to view the networks' settings.")Setup two virtual LAN networks and use net-shell to view the networks' settings.
