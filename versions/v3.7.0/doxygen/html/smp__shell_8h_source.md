---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/smp__shell_8h_source.html
original_path: doxygen/html/smp__shell_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

smp\_shell.h

[Go to the documentation of this file.](smp__shell_8h.md)

1/\*

2 \* Copyright (c) 2019 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

10

11#ifndef ZEPHYR\_INCLUDE\_MGMT\_SMP\_SHELL\_H\_

12#define ZEPHYR\_INCLUDE\_MGMT\_SMP\_SHELL\_H\_

13

14#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

15

16#ifdef \_\_cplusplus

17extern "C" {

18#endif

19

[ 20](smp__shell_8h.md#a472d6f81315fea4827be0a91557832eb)#define SMP\_SHELL\_RX\_BUF\_SIZE 127

21

[ 23](structsmp__shell__data.md)struct [smp\_shell\_data](structsmp__shell__data.md) {

[ 24](structsmp__shell__data.md#a67997e0400ee096e98781b839df3d6c2) struct [net\_buf\_pool](structnet__buf__pool.md) \*[buf\_pool](structsmp__shell__data.md#a67997e0400ee096e98781b839df3d6c2);

[ 25](structsmp__shell__data.md#a3e15c83e64e1cab0f14141d2a6dd7bed) struct [k\_fifo](structk__fifo.md) [buf\_ready](structsmp__shell__data.md#a3e15c83e64e1cab0f14141d2a6dd7bed);

[ 26](structsmp__shell__data.md#a281058a6cb23102af46cb0457c3a3232) struct [net\_buf](structnet__buf.md) \*[buf](structsmp__shell__data.md#a281058a6cb23102af46cb0457c3a3232);

[ 27](structsmp__shell__data.md#aea6798b62094c9d3bcc3dc6926800af4) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [esc\_state](structsmp__shell__data.md#aea6798b62094c9d3bcc3dc6926800af4);

28};

29

[ 42](smp__shell_8h.md#a785293b670fcc10190e6c3d480a7d6d6)size\_t [smp\_shell\_rx\_bytes](smp__shell_8h.md#a785293b670fcc10190e6c3d480a7d6d6)(struct [smp\_shell\_data](structsmp__shell__data.md) \*[data](structnet__buf.md#ac6eef59915e7ce167442fdacbbfb5e56), const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*bytes,

43 size\_t [size](structnet__buf.md#a1522d81a002804223e25300a6961f527));

44

[ 52](smp__shell_8h.md#a44b90f6ba276d8d7a89d6b90c8bb0341)void [smp\_shell\_process](smp__shell_8h.md#a44b90f6ba276d8d7a89d6b90c8bb0341)(struct [smp\_shell\_data](structsmp__shell__data.md) \*[data](structnet__buf.md#ac6eef59915e7ce167442fdacbbfb5e56));

53

[ 62](smp__shell_8h.md#a1b71c4da07049b47269002ef6ec2b256)int [smp\_shell\_init](smp__shell_8h.md#a1b71c4da07049b47269002ef6ec2b256)(void);

63

64#ifdef \_\_cplusplus

65}

66#endif

67

68#endif

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[types.h](include_2zephyr_2types_8h.md)

[smp\_shell\_init](smp__shell_8h.md#a1b71c4da07049b47269002ef6ec2b256)

int smp\_shell\_init(void)

Initializes SMP transport over shell.

[smp\_shell\_process](smp__shell_8h.md#a44b90f6ba276d8d7a89d6b90c8bb0341)

void smp\_shell\_process(struct smp\_shell\_data \*data)

Processes SMP data and executes command if full frame was received.

[smp\_shell\_rx\_bytes](smp__shell_8h.md#a785293b670fcc10190e6c3d480a7d6d6)

size\_t smp\_shell\_rx\_bytes(struct smp\_shell\_data \*data, const uint8\_t \*bytes, size\_t size)

Attempt to process received bytes as part of an SMP frame.

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[k\_fifo](structk__fifo.md)

**Definition** kernel.h:2391

[net\_buf\_pool](structnet__buf__pool.md)

Network buffer pool representation.

**Definition** buf.h:1076

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** buf.h:1004

[net\_buf::size](structnet__buf.md#a1522d81a002804223e25300a6961f527)

uint16\_t size

Amount of data that this buffer can store.

**Definition** buf.h:1036

[net\_buf::data](structnet__buf.md#ac6eef59915e7ce167442fdacbbfb5e56)

uint8\_t \* data

Pointer to the start of data in the buffer.

**Definition** buf.h:1030

[smp\_shell\_data](structsmp__shell__data.md)

Data used by SMP shell.

**Definition** smp\_shell.h:23

[smp\_shell\_data::buf](structsmp__shell__data.md#a281058a6cb23102af46cb0457c3a3232)

struct net\_buf \* buf

**Definition** smp\_shell.h:26

[smp\_shell\_data::buf\_ready](structsmp__shell__data.md#a3e15c83e64e1cab0f14141d2a6dd7bed)

struct k\_fifo buf\_ready

**Definition** smp\_shell.h:25

[smp\_shell\_data::buf\_pool](structsmp__shell__data.md#a67997e0400ee096e98781b839df3d6c2)

struct net\_buf\_pool \* buf\_pool

**Definition** smp\_shell.h:24

[smp\_shell\_data::esc\_state](structsmp__shell__data.md#aea6798b62094c9d3bcc3dc6926800af4)

atomic\_t esc\_state

**Definition** smp\_shell.h:27

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [transport](dir_9a3f12841ae237fd7345c80156d89ad0.md)
- [smp\_shell.h](smp__shell_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
