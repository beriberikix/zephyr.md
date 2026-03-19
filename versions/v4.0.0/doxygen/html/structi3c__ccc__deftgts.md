---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structi3c__ccc__deftgts.html
original_path: doxygen/html/structi3c__ccc__deftgts.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i3c\_ccc\_deftgts Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [I3C Interface](group__i3c__interface.md) » [I3C Common Command Codes](group__i3c__ccc.md)

Payload for DEFTGTS CCC (Define List of Targets).
[More...](#details)

`#include <[ccc.h](ccc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [count](#a82a12e711417111855d76171fbd008c2) |
|  | Number of Targets (and Groups) present on the I3C Bus. |
| struct [i3c\_ccc\_deftgts\_active\_controller](structi3c__ccc__deftgts__active__controller.md) | [active\_controller](#a1f59c280bd388eb7e7818eb674b5f12f) |
|  | Data describing the active controller. |
| struct [i3c\_ccc\_deftgts\_target](structi3c__ccc__deftgts__target.md) | [targets](#a3ead83f46d63c4dd4723ef76dba770ee) [] |
|  | Data describing the target(s) on the bus. |

## Detailed Description

Payload for DEFTGTS CCC (Define List of Targets).

Note
:   `[i3c_ccc_deftgts_target](structi3c__ccc__deftgts__target.md "The target device part of payload for DEFTGTS CCC.")` is an array of targets, where the number of elements is dependent on the number of I3C targets on the bus. Please have enough space for both read and write of this CCC.

## Field Documentation

## [◆ ](#a1f59c280bd388eb7e7818eb674b5f12f)active\_controller

| struct [i3c\_ccc\_deftgts\_active\_controller](structi3c__ccc__deftgts__active__controller.md) i3c\_ccc\_deftgts::active\_controller |
| --- |

Data describing the active controller.

## [◆ ](#a82a12e711417111855d76171fbd008c2)count

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_ccc\_deftgts::count |
| --- |

Number of Targets (and Groups) present on the I3C Bus.

## [◆ ](#a3ead83f46d63c4dd4723ef76dba770ee)targets

| struct [i3c\_ccc\_deftgts\_target](structi3c__ccc__deftgts__target.md) i3c\_ccc\_deftgts::targets[] |
| --- |

Data describing the target(s) on the bus.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/i3c/[ccc.h](ccc_8h_source.md)

- [i3c\_ccc\_deftgts](structi3c__ccc__deftgts.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
