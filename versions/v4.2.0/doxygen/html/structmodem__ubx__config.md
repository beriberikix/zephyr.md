---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structmodem__ubx__config.html
original_path: doxygen/html/structmodem__ubx__config.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

modem\_ubx\_config Struct Reference

[Connectivity](group__connectivity.md) » [Modem APIs](group__modem.md) » [Modem Ubx](group__modem__ubx.md)

`#include <[zephyr/modem/ubx.h](ubx_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void \* | [user\_data](#acac2ab2800443c4f60cbf5df9ca8cd5e) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [receive\_buf](#a7ac0f254167c3197366b210bef2ac75d) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [receive\_buf\_size](#a75634cde7a69ef78ea0370f423307a0e) |
| struct { |  |
| const struct [modem\_ubx\_match](structmodem__ubx__match.md) \*   [array](#a75237681e1c9bf094b347e71e1ad823e) |  |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9)   [size](#a19f107638346a44bddc73045f595ec98) |  |
| } | [unsol\_matches](#a08ba4ac10872f451a302fcbc04a04253) |

## Field Documentation

## [◆ ](#a75237681e1c9bf094b347e71e1ad823e)array

| const struct [modem\_ubx\_match](structmodem__ubx__match.md)\* modem\_ubx\_config::array |
| --- |

## [◆ ](#a7ac0f254167c3197366b210bef2ac75d)receive\_buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* modem\_ubx\_config::receive\_buf |
| --- |

## [◆ ](#a75634cde7a69ef78ea0370f423307a0e)receive\_buf\_size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) modem\_ubx\_config::receive\_buf\_size |
| --- |

## [◆ ](#a19f107638346a44bddc73045f595ec98)size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) modem\_ubx\_config::size |
| --- |

## [◆ ](#a08ba4ac10872f451a302fcbc04a04253)[struct]

| struct { ... } modem\_ubx\_config::unsol\_matches |
| --- |

## [◆ ](#acac2ab2800443c4f60cbf5df9ca8cd5e)user\_data

| void\* modem\_ubx\_config::user\_data |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/modem/[ubx.h](ubx_8h_source.md)

- [modem\_ubx\_config](structmodem__ubx__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
