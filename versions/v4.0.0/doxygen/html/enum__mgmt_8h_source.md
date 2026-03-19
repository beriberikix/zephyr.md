---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/enum__mgmt_8h_source.html
original_path: doxygen/html/enum__mgmt_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

enum\_mgmt.h

[Go to the documentation of this file.](enum__mgmt_8h.md)

1/\*

2 \* Copyright (c) 2024 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef H\_ENUM\_MGMT\_

8#define H\_ENUM\_MGMT\_

9

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

[ 24](group__mcumgr__enum__mgmt.md#gab16f2823b9bb4140a2fc336af5d16d2b)#define ENUM\_MGMT\_ID\_COUNT 0

[ 25](group__mcumgr__enum__mgmt.md#ga9b6c5a3021a30f8f6a83694ff9a07bf4)#define ENUM\_MGMT\_ID\_LIST 1

[ 26](group__mcumgr__enum__mgmt.md#ga5b08e51b1e32c27da5597fab4f68f94e)#define ENUM\_MGMT\_ID\_SINGLE 2

[ 27](group__mcumgr__enum__mgmt.md#ga03edf25ed33ccdf00b0a21ee574e1b4d)#define ENUM\_MGMT\_ID\_DETAILS 3

28

[ 32](group__mcumgr__enum__mgmt.md#gaceaae2d8284b4a64b1303513e6aa3099)enum [enum\_mgmt\_err\_code\_t](group__mcumgr__enum__mgmt.md#gaceaae2d8284b4a64b1303513e6aa3099) {

[ 34](group__mcumgr__enum__mgmt.md#ggaceaae2d8284b4a64b1303513e6aa3099aab31067e337c3220232e8eb3b3d885c0) [ENUM\_MGMT\_ERR\_OK](group__mcumgr__enum__mgmt.md#ggaceaae2d8284b4a64b1303513e6aa3099aab31067e337c3220232e8eb3b3d885c0) = 0,

35

[ 37](group__mcumgr__enum__mgmt.md#ggaceaae2d8284b4a64b1303513e6aa3099a7f535a752e4c789024e4fecb5cdd7c7f) [ENUM\_MGMT\_ERR\_UNKNOWN](group__mcumgr__enum__mgmt.md#ggaceaae2d8284b4a64b1303513e6aa3099a7f535a752e4c789024e4fecb5cdd7c7f),

38

[ 40](group__mcumgr__enum__mgmt.md#ggaceaae2d8284b4a64b1303513e6aa3099a7866b895eac198fe6eb021ef385a185e) [ENUM\_MGMT\_ERR\_TOO\_MANY\_GROUP\_ENTRIES](group__mcumgr__enum__mgmt.md#ggaceaae2d8284b4a64b1303513e6aa3099a7866b895eac198fe6eb021ef385a185e),

41

[ 43](group__mcumgr__enum__mgmt.md#ggaceaae2d8284b4a64b1303513e6aa3099ac056ab2ae764f50715d9ee478bc0c153) [ENUM\_MGMT\_ERR\_INSUFFICIENT\_HEAP\_FOR\_ENTRIES](group__mcumgr__enum__mgmt.md#ggaceaae2d8284b4a64b1303513e6aa3099ac056ab2ae764f50715d9ee478bc0c153),

44

[ 46](group__mcumgr__enum__mgmt.md#ggaceaae2d8284b4a64b1303513e6aa3099af2dff8560e72db54fea41a6345aa5f72) [ENUM\_MGMT\_ERR\_INDEX\_TOO\_LARGE](group__mcumgr__enum__mgmt.md#ggaceaae2d8284b4a64b1303513e6aa3099af2dff8560e72db54fea41a6345aa5f72),

47};

48

52

53#ifdef \_\_cplusplus

54}

55#endif

56

57#endif /\* H\_ENUM\_MGMT\_ \*/

[enum\_mgmt\_err\_code\_t](group__mcumgr__enum__mgmt.md#gaceaae2d8284b4a64b1303513e6aa3099)

enum\_mgmt\_err\_code\_t

Command result codes for enumeration management group.

**Definition** enum\_mgmt.h:32

[ENUM\_MGMT\_ERR\_TOO\_MANY\_GROUP\_ENTRIES](group__mcumgr__enum__mgmt.md#ggaceaae2d8284b4a64b1303513e6aa3099a7866b895eac198fe6eb021ef385a185e)

@ ENUM\_MGMT\_ERR\_TOO\_MANY\_GROUP\_ENTRIES

Too many entries were provided.

**Definition** enum\_mgmt.h:40

[ENUM\_MGMT\_ERR\_UNKNOWN](group__mcumgr__enum__mgmt.md#ggaceaae2d8284b4a64b1303513e6aa3099a7f535a752e4c789024e4fecb5cdd7c7f)

@ ENUM\_MGMT\_ERR\_UNKNOWN

Unknown error occurred.

**Definition** enum\_mgmt.h:37

[ENUM\_MGMT\_ERR\_OK](group__mcumgr__enum__mgmt.md#ggaceaae2d8284b4a64b1303513e6aa3099aab31067e337c3220232e8eb3b3d885c0)

@ ENUM\_MGMT\_ERR\_OK

No error, this is implied if there is no ret value in the response.

**Definition** enum\_mgmt.h:34

[ENUM\_MGMT\_ERR\_INSUFFICIENT\_HEAP\_FOR\_ENTRIES](group__mcumgr__enum__mgmt.md#ggaceaae2d8284b4a64b1303513e6aa3099ac056ab2ae764f50715d9ee478bc0c153)

@ ENUM\_MGMT\_ERR\_INSUFFICIENT\_HEAP\_FOR\_ENTRIES

Insufficient heap memory to store entry data.

**Definition** enum\_mgmt.h:43

[ENUM\_MGMT\_ERR\_INDEX\_TOO\_LARGE](group__mcumgr__enum__mgmt.md#ggaceaae2d8284b4a64b1303513e6aa3099af2dff8560e72db54fea41a6345aa5f72)

@ ENUM\_MGMT\_ERR\_INDEX\_TOO\_LARGE

Provided index is larger than the number of supported grouped.

**Definition** enum\_mgmt.h:46

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [grp](dir_75a5d043a2b1048bf3665f6cb87645f5.md)
- [enum\_mgmt](dir_7749fe9dc62ba7fc2a3ca61de6b2d4b0.md)
- [enum\_mgmt.h](enum__mgmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
