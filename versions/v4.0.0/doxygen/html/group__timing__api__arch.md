---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__timing__api__arch.html
original_path: doxygen/html/group__timing__api__arch.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Arch specific Timing Measurement APIs

[Operating System Services](group__os__services.md) » [Timing Measurement APIs](group__timing__api.md)

Arch specific Timing Measurement APIs.
[More...](#details)

| Functions | |
| --- | --- |
| void | [arch\_timing\_init](#ga5d9923569b40437c28879ff4b3ff77c2) (void) |
|  | Initialize the timing subsystem. |
| void | [arch\_timing\_start](#gaf8cd88e81c2104b5eb0fbe42967b7834) (void) |
|  | Signal the start of the timing information gathering. |
| void | [arch\_timing\_stop](#ga566483c64f5c5d2f0465e3f969303fd3) (void) |
|  | Signal the end of the timing information gathering. |
| [timing\_t](include_2zephyr_2timing_2types_8h.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2) | [arch\_timing\_counter\_get](#gad7a709477650c8596a96fe080f583fdd) (void) |
|  | Return timing counter. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [arch\_timing\_cycles\_get](#ga44d3a7bd8b7008c9cd6c0524e97f128c) (volatile [timing\_t](include_2zephyr_2timing_2types_8h.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2) \*const start, volatile [timing\_t](include_2zephyr_2timing_2types_8h.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2) \*const end) |
|  | Get number of cycles between `start` and `end`. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [arch\_timing\_freq\_get](#ga026409e1dc323ceddb82b2a6f1cc7ca2) (void) |
|  | Get frequency of counter used (in Hz). |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [arch\_timing\_cycles\_to\_ns](#ga8424bc96c05dcae34b7ffd445e2916fe) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) cycles) |
|  | Convert number of `cycles` into nanoseconds. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [arch\_timing\_cycles\_to\_ns\_avg](#ga925b4caff80f1dbac36531b479b24364) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) cycles, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) count) |
|  | Convert number of `cycles` into nanoseconds with averaging. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [arch\_timing\_freq\_get\_mhz](#ga1f7bfb9ce0588f3b423c2a63933d40eb) (void) |
|  | Get frequency of counter used (in MHz). |

## Detailed Description

Arch specific Timing Measurement APIs.

Implements the necessary bits to support timing measurement using architecture specific timing measurement mechanism.

## Function Documentation

## [◆ ](#gad7a709477650c8596a96fe080f583fdd)arch\_timing\_counter\_get()

| [timing\_t](include_2zephyr_2timing_2types_8h.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2) arch\_timing\_counter\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Return timing counter.

Note
:   Any call to [arch\_timing\_counter\_get()](#gad7a709477650c8596a96fe080f583fdd) must be done between calls to [arch\_timing\_start()](#gaf8cd88e81c2104b5eb0fbe42967b7834) and [arch\_timing\_stop()](#ga566483c64f5c5d2f0465e3f969303fd3), and on the same CPU core.

Note
:   Not all architectures have a timing counter with 64 bit precision. It is possible to see this value "go backwards" due to internal rollover. Timing code must be prepared to address the rollover (with platform-dependent code, e.g. by casting to a [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) before subtraction) or by using [arch\_timing\_cycles\_get()](#ga44d3a7bd8b7008c9cd6c0524e97f128c) which is required to understand the distinction.

Returns
:   Timing counter.

See also
:   [timing\_counter\_get()](group__timing__api.md#gaa5736c87362de09749af1d8ff30b8208 "Return timing counter.")

## [◆ ](#ga44d3a7bd8b7008c9cd6c0524e97f128c)arch\_timing\_cycles\_get()

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) arch\_timing\_cycles\_get | ( | volatile [timing\_t](include_2zephyr_2timing_2types_8h.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2) \*const | *start*, |
| --- | --- | --- | --- |
|  |  | volatile [timing\_t](include_2zephyr_2timing_2types_8h.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2) \*const | *end* ) |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Get number of cycles between `start` and `end`.

Note
:   For some architectures, the raw numbers from counter need to be scaled to obtain actual number of cycles, or may roll over internally. This function computes a positive-definite interval between two returned cycle values.

Parameters
:   | start | Pointer to counter at start of a measured execution. |
    | --- | --- |
    | end | Pointer to counter at stop of a measured execution. |

Returns
:   Number of cycles between start and end.

See also
:   [timing\_cycles\_get()](group__timing__api.md#gaa12074c7645b19578e7ca573c6aa2955 "Get number of cycles between start and end.")

## [◆ ](#ga8424bc96c05dcae34b7ffd445e2916fe)arch\_timing\_cycles\_to\_ns()

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) arch\_timing\_cycles\_to\_ns | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *cycles* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Convert number of `cycles` into nanoseconds.

Parameters
:   | cycles | Number of cycles |
    | --- | --- |

Returns
:   Converted time value

See also
:   [timing\_cycles\_to\_ns()](group__timing__api.md#ga14a85981068350f33c63c93c4b71afe2 "Convert number of cycles into nanoseconds.")

## [◆ ](#ga925b4caff80f1dbac36531b479b24364)arch\_timing\_cycles\_to\_ns\_avg()

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) arch\_timing\_cycles\_to\_ns\_avg | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *cycles*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *count* ) |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Convert number of `cycles` into nanoseconds with averaging.

Parameters
:   | cycles | Number of cycles |
    | --- | --- |
    | count | Times of accumulated cycles to average over |

Returns
:   Converted time value

See also
:   [timing\_cycles\_to\_ns\_avg()](group__timing__api.md#ga28b0252f3395b6e6b549cb03ea4dbef4 "Convert number of cycles into nanoseconds with averaging.")

## [◆ ](#ga026409e1dc323ceddb82b2a6f1cc7ca2)arch\_timing\_freq\_get()

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) arch\_timing\_freq\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Get frequency of counter used (in Hz).

Returns
:   Frequency of counter used for timing in Hz.

See also
:   [timing\_freq\_get()](group__timing__api.md#gab72ed08d19630cb4cbea4977f2e6723b "Get frequency of counter used (in Hz).")

## [◆ ](#ga1f7bfb9ce0588f3b423c2a63933d40eb)arch\_timing\_freq\_get\_mhz()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arch\_timing\_freq\_get\_mhz | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Get frequency of counter used (in MHz).

Returns
:   Frequency of counter used for timing in MHz.

See also
:   [timing\_freq\_get\_mhz()](group__timing__api.md#ga65370ad32eadf61c84b90dc04ecd1d56 "Get frequency of counter used (in MHz).")

## [◆ ](#ga5d9923569b40437c28879ff4b3ff77c2)arch\_timing\_init()

| void arch\_timing\_init | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Initialize the timing subsystem.

Perform the necessary steps to initialize the timing subsystem.

See also
:   [timing\_init()](group__timing__api.md#ga50ff9040b99d95c56f494014831e4b47 "Initialize the timing subsystem.")

## [◆ ](#gaf8cd88e81c2104b5eb0fbe42967b7834)arch\_timing\_start()

| void arch\_timing\_start | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Signal the start of the timing information gathering.

Signal to the timing subsystem that timing information will be gathered from this point forward.

Note
:   Any call to [arch\_timing\_counter\_get()](#gad7a709477650c8596a96fe080f583fdd) must be done between calls to [arch\_timing\_start()](#gaf8cd88e81c2104b5eb0fbe42967b7834) and [arch\_timing\_stop()](#ga566483c64f5c5d2f0465e3f969303fd3), and on the same CPU core.

See also
:   [timing\_start()](group__timing__api.md#ga3c28bb4ced0467c284d33c800e070bde "Signal the start of the timing information gathering.")

## [◆ ](#ga566483c64f5c5d2f0465e3f969303fd3)arch\_timing\_stop()

| void arch\_timing\_stop | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Signal the end of the timing information gathering.

Signal to the timing subsystem that timing information is no longer being gathered from this point forward.

Note
:   Any call to [arch\_timing\_counter\_get()](#gad7a709477650c8596a96fe080f583fdd) must be done between calls to [arch\_timing\_start()](#gaf8cd88e81c2104b5eb0fbe42967b7834) and [arch\_timing\_stop()](#ga566483c64f5c5d2f0465e3f969303fd3), and on the same CPU core.

See also
:   [timing\_stop()](group__timing__api.md#gade1584bf683c9c61905513efa4d99cf2 "Signal the end of the timing information gathering.")

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
