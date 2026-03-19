---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/os__mgmt__client_8h_source.html
original_path: doxygen/html/os__mgmt__client_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

os\_mgmt\_client.h

[Go to the documentation of this file.](os__mgmt__client_8h.md)

1/\*

2 \* Copyright (c) 2023 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef H\_OS\_MGMT\_CLIENT\_

8#define H\_OS\_MGMT\_CLIENT\_

9

10#include <[inttypes.h](inttypes_8h.md)>

11#include <[zephyr/mgmt/mcumgr/smp/smp\_client.h](smp__client_8h.md)>

12

19

20#ifdef \_\_cplusplus

21extern "C" {

22#endif

23

[ 27](structos__mgmt__client.md)struct [os\_mgmt\_client](structos__mgmt__client.md) {

[ 29](structos__mgmt__client.md#ada340aa0c6da9632410c36695adc0c33) struct [smp\_client\_object](structsmp__client__object.md) \*[smp\_client](structos__mgmt__client.md#ada340aa0c6da9632410c36695adc0c33);

[ 31](structos__mgmt__client.md#ac177e863befa59a099efd3ee7de0acc3) int [status](structos__mgmt__client.md#ac177e863befa59a099efd3ee7de0acc3);

32};

33

[ 41](group__mcumgr__os__mgmt__client.md#gafab4d3da30fa2bf855110d541b8fee08)void [os\_mgmt\_client\_init](group__mcumgr__os__mgmt__client.md#gafab4d3da30fa2bf855110d541b8fee08)(struct [os\_mgmt\_client](structos__mgmt__client.md) \*client, struct [smp\_client\_object](structsmp__client__object.md) \*smp\_client);

42

[ 53](group__mcumgr__os__mgmt__client.md#ga2dd2edb7c3952413c361b3d38dc2eaad)int [os\_mgmt\_client\_echo](group__mcumgr__os__mgmt__client.md#ga2dd2edb7c3952413c361b3d38dc2eaad)(struct [os\_mgmt\_client](structos__mgmt__client.md) \*client, const char \*echo\_string, size\_t max\_len);

54

[ 63](group__mcumgr__os__mgmt__client.md#ga5cb153bf30c40e82e8f55ac18a45fa09)int [os\_mgmt\_client\_reset](group__mcumgr__os__mgmt__client.md#ga5cb153bf30c40e82e8f55ac18a45fa09)(struct [os\_mgmt\_client](structos__mgmt__client.md) \*client);

64

68

69#ifdef \_\_cplusplus

70}

71#endif

72

73#endif /\* H\_OS\_MGMT\_CLIENT\_ \*/

[os\_mgmt\_client\_echo](group__mcumgr__os__mgmt__client.md#ga2dd2edb7c3952413c361b3d38dc2eaad)

int os\_mgmt\_client\_echo(struct os\_mgmt\_client \*client, const char \*echo\_string, size\_t max\_len)

Send SMP message for Echo command.

[os\_mgmt\_client\_reset](group__mcumgr__os__mgmt__client.md#ga5cb153bf30c40e82e8f55ac18a45fa09)

int os\_mgmt\_client\_reset(struct os\_mgmt\_client \*client)

Send SMP Reset command.

[os\_mgmt\_client\_init](group__mcumgr__os__mgmt__client.md#gafab4d3da30fa2bf855110d541b8fee08)

void os\_mgmt\_client\_init(struct os\_mgmt\_client \*client, struct smp\_client\_object \*smp\_client)

Initialize OS management client.

[inttypes.h](inttypes_8h.md)

[smp\_client.h](smp__client_8h.md)

[os\_mgmt\_client](structos__mgmt__client.md)

OS mgmt client object.

**Definition** os\_mgmt\_client.h:27

[os\_mgmt\_client::status](structos__mgmt__client.md#ac177e863befa59a099efd3ee7de0acc3)

int status

Command status.

**Definition** os\_mgmt\_client.h:31

[os\_mgmt\_client::smp\_client](structos__mgmt__client.md#ada340aa0c6da9632410c36695adc0c33)

struct smp\_client\_object \* smp\_client

SMP client object.

**Definition** os\_mgmt\_client.h:29

[smp\_client\_object](structsmp__client__object.md)

SMP client object.

**Definition** smp\_client.h:26

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [grp](dir_75a5d043a2b1048bf3665f6cb87645f5.md)
- [os\_mgmt](dir_1a5ff9dfdb0e06a8ce3ba8e3db8b26fb.md)
- [os\_mgmt\_client.h](os__mgmt__client_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
