---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/log__frontend__stmesp_8h.html
original_path: doxygen/html/log__frontend__stmesp_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_frontend\_stmesp.h File Reference

`#include <[errno.h](errno_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`

[Go to the source code of this file.](log__frontend__stmesp_8h_source.md)

| Macros | |
| --- | --- |
| #define | [LOG\_FRONTEND\_STMESP\_LOG0](#ae583dd282c17ad3330955b98206b401a)(\_source, ...) |
|  | Macro for handling a turbo log message with no arguments. |
| #define | [LOG\_FRONTEND\_STMESP\_LOG1](#ae82104c26a3426e5c1ab45ba1149204a)(\_source, ...) |
|  | Macro for handling a turbo log message with one argument. |

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
| void | [log\_frontend\_stmesp\_log0](#af3052fc610038ca8b3c2b9488a98d54a) (const void \*source, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) x) |
|  | Function called for log message with no arguments when turbo logging is enabled. |
| void | [log\_frontend\_stmesp\_log1](#a7b9ad98fd11cbc6c28cc6b38307d52c6) (const void \*source, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) x, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arg) |
|  | Function called for log message with one argument when turbo logging is enabled. |
|  | [TYPE\_SECTION\_START\_EXTERN](#a135d13f257ea7bc2a2993d735cede654) (const char \*, log\_stmesp\_ptr) |

## Macro Definition Documentation

## [◆ ](#ae583dd282c17ad3330955b98206b401a)LOG\_FRONTEND\_STMESP\_LOG0

| #define LOG\_FRONTEND\_STMESP\_LOG0 | ( |  | *\_source*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

**Value:**

do { \

static const char \_str[] \_\_in\_section(\_log\_stmesp\_str, static, \_) \

\_\_used \_\_noasan \_\_aligned(sizeof([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))) = [GET\_ARG\_N](group__sys-util.md#gabbe04a4d59a495b2b86196304b937ec6)(1, \_\_VA\_ARGS\_\_); \

static const char \*\_str\_ptr \_\_in\_section(\_log\_stmesp\_ptr, static, \_) \

\_\_used \_\_noasan = \_str; \

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) idx = \

(([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))&\_str\_ptr - ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))[TYPE\_SECTION\_START](group__iterable__section__apis.md#gac97b7f4fd42a2d9e11b6a585bc716a05)(log\_stmesp\_ptr)) / \

sizeof(void \*); \

log\_frontend\_stmesp\_log0(\_source, idx); \

} while (0)

[TYPE\_SECTION\_START](group__iterable__section__apis.md#gac97b7f4fd42a2d9e11b6a585bc716a05)

#define TYPE\_SECTION\_START(secname)

iterable section start symbol for a generic type

**Definition** iterable\_sections.h:55

[GET\_ARG\_N](group__sys-util.md#gabbe04a4d59a495b2b86196304b937ec6)

#define GET\_ARG\_N(N,...)

Get nth argument from argument list.

**Definition** util\_macro.h:391

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

Macro for handling a turbo log message with no arguments.

Parameters
:   | \_source | Pointer to the source structure. |
    | --- | --- |
    | ... | String. |

## [◆ ](#ae82104c26a3426e5c1ab45ba1149204a)LOG\_FRONTEND\_STMESP\_LOG1

| #define LOG\_FRONTEND\_STMESP\_LOG1 | ( |  | *\_source*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

**Value:**

do { \

static const char \_str[] \_\_in\_section(\_log\_stmesp\_str, static, \_) \

\_\_used \_\_noasan \_\_aligned(sizeof([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))) = [GET\_ARG\_N](group__sys-util.md#gabbe04a4d59a495b2b86196304b937ec6)(1, \_\_VA\_ARGS\_\_); \

static const char \*\_str\_ptr \_\_in\_section(\_log\_stmesp\_ptr, static, \_) \

\_\_used \_\_noasan = \_str; \

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) idx = \

(([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))&\_str\_ptr - ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))[TYPE\_SECTION\_START](group__iterable__section__apis.md#gac97b7f4fd42a2d9e11b6a585bc716a05)(log\_stmesp\_ptr)) / \

sizeof(void \*); \

log\_frontend\_stmesp\_log1(\_source, idx, ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))([GET\_ARG\_N](group__sys-util.md#gabbe04a4d59a495b2b86196304b937ec6)(2, \_\_VA\_ARGS\_\_))); \

} while (0)

Macro for handling a turbo log message with one argument.

Parameters
:   | \_source | Pointer to the source structure. |
    | --- | --- |
    | ... | String with one numeric argument. |

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

## [◆ ](#af3052fc610038ca8b3c2b9488a98d54a)log\_frontend\_stmesp\_log0()

| void log\_frontend\_stmesp\_log0 | ( | const void \* | *source*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *x* ) |

Function called for log message with no arguments when turbo logging is enabled.

Parameters
:   | source | Pointer to the source structure. |
    | --- | --- |
    | x | Index of the string used for the log message. |

## [◆ ](#a7b9ad98fd11cbc6c28cc6b38307d52c6)log\_frontend\_stmesp\_log1()

| void log\_frontend\_stmesp\_log1 | ( | const void \* | *source*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *x*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *arg* ) |

Function called for log message with one argument when turbo logging is enabled.

Parameters
:   | source | Pointer to the source structure. |
    | --- | --- |
    | x | Index of the string used for the log message. |
    | arg | Argument. |

## [◆ ](#ae222ceeee8aa370e3aaeb6eb8f1e1a8f)log\_frontend\_stmesp\_pre\_sleep()

| void log\_frontend\_stmesp\_pre\_sleep | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Hook to be called before going to sleep.

Hook writes dummy data to the STM Stimulus Port to ensure that all logging data is flushed.

## [◆ ](#ab2b829f38108c54490090dcd97719cec)log\_frontend\_stmesp\_tp()

| | void log\_frontend\_stmesp\_tp | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *x* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Trace point.

Write a trace point information using STM. Number of unique trace points is limited to 32768 - CONFIG\_LOG\_FRONTEND\_STMESP\_TP\_CHAN\_BASE per core.

Parameters
:   | x | Trace point ID. |
    | --- | --- |

## [◆ ](#a68b8bdb65457ffa2c0ab7c97b8414600)log\_frontend\_stmesp\_tp\_d32()

| | void log\_frontend\_stmesp\_tp\_d32 | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *x*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *d* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Trace point with 32 bit data.

Write a trace point information using STM. Number of unique trace points is limited to 32768 - CONFIG\_LOG\_FRONTEND\_STMESP\_TP\_CHAN\_BASE per core.

Parameters
:   | x | Trace point ID. |
    | --- | --- |
    | [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417) | Data. 32 bit word. |

## [◆ ](#a135d13f257ea7bc2a2993d735cede654)TYPE\_SECTION\_START\_EXTERN()

| TYPE\_SECTION\_START\_EXTERN | ( | const char \* | , |
| --- | --- | --- | --- |
|  |  | log\_stmesp\_ptr | ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log\_frontend\_stmesp.h](log__frontend__stmesp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
