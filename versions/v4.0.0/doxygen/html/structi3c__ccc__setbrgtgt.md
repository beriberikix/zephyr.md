---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structi3c__ccc__setbrgtgt.html
original_path: doxygen/html/structi3c__ccc__setbrgtgt.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i3c\_ccc\_setbrgtgt Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [I3C Interface](group__i3c__interface.md) » [I3C Common Command Codes](group__i3c__ccc.md)

Payload for SETBRGTGT CCC (Set Bridge Targets).
[More...](#details)

`#include <[ccc.h](ccc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [count](#a9099e2979baca2c3fbbb7a6b781edbf3) |
|  | Number of bridged targets. |
| struct [i3c\_ccc\_setbrgtgt\_tgt](structi3c__ccc__setbrgtgt__tgt.md) | [targets](#aa019eb13d7da60941382c6e43884b60d) [] |
|  | Array of bridged targets. |

## Detailed Description

Payload for SETBRGTGT CCC (Set Bridge Targets).

Note that the bridge target address is encoded within struct [i3c\_ccc\_target\_payload](structi3c__ccc__target__payload.md "Payload structure for Direct CCC to one target.") instead of being encoded in this payload.

## Field Documentation

## [◆ ](#a9099e2979baca2c3fbbb7a6b781edbf3)count

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_ccc\_setbrgtgt::count |
| --- |

Number of bridged targets.

## [◆ ](#aa019eb13d7da60941382c6e43884b60d)targets

| struct [i3c\_ccc\_setbrgtgt\_tgt](structi3c__ccc__setbrgtgt__tgt.md) i3c\_ccc\_setbrgtgt::targets[] |
| --- |

Array of bridged targets.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/i3c/[ccc.h](ccc_8h_source.md)

- [i3c\_ccc\_setbrgtgt](structi3c__ccc__setbrgtgt.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
