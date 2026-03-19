---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structdac__channel__cfg.html
original_path: doxygen/html/structdac__channel__cfg.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dac\_channel\_cfg Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [DAC driver APIs](group__dac__interface.md)

Structure for specifying the configuration of a DAC channel.
[More...](#details)

`#include <[dac.h](dac_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [channel\_id](#a41a1708aa81b2a808556ec976ce303f3) |
|  | Channel identifier of the DAC that should be configured. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [resolution](#a4ba4f6dde3e4525e0a0e71fea5aeaef3) |
|  | Desired resolution of the DAC (depends on device capabilities). |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [buffered](#a31df5ad55f40cb89819fac3acd6b4d96): 1 |
|  | Enable output buffer for this channel. |

## Detailed Description

Structure for specifying the configuration of a DAC channel.

## Field Documentation

## [◆ ](#a31df5ad55f40cb89819fac3acd6b4d96)buffered

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) dac\_channel\_cfg::buffered |
| --- |

Enable output buffer for this channel.

This is relevant for instance if the output is directly connected to the load, without an amplifierin between. The actual details on this are hardware dependent.

## [◆ ](#a41a1708aa81b2a808556ec976ce303f3)channel\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dac\_channel\_cfg::channel\_id |
| --- |

Channel identifier of the DAC that should be configured.

## [◆ ](#a4ba4f6dde3e4525e0a0e71fea5aeaef3)resolution

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dac\_channel\_cfg::resolution |
| --- |

Desired resolution of the DAC (depends on device capabilities).

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[dac.h](dac_8h_source.md)

- [dac\_channel\_cfg](structdac__channel__cfg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
