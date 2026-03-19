---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structmpl__cmd.html
original_path: doxygen/html/structmpl__cmd.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mpl\_cmd Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Media Proxy](group__bt__media__proxy.md)

Media player command.
[More...](#details)

`#include <[media_proxy.h](media__proxy_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [opcode](#a5cb29ca9e5a6b8249c69cc975b345e2f) |
|  | The opcode. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [use\_param](#aca5e50b9f883a3c81f10ad51032a31f9) |
|  | Whether or not the [mpl\_cmd::param](#ade5ed4d0ff2aeb192b8ed6b586c9bc9e) is used. |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [param](#ade5ed4d0ff2aeb192b8ed6b586c9bc9e) |
|  | A 32-bit signed parameter. |

## Detailed Description

Media player command.

## Field Documentation

## [◆ ](#a5cb29ca9e5a6b8249c69cc975b345e2f)opcode

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mpl\_cmd::opcode |
| --- |

The opcode.

See the MEDIA\_PROXY\_OP\_\* values

## [◆ ](#ade5ed4d0ff2aeb192b8ed6b586c9bc9e)param

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) mpl\_cmd::param |
| --- |

A 32-bit signed parameter.

The parameter value depends on the [mpl\_cmd::opcode](#a5cb29ca9e5a6b8249c69cc975b345e2f)

## [◆ ](#aca5e50b9f883a3c81f10ad51032a31f9)use\_param

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) mpl\_cmd::use\_param |
| --- |

Whether or not the [mpl\_cmd::param](#ade5ed4d0ff2aeb192b8ed6b586c9bc9e) is used.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[media\_proxy.h](media__proxy_8h_source.md)

- [mpl\_cmd](structmpl__cmd.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
