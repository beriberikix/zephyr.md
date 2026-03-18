---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/ipv4__autoconf_8h.html
original_path: doxygen/html/ipv4__autoconf_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ipv4\_autoconf.h File Reference

IPv4 Autoconfiguration.
[More...](#details)

[Go to the source code of this file.](ipv4__autoconf_8h_source.md)

| Macros | |
| --- | --- |
| #define | [net\_ipv4\_autoconf\_init](#a20d767a6d3b73cb9075384313e425e80)(...) |
|  | Initialize IPv4 auto configuration engine. |

| Enumerations | |
| --- | --- |
| enum | [net\_ipv4\_autoconf\_state](#abdf8bb08f12768aad2ff95b902bdc899) {     [NET\_IPV4\_AUTOCONF\_INIT](#abdf8bb08f12768aad2ff95b902bdc899a8e1f10d00b92cfee0e9ecda9f1dc840b) , [NET\_IPV4\_AUTOCONF\_PROBE](#abdf8bb08f12768aad2ff95b902bdc899a346aab74cb52d65887c523cf7d802765) , [NET\_IPV4\_AUTOCONF\_ANNOUNCE](#abdf8bb08f12768aad2ff95b902bdc899a1b050e88e0ad48c4a2f954e0995864c9) , [NET\_IPV4\_AUTOCONF\_ASSIGNED](#abdf8bb08f12768aad2ff95b902bdc899a749a2be0ebf1852694521f72d4b3bde2) ,     [NET\_IPV4\_AUTOCONF\_RENEW](#abdf8bb08f12768aad2ff95b902bdc899abd136a5eb78ed7000243edcb0d673674)   } |
|  | Current state of IPv4 Autoconfiguration. [More...](#abdf8bb08f12768aad2ff95b902bdc899) |

## Detailed Description

IPv4 Autoconfiguration.

## Macro Definition Documentation

## [◆ ](#a20d767a6d3b73cb9075384313e425e80)net\_ipv4\_autoconf\_init

| #define net\_ipv4\_autoconf\_init | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

Initialize IPv4 auto configuration engine.

## Enumeration Type Documentation

## [◆ ](#abdf8bb08f12768aad2ff95b902bdc899)net\_ipv4\_autoconf\_state

| enum [net\_ipv4\_autoconf\_state](#abdf8bb08f12768aad2ff95b902bdc899) |
| --- |

Current state of IPv4 Autoconfiguration.

| Enumerator | |
| --- | --- |
| NET\_IPV4\_AUTOCONF\_INIT |  |
| NET\_IPV4\_AUTOCONF\_PROBE |  |
| NET\_IPV4\_AUTOCONF\_ANNOUNCE |  |
| NET\_IPV4\_AUTOCONF\_ASSIGNED |  |
| NET\_IPV4\_AUTOCONF\_RENEW |  |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [ipv4\_autoconf.h](ipv4__autoconf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
