---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structin6__addr.html
original_path: doxygen/html/structin6__addr.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

in6\_addr Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [IPv4/IPv6 primitives and helpers](group__ip__4__6.md)

IPv6 address struct.
[More...](#details)

`#include <[net_ip.h](net__ip_8h_source.md)>`

| Data Fields | |
| --- | --- |
| union { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [s6\_addr](#aa1d600770ac35faa253a53aecd9b3786) [16] |  |
|  | IPv6 address buffer. [More...](#aa1d600770ac35faa253a53aecd9b3786) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [s6\_addr16](#ac639658b289173e364d9e067ec2ceb69) [8] |  |
|  | In big endian. [More...](#ac639658b289173e364d9e067ec2ceb69) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [s6\_addr32](#ab436399c6fe320d361b024bf78af4aba) [4] |  |
|  | In big endian. [More...](#ab436399c6fe320d361b024bf78af4aba) |
| }; |  |

## Detailed Description

IPv6 address struct.

## Field Documentation

## [◆ ](#a9637f26bee5251ad956589aec2273147)[union]

| union { ... } [in6\_addr](structin6__addr.md) |
| --- |

## [◆ ](#aa1d600770ac35faa253a53aecd9b3786)s6\_addr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) in6\_addr::s6\_addr[16] |
| --- |

IPv6 address buffer.

## [◆ ](#ac639658b289173e364d9e067ec2ceb69)s6\_addr16

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) in6\_addr::s6\_addr16[8] |
| --- |

In big endian.

## [◆ ](#ab436399c6fe320d361b024bf78af4aba)s6\_addr32

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) in6\_addr::s6\_addr32[4] |
| --- |

In big endian.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_ip.h](net__ip_8h_source.md)

- [in6\_addr](structin6__addr.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
