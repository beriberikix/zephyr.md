---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/riscv__plic_8h.html
original_path: doxygen/html/riscv__plic_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

riscv\_plic.h File Reference

Driver for Platform Level Interrupt Controller (PLIC).
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`

[Go to the source code of this file.](riscv__plic_8h_source.md)

| Functions | |
| --- | --- |
| void | [riscv\_plic\_irq\_enable](#aa2f97f63d37ae4fc381d79bdf78a274d) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq) |
|  | Enable interrupt. |
| void | [riscv\_plic\_irq\_disable](#a69dafac67e153be3be5f209050bd27ad) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq) |
|  | Disable interrupt. |
| int | [riscv\_plic\_irq\_is\_enabled](#aa6aaaff9f5af0f4acbbea187f13a5e6b) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq) |
|  | Check if an interrupt is enabled. |
| void | [riscv\_plic\_set\_priority](#aa73cba0daaafa6dc0d1b54abbbc5172a) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) prio) |
|  | Set interrupt priority. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [riscv\_plic\_get\_irq](#a1208afc18002e5c1d2539958a0331647) (void) |
|  | Get active interrupt ID. |
| const struct [device](structdevice.md) \* | [riscv\_plic\_get\_dev](#a94ba6fdef8d90dae8b184f902519d248) (void) |
|  | Get active interrupt controller device. |

## Detailed Description

Driver for Platform Level Interrupt Controller (PLIC).

## Function Documentation

## [◆ ](#a94ba6fdef8d90dae8b184f902519d248)riscv\_plic\_get\_dev()

| const struct [device](structdevice.md) \* riscv\_plic\_get\_dev | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Get active interrupt controller device.

Returns
:   Returns device pointer of the active interrupt device

## [◆ ](#a1208afc18002e5c1d2539958a0331647)riscv\_plic\_get\_irq()

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int riscv\_plic\_get\_irq | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Get active interrupt ID.

Returns
:   Returns the ID of an active interrupt

## [◆ ](#a69dafac67e153be3be5f209050bd27ad)riscv\_plic\_irq\_disable()

| void riscv\_plic\_irq\_disable | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *irq* | ) |  |
| --- | --- | --- | --- | --- | --- |

Disable interrupt.

Parameters
:   | irq | Multi-level encoded interrupt ID |
    | --- | --- |

## [◆ ](#aa2f97f63d37ae4fc381d79bdf78a274d)riscv\_plic\_irq\_enable()

| void riscv\_plic\_irq\_enable | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *irq* | ) |  |
| --- | --- | --- | --- | --- | --- |

Enable interrupt.

Parameters
:   | irq | Multi-level encoded interrupt ID |
    | --- | --- |

## [◆ ](#aa6aaaff9f5af0f4acbbea187f13a5e6b)riscv\_plic\_irq\_is\_enabled()

| int riscv\_plic\_irq\_is\_enabled | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *irq* | ) |  |
| --- | --- | --- | --- | --- | --- |

Check if an interrupt is enabled.

Parameters
:   | irq | Multi-level encoded interrupt ID |
    | --- | --- |

Returns
:   Returns true if interrupt is enabled, false otherwise

## [◆ ](#aa73cba0daaafa6dc0d1b54abbbc5172a)riscv\_plic\_set\_priority()

| void riscv\_plic\_set\_priority | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *irq*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *prio* ) |

Set interrupt priority.

Parameters
:   | irq | Multi-level encoded interrupt ID |
    | --- | --- |
    | prio | interrupt priority |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [riscv\_plic.h](riscv__plic_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
