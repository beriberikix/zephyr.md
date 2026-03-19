---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structi3c__ccc__deftgts__target.html
original_path: doxygen/html/structi3c__ccc__deftgts__target.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i3c\_ccc\_deftgts\_target Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [I3C Interface](group__i3c__interface.md) » [I3C Common Command Codes](group__i3c__ccc.md)

The target device part of payload for DEFTGTS CCC.
[More...](#details)

`#include <[ccc.h](ccc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [addr](#a34a02df3d4dc456733746437b2cd983a) |
|  | Dynamic Address of a target device, or a group address. |
| union { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [dcr](#a08689c18d74fa4b74fc2ada055394e65) |  |
|  | Device Characteristic Register of a I3C target device or a group. [More...](#a08689c18d74fa4b74fc2ada055394e65) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [lvr](#ab4fbe6aac8d5860ef90613e51b15ef83) |  |
|  | Legacy Virtual Register for legacy I2C device. [More...](#ab4fbe6aac8d5860ef90613e51b15ef83) |
| }; |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bcr](#a7c234182e16da66c308e86d72591063d) |
|  | Bus Characteristic Register of a target device or a group. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [static\_addr](#a7374dd59c060462af7ca366ae7165107) |
|  | Static Address of a target device or a group. |

## Detailed Description

The target device part of payload for DEFTGTS CCC.

This is used by DEFTGTS (Define List of Targets) CCC to describe the existing target devices on the I3C bus.

## Field Documentation

## [◆ ](#af6813c89b8779b8eff2c67434515caae)[union]

| union { ... } [i3c\_ccc\_deftgts\_target](structi3c__ccc__deftgts__target.md) |
| --- |

## [◆ ](#a34a02df3d4dc456733746437b2cd983a)addr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_ccc\_deftgts\_target::addr |
| --- |

Dynamic Address of a target device, or a group address.

## [◆ ](#a7c234182e16da66c308e86d72591063d)bcr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_ccc\_deftgts\_target::bcr |
| --- |

Bus Characteristic Register of a target device or a group.

## [◆ ](#a08689c18d74fa4b74fc2ada055394e65)dcr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_ccc\_deftgts\_target::dcr |
| --- |

Device Characteristic Register of a I3C target device or a group.

## [◆ ](#ab4fbe6aac8d5860ef90613e51b15ef83)lvr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_ccc\_deftgts\_target::lvr |
| --- |

Legacy Virtual Register for legacy I2C device.

## [◆ ](#a7374dd59c060462af7ca366ae7165107)static\_addr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_ccc\_deftgts\_target::static\_addr |
| --- |

Static Address of a target device or a group.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/i3c/[ccc.h](ccc_8h_source.md)

- [i3c\_ccc\_deftgts\_target](structi3c__ccc__deftgts__target.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
