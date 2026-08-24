---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structmodem__ubx__script.html
original_path: doxygen/html/structmodem__ubx__script.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

modem\_ubx\_script Struct Reference

[Connectivity](group__connectivity.md) » [Modem APIs](group__modem.md) » [Modem Ubx](group__modem__ubx.md)

`#include <[zephyr/modem/ubx.h](ubx_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct { |  |
| const struct [ubx\_frame](structubx__frame.md) \*   [buf](#aade7c60068e44b39bfac09415e31417c) |  |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [len](#a033047efbf34102985fad507711905ec) |  |
| } | [request](#ab91b22317aa1cfb36f7c24de2b425137) |
| struct { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*   [buf](#aa1ffe8666c2e2169c6067710f9b3ccc7) |  |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [buf\_len](#a9882eb3b10b9739c916f5317fda412ea) |  |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [received\_len](#a716f90ed421af01c829cb716d94a9a76) |  |
| } | [response](#a90d08ee6c3832f3d0198cea0aa7b3b8d) |
| struct [modem\_ubx\_match](structmodem__ubx__match.md) | [match](#a1e91925ba17f30685db67d4f326d2f31) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [retry\_count](#a4910a3551004f19249c66a5b695795ce) |
| [k\_timeout\_t](structk__timeout__t.md) | [timeout](#a041de757b5fb26f1cdfb89cb19610f11) |

## Field Documentation

## [◆ ](#aa1ffe8666c2e2169c6067710f9b3ccc7)buf [1/2]

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* modem\_ubx\_script::buf |
| --- |

## [◆ ](#aade7c60068e44b39bfac09415e31417c)buf [2/2]

| const struct [ubx\_frame](structubx__frame.md)\* modem\_ubx\_script::buf |
| --- |

## [◆ ](#a9882eb3b10b9739c916f5317fda412ea)buf\_len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) modem\_ubx\_script::buf\_len |
| --- |

## [◆ ](#a033047efbf34102985fad507711905ec)len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) modem\_ubx\_script::len |
| --- |

## [◆ ](#a1e91925ba17f30685db67d4f326d2f31)match

| struct [modem\_ubx\_match](structmodem__ubx__match.md) modem\_ubx\_script::match |
| --- |

## [◆ ](#a716f90ed421af01c829cb716d94a9a76)received\_len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) modem\_ubx\_script::received\_len |
| --- |

## [◆ ](#ab91b22317aa1cfb36f7c24de2b425137)[struct]

| struct { ... } modem\_ubx\_script::request |
| --- |

## [◆ ](#a90d08ee6c3832f3d0198cea0aa7b3b8d)[struct]

| struct { ... } modem\_ubx\_script::response |
| --- |

## [◆ ](#a4910a3551004f19249c66a5b695795ce)retry\_count

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) modem\_ubx\_script::retry\_count |
| --- |

## [◆ ](#a041de757b5fb26f1cdfb89cb19610f11)timeout

| [k\_timeout\_t](structk__timeout__t.md) modem\_ubx\_script::timeout |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/modem/[ubx.h](ubx_8h_source.md)

- [modem\_ubx\_script](structmodem__ubx__script.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
