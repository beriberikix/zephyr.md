---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/stat__mgmt_8h_source.html
original_path: doxygen/html/stat__mgmt_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stat\_mgmt.h

[Go to the documentation of this file.](stat__mgmt_8h.md)

1/\*

2 \* Copyright (c) 2018-2021 mcumgr authors

3 \* Copyright (c) 2023 Nordic Semiconductor ASA

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef H\_STAT\_MGMT\_

9#define H\_STAT\_MGMT\_

10

11#ifdef \_\_cplusplus

12extern "C" {

13#endif

14

[ 18](stat__mgmt_8h.md#a155235d2c21b5a698d833ca468d9473e)#define STAT\_MGMT\_ID\_SHOW 0

[ 19](stat__mgmt_8h.md#aed49473584422e0270f2f06e0ee0c330)#define STAT\_MGMT\_ID\_LIST 1

20

[ 24](stat__mgmt_8h.md#a9144a5e8c384093e47603a15b3d1ff69)enum [stat\_mgmt\_err\_code\_t](stat__mgmt_8h.md#a9144a5e8c384093e47603a15b3d1ff69) {

[ 26](stat__mgmt_8h.md#a9144a5e8c384093e47603a15b3d1ff69a8aa83ae8d80615f2789bc788dd260577) [STAT\_MGMT\_ERR\_OK](stat__mgmt_8h.md#a9144a5e8c384093e47603a15b3d1ff69a8aa83ae8d80615f2789bc788dd260577) = 0,

27

[ 29](stat__mgmt_8h.md#a9144a5e8c384093e47603a15b3d1ff69aba909444504e8d93eafc8b29a171bc82) [STAT\_MGMT\_ERR\_UNKNOWN](stat__mgmt_8h.md#a9144a5e8c384093e47603a15b3d1ff69aba909444504e8d93eafc8b29a171bc82),

30

[ 32](stat__mgmt_8h.md#a9144a5e8c384093e47603a15b3d1ff69a1bff1f2f9b3f7d1a7ca09e80c4665710) [STAT\_MGMT\_ERR\_INVALID\_GROUP](stat__mgmt_8h.md#a9144a5e8c384093e47603a15b3d1ff69a1bff1f2f9b3f7d1a7ca09e80c4665710),

33

[ 35](stat__mgmt_8h.md#a9144a5e8c384093e47603a15b3d1ff69a58b33ada336c88be45f3321dde52b52e) [STAT\_MGMT\_ERR\_INVALID\_STAT\_NAME](stat__mgmt_8h.md#a9144a5e8c384093e47603a15b3d1ff69a58b33ada336c88be45f3321dde52b52e),

36

[ 38](stat__mgmt_8h.md#a9144a5e8c384093e47603a15b3d1ff69ad6158abd9117931ece95a74473282b58) [STAT\_MGMT\_ERR\_INVALID\_STAT\_SIZE](stat__mgmt_8h.md#a9144a5e8c384093e47603a15b3d1ff69ad6158abd9117931ece95a74473282b58),

39

[ 41](stat__mgmt_8h.md#a9144a5e8c384093e47603a15b3d1ff69a7e1dc898fd0e6ace7dafd47ed766e833) [STAT\_MGMT\_ERR\_WALK\_ABORTED](stat__mgmt_8h.md#a9144a5e8c384093e47603a15b3d1ff69a7e1dc898fd0e6ace7dafd47ed766e833),

42};

43

[ 47](structstat__mgmt__entry.md)struct [stat\_mgmt\_entry](structstat__mgmt__entry.md) {

[ 48](structstat__mgmt__entry.md#a44621593259f6f298bb62eb2675c1efb) const char \*[name](structstat__mgmt__entry.md#a44621593259f6f298bb62eb2675c1efb);

[ 49](structstat__mgmt__entry.md#aa8441c1d2a1ce5acaa660e2e9b9d260d) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [value](structstat__mgmt__entry.md#aa8441c1d2a1ce5acaa660e2e9b9d260d);

50};

51

52#ifdef \_\_cplusplus

53}

54#endif

55

56#endif /\* H\_STAT\_MGMT\_ \*/

[stat\_mgmt\_err\_code\_t](stat__mgmt_8h.md#a9144a5e8c384093e47603a15b3d1ff69)

stat\_mgmt\_err\_code\_t

Command result codes for statistics management group.

**Definition** stat\_mgmt.h:24

[STAT\_MGMT\_ERR\_INVALID\_GROUP](stat__mgmt_8h.md#a9144a5e8c384093e47603a15b3d1ff69a1bff1f2f9b3f7d1a7ca09e80c4665710)

@ STAT\_MGMT\_ERR\_INVALID\_GROUP

The provided statistic group name was not found.

**Definition** stat\_mgmt.h:32

[STAT\_MGMT\_ERR\_INVALID\_STAT\_NAME](stat__mgmt_8h.md#a9144a5e8c384093e47603a15b3d1ff69a58b33ada336c88be45f3321dde52b52e)

@ STAT\_MGMT\_ERR\_INVALID\_STAT\_NAME

The provided statistic name was not found.

**Definition** stat\_mgmt.h:35

[STAT\_MGMT\_ERR\_WALK\_ABORTED](stat__mgmt_8h.md#a9144a5e8c384093e47603a15b3d1ff69a7e1dc898fd0e6ace7dafd47ed766e833)

@ STAT\_MGMT\_ERR\_WALK\_ABORTED

Walk through of statistics was aborted.

**Definition** stat\_mgmt.h:41

[STAT\_MGMT\_ERR\_OK](stat__mgmt_8h.md#a9144a5e8c384093e47603a15b3d1ff69a8aa83ae8d80615f2789bc788dd260577)

@ STAT\_MGMT\_ERR\_OK

No error, this is implied if there is no ret value in the response.

**Definition** stat\_mgmt.h:26

[STAT\_MGMT\_ERR\_UNKNOWN](stat__mgmt_8h.md#a9144a5e8c384093e47603a15b3d1ff69aba909444504e8d93eafc8b29a171bc82)

@ STAT\_MGMT\_ERR\_UNKNOWN

Unknown error occurred.

**Definition** stat\_mgmt.h:29

[STAT\_MGMT\_ERR\_INVALID\_STAT\_SIZE](stat__mgmt_8h.md#a9144a5e8c384093e47603a15b3d1ff69ad6158abd9117931ece95a74473282b58)

@ STAT\_MGMT\_ERR\_INVALID\_STAT\_SIZE

The size of the statistic cannot be handled.

**Definition** stat\_mgmt.h:38

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[stat\_mgmt\_entry](structstat__mgmt__entry.md)

Represents a single value in a statistics group.

**Definition** stat\_mgmt.h:47

[stat\_mgmt\_entry::name](structstat__mgmt__entry.md#a44621593259f6f298bb62eb2675c1efb)

const char \* name

**Definition** stat\_mgmt.h:48

[stat\_mgmt\_entry::value](structstat__mgmt__entry.md#aa8441c1d2a1ce5acaa660e2e9b9d260d)

uint64\_t value

**Definition** stat\_mgmt.h:49

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [grp](dir_75a5d043a2b1048bf3665f6cb87645f5.md)
- [stat\_mgmt](dir_02a570021bf1e49be869a1f46be4c519.md)
- [stat\_mgmt.h](stat__mgmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
