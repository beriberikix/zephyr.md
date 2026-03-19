---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/op__agg__cli_8h_source.html
original_path: doxygen/html/op__agg__cli_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

op\_agg\_cli.h

[Go to the documentation of this file.](op__agg__cli_8h.md)

1/\*

2 \* Copyright (c) 2022 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef BT\_MESH\_OP\_AGG\_CLI\_H\_\_

8#define BT\_MESH\_OP\_AGG\_CLI\_H\_\_

9

10#include <[zephyr/bluetooth/mesh.h](mesh_8h.md)>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

21

[ 26](group__bt__mesh__op__agg__cli.md#ga0a8dec4b4f53d1ec95db1efc4ab22f69)#define BT\_MESH\_MODEL\_OP\_AGG\_CLI \

27 BT\_MESH\_MODEL\_CB(BT\_MESH\_MODEL\_ID\_OP\_AGG\_CLI, \_bt\_mesh\_op\_agg\_cli\_op, \

28 NULL, NULL, &\_bt\_mesh\_op\_agg\_cli\_cb)

29

[ 39](group__bt__mesh__op__agg__cli.md#gac1905d778362faf442a9538adca34a8c)int [bt\_mesh\_op\_agg\_cli\_seq\_start](group__bt__mesh__op__agg__cli.md#gac1905d778362faf442a9538adca34a8c)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) app\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dst,

40 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr);

41

[ 49](group__bt__mesh__op__agg__cli.md#gab151f44fcb5d3f3f0f1dafaf90f05c18)int [bt\_mesh\_op\_agg\_cli\_seq\_send](group__bt__mesh__op__agg__cli.md#gab151f44fcb5d3f3f0f1dafaf90f05c18)(void);

50

[ 53](group__bt__mesh__op__agg__cli.md#ga00b5e695503ba169a1b5ec626413b322)void [bt\_mesh\_op\_agg\_cli\_seq\_abort](group__bt__mesh__op__agg__cli.md#ga00b5e695503ba169a1b5ec626413b322)(void);

54

[ 59](group__bt__mesh__op__agg__cli.md#gadbc347b2dc3d78a4ac71d424f0623b6f)bool [bt\_mesh\_op\_agg\_cli\_seq\_is\_started](group__bt__mesh__op__agg__cli.md#gadbc347b2dc3d78a4ac71d424f0623b6f)(void);

60

[ 65](group__bt__mesh__op__agg__cli.md#ga4269bc6118371e2af0967841b18a02dd)size\_t [bt\_mesh\_op\_agg\_cli\_seq\_tailroom](group__bt__mesh__op__agg__cli.md#ga4269bc6118371e2af0967841b18a02dd)(void);

66

[ 71](group__bt__mesh__op__agg__cli.md#ga83e44b062babcf0bdb343455e3eddf5f)[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [bt\_mesh\_op\_agg\_cli\_timeout\_get](group__bt__mesh__op__agg__cli.md#ga83e44b062babcf0bdb343455e3eddf5f)(void);

72

[ 77](group__bt__mesh__op__agg__cli.md#gaf70cebae8dbd6eb4ef6402585a90e0d5)void [bt\_mesh\_op\_agg\_cli\_timeout\_set](group__bt__mesh__op__agg__cli.md#gaf70cebae8dbd6eb4ef6402585a90e0d5)([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout);

78

80extern const struct [bt\_mesh\_model\_op](structbt__mesh__model__op.md) \_bt\_mesh\_op\_agg\_cli\_op[];

81extern const struct [bt\_mesh\_model\_cb](structbt__mesh__model__cb.md) \_bt\_mesh\_op\_agg\_cli\_cb;

83

87

88#ifdef \_\_cplusplus

89}

90#endif

91

92#endif /\* BT\_MESH\_OP\_AGG\_CLI\_H\_\_ \*/

[bt\_mesh\_op\_agg\_cli\_seq\_abort](group__bt__mesh__op__agg__cli.md#ga00b5e695503ba169a1b5ec626413b322)

void bt\_mesh\_op\_agg\_cli\_seq\_abort(void)

Abort Opcodes Aggregator context.

[bt\_mesh\_op\_agg\_cli\_seq\_tailroom](group__bt__mesh__op__agg__cli.md#ga4269bc6118371e2af0967841b18a02dd)

size\_t bt\_mesh\_op\_agg\_cli\_seq\_tailroom(void)

Get Opcodes Aggregator context tailroom.

[bt\_mesh\_op\_agg\_cli\_timeout\_get](group__bt__mesh__op__agg__cli.md#ga83e44b062babcf0bdb343455e3eddf5f)

int32\_t bt\_mesh\_op\_agg\_cli\_timeout\_get(void)

Get the current transmission timeout value.

[bt\_mesh\_op\_agg\_cli\_seq\_send](group__bt__mesh__op__agg__cli.md#gab151f44fcb5d3f3f0f1dafaf90f05c18)

int bt\_mesh\_op\_agg\_cli\_seq\_send(void)

Opcodes Aggregator message send.

[bt\_mesh\_op\_agg\_cli\_seq\_start](group__bt__mesh__op__agg__cli.md#gac1905d778362faf442a9538adca34a8c)

int bt\_mesh\_op\_agg\_cli\_seq\_start(uint16\_t net\_idx, uint16\_t app\_idx, uint16\_t dst, uint16\_t elem\_addr)

Configure Opcodes Aggregator context.

[bt\_mesh\_op\_agg\_cli\_seq\_is\_started](group__bt__mesh__op__agg__cli.md#gadbc347b2dc3d78a4ac71d424f0623b6f)

bool bt\_mesh\_op\_agg\_cli\_seq\_is\_started(void)

Check if Opcodes Aggregator Sequence context is started.

[bt\_mesh\_op\_agg\_cli\_timeout\_set](group__bt__mesh__op__agg__cli.md#gaf70cebae8dbd6eb4ef6402585a90e0d5)

void bt\_mesh\_op\_agg\_cli\_timeout\_set(int32\_t timeout)

Set the transmission timeout value.

[mesh.h](mesh_8h.md)

Bluetooth Mesh Profile APIs.

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[bt\_mesh\_model\_cb](structbt__mesh__model__cb.md)

Model callback functions.

**Definition** access.h:813

[bt\_mesh\_model\_op](structbt__mesh__model__op.md)

Model opcode handler.

**Definition** access.h:363

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [op\_agg\_cli.h](op__agg__cli_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
