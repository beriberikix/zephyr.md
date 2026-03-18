---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/sar__cfg__cli_8h_source.html
original_path: doxygen/html/sar__cfg__cli_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sar\_cfg\_cli.h

[Go to the documentation of this file.](sar__cfg__cli_8h.md)

1/\*

2 \* Copyright (c) 2021 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

10#ifndef BT\_MESH\_SAR\_CFG\_CLI\_H\_\_

11#define BT\_MESH\_SAR\_CFG\_CLI\_H\_\_

12

13#include <[zephyr/bluetooth/mesh.h](mesh_8h.md)>

14#include <[zephyr/bluetooth/mesh/sar\_cfg.h](sar__cfg_8h.md)>

15

22

23#ifdef \_\_cplusplus

24extern "C" {

25#endif

26

[ 28](structbt__mesh__sar__cfg__cli.md)struct [bt\_mesh\_sar\_cfg\_cli](structbt__mesh__sar__cfg__cli.md) {

[ 30](structbt__mesh__sar__cfg__cli.md#a94056c2b7bfc1b495b5bf7e6a5fe3066) const struct [bt\_mesh\_model](structbt__mesh__model.md) \*[model](structbt__mesh__sar__cfg__cli.md#a94056c2b7bfc1b495b5bf7e6a5fe3066);

31

32 /\* Publication structure instance \*/

[ 33](structbt__mesh__sar__cfg__cli.md#a16a6f6c0b0ac8ae80abfb48a5f231418) struct [bt\_mesh\_model\_pub](structbt__mesh__model__pub.md) [pub](structbt__mesh__sar__cfg__cli.md#a16a6f6c0b0ac8ae80abfb48a5f231418);

34

35 /\* Synchronous message timeout in milliseconds. \*/

[ 36](structbt__mesh__sar__cfg__cli.md#a31fdb2608f2cf80ea17dd1f72e634769) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [timeout](structbt__mesh__sar__cfg__cli.md#a31fdb2608f2cf80ea17dd1f72e634769);

37

38 /\* Internal parameters for tracking message responses. \*/

[ 39](structbt__mesh__sar__cfg__cli.md#a30889368bd4e87efd39b6c456b3510d8) struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) [ack\_ctx](structbt__mesh__sar__cfg__cli.md#a30889368bd4e87efd39b6c456b3510d8);

40};

41

[ 48](group__bt__mesh__sar__cfg__cli.md#ga742d31e7175e472f1a096ffa6a5acdc5)#define BT\_MESH\_MODEL\_SAR\_CFG\_CLI(\_cli) \

49 BT\_MESH\_MODEL\_CB(BT\_MESH\_MODEL\_ID\_SAR\_CFG\_CLI, \

50 \_bt\_mesh\_sar\_cfg\_cli\_op, \_cli.pub, \_cli, \

51 &\_bt\_mesh\_sar\_cfg\_cli\_cb)

52

[ 61](group__bt__mesh__sar__cfg__cli.md#ga893ef5861708bec12f87b9f9cc64b9fc)int [bt\_mesh\_sar\_cfg\_cli\_transmitter\_get](group__bt__mesh__sar__cfg__cli.md#ga893ef5861708bec12f87b9f9cc64b9fc)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

62 struct [bt\_mesh\_sar\_tx](structbt__mesh__sar__tx.md) \*rsp);

63

[ 73](group__bt__mesh__sar__cfg__cli.md#ga32e2a580b24a41761911e88413e9664e)int [bt\_mesh\_sar\_cfg\_cli\_transmitter\_set](group__bt__mesh__sar__cfg__cli.md#ga32e2a580b24a41761911e88413e9664e)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

74 const struct [bt\_mesh\_sar\_tx](structbt__mesh__sar__tx.md) \*set,

75 struct [bt\_mesh\_sar\_tx](structbt__mesh__sar__tx.md) \*rsp);

76

[ 85](group__bt__mesh__sar__cfg__cli.md#ga444c99254ef2ccdd10dac08a94219d79)int [bt\_mesh\_sar\_cfg\_cli\_receiver\_get](group__bt__mesh__sar__cfg__cli.md#ga444c99254ef2ccdd10dac08a94219d79)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

86 struct [bt\_mesh\_sar\_rx](structbt__mesh__sar__rx.md) \*rsp);

87

[ 97](group__bt__mesh__sar__cfg__cli.md#ga884025b2baf8559950ba6dc83e9ef486)int [bt\_mesh\_sar\_cfg\_cli\_receiver\_set](group__bt__mesh__sar__cfg__cli.md#ga884025b2baf8559950ba6dc83e9ef486)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr,

98 const struct [bt\_mesh\_sar\_rx](structbt__mesh__sar__rx.md) \*set,

99 struct [bt\_mesh\_sar\_rx](structbt__mesh__sar__rx.md) \*rsp);

100

[ 105](group__bt__mesh__sar__cfg__cli.md#ga998846e5735676dc5f79b387d02630d4)[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [bt\_mesh\_sar\_cfg\_cli\_timeout\_get](group__bt__mesh__sar__cfg__cli.md#ga998846e5735676dc5f79b387d02630d4)(void);

106

[ 111](group__bt__mesh__sar__cfg__cli.md#ga57d7c6a973b35f53689cbf8a065a538f)void [bt\_mesh\_sar\_cfg\_cli\_timeout\_set](group__bt__mesh__sar__cfg__cli.md#ga57d7c6a973b35f53689cbf8a065a538f)([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout);

112

114extern const struct [bt\_mesh\_model\_op](structbt__mesh__model__op.md) \_bt\_mesh\_sar\_cfg\_cli\_op[];

115extern const struct [bt\_mesh\_model\_cb](structbt__mesh__model__cb.md) \_bt\_mesh\_sar\_cfg\_cli\_cb;

117

118#ifdef \_\_cplusplus

119}

120#endif

121

122#endif /\* BT\_MESH\_SAR\_CFG\_CLI\_H\_\_ \*/

123

[bt\_mesh\_sar\_cfg\_cli\_transmitter\_set](group__bt__mesh__sar__cfg__cli.md#ga32e2a580b24a41761911e88413e9664e)

int bt\_mesh\_sar\_cfg\_cli\_transmitter\_set(uint16\_t net\_idx, uint16\_t addr, const struct bt\_mesh\_sar\_tx \*set, struct bt\_mesh\_sar\_tx \*rsp)

Set the SAR Transmitter state of the target node.

[bt\_mesh\_sar\_cfg\_cli\_receiver\_get](group__bt__mesh__sar__cfg__cli.md#ga444c99254ef2ccdd10dac08a94219d79)

int bt\_mesh\_sar\_cfg\_cli\_receiver\_get(uint16\_t net\_idx, uint16\_t addr, struct bt\_mesh\_sar\_rx \*rsp)

Get the SAR Receiver state of the target node.

[bt\_mesh\_sar\_cfg\_cli\_timeout\_set](group__bt__mesh__sar__cfg__cli.md#ga57d7c6a973b35f53689cbf8a065a538f)

void bt\_mesh\_sar\_cfg\_cli\_timeout\_set(int32\_t timeout)

Set the transmission timeout value.

[bt\_mesh\_sar\_cfg\_cli\_receiver\_set](group__bt__mesh__sar__cfg__cli.md#ga884025b2baf8559950ba6dc83e9ef486)

int bt\_mesh\_sar\_cfg\_cli\_receiver\_set(uint16\_t net\_idx, uint16\_t addr, const struct bt\_mesh\_sar\_rx \*set, struct bt\_mesh\_sar\_rx \*rsp)

Set the SAR Receiver state of the target node.

[bt\_mesh\_sar\_cfg\_cli\_transmitter\_get](group__bt__mesh__sar__cfg__cli.md#ga893ef5861708bec12f87b9f9cc64b9fc)

int bt\_mesh\_sar\_cfg\_cli\_transmitter\_get(uint16\_t net\_idx, uint16\_t addr, struct bt\_mesh\_sar\_tx \*rsp)

Get the SAR Transmitter state of the target node.

[bt\_mesh\_sar\_cfg\_cli\_timeout\_get](group__bt__mesh__sar__cfg__cli.md#ga998846e5735676dc5f79b387d02630d4)

int32\_t bt\_mesh\_sar\_cfg\_cli\_timeout\_get(void)

Get the current transmission timeout value.

[mesh.h](mesh_8h.md)

Bluetooth Mesh Profile APIs.

[sar\_cfg.h](sar__cfg_8h.md)

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[bt\_mesh\_model\_cb](structbt__mesh__model__cb.md)

Model callback functions.

**Definition** access.h:803

[bt\_mesh\_model\_op](structbt__mesh__model__op.md)

Model opcode handler.

**Definition** access.h:359

[bt\_mesh\_model\_pub](structbt__mesh__model__pub.md)

Model publication context.

**Definition** access.h:698

[bt\_mesh\_model](structbt__mesh__model.md)

Abstraction that describes a Mesh Model instance.

**Definition** access.h:881

[bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md)

Acknowledged message context for tracking the status of model messages pending a response.

**Definition** msg.h:172

[bt\_mesh\_sar\_cfg\_cli](structbt__mesh__sar__cfg__cli.md)

Mesh SAR Configuration Client Model Context.

**Definition** sar\_cfg\_cli.h:28

[bt\_mesh\_sar\_cfg\_cli::pub](structbt__mesh__sar__cfg__cli.md#a16a6f6c0b0ac8ae80abfb48a5f231418)

struct bt\_mesh\_model\_pub pub

**Definition** sar\_cfg\_cli.h:33

[bt\_mesh\_sar\_cfg\_cli::ack\_ctx](structbt__mesh__sar__cfg__cli.md#a30889368bd4e87efd39b6c456b3510d8)

struct bt\_mesh\_msg\_ack\_ctx ack\_ctx

**Definition** sar\_cfg\_cli.h:39

[bt\_mesh\_sar\_cfg\_cli::timeout](structbt__mesh__sar__cfg__cli.md#a31fdb2608f2cf80ea17dd1f72e634769)

int32\_t timeout

**Definition** sar\_cfg\_cli.h:36

[bt\_mesh\_sar\_cfg\_cli::model](structbt__mesh__sar__cfg__cli.md#a94056c2b7bfc1b495b5bf7e6a5fe3066)

const struct bt\_mesh\_model \* model

Access model pointer.

**Definition** sar\_cfg\_cli.h:30

[bt\_mesh\_sar\_rx](structbt__mesh__sar__rx.md)

SAR Receiver Configuration state structure.

**Definition** sar\_cfg.h:47

[bt\_mesh\_sar\_tx](structbt__mesh__sar__tx.md)

SAR Transmitter Configuration state structure.

**Definition** sar\_cfg.h:23

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [sar\_cfg\_cli.h](sar__cfg__cli_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
