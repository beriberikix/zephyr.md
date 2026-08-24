---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structdsa__switch__context.html
original_path: doxygen/html/structdsa__switch__context.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dsa\_switch\_context Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Distributed Switch Architecture (DSA)](group__dsa__core.md)

DSA switch context data.
[More...](#details)

`#include <[zephyr/net/dsa_core.h](dsa__core_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [net\_if](structnet__if.md) \* | [iface\_user](#ad6670b8743639c7837b9188a9e8a70eb) [DSA\_PORT\_MAX\_COUNT] |
|  | Pointers to all DSA user network interfaces. |
| struct [net\_if](structnet__if.md) \* | [iface\_conduit](#a227551d262998fb83dcd06ebfccdb4d7) |
|  | Pointer to DSA conduit network interface. |
| struct [dsa\_api](structdsa__api.md) \* | [dapi](#a4ca4e815b96c29cb26aef7ff02d8b03c) |
|  | DSA specific API callbacks. |
| void \* | [prv\_data](#a0eb8ee97a922eaefdaed00cf75ec5a26) |
|  | Instance specific data. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [num\_ports](#ae9437d8ef21a64cdb297623096cd77f3) |
|  | Number of ports in the DSA switch. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [init\_ports](#a68a619b3db141ba6127ccc4577f2edf5) |
|  | Number of initialized ports in the DSA switch. |

## Detailed Description

DSA switch context data.

## Field Documentation

## [◆ ](#a4ca4e815b96c29cb26aef7ff02d8b03c)dapi

| struct [dsa\_api](structdsa__api.md)\* dsa\_switch\_context::dapi |
| --- |

DSA specific API callbacks.

## [◆ ](#a227551d262998fb83dcd06ebfccdb4d7)iface\_conduit

| struct [net\_if](structnet__if.md)\* dsa\_switch\_context::iface\_conduit |
| --- |

Pointer to DSA conduit network interface.

## [◆ ](#ad6670b8743639c7837b9188a9e8a70eb)iface\_user

| struct [net\_if](structnet__if.md)\* dsa\_switch\_context::iface\_user[DSA\_PORT\_MAX\_COUNT] |
| --- |

Pointers to all DSA user network interfaces.

## [◆ ](#a68a619b3db141ba6127ccc4577f2edf5)init\_ports

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dsa\_switch\_context::init\_ports |
| --- |

Number of initialized ports in the DSA switch.

## [◆ ](#ae9437d8ef21a64cdb297623096cd77f3)num\_ports

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dsa\_switch\_context::num\_ports |
| --- |

Number of ports in the DSA switch.

## [◆ ](#a0eb8ee97a922eaefdaed00cf75ec5a26)prv\_data

| void\* dsa\_switch\_context::prv\_data |
| --- |

Instance specific data.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[dsa\_core.h](dsa__core_8h_source.md)

- [dsa\_switch\_context](structdsa__switch__context.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
