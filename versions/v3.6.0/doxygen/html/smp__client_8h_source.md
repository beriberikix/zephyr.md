---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/smp__client_8h_source.html
original_path: doxygen/html/smp__client_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

smp\_client.h

[Go to the documentation of this file.](smp__client_8h.md)

1/\*

2 \* Copyright (c) 2023 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef H\_SMP\_CLIENT\_

8#define H\_SMP\_CLIENT\_

9

10#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

11#include <[zephyr/net/buf.h](net_2buf_8h.md)>

12#include <mgmt/mcumgr/transport/smp\_internal.h>

13#include <[zephyr/mgmt/mcumgr/smp/smp.h](mgmt_2mcumgr_2smp_2smp_8h.md)>

14#include <[zephyr/mgmt/mcumgr/transport/smp.h](mgmt_2mcumgr_2transport_2smp_8h.md)>

15

22

[ 26](structsmp__client__object.md)struct [smp\_client\_object](structsmp__client__object.md) {

[ 28](structsmp__client__object.md#ae4c73b23b90ef9f6cb8a93efde992c8a) struct [k\_work](structk__work.md) [work](structsmp__client__object.md#ae4c73b23b90ef9f6cb8a93efde992c8a);

[ 30](structsmp__client__object.md#a5d3cf1e109692112bf52b0b8514bab9f) struct [k\_fifo](structk__fifo.md) [tx\_fifo](structsmp__client__object.md#a5d3cf1e109692112bf52b0b8514bab9f);

[ 32](structsmp__client__object.md#a01507d6fa5a75751b39ccda82d0836ef) struct [smp\_transport](structsmp__transport.md) \*[smpt](structsmp__client__object.md#a01507d6fa5a75751b39ccda82d0836ef);

[ 34](structsmp__client__object.md#a0de9e7ee538b84cf1a6065b7b8b0bc53) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [smp\_seq](structsmp__client__object.md#a0de9e7ee538b84cf1a6065b7b8b0bc53);

35};

36

37#ifdef \_\_cplusplus

38extern "C" {

39#endif

40

[ 50](group__mcumgr__smp__client.md#ga07f36d0ac230d158c2959e8010444e47)int [smp\_client\_object\_init](group__mcumgr__smp__client.md#ga07f36d0ac230d158c2959e8010444e47)(struct [smp\_client\_object](structsmp__client__object.md) \*smp\_client, int smp\_type);

51

[ 61](group__mcumgr__smp__client.md#gae7974bf0e951403f6dfe8b33a2547acc)typedef int (\*[smp\_client\_res\_fn](group__mcumgr__smp__client.md#gae7974bf0e951403f6dfe8b33a2547acc))(struct [net\_buf](structnet__buf.md) \*nb, void \*[user\_data](structnet__buf.md#ade8055f804d5a1fea13e55d71d92a5e7));

62

[ 72](group__mcumgr__smp__client.md#ga42022a3ea929da134644996c4414cfce)int [smp\_client\_single\_response](group__mcumgr__smp__client.md#ga42022a3ea929da134644996c4414cfce)(struct [net\_buf](structnet__buf.md) \*nb, const struct smp\_hdr \*res\_hdr);

73

[ 86](group__mcumgr__smp__client.md#ga57ec028fc6bcb3591298815b1d9b8a3b)struct [net\_buf](structnet__buf.md) \*[smp\_client\_buf\_allocation](group__mcumgr__smp__client.md#ga57ec028fc6bcb3591298815b1d9b8a3b)(struct [smp\_client\_object](structsmp__client__object.md) \*smp\_client, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) group,

87 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) command\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) op,

88 enum [smp\_mcumgr\_version\_t](mgmt_2mcumgr_2smp_2smp_8h.md#aa05d01653e39ef61a93f33319c9a00ed) version);

[ 94](group__mcumgr__smp__client.md#gace302f95e5f45076db72fbecf190f0f5)void [smp\_client\_buf\_free](group__mcumgr__smp__client.md#gace302f95e5f45076db72fbecf190f0f5)(struct [net\_buf](structnet__buf.md) \*nb);

95

[ 109](group__mcumgr__smp__client.md#gaeb20d13ddf14ddb924b0a84a014abda5)int [smp\_client\_send\_cmd](group__mcumgr__smp__client.md#gaeb20d13ddf14ddb924b0a84a014abda5)(struct [smp\_client\_object](structsmp__client__object.md) \*smp\_client, struct [net\_buf](structnet__buf.md) \*nb,

110 [smp\_client\_res\_fn](group__mcumgr__smp__client.md#gae7974bf0e951403f6dfe8b33a2547acc) cb, void \*[user\_data](structnet__buf.md#ade8055f804d5a1fea13e55d71d92a5e7), int timeout\_in\_sec);

111

115

116#ifdef \_\_cplusplus

117}

118#endif

119

120#endif /\* H\_SMP\_CLIENT\_ \*/

[smp\_client\_object\_init](group__mcumgr__smp__client.md#ga07f36d0ac230d158c2959e8010444e47)

int smp\_client\_object\_init(struct smp\_client\_object \*smp\_client, int smp\_type)

Initialize a SMP client object.

[smp\_client\_single\_response](group__mcumgr__smp__client.md#ga42022a3ea929da134644996c4414cfce)

int smp\_client\_single\_response(struct net\_buf \*nb, const struct smp\_hdr \*res\_hdr)

SMP client response handler.

[smp\_client\_buf\_allocation](group__mcumgr__smp__client.md#ga57ec028fc6bcb3591298815b1d9b8a3b)

struct net\_buf \* smp\_client\_buf\_allocation(struct smp\_client\_object \*smp\_client, uint16\_t group, uint8\_t command\_id, uint8\_t op, enum smp\_mcumgr\_version\_t version)

Allocate buffer and initialize with SMP header.

[smp\_client\_buf\_free](group__mcumgr__smp__client.md#gace302f95e5f45076db72fbecf190f0f5)

void smp\_client\_buf\_free(struct net\_buf \*nb)

Free a SMP client buffer.

[smp\_client\_res\_fn](group__mcumgr__smp__client.md#gae7974bf0e951403f6dfe8b33a2547acc)

int(\* smp\_client\_res\_fn)(struct net\_buf \*nb, void \*user\_data)

Response callback for SMP send.

**Definition** smp\_client.h:61

[smp\_client\_send\_cmd](group__mcumgr__smp__client.md#gaeb20d13ddf14ddb924b0a84a014abda5)

int smp\_client\_send\_cmd(struct smp\_client\_object \*smp\_client, struct net\_buf \*nb, smp\_client\_res\_fn cb, void \*user\_data, int timeout\_in\_sec)

SMP client data send request.

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[smp.h](mgmt_2mcumgr_2smp_2smp_8h.md)

SMP - Simple Management Protocol.

[smp\_mcumgr\_version\_t](mgmt_2mcumgr_2smp_2smp_8h.md#aa05d01653e39ef61a93f33319c9a00ed)

smp\_mcumgr\_version\_t

SMP MCUmgr protocol version, part of the SMP header.

**Definition** smp.h:39

[smp.h](mgmt_2mcumgr_2transport_2smp_8h.md)

[buf.h](net_2buf_8h.md)

Buffer management.

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[k\_fifo](structk__fifo.md)

**Definition** kernel.h:2374

[k\_work](structk__work.md)

A structure used to submit work.

**Definition** kernel.h:3861

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** buf.h:910

[net\_buf::user\_data](structnet__buf.md#ade8055f804d5a1fea13e55d71d92a5e7)

uint8\_t user\_data[]

System metadata for this buffer.

**Definition** buf.h:955

[smp\_client\_object](structsmp__client__object.md)

SMP client object.

**Definition** smp\_client.h:26

[smp\_client\_object::smpt](structsmp__client__object.md#a01507d6fa5a75751b39ccda82d0836ef)

struct smp\_transport \* smpt

SMP transport object.

**Definition** smp\_client.h:32

[smp\_client\_object::smp\_seq](structsmp__client__object.md#a0de9e7ee538b84cf1a6065b7b8b0bc53)

uint8\_t smp\_seq

SMP SEQ.

**Definition** smp\_client.h:34

[smp\_client\_object::tx\_fifo](structsmp__client__object.md#a5d3cf1e109692112bf52b0b8514bab9f)

struct k\_fifo tx\_fifo

FIFO for client TX queue.

**Definition** smp\_client.h:30

[smp\_client\_object::work](structsmp__client__object.md#ae4c73b23b90ef9f6cb8a93efde992c8a)

struct k\_work work

Must be the first member.

**Definition** smp\_client.h:28

[smp\_transport](structsmp__transport.md)

SMP transport object for sending SMP responses.

**Definition** smp.h:118

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [smp](dir_e62cfe388532d436a5daefec152a780b.md)
- [smp\_client.h](smp__client_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
