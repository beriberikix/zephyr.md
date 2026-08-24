---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structmodem__ubx.html
original_path: doxygen/html/structmodem__ubx.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

modem\_ubx Struct Reference

[Connectivity](group__connectivity.md) » [Modem APIs](group__modem.md) » [Modem Ubx](group__modem__ubx.md)

`#include <[zephyr/modem/ubx.h](ubx_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void \* | [user\_data](#ad98fcc4a93781ff5cd5406cb0560c849) |
| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) | [attached](#a337b4afe37e031ecd563572951be9412) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [receive\_buf](#a0bc3ee485c2e6f63727efae5b61a64ac) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [receive\_buf\_size](#a4add513db024eb040de858e8901bc017) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [receive\_buf\_offset](#a639183a5a24d953015df30f64b2f1c85) |
| struct [modem\_ubx\_script](structmodem__ubx__script.md) \* | [script](#ac9a3b4009eabeb92e2e3cff093d74d2c) |
| struct modem\_pipe \* | [pipe](#a1b853c80109313feaebfb8cdb24b950c) |
| struct [k\_work](structk__work.md) | [process\_work](#adfd9249b1f72aae1f2b9818cbf0de640) |
| struct [k\_sem](structk__sem.md) | [script\_stopped\_sem](#ae5c5914a3c88b908e80646d71ada7bfe) |
| struct [k\_sem](structk__sem.md) | [script\_running\_sem](#a0489f188b1dcdd54ba756ad821c62db5) |
| struct { |  |
| const struct [modem\_ubx\_match](structmodem__ubx__match.md) \*   [array](#ae7182d2345bcd3585828f0f48d42321a) |  |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9)   [size](#a98b8d6b02acbfa564b510b6f7c9908d5) |  |
| } | [unsol\_matches](#aeeb735c338ed161d7eddeaa561cca5d9) |

## Field Documentation

## [◆ ](#ae7182d2345bcd3585828f0f48d42321a)array

| const struct [modem\_ubx\_match](structmodem__ubx__match.md)\* modem\_ubx::array |
| --- |

## [◆ ](#a337b4afe37e031ecd563572951be9412)attached

| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) modem\_ubx::attached |
| --- |

## [◆ ](#a1b853c80109313feaebfb8cdb24b950c)pipe

| struct modem\_pipe\* modem\_ubx::pipe |
| --- |

## [◆ ](#adfd9249b1f72aae1f2b9818cbf0de640)process\_work

| struct [k\_work](structk__work.md) modem\_ubx::process\_work |
| --- |

## [◆ ](#a0bc3ee485c2e6f63727efae5b61a64ac)receive\_buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* modem\_ubx::receive\_buf |
| --- |

## [◆ ](#a639183a5a24d953015df30f64b2f1c85)receive\_buf\_offset

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) modem\_ubx::receive\_buf\_offset |
| --- |

## [◆ ](#a4add513db024eb040de858e8901bc017)receive\_buf\_size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) modem\_ubx::receive\_buf\_size |
| --- |

## [◆ ](#ac9a3b4009eabeb92e2e3cff093d74d2c)script

| struct [modem\_ubx\_script](structmodem__ubx__script.md)\* modem\_ubx::script |
| --- |

## [◆ ](#a0489f188b1dcdd54ba756ad821c62db5)script\_running\_sem

| struct [k\_sem](structk__sem.md) modem\_ubx::script\_running\_sem |
| --- |

## [◆ ](#ae5c5914a3c88b908e80646d71ada7bfe)script\_stopped\_sem

| struct [k\_sem](structk__sem.md) modem\_ubx::script\_stopped\_sem |
| --- |

## [◆ ](#a98b8d6b02acbfa564b510b6f7c9908d5)size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) modem\_ubx::size |
| --- |

## [◆ ](#aeeb735c338ed161d7eddeaa561cca5d9)[struct]

| struct { ... } modem\_ubx::unsol\_matches |
| --- |

## [◆ ](#ad98fcc4a93781ff5cd5406cb0560c849)user\_data

| void\* modem\_ubx::user\_data |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/modem/[ubx.h](ubx_8h_source.md)

- [modem\_ubx](structmodem__ubx.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
