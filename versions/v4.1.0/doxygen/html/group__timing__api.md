---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__timing__api.html
original_path: doxygen/html/group__timing__api.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Timing Measurement APIs

[Operating System Services](group__os__services.md)

Timing Measurement APIs.
[More...](#details)

| Topics | |
| --- | --- |
|  | [Arch specific Timing Measurement APIs](group__timing__api__arch.md) |
|  | Arch specific Timing Measurement APIs. |
|  | [Board specific Timing Measurement APIs](group__timing__api__board.md) |
|  | Board specific Timing Measurement APIs. |
|  | [SoC specific Timing Measurement APIs](group__timing__api__soc.md) |
|  | SoC specific Timing Measurement APIs. |

| Functions | |
| --- | --- |
| void | [timing\_init](#ga50ff9040b99d95c56f494014831e4b47) (void) |
|  | Initialize the timing subsystem. |
| void | [timing\_start](#ga3c28bb4ced0467c284d33c800e070bde) (void) |
|  | Signal the start of the timing information gathering. |
| void | [timing\_stop](#gade1584bf683c9c61905513efa4d99cf2) (void) |
|  | Signal the end of the timing information gathering. |
| static [timing\_t](include_2zephyr_2timing_2types_8h.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2) | [timing\_counter\_get](#gaa5736c87362de09749af1d8ff30b8208) (void) |
|  | Return timing counter. |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [timing\_cycles\_get](#gaa12074c7645b19578e7ca573c6aa2955) (volatile [timing\_t](include_2zephyr_2timing_2types_8h.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2) \*const start, volatile [timing\_t](include_2zephyr_2timing_2types_8h.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2) \*const end) |
|  | Get number of cycles between `start` and `end`. |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [timing\_freq\_get](#gab72ed08d19630cb4cbea4977f2e6723b) (void) |
|  | Get frequency of counter used (in Hz). |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [timing\_cycles\_to\_ns](#ga14a85981068350f33c63c93c4b71afe2) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) cycles) |
|  | Convert number of `cycles` into nanoseconds. |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [timing\_cycles\_to\_ns\_avg](#ga28b0252f3395b6e6b549cb03ea4dbef4) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) cycles, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) count) |
|  | Convert number of `cycles` into nanoseconds with averaging. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [timing\_freq\_get\_mhz](#ga65370ad32eadf61c84b90dc04ecd1d56) (void) |
|  | Get frequency of counter used (in MHz). |

## Detailed Description

Timing Measurement APIs.

The timing measurement APIs can be used to obtain execution time of a section of code to aid in analysis and optimization.

Please note that the timing functions may use a different timer than the default kernel timer, where the timer being used is specified by architecture, SoC or board configuration.

## Function Documentation

## [◆ ](#gaa5736c87362de09749af1d8ff30b8208)timing\_counter\_get()

| | [timing\_t](include_2zephyr_2timing_2types_8h.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2) timing\_counter\_get | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[timing.h](timing_8h.md)>`

Return timing counter.

Returns
:   Timing counter.

## [◆ ](#gaa12074c7645b19578e7ca573c6aa2955)timing\_cycles\_get()

| | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) timing\_cycles\_get | ( | volatile [timing\_t](include_2zephyr_2timing_2types_8h.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2) \*const | *start*, | | --- | --- | --- | --- | |  |  | volatile [timing\_t](include_2zephyr_2timing_2types_8h.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2) \*const | *end* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[timing.h](timing_8h.md)>`

Get number of cycles between `start` and `end`.

For some architectures or SoCs, the raw numbers from counter need to be scaled to obtain actual number of cycles.

Parameters
:   | start | Pointer to counter at start of a measured execution. |
    | --- | --- |
    | end | Pointer to counter at stop of a measured execution. |

Returns
:   Number of cycles between start and end.

## [◆ ](#ga14a85981068350f33c63c93c4b71afe2)timing\_cycles\_to\_ns()

| | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) timing\_cycles\_to\_ns | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *cycles* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[timing.h](timing_8h.md)>`

Convert number of `cycles` into nanoseconds.

Parameters
:   | cycles | Number of cycles |
    | --- | --- |

Returns
:   Converted time value

## [◆ ](#ga28b0252f3395b6e6b549cb03ea4dbef4)timing\_cycles\_to\_ns\_avg()

| | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) timing\_cycles\_to\_ns\_avg | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *cycles*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *count* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[timing.h](timing_8h.md)>`

Convert number of `cycles` into nanoseconds with averaging.

Parameters
:   | cycles | Number of cycles |
    | --- | --- |
    | count | Times of accumulated cycles to average over |

Returns
:   Converted time value

## [◆ ](#gab72ed08d19630cb4cbea4977f2e6723b)timing\_freq\_get()

| | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) timing\_freq\_get | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[timing.h](timing_8h.md)>`

Get frequency of counter used (in Hz).

Returns
:   Frequency of counter used for timing in Hz.

## [◆ ](#ga65370ad32eadf61c84b90dc04ecd1d56)timing\_freq\_get\_mhz()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) timing\_freq\_get\_mhz | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[timing.h](timing_8h.md)>`

Get frequency of counter used (in MHz).

Returns
:   Frequency of counter used for timing in MHz.

## [◆ ](#ga50ff9040b99d95c56f494014831e4b47)timing\_init()

| void timing\_init | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[timing.h](timing_8h.md)>`

Initialize the timing subsystem.

Perform the necessary steps to initialize the timing subsystem.

## [◆ ](#ga3c28bb4ced0467c284d33c800e070bde)timing\_start()

| void timing\_start | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[timing.h](timing_8h.md)>`

Signal the start of the timing information gathering.

Signal to the timing subsystem that timing information will be gathered from this point forward.

## [◆ ](#gade1584bf683c9c61905513efa4d99cf2)timing\_stop()

| void timing\_stop | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[timing.h](timing_8h.md)>`

Signal the end of the timing information gathering.

Signal to the timing subsystem that timing information is no longer being gathered from this point forward.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
