---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/riscv__clic_8h_source.html
original_path: doxygen/html/riscv__clic_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

riscv\_clic.h

[Go to the documentation of this file.](riscv__clic_8h.md)

1/\*

2 \* Copyright (c) 2022 Carlo Caione <ccaione@baylibre.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_RISCV\_CLIC\_H\_

13#define ZEPHYR\_INCLUDE\_DRIVERS\_RISCV\_CLIC\_H\_

14

[ 20](riscv__clic_8h.md#a97a6fb5c16f1542d7c3010212a5efa05)void [riscv\_clic\_irq\_enable](riscv__clic_8h.md#a97a6fb5c16f1542d7c3010212a5efa05)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq);

21

[ 27](riscv__clic_8h.md#ac46870266793fabffd76b29c06834b35)void [riscv\_clic\_irq\_disable](riscv__clic_8h.md#ac46870266793fabffd76b29c06834b35)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq);

28

[ 35](riscv__clic_8h.md#aabf4e38a154115fb4ee112b0c04af71f)int [riscv\_clic\_irq\_is\_enabled](riscv__clic_8h.md#aabf4e38a154115fb4ee112b0c04af71f)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq);

36

[ 44](riscv__clic_8h.md#a58034939d55cac9197e0494ef40f0276)void [riscv\_clic\_irq\_priority\_set](riscv__clic_8h.md#a58034939d55cac9197e0494ef40f0276)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) prio, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

45

[ 51](riscv__clic_8h.md#aefcfc1008aba2e0f98f24b26113b776e)void [riscv\_clic\_irq\_vector\_set](riscv__clic_8h.md#aefcfc1008aba2e0f98f24b26113b776e)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq);

52

53#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_RISCV\_CLIC\_H\_ \*/

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[riscv\_clic\_irq\_priority\_set](riscv__clic_8h.md#a58034939d55cac9197e0494ef40f0276)

void riscv\_clic\_irq\_priority\_set(uint32\_t irq, uint32\_t prio, uint32\_t flags)

Set interrupt priority.

[riscv\_clic\_irq\_enable](riscv__clic_8h.md#a97a6fb5c16f1542d7c3010212a5efa05)

void riscv\_clic\_irq\_enable(uint32\_t irq)

Enable interrupt.

[riscv\_clic\_irq\_is\_enabled](riscv__clic_8h.md#aabf4e38a154115fb4ee112b0c04af71f)

int riscv\_clic\_irq\_is\_enabled(uint32\_t irq)

Check if an interrupt is enabled.

[riscv\_clic\_irq\_disable](riscv__clic_8h.md#ac46870266793fabffd76b29c06834b35)

void riscv\_clic\_irq\_disable(uint32\_t irq)

Disable interrupt.

[riscv\_clic\_irq\_vector\_set](riscv__clic_8h.md#aefcfc1008aba2e0f98f24b26113b776e)

void riscv\_clic\_irq\_vector\_set(uint32\_t irq)

Set vector mode of interrupt.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [riscv\_clic.h](riscv__clic_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
