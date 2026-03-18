---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structnet__trickle.html
original_path: doxygen/html/structnet__trickle.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_trickle Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Trickle Algorithm Library](group__trickle.md)

The variable names are taken directly from RFC 6206 when applicable.
[More...](#details)

`#include <[trickle.h](trickle_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [Imin](#aaf14e013a0fa74488a26cd7ff476f6e7) |
|  | Min interval size in ms. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [Imax](#a01ffd968b645bb66db67c759520298aa) |
|  | Max number of doublings. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [k](#a7c3399e45f85874cec48434d605066d9) |
|  | Redundancy constant. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [I](#a6186d8e41cce5193851587d1c72162ea) |
|  | Current interval size. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [Istart](#aab8a98c8a918528db6f2ddec85df4796) |
|  | Start of the interval in ms. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [c](#aaa03f7763e6bd335b932896ee4433b3b) |
|  | Consistency counter. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [Imax\_abs](#ae9f7ecd9b9730cd1c232ead5d21fec05) |
|  | Max interval size in ms (not doublings). |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [double\_to](#a2a1fb8ad04123ebcb781bc3e0173d8be) |
| struct [k\_work\_delayable](structk__work__delayable.md) | [timer](#a2dde5d732f009a85a27ff6fa0c778636) |
| [net\_trickle\_cb\_t](group__trickle.md#gaef7719dc563ae9bb93ed5313ed568b44) | [cb](#a63a3cbf019c99def91e3a9dde7c2f9b4) |
|  | Callback to be called when timer expires. |
| void \* | [user\_data](#a40f69e10d41e34541ca88c092d6a3341) |

## Detailed Description

The variable names are taken directly from RFC 6206 when applicable.

Note that the struct members should not be accessed directly but only via the Trickle API.

## Field Documentation

## [◆ ](#aaa03f7763e6bd335b932896ee4433b3b)c

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_trickle::c |
| --- |

Consistency counter.

## [◆ ](#a63a3cbf019c99def91e3a9dde7c2f9b4)cb

| [net\_trickle\_cb\_t](group__trickle.md#gaef7719dc563ae9bb93ed5313ed568b44) net\_trickle::cb |
| --- |

Callback to be called when timer expires.

## [◆ ](#a2a1fb8ad04123ebcb781bc3e0173d8be)double\_to

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) net\_trickle::double\_to |
| --- |

## [◆ ](#a6186d8e41cce5193851587d1c72162ea)I

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_trickle::I |
| --- |

Current interval size.

## [◆ ](#a01ffd968b645bb66db67c759520298aa)Imax

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_trickle::Imax |
| --- |

Max number of doublings.

## [◆ ](#ae9f7ecd9b9730cd1c232ead5d21fec05)Imax\_abs

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_trickle::Imax\_abs |
| --- |

Max interval size in ms (not doublings).

## [◆ ](#aaf14e013a0fa74488a26cd7ff476f6e7)Imin

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_trickle::Imin |
| --- |

Min interval size in ms.

## [◆ ](#aab8a98c8a918528db6f2ddec85df4796)Istart

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) net\_trickle::Istart |
| --- |

Start of the interval in ms.

## [◆ ](#a7c3399e45f85874cec48434d605066d9)k

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_trickle::k |
| --- |

Redundancy constant.

## [◆ ](#a2dde5d732f009a85a27ff6fa0c778636)timer

| struct [k\_work\_delayable](structk__work__delayable.md) net\_trickle::timer |
| --- |

## [◆ ](#a40f69e10d41e34541ca88c092d6a3341)user\_data

| void\* net\_trickle::user\_data |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/net/[trickle.h](trickle_8h_source.md)

- [net\_trickle](structnet__trickle.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
