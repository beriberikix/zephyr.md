---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structdsa__port__config.html
original_path: doxygen/html/structdsa__port__config.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dsa\_port\_config Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Distributed Switch Architecture (DSA)](group__dsa__core.md)

Structure of DSA port configuration.
[More...](#details)

`#include <[zephyr/net/dsa_core.h](dsa__core_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [mac\_addr](#a96b55ad5f534ae4837236c0ef6f2d75b) [6] |
|  | Port mac address. |
| const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [use\_random\_mac\_addr](#a1ce3b39d25b2321984d91b4f311581ba) |
|  | Use random mac address or not. |
| const int | [port\_idx](#a521f8ad8298fce309f80785b850f6eef) |
|  | Port index. |
| const struct [device](structdevice.md) \* | [phy\_dev](#acebba6797230c65baac4403b578e1cbb) |
|  | PHY device. |
| const char \* | [phy\_mode](#a8eac549c19d9f9999b95c95fa112ff97) |
|  | PHY mode. |
| const struct [device](structdevice.md) \* | [ethernet\_connection](#a97138eca5243d1564badfe89fd04bbd4) |
|  | Ethernet device connected to the port. |
| void \* | [prv\_config](#a3ab024894788e956b545d6b3114e8739) |
|  | Instance specific config. |

## Detailed Description

Structure of DSA port configuration.

## Field Documentation

## [◆ ](#a97138eca5243d1564badfe89fd04bbd4)ethernet\_connection

| const struct [device](structdevice.md)\* dsa\_port\_config::ethernet\_connection |
| --- |

Ethernet device connected to the port.

## [◆ ](#a96b55ad5f534ae4837236c0ef6f2d75b)mac\_addr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dsa\_port\_config::mac\_addr[6] |
| --- |

Port mac address.

## [◆ ](#acebba6797230c65baac4403b578e1cbb)phy\_dev

| const struct [device](structdevice.md)\* dsa\_port\_config::phy\_dev |
| --- |

PHY device.

## [◆ ](#a8eac549c19d9f9999b95c95fa112ff97)phy\_mode

| const char\* dsa\_port\_config::phy\_mode |
| --- |

PHY mode.

## [◆ ](#a521f8ad8298fce309f80785b850f6eef)port\_idx

| const int dsa\_port\_config::port\_idx |
| --- |

Port index.

## [◆ ](#a3ab024894788e956b545d6b3114e8739)prv\_config

| void\* dsa\_port\_config::prv\_config |
| --- |

Instance specific config.

## [◆ ](#a1ce3b39d25b2321984d91b4f311581ba)use\_random\_mac\_addr

| const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) dsa\_port\_config::use\_random\_mac\_addr |
| --- |

Use random mac address or not.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[dsa\_core.h](dsa__core_8h_source.md)

- [dsa\_port\_config](structdsa__port__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
