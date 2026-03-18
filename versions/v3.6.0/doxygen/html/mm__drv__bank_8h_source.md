---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/mm__drv__bank_8h_source.html
original_path: doxygen/html/mm__drv__bank_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mm\_drv\_bank.h

[Go to the documentation of this file.](mm__drv__bank_8h.md)

1/\*

2 \* Copyright (c) 2023 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

17

18#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_MM\_DRV\_BANK\_H

19#define ZEPHYR\_INCLUDE\_DRIVERS\_MM\_DRV\_BANK\_H

20

21#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

22#include <[zephyr/sys/mem\_stats.h](mem__stats_8h.md)>

23#include <[stdint.h](stdint_8h.md)>

24

38

[ 42](structsys__mm__drv__bank.md)struct [sys\_mm\_drv\_bank](structsys__mm__drv__bank.md) {

[ 44](structsys__mm__drv__bank.md#a8fd91db4f69c273b2d26bb770292cd83) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [unmapped\_pages](structsys__mm__drv__bank.md#a8fd91db4f69c273b2d26bb770292cd83);

45

[ 47](structsys__mm__drv__bank.md#a2e84b41e42b801825aa694e569e8ad6c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [mapped\_pages](structsys__mm__drv__bank.md#a2e84b41e42b801825aa694e569e8ad6c);

48

[ 50](structsys__mm__drv__bank.md#a69f4b9f6a7fed6403e7271a4ecbe5ad1) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [max\_mapped\_pages](structsys__mm__drv__bank.md#a69f4b9f6a7fed6403e7271a4ecbe5ad1);

51};

52

[ 65](group__mm__drv__bank__apis.md#gad8f2956ec2346812977abf91506911fb)void [sys\_mm\_drv\_bank\_init](group__mm__drv__bank__apis.md#gad8f2956ec2346812977abf91506911fb)(struct [sys\_mm\_drv\_bank](structsys__mm__drv__bank.md) \*bank, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bank\_pages);

66

[ 77](group__mm__drv__bank__apis.md#ga24f5119ac69d07bdba20fbfb2427939f)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sys\_mm\_drv\_bank\_page\_mapped](group__mm__drv__bank__apis.md#ga24f5119ac69d07bdba20fbfb2427939f)(struct [sys\_mm\_drv\_bank](structsys__mm__drv__bank.md) \*bank);

78

[ 89](group__mm__drv__bank__apis.md#gac1afd8ab934ce15f77de9d3f113cfa43)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sys\_mm\_drv\_bank\_page\_unmapped](group__mm__drv__bank__apis.md#gac1afd8ab934ce15f77de9d3f113cfa43)(struct [sys\_mm\_drv\_bank](structsys__mm__drv__bank.md) \*bank);

90

[ 100](group__mm__drv__bank__apis.md#ga55404378ab66ef3393e652a57eacc881)void [sys\_mm\_drv\_bank\_stats\_reset\_max](group__mm__drv__bank__apis.md#ga55404378ab66ef3393e652a57eacc881)(struct [sys\_mm\_drv\_bank](structsys__mm__drv__bank.md) \*bank);

101

[ 110](group__mm__drv__bank__apis.md#gaa0ae8be368233f6dfd88a54ae7ae1db0)void [sys\_mm\_drv\_bank\_stats\_get](group__mm__drv__bank__apis.md#gaa0ae8be368233f6dfd88a54ae7ae1db0)(struct [sys\_mm\_drv\_bank](structsys__mm__drv__bank.md) \*bank,

111 struct [sys\_memory\_stats](structsys__memory__stats.md) \*stats);

112

116

117#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_MM\_DRV\_BANK\_H \*/

[sys\_mm\_drv\_bank\_page\_mapped](group__mm__drv__bank__apis.md#ga24f5119ac69d07bdba20fbfb2427939f)

uint32\_t sys\_mm\_drv\_bank\_page\_mapped(struct sys\_mm\_drv\_bank \*bank)

Track the mapping of a page in the specified memory bank.

[sys\_mm\_drv\_bank\_stats\_reset\_max](group__mm__drv__bank__apis.md#ga55404378ab66ef3393e652a57eacc881)

void sys\_mm\_drv\_bank\_stats\_reset\_max(struct sys\_mm\_drv\_bank \*bank)

Reset the max number of pages mapped in the bank.

[sys\_mm\_drv\_bank\_stats\_get](group__mm__drv__bank__apis.md#gaa0ae8be368233f6dfd88a54ae7ae1db0)

void sys\_mm\_drv\_bank\_stats\_get(struct sys\_mm\_drv\_bank \*bank, struct sys\_memory\_stats \*stats)

Retrieve the memory usage stats for the specified memory bank.

[sys\_mm\_drv\_bank\_page\_unmapped](group__mm__drv__bank__apis.md#gac1afd8ab934ce15f77de9d3f113cfa43)

uint32\_t sys\_mm\_drv\_bank\_page\_unmapped(struct sys\_mm\_drv\_bank \*bank)

Track the unmapping of a page in the specified memory bank.

[sys\_mm\_drv\_bank\_init](group__mm__drv__bank__apis.md#gad8f2956ec2346812977abf91506911fb)

void sys\_mm\_drv\_bank\_init(struct sys\_mm\_drv\_bank \*bank, uint32\_t bank\_pages)

Initialize a memory bank's data structure.

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[mem\_stats.h](mem__stats_8h.md)

Memory Statistics.

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[sys\_memory\_stats](structsys__memory__stats.md)

**Definition** mem\_stats.h:24

[sys\_mm\_drv\_bank](structsys__mm__drv__bank.md)

Information about memory banks.

**Definition** mm\_drv\_bank.h:42

[sys\_mm\_drv\_bank::mapped\_pages](structsys__mm__drv__bank.md#a2e84b41e42b801825aa694e569e8ad6c)

uint32\_t mapped\_pages

Number of mapped pages.

**Definition** mm\_drv\_bank.h:47

[sys\_mm\_drv\_bank::max\_mapped\_pages](structsys__mm__drv__bank.md#a69f4b9f6a7fed6403e7271a4ecbe5ad1)

uint32\_t max\_mapped\_pages

Maximum number of mapped pages since last counter reset.

**Definition** mm\_drv\_bank.h:50

[sys\_mm\_drv\_bank::unmapped\_pages](structsys__mm__drv__bank.md#a8fd91db4f69c273b2d26bb770292cd83)

uint32\_t unmapped\_pages

Number of unmapped pages.

**Definition** mm\_drv\_bank.h:44

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mm](dir_464cfbc388e9245b11da9b89dd2be842.md)
- [mm\_drv\_bank.h](mm__drv__bank_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
