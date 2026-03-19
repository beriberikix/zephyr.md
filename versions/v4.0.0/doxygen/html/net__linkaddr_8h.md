---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/net__linkaddr_8h.html
original_path: doxygen/html/net__linkaddr_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_linkaddr.h File Reference

Public API for network link address.
[More...](#details)

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[errno.h](errno_8h_source.md)>`

[Go to the source code of this file.](net__linkaddr_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [net\_linkaddr](structnet__linkaddr.md) |
|  | Hardware link address structure. [More...](structnet__linkaddr.md#details) |
| struct | [net\_linkaddr\_storage](structnet__linkaddr__storage.md) |
|  | Hardware link address structure. [More...](structnet__linkaddr__storage.md#details) |

| Macros | |
| --- | --- |
| #define | [NET\_LINK\_ADDR\_MAX\_LENGTH](group__net__linkaddr.md#ga5680cf2ac9302bbee824148f36193b2b)   6 |
|  | Maximum length of the link address. |

| Enumerations | |
| --- | --- |
| enum | [net\_link\_type](group__net__linkaddr.md#ga1312c2322bc4a4f1c3b76d6466806b24) {     [NET\_LINK\_UNKNOWN](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24a3e12f6af3333134a3e118fb16458bd34) = 0 , [NET\_LINK\_IEEE802154](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24a4f365da4c9300c31cd4022600e630ce3) , [NET\_LINK\_BLUETOOTH](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24abc3c811d04e998cbf498cc19644d182a) , [NET\_LINK\_ETHERNET](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24a7fc0b181a04fe90ca3a9c72170810d7b) ,     [NET\_LINK\_DUMMY](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24a7895ba2ce84de4c6dc03cbc57a87b7c8) , [NET\_LINK\_CANBUS\_RAW](group__net__linkaddr.md#gga1312c2322bc4a4f1c3b76d6466806b24ab452eaef0ff58af43468da87ecfa404a)   } |
|  | Type of the link address. [More...](group__net__linkaddr.md#ga1312c2322bc4a4f1c3b76d6466806b24) |

| Functions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [net\_linkaddr\_cmp](group__net__linkaddr.md#ga36387353825a70fbe54dd16d076a9e26) (struct [net\_linkaddr](structnet__linkaddr.md) \*lladdr1, struct [net\_linkaddr](structnet__linkaddr.md) \*lladdr2) |
|  | Compare two link layer addresses. |
| static int | [net\_linkaddr\_set](group__net__linkaddr.md#gaa20d6cb50b240f9306ea88b1dc4c1de4) (struct [net\_linkaddr\_storage](structnet__linkaddr__storage.md) \*lladdr\_store, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*new\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) new\_len) |
|  | Set the member data of a link layer address storage structure. |

## Detailed Description

Public API for network link address.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [net\_linkaddr.h](net__linkaddr_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
