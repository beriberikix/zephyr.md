---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__mdf__interface__bd8lb600fs.html
original_path: doxygen/html/group__mdf__interface__bd8lb600fs.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

MFD BD8LB600FS interface

[Device Driver APIs](group__io__interfaces.md) » [Multi Function Device Drivers APIs](group__mfd__interfaces.md)

| Functions | |
| --- | --- |
| int | [mfd\_bd8lb600fs\_set\_outputs](#gaf155a458b77540f991d53c0827fad5cd) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) values) |
|  | set outputs |
| int | [mfd\_bd8lb600fs\_get\_output\_diagnostics](#ga478f99d83f78a0ec0fcabeb3103df015) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*old, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*ocp\_or\_tsd) |
|  | get output diagnostics |

## Detailed Description

## Function Documentation

## [◆ ](#ga478f99d83f78a0ec0fcabeb3103df015)mfd\_bd8lb600fs\_get\_output\_diagnostics()

| int mfd\_bd8lb600fs\_get\_output\_diagnostics | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *old*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *ocp\_or\_tsd* ) |

`#include <[bd8lb600fs.h](mfd_2bd8lb600fs_8h.md)>`

get output diagnostics

Fetch the current diagnostics from all instances, as multiple instances might be daisy chained together. Each bit in old and ocp\_or\_tsd corresponds to one output. A set bit means that the function is active, therefore either there is an open load, an over current or a too high temperature.

OLD - open load OCP - over current protection TSD - thermal shutdown

Parameters
:   | [in] | dev | instance of BD8LB600FS MFD |
    | --- | --- | --- |
    | [out] | old | open load values |
    | [out] | ocp\_or\_tsd | over current protection or thermal shutdown values |

Return values
:   | 0 | if successful |
    | --- | --- |

## [◆ ](#gaf155a458b77540f991d53c0827fad5cd)mfd\_bd8lb600fs\_set\_outputs()

| int mfd\_bd8lb600fs\_set\_outputs | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *values* ) |

`#include <[bd8lb600fs.h](mfd_2bd8lb600fs_8h.md)>`

set outputs

Parameters
:   | [in] | dev | instance of BD8LB600FS MFD |
    | --- | --- | --- |
    | [in] | values | values for outputs, one bit per output |

Return values
:   | 0 | if successful |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
