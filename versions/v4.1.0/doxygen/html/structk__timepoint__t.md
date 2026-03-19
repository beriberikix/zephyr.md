---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structk__timepoint__t.html
original_path: doxygen/html/structk__timepoint__t.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

k\_timepoint\_t Struct Reference

[Kernel APIs](group__kernel__apis.md) » [System Clock APIs](group__clock__apis.md)

Kernel timepoint type.
[More...](#details)

`#include <[sys_clock.h](sys__clock_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [tick](#a33e68c86f68dad539d7c2a70e6f80fbe) |

## Detailed Description

Kernel timepoint type.

Absolute timepoints are stored in this opaque type. It is best not to inspect its content directly.

See also
:   [sys\_timepoint\_calc()](group__clock__apis.md#ga509cf4599c1f162c97540743e8c21d33 "Calculate a timepoint value.")
:   [sys\_timepoint\_timeout()](group__clock__apis.md#ga6f6d06ef8c13e2fa54c63831fc00ecaa "Remaining time to given timepoint.")
:   [sys\_timepoint\_expired()](group__clock__apis.md#ga87d0d7a0f7bcdcc8c4909962eac12985 "Indicates if timepoint is expired.")

## Field Documentation

## [◆ ](#a33e68c86f68dad539d7c2a70e6f80fbe)tick

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) k\_timepoint\_t::tick |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/[sys\_clock.h](sys__clock_8h_source.md)

- [k\_timepoint\_t](structk__timepoint__t.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
