---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/enum__mgmt__callbacks_8h_source.html
original_path: doxygen/html/enum__mgmt__callbacks_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

enum\_mgmt\_callbacks.h

[Go to the documentation of this file.](enum__mgmt__callbacks_8h.md)

1/\*

2 \* Copyright (c) 2024 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef H\_MCUMGR\_ENUM\_MGMT\_CALLBACKS\_

8#define H\_MCUMGR\_ENUM\_MGMT\_CALLBACKS\_

9

10#ifdef \_\_cplusplus

11extern "C" {

12#endif

13

20

[ 26](structenum__mgmt__detail__output.md)struct [enum\_mgmt\_detail\_output](structenum__mgmt__detail__output.md) {

[ 28](structenum__mgmt__detail__output.md#a787c1a41fbe135b85176d3b0bb6ccd92) const struct [mgmt\_group](structmgmt__group.md) \*[group](structenum__mgmt__detail__output.md#a787c1a41fbe135b85176d3b0bb6ccd92);

29

[ 34](structenum__mgmt__detail__output.md#a140d1f5cd4e4f7a88c5a1da98a927161) zcbor\_state\_t \*[zse](structenum__mgmt__detail__output.md#a140d1f5cd4e4f7a88c5a1da98a927161);

35};

36

40

41#ifdef \_\_cplusplus

42}

43#endif

44

45#endif

[enum\_mgmt\_detail\_output](structenum__mgmt__detail__output.md)

Structure provided in the MGMT\_EVT\_OP\_ENUM\_MGMT\_DETAILS notification callback: This callback function...

**Definition** enum\_mgmt\_callbacks.h:26

[enum\_mgmt\_detail\_output::zse](structenum__mgmt__detail__output.md#a140d1f5cd4e4f7a88c5a1da98a927161)

zcbor\_state\_t \* zse

The zcbor encoder which is currently being used to output group information, additional fields to the...

**Definition** enum\_mgmt\_callbacks.h:34

[enum\_mgmt\_detail\_output::group](structenum__mgmt__detail__output.md#a787c1a41fbe135b85176d3b0bb6ccd92)

const struct mgmt\_group \* group

The group that is currently being enumerated.

**Definition** enum\_mgmt\_callbacks.h:28

[mgmt\_group](structmgmt__group.md)

A collection of handlers for an entire command group.

**Definition** mgmt.h:85

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [grp](dir_75a5d043a2b1048bf3665f6cb87645f5.md)
- [enum\_mgmt](dir_7749fe9dc62ba7fc2a3ca61de6b2d4b0.md)
- [enum\_mgmt\_callbacks.h](enum__mgmt__callbacks_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
