---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/shell__mgmt_8h_source.html
original_path: doxygen/html/shell__mgmt_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_mgmt.h

[Go to the documentation of this file.](shell__mgmt_8h.md)

1/\*

2 \* Copyright (c) 2018-2021 mcumgr authors

3 \* Copyright (c) 2023 Nordic Semiconductor ASA

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef H\_SHELL\_MGMT\_

9#define H\_SHELL\_MGMT\_

10

11#ifdef \_\_cplusplus

12extern "C" {

13#endif

14

[ 18](shell__mgmt_8h.md#a5b360507490dd79996c59bb51b0bb791)#define SHELL\_MGMT\_ID\_EXEC 0

19

[ 23](shell__mgmt_8h.md#ac37bf991450de1611ae54fd671b61581)enum [shell\_mgmt\_err\_code\_t](shell__mgmt_8h.md#ac37bf991450de1611ae54fd671b61581) {

[ 25](shell__mgmt_8h.md#ac37bf991450de1611ae54fd671b61581a461f818c3dc3aee4423d6bb94108ed51) [SHELL\_MGMT\_ERR\_OK](shell__mgmt_8h.md#ac37bf991450de1611ae54fd671b61581a461f818c3dc3aee4423d6bb94108ed51) = 0,

26

[ 28](shell__mgmt_8h.md#ac37bf991450de1611ae54fd671b61581a2e103a732de87c555b1e4ad5eccceb02) [SHELL\_MGMT\_ERR\_UNKNOWN](shell__mgmt_8h.md#ac37bf991450de1611ae54fd671b61581a2e103a732de87c555b1e4ad5eccceb02),

29

[ 31](shell__mgmt_8h.md#ac37bf991450de1611ae54fd671b61581a0086ab17e2685dc66e44704c6cd19205) [SHELL\_MGMT\_ERR\_COMMAND\_TOO\_LONG](shell__mgmt_8h.md#ac37bf991450de1611ae54fd671b61581a0086ab17e2685dc66e44704c6cd19205),

32

[ 34](shell__mgmt_8h.md#ac37bf991450de1611ae54fd671b61581a0ccd61db1c1f552a01d77128a4a75881) [SHELL\_MGMT\_ERR\_EMPTY\_COMMAND](shell__mgmt_8h.md#ac37bf991450de1611ae54fd671b61581a0ccd61db1c1f552a01d77128a4a75881),

35};

36

37#ifdef \_\_cplusplus

38}

39#endif

40

41#endif /\* H\_SHELL\_MGMT\_ \*/

[shell\_mgmt\_err\_code\_t](shell__mgmt_8h.md#ac37bf991450de1611ae54fd671b61581)

shell\_mgmt\_err\_code\_t

Command result codes for shell management group.

**Definition** shell\_mgmt.h:23

[SHELL\_MGMT\_ERR\_COMMAND\_TOO\_LONG](shell__mgmt_8h.md#ac37bf991450de1611ae54fd671b61581a0086ab17e2685dc66e44704c6cd19205)

@ SHELL\_MGMT\_ERR\_COMMAND\_TOO\_LONG

The provided command to execute is too long.

**Definition** shell\_mgmt.h:31

[SHELL\_MGMT\_ERR\_EMPTY\_COMMAND](shell__mgmt_8h.md#ac37bf991450de1611ae54fd671b61581a0ccd61db1c1f552a01d77128a4a75881)

@ SHELL\_MGMT\_ERR\_EMPTY\_COMMAND

No command to execute was provided.

**Definition** shell\_mgmt.h:34

[SHELL\_MGMT\_ERR\_UNKNOWN](shell__mgmt_8h.md#ac37bf991450de1611ae54fd671b61581a2e103a732de87c555b1e4ad5eccceb02)

@ SHELL\_MGMT\_ERR\_UNKNOWN

Unknown error occurred.

**Definition** shell\_mgmt.h:28

[SHELL\_MGMT\_ERR\_OK](shell__mgmt_8h.md#ac37bf991450de1611ae54fd671b61581a461f818c3dc3aee4423d6bb94108ed51)

@ SHELL\_MGMT\_ERR\_OK

No error, this is implied if there is no ret value in the response.

**Definition** shell\_mgmt.h:25

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [grp](dir_75a5d043a2b1048bf3665f6cb87645f5.md)
- [shell\_mgmt](dir_5e8382db16a4734888c451bd3831b770.md)
- [shell\_mgmt.h](shell__mgmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
