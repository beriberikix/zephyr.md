---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/dw__ace_8h.html
original_path: doxygen/html/dw__ace_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dw\_ace.h File Reference

`#include <[zephyr/device.h](device_8h_source.md)>`

[Go to the source code of this file.](dw__ace_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [dw\_ace\_v1\_ictl\_driver\_api](structdw__ace__v1__ictl__driver__api.md) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [irq\_enable\_t](#a99f66a0736502ea18deb13e0a5d9958e)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq) |
| typedef void(\* | [irq\_disable\_t](#a1e71aa00761ed1a478f92de8a1342564)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq) |
| typedef int(\* | [irq\_is\_enabled\_t](#af94ebd4f440b084d94d42eed62e159cc)) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
| typedef int(\* | [irq\_connect\_dynamic\_t](#a5b6d1259c32080069df86d5e4fd506cb)) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int priority, void(\*routine) (const void \*parameter), const void \*parameter, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |

## Typedef Documentation

## [◆ ](#a5b6d1259c32080069df86d5e4fd506cb)irq\_connect\_dynamic\_t

| typedef int(\* irq\_connect\_dynamic\_t) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int priority, void(\*routine)(const void \*parameter), const void \*parameter, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
| --- |

## [◆ ](#a1e71aa00761ed1a478f92de8a1342564)irq\_disable\_t

| typedef void(\* irq\_disable\_t) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq) |
| --- |

## [◆ ](#a99f66a0736502ea18deb13e0a5d9958e)irq\_enable\_t

| typedef void(\* irq\_enable\_t) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq) |
| --- |

## [◆ ](#af94ebd4f440b084d94d42eed62e159cc)irq\_is\_enabled\_t

| typedef int(\* irq\_is\_enabled\_t) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [dw\_ace.h](dw__ace_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
