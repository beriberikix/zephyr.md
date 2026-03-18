---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/ipv4__autoconf_8h.html
original_path: doxygen/html/ipv4__autoconf_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ipv4\_autoconf.h File Reference

IPv4 Autoconfiguration.
[More...](#details)

[Go to the source code of this file.](ipv4__autoconf_8h_source.md)

| Enumerations | |
| --- | --- |
| enum | [net\_ipv4\_autoconf\_state](#abdf8bb08f12768aad2ff95b902bdc899) { [NET\_IPV4\_AUTOCONF\_INIT](#abdf8bb08f12768aad2ff95b902bdc899a8e1f10d00b92cfee0e9ecda9f1dc840b) , [NET\_IPV4\_AUTOCONF\_ASSIGNED](#abdf8bb08f12768aad2ff95b902bdc899a749a2be0ebf1852694521f72d4b3bde2) , [NET\_IPV4\_AUTOCONF\_RENEW](#abdf8bb08f12768aad2ff95b902bdc899abd136a5eb78ed7000243edcb0d673674) } |
|  | Current state of IPv4 Autoconfiguration. [More...](#abdf8bb08f12768aad2ff95b902bdc899) |

| Functions | |
| --- | --- |
| static void | [net\_ipv4\_autoconf\_start](#a5cbac9cab526f57c9b4a8ec141dbfb99) (struct [net\_if](structnet__if.md) \*iface) |
|  | Start IPv4 autoconfiguration RFC 3927: IPv4 Link Local. |
| static void | [net\_ipv4\_autoconf\_reset](#a4845fd81288d96d72bbf7e8001fd31a5) (struct [net\_if](structnet__if.md) \*iface) |
|  | Reset autoconf process. |

## Detailed Description

IPv4 Autoconfiguration.

## Enumeration Type Documentation

## [◆ ](#abdf8bb08f12768aad2ff95b902bdc899)net\_ipv4\_autoconf\_state

| enum [net\_ipv4\_autoconf\_state](#abdf8bb08f12768aad2ff95b902bdc899) |
| --- |

Current state of IPv4 Autoconfiguration.

| Enumerator | |
| --- | --- |
| NET\_IPV4\_AUTOCONF\_INIT | Initialization state. |
| NET\_IPV4\_AUTOCONF\_ASSIGNED | Assigned state. |
| NET\_IPV4\_AUTOCONF\_RENEW | Renew state. |

## Function Documentation

## [◆ ](#a4845fd81288d96d72bbf7e8001fd31a5)net\_ipv4\_autoconf\_reset()

| | void net\_ipv4\_autoconf\_reset | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Reset autoconf process.

Reset IPv4 IP autoconfiguration

Parameters
:   | iface | A valid pointer on an interface |
    | --- | --- |

## [◆ ](#a5cbac9cab526f57c9b4a8ec141dbfb99)net\_ipv4\_autoconf\_start()

| | void net\_ipv4\_autoconf\_start | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Start IPv4 autoconfiguration RFC 3927: IPv4 Link Local.

Start IPv4 IP autoconfiguration

Parameters
:   | iface | A valid pointer on an interface |
    | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [ipv4\_autoconf.h](ipv4__autoconf_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
