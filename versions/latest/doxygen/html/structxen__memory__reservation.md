---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structxen__memory__reservation.html
original_path: doxygen/html/structxen__memory__reservation.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

xen\_memory\_reservation Struct Reference

`#include <[memory.h](public_2memory_8h_source.md)>`

| Public Member Functions | |
| --- | --- |
|  | [XEN\_GUEST\_HANDLE](#a94ed3926aa2d7f7c759fe9cbd59b042a) ([xen\_pfn\_t](arch-arm_8h.md#a564b8052e6905461f66db791246d2226)) extent\_start |

| Data Fields | |
| --- | --- |
| [xen\_ulong\_t](arch-arm_8h.md#a9dd3dbb4741d391e0fff3f0e7d55cccc) | [nr\_extents](#a0ab0fec872492d02f73d5dde37ef93bb) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [extent\_order](#ad0acf08be6cf896b508744cc6398b6b6) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [address\_bits](#a18732ad7ad5cde2ab44cef84af689ee2) |
| [domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee) | [domid](#a20ea11d84f179b236346ec129e94f6d0) |

## Member Function Documentation

## [◆ ](#a94ed3926aa2d7f7c759fe9cbd59b042a)XEN\_GUEST\_HANDLE()

| xen\_memory\_reservation::XEN\_GUEST\_HANDLE | ( | [xen\_pfn\_t](arch-arm_8h.md#a564b8052e6905461f66db791246d2226) |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## Field Documentation

## [◆ ](#a18732ad7ad5cde2ab44cef84af689ee2)address\_bits

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int xen\_memory\_reservation::address\_bits |
| --- |

## [◆ ](#a20ea11d84f179b236346ec129e94f6d0)domid

| [domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee) xen\_memory\_reservation::domid |
| --- |

## [◆ ](#ad0acf08be6cf896b508744cc6398b6b6)extent\_order

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int xen\_memory\_reservation::extent\_order |
| --- |

## [◆ ](#a0ab0fec872492d02f73d5dde37ef93bb)nr\_extents

| [xen\_ulong\_t](arch-arm_8h.md#a9dd3dbb4741d391e0fff3f0e7d55cccc) xen\_memory\_reservation::nr\_extents |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/xen/public/[memory.h](public_2memory_8h_source.md)

- [xen\_memory\_reservation](structxen__memory__reservation.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
