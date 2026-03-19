---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ethernet__mgmt_8h.html
original_path: doxygen/html/ethernet__mgmt_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ethernet\_mgmt.h File Reference

Ethernet Management interface public header.
[More...](#details)

`#include <[zephyr/net/ethernet.h](ethernet_8h_source.md)>`  
`#include <[zephyr/net/net_mgmt.h](net__mgmt_8h_source.md)>`

[Go to the source code of this file.](ethernet__mgmt_8h_source.md)

| Functions | |
| --- | --- |
| void | [ethernet\_mgmt\_raise\_carrier\_on\_event](group__ethernet__mgmt.md#ga07ea7707f01d0c34724e0a71c463f1ad) (struct [net\_if](structnet__if.md) \*iface) |
|  | Raise CARRIER\_ON event when Ethernet is connected. |
| void | [ethernet\_mgmt\_raise\_carrier\_off\_event](group__ethernet__mgmt.md#ga039b86d955331f483386b04ec51c3b4d) (struct [net\_if](structnet__if.md) \*iface) |
|  | Raise CARRIER\_OFF event when Ethernet is disconnected. |
| void | [ethernet\_mgmt\_raise\_vlan\_enabled\_event](group__ethernet__mgmt.md#gaf7fe2fdca74cd547a4d015bfe0dd7536) (struct [net\_if](structnet__if.md) \*iface, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag) |
|  | Raise VLAN\_ENABLED event when VLAN is enabled. |
| void | [ethernet\_mgmt\_raise\_vlan\_disabled\_event](group__ethernet__mgmt.md#gac02c1f616aee2a7381aa6eebba3f799f) (struct [net\_if](structnet__if.md) \*iface, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag) |
|  | Raise VLAN\_DISABLED event when VLAN is disabled. |

## Detailed Description

Ethernet Management interface public header.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [ethernet\_mgmt.h](ethernet__mgmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
