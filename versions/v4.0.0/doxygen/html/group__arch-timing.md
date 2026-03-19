---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__arch-timing.html
original_path: doxygen/html/group__arch-timing.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Architecture timing APIs

[Internal and System API](group__internal__api.md) » [Architecture Interface](group__arch-interface.md)

| Functions | |
| --- | --- |
| void | [arch\_busy\_wait](#gaffc9f3013d53e72c25243ce4f972549f) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) usec\_to\_wait) |
|  | Architecture-specific implementation of busy-waiting. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [arch\_k\_cycle\_get\_32](#ga9ee9f897ec750957de45bf8d43349d5e) (void) |
|  | Obtain the current cycle count, in units specified by CONFIG\_SYS\_CLOCK\_HW\_CYCLES\_PER\_SEC. |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [arch\_k\_cycle\_get\_64](#gacc1ed8d949f694a1d39e389334caf971) (void) |
|  | As for [arch\_k\_cycle\_get\_32()](#ga9ee9f897ec750957de45bf8d43349d5e), but with a 64 bit return value. |

## Detailed Description

## Function Documentation

## [◆ ](#gaffc9f3013d53e72c25243ce4f972549f)arch\_busy\_wait()

| void arch\_busy\_wait | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *usec\_to\_wait* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel_arch_interface.h](kernel__arch__interface_8h.md)>`

Architecture-specific implementation of busy-waiting.

Parameters
:   | usec\_to\_wait | Wait period, in microseconds |
    | --- | --- |

## [◆ ](#ga9ee9f897ec750957de45bf8d43349d5e)arch\_k\_cycle\_get\_32()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arch\_k\_cycle\_get\_32 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[arch_interface.h](arch__interface_8h.md)>`

Obtain the current cycle count, in units specified by CONFIG\_SYS\_CLOCK\_HW\_CYCLES\_PER\_SEC.

While this is historically specified as part of the architecture API, in practice virtually all platforms forward it to the [sys\_clock\_cycle\_get\_32()](arc_2v2_2misc_8h.md#a42dcd1878309a82246dbfa26510f868a) API provided by the timer driver.

See also
:   [k\_cycle\_get\_32()](group__clock__apis.md#ga208687de625e0036558343b4e66143d3 "Read the hardware clock.")

Returns
:   The current cycle time. This should count up monotonically through the full 32 bit space, wrapping at 0xffffffff. Hardware with fewer bits of precision in the timer is expected to synthesize a 32 bit count.

## [◆ ](#gacc1ed8d949f694a1d39e389334caf971)arch\_k\_cycle\_get\_64()

| | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) arch\_k\_cycle\_get\_64 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[arch_interface.h](arch__interface_8h.md)>`

As for [arch\_k\_cycle\_get\_32()](#ga9ee9f897ec750957de45bf8d43349d5e), but with a 64 bit return value.

Not all timer hardware has a 64 bit timer, this needs to be implemented only if CONFIG\_TIMER\_HAS\_64BIT\_CYCLE\_COUNTER is set.

See also
:   [arch\_k\_cycle\_get\_32()](#ga9ee9f897ec750957de45bf8d43349d5e)

Returns
:   The current cycle time. This should count up monotonically through the full 64 bit space, wrapping at 2^64-1. Hardware with fewer bits of precision in the timer is generally not expected to implement this API.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
