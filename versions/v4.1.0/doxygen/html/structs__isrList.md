---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structs__isrList.html
original_path: doxygen/html/structs__isrList.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

s\_isrList Struct Reference

`#include <[arch.h](x86_2ia32_2arch_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void \* | [fnc](#a62299be9af7bf7d395c5ad34fdcc4f03) |
|  | Address of ISR/stub. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [irq](#a885d8d1a26e11d2b6fb6b951da96550c) |
|  | IRQ associated with the ISR/stub, or -1 if this is not associated with a real interrupt; in this case vec must not be -1. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [priority](#af8bdba11e6c31f4920b18c117bb93bf9) |
|  | Priority associated with the IRQ. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [vec](#af1bc7016fb72489f391db03a9fdf0fd3) |
|  | Vector number associated with ISR/stub, or -1 to assign based on priority. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [dpl](#a6e70d162cb57609281f497ea5eb0321e) |
|  | Privilege level associated with ISR/stub. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [tss](#a2278f1081695c526ba30fa5f9f8aaecd) |
|  | If nonzero, specifies a TSS segment selector. |

## Field Documentation

## [◆ ](#a6e70d162cb57609281f497ea5eb0321e)dpl

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int s\_isrList::dpl |
| --- |

Privilege level associated with ISR/stub.

## [◆ ](#a62299be9af7bf7d395c5ad34fdcc4f03)fnc

| void\* s\_isrList::fnc |
| --- |

Address of ISR/stub.

## [◆ ](#a885d8d1a26e11d2b6fb6b951da96550c)irq

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int s\_isrList::irq |
| --- |

IRQ associated with the ISR/stub, or -1 if this is not associated with a real interrupt; in this case vec must not be -1.

## [◆ ](#af8bdba11e6c31f4920b18c117bb93bf9)priority

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int s\_isrList::priority |
| --- |

Priority associated with the IRQ.

Ignored if vec is not -1

## [◆ ](#a2278f1081695c526ba30fa5f9f8aaecd)tss

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int s\_isrList::tss |
| --- |

If nonzero, specifies a TSS segment selector.

Will configure a task gate instead of an interrupt gate. fnc parameter will be ignored

## [◆ ](#af1bc7016fb72489f391db03a9fdf0fd3)vec

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int s\_isrList::vec |
| --- |

Vector number associated with ISR/stub, or -1 to assign based on priority.

---

The documentation for this struct was generated from the following file:

- zephyr/arch/x86/ia32/[arch.h](x86_2ia32_2arch_8h_source.md)

- [s\_isrList](structs__isrList.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
