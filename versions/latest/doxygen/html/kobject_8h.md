---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/kobject_8h.html
original_path: doxygen/html/kobject_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

kobject.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`  
`#include <[zephyr/sys/internal/kobject_internal.h](kobject__internal_8h_source.md)>`  
`#include <zephyr/syscalls/kobject.h>`

[Go to the source code of this file.](kobject_8h_source.md)

| Macros | |
| --- | --- |
| #define | [K\_THREAD\_ACCESS\_GRANT](group__usermode__apis.md#ga6a2dae4c6dc6959d8785ff1924b1b424)(name\_, ...) |
|  | Grant a static thread access to a list of kernel objects. |
| #define | [K\_OBJ\_FLAG\_INITIALIZED](group__usermode__apis.md#ga1418482d67c7964855570fd0ac79628d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Object initialized. |
| #define | [K\_OBJ\_FLAG\_PUBLIC](group__usermode__apis.md#ga8892f9343266ec24abf25e29f3f6bc9b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Object is Public. |
| #define | [K\_OBJ\_FLAG\_ALLOC](group__usermode__apis.md#ga1bf7c8c1d5fe0a7358dd70c4663a5a7a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Object allocated. |
| #define | [K\_OBJ\_FLAG\_DRIVER](group__usermode__apis.md#ga82d3a7242074db70130415201d3d0fd6)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Driver Object. |

| Enumerations | |
| --- | --- |
| enum | [k\_objects](#af3a248c0e3b05c84b1dd38642f7cf2a1) { [K\_OBJ\_ANY](#af3a248c0e3b05c84b1dd38642f7cf2a1a51b9ec845f71832ad8fbb35d0cb3e5f6) , [K\_OBJ\_LAST](#af3a248c0e3b05c84b1dd38642f7cf2a1a7aecd777175f519ce8240e337e1cf430) } |
|  | Kernel Object Types. [More...](#af3a248c0e3b05c84b1dd38642f7cf2a1) |

| Functions | |
| --- | --- |
| void | [k\_object\_access\_grant](group__usermode__apis.md#ga94087bedf96fe2a2bea437d3d585ca22) (const void \*object, struct [k\_thread](structk__thread.md) \*thread) |
|  | Grant a thread access to a kernel object. |
| void | [k\_object\_access\_revoke](group__usermode__apis.md#gab70fe65497da1347cc4b7bf7ca2daf22) (const void \*object, struct [k\_thread](structk__thread.md) \*thread) |
|  | Revoke a thread's access to a kernel object. |
| void | [k\_object\_release](group__usermode__apis.md#ga3cb1a024c0178918def2dd0186e565b3) (const void \*object) |
|  | Release an object. |
| void | [k\_object\_access\_all\_grant](group__usermode__apis.md#gababc731e98a6378323c0d633b2abaa6a) (const void \*object) |
|  | Grant all present and future threads access to an object. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [k\_object\_is\_valid](group__usermode__apis.md#gaacd9b4b517db99b3b027dd717e6746b4) (const void \*obj, enum [k\_objects](#af3a248c0e3b05c84b1dd38642f7cf2a1) otype) |
|  | Check if a kernel object is of certain type and is valid. |
| void \* | [k\_object\_alloc](group__usermode__apis.md#ga5bba3a354fbc63673c76c9815db40812) (enum [k\_objects](#af3a248c0e3b05c84b1dd38642f7cf2a1) otype) |
|  | Allocate a kernel object of a designated type. |
| void \* | [k\_object\_alloc\_size](group__usermode__apis.md#gab99a640325f14a6505a85218dcba5446) (enum [k\_objects](#af3a248c0e3b05c84b1dd38642f7cf2a1) otype, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Allocate a kernel object of a designated type and a given size. |
| void | [k\_object\_free](group__usermode__apis.md#ga9cc15e8fd7df9cb81c3d7b6c79917aab) (void \*obj) |
|  | Free a kernel object previously allocated with [k\_object\_alloc()](group__usermode__apis.md#ga5bba3a354fbc63673c76c9815db40812 "Allocate a kernel object of a designated type."). |

## Enumeration Type Documentation

## [◆ ](#af3a248c0e3b05c84b1dd38642f7cf2a1)k\_objects

| enum [k\_objects](#af3a248c0e3b05c84b1dd38642f7cf2a1) |
| --- |

Kernel Object Types.

This enumeration needs to be kept in sync with the lists of kernel objects and subsystems in scripts/build/gen\_kobject\_list.py, as well as the otype\_to\_str() function in kernel/userspace.c

| Enumerator | |
| --- | --- |
| K\_OBJ\_ANY |  |
| K\_OBJ\_LAST |  |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [kobject.h](kobject_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
