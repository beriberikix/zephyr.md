---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/img__mgmt__callbacks_8h_source.html
original_path: doxygen/html/img__mgmt__callbacks_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

img\_mgmt\_callbacks.h

[Go to the documentation of this file.](img__mgmt__callbacks_8h.md)

1/\*

2 \* Copyright (c) 2022 Laird Connectivity

3 \* Copyright (c) 2022 Nordic Semiconductor ASA

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef H\_MCUMGR\_IMG\_MGMT\_CALLBACKS\_

9#define H\_MCUMGR\_IMG\_MGMT\_CALLBACKS\_

10

11#ifdef \_\_cplusplus

12extern "C" {

13#endif

14

15/\* Dummy definitions, include zephyr/mgmt/mcumgr/grp/img\_mgmt/img\_mgmt.h for actual definitions \*/

16struct [img\_mgmt\_upload\_action](structimg__mgmt__upload__action.md);

17struct [img\_mgmt\_upload\_req](structimg__mgmt__upload__req.md);

18

25

[ 32](structimg__mgmt__upload__check.md)struct [img\_mgmt\_upload\_check](structimg__mgmt__upload__check.md) {

[ 34](structimg__mgmt__upload__check.md#aea96e650e2701e6064638dd4c384df55) struct [img\_mgmt\_upload\_action](structimg__mgmt__upload__action.md) \*[action](structimg__mgmt__upload__check.md#aea96e650e2701e6064638dd4c384df55);

35

[ 37](structimg__mgmt__upload__check.md#ab8a3e937302b1def309508eace664793) struct [img\_mgmt\_upload\_req](structimg__mgmt__upload__req.md) \*[req](structimg__mgmt__upload__check.md#ab8a3e937302b1def309508eace664793);

38};

39

43

44#ifdef \_\_cplusplus

45}

46#endif

47

48#endif

[img\_mgmt\_upload\_action](structimg__mgmt__upload__action.md)

Describes what to do during processing of an upload request.

**Definition** img\_mgmt.h:206

[img\_mgmt\_upload\_check](structimg__mgmt__upload__check.md)

Structure provided in the MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_CHUNK notification callback: This callback functio...

**Definition** img\_mgmt\_callbacks.h:32

[img\_mgmt\_upload\_check::req](structimg__mgmt__upload__check.md#ab8a3e937302b1def309508eace664793)

struct img\_mgmt\_upload\_req \* req

Upload request information.

**Definition** img\_mgmt\_callbacks.h:37

[img\_mgmt\_upload\_check::action](structimg__mgmt__upload__check.md#aea96e650e2701e6064638dd4c384df55)

struct img\_mgmt\_upload\_action \* action

Action to take.

**Definition** img\_mgmt\_callbacks.h:34

[img\_mgmt\_upload\_req](structimg__mgmt__upload__req.md)

Represents an individual upload request.

**Definition** img\_mgmt.h:183

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [grp](dir_75a5d043a2b1048bf3665f6cb87645f5.md)
- [img\_mgmt](dir_731c1b2142dfc9d7fee3a06aa394438e.md)
- [img\_mgmt\_callbacks.h](img__mgmt__callbacks_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
