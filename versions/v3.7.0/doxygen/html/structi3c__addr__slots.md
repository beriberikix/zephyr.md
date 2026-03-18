---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structi3c__addr__slots.html
original_path: doxygen/html/structi3c__addr__slots.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i3c\_addr\_slots Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [I3C Interface](group__i3c__interface.md) » [I3C Address-related Helper Code](group__i3c__addresses.md)

Structure to keep track of addresses on I3C bus.
[More...](#details)

`#include <[addresses.h](addresses_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [slots](#a8117bc5c9b55bb074a845f8a4fe405fb) [((0x7F+1) \*2)/[BITS\_PER\_LONG](group__sys-util.md#ga2f660aa23a5dbc0f4b8df48b4302b8c3)] |

## Detailed Description

Structure to keep track of addresses on I3C bus.

## Field Documentation

## [◆ ](#a8117bc5c9b55bb074a845f8a4fe405fb)slots

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long i3c\_addr\_slots::slots[((0x7F+1) \*2)/[BITS\_PER\_LONG](group__sys-util.md#ga2f660aa23a5dbc0f4b8df48b4302b8c3)] |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/i3c/[addresses.h](addresses_8h_source.md)

- [i3c\_addr\_slots](structi3c__addr__slots.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
