---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/group__net__linkaddr.html
original_path: doxygen/html/group__net__linkaddr.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Network Link Address Library

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

Network link address library.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [net\_linkaddr](structnet__linkaddr.md) |
|  | Hardware link address structure. [More...](structnet__linkaddr.md#details) |

| Macros | |
| --- | --- |
| #define | [NET\_LINK\_ADDR\_MAX\_LENGTH](#ga5680cf2ac9302bbee824148f36193b2b)   6 |
|  | Maximum length of the link address. |

| Enumerations | |
| --- | --- |
| enum | [net\_link\_type](#ga1312c2322bc4a4f1c3b76d6466806b24) {     [NET\_LINK\_UNKNOWN](#gga1312c2322bc4a4f1c3b76d6466806b24a3e12f6af3333134a3e118fb16458bd34) = 0 , [NET\_LINK\_IEEE802154](#gga1312c2322bc4a4f1c3b76d6466806b24a4f365da4c9300c31cd4022600e630ce3) , [NET\_LINK\_BLUETOOTH](#gga1312c2322bc4a4f1c3b76d6466806b24abc3c811d04e998cbf498cc19644d182a) , [NET\_LINK\_ETHERNET](#gga1312c2322bc4a4f1c3b76d6466806b24a7fc0b181a04fe90ca3a9c72170810d7b) ,     [NET\_LINK\_DUMMY](#gga1312c2322bc4a4f1c3b76d6466806b24a7895ba2ce84de4c6dc03cbc57a87b7c8) , [NET\_LINK\_CANBUS\_RAW](#gga1312c2322bc4a4f1c3b76d6466806b24ab452eaef0ff58af43468da87ecfa404a)   } |
|  | Type of the link address. [More...](#ga1312c2322bc4a4f1c3b76d6466806b24) |

| Functions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_linkaddr\_cmp](#ga36387353825a70fbe54dd16d076a9e26) (struct [net\_linkaddr](structnet__linkaddr.md) \*lladdr1, struct [net\_linkaddr](structnet__linkaddr.md) \*lladdr2) |
|  | Compare two link layer addresses. |
| static int | [net\_linkaddr\_set](#gab0c451240b31d61749b724eaa6d61d45) (struct [net\_linkaddr](structnet__linkaddr.md) \*lladdr, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*new\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) new\_len) |
|  | Set the member data of a link layer address storage structure. |
| static int | [net\_linkaddr\_copy](#ga1230eb353dd8f6671bf8ed31c464b712) (struct [net\_linkaddr](structnet__linkaddr.md) \*dst, const struct [net\_linkaddr](structnet__linkaddr.md) \*src) |
|  | Copy link address from one variable to another. |
| static int | [net\_linkaddr\_create](#gae8a73ee528b82ae36357bd066dc8128b) (struct [net\_linkaddr](structnet__linkaddr.md) \*lladdr, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len, enum [net\_link\_type](#ga1312c2322bc4a4f1c3b76d6466806b24) type) |
|  | Create a link address structure. |
| static int | [net\_linkaddr\_clear](#ga4061ecaf3b1c4c06968ef6a744de0185) (struct [net\_linkaddr](structnet__linkaddr.md) \*lladdr) |
|  | Clear link address. |

## Detailed Description

Network link address library.

Since
:   1.0

Version
:   1.0.0

## Macro Definition Documentation

## [◆ ](#ga5680cf2ac9302bbee824148f36193b2b)NET\_LINK\_ADDR\_MAX\_LENGTH

| #define NET\_LINK\_ADDR\_MAX\_LENGTH   6 |
| --- |

`#include <[zephyr/net/net_linkaddr.h](net__linkaddr_8h.md)>`

Maximum length of the link address.

## Enumeration Type Documentation

## [◆ ](#ga1312c2322bc4a4f1c3b76d6466806b24)net\_link\_type

| enum [net\_link\_type](#ga1312c2322bc4a4f1c3b76d6466806b24) |
| --- |

`#include <[zephyr/net/net_linkaddr.h](net__linkaddr_8h.md)>`

Type of the link address.

This indicates the network technology that this address is used in. Note that in order to save space we store the value into a [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) variable, so please do not introduce any values > 255 in this enum.

| Enumerator | |
| --- | --- |
| NET\_LINK\_UNKNOWN | Unknown link address type. |
| NET\_LINK\_IEEE802154 | IEEE 802.15.4 link address. |
| NET\_LINK\_BLUETOOTH | Bluetooth IPSP link address. |
| NET\_LINK\_ETHERNET | Ethernet link address. |
| NET\_LINK\_DUMMY | Dummy link address.  Used in testing apps and loopback support. |
| NET\_LINK\_CANBUS\_RAW | CANBUS link address. |

## Function Documentation

## [◆ ](#ga4061ecaf3b1c4c06968ef6a744de0185)net\_linkaddr\_clear()

| | int net\_linkaddr\_clear | ( | struct [net\_linkaddr](structnet__linkaddr.md) \* | *lladdr* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/net/net_linkaddr.h](net__linkaddr_8h.md)>`

Clear link address.

Parameters
:   | lladdr | The link address structure. |
    | --- | --- |

Returns
:   0 if ok, <0 if error

## [◆ ](#ga36387353825a70fbe54dd16d076a9e26)net\_linkaddr\_cmp()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_linkaddr\_cmp | ( | struct [net\_linkaddr](structnet__linkaddr.md) \* | *lladdr1*, | | --- | --- | --- | --- | |  |  | struct [net\_linkaddr](structnet__linkaddr.md) \* | *lladdr2* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/net/net_linkaddr.h](net__linkaddr_8h.md)>`

Compare two link layer addresses.

Parameters
:   | lladdr1 | Pointer to a link layer address |
    | --- | --- |
    | lladdr2 | Pointer to a link layer address |

Returns
:   True if the addresses are the same, false otherwise.

## [◆ ](#ga1230eb353dd8f6671bf8ed31c464b712)net\_linkaddr\_copy()

| | int net\_linkaddr\_copy | ( | struct [net\_linkaddr](structnet__linkaddr.md) \* | *dst*, | | --- | --- | --- | --- | |  |  | const struct [net\_linkaddr](structnet__linkaddr.md) \* | *src* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/net/net_linkaddr.h](net__linkaddr_8h.md)>`

Copy link address from one variable to another.

Parameters
:   | dst | The link address structure destination. |
    | --- | --- |
    | src | The link address structure to source. |

Returns
:   0 if ok, <0 if error

## [◆ ](#gae8a73ee528b82ae36357bd066dc8128b)net\_linkaddr\_create()

| | int net\_linkaddr\_create | ( | struct [net\_linkaddr](structnet__linkaddr.md) \* | *lladdr*, | | --- | --- | --- | --- | |  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *addr*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *len*, | |  |  | enum [net\_link\_type](#ga1312c2322bc4a4f1c3b76d6466806b24) | *type* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/net/net_linkaddr.h](net__linkaddr_8h.md)>`

Create a link address structure.

Parameters
:   | lladdr | The link address structure to change. |
    | --- | --- |
    | addr | Array of bytes containing the link address. If set to NULL, the address will be cleared. |
    | len | Length of the link address array. |
    | type | Type of the link address. |

Returns
:   0 if ok, <0 if error

## [◆ ](#gab0c451240b31d61749b724eaa6d61d45)net\_linkaddr\_set()

| | int net\_linkaddr\_set | ( | struct [net\_linkaddr](structnet__linkaddr.md) \* | *lladdr*, | | --- | --- | --- | --- | |  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *new\_addr*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *new\_len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/net/net_linkaddr.h](net__linkaddr_8h.md)>`

Set the member data of a link layer address storage structure.

Parameters
:   | lladdr | The link address storage structure to change. |
    | --- | --- |
    | new\_addr | Array of bytes containing the link address. |
    | new\_len | Length of the link address array. This value should always be <= NET\_LINK\_ADDR\_MAX\_LENGTH. |

Returns
:   0 if ok, <0 if error

- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
