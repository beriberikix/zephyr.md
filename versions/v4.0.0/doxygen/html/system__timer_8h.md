---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/system__timer_8h.html
original_path: doxygen/html/system__timer_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

system\_timer.h File Reference

Timer driver API.
[More...](#details)

`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`

[Go to the source code of this file.](system__timer_8h_source.md)

| Functions | |
| --- | --- |
| void | [sys\_clock\_set\_timeout](group__clock__apis.md#ga747c1f4a99a3bc48e7ec65d7bc5e4767) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) ticks, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) idle) |
|  | Set system clock timeout. |
| void | [sys\_clock\_idle\_exit](group__clock__apis.md#ga6ca2139000b8c75b1ed2c6c1f672ff79) (void) |
|  | Timer idle exit notification. |
| void | [sys\_clock\_announce](group__clock__apis.md#gaa7d3b1bdb8d15c907aaafea3b96ac2b5) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) ticks) |
|  | Announce time progress to the kernel. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sys\_clock\_elapsed](group__clock__apis.md#gaa9b6d8eebc69d2808beb0580d974bb84) (void) |
|  | Ticks elapsed since last [sys\_clock\_announce()](group__clock__apis.md#gaa7d3b1bdb8d15c907aaafea3b96ac2b5 "Announce time progress to the kernel.") call. |
| void | [sys\_clock\_disable](group__clock__apis.md#ga49c900ab49a72c347d0aefb14aecb550) (void) |
|  | Disable system timer. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sys\_clock\_cycle\_get\_32](group__clock__apis.md#ga42dcd1878309a82246dbfa26510f868a) (void) |
|  | Hardware cycle counter. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [sys\_clock\_cycle\_get\_64](group__clock__apis.md#ga25328a181bd0229ef5110c15e8452fc1) (void) |
|  | 64 bit hardware cycle counter |

## Detailed Description

Timer driver API.

Declare API implemented by system timer driver and used by kernel components.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [timer](dir_21cf19e3c466cbc66f61aa827c3fd772.md)
- [system\_timer.h](system__timer_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
