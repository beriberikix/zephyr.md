---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__pcie__vc__host__interface.html
original_path: doxygen/html/group__pcie__vc__host__interface.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

PCIe Virtual Channel Host Interface

[Device Driver APIs](group__io__interfaces.md) » [PCIe Host Interface](group__pcie__host__interface.md)

PCIe Virtual Channel Host Interface.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [pcie\_vctc\_map](structpcie__vctc__map.md) |

| Macros | |
| --- | --- |
| #define | [PCIE\_VC\_MAX\_COUNT](#ga0567fabc02828372f4e901bb193c9b89)   8U |
| #define | [PCIE\_VC\_SET\_TC0](#gae1ec2ec11736ed97c6e41a2d8c7f4a39)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [PCIE\_VC\_SET\_TC1](#gab4d53cac004ac7b6258fbd387fc90051)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [PCIE\_VC\_SET\_TC2](#ga3d0311d99240527d86e8f8452f405736)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [PCIE\_VC\_SET\_TC3](#ga3122990fd5879e076346efdc706b640e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [PCIE\_VC\_SET\_TC4](#ga2259546ee27ce43dfb15ea69bdb66a7c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| #define | [PCIE\_VC\_SET\_TC5](#ga9a796b9570585c60c70fb641e0a5a733)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| #define | [PCIE\_VC\_SET\_TC6](#gaf8ff3086a4a5003f303f7b17e2319c09)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| #define | [PCIE\_VC\_SET\_TC7](#gacbd9b1877530539d1a14a35d35744634)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |

| Functions | |
| --- | --- |
| int | [pcie\_vc\_enable](#ga179628024fc9d651d1027833377ee9d2) ([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf) |
|  | Enable PCIe Virtual Channel handling. |
| int | [pcie\_vc\_disable](#ga89c684f7ff5e82da86df27d061a8fbd7) ([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf) |
|  | Disable PCIe Virtual Channel handling. |
| int | [pcie\_vc\_map\_tc](#gafd4429e8c14821c685c4103f34b340c8) ([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, struct [pcie\_vctc\_map](structpcie__vctc__map.md) \*map) |
|  | Map PCIe TC/VC. |

## Detailed Description

PCIe Virtual Channel Host Interface.

## Macro Definition Documentation

## [◆ ](#ga0567fabc02828372f4e901bb193c9b89)PCIE\_VC\_MAX\_COUNT

| #define PCIE\_VC\_MAX\_COUNT   8U |
| --- |

`#include <[vc.h](vc_8h.md)>`

## [◆ ](#gae1ec2ec11736ed97c6e41a2d8c7f4a39)PCIE\_VC\_SET\_TC0

| #define PCIE\_VC\_SET\_TC0   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[vc.h](vc_8h.md)>`

## [◆ ](#gab4d53cac004ac7b6258fbd387fc90051)PCIE\_VC\_SET\_TC1

| #define PCIE\_VC\_SET\_TC1   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[vc.h](vc_8h.md)>`

## [◆ ](#ga3d0311d99240527d86e8f8452f405736)PCIE\_VC\_SET\_TC2

| #define PCIE\_VC\_SET\_TC2   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

`#include <[vc.h](vc_8h.md)>`

## [◆ ](#ga3122990fd5879e076346efdc706b640e)PCIE\_VC\_SET\_TC3

| #define PCIE\_VC\_SET\_TC3   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

`#include <[vc.h](vc_8h.md)>`

## [◆ ](#ga2259546ee27ce43dfb15ea69bdb66a7c)PCIE\_VC\_SET\_TC4

| #define PCIE\_VC\_SET\_TC4   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

`#include <[vc.h](vc_8h.md)>`

## [◆ ](#ga9a796b9570585c60c70fb641e0a5a733)PCIE\_VC\_SET\_TC5

| #define PCIE\_VC\_SET\_TC5   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

`#include <[vc.h](vc_8h.md)>`

## [◆ ](#gaf8ff3086a4a5003f303f7b17e2319c09)PCIE\_VC\_SET\_TC6

| #define PCIE\_VC\_SET\_TC6   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

`#include <[vc.h](vc_8h.md)>`

## [◆ ](#gacbd9b1877530539d1a14a35d35744634)PCIE\_VC\_SET\_TC7

| #define PCIE\_VC\_SET\_TC7   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

`#include <[vc.h](vc_8h.md)>`

## Function Documentation

## [◆ ](#ga89c684f7ff5e82da86df27d061a8fbd7)pcie\_vc\_disable()

| int pcie\_vc\_disable | ( | [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) | *bdf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[vc.h](vc_8h.md)>`

Disable PCIe Virtual Channel handling.

Parameters
:   | bdf | the target PCI endpoint |
    | --- | --- |

Returns
:   0 on success, a negative error code otherwise

## [◆ ](#ga179628024fc9d651d1027833377ee9d2)pcie\_vc\_enable()

| int pcie\_vc\_enable | ( | [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) | *bdf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[vc.h](vc_8h.md)>`

Enable PCIe Virtual Channel handling.

Parameters
:   | bdf | the target PCI endpoint |
    | --- | --- |

Returns
:   0 on success, a negative error code otherwise

Note: Not being able to enable such feature is a non-fatal error and any code using it should behave accordingly (displaying some info, and ignoring it for instance).

## [◆ ](#gafd4429e8c14821c685c4103f34b340c8)pcie\_vc\_map\_tc()

| int pcie\_vc\_map\_tc | ( | [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) | *bdf*, |
| --- | --- | --- | --- |
|  |  | struct [pcie\_vctc\_map](structpcie__vctc__map.md) \* | *map* ) |

`#include <[vc.h](vc_8h.md)>`

Map PCIe TC/VC.

Parameters
:   | bdf | the target PCI endpoint |
    | --- | --- |
    | map | the tc/vc map to apply |

Returns
:   0 on success, a negative error code otherwise

Note: VC must be disabled prior to call this function and enabled afterward in order for the endpoint to take advandage of the map.

Note: Not being able to enable such feature is a non-fatal error and any code using it should behave accordingly (displaying some info, and ignoring it for instance).

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
