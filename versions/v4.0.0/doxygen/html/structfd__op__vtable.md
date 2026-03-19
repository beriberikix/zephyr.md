---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structfd__op__vtable.html
original_path: doxygen/html/structfd__op__vtable.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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
| union { |  |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\*   [read](#a8caad0c1e96cdb67ef02f918ab8aff17) )(void \*obj, void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) sz) |  |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\*   [read\_offs](#a6748a61747f3ffd0c16174e5ad6d9829) )(void \*obj, void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9)         sz, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset) |  |
| }; |  |
| union { |  |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\*   [write](#ac59ee326ff54a6a2324bf3425f4a3d5a) )(void \*obj, const void \*buf,         [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) sz) |  |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\*   [write\_offs](#a48338a129571b7c76abc4a1b5a6372af) )(void \*obj, const void \*buf,         [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) sz, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset) |  |
| }; |  |
| union { |  |
| int(\*   [close](#a80704417dfe01e8289d1f7fca819f5f1) )(void \*obj) |  |
| int(\*   [close2](#a139c24a21d141ccfdc7b00cf821f9a5e) )(void \*obj, int fd) |  |
| }; |  |
| int(\* | [ioctl](#aff079f05422413a0df3394ddfecc0298) )(void \*obj, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int request, va\_list args) |

## Detailed Description

File descriptor virtual method table.

Currently all operations beyond read/write/close go thru ioctl method.

## Field Documentation

## [◆ ](#a2cc13673e6545c6a0c65658e94a24290)[union]

| union { ... } [fd\_op\_vtable](structfd__op__vtable.md) |
| --- |

## [◆ ](#a857669958f9ff29d4f29aca68ff53943)[union]

| union { ... } [fd\_op\_vtable](structfd__op__vtable.md) |
| --- |

## [◆ ](#a5bab4b02306d78ec1943219d2478ca51)[union]

| union { ... } [fd\_op\_vtable](structfd__op__vtable.md) |
| --- |

## [◆ ](#a80704417dfe01e8289d1f7fca819f5f1)close

| int(\* fd\_op\_vtable::close) (void \*obj) |
| --- |

## [◆ ](#a139c24a21d141ccfdc7b00cf821f9a5e)close2

| int(\* fd\_op\_vtable::close2) (void \*obj, int fd) |
| --- |

## [◆ ](#aff079f05422413a0df3394ddfecc0298)ioctl

| int(\* fd\_op\_vtable::ioctl) (void \*obj, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int request, va\_list args) |
| --- |

## [◆ ](#a8caad0c1e96cdb67ef02f918ab8aff17)read

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\* fd\_op\_vtable::read) (void \*obj, void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) sz) |
| --- |

## [◆ ](#a6748a61747f3ffd0c16174e5ad6d9829)read\_offs

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\* fd\_op\_vtable::read\_offs) (void \*obj, void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) sz, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset) |
| --- |

## [◆ ](#ac59ee326ff54a6a2324bf3425f4a3d5a)write

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\* fd\_op\_vtable::write) (void \*obj, const void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) sz) |
| --- |

## [◆ ](#a48338a129571b7c76abc4a1b5a6372af)write\_offs

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\* fd\_op\_vtable::write\_offs) (void \*obj, const void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) sz, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset) |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/sys/[fdtable.h](fdtable_8h_source.md)

- [fd\_op\_vtable](structfd__op__vtable.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
