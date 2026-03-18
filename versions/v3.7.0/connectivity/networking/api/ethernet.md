---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/networking/api/ethernet.html
original_path: connectivity/networking/api/ethernet.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Ethernet

## [Overview](#id1)

Ethernet is a networking technology commonly used in local area networks (LAN).
For more information, see this
[Ethernet Wikipedia article](https://en.wikipedia.org/wiki/Ethernet).

Zephyr supports following Ethernet features:

- 10, 100 and 1000 Mbit/sec links
- Auto negotiation
- Half/full duplex
- Promiscuous mode
- TX and RX checksum offloading
- MAC address filtering
- [Virtual LANs](vlan.md#vlan-interface)
- [Priority queues](traffic-class.md#traffic-class-support)
- [IEEE 802.1AS (gPTP)](gptp.md#gptp-interface)
- [IEEE 802.1Qav (credit based shaping)](8021Qav.md#qav)
- [LLDP (Link Layer Discovery Protocol)](lldp.md#lldp-interface)

Not all Ethernet device drivers support all of these features. You can
see what is supported by `net iface` net-shell command. It will print
currently supported Ethernet features.

## [API Reference](#id2)

Related code samples

[Inter-VM Shared Memory (ivshmem) Ethernet](../../../samples/drivers/ethernet/eth_ivshmem/README.md#eth-ivshmem "Communicate with another "cell" in the Jailhouse hypervisor using IVSHMEM Ethernet.")
:   Communicate with another "cell" in the Jailhouse hypervisor using IVSHMEM Ethernet.

[Packet socket](../../../samples/net/sockets/packet/README.md#packet-socket "Use raw packet sockets over Ethernet.")
:   Use raw packet sockets over Ethernet.

[UDP sender using SO\_TXTIME](../../../samples/net/sockets/txtime/README.md#so_txtime "Control the transmission time of a packet using SO_TXTIME socket option.")
:   Control the transmission time of a packet using SO\_TXTIME socket option.

*group* Ethernet Support Functions
:   Ethernet support functions.

    Defines

    NET\_ETH\_ADDR\_LEN
    :   Ethernet MAC address length.

    NET\_ETH\_MINIMAL\_FRAME\_SIZE
    :   Minimum Ethernet frame size.

    NET\_ETH\_MTU
    :   Ethernet MTU size.

    ETH\_NET\_DEVICE\_INIT(dev\_id, name, init\_fn, pm, data, config, prio, api, mtu)
    :   Create an Ethernet network interface and bind it to network device.

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

    ETH\_NET\_DEVICE\_INIT\_INSTANCE(dev\_id, name, instance, init\_fn, pm, data, config, prio, api, mtu)
    :   Create multiple Ethernet network interfaces and bind them to network devices.

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
            - **mtu** – Maximum transfer unit in bytes for this network interface.

    ETH\_NET\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, config, prio, api, mtu)
    :   Like ETH\_NET\_DEVICE\_INIT but taking metadata from a devicetree.

        Create an Ethernet network interface and bind it to network device.

        Parameters:
        :   - **node\_id** – The devicetree node identifier.
            - **init\_fn** – Address to the init function of the driver.
            - **pm** – Reference to struct [pm\_device](../../../services/pm/api/index.md#structpm__device) associated with the device. (optional).
            - **data** – Pointer to the device’s private data.
            - **config** – The address to the structure containing the configuration information for this instance of the driver.
            - **prio** – The initialization level at which configuration occurs.
            - **api** – Provides an initial pointer to the API function struct used by the driver. Can be NULL.
            - **mtu** – Maximum transfer unit in bytes for this network interface.

    ETH\_NET\_DEVICE\_DT\_INST\_DEFINE(inst, ...)
    :   Like ETH\_NET\_DEVICE\_DT\_DEFINE for an instance of a DT\_DRV\_COMPAT compatible.

        Parameters:
        :   - **inst** – instance number. This is replaced by `DT_DRV_COMPAT(inst)` in the call to ETH\_NET\_DEVICE\_DT\_DEFINE.
            - **...** – other parameters as expected by ETH\_NET\_DEVICE\_DT\_DEFINE.

    Enums

    enum ethernet\_hw\_caps
    :   Ethernet hardware capabilities.

        *Values:*

        enumerator ETHERNET\_HW\_TX\_CHKSUM\_OFFLOAD = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(0)
        :   TX Checksum offloading supported for all of IPv4, UDP, TCP.

        enumerator ETHERNET\_HW\_RX\_CHKSUM\_OFFLOAD = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(1)
        :   RX Checksum offloading supported for all of IPv4, UDP, TCP.

        enumerator ETHERNET\_HW\_VLAN = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(2)
        :   VLAN supported.

        enumerator ETHERNET\_AUTO\_NEGOTIATION\_SET = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(3)
        :   Enabling/disabling auto negotiation supported.

        enumerator ETHERNET\_LINK\_10BASE\_T = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(4)
        :   10 Mbits link supported

        enumerator ETHERNET\_LINK\_100BASE\_T = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(5)
        :   100 Mbits link supported

        enumerator ETHERNET\_LINK\_1000BASE\_T = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(6)
        :   1 Gbits link supported

        enumerator ETHERNET\_DUPLEX\_SET = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(7)
        :   Changing duplex (half/full) supported.

        enumerator ETHERNET\_PTP = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(8)
        :   IEEE 802.1AS (gPTP) clock supported.

        enumerator ETHERNET\_QAV = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(9)
        :   IEEE 802.1Qav (credit-based shaping) supported.

        enumerator ETHERNET\_PROMISC\_MODE = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(10)
        :   Promiscuous mode supported.

        enumerator ETHERNET\_PRIORITY\_QUEUES = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(11)
        :   Priority queues available.

        enumerator ETHERNET\_HW\_FILTERING = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(12)
        :   MAC address filtering supported.

        enumerator ETHERNET\_LLDP = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(13)
        :   Link Layer Discovery Protocol supported.

        enumerator ETHERNET\_HW\_VLAN\_TAG\_STRIP = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(14)
        :   VLAN Tag stripping.

        enumerator ETHERNET\_DSA\_SLAVE\_PORT = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(15)
        :   DSA switch slave port.

        enumerator ETHERNET\_DSA\_MASTER\_PORT = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(16)
        :   DSA switch master port.

        enumerator ETHERNET\_QBV = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(17)
        :   IEEE 802.1Qbv (scheduled traffic) supported.

        enumerator ETHERNET\_QBU = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(18)
        :   IEEE 802.1Qbu (frame preemption) supported.

        enumerator ETHERNET\_TXTIME = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(19)
        :   TXTIME supported.

        enumerator ETHERNET\_TXINJECTION\_MODE = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(20)
        :   TX-Injection supported.

    enum ethernet\_if\_types
    :   Types of Ethernet L2.

        *Values:*

        enumerator L2\_ETH\_IF\_TYPE\_ETHERNET
        :   IEEE 802.3 Ethernet (default).

        enumerator L2\_ETH\_IF\_TYPE\_WIFI
        :   IEEE 802.11 Wi-Fi.

    enum ethernet\_checksum\_support
    :   Protocols that are supported by checksum offloading.

        *Values:*

        enumerator ETHERNET\_CHECKSUM\_SUPPORT\_NONE = NET\_IF\_CHECKSUM\_NONE\_BIT
        :   Device does not support any L3/L4 checksum offloading.

        enumerator ETHERNET\_CHECKSUM\_SUPPORT\_IPV4\_HEADER = NET\_IF\_CHECKSUM\_IPV4\_HEADER\_BIT
        :   Device supports checksum offloading for the IPv4 header.

        enumerator ETHERNET\_CHECKSUM\_SUPPORT\_IPV4\_ICMP = NET\_IF\_CHECKSUM\_IPV4\_ICMP\_BIT
        :   Device supports checksum offloading for ICMPv4 payload (implies IPv4 header).

        enumerator ETHERNET\_CHECKSUM\_SUPPORT\_IPV6\_HEADER = NET\_IF\_CHECKSUM\_IPV6\_HEADER\_BIT
        :   Device supports checksum offloading for the IPv6 header.

        enumerator ETHERNET\_CHECKSUM\_SUPPORT\_IPV6\_ICMP = NET\_IF\_CHECKSUM\_IPV6\_ICMP\_BIT
        :   Device supports checksum offloading for ICMPv6 payload (implies IPv6 header).

        enumerator ETHERNET\_CHECKSUM\_SUPPORT\_TCP = NET\_IF\_CHECKSUM\_TCP\_BIT
        :   Device supports TCP checksum offloading for all supported IP protocols.

        enumerator ETHERNET\_CHECKSUM\_SUPPORT\_UDP = NET\_IF\_CHECKSUM\_UDP\_BIT
        :   Device supports UDP checksum offloading for all supported IP protocols.

    Functions

    static inline bool net\_eth\_is\_addr\_broadcast(struct [net\_eth\_addr](#c.net_eth_addr) \*addr)
    :   Check if the Ethernet MAC address is a broadcast address.

        Parameters:
        :   - **addr** – A valid pointer to a Ethernet MAC address.

        Returns:
        :   true if address is a broadcast address, false if not

    static inline bool net\_eth\_is\_addr\_all\_zeroes(struct [net\_eth\_addr](#c.net_eth_addr) \*addr)
    :   Check if the Ethernet MAC address is a all zeroes address.

        Parameters:
        :   - **addr** – A valid pointer to an Ethernet MAC address.

        Returns:
        :   true if address is an all zeroes address, false if not

    static inline bool net\_eth\_is\_addr\_unspecified(struct [net\_eth\_addr](#c.net_eth_addr) \*addr)
    :   Check if the Ethernet MAC address is unspecified.

        Parameters:
        :   - **addr** – A valid pointer to a Ethernet MAC address.

        Returns:
        :   true if address is unspecified, false if not

    static inline bool net\_eth\_is\_addr\_multicast(struct [net\_eth\_addr](#c.net_eth_addr) \*addr)
    :   Check if the Ethernet MAC address is a multicast address.

        Parameters:
        :   - **addr** – A valid pointer to a Ethernet MAC address.

        Returns:
        :   true if address is a multicast address, false if not

    static inline bool net\_eth\_is\_addr\_group(struct [net\_eth\_addr](#c.net_eth_addr) \*addr)
    :   Check if the Ethernet MAC address is a group address.

        Parameters:
        :   - **addr** – A valid pointer to a Ethernet MAC address.

        Returns:
        :   true if address is a group address, false if not

    static inline bool net\_eth\_is\_addr\_valid(struct [net\_eth\_addr](#c.net_eth_addr) \*addr)
    :   Check if the Ethernet MAC address is valid.

        Parameters:
        :   - **addr** – A valid pointer to a Ethernet MAC address.

        Returns:
        :   true if address is valid, false if not

    static inline bool net\_eth\_is\_addr\_lldp\_multicast(struct [net\_eth\_addr](#c.net_eth_addr) \*addr)
    :   Check if the Ethernet MAC address is a LLDP multicast address.

        Parameters:
        :   - **addr** – A valid pointer to a Ethernet MAC address.

        Returns:
        :   true if address is a LLDP multicast address, false if not

    static inline bool net\_eth\_is\_addr\_ptp\_multicast(struct [net\_eth\_addr](#c.net_eth_addr) \*addr)
    :   Check if the Ethernet MAC address is a PTP multicast address.

        Parameters:
        :   - **addr** – A valid pointer to a Ethernet MAC address.

        Returns:
        :   true if address is a PTP multicast address, false if not

    const struct [net\_eth\_addr](#c.net_eth_addr) \*net\_eth\_broadcast\_addr(void)
    :   Return Ethernet broadcast address.

        Returns:
        :   Ethernet broadcast address.

    void net\_eth\_ipv4\_mcast\_to\_mac\_addr(const struct [in\_addr](ip_4_6.md#c.in_addr "in_addr") \*ipv4\_addr, struct [net\_eth\_addr](#c.net_eth_addr) \*mac\_addr)
    :   Convert IPv4 multicast address to Ethernet address.

        Parameters:
        :   - **ipv4\_addr** – IPv4 multicast address
            - **mac\_addr** – Output buffer for Ethernet address

    void net\_eth\_ipv6\_mcast\_to\_mac\_addr(const struct [in6\_addr](ip_4_6.md#c.in6_addr "in6_addr") \*ipv6\_addr, struct [net\_eth\_addr](#c.net_eth_addr) \*mac\_addr)
    :   Convert IPv6 multicast address to Ethernet address.

        Parameters:
        :   - **ipv6\_addr** – IPv6 multicast address
            - **mac\_addr** – Output buffer for Ethernet address

    static inline enum [ethernet\_hw\_caps](#c.ethernet_hw_caps) net\_eth\_get\_hw\_capabilities(struct [net\_if](net_if.md#c.net_if "net_if") \*iface)
    :   Return ethernet device hardware capability information.

        Parameters:
        :   - **iface** – Network interface

        Returns:
        :   Hardware capabilities

    static inline int net\_eth\_get\_hw\_config(struct [net\_if](net_if.md#c.net_if "net_if") \*iface, enum ethernet\_config\_type type, struct ethernet\_config \*config)
    :   Return ethernet device hardware configuration information.

        Parameters:
        :   - **iface** – Network interface
            - **type** – configuration type
            - **config** – Ethernet configuration

        Returns:
        :   0 if ok, <0 if error

    static inline int net\_eth\_vlan\_enable(struct [net\_if](net_if.md#c.net_if "net_if") \*iface, uint16\_t tag)
    :   Add VLAN tag to the interface.

        Parameters:
        :   - **iface** – Interface to use.
            - **tag** – VLAN tag to add

        Returns:
        :   0 if ok, <0 if error

    static inline int net\_eth\_vlan\_disable(struct [net\_if](net_if.md#c.net_if "net_if") \*iface, uint16\_t tag)
    :   Remove VLAN tag from the interface.

        Parameters:
        :   - **iface** – Interface to use.
            - **tag** – VLAN tag to remove

        Returns:
        :   0 if ok, <0 if error

    static inline uint16\_t net\_eth\_get\_vlan\_tag(struct [net\_if](net_if.md#c.net_if "net_if") \*iface)
    :   Return VLAN tag specified to network interface.

        Note that the interface parameter must be the VLAN interface, and not the Ethernet one.

        Parameters:
        :   - **iface** – VLAN network interface.

        Returns:
        :   VLAN tag for this interface or NET\_VLAN\_TAG\_UNSPEC if VLAN is not configured for that interface.

    static inline struct [net\_if](net_if.md#c.net_if "net_if") \*net\_eth\_get\_vlan\_iface(struct [net\_if](net_if.md#c.net_if "net_if") \*iface, uint16\_t tag)
    :   Return network interface related to this VLAN tag.

        Parameters:
        :   - **iface** – Main network interface (not the VLAN one).
            - **tag** – VLAN tag

        Returns:
        :   Network interface related to this tag or NULL if no such interface exists.

    static inline struct [net\_if](net_if.md#c.net_if "net_if") \*net\_eth\_get\_vlan\_main(struct [net\_if](net_if.md#c.net_if "net_if") \*iface)
    :   Return main network interface that is attached to this VLAN tag.

        Parameters:
        :   - **iface** – VLAN network interface. This is used to get the pointer to ethernet L2 context

        Returns:
        :   Network interface related to this tag or NULL if no such interface exists.

    static inline bool net\_eth\_is\_vlan\_enabled(struct ethernet\_context \*ctx, struct [net\_if](net_if.md#c.net_if "net_if") \*iface)
    :   Check if there are any VLAN interfaces enabled to this specific Ethernet network interface.

        Note that the iface must be the actual Ethernet interface and not the virtual VLAN interface.

        Parameters:
        :   - **ctx** – Ethernet context
            - **iface** – Ethernet network interface

        Returns:
        :   True if there are enabled VLANs for this network interface, false if not.

    static inline bool net\_eth\_get\_vlan\_status(struct [net\_if](net_if.md#c.net_if "net_if") \*iface)
    :   Get VLAN status for a given network interface (enabled or not).

        Parameters:
        :   - **iface** – Network interface

        Returns:
        :   True if VLAN is enabled for this network interface, false if not.

    static inline bool net\_eth\_is\_vlan\_interface(struct [net\_if](net_if.md#c.net_if "net_if") \*iface)
    :   Check if the given interface is a VLAN interface.

        Parameters:
        :   - **iface** – Network interface

        Returns:
        :   True if this network interface is VLAN one, false if not.

    void net\_eth\_carrier\_on(struct [net\_if](net_if.md#c.net_if "net_if") \*iface)
    :   Inform ethernet L2 driver that ethernet carrier is detected.

        This happens when cable is connected.

        Parameters:
        :   - **iface** – Network interface

    void net\_eth\_carrier\_off(struct [net\_if](net_if.md#c.net_if "net_if") \*iface)
    :   Inform ethernet L2 driver that ethernet carrier was lost.

        This happens when cable is disconnected.

        Parameters:
        :   - **iface** – Network interface

    int net\_eth\_promisc\_mode(struct [net\_if](net_if.md#c.net_if "net_if") \*iface, bool enable)
    :   Set promiscuous mode either ON or OFF.

        Parameters:
        :   - **iface** – Network interface
            - **enable** – on (true) or off (false)

        Returns:
        :   0 if mode set or unset was successful, <0 otherwise.

    int net\_eth\_txinjection\_mode(struct [net\_if](net_if.md#c.net_if "net_if") \*iface, bool enable)
    :   Set TX-Injection mode either ON or OFF.

        Parameters:
        :   - **iface** – Network interface
            - **enable** – on (true) or off (false)

        Returns:
        :   0 if mode set or unset was successful, <0 otherwise.

    int net\_eth\_mac\_filter(struct [net\_if](net_if.md#c.net_if "net_if") \*iface, struct [net\_eth\_addr](#c.net_eth_addr) \*mac, enum ethernet\_filter\_type type, bool enable)
    :   Set or unset HW filtering for MAC address `mac`.

        Parameters:
        :   - **iface** – Network interface
            - **mac** – Pointer to an ethernet MAC address
            - **type** – Filter type, either source or destination
            - **enable** – Set (true) or unset (false)

        Returns:
        :   0 if filter set or unset was successful, <0 otherwise.

    static inline const struct [device](../../../kernel/drivers/index.md#c.device "device") \*net\_eth\_get\_ptp\_clock(struct [net\_if](net_if.md#c.net_if "net_if") \*iface)
    :   Return PTP clock that is tied to this ethernet network interface.

        Parameters:
        :   - **iface** – Network interface

        Returns:
        :   Pointer to PTP clock if found, NULL if not found or if this ethernet interface does not support PTP.

    const struct [device](../../../kernel/drivers/index.md#c.device "device") \*net\_eth\_get\_ptp\_clock\_by\_index(int index)
    :   Return PTP clock that is tied to this ethernet network interface index.

        Parameters:
        :   - **index** – Network interface index

        Returns:
        :   Pointer to PTP clock if found, NULL if not found or if this ethernet interface index does not support PTP.

    static inline int net\_eth\_get\_ptp\_port(struct [net\_if](net_if.md#c.net_if "net_if") \*iface)
    :   Return PTP port number attached to this interface.

        Parameters:
        :   - **iface** – Network interface

        Returns:
        :   Port number, no such port if < 0

    static inline void net\_eth\_set\_ptp\_port(struct [net\_if](net_if.md#c.net_if "net_if") \*iface, int port)
    :   Set PTP port number attached to this interface.

        Parameters:
        :   - **iface** – Network interface
            - **port** – Port number to set

    static inline bool net\_eth\_type\_is\_wifi(struct [net\_if](net_if.md#c.net_if "net_if") \*iface)
    :   Check if the Ethernet L2 network interface can perform Wi-Fi.

        Parameters:
        :   - **iface** – Pointer to network interface

        Returns:
        :   True if interface supports Wi-Fi, False otherwise.

    struct net\_eth\_addr
    :   *#include <ethernet.h>*

        Ethernet address.

        Public Members

        uint8\_t addr[6U]
        :   Buffer storing the address.

    struct ethernet\_t1s\_param
    :   *#include <ethernet.h>*

        Ethernet T1S specific parameters.

        Public Members

        enum ethernet\_t1s\_param\_type type
        :   Type of T1S parameter.

        bool enable
        :   T1S PLCA enabled.

        uint8\_t node\_id
        :   T1S PLCA node id range: 0 to 254.

        uint8\_t node\_count
        :   T1S PLCA node count range: 1 to 255.

        uint8\_t burst\_count
        :   T1S PLCA burst count range: 0x0 to 0xFF.

        uint8\_t burst\_timer
        :   T1S PLCA burst timer.

        uint8\_t to\_timer
        :   T1S PLCA TO value.

        struct [ethernet\_t1s\_param](#c.ethernet_t1s_param).[anonymous].[anonymous] plca
        :   PLCA is the Physical Layer (PHY) Collision Avoidance technique employed with multidrop 10Base-T1S standard.

            The PLCA parameters are described in standard [1] as registers in memory map 4 (MMS = 4) (point 9.6).

            IDVER (PLCA ID Version) CTRL0 (PLCA Control 0) CTRL1 (PLCA Control 1) STATUS (PLCA Status) TOTMR (PLCA TO Control) BURST (PLCA Burst Control)

            Those registers are implemented by each OA TC6 compliant vendor (like for e.g. LAN865x - e.g. [2]).

            Documents: [1] - “OPEN Alliance 10BASE-T1x MAC-PHY Serial

            Interface” (ver. 1.1) [2] - “DS60001734C” - LAN865x data sheet

    struct ethernet\_qav\_param
    :   *#include <ethernet.h>*

        Ethernet Qav specific parameters.

        Public Members

        int queue\_id
        :   ID of the priority queue to use.

        enum ethernet\_qav\_param\_type type
        :   Type of Qav parameter.

        bool enabled
        :   True if Qav is enabled for queue.

        unsigned int delta\_bandwidth
        :   Delta Bandwidth (percentage of bandwidth).

        unsigned int idle\_slope
        :   Idle Slope (bits per second).

        unsigned int oper\_idle\_slope
        :   Oper Idle Slope (bits per second).

        unsigned int traffic\_class
        :   Traffic class the queue is bound to.

    struct ethernet\_qbv\_param
    :   *#include <ethernet.h>*

        Ethernet Qbv specific parameters.

        Public Members

        int port\_id
        :   Port id.

        enum ethernet\_qbv\_param\_type type
        :   Type of Qbv parameter.

        enum ethernet\_qbv\_state\_type state
        :   What state (Admin/Oper) parameters are these.

        bool enabled
        :   True if Qbv is enabled or not.

        bool gate\_status[NET\_TC\_TX\_COUNT]
        :   True = open, False = closed.

        enum ethernet\_gate\_state\_operation operation
        :   GateState operation.

        uint32\_t time\_interval
        :   Time interval ticks (nanoseconds).

        uint16\_t row
        :   Gate control list row.

        struct [ethernet\_qbv\_param](#c.ethernet_qbv_param).[anonymous].[anonymous] gate\_control
        :   Gate control information.

        uint32\_t gate\_control\_list\_len
        :   Number of entries in gate control list.

        struct [net\_ptp\_extended\_time](ptp_time.md#c.net_ptp_extended_time "net_ptp_extended_time") base\_time
        :   Base time.

        struct [net\_ptp\_time](ptp_time.md#c.net_ptp_time "net_ptp_time") cycle\_time
        :   Cycle time.

        uint32\_t extension\_time
        :   Extension time (nanoseconds).

    struct ethernet\_qbu\_param
    :   *#include <ethernet.h>*

        Ethernet Qbu specific parameters.

        Public Members

        int port\_id
        :   Port id.

        enum ethernet\_qbu\_param\_type type
        :   Type of Qbu parameter.

        uint32\_t hold\_advance
        :   Hold advance (nanoseconds).

        uint32\_t release\_advance
        :   Release advance (nanoseconds).

        enum ethernet\_qbu\_preempt\_status frame\_preempt\_statuses[NET\_TC\_TX\_COUNT]
        :   sequence of framePreemptionAdminStatus values

        bool enabled
        :   True if Qbu is enabled or not.

        bool link\_partner\_status
        :   Link partner status (from Qbr).

        uint8\_t additional\_fragment\_size
        :   Additional fragment size (from Qbr).

            The minimum non-final fragment size is (additional\_fragment\_size + 1) \* 64 octets

    struct ethernet\_filter
    :   *#include <ethernet.h>*

        Ethernet filter description.

        Public Members

        enum ethernet\_filter\_type type
        :   Type of filter.

        struct [net\_eth\_addr](#c.net_eth_addr) mac\_address
        :   MAC address to filter.

        bool set
        :   Set (true) or unset (false) the filter.

    struct ethernet\_txtime\_param
    :   *#include <ethernet.h>*

        Ethernet TXTIME specific parameters.

        Public Members

        enum ethernet\_txtime\_param\_type type
        :   Type of TXTIME parameter.

        int queue\_id
        :   Queue number for configuring TXTIME.

        bool enable\_txtime
        :   Enable or disable TXTIME per queue.

    struct ethernet\_api
    :   *#include <ethernet.h>*

        Ethernet L2 API operations.

        Public Members

        struct net\_if\_api iface\_api
        :   The net\_if\_api must be placed in first position in this struct so that we are compatible with network interface API.

        int (\*start)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
        :   Collect optional ethernet specific statistics.

            This pointer should be set by driver if statistics needs to be collected for that driver. Start the device

        int (\*stop)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
        :   Stop the device.

        enum [ethernet\_hw\_caps](#c.ethernet_hw_caps) (\*get\_capabilities)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
        :   Get the device capabilities.

        int (\*set\_config)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, enum ethernet\_config\_type type, const struct ethernet\_config \*config)
        :   Set specific hardware configuration.

        int (\*get\_config)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, enum ethernet\_config\_type type, struct ethernet\_config \*config)
        :   Get hardware specific configuration.

        int (\*send)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, struct [net\_pkt](net_pkt.md#c.net_pkt "net_pkt") \*pkt)
        :   The IP stack will call this function when a VLAN tag is enabled or disabled.

            If enable is set to true, then the VLAN tag was added, if it is false then the tag was removed. The driver can utilize this information if needed. Return ptp\_clock device that is tied to this ethernet device Send a network packet

    struct ethernet\_lldp
    :   *#include <ethernet.h>*

        Ethernet LLDP specific parameters.

        Public Members

        [sys\_snode\_t](../../../kernel/data_structures/slist.md#c.sys_snode_t "sys_snode_t") node
        :   Used for track timers.

        const struct [net\_lldpdu](lldp.md#c.net_lldpdu "net_lldpdu") \*lldpdu
        :   LLDP Data Unit mandatory TLVs for the interface.

        const uint8\_t \*optional\_du
        :   LLDP Data Unit optional TLVs for the interface.

        size\_t optional\_len
        :   Length of the optional Data Unit TLVs.

        struct [net\_if](net_if.md#c.net_if "net_if") \*iface
        :   Network interface that has LLDP supported.

        int64\_t tx\_timer\_start
        :   LLDP TX timer start time.

        uint32\_t tx\_timer\_timeout
        :   LLDP TX timeout.

        [net\_lldp\_recv\_cb\_t](lldp.md#c.net_lldp_recv_cb_t "net_lldp_recv_cb_t") cb
        :   LLDP RX callback function.

*group* Ethernet MII Support Functions
:   Ethernet MII (media independent interface) functions.

    Defines

    MII\_BMCR
    :   Basic Mode Control Register.

    MII\_BMSR
    :   Basic Mode Status Register.

    MII\_PHYID1R
    :   PHY ID 1 Register.

    MII\_PHYID2R
    :   PHY ID 2 Register.

    MII\_ANAR
    :   Auto-Negotiation Advertisement Register.

    MII\_ANLPAR
    :   Auto-Negotiation Link Partner Ability Reg.

    MII\_ANER
    :   Auto-Negotiation Expansion Register.

    MII\_ANNPTR
    :   Auto-Negotiation Next Page Transmit Register.

    MII\_ANLPRNPR
    :   Auto-Negotiation Link Partner Received Next Page Reg.

    MII\_1KTCR
    :   1000BASE-T Control Register

    MII\_1KSTSR
    :   1000BASE-T Status Register

    MII\_MMD\_ACR
    :   MMD Access Control Register.

    MII\_MMD\_AADR
    :   MMD Access Address Data Register.

    MII\_ESTAT
    :   Extended Status Register.

    MII\_BMCR\_RESET
    :   PHY reset.

    MII\_BMCR\_LOOPBACK
    :   enable loopback mode

    MII\_BMCR\_SPEED\_LSB
    :   10=1000Mbps 01=100Mbps; 00=10Mbps

    MII\_BMCR\_AUTONEG\_ENABLE
    :   Auto-Negotiation enable.

    MII\_BMCR\_POWER\_DOWN
    :   power down mode

    MII\_BMCR\_ISOLATE
    :   isolate electrically PHY from MII

    MII\_BMCR\_AUTONEG\_RESTART
    :   restart auto-negotiation

    MII\_BMCR\_DUPLEX\_MODE
    :   full duplex mode

    MII\_BMCR\_SPEED\_MSB
    :   10=1000Mbps 01=100Mbps; 00=10Mbps

    MII\_BMCR\_SPEED\_MASK
    :   Link Speed Field.

    MII\_BMCR\_SPEED\_10
    :   select speed 10 Mb/s

    MII\_BMCR\_SPEED\_100
    :   select speed 100 Mb/s

    MII\_BMCR\_SPEED\_1000
    :   select speed 1000 Mb/s

    MII\_BMSR\_100BASE\_T4
    :   100BASE-T4 capable

    MII\_BMSR\_100BASE\_X\_FULL
    :   100BASE-X full duplex capable

    MII\_BMSR\_100BASE\_X\_HALF
    :   100BASE-X half duplex capable

    MII\_BMSR\_10\_FULL
    :   10 Mb/s full duplex capable

    MII\_BMSR\_10\_HALF
    :   10 Mb/s half duplex capable

    MII\_BMSR\_100BASE\_T2\_FULL
    :   100BASE-T2 full duplex capable

    MII\_BMSR\_100BASE\_T2\_HALF
    :   100BASE-T2 half duplex capable

    MII\_BMSR\_EXTEND\_STATUS
    :   extend status information in reg 15

    MII\_BMSR\_MF\_PREAMB\_SUPPR
    :   PHY accepts management frames with preamble suppressed.

    MII\_BMSR\_AUTONEG\_COMPLETE
    :   Auto-negotiation process completed.

    MII\_BMSR\_REMOTE\_FAULT
    :   remote fault detected

    MII\_BMSR\_AUTONEG\_ABILITY
    :   PHY is able to perform Auto-Negotiation.

    MII\_BMSR\_LINK\_STATUS
    :   link is up

    MII\_BMSR\_JABBER\_DETECT
    :   jabber condition detected

    MII\_BMSR\_EXTEND\_CAPAB
    :   extended register capabilities

    MII\_ADVERTISE\_NEXT\_PAGE
    :   next page

    MII\_ADVERTISE\_LPACK
    :   link partner acknowledge response

    MII\_ADVERTISE\_REMOTE\_FAULT
    :   remote fault

    MII\_ADVERTISE\_ASYM\_PAUSE
    :   try for asymmetric pause

    MII\_ADVERTISE\_PAUSE
    :   try for pause

    MII\_ADVERTISE\_100BASE\_T4
    :   try for 100BASE-T4 support

    MII\_ADVERTISE\_100\_FULL
    :   try for 100BASE-X full duplex support

    MII\_ADVERTISE\_100\_HALF
    :   try for 100BASE-X support

    MII\_ADVERTISE\_10\_FULL
    :   try for 10 Mb/s full duplex support

    MII\_ADVERTISE\_10\_HALF
    :   try for 10 Mb/s half duplex support

    MII\_ADVERTISE\_SEL\_MASK
    :   Selector Field Mask.

    MII\_ADVERTISE\_SEL\_IEEE\_802\_3
    :   Selector Field.

    MII\_ADVERTISE\_1000\_FULL
    :   try for 1000BASE-T full duplex support

    MII\_ADVERTISE\_1000\_HALF
    :   try for 1000BASE-T half duplex support

    MII\_ADVERTISE\_ALL
    :   Advertise all speeds.

    MII\_ESTAT\_1000BASE\_X\_FULL
    :   1000BASE-X full-duplex capable

    MII\_ESTAT\_1000BASE\_X\_HALF
    :   1000BASE-X half-duplex capable

    MII\_ESTAT\_1000BASE\_T\_FULL
    :   1000BASE-T full-duplex capable

    MII\_ESTAT\_1000BASE\_T\_HALF
    :   1000BASE-T half-duplex capable
