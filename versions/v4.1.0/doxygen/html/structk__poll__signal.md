---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structk__poll__signal.html
original_path: doxygen/html/structk__poll__signal.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

k\_poll\_signal Struct Reference

[Kernel APIs](group__kernel__apis.md) » [Async polling APIs](group__poll__apis.md)

`#include <[kernel.h](kernel_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) | [poll\_events](#a22e88955ba0e369d39edefadcf4c60fd) |
|  | PRIVATE - DO NOT TOUCH. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [signaled](#ae9fe6751d75f7d2b2800cb723603c0fe) |
|  | 1 if the event has been signaled, 0 otherwise. |
| int | [result](#ab438c1e36cecda66fe2c4642518a1db1) |
|  | custom result value passed to [k\_poll\_signal\_raise()](group__poll__apis.md#gad0bf3825f828ec3ca37481bf3cbd6723 "Signal a poll signal object.") if needed |

## Field Documentation

## [◆ ](#a22e88955ba0e369d39edefadcf4c60fd)poll\_events

| [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) k\_poll\_signal::poll\_events |
| --- |

PRIVATE - DO NOT TOUCH.

## [◆ ](#ab438c1e36cecda66fe2c4642518a1db1)result

| int k\_poll\_signal::result |
| --- |

custom result value passed to [k\_poll\_signal\_raise()](group__poll__apis.md#gad0bf3825f828ec3ca37481bf3cbd6723 "Signal a poll signal object.") if needed

## [◆ ](#ae9fe6751d75f7d2b2800cb723603c0fe)signaled

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int k\_poll\_signal::signaled |
| --- |

1 if the event has been signaled, 0 otherwise.

Stays set to 1 until user resets it to 0.

---

The documentation for this struct was generated from the following file:

- zephyr/[kernel.h](kernel_8h_source.md)

- [k\_poll\_signal](structk__poll__signal.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
