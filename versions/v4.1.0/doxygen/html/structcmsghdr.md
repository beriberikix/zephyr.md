---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structcmsghdr.html
original_path: doxygen/html/structcmsghdr.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cmsghdr Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [IPv4/IPv6 primitives and helpers](group__ip__4__6.md)

Control message ancillary data.
[More...](#details)

`#include <[net_ip.h](net__ip_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) | [cmsg\_len](#a7cf479e5e162e65ad164616453d61df2) |
|  | Number of bytes, including header. |
| int | [cmsg\_level](#ac0ff1400cb63fbc2e0ece19434cb8fef) |
|  | Originating protocol. |
| int | [cmsg\_type](#a4c7cabf7899a688ce10bc92773fca9c1) |
|  | Protocol-specific type. |
| z\_max\_align\_t | [cmsg\_data](#a92c00d02575707f72c04f090b6f8d399) [] |
|  | Flexible array member to force alignment of cmsghdr. |

## Detailed Description

Control message ancillary data.

## Field Documentation

## [◆ ](#a92c00d02575707f72c04f090b6f8d399)cmsg\_data

| z\_max\_align\_t cmsghdr::cmsg\_data[] |
| --- |

Flexible array member to force alignment of cmsghdr.

## [◆ ](#a7cf479e5e162e65ad164616453d61df2)cmsg\_len

| [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) cmsghdr::cmsg\_len |
| --- |

Number of bytes, including header.

## [◆ ](#ac0ff1400cb63fbc2e0ece19434cb8fef)cmsg\_level

| int cmsghdr::cmsg\_level |
| --- |

Originating protocol.

## [◆ ](#a4c7cabf7899a688ce10bc92773fca9c1)cmsg\_type

| int cmsghdr::cmsg\_type |
| --- |

Protocol-specific type.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_ip.h](net__ip_8h_source.md)

- [cmsghdr](structcmsghdr.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
