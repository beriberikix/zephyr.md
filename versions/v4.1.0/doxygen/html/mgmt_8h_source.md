---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/mgmt_8h_source.html
original_path: doxygen/html/mgmt_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mgmt.h

[Go to the documentation of this file.](mgmt_8h.md)

1/\*

2 \* Copyright (c) 2018-2021 mcumgr authors

3 \* Copyright (c) 2022-2024 Nordic Semiconductor ASA

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

8#ifndef H\_MGMT\_MGMT\_

9#define H\_MGMT\_MGMT\_

10

11#include <[inttypes.h](inttypes_8h.md)>

12#include <[zephyr/sys/slist.h](slist_8h.md)>

13#include <[zephyr/mgmt/mcumgr/smp/smp.h](mgmt_2mcumgr_2smp_2smp_8h.md)>

14#include <[zephyr/mgmt/mcumgr/mgmt/mgmt\_defines.h](mgmt__defines_8h.md)>

15

16#ifdef \_\_cplusplus

17extern "C" {

18#endif

19

28

[ 39](group__mcumgr__mgmt__api.md#ga292686c742179758ca5b853fc21fe302)typedef void \*(\*mgmt\_alloc\_rsp\_fn)(const void \*src\_buf, void \*arg);

40

[ 49](group__mcumgr__mgmt__api.md#ga1346d5160823c5e43fce3e6cba9f8607)typedef void (\*[mgmt\_reset\_buf\_fn](group__mcumgr__mgmt__api.md#ga1346d5160823c5e43fce3e6cba9f8607))(void \*buf, void \*arg);

50

51#ifdef CONFIG\_MCUMGR\_SMP\_VERBOSE\_ERR\_RESPONSE

52#define MGMT\_CTXT\_SET\_RC\_RSN(mc, rsn) ((mc->rc\_rsn) = (rsn))

53#define MGMT\_CTXT\_RC\_RSN(mc) ((mc)->rc\_rsn)

54#else

[ 55](group__mcumgr__mgmt__api.md#ga8027c2a587a835d92450f2935e66eea0)#define MGMT\_CTXT\_SET\_RC\_RSN(mc, rsn)

[ 56](group__mcumgr__mgmt__api.md#ga4d22641395a665a911be715c2531fbd8)#define MGMT\_CTXT\_RC\_RSN(mc) NULL

57#endif

58

[ 68](group__mcumgr__mgmt__api.md#gaaafc2c73e1616340e29df6a1ba94c241)typedef int (\*[mgmt\_handler\_fn](group__mcumgr__mgmt__api.md#gaaafc2c73e1616340e29df6a1ba94c241))(struct [smp\_streamer](structsmp__streamer.md) \*ctxt);

69

[ 74](structmgmt__handler.md)struct [mgmt\_handler](structmgmt__handler.md) {

[ 75](structmgmt__handler.md#a7cc4917fa24afef79f1a8de8549a21e4) [mgmt\_handler\_fn](group__mcumgr__mgmt__api.md#gaaafc2c73e1616340e29df6a1ba94c241) [mh\_read](structmgmt__handler.md#a7cc4917fa24afef79f1a8de8549a21e4);

[ 76](structmgmt__handler.md#a1bc6b52645f6eb1d0e0b0c695d972c15) [mgmt\_handler\_fn](group__mcumgr__mgmt__api.md#gaaafc2c73e1616340e29df6a1ba94c241) [mh\_write](structmgmt__handler.md#a1bc6b52645f6eb1d0e0b0c695d972c15);

77#if defined(CONFIG\_MCUMGR\_MGMT\_HANDLER\_USER\_DATA)

78 void \*user\_data;

79#endif

80};

81

[ 85](structmgmt__group.md)struct [mgmt\_group](structmgmt__group.md) {

[ 87](structmgmt__group.md#ac150809b03f73c4c2f94742504af772c) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structmgmt__group.md#ac150809b03f73c4c2f94742504af772c);

88

[ 90](structmgmt__group.md#a7a6e90e500716095b9a22e3f56edac03) const struct [mgmt\_handler](structmgmt__handler.md) \*[mg\_handlers](structmgmt__group.md#a7a6e90e500716095b9a22e3f56edac03);

[ 91](structmgmt__group.md#a8b2de48e97c0de4c902d72aba4e920b4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [mg\_handlers\_count](structmgmt__group.md#a8b2de48e97c0de4c902d72aba4e920b4);

92

[ 94](structmgmt__group.md#a9d55dbf947096eed7cacfb9087d304d4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [mg\_group\_id](structmgmt__group.md#a9d55dbf947096eed7cacfb9087d304d4);

95

96#if defined(CONFIG\_MCUMGR\_SMP\_SUPPORT\_ORIGINAL\_PROTOCOL)

100 smp\_translate\_error\_fn mg\_translate\_error;

101#endif

102

103#if defined(CONFIG\_MCUMGR\_MGMT\_CUSTOM\_PAYLOAD)

105 bool custom\_payload;

106#endif

107

108#if IS\_ENABLED(CONFIG\_MCUMGR\_GRP\_ENUM\_DETAILS\_NAME)

110 const char \*mg\_group\_name;

111#endif

112};

113

[ 119](group__mcumgr__mgmt__api.md#ga70379f21faacddb5cc4a66f37a576ea0)void [mgmt\_register\_group](group__mcumgr__mgmt__api.md#ga70379f21faacddb5cc4a66f37a576ea0)(struct [mgmt\_group](structmgmt__group.md) \*[group](structgroup.md));

120

[ 126](group__mcumgr__mgmt__api.md#ga87e98bdf47d1c7798098444f69ccf8b8)void [mgmt\_unregister\_group](group__mcumgr__mgmt__api.md#ga87e98bdf47d1c7798098444f69ccf8b8)(struct [mgmt\_group](structmgmt__group.md) \*[group](structgroup.md));

127

[ 136](group__mcumgr__mgmt__api.md#ga9f63f42cd468ce85d0f800dc1472a5c8)typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[mgmt\_groups\_cb\_t](group__mcumgr__mgmt__api.md#ga9f63f42cd468ce85d0f800dc1472a5c8))(const struct [mgmt\_group](structmgmt__group.md) \*[group](structgroup.md), void \*user\_data);

137

[ 144](group__mcumgr__mgmt__api.md#ga125e3a6d076cade80f2080915a06ac67)void [mgmt\_groups\_foreach](group__mcumgr__mgmt__api.md#ga125e3a6d076cade80f2080915a06ac67)([mgmt\_groups\_cb\_t](group__mcumgr__mgmt__api.md#ga9f63f42cd468ce85d0f800dc1472a5c8) user\_cb, void \*user\_data);

145

[ 155](group__mcumgr__mgmt__api.md#ga620862436fad440b9d2b9d8112be4ad1)const struct [mgmt\_handler](structmgmt__handler.md) \*[mgmt\_find\_handler](group__mcumgr__mgmt__api.md#ga620862436fad440b9d2b9d8112be4ad1)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) group\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) command\_id);

156

[ 165](group__mcumgr__mgmt__api.md#gae88bc30026fbff6530179a94ba8f11ae)const struct [mgmt\_group](structmgmt__group.md) \*[mgmt\_find\_group](group__mcumgr__mgmt__api.md#gae88bc30026fbff6530179a94ba8f11ae)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) group\_id);

166

[ 176](group__mcumgr__mgmt__api.md#gaec6ccbcaf28404b4b3662d5059f0a32b)const struct [mgmt\_handler](structmgmt__handler.md) \*[mgmt\_get\_handler](group__mcumgr__mgmt__api.md#gaec6ccbcaf28404b4b3662d5059f0a32b)(const struct [mgmt\_group](structmgmt__group.md) \*[group](structgroup.md), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) command\_id);

177

178#if defined(CONFIG\_MCUMGR\_SMP\_SUPPORT\_ORIGINAL\_PROTOCOL)

188smp\_translate\_error\_fn mgmt\_find\_error\_translation\_function([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) group\_id);

189#endif

190

194

195#ifdef \_\_cplusplus

196}

197#endif

198

199#endif /\* MGMT\_MGMT\_H\_ \*/

[mgmt\_groups\_foreach](group__mcumgr__mgmt__api.md#ga125e3a6d076cade80f2080915a06ac67)

void mgmt\_groups\_foreach(mgmt\_groups\_cb\_t user\_cb, void \*user\_data)

Iterate over groups.

[mgmt\_reset\_buf\_fn](group__mcumgr__mgmt__api.md#ga1346d5160823c5e43fce3e6cba9f8607)

void(\* mgmt\_reset\_buf\_fn)(void \*buf, void \*arg)

Resets a buffer to a length of 0.

**Definition** mgmt.h:49

[mgmt\_find\_handler](group__mcumgr__mgmt__api.md#ga620862436fad440b9d2b9d8112be4ad1)

const struct mgmt\_handler \* mgmt\_find\_handler(uint16\_t group\_id, uint16\_t command\_id)

Finds a registered command handler.

[mgmt\_register\_group](group__mcumgr__mgmt__api.md#ga70379f21faacddb5cc4a66f37a576ea0)

void mgmt\_register\_group(struct mgmt\_group \*group)

Registers a full command group.

[mgmt\_unregister\_group](group__mcumgr__mgmt__api.md#ga87e98bdf47d1c7798098444f69ccf8b8)

void mgmt\_unregister\_group(struct mgmt\_group \*group)

Unregisters a full command group.

[mgmt\_groups\_cb\_t](group__mcumgr__mgmt__api.md#ga9f63f42cd468ce85d0f800dc1472a5c8)

bool(\* mgmt\_groups\_cb\_t)(const struct mgmt\_group \*group, void \*user\_data)

Group iteration callback.

**Definition** mgmt.h:136

[mgmt\_handler\_fn](group__mcumgr__mgmt__api.md#gaaafc2c73e1616340e29df6a1ba94c241)

int(\* mgmt\_handler\_fn)(struct smp\_streamer \*ctxt)

Processes a request and writes the corresponding response.

**Definition** mgmt.h:68

[mgmt\_find\_group](group__mcumgr__mgmt__api.md#gae88bc30026fbff6530179a94ba8f11ae)

const struct mgmt\_group \* mgmt\_find\_group(uint16\_t group\_id)

Finds a registered command group.

[mgmt\_get\_handler](group__mcumgr__mgmt__api.md#gaec6ccbcaf28404b4b3662d5059f0a32b)

const struct mgmt\_handler \* mgmt\_get\_handler(const struct mgmt\_group \*group, uint16\_t command\_id)

Finds a registered command handler.

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[inttypes.h](inttypes_8h.md)

[smp.h](mgmt_2mcumgr_2smp_2smp_8h.md)

SMP - Simple Management Protocol.

[mgmt\_defines.h](mgmt__defines_8h.md)

[slist.h](slist_8h.md)

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[group](structgroup.md)

Group structure.

**Definition** grp.h:18

[mgmt\_group](structmgmt__group.md)

A collection of handlers for an entire command group.

**Definition** mgmt.h:85

[mgmt\_group::mg\_handlers](structmgmt__group.md#a7a6e90e500716095b9a22e3f56edac03)

const struct mgmt\_handler \* mg\_handlers

Array of handlers; one entry per command ID.

**Definition** mgmt.h:90

[mgmt\_group::mg\_handlers\_count](structmgmt__group.md#a8b2de48e97c0de4c902d72aba4e920b4)

uint16\_t mg\_handlers\_count

**Definition** mgmt.h:91

[mgmt\_group::mg\_group\_id](structmgmt__group.md#a9d55dbf947096eed7cacfb9087d304d4)

uint16\_t mg\_group\_id

The numeric ID of this group.

**Definition** mgmt.h:94

[mgmt\_group::node](structmgmt__group.md#ac150809b03f73c4c2f94742504af772c)

sys\_snode\_t node

Entry list node.

**Definition** mgmt.h:87

[mgmt\_handler](structmgmt__handler.md)

Read handler and write handler for a single command ID.

**Definition** mgmt.h:74

[mgmt\_handler::mh\_write](structmgmt__handler.md#a1bc6b52645f6eb1d0e0b0c695d972c15)

mgmt\_handler\_fn mh\_write

**Definition** mgmt.h:76

[mgmt\_handler::mh\_read](structmgmt__handler.md#a7cc4917fa24afef79f1a8de8549a21e4)

mgmt\_handler\_fn mh\_read

**Definition** mgmt.h:75

[smp\_streamer](structsmp__streamer.md)

Decodes, encodes, and transmits SMP packets.

**Definition** smp.h:83

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [mgmt](dir_138c477f5f1e916a824d5e5e3c2b43b2.md)
- [mgmt.h](mgmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
