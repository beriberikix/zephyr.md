---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structi3c__ccc__getpid.html
original_path: doxygen/html/structi3c__ccc__getpid.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i3c\_ccc\_getpid Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [I3C Interface](group__i3c__interface.md) » [I3C Common Command Codes](group__i3c__ccc.md)

Payload for GETPID CCC (Get Provisioned ID).
[More...](#details)

`#include <[ccc.h](ccc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [pid](#a060023fcb180e44b39a73c0f955f02c7) [6] |
|  | 48-bit Provisioned ID. |

## Detailed Description

Payload for GETPID CCC (Get Provisioned ID).

## Field Documentation

## [◆ ](#a060023fcb180e44b39a73c0f955f02c7)pid

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_ccc\_getpid::pid[6] |
| --- |

48-bit Provisioned ID.

Note
:   Data is big-endian where first byte is MSB.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/i3c/[ccc.h](ccc_8h_source.md)

- [i3c\_ccc\_getpid](structi3c__ccc__getpid.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
