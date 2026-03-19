---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structlitex__clk__setup.html
original_path: doxygen/html/structlitex__clk__setup.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

litex\_clk\_setup Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Clock Control Interface](group__clock__control__interface.md) » [LiteX Clock Control driver interface](group__clock__control__litex__interface.md)

Structure for interfacing with clock control API.
[More...](#details)

`#include <[clock_control_litex.h](clock__control__litex_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [clkout\_nr](#a3aae2c535eda1df7dcde112a87a9f767) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [rate](#a630a776504a52618c9bbdb6899956567) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [phase](#a5f0684af5cddeb4222142c57ff935b2d) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [duty](#a237035479b7a9fec8eaa5ac9c104e977) |

## Detailed Description

Structure for interfacing with clock control API.

Parameters
:   | [clkout\_nr](#a3aae2c535eda1df7dcde112a87a9f767) | Number of clock output to be changed |
    | --- | --- |
    | [rate](#a630a776504a52618c9bbdb6899956567) | Frequency to set given in Hz |
    | [phase](#a5f0684af5cddeb4222142c57ff935b2d) | Phase offset in degrees |
    | [duty](#a237035479b7a9fec8eaa5ac9c104e977) | Duty cycle of clock signal in percent |

## Field Documentation

## [◆ ](#a3aae2c535eda1df7dcde112a87a9f767)clkout\_nr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) litex\_clk\_setup::clkout\_nr |
| --- |

## [◆ ](#a237035479b7a9fec8eaa5ac9c104e977)duty

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) litex\_clk\_setup::duty |
| --- |

## [◆ ](#a5f0684af5cddeb4222142c57ff935b2d)phase

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) litex\_clk\_setup::phase |
| --- |

## [◆ ](#a630a776504a52618c9bbdb6899956567)rate

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) litex\_clk\_setup::rate |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/clock\_control/[clock\_control\_litex.h](clock__control__litex_8h_source.md)

- [litex\_clk\_setup](structlitex__clk__setup.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
