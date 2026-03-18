---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/bluetooth_2mesh_2shell_8h_source.html
original_path: doxygen/html/bluetooth_2mesh_2shell_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell.h

[Go to the documentation of this file.](bluetooth_2mesh_2shell_8h.md)

1/\*

2 \* Copyright (c) 2021 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_SHELL\_H\_

7#define ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_SHELL\_H\_

8

9#include <[zephyr/bluetooth/mesh.h](mesh_8h.md)>

10

11#ifdef \_\_cplusplus

12extern "C" {

13#endif

14

[ 16](bluetooth_2mesh_2shell_8h.md#aac63a324676ab3297e509fc5d1afe951)#define BT\_MESH\_SHELL\_CUR\_FAULTS\_MAX 4

17

[ 24](bluetooth_2mesh_2shell_8h.md#a8cd77ce286185c704e64c891d315a1d0)#define BT\_MESH\_SHELL\_HEALTH\_PUB\_DEFINE(\_name) \

25 BT\_MESH\_HEALTH\_PUB\_DEFINE(\_name, \

26 BT\_MESH\_SHELL\_CUR\_FAULTS\_MAX);

27

[ 29](structbt__mesh__shell__target.md)struct [bt\_mesh\_shell\_target](structbt__mesh__shell__target.md) {

30 /\* Current destination address \*/

[ 31](structbt__mesh__shell__target.md#a48a9039d99fefb8a536c427161359485) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [dst](structbt__mesh__shell__target.md#a48a9039d99fefb8a536c427161359485);

32 /\* Current net index \*/

[ 33](structbt__mesh__shell__target.md#a2cb816bbfd493656d327cd604254fdbd) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_idx](structbt__mesh__shell__target.md#a2cb816bbfd493656d327cd604254fdbd);

34 /\* Current app index \*/

[ 35](structbt__mesh__shell__target.md#a52c511cf9843512ec6d8db7cec6f6fa1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [app\_idx](structbt__mesh__shell__target.md#a52c511cf9843512ec6d8db7cec6f6fa1);

36};

37

39extern struct [bt\_mesh\_health\_srv](structbt__mesh__health__srv.md) [bt\_mesh\_shell\_health\_srv](bluetooth_2mesh_2shell_8h.md#a313cd00833d5b522a73a3ac5e4eb9596);

40

42extern const struct [bt\_mesh\_models\_metadata\_entry](structbt__mesh__models__metadata__entry.md) [health\_srv\_meta](bluetooth_2mesh_2shell_8h.md#a5ccd2d0b4a3ff642a89fcd77dd0e935f)[];

43

45extern struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) [bt\_mesh\_shell\_health\_cli](bluetooth_2mesh_2shell_8h.md#a4c7a470a6d7cc91ea1b240756053d017);

46

48extern struct [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) [bt\_mesh\_shell\_dfu\_srv](bluetooth_2mesh_2shell_8h.md#a0bac1827aa84e4801252c9b955373067);

49

51extern struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) [bt\_mesh\_shell\_dfu\_cli](bluetooth_2mesh_2shell_8h.md#a9bc67c98117f6a8741bbd3e40f718b3b);

52

54extern struct [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md) [bt\_mesh\_shell\_blob\_srv](bluetooth_2mesh_2shell_8h.md#a4c4b37f663428cedfb466832963b9c1b);

55

57extern struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) [bt\_mesh\_shell\_blob\_cli](bluetooth_2mesh_2shell_8h.md#accbfc012251815338ace23f8cb49fff6);

58

60extern struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) [bt\_mesh\_shell\_rpr\_cli](bluetooth_2mesh_2shell_8h.md#a231f1c8492097ae23edb2aeb82139752);

61

63extern struct [bt\_mesh\_prov](structbt__mesh__prov.md) [bt\_mesh\_shell\_prov](bluetooth_2mesh_2shell_8h.md#a1e999cded973436a218782acac1ab15b);

64

66extern struct [bt\_mesh\_shell\_target](structbt__mesh__shell__target.md) [bt\_mesh\_shell\_target\_ctx](bluetooth_2mesh_2shell_8h.md#ab76d90bc284131a56904a2c1b9c19ae2);

67

68#ifdef \_\_cplusplus

69}

70#endif

71

72#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_SHELL\_H\_ \*/

[bt\_mesh\_shell\_dfu\_srv](bluetooth_2mesh_2shell_8h.md#a0bac1827aa84e4801252c9b955373067)

struct bt\_mesh\_dfu\_srv bt\_mesh\_shell\_dfu\_srv

External reference to Firmware Update Server.

[bt\_mesh\_shell\_prov](bluetooth_2mesh_2shell_8h.md#a1e999cded973436a218782acac1ab15b)

struct bt\_mesh\_prov bt\_mesh\_shell\_prov

External reference to provisioning handler.

[bt\_mesh\_shell\_rpr\_cli](bluetooth_2mesh_2shell_8h.md#a231f1c8492097ae23edb2aeb82139752)

struct bt\_mesh\_rpr\_cli bt\_mesh\_shell\_rpr\_cli

External reference to Remote Provisioning Client.

[bt\_mesh\_shell\_health\_srv](bluetooth_2mesh_2shell_8h.md#a313cd00833d5b522a73a3ac5e4eb9596)

struct bt\_mesh\_health\_srv bt\_mesh\_shell\_health\_srv

External reference to health server.

[bt\_mesh\_shell\_blob\_srv](bluetooth_2mesh_2shell_8h.md#a4c4b37f663428cedfb466832963b9c1b)

struct bt\_mesh\_blob\_srv bt\_mesh\_shell\_blob\_srv

External reference to BLOB Transfer Server.

[bt\_mesh\_shell\_health\_cli](bluetooth_2mesh_2shell_8h.md#a4c7a470a6d7cc91ea1b240756053d017)

struct bt\_mesh\_health\_cli bt\_mesh\_shell\_health\_cli

External reference to health client.

[health\_srv\_meta](bluetooth_2mesh_2shell_8h.md#a5ccd2d0b4a3ff642a89fcd77dd0e935f)

const struct bt\_mesh\_models\_metadata\_entry health\_srv\_meta[]

External reference to health server metadata.

[bt\_mesh\_shell\_dfu\_cli](bluetooth_2mesh_2shell_8h.md#a9bc67c98117f6a8741bbd3e40f718b3b)

struct bt\_mesh\_dfu\_cli bt\_mesh\_shell\_dfu\_cli

External reference to Firmware Update Client.

[bt\_mesh\_shell\_target\_ctx](bluetooth_2mesh_2shell_8h.md#ab76d90bc284131a56904a2c1b9c19ae2)

struct bt\_mesh\_shell\_target bt\_mesh\_shell\_target\_ctx

External reference to shell target context.

[bt\_mesh\_shell\_blob\_cli](bluetooth_2mesh_2shell_8h.md#accbfc012251815338ace23f8cb49fff6)

struct bt\_mesh\_blob\_cli bt\_mesh\_shell\_blob\_cli

External reference to BLOB Transfer Client.

[mesh.h](mesh_8h.md)

Bluetooth Mesh Profile APIs.

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md)

BLOB Transfer Client model instance.

**Definition** blob\_cli.h:289

[bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md)

BLOB Transfer Server instance.

**Definition** blob\_srv.h:131

[bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md)

Firmware Update Client model instance.

**Definition** dfu\_cli.h:184

[bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md)

Firmware Update Server instance.

**Definition** dfu\_srv.h:176

[bt\_mesh\_health\_cli](structbt__mesh__health__cli.md)

Health Client Model Context.

**Definition** health\_cli.h:27

[bt\_mesh\_health\_srv](structbt__mesh__health__srv.md)

Mesh Health Server Model Context.

**Definition** health\_srv.h:150

[bt\_mesh\_models\_metadata\_entry](structbt__mesh__models__metadata__entry.md)

Models Metadata Entry struct.

**Definition** access.h:778

[bt\_mesh\_prov](structbt__mesh__prov.md)

Provisioning properties & capabilities.

**Definition** main.h:115

[bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md)

Remote Provisioning Client model instance.

**Definition** rpr\_cli.h:64

[bt\_mesh\_shell\_target](structbt__mesh__shell__target.md)

Target context for the mesh shell.

**Definition** shell.h:29

[bt\_mesh\_shell\_target::net\_idx](structbt__mesh__shell__target.md#a2cb816bbfd493656d327cd604254fdbd)

uint16\_t net\_idx

**Definition** shell.h:33

[bt\_mesh\_shell\_target::dst](structbt__mesh__shell__target.md#a48a9039d99fefb8a536c427161359485)

uint16\_t dst

**Definition** shell.h:31

[bt\_mesh\_shell\_target::app\_idx](structbt__mesh__shell__target.md#a52c511cf9843512ec6d8db7cec6f6fa1)

uint16\_t app\_idx

**Definition** shell.h:35

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [shell.h](bluetooth_2mesh_2shell_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
