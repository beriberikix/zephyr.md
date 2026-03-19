---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/riscv__clic_8h.html
original_path: doxygen/html/riscv__clic_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

riscv\_clic.h File Reference

Driver for Core-Local Interrupt Controller (CLIC).
[More...](#details)

[Go to the source code of this file.](riscv__clic_8h_source.md)

| Functions | |
| --- | --- |
| void | [riscv\_clic\_irq\_enable](#a97a6fb5c16f1542d7c3010212a5efa05) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq) |
|  | Enable interrupt. |
| void | [riscv\_clic\_irq\_disable](#ac46870266793fabffd76b29c06834b35) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq) |
|  | Disable interrupt. |
| int | [riscv\_clic\_irq\_is\_enabled](#aabf4e38a154115fb4ee112b0c04af71f) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq) |
|  | Check if an interrupt is enabled. |
| void | [riscv\_clic\_irq\_priority\_set](#a58034939d55cac9197e0494ef40f0276) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) prio, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Set interrupt priority. |
| void | [riscv\_clic\_irq\_vector\_set](#aefcfc1008aba2e0f98f24b26113b776e) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq) |
|  | Set vector mode of interrupt. |

## Detailed Description

Driver for Core-Local Interrupt Controller (CLIC).

## Function Documentation

## [◆ ](#ac46870266793fabffd76b29c06834b35)riscv\_clic\_irq\_disable()

| void riscv\_clic\_irq\_disable | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *irq* | ) |  |
| --- | --- | --- | --- | --- | --- |

Disable interrupt.

Parameters
:   | irq | interrupt ID |
    | --- | --- |

## [◆ ](#a97a6fb5c16f1542d7c3010212a5efa05)riscv\_clic\_irq\_enable()

| void riscv\_clic\_irq\_enable | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *irq* | ) |  |
| --- | --- | --- | --- | --- | --- |

Enable interrupt.

Parameters
:   | irq | interrupt ID |
    | --- | --- |

## [◆ ](#aabf4e38a154115fb4ee112b0c04af71f)riscv\_clic\_irq\_is\_enabled()

| int riscv\_clic\_irq\_is\_enabled | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *irq* | ) |  |
| --- | --- | --- | --- | --- | --- |

Check if an interrupt is enabled.

Parameters
:   | irq | interrupt ID |
    | --- | --- |

Returns
:   Returns true if interrupt is enabled, false otherwise

## [◆ ](#a58034939d55cac9197e0494ef40f0276)riscv\_clic\_irq\_priority\_set()

| void riscv\_clic\_irq\_priority\_set | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *irq*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *prio*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags* ) |

Set interrupt priority.

Parameters
:   | irq | interrupt ID |
    | --- | --- |
    | prio | interrupt priority |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | interrupt flags |

## [◆ ](#aefcfc1008aba2e0f98f24b26113b776e)riscv\_clic\_irq\_vector\_set()

| void riscv\_clic\_irq\_vector\_set | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *irq* | ) |  |
| --- | --- | --- | --- | --- | --- |

Set vector mode of interrupt.

Parameters
:   | irq | interrupt ID |
    | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [riscv\_clic.h](riscv__clic_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
