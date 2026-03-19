---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__net__if.html
original_path: doxygen/html/group__net__if.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Network Interface abstraction layer

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

Network Interface abstraction layer.
[More...](#details)

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
| #define | [NET\_DEVICE\_INIT](#ga02971562c42494e2a5f71e1f8587e709)(dev\_id, name, init\_fn, pm, data, config, prio, api, l2, l2\_ctx\_type, mtu) |
|  | Create a network interface and bind it to network device. |
| #define | [NET\_DEVICE\_DT\_DEFINE](#gab1f762b01ae7bc37cd4a25724c123dda)(node\_id, init\_fn, pm, data, config, prio, api, l2, l2\_ctx\_type, mtu) |
|  | Like NET\_DEVICE\_INIT but taking metadata from a devicetree node. |
| #define | [NET\_DEVICE\_DT\_INST\_DEFINE](#ga7edd8bc59444d92cad0371c36f9949b7)(inst, ...) |
|  | Like NET\_DEVICE\_DT\_DEFINE for an instance of a DT\_DRV\_COMPAT compatible. |
| #define | [NET\_DEVICE\_INIT\_INSTANCE](#gacc7edecdd9de9920cc155977d8fec2a2)(dev\_id, name, instance, init\_fn, pm, data, config, prio, api, l2, l2\_ctx\_type, mtu) |
|  | Create multiple network interfaces and bind them to network device. |
| #define | [NET\_DEVICE\_DT\_DEFINE\_INSTANCE](#ga50702b043a0791e59e7d5679dda1d9e8)(node\_id, instance, init\_fn, pm, data, config, prio, api, l2, l2\_ctx\_type, mtu) |
|  | Like NET\_DEVICE\_OFFLOAD\_INIT but taking metadata from a devicetree. |
| #define | [NET\_DEVICE\_DT\_INST\_DEFINE\_INSTANCE](#gabe4b8589996a53cbc50b76c8ea15aa0c)(inst, ...) |
|  | Like NET\_DEVICE\_DT\_DEFINE\_INSTANCE for an instance of a DT\_DRV\_COMPAT compatible. |
| #define | [NET\_DEVICE\_OFFLOAD\_INIT](#ga255672607b7958db3f464d2a57a7e635)(dev\_id, name, init\_fn, pm, data, config, prio, api, mtu) |
|  | Create a offloaded network interface and bind it to network device. |
| #define | [NET\_DEVICE\_DT\_OFFLOAD\_DEFINE](#gab2b287025e194dec1fab24e44d95362f)(node\_id, init\_fn, pm, data, config, prio, api, mtu) |
|  | Like NET\_DEVICE\_OFFLOAD\_INIT but taking metadata from a devicetree node. |
| #define | [NET\_DEVICE\_DT\_INST\_OFFLOAD\_DEFINE](#ga1cab6943a28e3d3754e36623834b93fd)(inst, ...) |
|  | Like NET\_DEVICE\_DT\_OFFLOAD\_DEFINE for an instance of a DT\_DRV\_COMPAT compatible. |
| #define | [NET\_IFACE\_COUNT](#ga6c081875a6f5a848b3ad2fd220c63c3c)(\_dst) |
|  | Count the number of network interfaces. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [net\_socket\_create\_t](#gaef3dfe26195514aac625e9f22e399759)) (int, int, int) |
|  | A function prototype to create an offloaded socket. |
| typedef void(\* | [net\_if\_ip\_addr\_cb\_t](#gab58d8561a4f21899e2db34043d346516)) (struct [net\_if](structnet__if.md) \*iface, struct [net\_if\_addr](structnet__if__addr.md) \*addr, void \*user\_data) |
|  | Callback used while iterating over network interface IP addresses. |
| typedef void(\* | [net\_if\_ip\_maddr\_cb\_t](#ga726eed76563c223de8f611e2544febe9)) (struct [net\_if](structnet__if.md) \*iface, struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*maddr, void \*user\_data) |
|  | Callback used while iterating over network interface multicast IP addresses. |
| typedef void(\* | [net\_if\_mcast\_callback\_t](#ga0d64291573740a67eae7ff3fcc0910c5)) (struct [net\_if](structnet__if.md) \*iface, const struct net\_addr \*addr, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) is\_joined) |
|  | Define a callback that is called whenever a IPv6 or IPv4 multicast address group is joined or left. |
| typedef void(\* | [net\_if\_link\_callback\_t](#ga0f87d5753fcd7cce40ecd161e6c91078)) (struct [net\_if](structnet__if.md) \*iface, struct [net\_linkaddr](structnet__linkaddr.md) \*dst, int status) |
|  | Define callback that is called after a network packet has been sent. |
| typedef void(\* | [net\_if\_cb\_t](#gac48ab8e6337e7cf387af9b293f254a80)) (struct [net\_if](structnet__if.md) \*iface, void \*user\_data) |
|  | Callback used while iterating over network interfaces. |

| Enumerations | |
| --- | --- |
| enum | [net\_if\_flag](#gae691e5537917ffce27ad0db82c730371) {     [NET\_IF\_UP](#ggae691e5537917ffce27ad0db82c730371ab0ab7393d643354c46c3437d74c15840) , [NET\_IF\_POINTOPOINT](#ggae691e5537917ffce27ad0db82c730371a3256ef2d537c85b4c2b33b92935e1009) , [NET\_IF\_PROMISC](#ggae691e5537917ffce27ad0db82c730371a700d92a5b0de3c779e59806137b35141) , [NET\_IF\_NO\_AUTO\_START](#ggae691e5537917ffce27ad0db82c730371a0babb762301878eaf8ef8a05213ecf05) ,     [NET\_IF\_SUSPENDED](#ggae691e5537917ffce27ad0db82c730371aaaeafc62e61ec120609205770c8b54f0) , [NET\_IF\_FORWARD\_MULTICASTS](#ggae691e5537917ffce27ad0db82c730371a581971c9d93a910c4c607da45aa2e4ac) , [NET\_IF\_IPV4](#ggae691e5537917ffce27ad0db82c730371a67d2c0fe390ab16f347ee2dc0a056329) , [NET\_IF\_IPV6](#ggae691e5537917ffce27ad0db82c730371aab31a9e1e8c02159f45efc4e0455a4d6) ,     [NET\_IF\_RUNNING](#ggae691e5537917ffce27ad0db82c730371add3e2ecdcd5de3154f9bd2836428a25a) , [NET\_IF\_LOWER\_UP](#ggae691e5537917ffce27ad0db82c730371ab1a529826bad6b4bcd04185372f97d6d) , [NET\_IF\_DORMANT](#ggae691e5537917ffce27ad0db82c730371a7dd1db72a37b1fbc4c4491ce1c75238d) , [NET\_IF\_IPV6\_NO\_ND](#ggae691e5537917ffce27ad0db82c730371a542ecce860ef3bf2df493da8d4c6a2f7) ,     [NET\_IF\_IPV6\_NO\_MLD](#ggae691e5537917ffce27ad0db82c730371a1d362cfabb58eb220ddb069431221fbe) , [NET\_IF\_NO\_TX\_LOCK](#ggae691e5537917ffce27ad0db82c730371ae8d564e1577c8daad8ce50a729c500c9)   } |
|  | Network interface flags. [More...](#gae691e5537917ffce27ad0db82c730371) |
| enum | [net\_if\_oper\_state](#gadfe9d90f24046cd9bd4bbee096e747b9) {     [NET\_IF\_OPER\_UNKNOWN](#ggadfe9d90f24046cd9bd4bbee096e747b9ac7cae092ea6ceeb62499a9b435ac4b58) , [NET\_IF\_OPER\_NOTPRESENT](#ggadfe9d90f24046cd9bd4bbee096e747b9a8f9f55840e75693163197baae9d50c32) , [NET\_IF\_OPER\_DOWN](#ggadfe9d90f24046cd9bd4bbee096e747b9adb20a95215310c420f8dae7e17a2f367) , [NET\_IF\_OPER\_LOWERLAYERDOWN](#ggadfe9d90f24046cd9bd4bbee096e747b9ae7e9b8b12ae618a5ee1483dee916aab4) ,     [NET\_IF\_OPER\_TESTING](#ggadfe9d90f24046cd9bd4bbee096e747b9a2240173b5c247ab5eb0a9a6afafb296f) , [NET\_IF\_OPER\_DORMANT](#ggadfe9d90f24046cd9bd4bbee096e747b9a5cbe2aa27a444444d4acf122113d430d) , [NET\_IF\_OPER\_UP](#ggadfe9d90f24046cd9bd4bbee096e747b9a6b99bfc28d831292029761d74209ee03)   } |
|  | Network interface operational status (RFC 2863). [More...](#gadfe9d90f24046cd9bd4bbee096e747b9) |
| enum | [net\_if\_checksum\_type](#ga8db412ae79c64cafe81a66f5acb2f8e9) {     [NET\_IF\_CHECKSUM\_IPV4\_HEADER](#gga8db412ae79c64cafe81a66f5acb2f8e9a75e4a0946d0e6755ebd7cc62558aee30) = NET\_IF\_CHECKSUM\_IPV4\_HEADER\_BIT , [NET\_IF\_CHECKSUM\_IPV4\_TCP](#gga8db412ae79c64cafe81a66f5acb2f8e9aaed32a3cb700eac3b67c6c7e5a0cd0ad) , [NET\_IF\_CHECKSUM\_IPV4\_UDP](#gga8db412ae79c64cafe81a66f5acb2f8e9afe1eaaa765c8ec3c61618e943cd3f1c3) , [NET\_IF\_CHECKSUM\_IPV4\_ICMP](#gga8db412ae79c64cafe81a66f5acb2f8e9a2aef87c97f22fdccdf1925d2687436b1) = NET\_IF\_CHECKSUM\_IPV4\_ICMP\_BIT ,     [NET\_IF\_CHECKSUM\_IPV6\_HEADER](#gga8db412ae79c64cafe81a66f5acb2f8e9ab204c7d5fddbd2c11e07a8831df6c00b) = NET\_IF\_CHECKSUM\_IPV6\_HEADER\_BIT , [NET\_IF\_CHECKSUM\_IPV6\_TCP](#gga8db412ae79c64cafe81a66f5acb2f8e9a31e33593e4e7f7f9b36e319e0991ab13) , [NET\_IF\_CHECKSUM\_IPV6\_UDP](#gga8db412ae79c64cafe81a66f5acb2f8e9a70b1272e2125cea9204bae144fd86660) , [NET\_IF\_CHECKSUM\_IPV6\_ICMP](#gga8db412ae79c64cafe81a66f5acb2f8e9af5b3bc7cb5e9771cd9fd57d9fda4c3b3) = NET\_IF\_CHECKSUM\_IPV6\_ICMP\_BIT   } |
|  | Type of checksum for which support in the interface will be queried. [More...](#ga8db412ae79c64cafe81a66f5acb2f8e9) |

| Functions | |
| --- | --- |
| static void | [net\_if\_flag\_set](#ga52f9fca13e9f836799e0e40f581744d2) (struct [net\_if](structnet__if.md) \*iface, enum [net\_if\_flag](#gae691e5537917ffce27ad0db82c730371) value) |
|  | Set a value in network interface flags. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_flag\_test\_and\_set](#ga42e7482191a92007960601f8bb621dca) (struct [net\_if](structnet__if.md) \*iface, enum [net\_if\_flag](#gae691e5537917ffce27ad0db82c730371) value) |
|  | Test and set a value in network interface flags. |
| static void | [net\_if\_flag\_clear](#gaff751b6a92b0c608ecfc50e8c0587fd3) (struct [net\_if](structnet__if.md) \*iface, enum [net\_if\_flag](#gae691e5537917ffce27ad0db82c730371) value) |
|  | Clear a value in network interface flags. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_flag\_test\_and\_clear](#gab8f371c7f8890cf4728177f6595141d7) (struct [net\_if](structnet__if.md) \*iface, enum [net\_if\_flag](#gae691e5537917ffce27ad0db82c730371) value) |
|  | Test and clear a value in network interface flags. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_flag\_is\_set](#gae1f373ddd61c18a81481d8ddcfb12543) (struct [net\_if](structnet__if.md) \*iface, enum [net\_if\_flag](#gae691e5537917ffce27ad0db82c730371) value) |
|  | Check if a value in network interface flags is set. |
| static enum [net\_if\_oper\_state](#gadfe9d90f24046cd9bd4bbee096e747b9) | [net\_if\_oper\_state\_set](#ga1f1bf845e63cce02e2183889cc85d57e) (struct [net\_if](structnet__if.md) \*iface, enum [net\_if\_oper\_state](#gadfe9d90f24046cd9bd4bbee096e747b9) oper\_state) |
|  | Set an operational state on an interface. |
| static enum [net\_if\_oper\_state](#gadfe9d90f24046cd9bd4bbee096e747b9) | [net\_if\_oper\_state](#gad9e957a4866b4566296ee39392fde0e4) (struct [net\_if](structnet__if.md) \*iface) |
|  | Get an operational state of an interface. |
| enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) | [net\_if\_send\_data](#gada0398d757eab28d16a129692c309f4d) (struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | Send a packet through a net iface. |
| static const struct [net\_l2](structnet__l2.md) \* | [net\_if\_l2](#gafa451f6118529d1d084704d00b2aae20) (struct [net\_if](structnet__if.md) \*iface) |
|  | Get a pointer to the interface L2. |
| enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) | [net\_if\_recv\_data](#ga72ed21ca0cb220199f5a2070137c7fef) (struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | Input a packet through a net iface. |
| static void \* | [net\_if\_l2\_data](#ga3cad2d51fc9cc225619585e06e252db0) (struct [net\_if](structnet__if.md) \*iface) |
|  | Get a pointer to the interface L2 private data. |
| static const struct [device](structdevice.md) \* | [net\_if\_get\_device](#gaeb8c703f273bc07ae9bb7a0d8bfe6f3d) (struct [net\_if](structnet__if.md) \*iface) |
|  | Get an network interface's device. |
| void | [net\_if\_queue\_tx](#ga56c4d37edcea540be09ebcdf97265aed) (struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | Queue a packet to the net interface TX queue. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_is\_ip\_offloaded](#ga6bfa5f84a2127bbad27a0a3b319526a1) (struct [net\_if](structnet__if.md) \*iface) |
|  | Return the IP offload status. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_is\_offloaded](#gaecedc93a6dab2c57fe686718ea4d78af) (struct [net\_if](structnet__if.md) \*iface) |
|  | Return offload status of a given network interface. |
| static struct net\_offload \* | [net\_if\_offload](#ga520939e94620ca75475a71f153df6d4a) (struct [net\_if](structnet__if.md) \*iface) |
|  | Return the IP offload plugin. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_is\_socket\_offloaded](#gaf308baf2241fa455b50b439b7fab3f1e) (struct [net\_if](structnet__if.md) \*iface) |
|  | Return the socket offload status. |
| static void | [net\_if\_socket\_offload\_set](#ga9db52875580115c743b1f35cd6c46796) (struct [net\_if](structnet__if.md) \*iface, [net\_socket\_create\_t](#gaef3dfe26195514aac625e9f22e399759) socket\_offload) |
|  | Set the function to create an offloaded socket. |
| static [net\_socket\_create\_t](#gaef3dfe26195514aac625e9f22e399759) | [net\_if\_socket\_offload](#gafb2bbaec96c4759d920b2866c0b3ef3a) (struct [net\_if](structnet__if.md) \*iface) |
|  | Return the function to create an offloaded socket. |
| static struct [net\_linkaddr](structnet__linkaddr.md) \* | [net\_if\_get\_link\_addr](#ga467186e964bf721e14fed38392f21872) (struct [net\_if](structnet__if.md) \*iface) |
|  | Get an network interface's link address. |
| static struct [net\_if\_config](structnet__if__config.md) \* | [net\_if\_get\_config](#gae271e0e4dcb031a83d9908e597a45048) (struct [net\_if](structnet__if.md) \*iface) |
|  | Return network configuration for this network interface. |
| static void | [net\_if\_start\_dad](#ga9655c010ccbf989e9328271f5dbcc685) (struct [net\_if](structnet__if.md) \*iface) |
|  | Start duplicate address detection procedure. |
| void | [net\_if\_start\_rs](#gab9bdb7f8a9eeed4d9b70965b8af82cb7) (struct [net\_if](structnet__if.md) \*iface) |
|  | Start neighbor discovery and send router solicitation message. |
| static void | [net\_if\_stop\_rs](#gab0195bb2151a1ba722a0b11d81066988) (struct [net\_if](structnet__if.md) \*iface) |
|  | Stop neighbor discovery. |
| static void | [net\_if\_nbr\_reachability\_hint](#ga51af469ff3d7d9f760d63a8a9c7be8b5) (struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*ipv6\_addr) |
|  | Provide a reachability hint for IPv6 Neighbor Discovery. |
| static int | [net\_if\_set\_link\_addr](#ga52b41b2f8b7d3405338a0539542677a0) (struct [net\_if](structnet__if.md) \*iface, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len, enum [net\_link\_type](group__net__linkaddr.md#ga1312c2322bc4a4f1c3b76d6466806b24) type) |
|  | Set a network interface's link address. |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [net\_if\_get\_mtu](#gacddc98531c5748db5a34f5c3a3e96e86) (struct [net\_if](structnet__if.md) \*iface) |
|  | Get an network interface's MTU. |
| static void | [net\_if\_set\_mtu](#ga76b140c6fc39b94ff4102e08e3a58e81) (struct [net\_if](structnet__if.md) \*iface, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mtu) |
|  | Set an network interface's MTU. |
| static void | [net\_if\_addr\_set\_lf](#gae66f6e7bd31545e6161fcd4600fe5842) (struct [net\_if\_addr](structnet__if__addr.md) \*ifaddr, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) is\_infinite) |
|  | Set the infinite status of the network interface address. |
| struct [net\_if](structnet__if.md) \* | [net\_if\_get\_by\_link\_addr](#ga1b058361dc9bcac7d842bb49846a0c79) (struct [net\_linkaddr](structnet__linkaddr.md) \*ll\_addr) |
|  | Get an interface according to link layer address. |
| struct [net\_if](structnet__if.md) \* | [net\_if\_lookup\_by\_dev](#gadbb8be32caa896bdcdeee19425134827) (const struct [device](structdevice.md) \*dev) |
|  | Find an interface from it's related device. |
| static struct [net\_if\_config](structnet__if__config.md) \* | [net\_if\_config\_get](#gae2323a72714e29836d8296dfc330f7fd) (struct [net\_if](structnet__if.md) \*iface) |
|  | Get network interface IP config. |
| void | [net\_if\_router\_rm](#gadc87242eb7205362a308b3c4437bf76d) (struct [net\_if\_router](structnet__if__router.md) \*router) |
|  | Remove a router from the system. |
| void | [net\_if\_set\_default](#ga0a1f27ec893e1af3c97f130be4616589) (struct [net\_if](structnet__if.md) \*iface) |
|  | Set the default network interface. |
| struct [net\_if](structnet__if.md) \* | [net\_if\_get\_default](#ga55214771e462cbd4930ffa738813cb87) (void) |
|  | Get the default network interface. |
| struct [net\_if](structnet__if.md) \* | [net\_if\_get\_first\_by\_type](#ga762337e8b66874a0fbf59bdbeba173f5) (const struct [net\_l2](structnet__l2.md) \*l2) |
|  | Get the first network interface according to its type. |
| struct [net\_if](structnet__if.md) \* | [net\_if\_get\_first\_up](#ga03d8c6aebb1412382a9eec636c227238) (void) |
|  | Get the first network interface which is up. |
| int | [net\_if\_config\_ipv6\_get](#ga56c9aef19bc9827d9ec96c00e10840fa) (struct [net\_if](structnet__if.md) \*iface, struct [net\_if\_ipv6](structnet__if__ipv6.md) \*\*ipv6) |
|  | Allocate network interface IPv6 config. |
| int | [net\_if\_config\_ipv6\_put](#ga8af1400b354c42a64795cdb1a600ddd6) (struct [net\_if](structnet__if.md) \*iface) |
|  | Release network interface IPv6 config. |
| struct [net\_if\_addr](structnet__if__addr.md) \* | [net\_if\_ipv6\_addr\_lookup](#ga13b5a26fc672d15697f99e85543184bb) (const struct [in6\_addr](structin6__addr.md) \*addr, struct [net\_if](structnet__if.md) \*\*iface) |
|  | Check if this IPv6 address belongs to one of the interfaces. |
| struct [net\_if\_addr](structnet__if__addr.md) \* | [net\_if\_ipv6\_addr\_lookup\_by\_iface](#gab53eabb540a4487d83f27c8e319c736a) (struct [net\_if](structnet__if.md) \*iface, struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if this IPv6 address belongs to this specific interfaces. |
| int | [net\_if\_ipv6\_addr\_lookup\_by\_index](#ga1527872e5285790d50028a183608ac02) (const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if this IPv6 address belongs to one of the interface indices. |
| struct [net\_if\_addr](structnet__if__addr.md) \* | [net\_if\_ipv6\_addr\_add](#gae00484a7fe32671a4ca04ff525e640c6) (struct [net\_if](structnet__if.md) \*iface, struct [in6\_addr](structin6__addr.md) \*addr, enum [net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41) addr\_type, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) vlifetime) |
|  | Add a IPv6 address to an interface. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_ipv6\_addr\_add\_by\_index](#ga980bffb649ed48775bdc6cb2a0caef15) (int index, struct [in6\_addr](structin6__addr.md) \*addr, enum [net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41) addr\_type, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) vlifetime) |
|  | Add a IPv6 address to an interface by index. |
| void | [net\_if\_ipv6\_addr\_update\_lifetime](#gaef8a6752a201f81636c4ffc1ebba4a25) (struct [net\_if\_addr](structnet__if__addr.md) \*ifaddr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) vlifetime) |
|  | Update validity lifetime time of an IPv6 address. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_ipv6\_addr\_rm](#ga614e1458fa28d26c26f447e9fbcc2cb7) (struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Remove an IPv6 address from an interface. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_ipv6\_addr\_rm\_by\_index](#gac159e3b0fbf558d5fb09774141da7d6d) (int index, const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Remove an IPv6 address from an interface by index. |
| void | [net\_if\_ipv6\_addr\_foreach](#ga5ac646ad7fda0fa48e78c15b4ca52d50) (struct [net\_if](structnet__if.md) \*iface, [net\_if\_ip\_addr\_cb\_t](#gab58d8561a4f21899e2db34043d346516) cb, void \*user\_data) |
|  | Go through all IPv6 addresses on a network interface and call callback for each used address. |
| struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \* | [net\_if\_ipv6\_maddr\_add](#ga7ae82a491193dfea9b92cb9cbaf26f98) (struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Add a IPv6 multicast address to an interface. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_ipv6\_maddr\_rm](#gaf0ce126bb5019ff5f5ff0876b9712ad9) (struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Remove an IPv6 multicast address from an interface. |
| void | [net\_if\_ipv6\_maddr\_foreach](#gab677496fb2e27be2df299a346e9c7132) (struct [net\_if](structnet__if.md) \*iface, [net\_if\_ip\_maddr\_cb\_t](#ga726eed76563c223de8f611e2544febe9) cb, void \*user\_data) |
|  | Go through all IPv6 multicast addresses on a network interface and call callback for each used address. |
| struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \* | [net\_if\_ipv6\_maddr\_lookup](#gadb4031153c4fef86110879befa6b9975) (const struct [in6\_addr](structin6__addr.md) \*addr, struct [net\_if](structnet__if.md) \*\*iface) |
|  | Check if this IPv6 multicast address belongs to a specific interface or one of the interfaces. |
| void | [net\_if\_mcast\_mon\_register](#ga8fdd0665ed76db6055777e395ca60255) (struct [net\_if\_mcast\_monitor](structnet__if__mcast__monitor.md) \*mon, struct [net\_if](structnet__if.md) \*iface, [net\_if\_mcast\_callback\_t](#ga0d64291573740a67eae7ff3fcc0910c5) cb) |
|  | Register a multicast monitor. |
| void | [net\_if\_mcast\_mon\_unregister](#gad323732fe3d178a5dfdf0900e5cb5683) (struct [net\_if\_mcast\_monitor](structnet__if__mcast__monitor.md) \*mon) |
|  | Unregister a multicast monitor. |
| void | [net\_if\_mcast\_monitor](#ga372ef131263269cd65586d87997df745) (struct [net\_if](structnet__if.md) \*iface, const struct net\_addr \*addr, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) is\_joined) |
|  | Call registered multicast monitors. |
| void | [net\_if\_ipv6\_maddr\_join](#ga49dbc954015307222f176f4149829b76) (struct [net\_if](structnet__if.md) \*iface, struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*addr) |
|  | Mark a given multicast address to be joined. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_ipv6\_maddr\_is\_joined](#gabe2c16a378a35a22d008bff9142e5449) (struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*addr) |
|  | Check if given multicast address is joined or not. |
| void | [net\_if\_ipv6\_maddr\_leave](#gad24d5537d52de9781a7a6a55ceedd92b) (struct [net\_if](structnet__if.md) \*iface, struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*addr) |
|  | Mark a given multicast address to be left. |
| struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) \* | [net\_if\_ipv6\_prefix\_get](#gae9f98dff661d52c5e3e5e185f0ed9cc0) (struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Return prefix that corresponds to this IPv6 address. |
| struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) \* | [net\_if\_ipv6\_prefix\_lookup](#gaaf9af457b97c0d432b6f9f9fdd184834) (struct [net\_if](structnet__if.md) \*iface, struct [in6\_addr](structin6__addr.md) \*addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len) |
|  | Check if this IPv6 prefix belongs to this interface. |
| struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) \* | [net\_if\_ipv6\_prefix\_add](#ga2f0c98b16b090d9aea07941c64cbe035) (struct [net\_if](structnet__if.md) \*iface, struct [in6\_addr](structin6__addr.md) \*prefix, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) lifetime) |
|  | Add a IPv6 prefix to an network interface. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_ipv6\_prefix\_rm](#ga36f18c7a3ff1777006290170b726deed) (struct [net\_if](structnet__if.md) \*iface, struct [in6\_addr](structin6__addr.md) \*addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len) |
|  | Remove an IPv6 prefix from an interface. |
| static void | [net\_if\_ipv6\_prefix\_set\_lf](#gaa3c711e814fb6a4e552b4ef723d0baa0) (struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) \*prefix, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) is\_infinite) |
|  | Set the infinite status of the prefix. |
| void | [net\_if\_ipv6\_prefix\_set\_timer](#ga68cffe343c518bad7f7f152e30f7f9ee) (struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) \*prefix, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) lifetime) |
|  | Set the prefix lifetime timer. |
| void | [net\_if\_ipv6\_prefix\_unset\_timer](#ga2d68cb6dcfcffd3f87bbfb3dfce791ff) (struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) \*prefix) |
|  | Unset the prefix lifetime timer. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_ipv6\_addr\_onlink](#ga25d6e2253c1d361553d478f7c948a28a) (struct [net\_if](structnet__if.md) \*\*iface, struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if this IPv6 address is part of the subnet of our network interface. |
| static struct [in6\_addr](structin6__addr.md) \* | [net\_if\_router\_ipv6](#gadbf1538003473d448ff0808896b732a5) (struct [net\_if\_router](structnet__if__router.md) \*router) |
|  | Get the IPv6 address of the given router. |
| struct [net\_if\_router](structnet__if__router.md) \* | [net\_if\_ipv6\_router\_lookup](#gacece4ee588082259b3b5cfcd5ac1d552) (struct [net\_if](structnet__if.md) \*iface, struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Check if IPv6 address is one of the routers configured in the system. |
| struct [net\_if\_router](structnet__if__router.md) \* | [net\_if\_ipv6\_router\_find\_default](#ga36dab2a8fd9120ebc9c8b18f1875ccfd) (struct [net\_if](structnet__if.md) \*iface, struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Find default router for this IPv6 address. |
| void | [net\_if\_ipv6\_router\_update\_lifetime](#gaadba4957802dc376ef011590c91c6af6) (struct [net\_if\_router](structnet__if__router.md) \*router, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) lifetime) |
|  | Update validity lifetime time of a router. |
| struct [net\_if\_router](structnet__if__router.md) \* | [net\_if\_ipv6\_router\_add](#ga9c766ed70ada6eb551ac6542d7ac1ca3) (struct [net\_if](structnet__if.md) \*iface, struct [in6\_addr](structin6__addr.md) \*addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) router\_lifetime) |
|  | Add IPv6 router to the system. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_ipv6\_router\_rm](#ga1d108aa0b54c072e0aa9d0c049f02807) (struct [net\_if\_router](structnet__if__router.md) \*router) |
|  | Remove IPv6 router from the system. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [net\_if\_ipv6\_get\_hop\_limit](#ga66d0a9a8eef095f6d4d44f35dd67f2b6) (struct [net\_if](structnet__if.md) \*iface) |
|  | Get IPv6 hop limit specified for a given interface. |
| static void | [net\_if\_ipv6\_set\_hop\_limit](#ga5bf726bb5c1d232103ec6841e7d0cd8c) (struct [net\_if](structnet__if.md) \*iface, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hop\_limit) |
|  | Set the default IPv6 hop limit of a given interface. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [net\_if\_ipv6\_get\_mcast\_hop\_limit](#ga56e7086633bcf4537f54c7ca70e6c900) (struct [net\_if](structnet__if.md) \*iface) |
|  | Get IPv6 multicast hop limit specified for a given interface. |
| static void | [net\_if\_ipv6\_set\_mcast\_hop\_limit](#gaf56a433679ea9701cf8baa3208f8ccc3) (struct [net\_if](structnet__if.md) \*iface, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hop\_limit) |
|  | Set the default IPv6 multicast hop limit of a given interface. |
| static void | [net\_if\_ipv6\_set\_base\_reachable\_time](#gab3939d735b660f8f02124df656ceba2c) (struct [net\_if](structnet__if.md) \*iface, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) reachable\_time) |
|  | Set IPv6 reachable time for a given interface. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [net\_if\_ipv6\_get\_reachable\_time](#ga9dd1f91edbb519a6a079f363c33efacf) (struct [net\_if](structnet__if.md) \*iface) |
|  | Get IPv6 reachable timeout specified for a given interface. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [net\_if\_ipv6\_calc\_reachable\_time](#gab1861b5cefa73b4eefbb447cb1438cdc) (struct [net\_if\_ipv6](structnet__if__ipv6.md) \*ipv6) |
|  | Calculate next reachable time value for IPv6 reachable time. |
| static void | [net\_if\_ipv6\_set\_reachable\_time](#ga8328266b870fd200660cb2becaab3de4) (struct [net\_if\_ipv6](structnet__if__ipv6.md) \*ipv6) |
|  | Set IPv6 reachable time for a given interface. |
| static void | [net\_if\_ipv6\_set\_retrans\_timer](#gad74566e5a34f447d2ac63d2c0e82eeff) (struct [net\_if](structnet__if.md) \*iface, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) retrans\_timer) |
|  | Set IPv6 retransmit timer for a given interface. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [net\_if\_ipv6\_get\_retrans\_timer](#gaddbf5a6ba412e6bdb7e31568fe827bd0) (struct [net\_if](structnet__if.md) \*iface) |
|  | Get IPv6 retransmit timer specified for a given interface. |
| static const struct [in6\_addr](structin6__addr.md) \* | [net\_if\_ipv6\_select\_src\_addr](#ga50689a1afdb37a7087bf47a12cc50438) (struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*dst) |
|  | Get a IPv6 source address that should be used when sending network data to destination. |
| static const struct [in6\_addr](structin6__addr.md) \* | [net\_if\_ipv6\_select\_src\_addr\_hint](#ga5cf4717e632f712045dd4fe81b30245c) (struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*dst, int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Get a IPv6 source address that should be used when sending network data to destination. |
| static struct [net\_if](structnet__if.md) \* | [net\_if\_ipv6\_select\_src\_iface](#gae1495ac9e743be54b8d90bd4ff4700ab) (const struct [in6\_addr](structin6__addr.md) \*dst) |
|  | Get a network interface that should be used when sending IPv6 network data to destination. |
| struct [in6\_addr](structin6__addr.md) \* | [net\_if\_ipv6\_get\_ll](#gad6f3e1e349e281887352652f6f32274e) (struct [net\_if](structnet__if.md) \*iface, enum [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) addr\_state) |
|  | Get a IPv6 link local address in a given state. |
| struct [in6\_addr](structin6__addr.md) \* | [net\_if\_ipv6\_get\_ll\_addr](#ga85b7a923d46d36ecd63f9930bd8970c4) (enum [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), struct [net\_if](structnet__if.md) \*\*iface) |
|  | Return link local IPv6 address from the first interface that has a link local address matching give state. |
| void | [net\_if\_ipv6\_dad\_failed](#ga1dd53d92f803cff3be4826ddfb6b7211) (struct [net\_if](structnet__if.md) \*iface, const struct [in6\_addr](structin6__addr.md) \*addr) |
|  | Stop IPv6 Duplicate Address Detection (DAD) procedure if we find out that our IPv6 address is already in use. |
| struct [in6\_addr](structin6__addr.md) \* | [net\_if\_ipv6\_get\_global\_addr](#gaca7d686c772deac13a027cc046333126) (enum [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), struct [net\_if](structnet__if.md) \*\*iface) |
|  | Return global IPv6 address from the first interface that has a global IPv6 address matching the given state. |
| int | [net\_if\_config\_ipv4\_get](#ga3390e248249b28f2c80e2ca0bc79d236) (struct [net\_if](structnet__if.md) \*iface, struct [net\_if\_ipv4](structnet__if__ipv4.md) \*\*ipv4) |
|  | Allocate network interface IPv4 config. |
| int | [net\_if\_config\_ipv4\_put](#ga88c13a45617480a665c7f9f589ec8e10) (struct [net\_if](structnet__if.md) \*iface) |
|  | Release network interface IPv4 config. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [net\_if\_ipv4\_get\_ttl](#ga7e1fd28dbcf1164d056296b4df782e64) (struct [net\_if](structnet__if.md) \*iface) |
|  | Get IPv4 time-to-live value specified for a given interface. |
| void | [net\_if\_ipv4\_set\_ttl](#ga5544374d7ebea26a239d561083f0203d) (struct [net\_if](structnet__if.md) \*iface, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ttl) |
|  | Set IPv4 time-to-live value specified to a given interface. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [net\_if\_ipv4\_get\_mcast\_ttl](#ga71acb65b1988aab8cca9c9604c86231e) (struct [net\_if](structnet__if.md) \*iface) |
|  | Get IPv4 multicast time-to-live value specified for a given interface. |
| void | [net\_if\_ipv4\_set\_mcast\_ttl](#ga9452fef4f1309fb1a53a6a8b4f222377) (struct [net\_if](structnet__if.md) \*iface, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ttl) |
|  | Set IPv4 multicast time-to-live value specified to a given interface. |
| struct [net\_if\_addr](structnet__if__addr.md) \* | [net\_if\_ipv4\_addr\_lookup](#ga04a8f21d173d51bdcc092b92ed949e53) (const struct [in\_addr](structin__addr.md) \*addr, struct [net\_if](structnet__if.md) \*\*iface) |
|  | Check if this IPv4 address belongs to one of the interfaces. |
| struct [net\_if\_addr](structnet__if__addr.md) \* | [net\_if\_ipv4\_addr\_add](#ga7190958f740cac56de3a13fe688b3b5d) (struct [net\_if](structnet__if.md) \*iface, struct [in\_addr](structin__addr.md) \*addr, enum [net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41) addr\_type, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) vlifetime) |
|  | Add a IPv4 address to an interface. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_ipv4\_addr\_rm](#ga4433304d46b6559604486b828e7d9dec) (struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*addr) |
|  | Remove a IPv4 address from an interface. |
| int | [net\_if\_ipv4\_addr\_lookup\_by\_index](#ga0a22661727316517685afcd551e7b38e) (const struct [in\_addr](structin__addr.md) \*addr) |
|  | Check if this IPv4 address belongs to one of the interface indices. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_ipv4\_addr\_add\_by\_index](#gad140a69cf510ad99a8a8c770bab95bc9) (int index, struct [in\_addr](structin__addr.md) \*addr, enum [net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41) addr\_type, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) vlifetime) |
|  | Add a IPv4 address to an interface by network interface index. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_ipv4\_addr\_rm\_by\_index](#gac5bf15f948ab195cecce98d1b40bda37) (int index, const struct [in\_addr](structin__addr.md) \*addr) |
|  | Remove a IPv4 address from an interface by interface index. |
| void | [net\_if\_ipv4\_addr\_foreach](#gaae71be476e27c178ebb21b0f183c2825) (struct [net\_if](structnet__if.md) \*iface, [net\_if\_ip\_addr\_cb\_t](#gab58d8561a4f21899e2db34043d346516) cb, void \*user\_data) |
|  | Go through all IPv4 addresses on a network interface and call callback for each used address. |
| struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \* | [net\_if\_ipv4\_maddr\_add](#gaa43fa83711703f8737e50b639e11b16c) (struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*addr) |
|  | Add a IPv4 multicast address to an interface. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_ipv4\_maddr\_rm](#ga1d9273e10ab089d0f02b2b17d10a9e60) (struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*addr) |
|  | Remove an IPv4 multicast address from an interface. |
| void | [net\_if\_ipv4\_maddr\_foreach](#gae82f53c670f602e9c37b65abb6dfaec7) (struct [net\_if](structnet__if.md) \*iface, [net\_if\_ip\_maddr\_cb\_t](#ga726eed76563c223de8f611e2544febe9) cb, void \*user\_data) |
|  | Go through all IPv4 multicast addresses on a network interface and call callback for each used address. |
| struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \* | [net\_if\_ipv4\_maddr\_lookup](#gadc1514a0d6852de9dbce043bc99d4eb0) (const struct [in\_addr](structin__addr.md) \*addr, struct [net\_if](structnet__if.md) \*\*iface) |
|  | Check if this IPv4 multicast address belongs to a specific interface or one of the interfaces. |
| void | [net\_if\_ipv4\_maddr\_join](#gae275a5e75817aa178d36f422573ad76a) (struct [net\_if](structnet__if.md) \*iface, struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*addr) |
|  | Mark a given multicast address to be joined. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_ipv4\_maddr\_is\_joined](#gaa30769fc8016f1a7496b3ede277d8d8a) (struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*addr) |
|  | Check if given multicast address is joined or not. |
| void | [net\_if\_ipv4\_maddr\_leave](#ga1408fe384736d20f36c035c10007113c) (struct [net\_if](structnet__if.md) \*iface, struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*addr) |
|  | Mark a given multicast address to be left. |
| static struct [in\_addr](structin__addr.md) \* | [net\_if\_router\_ipv4](#ga2a48e13941c91ddb9bbc63d014729be1) (struct [net\_if\_router](structnet__if__router.md) \*router) |
|  | Get the IPv4 address of the given router. |
| struct [net\_if\_router](structnet__if__router.md) \* | [net\_if\_ipv4\_router\_lookup](#ga01f995b00248ad5da734e4d58a4353aa) (struct [net\_if](structnet__if.md) \*iface, struct [in\_addr](structin__addr.md) \*addr) |
|  | Check if IPv4 address is one of the routers configured in the system. |
| struct [net\_if\_router](structnet__if__router.md) \* | [net\_if\_ipv4\_router\_find\_default](#ga25672516d7f383807e7dd9ce5f46a94f) (struct [net\_if](structnet__if.md) \*iface, struct [in\_addr](structin__addr.md) \*addr) |
|  | Find default router for this IPv4 address. |
| struct [net\_if\_router](structnet__if__router.md) \* | [net\_if\_ipv4\_router\_add](#ga44984001411077c7a2ef68afb361b40f) (struct [net\_if](structnet__if.md) \*iface, struct [in\_addr](structin__addr.md) \*addr, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) is\_default, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) router\_lifetime) |
|  | Add IPv4 router to the system. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_ipv4\_router\_rm](#ga6be14f5307bc63ce87ff0a3fad7c7f4d) (struct [net\_if\_router](structnet__if__router.md) \*router) |
|  | Remove IPv4 router from the system. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_ipv4\_addr\_mask\_cmp](#ga558b31e556a1a4b8d1e68a78f3f755ea) (struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*addr) |
|  | Check if the given IPv4 address belongs to local subnet. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_ipv4\_is\_addr\_bcast](#ga8f93179138c1942bc1a099102a4314cf) (struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*addr) |
|  | Check if the given IPv4 address is a broadcast address. |
| static struct [net\_if](structnet__if.md) \* | [net\_if\_ipv4\_select\_src\_iface](#gafea1a35f452ad8168855852cbfdf0024) (const struct [in\_addr](structin__addr.md) \*dst) |
|  | Get a network interface that should be used when sending IPv4 network data to destination. |
| static const struct [in\_addr](structin__addr.md) \* | [net\_if\_ipv4\_select\_src\_addr](#gad6ec091f61ba3055be60c77ce085522f) (struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*dst) |
|  | Get a IPv4 source address that should be used when sending network data to destination. |
| struct [in\_addr](structin__addr.md) \* | [net\_if\_ipv4\_get\_ll](#gad2ffe8df3d5ccca5094daecf3b9a8508) (struct [net\_if](structnet__if.md) \*iface, enum [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) addr\_state) |
|  | Get a IPv4 link local address in a given state. |
| struct [in\_addr](structin__addr.md) \* | [net\_if\_ipv4\_get\_global\_addr](#gad791780f25d19acfe49d5272eae2d019) (struct [net\_if](structnet__if.md) \*iface, enum [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) addr\_state) |
|  | Get a IPv4 global address in a given state. |
| struct [in\_addr](structin__addr.md) | [net\_if\_ipv4\_get\_netmask\_by\_addr](#gadfad7d9232bf58c5626266387a2eb761) (struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*addr) |
|  | Get IPv4 netmask related to an address of an interface. |
| struct [in\_addr](structin__addr.md) | [net\_if\_ipv4\_get\_netmask](#ga41aeb0e7c5f9bc837f7b2ec13401afd1) (struct [net\_if](structnet__if.md) \*iface) |
|  | Get IPv4 netmask of an interface. |
| void | [net\_if\_ipv4\_set\_netmask](#gad599bd11663fefa7d785b9fc5d52caf0) (struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*netmask) |
|  | Set IPv4 netmask for an interface. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_ipv4\_set\_netmask\_by\_index](#ga94f2d2e69548609dd329c7e6b21e8958) (int index, const struct [in\_addr](structin__addr.md) \*netmask) |
|  | Set IPv4 netmask for an interface index. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_ipv4\_set\_netmask\_by\_addr\_by\_index](#ga895cfd55f79f7fb78a17cf0e3004fa06) (int index, const struct [in\_addr](structin__addr.md) \*addr, const struct [in\_addr](structin__addr.md) \*netmask) |
|  | Set IPv4 netmask for an interface index for a given address. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_ipv4\_set\_netmask\_by\_addr](#ga7beda6ccba46fce3cf2da1ce6c0725ec) (struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*addr, const struct [in\_addr](structin__addr.md) \*netmask) |
|  | Set IPv4 netmask for an interface index for a given address. |
| struct [in\_addr](structin__addr.md) | [net\_if\_ipv4\_get\_gw](#gae42f6f9620e40e2d2b36d30e81bb82d9) (struct [net\_if](structnet__if.md) \*iface) |
|  | Get IPv4 gateway of an interface. |
| void | [net\_if\_ipv4\_set\_gw](#ga310ccbd9b37629422ca8e32836362724) (struct [net\_if](structnet__if.md) \*iface, const struct [in\_addr](structin__addr.md) \*gw) |
|  | Set IPv4 gateway for an interface. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_ipv4\_set\_gw\_by\_index](#gadef49124c331817165475c69fb9104e0) (int index, const struct [in\_addr](structin__addr.md) \*gw) |
|  | Set IPv4 gateway for an interface index. |
| struct [net\_if](structnet__if.md) \* | [net\_if\_select\_src\_iface](#ga001b1cdde5febcf3970848c7c185c81c) (const struct [sockaddr](structsockaddr.md) \*dst) |
|  | Get a network interface that should be used when sending IPv6 or IPv4 network data to destination. |
| void | [net\_if\_register\_link\_cb](#gaa81b7d9ed8dc05da3391265dbc89b665) (struct [net\_if\_link\_cb](structnet__if__link__cb.md) \*link, [net\_if\_link\_callback\_t](#ga0f87d5753fcd7cce40ecd161e6c91078) cb) |
|  | Register a link callback. |
| void | [net\_if\_unregister\_link\_cb](#ga6ba64fac6e8d846ae7be5990f49a8293) (struct [net\_if\_link\_cb](structnet__if__link__cb.md) \*link) |
|  | Unregister a link callback. |
| void | [net\_if\_call\_link\_cb](#gaaa64aa4391a85760bb2daf600ac4d898) (struct [net\_if](structnet__if.md) \*iface, struct [net\_linkaddr](structnet__linkaddr.md) \*lladdr, int status) |
|  | Call a link callback function. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_need\_calc\_rx\_checksum](#ga8048e722f6442bcd5b6881bd71e791a5) (struct [net\_if](structnet__if.md) \*iface, enum [net\_if\_checksum\_type](#ga8db412ae79c64cafe81a66f5acb2f8e9) chksum\_type) |
|  | Check if received network packet checksum calculation can be avoided or not. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_need\_calc\_tx\_checksum](#ga9634c3e71e934ab3a07bec989b364663) (struct [net\_if](structnet__if.md) \*iface, enum [net\_if\_checksum\_type](#ga8db412ae79c64cafe81a66f5acb2f8e9) chksum\_type) |
|  | Check if network packet checksum calculation can be avoided or not when sending the packet. |
| struct [net\_if](structnet__if.md) \* | [net\_if\_get\_by\_index](#ga72708cdb7f133fe5d7edf819756c3516) (int index) |
|  | Get interface according to index. |
| int | [net\_if\_get\_by\_iface](#ga02445f6c61f0d29f56ac0ef59e025630) (struct [net\_if](structnet__if.md) \*iface) |
|  | Get interface index according to pointer. |
| void | [net\_if\_foreach](#ga96b198fd9df4a985b0dde84dd7152815) ([net\_if\_cb\_t](#gac48ab8e6337e7cf387af9b293f254a80) cb, void \*user\_data) |
|  | Go through all the network interfaces and call callback for each interface. |
| int | [net\_if\_up](#ga02644cc623fc7a8878c17d54984e4210) (struct [net\_if](structnet__if.md) \*iface) |
|  | Bring interface up. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_is\_up](#ga7e9b368d4abf9da5656140df70cfa334) (struct [net\_if](structnet__if.md) \*iface) |
|  | Check if interface is up and running. |
| int | [net\_if\_down](#ga2187650062d6139b9f4b81745a206803) (struct [net\_if](structnet__if.md) \*iface) |
|  | Bring interface down. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_is\_admin\_up](#ga099a484a654ad9af35d3212fc2c995b2) (struct [net\_if](structnet__if.md) \*iface) |
|  | Check if interface was brought up by the administrator. |
| void | [net\_if\_carrier\_on](#ga35e5db3a631ac9039f14d86e59fc0dcc) (struct [net\_if](structnet__if.md) \*iface) |
|  | Underlying network device has detected the carrier (cable connected). |
| void | [net\_if\_carrier\_off](#ga6839941422a88c1f707ab70ea34df323) (struct [net\_if](structnet__if.md) \*iface) |
|  | Underlying network device has lost the carrier (cable disconnected). |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_is\_carrier\_ok](#ga095554237016e563d76cfd602d1dae77) (struct [net\_if](structnet__if.md) \*iface) |
|  | Check if carrier is present on network device. |
| void | [net\_if\_dormant\_on](#ga89a3374d4bb116460a7b7c50a750b593) (struct [net\_if](structnet__if.md) \*iface) |
|  | Mark interface as dormant. |
| void | [net\_if\_dormant\_off](#ga1c31fac887d944ac0a16aad70e889496) (struct [net\_if](structnet__if.md) \*iface) |
|  | Mark interface as not dormant. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_is\_dormant](#ga6e2e6102271c37acaa59c54e2aa6b413) (struct [net\_if](structnet__if.md) \*iface) |
|  | Check if the interface is dormant. |
| static int | [net\_if\_set\_promisc](#gaf9f81f3b9697ca47f7674d85f37a8d80) (struct [net\_if](structnet__if.md) \*iface) |
|  | Set network interface into promiscuous mode. |
| static void | [net\_if\_unset\_promisc](#ga9c8212c087883510050ac6a39ef0a7bf) (struct [net\_if](structnet__if.md) \*iface) |
|  | Set network interface into normal mode. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_is\_promisc](#ga9f1a6eab849517734ec422deb0ba71f5) (struct [net\_if](structnet__if.md) \*iface) |
|  | Check if promiscuous mode is set or not. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_are\_pending\_tx\_packets](#ga3cddda628eca248246f9aa3b81938f95) (struct [net\_if](structnet__if.md) \*iface) |
|  | Check if there are any pending TX network data for a given network interface. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_if\_is\_wifi](#gaa458b5f349c55007108b47b99f4954d5) (struct [net\_if](structnet__if.md) \*iface) |
|  | Check if the network interface supports Wi-Fi. |
| struct [net\_if](structnet__if.md) \* | [net\_if\_get\_first\_wifi](#ga6e89bbafb6c0acdc6bf51078e2027236) (void) |
|  | Get first Wi-Fi network interface. |
| struct [net\_if](structnet__if.md) \* | [net\_if\_get\_wifi\_sta](#ga0fc3ba6172956f6847027e0bd3d367de) (void) |
|  | Get Wi-Fi network station interface. |
| struct [net\_if](structnet__if.md) \* | [net\_if\_get\_wifi\_sap](#gaf830eab616191009d88f58b761694b49) (void) |
|  | Get first Wi-Fi network Soft-AP interface. |
| int | [net\_if\_get\_name](#ga5f653cd73c1ecd548a931eb7fbd170f7) (struct [net\_if](structnet__if.md) \*iface, char \*buf, int len) |
|  | Get network interface name. |
| int | [net\_if\_set\_name](#ga05dec64966fc39e3deb0679b9585688b) (struct [net\_if](structnet__if.md) \*iface, const char \*buf) |
|  | Set network interface name. |
| int | [net\_if\_get\_by\_name](#ga1774ac036032bb0dc2c662f6f4f66a7f) (const char \*name) |
|  | Get interface index according to its name. |

## Detailed Description

Network Interface abstraction layer.

Since
:   1.5

Version
:   1.0.0

## Macro Definition Documentation

## [◆ ](#gab1f762b01ae7bc37cd4a25724c123dda)NET\_DEVICE\_DT\_DEFINE

| #define NET\_DEVICE\_DT\_DEFINE | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *init\_fn*, |
|  |  |  | *pm*, |
|  |  |  | *data*, |
|  |  |  | *config*, |
|  |  |  | *prio*, |
|  |  |  | *api*, |
|  |  |  | *l2*, |
|  |  |  | *l2\_ctx\_type*, |
|  |  |  | *mtu* ) |

`#include <[net_if.h](net__if_8h.md)>`

**Value:**

Z\_NET\_DEVICE\_INIT(node\_id, Z\_DEVICE\_DT\_DEV\_ID(node\_id), \

[DEVICE\_DT\_NAME](group__device__model.md#gad864d7a50ee45285dacd68be1e5a49ce)(node\_id), init\_fn, pm, data, \

config, prio, api, l2, l2\_ctx\_type, mtu)

[DEVICE\_DT\_NAME](group__device__model.md#gad864d7a50ee45285dacd68be1e5a49ce)

#define DEVICE\_DT\_NAME(node\_id)

Return a string name for a devicetree node.

**Definition** device.h:185

Like NET\_DEVICE\_INIT but taking metadata from a devicetree node.

Create a network interface and bind it to network device.

Parameters
:   | node\_id | The devicetree node identifier. |
    | --- | --- |
    | init\_fn | Address to the init function of the driver. |
    | pm | Reference to struct [pm\_device](structpm__device.md "Runtime PM info for device with generic PM.") associated with the device. (optional). |
    | data | Pointer to the device's private data. |
    | config | The address to the structure containing the configuration information for this instance of the driver. |
    | prio | The initialization level at which configuration occurs. |
    | api | Provides an initial pointer to the API function struct used by the driver. Can be NULL. |
    | l2 | Network L2 layer for this network interface. |
    | l2\_ctx\_type | Type of L2 context data. |
    | mtu | Maximum transfer unit in bytes for this network interface. |

## [◆ ](#ga50702b043a0791e59e7d5679dda1d9e8)NET\_DEVICE\_DT\_DEFINE\_INSTANCE

| #define NET\_DEVICE\_DT\_DEFINE\_INSTANCE | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *instance*, |
|  |  |  | *init\_fn*, |
|  |  |  | *pm*, |
|  |  |  | *data*, |
|  |  |  | *config*, |
|  |  |  | *prio*, |
|  |  |  | *api*, |
|  |  |  | *l2*, |
|  |  |  | *l2\_ctx\_type*, |
|  |  |  | *mtu* ) |

`#include <[net_if.h](net__if_8h.md)>`

**Value:**

Z\_NET\_DEVICE\_INIT\_INSTANCE(node\_id, \

Z\_DEVICE\_DT\_DEV\_ID(node\_id), \

[DEVICE\_DT\_NAME](group__device__model.md#gad864d7a50ee45285dacd68be1e5a49ce)(node\_id), instance, \

init\_fn, pm, data, config, prio, \

api, l2, l2\_ctx\_type, mtu)

Like NET\_DEVICE\_OFFLOAD\_INIT but taking metadata from a devicetree.

Create multiple network interfaces and bind them to network device. If your network device needs more than one instance of a network interface, use this macro below and provide a different instance suffix each time (0, 1, 2, ... or a, b, c ... whatever works for you)

Parameters
:   | node\_id | The devicetree node identifier. |
    | --- | --- |
    | instance | Instance identifier. |
    | init\_fn | Address to the init function of the driver. |
    | pm | Reference to struct [pm\_device](structpm__device.md "Runtime PM info for device with generic PM.") associated with the device. (optional). |
    | data | Pointer to the device's private data. |
    | config | The address to the structure containing the configuration information for this instance of the driver. |
    | prio | The initialization level at which configuration occurs. |
    | api | Provides an initial pointer to the API function struct used by the driver. Can be NULL. |
    | l2 | Network L2 layer for this network interface. |
    | l2\_ctx\_type | Type of L2 context data. |
    | mtu | Maximum transfer unit in bytes for this network interface. |

## [◆ ](#ga7edd8bc59444d92cad0371c36f9949b7)NET\_DEVICE\_DT\_INST\_DEFINE

| #define NET\_DEVICE\_DT\_INST\_DEFINE | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[net_if.h](net__if_8h.md)>`

**Value:**

[NET\_DEVICE\_DT\_DEFINE](#gab1f762b01ae7bc37cd4a25724c123dda)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), \_\_VA\_ARGS\_\_)

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3909

[NET\_DEVICE\_DT\_DEFINE](#gab1f762b01ae7bc37cd4a25724c123dda)

#define NET\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, config, prio, api, l2, l2\_ctx\_type, mtu)

Like NET\_DEVICE\_INIT but taking metadata from a devicetree node.

**Definition** net\_if.h:3401

Like NET\_DEVICE\_DT\_DEFINE for an instance of a DT\_DRV\_COMPAT compatible.

Parameters
:   | inst | instance number. This is replaced by DT\_DRV\_COMPAT(inst) in the call to NET\_DEVICE\_DT\_DEFINE. |
    | --- | --- |
    | ... | other parameters as expected by NET\_DEVICE\_DT\_DEFINE. |

## [◆ ](#gabe4b8589996a53cbc50b76c8ea15aa0c)NET\_DEVICE\_DT\_INST\_DEFINE\_INSTANCE

| #define NET\_DEVICE\_DT\_INST\_DEFINE\_INSTANCE | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[net_if.h](net__if_8h.md)>`

**Value:**

[NET\_DEVICE\_DT\_DEFINE\_INSTANCE](#ga50702b043a0791e59e7d5679dda1d9e8)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), \_\_VA\_ARGS\_\_)

[NET\_DEVICE\_DT\_DEFINE\_INSTANCE](#ga50702b043a0791e59e7d5679dda1d9e8)

#define NET\_DEVICE\_DT\_DEFINE\_INSTANCE(node\_id, instance, init\_fn, pm, data, config, prio, api, l2, l2\_ctx\_type, mtu)

Like NET\_DEVICE\_OFFLOAD\_INIT but taking metadata from a devicetree.

**Definition** net\_if.h:3470

Like NET\_DEVICE\_DT\_DEFINE\_INSTANCE for an instance of a DT\_DRV\_COMPAT compatible.

Parameters
:   | inst | instance number. This is replaced by DT\_DRV\_COMPAT(inst) in the call to NET\_DEVICE\_DT\_DEFINE\_INSTANCE. |
    | --- | --- |
    | ... | other parameters as expected by NET\_DEVICE\_DT\_DEFINE\_INSTANCE. |

## [◆ ](#ga1cab6943a28e3d3754e36623834b93fd)NET\_DEVICE\_DT\_INST\_OFFLOAD\_DEFINE

| #define NET\_DEVICE\_DT\_INST\_OFFLOAD\_DEFINE | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[net_if.h](net__if_8h.md)>`

**Value:**

[NET\_DEVICE\_DT\_OFFLOAD\_DEFINE](#gab2b287025e194dec1fab24e44d95362f)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), \_\_VA\_ARGS\_\_)

[NET\_DEVICE\_DT\_OFFLOAD\_DEFINE](#gab2b287025e194dec1fab24e44d95362f)

#define NET\_DEVICE\_DT\_OFFLOAD\_DEFINE(node\_id, init\_fn, pm, data, config, prio, api, mtu)

Like NET\_DEVICE\_OFFLOAD\_INIT but taking metadata from a devicetree node.

**Definition** net\_if.h:3542

Like NET\_DEVICE\_DT\_OFFLOAD\_DEFINE for an instance of a DT\_DRV\_COMPAT compatible.

Parameters
:   | inst | instance number. This is replaced by DT\_DRV\_COMPAT(inst) in the call to NET\_DEVICE\_DT\_OFFLOAD\_DEFINE. |
    | --- | --- |
    | ... | other parameters as expected by NET\_DEVICE\_DT\_OFFLOAD\_DEFINE. |

## [◆ ](#gab2b287025e194dec1fab24e44d95362f)NET\_DEVICE\_DT\_OFFLOAD\_DEFINE

| #define NET\_DEVICE\_DT\_OFFLOAD\_DEFINE | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *init\_fn*, |
|  |  |  | *pm*, |
|  |  |  | *data*, |
|  |  |  | *config*, |
|  |  |  | *prio*, |
|  |  |  | *api*, |
|  |  |  | *mtu* ) |

`#include <[net_if.h](net__if_8h.md)>`

**Value:**

Z\_NET\_DEVICE\_OFFLOAD\_INIT(node\_id, Z\_DEVICE\_DT\_DEV\_ID(node\_id), \

[DEVICE\_DT\_NAME](group__device__model.md#gad864d7a50ee45285dacd68be1e5a49ce)(node\_id), init\_fn, pm, \

data, config, prio, api, mtu)

Like NET\_DEVICE\_OFFLOAD\_INIT but taking metadata from a devicetree node.

Create a offloaded network interface and bind it to network device. The offloaded network interface is implemented by a device vendor HAL or similar.

Parameters
:   | node\_id | The devicetree node identifier. |
    | --- | --- |
    | init\_fn | Address to the init function of the driver. |
    | pm | Reference to struct [pm\_device](structpm__device.md "Runtime PM info for device with generic PM.") associated with the device. (optional). |
    | data | Pointer to the device's private data. |
    | config | The address to the structure containing the configuration information for this instance of the driver. |
    | prio | The initialization level at which configuration occurs. |
    | api | Provides an initial pointer to the API function struct used by the driver. Can be NULL. |
    | mtu | Maximum transfer unit in bytes for this network interface. |

## [◆ ](#ga02971562c42494e2a5f71e1f8587e709)NET\_DEVICE\_INIT

| #define NET\_DEVICE\_INIT | ( |  | *dev\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name*, |
|  |  |  | *init\_fn*, |
|  |  |  | *pm*, |
|  |  |  | *data*, |
|  |  |  | *config*, |
|  |  |  | *prio*, |
|  |  |  | *api*, |
|  |  |  | *l2*, |
|  |  |  | *l2\_ctx\_type*, |
|  |  |  | *mtu* ) |

`#include <[net_if.h](net__if_8h.md)>`

**Value:**

Z\_NET\_DEVICE\_INIT([DT\_INVALID\_NODE](group__devicetree-generic-id.md#ga710cc4455dd7e738f43f750153163855), dev\_id, name, init\_fn, pm, \

data, config, prio, api, l2, l2\_ctx\_type, mtu)

[DT\_INVALID\_NODE](group__devicetree-generic-id.md#ga710cc4455dd7e738f43f750153163855)

#define DT\_INVALID\_NODE

Name for an invalid node identifier.

**Definition** devicetree.h:83

Create a network interface and bind it to network device.

Parameters
:   | dev\_id | Network device id. |
    | --- | --- |
    | name | The name this instance of the driver exposes to the system. |
    | init\_fn | Address to the init function of the driver. |
    | pm | Reference to struct [pm\_device](structpm__device.md "Runtime PM info for device with generic PM.") associated with the device. (optional). |
    | data | Pointer to the device's private data. |
    | config | The address to the structure containing the configuration information for this instance of the driver. |
    | prio | The initialization level at which configuration occurs. |
    | api | Provides an initial pointer to the API function struct used by the driver. Can be NULL. |
    | l2 | Network L2 layer for this network interface. |
    | l2\_ctx\_type | Type of L2 context data. |
    | mtu | Maximum transfer unit in bytes for this network interface. |

## [◆ ](#gacc7edecdd9de9920cc155977d8fec2a2)NET\_DEVICE\_INIT\_INSTANCE

| #define NET\_DEVICE\_INIT\_INSTANCE | ( |  | *dev\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name*, |
|  |  |  | *instance*, |
|  |  |  | *init\_fn*, |
|  |  |  | *pm*, |
|  |  |  | *data*, |
|  |  |  | *config*, |
|  |  |  | *prio*, |
|  |  |  | *api*, |
|  |  |  | *l2*, |
|  |  |  | *l2\_ctx\_type*, |
|  |  |  | *mtu* ) |

`#include <[net_if.h](net__if_8h.md)>`

**Value:**

Z\_NET\_DEVICE\_INIT\_INSTANCE([DT\_INVALID\_NODE](group__devicetree-generic-id.md#ga710cc4455dd7e738f43f750153163855), dev\_id, name, \

instance, init\_fn, pm, data, config, \

prio, api, l2, l2\_ctx\_type, mtu)

Create multiple network interfaces and bind them to network device.

If your network device needs more than one instance of a network interface, use this macro below and provide a different instance suffix each time (0, 1, 2, ... or a, b, c ... whatever works for you)

Parameters
:   | dev\_id | Network device id. |
    | --- | --- |
    | name | The name this instance of the driver exposes to the system. |
    | instance | Instance identifier. |
    | init\_fn | Address to the init function of the driver. |
    | pm | Reference to struct [pm\_device](structpm__device.md "Runtime PM info for device with generic PM.") associated with the device. (optional). |
    | data | Pointer to the device's private data. |
    | config | The address to the structure containing the configuration information for this instance of the driver. |
    | prio | The initialization level at which configuration occurs. |
    | api | Provides an initial pointer to the API function struct used by the driver. Can be NULL. |
    | l2 | Network L2 layer for this network interface. |
    | l2\_ctx\_type | Type of L2 context data. |
    | mtu | Maximum transfer unit in bytes for this network interface. |

## [◆ ](#ga255672607b7958db3f464d2a57a7e635)NET\_DEVICE\_OFFLOAD\_INIT

| #define NET\_DEVICE\_OFFLOAD\_INIT | ( |  | *dev\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name*, |
|  |  |  | *init\_fn*, |
|  |  |  | *pm*, |
|  |  |  | *data*, |
|  |  |  | *config*, |
|  |  |  | *prio*, |
|  |  |  | *api*, |
|  |  |  | *mtu* ) |

`#include <[net_if.h](net__if_8h.md)>`

**Value:**

Z\_NET\_DEVICE\_OFFLOAD\_INIT([DT\_INVALID\_NODE](group__devicetree-generic-id.md#ga710cc4455dd7e738f43f750153163855), dev\_id, name, \

init\_fn, pm, data, config, prio, api, \

mtu)

Create a offloaded network interface and bind it to network device.

The offloaded network interface is implemented by a device vendor HAL or similar.

Parameters
:   | dev\_id | Network device id. |
    | --- | --- |
    | name | The name this instance of the driver exposes to the system. |
    | init\_fn | Address to the init function of the driver. |
    | pm | Reference to struct [pm\_device](structpm__device.md "Runtime PM info for device with generic PM.") associated with the device. (optional). |
    | data | Pointer to the device's private data. |
    | config | The address to the structure containing the configuration information for this instance of the driver. |
    | prio | The initialization level at which configuration occurs. |
    | api | Provides an initial pointer to the API function struct used by the driver. Can be NULL. |
    | mtu | Maximum transfer unit in bytes for this network interface. |

## [◆ ](#ga6c081875a6f5a848b3ad2fd220c63c3c)NET\_IFACE\_COUNT

| #define NET\_IFACE\_COUNT | ( |  | *\_dst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

**Value:**

do { \

extern struct [net\_if](structnet__if.md) \_net\_if\_list\_start[]; \

extern struct [net\_if](structnet__if.md) \_net\_if\_list\_end[]; \

\*(\_dst) = (([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))\_net\_if\_list\_end - \

([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))\_net\_if\_list\_start) / \

sizeof(struct [net\_if](structnet__if.md)); \

} while (0)

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[net\_if](structnet__if.md)

Network Interface structure.

**Definition** net\_if.h:714

Count the number of network interfaces.

Parameters
:   | [out] | \_dst | Pointer to location where result is written. |
    | --- | --- | --- |

## Typedef Documentation

## [◆ ](#gac48ab8e6337e7cf387af9b293f254a80)net\_if\_cb\_t

| typedef void(\* net\_if\_cb\_t) (struct [net\_if](structnet__if.md) \*iface, void \*user\_data) |
| --- |

`#include <[net_if.h](net__if_8h.md)>`

Callback used while iterating over network interfaces.

Parameters
:   | iface | Pointer to current network interface |
    | --- | --- |
    | user\_data | A valid pointer to user data or NULL |

## [◆ ](#gab58d8561a4f21899e2db34043d346516)net\_if\_ip\_addr\_cb\_t

| typedef void(\* net\_if\_ip\_addr\_cb\_t) (struct [net\_if](structnet__if.md) \*iface, struct [net\_if\_addr](structnet__if__addr.md) \*addr, void \*user\_data) |
| --- |

`#include <[net_if.h](net__if_8h.md)>`

Callback used while iterating over network interface IP addresses.

Parameters
:   | iface | Pointer to the network interface the address belongs to |
    | --- | --- |
    | addr | Pointer to current IP address |
    | user\_data | A valid pointer to user data or NULL |

## [◆ ](#ga726eed76563c223de8f611e2544febe9)net\_if\_ip\_maddr\_cb\_t

| typedef void(\* net\_if\_ip\_maddr\_cb\_t) (struct [net\_if](structnet__if.md) \*iface, struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \*maddr, void \*user\_data) |
| --- |

`#include <[net_if.h](net__if_8h.md)>`

Callback used while iterating over network interface multicast IP addresses.

Parameters
:   | iface | Pointer to the network interface the address belongs to |
    | --- | --- |
    | maddr | Pointer to current multicast IP address |
    | user\_data | A valid pointer to user data or NULL |

## [◆ ](#ga0f87d5753fcd7cce40ecd161e6c91078)net\_if\_link\_callback\_t

| typedef void(\* net\_if\_link\_callback\_t) (struct [net\_if](structnet__if.md) \*iface, struct [net\_linkaddr](structnet__linkaddr.md) \*dst, int status) |
| --- |

`#include <[net_if.h](net__if_8h.md)>`

Define callback that is called after a network packet has been sent.

Parameters
:   | iface | A pointer to a struct [net\_if](structnet__if.md "Network Interface structure.") to which the [net\_pkt](structnet__pkt.md "Network packet.") was sent to. |
    | --- | --- |
    | dst | Link layer address of the destination where the network packet was sent. |
    | status | Send status, 0 is ok, < 0 error. |

## [◆ ](#ga0d64291573740a67eae7ff3fcc0910c5)net\_if\_mcast\_callback\_t

| typedef void(\* net\_if\_mcast\_callback\_t) (struct [net\_if](structnet__if.md) \*iface, const struct net\_addr \*addr, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) is\_joined) |
| --- |

`#include <[net_if.h](net__if_8h.md)>`

Define a callback that is called whenever a IPv6 or IPv4 multicast address group is joined or left.

Parameters
:   | iface | A pointer to a struct [net\_if](structnet__if.md "Network Interface structure.") to which the multicast address is attached. |
    | --- | --- |
    | addr | IP multicast address. |
    | is\_joined | True if the multicast group is joined, false if group is left. |

## [◆ ](#gaef3dfe26195514aac625e9f22e399759)net\_socket\_create\_t

| typedef int(\* net\_socket\_create\_t) (int, int, int) |
| --- |

`#include <[net_if.h](net__if_8h.md)>`

A function prototype to create an offloaded socket.

The prototype is compatible with [socket()](posix_2sys_2socket_8h.md#a4dcc080bfb18d95d173bc205084f8b0a) function.

## Enumeration Type Documentation

## [◆ ](#ga8db412ae79c64cafe81a66f5acb2f8e9)net\_if\_checksum\_type

| enum [net\_if\_checksum\_type](#ga8db412ae79c64cafe81a66f5acb2f8e9) |
| --- |

`#include <[net_if.h](net__if_8h.md)>`

Type of checksum for which support in the interface will be queried.

| Enumerator | |
| --- | --- |
| NET\_IF\_CHECKSUM\_IPV4\_HEADER | Interface supports IP version 4 header checksum calculation. |
| NET\_IF\_CHECKSUM\_IPV4\_TCP | Interface supports checksum calculation for TCP payload in IPv4. |
| NET\_IF\_CHECKSUM\_IPV4\_UDP | Interface supports checksum calculation for UDP payload in IPv4. |
| NET\_IF\_CHECKSUM\_IPV4\_ICMP | Interface supports checksum calculation for ICMP4 payload in IPv4. |
| NET\_IF\_CHECKSUM\_IPV6\_HEADER | Interface supports IP version 6 header checksum calculation. |
| NET\_IF\_CHECKSUM\_IPV6\_TCP | Interface supports checksum calculation for TCP payload in IPv6. |
| NET\_IF\_CHECKSUM\_IPV6\_UDP | Interface supports checksum calculation for UDP payload in IPv6. |
| NET\_IF\_CHECKSUM\_IPV6\_ICMP | Interface supports checksum calculation for ICMP6 payload in IPv6. |

## [◆ ](#gae691e5537917ffce27ad0db82c730371)net\_if\_flag

| enum [net\_if\_flag](#gae691e5537917ffce27ad0db82c730371) |
| --- |

`#include <[net_if.h](net__if_8h.md)>`

Network interface flags.

| Enumerator | |
| --- | --- |
| NET\_IF\_UP | Interface is admin up. |
| NET\_IF\_POINTOPOINT | Interface is pointopoint. |
| NET\_IF\_PROMISC | Interface is in promiscuous mode. |
| NET\_IF\_NO\_AUTO\_START | Do not start the interface immediately after initialization.  This requires that either the device driver or some other entity will need to manually take the interface up when needed. For example for Ethernet this will happen when the driver calls the [net\_eth\_carrier\_on()](group__ethernet.md#gabeb21cb06b18674b73fbd0f42ee726f0 "Inform ethernet L2 driver that ethernet carrier is detected.") function. |
| NET\_IF\_SUSPENDED | Power management specific: interface is being suspended. |
| NET\_IF\_FORWARD\_MULTICASTS | Flag defines if received multicasts of other interface are forwarded on this interface.  This activates multicast routing / forwarding for this interface. |
| NET\_IF\_IPV4 | Interface supports IPv4. |
| NET\_IF\_IPV6 | Interface supports IPv6. |
| NET\_IF\_RUNNING | Interface up and running (ready to receive and transmit). |
| NET\_IF\_LOWER\_UP | Driver signals L1 is up. |
| NET\_IF\_DORMANT | Driver signals dormant. |
| NET\_IF\_IPV6\_NO\_ND | IPv6 Neighbor Discovery disabled. |
| NET\_IF\_IPV6\_NO\_MLD | IPv6 Multicast Listener Discovery disabled. |
| NET\_IF\_NO\_TX\_LOCK | Mutex locking on TX data path disabled on the interface. |

## [◆ ](#gadfe9d90f24046cd9bd4bbee096e747b9)net\_if\_oper\_state

| enum [net\_if\_oper\_state](#gadfe9d90f24046cd9bd4bbee096e747b9) |
| --- |

`#include <[net_if.h](net__if_8h.md)>`

Network interface operational status (RFC 2863).

| Enumerator | |
| --- | --- |
| NET\_IF\_OPER\_UNKNOWN | Initial (unknown) value. |
| NET\_IF\_OPER\_NOTPRESENT | Hardware missing. |
| NET\_IF\_OPER\_DOWN | Interface is down. |
| NET\_IF\_OPER\_LOWERLAYERDOWN | Lower layer interface is down. |
| NET\_IF\_OPER\_TESTING | Training mode. |
| NET\_IF\_OPER\_DORMANT | Waiting external action. |
| NET\_IF\_OPER\_UP | Interface is up. |

## Function Documentation

## [◆ ](#gae66f6e7bd31545e6161fcd4600fe5842)net\_if\_addr\_set\_lf()

| | void net\_if\_addr\_set\_lf | ( | struct [net\_if\_addr](structnet__if__addr.md) \* | *ifaddr*, | | --- | --- | --- | --- | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *is\_infinite* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Set the infinite status of the network interface address.

Parameters
:   | ifaddr | IP address for network interface |
    | --- | --- |
    | is\_infinite | Infinite status |

## [◆ ](#ga3cddda628eca248246f9aa3b81938f95)net\_if\_are\_pending\_tx\_packets()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_if\_are\_pending\_tx\_packets | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Check if there are any pending TX network data for a given network interface.

Parameters
:   | iface | Pointer to network interface |
    | --- | --- |

Returns
:   True if there are pending TX network packets for this network interface, False otherwise.

## [◆ ](#gaaa64aa4391a85760bb2daf600ac4d898)net\_if\_call\_link\_cb()

| void net\_if\_call\_link\_cb | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | struct [net\_linkaddr](structnet__linkaddr.md) \* | *lladdr*, |
|  |  | int | *status* ) |

`#include <[net_if.h](net__if_8h.md)>`

Call a link callback function.

Parameters
:   | iface | Network interface. |
    | --- | --- |
    | lladdr | Destination link layer address |
    | status | 0 is ok, < 0 error |

## [◆ ](#ga6839941422a88c1f707ab70ea34df323)net\_if\_carrier\_off()

| void net\_if\_carrier\_off | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Underlying network device has lost the carrier (cable disconnected).

The function should be used by the respective network device driver or L2 implementation to update its state on a network interface.

Parameters
:   | iface | Pointer to network interface |
    | --- | --- |

## [◆ ](#ga35e5db3a631ac9039f14d86e59fc0dcc)net\_if\_carrier\_on()

| void net\_if\_carrier\_on | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Underlying network device has detected the carrier (cable connected).

The function should be used by the respective network device driver or L2 implementation to update its state on a network interface.

Parameters
:   | iface | Pointer to network interface |
    | --- | --- |

## [◆ ](#gae2323a72714e29836d8296dfc330f7fd)net\_if\_config\_get()

| | struct [net\_if\_config](structnet__if__config.md) \* net\_if\_config\_get | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Get network interface IP config.

Parameters
:   | iface | Interface to use. |
    | --- | --- |

Returns
:   NULL if not found or pointer to correct config settings.

## [◆ ](#ga3390e248249b28f2c80e2ca0bc79d236)net\_if\_config\_ipv4\_get()

| int net\_if\_config\_ipv4\_get | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | struct [net\_if\_ipv4](structnet__if__ipv4.md) \*\* | *ipv4* ) |

`#include <[net_if.h](net__if_8h.md)>`

Allocate network interface IPv4 config.

This function will allocate new IPv4 config.

Parameters
:   | iface | Interface to use. |
    | --- | --- |
    | ipv4 | Pointer to allocated IPv4 struct is returned to caller. |

Returns
:   0 if ok, <0 if error

## [◆ ](#ga88c13a45617480a665c7f9f589ec8e10)net\_if\_config\_ipv4\_put()

| int net\_if\_config\_ipv4\_put | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Release network interface IPv4 config.

Parameters
:   | iface | Interface to use. |
    | --- | --- |

Returns
:   0 if ok, <0 if error

## [◆ ](#ga56c9aef19bc9827d9ec96c00e10840fa)net\_if\_config\_ipv6\_get()

| int net\_if\_config\_ipv6\_get | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | struct [net\_if\_ipv6](structnet__if__ipv6.md) \*\* | *ipv6* ) |

`#include <[net_if.h](net__if_8h.md)>`

Allocate network interface IPv6 config.

This function will allocate new IPv6 config.

Parameters
:   | iface | Interface to use. |
    | --- | --- |
    | ipv6 | Pointer to allocated IPv6 struct is returned to caller. |

Returns
:   0 if ok, <0 if error

## [◆ ](#ga8af1400b354c42a64795cdb1a600ddd6)net\_if\_config\_ipv6\_put()

| int net\_if\_config\_ipv6\_put | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Release network interface IPv6 config.

Parameters
:   | iface | Interface to use. |
    | --- | --- |

Returns
:   0 if ok, <0 if error

## [◆ ](#ga1c31fac887d944ac0a16aad70e889496)net\_if\_dormant\_off()

| void net\_if\_dormant\_off | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Mark interface as not dormant.

The function should be used by the respective network device driver or L2 implementation to update its state on a network interface.

Parameters
:   | iface | Pointer to network interface |
    | --- | --- |

## [◆ ](#ga89a3374d4bb116460a7b7c50a750b593)net\_if\_dormant\_on()

| void net\_if\_dormant\_on | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Mark interface as dormant.

Dormant state indicates that the interface is not ready to pass packets yet, but is waiting for some event (for example Wi-Fi network association).

The function should be used by the respective network device driver or L2 implementation to update its state on a network interface.

Parameters
:   | iface | Pointer to network interface |
    | --- | --- |

## [◆ ](#ga2187650062d6139b9f4b81745a206803)net\_if\_down()

| int net\_if\_down | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Bring interface down.

Parameters
:   | iface | Pointer to network interface |
    | --- | --- |

Returns
:   0 on success

## [◆ ](#gaff751b6a92b0c608ecfc50e8c0587fd3)net\_if\_flag\_clear()

| | void net\_if\_flag\_clear | ( | struct [net\_if](structnet__if.md) \* | *iface*, | | --- | --- | --- | --- | |  |  | enum [net\_if\_flag](#gae691e5537917ffce27ad0db82c730371) | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Clear a value in network interface flags.

Parameters
:   | iface | Pointer to network interface |
    | --- | --- |
    | value | Flag value |

## [◆ ](#gae1f373ddd61c18a81481d8ddcfb12543)net\_if\_flag\_is\_set()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_if\_flag\_is\_set | ( | struct [net\_if](structnet__if.md) \* | *iface*, | | --- | --- | --- | --- | |  |  | enum [net\_if\_flag](#gae691e5537917ffce27ad0db82c730371) | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Check if a value in network interface flags is set.

Parameters
:   | iface | Pointer to network interface |
    | --- | --- |
    | value | Flag value |

Returns
:   True if the value is set, false otherwise

## [◆ ](#ga52f9fca13e9f836799e0e40f581744d2)net\_if\_flag\_set()

| | void net\_if\_flag\_set | ( | struct [net\_if](structnet__if.md) \* | *iface*, | | --- | --- | --- | --- | |  |  | enum [net\_if\_flag](#gae691e5537917ffce27ad0db82c730371) | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Set a value in network interface flags.

Parameters
:   | iface | Pointer to network interface |
    | --- | --- |
    | value | Flag value |

## [◆ ](#gab8f371c7f8890cf4728177f6595141d7)net\_if\_flag\_test\_and\_clear()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_if\_flag\_test\_and\_clear | ( | struct [net\_if](structnet__if.md) \* | *iface*, | | --- | --- | --- | --- | |  |  | enum [net\_if\_flag](#gae691e5537917ffce27ad0db82c730371) | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Test and clear a value in network interface flags.

Parameters
:   | iface | Pointer to network interface |
    | --- | --- |
    | value | Flag value |

Returns
:   true if the bit was set, false if it wasn't.

## [◆ ](#ga42e7482191a92007960601f8bb621dca)net\_if\_flag\_test\_and\_set()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_if\_flag\_test\_and\_set | ( | struct [net\_if](structnet__if.md) \* | *iface*, | | --- | --- | --- | --- | |  |  | enum [net\_if\_flag](#gae691e5537917ffce27ad0db82c730371) | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Test and set a value in network interface flags.

Parameters
:   | iface | Pointer to network interface |
    | --- | --- |
    | value | Flag value |

Returns
:   true if the bit was set, false if it wasn't.

## [◆ ](#ga96b198fd9df4a985b0dde84dd7152815)net\_if\_foreach()

| void net\_if\_foreach | ( | [net\_if\_cb\_t](#gac48ab8e6337e7cf387af9b293f254a80) | *cb*, |
| --- | --- | --- | --- |
|  |  | void \* | *user\_data* ) |

`#include <[net_if.h](net__if_8h.md)>`

Go through all the network interfaces and call callback for each interface.

Parameters
:   | cb | User-supplied callback function to call |
    | --- | --- |
    | user\_data | User specified data |

## [◆ ](#ga02445f6c61f0d29f56ac0ef59e025630)net\_if\_get\_by\_iface()

| int net\_if\_get\_by\_iface | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Get interface index according to pointer.

Parameters
:   | iface | Pointer to network interface |
    | --- | --- |

Returns
:   Interface index

## [◆ ](#ga72708cdb7f133fe5d7edf819756c3516)net\_if\_get\_by\_index()

| struct [net\_if](structnet__if.md) \* net\_if\_get\_by\_index | ( | int | *index* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Get interface according to index.

This is a syscall only to provide access to the object for purposes of assigning permissions.

Parameters
:   | index | Interface index |
    | --- | --- |

Returns
:   Pointer to interface or NULL if not found.

## [◆ ](#ga1b058361dc9bcac7d842bb49846a0c79)net\_if\_get\_by\_link\_addr()

| struct [net\_if](structnet__if.md) \* net\_if\_get\_by\_link\_addr | ( | struct [net\_linkaddr](structnet__linkaddr.md) \* | *ll\_addr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Get an interface according to link layer address.

Parameters
:   | ll\_addr | Link layer address. |
    | --- | --- |

Returns
:   Network interface or NULL if not found.

## [◆ ](#ga1774ac036032bb0dc2c662f6f4f66a7f)net\_if\_get\_by\_name()

| int net\_if\_get\_by\_name | ( | const char \* | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Get interface index according to its name.

Parameters
:   | name | Name of the network interface |
    | --- | --- |

Returns
:   Interface index

## [◆ ](#gae271e0e4dcb031a83d9908e597a45048)net\_if\_get\_config()

| | struct [net\_if\_config](structnet__if__config.md) \* net\_if\_get\_config | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Return network configuration for this network interface.

Parameters
:   | iface | Pointer to a network interface structure |
    | --- | --- |

Returns
:   Pointer to configuration

## [◆ ](#ga55214771e462cbd4930ffa738813cb87)net\_if\_get\_default()

| struct [net\_if](structnet__if.md) \* net\_if\_get\_default | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Get the default network interface.

Returns
:   Default interface or NULL if no interfaces are configured.

## [◆ ](#gaeb8c703f273bc07ae9bb7a0d8bfe6f3d)net\_if\_get\_device()

| | const struct [device](structdevice.md) \* net\_if\_get\_device | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Get an network interface's device.

Parameters
:   | iface | Pointer to a network interface structure |
    | --- | --- |

Returns
:   a pointer to the device driver instance

## [◆ ](#ga762337e8b66874a0fbf59bdbeba173f5)net\_if\_get\_first\_by\_type()

| struct [net\_if](structnet__if.md) \* net\_if\_get\_first\_by\_type | ( | const struct [net\_l2](structnet__l2.md) \* | *l2* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Get the first network interface according to its type.

Parameters
:   | l2 | Layer 2 type of the network interface. |
    | --- | --- |

Returns
:   First network interface of a given type or NULL if no such interfaces was found.

## [◆ ](#ga03d8c6aebb1412382a9eec636c227238)net\_if\_get\_first\_up()

| struct [net\_if](structnet__if.md) \* net\_if\_get\_first\_up | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Get the first network interface which is up.

Returns
:   First network interface which is up or NULL if all interfaces are down.

## [◆ ](#ga6e89bbafb6c0acdc6bf51078e2027236)net\_if\_get\_first\_wifi()

| struct [net\_if](structnet__if.md) \* net\_if\_get\_first\_wifi | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Get first Wi-Fi network interface.

Returns
:   Pointer to network interface, NULL if not found.

## [◆ ](#ga467186e964bf721e14fed38392f21872)net\_if\_get\_link\_addr()

| | struct [net\_linkaddr](structnet__linkaddr.md) \* net\_if\_get\_link\_addr | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Get an network interface's link address.

Parameters
:   | iface | Pointer to a network interface structure |
    | --- | --- |

Returns
:   a pointer to the network link address

## [◆ ](#gacddc98531c5748db5a34f5c3a3e96e86)net\_if\_get\_mtu()

| | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_if\_get\_mtu | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Get an network interface's MTU.

Parameters
:   | iface | Pointer to a network interface structure |
    | --- | --- |

Returns
:   the MTU

## [◆ ](#ga5f653cd73c1ecd548a931eb7fbd170f7)net\_if\_get\_name()

| int net\_if\_get\_name | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | char \* | *buf*, |
|  |  | int | *len* ) |

`#include <[net_if.h](net__if_8h.md)>`

Get network interface name.

If interface name support is not enabled, empty string is returned.

Parameters
:   | iface | Pointer to network interface |
    | --- | --- |
    | buf | User supplied buffer |
    | len | Length of the user supplied buffer |

Returns
:   Length of the interface name copied to buf, -EINVAL if invalid parameters, -ERANGE if name cannot be copied to the user supplied buffer, -ENOTSUP if interface name support is disabled,

## [◆ ](#gaf830eab616191009d88f58b761694b49)net\_if\_get\_wifi\_sap()

| struct [net\_if](structnet__if.md) \* net\_if\_get\_wifi\_sap | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Get first Wi-Fi network Soft-AP interface.

Returns
:   Pointer to network interface, NULL if not found.

## [◆ ](#ga0fc3ba6172956f6847027e0bd3d367de)net\_if\_get\_wifi\_sta()

| struct [net\_if](structnet__if.md) \* net\_if\_get\_wifi\_sta | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Get Wi-Fi network station interface.

Returns
:   Pointer to network interface, NULL if not found.

## [◆ ](#ga7190958f740cac56de3a13fe688b3b5d)net\_if\_ipv4\_addr\_add()

| struct [net\_if\_addr](structnet__if__addr.md) \* net\_if\_ipv4\_addr\_add | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | struct [in\_addr](structin__addr.md) \* | *addr*, |
|  |  | enum [net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41) | *addr\_type*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *vlifetime* ) |

`#include <[net_if.h](net__if_8h.md)>`

Add a IPv4 address to an interface.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | addr | IPv4 address |
    | addr\_type | IPv4 address type |
    | vlifetime | Validity time for this address |

Returns
:   Pointer to interface address, NULL if cannot be added

## [◆ ](#gad140a69cf510ad99a8a8c770bab95bc9)net\_if\_ipv4\_addr\_add\_by\_index()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_if\_ipv4\_addr\_add\_by\_index | ( | int | *index*, |
| --- | --- | --- | --- |
|  |  | struct [in\_addr](structin__addr.md) \* | *addr*, |
|  |  | enum [net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41) | *addr\_type*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *vlifetime* ) |

`#include <[net_if.h](net__if_8h.md)>`

Add a IPv4 address to an interface by network interface index.

Parameters
:   | index | Network interface index |
    | --- | --- |
    | addr | IPv4 address |
    | addr\_type | IPv4 address type |
    | vlifetime | Validity time for this address |

Returns
:   True if ok, false if the address could not be added

## [◆ ](#gaae71be476e27c178ebb21b0f183c2825)net\_if\_ipv4\_addr\_foreach()

| void net\_if\_ipv4\_addr\_foreach | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | [net\_if\_ip\_addr\_cb\_t](#gab58d8561a4f21899e2db34043d346516) | *cb*, |
|  |  | void \* | *user\_data* ) |

`#include <[net_if.h](net__if_8h.md)>`

Go through all IPv4 addresses on a network interface and call callback for each used address.

Parameters
:   | iface | Pointer to the network interface |
    | --- | --- |
    | cb | User-supplied callback function to call |
    | user\_data | User specified data |

## [◆ ](#ga04a8f21d173d51bdcc092b92ed949e53)net\_if\_ipv4\_addr\_lookup()

| struct [net\_if\_addr](structnet__if__addr.md) \* net\_if\_ipv4\_addr\_lookup | ( | const struct [in\_addr](structin__addr.md) \* | *addr*, |
| --- | --- | --- | --- |
|  |  | struct [net\_if](structnet__if.md) \*\* | *iface* ) |

`#include <[net_if.h](net__if_8h.md)>`

Check if this IPv4 address belongs to one of the interfaces.

Parameters
:   | addr | IPv4 address |
    | --- | --- |
    | iface | Interface is returned |

Returns
:   Pointer to interface address, NULL if not found.

## [◆ ](#ga0a22661727316517685afcd551e7b38e)net\_if\_ipv4\_addr\_lookup\_by\_index()

| int net\_if\_ipv4\_addr\_lookup\_by\_index | ( | const struct [in\_addr](structin__addr.md) \* | *addr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Check if this IPv4 address belongs to one of the interface indices.

Parameters
:   | addr | IPv4 address |
    | --- | --- |

Returns
:   >0 if address was found in given network interface index, all other values mean address was not found

## [◆ ](#ga558b31e556a1a4b8d1e68a78f3f755ea)net\_if\_ipv4\_addr\_mask\_cmp()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_if\_ipv4\_addr\_mask\_cmp | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | const struct [in\_addr](structin__addr.md) \* | *addr* ) |

`#include <[net_if.h](net__if_8h.md)>`

Check if the given IPv4 address belongs to local subnet.

Parameters
:   | iface | Interface to use. Must be a valid pointer to an interface. |
    | --- | --- |
    | addr | IPv4 address |

Returns
:   True if address is part of local subnet, false otherwise.

## [◆ ](#ga4433304d46b6559604486b828e7d9dec)net\_if\_ipv4\_addr\_rm()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_if\_ipv4\_addr\_rm | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | const struct [in\_addr](structin__addr.md) \* | *addr* ) |

`#include <[net_if.h](net__if_8h.md)>`

Remove a IPv4 address from an interface.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | addr | IPv4 address |

Returns
:   True if successfully removed, false otherwise

## [◆ ](#gac5bf15f948ab195cecce98d1b40bda37)net\_if\_ipv4\_addr\_rm\_by\_index()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_if\_ipv4\_addr\_rm\_by\_index | ( | int | *index*, |
| --- | --- | --- | --- |
|  |  | const struct [in\_addr](structin__addr.md) \* | *addr* ) |

`#include <[net_if.h](net__if_8h.md)>`

Remove a IPv4 address from an interface by interface index.

Parameters
:   | index | Network interface index |
    | --- | --- |
    | addr | IPv4 address |

Returns
:   True if successfully removed, false otherwise

## [◆ ](#gad791780f25d19acfe49d5272eae2d019)net\_if\_ipv4\_get\_global\_addr()

| struct [in\_addr](structin__addr.md) \* net\_if\_ipv4\_get\_global\_addr | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | enum [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) | *addr\_state* ) |

`#include <[net_if.h](net__if_8h.md)>`

Get a IPv4 global address in a given state.

Parameters
:   | iface | Interface to use. Must be a valid pointer to an interface. |
    | --- | --- |
    | addr\_state | IPv4 address state (preferred, tentative, deprecated) |

Returns
:   Pointer to link local IPv4 address, NULL if no proper IPv4 address could be found.

## [◆ ](#gae42f6f9620e40e2d2b36d30e81bb82d9)net\_if\_ipv4\_get\_gw()

| struct [in\_addr](structin__addr.md) net\_if\_ipv4\_get\_gw | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Get IPv4 gateway of an interface.

Parameters
:   | iface | Interface to use. |
    | --- | --- |

Returns
:   The gateway set on the interface, unspecified address if not found.

## [◆ ](#gad2ffe8df3d5ccca5094daecf3b9a8508)net\_if\_ipv4\_get\_ll()

| struct [in\_addr](structin__addr.md) \* net\_if\_ipv4\_get\_ll | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | enum [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) | *addr\_state* ) |

`#include <[net_if.h](net__if_8h.md)>`

Get a IPv4 link local address in a given state.

Parameters
:   | iface | Interface to use. Must be a valid pointer to an interface. |
    | --- | --- |
    | addr\_state | IPv4 address state (preferred, tentative, deprecated) |

Returns
:   Pointer to link local IPv4 address, NULL if no proper IPv4 address could be found.

## [◆ ](#ga71acb65b1988aab8cca9c9604c86231e)net\_if\_ipv4\_get\_mcast\_ttl()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_if\_ipv4\_get\_mcast\_ttl | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Get IPv4 multicast time-to-live value specified for a given interface.

Parameters
:   | iface | Network interface |
    | --- | --- |

Returns
:   Time-to-live

## [◆ ](#ga41aeb0e7c5f9bc837f7b2ec13401afd1)net\_if\_ipv4\_get\_netmask()

| struct [in\_addr](structin__addr.md) net\_if\_ipv4\_get\_netmask | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Get IPv4 netmask of an interface.

**[Deprecated](deprecated.md#_deprecated000021)**
:   Use [net\_if\_ipv4\_get\_netmask\_by\_addr()](#gadfad7d9232bf58c5626266387a2eb761) instead.

Parameters
:   | iface | Interface to use. |
    | --- | --- |

Returns
:   The netmask set on the interface, unspecified address if not found.

## [◆ ](#gadfad7d9232bf58c5626266387a2eb761)net\_if\_ipv4\_get\_netmask\_by\_addr()

| struct [in\_addr](structin__addr.md) net\_if\_ipv4\_get\_netmask\_by\_addr | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | const struct [in\_addr](structin__addr.md) \* | *addr* ) |

`#include <[net_if.h](net__if_8h.md)>`

Get IPv4 netmask related to an address of an interface.

Parameters
:   | iface | Interface to use. |
    | --- | --- |
    | addr | IPv4 address to check. |

Returns
:   The netmask set on the interface related to the give address, unspecified address if not found.

## [◆ ](#ga7e1fd28dbcf1164d056296b4df782e64)net\_if\_ipv4\_get\_ttl()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_if\_ipv4\_get\_ttl | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Get IPv4 time-to-live value specified for a given interface.

Parameters
:   | iface | Network interface |
    | --- | --- |

Returns
:   Time-to-live

## [◆ ](#ga8f93179138c1942bc1a099102a4314cf)net\_if\_ipv4\_is\_addr\_bcast()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_if\_ipv4\_is\_addr\_bcast | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | const struct [in\_addr](structin__addr.md) \* | *addr* ) |

`#include <[net_if.h](net__if_8h.md)>`

Check if the given IPv4 address is a broadcast address.

Parameters
:   | iface | Interface to use. Must be a valid pointer to an interface. |
    | --- | --- |
    | addr | IPv4 address, this should be in network byte order |

Returns
:   True if address is a broadcast address, false otherwise.

## [◆ ](#gaa43fa83711703f8737e50b639e11b16c)net\_if\_ipv4\_maddr\_add()

| struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \* net\_if\_ipv4\_maddr\_add | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | const struct [in\_addr](structin__addr.md) \* | *addr* ) |

`#include <[net_if.h](net__if_8h.md)>`

Add a IPv4 multicast address to an interface.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | addr | IPv4 multicast address |

Returns
:   Pointer to interface multicast address, NULL if cannot be added

## [◆ ](#gae82f53c670f602e9c37b65abb6dfaec7)net\_if\_ipv4\_maddr\_foreach()

| void net\_if\_ipv4\_maddr\_foreach | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | [net\_if\_ip\_maddr\_cb\_t](#ga726eed76563c223de8f611e2544febe9) | *cb*, |
|  |  | void \* | *user\_data* ) |

`#include <[net_if.h](net__if_8h.md)>`

Go through all IPv4 multicast addresses on a network interface and call callback for each used address.

Parameters
:   | iface | Pointer to the network interface |
    | --- | --- |
    | cb | User-supplied callback function to call |
    | user\_data | User specified data |

## [◆ ](#gaa30769fc8016f1a7496b3ede277d8d8a)net\_if\_ipv4\_maddr\_is\_joined()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_if\_ipv4\_maddr\_is\_joined | ( | struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \* | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Check if given multicast address is joined or not.

Parameters
:   | addr | IPv4 multicast address |
    | --- | --- |

Returns
:   True if address is joined, False otherwise.

## [◆ ](#gae275a5e75817aa178d36f422573ad76a)net\_if\_ipv4\_maddr\_join()

| void net\_if\_ipv4\_maddr\_join | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \* | *addr* ) |

`#include <[net_if.h](net__if_8h.md)>`

Mark a given multicast address to be joined.

Parameters
:   | iface | Network interface the address belongs to |
    | --- | --- |
    | addr | IPv4 multicast address |

## [◆ ](#ga1408fe384736d20f36c035c10007113c)net\_if\_ipv4\_maddr\_leave()

| void net\_if\_ipv4\_maddr\_leave | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \* | *addr* ) |

`#include <[net_if.h](net__if_8h.md)>`

Mark a given multicast address to be left.

Parameters
:   | iface | Network interface the address belongs to |
    | --- | --- |
    | addr | IPv4 multicast address |

## [◆ ](#gadc1514a0d6852de9dbce043bc99d4eb0)net\_if\_ipv4\_maddr\_lookup()

| struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \* net\_if\_ipv4\_maddr\_lookup | ( | const struct [in\_addr](structin__addr.md) \* | *addr*, |
| --- | --- | --- | --- |
|  |  | struct [net\_if](structnet__if.md) \*\* | *iface* ) |

`#include <[net_if.h](net__if_8h.md)>`

Check if this IPv4 multicast address belongs to a specific interface or one of the interfaces.

Parameters
:   | addr | IPv4 address |
    | --- | --- |
    | iface | If \*iface is null, then pointer to interface is returned, otherwise the \*iface value needs to be matched. |

Returns
:   Pointer to interface multicast address, NULL if not found.

## [◆ ](#ga1d9273e10ab089d0f02b2b17d10a9e60)net\_if\_ipv4\_maddr\_rm()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_if\_ipv4\_maddr\_rm | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | const struct [in\_addr](structin__addr.md) \* | *addr* ) |

`#include <[net_if.h](net__if_8h.md)>`

Remove an IPv4 multicast address from an interface.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | addr | IPv4 multicast address |

Returns
:   True if successfully removed, false otherwise

## [◆ ](#ga44984001411077c7a2ef68afb361b40f)net\_if\_ipv4\_router\_add()

| struct [net\_if\_router](structnet__if__router.md) \* net\_if\_ipv4\_router\_add | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | struct [in\_addr](structin__addr.md) \* | *addr*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *is\_default*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *router\_lifetime* ) |

`#include <[net_if.h](net__if_8h.md)>`

Add IPv4 router to the system.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | addr | IPv4 address |
    | is\_default | Is this router the default one |
    | router\_lifetime | Lifetime of the router |

Returns
:   Pointer to router information, NULL if could not be added

## [◆ ](#ga25672516d7f383807e7dd9ce5f46a94f)net\_if\_ipv4\_router\_find\_default()

| struct [net\_if\_router](structnet__if__router.md) \* net\_if\_ipv4\_router\_find\_default | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | struct [in\_addr](structin__addr.md) \* | *addr* ) |

`#include <[net_if.h](net__if_8h.md)>`

Find default router for this IPv4 address.

Parameters
:   | iface | Network interface. This can be NULL in which case we go through all the network interfaces to find a suitable router. |
    | --- | --- |
    | addr | IPv4 address |

Returns
:   Pointer to router information, NULL if cannot be found

## [◆ ](#ga01f995b00248ad5da734e4d58a4353aa)net\_if\_ipv4\_router\_lookup()

| struct [net\_if\_router](structnet__if__router.md) \* net\_if\_ipv4\_router\_lookup | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | struct [in\_addr](structin__addr.md) \* | *addr* ) |

`#include <[net_if.h](net__if_8h.md)>`

Check if IPv4 address is one of the routers configured in the system.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | addr | IPv4 address |

Returns
:   Pointer to router information, NULL if cannot be found

## [◆ ](#ga6be14f5307bc63ce87ff0a3fad7c7f4d)net\_if\_ipv4\_router\_rm()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_if\_ipv4\_router\_rm | ( | struct [net\_if\_router](structnet__if__router.md) \* | *router* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Remove IPv4 router from the system.

Parameters
:   | router | Router information. |
    | --- | --- |

Returns
:   True if successfully removed, false otherwise

## [◆ ](#gad6ec091f61ba3055be60c77ce085522f)net\_if\_ipv4\_select\_src\_addr()

| | const struct [in\_addr](structin__addr.md) \* net\_if\_ipv4\_select\_src\_addr | ( | struct [net\_if](structnet__if.md) \* | *iface*, | | --- | --- | --- | --- | |  |  | const struct [in\_addr](structin__addr.md) \* | *dst* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Get a IPv4 source address that should be used when sending network data to destination.

Parameters
:   | iface | Interface to use when sending the packet. If the interface is not known, then NULL can be given. |
    | --- | --- |
    | dst | IPv4 destination address |

Returns
:   Pointer to IPv4 address to use, NULL if no IPv4 address could be found.

## [◆ ](#gafea1a35f452ad8168855852cbfdf0024)net\_if\_ipv4\_select\_src\_iface()

| | struct [net\_if](structnet__if.md) \* net\_if\_ipv4\_select\_src\_iface | ( | const struct [in\_addr](structin__addr.md) \* | *dst* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Get a network interface that should be used when sending IPv4 network data to destination.

Parameters
:   | dst | IPv4 destination address |
    | --- | --- |

Returns
:   Pointer to network interface to use, NULL if no suitable interface could be found.

## [◆ ](#ga310ccbd9b37629422ca8e32836362724)net\_if\_ipv4\_set\_gw()

| void net\_if\_ipv4\_set\_gw | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | const struct [in\_addr](structin__addr.md) \* | *gw* ) |

`#include <[net_if.h](net__if_8h.md)>`

Set IPv4 gateway for an interface.

Parameters
:   | iface | Interface to use. |
    | --- | --- |
    | gw | IPv4 address of an gateway |

## [◆ ](#gadef49124c331817165475c69fb9104e0)net\_if\_ipv4\_set\_gw\_by\_index()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_if\_ipv4\_set\_gw\_by\_index | ( | int | *index*, |
| --- | --- | --- | --- |
|  |  | const struct [in\_addr](structin__addr.md) \* | *gw* ) |

`#include <[net_if.h](net__if_8h.md)>`

Set IPv4 gateway for an interface index.

Parameters
:   | index | Network interface index |
    | --- | --- |
    | gw | IPv4 address of an gateway |

Returns
:   True if gateway was added, false otherwise.

## [◆ ](#ga9452fef4f1309fb1a53a6a8b4f222377)net\_if\_ipv4\_set\_mcast\_ttl()

| void net\_if\_ipv4\_set\_mcast\_ttl | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ttl* ) |

`#include <[net_if.h](net__if_8h.md)>`

Set IPv4 multicast time-to-live value specified to a given interface.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | ttl | Time-to-live value |

## [◆ ](#gad599bd11663fefa7d785b9fc5d52caf0)net\_if\_ipv4\_set\_netmask()

| void net\_if\_ipv4\_set\_netmask | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | const struct [in\_addr](structin__addr.md) \* | *netmask* ) |

`#include <[net_if.h](net__if_8h.md)>`

Set IPv4 netmask for an interface.

**[Deprecated](deprecated.md#_deprecated000022)**
:   Use [net\_if\_ipv4\_set\_netmask\_by\_addr()](#ga7beda6ccba46fce3cf2da1ce6c0725ec) instead.

Parameters
:   | iface | Interface to use. |
    | --- | --- |
    | netmask | IPv4 netmask |

## [◆ ](#ga7beda6ccba46fce3cf2da1ce6c0725ec)net\_if\_ipv4\_set\_netmask\_by\_addr()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_if\_ipv4\_set\_netmask\_by\_addr | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | const struct [in\_addr](structin__addr.md) \* | *addr*, |
|  |  | const struct [in\_addr](structin__addr.md) \* | *netmask* ) |

`#include <[net_if.h](net__if_8h.md)>`

Set IPv4 netmask for an interface index for a given address.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | addr | IPv4 address related to this netmask |
    | netmask | IPv4 netmask |

Returns
:   True if netmask was added, false otherwise.

## [◆ ](#ga895cfd55f79f7fb78a17cf0e3004fa06)net\_if\_ipv4\_set\_netmask\_by\_addr\_by\_index()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_if\_ipv4\_set\_netmask\_by\_addr\_by\_index | ( | int | *index*, |
| --- | --- | --- | --- |
|  |  | const struct [in\_addr](structin__addr.md) \* | *addr*, |
|  |  | const struct [in\_addr](structin__addr.md) \* | *netmask* ) |

`#include <[net_if.h](net__if_8h.md)>`

Set IPv4 netmask for an interface index for a given address.

Parameters
:   | index | Network interface index |
    | --- | --- |
    | addr | IPv4 address related to this netmask |
    | netmask | IPv4 netmask |

Returns
:   True if netmask was added, false otherwise.

## [◆ ](#ga94f2d2e69548609dd329c7e6b21e8958)net\_if\_ipv4\_set\_netmask\_by\_index()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_if\_ipv4\_set\_netmask\_by\_index | ( | int | *index*, |
| --- | --- | --- | --- |
|  |  | const struct [in\_addr](structin__addr.md) \* | *netmask* ) |

`#include <[net_if.h](net__if_8h.md)>`

Set IPv4 netmask for an interface index.

**[Deprecated](deprecated.md#_deprecated000023)**
:   Use [net\_if\_ipv4\_set\_netmask\_by\_addr()](#ga7beda6ccba46fce3cf2da1ce6c0725ec) instead.

Parameters
:   | index | Network interface index |
    | --- | --- |
    | netmask | IPv4 netmask |

Returns
:   True if netmask was added, false otherwise.

## [◆ ](#ga5544374d7ebea26a239d561083f0203d)net\_if\_ipv4\_set\_ttl()

| void net\_if\_ipv4\_set\_ttl | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ttl* ) |

`#include <[net_if.h](net__if_8h.md)>`

Set IPv4 time-to-live value specified to a given interface.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | ttl | Time-to-live value |

## [◆ ](#gae00484a7fe32671a4ca04ff525e640c6)net\_if\_ipv6\_addr\_add()

| struct [net\_if\_addr](structnet__if__addr.md) \* net\_if\_ipv6\_addr\_add | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | struct [in6\_addr](structin6__addr.md) \* | *addr*, |
|  |  | enum [net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41) | *addr\_type*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *vlifetime* ) |

`#include <[net_if.h](net__if_8h.md)>`

Add a IPv6 address to an interface.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | addr | IPv6 address |
    | addr\_type | IPv6 address type |
    | vlifetime | Validity time for this address |

Returns
:   Pointer to interface address, NULL if cannot be added

## [◆ ](#ga980bffb649ed48775bdc6cb2a0caef15)net\_if\_ipv6\_addr\_add\_by\_index()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_if\_ipv6\_addr\_add\_by\_index | ( | int | *index*, |
| --- | --- | --- | --- |
|  |  | struct [in6\_addr](structin6__addr.md) \* | *addr*, |
|  |  | enum [net\_addr\_type](group__ip__4__6.md#gafecee2d4a331dc85ad962b81a6303e41) | *addr\_type*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *vlifetime* ) |

`#include <[net_if.h](net__if_8h.md)>`

Add a IPv6 address to an interface by index.

Parameters
:   | index | Network interface index |
    | --- | --- |
    | addr | IPv6 address |
    | addr\_type | IPv6 address type |
    | vlifetime | Validity time for this address |

Returns
:   True if ok, false if address could not be added

## [◆ ](#ga5ac646ad7fda0fa48e78c15b4ca52d50)net\_if\_ipv6\_addr\_foreach()

| void net\_if\_ipv6\_addr\_foreach | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | [net\_if\_ip\_addr\_cb\_t](#gab58d8561a4f21899e2db34043d346516) | *cb*, |
|  |  | void \* | *user\_data* ) |

`#include <[net_if.h](net__if_8h.md)>`

Go through all IPv6 addresses on a network interface and call callback for each used address.

Parameters
:   | iface | Pointer to the network interface |
    | --- | --- |
    | cb | User-supplied callback function to call |
    | user\_data | User specified data |

## [◆ ](#ga13b5a26fc672d15697f99e85543184bb)net\_if\_ipv6\_addr\_lookup()

| struct [net\_if\_addr](structnet__if__addr.md) \* net\_if\_ipv6\_addr\_lookup | ( | const struct [in6\_addr](structin6__addr.md) \* | *addr*, |
| --- | --- | --- | --- |
|  |  | struct [net\_if](structnet__if.md) \*\* | *iface* ) |

`#include <[net_if.h](net__if_8h.md)>`

Check if this IPv6 address belongs to one of the interfaces.

Parameters
:   | addr | IPv6 address |
    | --- | --- |
    | iface | Pointer to interface is returned |

Returns
:   Pointer to interface address, NULL if not found.

## [◆ ](#gab53eabb540a4487d83f27c8e319c736a)net\_if\_ipv6\_addr\_lookup\_by\_iface()

| struct [net\_if\_addr](structnet__if__addr.md) \* net\_if\_ipv6\_addr\_lookup\_by\_iface | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | struct [in6\_addr](structin6__addr.md) \* | *addr* ) |

`#include <[net_if.h](net__if_8h.md)>`

Check if this IPv6 address belongs to this specific interfaces.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | addr | IPv6 address |

Returns
:   Pointer to interface address, NULL if not found.

## [◆ ](#ga1527872e5285790d50028a183608ac02)net\_if\_ipv6\_addr\_lookup\_by\_index()

| int net\_if\_ipv6\_addr\_lookup\_by\_index | ( | const struct [in6\_addr](structin6__addr.md) \* | *addr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Check if this IPv6 address belongs to one of the interface indices.

Parameters
:   | addr | IPv6 address |
    | --- | --- |

Returns
:   >0 if address was found in given network interface index, all other values mean address was not found

## [◆ ](#ga25d6e2253c1d361553d478f7c948a28a)net\_if\_ipv6\_addr\_onlink()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_if\_ipv6\_addr\_onlink | ( | struct [net\_if](structnet__if.md) \*\* | *iface*, |
| --- | --- | --- | --- |
|  |  | struct [in6\_addr](structin6__addr.md) \* | *addr* ) |

`#include <[net_if.h](net__if_8h.md)>`

Check if this IPv6 address is part of the subnet of our network interface.

Parameters
:   | iface | Network interface. This is returned to the caller. The iface can be NULL in which case we check all the interfaces. |
    | --- | --- |
    | addr | IPv6 address |

Returns
:   True if address is part of our subnet, false otherwise

## [◆ ](#ga614e1458fa28d26c26f447e9fbcc2cb7)net\_if\_ipv6\_addr\_rm()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_if\_ipv6\_addr\_rm | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | const struct [in6\_addr](structin6__addr.md) \* | *addr* ) |

`#include <[net_if.h](net__if_8h.md)>`

Remove an IPv6 address from an interface.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | addr | IPv6 address |

Returns
:   True if successfully removed, false otherwise

## [◆ ](#gac159e3b0fbf558d5fb09774141da7d6d)net\_if\_ipv6\_addr\_rm\_by\_index()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_if\_ipv6\_addr\_rm\_by\_index | ( | int | *index*, |
| --- | --- | --- | --- |
|  |  | const struct [in6\_addr](structin6__addr.md) \* | *addr* ) |

`#include <[net_if.h](net__if_8h.md)>`

Remove an IPv6 address from an interface by index.

Parameters
:   | index | Network interface index |
    | --- | --- |
    | addr | IPv6 address |

Returns
:   True if successfully removed, false otherwise

## [◆ ](#gaef8a6752a201f81636c4ffc1ebba4a25)net\_if\_ipv6\_addr\_update\_lifetime()

| void net\_if\_ipv6\_addr\_update\_lifetime | ( | struct [net\_if\_addr](structnet__if__addr.md) \* | *ifaddr*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *vlifetime* ) |

`#include <[net_if.h](net__if_8h.md)>`

Update validity lifetime time of an IPv6 address.

Parameters
:   | ifaddr | Network IPv6 address |
    | --- | --- |
    | vlifetime | Validity time for this address |

## [◆ ](#gab1861b5cefa73b4eefbb447cb1438cdc)net\_if\_ipv6\_calc\_reachable\_time()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_if\_ipv6\_calc\_reachable\_time | ( | struct [net\_if\_ipv6](structnet__if__ipv6.md) \* | *ipv6* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Calculate next reachable time value for IPv6 reachable time.

Parameters
:   | ipv6 | IPv6 address configuration |
    | --- | --- |

Returns
:   Reachable time

## [◆ ](#ga1dd53d92f803cff3be4826ddfb6b7211)net\_if\_ipv6\_dad\_failed()

| void net\_if\_ipv6\_dad\_failed | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | const struct [in6\_addr](structin6__addr.md) \* | *addr* ) |

`#include <[net_if.h](net__if_8h.md)>`

Stop IPv6 Duplicate Address Detection (DAD) procedure if we find out that our IPv6 address is already in use.

Parameters
:   | iface | Interface where the DAD was running. |
    | --- | --- |
    | addr | IPv6 address that failed DAD |

## [◆ ](#gaca7d686c772deac13a027cc046333126)net\_if\_ipv6\_get\_global\_addr()

| struct [in6\_addr](structin6__addr.md) \* net\_if\_ipv6\_get\_global\_addr | ( | enum [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) | *state*, |
| --- | --- | --- | --- |
|  |  | struct [net\_if](structnet__if.md) \*\* | *iface* ) |

`#include <[net_if.h](net__if_8h.md)>`

Return global IPv6 address from the first interface that has a global IPv6 address matching the given state.

Parameters
:   | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | IPv6 address state (ANY, TENTATIVE, PREFERRED, DEPRECATED) |
    | --- | --- |
    | iface | Caller can give an interface to check. If iface is set to NULL, then all the interfaces are checked. Pointer to interface where the IPv6 address is defined is returned to the caller. |

Returns
:   Pointer to IPv6 address, NULL if not found.

## [◆ ](#ga66d0a9a8eef095f6d4d44f35dd67f2b6)net\_if\_ipv6\_get\_hop\_limit()

| | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_if\_ipv6\_get\_hop\_limit | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Get IPv6 hop limit specified for a given interface.

This is the default value but can be overridden by the user.

Parameters
:   | iface | Network interface |
    | --- | --- |

Returns
:   Hop limit

## [◆ ](#gad6f3e1e349e281887352652f6f32274e)net\_if\_ipv6\_get\_ll()

| struct [in6\_addr](structin6__addr.md) \* net\_if\_ipv6\_get\_ll | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | enum [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) | *addr\_state* ) |

`#include <[net_if.h](net__if_8h.md)>`

Get a IPv6 link local address in a given state.

Parameters
:   | iface | Interface to use. Must be a valid pointer to an interface. |
    | --- | --- |
    | addr\_state | IPv6 address state (preferred, tentative, deprecated) |

Returns
:   Pointer to link local IPv6 address, NULL if no proper IPv6 address could be found.

## [◆ ](#ga85b7a923d46d36ecd63f9930bd8970c4)net\_if\_ipv6\_get\_ll\_addr()

| struct [in6\_addr](structin6__addr.md) \* net\_if\_ipv6\_get\_ll\_addr | ( | enum [net\_addr\_state](group__ip__4__6.md#ga32e58fc83532ef57eeb6ff952f17288d) | *state*, |
| --- | --- | --- | --- |
|  |  | struct [net\_if](structnet__if.md) \*\* | *iface* ) |

`#include <[net_if.h](net__if_8h.md)>`

Return link local IPv6 address from the first interface that has a link local address matching give state.

Parameters
:   | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | IPv6 address state (ANY, TENTATIVE, PREFERRED, DEPRECATED) |
    | --- | --- |
    | iface | Pointer to interface is returned |

Returns
:   Pointer to IPv6 address, NULL if not found.

## [◆ ](#ga56e7086633bcf4537f54c7ca70e6c900)net\_if\_ipv6\_get\_mcast\_hop\_limit()

| | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_if\_ipv6\_get\_mcast\_hop\_limit | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Get IPv6 multicast hop limit specified for a given interface.

This is the default value but can be overridden by the user.

Parameters
:   | iface | Network interface |
    | --- | --- |

Returns
:   Hop limit

## [◆ ](#ga9dd1f91edbb519a6a079f363c33efacf)net\_if\_ipv6\_get\_reachable\_time()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_if\_ipv6\_get\_reachable\_time | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Get IPv6 reachable timeout specified for a given interface.

Parameters
:   | iface | Network interface |
    | --- | --- |

Returns
:   Reachable timeout

## [◆ ](#gaddbf5a6ba412e6bdb7e31568fe827bd0)net\_if\_ipv6\_get\_retrans\_timer()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_if\_ipv6\_get\_retrans\_timer | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Get IPv6 retransmit timer specified for a given interface.

Parameters
:   | iface | Network interface |
    | --- | --- |

Returns
:   Retransmit timer

## [◆ ](#ga7ae82a491193dfea9b92cb9cbaf26f98)net\_if\_ipv6\_maddr\_add()

| struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \* net\_if\_ipv6\_maddr\_add | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | const struct [in6\_addr](structin6__addr.md) \* | *addr* ) |

`#include <[net_if.h](net__if_8h.md)>`

Add a IPv6 multicast address to an interface.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | addr | IPv6 multicast address |

Returns
:   Pointer to interface multicast address, NULL if cannot be added

## [◆ ](#gab677496fb2e27be2df299a346e9c7132)net\_if\_ipv6\_maddr\_foreach()

| void net\_if\_ipv6\_maddr\_foreach | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | [net\_if\_ip\_maddr\_cb\_t](#ga726eed76563c223de8f611e2544febe9) | *cb*, |
|  |  | void \* | *user\_data* ) |

`#include <[net_if.h](net__if_8h.md)>`

Go through all IPv6 multicast addresses on a network interface and call callback for each used address.

Parameters
:   | iface | Pointer to the network interface |
    | --- | --- |
    | cb | User-supplied callback function to call |
    | user\_data | User specified data |

## [◆ ](#gabe2c16a378a35a22d008bff9142e5449)net\_if\_ipv6\_maddr\_is\_joined()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_if\_ipv6\_maddr\_is\_joined | ( | struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \* | *addr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Check if given multicast address is joined or not.

Parameters
:   | addr | IPv6 multicast address |
    | --- | --- |

Returns
:   True if address is joined, False otherwise.

## [◆ ](#ga49dbc954015307222f176f4149829b76)net\_if\_ipv6\_maddr\_join()

| void net\_if\_ipv6\_maddr\_join | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \* | *addr* ) |

`#include <[net_if.h](net__if_8h.md)>`

Mark a given multicast address to be joined.

Parameters
:   | iface | Network interface the address belongs to |
    | --- | --- |
    | addr | IPv6 multicast address |

## [◆ ](#gad24d5537d52de9781a7a6a55ceedd92b)net\_if\_ipv6\_maddr\_leave()

| void net\_if\_ipv6\_maddr\_leave | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \* | *addr* ) |

`#include <[net_if.h](net__if_8h.md)>`

Mark a given multicast address to be left.

Parameters
:   | iface | Network interface the address belongs to |
    | --- | --- |
    | addr | IPv6 multicast address |

## [◆ ](#gadb4031153c4fef86110879befa6b9975)net\_if\_ipv6\_maddr\_lookup()

| struct [net\_if\_mcast\_addr](structnet__if__mcast__addr.md) \* net\_if\_ipv6\_maddr\_lookup | ( | const struct [in6\_addr](structin6__addr.md) \* | *addr*, |
| --- | --- | --- | --- |
|  |  | struct [net\_if](structnet__if.md) \*\* | *iface* ) |

`#include <[net_if.h](net__if_8h.md)>`

Check if this IPv6 multicast address belongs to a specific interface or one of the interfaces.

Parameters
:   | addr | IPv6 address |
    | --- | --- |
    | iface | If \*iface is null, then pointer to interface is returned, otherwise the \*iface value needs to be matched. |

Returns
:   Pointer to interface multicast address, NULL if not found.

## [◆ ](#gaf0ce126bb5019ff5f5ff0876b9712ad9)net\_if\_ipv6\_maddr\_rm()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_if\_ipv6\_maddr\_rm | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | const struct [in6\_addr](structin6__addr.md) \* | *addr* ) |

`#include <[net_if.h](net__if_8h.md)>`

Remove an IPv6 multicast address from an interface.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | addr | IPv6 multicast address |

Returns
:   True if successfully removed, false otherwise

## [◆ ](#ga2f0c98b16b090d9aea07941c64cbe035)net\_if\_ipv6\_prefix\_add()

| struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) \* net\_if\_ipv6\_prefix\_add | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | struct [in6\_addr](structin6__addr.md) \* | *prefix*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *len*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *lifetime* ) |

`#include <[net_if.h](net__if_8h.md)>`

Add a IPv6 prefix to an network interface.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | prefix | IPv6 address |
    | len | Prefix length |
    | lifetime | Prefix lifetime in seconds |

Returns
:   Pointer to prefix, NULL if the prefix was not added.

## [◆ ](#gae9f98dff661d52c5e3e5e185f0ed9cc0)net\_if\_ipv6\_prefix\_get()

| struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) \* net\_if\_ipv6\_prefix\_get | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | const struct [in6\_addr](structin6__addr.md) \* | *addr* ) |

`#include <[net_if.h](net__if_8h.md)>`

Return prefix that corresponds to this IPv6 address.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | addr | IPv6 address |

Returns
:   Pointer to prefix, NULL if not found.

## [◆ ](#gaaf9af457b97c0d432b6f9f9fdd184834)net\_if\_ipv6\_prefix\_lookup()

| struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) \* net\_if\_ipv6\_prefix\_lookup | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | struct [in6\_addr](structin6__addr.md) \* | *addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *len* ) |

`#include <[net_if.h](net__if_8h.md)>`

Check if this IPv6 prefix belongs to this interface.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | addr | IPv6 address |
    | len | Prefix length |

Returns
:   Pointer to prefix, NULL if not found.

## [◆ ](#ga36f18c7a3ff1777006290170b726deed)net\_if\_ipv6\_prefix\_rm()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_if\_ipv6\_prefix\_rm | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | struct [in6\_addr](structin6__addr.md) \* | *addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *len* ) |

`#include <[net_if.h](net__if_8h.md)>`

Remove an IPv6 prefix from an interface.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | addr | IPv6 prefix address |
    | len | Prefix length |

Returns
:   True if successfully removed, false otherwise

## [◆ ](#gaa3c711e814fb6a4e552b4ef723d0baa0)net\_if\_ipv6\_prefix\_set\_lf()

| | void net\_if\_ipv6\_prefix\_set\_lf | ( | struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) \* | *prefix*, | | --- | --- | --- | --- | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *is\_infinite* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Set the infinite status of the prefix.

Parameters
:   | prefix | IPv6 address |
    | --- | --- |
    | is\_infinite | Infinite status |

## [◆ ](#ga68cffe343c518bad7f7f152e30f7f9ee)net\_if\_ipv6\_prefix\_set\_timer()

| void net\_if\_ipv6\_prefix\_set\_timer | ( | struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) \* | *prefix*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *lifetime* ) |

`#include <[net_if.h](net__if_8h.md)>`

Set the prefix lifetime timer.

Parameters
:   | prefix | IPv6 address |
    | --- | --- |
    | lifetime | Prefix lifetime in seconds |

## [◆ ](#ga2d68cb6dcfcffd3f87bbfb3dfce791ff)net\_if\_ipv6\_prefix\_unset\_timer()

| void net\_if\_ipv6\_prefix\_unset\_timer | ( | struct [net\_if\_ipv6\_prefix](structnet__if__ipv6__prefix.md) \* | *prefix* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Unset the prefix lifetime timer.

Parameters
:   | prefix | IPv6 address |
    | --- | --- |

## [◆ ](#ga9c766ed70ada6eb551ac6542d7ac1ca3)net\_if\_ipv6\_router\_add()

| struct [net\_if\_router](structnet__if__router.md) \* net\_if\_ipv6\_router\_add | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | struct [in6\_addr](structin6__addr.md) \* | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *router\_lifetime* ) |

`#include <[net_if.h](net__if_8h.md)>`

Add IPv6 router to the system.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | addr | IPv6 address |
    | router\_lifetime | Lifetime of the router |

Returns
:   Pointer to router information, NULL if could not be added

## [◆ ](#ga36dab2a8fd9120ebc9c8b18f1875ccfd)net\_if\_ipv6\_router\_find\_default()

| struct [net\_if\_router](structnet__if__router.md) \* net\_if\_ipv6\_router\_find\_default | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | struct [in6\_addr](structin6__addr.md) \* | *addr* ) |

`#include <[net_if.h](net__if_8h.md)>`

Find default router for this IPv6 address.

Parameters
:   | iface | Network interface. This can be NULL in which case we go through all the network interfaces to find a suitable router. |
    | --- | --- |
    | addr | IPv6 address |

Returns
:   Pointer to router information, NULL if cannot be found

## [◆ ](#gacece4ee588082259b3b5cfcd5ac1d552)net\_if\_ipv6\_router\_lookup()

| struct [net\_if\_router](structnet__if__router.md) \* net\_if\_ipv6\_router\_lookup | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | struct [in6\_addr](structin6__addr.md) \* | *addr* ) |

`#include <[net_if.h](net__if_8h.md)>`

Check if IPv6 address is one of the routers configured in the system.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | addr | IPv6 address |

Returns
:   Pointer to router information, NULL if cannot be found

## [◆ ](#ga1d108aa0b54c072e0aa9d0c049f02807)net\_if\_ipv6\_router\_rm()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_if\_ipv6\_router\_rm | ( | struct [net\_if\_router](structnet__if__router.md) \* | *router* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Remove IPv6 router from the system.

Parameters
:   | router | Router information. |
    | --- | --- |

Returns
:   True if successfully removed, false otherwise

## [◆ ](#gaadba4957802dc376ef011590c91c6af6)net\_if\_ipv6\_router\_update\_lifetime()

| void net\_if\_ipv6\_router\_update\_lifetime | ( | struct [net\_if\_router](structnet__if__router.md) \* | *router*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *lifetime* ) |

`#include <[net_if.h](net__if_8h.md)>`

Update validity lifetime time of a router.

Parameters
:   | router | Network IPv6 address |
    | --- | --- |
    | lifetime | Lifetime of this router. |

## [◆ ](#ga50689a1afdb37a7087bf47a12cc50438)net\_if\_ipv6\_select\_src\_addr()

| | const struct [in6\_addr](structin6__addr.md) \* net\_if\_ipv6\_select\_src\_addr | ( | struct [net\_if](structnet__if.md) \* | *iface*, | | --- | --- | --- | --- | |  |  | const struct [in6\_addr](structin6__addr.md) \* | *dst* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Get a IPv6 source address that should be used when sending network data to destination.

Parameters
:   | iface | Interface that was used when packet was received. If the interface is not known, then NULL can be given. |
    | --- | --- |
    | dst | IPv6 destination address |

Returns
:   Pointer to IPv6 address to use, NULL if no IPv6 address could be found.

## [◆ ](#ga5cf4717e632f712045dd4fe81b30245c)net\_if\_ipv6\_select\_src\_addr\_hint()

| | const struct [in6\_addr](structin6__addr.md) \* net\_if\_ipv6\_select\_src\_addr\_hint | ( | struct [net\_if](structnet__if.md) \* | *iface*, | | --- | --- | --- | --- | |  |  | const struct [in6\_addr](structin6__addr.md) \* | *dst*, | |  |  | int | *flags* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Get a IPv6 source address that should be used when sending network data to destination.

Use a hint set to the socket to select the proper address.

Parameters
:   | iface | Interface that was used when packet was received. If the interface is not known, then NULL can be given. |
    | --- | --- |
    | dst | IPv6 destination address |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Hint from the related socket. See RFC 5014 for value details. |

Returns
:   Pointer to IPv6 address to use, NULL if no IPv6 address could be found.

## [◆ ](#gae1495ac9e743be54b8d90bd4ff4700ab)net\_if\_ipv6\_select\_src\_iface()

| | struct [net\_if](structnet__if.md) \* net\_if\_ipv6\_select\_src\_iface | ( | const struct [in6\_addr](structin6__addr.md) \* | *dst* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Get a network interface that should be used when sending IPv6 network data to destination.

Parameters
:   | dst | IPv6 destination address |
    | --- | --- |

Returns
:   Pointer to network interface to use, NULL if no suitable interface could be found.

## [◆ ](#gab3939d735b660f8f02124df656ceba2c)net\_if\_ipv6\_set\_base\_reachable\_time()

| | void net\_if\_ipv6\_set\_base\_reachable\_time | ( | struct [net\_if](structnet__if.md) \* | *iface*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *reachable\_time* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Set IPv6 reachable time for a given interface.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | reachable\_time | New reachable time |

## [◆ ](#ga5bf726bb5c1d232103ec6841e7d0cd8c)net\_if\_ipv6\_set\_hop\_limit()

| | void net\_if\_ipv6\_set\_hop\_limit | ( | struct [net\_if](structnet__if.md) \* | *iface*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *hop\_limit* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Set the default IPv6 hop limit of a given interface.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | hop\_limit | New hop limit |

## [◆ ](#gaf56a433679ea9701cf8baa3208f8ccc3)net\_if\_ipv6\_set\_mcast\_hop\_limit()

| | void net\_if\_ipv6\_set\_mcast\_hop\_limit | ( | struct [net\_if](structnet__if.md) \* | *iface*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *hop\_limit* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Set the default IPv6 multicast hop limit of a given interface.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | hop\_limit | New hop limit |

## [◆ ](#ga8328266b870fd200660cb2becaab3de4)net\_if\_ipv6\_set\_reachable\_time()

| | void net\_if\_ipv6\_set\_reachable\_time | ( | struct [net\_if\_ipv6](structnet__if__ipv6.md) \* | *ipv6* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Set IPv6 reachable time for a given interface.

This requires that base reachable time is set for the interface.

Parameters
:   | ipv6 | IPv6 address configuration |
    | --- | --- |

## [◆ ](#gad74566e5a34f447d2ac63d2c0e82eeff)net\_if\_ipv6\_set\_retrans\_timer()

| | void net\_if\_ipv6\_set\_retrans\_timer | ( | struct [net\_if](structnet__if.md) \* | *iface*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *retrans\_timer* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Set IPv6 retransmit timer for a given interface.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | retrans\_timer | New retransmit timer |

## [◆ ](#ga099a484a654ad9af35d3212fc2c995b2)net\_if\_is\_admin\_up()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_if\_is\_admin\_up | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Check if interface was brought up by the administrator.

Parameters
:   | iface | Pointer to network interface |
    | --- | --- |

Returns
:   True if interface is admin up, false otherwise.

## [◆ ](#ga095554237016e563d76cfd602d1dae77)net\_if\_is\_carrier\_ok()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_if\_is\_carrier\_ok | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Check if carrier is present on network device.

Parameters
:   | iface | Pointer to network interface |
    | --- | --- |

Returns
:   True if carrier is present, false otherwise.

## [◆ ](#ga6e2e6102271c37acaa59c54e2aa6b413)net\_if\_is\_dormant()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_if\_is\_dormant | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Check if the interface is dormant.

Parameters
:   | iface | Pointer to network interface |
    | --- | --- |

Returns
:   True if interface is dormant, false otherwise.

## [◆ ](#ga6bfa5f84a2127bbad27a0a3b319526a1)net\_if\_is\_ip\_offloaded()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_if\_is\_ip\_offloaded | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Return the IP offload status.

Parameters
:   | iface | Network interface |
    | --- | --- |

Returns
:   True if IP offloading is active, false otherwise.

## [◆ ](#gaecedc93a6dab2c57fe686718ea4d78af)net\_if\_is\_offloaded()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_if\_is\_offloaded | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Return offload status of a given network interface.

Parameters
:   | iface | Network interface |
    | --- | --- |

Returns
:   True if IP or socket offloading is active, false otherwise.

## [◆ ](#ga9f1a6eab849517734ec422deb0ba71f5)net\_if\_is\_promisc()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_if\_is\_promisc | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Check if promiscuous mode is set or not.

Parameters
:   | iface | Pointer to network interface |
    | --- | --- |

Returns
:   True if interface is in promisc mode, False if interface is not in promiscuous mode.

## [◆ ](#gaf308baf2241fa455b50b439b7fab3f1e)net\_if\_is\_socket\_offloaded()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_if\_is\_socket\_offloaded | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Return the socket offload status.

Parameters
:   | iface | Network interface |
    | --- | --- |

Returns
:   True if socket offloading is active, false otherwise.

## [◆ ](#ga7e9b368d4abf9da5656140df70cfa334)net\_if\_is\_up()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_if\_is\_up | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Check if interface is up and running.

Parameters
:   | iface | Pointer to network interface |
    | --- | --- |

Returns
:   True if interface is up, False if it is down.

## [◆ ](#gaa458b5f349c55007108b47b99f4954d5)net\_if\_is\_wifi()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_if\_is\_wifi | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Check if the network interface supports Wi-Fi.

Parameters
:   | iface | Pointer to network interface |
    | --- | --- |

Returns
:   True if interface supports Wi-Fi, False otherwise.

## [◆ ](#gafa451f6118529d1d084704d00b2aae20)net\_if\_l2()

| | const struct [net\_l2](structnet__l2.md) \* net\_if\_l2 | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Get a pointer to the interface L2.

Parameters
:   | iface | a valid pointer to a network interface structure |
    | --- | --- |

Returns
:   a pointer to the iface L2

## [◆ ](#ga3cad2d51fc9cc225619585e06e252db0)net\_if\_l2\_data()

| | void \* net\_if\_l2\_data | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Get a pointer to the interface L2 private data.

Parameters
:   | iface | a valid pointer to a network interface structure |
    | --- | --- |

Returns
:   a pointer to the iface L2 data

## [◆ ](#gadbb8be32caa896bdcdeee19425134827)net\_if\_lookup\_by\_dev()

| struct [net\_if](structnet__if.md) \* net\_if\_lookup\_by\_dev | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Find an interface from it's related device.

Parameters
:   | dev | A valid struct device pointer to relate with an interface |
    | --- | --- |

Returns
:   a valid struct [net\_if](structnet__if.md "Network Interface structure.") pointer on success, NULL otherwise

## [◆ ](#ga8fdd0665ed76db6055777e395ca60255)net\_if\_mcast\_mon\_register()

| void net\_if\_mcast\_mon\_register | ( | struct [net\_if\_mcast\_monitor](structnet__if__mcast__monitor.md) \* | *mon*, |
| --- | --- | --- | --- |
|  |  | struct [net\_if](structnet__if.md) \* | *iface*, |
|  |  | [net\_if\_mcast\_callback\_t](#ga0d64291573740a67eae7ff3fcc0910c5) | *cb* ) |

`#include <[net_if.h](net__if_8h.md)>`

Register a multicast monitor.

Parameters
:   | mon | Monitor handle. This is a pointer to a monitor storage structure which should be allocated by caller, but does not need to be initialized. |
    | --- | --- |
    | iface | Network interface or NULL for all interfaces |
    | cb | Monitor callback |

## [◆ ](#gad323732fe3d178a5dfdf0900e5cb5683)net\_if\_mcast\_mon\_unregister()

| void net\_if\_mcast\_mon\_unregister | ( | struct [net\_if\_mcast\_monitor](structnet__if__mcast__monitor.md) \* | *mon* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Unregister a multicast monitor.

Parameters
:   | mon | Monitor handle |
    | --- | --- |

## [◆ ](#ga372ef131263269cd65586d87997df745)net\_if\_mcast\_monitor()

| void net\_if\_mcast\_monitor | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | const struct net\_addr \* | *addr*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *is\_joined* ) |

`#include <[net_if.h](net__if_8h.md)>`

Call registered multicast monitors.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | addr | Multicast address |
    | is\_joined | Is this multicast address group joined (true) or not (false) |

## [◆ ](#ga51af469ff3d7d9f760d63a8a9c7be8b5)net\_if\_nbr\_reachability\_hint()

| | void net\_if\_nbr\_reachability\_hint | ( | struct [net\_if](structnet__if.md) \* | *iface*, | | --- | --- | --- | --- | |  |  | const struct [in6\_addr](structin6__addr.md) \* | *ipv6\_addr* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Provide a reachability hint for IPv6 Neighbor Discovery.

This function is intended for upper-layer protocols to inform the IPv6 Neighbor Discovery process about an active link to a specific neighbor. By signaling a recent "forward progress" event, such as the reception of an ACK, this function can help reduce unnecessary ND traffic as per the guidelines in RFC 4861 (section 7.3).

Parameters
:   | iface | A pointer to the network interface. |
    | --- | --- |
    | ipv6\_addr | Pointer to the IPv6 address of the neighbor node. |

## [◆ ](#ga8048e722f6442bcd5b6881bd71e791a5)net\_if\_need\_calc\_rx\_checksum()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_if\_need\_calc\_rx\_checksum | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | enum [net\_if\_checksum\_type](#ga8db412ae79c64cafe81a66f5acb2f8e9) | *chksum\_type* ) |

`#include <[net_if.h](net__if_8h.md)>`

Check if received network packet checksum calculation can be avoided or not.

For example many ethernet devices support network packet offloading in which case the IP stack does not need to calculate the checksum.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | chksum\_type | L3 and/or L4 protocol for which to compute checksum |

Returns
:   True if checksum needs to be calculated, false otherwise.

## [◆ ](#ga9634c3e71e934ab3a07bec989b364663)net\_if\_need\_calc\_tx\_checksum()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_if\_need\_calc\_tx\_checksum | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | enum [net\_if\_checksum\_type](#ga8db412ae79c64cafe81a66f5acb2f8e9) | *chksum\_type* ) |

`#include <[net_if.h](net__if_8h.md)>`

Check if network packet checksum calculation can be avoided or not when sending the packet.

For example many ethernet devices support network packet offloading in which case the IP stack does not need to calculate the checksum.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | chksum\_type | L3 and/or L4 protocol for which to compute checksum |

Returns
:   True if checksum needs to be calculated, false otherwise.

## [◆ ](#ga520939e94620ca75475a71f153df6d4a)net\_if\_offload()

| | struct net\_offload \* net\_if\_offload | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Return the IP offload plugin.

Parameters
:   | iface | Network interface |
    | --- | --- |

Returns
:   NULL if there is no offload plugin defined, valid pointer otherwise

## [◆ ](#gad9e957a4866b4566296ee39392fde0e4)net\_if\_oper\_state()

| | enum [net\_if\_oper\_state](#gadfe9d90f24046cd9bd4bbee096e747b9) [net\_if\_oper\_state](#gadfe9d90f24046cd9bd4bbee096e747b9) | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Get an operational state of an interface.

Parameters
:   | iface | Pointer to network interface |
    | --- | --- |

Returns
:   Operational state of an interface

## [◆ ](#ga1f1bf845e63cce02e2183889cc85d57e)net\_if\_oper\_state\_set()

| | enum [net\_if\_oper\_state](#gadfe9d90f24046cd9bd4bbee096e747b9) net\_if\_oper\_state\_set | ( | struct [net\_if](structnet__if.md) \* | *iface*, | | --- | --- | --- | --- | |  |  | enum [net\_if\_oper\_state](#gadfe9d90f24046cd9bd4bbee096e747b9) | *oper\_state* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Set an operational state on an interface.

Parameters
:   | iface | Pointer to network interface |
    | --- | --- |
    | oper\_state | Operational state to set |

Returns
:   The new operational state of an interface

## [◆ ](#ga56c4d37edcea540be09ebcdf97265aed)net\_if\_queue\_tx()

| void net\_if\_queue\_tx | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | struct [net\_pkt](structnet__pkt.md) \* | *pkt* ) |

`#include <[net_if.h](net__if_8h.md)>`

Queue a packet to the net interface TX queue.

Parameters
:   | iface | Pointer to a network interface structure |
    | --- | --- |
    | pkt | Pointer to a net packet to queue |

## [◆ ](#ga72ed21ca0cb220199f5a2070137c7fef)net\_if\_recv\_data()

| enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) net\_if\_recv\_data | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | struct [net\_pkt](structnet__pkt.md) \* | *pkt* ) |

`#include <[net_if.h](net__if_8h.md)>`

Input a packet through a net iface.

Parameters
:   | iface | Pointer to a network interface structure |
    | --- | --- |
    | pkt | Pointer to a net packet to input |

Returns
:   verdict about the packet

## [◆ ](#gaa81b7d9ed8dc05da3391265dbc89b665)net\_if\_register\_link\_cb()

| void net\_if\_register\_link\_cb | ( | struct [net\_if\_link\_cb](structnet__if__link__cb.md) \* | *link*, |
| --- | --- | --- | --- |
|  |  | [net\_if\_link\_callback\_t](#ga0f87d5753fcd7cce40ecd161e6c91078) | *cb* ) |

`#include <[net_if.h](net__if_8h.md)>`

Register a link callback.

Parameters
:   | link | Caller specified handler for the callback. |
    | --- | --- |
    | cb | Callback to register. |

## [◆ ](#ga2a48e13941c91ddb9bbc63d014729be1)net\_if\_router\_ipv4()

| | struct [in\_addr](structin__addr.md) \* net\_if\_router\_ipv4 | ( | struct [net\_if\_router](structnet__if__router.md) \* | *router* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Get the IPv4 address of the given router.

Parameters
:   | router | a network router |
    | --- | --- |

Returns
:   pointer to the IPv4 address, or NULL if none

## [◆ ](#gadbf1538003473d448ff0808896b732a5)net\_if\_router\_ipv6()

| | struct [in6\_addr](structin6__addr.md) \* net\_if\_router\_ipv6 | ( | struct [net\_if\_router](structnet__if__router.md) \* | *router* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Get the IPv6 address of the given router.

Parameters
:   | router | a network router |
    | --- | --- |

Returns
:   pointer to the IPv6 address, or NULL if none

## [◆ ](#gadc87242eb7205362a308b3c4437bf76d)net\_if\_router\_rm()

| void net\_if\_router\_rm | ( | struct [net\_if\_router](structnet__if__router.md) \* | *router* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Remove a router from the system.

Parameters
:   | router | Pointer to existing router |
    | --- | --- |

## [◆ ](#ga001b1cdde5febcf3970848c7c185c81c)net\_if\_select\_src\_iface()

| struct [net\_if](structnet__if.md) \* net\_if\_select\_src\_iface | ( | const struct [sockaddr](structsockaddr.md) \* | *dst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Get a network interface that should be used when sending IPv6 or IPv4 network data to destination.

Parameters
:   | dst | IPv6 or IPv4 destination address |
    | --- | --- |

Returns
:   Pointer to network interface to use. Note that the function will return the default network interface if the best network interface is not found.

## [◆ ](#gada0398d757eab28d16a129692c309f4d)net\_if\_send\_data()

| enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896) net\_if\_send\_data | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | struct [net\_pkt](structnet__pkt.md) \* | *pkt* ) |

`#include <[net_if.h](net__if_8h.md)>`

Send a packet through a net iface.

Parameters
:   | iface | Pointer to a network interface structure |
    | --- | --- |
    | pkt | Pointer to a net packet to send |

return verdict about the packet

## [◆ ](#ga0a1f27ec893e1af3c97f130be4616589)net\_if\_set\_default()

| void net\_if\_set\_default | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Set the default network interface.

Parameters
:   | iface | New default interface, or NULL to revert to the one set by Kconfig. |
    | --- | --- |

## [◆ ](#ga52b41b2f8b7d3405338a0539542677a0)net\_if\_set\_link\_addr()

| | int net\_if\_set\_link\_addr | ( | struct [net\_if](structnet__if.md) \* | *iface*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *addr*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *len*, | |  |  | enum [net\_link\_type](group__net__linkaddr.md#ga1312c2322bc4a4f1c3b76d6466806b24) | *type* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Set a network interface's link address.

Parameters
:   | iface | Pointer to a network interface structure |
    | --- | --- |
    | addr | A pointer to a [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) buffer representing the address. The buffer must remain valid throughout interface lifetime. |
    | len | length of the address buffer |
    | type | network bearer type of this link address |

Returns
:   0 on success

## [◆ ](#ga76b140c6fc39b94ff4102e08e3a58e81)net\_if\_set\_mtu()

| | void net\_if\_set\_mtu | ( | struct [net\_if](structnet__if.md) \* | *iface*, | | --- | --- | --- | --- | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *mtu* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Set an network interface's MTU.

Parameters
:   | iface | Pointer to a network interface structure |
    | --- | --- |
    | mtu | New MTU, note that we store only 16 bit mtu value. |

## [◆ ](#ga05dec64966fc39e3deb0679b9585688b)net\_if\_set\_name()

| int net\_if\_set\_name | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | const char \* | *buf* ) |

`#include <[net_if.h](net__if_8h.md)>`

Set network interface name.

Normally this function is not needed to call as the system will automatically assign a name to the network interface.

Parameters
:   | iface | Pointer to network interface |
    | --- | --- |
    | buf | User supplied name |

Returns
:   0 name is set correctly -ENOTSUP interface name support is disabled -EINVAL if invalid parameters are given, -ENAMETOOLONG if name is too long

## [◆ ](#gaf9f81f3b9697ca47f7674d85f37a8d80)net\_if\_set\_promisc()

| | int net\_if\_set\_promisc | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Set network interface into promiscuous mode.

Note that not all network technologies will support this.

Parameters
:   | iface | Pointer to network interface |
    | --- | --- |

Returns
:   0 on success, <0 if error

## [◆ ](#gafb2bbaec96c4759d920b2866c0b3ef3a)net\_if\_socket\_offload()

| | [net\_socket\_create\_t](#gaef3dfe26195514aac625e9f22e399759) net\_if\_socket\_offload | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Return the function to create an offloaded socket.

Parameters
:   | iface | Network interface |
    | --- | --- |

Returns
:   NULL if the interface is not socket offloaded, valid pointer otherwise

## [◆ ](#ga9db52875580115c743b1f35cd6c46796)net\_if\_socket\_offload\_set()

| | void net\_if\_socket\_offload\_set | ( | struct [net\_if](structnet__if.md) \* | *iface*, | | --- | --- | --- | --- | |  |  | [net\_socket\_create\_t](#gaef3dfe26195514aac625e9f22e399759) | *socket\_offload* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Set the function to create an offloaded socket.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | socket\_offload | A function to create an offloaded socket |

## [◆ ](#ga9655c010ccbf989e9328271f5dbcc685)net\_if\_start\_dad()

| | void net\_if\_start\_dad | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Start duplicate address detection procedure.

Parameters
:   | iface | Pointer to a network interface structure |
    | --- | --- |

## [◆ ](#gab9bdb7f8a9eeed4d9b70965b8af82cb7)net\_if\_start\_rs()

| void net\_if\_start\_rs | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Start neighbor discovery and send router solicitation message.

Parameters
:   | iface | Pointer to a network interface structure |
    | --- | --- |

## [◆ ](#gab0195bb2151a1ba722a0b11d81066988)net\_if\_stop\_rs()

| | void net\_if\_stop\_rs | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Stop neighbor discovery.

Parameters
:   | iface | Pointer to a network interface structure |
    | --- | --- |

## [◆ ](#ga6ba64fac6e8d846ae7be5990f49a8293)net\_if\_unregister\_link\_cb()

| void net\_if\_unregister\_link\_cb | ( | struct [net\_if\_link\_cb](structnet__if__link__cb.md) \* | *link* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Unregister a link callback.

Parameters
:   | link | Caller specified handler for the callback. |
    | --- | --- |

## [◆ ](#ga9c8212c087883510050ac6a39ef0a7bf)net\_if\_unset\_promisc()

| | void net\_if\_unset\_promisc | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Set network interface into normal mode.

Parameters
:   | iface | Pointer to network interface |
    | --- | --- |

## [◆ ](#ga02644cc623fc7a8878c17d54984e4210)net\_if\_up()

| int net\_if\_up | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_if.h](net__if_8h.md)>`

Bring interface up.

Parameters
:   | iface | Pointer to network interface |
    | --- | --- |

Returns
:   0 on success

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
