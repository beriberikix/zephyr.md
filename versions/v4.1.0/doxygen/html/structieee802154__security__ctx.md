---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structieee802154__security__ctx.html
original_path: doxygen/html/structieee802154__security__ctx.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ieee802154\_security\_ctx Struct Reference

[Connectivity](group__connectivity.md) » [IEEE 802.15.4 and Thread APIs](group__ieee802154.md) » [IEEE 802.15.4 L2](group__ieee802154__l2.md)

Interface-level security attributes, see section 9.5.
[More...](#details)

`#include <[ieee802154.h](ieee802154_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [frame\_counter](#adc4ce1ddf15b8b0bc4f283747b858b02) |
|  | Interface-level outgoing frame counter, section 9.5, table 9-8, secFrameCounter. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [key](#a3478b9a5430e12ca2c5641e1417a43d4) [16] |
|  | Interface-level frame encryption security key material. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [key\_len](#a1665374abce017c4b60e5c2085b19d8f) |
|  | Length in bytes of the interface-level security key material. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [level](#a65d1ca01bf7ed917a008591c8be0ca19): 3 |
|  | Frame security level, possible values are defined in section 9.4.2.2, table 9-6. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [key\_mode](#afc41da04241f4fcc11e9d9f7728315d9): 2 |
|  | Frame security key mode. |

## Detailed Description

Interface-level security attributes, see section 9.5.

## Field Documentation

## [◆ ](#adc4ce1ddf15b8b0bc4f283747b858b02)frame\_counter

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ieee802154\_security\_ctx::frame\_counter |
| --- |

Interface-level outgoing frame counter, section 9.5, table 9-8, secFrameCounter.

Only used when the driver does not implement key-specific frame counters.

## [◆ ](#a3478b9a5430e12ca2c5641e1417a43d4)key

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ieee802154\_security\_ctx::key[16] |
| --- |

Interface-level frame encryption security key material.

Currently native L2 only supports a single secKeySource, see section 9.5, table 9-9, in combination with secKeyMode zero (implicit key mode), see section 9.4.2.3, table 9-7.

Warning
:   This is no longer in accordance with the 2015+ versions of the standard and needs to be extended in the future for full security procedure compliance.

## [◆ ](#a1665374abce017c4b60e5c2085b19d8f)key\_len

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ieee802154\_security\_ctx::key\_len |
| --- |

Length in bytes of the interface-level security key material.

## [◆ ](#afc41da04241f4fcc11e9d9f7728315d9)key\_mode

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ieee802154\_security\_ctx::key\_mode |
| --- |

Frame security key mode.

Currently only implicit key mode is partially supported, see section 9.4.2.3, table 9-7, secKeyMode.

Warning
:   This is no longer in accordance with the 2015+ versions of the standard and needs to be extended in the future for full security procedure compliance.

## [◆ ](#a65d1ca01bf7ed917a008591c8be0ca19)level

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ieee802154\_security\_ctx::level |
| --- |

Frame security level, possible values are defined in section 9.4.2.2, table 9-6.

Warning
:   Currently native L2 allows to configure one common security level for all frame types, commands and information elements. This is no longer in accordance with the 2015+ versions of the standard and needs to be extended in the future for full security procedure compliance.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[ieee802154.h](ieee802154_8h_source.md)

- [ieee802154\_security\_ctx](structieee802154__security__ctx.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
