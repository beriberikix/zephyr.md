---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structmodem__ubx.html
original_path: doxygen/html/structmodem__ubx.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

modem\_ubx Struct Reference

[Connectivity](group__connectivity.md) » [Modem APIs](group__modem.md) » [Modem Ubx](group__modem__ubx.md)

`#include <[ubx.h](ubx_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void \* | [user\_data](#ad98fcc4a93781ff5cd5406cb0560c849) |
| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) | [state](#a6d07a9579a24e28b8c55133d9df4c8da) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [receive\_buf](#a0bc3ee485c2e6f63727efae5b61a64ac) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [receive\_buf\_size](#a4add513db024eb040de858e8901bc017) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [work\_buf](#aad1408bdba802cbf2c98e447c53299dc) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [work\_buf\_size](#a2197970808d4b5b5bda78d70d3669a38) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [work\_buf\_len](#a9a4d782877f3b6e28ca385d438d00837) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [ubx\_preamble\_sync\_chars\_received](#a7ad137c9494039cdbc986af00b6e946b) |
| const struct [modem\_ubx\_script](structmodem__ubx__script.md) \* | [script](#aa62a198023dcc02706f4a653e4eadbe5) |
| struct modem\_pipe \* | [pipe](#a1b853c80109313feaebfb8cdb24b950c) |
| struct [k\_work](structk__work.md) | [send\_work](#aedbd81b987524f65c54838ea445bd8fd) |
| struct [k\_work](structk__work.md) | [process\_work](#adfd9249b1f72aae1f2b9818cbf0de640) |
| struct k\_sem | [script\_stopped\_sem](#ae5c5914a3c88b908e80646d71ada7bfe) |
| struct k\_sem | [script\_running\_sem](#a0489f188b1dcdd54ba756ad821c62db5) |

## Field Documentation

## [◆ ](#a1b853c80109313feaebfb8cdb24b950c)pipe

| struct modem\_pipe\* modem\_ubx::pipe |
| --- |

## [◆ ](#adfd9249b1f72aae1f2b9818cbf0de640)process\_work

| struct [k\_work](structk__work.md) modem\_ubx::process\_work |
| --- |

## [◆ ](#a0bc3ee485c2e6f63727efae5b61a64ac)receive\_buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* modem\_ubx::receive\_buf |
| --- |

## [◆ ](#a4add513db024eb040de858e8901bc017)receive\_buf\_size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) modem\_ubx::receive\_buf\_size |
| --- |

## [◆ ](#aa62a198023dcc02706f4a653e4eadbe5)script

| const struct [modem\_ubx\_script](structmodem__ubx__script.md)\* modem\_ubx::script |
| --- |

## [◆ ](#a0489f188b1dcdd54ba756ad821c62db5)script\_running\_sem

| struct k\_sem modem\_ubx::script\_running\_sem |
| --- |

## [◆ ](#ae5c5914a3c88b908e80646d71ada7bfe)script\_stopped\_sem

| struct k\_sem modem\_ubx::script\_stopped\_sem |
| --- |

## [◆ ](#aedbd81b987524f65c54838ea445bd8fd)send\_work

| struct [k\_work](structk__work.md) modem\_ubx::send\_work |
| --- |

## [◆ ](#a6d07a9579a24e28b8c55133d9df4c8da)state

| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) modem\_ubx::state |
| --- |

## [◆ ](#a7ad137c9494039cdbc986af00b6e946b)ubx\_preamble\_sync\_chars\_received

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) modem\_ubx::ubx\_preamble\_sync\_chars\_received |
| --- |

## [◆ ](#ad98fcc4a93781ff5cd5406cb0560c849)user\_data

| void\* modem\_ubx::user\_data |
| --- |

## [◆ ](#aad1408bdba802cbf2c98e447c53299dc)work\_buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* modem\_ubx::work\_buf |
| --- |

## [◆ ](#a9a4d782877f3b6e28ca385d438d00837)work\_buf\_len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) modem\_ubx::work\_buf\_len |
| --- |

## [◆ ](#a2197970808d4b5b5bda78d70d3669a38)work\_buf\_size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) modem\_ubx::work\_buf\_size |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/modem/[ubx.h](ubx_8h_source.md)

- [modem\_ubx](structmodem__ubx.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
