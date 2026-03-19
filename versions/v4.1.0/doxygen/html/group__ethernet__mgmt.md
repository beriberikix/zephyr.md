---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__ethernet__mgmt.html
original_path: doxygen/html/group__ethernet__mgmt.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Ethernet Library

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

Ethernet library.
[More...](#details)

| Functions | |
| --- | --- |
| void | [ethernet\_mgmt\_raise\_carrier\_on\_event](#ga07ea7707f01d0c34724e0a71c463f1ad) (struct [net\_if](structnet__if.md) \*iface) |
|  | Raise CARRIER\_ON event when Ethernet is connected. |
| void | [ethernet\_mgmt\_raise\_carrier\_off\_event](#ga039b86d955331f483386b04ec51c3b4d) (struct [net\_if](structnet__if.md) \*iface) |
|  | Raise CARRIER\_OFF event when Ethernet is disconnected. |
| void | [ethernet\_mgmt\_raise\_vlan\_enabled\_event](#gaf7fe2fdca74cd547a4d015bfe0dd7536) (struct [net\_if](structnet__if.md) \*iface, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag) |
|  | Raise VLAN\_ENABLED event when VLAN is enabled. |
| void | [ethernet\_mgmt\_raise\_vlan\_disabled\_event](#gac02c1f616aee2a7381aa6eebba3f799f) (struct [net\_if](structnet__if.md) \*iface, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tag) |
|  | Raise VLAN\_DISABLED event when VLAN is disabled. |

## Detailed Description

Ethernet library.

Since
:   1.12

Version
:   0.8.0

## Function Documentation

## [◆ ](#ga039b86d955331f483386b04ec51c3b4d)ethernet\_mgmt\_raise\_carrier\_off\_event()

| void ethernet\_mgmt\_raise\_carrier\_off\_event | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ethernet_mgmt.h](ethernet__mgmt_8h.md)>`

Raise CARRIER\_OFF event when Ethernet is disconnected.

Parameters
:   | iface | Ethernet network interface. |
    | --- | --- |

## [◆ ](#ga07ea7707f01d0c34724e0a71c463f1ad)ethernet\_mgmt\_raise\_carrier\_on\_event()

| void ethernet\_mgmt\_raise\_carrier\_on\_event | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ethernet_mgmt.h](ethernet__mgmt_8h.md)>`

Raise CARRIER\_ON event when Ethernet is connected.

Parameters
:   | iface | Ethernet network interface. |
    | --- | --- |

## [◆ ](#gac02c1f616aee2a7381aa6eebba3f799f)ethernet\_mgmt\_raise\_vlan\_disabled\_event()

| void ethernet\_mgmt\_raise\_vlan\_disabled\_event | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *tag* ) |

`#include <[ethernet_mgmt.h](ethernet__mgmt_8h.md)>`

Raise VLAN\_DISABLED event when VLAN is disabled.

Parameters
:   | iface | Ethernet network interface. |
    | --- | --- |
    | tag | VLAN tag which is disabled. |

## [◆ ](#gaf7fe2fdca74cd547a4d015bfe0dd7536)ethernet\_mgmt\_raise\_vlan\_enabled\_event()

| void ethernet\_mgmt\_raise\_vlan\_enabled\_event | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *tag* ) |

`#include <[ethernet_mgmt.h](ethernet__mgmt_8h.md)>`

Raise VLAN\_ENABLED event when VLAN is enabled.

Parameters
:   | iface | Ethernet network interface. |
    | --- | --- |
    | tag | VLAN tag which is enabled. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
