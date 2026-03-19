---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ccp_8h_source.html
original_path: doxygen/html/ccp_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ccp.h

[Go to the documentation of this file.](ccp_8h.md)

1

5

6/\*

7 \* Copyright (c) 2024 Nordic Semiconductor ASA

8 \*

9 \* SPDX-License-Identifier: Apache-2.0

10 \*/

11

12#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_CCP\_H\_

13#define ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_CCP\_H\_

14

34#include <[stdint.h](stdint_8h.md)>

35

36#include <zephyr/autoconf.h>

37#include <[zephyr/bluetooth/audio/tbs.h](tbs_8h.md)>

38#include <[zephyr/bluetooth/conn.h](conn_8h.md)>

39#include <[zephyr/sys/slist.h](slist_8h.md)>

40

41#ifdef \_\_cplusplus

42extern "C" {

43#endif

50struct bt\_ccp\_call\_control\_server\_bearer;

51

[ 74](group__bt__ccp__call__control__server.md#ga5e5acb90cc39b5f8a4e25d8ab8a11b10)int [bt\_ccp\_call\_control\_server\_register\_bearer](group__bt__ccp__call__control__server.md#ga5e5acb90cc39b5f8a4e25d8ab8a11b10)(const struct [bt\_tbs\_register\_param](structbt__tbs__register__param.md) \*param,

75 struct bt\_ccp\_call\_control\_server\_bearer \*\*bearer);

76

[ 93](group__bt__ccp__call__control__server.md#gaa2486dec8a47bd7f4cd4076477e8ac4a)int [bt\_ccp\_call\_control\_server\_unregister\_bearer](group__bt__ccp__call__control__server.md#gaa2486dec8a47bd7f4cd4076477e8ac4a)(struct bt\_ccp\_call\_control\_server\_bearer \*bearer);

94 /\* End of group bt\_ccp\_call\_control\_server \*/

96

103struct bt\_ccp\_call\_control\_client;

104

106struct bt\_ccp\_call\_control\_client\_bearer;

107

[ 109](structbt__ccp__call__control__client__bearers.md)struct [bt\_ccp\_call\_control\_client\_bearers](structbt__ccp__call__control__client__bearers.md) {

110#if defined(CONFIG\_BT\_TBS\_CLIENT\_GTBS)

112 struct bt\_ccp\_call\_control\_client\_bearer \*gtbs\_bearer;

113#endif /\* CONFIG\_BT\_TBS\_CLIENT\_GTBS \*/

114

115#if defined(CONFIG\_BT\_TBS\_CLIENT\_TBS)

117 size\_t tbs\_count;

118

120 struct bt\_ccp\_call\_control\_client\_bearer

121 \*tbs\_bearers[CONFIG\_BT\_CCP\_CALL\_CONTROL\_CLIENT\_BEARER\_COUNT];

122#endif /\* CONFIG\_BT\_TBS\_CLIENT\_TBS \*/

123};

124

[ 130](structbt__ccp__call__control__client__cb.md)struct [bt\_ccp\_call\_control\_client\_cb](structbt__ccp__call__control__client__cb.md) {

[ 141](structbt__ccp__call__control__client__cb.md#a322f75bc9d28efc74f9a4571e952ed5e) void (\*[discover](structbt__ccp__call__control__client__cb.md#a322f75bc9d28efc74f9a4571e952ed5e))(struct bt\_ccp\_call\_control\_client \*client, int err,

142 struct [bt\_ccp\_call\_control\_client\_bearers](structbt__ccp__call__control__client__bearers.md) \*bearers);

143

146 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \_node;

148};

149

[ 168](group__bt__ccp__call__control__client.md#ga2a5bce65e39ba05625423308f996021d)int [bt\_ccp\_call\_control\_client\_discover](group__bt__ccp__call__control__client.md#ga2a5bce65e39ba05625423308f996021d)(struct bt\_conn \*conn,

169 struct bt\_ccp\_call\_control\_client \*\*out\_client);

170

[ 180](group__bt__ccp__call__control__client.md#ga8c5c3907759fe02745339b9456cca05f)int [bt\_ccp\_call\_control\_client\_register\_cb](group__bt__ccp__call__control__client.md#ga8c5c3907759fe02745339b9456cca05f)(struct [bt\_ccp\_call\_control\_client\_cb](structbt__ccp__call__control__client__cb.md) \*cb);

181

[ 191](group__bt__ccp__call__control__client.md#ga534a15db3e87d63942de6ba4bd8377db)int [bt\_ccp\_call\_control\_client\_unregister\_cb](group__bt__ccp__call__control__client.md#ga534a15db3e87d63942de6ba4bd8377db)(struct [bt\_ccp\_call\_control\_client\_cb](structbt__ccp__call__control__client__cb.md) \*cb); /\* End of group bt\_ccp\_call\_control\_client \*/

193#ifdef \_\_cplusplus

194}

195#endif

196

200

201#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_CCP\_H\_ \*/

[conn.h](conn_8h.md)

Bluetooth connection handling.

[bt\_ccp\_call\_control\_client\_discover](group__bt__ccp__call__control__client.md#ga2a5bce65e39ba05625423308f996021d)

int bt\_ccp\_call\_control\_client\_discover(struct bt\_conn \*conn, struct bt\_ccp\_call\_control\_client \*\*out\_client)

Discovers the Telephone Bearer Service (TBS) support on a remote device.

[bt\_ccp\_call\_control\_client\_unregister\_cb](group__bt__ccp__call__control__client.md#ga534a15db3e87d63942de6ba4bd8377db)

int bt\_ccp\_call\_control\_client\_unregister\_cb(struct bt\_ccp\_call\_control\_client\_cb \*cb)

Unregister callbacks for the Call Control Client.

[bt\_ccp\_call\_control\_client\_register\_cb](group__bt__ccp__call__control__client.md#ga8c5c3907759fe02745339b9456cca05f)

int bt\_ccp\_call\_control\_client\_register\_cb(struct bt\_ccp\_call\_control\_client\_cb \*cb)

Register callbacks for the Call Control Client.

[bt\_ccp\_call\_control\_server\_register\_bearer](group__bt__ccp__call__control__server.md#ga5e5acb90cc39b5f8a4e25d8ab8a11b10)

int bt\_ccp\_call\_control\_server\_register\_bearer(const struct bt\_tbs\_register\_param \*param, struct bt\_ccp\_call\_control\_server\_bearer \*\*bearer)

Register a Telephone Bearer.

[bt\_ccp\_call\_control\_server\_unregister\_bearer](group__bt__ccp__call__control__server.md#gaa2486dec8a47bd7f4cd4076477e8ac4a)

int bt\_ccp\_call\_control\_server\_unregister\_bearer(struct bt\_ccp\_call\_control\_server\_bearer \*bearer)

Unregister a Telephone Bearer.

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[slist.h](slist_8h.md)

[stdint.h](stdint_8h.md)

[bt\_ccp\_call\_control\_client\_bearers](structbt__ccp__call__control__client__bearers.md)

Struct with information about bearers of a client.

**Definition** ccp.h:109

[bt\_ccp\_call\_control\_client\_cb](structbt__ccp__call__control__client__cb.md)

Struct to hold the Telephone Bearer Service client callbacks.

**Definition** ccp.h:130

[bt\_ccp\_call\_control\_client\_cb::discover](structbt__ccp__call__control__client__cb.md#a322f75bc9d28efc74f9a4571e952ed5e)

void(\* discover)(struct bt\_ccp\_call\_control\_client \*client, int err, struct bt\_ccp\_call\_control\_client\_bearers \*bearers)

Callback function for bt\_ccp\_call\_control\_client\_discover().

**Definition** ccp.h:141

[bt\_tbs\_register\_param](structbt__tbs__register__param.md)

Parameters for registering a Telephone Bearer Service.

**Definition** tbs.h:466

[tbs.h](tbs_8h.md)

Public APIs for Bluetooth Telephone Bearer Service.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [ccp.h](ccp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
