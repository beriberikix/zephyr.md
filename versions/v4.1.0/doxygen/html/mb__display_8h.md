---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/mb__display_8h.html
original_path: doxygen/html/mb__display_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mb\_display.h File Reference

BBC micro:bit display APIs.
[More...](#details)

`#include <[stdio.h](stdio_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`

[Go to the source code of this file.](mb__display_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [mb\_image](structmb__image.md) |
|  | Representation of a BBC micro:bit display image. [More...](structmb__image.md#details) |

| Macros | |
| --- | --- |
| #define | [MB\_IMAGE](group__mb__display.md#ga529a5650acaf699b23b4b4234127cf2c)(\_rows...) |
|  | Generate an image object from a given array rows/columns. |

| Enumerations | |
| --- | --- |
| enum | [mb\_display\_mode](group__mb__display.md#ga750a177cffbb90ab38392d9ebad9a8eb) { [MB\_DISPLAY\_MODE\_DEFAULT](group__mb__display.md#gga750a177cffbb90ab38392d9ebad9a8eba804d6d635a1525c85fd4bd349a56fff5) , [MB\_DISPLAY\_MODE\_SINGLE](group__mb__display.md#gga750a177cffbb90ab38392d9ebad9a8eba4cc5223f0f4d28c9bb7c8be5ee6a744a) , [MB\_DISPLAY\_MODE\_SCROLL](group__mb__display.md#gga750a177cffbb90ab38392d9ebad9a8ebaa9e5d94518766711673e3c1e7b513e69) , [MB\_DISPLAY\_FLAG\_LOOP](group__mb__display.md#gga750a177cffbb90ab38392d9ebad9a8ebac96bf2e5073ffa9ec8521b67c8d581cc) = BIT(16) } |
|  | Display mode. [More...](group__mb__display.md#ga750a177cffbb90ab38392d9ebad9a8eb) |

| Functions | |
| --- | --- |
| struct mb\_display \* | [mb\_display\_get](group__mb__display.md#ga94e3eadd1cf386b8d9494ccfa8afaa40) (void) |
|  | Get a pointer to the BBC micro:bit display object. |
| void | [mb\_display\_image](group__mb__display.md#ga2a6e20d57d0d65033281dd7c3ea19126) (struct mb\_display \*disp, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mode, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) duration, const struct [mb\_image](structmb__image.md) \*img, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) img\_count) |
|  | Display one or more images on the BBC micro:bit LED display. |
| void | [mb\_display\_print](group__mb__display.md#ga993a6a0225206f53170d25d9177c1225) (struct mb\_display \*disp, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mode, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) duration, const char \*fmt,...) |
|  | Print a string of characters on the BBC micro:bit LED display. |
| void | [mb\_display\_stop](group__mb__display.md#gad15b3635993007d8aad9364cbe29311b) (struct mb\_display \*disp) |
|  | Stop the ongoing display of an image. |

## Detailed Description

BBC micro:bit display APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [display](dir_dbe0bbdb2da2eed929c1e8ee8e4a99ef.md)
- [mb\_display.h](mb__display_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
