---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/log__frontend__stmesp_8h.html
original_path: doxygen/html/log__frontend__stmesp_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_frontend\_stmesp.h File Reference

`#include <[errno.h](errno_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`

[Go to the source code of this file.](log__frontend__stmesp_8h_source.md)

| Functions | |
| --- | --- |
| int | [log\_frontend\_stmesp\_etr\_ready](#afdfa76ad219bd073b54825ae50cf13d3) (void) |
|  | Notify frontend that ETR/STM is ready. |
| void | [log\_frontend\_stmesp\_pre\_sleep](#ae222ceeee8aa370e3aaeb6eb8f1e1a8f) (void) |
|  | Hook to be called before going to sleep. |
| void | [log\_frontend\_stmesp\_dummy\_write](#acb1274db685fbd6282868b03d3c627da) (void) |
|  | Perform a dummy write to STMESP. |
| static void | [log\_frontend\_stmesp\_tp](#ab2b829f38108c54490090dcd97719cec) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) x) |
|  | Trace point. |
| static void | [log\_frontend\_stmesp\_tp\_d32](#a68b8bdb65457ffa2c0ab7c97b8414600) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) x, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)) |
|  | Trace point with 32 bit data. |

## Function Documentation

## [◆ ](#acb1274db685fbd6282868b03d3c627da)log\_frontend\_stmesp\_dummy\_write()

| void log\_frontend\_stmesp\_dummy\_write | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Perform a dummy write to STMESP.

It can be used to force flushing STM data.

## [◆ ](#afdfa76ad219bd073b54825ae50cf13d3)log\_frontend\_stmesp\_etr\_ready()

| int log\_frontend\_stmesp\_etr\_ready | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Notify frontend that ETR/STM is ready.

Log frontend optionally dumps buffered data and start to write to the STM stimulus port.

Note
:   Function is applicable only for the domain that performs initial ETR/STM setup.

Return values
:   | 0 | on success. |
    | --- | --- |
    | -EIO | if there was an internal failure. |

## [◆ ](#ae222ceeee8aa370e3aaeb6eb8f1e1a8f)log\_frontend\_stmesp\_pre\_sleep()

| void log\_frontend\_stmesp\_pre\_sleep | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Hook to be called before going to sleep.

Hook writes dummy data to the STM Stimulus Port to ensure that all logging data is flushed.

## [◆ ](#ab2b829f38108c54490090dcd97719cec)log\_frontend\_stmesp\_tp()

| | void log\_frontend\_stmesp\_tp | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *x* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Trace point.

Write a trace point information using STM. Number of unique trace points is limited to 65536 - CONFIG\_LOG\_FRONTEND\_STMESP\_TP\_CHAN\_BASE per core.

Parameters
:   | x | Trace point ID. |
    | --- | --- |

## [◆ ](#a68b8bdb65457ffa2c0ab7c97b8414600)log\_frontend\_stmesp\_tp\_d32()

| | void log\_frontend\_stmesp\_tp\_d32 | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *x*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *d* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Trace point with 32 bit data.

Write a trace point information using STM. Number of unique trace points is limited to 65536 - CONFIG\_LOG\_FRONTEND\_STMESP\_TP\_CHAN\_BASE per core.

Parameters
:   | x | Trace point ID. |
    | --- | --- |
    | [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417) | Data. 32 bit word. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log\_frontend\_stmesp.h](log__frontend__stmesp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
