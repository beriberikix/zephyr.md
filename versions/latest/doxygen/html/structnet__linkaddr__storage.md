---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structnet__linkaddr__storage.html
original_path: doxygen/html/structnet__linkaddr__storage.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_linkaddr\_storage Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Link Address Library](group__net__linkaddr.md)

Hardware link address structure.
[More...](#details)

`#include <[net_linkaddr.h](net__linkaddr_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [type](#a00ae00d99b6022663e0f5a3894704ca8) |
|  | What kind of address is this for. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [len](#ab1d9024ef8574f6e7daaa19ee5266a11) |
|  | The real length of the ll address. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [addr](#ae37b0b74f3d2b7ec09e2c2022e86c0bb) [6] |
|  | The array of bytes representing the address. |

## Detailed Description

Hardware link address structure.

Used to hold the link address information. This variant is needed when we have to store the link layer address.

Note that you cannot cast this to [net\_linkaddr](structnet__linkaddr.md "Hardware link address structure.") as [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* is handled differently than [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr[] and the fields are purposely in different order.

## Field Documentation

## [◆ ](#ae37b0b74f3d2b7ec09e2c2022e86c0bb)addr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_linkaddr\_storage::addr[6] |
| --- |

The array of bytes representing the address.

## [◆ ](#ab1d9024ef8574f6e7daaa19ee5266a11)len

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_linkaddr\_storage::len |
| --- |

The real length of the ll address.

## [◆ ](#a00ae00d99b6022663e0f5a3894704ca8)type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_linkaddr\_storage::type |
| --- |

What kind of address is this for.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_linkaddr.h](net__linkaddr_8h_source.md)

- [net\_linkaddr\_storage](structnet__linkaddr__storage.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
