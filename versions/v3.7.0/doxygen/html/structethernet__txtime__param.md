---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structethernet__txtime__param.html
original_path: doxygen/html/structethernet__txtime__param.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ethernet\_txtime\_param Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Ethernet Support Functions](group__ethernet.md)

Ethernet TXTIME specific parameters.
[More...](#details)

`#include <[ethernet.h](ethernet_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum ethernet\_txtime\_param\_type | [type](#ab4a709e6907e76f9cf23c085f5be5d99) |
|  | Type of TXTIME parameter. |
| int | [queue\_id](#aa4a46b7153b2a69ca0134f4e10bc7165) |
|  | Queue number for configuring TXTIME. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [enable\_txtime](#a74b1e05cf0fac8aa435ba966e110ae27) |
|  | Enable or disable TXTIME per queue. |

## Detailed Description

Ethernet TXTIME specific parameters.

## Field Documentation

## [◆ ](#a74b1e05cf0fac8aa435ba966e110ae27)enable\_txtime

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) ethernet\_txtime\_param::enable\_txtime |
| --- |

Enable or disable TXTIME per queue.

## [◆ ](#aa4a46b7153b2a69ca0134f4e10bc7165)queue\_id

| int ethernet\_txtime\_param::queue\_id |
| --- |

Queue number for configuring TXTIME.

## [◆ ](#ab4a709e6907e76f9cf23c085f5be5d99)type

| enum ethernet\_txtime\_param\_type ethernet\_txtime\_param::type |
| --- |

Type of TXTIME parameter.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[ethernet.h](ethernet_8h_source.md)

- [ethernet\_txtime\_param](structethernet__txtime__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
