---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ethernet_8h.html
original_path: doxygen/html/ethernet_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ethernet.h File Reference

Ethernet.
[More...](#details)

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[zephyr/sys/atomic.h](sys_2atomic_8h_source.md)>`  
`#include <[zephyr/net/net_ip.h](net__ip_8h_source.md)>`  
`#include <[zephyr/net/net_pkt.h](net__pkt_8h_source.md)>`  
`#include <[zephyr/net/lldp.h](lldp_8h_source.md)>`  
`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`  
`#include <[zephyr/net/net_if.h](net__if_8h_source.md)>`  
`#include <[zephyr/net/ethernet_vlan.h](ethernet__vlan_8h_source.md)>`  
`#include <[zephyr/net/ptp_time.h](ptp__time_8h_source.md)>`  
`#include <zephyr/syscalls/ethernet.h>`

[Go to the source code of this file.](ethernet_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [net\_eth\_addr](structnet__eth__addr.md) |
|  | Ethernet address. [More...](structnet__eth__addr.md#details) |
| struct | [ethernet\_t1s\_param](structethernet__t1s__param.md) |
|  | Ethernet T1S specific parameters. [More...](structethernet__t1s__param.md#details) |
| struct | [ethernet\_qav\_param](structethernet__qav__param.md) |
|  | Ethernet Qav specific parameters. [More...](structethernet__qav__param.md#details) |
| struct | [ethernet\_qbv\_param](structethernet__qbv__param.md) |
|  | Ethernet Qbv specific parameters. [More...](structethernet__qbv__param.md#details) |
| struct | [ethernet\_qbu\_param](structethernet__qbu__param.md) |
|  | Ethernet Qbu specific parameters. [More...](structethernet__qbu__param.md#details) |
| struct | [ethernet\_filter](structethernet__filter.md) |
|  | Ethernet filter description. [More...](structethernet__filter.md#details) |
| struct | [ethernet\_txtime\_param](structethernet__txtime__param.md) |
|  | Ethernet TXTIME specific parameters. [More...](structethernet__txtime__param.md#details) |
| struct | [ethernet\_api](structethernet__api.md) |
|  | Ethernet L2 API operations. [More...](structethernet__api.md#details) |
| struct | [ethernet\_lldp](structethernet__lldp.md) |
|  | Ethernet LLDP specific parameters. [More...](structethernet__lldp.md#details) |

| Macros | |
| --- | --- |
| #define | [NET\_ETH\_ADDR\_LEN](group__ethernet.md#ga399425f810c00bcf9babec019bc2ff12)   6U |
|  | Ethernet MAC address length. |
| #define | [NET\_ETH\_MINIMAL\_FRAME\_SIZE](group__ethernet.md#ga4cc1bb4cfa00b7749838eae3ae11048c)   60 |
|  | Minimum Ethernet frame size. |
| #define | [NET\_ETH\_MTU](group__ethernet.md#gaa337199b1edc50c9003afa5c3a951d8b)   1500 |
|  | Ethernet MTU size. |
| #define | [ETH\_NET\_DEVICE\_INIT](group__ethernet.md#ga197e02748be8eaf410f7deb57c984642)(dev\_id, name, init\_fn, pm, data, config, prio, api, mtu) |
|  | Create an Ethernet network interface and bind it to network device. |
| #define | [ETH\_NET\_DEVICE\_INIT\_INSTANCE](group__ethernet.md#ga3dc27a54b7ae178e8c4daeba4c84aab0)(dev\_id, name, instance, init\_fn, pm, data, config, prio, api, mtu) |
|  | Create multiple Ethernet network interfaces and bind them to network devices. |
| #define | [ETH\_NET\_DEVICE\_DT\_DEFINE](group__ethernet.md#ga9f67fee695953f24b1e5d9e49041aa99)(node\_id, init\_fn, pm, data, config, prio, api, mtu) |
|  | Like ETH\_NET\_DEVICE\_INIT but taking metadata from a devicetree. |
| #define | [ETH\_NET\_DEVICE\_DT\_INST\_DEFINE](group__ethernet.md#gaecf9f102108836ed9cf7e2cdb3c90579)(inst, ...) |
|  | Like ETH\_NET\_DEVICE\_DT\_DEFINE for an instance of a DT\_DRV\_COMPAT compatible. |
| #define | [ETH\_NET\_L3\_REGISTER](group__ethernet.md#gaf6524602e433313c15ea2cef762ff0dc)(name, ptype, handler) |
|  | Ethernet L3 protocol register macro. |

| Enumerations | |
| --- | --- |
| enum | [ethernet\_hw\_caps](group__ethernet.md#ga9162ff11d626813fc840df0b67820ac5) {     [ETHERNET\_HW\_TX\_CHKSUM\_OFFLOAD](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5aefaa7e72a676d6b1ad570a96be1a3861) = BIT(0) , [ETHERNET\_HW\_RX\_CHKSUM\_OFFLOAD](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a8341893ee775dca3609ce1316d948e33) = BIT(1) , [ETHERNET\_HW\_VLAN](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a0bdf56b7f06fa68125bce800f9adfb95) = BIT(2) , [ETHERNET\_AUTO\_NEGOTIATION\_SET](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a93c074b73420abed7d1f59f231da990a) = BIT(3) ,     [ETHERNET\_LINK\_10BASE\_T](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a26084acbb9f8c65fdb427c7d8b9b4fb6) = BIT(4) , [ETHERNET\_LINK\_100BASE\_T](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a6fc62894c7ebe8697f1c45f4fc54ed3e) = BIT(5) , [ETHERNET\_LINK\_1000BASE\_T](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a885ef0a35e462efa43e59c2f625964b8) = BIT(6) , [ETHERNET\_DUPLEX\_SET](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a1e37eeba16e05b12580e5eacd36a25cc) = BIT(7) ,     [ETHERNET\_PTP](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a604198d571bf2c4e7227bdeaefc2868a) = BIT(8) , [ETHERNET\_QAV](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a7ec920ceb8cfba6424040079d6eeef42) = BIT(9) , [ETHERNET\_PROMISC\_MODE](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5ad040f4a5749f66a377b840a4da8fb64d) = BIT(10) , [ETHERNET\_PRIORITY\_QUEUES](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a1e32518640964a73d4154ed8bc527475) = BIT(11) ,     [ETHERNET\_HW\_FILTERING](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a50d1e4418926b586f6b50acd828f57fe) = BIT(12) , [ETHERNET\_LLDP](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a8da4ebc3e888ac358f88aa9671e732c2) = BIT(13) , [ETHERNET\_HW\_VLAN\_TAG\_STRIP](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a1f33c56862228a647b583ae7e0605ac5) = BIT(14) , [ETHERNET\_DSA\_SLAVE\_PORT](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a77fe3d1049f9295102f3f2863df84dd7) = BIT(15) ,     [ETHERNET\_DSA\_MASTER\_PORT](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a762faf9045477a959e9ec11ce099a883) = BIT(16) , [ETHERNET\_QBV](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5acf17cbf803c3a0fe858ef939ccfe3b85) = BIT(17) , [ETHERNET\_QBU](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a68e30ff24a3eb75def8e154ac00dea08) = BIT(18) , [ETHERNET\_TXTIME](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5ac72ff66c3172da29ec9fefad7593ffd2) = BIT(19) ,     [ETHERNET\_TXINJECTION\_MODE](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a785ca3331fc7e92526d7c0faef34bd8b) = BIT(20) , [ETHERNET\_LINK\_2500BASE\_T](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a68df8dcd314f5d0fb1c488aa13e868fb) = BIT(21) , [ETHERNET\_LINK\_5000BASE\_T](group__ethernet.md#gga9162ff11d626813fc840df0b67820ac5a9e8239e72e66276f194864f292268b9b) = BIT(22)   } |
|  | Ethernet hardware capabilities. [More...](group__ethernet.md#ga9162ff11d626813fc840df0b67820ac5) |
| enum | [ethernet\_if\_types](group__ethernet.md#ga139cc696837611a522b289f2ea7bf6fc) { [L2\_ETH\_IF\_TYPE\_ETHERNET](group__ethernet.md#gga139cc696837611a522b289f2ea7bf6fca25c90e15f09a19a8ca7d0ea9d1836530) , [L2\_ETH\_IF\_TYPE\_WIFI](group__ethernet.md#gga139cc696837611a522b289f2ea7bf6fca32862b06ca0a77a8cf66d167c4496671) } |
|  | Types of Ethernet L2. [More...](group__ethernet.md#ga139cc696837611a522b289f2ea7bf6fc) |
| enum | [ethernet\_checksum\_support](group__ethernet.md#gabf86b7f09a9d041eea25357cd7a85ede) {     [ETHERNET\_CHECKSUM\_SUPPORT\_NONE](group__ethernet.md#ggabf86b7f09a9d041eea25357cd7a85edea90314c44dca3c123d1a0bd70f108524d) = NET\_IF\_CHECKSUM\_NONE\_BIT , [ETHERNET\_CHECKSUM\_SUPPORT\_IPV4\_HEADER](group__ethernet.md#ggabf86b7f09a9d041eea25357cd7a85edea6485d2abcd3dae6786022aa286234ed4) = NET\_IF\_CHECKSUM\_IPV4\_HEADER\_BIT , [ETHERNET\_CHECKSUM\_SUPPORT\_IPV4\_ICMP](group__ethernet.md#ggabf86b7f09a9d041eea25357cd7a85edea5671ade139cb0cd28d02e3215337acb9) = NET\_IF\_CHECKSUM\_IPV4\_ICMP\_BIT , [ETHERNET\_CHECKSUM\_SUPPORT\_IPV6\_HEADER](group__ethernet.md#ggabf86b7f09a9d041eea25357cd7a85edea557127c3bc97969fe57fcd8ac55567b5) = NET\_IF\_CHECKSUM\_IPV6\_HEADER\_BIT ,     [ETHERNET\_CHECKSUM\_SUPPORT\_IPV6\_ICMP](group__ethernet.md#ggabf86b7f09a9d041eea25357cd7a85edeac64b392a0591cfe7aa5564a476fe20be) = NET\_IF\_CHECKSUM\_IPV6\_ICMP\_BIT , [ETHERNET\_CHECKSUM\_SUPPORT\_TCP](group__ethernet.md#ggabf86b7f09a9d041eea25357cd7a85edea3346f0e3d0b350c7fe663cfe389c1e02) = NET\_IF\_CHECKSUM\_TCP\_BIT , [ETHERNET\_CHECKSUM\_SUPPORT\_UDP](group__ethernet.md#ggabf86b7f09a9d041eea25357cd7a85edea03e31130ecef7ac032bceed6f3091af8) = NET\_IF\_CHECKSUM\_UDP\_BIT   } |
|  | Protocols that are supported by checksum offloading. [More...](group__ethernet.md#gabf86b7f09a9d041eea25357cd7a85ede) |

| Functions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_eth\_is\_addr\_broadcast](group__ethernet.md#ga76a5fe39ce12478c666d87f4aec3d579) (struct [net\_eth\_addr](structnet__eth__addr.md) \*addr) |
|  | Check if the Ethernet MAC address is a broadcast address. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_eth\_is\_addr\_all\_zeroes](group__ethernet.md#ga237aab2d07ffa84355981d02a4576ebe) (struct [net\_eth\_addr](structnet__eth__addr.md) \*addr) |
|  | Check if the Ethernet MAC address is a all zeroes address. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_eth\_is\_addr\_unspecified](group__ethernet.md#ga89964de263029223d119f361fbd94bfd) (struct [net\_eth\_addr](structnet__eth__addr.md) \*addr) |
|  | Check if the Ethernet MAC address is unspecified. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_eth\_is\_addr\_multicast](group__ethernet.md#ga2755ecb84e9759c24302e33a56a1fc84) (struct [net\_eth\_addr](structnet__eth__addr.md) \*addr) |
|  | Check if the Ethernet MAC address is a multicast address. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_eth\_is\_addr\_group](group__ethernet.md#ga82ad9574acb697c26a9aa11316867d3c) (struct [net\_eth\_addr](structnet__eth__addr.md) \*addr) |
|  | Check if the Ethernet MAC address is a group address. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_eth\_is\_addr\_valid](group__ethernet.md#gaf20472f9d60e5cddffed2919b3091030) (struct [net\_eth\_addr](structnet__eth__addr.md) \*addr) |
|  | Check if the Ethernet MAC address is valid. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_eth\_is\_addr\_lldp\_multicast](group__ethernet.md#gaec6fb3c05792bdd30596137686f3251a) (struct [net\_eth\_addr](structnet__eth__addr.md) \*addr) |
|  | Check if the Ethernet MAC address is a LLDP multicast address. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_eth\_is\_addr\_ptp\_multicast](group__ethernet.md#gaeddfa5b3ff6e356393114b351f87fe43) (struct [net\_eth\_addr](structnet__eth__addr.md) \*addr) |
|  | Check if the Ethernet MAC address is a PTP multicast address. |
| const struct [net\_eth\_addr](structnet__eth__addr.md) \* | [net\_eth\_broadcast\_addr](group__ethernet.md#gae66b24a847f8e0ad119c6c466331afd6) (void) |
|  | Return Ethernet broadcast address. |
| void | [net\_eth\_ipv4\_mcast\_to\_mac\_addr](group__ethernet.md#gae3ce2bd669391071635f5709d1c3cd8e) (const struct [in\_addr](structin__addr.md) \*ipv4\_addr, struct [net\_eth\_addr](structnet__eth__addr.md) \*mac\_addr) |
|  | Convert IPv4 multicast address to Ethernet address. |
| void | [net\_eth\_ipv6\_mcast\_to\_mac\_addr](group__ethernet.md#gaa08d5237c26e8c05748d58eb65b15c2f) (const struct [in6\_addr](structin6__addr.md) \*ipv6\_addr, struct [net\_eth\_addr](structnet__eth__addr.md) \*mac\_addr) |
|  | Convert IPv6 multicast address to Ethernet address. |
| static enum [ethernet\_hw\_caps](group__ethernet.md#ga9162ff11d626813fc840df0b67820ac5) | [net\_eth\_get\_hw\_capabilities](group__ethernet.md#gab0a3b4584bb6ce1d27b98b063fd3fcbd) (struct [net\_if](structnet__if.md) \*iface) |
|  | Return ethernet device hardware capability information. |
| static int | [net\_eth\_get\_hw\_config](group__ethernet.md#ga1246be489eb7130100bbaebbb73961c5) (struct [net\_if](structnet__if.md) \*iface, enum ethernet\_config\_type type, struct ethernet\_config \*config) |
|  | Return ethernet device hardware configuration information. |
| static int | [net\_eth\_vlan\_enable](group__ethernet.md#ga16cbc14e3a0a470bbbd5aeb5e73dc1de) (struct [net\_if](structnet__if.md) \*iface, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag) |
|  | Add VLAN tag to the interface. |
| static int | [net\_eth\_vlan\_disable](group__ethernet.md#gab71a741cea5f645f4354a1abc9c95a50) (struct [net\_if](structnet__if.md) \*iface, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag) |
|  | Remove VLAN tag from the interface. |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_eth\_get\_vlan\_tag](group__ethernet.md#ga6184c43a62e4af9958412f99991358c9) (struct [net\_if](structnet__if.md) \*iface) |
|  | Return VLAN tag specified to network interface. |
| static struct [net\_if](structnet__if.md) \* | [net\_eth\_get\_vlan\_iface](group__ethernet.md#gad9d890dcf7f5ee3659bf3bd5949faa4e) (struct [net\_if](structnet__if.md) \*iface, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag) |
|  | Return network interface related to this VLAN tag. |
| static struct [net\_if](structnet__if.md) \* | [net\_eth\_get\_vlan\_main](group__ethernet.md#ga010a95a0239a800131ac3d43dd54737f) (struct [net\_if](structnet__if.md) \*iface) |
|  | Return main network interface that is attached to this VLAN tag. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_eth\_is\_vlan\_enabled](group__ethernet.md#gac536aa7154c4a8d194ec67efb68e275c) (struct ethernet\_context \*ctx, struct [net\_if](structnet__if.md) \*iface) |
|  | Check if there are any VLAN interfaces enabled to this specific Ethernet network interface. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_eth\_get\_vlan\_status](group__ethernet.md#ga78aad58ec66710034cab8891ad638a2c) (struct [net\_if](structnet__if.md) \*iface) |
|  | Get VLAN status for a given network interface (enabled or not). |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_eth\_is\_vlan\_interface](group__ethernet.md#ga8ca1eccc88a351241298d358ec28fdf5) (struct [net\_if](structnet__if.md) \*iface) |
|  | Check if the given interface is a VLAN interface. |
| void | [net\_eth\_carrier\_on](group__ethernet.md#gabeb21cb06b18674b73fbd0f42ee726f0) (struct [net\_if](structnet__if.md) \*iface) |
|  | Inform ethernet L2 driver that ethernet carrier is detected. |
| void | [net\_eth\_carrier\_off](group__ethernet.md#ga4dcf5047108b509e349b02fe35c10d75) (struct [net\_if](structnet__if.md) \*iface) |
|  | Inform ethernet L2 driver that ethernet carrier was lost. |
| int | [net\_eth\_promisc\_mode](group__ethernet.md#ga42a3c6b04ef8827e3443c5aebe5541b9) (struct [net\_if](structnet__if.md) \*iface, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Set promiscuous mode either ON or OFF. |
| int | [net\_eth\_txinjection\_mode](group__ethernet.md#gafbb76d53f9f80628d18d39368a28f984) (struct [net\_if](structnet__if.md) \*iface, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Set TX-Injection mode either ON or OFF. |
| int | [net\_eth\_mac\_filter](group__ethernet.md#ga920bddac077675d544a21fb5650c945e) (struct [net\_if](structnet__if.md) \*iface, struct [net\_eth\_addr](structnet__eth__addr.md) \*mac, enum ethernet\_filter\_type type, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Set or unset HW filtering for MAC address `mac`. |
| const struct [device](structdevice.md) \* | [net\_eth\_get\_phy](group__ethernet.md#ga7225d06fbaa12d4668fa165d9e8f0845) (struct [net\_if](structnet__if.md) \*iface) |
|  | Return the PHY device that is tied to this ethernet network interface. |
| static const struct [device](structdevice.md) \* | [net\_eth\_get\_ptp\_clock](group__ethernet.md#ga37ff48434c56bbb24422dd805449b6f3) (struct [net\_if](structnet__if.md) \*iface) |
|  | Return PTP clock that is tied to this ethernet network interface. |
| const struct [device](structdevice.md) \* | [net\_eth\_get\_ptp\_clock\_by\_index](group__ethernet.md#ga84c37db5687c5264bec99976a1108ab6) (int index) |
|  | Return PTP clock that is tied to this ethernet network interface index. |
| static int | [net\_eth\_get\_ptp\_port](group__ethernet.md#ga37c5d1d5d534c6d024b060ae54bbd82a) (struct [net\_if](structnet__if.md) \*iface) |
|  | Return PTP port number attached to this interface. |
| static void | [net\_eth\_set\_ptp\_port](group__ethernet.md#ga1424a7e54b8b439b7000dfb23f825231) (struct [net\_if](structnet__if.md) \*iface, int port) |
|  | Set PTP port number attached to this interface. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_eth\_type\_is\_wifi](group__ethernet.md#ga6e603f6f74e6d7e988e7119a6df2ab4d) (struct [net\_if](structnet__if.md) \*iface) |
|  | Check if the Ethernet L2 network interface can perform Wi-Fi. |

## Detailed Description

Ethernet.

This is not to be included by the application.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [ethernet.h](ethernet_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
