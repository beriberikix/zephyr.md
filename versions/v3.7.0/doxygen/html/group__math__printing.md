---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__math__printing.html
original_path: doxygen/html/group__math__printing.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Helper macros for printing Q values.

[DSP Interface](group__math__dsp.md)

Extends the existing inttypes headers for print formatting.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [PRIq](#ga08618ad8449ee21f0a57c151541e8ef8)(precision) |
|  | Insert Q value format string. |
| #define | [PRIq\_arg](#gad0393d2bb183784a9c09f2c05d7987f9)(q, precision, shift) |
|  | Insert Q value arguments to print format. |

## Detailed Description

Extends the existing inttypes headers for print formatting.

Usage:

[printk](printk_8h.md#a768a7dff8592b69f327a08f96b00fa54)("Value=%" [PRIq](#ga08618ad8449ee21f0a57c151541e8ef8) "\n", [PRIq\_arg](#gad0393d2bb183784a9c09f2c05d7987f9)(value, 6, 2));

[PRIq](#ga08618ad8449ee21f0a57c151541e8ef8)

#define PRIq(precision)

Insert Q value format string.

**Definition** print\_format.h:30

[PRIq\_arg](#gad0393d2bb183784a9c09f2c05d7987f9)

#define PRIq\_arg(q, precision, shift)

Insert Q value arguments to print format.

**Definition** print\_format.h:58

[printk](printk_8h.md#a768a7dff8592b69f327a08f96b00fa54)

static void printk(const char \*fmt,...)

Print kernel debugging message.

**Definition** printk.h:51

For a Q value representing 0.5, the expected output will be: "Value=2.000000"

## Macro Definition Documentation

## [◆ ](#ga08618ad8449ee21f0a57c151541e8ef8)PRIq

| #define PRIq | ( |  | *precision* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[print_format.h](print__format_8h.md)>`

**Value:**

"s%" [PRIu32](inttypes_8h.md#aaf2af4a10f0bd308e9c349c8382382be) ".%0" [STRINGIFY](common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(precision) [PRIu32](inttypes_8h.md#aaf2af4a10f0bd308e9c349c8382382be)

[STRINGIFY](common_8h.md#a4689212d5a549893cabb9d7782eecfb6)

#define STRINGIFY(s)

**Definition** common.h:134

[PRIu32](inttypes_8h.md#aaf2af4a10f0bd308e9c349c8382382be)

#define PRIu32

**Definition** inttypes.h:60

Insert Q value format string.

## [◆ ](#gad0393d2bb183784a9c09f2c05d7987f9)PRIq\_arg

| #define PRIq\_arg | ( |  | *q*, |
| --- | --- | --- | --- |
|  |  |  | *precision*, |
|  |  |  | *shift* ) |

`#include <[print_format.h](print__format_8h.md)>`

**Value:**

((q) < 0 ? "-" : ""), ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))\_\_PRIq\_arg\_get\_int(q, shift), \

([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f))\_\_PRIq\_arg\_get\_frac(q, precision, shift)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

Insert Q value arguments to print format.

Parameters
:   | [in] | q | The q value |
    | --- | --- | --- |
    | [in] | precision | Number of decimal points to print |
    | [in] | shift | The "scale" to shift `q` by |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
