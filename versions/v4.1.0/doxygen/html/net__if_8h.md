---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/net__if_8h.html
original_path: doxygen/html/net__if_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_if.h File Reference

Public API for network interface.
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`  
`#include <[zephyr/net/net_core.h](net__core_8h_source.md)>`  
`#include <[zephyr/net/hostname.h](hostname_8h_source.md)>`  
`#include <[zephyr/net/net_linkaddr.h](net__linkaddr_8h_source.md)>`  
`#include <[zephyr/net/net_ip.h](net__ip_8h_source.md)>`  
`#include <[zephyr/net/net_l2.h](net__l2_8h_source.md)>`  
`#include <[zephyr/net/net_stats.h](net__stats_8h_source.md)>`  
`#include <[zephyr/net/net_timeout.h](net__timeout_8h_source.md)>`  
`#include <[zephyr/net/prometheus/collector.h](collector_8h_source.md)>`  
`#include <zephyr/syscalls/net_if.h>`

[Go to the source code of this file.](net__if_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [net\_if\_addr](structnet__if__addr.md) |
|  | Network Interface unicast IP addresses. [More...](structnet__if__addr.md#details) |
| struct | [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) |
|  | Network Interface multicast IP addresses. [More...](structnet__if__mcast__addr.md#details) |
| struct | [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) |
|  | Network Interface IPv6 prefixes. [More...](structnet__if__ipv6__prefix.md#details) |
| struct | [net\_if\_router](structnet__if__router.md) |
|  | Information about routers in the system. [More...](structnet__if__router.md#details) |
| struct | [net\_if\_ipv6](structnet__if__ipv6.md) |
|  | IPv6 configuration. [More...](structnet__if__ipv6.md#details) |
| struct | [net\_if\_addr\_ipv4](structnet__if__addr__ipv4.md) |
|  | Network Interface unicast IPv4 address and netmask. [More...](structnet__if__addr__ipv4.md#details) |
| struct | [net\_if\_ipv4](structnet__if__ipv4.md) |
|  | IPv4 configuration. [More...](structnet__if__ipv4.md#details) |
| struct | [net\_if\_ip](structnet__if__ip.md) |
|  | Network interface IP address configuration. [More...](structnet__if__ip.md#details) |
| struct | [net\_if\_config](structnet__if__config.md) |
|  | IP and other configuration related data for network interface. [More...](structnet__if__config.md#details) |
| struct | [net\_traffic\_class](structnet__traffic__class.md) |
|  | Network traffic class. [More...](structnet__traffic__class.md#details) |
| struct | [net\_if\_dev](structnet__if__dev.md) |
|  | Network Interface Device structure. [More...](structnet__if__dev.md#details) |
| struct | [net\_if](structnet__if.md) |
|  | Network Interface structure. [More...](structnet__if.md#details) |
| struct | [net\_if\_mcast\_monitor](structnet__if__mcast__monitor.md) |
|  | Multicast monitor handler struct. [More...](structnet__if__mcast__monitor.md#details) |
| struct | [net\_if\_link\_cb](structnet__if__link__cb.md) |
|  | Link callback handler struct. [More...](structnet__if__link__cb.md#details) |

| Macros | |
| --- | --- |
| #define | [NET\_DEVICE\_INIT](group__net__if.md#ga02971562c42494e2a5f71e1f8587e709)(dev\_id, name, init\_fn, pm, data, config, prio, api, l2, l2\_ctx\_type, mtu) |
|  | Create a network interface and bind it to network device. |
| #define | [NET\_DEVICE\_DT\_DEFINE](group__net__if.md#gab1f762b01ae7bc37cd4a25724c123dda)(node\_id, init\_fn, pm, data, config, prio, api, l2, l2\_ctx\_type, mtu) |
|  | Like NET\_DEVICE\_INIT but taking metadata from a devicetree node. |
| #define | [NET\_DEVICE\_DT\_INST\_DEFINE](group__net__if.md#ga7edd8bc59444d92cad0371c36f9949b7)(inst, ...) |
|  | Like NET\_DEVICE\_DT\_DEFINE for an instance of a DT\_DRV\_COMPAT compatible. |
| #define | [NET\_DEVICE\_INIT\_INSTANCE](group__net__if.md#gacc7edecdd9de9920cc155977d8fec2a2)(dev\_id, name, instance, init\_fn, pm, data, config, prio, api, l2, l2\_ctx\_type, mtu) |
|  | Create multiple network interfaces and bind them to network device. |
| #define | [NET\_DEVICE\_DT\_DEFINE\_INSTANCE](group__net__if.md#ga50702b043a0791e59e7d5679dda1d9e8)(node\_id, instance, init\_fn, pm, data, config, prio, api, l2, l2\_ctx\_type, mtu) |
|  | Like NET\_DEVICE\_OFFLOAD\_INIT but taking metadata from a devicetree. |
| #define | [NET\_DEVICE\_DT\_INST\_DEFINE\_INSTANCE](group__net__if.md#gabe4b8589996a53cbc50b76c8ea15aa0c)(inst, ...) |
|  | Like NET\_DEVICE\_DT\_DEFINE\_INSTANCE for an instance of a DT\_DRV\_COMPAT compatible. |
| #define | [NET\_DEVICE\_OFFLOAD\_INIT](group__net__if.md#ga255672607b7958db3f464d2a57a7e635)(dev\_id, name, init\_fn, pm, data, config, prio, api, mtu) |
|  | Create a offloaded network interface and bind it to network device. |
| #define | [NET\_DEVICE\_DT\_OFFLOAD\_DEFINE](group__net__if.md#gab2b287025e194dec1fab24e44d95362f)(node\_id, init\_fn, pm, data, config, prio, api, mtu) |
|  | Like NET\_DEVICE\_OFFLOAD\_INIT but taking metadata from a devicetree node. |
| #define | [NET\_DEVICE\_DT\_INST\_OFFLOAD\_DEFINE](group__net__if.md#ga1cab6943a28e3d3754e36623834b93fd)(inst, ...) |
|  | Like NET\_DEVICE\_DT\_OFFLOAD\_DEFINE for an instance of a DT\_DRV\_COMPAT compatible. |
| #define | [NET\_IFACE\_COUNT](group__net__if.md#ga6c081875a6f5a848b3ad2fd220c63c3c)(\_dst) |
|  | Count the number of network interfaces. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [net\_socket\_create\_t](group__net__if.md#gaef3dfe26195514aac625e9f22e399759)) (int, int, int) |
|  | A function prototype to create an offloaded socket. |
| typedef void(\* | [net\_if\_ip\_addr\_cb\_t](group__net__if.md#gab58d8561a4f21899e2db34043d346516)) (struct [net\_if](structnet__if.md) \*iface, struct [net\_if\_addr](structnet__if__addr.md) \*addr, void \*user\_data) |
|  | Callback used while iterating over network interface IP addresses. |
| typedef void(\* | [net\_if\_ip\_maddr\_cb\_t](group__net__if.md#ga726eed76563c223de8f611e2544febe9)) (struct [net\_if](structnet__if.md) \*iface, struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*maddr, void \*user\_data) |
|  | Callback used while iterating over network interface multicast IP addresses. |
| typedef void(\* | [net\_if\_mcast\_callback\_t](group__net__if.md#ga0d64291573740a67eae7ff3fcc0910c5)) (struct [net\_if](structnet__if.md) \*iface, const struct net\_addr \*addr, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) is\_joined) |
|  | Define a callback that is called whenever a IPv6 or IPv4 multicast address group is joined or left. |
| typedef void(\* | [net\_if\_link\_callback\_t](group__net__if.md#ga0f87d5753fcd7cce40ecd161e6c91078)) (struct [net\_if](structnet__if.md) \*iface, struct [net\_linkaddr](structnet__linkaddr.md) \*dst, int status) |
|  | Define callback that is called after a network packet has been sent. |
| typedef void(\* | [net\_if\_cb\_t](group__net__if.md#gac48ab8e6337e7cf387af9b293f254a80)) (struct [net\_if](structnet__if.md) \*iface, void \*user\_data) |
|  | Callback used while iterating over network interfaces. |

| Enumerations | |
| --- | --- |
| enum | [net\_if\_flag](group__net__if.md#gae691e5537917ffce27ad0db82c730371) {     [NET\_IF\_UP](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ab0ab7393d643354c46c3437d74c15840) , [NET\_IF\_POINTOPOINT](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a3256ef2d537c85b4c2b33b92935e1009) , [NET\_IF\_PROMISC](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a700d92a5b0de3c779e59806137b35141) , [NET\_IF\_NO\_AUTO\_START](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a0babb762301878eaf8ef8a05213ecf05) ,     [NET\_IF\_SUSPENDED](group__net__if.md#ggae691e5537917ffce27ad0db82c730371aaaeafc62e61ec120609205770c8b54f0) , [NET\_IF\_FORWARD\_MULTICASTS](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a581971c9d93a910c4c607da45aa2e4ac) , [NET\_IF\_IPV4](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a67d2c0fe390ab16f347ee2dc0a056329) , [NET\_IF\_IPV6](group__net__if.md#ggae691e5537917ffce27ad0db82c730371aab31a9e1e8c02159f45efc4e0455a4d6) ,     [NET\_IF\_RUNNING](group__net__if.md#ggae691e5537917ffce27ad0db82c730371add3e2ecdcd5de3154f9bd2836428a25a) , [NET\_IF\_LOWER\_UP](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ab1a529826bad6b4bcd04185372f97d6d) , [NET\_IF\_DORMANT](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a7dd1db72a37b1fbc4c4491ce1c75238d) , [NET\_IF\_IPV6\_NO\_ND](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a542ecce860ef3bf2df493da8d4c6a2f7) ,     [NET\_IF\_IPV6\_NO\_MLD](group__net__if.md#ggae691e5537917ffce27ad0db82c730371a1d362cfabb58eb220ddb069431221fbe) , [NET\_IF\_NO\_TX\_LOCK](group__net__if.md#ggae691e5537917ffce27ad0db82c730371ae8d564e1577c8daad8ce50a729c500c9)   } |
|  | Network interface flags. [More...](group__net__if.md#gae691e5537917ffce27ad0db82c730371) |
| enum | [net\_if\_oper\_state](group__net__if.md#gadfe9d90f24046cd9bd4bbee096e747b9) {     [NET\_IF\_OPER\_UNKNOWN](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9ac7cae092ea6ceeb62499a9b435ac4b58) , [NET\_IF\_OPER\_NOTPRESENT](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a8f9f55840e75693163197baae9d50c32) , [NET\_IF\_OPER\_DOWN](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9adb20a95215310c420f8dae7e17a2f367) , [NET\_IF\_OPER\_LOWERLAYERDOWN](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9ae7e9b8b12ae618a5ee1483dee916aab4) ,     [NET\_IF\_OPER\_TESTING](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a2240173b5c247ab5eb0a9a6afafb296f) , [NET\_IF\_OPER\_DORMANT](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a5cbe2aa27a444444d4acf122113d430d) , [NET\_IF\_OPER\_UP](group__net__if.md#ggadfe9d90f24046cd9bd4bbee096e747b9a6b99bfc28d831292029761d74209ee03)   } |
|  | Network interface operational status (RFC 2863). [More...](group__net__if.md#gadfe9d90f24046cd9bd4bbee096e747b9) |
| enum | [net\_if\_checksum\_type](group__net__if.md#ga8db412ae79c64cafe81a66f5acb2f8e9) {     [NET\_IF\_CHECKSUM\_IPV4\_HEADER](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9a75e4a0946d0e6755ebd7cc62558aee30) = NET\_IF\_CHECKSUM\_IPV4\_HEADER\_BIT , [NET\_IF\_CHECKSUM\_IPV4\_TCP](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9aaed32a3cb700eac3b67c6c7e5a0cd0ad) , [NET\_IF\_CHECKSUM\_IPV4\_UDP](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9afe1eaaa765c8ec3c61618e943cd3f1c3) , [NET\_IF\_CHECKSUM\_IPV4\_ICMP](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9a2aef87c97f22fdccdf1925d2687436b1) = NET\_IF\_CHECKSUM\_IPV4\_ICMP\_BIT ,     [NET\_IF\_CHECKSUM\_IPV6\_HEADER](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9ab204c7d5fddbd2c11e07a8831df6c00b) = NET\_IF\_CHECKSUM\_IPV6\_HEADER\_BIT , [NET\_IF\_CHECKSUM\_IPV6\_TCP](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9a31e33593e4e7f7f9b36e319e0991ab13) , [NET\_IF\_CHECKSUM\_IPV6\_UDP](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9a70b1272e2125cea9204bae144fd86660) , [NET\_IF\_CHECKSUM\_IPV6\_ICMP](group__net__if.md#gga8db412ae79c64cafe81a66f5acb2f8e9af5b3bc7cb5e9771cd9fd57d9fda4c3b3) = NET\_IF\_CHECKSUM\_IPV6\_ICMP\_BIT   } |
|  | Type of checksum for which support in the interface will be queried. [More...](group__net__if.md#ga8db412ae79c64cafe81a66f5acb2f8e9) |

| Functions | |
| --- | --- |
| static void | [net\_if\_flag\_set](group__net__if.md#ga52f9fca13e9f836799e0e40f581744d2) (struct [net\_if](structnet__if.md) \*iface, enum [net\_if\_flag](group__net__if.md#gae691e5537917ffce27ad0db82c730371) value) |
|  | Set a value in network interface flags. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_flag\_test\_and\_set](group__net__if.md#ga42e7482191a92007960601f8bb621dca) (struct [net\_if](structnet__if.md) \*iface, enum [net\_if\_flag](group__net__if.md#gae691e5537917ffce27ad0db82c730371) value) |
|  | Test and set a value in network interface flags. |
| static void | [net\_if\_flag\_clear](group__net__if.md#gaff751b6a92b0c608ecfc50e8c0587fd3) (struct [net\_if](structnet__if.md) \*iface, enum [net\_if\_flag](group__net__if.md#gae691e5537917ffce27ad0db82c730371) value) |
|  | Clear a value in network interface flags. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_flag\_test\_and\_clear](group__net__if.md#gab8f371c7f8890cf4728177f6595141d7) (struct [net\_if](structnet__if.md) \*iface, enum [net\_if\_flag](group__net__if.md#gae691e5537917ffce27ad0db82c730371) value) |
|  | Test and clear a value in network interface flags. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_flag\_is\_set](group__net__if.md#gae1f373ddd61c18a81481d8ddcfb12543) (struct [net\_if](structnet__if.md) \*iface, enum [net\_if\_flag](group__net__if.md#gae691e5537917ffce27ad0db82c730371) value) |
|  | Check if a value in network interface flags is set. |
| static enum [net\_if\_oper\_state](group__net__if.md#gadfe9d90f24046cd9bd4bbee096e747b9) | [net\_if\_oper\_state\_set](group__net__if.md#ga1f1bf845e63cce02e2183889cc85d57e) (struct [net\_if](structnet__if.md) \*iface, enum [net\_if\_oper\_state](group__net__if.md#gadfe9d90f24046cd9bd4bbee096e747b9) oper\_state) |
|  | Set an operational state on an interface. |
| static enum [net\_if\_oper\_state](group__net__if.md#gadfe9d90f24046cd9bd4bbee096e747b9) | [net\_if\_oper\_state](group__net__if.md#gad9e957a4866b4566296ee39392fde0e4) (struct [net\_if](structnet__if.md) \*iface) |
|  | Get an operational state of an interface. |
| enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) | [net\_if\_send\_data](group__net__if.md#gada0398d757eab28d16a129692c309f4d) (struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | Send a packet through a net iface. |
| static const struct [net\_l2](structnet__l2.md) \* | [net\_if\_l2](group__net__if.md#gafa451f6118529d1d084704d00b2aae20) (struct [net\_if](structnet__if.md) \*iface) |
|  | Get a pointer to the interface L2. |
| enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) | [net\_if\_recv\_data](group__net__if.md#ga72ed21ca0cb220199f5a2070137c7fef) (struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | Input a packet through a net iface. |
| static void \* | [net\_if\_l2\_data](group__net__if.md#ga3cad2d51fc9cc225619585e06e252db0) (struct [net\_if](structnet__if.md) \*iface) |
|  | Get a pointer to the interface L2 private data. |
| static const struct [device](structdevice.md) \* | [net\_if\_get\_device](group__net__if.md#gaeb8c703f273bc07ae9bb7a0d8bfe6f3d) (struct [net\_if](structnet__if.md) \*iface) |
|  | Get an network interface's device. |
| void | [net\_if\_queue\_tx](group__net__if.md#ga56c4d37edcea540be09ebcdf97265aed) (struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | Queue a packet to the net interface TX queue. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_is\_ip\_offloaded](group__net__if.md#ga6bfa5f84a2127bbad27a0a3b319526a1) (struct [net\_if](structnet__if.md) \*iface) |
|  | Return the IP offload status. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_is\_offloaded](group__net__if.md#gaecedc93a6dab2c57fe686718ea4d78af) (struct [net\_if](structnet__if.md) \*iface) |
|  | Return offload status of a given network interface. |
| static struct net\_offload \* | [net\_if\_offload](group__net__if.md#ga520939e94620ca75475a71f153df6d4a) (struct [net\_if](structnet__if.md) \*iface) |
|  | Return the IP offload plugin. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_is\_socket\_offloaded](group__net__if.md#gaf308baf2241fa455b50b439b7fab3f1e) (struct [net\_if](structnet__if.md) \*iface) |
|  | Return the socket offload status. |
| static void | [net\_if\_socket\_offload\_set](group__net__if.md#ga9db52875580115c743b1f35cd6c46796) (struct [net\_if](structnet__if.md) \*iface, [net\_socket\_create\_t](group__net__if.md#gaef3dfe26195514aac625e9f22e399759) socket\_offload) |
|  | Set the function to create an offloaded socket. |
| static [net\_socket\_create\_t](group__net__if.md#gaef3dfe26195514aac625e9f22e399759) | [net\_if\_socket\_offload](group__net__if.md#gafb2bbaec96c4759d920b2866c0b3ef3a) (struct [net\_if](structnet__if.md) \*iface) |
|  | Return the function to create an offloaded socket. |
| static struct [net\_linkaddr](structnet__linkaddr.md) \* | [net\_if\_get\_link\_addr](group__net__if.md#ga467186e964bf721e14fed38392f21872) (struct [net\_if](structnet__if.md) \*iface) |
|  | Get an network interface's link address. |
| static struct [net\_if\_config](structnet__if__config.md) \* | [net\_if\_get\_config](group__net__if.md#gae271e0e4dcb031a83d9908e597a45048) (struct [net\_if](structnet__if.md) \*iface) |
|  | Return network configuration for this network interface. |
| static void | [net\_if\_start\_dad](group__net__if.md#ga9655c010ccbf989e9328271f5dbcc685) (struct [net\_if](structnet__if.md) \*iface) |
|  | Start duplicate address detection procedure. |
| void | [net\_if\_start\_rs](group__net__if.md#gab9bdb7f8a9eeed4d9b70965b8af82cb7) (struct [net\_if](structnet__if.md) \*iface) |
|  | Start neighbor discovery and send router solicitation message. |
| static void | [net\_if\_stop\_rs](group__net__if.md#gab0195bb2151a1ba722a0b11d81066988) (struct [net\_if](structnet__if.md) \*iface) |
|  | Stop neighbor discovery. |
| static void | [net\_if\_nbr\_reachability\_hint](group__net__if.md#ga51af469ff3d7d9f760d63a8a9c7be8b5) (struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*ipv6\_addr) |
|  | Provide a reachability hint for IPv6 Neighbor Discovery. |
| static int | [net\_if\_set\_link\_addr](group__net__if.md#ga52b41b2f8b7d3405338a0539542677a0) (struct [net\_if](structnet__if.md) \*iface, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len, enum [net\_link\_type](group__net__linkaddr.md#ga1312c2322bc4a4f1c3b76d6466806b24) type) |
|  | Set a network interface's link address. |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_if\_get\_mtu](group__net__if.md#gacddc98531c5748db5a34f5c3a3e96e86) (struct [net\_if](structnet__if.md) \*iface) |
|  | Get an network interface's MTU. |
| static void | [net\_if\_set\_mtu](group__net__if.md#ga76b140c6fc39b94ff4102e08e3a58e81) (struct [net\_if](structnet__if.md) \*iface, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mtu) |
|  | Set an network interface's MTU. |
| static void | [net\_if\_addr\_set\_lf](group__net__if.md#gae66f6e7bd31545e6161fcd4600fe5842) (struct [net\_if\_addr](structnet__if__addr.md) \*ifaddr, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) is\_infinite) |
|  | Set the infinite status of the network interface address. |
| struct [net\_if](structnet__if.md) \* | [net\_if\_get\_by\_link\_addr](group__net__if.md#ga1b058361dc9bcac7d842bb49846a0c79) (struct [net\_linkaddr](structnet__linkaddr.md) \*ll\_addr) |
|  | Get an interface according to link layer address. |
| struct [net\_if](structnet__if.md) \* | [net\_if\_lookup\_by\_dev](group__net__if.md#gadbb8be32caa896bdcdeee19425134827) (const struct [device](structdevice.md) \*dev) |
|  | Find an interface from it's related device. |
| static struct [net\_if\_config](structnet__if__config.md) \* | [net\_if\_config\_get](group__net__if.md#gae2323a72714e29836d8296dfc330f7fd) (struct [net\_if](structnet__if.md) \*iface) |
|  | Get network interface IP config. |
| void | [net\_if\_router\_rm](group__net__if.md#gadc87242eb7205362a308b3c4437bf76d) (struct [net\_if\_router](structnet__if__router.md) \*router) |
|  | Remove a router from the system. |
| void | [net\_if\_set\_default](group__net__if.md#ga0a1f27ec893e1af3c97f130be4616589) (struct [net\_if](structnet__if.md) \*iface) |
|  | Set the default network interface. |
| struct [net\_if](structnet__if.md) \* | [net\_if\_get\_default](group__net__if.md#ga55214771e462cbd4930ffa738813cb87) (void) |
|  | Get the default network interface. |
| struct [net\_if](structnet__if.md) \* | [net\_if\_get\_first\_by\_type](group__net__if.md#ga762337e8b66874a0fbf59bdbeba173f5) (const struct [net\_l2](structnet__l2.md) \*l2) |
|  | Get the first network interface according to its type. |
| struct [net\_if](structnet__if.md) \* | [net\_if\_get\_first\_up](group__net__if.md#ga03d8c6aebb1412382a9eec636c227238) (void) |
|  | Get the first network interface which is up. |
| int | [net\_if\_config\_ipv6\_get](group__net__if.md#ga56c9aef19bc9827d9ec96c00e10840fa) (struct [net\_if](structnet__if.md) \*iface, struct [net\_if\_ipv6](structnet__if__ipv6.md) \*\*ipv6) |
|  | Allocate network interface IPv6 config. |
| int | [net\_if\_config\_ipv6\_put](group__net__if.md#ga8af1400b354c42a64795cdb1a600ddd6) (struct [net\_if](structnet__if.md) \*iface) |
|  | Release network interface IPv6 config. |
| struct [net\_if\_addr](structnet__if__addr.md) \* | [net\_if\_ipv6\_addr\_lookup](group__net__if.md#ga13b5a26fc672d15697f99e85543184bb) (const struct [in6\_addr](structin6__addr.md) \*addr, struct [net\_if](structnet__if.md) \*\*iface) |
|  | Check if this IPv6 address belongs to one of the interfaces. |
| struct [net\_if\_addr](structnet__if__addr.md) \* | [net\_if\_ipv6\_addr\_lookup\_by\_iface](group__net__if.md#gab53eabb540a4487d83f27c8e319c736a) (struct [net\_if](structnet__if.md) \*iface, struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if this IPv6 address belongs to this specific interfaces. |
| int | [net\_if\_ipv6\_addr\_lookup\_by\_index](group__net__if.md#ga1527872e5285790d50028a183608ac02) (const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if this IPv6 address belongs to one of the interface indices. |
| struct [net\_if\_addr](structnet__if__addr.md) \* | [net\_if\_ipv6\_addr\_add](group__net__if.md#gae00484a7fe32671a4ca04ff525e640c6) (struct [net\_if](structnet__if.md) \*iface, struct [in6\_addr](structin6__addr.md) \*addr, enum [net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41) addr\_type, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) vlifetime) |
|  | Add a IPv6 address to an interface. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_ipv6\_addr\_add\_by\_index](group__net__if.md#ga980bffb649ed48775bdc6cb2a0caef15) (int index, struct [in6\_addr](structin6__addr.md) \*addr, enum [net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41) addr\_type, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) vlifetime) |
|  | Add a IPv6 address to an interface by index. |
| void | [net\_if\_ipv6\_addr\_update\_lifetime](group__net__if.md#gaef8a6752a201f81636c4ffc1ebba4a25) (struct [net\_if\_addr](structnet__if__addr.md) \*ifaddr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) vlifetime) |
|  | Update validity lifetime time of an IPv6 address. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_ipv6\_addr\_rm](group__net__if.md#ga614e1458fa28d26c26f447e9fbcc2cb7) (struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Remove an IPv6 address from an interface. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_ipv6\_addr\_rm\_by\_index](group__net__if.md#gac159e3b0fbf558d5fb09774141da7d6d) (int index, const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Remove an IPv6 address from an interface by index. |
| void | [net\_if\_ipv6\_addr\_foreach](group__net__if.md#ga5ac646ad7fda0fa48e78c15b4ca52d50) (struct [net\_if](structnet__if.md) \*iface, [net\_if\_ip\_addr\_cb\_t](group__net__if.md#gab58d8561a4f21899e2db34043d346516) cb, void \*user\_data) |
|  | Go through all IPv6 addresses on a network interface and call callback for each used address. |
| struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \* | [net\_if\_ipv6\_maddr\_add](group__net__if.md#ga7ae82a491193dfea9b92cb9cbaf26f98) (struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Add a IPv6 multicast address to an interface. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_ipv6\_maddr\_rm](group__net__if.md#gaf0ce126bb5019ff5f5ff0876b9712ad9) (struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Remove an IPv6 multicast address from an interface. |
| void | [net\_if\_ipv6\_maddr\_foreach](group__net__if.md#gab677496fb2e27be2df299a346e9c7132) (struct [net\_if](structnet__if.md) \*iface, [net\_if\_ip\_maddr\_cb\_t](group__net__if.md#ga726eed76563c223de8f611e2544febe9) cb, void \*user\_data) |
|  | Go through all IPv6 multicast addresses on a network interface and call callback for each used address. |
| struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \* | [net\_if\_ipv6\_maddr\_lookup](group__net__if.md#gadb4031153c4fef86110879befa6b9975) (const struct [in6\_addr](structin6__addr.md) \*addr, struct [net\_if](structnet__if.md) \*\*iface) |
|  | Check if this IPv6 multicast address belongs to a specific interface or one of the interfaces. |
| void | [net\_if\_mcast\_mon\_register](group__net__if.md#ga8fdd0665ed76db6055777e395ca60255) (struct [net\_if\_mcast\_monitor](structnet__if__mcast__monitor.md) \*mon, struct [net\_if](structnet__if.md) \*iface, [net\_if\_mcast\_callback\_t](group__net__if.md#ga0d64291573740a67eae7ff3fcc0910c5) cb) |
|  | Register a multicast monitor. |
| void | [net\_if\_mcast\_mon\_unregister](group__net__if.md#gad323732fe3d178a5dfdf0900e5cb5683) (struct [net\_if\_mcast\_monitor](structnet__if__mcast__monitor.md) \*mon) |
|  | Unregister a multicast monitor. |
| void | [net\_if\_mcast\_monitor](group__net__if.md#ga372ef131263269cd65586d87997df745) (struct [net\_if](structnet__if.md) \*iface, const struct net\_addr \*addr, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) is\_joined) |
|  | Call registered multicast monitors. |
| void | [net\_if\_ipv6\_maddr\_join](group__net__if.md#ga49dbc954015307222f176f4149829b76) (struct [net\_if](structnet__if.md) \*iface, struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*addr) |
|  | Mark a given multicast address to be joined. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_ipv6\_maddr\_is\_joined](group__net__if.md#gabe2c16a378a35a22d008bff9142e5449) (struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*addr) |
|  | Check if given multicast address is joined or not. |
| void | [net\_if\_ipv6\_maddr\_leave](group__net__if.md#gad24d5537d52de9781a7a6a55ceedd92b) (struct [net\_if](structnet__if.md) \*iface, struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*addr) |
|  | Mark a given multicast address to be left. |
| struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) \* | [net\_if\_ipv6\_prefix\_get](group__net__if.md#gae9f98dff661d52c5e3e5e185f0ed9cc0) (struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Return prefix that corresponds to this IPv6 address. |
| struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) \* | [net\_if\_ipv6\_prefix\_lookup](group__net__if.md#gaaf9af457b97c0d432b6f9f9fdd184834) (struct [net\_if](structnet__if.md) \*iface, struct [in6\_addr](structin6__addr.md) \*addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len) |
|  | Check if this IPv6 prefix belongs to this interface. |
| struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) \* | [net\_if\_ipv6\_prefix\_add](group__net__if.md#ga2f0c98b16b090d9aea07941c64cbe035) (struct [net\_if](structnet__if.md) \*iface, struct [in6\_addr](structin6__addr.md) \*prefix, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) lifetime) |
|  | Add a IPv6 prefix to an network interface. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_ipv6\_prefix\_rm](group__net__if.md#ga36f18c7a3ff1777006290170b726deed) (struct [net\_if](structnet__if.md) \*iface, struct [in6\_addr](structin6__addr.md) \*addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len) |
|  | Remove an IPv6 prefix from an interface. |
| static void | [net\_if\_ipv6\_prefix\_set\_lf](group__net__if.md#gaa3c711e814fb6a4e552b4ef723d0baa0) (struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) \*prefix, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) is\_infinite) |
|  | Set the infinite status of the prefix. |
| void | [net\_if\_ipv6\_prefix\_set\_timer](group__net__if.md#ga68cffe343c518bad7f7f152e30f7f9ee) (struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) \*prefix, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) lifetime) |
|  | Set the prefix lifetime timer. |
| void | [net\_if\_ipv6\_prefix\_unset\_timer](group__net__if.md#ga2d68cb6dcfcffd3f87bbfb3dfce791ff) (struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) \*prefix) |
|  | Unset the prefix lifetime timer. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_ipv6\_addr\_onlink](group__net__if.md#ga25d6e2253c1d361553d478f7c948a28a) (struct [net\_if](structnet__if.md) \*\*iface, struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if this IPv6 address is part of the subnet of our network interface. |
| static struct [in6\_addr](structin6__addr.md) \* | [net\_if\_router\_ipv6](group__net__if.md#gadbf1538003473d448ff0808896b732a5) (struct [net\_if\_router](structnet__if__router.md) \*router) |
|  | Get the IPv6 address of the given router. |
| struct [net\_if\_router](structnet__if__router.md) \* | [net\_if\_ipv6\_router\_lookup](group__net__if.md#gacece4ee588082259b3b5cfcd5ac1d552) (struct [net\_if](structnet__if.md) \*iface, struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if IPv6 address is one of the routers configured in the system. |
| struct [net\_if\_router](structnet__if__router.md) \* | [net\_if\_ipv6\_router\_find\_default](group__net__if.md#ga36dab2a8fd9120ebc9c8b18f1875ccfd) (struct [net\_if](structnet__if.md) \*iface, struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Find default router for this IPv6 address. |
| void | [net\_if\_ipv6\_router\_update\_lifetime](group__net__if.md#gaadba4957802dc376ef011590c91c6af6) (struct [net\_if\_router](structnet__if__router.md) \*router, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) lifetime) |
|  | Update validity lifetime time of a router. |
| struct [net\_if\_router](structnet__if__router.md) \* | [net\_if\_ipv6\_router\_add](group__net__if.md#ga9c766ed70ada6eb551ac6542d7ac1ca3) (struct [net\_if](structnet__if.md) \*iface, struct [in6\_addr](structin6__addr.md) \*addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) router\_lifetime) |
|  | Add IPv6 router to the system. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_ipv6\_router\_rm](group__net__if.md#ga1d108aa0b54c072e0aa9d0c049f02807) (struct [net\_if\_router](structnet__if__router.md) \*router) |
|  | Remove IPv6 router from the system. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [net\_if\_ipv6\_get\_hop\_limit](group__net__if.md#ga66d0a9a8eef095f6d4d44f35dd67f2b6) (struct [net\_if](structnet__if.md) \*iface) |
|  | Get IPv6 hop limit specified for a given interface. |
| static void | [net\_if\_ipv6\_set\_hop\_limit](group__net__if.md#ga5bf726bb5c1d232103ec6841e7d0cd8c) (struct [net\_if](structnet__if.md) \*iface, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hop\_limit) |
|  | Set the default IPv6 hop limit of a given interface. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [net\_if\_ipv6\_get\_mcast\_hop\_limit](group__net__if.md#ga56e7086633bcf4537f54c7ca70e6c900) (struct [net\_if](structnet__if.md) \*iface) |
|  | Get IPv6 multicast hop limit specified for a given interface. |
| static void | [net\_if\_ipv6\_set\_mcast\_hop\_limit](group__net__if.md#gaf56a433679ea9701cf8baa3208f8ccc3) (struct [net\_if](structnet__if.md) \*iface, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hop\_limit) |
|  | Set the default IPv6 multicast hop limit of a given interface. |
| static void | [net\_if\_ipv6\_set\_base\_reachable\_time](group__net__if.md#gab3939d735b660f8f02124df656ceba2c) (struct [net\_if](structnet__if.md) \*iface, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) reachable\_time) |
|  | Set IPv6 reachable time for a given interface. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [net\_if\_ipv6\_get\_reachable\_time](group__net__if.md#ga9dd1f91edbb519a6a079f363c33efacf) (struct [net\_if](structnet__if.md) \*iface) |
|  | Get IPv6 reachable timeout specified for a given interface. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [net\_if\_ipv6\_calc\_reachable\_time](group__net__if.md#gab1861b5cefa73b4eefbb447cb1438cdc) (struct [net\_if\_ipv6](structnet__if__ipv6.md) \*ipv6) |
|  | Calculate next reachable time value for IPv6 reachable time. |
| static void | [net\_if\_ipv6\_set\_reachable\_time](group__net__if.md#ga8328266b870fd200660cb2becaab3de4) (struct [net\_if\_ipv6](structnet__if__ipv6.md) \*ipv6) |
|  | Set IPv6 reachable time for a given interface. |
| static void | [net\_if\_ipv6\_set\_retrans\_timer](group__net__if.md#gad74566e5a34f447d2ac63d2c0e82eeff) (struct [net\_if](structnet__if.md) \*iface, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) retrans\_timer) |
|  | Set IPv6 retransmit timer for a given interface. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [net\_if\_ipv6\_get\_retrans\_timer](group__net__if.md#gaddbf5a6ba412e6bdb7e31568fe827bd0) (struct [net\_if](structnet__if.md) \*iface) |
|  | Get IPv6 retransmit timer specified for a given interface. |
| static const struct [in6\_addr](structin6__addr.md) \* | [net\_if\_ipv6\_select\_src\_addr](group__net__if.md#ga50689a1afdb37a7087bf47a12cc50438) (struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*dst) |
|  | Get a IPv6 source address that should be used when sending network data to destination. |
| static const struct [in6\_addr](structin6__addr.md) \* | [net\_if\_ipv6\_select\_src\_addr\_hint](group__net__if.md#ga5cf4717e632f712045dd4fe81b30245c) (struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*dst, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Get a IPv6 source address that should be used when sending network data to destination. |
| static struct [net\_if](structnet__if.md) \* | [net\_if\_ipv6\_select\_src\_iface](group__net__if.md#gae1495ac9e743be54b8d90bd4ff4700ab) (const struct [in6\_addr](structin6__addr.md) \*dst) |
|  | Get a network interface that should be used when sending IPv6 network data to destination. |
| struct [in6\_addr](structin6__addr.md) \* | [net\_if\_ipv6\_get\_ll](group__net__if.md#gad6f3e1e349e281887352652f6f32274e) (struct [net\_if](structnet__if.md) \*iface, enum [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) addr\_state) |
|  | Get a IPv6 link local address in a given state. |
| struct [in6\_addr](structin6__addr.md) \* | [net\_if\_ipv6\_get\_ll\_addr](group__net__if.md#ga85b7a923d46d36ecd63f9930bd8970c4) (enum [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), struct [net\_if](structnet__if.md) \*\*iface) |
|  | Return link local IPv6 address from the first interface that has a link local address matching give state. |
| void | [net\_if\_ipv6\_dad\_failed](group__net__if.md#ga1dd53d92f803cff3be4826ddfb6b7211) (struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Stop IPv6 Duplicate Address Detection (DAD) procedure if we find out that our IPv6 address is already in use. |
| struct [in6\_addr](structin6__addr.md) \* | [net\_if\_ipv6\_get\_global\_addr](group__net__if.md#gaca7d686c772deac13a027cc046333126) (enum [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), struct [net\_if](structnet__if.md) \*\*iface) |
|  | Return global IPv6 address from the first interface that has a global IPv6 address matching the given state. |
| int | [net\_if\_config\_ipv4\_get](group__net__if.md#ga3390e248249b28f2c80e2ca0bc79d236) (struct [net\_if](structnet__if.md) \*iface, struct [net\_if\_ipv4](structnet__if__ipv4.md) \*\*ipv4) |
|  | Allocate network interface IPv4 config. |
| int | [net\_if\_config\_ipv4\_put](group__net__if.md#ga88c13a45617480a665c7f9f589ec8e10) (struct [net\_if](structnet__if.md) \*iface) |
|  | Release network interface IPv4 config. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [net\_if\_ipv4\_get\_ttl](group__net__if.md#ga7e1fd28dbcf1164d056296b4df782e64) (struct [net\_if](structnet__if.md) \*iface) |
|  | Get IPv4 time-to-live value specified for a given interface. |
| void | [net\_if\_ipv4\_set\_ttl](group__net__if.md#ga5544374d7ebea26a239d561083f0203d) (struct [net\_if](structnet__if.md) \*iface, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ttl) |
|  | Set IPv4 time-to-live value specified to a given interface. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [net\_if\_ipv4\_get\_mcast\_ttl](group__net__if.md#ga71acb65b1988aab8cca9c9604c86231e) (struct [net\_if](structnet__if.md) \*iface) |
|  | Get IPv4 multicast time-to-live value specified for a given interface. |
| void | [net\_if\_ipv4\_set\_mcast\_ttl](group__net__if.md#ga9452fef4f1309fb1a53a6a8b4f222377) (struct [net\_if](structnet__if.md) \*iface, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ttl) |
|  | Set IPv4 multicast time-to-live value specified to a given interface. |
| struct [net\_if\_addr](structnet__if__addr.md) \* | [net\_if\_ipv4\_addr\_lookup](group__net__if.md#ga04a8f21d173d51bdcc092b92ed949e53) (const struct [in\_addr](structin__addr.md) \*addr, struct [net\_if](structnet__if.md) \*\*iface) |
|  | Check if this IPv4 address belongs to one of the interfaces. |
| struct [net\_if\_addr](structnet__if__addr.md) \* | [net\_if\_ipv4\_addr\_add](group__net__if.md#ga7190958f740cac56de3a13fe688b3b5d) (struct [net\_if](structnet__if.md) \*iface, struct [in\_addr](structin__addr.md) \*addr, enum [net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41) addr\_type, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) vlifetime) |
|  | Add a IPv4 address to an interface. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_ipv4\_addr\_rm](group__net__if.md#ga4433304d46b6559604486b828e7d9dec) (struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*addr) |
|  | Remove a IPv4 address from an interface. |
| int | [net\_if\_ipv4\_addr\_lookup\_by\_index](group__net__if.md#ga0a22661727316517685afcd551e7b38e) (const struct [in\_addr](structin__addr.md) \*addr) |
|  | Check if this IPv4 address belongs to one of the interface indices. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_ipv4\_addr\_add\_by\_index](group__net__if.md#gad140a69cf510ad99a8a8c770bab95bc9) (int index, struct [in\_addr](structin__addr.md) \*addr, enum [net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41) addr\_type, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) vlifetime) |
|  | Add a IPv4 address to an interface by network interface index. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_ipv4\_addr\_rm\_by\_index](group__net__if.md#gac5bf15f948ab195cecce98d1b40bda37) (int index, const struct [in\_addr](structin__addr.md) \*addr) |
|  | Remove a IPv4 address from an interface by interface index. |
| void | [net\_if\_ipv4\_addr\_foreach](group__net__if.md#gaae71be476e27c178ebb21b0f183c2825) (struct [net\_if](structnet__if.md) \*iface, [net\_if\_ip\_addr\_cb\_t](group__net__if.md#gab58d8561a4f21899e2db34043d346516) cb, void \*user\_data) |
|  | Go through all IPv4 addresses on a network interface and call callback for each used address. |
| struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \* | [net\_if\_ipv4\_maddr\_add](group__net__if.md#gaa43fa83711703f8737e50b639e11b16c) (struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*addr) |
|  | Add a IPv4 multicast address to an interface. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_ipv4\_maddr\_rm](group__net__if.md#ga1d9273e10ab089d0f02b2b17d10a9e60) (struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*addr) |
|  | Remove an IPv4 multicast address from an interface. |
| void | [net\_if\_ipv4\_maddr\_foreach](group__net__if.md#gae82f53c670f602e9c37b65abb6dfaec7) (struct [net\_if](structnet__if.md) \*iface, [net\_if\_ip\_maddr\_cb\_t](group__net__if.md#ga726eed76563c223de8f611e2544febe9) cb, void \*user\_data) |
|  | Go through all IPv4 multicast addresses on a network interface and call callback for each used address. |
| struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \* | [net\_if\_ipv4\_maddr\_lookup](group__net__if.md#gadc1514a0d6852de9dbce043bc99d4eb0) (const struct [in\_addr](structin__addr.md) \*addr, struct [net\_if](structnet__if.md) \*\*iface) |
|  | Check if this IPv4 multicast address belongs to a specific interface or one of the interfaces. |
| void | [net\_if\_ipv4\_maddr\_join](group__net__if.md#gae275a5e75817aa178d36f422573ad76a) (struct [net\_if](structnet__if.md) \*iface, struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*addr) |
|  | Mark a given multicast address to be joined. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_ipv4\_maddr\_is\_joined](group__net__if.md#gaa30769fc8016f1a7496b3ede277d8d8a) (struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*addr) |
|  | Check if given multicast address is joined or not. |
| void | [net\_if\_ipv4\_maddr\_leave](group__net__if.md#ga1408fe384736d20f36c035c10007113c) (struct [net\_if](structnet__if.md) \*iface, struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*addr) |
|  | Mark a given multicast address to be left. |
| static struct [in\_addr](structin__addr.md) \* | [net\_if\_router\_ipv4](group__net__if.md#ga2a48e13941c91ddb9bbc63d014729be1) (struct [net\_if\_router](structnet__if__router.md) \*router) |
|  | Get the IPv4 address of the given router. |
| struct [net\_if\_router](structnet__if__router.md) \* | [net\_if\_ipv4\_router\_lookup](group__net__if.md#ga01f995b00248ad5da734e4d58a4353aa) (struct [net\_if](structnet__if.md) \*iface, struct [in\_addr](structin__addr.md) \*addr) |
|  | Check if IPv4 address is one of the routers configured in the system. |
| struct [net\_if\_router](structnet__if__router.md) \* | [net\_if\_ipv4\_router\_find\_default](group__net__if.md#ga25672516d7f383807e7dd9ce5f46a94f) (struct [net\_if](structnet__if.md) \*iface, struct [in\_addr](structin__addr.md) \*addr) |
|  | Find default router for this IPv4 address. |
| struct [net\_if\_router](structnet__if__router.md) \* | [net\_if\_ipv4\_router\_add](group__net__if.md#ga44984001411077c7a2ef68afb361b40f) (struct [net\_if](structnet__if.md) \*iface, struct [in\_addr](structin__addr.md) \*addr, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) is\_default, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) router\_lifetime) |
|  | Add IPv4 router to the system. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_ipv4\_router\_rm](group__net__if.md#ga6be14f5307bc63ce87ff0a3fad7c7f4d) (struct [net\_if\_router](structnet__if__router.md) \*router) |
|  | Remove IPv4 router from the system. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_ipv4\_addr\_mask\_cmp](group__net__if.md#ga558b31e556a1a4b8d1e68a78f3f755ea) (struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*addr) |
|  | Check if the given IPv4 address belongs to local subnet. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_ipv4\_is\_addr\_bcast](group__net__if.md#ga8f93179138c1942bc1a099102a4314cf) (struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*addr) |
|  | Check if the given IPv4 address is a broadcast address. |
| static struct [net\_if](structnet__if.md) \* | [net\_if\_ipv4\_select\_src\_iface](group__net__if.md#gafea1a35f452ad8168855852cbfdf0024) (const struct [in\_addr](structin__addr.md) \*dst) |
|  | Get a network interface that should be used when sending IPv4 network data to destination. |
| static const struct [in\_addr](structin__addr.md) \* | [net\_if\_ipv4\_select\_src\_addr](group__net__if.md#gad6ec091f61ba3055be60c77ce085522f) (struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*dst) |
|  | Get a IPv4 source address that should be used when sending network data to destination. |
| struct [in\_addr](structin__addr.md) \* | [net\_if\_ipv4\_get\_ll](group__net__if.md#gad2ffe8df3d5ccca5094daecf3b9a8508) (struct [net\_if](structnet__if.md) \*iface, enum [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) addr\_state) |
|  | Get a IPv4 link local address in a given state. |
| struct [in\_addr](structin__addr.md) \* | [net\_if\_ipv4\_get\_global\_addr](group__net__if.md#gad791780f25d19acfe49d5272eae2d019) (struct [net\_if](structnet__if.md) \*iface, enum [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) addr\_state) |
|  | Get a IPv4 global address in a given state. |
| struct [in\_addr](structin__addr.md) | [net\_if\_ipv4\_get\_netmask\_by\_addr](group__net__if.md#gadfad7d9232bf58c5626266387a2eb761) (struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*addr) |
|  | Get IPv4 netmask related to an address of an interface. |
| struct [in\_addr](structin__addr.md) | [net\_if\_ipv4\_get\_netmask](group__net__if.md#ga41aeb0e7c5f9bc837f7b2ec13401afd1) (struct [net\_if](structnet__if.md) \*iface) |
|  | Get IPv4 netmask of an interface. |
| void | [net\_if\_ipv4\_set\_netmask](group__net__if.md#gad599bd11663fefa7d785b9fc5d52caf0) (struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*netmask) |
|  | Set IPv4 netmask for an interface. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_ipv4\_set\_netmask\_by\_index](group__net__if.md#ga94f2d2e69548609dd329c7e6b21e8958) (int index, const struct [in\_addr](structin__addr.md) \*netmask) |
|  | Set IPv4 netmask for an interface index. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_ipv4\_set\_netmask\_by\_addr\_by\_index](group__net__if.md#ga895cfd55f79f7fb78a17cf0e3004fa06) (int index, const struct [in\_addr](structin__addr.md) \*addr, const struct [in\_addr](structin__addr.md) \*netmask) |
|  | Set IPv4 netmask for an interface index for a given address. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_ipv4\_set\_netmask\_by\_addr](group__net__if.md#ga7beda6ccba46fce3cf2da1ce6c0725ec) (struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*addr, const struct [in\_addr](structin__addr.md) \*netmask) |
|  | Set IPv4 netmask for an interface index for a given address. |
| struct [in\_addr](structin__addr.md) | [net\_if\_ipv4\_get\_gw](group__net__if.md#gae42f6f9620e40e2d2b36d30e81bb82d9) (struct [net\_if](structnet__if.md) \*iface) |
|  | Get IPv4 gateway of an interface. |
| void | [net\_if\_ipv4\_set\_gw](group__net__if.md#ga310ccbd9b37629422ca8e32836362724) (struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*gw) |
|  | Set IPv4 gateway for an interface. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_ipv4\_set\_gw\_by\_index](group__net__if.md#gadef49124c331817165475c69fb9104e0) (int index, const struct [in\_addr](structin__addr.md) \*gw) |
|  | Set IPv4 gateway for an interface index. |
| struct [net\_if](structnet__if.md) \* | [net\_if\_select\_src\_iface](group__net__if.md#ga001b1cdde5febcf3970848c7c185c81c) (const struct [sockaddr](structsockaddr.md) \*dst) |
|  | Get a network interface that should be used when sending IPv6 or IPv4 network data to destination. |
| void | [net\_if\_register\_link\_cb](group__net__if.md#gaa81b7d9ed8dc05da3391265dbc89b665) (struct [net\_if\_link\_cb](structnet__if__link__cb.md) \*link, [net\_if\_link\_callback\_t](group__net__if.md#ga0f87d5753fcd7cce40ecd161e6c91078) cb) |
|  | Register a link callback. |
| void | [net\_if\_unregister\_link\_cb](group__net__if.md#ga6ba64fac6e8d846ae7be5990f49a8293) (struct [net\_if\_link\_cb](structnet__if__link__cb.md) \*link) |
|  | Unregister a link callback. |
| void | [net\_if\_call\_link\_cb](group__net__if.md#gaaa64aa4391a85760bb2daf600ac4d898) (struct [net\_if](structnet__if.md) \*iface, struct [net\_linkaddr](structnet__linkaddr.md) \*lladdr, int status) |
|  | Call a link callback function. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_need\_calc\_rx\_checksum](group__net__if.md#ga8048e722f6442bcd5b6881bd71e791a5) (struct [net\_if](structnet__if.md) \*iface, enum [net\_if\_checksum\_type](group__net__if.md#ga8db412ae79c64cafe81a66f5acb2f8e9) chksum\_type) |
|  | Check if received network packet checksum calculation can be avoided or not. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_need\_calc\_tx\_checksum](group__net__if.md#ga9634c3e71e934ab3a07bec989b364663) (struct [net\_if](structnet__if.md) \*iface, enum [net\_if\_checksum\_type](group__net__if.md#ga8db412ae79c64cafe81a66f5acb2f8e9) chksum\_type) |
|  | Check if network packet checksum calculation can be avoided or not when sending the packet. |
| struct [net\_if](structnet__if.md) \* | [net\_if\_get\_by\_index](group__net__if.md#ga72708cdb7f133fe5d7edf819756c3516) (int index) |
|  | Get interface according to index. |
| int | [net\_if\_get\_by\_iface](group__net__if.md#ga02445f6c61f0d29f56ac0ef59e025630) (struct [net\_if](structnet__if.md) \*iface) |
|  | Get interface index according to pointer. |
| void | [net\_if\_foreach](group__net__if.md#ga96b198fd9df4a985b0dde84dd7152815) ([net\_if\_cb\_t](group__net__if.md#gac48ab8e6337e7cf387af9b293f254a80) cb, void \*user\_data) |
|  | Go through all the network interfaces and call callback for each interface. |
| int | [net\_if\_up](group__net__if.md#ga02644cc623fc7a8878c17d54984e4210) (struct [net\_if](structnet__if.md) \*iface) |
|  | Bring interface up. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_is\_up](group__net__if.md#ga7e9b368d4abf9da5656140df70cfa334) (struct [net\_if](structnet__if.md) \*iface) |
|  | Check if interface is up and running. |
| int | [net\_if\_down](group__net__if.md#ga2187650062d6139b9f4b81745a206803) (struct [net\_if](structnet__if.md) \*iface) |
|  | Bring interface down. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_is\_admin\_up](group__net__if.md#ga099a484a654ad9af35d3212fc2c995b2) (struct [net\_if](structnet__if.md) \*iface) |
|  | Check if interface was brought up by the administrator. |
| void | [net\_if\_carrier\_on](group__net__if.md#ga35e5db3a631ac9039f14d86e59fc0dcc) (struct [net\_if](structnet__if.md) \*iface) |
|  | Underlying network device has detected the carrier (cable connected). |
| void | [net\_if\_carrier\_off](group__net__if.md#ga6839941422a88c1f707ab70ea34df323) (struct [net\_if](structnet__if.md) \*iface) |
|  | Underlying network device has lost the carrier (cable disconnected). |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_is\_carrier\_ok](group__net__if.md#ga095554237016e563d76cfd602d1dae77) (struct [net\_if](structnet__if.md) \*iface) |
|  | Check if carrier is present on network device. |
| void | [net\_if\_dormant\_on](group__net__if.md#ga89a3374d4bb116460a7b7c50a750b593) (struct [net\_if](structnet__if.md) \*iface) |
|  | Mark interface as dormant. |
| void | [net\_if\_dormant\_off](group__net__if.md#ga1c31fac887d944ac0a16aad70e889496) (struct [net\_if](structnet__if.md) \*iface) |
|  | Mark interface as not dormant. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_is\_dormant](group__net__if.md#ga6e2e6102271c37acaa59c54e2aa6b413) (struct [net\_if](structnet__if.md) \*iface) |
|  | Check if the interface is dormant. |
| static int | [net\_if\_set\_promisc](group__net__if.md#gaf9f81f3b9697ca47f7674d85f37a8d80) (struct [net\_if](structnet__if.md) \*iface) |
|  | Set network interface into promiscuous mode. |
| static void | [net\_if\_unset\_promisc](group__net__if.md#ga9c8212c087883510050ac6a39ef0a7bf) (struct [net\_if](structnet__if.md) \*iface) |
|  | Set network interface into normal mode. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_is\_promisc](group__net__if.md#ga9f1a6eab849517734ec422deb0ba71f5) (struct [net\_if](structnet__if.md) \*iface) |
|  | Check if promiscuous mode is set or not. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_are\_pending\_tx\_packets](group__net__if.md#ga3cddda628eca248246f9aa3b81938f95) (struct [net\_if](structnet__if.md) \*iface) |
|  | Check if there are any pending TX network data for a given network interface. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_is\_wifi](group__net__if.md#gaa458b5f349c55007108b47b99f4954d5) (struct [net\_if](structnet__if.md) \*iface) |
|  | Check if the network interface supports Wi-Fi. |
| struct [net\_if](structnet__if.md) \* | [net\_if\_get\_first\_wifi](group__net__if.md#ga6e89bbafb6c0acdc6bf51078e2027236) (void) |
|  | Get first Wi-Fi network interface. |
| struct [net\_if](structnet__if.md) \* | [net\_if\_get\_wifi\_sta](group__net__if.md#ga0fc3ba6172956f6847027e0bd3d367de) (void) |
|  | Get Wi-Fi network station interface. |
| struct [net\_if](structnet__if.md) \* | [net\_if\_get\_wifi\_sap](group__net__if.md#gaf830eab616191009d88f58b761694b49) (void) |
|  | Get first Wi-Fi network Soft-AP interface. |
| int | [net\_if\_get\_name](group__net__if.md#ga5f653cd73c1ecd548a931eb7fbd170f7) (struct [net\_if](structnet__if.md) \*iface, char \*buf, int len) |
|  | Get network interface name. |
| int | [net\_if\_set\_name](group__net__if.md#ga05dec64966fc39e3deb0679b9585688b) (struct [net\_if](structnet__if.md) \*iface, const char \*buf) |
|  | Set network interface name. |
| int | [net\_if\_get\_by\_name](group__net__if.md#ga1774ac036032bb0dc2c662f6f4f66a7f) (const char \*name) |
|  | Get interface index according to its name. |

## Detailed Description

Public API for network interface.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_if.h](net__if_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
