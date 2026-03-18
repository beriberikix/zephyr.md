---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structmsghdr.html
original_path: doxygen/html/structmsghdr.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

msghdr Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [IPv4/IPv6 primitives and helpers](group__ip__4__6.md)

Message struct.
[More...](#details)

`#include <[net_ip.h](net__ip_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void \* | [msg\_name](#a691a8866b21c7083974a2ff1e7987ce1) |
|  | Optional socket address, big endian. |
| [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) | [msg\_namelen](#a47762b69eee1c9ba5736d64516ea0960) |
|  | Size of socket address. |
| struct [iovec](structiovec.md) \* | [msg\_iov](#a1b893a6f84c4ba52708c5dcfcc720293) |
|  | Scatter/gather array. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [msg\_iovlen](#ad4ef1bd6821e599bf42f936850d2c4d7) |
|  | Number of elements in msg\_iov. |
| void \* | [msg\_control](#afba5fc31b0f197e25602d2232ca6d783) |
|  | Ancillary data. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [msg\_controllen](#a9fa41b0e9a02b5dc9a01aa6f18108adb) |
|  | Ancillary data buffer len. |
| int | [msg\_flags](#a9e8ff97d402c99551cbfd564e9e10a74) |
|  | Flags on received message. |

## Detailed Description

Message struct.

## Field Documentation

## [◆ ](#afba5fc31b0f197e25602d2232ca6d783)msg\_control

| void\* msghdr::msg\_control |
| --- |

Ancillary data.

## [◆ ](#a9fa41b0e9a02b5dc9a01aa6f18108adb)msg\_controllen

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) msghdr::msg\_controllen |
| --- |

Ancillary data buffer len.

## [◆ ](#a9e8ff97d402c99551cbfd564e9e10a74)msg\_flags

| int msghdr::msg\_flags |
| --- |

Flags on received message.

## [◆ ](#a1b893a6f84c4ba52708c5dcfcc720293)msg\_iov

| struct [iovec](structiovec.md)\* msghdr::msg\_iov |
| --- |

Scatter/gather array.

## [◆ ](#ad4ef1bd6821e599bf42f936850d2c4d7)msg\_iovlen

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) msghdr::msg\_iovlen |
| --- |

Number of elements in msg\_iov.

## [◆ ](#a691a8866b21c7083974a2ff1e7987ce1)msg\_name

| void\* msghdr::msg\_name |
| --- |

Optional socket address, big endian.

## [◆ ](#a47762b69eee1c9ba5736d64516ea0960)msg\_namelen

| [socklen\_t](group__ip__4__6.md#gacf0ed818b0a3c85ff6a9206679d6d91a) msghdr::msg\_namelen |
| --- |

Size of socket address.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_ip.h](net__ip_8h_source.md)

- [msghdr](structmsghdr.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
