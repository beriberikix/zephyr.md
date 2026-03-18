---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/sol__pdu__rpl__cli_8h_source.html
original_path: doxygen/html/sol__pdu__rpl__cli_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sol\_pdu\_rpl\_cli.h

[Go to the documentation of this file.](sol__pdu__rpl__cli_8h.md)

1/\*

2 \* Copyright (c) 2022 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef BT\_MESH\_SOL\_PDU\_RPL\_CLI\_H\_\_

8#define BT\_MESH\_SOL\_PDU\_RPL\_CLI\_H\_\_

9

10#include <[zephyr/bluetooth/mesh.h](mesh_8h.md)>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

21

[ 23](structbt__mesh__sol__pdu__rpl__cli.md)struct [bt\_mesh\_sol\_pdu\_rpl\_cli](structbt__mesh__sol__pdu__rpl__cli.md) {

[ 25](structbt__mesh__sol__pdu__rpl__cli.md#a272ff5ae0930f51c9175d99f5c9066e2) const struct [bt\_mesh\_model](structbt__mesh__model.md) \*[model](structbt__mesh__sol__pdu__rpl__cli.md#a272ff5ae0930f51c9175d99f5c9066e2);

26

27 /\* Internal parameters for tracking message responses. \*/

[ 28](structbt__mesh__sol__pdu__rpl__cli.md#a291134f4b6acc60671307ef3b53c4ac8) struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) [ack\_ctx](structbt__mesh__sol__pdu__rpl__cli.md#a291134f4b6acc60671307ef3b53c4ac8);

29

[ 41](structbt__mesh__sol__pdu__rpl__cli.md#a6c734589ee3361bfc071da55521a6dee) void (\*[srpl\_status](structbt__mesh__sol__pdu__rpl__cli.md#a6c734589ee3361bfc071da55521a6dee))(struct [bt\_mesh\_sol\_pdu\_rpl\_cli](structbt__mesh__sol__pdu__rpl__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

42 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) range\_start, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) range\_length);

43};

44

[ 48](group__bt__mesh__sol__pdu__rpl__cli.md#gac5969e20994b07977484391ac2d7bacb)#define BT\_MESH\_MODEL\_SOL\_PDU\_RPL\_CLI(cli\_data) \

49 BT\_MESH\_MODEL\_CB(BT\_MESH\_MODEL\_ID\_SOL\_PDU\_RPL\_CLI, \

50 \_bt\_mesh\_sol\_pdu\_rpl\_cli\_op, NULL, cli\_data, \

51 &\_bt\_mesh\_sol\_pdu\_rpl\_cli\_cb)

52

[ 71](group__bt__mesh__sol__pdu__rpl__cli.md#gae7e8a0e364c6695a467a64cd89627d81)int [bt\_mesh\_sol\_pdu\_rpl\_clear](group__bt__mesh__sol__pdu__rpl__cli.md#gae7e8a0e364c6695a467a64cd89627d81)(struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) range\_start,

72 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) range\_len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*start\_rsp, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*len\_rsp);

73

74

[ 84](group__bt__mesh__sol__pdu__rpl__cli.md#ga68fb70fbfb87e76ef6fdb5ac8a1a9506)int [bt\_mesh\_sol\_pdu\_rpl\_clear\_unack](group__bt__mesh__sol__pdu__rpl__cli.md#ga68fb70fbfb87e76ef6fdb5ac8a1a9506)(struct [bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md) \*ctx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) range\_start,

85 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) range\_len);

86

[ 91](group__bt__mesh__sol__pdu__rpl__cli.md#gadabdbd95f39a498307e3ca9e50acfeb9)void [bt\_mesh\_sol\_pdu\_rpl\_cli\_timeout\_set](group__bt__mesh__sol__pdu__rpl__cli.md#gadabdbd95f39a498307e3ca9e50acfeb9)([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout);

92

94extern const struct [bt\_mesh\_model\_op](structbt__mesh__model__op.md) \_bt\_mesh\_sol\_pdu\_rpl\_cli\_op[];

95extern const struct [bt\_mesh\_model\_cb](structbt__mesh__model__cb.md) \_bt\_mesh\_sol\_pdu\_rpl\_cli\_cb;

97

99

100#ifdef \_\_cplusplus

101}

