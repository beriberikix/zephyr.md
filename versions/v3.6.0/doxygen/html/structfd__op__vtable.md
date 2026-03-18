---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structfd__op__vtable.html
original_path: doxygen/html/structfd__op__vtable.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fd\_op\_vtable Struct Reference

File descriptor virtual method table.
[More...](#details)

`#include <[fdtable.h](fdtable_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\* | [read](#a8caad0c1e96cdb67ef02f918ab8aff17) )(void \*obj, void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) sz) |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\* | [write](#ac59ee326ff54a6a2324bf3425f4a3d5a) )(void \*obj, const void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) sz) |
| int(\* | [close](#a80704417dfe01e8289d1f7fca819f5f1) )(void \*obj) |
| int(\* | [ioctl](#aff079f05422413a0df3394ddfecc0298) )(void \*obj, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int request, va\_list args) |

## Detailed Description

File descriptor virtual method table.

Currently all operations beyond read/write/close go thru ioctl method.

## Field Documentation

## [◆ ](#a80704417dfe01e8289d1f7fca819f5f1)close

| int(\* fd\_op\_vtable::close) (void \*obj) |
| --- |

## [◆ ](#aff079f05422413a0df3394ddfecc0298)ioctl

| int(\* fd\_op\_vtable::ioctl) (void \*obj, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int request, va\_list args) |
| --- |

## [◆ ](#a8caad0c1e96cdb67ef02f918ab8aff17)read

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\* fd\_op\_vtable::read) (void \*obj, void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) sz) |
| --- |

## [◆ ](#ac59ee326ff54a6a2324bf3425f4a3d5a)write

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\* fd\_op\_vtable::write) (void \*obj, const void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) sz) |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/sys/[fdtable.h](fdtable_8h_source.md)

- [fd\_op\_vtable](structfd__op__vtable.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
