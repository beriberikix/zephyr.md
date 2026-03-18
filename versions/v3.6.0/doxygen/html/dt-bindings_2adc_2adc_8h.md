---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/dt-bindings_2adc_2adc_8h.html
original_path: doxygen/html/dt-bindings_2adc_2adc_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

adc.h File Reference

[Go to the source code of this file.](dt-bindings_2adc_2adc_8h_source.md)

| Macros | |
| --- | --- |
| #define | [BIT\_MASK](#a3c12c6d36ad0aa481a3436923d21f4f8)(n) |
| #define | [ADC\_ACQ\_TIME\_MICROSECONDS](#aa80dca07e438ccb1c4f45b9a8052f44e)   (1) |
|  | Acquisition time is expressed in microseconds. |
| #define | [ADC\_ACQ\_TIME\_NANOSECONDS](#a1d7580e098809a5ba2dec139a05af988)   (2) |
|  | Acquisition time is expressed in nanoseconds. |
| #define | [ADC\_ACQ\_TIME\_TICKS](#acff5af9f7a7b49bbfeab1b6716c7c18f)   (3) |
|  | Acquisition time is expressed in ADC ticks. |
| #define | [ADC\_ACQ\_TIME](#a313a316cb91adcef0125679220efe2b7)(unit, value) |
|  | Macro for composing the acquisition time value in given units. |
| #define | [ADC\_ACQ\_TIME\_DEFAULT](#a3f0840d3d6300e9c26be1b2889ecbd54)   0 |
|  | Value indicating that the default acquisition time should be used. |
| #define | [ADC\_ACQ\_TIME\_MAX](#a5c89f077922d9b84229b5525f5408ebe)   [BIT\_MASK](#a3c12c6d36ad0aa481a3436923d21f4f8)(14) |
| #define | [ADC\_ACQ\_TIME\_UNIT](#ae66e4a40b8e4b1e34c68b806363b95cf)([time](lib_2libc_2minimal_2include_2time_8h.md#a99ef1cb2c789827dd5db3886dccf9067)) |
| #define | [ADC\_ACQ\_TIME\_VALUE](#a720640550d3a29e0181819ec31d5dda6)([time](lib_2libc_2minimal_2include_2time_8h.md#a99ef1cb2c789827dd5db3886dccf9067)) |

## Macro Definition Documentation

## [◆ ](#a313a316cb91adcef0125679220efe2b7)ADC\_ACQ\_TIME

| #define ADC\_ACQ\_TIME | ( |  | *unit*, |
| --- | --- | --- | --- |
|  |  |  | *value* ) |

**Value:**

(((unit) << 14) | ((value) & [BIT\_MASK](#a3c12c6d36ad0aa481a3436923d21f4f8)(14)))

[BIT\_MASK](#a3c12c6d36ad0aa481a3436923d21f4f8)

#define BIT\_MASK(n)

**Definition** adc.h:14

Macro for composing the acquisition time value in given units.

## [◆ ](#a3f0840d3d6300e9c26be1b2889ecbd54)ADC\_ACQ\_TIME\_DEFAULT

| #define ADC\_ACQ\_TIME\_DEFAULT   0 |
| --- |

Value indicating that the default acquisition time should be used.

## [◆ ](#a5c89f077922d9b84229b5525f5408ebe)ADC\_ACQ\_TIME\_MAX

| #define ADC\_ACQ\_TIME\_MAX   [BIT\_MASK](#a3c12c6d36ad0aa481a3436923d21f4f8)(14) |
| --- |

## [◆ ](#aa80dca07e438ccb1c4f45b9a8052f44e)ADC\_ACQ\_TIME\_MICROSECONDS

| #define ADC\_ACQ\_TIME\_MICROSECONDS   (1) |
| --- |

Acquisition time is expressed in microseconds.

## [◆ ](#a1d7580e098809a5ba2dec139a05af988)ADC\_ACQ\_TIME\_NANOSECONDS

| #define ADC\_ACQ\_TIME\_NANOSECONDS   (2) |
| --- |

Acquisition time is expressed in nanoseconds.

## [◆ ](#acff5af9f7a7b49bbfeab1b6716c7c18f)ADC\_ACQ\_TIME\_TICKS

| #define ADC\_ACQ\_TIME\_TICKS   (3) |
| --- |

Acquisition time is expressed in ADC ticks.

## [◆ ](#ae66e4a40b8e4b1e34c68b806363b95cf)ADC\_ACQ\_TIME\_UNIT

| #define ADC\_ACQ\_TIME\_UNIT | ( |  | *[time](lib_2libc_2minimal_2include_2time_8h.md#a99ef1cb2c789827dd5db3886dccf9067)* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((([time](lib_2libc_2minimal_2include_2time_8h.md#a99ef1cb2c789827dd5db3886dccf9067)) >> 14) & [BIT\_MASK](#a3c12c6d36ad0aa481a3436923d21f4f8)(2))

[time](lib_2libc_2minimal_2include_2time_8h.md#a99ef1cb2c789827dd5db3886dccf9067)

time\_t time(time\_t \*tloc)

## [◆ ](#a720640550d3a29e0181819ec31d5dda6)ADC\_ACQ\_TIME\_VALUE

| #define ADC\_ACQ\_TIME\_VALUE | ( |  | *[time](lib_2libc_2minimal_2include_2time_8h.md#a99ef1cb2c789827dd5db3886dccf9067)* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(([time](lib_2libc_2minimal_2include_2time_8h.md#a99ef1cb2c789827dd5db3886dccf9067)) & [BIT\_MASK](#a3c12c6d36ad0aa481a3436923d21f4f8)(14))

## [◆ ](#a3c12c6d36ad0aa481a3436923d21f4f8)BIT\_MASK

| #define BIT\_MASK | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((1 << (n)) - 1)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [adc](dir_1661dc856f6689c520a6419e0ea32218.md)
- [adc.h](dt-bindings_2adc_2adc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
