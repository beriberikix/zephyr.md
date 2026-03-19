---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/zephyr__basic_8h_source.html
original_path: doxygen/html/zephyr__basic_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

zephyr\_basic.h

[Go to the documentation of this file.](zephyr__basic_8h.md)

1/\*

2 \* Copyright (c) 2021-2023 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_ZEPHYR\_MCUMGR\_GRP\_ZBASIC\_H\_

7#define ZEPHYR\_INCLUDE\_ZEPHYR\_MCUMGR\_GRP\_ZBASIC\_H\_

8

9#ifdef \_\_cplusplus

10extern "C" {

11#endif

12

[ 16](zephyr__basic_8h.md#a335d87c4927506ef1e5a52e3ae2b23d2)#define ZEPHYR\_MGMT\_GRP\_BASIC\_CMD\_ERASE\_STORAGE 0 /\* Command to erase storage partition \*/

17

[ 21](zephyr__basic_8h.md#ab466c726d85f3289b3a064d64169914c)enum [zephyr\_basic\_group\_err\_code\_t](zephyr__basic_8h.md#ab466c726d85f3289b3a064d64169914c) {

[ 23](zephyr__basic_8h.md#ab466c726d85f3289b3a064d64169914ca702e02a1122d1c119bf75a41f55e2681) [ZEPHYRBASIC\_MGMT\_ERR\_OK](zephyr__basic_8h.md#ab466c726d85f3289b3a064d64169914ca702e02a1122d1c119bf75a41f55e2681) = 0,

24

[ 26](zephyr__basic_8h.md#ab466c726d85f3289b3a064d64169914ca216aefbd7a6da787225bcb18c26e41d2) [ZEPHYRBASIC\_MGMT\_ERR\_UNKNOWN](zephyr__basic_8h.md#ab466c726d85f3289b3a064d64169914ca216aefbd7a6da787225bcb18c26e41d2),

27

[ 29](zephyr__basic_8h.md#ab466c726d85f3289b3a064d64169914cadf1c7bf6b4b8aa33c5b2669449200362) [ZEPHYRBASIC\_MGMT\_ERR\_FLASH\_OPEN\_FAILED](zephyr__basic_8h.md#ab466c726d85f3289b3a064d64169914cadf1c7bf6b4b8aa33c5b2669449200362),

30

[ 32](zephyr__basic_8h.md#ab466c726d85f3289b3a064d64169914ca7d6e0c3f222a93811317e1ba6809e53f) [ZEPHYRBASIC\_MGMT\_ERR\_FLASH\_CONFIG\_QUERY\_FAIL](zephyr__basic_8h.md#ab466c726d85f3289b3a064d64169914ca7d6e0c3f222a93811317e1ba6809e53f),

33

[ 35](zephyr__basic_8h.md#ab466c726d85f3289b3a064d64169914caa2abbcccf19a206dd04938d66ae21646) [ZEPHYRBASIC\_MGMT\_ERR\_FLASH\_ERASE\_FAILED](zephyr__basic_8h.md#ab466c726d85f3289b3a064d64169914caa2abbcccf19a206dd04938d66ae21646),

36};

37

38#ifdef \_\_cplusplus

39}

40#endif

41

42#endif /\* ZEPHYR\_INCLUDE\_ZEPHYR\_MCUMGR\_GRP\_ZBASIC\_H\_ \*/

[zephyr\_basic\_group\_err\_code\_t](zephyr__basic_8h.md#ab466c726d85f3289b3a064d64169914c)

zephyr\_basic\_group\_err\_code\_t

Command result codes for statistics management group.

**Definition** zephyr\_basic.h:21

[ZEPHYRBASIC\_MGMT\_ERR\_UNKNOWN](zephyr__basic_8h.md#ab466c726d85f3289b3a064d64169914ca216aefbd7a6da787225bcb18c26e41d2)

@ ZEPHYRBASIC\_MGMT\_ERR\_UNKNOWN

Unknown error occurred.

**Definition** zephyr\_basic.h:26

[ZEPHYRBASIC\_MGMT\_ERR\_OK](zephyr__basic_8h.md#ab466c726d85f3289b3a064d64169914ca702e02a1122d1c119bf75a41f55e2681)

@ ZEPHYRBASIC\_MGMT\_ERR\_OK

No error, this is implied if there is no ret value in the response.

**Definition** zephyr\_basic.h:23

[ZEPHYRBASIC\_MGMT\_ERR\_FLASH\_CONFIG\_QUERY\_FAIL](zephyr__basic_8h.md#ab466c726d85f3289b3a064d64169914ca7d6e0c3f222a93811317e1ba6809e53f)

@ ZEPHYRBASIC\_MGMT\_ERR\_FLASH\_CONFIG\_QUERY\_FAIL

Querying the flash area parameters has failed.

**Definition** zephyr\_basic.h:32

[ZEPHYRBASIC\_MGMT\_ERR\_FLASH\_ERASE\_FAILED](zephyr__basic_8h.md#ab466c726d85f3289b3a064d64169914caa2abbcccf19a206dd04938d66ae21646)

@ ZEPHYRBASIC\_MGMT\_ERR\_FLASH\_ERASE\_FAILED

Erasing the flash area has failed.

**Definition** zephyr\_basic.h:35

[ZEPHYRBASIC\_MGMT\_ERR\_FLASH\_OPEN\_FAILED](zephyr__basic_8h.md#ab466c726d85f3289b3a064d64169914cadf1c7bf6b4b8aa33c5b2669449200362)

@ ZEPHYRBASIC\_MGMT\_ERR\_FLASH\_OPEN\_FAILED

Opening of the flash area has failed.

**Definition** zephyr\_basic.h:29

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [grp](dir_75a5d043a2b1048bf3665f6cb87645f5.md)
- [zephyr](dir_9b96e56ee9a524e0ef9971c4556f53ad.md)
- [zephyr\_basic.h](zephyr__basic_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
