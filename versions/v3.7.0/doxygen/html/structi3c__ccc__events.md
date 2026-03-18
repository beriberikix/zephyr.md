---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structi3c__ccc__events.html
original_path: doxygen/html/structi3c__ccc__events.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i3c\_ccc\_events Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [I3C Interface](group__i3c__interface.md) » [I3C Common Command Codes](group__i3c__ccc.md)

Payload for ENEC/DISEC CCC (Target Events Command).
[More...](#details)

`#include <[ccc.h](ccc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [events](#ac34bcdae31cdc718eb54962d6b707320) |
|  | Event byte: |

## Detailed Description

Payload for ENEC/DISEC CCC (Target Events Command).

## Field Documentation

## [◆ ](#ac34bcdae31cdc718eb54962d6b707320)events

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_ccc\_events::events |
| --- |

Event byte:

- Bit[0]: ENINT/DISINT:
  - Target Interrupt Requests
- Bit[1]: ENCR/DISCR:
  - Controller Role Requests
- Bit[3]: ENHJ/DISHJ:
  - Hot-Join Event

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/i3c/[ccc.h](ccc_8h_source.md)

- [i3c\_ccc\_events](structi3c__ccc__events.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
