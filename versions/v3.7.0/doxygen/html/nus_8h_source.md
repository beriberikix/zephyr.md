---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/nus_8h_source.html
original_path: doxygen/html/nus_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nus.h

[Go to the documentation of this file.](nus_8h.md)

1/\*

2 \* Copyright (c) 2024 Croxel, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_SERVICES\_NUS\_H\_

8#define ZEPHYR\_INCLUDE\_BLUETOOTH\_SERVICES\_NUS\_H\_

9

10#include <[zephyr/bluetooth/uuid.h](uuid_8h.md)>

11#include <[zephyr/bluetooth/services/nus/inst.h](inst_8h.md)>

12#include <[zephyr/sys/slist.h](slist_8h.md)>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

[ 23](nus_8h.md#a8da4aaa9c77a537805c7b5bff7fc4aa6)#define BT\_UUID\_NUS\_SRV\_VAL \

24 BT\_UUID\_128\_ENCODE(0x6e400001, 0xb5a3, 0xf393, 0xe0a9, 0xe50e24dcca9e)

[ 25](nus_8h.md#ada90c739cf936ec52008fcc4f272e207)#define BT\_UUID\_NUS\_RX\_CHAR\_VAL \

26 BT\_UUID\_128\_ENCODE(0x6e400002, 0xb5a3, 0xf393, 0xe0a9, 0xe50e24dcca9e)

[ 27](nus_8h.md#a7636b61879884e6f6fc8e871ae09160b)#define BT\_UUID\_NUS\_TX\_CHAR\_VAL \

28 BT\_UUID\_128\_ENCODE(0x6e400003, 0xb5a3, 0xf393, 0xe0a9, 0xe50e24dcca9e)

29

[ 35](nus_8h.md#a54ba967101dc2a5515b9cfd1272c569b)#define BT\_NUS\_INST\_DEFINE(\_name) \

36 Z\_INTERNAL\_BT\_NUS\_INST\_DEFINE(\_name)

37

[ 39](structbt__nus__cb.md)struct [bt\_nus\_cb](structbt__nus__cb.md) {

[ 46](structbt__nus__cb.md#a3fc8fcca9d16f18c506ad13d2356e32c) void (\*[notif\_enabled](structbt__nus__cb.md#a3fc8fcca9d16f18c506ad13d2356e32c))(bool enabled, void \*[ctx](structbt__nus__cb.md#ab28ef9120ed04be0c7dbdd5c76556864));

47

[ 55](structbt__nus__cb.md#ad95d3bb5f927c25058c4ec6a89c665a4) void (\*[received](structbt__nus__cb.md#ad95d3bb5f927c25058c4ec6a89c665a4))(struct bt\_conn \*conn, const void \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, void \*[ctx](structbt__nus__cb.md#ab28ef9120ed04be0c7dbdd5c76556864));

56

[ 58](structbt__nus__cb.md#ab28ef9120ed04be0c7dbdd5c76556864) void \*[ctx](structbt__nus__cb.md#ab28ef9120ed04be0c7dbdd5c76556864);

59

61 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \_node;

62};

63

[ 77](nus_8h.md#a84cb19f07f861963c73614a04c0a375f)int [bt\_nus\_inst\_cb\_register](nus_8h.md#a84cb19f07f861963c73614a04c0a375f)(struct [bt\_nus\_inst](structbt__nus__inst.md) \*inst, struct [bt\_nus\_cb](structbt__nus__cb.md) \*cb, void \*ctx);

78

[ 93](nus_8h.md#a997453fc8108f64a95186b130ea68076)int [bt\_nus\_inst\_send](nus_8h.md#a997453fc8108f64a95186b130ea68076)(struct bt\_conn \*conn,

94 struct [bt\_nus\_inst](structbt__nus__inst.md) \*inst,

95 const void \*data,

96 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len);

97

[ 107](nus_8h.md#a1a28f3d267b34856450f60803eed485f)static inline int [bt\_nus\_cb\_register](nus_8h.md#a1a28f3d267b34856450f60803eed485f)(struct [bt\_nus\_cb](structbt__nus__cb.md) \*cb, void \*ctx)

108{

109 return [bt\_nus\_inst\_cb\_register](nus_8h.md#a84cb19f07f861963c73614a04c0a375f)(NULL, cb, ctx);

110}

111

[ 125](nus_8h.md#a950188897461f1c1f78ffbabeae1180a)static inline int [bt\_nus\_send](nus_8h.md#a950188897461f1c1f78ffbabeae1180a)(struct bt\_conn \*conn, const void \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len)

126{

127 return [bt\_nus\_inst\_send](nus_8h.md#a997453fc8108f64a95186b130ea68076)(conn, NULL, data, len);

128}

129

130#ifdef \_\_cplusplus

131}

132#endif

133

134

135#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_SERVICES\_NUS\_H\_ \*/

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[inst.h](inst_8h.md)

[bt\_nus\_cb\_register](nus_8h.md#a1a28f3d267b34856450f60803eed485f)

static int bt\_nus\_cb\_register(struct bt\_nus\_cb \*cb, void \*ctx)

NUS server callback register.

**Definition** nus.h:107

[bt\_nus\_inst\_cb\_register](nus_8h.md#a84cb19f07f861963c73614a04c0a375f)

int bt\_nus\_inst\_cb\_register(struct bt\_nus\_inst \*inst, struct bt\_nus\_cb \*cb, void \*ctx)

NUS server Instance callback register.

[bt\_nus\_send](nus_8h.md#a950188897461f1c1f78ffbabeae1180a)

static int bt\_nus\_send(struct bt\_conn \*conn, const void \*data, uint16\_t len)

Send Data over NUS.

**Definition** nus.h:125

[bt\_nus\_inst\_send](nus_8h.md#a997453fc8108f64a95186b130ea68076)

int bt\_nus\_inst\_send(struct bt\_conn \*conn, struct bt\_nus\_inst \*inst, const void \*data, uint16\_t len)

Send Data to NUS Instance.

[slist.h](slist_8h.md)

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[bt\_nus\_cb](structbt__nus__cb.md)

Callbacks for getting notified on NUS Service occurrences.

**Definition** nus.h:39

[bt\_nus\_cb::notif\_enabled](structbt__nus__cb.md#a3fc8fcca9d16f18c506ad13d2356e32c)

void(\* notif\_enabled)(bool enabled, void \*ctx)

Notifications subscription changed.

**Definition** nus.h:46

[bt\_nus\_cb::ctx](structbt__nus__cb.md#ab28ef9120ed04be0c7dbdd5c76556864)

void \* ctx

Internal member.

**Definition** nus.h:58

[bt\_nus\_cb::received](structbt__nus__cb.md#ad95d3bb5f927c25058c4ec6a89c665a4)

void(\* received)(struct bt\_conn \*conn, const void \*data, uint16\_t len, void \*ctx)

Received Data.

**Definition** nus.h:55

[bt\_nus\_inst](structbt__nus__inst.md)

**Definition** inst.h:18

[uuid.h](uuid_8h.md)

Bluetooth UUID handling.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [services](dir_e4028deab123aca136adb6f86dc413ad.md)
- [nus.h](nus_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
