---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structi3c__ccc__address.html
original_path: doxygen/html/structi3c__ccc__address.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i3c\_ccc\_address Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [I3C Interface](group__i3c__interface.md) » [I3C Common Command Codes](group__i3c__ccc.md)

Payload for a single device address.
[More...](#details)

`#include <[ccc.h](ccc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [addr](#afc3d7db034b3fd72c6118790a18a677b) |

## Detailed Description

Payload for a single device address.

This is used for:

- SETDASA (Set Dynamic Address from Static Address)
- SETNEWDA (Set New Dynamic Address)
- SETGRPA (Set Group Address)
- GETACCCR (Get Accept Controller Role)

Note that the target address is encoded within struct [i3c\_ccc\_target\_payload](structi3c__ccc__target__payload.md "Payload structure for Direct CCC to one target.") instead of being encoded in this payload.

## Field Documentation

## [◆ ](#afc3d7db034b3fd72c6118790a18a677b)addr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_ccc\_address::addr |
| --- |

- For SETDASA, Static Address to be assigned as Dynamic Address.
- For SETNEWDA, new Dynamic Address to be assigned.
- For SETGRPA, new Group Address to be set.
- For GETACCCR, the correct address of Secondary Controller.

Note
:   For SETDATA, SETNEWDA and SETGRPA, the address is left-shift by 1, and bit[0] is always 0.
:   Fpr SET GETACCCR, the address is left-shift by 1, and bit[0] is the calculated odd parity bit.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/i3c/[ccc.h](ccc_8h_source.md)

- [i3c\_ccc\_address](structi3c__ccc__address.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
