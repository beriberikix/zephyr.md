---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structi3c__config__target.html
original_path: doxygen/html/structi3c__config__target.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i3c\_config\_target Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [I3C Interface](group__i3c__interface.md) » [I3C Target Device API](group__i3c__target__device.md)

Configuration parameters for I3C hardware to act as target device.
[More...](#details)

`#include <[target_device.h](target__device_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [enable](#abbfb2e5c4d061b60f3e0f92ee17f4ee7) |
|  | If the hardware is to act as a target device on the bus. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [static\_addr](#ab5345d23ba2afffbf48010e7edff3c26) |
|  | I3C target address. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [pid](#a62e1b1a3dff6cc570ecccdfcfc6b196d) |
|  | Provisioned ID. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pid\_random](#a2ad289658811d142ba9091574acf485b) |
|  | True if lower 32-bit of Provisioned ID is random. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bcr](#a1d0b97d6428e471bcf9b6945da947b36) |
|  | Bus Characteristics Register (BCR). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [dcr](#afaa68c94b35f512a597b35752db8d66e) |
|  | Device Characteristics Register (DCR). |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [max\_read\_len](#a4339c8dd33b17ce8363bf28177411830) |
|  | Maximum Read Length (MRL). |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [max\_write\_len](#aca4dc4aa873ca447d06e573d485ab854) |
|  | Maximum Write Length (MWL). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [supported\_hdr](#a78a74f81e632a428db59803b55239419) |
|  | Bit mask of supported HDR modes (0 - 7). |

## Detailed Description

Configuration parameters for I3C hardware to act as target device.

This can also be used to configure the controller if it is to act as a secondary controller on the bus.

## Field Documentation

## [◆ ](#a1d0b97d6428e471bcf9b6945da947b36)bcr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_config\_target::bcr |
| --- |

Bus Characteristics Register (BCR).

## [◆ ](#afaa68c94b35f512a597b35752db8d66e)dcr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_config\_target::dcr |
| --- |

Device Characteristics Register (DCR).

## [◆ ](#abbfb2e5c4d061b60f3e0f92ee17f4ee7)enable

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) i3c\_config\_target::enable |
| --- |

If the hardware is to act as a target device on the bus.

## [◆ ](#a4339c8dd33b17ce8363bf28177411830)max\_read\_len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) i3c\_config\_target::max\_read\_len |
| --- |

Maximum Read Length (MRL).

## [◆ ](#aca4dc4aa873ca447d06e573d485ab854)max\_write\_len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) i3c\_config\_target::max\_write\_len |
| --- |

Maximum Write Length (MWL).

## [◆ ](#a62e1b1a3dff6cc570ecccdfcfc6b196d)pid

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) i3c\_config\_target::pid |
| --- |

Provisioned ID.

## [◆ ](#a2ad289658811d142ba9091574acf485b)pid\_random

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) i3c\_config\_target::pid\_random |
| --- |

True if lower 32-bit of Provisioned ID is random.

This sets the bit 32 of Provisioned ID which means the lower 32-bit is random value.

## [◆ ](#ab5345d23ba2afffbf48010e7edff3c26)static\_addr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_config\_target::static\_addr |
| --- |

I3C target address.

Used used when operates as secondary controller or as a target device.

## [◆ ](#a78a74f81e632a428db59803b55239419)supported\_hdr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_config\_target::supported\_hdr |
| --- |

Bit mask of supported HDR modes (0 - 7).

This can be used to enable or disable HDR mode supported by the hardware at runtime.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/i3c/[target\_device.h](target__device_8h_source.md)

- [i3c\_config\_target](structi3c__config__target.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
