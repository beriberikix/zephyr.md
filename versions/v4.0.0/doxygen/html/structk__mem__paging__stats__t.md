---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structk__mem__paging__stats__t.html
original_path: doxygen/html/structk__mem__paging__stats__t.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

k\_mem\_paging\_stats\_t Struct Reference

[Kernel APIs](group__kernel__apis.md) » [Kernel Memory Management](group__kernel__memory__management.md) » [Demand Paging](group__demand__paging.md) » [Demand Paging APIs](group__mem-demand-paging.md)

Paging Statistics.
[More...](#details)

`#include <[demand_paging.h](demand__paging_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct { |  |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long   [cnt](#a3daad63e37d200f44d88c3d4e49f361a) |  |
|  | Number of page faults. [More...](#a3daad63e37d200f44d88c3d4e49f361a) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long   [irq\_locked](#aa762731df50fc81d08beb3628f9dbd71) |  |
|  | Number of page faults with IRQ locked. [More...](#aa762731df50fc81d08beb3628f9dbd71) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long   [irq\_unlocked](#a2c2183c1679ae158bdd232fa1fdeb250) |  |
|  | Number of page faults with IRQ unlocked. [More...](#a2c2183c1679ae158bdd232fa1fdeb250) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long   [in\_isr](#a210c83357c14a06fbd69b0cf2263fbb6) |  |
|  | Number of page faults while in ISR. [More...](#a210c83357c14a06fbd69b0cf2263fbb6) |
| } | [pagefaults](#af6331dae30074d48396151b33ac7a0a7) |
| struct { |  |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long   [clean](#a7b421897b3125d1a44284ca964ef1f66) |  |
|  | Number of clean pages selected for eviction. [More...](#a7b421897b3125d1a44284ca964ef1f66) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long   [dirty](#a4f8523c0e78c8de1e2443a194e875609) |  |
|  | Number of dirty pages selected for eviction. [More...](#a4f8523c0e78c8de1e2443a194e875609) |
| } | [eviction](#aa8175953fd7fa0a5057069b73b930f3b) |

## Detailed Description

Paging Statistics.

## Field Documentation

## [◆ ](#a7b421897b3125d1a44284ca964ef1f66)clean

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long k\_mem\_paging\_stats\_t::clean |
| --- |

Number of clean pages selected for eviction.

## [◆ ](#a3daad63e37d200f44d88c3d4e49f361a)cnt

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long k\_mem\_paging\_stats\_t::cnt |
| --- |

Number of page faults.

## [◆ ](#a4f8523c0e78c8de1e2443a194e875609)dirty

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long k\_mem\_paging\_stats\_t::dirty |
| --- |

Number of dirty pages selected for eviction.

## [◆ ](#aa8175953fd7fa0a5057069b73b930f3b)[struct]

| struct { ... } k\_mem\_paging\_stats\_t::eviction |
| --- |

## [◆ ](#a210c83357c14a06fbd69b0cf2263fbb6)in\_isr

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long k\_mem\_paging\_stats\_t::in\_isr |
| --- |

Number of page faults while in ISR.

## [◆ ](#aa762731df50fc81d08beb3628f9dbd71)irq\_locked

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long k\_mem\_paging\_stats\_t::irq\_locked |
| --- |

Number of page faults with IRQ locked.

## [◆ ](#a2c2183c1679ae158bdd232fa1fdeb250)irq\_unlocked

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long k\_mem\_paging\_stats\_t::irq\_unlocked |
| --- |

Number of page faults with IRQ unlocked.

## [◆ ](#af6331dae30074d48396151b33ac7a0a7)[struct]

| struct { ... } k\_mem\_paging\_stats\_t::pagefaults |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/kernel/mm/[demand\_paging.h](demand__paging_8h_source.md)

- [k\_mem\_paging\_stats\_t](structk__mem__paging__stats__t.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
