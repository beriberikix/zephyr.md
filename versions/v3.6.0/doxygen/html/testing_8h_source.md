---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/testing_8h_source.html
original_path: doxygen/html/testing_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

testing.h

[Go to the documentation of this file.](testing_8h.md)

1

5

6/\*

7 \* Copyright (c) 2017 Intel Corporation

8 \*

9 \* SPDX-License-Identifier: Apache-2.0

10 \*/

11#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_TESTING\_H\_

12#define ZEPHYR\_INCLUDE\_BLUETOOTH\_TESTING\_H\_

13

14#include <[stdint.h](stdint_8h.md)>

15

16#if defined(CONFIG\_BT\_MESH)

17#include <[zephyr/bluetooth/mesh.h](mesh_8h.md)>

18#endif /\* CONFIG\_BT\_MESH \*/

19

26

27#ifdef \_\_cplusplus

28extern "C" {

29#endif

30

[ 36](structbt__test__cb.md)struct [bt\_test\_cb](structbt__test__cb.md) {

37#if defined(CONFIG\_BT\_MESH)

38 void (\*mesh\_net\_recv)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ttl, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ctl, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) src, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dst,

39 const void \*payload, size\_t payload\_len);

40 void (\*mesh\_model\_recv)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) src, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dst, const void \*payload,

41 size\_t payload\_len);

42 void (\*mesh\_model\_bound)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model,

43 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_idx);

44 void (\*mesh\_model\_unbound)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, const struct [bt\_mesh\_model](structbt__mesh__model.md) \*model,

45 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_idx);

46 void (\*mesh\_prov\_invalid\_bearer)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) opcode);

47 void (\*mesh\_trans\_incomp\_timer\_exp)(void);

48#endif /\* CONFIG\_BT\_MESH \*/

49

[ 50](structbt__test__cb.md#a278d2594ff7ad63e9b569eeb1dfef636) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structbt__test__cb.md#a278d2594ff7ad63e9b569eeb1dfef636);

51};

52

[ 57](group__bt__test__cb.md#gae1e022f389f26c9505461c31ed01c632)void [bt\_test\_cb\_register](group__bt__test__cb.md#gae1e022f389f26c9505461c31ed01c632)(struct [bt\_test\_cb](structbt__test__cb.md) \*[cb](structbt__mesh__model.md#a67a91d64051e055b79f5d9166ab12660));

58

[ 63](group__bt__test__cb.md#ga2d2c1085532ce33175e20bf6ef48329c)void [bt\_test\_cb\_unregister](group__bt__test__cb.md#ga2d2c1085532ce33175e20bf6ef48329c)(struct [bt\_test\_cb](structbt__test__cb.md) \*[cb](structbt__mesh__model.md#a67a91d64051e055b79f5d9166ab12660));

64

[ 74](group__bt__test__cb.md#gad0590321fdc43ee71b10a9a1d260bb92)int [bt\_test\_mesh\_lpn\_group\_add](group__bt__test__cb.md#gad0590321fdc43ee71b10a9a1d260bb92)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) group);

75

[ 87](group__bt__test__cb.md#gaa33faa58edd5a8bf286815309571baf7)int [bt\_test\_mesh\_lpn\_group\_remove](group__bt__test__cb.md#gaa33faa58edd5a8bf286815309571baf7)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*[groups](structbt__mesh__model.md#a460ab46730afa4f74e4066f787864b0b), size\_t groups\_count);

88

[ 93](group__bt__test__cb.md#ga02e2d32cec7115970a4278d733df1879)int [bt\_test\_mesh\_rpl\_clear](group__bt__test__cb.md#ga02e2d32cec7115970a4278d733df1879)(void);

94

98

99#ifdef \_\_cplusplus

100}

101#endif

102

103#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_TESTING\_H\_ \*/

[bt\_test\_mesh\_rpl\_clear](group__bt__test__cb.md#ga02e2d32cec7115970a4278d733df1879)

int bt\_test\_mesh\_rpl\_clear(void)

Clear replay protection list cache.

[bt\_test\_cb\_unregister](group__bt__test__cb.md#ga2d2c1085532ce33175e20bf6ef48329c)

void bt\_test\_cb\_unregister(struct bt\_test\_cb \*cb)

Unregister callbacks for Bluetooth testing purposes.

[bt\_test\_mesh\_lpn\_group\_remove](group__bt__test__cb.md#gaa33faa58edd5a8bf286815309571baf7)

int bt\_test\_mesh\_lpn\_group\_remove(uint16\_t \*groups, size\_t groups\_count)

Send Friend Subscription List Remove message.

[bt\_test\_mesh\_lpn\_group\_add](group__bt__test__cb.md#gad0590321fdc43ee71b10a9a1d260bb92)

int bt\_test\_mesh\_lpn\_group\_add(uint16\_t group)

Send Friend Subscription List Add message.

[bt\_test\_cb\_register](group__bt__test__cb.md#gae1e022f389f26c9505461c31ed01c632)

void bt\_test\_cb\_register(struct bt\_test\_cb \*cb)

Register callbacks for Bluetooth testing purposes.

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[mesh.h](mesh_8h.md)

Bluetooth Mesh Profile APIs.

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[bt\_mesh\_model](structbt__mesh__model.md)

Abstraction that describes a Mesh Model instance.

**Definition** access.h:881

[bt\_mesh\_model::groups](structbt__mesh__model.md#a460ab46730afa4f74e4066f787864b0b)

uint16\_t \*const groups

Subscription List (group or virtual addresses).

**Definition** access.h:911

[bt\_mesh\_model::cb](structbt__mesh__model.md#a67a91d64051e055b79f5d9166ab12660)

const struct bt\_mesh\_model\_cb \*const cb

Model callback structure.

**Definition** access.h:923

[bt\_test\_cb](structbt__test__cb.md)

Bluetooth Testing callbacks structure.

**Definition** testing.h:36

[bt\_test\_cb::node](structbt__test__cb.md#a278d2594ff7ad63e9b569eeb1dfef636)

sys\_snode\_t node

**Definition** testing.h:50

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [testing.h](testing_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
