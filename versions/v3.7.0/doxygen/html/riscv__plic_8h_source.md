---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/riscv__plic_8h_source.html
original_path: doxygen/html/riscv__plic_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

riscv\_plic.h

[Go to the documentation of this file.](riscv__plic_8h.md)

1/\*

2 \* Copyright (c) 2022 Carlo Caione <ccaione@baylibre.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_RISCV\_PLIC\_H\_

13#define ZEPHYR\_INCLUDE\_DRIVERS\_RISCV\_PLIC\_H\_

14

15#include <[zephyr/device.h](device_8h.md)>

16

[ 22](riscv__plic_8h.md#aa2f97f63d37ae4fc381d79bdf78a274d)void [riscv\_plic\_irq\_enable](riscv__plic_8h.md#aa2f97f63d37ae4fc381d79bdf78a274d)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq);

23

[ 29](riscv__plic_8h.md#a69dafac67e153be3be5f209050bd27ad)void [riscv\_plic\_irq\_disable](riscv__plic_8h.md#a69dafac67e153be3be5f209050bd27ad)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq);

30

[ 37](riscv__plic_8h.md#aa6aaaff9f5af0f4acbbea187f13a5e6b)int [riscv\_plic\_irq\_is\_enabled](riscv__plic_8h.md#aa6aaaff9f5af0f4acbbea187f13a5e6b)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq);

38

[ 45](riscv__plic_8h.md#aa73cba0daaafa6dc0d1b54abbbc5172a)void [riscv\_plic\_set\_priority](riscv__plic_8h.md#aa73cba0daaafa6dc0d1b54abbbc5172a)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) prio);

46

[ 52](riscv__plic_8h.md#a1208afc18002e5c1d2539958a0331647)unsigned int [riscv\_plic\_get\_irq](riscv__plic_8h.md#a1208afc18002e5c1d2539958a0331647)(void);

53

[ 59](riscv__plic_8h.md#a94ba6fdef8d90dae8b184f902519d248)const struct [device](structdevice.md) \*[riscv\_plic\_get\_dev](riscv__plic_8h.md#a94ba6fdef8d90dae8b184f902519d248)(void);

60

61#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_RISCV\_PLIC\_H\_ \*/

[device.h](device_8h.md)

[riscv\_plic\_get\_irq](riscv__plic_8h.md#a1208afc18002e5c1d2539958a0331647)

unsigned int riscv\_plic\_get\_irq(void)

Get active interrupt ID.

[riscv\_plic\_irq\_disable](riscv__plic_8h.md#a69dafac67e153be3be5f209050bd27ad)

void riscv\_plic\_irq\_disable(uint32\_t irq)

Disable interrupt.

[riscv\_plic\_get\_dev](riscv__plic_8h.md#a94ba6fdef8d90dae8b184f902519d248)

const struct device \* riscv\_plic\_get\_dev(void)

Get active interrupt controller device.

[riscv\_plic\_irq\_enable](riscv__plic_8h.md#aa2f97f63d37ae4fc381d79bdf78a274d)

void riscv\_plic\_irq\_enable(uint32\_t irq)

Enable interrupt.

[riscv\_plic\_irq\_is\_enabled](riscv__plic_8h.md#aa6aaaff9f5af0f4acbbea187f13a5e6b)

int riscv\_plic\_irq\_is\_enabled(uint32\_t irq)

Check if an interrupt is enabled.

[riscv\_plic\_set\_priority](riscv__plic_8h.md#aa73cba0daaafa6dc0d1b54abbbc5172a)

void riscv\_plic\_set\_priority(uint32\_t irq, uint32\_t prio)

Set interrupt priority.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [riscv\_plic.h](riscv__plic_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