102#endif

103

104#endif /\* BT\_MESH\_SOL\_PDU\_RPL\_CLI\_H\_\_ \*/

[bt\_mesh\_sol\_pdu\_rpl\_clear\_unack](group__bt__mesh__sol__pdu__rpl__cli.md#ga68fb70fbfb87e76ef6fdb5ac8a1a9506)

int bt\_mesh\_sol\_pdu\_rpl\_clear\_unack(struct bt\_mesh\_msg\_ctx \*ctx, uint16\_t range\_start, uint8\_t range\_len)

Remove entries from Solicitation PDU RPL of addresses in given range (unacked).

[bt\_mesh\_sol\_pdu\_rpl\_cli\_timeout\_set](group__bt__mesh__sol__pdu__rpl__cli.md#gadabdbd95f39a498307e3ca9e50acfeb9)

void bt\_mesh\_sol\_pdu\_rpl\_cli\_timeout\_set(int32\_t timeout)

Set the transmission timeout value.

[bt\_mesh\_sol\_pdu\_rpl\_clear](group__bt__mesh__sol__pdu__rpl__cli.md#gae7e8a0e364c6695a467a64cd89627d81)

int bt\_mesh\_sol\_pdu\_rpl\_clear(struct bt\_mesh\_msg\_ctx \*ctx, uint16\_t range\_start, uint8\_t range\_len, uint16\_t \*start\_rsp, uint8\_t \*len\_rsp)

Remove entries from Solicitation PDU RPL of addresses in given range.

[mesh.h](mesh_8h.md)

Bluetooth Mesh Profile APIs.

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[bt\_mesh\_model\_cb](structbt__mesh__model__cb.md)

Model callback functions.

**Definition** access.h:809

[bt\_mesh\_model\_op](structbt__mesh__model__op.md)

Model opcode handler.

**Definition** access.h:359

[bt\_mesh\_model](structbt__mesh__model.md)

Abstraction that describes a Mesh Model instance.

**Definition** access.h:887

[bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md)

Acknowledged message context for tracking the status of model messages pending a response.

**Definition** msg.h:172

[bt\_mesh\_msg\_ctx](structbt__mesh__msg__ctx.md)

Message sending context.

**Definition** msg.h:76

[bt\_mesh\_sol\_pdu\_rpl\_cli](structbt__mesh__sol__pdu__rpl__cli.md)

Solicitation PDU RPL Client Model Context.

**Definition** sol\_pdu\_rpl\_cli.h:23

[bt\_mesh\_sol\_pdu\_rpl\_cli::model](structbt__mesh__sol__pdu__rpl__cli.md#a272ff5ae0930f51c9175d99f5c9066e2)

const struct bt\_mesh\_model \* model

Solicitation PDU RPL model entry pointer.

**Definition** sol\_pdu\_rpl\_cli.h:25

[bt\_mesh\_sol\_pdu\_rpl\_cli::ack\_ctx](structbt__mesh__sol__pdu__rpl__cli.md#a291134f4b6acc60671307ef3b53c4ac8)

struct bt\_mesh\_msg\_ack\_ctx ack\_ctx

**Definition** sol\_pdu\_rpl\_cli.h:28

[bt\_mesh\_sol\_pdu\_rpl\_cli::srpl\_status](structbt__mesh__sol__pdu__rpl__cli.md#a6c734589ee3361bfc071da55521a6dee)

void(\* srpl\_status)(struct bt\_mesh\_sol\_pdu\_rpl\_cli \*cli, uint16\_t addr, uint16\_t range\_start, uint8\_t range\_length)

Optional callback for Solicitation PDU RPL Status messages.

**Definition** sol\_pdu\_rpl\_cli.h:41

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [sol\_pdu\_rpl\_cli.h](sol__pdu__rpl__cli_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
