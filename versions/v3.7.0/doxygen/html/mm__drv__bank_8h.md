---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/mm__drv__bank_8h.html
original_path: doxygen/html/mm__drv__bank_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mm\_drv\_bank.h File Reference

Memory Banks Driver APIs.
[More...](#details)

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/sys/mem_stats.h](mem__stats_8h_source.md)>`  
`#include <[stdint.h](stdint_8h_source.md)>`

[Go to the source code of this file.](mm__drv__bank_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [sys\_mm\_drv\_bank](structsys__mm__drv__bank.md) |
|  | Information about memory banks. [More...](structsys__mm__drv__bank.md#details) |

| Functions | |
| --- | --- |
| void | [sys\_mm\_drv\_bank\_init](group__mm__drv__bank__apis.md#gad8f2956ec2346812977abf91506911fb) (struct [sys\_mm\_drv\_bank](structsys__mm__drv__bank.md) \*bank, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bank\_pages) |
|  | Initialize a memory bank's data structure. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sys\_mm\_drv\_bank\_page\_mapped](group__mm__drv__bank__apis.md#ga24f5119ac69d07bdba20fbfb2427939f) (struct [sys\_mm\_drv\_bank](structsys__mm__drv__bank.md) \*bank) |
|  | Track the mapping of a page in the specified memory bank. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sys\_mm\_drv\_bank\_page\_unmapped](group__mm__drv__bank__apis.md#gac1afd8ab934ce15f77de9d3f113cfa43) (struct [sys\_mm\_drv\_bank](structsys__mm__drv__bank.md) \*bank) |
|  | Track the unmapping of a page in the specified memory bank. |
| void | [sys\_mm\_drv\_bank\_stats\_reset\_max](group__mm__drv__bank__apis.md#ga55404378ab66ef3393e652a57eacc881) (struct [sys\_mm\_drv\_bank](structsys__mm__drv__bank.md) \*bank) |
|  | Reset the max number of pages mapped in the bank. |
| void | [sys\_mm\_drv\_bank\_stats\_get](group__mm__drv__bank__apis.md#gaa0ae8be368233f6dfd88a54ae7ae1db0) (struct [sys\_mm\_drv\_bank](structsys__mm__drv__bank.md) \*bank, struct [sys\_memory\_stats](structsys__memory__stats.md) \*stats) |
|  | Retrieve the memory usage stats for the specified memory bank. |

## Detailed Description

Memory Banks Driver APIs.

This contains generic APIs to be used by a system-wide memory management driver to track page usage within memory banks.

Note
:   The caller of these functions needs to ensure proper locking to protect the data when using these APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mm](dir_464cfbc388e9245b11da9b89dd2be842.md)
- [mm\_drv\_bank.h](mm__drv__bank_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
