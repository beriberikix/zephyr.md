---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structpdm__io__cfg.html
original_path: doxygen/html/structpdm__io__cfg.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pdm\_io\_cfg Struct Reference

[Audio](group__audio__interface.md) » [Digital Microphone Interface](group__audio__dmic__interface.md)

PDM Input/Output signal configuration.
[More...](#details)

`#include <[dmic.h](dmic_8h_source.md)>`

| Data Fields | |
| --- | --- |
| Parameters common to all PDM controllers | |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [min\_pdm\_clk\_freq](#ae308635d30eaee617cb62c03c0255f37) |
|  | Minimum clock frequency supported by the mic. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [max\_pdm\_clk\_freq](#a4f07b2239435b0ac21e1049413d1a03a) |
|  | Maximum clock frequency supported by the mic. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [min\_pdm\_clk\_dc](#a14d6d390746f7731c4ff203a4beec5fe) |
|  | Minimum duty cycle in % supported by the mic. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [max\_pdm\_clk\_dc](#aa03fbcc1f17fb2597bfa8c1898b74455) |
|  | Maximum duty cycle in % supported by the mic. |
| Parameters unique to each PDM controller | |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [pdm\_clk\_pol](#a4a12d293f2c8edae3e7e5b71646ee55e) |
|  | Bit mask to optionally invert PDM clock. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [pdm\_data\_pol](#aa242b3383b20e0673ed47eea8450e9a7) |
|  | Bit mask to optionally invert mic data. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pdm\_clk\_skew](#a692d7e838db86ca84558eb3e3170551a) |
|  | Collection of clock skew values for each PDM port. |

## Detailed Description

PDM Input/Output signal configuration.

## Field Documentation

## [◆ ](#aa03fbcc1f17fb2597bfa8c1898b74455)max\_pdm\_clk\_dc

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pdm\_io\_cfg::max\_pdm\_clk\_dc |
| --- |

Maximum duty cycle in % supported by the mic.

## [◆ ](#a4f07b2239435b0ac21e1049413d1a03a)max\_pdm\_clk\_freq

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pdm\_io\_cfg::max\_pdm\_clk\_freq |
| --- |

Maximum clock frequency supported by the mic.

## [◆ ](#a14d6d390746f7731c4ff203a4beec5fe)min\_pdm\_clk\_dc

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pdm\_io\_cfg::min\_pdm\_clk\_dc |
| --- |

Minimum duty cycle in % supported by the mic.

## [◆ ](#ae308635d30eaee617cb62c03c0255f37)min\_pdm\_clk\_freq

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pdm\_io\_cfg::min\_pdm\_clk\_freq |
| --- |

Minimum clock frequency supported by the mic.

## [◆ ](#a4a12d293f2c8edae3e7e5b71646ee55e)pdm\_clk\_pol

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pdm\_io\_cfg::pdm\_clk\_pol |
| --- |

Bit mask to optionally invert PDM clock.

## [◆ ](#a692d7e838db86ca84558eb3e3170551a)pdm\_clk\_skew

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pdm\_io\_cfg::pdm\_clk\_skew |
| --- |

Collection of clock skew values for each PDM port.

## [◆ ](#aa242b3383b20e0673ed47eea8450e9a7)pdm\_data\_pol

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pdm\_io\_cfg::pdm\_data\_pol |
| --- |

Bit mask to optionally invert mic data.

---

The documentation for this struct was generated from the following file:

- zephyr/audio/[dmic.h](dmic_8h_source.md)

- [pdm\_io\_cfg](structpdm__io__cfg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
