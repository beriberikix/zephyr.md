---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/od__priv__proxy__cli_8h_source.html
original_path: doxygen/html/od__priv__proxy__cli_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

od\_priv\_proxy\_cli.h

[Go to the documentation of this file.](od__priv__proxy__cli_8h.md)

1/\*

2 \* Copyright (c) 2022 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef BT\_MESH\_OD\_PRIV\_PROXY\_CLI\_H\_\_

8#define BT\_MESH\_OD\_PRIV\_PROXY\_CLI\_H\_\_

9

10#include <[zephyr/bluetooth/mesh.h](mesh_8h.md)>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

21

[ 23](structbt__mesh__od__priv__proxy__cli.md)struct [bt\_mesh\_od\_priv\_proxy\_cli](structbt__mesh__od__priv__proxy__cli.md) {

[ 25](structbt__mesh__od__priv__proxy__cli.md#aeab540da0e42de4aa3e1550cd933f805) const struct [bt\_mesh\_model](structbt__mesh__model.md) \*[model](structbt__mesh__od__priv__proxy__cli.md#aeab540da0e42de4aa3e1550cd933f805);

26

27 /\* Internal parameters for tracking message responses. \*/

[ 28](structbt__mesh__od__priv__proxy__cli.md#a8f172612abc904718018a6c2d9002e5e) struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) [ack\_ctx](structbt__mesh__od__priv__proxy__cli.md#a8f172612abc904718018a6c2d9002e5e);

29

[ 39](structbt__mesh__od__priv__proxy__cli.md#aebd18bb98ded2e5dc3fca3fe121f3bc6) void (\*[od\_status](structbt__mesh__od__priv__proxy__cli.md#aebd18bb98ded2e5dc3fca3fe121f3bc6))(struct [bt\_mesh\_od\_priv\_proxy\_cli](structbt__mesh__od__priv__proxy__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

40};

41

[ 45](group__bt__mesh__od__priv__proxy__cli.md#ga037391820efab2b953805f6373431ca9)#define BT\_MESH\_MODEL\_OD\_PRIV\_PROXY\_CLI(cli\_data) \

46 BT\_MESH\_MODEL\_CB(BT\_MESH\_MODEL\_ID\_ON\_DEMAND\_PROXY\_CLI, \

47 \_bt\_mesh\_od\_priv\_proxy\_cli\_op, NULL, cli\_data, \

48 &\_bt\_mesh\_od\_priv\_proxy\_cli\_cb)

49

[ 65](group__bt__mesh__od__priv__proxy__cli.md#ga11357595b2d837f6172a2ec98d1e9973)int [bt\_mesh\_od\_priv\_proxy\_cli\_get](group__bt__mesh__od__priv__proxy__cli.md#ga11357595b2d837f6172a2ec98d1e9973)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*val\_rsp);

66

[ 83](group__bt__mesh__od__priv__proxy__cli.md#ga9b239c221f8c74108e2a7e5276122e1f)int [bt\_mesh\_od\_priv\_proxy\_cli\_set](group__bt__mesh__od__priv__proxy__cli.md#ga9b239c221f8c74108e2a7e5276122e1f)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*val\_rsp);

84

[ 89](group__bt__mesh__od__priv__proxy__cli.md#gad613c78e708f0df5aabda9e16fae6a2c)void [bt\_mesh\_od\_priv\_proxy\_cli\_timeout\_set](group__bt__mesh__od__priv__proxy__cli.md#gad613c78e708f0df5aabda9e16fae6a2c)([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout);

90

92extern const struct [bt\_mesh\_model\_op](structbt__mesh__model__op.md) \_bt\_mesh\_od\_priv\_proxy\_cli\_op[];

93extern const struct [bt\_mesh\_model\_cb](structbt__mesh__model__cb.md) \_bt\_mesh\_od\_priv\_proxy\_cli\_cb;

95

97

98#ifdef \_\_cplusplus

99}

100#endif

101

102#endif /\* BT\_MESH\_OD\_PRIV\_PROXY\_CLI\_H\_\_ \*/

[bt\_mesh\_od\_priv\_proxy\_cli\_get](group__bt__mesh__od__priv__proxy__cli.md#ga11357595b2d837f6172a2ec98d1e9973)

int bt\_mesh\_od\_priv\_proxy\_cli\_get(uint16\_t net\_idx, uint16\_t addr, uint8\_t \*val\_rsp)

Get the target's On-Demand Private GATT Proxy state.

[bt\_mesh\_od\_priv\_proxy\_cli\_set](group__bt__mesh__od__priv__proxy__cli.md#ga9b239c221f8c74108e2a7e5276122e1f)

int bt\_mesh\_od\_priv\_proxy\_cli\_set(uint16\_t net\_idx, uint16\_t addr, uint8\_t val, uint8\_t \*val\_rsp)

Set the target's On-Demand Private GATT Proxy state.

[bt\_mesh\_od\_priv\_proxy\_cli\_timeout\_set](group__bt__mesh__od__priv__proxy__cli.md#gad613c78e708f0df5aabda9e16fae6a2c)

void bt\_mesh\_od\_priv\_proxy\_cli\_timeout\_set(int32\_t timeout)

Set the transmission timeout value.

[mesh.h](mesh_8h.md)

Bluetooth Mesh Profile APIs.

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

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

**Definition** access.h:803

[bt\_mesh\_model\_op](structbt__mesh__model__op.md)

Model opcode handler.

**Definition** access.h:359

[bt\_mesh\_model](structbt__mesh__model.md)

Abstraction that describes a Mesh Model instance.

**Definition** access.h:881

[bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md)

Acknowledged message context for tracking the status of model messages pending a response.

**Definition** msg.h:172

[bt\_mesh\_od\_priv\_proxy\_cli](structbt__mesh__od__priv__proxy__cli.md)

On-Demand Private Proxy Client Model Context.

**Definition** od\_priv\_proxy\_cli.h:23

[bt\_mesh\_od\_priv\_proxy\_cli::ack\_ctx](structbt__mesh__od__priv__proxy__cli.md#a8f172612abc904718018a6c2d9002e5e)

struct bt\_mesh\_msg\_ack\_ctx ack\_ctx

**Definition** od\_priv\_proxy\_cli.h:28

[bt\_mesh\_od\_priv\_proxy\_cli::model](structbt__mesh__od__priv__proxy__cli.md#aeab540da0e42de4aa3e1550cd933f805)

const struct bt\_mesh\_model \* model

Solicitation PDU RPL model entry pointer.

**Definition** od\_priv\_proxy\_cli.h:25

[bt\_mesh\_od\_priv\_proxy\_cli::od\_status](structbt__mesh__od__priv__proxy__cli.md#aebd18bb98ded2e5dc3fca3fe121f3bc6)

void(\* od\_status)(struct bt\_mesh\_od\_priv\_proxy\_cli \*cli, uint16\_t addr, uint8\_t state)

Optional callback for On-Demand Private Proxy Status messages.

**Definition** od\_priv\_proxy\_cli.h:39

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [od\_priv\_proxy\_cli.h](od__priv__proxy__cli_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
