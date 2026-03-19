---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/gicv3__its_8h.html
original_path: doxygen/html/gicv3__its_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gicv3\_its.h File Reference

Driver for ARM Generic Interrupt Controller V3 Interrupt Translation Service.
[More...](#details)

[Go to the source code of this file.](gicv3__its_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [its\_driver\_api](structits__driver__api.md) |

| Typedefs | |
| --- | --- |
| typedef [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int(\* | [its\_api\_alloc\_intid\_t](#a49dff2553cbd48edc7057157d2ecb45d)) (const struct [device](structdevice.md) \*dev) |
| typedef int(\* | [its\_api\_setup\_deviceid\_t](#a39f4a213de953b77615b270f3ff13832)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) device\_id, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int nites) |
| typedef int(\* | [its\_api\_map\_intid\_t](#a2642c1f7ecf45d404c17cdbcd824bb45)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) device\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event\_id, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int intid) |
| typedef int(\* | [its\_api\_send\_int\_t](#a26bf8d071e3cb856fc81d8911e942f5a)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) device\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event\_id) |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* | [its\_api\_get\_msi\_addr\_t](#add616700e3aeee952187ef96cb2d19c9)) (const struct [device](structdevice.md) \*dev) |

| Functions | |
| --- | --- |
| static int | [its\_alloc\_intid](#a5c50167a84a3b7d8e3cf01d226deb3d3) (const struct [device](structdevice.md) \*dev) |
| static int | [its\_setup\_deviceid](#a05032faf2fdcde27760871345756d3e5) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) device\_id, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int nites) |
| static int | [its\_map\_intid](#ac4899e33d0636465265a3072aa5510cc) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) device\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event\_id, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int intid) |
| static int | [its\_send\_int](#a6139a7f275a6016ecadcb0ee2dfcc327) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) device\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event\_id) |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [its\_get\_msi\_addr](#afcd0b4735367a10465e81b46d333b06b) (const struct [device](structdevice.md) \*dev) |

## Detailed Description

Driver for ARM Generic Interrupt Controller V3 Interrupt Translation Service.

The Generic Interrupt Controller (GIC) Interrupt Translation Service translates an input EventID from a device, identified by its DeviceID, determines a corresponding INTID for this input and the target Redistributor and, through this, the target PE for that INTID.

## Typedef Documentation

## [◆ ](#a49dff2553cbd48edc7057157d2ecb45d)its\_api\_alloc\_intid\_t

| typedef [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int(\* its\_api\_alloc\_intid\_t) (const struct [device](structdevice.md) \*dev) |
| --- |

## [◆ ](#add616700e3aeee952187ef96cb2d19c9)its\_api\_get\_msi\_addr\_t

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* its\_api\_get\_msi\_addr\_t) (const struct [device](structdevice.md) \*dev) |
| --- |

## [◆ ](#a2642c1f7ecf45d404c17cdbcd824bb45)its\_api\_map\_intid\_t

| typedef int(\* its\_api\_map\_intid\_t) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) device\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event\_id, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int intid) |
| --- |

## [◆ ](#a26bf8d071e3cb856fc81d8911e942f5a)its\_api\_send\_int\_t

| typedef int(\* its\_api\_send\_int\_t) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) device\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event\_id) |
| --- |

## [◆ ](#a39f4a213de953b77615b270f3ff13832)its\_api\_setup\_deviceid\_t

| typedef int(\* its\_api\_setup\_deviceid\_t) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) device\_id, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int nites) |
| --- |

## Function Documentation

## [◆ ](#a5c50167a84a3b7d8e3cf01d226deb3d3)its\_alloc\_intid()

| | int its\_alloc\_intid | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#afcd0b4735367a10465e81b46d333b06b)its\_get\_msi\_addr()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) its\_get\_msi\_addr | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ac4899e33d0636465265a3072aa5510cc)its\_map\_intid()

| | int its\_map\_intid | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *device\_id*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *event\_id*, | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *intid* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a6139a7f275a6016ecadcb0ee2dfcc327)its\_send\_int()

| | int its\_send\_int | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *device\_id*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *event\_id* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a05032faf2fdcde27760871345756d3e5)its\_setup\_deviceid()

| | int its\_setup\_deviceid | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *device\_id*, | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *nites* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [gicv3\_its.h](gicv3__its_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
