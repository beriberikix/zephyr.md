---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__timing__api__board.html
original_path: doxygen/html/group__timing__api__board.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Board specific Timing Measurement APIs

[Operating System Services](group__os__services.md) » [Timing Measurement APIs](group__timing__api.md)

Board specific Timing Measurement APIs.
[More...](#details)

| Functions | |
| --- | --- |
| void | [board\_timing\_init](#ga742db89830e823a804691d1946a8659c) (void) |
|  | Initialize the timing subsystem. |
| void | [board\_timing\_start](#gaf086f6f6881fd1e530a91f56c7ca3972) (void) |
|  | Signal the start of the timing information gathering. |
| void | [board\_timing\_stop](#ga5cf801e99ca32b4dcb86d82c8d4c10d8) (void) |
|  | Signal the end of the timing information gathering. |
| [timing\_t](include_2zephyr_2timing_2types_8h.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2) | [board\_timing\_counter\_get](#gafda53aa3668e5a98d92d48eec6c6da3a) (void) |
|  | Return timing counter. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [board\_timing\_cycles\_get](#ga087f9f0a8915ec2f23e64c2e8b023ec8) (volatile [timing\_t](include_2zephyr_2timing_2types_8h.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2) \*const start, volatile [timing\_t](include_2zephyr_2timing_2types_8h.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2) \*const end) |
|  | Get number of cycles between `start` and `end`. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [board\_timing\_freq\_get](#ga905f59f65aae3802906274ff6d8ab1ee) (void) |
|  | Get frequency of counter used (in Hz). |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [board\_timing\_cycles\_to\_ns](#ga05755593eaf5ab7c2cc9af3d33bea343) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) cycles) |
|  | Convert number of `cycles` into nanoseconds. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [board\_timing\_cycles\_to\_ns\_avg](#ga69ec0aee09f8492f293a3e90a49faa83) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) cycles, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) count) |
|  | Convert number of `cycles` into nanoseconds with averaging. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [board\_timing\_freq\_get\_mhz](#gac32edf3332275176d6fa7563da0e06ff) (void) |
|  | Get frequency of counter used (in MHz). |

## Detailed Description

Board specific Timing Measurement APIs.

Implements the necessary bits to support timing measurement using board specific timing measurement mechanism.

## Function Documentation

## [◆ ](#gafda53aa3668e5a98d92d48eec6c6da3a)board\_timing\_counter\_get()

| [timing\_t](include_2zephyr_2timing_2types_8h.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2) board\_timing\_counter\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[timing.h](timing_8h.md)>`

Return timing counter.

Note
:   Not all timing counters have 64 bit precision. It is possible to see this value "go backwards" due to internal rollover. Timing code must be prepared to address the rollover (with board dependent code, e.g. by casting to a [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) before subtraction) or by using [board\_timing\_cycles\_get()](#ga087f9f0a8915ec2f23e64c2e8b023ec8) which is required to understand the distinction.

Returns
:   Timing counter.

See also
:   [timing\_counter\_get()](group__timing__api.md#gaa5736c87362de09749af1d8ff30b8208 "Return timing counter.")

## [◆ ](#ga087f9f0a8915ec2f23e64c2e8b023ec8)board\_timing\_cycles\_get()

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) board\_timing\_cycles\_get | ( | volatile [timing\_t](include_2zephyr_2timing_2types_8h.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2) \*const | *start*, |
| --- | --- | --- | --- |
|  |  | volatile [timing\_t](include_2zephyr_2timing_2types_8h.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2) \*const | *end* ) |

`#include <[timing.h](timing_8h.md)>`

Get number of cycles between `start` and `end`.

Note
:   The raw numbers from counter need to be scaled to obtain actual number of cycles, or may roll over internally. This function computes a positive-definite interval between two returned cycle values.

Parameters
:   | start | Pointer to counter at start of a measured execution. |
    | --- | --- |
    | end | Pointer to counter at stop of a measured execution. |

Returns
:   Number of cycles between start and end.

See also
:   [timing\_cycles\_get()](group__timing__api.md#gaa12074c7645b19578e7ca573c6aa2955 "Get number of cycles between start and end.")

## [◆ ](#ga05755593eaf5ab7c2cc9af3d33bea343)board\_timing\_cycles\_to\_ns()

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) board\_timing\_cycles\_to\_ns | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *cycles* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[timing.h](timing_8h.md)>`

Convert number of `cycles` into nanoseconds.

Parameters
:   | cycles | Number of cycles |
    | --- | --- |

Returns
:   Converted time value

See also
:   [timing\_cycles\_to\_ns()](group__timing__api.md#ga14a85981068350f33c63c93c4b71afe2 "Convert number of cycles into nanoseconds.")

## [◆ ](#ga69ec0aee09f8492f293a3e90a49faa83)board\_timing\_cycles\_to\_ns\_avg()

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) board\_timing\_cycles\_to\_ns\_avg | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *cycles*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *count* ) |

`#include <[timing.h](timing_8h.md)>`

Convert number of `cycles` into nanoseconds with averaging.

Parameters
:   | cycles | Number of cycles |
    | --- | --- |
    | count | Times of accumulated cycles to average over |

Returns
:   Converted time value

See also
:   [timing\_cycles\_to\_ns\_avg()](group__timing__api.md#ga28b0252f3395b6e6b549cb03ea4dbef4 "Convert number of cycles into nanoseconds with averaging.")

## [◆ ](#ga905f59f65aae3802906274ff6d8ab1ee)board\_timing\_freq\_get()

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) board\_timing\_freq\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[timing.h](timing_8h.md)>`

Get frequency of counter used (in Hz).

Returns
:   Frequency of counter used for timing in Hz.

See also
:   [timing\_freq\_get()](group__timing__api.md#gab72ed08d19630cb4cbea4977f2e6723b "Get frequency of counter used (in Hz).")

## [◆ ](#gac32edf3332275176d6fa7563da0e06ff)board\_timing\_freq\_get\_mhz()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) board\_timing\_freq\_get\_mhz | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[timing.h](timing_8h.md)>`

Get frequency of counter used (in MHz).

Returns
:   Frequency of counter used for timing in MHz.

See also
:   [timing\_freq\_get\_mhz()](group__timing__api.md#ga65370ad32eadf61c84b90dc04ecd1d56 "Get frequency of counter used (in MHz).")

## [◆ ](#ga742db89830e823a804691d1946a8659c)board\_timing\_init()

| void board\_timing\_init | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[timing.h](timing_8h.md)>`

Initialize the timing subsystem.

Perform the necessary steps to initialize the timing subsystem.

See also
:   [timing\_init()](group__timing__api.md#ga50ff9040b99d95c56f494014831e4b47 "Initialize the timing subsystem.")

## [◆ ](#gaf086f6f6881fd1e530a91f56c7ca3972)board\_timing\_start()

| void board\_timing\_start | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[timing.h](timing_8h.md)>`

Signal the start of the timing information gathering.

Signal to the timing subsystem that timing information will be gathered from this point forward.

See also
:   [timing\_start()](group__timing__api.md#ga3c28bb4ced0467c284d33c800e070bde "Signal the start of the timing information gathering.")

## [◆ ](#ga5cf801e99ca32b4dcb86d82c8d4c10d8)board\_timing\_stop()

| void board\_timing\_stop | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[timing.h](timing_8h.md)>`

Signal the end of the timing information gathering.

Signal to the timing subsystem that timing information is no longer being gathered from this point forward.

See also
:   [timing\_stop()](group__timing__api.md#gade1584bf683c9c61905513efa4d99cf2 "Signal the end of the timing information gathering.")

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
