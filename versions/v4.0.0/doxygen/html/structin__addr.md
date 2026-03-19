---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structin__addr.html
original_path: doxygen/html/structin__addr.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

in\_addr Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [IPv4/IPv6 primitives and helpers](group__ip__4__6.md)

IPv4 address struct.
[More...](#details)

`#include <[net_ip.h](net__ip_8h_source.md)>`

| Data Fields | |
| --- | --- |
| union { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [s4\_addr](#a4fd35e401c510fabab8979eb8416dd9b) [4] |  |
|  | IPv4 address buffer. [More...](#a4fd35e401c510fabab8979eb8416dd9b) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [s4\_addr16](#ab3122fff9d58baf7dc4f12c6f021fd86) [2] |  |
|  | In big endian. [More...](#ab3122fff9d58baf7dc4f12c6f021fd86) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [s4\_addr32](#ae4e092a27efb643067d7ce10bd454bed) [1] |  |
|  | In big endian. [More...](#ae4e092a27efb643067d7ce10bd454bed) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [s\_addr](#a5abe94a260a50619a60ce111a59f00b5) |  |
|  | In big endian, for POSIX compatibility. [More...](#a5abe94a260a50619a60ce111a59f00b5) |
| }; |  |

## Detailed Description

IPv4 address struct.

## Field Documentation

## [◆ ](#abfe49d626f4df74c4ac51aee66ce9661)[union]

| union { ... } [in\_addr](structin__addr.md) |
| --- |

## [◆ ](#a4fd35e401c510fabab8979eb8416dd9b)s4\_addr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) in\_addr::s4\_addr[4] |
| --- |

IPv4 address buffer.

## [◆ ](#ab3122fff9d58baf7dc4f12c6f021fd86)s4\_addr16

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) in\_addr::s4\_addr16[2] |
| --- |

In big endian.

## [◆ ](#ae4e092a27efb643067d7ce10bd454bed)s4\_addr32

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) in\_addr::s4\_addr32[1] |
| --- |

In big endian.

## [◆ ](#a5abe94a260a50619a60ce111a59f00b5)s\_addr

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) in\_addr::s\_addr |
| --- |

In big endian, for POSIX compatibility.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_ip.h](net__ip_8h_source.md)

- [in\_addr](structin__addr.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
