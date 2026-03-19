---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structrtio__sqe.html
original_path: doxygen/html/structrtio__sqe.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rtio\_sqe Struct Reference

[Operating System Services](group__os__services.md) » [RTIO](group__rtio.md)

A submission queue event.
[More...](#details)

`#include <[rtio.h](rtio_2rtio_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [op](#a1d8d3e3426e47a2c7f54d98f51acd953) |
|  | Op code. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [prio](#a528eb9b721be7b8a8898ab16a7e2d9a7) |
|  | Op priority. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [flags](#aad2ff8524df0e24b812e77e2393bf5b0) |
|  | Op Flags. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [iodev\_flags](#af979ffa7bd3efaa6cbcb1344404cb985) |
|  | Op iodev flags. |
| const struct [rtio\_iodev](structrtio__iodev.md) \* | [iodev](#a6c784702f011592c84feacd57915bbfc) |
|  | Device to operation on. |
| void \* | [userdata](#a0ed519ee0b5867ff73bdaf37f983c971) |
|  | User provided data which is returned upon operation completion. |
| union { |  |
| struct { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [buf\_len](#a67376f40a13960b152a23da250275722) |  |
|  | Length of buffer. [More...](#a67376f40a13960b152a23da250275722) |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*   [buf](#ab71176c084e8b8eb65dfeb3018ae2a49) |  |
|  | Buffer to write from. [More...](#ab71176c084e8b8eb65dfeb3018ae2a49) |
| }   [tx](#a4399cf25c7e761126a6218c2b7e3192d) |
|  | OP\_TX. [More...](#a4399cf25c7e761126a6218c2b7e3192d) |
| struct { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [buf\_len](#a67376f40a13960b152a23da250275722) |  |
|  | Length of buffer. [More...](#a67376f40a13960b152a23da250275722) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*   [buf](#a55e98f27b26393fee8e179b7bdb6a52e) |  |
|  | Buffer to read into. [More...](#a55e98f27b26393fee8e179b7bdb6a52e) |
| }   [rx](#a37a98afc43f26355c70e7036725b2544) |
|  | OP\_RX. [More...](#a37a98afc43f26355c70e7036725b2544) |
| struct { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [buf\_len](#a4125148f520b61d0fe3ba156fbb53322) |  |
|  | Length of tiny buffer. [More...](#a4125148f520b61d0fe3ba156fbb53322) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [buf](#a8f0544318fa972be2541ae1e85efc33f) [7] |  |
|  | Tiny buffer. [More...](#a8f0544318fa972be2541ae1e85efc33f) |
| }   [tiny\_tx](#a19ace9c984538c2022e7f8ecaefa075d) |
|  | OP\_TINY\_TX. [More...](#a19ace9c984538c2022e7f8ecaefa075d) |
| struct { |  |
| [rtio\_callback\_t](group__rtio.md#gad1dbd690e6cf88d7c788436dd04d1a00)   [callback](#af8c31c33e9fedebe55cac73595d0f696) |  |
| void \*   [arg0](#a438d2156a61aef9ca840af9c01d5dfa4) |  |
|  | Last argument given to callback. [More...](#a438d2156a61aef9ca840af9c01d5dfa4) |
| }   [callback](#add4f73af249b5b548ddf8f5b8d84af2b) |
|  | OP\_CALLBACK. [More...](#add4f73af249b5b548ddf8f5b8d84af2b) |
| struct { |  |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [buf\_len](#a67376f40a13960b152a23da250275722) |  |
|  | Length of tx and rx buffers. [More...](#a67376f40a13960b152a23da250275722) |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*   [tx\_buf](#a18bfa63542954f4bb8b924c92c48e931) |  |
|  | Buffer to write from. [More...](#a18bfa63542954f4bb8b924c92c48e931) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*   [rx\_buf](#a4d2090fc11b897724a883ad1087d9f73) |  |
|  | Buffer to read into. [More...](#a4d2090fc11b897724a883ad1087d9f73) |
| }   [txrx](#a5f2511eb361a7a4d54a92fae4d391e8c) |
|  | OP\_TXRX. [More...](#a5f2511eb361a7a4d54a92fae4d391e8c) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [i2c\_config](#a07bf344b1b1063b8bea80cf5ba1c1cc5) |  |
|  | OP\_I2C\_CONFIGURE. [More...](#a07bf344b1b1063b8bea80cf5ba1c1cc5) |
| }; |  |

## Detailed Description

A submission queue event.

## Field Documentation

## [◆ ](#a2c9c387b0ed438ca5e4b7afdf749544e)[union]

| union { ... } [rtio\_sqe](structrtio__sqe.md) |
| --- |

## [◆ ](#a438d2156a61aef9ca840af9c01d5dfa4)arg0

| void\* rtio\_sqe::arg0 |
| --- |

Last argument given to callback.

## [◆ ](#a8f0544318fa972be2541ae1e85efc33f)buf [1/3]

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rtio\_sqe::buf[7] |
| --- |

Tiny buffer.

## [◆ ](#a55e98f27b26393fee8e179b7bdb6a52e)buf [2/3]

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* rtio\_sqe::buf |
| --- |

Buffer to read into.

## [◆ ](#ab71176c084e8b8eb65dfeb3018ae2a49)buf [3/3]

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* rtio\_sqe::buf |
| --- |

Buffer to write from.

## [◆ ](#a4125148f520b61d0fe3ba156fbb53322)buf\_len [1/2]

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rtio\_sqe::buf\_len |
| --- |

Length of tiny buffer.

## [◆ ](#a67376f40a13960b152a23da250275722)buf\_len [2/2]

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) rtio\_sqe::buf\_len |
| --- |

Length of buffer.

Length of tx and rx buffers.

## [◆ ](#add4f73af249b5b548ddf8f5b8d84af2b)[struct] [1/2]

| struct { ... } rtio\_sqe::callback |
| --- |

OP\_CALLBACK.

## [◆ ](#af8c31c33e9fedebe55cac73595d0f696)callback [2/2]

| [rtio\_callback\_t](group__rtio.md#gad1dbd690e6cf88d7c788436dd04d1a00) rtio\_sqe::callback |
| --- |

## [◆ ](#aad2ff8524df0e24b812e77e2393bf5b0)flags

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) rtio\_sqe::flags |
| --- |

Op Flags.

## [◆ ](#a07bf344b1b1063b8bea80cf5ba1c1cc5)i2c\_config

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) rtio\_sqe::i2c\_config |
| --- |

OP\_I2C\_CONFIGURE.

## [◆ ](#a6c784702f011592c84feacd57915bbfc)iodev

| const struct [rtio\_iodev](structrtio__iodev.md)\* rtio\_sqe::iodev |
| --- |

Device to operation on.

## [◆ ](#af979ffa7bd3efaa6cbcb1344404cb985)iodev\_flags

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) rtio\_sqe::iodev\_flags |
| --- |

Op iodev flags.

## [◆ ](#a1d8d3e3426e47a2c7f54d98f51acd953)op

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rtio\_sqe::op |
| --- |

Op code.

## [◆ ](#a528eb9b721be7b8a8898ab16a7e2d9a7)prio

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rtio\_sqe::prio |
| --- |

Op priority.

## [◆ ](#a37a98afc43f26355c70e7036725b2544)[struct]

| struct { ... } rtio\_sqe::rx |
| --- |

OP\_RX.

## [◆ ](#a4d2090fc11b897724a883ad1087d9f73)rx\_buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* rtio\_sqe::rx\_buf |
| --- |

Buffer to read into.

## [◆ ](#a19ace9c984538c2022e7f8ecaefa075d)[struct]

| struct { ... } rtio\_sqe::tiny\_tx |
| --- |

OP\_TINY\_TX.

## [◆ ](#a4399cf25c7e761126a6218c2b7e3192d)[struct]

| struct { ... } rtio\_sqe::tx |
| --- |

OP\_TX.

## [◆ ](#a18bfa63542954f4bb8b924c92c48e931)tx\_buf

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* rtio\_sqe::tx\_buf |
| --- |

Buffer to write from.

## [◆ ](#a5f2511eb361a7a4d54a92fae4d391e8c)[struct]

| struct { ... } rtio\_sqe::txrx |
| --- |

OP\_TXRX.

## [◆ ](#a0ed519ee0b5867ff73bdaf37f983c971)userdata

| void\* rtio\_sqe::userdata |
| --- |

User provided data which is returned upon operation completion.

Could be a pointer or integer.

If unique identification of completions is desired this should be unique as well.

---

The documentation for this struct was generated from the following file:

- zephyr/rtio/[rtio.h](rtio_2rtio_8h_source.md)

- [rtio\_sqe](structrtio__sqe.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
