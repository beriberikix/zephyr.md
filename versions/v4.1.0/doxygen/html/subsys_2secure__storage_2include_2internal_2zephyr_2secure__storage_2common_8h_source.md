---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2common_8h_source.html
original_path: doxygen/html/subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2common_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

common.h

[Go to the documentation of this file.](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2common_8h.md)

1/\* Copyright (c) 2024 Nordic Semiconductor

2 \* SPDX-License-Identifier: Apache-2.0

3 \*/

4#ifndef SECURE\_STORAGE\_COMMON\_H

5#define SECURE\_STORAGE\_COMMON\_H

6

8#include <[stdint.h](stdint_8h.md)>

9

10/\* A size-optimized version of `psa\_storage\_create\_flags\_t`. Used for storing the `create\_flags`. \*/

[ 11](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2common_8h.md#ac3c7c0ba918fe964b4c39ae0d8047bdd)typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [secure\_storage\_packed\_create\_flags\_t](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2common_8h.md#ac3c7c0ba918fe964b4c39ae0d8047bdd);

12

[ 13](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2common_8h.md#ae07ad04cdb4e399b0751f58415d5e514)#define SECURE\_STORAGE\_ALL\_CREATE\_FLAGS \

14 (PSA\_STORAGE\_FLAG\_NONE | \

15 PSA\_STORAGE\_FLAG\_WRITE\_ONCE | \

16 PSA\_STORAGE\_FLAG\_NO\_CONFIDENTIALITY | \

17 PSA\_STORAGE\_FLAG\_NO\_REPLAY\_PROTECTION)

18

19#endif

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[secure\_storage\_packed\_create\_flags\_t](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2common_8h.md#ac3c7c0ba918fe964b4c39ae0d8047bdd)

uint8\_t secure\_storage\_packed\_create\_flags\_t

**Definition** common.h:11

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [secure\_storage](dir_5fedd937c27a983db9815c43dc43c138.md)
- [include](dir_3887dba27d172300e5fca4cbd714c7ed.md)
- [internal](dir_49025992370a830d8c3dd47cf1bb57bb.md)
- [zephyr](dir_29af7cd685f88a83c3e1809490f18587.md)
- [secure\_storage](dir_b251feb5349caf21c27bf417dfd4e083.md)
- [common.h](subsys_2secure__storage_2include_2internal_2zephyr_2secure__storage_2common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
