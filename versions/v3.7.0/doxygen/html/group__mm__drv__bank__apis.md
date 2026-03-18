---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__mm__drv__bank__apis.html
original_path: doxygen/html/group__mm__drv__bank__apis.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Memory Banks Driver APIs

[Operating System Services](group__os__services.md) » [Memory Management](group__memory__management.md)

Memory Banks Driver APIs.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [sys\_mm\_drv\_bank](structsys__mm__drv__bank.md) |
|  | Information about memory banks. [More...](structsys__mm__drv__bank.md#details) |

| Functions | |
| --- | --- |
| void | [sys\_mm\_drv\_bank\_init](#gad8f2956ec2346812977abf91506911fb) (struct [sys\_mm\_drv\_bank](structsys__mm__drv__bank.md) \*bank, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bank\_pages) |
|  | Initialize a memory bank's data structure. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sys\_mm\_drv\_bank\_page\_mapped](#ga24f5119ac69d07bdba20fbfb2427939f) (struct [sys\_mm\_drv\_bank](structsys__mm__drv__bank.md) \*bank) |
|  | Track the mapping of a page in the specified memory bank. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sys\_mm\_drv\_bank\_page\_unmapped](#gac1afd8ab934ce15f77de9d3f113cfa43) (struct [sys\_mm\_drv\_bank](structsys__mm__drv__bank.md) \*bank) |
|  | Track the unmapping of a page in the specified memory bank. |
| void | [sys\_mm\_drv\_bank\_stats\_reset\_max](#ga55404378ab66ef3393e652a57eacc881) (struct [sys\_mm\_drv\_bank](structsys__mm__drv__bank.md) \*bank) |
|  | Reset the max number of pages mapped in the bank. |
| void | [sys\_mm\_drv\_bank\_stats\_get](#gaa0ae8be368233f6dfd88a54ae7ae1db0) (struct [sys\_mm\_drv\_bank](structsys__mm__drv__bank.md) \*bank, struct [sys\_memory\_stats](structsys__memory__stats.md) \*stats) |
|  | Retrieve the memory usage stats for the specified memory bank. |

## Detailed Description

Memory Banks Driver APIs.

This contains APIs for a system-wide memory management driver to track page usage within memory banks.

Note
:   The caller of these functions needs to ensure proper locking to protect the data when using these APIs.

## Function Documentation

## [◆ ](#gad8f2956ec2346812977abf91506911fb)sys\_mm\_drv\_bank\_init()

| void sys\_mm\_drv\_bank\_init | ( | struct [sys\_mm\_drv\_bank](structsys__mm__drv__bank.md) \* | *bank*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *bank\_pages* ) |

`#include <[mm_drv_bank.h](mm__drv__bank_8h.md)>`

Initialize a memory bank's data structure.

The driver may wish to track various information about the memory banks that it uses. This routine will initialize a generic structure containing that information. Since at the power on all memory banks are switched on it will start with all pages mapped. In next phase of driver initialization unused pages will be unmapped.

Parameters
:   | [in,out] | bank | Pointer to the memory bank structure used for tracking |
    | --- | --- | --- |
    | [in] | bank\_pages | Number of pages in the memory bank |

## [◆ ](#ga24f5119ac69d07bdba20fbfb2427939f)sys\_mm\_drv\_bank\_page\_mapped()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sys\_mm\_drv\_bank\_page\_mapped | ( | struct [sys\_mm\_drv\_bank](structsys__mm__drv__bank.md) \* | *bank* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mm_drv_bank.h](mm__drv__bank_8h.md)>`

Track the mapping of a page in the specified memory bank.

This function is used to update the number of mapped pages within the specified memory bank.

Parameters
:   | [in,out] | bank | Pointer to the memory bank's data structure |
    | --- | --- | --- |

Returns
:   The number of pages mapped within the memory bank

## [◆ ](#gac1afd8ab934ce15f77de9d3f113cfa43)sys\_mm\_drv\_bank\_page\_unmapped()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sys\_mm\_drv\_bank\_page\_unmapped | ( | struct [sys\_mm\_drv\_bank](structsys__mm__drv__bank.md) \* | *bank* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mm_drv_bank.h](mm__drv__bank_8h.md)>`

Track the unmapping of a page in the specified memory bank.

This function is used to update the number of unmapped pages within the specified memory bank.

Parameters
:   | [in,out] | bank | Pointer to the memory bank's data structure |
    | --- | --- | --- |

Returns
:   The number of unmapped pages within the memory bank

## [◆ ](#gaa0ae8be368233f6dfd88a54ae7ae1db0)sys\_mm\_drv\_bank\_stats\_get()

| void sys\_mm\_drv\_bank\_stats\_get | ( | struct [sys\_mm\_drv\_bank](structsys__mm__drv__bank.md) \* | *bank*, |
| --- | --- | --- | --- |
|  |  | struct [sys\_memory\_stats](structsys__memory__stats.md) \* | *stats* ) |

`#include <[mm_drv_bank.h](mm__drv__bank_8h.md)>`

Retrieve the memory usage stats for the specified memory bank.

This routine extracts the system memory stats from the memory bank.

Parameters
:   | [in] | bank | Pointer to the memory bank's data structure |
    | --- | --- | --- |
    | [in,out] | stats | Pointer to memory into which to copy the system memory stats |

## [◆ ](#ga55404378ab66ef3393e652a57eacc881)sys\_mm\_drv\_bank\_stats\_reset\_max()

| void sys\_mm\_drv\_bank\_stats\_reset\_max | ( | struct [sys\_mm\_drv\_bank](structsys__mm__drv__bank.md) \* | *bank* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mm_drv_bank.h](mm__drv__bank_8h.md)>`

Reset the max number of pages mapped in the bank.

This routine is used to reset the maximum number of pages mapped in the specified memory bank to the current number of pages mapped in that memory bank.

Parameters
:   | [in,out] | bank | Pointer to the memory bank's data structure |
    | --- | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
