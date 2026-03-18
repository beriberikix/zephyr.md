---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/dns__sd_8h.html
original_path: doxygen/html/dns__sd_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dns\_sd.h File Reference

DNS Service Discovery.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/sys/byteorder.h](sys_2byteorder_8h_source.md)>`

[Go to the source code of this file.](dns__sd_8h_source.md)

| Macros | |
| --- | --- |
| #define | [DNS\_SD\_INSTANCE\_MIN\_SIZE](group__dns__sd.md#ga4d1f5462555d6051bdeaa21b02e7aa6e)   1 |
|  | RFC 1034 Section 3.1. |
| #define | [DNS\_SD\_INSTANCE\_MAX\_SIZE](group__dns__sd.md#ga5c0993b8bc21d47fa15f56acb313ac31)   63 |
|  | RFC 1034 Section 3.1, RFC 6763 Section 7.2. |
| #define | [DNS\_SD\_SERVICE\_MIN\_SIZE](group__dns__sd.md#gacc652552aa567206ab7a4d7d070d1fbc)   2 |
|  | RFC 6763 Section 7.2 - inclusive of underscore. |
| #define | [DNS\_SD\_SERVICE\_MAX\_SIZE](group__dns__sd.md#gab4d208eac1491c45cb47e87c90a78c26)   16 |
|  | RFC 6763 Section 7.2 - inclusive of underscore. |
| #define | [DNS\_SD\_SERVICE\_PREFIX](group__dns__sd.md#ga81cac0a52e58142e492bad244ff97490)   '\_' |
|  | RFC 6763 Section 4.1.2. |
| #define | [DNS\_SD\_PROTO\_SIZE](group__dns__sd.md#gafb686ae445f5bd640176f59d62df2bdc)   4 |
|  | RFC 6763 Section 4.1.2 - either \_tcp or \_udp (case insensitive). |
| #define | [DNS\_SD\_DOMAIN\_MIN\_SIZE](group__dns__sd.md#ga19d655c1778143e2aed5d2d69a757422)   2 |
|  | ICANN Rules for TLD naming. |
| #define | [DNS\_SD\_DOMAIN\_MAX\_SIZE](group__dns__sd.md#gaa93b197f2b9a3b13c7ed8f3c455f11cb)   63 |
|  | RFC 1034 Section 3.1, RFC 6763 Section 7.2. |
| #define | [DNS\_SD\_MIN\_LABELS](group__dns__sd.md#gaeec792bc3111e1961eb2e21cd8bea80a)   3 |
|  | Minimum number of segments in a fully-qualified name. |
| #define | [DNS\_SD\_MAX\_LABELS](group__dns__sd.md#ga269e2f3bbf15a5ccd81a444749faa384)   4 |
|  | Maximum number of segments in a fully-qualified name. |
| #define | [DNS\_SD\_REGISTER\_SERVICE](group__dns__sd.md#ga0c0060a680d5c4fe56f2815c920c3627)(\_id, \_instance, \_service, \_proto, \_domain, \_text, \_port) |
|  | Register a service for DNS Service Discovery. |
| #define | [DNS\_SD\_REGISTER\_TCP\_SERVICE](group__dns__sd.md#ga96abc525d755c138304f07cdd2d9e1c2)(id, instance, service, domain, text, port) |
|  | Register a TCP service for DNS Service Discovery. |
| #define | [DNS\_SD\_REGISTER\_UDP\_SERVICE](group__dns__sd.md#gaf8abe0968552213d46b49be16c1f21d6)(id, instance, service, domain, text, port) |
|  | Register a UDP service for DNS Service Discovery. |
| #define | [DNS\_SD\_EMPTY\_TXT](group__dns__sd.md#ga221216c5ffd142aa4c6cade4064d580f)   dns\_sd\_empty\_txt |
|  | Empty DNS-SD TXT specifier. |

| Functions | |
| --- | --- |
| static [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [dns\_sd\_txt\_size](group__dns__sd.md#ga6d68e785607089df42d534c2f876c6d5) (const struct dns\_sd\_rec \*rec) |
|  | Obtain the size of DNS-SD TXT data. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [dns\_sd\_is\_service\_type\_enumeration](group__dns__sd.md#gaeba098fa6d159067c70588cb60056277) (const struct dns\_sd\_rec \*rec) |
|  | Check if *rec* is a DNS-SD Service Type Enumeration. |
| void | [dns\_sd\_create\_wildcard\_filter](group__dns__sd.md#ga328d71e26411460b1b329db8f1ebd37b) (struct dns\_sd\_rec \*filter) |
|  | Create a wildcard filter for DNS-SD records. |

## Detailed Description

DNS Service Discovery.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [dns\_sd.h](dns__sd_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
