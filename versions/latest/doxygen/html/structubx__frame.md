---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structubx__frame.html
original_path: doxygen/html/structubx__frame.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ubx\_frame Struct Reference

[Connectivity](group__connectivity.md) » [Modem APIs](group__modem.md) » [Modem Ubx](group__modem__ubx.md)

`#include <[ubx.h](ubx_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [preamble\_sync\_char\_1](#acf80f38e8f26bb32848ae2978a1f87a1) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [preamble\_sync\_char\_2](#ac61fb72df7c1cd8a9bacb787071cb77d) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [message\_class](#ab0e1094b79fa8ec4ad32a49d6eb58cd7) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [message\_id](#aca1010905f7286c6627379a3510ff4d8) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [payload\_size\_low](#aa23a944475ce3926847c267e5463f17f) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [payload\_size\_high](#a2f3dda8dff68c4f26ad256453e0302d6) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [payload\_and\_checksum](#a70c465b5bd1e9837c253d78fb210f4ce) [] |

## Field Documentation

## [◆ ](#ab0e1094b79fa8ec4ad32a49d6eb58cd7)message\_class

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ubx\_frame::message\_class |
| --- |

## [◆ ](#aca1010905f7286c6627379a3510ff4d8)message\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ubx\_frame::message\_id |
| --- |

## [◆ ](#a70c465b5bd1e9837c253d78fb210f4ce)payload\_and\_checksum

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ubx\_frame::payload\_and\_checksum[] |
| --- |

## [◆ ](#a2f3dda8dff68c4f26ad256453e0302d6)payload\_size\_high

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ubx\_frame::payload\_size\_high |
| --- |

## [◆ ](#aa23a944475ce3926847c267e5463f17f)payload\_size\_low

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ubx\_frame::payload\_size\_low |
| --- |

## [◆ ](#acf80f38e8f26bb32848ae2978a1f87a1)preamble\_sync\_char\_1

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ubx\_frame::preamble\_sync\_char\_1 |
| --- |

## [◆ ](#ac61fb72df7c1cd8a9bacb787071cb77d)preamble\_sync\_char\_2

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ubx\_frame::preamble\_sync\_char\_2 |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/modem/[ubx.h](ubx_8h_source.md)

- [ubx\_frame](structubx__frame.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
