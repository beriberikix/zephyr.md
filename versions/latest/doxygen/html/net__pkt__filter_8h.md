---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/net__pkt__filter_8h.html
original_path: doxygen/html/net__pkt__filter_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_pkt\_filter.h File Reference

Network packet filtering public header file.
[More...](#details)

`#include <[limits.h](limits_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`  
`#include <[zephyr/net/net_core.h](net__core_8h_source.md)>`  
`#include <[zephyr/net/ethernet.h](ethernet_8h_source.md)>`

[Go to the source code of this file.](net__pkt__filter_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [npf\_test](structnpf__test.md) |
|  | common filter test structure to be embedded into larger structures [More...](structnpf__test.md#details) |
| struct | [npf\_rule](structnpf__rule.md) |
|  | filter rule structure [More...](structnpf__rule.md#details) |
| struct | [npf\_rule\_list](structnpf__rule__list.md) |
|  | rule set for a given test location [More...](structnpf__rule__list.md#details) |

| Macros | |
| --- | --- |
| #define | [npf\_insert\_send\_rule](group__net__pkt__filter.md#ga4d3592647f81cd44a84ded4fff8edcf5)(rule) |
| #define | [npf\_insert\_recv\_rule](group__net__pkt__filter.md#ga3f6ecadc4842b61731984968ab4c6b89)(rule) |
| #define | [npf\_append\_send\_rule](group__net__pkt__filter.md#ga8cd06cba4360c1b56709e59ff06dbeb3)(rule) |
| #define | [npf\_append\_recv\_rule](group__net__pkt__filter.md#ga263c7ee6e3c860353b5720c613690b0a)(rule) |
| #define | [npf\_remove\_send\_rule](group__net__pkt__filter.md#ga43f03a0ce73d6dee52f43fd3577aa240)(rule) |
| #define | [npf\_remove\_recv\_rule](group__net__pkt__filter.md#gae78cb092522564303a665d1a5d3596b9)(rule) |
| #define | [npf\_remove\_all\_send\_rules](group__net__pkt__filter.md#gaea48284508ee244bce6d78b29bc2f471)() |
| #define | [npf\_remove\_all\_recv\_rules](group__net__pkt__filter.md#gac08801a6e8bd14bfd6eeaf2f28a1ed1a)() |
| #define | [NPF\_RULE](group__net__pkt__filter.md#ga2f45093d5ad164d5c51a8996f7f04d32)(\_name, \_result, ...) |
|  | Statically define one packet filter rule. |
| #define | [NPF\_IFACE\_MATCH](group__npf__basic__cond.md#ga465578272b616c6267ecd13fd86ca73b)(\_name, \_iface) |
|  | Statically define an "interface match" packet filter condition. |
| #define | [NPF\_IFACE\_UNMATCH](group__npf__basic__cond.md#gac3607a6736d70b0ea044a2ec7ab6d313)(\_name, \_iface) |
|  | Statically define an "interface unmatch" packet filter condition. |
| #define | [NPF\_ORIG\_IFACE\_MATCH](group__npf__basic__cond.md#ga55021acd131e4684568aaf6434b08789)(\_name, \_iface) |
|  | Statically define an "orig interface match" packet filter condition. |
| #define | [NPF\_ORIG\_IFACE\_UNMATCH](group__npf__basic__cond.md#gad959dc62d47ca3b4d2f24a6c862c7623)(\_name, \_iface) |
|  | Statically define an "orig interface unmatch" packet filter condition. |
| #define | [NPF\_SIZE\_MIN](group__npf__basic__cond.md#gaf142455f9bea3dea8faa0a913072b63e)(\_name, \_size) |
|  | Statically define a "data minimum size" packet filter condition. |
| #define | [NPF\_SIZE\_MAX](group__npf__basic__cond.md#gacd56b9bcf2b2ba4759402650a9bff67a)(\_name, \_size) |
|  | Statically define a "data maximum size" packet filter condition. |
| #define | [NPF\_SIZE\_BOUNDS](group__npf__basic__cond.md#gab402bb13c7899d57532d3dcf8a36ed4b)(\_name, \_min\_size, \_max\_size) |
|  | Statically define a "data bounded size" packet filter condition. |
| #define | [NPF\_IP\_SRC\_ADDR\_ALLOWLIST](group__npf__basic__cond.md#ga4dd013f0fb92eb0433f174cf40e89e00)(\_name, \_ip\_addr\_array, \_ip\_addr\_num, \_af) |
|  | Statically define a "ip address allowlist" packet filter condition. |
| #define | [NPF\_IP\_SRC\_ADDR\_BLOCKLIST](group__npf__basic__cond.md#ga57fe28a992b1afaf33581292fe5015bd)(\_name, \_ip\_addr\_array, \_ip\_addr\_num, \_af) |
|  | Statically define a "ip address blocklist" packet filter condition. |
| #define | [NPF\_ETH\_SRC\_ADDR\_MATCH](group__npf__eth__cond.md#gad2141ad8d6639c9b92569d55130ca1b1)(\_name, \_addr\_array) |
|  | Statically define a "source address match" packet filter condition. |
| #define | [NPF\_ETH\_SRC\_ADDR\_UNMATCH](group__npf__eth__cond.md#ga228eaa3784f663d8f2e2711e26409043)(\_name, \_addr\_array) |
|  | Statically define a "source address unmatch" packet filter condition. |
| #define | [NPF\_ETH\_DST\_ADDR\_MATCH](group__npf__eth__cond.md#ga3d22d687bcd56b7727c51c7bc7f36cac)(\_name, \_addr\_array) |
|  | Statically define a "destination address match" packet filter condition. |
| #define | [NPF\_ETH\_DST\_ADDR\_UNMATCH](group__npf__eth__cond.md#ga3b8a8a22eb992c0e02223f70723c3641)(\_name, \_addr\_array) |
|  | Statically define a "destination address unmatch" packet filter condition. |
| #define | [NPF\_ETH\_SRC\_ADDR\_MASK\_MATCH](group__npf__eth__cond.md#ga0e06ebc4c9a1a960651be1ba89eeb2fd)(\_name, \_addr\_array, ...) |
|  | Statically define a "source address match with mask" packet filter condition. |
| #define | [NPF\_ETH\_DST\_ADDR\_MASK\_MATCH](group__npf__eth__cond.md#ga7cf793af7b91eccc6e675ff19ed59a14)(\_name, \_addr\_array, ...) |
|  | Statically define a "destination address match with mask" packet filter condition. |
| #define | [NPF\_ETH\_TYPE\_MATCH](group__npf__eth__cond.md#gace7de72d4c64e128a825f28f94d8b1b2)(\_name, \_type) |
|  | Statically define an "Ethernet type match" packet filter condition. |
| #define | [NPF\_ETH\_TYPE\_UNMATCH](group__npf__eth__cond.md#gab9bf6d58433e273220c5fab76f608545)(\_name, \_type) |
|  | Statically define an "Ethernet type unmatch" packet filter condition. |

| Functions | |
| --- | --- |
| void | [npf\_insert\_rule](group__net__pkt__filter.md#ga3b2a85558b6756e76760d9a40c780e28) (struct [npf\_rule\_list](structnpf__rule__list.md) \*rules, struct [npf\_rule](structnpf__rule.md) \*rule) |
|  | Insert a rule at the front of given rule list. |
| void | [npf\_append\_rule](group__net__pkt__filter.md#gadfa956e4af3c45460846fc22f863e697) (struct [npf\_rule\_list](structnpf__rule__list.md) \*rules, struct [npf\_rule](structnpf__rule.md) \*rule) |
|  | Append a rule at the end of given rule list. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [npf\_remove\_rule](group__net__pkt__filter.md#ga4d7426db901debff35e1de5805e06c71) (struct [npf\_rule\_list](structnpf__rule__list.md) \*rules, struct [npf\_rule](structnpf__rule.md) \*rule) |
|  | Remove a rule from the given rule list. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [npf\_remove\_all\_rules](group__net__pkt__filter.md#ga54916eb4943e4b47cd31eb23827d0dd5) (struct [npf\_rule\_list](structnpf__rule__list.md) \*rules) |
|  | Remove all rules from the given rule list. |

| Variables | |
| --- | --- |
| struct [npf\_rule](structnpf__rule.md) | [npf\_default\_ok](group__net__pkt__filter.md#gaac489d75c023952243589cba7ff7367a) |
|  | Default rule list termination for accepting a packet. |
| struct [npf\_rule](structnpf__rule.md) | [npf\_default\_drop](group__net__pkt__filter.md#ga8fc592feedeceb5172f8747a29697dd7) |
|  | Default rule list termination for rejecting a packet. |
| struct [npf\_rule\_list](structnpf__rule__list.md) | [npf\_send\_rules](group__net__pkt__filter.md#ga8017a041d3168c76e39bdfac011b9315) |
|  | rule list applied to outgoing packets |
| struct [npf\_rule\_list](structnpf__rule__list.md) | [npf\_recv\_rules](group__net__pkt__filter.md#ga9714529658625e906264a46ad1a9be6f) |
|  | rule list applied to incoming packets |
| struct [npf\_rule\_list](structnpf__rule__list.md) | [npf\_local\_in\_recv\_rules](group__net__pkt__filter.md#ga571e9fb34eb4e3cbf38f885b5e786021) |
|  | rule list applied for local incoming packets |
| struct [npf\_rule\_list](structnpf__rule__list.md) | [npf\_ipv4\_recv\_rules](group__net__pkt__filter.md#gad521d7ac3270970833aec48d8a517d85) |
|  | rule list applied for IPv4 incoming packets |
| struct [npf\_rule\_list](structnpf__rule__list.md) | [npf\_ipv6\_recv\_rules](group__net__pkt__filter.md#gab91ca81aab2da48066538d72caf0c8ae) |
|  | rule list applied for IPv6 incoming packets |

## Detailed Description

Network packet filtering public header file.

The network packet filtering provides a mechanism for deciding the fate of an incoming or outgoing packet based on a set of basic rules.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_pkt\_filter.h](net__pkt__filter_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
