---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__fatal__types.html
original_path: doxygen/html/group__fatal__types.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Fatal error base types

[Kernel APIs](group__kernel__apis.md) » [Fatal error APIs](group__fatal__apis.md)

| Enumerations | |
| --- | --- |
| enum | [k\_fatal\_error\_reason](#ga5b7e799fa19549ef9416a2d6cba29b52) {     [K\_ERR\_CPU\_EXCEPTION](#gga5b7e799fa19549ef9416a2d6cba29b52af9ac087d07f036fae2e689a2afc8d88b) , [K\_ERR\_SPURIOUS\_IRQ](#gga5b7e799fa19549ef9416a2d6cba29b52a473dca11c5f93f5059a119a8e66e2db3) , [K\_ERR\_STACK\_CHK\_FAIL](#gga5b7e799fa19549ef9416a2d6cba29b52a4156a6495ca0fe0867a17a91efc42e91) , [K\_ERR\_KERNEL\_OOPS](#gga5b7e799fa19549ef9416a2d6cba29b52ad6bc280fafebf22e2c97481cc4a5b7c3) ,     [K\_ERR\_KERNEL\_PANIC](#gga5b7e799fa19549ef9416a2d6cba29b52a6ea29e224a1bc958a961420471711617) , [K\_ERR\_ARCH\_START](#gga5b7e799fa19549ef9416a2d6cba29b52a45d4bf1a392f99d6b4d15f50a0e333d1) = 16   } |

## Detailed Description

## Enumeration Type Documentation

## [◆ ](#ga5b7e799fa19549ef9416a2d6cba29b52)k\_fatal\_error\_reason

| enum [k\_fatal\_error\_reason](#ga5b7e799fa19549ef9416a2d6cba29b52) |
| --- |

`#include <[fatal_types.h](fatal__types_8h.md)>`

| Enumerator | |
| --- | --- |
| K\_ERR\_CPU\_EXCEPTION | Generic CPU exception, not covered by other codes. |
| K\_ERR\_SPURIOUS\_IRQ | Unhandled hardware interrupt. |
| K\_ERR\_STACK\_CHK\_FAIL | Faulting context overflowed its stack buffer. |
| K\_ERR\_KERNEL\_OOPS | Moderate severity software error. |
| K\_ERR\_KERNEL\_PANIC | High severity software error. |
| K\_ERR\_ARCH\_START | Arch specific fatal errors. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
