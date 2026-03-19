---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/inst_8h_source.html
original_path: doxygen/html/inst_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

inst.h

[Go to the documentation of this file.](inst_8h.md)

1/\*

2 \* Copyright (c) 2024 Croxel, Inc.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_SERVICES\_NUS\_INST\_H\_

8#define ZEPHYR\_INCLUDE\_BLUETOOTH\_SERVICES\_NUS\_INST\_H\_

9

10#include <[zephyr/bluetooth/gatt.h](gatt_8h.md)>

11#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

12#include <[zephyr/sys/slist.h](slist_8h.md)>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

[ 18](structbt__nus__inst.md)struct [bt\_nus\_inst](structbt__nus__inst.md) {

[ 20](structbt__nus__inst.md#a3a3dd0e1f20e47a39124f10982a6be59) const struct [bt\_gatt\_service\_static](structbt__gatt__service__static.md) \*[svc](structbt__nus__inst.md#a3a3dd0e1f20e47a39124f10982a6be59);

21

[ 23](structbt__nus__inst.md#a47c7d47a0cbad0e5696c64e3592de776) [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \*[cbs](structbt__nus__inst.md#a47c7d47a0cbad0e5696c64e3592de776);

24};

25

[ 26](inst_8h.md#a3752da6f7063510a04551609672b2583)#define BT\_UUID\_NUS\_SERVICE BT\_UUID\_DECLARE\_128(BT\_UUID\_NUS\_SRV\_VAL)

[ 27](inst_8h.md#ad652d719c4f193d433156afcb3d8fe87)#define BT\_UUID\_NUS\_TX\_CHAR BT\_UUID\_DECLARE\_128(BT\_UUID\_NUS\_TX\_CHAR\_VAL)

[ 28](inst_8h.md#aa9e0e0a89747210a3ebc36d85ce973d2)#define BT\_UUID\_NUS\_RX\_CHAR BT\_UUID\_DECLARE\_128(BT\_UUID\_NUS\_RX\_CHAR\_VAL)

29

[ 31](inst_8h.md#a3bb5cd4e4367d402f377cee751f9b434)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [nus\_bt\_chr\_write](inst_8h.md#a3bb5cd4e4367d402f377cee751f9b434)(struct bt\_conn \*conn, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr,

32 const void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

[ 33](inst_8h.md#a964bdf4d6c01f257533c0a5c337f562e)void [nus\_ccc\_cfg\_changed](inst_8h.md#a964bdf4d6c01f257533c0a5c337f562e)(const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) value);

34

35#define Z\_INTERNAL\_BT\_NUS\_INST\_DEFINE(\_name) \

36 \

37BT\_GATT\_SERVICE\_DEFINE(\_name##\_svc, \

38 BT\_GATT\_PRIMARY\_SERVICE(BT\_UUID\_NUS\_SERVICE), \

39 BT\_GATT\_CHARACTERISTIC(BT\_UUID\_NUS\_TX\_CHAR, \

40 BT\_GATT\_CHRC\_NOTIFY, \

41 BT\_GATT\_PERM\_NONE, \

42 NULL, NULL, NULL), \

43 BT\_GATT\_CCC(nus\_ccc\_cfg\_changed, \

44 BT\_GATT\_PERM\_READ | BT\_GATT\_PERM\_WRITE), \

45 BT\_GATT\_CHARACTERISTIC(BT\_UUID\_NUS\_RX\_CHAR, \

46 BT\_GATT\_CHRC\_WRITE | \

47 BT\_GATT\_CHRC\_WRITE\_WITHOUT\_RESP, \

48 BT\_GATT\_PERM\_WRITE, \

49 NULL, nus\_bt\_chr\_write, NULL), \

50); \

51 \

52sys\_slist\_t \_name##\_cbs = SYS\_SLIST\_STATIC\_INIT(&\_name##\_cbs); \

53 \

54STRUCT\_SECTION\_ITERABLE(bt\_nus\_inst, \_name) = { \

55 .svc = &\_name##\_svc, \

56 .cbs = &\_name##\_cbs, \

57}

58

59#ifdef \_\_cplusplus

60}

61#endif

62

63#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_SERVICES\_NUS\_INST\_H\_ \*/

[gatt.h](gatt_8h.md)

Generic Attribute Profile handling.

[sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8)

struct \_slist sys\_slist\_t

Single-linked list structure.

**Definition** slist.h:49

[nus\_bt\_chr\_write](inst_8h.md#a3bb5cd4e4367d402f377cee751f9b434)

ssize\_t nus\_bt\_chr\_write(struct bt\_conn \*conn, const struct bt\_gatt\_attr \*attr, const void \*buf, uint16\_t len, uint16\_t offset, uint8\_t flags)

Required as the service may be instantiated outside of the module.

[nus\_ccc\_cfg\_changed](inst_8h.md#a964bdf4d6c01f257533c0a5c337f562e)

void nus\_ccc\_cfg\_changed(const struct bt\_gatt\_attr \*attr, uint16\_t value)

[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)

\_\_SIZE\_TYPE\_\_ ssize\_t

**Definition** types.h:28

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[slist.h](slist_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[bt\_gatt\_attr](structbt__gatt__attr.md)

GATT Attribute.

**Definition** gatt.h:224

[bt\_gatt\_service\_static](structbt__gatt__service__static.md)

GATT Service structure.

**Definition** gatt.h:304

[bt\_nus\_inst](structbt__nus__inst.md)

**Definition** inst.h:18

[bt\_nus\_inst::svc](structbt__nus__inst.md#a3a3dd0e1f20e47a39124f10982a6be59)

const struct bt\_gatt\_service\_static \* svc

Pointer to the NUS Service Instance.

**Definition** inst.h:20

[bt\_nus\_inst::cbs](structbt__nus__inst.md#a47c7d47a0cbad0e5696c64e3592de776)

sys\_slist\_t \* cbs

List of subscribers to invoke callbacks on asynchronous events.

**Definition** inst.h:23

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [services](dir_e4028deab123aca136adb6f86dc413ad.md)
- [nus](dir_41b6aa38490ac2da296b10fec5e4989c.md)
- [inst.h](inst_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
