---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/networking/api/net_if.html
original_path: connectivity/networking/api/net_if.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

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
[`NET_IF_UP`](#c.net_if_flag.NET_IF_UP) flag and is controlled by the application. It can be
changed by calling [`net_if_up()`](#c.net_if_up) or [`net_if_down()`](#c.net_if_down) functions.
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

The PHY status is represented with [`NET_IF_LOWER_UP`](#c.net_if_flag.NET_IF_LOWER_UP) flag and can
be changed with [`net_if_carrier_on()`](#c.net_if_carrier_on) and [`net_if_carrier_off()`](#c.net_if_carrier_off). By
default, the flag is set on a newly initialized interface. An example of an
event that changes the carrier state is Ethernet cable being plugged in or out.

The network association status is represented with [`NET_IF_DORMANT`](#c.net_if_flag.NET_IF_DORMANT)
flag and can be changed with [`net_if_dormant_on()`](#c.net_if_dormant_on) and
[`net_if_dormant_off()`](#c.net_if_dormant_off). By default, the flag is cleared on a newly
initialized interface. An example of an event that changes the dormant state is
a Wi-Fi driver successfully connecting to an access point. In this scenario,
driver should set the dormant state to ON during initialization, and once it
detects that it connected to a Wi-Fi network, the dormant state should be set
to OFF.

The operational state of an interface is updated as follows:

> - `!net_if_is_admin_up()`
>
>   Interface is in [`NET_IF_OPER_DOWN`](#c.net_if_oper_state.NET_IF_OPER_DOWN).
> - `net_if_is_admin_up() && !net_if_is_carrier_ok()`
>
>   Interface is in [`NET_IF_OPER_DOWN`](#c.net_if_oper_state.NET_IF_OPER_DOWN) or
>   [`NET_IF_OPER_LOWERLAYERDOWN`](#c.net_if_oper_state.NET_IF_OPER_LOWERLAYERDOWN) if the interface is stacked
>   (virtual).
> - `net_if_is_admin_up() && net_if_is_carrier_ok() && net_if_is_dormant()`
>
>   Interface is in [`NET_IF_OPER_DORMANT`](#c.net_if_oper_state.NET_IF_OPER_DORMANT).
> - `net_if_is_admin_up() && net_if_is_carrier_ok() && !net_if_is_dormant()`
>
>   Interface is in [`NET_IF_OPER_UP`](#c.net_if_oper_state.NET_IF_OPER_UP).

Only after an interface enters [`NET_IF_OPER_UP`](#c.net_if_oper_state.NET_IF_OPER_UP) state the
[`NET_IF_RUNNING`](#c.net_if_flag.NET_IF_RUNNING) flag is set on the interface indicating that the
interface is ready to be used by the application.

## [API Reference](#id3)

Related code samples

[IPv4 autoconf client](../../../samples/net/ipv4_autoconf/README.md#ipv4-autoconf "Perform IPv4 autoconfiguration and self-assign a random IPv4 address")
:   Perform IPv4 autoconfiguration and self-assign a random IPv4 address

[Network management socket](../../../samples/net/sockets/net_mgmt/README.md#sockets-net-mgmt "Listen to network management events using a network management socket.")
:   Listen to network management events using a network management socket.

[Telnet console](../../../samples/net/telnet/README.md#telnet-console "Access Zephyr shell over telnet.")
:   Access Zephyr shell over telnet.

[Virtual LAN](../../../samples/net/vlan/README.md#vlan "Setup two virtual LAN networks and use net-shell to view the networks' settings.")
:   Setup two virtual LAN networks and use net-shell to view the networks' settings.

*group* net\_if
:   Network Interface abstraction layer.

    Defines

    NET\_DEVICE\_INIT(dev\_id, name, init\_fn, pm, data, config, prio, api, l2, l2\_ctx\_type, mtu)
    :   Create a network interface and bind it to network device.

        Parameters:
        :   - **dev\_id** – Network device id.
            - **name** – The name this instance of the driver exposes to the system.
            - **init\_fn** – Address to the init function of the driver.
            - **pm** – Reference to struct [pm\_device](../../../services/pm/api/index.md#structpm__device) associated with the device. (optional).
            - **data** – Pointer to the device’s private data.
            - **config** – The address to the structure containing the configuration information for this instance of the driver.
            - **prio** – The initialization level at which configuration occurs.
            - **api** – Provides an initial pointer to the API function struct used by the driver. Can be NULL.
            - **l2** – Network L2 layer for this network interface.
            - **l2\_ctx\_type** – Type of L2 context data.
            - **mtu** – Maximum transfer unit in bytes for this network interface.

    NET\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, config, prio, api, l2, l2\_ctx\_type, mtu)
    :   Like NET\_DEVICE\_INIT but taking metadata from a devicetree node.

        Create a network interface and bind it to network device.

        Parameters:
        :   - **node\_id** – The devicetree node identifier.
            - **init\_fn** – Address to the init function of the driver.
            - **pm** – Reference to struct [pm\_device](../../../services/pm/api/index.md#structpm__device) associated with the device. (optional).
            - **data** – Pointer to the device’s private data.
            - **config** – The address to the structure containing the configuration information for this instance of the driver.
            - **prio** – The initialization level at which configuration occurs.
            - **api** – Provides an initial pointer to the API function struct used by the driver. Can be NULL.
            - **l2** – Network L2 layer for this network interface.
            - **l2\_ctx\_type** – Type of L2 context data.
            - **mtu** – Maximum transfer unit in bytes for this network interface.

    NET\_DEVICE\_DT\_INST\_DEFINE(inst, ...)
    :   Like NET\_DEVICE\_DT\_DEFINE for an instance of a DT\_DRV\_COMPAT compatible.

        Parameters:
        :   - **inst** – instance number. This is replaced by `DT_DRV_COMPAT(inst)` in the call to NET\_DEVICE\_DT\_DEFINE.
            - **...** – other parameters as expected by NET\_DEVICE\_DT\_DEFINE.

    NET\_DEVICE\_INIT\_INSTANCE(dev\_id, name, instance, init\_fn, pm, data, config, prio, api, l2, l2\_ctx\_type, mtu)
    :   Create multiple network interfaces and bind them to network device.

        If your network device needs more than one instance of a network interface, use this macro below and provide a different instance suffix each time (0, 1, 2, … or a, b, c … whatever works for you)

        Parameters:
        :   - **dev\_id** – Network device id.
            - **name** – The name this instance of the driver exposes to the system.
            - **instance** – Instance identifier.
            - **init\_fn** – Address to the init function of the driver.
            - **pm** – Reference to struct [pm\_device](../../../services/pm/api/index.md#structpm__device) associated with the device. (optional).
            - **data** – Pointer to the device’s private data.
            - **config** – The address to the structure containing the configuration information for this instance of the driver.
            - **prio** – The initialization level at which configuration occurs.
            - **api** – Provides an initial pointer to the API function struct used by the driver. Can be NULL.
            - **l2** – Network L2 layer for this network interface.
            - **l2\_ctx\_type** – Type of L2 context data.
            - **mtu** – Maximum transfer unit in bytes for this network interface.

    NET\_DEVICE\_DT\_DEFINE\_INSTANCE(node\_id, instance, init\_fn, pm, data, config, prio, api, l2, l2\_ctx\_type, mtu)
    :   Like NET\_DEVICE\_OFFLOAD\_INIT but taking metadata from a devicetree.

        Create multiple network interfaces and bind them to network device. If your network device needs more than one instance of a network interface, use this macro below and provide a different instance suffix each time (0, 1, 2, … or a, b, c … whatever works for you)

        Parameters:
        :   - **node\_id** – The devicetree node identifier.
            - **instance** – Instance identifier.
            - **init\_fn** – Address to the init function of the driver.
            - **pm** – Reference to struct [pm\_device](../../../services/pm/api/index.md#structpm__device) associated with the device. (optional).
            - **data** – Pointer to the device’s private data.
            - **config** – The address to the structure containing the configuration information for this instance of the driver.
            - **prio** – The initialization level at which configuration occurs.
            - **api** – Provides an initial pointer to the API function struct used by the driver. Can be NULL.
            - **l2** – Network L2 layer for this network interface.
            - **l2\_ctx\_type** – Type of L2 context data.
            - **mtu** – Maximum transfer unit in bytes for this network interface.

    NET\_DEVICE\_DT\_INST\_DEFINE\_INSTANCE(inst, ...)
    :   Like NET\_DEVICE\_DT\_DEFINE\_INSTANCE for an instance of a DT\_DRV\_COMPAT compatible.

        Parameters:
        :   - **inst** – instance number. This is replaced by `DT_DRV_COMPAT(inst)` in the call to NET\_DEVICE\_DT\_DEFINE\_INSTANCE.
            - **...** – other parameters as expected by NET\_DEVICE\_DT\_DEFINE\_INSTANCE.

    NET\_DEVICE\_OFFLOAD\_INIT(dev\_id, name, init\_fn, pm, data, config, prio, api, mtu)
    :   Create a offloaded network interface and bind it to network device.

        The offloaded network interface is implemented by a device vendor HAL or similar.

        Parameters:
        :   - **dev\_id** – Network device id.
            - **name** – The name this instance of the driver exposes to the system.
            - **init\_fn** – Address to the init function of the driver.
            - **pm** – Reference to struct [pm\_device](../../../services/pm/api/index.md#structpm__device) associated with the device. (optional).
            - **data** – Pointer to the device’s private data.
            - **config** – The address to the structure containing the configuration information for this instance of the driver.
            - **prio** – The initialization level at which configuration occurs.
            - **api** – Provides an initial pointer to the API function struct used by the driver. Can be NULL.
            - **mtu** – Maximum transfer unit in bytes for this network interface.

    NET\_DEVICE\_DT\_OFFLOAD\_DEFINE(node\_id, init\_fn, pm, data, config, prio, api, mtu)
    :   Like NET\_DEVICE\_OFFLOAD\_INIT but taking metadata from a devicetree node.

        Create a offloaded network interface and bind it to network device. The offloaded network interface is implemented by a device vendor HAL or similar.

        Parameters:
        :   - **node\_id** – The devicetree node identifier.
            - **init\_fn** – Address to the init function of the driver.
            - **pm** – Reference to struct [pm\_device](../../../services/pm/api/index.md#structpm__device) associated with the device. (optional).
            - **data** – Pointer to the device’s private data.
            - **config** – The address to the structure containing the configuration information for this instance of the driver.
            - **prio** – The initialization level at which configuration occurs.
            - **api** – Provides an initial pointer to the API function struct used by the driver. Can be NULL.
            - **mtu** – Maximum transfer unit in bytes for this network interface.

    NET\_DEVICE\_DT\_INST\_OFFLOAD\_DEFINE(inst, ...)
    :   Like NET\_DEVICE\_DT\_OFFLOAD\_DEFINE for an instance of a DT\_DRV\_COMPAT compatible.

        Parameters:
        :   - **inst** – instance number. This is replaced by `DT_DRV_COMPAT(inst)` in the call to NET\_DEVICE\_DT\_OFFLOAD\_DEFINE.
            - **...** – other parameters as expected by NET\_DEVICE\_DT\_OFFLOAD\_DEFINE.

    NET\_IFACE\_COUNT(\_dst)
    :   Count the number of network interfaces.

        Parameters:
        :   - **\_dst** – **[out]** Pointer to location where result is written.

    Typedefs

    typedef int (\*net\_socket\_create\_t)(int, int, int)
    :   A function prototype to create an offloaded socket.

        The prototype is compatible with [socket()](sockets.md#group__bsd__sockets_1ga00c0ed5f8528aac995d803af4b827a9c) function.

    typedef void (\*net\_if\_ip\_addr\_cb\_t)(struct [net\_if](#c.net_if) \*iface, struct [net\_if\_addr](#c.net_if_addr) \*addr, void \*user\_data)
    :   Callback used while iterating over network interface IP addresses.

        Param iface:
        :   Pointer to the network interface the address belongs to

        Param addr:
        :   Pointer to current IP address

        Param user\_data:
        :   A valid pointer to user data or NULL

    typedef void (\*net\_if\_mcast\_callback\_t)(struct [net\_if](#c.net_if) \*iface, const struct net\_addr \*addr, bool is\_joined)
    :   Define a callback that is called whenever a IPv6 or IPv4 multicast address group is joined or left.

        Param iface:
        :   A pointer to a struct [net\_if](#structnet__if) to which the multicast address is attached.

        Param addr:
        :   IP multicast address.

        Param is\_joined:
        :   True if the multicast group is joined, false if group is left.

    typedef void (\*net\_if\_link\_callback\_t)(struct [net\_if](#c.net_if) \*iface, struct [net\_linkaddr](net_linkaddr.md#c.net_linkaddr "net_linkaddr") \*dst, int status)
    :   Define callback that is called after a network packet has been sent.

        Param iface:
        :   A pointer to a struct [net\_if](#structnet__if) to which the the [net\_pkt](net_pkt.md#structnet__pkt) was sent to.

        Param dst:
        :   Link layer address of the destination where the network packet was sent.

        Param status:
        :   Send status, 0 is ok, < 0 error.

    typedef void (\*net\_if\_cb\_t)(struct [net\_if](#c.net_if) \*iface, void \*user\_data)
    :   Callback used while iterating over network interfaces.

        Param iface:
        :   Pointer to current network interface

        Param user\_data:
        :   A valid pointer to user data or NULL

    Enums

    enum net\_if\_flag
    :   Network interface flags.

        *Values:*

        enumerator NET\_IF\_UP
        :   Interface is admin up.

        enumerator NET\_IF\_POINTOPOINT
        :   Interface is pointopoint.

        enumerator NET\_IF\_PROMISC
        :   Interface is in promiscuous mode.

        enumerator NET\_IF\_NO\_AUTO\_START
        :   Do not start the interface immediately after initialization.

            This requires that either the device driver or some other entity will need to manually take the interface up when needed. For example for Ethernet this will happen when the driver calls the [net\_eth\_carrier\_on()](ethernet.md#group__ethernet_1gabeb21cb06b18674b73fbd0f42ee726f0) function.

        enumerator NET\_IF\_SUSPENDED
        :   Power management specific: interface is being suspended.

        enumerator NET\_IF\_FORWARD\_MULTICASTS
        :   Flag defines if received multicasts of other interface are forwarded on this interface.

            This activates multicast routing / forwarding for this interface.

        enumerator NET\_IF\_IPV4
        :   Interface supports IPv4.

        enumerator NET\_IF\_IPV6
        :   Interface supports IPv6.

        enumerator NET\_IF\_RUNNING
        :   Interface up and running (ready to receive and transmit).

        enumerator NET\_IF\_LOWER\_UP
        :   Driver signals L1 is up.

        enumerator NET\_IF\_DORMANT
        :   Driver signals dormant.

        enumerator NET\_IF\_IPV6\_NO\_ND
        :   IPv6 Neighbor Discovery disabled.

        enumerator NET\_IF\_IPV6\_NO\_MLD
        :   IPv6 Multicast Listener Discovery disabled.

        enumerator NET\_IF\_NO\_TX\_LOCK
        :   Mutex locking on TX data path disabled on the interface.

    enum net\_if\_oper\_state
    :   Network interface operational status (RFC 2863).

        *Values:*

        enumerator NET\_IF\_OPER\_UNKNOWN

        enumerator NET\_IF\_OPER\_NOTPRESENT

        enumerator NET\_IF\_OPER\_DOWN

        enumerator NET\_IF\_OPER\_LOWERLAYERDOWN

        enumerator NET\_IF\_OPER\_TESTING

        enumerator NET\_IF\_OPER\_DORMANT

        enumerator NET\_IF\_OPER\_UP

    Functions

    static inline void net\_if\_lock(struct [net\_if](#c.net_if) \*iface)

    static inline void net\_if\_unlock(struct [net\_if](#c.net_if) \*iface)

    static inline bool net\_if\_flag\_is\_set(struct [net\_if](#c.net_if) \*iface, enum [net\_if\_flag](#c.net_if_flag) value)
    :   Check if a value in network interface flags is set.

        Parameters:
        :   - **iface** – Pointer to network interface
            - **value** – Flag value

        Returns:
        :   True if the value is set, false otherwise

    static inline void net\_if\_tx\_lock(struct [net\_if](#c.net_if) \*iface)

    static inline void net\_if\_tx\_unlock(struct [net\_if](#c.net_if) \*iface)

    static inline void net\_if\_flag\_set(struct [net\_if](#c.net_if) \*iface, enum [net\_if\_flag](#c.net_if_flag) value)
    :   Set a value in network interface flags.

        Parameters:
        :   - **iface** – Pointer to network interface
            - **value** – Flag value

    static inline bool net\_if\_flag\_test\_and\_set(struct [net\_if](#c.net_if) \*iface, enum [net\_if\_flag](#c.net_if_flag) value)
    :   Test and set a value in network interface flags.

        Parameters:
        :   - **iface** – Pointer to network interface
            - **value** – Flag value

        Returns:
        :   true if the bit was set, false if it wasn’t.

    static inline void net\_if\_flag\_clear(struct [net\_if](#c.net_if) \*iface, enum [net\_if\_flag](#c.net_if_flag) value)
    :   Clear a value in network interface flags.

        Parameters:
        :   - **iface** – Pointer to network interface
            - **value** – Flag value

    static inline bool net\_if\_flag\_test\_and\_clear(struct [net\_if](#c.net_if) \*iface, enum [net\_if\_flag](#c.net_if_flag) value)
    :   Test and clear a value in network interface flags.

        Parameters:
        :   - **iface** – Pointer to network interface
            - **value** – Flag value

        Returns:
        :   true if the bit was set, false if it wasn’t.

    static inline enum [net\_if\_oper\_state](#c.net_if_oper_state) net\_if\_oper\_state\_set(struct [net\_if](#c.net_if) \*iface, enum [net\_if\_oper\_state](#c.net_if_oper_state) oper\_state)
    :   Set an operational state on an interface.

        Parameters:
        :   - **iface** – Pointer to network interface
            - **oper\_state** – Operational state to set

        Returns:
        :   The new operational state of an interface

    static inline enum [net\_if\_oper\_state](#c.net_if_oper_state) net\_if\_oper\_state(struct [net\_if](#c.net_if) \*iface)
    :   Get an operational state of an interface.

        Parameters:
        :   - **iface** – Pointer to network interface

        Returns:
        :   Operational state of an interface

    enum [net\_verdict](net_core.md#c.net_verdict "net_verdict") net\_if\_send\_data(struct [net\_if](#c.net_if) \*iface, struct [net\_pkt](net_pkt.md#c.net_pkt "net_pkt") \*pkt)
    :   Send a packet through a net iface.

        return verdict about the packet

        Parameters:
        :   - **iface** – Pointer to a network interface structure
            - **pkt** – Pointer to a net packet to send

    static inline const struct [net\_l2](net_l2.md#c.net_l2 "net_l2") \*net\_if\_l2(struct [net\_if](#c.net_if) \*iface)
    :   Get a pointer to the interface L2.

        Parameters:
        :   - **iface** – a valid pointer to a network interface structure

        Returns:
        :   a pointer to the iface L2

    enum [net\_verdict](net_core.md#c.net_verdict "net_verdict") net\_if\_recv\_data(struct [net\_if](#c.net_if) \*iface, struct [net\_pkt](net_pkt.md#c.net_pkt "net_pkt") \*pkt)
    :   Input a packet through a net iface.

        Parameters:
        :   - **iface** – Pointer to a network interface structure
            - **pkt** – Pointer to a net packet to input

        Returns:
        :   verdict about the packet

    static inline void \*net\_if\_l2\_data(struct [net\_if](#c.net_if) \*iface)
    :   Get a pointer to the interface L2 private data.

        Parameters:
        :   - **iface** – a valid pointer to a network interface structure

        Returns:
        :   a pointer to the iface L2 data

    static inline const struct [device](../../../kernel/drivers/index.md#c.device "device") \*net\_if\_get\_device(struct [net\_if](#c.net_if) \*iface)
    :   Get an network interface’s device.

        Parameters:
        :   - **iface** – Pointer to a network interface structure

        Returns:
        :   a pointer to the device driver instance

    void net\_if\_queue\_tx(struct [net\_if](#c.net_if) \*iface, struct [net\_pkt](net_pkt.md#c.net_pkt "net_pkt") \*pkt)
    :   Queue a packet to the net interface TX queue.

        Parameters:
        :   - **iface** – Pointer to a network interface structure
            - **pkt** – Pointer to a net packet to queue

    static inline bool net\_if\_is\_ip\_offloaded(struct [net\_if](#c.net_if) \*iface)
    :   Return the IP offload status.

        Parameters:
        :   - **iface** – Network interface

        Returns:
        :   True if IP offloading is active, false otherwise.

    bool net\_if\_is\_offloaded(struct [net\_if](#c.net_if) \*iface)
    :   Return offload status of a given network interface.

        Parameters:
        :   - **iface** – Network interface

        Returns:
        :   True if IP or socket offloading is active, false otherwise.

    static inline struct net\_offload \*net\_if\_offload(struct [net\_if](#c.net_if) \*iface)
    :   Return the IP offload plugin.

        Parameters:
        :   - **iface** – Network interface

        Returns:
        :   NULL if there is no offload plugin defined, valid pointer otherwise

    static inline bool net\_if\_is\_socket\_offloaded(struct [net\_if](#c.net_if) \*iface)
    :   Return the socket offload status.

        Parameters:
        :   - **iface** – Network interface

        Returns:
        :   True if socket offloading is active, false otherwise.

    static inline void net\_if\_socket\_offload\_set(struct [net\_if](#c.net_if) \*iface, [net\_socket\_create\_t](#c.net_socket_create_t) socket\_offload)
    :   Set the function to create an offloaded socket.

        Parameters:
        :   - **iface** – Network interface
            - **socket\_offload** – A function to create an offloaded socket

    static inline [net\_socket\_create\_t](#c.net_socket_create_t) net\_if\_socket\_offload(struct [net\_if](#c.net_if) \*iface)
    :   Return the function to create an offloaded socket.

        Parameters:
        :   - **iface** – Network interface

        Returns:
        :   NULL if the interface is not socket offloaded, valid pointer otherwise

    static inline struct [net\_linkaddr](net_linkaddr.md#c.net_linkaddr "net_linkaddr") \*net\_if\_get\_link\_addr(struct [net\_if](#c.net_if) \*iface)
    :   Get an network interface’s link address.

        Parameters:
        :   - **iface** – Pointer to a network interface structure

        Returns:
        :   a pointer to the network link address

    static inline struct [net\_if\_config](#c.net_if_config) \*net\_if\_get\_config(struct [net\_if](#c.net_if) \*iface)
    :   Return network configuration for this network interface.

        Parameters:
        :   - **iface** – Pointer to a network interface structure

        Returns:
        :   Pointer to configuration

    static inline void net\_if\_start\_dad(struct [net\_if](#c.net_if) \*iface)
    :   Start duplicate address detection procedure.

        Parameters:
        :   - **iface** – Pointer to a network interface structure

    void net\_if\_start\_rs(struct [net\_if](#c.net_if) \*iface)
    :   Start neighbor discovery and send router solicitation message.

        Parameters:
        :   - **iface** – Pointer to a network interface structure

    static inline void net\_if\_stop\_rs(struct [net\_if](#c.net_if) \*iface)
    :   Stop neighbor discovery.

        Parameters:
        :   - **iface** – Pointer to a network interface structure

    static inline int net\_if\_set\_link\_addr(struct [net\_if](#c.net_if) \*iface, uint8\_t \*addr, uint8\_t len, enum [net\_link\_type](net_linkaddr.md#c.net_link_type "net_link_type") type)
    :   Set a network interface’s link address.

        Parameters:
        :   - **iface** – Pointer to a network interface structure
            - **addr** – A pointer to a uint8\_t buffer representing the address. The buffer must remain valid throughout interface lifetime.
            - **len** – length of the address buffer
            - **type** – network bearer type of this link address

        Returns:
        :   0 on success

    static inline uint16\_t net\_if\_get\_mtu(struct [net\_if](#c.net_if) \*iface)
    :   Get an network interface’s MTU.

        Parameters:
        :   - **iface** – Pointer to a network interface structure

        Returns:
        :   the MTU

    static inline void net\_if\_set\_mtu(struct [net\_if](#c.net_if) \*iface, uint16\_t mtu)
    :   Set an network interface’s MTU.

        Parameters:
        :   - **iface** – Pointer to a network interface structure
            - **mtu** – New MTU, note that we store only 16 bit mtu value.

    static inline void net\_if\_addr\_set\_lf(struct [net\_if\_addr](#c.net_if_addr) \*ifaddr, bool is\_infinite)
    :   Set the infinite status of the network interface address.

        Parameters:
        :   - **ifaddr** – IP address for network interface
            - **is\_infinite** – Infinite status

    struct [net\_if](#c.net_if) \*net\_if\_get\_by\_link\_addr(struct [net\_linkaddr](net_linkaddr.md#c.net_linkaddr "net_linkaddr") \*ll\_addr)
    :   Get an interface according to link layer address.

        Parameters:
        :   - **ll\_addr** – Link layer address.

        Returns:
        :   Network interface or NULL if not found.

    struct [net\_if](#c.net_if) \*net\_if\_lookup\_by\_dev(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Find an interface from it’s related device.

        Parameters:
        :   - **dev** – A valid struct device pointer to relate with an interface

        Returns:
        :   a valid struct [net\_if](#structnet__if) pointer on success, NULL otherwise

    static inline struct [net\_if\_config](#c.net_if_config) \*net\_if\_config\_get(struct [net\_if](#c.net_if) \*iface)
    :   Get network interface IP config.

        Parameters:
        :   - **iface** – Interface to use.

        Returns:
        :   NULL if not found or pointer to correct config settings.

    void net\_if\_router\_rm(struct [net\_if\_router](#c.net_if_router) \*router)
    :   Remove a router from the system.

        Parameters:
        :   - **router** – Pointer to existing router

    void net\_if\_set\_default(struct [net\_if](#c.net_if) \*iface)
    :   Set the default network interface.

        Parameters:
        :   - **iface** – New default interface, or NULL to revert to the one set by Kconfig.

    struct [net\_if](#c.net_if) \*net\_if\_get\_default(void)
    :   Get the default network interface.

        Returns:
        :   Default interface or NULL if no interfaces are configured.

    struct [net\_if](#c.net_if) \*net\_if\_get\_first\_by\_type(const struct [net\_l2](net_l2.md#c.net_l2 "net_l2") \*l2)
    :   Get the first network interface according to its type.

        Parameters:
        :   - **l2** – Layer 2 type of the network interface.

        Returns:
        :   First network interface of a given type or NULL if no such interfaces was found.

    struct [net\_if](#c.net_if) \*net\_if\_get\_first\_up(void)
    :   Get the first network interface which is up.

        Returns:
        :   First network interface which is up or NULL if all interfaces are down.

    int net\_if\_config\_ipv6\_get(struct [net\_if](#c.net_if) \*iface, struct [net\_if\_ipv6](#c.net_if_ipv6) \*\*ipv6)
    :   Allocate network interface IPv6 config.

        This function will allocate new IPv6 config.

        Parameters:
        :   - **iface** – Interface to use.
            - **ipv6** – Pointer to allocated IPv6 struct is returned to caller.

        Returns:
        :   0 if ok, <0 if error

    int net\_if\_config\_ipv6\_put(struct [net\_if](#c.net_if) \*iface)
    :   Release network interface IPv6 config.

        Parameters:
        :   - **iface** – Interface to use.

        Returns:
        :   0 if ok, <0 if error

    struct [net\_if\_addr](#c.net_if_addr) \*net\_if\_ipv6\_addr\_lookup(const struct [in6\_addr](ip_4_6.md#c.in6_addr "in6_addr") \*addr, struct [net\_if](#c.net_if) \*\*iface)
    :   Check if this IPv6 address belongs to one of the interfaces.

        Parameters:
        :   - **addr** – IPv6 address
            - **iface** – Pointer to interface is returned

        Returns:
        :   Pointer to interface address, NULL if not found.

    struct [net\_if\_addr](#c.net_if_addr) \*net\_if\_ipv6\_addr\_lookup\_by\_iface(struct [net\_if](#c.net_if) \*iface, struct [in6\_addr](ip_4_6.md#c.in6_addr "in6_addr") \*addr)
    :   Check if this IPv6 address belongs to this specific interfaces.

        Parameters:
        :   - **iface** – Network interface
            - **addr** – IPv6 address

        Returns:
        :   Pointer to interface address, NULL if not found.

    int net\_if\_ipv6\_addr\_lookup\_by\_index(const struct [in6\_addr](ip_4_6.md#c.in6_addr "in6_addr") \*addr)
    :   Check if this IPv6 address belongs to one of the interface indices.

        Parameters:
        :   - **addr** – IPv6 address

        Returns:
        :   >0 if address was found in given network interface index, all other values mean address was not found

    struct [net\_if\_addr](#c.net_if_addr) \*net\_if\_ipv6\_addr\_add(struct [net\_if](#c.net_if) \*iface, struct [in6\_addr](ip_4_6.md#c.in6_addr "in6_addr") \*addr, enum [net\_addr\_type](ip_4_6.md#c.net_addr_type "net_addr_type") addr\_type, uint32\_t vlifetime)
    :   Add a IPv6 address to an interface.

        Parameters:
        :   - **iface** – Network interface
            - **addr** – IPv6 address
            - **addr\_type** – IPv6 address type
            - **vlifetime** – Validity time for this address

        Returns:
        :   Pointer to interface address, NULL if cannot be added

    bool net\_if\_ipv6\_addr\_add\_by\_index(int index, struct [in6\_addr](ip_4_6.md#c.in6_addr "in6_addr") \*addr, enum [net\_addr\_type](ip_4_6.md#c.net_addr_type "net_addr_type") addr\_type, uint32\_t vlifetime)
    :   Add a IPv6 address to an interface by index.

        Parameters:
        :   - **index** – Network interface index
            - **addr** – IPv6 address
            - **addr\_type** – IPv6 address type
            - **vlifetime** – Validity time for this address

        Returns:
        :   True if ok, false if address could not be added

    void net\_if\_ipv6\_addr\_update\_lifetime(struct [net\_if\_addr](#c.net_if_addr) \*ifaddr, uint32\_t vlifetime)
    :   Update validity lifetime time of an IPv6 address.

        Parameters:
        :   - **ifaddr** – Network IPv6 address
            - **vlifetime** – Validity time for this address

    bool net\_if\_ipv6\_addr\_rm(struct [net\_if](#c.net_if) \*iface, const struct [in6\_addr](ip_4_6.md#c.in6_addr "in6_addr") \*addr)
    :   Remove an IPv6 address from an interface.

        Parameters:
        :   - **iface** – Network interface
            - **addr** – IPv6 address

        Returns:
        :   True if successfully removed, false otherwise

    bool net\_if\_ipv6\_addr\_rm\_by\_index(int index, const struct [in6\_addr](ip_4_6.md#c.in6_addr "in6_addr") \*addr)
    :   Remove an IPv6 address from an interface by index.

        Parameters:
        :   - **index** – Network interface index
            - **addr** – IPv6 address

        Returns:
        :   True if successfully removed, false otherwise

    void net\_if\_ipv6\_addr\_foreach(struct [net\_if](#c.net_if) \*iface, [net\_if\_ip\_addr\_cb\_t](#c.net_if_ip_addr_cb_t) cb, void \*user\_data)
    :   Go through all IPv6 addresses on a network interface and call callback for each used address.

        Parameters:
        :   - **iface** – Pointer to the network interface
            - **cb** – User-supplied callback function to call
            - **user\_data** – User specified data

    struct [net\_if\_mcast\_addr](#c.net_if_mcast_addr) \*net\_if\_ipv6\_maddr\_add(struct [net\_if](#c.net_if) \*iface, const struct [in6\_addr](ip_4_6.md#c.in6_addr "in6_addr") \*addr)
    :   Add a IPv6 multicast address to an interface.

        Parameters:
        :   - **iface** – Network interface
            - **addr** – IPv6 multicast address

        Returns:
        :   Pointer to interface multicast address, NULL if cannot be added

    bool net\_if\_ipv6\_maddr\_rm(struct [net\_if](#c.net_if) \*iface, const struct [in6\_addr](ip_4_6.md#c.in6_addr "in6_addr") \*addr)
    :   Remove an IPv6 multicast address from an interface.

        Parameters:
        :   - **iface** – Network interface
            - **addr** – IPv6 multicast address

        Returns:
        :   True if successfully removed, false otherwise

    struct [net\_if\_mcast\_addr](#c.net_if_mcast_addr) \*net\_if\_ipv6\_maddr\_lookup(const struct [in6\_addr](ip_4_6.md#c.in6_addr "in6_addr") \*addr, struct [net\_if](#c.net_if) \*\*iface)
    :   Check if this IPv6 multicast address belongs to a specific interface or one of the interfaces.

        Parameters:
        :   - **addr** – IPv6 address
            - **iface** – If \*iface is null, then pointer to interface is returned, otherwise the \*iface value needs to be matched.

        Returns:
        :   Pointer to interface multicast address, NULL if not found.

    void net\_if\_mcast\_mon\_register(struct [net\_if\_mcast\_monitor](#c.net_if_mcast_monitor) \*mon, struct [net\_if](#c.net_if) \*iface, [net\_if\_mcast\_callback\_t](#c.net_if_mcast_callback_t) cb)
    :   Register a multicast monitor.

        Parameters:
        :   - **mon** – Monitor handle. This is a pointer to a monitor storage structure which should be allocated by caller, but does not need to be initialized.
            - **iface** – Network interface
            - **cb** – Monitor callback

    void net\_if\_mcast\_mon\_unregister(struct [net\_if\_mcast\_monitor](#c.net_if_mcast_monitor) \*mon)
    :   Unregister a multicast monitor.

        Parameters:
        :   - **mon** – Monitor handle

    void net\_if\_mcast\_monitor(struct [net\_if](#c.net_if) \*iface, const struct net\_addr \*addr, bool is\_joined)
    :   Call registered multicast monitors.

        Parameters:
        :   - **iface** – Network interface
            - **addr** – Multicast address
            - **is\_joined** – Is this multicast address group joined (true) or not (false)

    void net\_if\_ipv6\_maddr\_join(struct [net\_if](#c.net_if) \*iface, struct [net\_if\_mcast\_addr](#c.net_if_mcast_addr) \*addr)
    :   Mark a given multicast address to be joined.

        Parameters:
        :   - **iface** – Network interface the address belongs to
            - **addr** – IPv6 multicast address

    static inline bool net\_if\_ipv6\_maddr\_is\_joined(struct [net\_if\_mcast\_addr](#c.net_if_mcast_addr) \*addr)
    :   Check if given multicast address is joined or not.

        Parameters:
        :   - **addr** – IPv6 multicast address

        Returns:
        :   True if address is joined, False otherwise.

    void net\_if\_ipv6\_maddr\_leave(struct [net\_if](#c.net_if) \*iface, struct [net\_if\_mcast\_addr](#c.net_if_mcast_addr) \*addr)
    :   Mark a given multicast address to be left.

        Parameters:
        :   - **iface** – Network interface the address belongs to
            - **addr** – IPv6 multicast address

    struct [net\_if\_ipv6\_prefix](#c.net_if_ipv6_prefix) \*net\_if\_ipv6\_prefix\_get(struct [net\_if](#c.net_if) \*iface, struct [in6\_addr](ip_4_6.md#c.in6_addr "in6_addr") \*addr)
    :   Return prefix that corresponds to this IPv6 address.

        Parameters:
        :   - **iface** – Network interface
            - **addr** – IPv6 address

        Returns:
        :   Pointer to prefix, NULL if not found.

    struct [net\_if\_ipv6\_prefix](#c.net_if_ipv6_prefix) \*net\_if\_ipv6\_prefix\_lookup(struct [net\_if](#c.net_if) \*iface, struct [in6\_addr](ip_4_6.md#c.in6_addr "in6_addr") \*addr, uint8\_t len)
    :   Check if this IPv6 prefix belongs to this interface.

        Parameters:
        :   - **iface** – Network interface
            - **addr** – IPv6 address
            - **len** – Prefix length

        Returns:
        :   Pointer to prefix, NULL if not found.

    struct [net\_if\_ipv6\_prefix](#c.net_if_ipv6_prefix) \*net\_if\_ipv6\_prefix\_add(struct [net\_if](#c.net_if) \*iface, struct [in6\_addr](ip_4_6.md#c.in6_addr "in6_addr") \*prefix, uint8\_t len, uint32\_t lifetime)
    :   Add a IPv6 prefix to an network interface.

        Parameters:
        :   - **iface** – Network interface
            - **prefix** – IPv6 address
            - **len** – Prefix length
            - **lifetime** – Prefix lifetime in seconds

        Returns:
        :   Pointer to prefix, NULL if the prefix was not added.

    bool net\_if\_ipv6\_prefix\_rm(struct [net\_if](#c.net_if) \*iface, struct [in6\_addr](ip_4_6.md#c.in6_addr "in6_addr") \*addr, uint8\_t len)
    :   Remove an IPv6 prefix from an interface.

        Parameters:
        :   - **iface** – Network interface
            - **addr** – IPv6 prefix address
            - **len** – Prefix length

        Returns:
        :   True if successfully removed, false otherwise

    static inline void net\_if\_ipv6\_prefix\_set\_lf(struct [net\_if\_ipv6\_prefix](#c.net_if_ipv6_prefix) \*prefix, bool is\_infinite)
    :   Set the infinite status of the prefix.

        Parameters:
        :   - **prefix** – IPv6 address
            - **is\_infinite** – Infinite status

    void net\_if\_ipv6\_prefix\_set\_timer(struct [net\_if\_ipv6\_prefix](#c.net_if_ipv6_prefix) \*prefix, uint32\_t lifetime)
    :   Set the prefix lifetime timer.

        Parameters:
        :   - **prefix** – IPv6 address
            - **lifetime** – Prefix lifetime in seconds

    void net\_if\_ipv6\_prefix\_unset\_timer(struct [net\_if\_ipv6\_prefix](#c.net_if_ipv6_prefix) \*prefix)
    :   Unset the prefix lifetime timer.

        Parameters:
        :   - **prefix** – IPv6 address

    bool net\_if\_ipv6\_addr\_onlink(struct [net\_if](#c.net_if) \*\*iface, struct [in6\_addr](ip_4_6.md#c.in6_addr "in6_addr") \*addr)
    :   Check if this IPv6 address is part of the subnet of our network interface.

        Parameters:
        :   - **iface** – Network interface. This is returned to the caller. The iface can be NULL in which case we check all the interfaces.
            - **addr** – IPv6 address

        Returns:
        :   True if address is part of our subnet, false otherwise

    static inline struct [in6\_addr](ip_4_6.md#c.in6_addr "in6_addr") \*net\_if\_router\_ipv6(struct [net\_if\_router](#c.net_if_router) \*router)
    :   Get the IPv6 address of the given router.

        Parameters:
        :   - **router** – a network router

        Returns:
        :   pointer to the IPv6 address, or NULL if none

    struct [net\_if\_router](#c.net_if_router) \*net\_if\_ipv6\_router\_lookup(struct [net\_if](#c.net_if) \*iface, struct [in6\_addr](ip_4_6.md#c.in6_addr "in6_addr") \*addr)
    :   Check if IPv6 address is one of the routers configured in the system.

        Parameters:
        :   - **iface** – Network interface
            - **addr** – IPv6 address

        Returns:
        :   Pointer to router information, NULL if cannot be found

    struct [net\_if\_router](#c.net_if_router) \*net\_if\_ipv6\_router\_find\_default(struct [net\_if](#c.net_if) \*iface, struct [in6\_addr](ip_4_6.md#c.in6_addr "in6_addr") \*addr)
    :   Find default router for this IPv6 address.

        Parameters:
        :   - **iface** – Network interface. This can be NULL in which case we go through all the network interfaces to find a suitable router.
            - **addr** – IPv6 address

        Returns:
        :   Pointer to router information, NULL if cannot be found

    void net\_if\_ipv6\_router\_update\_lifetime(struct [net\_if\_router](#c.net_if_router) \*router, uint16\_t lifetime)
    :   Update validity lifetime time of a router.

        Parameters:
        :   - **router** – Network IPv6 address
            - **lifetime** – Lifetime of this router.

    struct [net\_if\_router](#c.net_if_router) \*net\_if\_ipv6\_router\_add(struct [net\_if](#c.net_if) \*iface, struct [in6\_addr](ip_4_6.md#c.in6_addr "in6_addr") \*addr, uint16\_t router\_lifetime)
    :   Add IPv6 router to the system.

        Parameters:
        :   - **iface** – Network interface
            - **addr** – IPv6 address
            - **router\_lifetime** – Lifetime of the router

        Returns:
        :   Pointer to router information, NULL if could not be added

    bool net\_if\_ipv6\_router\_rm(struct [net\_if\_router](#c.net_if_router) \*router)
    :   Remove IPv6 router from the system.

        Parameters:
        :   - **router** – Router information.

        Returns:
        :   True if successfully removed, false otherwise

    uint8\_t net\_if\_ipv6\_get\_hop\_limit(struct [net\_if](#c.net_if) \*iface)
    :   Get IPv6 hop limit specified for a given interface.

        This is the default value but can be overridden by the user.

        Parameters:
        :   - **iface** – Network interface

        Returns:
        :   Hop limit

    void net\_if\_ipv6\_set\_hop\_limit(struct [net\_if](#c.net_if) \*iface, uint8\_t hop\_limit)
    :   Set the default IPv6 hop limit of a given interface.

        Parameters:
        :   - **iface** – Network interface
            - **hop\_limit** – New hop limit

    static inline void net\_ipv6\_set\_hop\_limit(struct [net\_if](#c.net_if) \*iface, uint8\_t hop\_limit)

    uint8\_t net\_if\_ipv6\_get\_mcast\_hop\_limit(struct [net\_if](#c.net_if) \*iface)
    :   Get IPv6 multicast hop limit specified for a given interface.

        This is the default value but can be overridden by the user.

        Parameters:
        :   - **iface** – Network interface

        Returns:
        :   Hop limit

    void net\_if\_ipv6\_set\_mcast\_hop\_limit(struct [net\_if](#c.net_if) \*iface, uint8\_t hop\_limit)
    :   Set the default IPv6 multicast hop limit of a given interface.

        Parameters:
        :   - **iface** – Network interface
            - **hop\_limit** – New hop limit

    static inline void net\_if\_ipv6\_set\_base\_reachable\_time(struct [net\_if](#c.net_if) \*iface, uint32\_t reachable\_time)
    :   Set IPv6 reachable time for a given interface.

        Parameters:
        :   - **iface** – Network interface
            - **reachable\_time** – New reachable time

    static inline uint32\_t net\_if\_ipv6\_get\_reachable\_time(struct [net\_if](#c.net_if) \*iface)
    :   Get IPv6 reachable timeout specified for a given interface.

        Parameters:
        :   - **iface** – Network interface

        Returns:
        :   Reachable timeout

    uint32\_t net\_if\_ipv6\_calc\_reachable\_time(struct [net\_if\_ipv6](#c.net_if_ipv6) \*ipv6)
    :   Calculate next reachable time value for IPv6 reachable time.

        Parameters:
        :   - **ipv6** – IPv6 address configuration

        Returns:
        :   Reachable time

    static inline void net\_if\_ipv6\_set\_reachable\_time(struct [net\_if\_ipv6](#c.net_if_ipv6) \*ipv6)
    :   Set IPv6 reachable time for a given interface.

        This requires that base reachable time is set for the interface.

        Parameters:
        :   - **ipv6** – IPv6 address configuration

    static inline void net\_if\_ipv6\_set\_retrans\_timer(struct [net\_if](#c.net_if) \*iface, uint32\_t retrans\_timer)
    :   Set IPv6 retransmit timer for a given interface.

        Parameters:
        :   - **iface** – Network interface
            - **retrans\_timer** – New retransmit timer

    static inline uint32\_t net\_if\_ipv6\_get\_retrans\_timer(struct [net\_if](#c.net_if) \*iface)
    :   Get IPv6 retransmit timer specified for a given interface.

        Parameters:
        :   - **iface** – Network interface

        Returns:
        :   Retransmit timer

    static inline const struct [in6\_addr](ip_4_6.md#c.in6_addr "in6_addr") \*net\_if\_ipv6\_select\_src\_addr(struct [net\_if](#c.net_if) \*iface, const struct [in6\_addr](ip_4_6.md#c.in6_addr "in6_addr") \*dst)
    :   Get a IPv6 source address that should be used when sending network data to destination.

        Parameters:
        :   - **iface** – Interface that was used when packet was received. If the interface is not known, then NULL can be given.
            - **dst** – IPv6 destination address

        Returns:
        :   Pointer to IPv6 address to use, NULL if no IPv6 address could be found.

    static inline struct [net\_if](#c.net_if) \*net\_if\_ipv6\_select\_src\_iface(const struct [in6\_addr](ip_4_6.md#c.in6_addr "in6_addr") \*dst)
    :   Get a network interface that should be used when sending IPv6 network data to destination.

        Parameters:
        :   - **dst** – IPv6 destination address

        Returns:
        :   Pointer to network interface to use, NULL if no suitable interface could be found.

    struct [in6\_addr](ip_4_6.md#c.in6_addr "in6_addr") \*net\_if\_ipv6\_get\_ll(struct [net\_if](#c.net_if) \*iface, enum [net\_addr\_state](ip_4_6.md#c.net_addr_state "net_addr_state") addr\_state)
    :   Get a IPv6 link local address in a given state.

        Parameters:
        :   - **iface** – Interface to use. Must be a valid pointer to an interface.
            - **addr\_state** – IPv6 address state (preferred, tentative, deprecated)

        Returns:
        :   Pointer to link local IPv6 address, NULL if no proper IPv6 address could be found.

    struct [in6\_addr](ip_4_6.md#c.in6_addr "in6_addr") \*net\_if\_ipv6\_get\_ll\_addr(enum [net\_addr\_state](ip_4_6.md#c.net_addr_state "net_addr_state") state, struct [net\_if](#c.net_if) \*\*iface)
    :   Return link local IPv6 address from the first interface that has a link local address matching give state.

        Parameters:
        :   - **state** – IPv6 address state (ANY, TENTATIVE, PREFERRED, DEPRECATED)
            - **iface** – Pointer to interface is returned

        Returns:
        :   Pointer to IPv6 address, NULL if not found.

    void net\_if\_ipv6\_dad\_failed(struct [net\_if](#c.net_if) \*iface, const struct [in6\_addr](ip_4_6.md#c.in6_addr "in6_addr") \*addr)
    :   Stop IPv6 Duplicate Address Detection (DAD) procedure if we find out that our IPv6 address is already in use.

        Parameters:
        :   - **iface** – Interface where the DAD was running.
            - **addr** – IPv6 address that failed DAD

    struct [in6\_addr](ip_4_6.md#c.in6_addr "in6_addr") \*net\_if\_ipv6\_get\_global\_addr(enum [net\_addr\_state](ip_4_6.md#c.net_addr_state "net_addr_state") state, struct [net\_if](#c.net_if) \*\*iface)
    :   Return global IPv6 address from the first interface that has a global IPv6 address matching the given state.

        Parameters:
        :   - **state** – IPv6 address state (ANY, TENTATIVE, PREFERRED, DEPRECATED)
            - **iface** – Caller can give an interface to check. If iface is set to NULL, then all the interfaces are checked. Pointer to interface where the IPv6 address is defined is returned to the caller.

        Returns:
        :   Pointer to IPv6 address, NULL if not found.

    int net\_if\_config\_ipv4\_get(struct [net\_if](#c.net_if) \*iface, struct [net\_if\_ipv4](#c.net_if_ipv4) \*\*ipv4)
    :   Allocate network interface IPv4 config.

        This function will allocate new IPv4 config.

        Parameters:
        :   - **iface** – Interface to use.
            - **ipv4** – Pointer to allocated IPv4 struct is returned to caller.

        Returns:
        :   0 if ok, <0 if error

    int net\_if\_config\_ipv4\_put(struct [net\_if](#c.net_if) \*iface)
    :   Release network interface IPv4 config.

        Parameters:
        :   - **iface** – Interface to use.

        Returns:
        :   0 if ok, <0 if error

    uint8\_t net\_if\_ipv4\_get\_ttl(struct [net\_if](#c.net_if) \*iface)
    :   Get IPv4 time-to-live value specified for a given interface.

        Parameters:
        :   - **iface** – Network interface

        Returns:
        :   Time-to-live

    void net\_if\_ipv4\_set\_ttl(struct [net\_if](#c.net_if) \*iface, uint8\_t ttl)
    :   Set IPv4 time-to-live value specified to a given interface.

        Parameters:
        :   - **iface** – Network interface
            - **ttl** – Time-to-live value

    uint8\_t net\_if\_ipv4\_get\_mcast\_ttl(struct [net\_if](#c.net_if) \*iface)
    :   Get IPv4 multicast time-to-live value specified for a given interface.

        Parameters:
        :   - **iface** – Network interface

        Returns:
        :   Time-to-live

    void net\_if\_ipv4\_set\_mcast\_ttl(struct [net\_if](#c.net_if) \*iface, uint8\_t ttl)
    :   Set IPv4 multicast time-to-live value specified to a given interface.

        Parameters:
        :   - **iface** – Network interface
            - **ttl** – Time-to-live value

    struct [net\_if\_addr](#c.net_if_addr) \*net\_if\_ipv4\_addr\_lookup(const struct [in\_addr](ip_4_6.md#c.in_addr "in_addr") \*addr, struct [net\_if](#c.net_if) \*\*iface)
    :   Check if this IPv4 address belongs to one of the interfaces.

        Parameters:
        :   - **addr** – IPv4 address
            - **iface** – Interface is returned

        Returns:
        :   Pointer to interface address, NULL if not found.

    struct [net\_if\_addr](#c.net_if_addr) \*net\_if\_ipv4\_addr\_add(struct [net\_if](#c.net_if) \*iface, struct [in\_addr](ip_4_6.md#c.in_addr "in_addr") \*addr, enum [net\_addr\_type](ip_4_6.md#c.net_addr_type "net_addr_type") addr\_type, uint32\_t vlifetime)
    :   Add a IPv4 address to an interface.

        Parameters:
        :   - **iface** – Network interface
            - **addr** – IPv4 address
            - **addr\_type** – IPv4 address type
            - **vlifetime** – Validity time for this address

        Returns:
        :   Pointer to interface address, NULL if cannot be added

    bool net\_if\_ipv4\_addr\_rm(struct [net\_if](#c.net_if) \*iface, const struct [in\_addr](ip_4_6.md#c.in_addr "in_addr") \*addr)
    :   Remove a IPv4 address from an interface.

        Parameters:
        :   - **iface** – Network interface
            - **addr** – IPv4 address

        Returns:
        :   True if successfully removed, false otherwise

    int net\_if\_ipv4\_addr\_lookup\_by\_index(const struct [in\_addr](ip_4_6.md#c.in_addr "in_addr") \*addr)
    :   Check if this IPv4 address belongs to one of the interface indices.

        Parameters:
        :   - **addr** – IPv4 address

        Returns:
        :   >0 if address was found in given network interface index, all other values mean address was not found

    bool net\_if\_ipv4\_addr\_add\_by\_index(int index, struct [in\_addr](ip_4_6.md#c.in_addr "in_addr") \*addr, enum [net\_addr\_type](ip_4_6.md#c.net_addr_type "net_addr_type") addr\_type, uint32\_t vlifetime)
    :   Add a IPv4 address to an interface by network interface index.

        Parameters:
        :   - **index** – Network interface index
            - **addr** – IPv4 address
            - **addr\_type** – IPv4 address type
            - **vlifetime** – Validity time for this address

        Returns:
        :   True if ok, false if the address could not be added

    bool net\_if\_ipv4\_addr\_rm\_by\_index(int index, const struct [in\_addr](ip_4_6.md#c.in_addr "in_addr") \*addr)
    :   Remove a IPv4 address from an interface by interface index.

        Parameters:
        :   - **index** – Network interface index
            - **addr** – IPv4 address

        Returns:
        :   True if successfully removed, false otherwise

    void net\_if\_ipv4\_addr\_foreach(struct [net\_if](#c.net_if) \*iface, [net\_if\_ip\_addr\_cb\_t](#c.net_if_ip_addr_cb_t) cb, void \*user\_data)
    :   Go through all IPv4 addresses on a network interface and call callback for each used address.

        Parameters:
        :   - **iface** – Pointer to the network interface
            - **cb** – User-supplied callback function to call
            - **user\_data** – User specified data

    struct [net\_if\_mcast\_addr](#c.net_if_mcast_addr) \*net\_if\_ipv4\_maddr\_add(struct [net\_if](#c.net_if) \*iface, const struct [in\_addr](ip_4_6.md#c.in_addr "in_addr") \*addr)
    :   Add a IPv4 multicast address to an interface.

        Parameters:
        :   - **iface** – Network interface
            - **addr** – IPv4 multicast address

        Returns:
        :   Pointer to interface multicast address, NULL if cannot be added

    bool net\_if\_ipv4\_maddr\_rm(struct [net\_if](#c.net_if) \*iface, const struct [in\_addr](ip_4_6.md#c.in_addr "in_addr") \*addr)
    :   Remove an IPv4 multicast address from an interface.

        Parameters:
        :   - **iface** – Network interface
            - **addr** – IPv4 multicast address

        Returns:
        :   True if successfully removed, false otherwise

    struct [net\_if\_mcast\_addr](#c.net_if_mcast_addr) \*net\_if\_ipv4\_maddr\_lookup(const struct [in\_addr](ip_4_6.md#c.in_addr "in_addr") \*addr, struct [net\_if](#c.net_if) \*\*iface)
    :   Check if this IPv4 multicast address belongs to a specific interface or one of the interfaces.

        Parameters:
        :   - **addr** – IPv4 address
            - **iface** – If \*iface is null, then pointer to interface is returned, otherwise the \*iface value needs to be matched.

        Returns:
        :   Pointer to interface multicast address, NULL if not found.

    void net\_if\_ipv4\_maddr\_join(struct [net\_if](#c.net_if) \*iface, struct [net\_if\_mcast\_addr](#c.net_if_mcast_addr) \*addr)
    :   Mark a given multicast address to be joined.

        Parameters:
        :   - **iface** – Network interface the address belongs to
            - **addr** – IPv4 multicast address

    static inline bool net\_if\_ipv4\_maddr\_is\_joined(struct [net\_if\_mcast\_addr](#c.net_if_mcast_addr) \*addr)
    :   Check if given multicast address is joined or not.

        Parameters:
        :   - **addr** – IPv4 multicast address

        Returns:
        :   True if address is joined, False otherwise.

    void net\_if\_ipv4\_maddr\_leave(struct [net\_if](#c.net_if) \*iface, struct [net\_if\_mcast\_addr](#c.net_if_mcast_addr) \*addr)
    :   Mark a given multicast address to be left.

        Parameters:
        :   - **iface** – Network interface the address belongs to
            - **addr** – IPv4 multicast address

    static inline struct [in\_addr](ip_4_6.md#c.in_addr "in_addr") \*net\_if\_router\_ipv4(struct [net\_if\_router](#c.net_if_router) \*router)
    :   Get the IPv4 address of the given router.

        Parameters:
        :   - **router** – a network router

        Returns:
        :   pointer to the IPv4 address, or NULL if none

    struct [net\_if\_router](#c.net_if_router) \*net\_if\_ipv4\_router\_lookup(struct [net\_if](#c.net_if) \*iface, struct [in\_addr](ip_4_6.md#c.in_addr "in_addr") \*addr)
    :   Check if IPv4 address is one of the routers configured in the system.

        Parameters:
        :   - **iface** – Network interface
            - **addr** – IPv4 address

        Returns:
        :   Pointer to router information, NULL if cannot be found

    struct [net\_if\_router](#c.net_if_router) \*net\_if\_ipv4\_router\_find\_default(struct [net\_if](#c.net_if) \*iface, struct [in\_addr](ip_4_6.md#c.in_addr "in_addr") \*addr)
    :   Find default router for this IPv4 address.

        Parameters:
        :   - **iface** – Network interface. This can be NULL in which case we go through all the network interfaces to find a suitable router.
            - **addr** – IPv4 address

        Returns:
        :   Pointer to router information, NULL if cannot be found

    struct [net\_if\_router](#c.net_if_router) \*net\_if\_ipv4\_router\_add(struct [net\_if](#c.net_if) \*iface, struct [in\_addr](ip_4_6.md#c.in_addr "in_addr") \*addr, bool is\_default, uint16\_t router\_lifetime)
    :   Add IPv4 router to the system.

        Parameters:
        :   - **iface** – Network interface
            - **addr** – IPv4 address
            - **is\_default** – Is this router the default one
            - **router\_lifetime** – Lifetime of the router

        Returns:
        :   Pointer to router information, NULL if could not be added

    bool net\_if\_ipv4\_router\_rm(struct [net\_if\_router](#c.net_if_router) \*router)
    :   Remove IPv4 router from the system.

        Parameters:
        :   - **router** – Router information.

        Returns:
        :   True if successfully removed, false otherwise

    bool net\_if\_ipv4\_addr\_mask\_cmp(struct [net\_if](#c.net_if) \*iface, const struct [in\_addr](ip_4_6.md#c.in_addr "in_addr") \*addr)
    :   Check if the given IPv4 address belongs to local subnet.

        Parameters:
        :   - **iface** – Interface to use. Must be a valid pointer to an interface.
            - **addr** – IPv4 address

        Returns:
        :   True if address is part of local subnet, false otherwise.

    bool net\_if\_ipv4\_is\_addr\_bcast(struct [net\_if](#c.net_if) \*iface, const struct [in\_addr](ip_4_6.md#c.in_addr "in_addr") \*addr)
    :   Check if the given IPv4 address is a broadcast address.

        Parameters:
        :   - **iface** – Interface to use. Must be a valid pointer to an interface.
            - **addr** – IPv4 address, this should be in network byte order

        Returns:
        :   True if address is a broadcast address, false otherwise.

    static inline struct [net\_if](#c.net_if) \*net\_if\_ipv4\_select\_src\_iface(const struct [in\_addr](ip_4_6.md#c.in_addr "in_addr") \*dst)
    :   Get a network interface that should be used when sending IPv4 network data to destination.

        Parameters:
        :   - **dst** – IPv4 destination address

        Returns:
        :   Pointer to network interface to use, NULL if no suitable interface could be found.

    static inline const struct [in\_addr](ip_4_6.md#c.in_addr "in_addr") \*net\_if\_ipv4\_select\_src\_addr(struct [net\_if](#c.net_if) \*iface, const struct [in\_addr](ip_4_6.md#c.in_addr "in_addr") \*dst)
    :   Get a IPv4 source address that should be used when sending network data to destination.

        Parameters:
        :   - **iface** – Interface to use when sending the packet. If the interface is not known, then NULL can be given.
            - **dst** – IPv4 destination address

        Returns:
        :   Pointer to IPv4 address to use, NULL if no IPv4 address could be found.

    struct [in\_addr](ip_4_6.md#c.in_addr "in_addr") \*net\_if\_ipv4\_get\_ll(struct [net\_if](#c.net_if) \*iface, enum [net\_addr\_state](ip_4_6.md#c.net_addr_state "net_addr_state") addr\_state)
    :   Get a IPv4 link local address in a given state.

        Parameters:
        :   - **iface** – Interface to use. Must be a valid pointer to an interface.
            - **addr\_state** – IPv4 address state (preferred, tentative, deprecated)

        Returns:
        :   Pointer to link local IPv4 address, NULL if no proper IPv4 address could be found.

    struct [in\_addr](ip_4_6.md#c.in_addr "in_addr") \*net\_if\_ipv4\_get\_global\_addr(struct [net\_if](#c.net_if) \*iface, enum [net\_addr\_state](ip_4_6.md#c.net_addr_state "net_addr_state") addr\_state)
    :   Get a IPv4 global address in a given state.

        Parameters:
        :   - **iface** – Interface to use. Must be a valid pointer to an interface.
            - **addr\_state** – IPv4 address state (preferred, tentative, deprecated)

        Returns:
        :   Pointer to link local IPv4 address, NULL if no proper IPv4 address could be found.

    struct [in\_addr](ip_4_6.md#c.in_addr "in_addr") net\_if\_ipv4\_get\_netmask(struct [net\_if](#c.net_if) \*iface)
    :   Get IPv4 netmask of an interface.

        Parameters:
        :   - **iface** – Interface to use.

        Returns:
        :   The netmask set on the interface, unspecified address if not found.

    void net\_if\_ipv4\_set\_netmask(struct [net\_if](#c.net_if) \*iface, const struct [in\_addr](ip_4_6.md#c.in_addr "in_addr") \*netmask)
    :   Set IPv4 netmask for an interface.

        Parameters:
        :   - **iface** – Interface to use.
            - **netmask** – IPv4 netmask

    bool net\_if\_ipv4\_set\_netmask\_by\_index(int index, const struct [in\_addr](ip_4_6.md#c.in_addr "in_addr") \*netmask)
    :   Set IPv4 netmask for an interface index.

        Parameters:
        :   - **index** – Network interface index
            - **netmask** – IPv4 netmask

        Returns:
        :   True if netmask was added, false otherwise.

    void net\_if\_ipv4\_set\_gw(struct [net\_if](#c.net_if) \*iface, const struct [in\_addr](ip_4_6.md#c.in_addr "in_addr") \*gw)
    :   Set IPv4 gateway for an interface.

        Parameters:
        :   - **iface** – Interface to use.
            - **gw** – IPv4 address of an gateway

    bool net\_if\_ipv4\_set\_gw\_by\_index(int index, const struct [in\_addr](ip_4_6.md#c.in_addr "in_addr") \*gw)
    :   Set IPv4 gateway for an interface index.

        Parameters:
        :   - **index** – Network interface index
            - **gw** – IPv4 address of an gateway

        Returns:
        :   True if gateway was added, false otherwise.

    struct [net\_if](#c.net_if) \*net\_if\_select\_src\_iface(const struct [sockaddr](ip_4_6.md#c.sockaddr "sockaddr") \*dst)
    :   Get a network interface that should be used when sending IPv6 or IPv4 network data to destination.

        Parameters:
        :   - **dst** – IPv6 or IPv4 destination address

        Returns:
        :   Pointer to network interface to use. Note that the function will return the default network interface if the best network interface is not found.

    void net\_if\_register\_link\_cb(struct [net\_if\_link\_cb](#c.net_if_link_cb) \*link, [net\_if\_link\_callback\_t](#c.net_if_link_callback_t) cb)
    :   Register a link callback.

        Parameters:
        :   - **link** – Caller specified handler for the callback.
            - **cb** – Callback to register.

    void net\_if\_unregister\_link\_cb(struct [net\_if\_link\_cb](#c.net_if_link_cb) \*link)
    :   Unregister a link callback.

        Parameters:
        :   - **link** – Caller specified handler for the callback.

    void net\_if\_call\_link\_cb(struct [net\_if](#c.net_if) \*iface, struct [net\_linkaddr](net_linkaddr.md#c.net_linkaddr "net_linkaddr") \*lladdr, int status)
    :   Call a link callback function.

        Parameters:
        :   - **iface** – Network interface.
            - **lladdr** – Destination link layer address
            - **status** – 0 is ok, < 0 error

    bool net\_if\_need\_calc\_rx\_checksum(struct [net\_if](#c.net_if) \*iface)
    :   Check if received network packet checksum calculation can be avoided or not.

        For example many ethernet devices support network packet offloading in which case the IP stack does not need to calculate the checksum.

        Parameters:
        :   - **iface** – Network interface

        Returns:
        :   True if checksum needs to be calculated, false otherwise.

    bool net\_if\_need\_calc\_tx\_checksum(struct [net\_if](#c.net_if) \*iface)
    :   Check if network packet checksum calculation can be avoided or not when sending the packet.

        For example many ethernet devices support network packet offloading in which case the IP stack does not need to calculate the checksum.

        Parameters:
        :   - **iface** – Network interface

        Returns:
        :   True if checksum needs to be calculated, false otherwise.

    struct [net\_if](#c.net_if) \*net\_if\_get\_by\_index(int index)
    :   Get interface according to index.

        This is a syscall only to provide access to the object for purposes of assigning permissions.

        Parameters:
        :   - **index** – Interface index

        Returns:
        :   Pointer to interface or NULL if not found.

    int net\_if\_get\_by\_iface(struct [net\_if](#c.net_if) \*iface)
    :   Get interface index according to pointer.

        Parameters:
        :   - **iface** – Pointer to network interface

        Returns:
        :   Interface index

    void net\_if\_foreach([net\_if\_cb\_t](#c.net_if_cb_t) cb, void \*user\_data)
    :   Go through all the network interfaces and call callback for each interface.

        Parameters:
        :   - **cb** – User-supplied callback function to call
            - **user\_data** – User specified data

    int net\_if\_up(struct [net\_if](#c.net_if) \*iface)
    :   Bring interface up.

        Parameters:
        :   - **iface** – Pointer to network interface

        Returns:
        :   0 on success

    static inline bool net\_if\_is\_up(struct [net\_if](#c.net_if) \*iface)
    :   Check if interface is is up and running.

        Parameters:
        :   - **iface** – Pointer to network interface

        Returns:
        :   True if interface is up, False if it is down.

    int net\_if\_down(struct [net\_if](#c.net_if) \*iface)
    :   Bring interface down.

        Parameters:
        :   - **iface** – Pointer to network interface

        Returns:
        :   0 on success

    static inline bool net\_if\_is\_admin\_up(struct [net\_if](#c.net_if) \*iface)
    :   Check if interface was brought up by the administrator.

        Parameters:
        :   - **iface** – Pointer to network interface

        Returns:
        :   True if interface is admin up, false otherwise.

    void net\_if\_carrier\_on(struct [net\_if](#c.net_if) \*iface)
    :   Underlying network device has detected the carrier (cable connected).

        The function should be used by the respective network device driver or L2 implementation to update its state on a network interface.

        Parameters:
        :   - **iface** – Pointer to network interface

    void net\_if\_carrier\_off(struct [net\_if](#c.net_if) \*iface)
    :   Underlying network device has lost the carrier (cable disconnected).

        The function should be used by the respective network device driver or L2 implementation to update its state on a network interface.

        Parameters:
        :   - **iface** – Pointer to network interface

    static inline bool net\_if\_is\_carrier\_ok(struct [net\_if](#c.net_if) \*iface)
    :   Check if carrier is present on network device.

        Parameters:
        :   - **iface** – Pointer to network interface

        Returns:
        :   True if carrier is present, false otherwise.

    void net\_if\_dormant\_on(struct [net\_if](#c.net_if) \*iface)
    :   Mark interface as dormant.

        Dormant state indicates that the interface is not ready to pass packets yet, but is waiting for some event (for example Wi-Fi network association).

        The function should be used by the respective network device driver or L2 implementation to update its state on a network interface.

        Parameters:
        :   - **iface** – Pointer to network interface

    void net\_if\_dormant\_off(struct [net\_if](#c.net_if) \*iface)
    :   Mark interface as not dormant.

        The function should be used by the respective network device driver or L2 implementation to update its state on a network interface.

        Parameters:
        :   - **iface** – Pointer to network interface

    static inline bool net\_if\_is\_dormant(struct [net\_if](#c.net_if) \*iface)
    :   Check if the interface is dormant.

        Parameters:
        :   - **iface** – Pointer to network interface

        Returns:
        :   True if interface is dormant, false otherwise.

    static inline int net\_if\_set\_promisc(struct [net\_if](#c.net_if) \*iface)
    :   Set network interface into promiscuous mode.

        Note that not all network technologies will support this.

        Parameters:
        :   - **iface** – Pointer to network interface

        Returns:
        :   0 on success, <0 if error

    static inline void net\_if\_unset\_promisc(struct [net\_if](#c.net_if) \*iface)
    :   Set network interface into normal mode.

        Parameters:
        :   - **iface** – Pointer to network interface

    static inline bool net\_if\_is\_promisc(struct [net\_if](#c.net_if) \*iface)
    :   Check if promiscuous mode is set or not.

        Parameters:
        :   - **iface** – Pointer to network interface

        Returns:
        :   True if interface is in promisc mode, False if interface is not in in promiscuous mode.

    static inline bool net\_if\_are\_pending\_tx\_packets(struct [net\_if](#c.net_if) \*iface)
    :   Check if there are any pending TX network data for a given network interface.

        Parameters:
        :   - **iface** – Pointer to network interface

        Returns:
        :   True if there are pending TX network packets for this network interface, False otherwise.

    bool net\_if\_is\_wifi(struct [net\_if](#c.net_if) \*iface)
    :   Check if the network interface supports Wi-Fi.

        Parameters:
        :   - **iface** – Pointer to network interface

        Returns:
        :   True if interface supports Wi-Fi, False otherwise.

    struct [net\_if](#c.net_if) \*net\_if\_get\_first\_wifi(void)
    :   Get first Wi-Fi network interface.

        Returns:
        :   Pointer to network interface, NULL if not found.

    int net\_if\_get\_name(struct [net\_if](#c.net_if) \*iface, char \*buf, int len)
    :   Get network interface name.

        If interface name support is not enabled, empty string is returned.

        Parameters:
        :   - **iface** – Pointer to network interface
            - **buf** – User supplied buffer
            - **len** – Length of the user supplied buffer

        Returns:
        :   Length of the interface name copied to buf, -EINVAL if invalid parameters, -ERANGE if name cannot be copied to the user supplied buffer, -ENOTSUP if interface name support is disabled,

    int net\_if\_set\_name(struct [net\_if](#c.net_if) \*iface, const char \*buf)
    :   Set network interface name.

        Normally this function is not needed to call as the system will automatically assign a name to the network interface.

        Parameters:
        :   - **iface** – Pointer to network interface
            - **buf** – User supplied name

        Returns:
        :   0 name is set correctly -ENOTSUP interface name support is disabled -EINVAL if invalid parameters are given, -ENAMETOOLONG if name is too long

    int net\_if\_get\_by\_name(const char \*name)
    :   Get interface index according to its name.

        Parameters:
        :   - **name** – Name of the network interface

        Returns:
        :   Interface index

    struct net\_if\_addr
    :   *#include <net\_if.h>*

        Network Interface unicast IP addresses.

        Stores the unicast IP addresses assigned to this network interface.

        Public Members

        struct net\_addr address
        :   IP address.

        enum [net\_addr\_type](ip_4_6.md#c.net_addr_type "net_addr_type") addr\_type
        :   How the IP address was set.

        enum [net\_addr\_state](ip_4_6.md#c.net_addr_state "net_addr_state") addr\_state
        :   What is the current state of the address.

        uint8\_t is\_infinite
        :   Is the IP address valid forever.

        uint8\_t is\_used
        :   Is this IP address used or not.

        uint8\_t is\_mesh\_local
        :   Is this IP address usage limited to the subnet (mesh) or not.

    struct net\_if\_mcast\_addr
    :   *#include <net\_if.h>*

        Network Interface multicast IP addresses.

        Stores the multicast IP addresses assigned to this network interface.

        Public Members

        struct net\_addr address
        :   IP address.

        uint8\_t is\_used
        :   Is this multicast IP address used or not.

        uint8\_t is\_joined
        :   Did we join to this group.

    struct net\_if\_ipv6\_prefix
    :   *#include <net\_if.h>*

        Network Interface IPv6 prefixes.

        Stores the IPV6 prefixes assigned to this network interface.

        Public Members

        struct [net\_timeout](net_timeout.md#c.net_timeout "net_timeout") lifetime
        :   Prefix lifetime.

        struct [in6\_addr](ip_4_6.md#c.in6_addr "in6_addr") prefix
        :   IPv6 prefix.

        struct [net\_if](#c.net_if) \*iface
        :   Backpointer to network interface where this prefix is used.

        uint8\_t len
        :   Prefix length.

        uint8\_t is\_infinite
        :   Is the IP prefix valid forever.

        uint8\_t is\_used
        :   Is this prefix used or not.

    struct net\_if\_router
    :   *#include <net\_if.h>*

        Information about routers in the system.

        Stores the router information.

        Public Members

        [sys\_snode\_t](../../../kernel/data_structures/slist.md#c.sys_snode_t "sys_snode_t") node
        :   Slist lifetime timer node.

        struct net\_addr address
        :   IP address.

        struct [net\_if](#c.net_if) \*iface
        :   Network interface the router is connected to.

        uint32\_t life\_start
        :   Router life timer start.

        uint16\_t lifetime
        :   Router lifetime.

        uint8\_t is\_used
        :   Is this router used or not.

        uint8\_t is\_default
        :   Is default router.

        uint8\_t is\_infinite
        :   Is the router valid forever.

    struct net\_if\_ipv6
    :   *#include <net\_if.h>*

        Public Members

        struct [net\_if\_addr](#c.net_if_addr) unicast[NET\_IF\_MAX\_IPV6\_ADDR]
        :   Unicast IP addresses.

        struct [net\_if\_mcast\_addr](#c.net_if_mcast_addr) mcast[NET\_IF\_MAX\_IPV6\_MADDR]
        :   Multicast IP addresses.

        struct [net\_if\_ipv6\_prefix](#c.net_if_ipv6_prefix) prefix[NET\_IF\_MAX\_IPV6\_PREFIX]
        :   Prefixes.

        uint32\_t base\_reachable\_time
        :   Default reachable time (RFC 4861, page 52).

        uint32\_t reachable\_time
        :   Reachable time (RFC 4861, page 20).

        uint32\_t retrans\_timer
        :   Retransmit timer (RFC 4861, page 52).

        uint8\_t hop\_limit
        :   IPv6 hop limit.

        uint8\_t mcast\_hop\_limit
        :   IPv6 multicast hop limit.

    struct net\_if\_ipv4
    :   *#include <net\_if.h>*

        Public Members

        struct [net\_if\_addr](#c.net_if_addr) unicast[NET\_IF\_MAX\_IPV4\_ADDR]
        :   Unicast IP addresses.

        struct [net\_if\_mcast\_addr](#c.net_if_mcast_addr) mcast[NET\_IF\_MAX\_IPV4\_MADDR]
        :   Multicast IP addresses.

        struct [in\_addr](ip_4_6.md#c.in_addr "in_addr") gw
        :   Gateway.

        struct [in\_addr](ip_4_6.md#c.in_addr "in_addr") netmask
        :   Netmask.

        uint8\_t ttl
        :   IPv4 time-to-live.

        uint8\_t mcast\_ttl
        :   IPv4 time-to-live for multicast packets.

    struct net\_if\_ip
    :   *#include <net\_if.h>*

        Network interface IP address configuration.

    struct net\_if\_config
    :   *#include <net\_if.h>*

        IP and other configuration related data for network interface.

    struct net\_traffic\_class
    :   *#include <net\_if.h>*

        Network traffic class.

        Traffic classes are used when sending or receiving data that is classified with different priorities. So some traffic can be marked as high priority and it will be sent or received first. Each network packet that is transmitted or received goes through a fifo to a thread that will transmit it.

        Public Members

        struct k\_fifo fifo
        :   Fifo for handling this Tx or Rx packet.

        struct [k\_thread](../../../kernel/services/threads/index.md#c.k_thread "k_thread") handler
        :   Traffic class handler thread.

        k\_thread\_stack\_t \*stack
        :   Stack for this handler.

    struct net\_if\_dev
    :   *#include <net\_if.h>*

        Network Interface Device structure.

        Used to handle a network interface on top of a device driver instance. There can be many [net\_if\_dev](#structnet__if__dev) instance against the same device.

        Such interface is mainly to be used by the link layer, but is also tight to a network context: it then makes the relation with a network context and the network device.

        Because of the strong relationship between a device driver and such network interface, each [net\_if\_dev](#structnet__if__dev) should be instantiated by one of the network device init macros found in net\_if.h.

        Public Members

        const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev
        :   The actually device driver instance the [net\_if](#structnet__if) is related to.

        const struct [net\_l2](net_l2.md#c.net_l2 "net_l2") \*const l2
        :   Interface’s L2 layer.

        void \*l2\_data
        :   Interface’s private L2 data pointer.

        struct [net\_linkaddr](net_linkaddr.md#c.net_linkaddr "net_linkaddr") link\_addr
        :   The hardware link address.

        uint16\_t mtu
        :   The hardware MTU.

        enum [net\_if\_oper\_state](#c.net_if_oper_state) oper\_state
        :   RFC 2863 operational status.

    struct net\_if
    :   *#include <net\_if.h>*

        Network Interface structure.

        Used to handle a network interface on top of a [net\_if\_dev](#structnet__if__dev) instance. There can be many [net\_if](#structnet__if) instance against the same [net\_if\_dev](#structnet__if__dev) instance.

        Public Members

        struct [net\_if\_dev](#c.net_if_dev) \*if\_dev
        :   The [net\_if\_dev](#structnet__if__dev) instance the [net\_if](#structnet__if) is related to.

        struct [net\_if\_config](#c.net_if_config) config
        :   Network interface instance configuration.

    struct net\_if\_mcast\_monitor
    :   *#include <net\_if.h>*

        Multicast monitor handler struct.

        Stores the multicast callback information. Caller must make sure that the variable pointed by this is valid during the lifetime of registration. Typically this means that the variable cannot be allocated from stack.

        Public Members

        [sys\_snode\_t](../../../kernel/data_structures/slist.md#c.sys_snode_t "sys_snode_t") node
        :   Node information for the slist.

        struct [net\_if](#c.net_if) \*iface
        :   Network interface.

        [net\_if\_mcast\_callback\_t](#c.net_if_mcast_callback_t) cb
        :   Multicast callback.

    struct net\_if\_link\_cb
    :   *#include <net\_if.h>*

        Link callback handler struct.

        Stores the link callback information. Caller must make sure that the variable pointed by this is valid during the lifetime of registration. Typically this means that the variable cannot be allocated from stack.

        Public Members

        [sys\_snode\_t](../../../kernel/data_structures/slist.md#c.sys_snode_t "sys_snode_t") node
        :   Node information for the slist.

        [net\_if\_link\_callback\_t](#c.net_if_link_callback_t) cb
        :   Link callback.
