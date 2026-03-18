---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structosdp__cmd.html
original_path: doxygen/html/structosdp__cmd.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

osdp\_cmd Struct Reference

OSDP Command Structure.
[More...](#details)

`#include <[osdp.h](osdp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [osdp\_cmd\_e](osdp_8h.md#abd8555e895d9370da1400f76c931ba21) | [id](#a47c50d8c39cd47a7ad282dc91c4e9da8) |
|  | Command ID. |
| union { |  |
| struct [osdp\_cmd\_led](structosdp__cmd__led.md)   [led](#acc408da549c0ef9a83e5a569b64dcb36) |  |
|  | LED command structure. [More...](#acc408da549c0ef9a83e5a569b64dcb36) |
| struct [osdp\_cmd\_buzzer](structosdp__cmd__buzzer.md)   [buzzer](#a62250f899e17c6fd94a1629f5ef9a479) |  |
|  | Buzzer command structure. [More...](#a62250f899e17c6fd94a1629f5ef9a479) |
| struct [osdp\_cmd\_text](structosdp__cmd__text.md)   [text](#a70630f6a8fbebacc27d889dec52336c8) |  |
|  | Text command structure. [More...](#a70630f6a8fbebacc27d889dec52336c8) |
| struct [osdp\_cmd\_output](structosdp__cmd__output.md)   [output](#aa745b1efadce9bc41e7253b76bdf2adf) |  |
|  | Output command structure. [More...](#aa745b1efadce9bc41e7253b76bdf2adf) |
| struct [osdp\_cmd\_comset](structosdp__cmd__comset.md)   [comset](#a54d63398e914cd41567288f0da456e11) |  |
|  | Comset command structure. [More...](#a54d63398e914cd41567288f0da456e11) |
| struct [osdp\_cmd\_keyset](structosdp__cmd__keyset.md)   [keyset](#ad629c2622377800a0deab60756fa35a4) |  |
|  | Keyset command structure. [More...](#ad629c2622377800a0deab60756fa35a4) |
| }; |  |
|  | Command. |

## Detailed Description

OSDP Command Structure.

This is a wrapper for all individual OSDP commands.

## Field Documentation

## [◆ ](#a706e31fbf66538a82d137676df0acc75)[union]

| union { ... } [osdp\_cmd](structosdp__cmd.md) |
| --- |

Command.

## [◆ ](#a62250f899e17c6fd94a1629f5ef9a479)buzzer

| struct [osdp\_cmd\_buzzer](structosdp__cmd__buzzer.md) osdp\_cmd::buzzer |
| --- |

Buzzer command structure.

## [◆ ](#a54d63398e914cd41567288f0da456e11)comset

| struct [osdp\_cmd\_comset](structosdp__cmd__comset.md) osdp\_cmd::comset |
| --- |

Comset command structure.

## [◆ ](#a47c50d8c39cd47a7ad282dc91c4e9da8)id

| enum [osdp\_cmd\_e](osdp_8h.md#abd8555e895d9370da1400f76c931ba21) osdp\_cmd::id |
| --- |

Command ID.

Used to select specific commands in union.

## [◆ ](#ad629c2622377800a0deab60756fa35a4)keyset

| struct [osdp\_cmd\_keyset](structosdp__cmd__keyset.md) osdp\_cmd::keyset |
| --- |

Keyset command structure.

## [◆ ](#acc408da549c0ef9a83e5a569b64dcb36)led

| struct [osdp\_cmd\_led](structosdp__cmd__led.md) osdp\_cmd::led |
| --- |

LED command structure.

## [◆ ](#aa745b1efadce9bc41e7253b76bdf2adf)output

| struct [osdp\_cmd\_output](structosdp__cmd__output.md) osdp\_cmd::output |
| --- |

Output command structure.

## [◆ ](#a70630f6a8fbebacc27d889dec52336c8)text

| struct [osdp\_cmd\_text](structosdp__cmd__text.md) osdp\_cmd::text |
| --- |

Text command structure.

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/[osdp.h](osdp_8h_source.md)

- [osdp\_cmd](structosdp__cmd.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
