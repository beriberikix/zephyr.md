---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/os__mgmt__callbacks_8h_source.html
original_path: doxygen/html/os__mgmt__callbacks_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

os\_mgmt\_callbacks.h

[Go to the documentation of this file.](os__mgmt__callbacks_8h.md)

1/\*

2 \* Copyright (c) 2023 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef H\_MCUMGR\_OS\_MGMT\_CALLBACKS\_

8#define H\_MCUMGR\_OS\_MGMT\_CALLBACKS\_

9

10#ifdef \_\_cplusplus

11extern "C" {

12#endif

13

20

[ 26](structos__mgmt__reset__data.md)struct [os\_mgmt\_reset\_data](structos__mgmt__reset__data.md) {

[ 28](structos__mgmt__reset__data.md#aa9defc41c1e9aff601b5c98cb307bc01) bool [force](structos__mgmt__reset__data.md#aa9defc41c1e9aff601b5c98cb307bc01);

29};

30

34

35#ifdef \_\_cplusplus

36}

37#endif

38

39#endif

[os\_mgmt\_reset\_data](structos__mgmt__reset__data.md)

Structure provided in the MGMT\_EVT\_OP\_OS\_MGMT\_RESET notification callback: This callback function is ...

**Definition** os\_mgmt\_callbacks.h:26

[os\_mgmt\_reset\_data::force](structos__mgmt__reset__data.md#aa9defc41c1e9aff601b5c98cb307bc01)

bool force

Contains the value of the force parameter.

**Definition** os\_mgmt\_callbacks.h:28

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [grp](dir_75a5d043a2b1048bf3665f6cb87645f5.md)
- [os\_mgmt](dir_1a5ff9dfdb0e06a8ce3ba8e3db8b26fb.md)
- [os\_mgmt\_callbacks.h](os__mgmt__callbacks_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
