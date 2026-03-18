---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structgdb__interrupt__ctx.html
original_path: doxygen/html/structgdb__interrupt__ctx.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gdb\_interrupt\_ctx Struct Reference

GDB interruption context.
[More...](#details)

`#include <[gdbstub.h](arch_2x86_2ia32_2gdbstub_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ss](#aa9270fa78d2485bc74090ac125686001) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [gs](#ac030129b89c096a3a63d500f7bad3694) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [fs](#aa848335652cd22a13d23417eceaba37c) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [es](#a23a3d136237cf2db7a49a538e9cbb5c1) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ds](#afe9a8264a1ba4402f1d6ceed42c2fe35) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [edi](#a9bdc030dfe999ce4d2c5dacf999a8152) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [esi](#aa174bfc58d6f4bd0aa10e48139aae073) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ebp](#ac7ae28c665e573abbfcdafe07e5da473) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [esp](#a8284780b26c1ba6fd3117fc1f5a1ea1f) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ebx](#a61abfb0bf1858ae4cba3d72bd5f8d95d) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [edx](#a483bef7f8235e91ba450073dcdf9d6bb) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [ecx](#ae23b76372e6aa71488427327240d078a) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [eax](#ad60975255b667db74255d1a8534b759a) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [vector](#af3d805bf15d0c6bac1382e2cfe58bef4) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [error\_code](#a106553cd8345cd8179aa3e5b6d9a10b8) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [eip](#a4c77f1335eb4dfe2d54f2e3d2526af92) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [cs](#ad09b829083a190226461accdfc7bf17d) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [eflags](#a248f18679b999bc4cf5438d729725a1e) |

## Detailed Description

GDB interruption context.

The exception stack frame contents used by gdbstub. The contents of this struct are used to display information about the current cpu state.

## Field Documentation

## [◆ ](#ad09b829083a190226461accdfc7bf17d)cs

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) gdb\_interrupt\_ctx::cs |
| --- |

## [◆ ](#afe9a8264a1ba4402f1d6ceed42c2fe35)ds

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) gdb\_interrupt\_ctx::ds |
| --- |

## [◆ ](#ad60975255b667db74255d1a8534b759a)eax

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) gdb\_interrupt\_ctx::eax |
| --- |

## [◆ ](#ac7ae28c665e573abbfcdafe07e5da473)ebp

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) gdb\_interrupt\_ctx::ebp |
| --- |

## [◆ ](#a61abfb0bf1858ae4cba3d72bd5f8d95d)ebx

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) gdb\_interrupt\_ctx::ebx |
| --- |

## [◆ ](#ae23b76372e6aa71488427327240d078a)ecx

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) gdb\_interrupt\_ctx::ecx |
| --- |

## [◆ ](#a9bdc030dfe999ce4d2c5dacf999a8152)edi

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) gdb\_interrupt\_ctx::edi |
| --- |

## [◆ ](#a483bef7f8235e91ba450073dcdf9d6bb)edx

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) gdb\_interrupt\_ctx::edx |
| --- |

## [◆ ](#a248f18679b999bc4cf5438d729725a1e)eflags

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) gdb\_interrupt\_ctx::eflags |
| --- |

## [◆ ](#a4c77f1335eb4dfe2d54f2e3d2526af92)eip

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) gdb\_interrupt\_ctx::eip |
| --- |

## [◆ ](#a106553cd8345cd8179aa3e5b6d9a10b8)error\_code

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) gdb\_interrupt\_ctx::error\_code |
| --- |

## [◆ ](#a23a3d136237cf2db7a49a538e9cbb5c1)es

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) gdb\_interrupt\_ctx::es |
| --- |

## [◆ ](#aa174bfc58d6f4bd0aa10e48139aae073)esi

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) gdb\_interrupt\_ctx::esi |
| --- |

## [◆ ](#a8284780b26c1ba6fd3117fc1f5a1ea1f)esp

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) gdb\_interrupt\_ctx::esp |
| --- |

## [◆ ](#aa848335652cd22a13d23417eceaba37c)fs

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) gdb\_interrupt\_ctx::fs |
| --- |

## [◆ ](#ac030129b89c096a3a63d500f7bad3694)gs

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) gdb\_interrupt\_ctx::gs |
| --- |

## [◆ ](#aa9270fa78d2485bc74090ac125686001)ss

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) gdb\_interrupt\_ctx::ss |
| --- |

## [◆ ](#af3d805bf15d0c6bac1382e2cfe58bef4)vector

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) gdb\_interrupt\_ctx::vector |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/arch/x86/ia32/[gdbstub.h](arch_2x86_2ia32_2gdbstub_8h_source.md)

- [gdb\_interrupt\_ctx](structgdb__interrupt__ctx.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
