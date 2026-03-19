---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/rfcomm_8h_source.html
original_path: doxygen/html/rfcomm_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rfcomm.h

[Go to the documentation of this file.](rfcomm_8h.md)

1

4

5/\*

6 \* Copyright (c) 2015-2016 Intel Corporation

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_RFCOMM\_H\_

11#define ZEPHYR\_INCLUDE\_BLUETOOTH\_RFCOMM\_H\_

12

19

20#include <[zephyr/bluetooth/buf.h](bluetooth_2buf_8h.md)>

21#include <[zephyr/bluetooth/conn.h](conn_8h.md)>

22#include <[zephyr/bluetooth/l2cap.h](l2cap_8h.md)>

23

24#ifdef \_\_cplusplus

25extern "C" {

26#endif

27

[ 29](group__bt__rfcomm.md#ga8d7b15c80fc69a25b105aadf6f3a6a6d)#define BT\_RFCOMM\_HDR\_MAX\_SIZE 4

[ 31](group__bt__rfcomm.md#gaea26fe8eac8c5792a4cb78404dc4f7c1)#define BT\_RFCOMM\_FCS\_SIZE 1

32

[ 40](group__bt__rfcomm.md#gabb568d7f32dbd0720f203538e3aa345c)#define BT\_RFCOMM\_BUF\_SIZE(mtu) \

41 BT\_L2CAP\_BUF\_SIZE(BT\_RFCOMM\_HDR\_MAX\_SIZE + BT\_RFCOMM\_FCS\_SIZE + (mtu))

42

43/\* RFCOMM channels (1-30): pre-allocated for profiles to avoid conflicts \*/

44enum {

[ 45](group__bt__rfcomm.md#ggafccaaeb8f4d4f3e3834f358ccfdfb86baa62985d89ab11a130eed284d98b7b1e4) [BT\_RFCOMM\_CHAN\_HFP\_HF](group__bt__rfcomm.md#ggafccaaeb8f4d4f3e3834f358ccfdfb86baa62985d89ab11a130eed284d98b7b1e4) = 1,

[ 46](group__bt__rfcomm.md#ggafccaaeb8f4d4f3e3834f358ccfdfb86bac7f345a01b4d9aca4c2a879dce05e0dd) [BT\_RFCOMM\_CHAN\_HFP\_AG](group__bt__rfcomm.md#ggafccaaeb8f4d4f3e3834f358ccfdfb86bac7f345a01b4d9aca4c2a879dce05e0dd),

[ 47](group__bt__rfcomm.md#ggafccaaeb8f4d4f3e3834f358ccfdfb86badc095ec30d3edf16ef95ece5b3c1104b) [BT\_RFCOMM\_CHAN\_HSP\_AG](group__bt__rfcomm.md#ggafccaaeb8f4d4f3e3834f358ccfdfb86badc095ec30d3edf16ef95ece5b3c1104b),

[ 48](group__bt__rfcomm.md#ggafccaaeb8f4d4f3e3834f358ccfdfb86baaf92af85143e2a0430d5a99c9a0d3c25) [BT\_RFCOMM\_CHAN\_HSP\_HS](group__bt__rfcomm.md#ggafccaaeb8f4d4f3e3834f358ccfdfb86baaf92af85143e2a0430d5a99c9a0d3c25),

[ 49](group__bt__rfcomm.md#ggafccaaeb8f4d4f3e3834f358ccfdfb86ba05cfd05b25c785acb72916b723141495) [BT\_RFCOMM\_CHAN\_SPP](group__bt__rfcomm.md#ggafccaaeb8f4d4f3e3834f358ccfdfb86ba05cfd05b25c785acb72916b723141495),

[ 50](group__bt__rfcomm.md#ggafccaaeb8f4d4f3e3834f358ccfdfb86ba91be303c7fb7bb210d8209ee746a4302) [BT\_RFCOMM\_CHAN\_DYNAMIC\_START](group__bt__rfcomm.md#ggafccaaeb8f4d4f3e3834f358ccfdfb86ba91be303c7fb7bb210d8209ee746a4302),

51};

52

53struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md);

54

[ 56](structbt__rfcomm__dlc__ops.md)struct [bt\_rfcomm\_dlc\_ops](structbt__rfcomm__dlc__ops.md) {

[ 64](structbt__rfcomm__dlc__ops.md#aba1719c36e7a1dc9705994bcdf134e28) void (\*[connected](structbt__rfcomm__dlc__ops.md#aba1719c36e7a1dc9705994bcdf134e28))(struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \*dlc);

65

[ 74](structbt__rfcomm__dlc__ops.md#a4eeaf7b5db6c93e846a72797e6612d30) void (\*[disconnected](structbt__rfcomm__dlc__ops.md#a4eeaf7b5db6c93e846a72797e6612d30))(struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \*dlc);

75

[ 81](structbt__rfcomm__dlc__ops.md#a4a4e29065b267f0370df5ea602223d0a) void (\*[recv](structbt__rfcomm__dlc__ops.md#a4a4e29065b267f0370df5ea602223d0a))(struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \*dlc, struct [net\_buf](structnet__buf.md) \*buf);

82

[ 88](structbt__rfcomm__dlc__ops.md#a3ba98c41e03c88f330cba0e3539a1cec) void (\*[sent](structbt__rfcomm__dlc__ops.md#a3ba98c41e03c88f330cba0e3539a1cec))(struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \*dlc, int err);

89};

90

[ 93](group__bt__rfcomm.md#gaa70d7971435dc7e6421372d7385811b2)typedef enum [bt\_rfcomm\_role](group__bt__rfcomm.md#gaa70d7971435dc7e6421372d7385811b2) {

[ 94](group__bt__rfcomm.md#ggaa70d7971435dc7e6421372d7385811b2aa0b65eed9632ff8ad3235b4c0eae166d) [BT\_RFCOMM\_ROLE\_ACCEPTOR](group__bt__rfcomm.md#ggaa70d7971435dc7e6421372d7385811b2aa0b65eed9632ff8ad3235b4c0eae166d),

[ 95](group__bt__rfcomm.md#ggaa70d7971435dc7e6421372d7385811b2a20601c2b890ee84b83dfc9ed55e07cf8) [BT\_RFCOMM\_ROLE\_INITIATOR](group__bt__rfcomm.md#ggaa70d7971435dc7e6421372d7385811b2a20601c2b890ee84b83dfc9ed55e07cf8)

[ 96](group__bt__rfcomm.md#ga11f290d34ad631afaa10caf2cefd72b9)} \_\_packed [bt\_rfcomm\_role\_t](group__bt__rfcomm.md#ga11f290d34ad631afaa10caf2cefd72b9);

97

[ 99](structbt__rfcomm__dlc.md)struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) {

100 /\* Response Timeout eXpired (RTX) timer \*/

[ 101](structbt__rfcomm__dlc.md#a82bcf4d9e08dba8d610e92b45abb9ac2) struct [k\_work\_delayable](structk__work__delayable.md) [rtx\_work](structbt__rfcomm__dlc.md#a82bcf4d9e08dba8d610e92b45abb9ac2);

102

103 /\* Queue for outgoing data \*/

[ 104](structbt__rfcomm__dlc.md#a194bfdb88a7fcfcf9cfee6fe878bdee8) struct [k\_fifo](structk__fifo.md) [tx\_queue](structbt__rfcomm__dlc.md#a194bfdb88a7fcfcf9cfee6fe878bdee8);

105

106 /\* TX credits, Reuse as a binary sem for MSC FC if CFC is not enabled \*/

[ 107](structbt__rfcomm__dlc.md#a29b3c942a1d434214637e5d00b68fb33) struct k\_sem [tx\_credits](structbt__rfcomm__dlc.md#a29b3c942a1d434214637e5d00b68fb33);

108

[ 109](structbt__rfcomm__dlc.md#af134e53ac7db47f18de810dbeacdc500) struct bt\_rfcomm\_session \*[session](structbt__rfcomm__dlc.md#af134e53ac7db47f18de810dbeacdc500);

[ 110](structbt__rfcomm__dlc.md#a0054c0b539b947688555b5663c585bb7) struct [bt\_rfcomm\_dlc\_ops](structbt__rfcomm__dlc__ops.md) \*[ops](structbt__rfcomm__dlc.md#a0054c0b539b947688555b5663c585bb7);

111 struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \*\_next;

112

[ 113](structbt__rfcomm__dlc.md#ab298ebd444566533018eabdc5a69c8ba) [bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783) [required\_sec\_level](structbt__rfcomm__dlc.md#ab298ebd444566533018eabdc5a69c8ba);

[ 114](structbt__rfcomm__dlc.md#a984c80865ff8f6b6bc19d3a978e279d0) [bt\_rfcomm\_role\_t](group__bt__rfcomm.md#ga11f290d34ad631afaa10caf2cefd72b9) [role](structbt__rfcomm__dlc.md#a984c80865ff8f6b6bc19d3a978e279d0);

115

[ 116](structbt__rfcomm__dlc.md#a2334abbaacad9b98c2cb2c5650644854) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [mtu](structbt__rfcomm__dlc.md#a2334abbaacad9b98c2cb2c5650644854);

[ 117](structbt__rfcomm__dlc.md#a20d9d284da592d268efbecf29313aed8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dlci](structbt__rfcomm__dlc.md#a20d9d284da592d268efbecf29313aed8);

[ 118](structbt__rfcomm__dlc.md#ac7f484917494af6a355500cc181ed4ec) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state](structbt__rfcomm__dlc.md#ac7f484917494af6a355500cc181ed4ec);

[ 119](structbt__rfcomm__dlc.md#ac946b1f3f017a9ef50a8079aa5846df3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rx\_credit](structbt__rfcomm__dlc.md#ac946b1f3f017a9ef50a8079aa5846df3);

120

121 /\* Stack & kernel data for TX thread \*/

[ 122](structbt__rfcomm__dlc.md#aef7415017cc80c20031804494290675d) struct [k\_thread](structk__thread.md) [tx\_thread](structbt__rfcomm__dlc.md#aef7415017cc80c20031804494290675d);

123#if defined(CONFIG\_BT\_RFCOMM\_DLC\_STACK\_SIZE)

124 [K\_KERNEL\_STACK\_MEMBER](group__thread__stack__api.md#ga600162959def399e70310b944834711f)(stack, CONFIG\_BT\_RFCOMM\_DLC\_STACK\_SIZE);

125#endif /\* CONFIG\_BT\_RFCOMM\_DLC\_STACK\_SIZE \*/

126};

127

[ 128](structbt__rfcomm__server.md)struct [bt\_rfcomm\_server](structbt__rfcomm__server.md) {

[ 139](structbt__rfcomm__server.md#a30b22ea64c0fdd7130e8aaa79519e776) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel](structbt__rfcomm__server.md#a30b22ea64c0fdd7130e8aaa79519e776);

140

[ 152](structbt__rfcomm__server.md#ac08708bb8161f787737962f62d3c003f) int (\*[accept](structbt__rfcomm__server.md#ac08708bb8161f787737962f62d3c003f))(struct bt\_conn \*conn, struct [bt\_rfcomm\_server](structbt__rfcomm__server.md) \*server,

153 struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \*\*dlc);

154

155 struct [bt\_rfcomm\_server](structbt__rfcomm__server.md) \*\_next;

156};

157

[ 168](group__bt__rfcomm.md#gafd0ffcff41e233f74dc2726e889f5401)int [bt\_rfcomm\_server\_register](group__bt__rfcomm.md#gafd0ffcff41e233f74dc2726e889f5401)(struct [bt\_rfcomm\_server](structbt__rfcomm__server.md) \*server);

169

[ 182](group__bt__rfcomm.md#ga2fb8e3ce2a39d0a3c5bea9b3c24a7ab7)int [bt\_rfcomm\_dlc\_connect](group__bt__rfcomm.md#ga2fb8e3ce2a39d0a3c5bea9b3c24a7ab7)(struct bt\_conn \*conn, struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \*dlc,

183 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel](structbt__rfcomm__server.md#a30b22ea64c0fdd7130e8aaa79519e776));

184

[ 195](group__bt__rfcomm.md#ga593841aef52027598977b7b2bbd0237d)int [bt\_rfcomm\_dlc\_send](group__bt__rfcomm.md#ga593841aef52027598977b7b2bbd0237d)(struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \*dlc, struct [net\_buf](structnet__buf.md) \*buf);

196

[ 206](group__bt__rfcomm.md#ga998328b021ec53f7e291ab76856ffa18)int [bt\_rfcomm\_dlc\_disconnect](group__bt__rfcomm.md#ga998328b021ec53f7e291ab76856ffa18)(struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \*dlc);

207

[ 215](group__bt__rfcomm.md#gaed05e67dc975d94e1209372d5817077a)struct [net\_buf](structnet__buf.md) \*[bt\_rfcomm\_create\_pdu](group__bt__rfcomm.md#gaed05e67dc975d94e1209372d5817077a)(struct [net\_buf\_pool](structnet__buf__pool.md) \*pool);

216

217#ifdef \_\_cplusplus

218}

219#endif

220

224

225#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_RFCOMM\_H\_ \*/

[buf.h](bluetooth_2buf_8h.md)

Bluetooth data buffer API.

[conn.h](conn_8h.md)

Bluetooth connection handling.

[bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783)

bt\_security\_t

Security level.

**Definition** conn.h:810

[bt\_rfcomm\_role\_t](group__bt__rfcomm.md#ga11f290d34ad631afaa10caf2cefd72b9)

enum bt\_rfcomm\_role bt\_rfcomm\_role\_t

Role of RFCOMM session and dlc.

[bt\_rfcomm\_dlc\_connect](group__bt__rfcomm.md#ga2fb8e3ce2a39d0a3c5bea9b3c24a7ab7)

int bt\_rfcomm\_dlc\_connect(struct bt\_conn \*conn, struct bt\_rfcomm\_dlc \*dlc, uint8\_t channel)

Connect RFCOMM channel.

[bt\_rfcomm\_dlc\_send](group__bt__rfcomm.md#ga593841aef52027598977b7b2bbd0237d)

int bt\_rfcomm\_dlc\_send(struct bt\_rfcomm\_dlc \*dlc, struct net\_buf \*buf)

Send data to RFCOMM.

[bt\_rfcomm\_dlc\_disconnect](group__bt__rfcomm.md#ga998328b021ec53f7e291ab76856ffa18)

int bt\_rfcomm\_dlc\_disconnect(struct bt\_rfcomm\_dlc \*dlc)

Disconnect RFCOMM dlc.

[bt\_rfcomm\_role](group__bt__rfcomm.md#gaa70d7971435dc7e6421372d7385811b2)

bt\_rfcomm\_role

Role of RFCOMM session and dlc.

**Definition** rfcomm.h:93

[bt\_rfcomm\_create\_pdu](group__bt__rfcomm.md#gaed05e67dc975d94e1209372d5817077a)

struct net\_buf \* bt\_rfcomm\_create\_pdu(struct net\_buf\_pool \*pool)

Allocate the buffer from pool after reserving head room for RFCOMM, L2CAP and ACL headers.

[bt\_rfcomm\_server\_register](group__bt__rfcomm.md#gafd0ffcff41e233f74dc2726e889f5401)

int bt\_rfcomm\_server\_register(struct bt\_rfcomm\_server \*server)

Register RFCOMM server.

[BT\_RFCOMM\_ROLE\_INITIATOR](group__bt__rfcomm.md#ggaa70d7971435dc7e6421372d7385811b2a20601c2b890ee84b83dfc9ed55e07cf8)

@ BT\_RFCOMM\_ROLE\_INITIATOR

**Definition** rfcomm.h:95

[BT\_RFCOMM\_ROLE\_ACCEPTOR](group__bt__rfcomm.md#ggaa70d7971435dc7e6421372d7385811b2aa0b65eed9632ff8ad3235b4c0eae166d)

@ BT\_RFCOMM\_ROLE\_ACCEPTOR

**Definition** rfcomm.h:94

[BT\_RFCOMM\_CHAN\_SPP](group__bt__rfcomm.md#ggafccaaeb8f4d4f3e3834f358ccfdfb86ba05cfd05b25c785acb72916b723141495)

@ BT\_RFCOMM\_CHAN\_SPP

**Definition** rfcomm.h:49

[BT\_RFCOMM\_CHAN\_DYNAMIC\_START](group__bt__rfcomm.md#ggafccaaeb8f4d4f3e3834f358ccfdfb86ba91be303c7fb7bb210d8209ee746a4302)

@ BT\_RFCOMM\_CHAN\_DYNAMIC\_START

**Definition** rfcomm.h:50

[BT\_RFCOMM\_CHAN\_HFP\_HF](group__bt__rfcomm.md#ggafccaaeb8f4d4f3e3834f358ccfdfb86baa62985d89ab11a130eed284d98b7b1e4)

@ BT\_RFCOMM\_CHAN\_HFP\_HF

**Definition** rfcomm.h:45

[BT\_RFCOMM\_CHAN\_HSP\_HS](group__bt__rfcomm.md#ggafccaaeb8f4d4f3e3834f358ccfdfb86baaf92af85143e2a0430d5a99c9a0d3c25)

@ BT\_RFCOMM\_CHAN\_HSP\_HS

**Definition** rfcomm.h:48

[BT\_RFCOMM\_CHAN\_HFP\_AG](group__bt__rfcomm.md#ggafccaaeb8f4d4f3e3834f358ccfdfb86bac7f345a01b4d9aca4c2a879dce05e0dd)

@ BT\_RFCOMM\_CHAN\_HFP\_AG

**Definition** rfcomm.h:46

[BT\_RFCOMM\_CHAN\_HSP\_AG](group__bt__rfcomm.md#ggafccaaeb8f4d4f3e3834f358ccfdfb86badc095ec30d3edf16ef95ece5b3c1104b)

@ BT\_RFCOMM\_CHAN\_HSP\_AG

**Definition** rfcomm.h:47

[K\_KERNEL\_STACK\_MEMBER](group__thread__stack__api.md#ga600162959def399e70310b944834711f)

#define K\_KERNEL\_STACK\_MEMBER(sym, size)

Define an embedded stack memory region.

**Definition** thread\_stack.h:279

[l2cap.h](l2cap_8h.md)

Bluetooth L2CAP handling.

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[bt\_rfcomm\_dlc\_ops](structbt__rfcomm__dlc__ops.md)

RFCOMM DLC operations structure.

**Definition** rfcomm.h:56

[bt\_rfcomm\_dlc\_ops::sent](structbt__rfcomm__dlc__ops.md#a3ba98c41e03c88f330cba0e3539a1cec)

void(\* sent)(struct bt\_rfcomm\_dlc \*dlc, int err)

DLC sent callback.

**Definition** rfcomm.h:88

[bt\_rfcomm\_dlc\_ops::recv](structbt__rfcomm__dlc__ops.md#a4a4e29065b267f0370df5ea602223d0a)

void(\* recv)(struct bt\_rfcomm\_dlc \*dlc, struct net\_buf \*buf)

DLC recv callback.

**Definition** rfcomm.h:81

[bt\_rfcomm\_dlc\_ops::disconnected](structbt__rfcomm__dlc__ops.md#a4eeaf7b5db6c93e846a72797e6612d30)

void(\* disconnected)(struct bt\_rfcomm\_dlc \*dlc)

DLC disconnected callback.

**Definition** rfcomm.h:74

[bt\_rfcomm\_dlc\_ops::connected](structbt__rfcomm__dlc__ops.md#aba1719c36e7a1dc9705994bcdf134e28)

void(\* connected)(struct bt\_rfcomm\_dlc \*dlc)

DLC connected callback.

**Definition** rfcomm.h:64

[bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md)

RFCOMM DLC structure.

**Definition** rfcomm.h:99

[bt\_rfcomm\_dlc::ops](structbt__rfcomm__dlc.md#a0054c0b539b947688555b5663c585bb7)

struct bt\_rfcomm\_dlc\_ops \* ops

**Definition** rfcomm.h:110

[bt\_rfcomm\_dlc::tx\_queue](structbt__rfcomm__dlc.md#a194bfdb88a7fcfcf9cfee6fe878bdee8)

struct k\_fifo tx\_queue

**Definition** rfcomm.h:104

[bt\_rfcomm\_dlc::dlci](structbt__rfcomm__dlc.md#a20d9d284da592d268efbecf29313aed8)

uint8\_t dlci

**Definition** rfcomm.h:117

[bt\_rfcomm\_dlc::mtu](structbt__rfcomm__dlc.md#a2334abbaacad9b98c2cb2c5650644854)

uint16\_t mtu

**Definition** rfcomm.h:116

[bt\_rfcomm\_dlc::tx\_credits](structbt__rfcomm__dlc.md#a29b3c942a1d434214637e5d00b68fb33)

struct k\_sem tx\_credits

**Definition** rfcomm.h:107

[bt\_rfcomm\_dlc::rtx\_work](structbt__rfcomm__dlc.md#a82bcf4d9e08dba8d610e92b45abb9ac2)

struct k\_work\_delayable rtx\_work

**Definition** rfcomm.h:101

[bt\_rfcomm\_dlc::role](structbt__rfcomm__dlc.md#a984c80865ff8f6b6bc19d3a978e279d0)

bt\_rfcomm\_role\_t role

**Definition** rfcomm.h:114

[bt\_rfcomm\_dlc::required\_sec\_level](structbt__rfcomm__dlc.md#ab298ebd444566533018eabdc5a69c8ba)

bt\_security\_t required\_sec\_level

**Definition** rfcomm.h:113

[bt\_rfcomm\_dlc::state](structbt__rfcomm__dlc.md#ac7f484917494af6a355500cc181ed4ec)

uint8\_t state

**Definition** rfcomm.h:118

[bt\_rfcomm\_dlc::rx\_credit](structbt__rfcomm__dlc.md#ac946b1f3f017a9ef50a8079aa5846df3)

uint8\_t rx\_credit

**Definition** rfcomm.h:119

[bt\_rfcomm\_dlc::tx\_thread](structbt__rfcomm__dlc.md#aef7415017cc80c20031804494290675d)

struct k\_thread tx\_thread

**Definition** rfcomm.h:122

[bt\_rfcomm\_dlc::session](structbt__rfcomm__dlc.md#af134e53ac7db47f18de810dbeacdc500)

struct bt\_rfcomm\_session \* session

**Definition** rfcomm.h:109

[bt\_rfcomm\_server](structbt__rfcomm__server.md)

**Definition** rfcomm.h:128

[bt\_rfcomm\_server::channel](structbt__rfcomm__server.md#a30b22ea64c0fdd7130e8aaa79519e776)

uint8\_t channel

Server Channel.

**Definition** rfcomm.h:139

[bt\_rfcomm\_server::accept](structbt__rfcomm__server.md#ac08708bb8161f787737962f62d3c003f)

int(\* accept)(struct bt\_conn \*conn, struct bt\_rfcomm\_server \*server, struct bt\_rfcomm\_dlc \*\*dlc)

Server accept callback.

**Definition** rfcomm.h:152

[k\_fifo](structk__fifo.md)

**Definition** kernel.h:2495

[k\_thread](structk__thread.md)

Thread Structure.

**Definition** thread.h:259

[k\_work\_delayable](structk__work__delayable.md)

A structure used to submit work after a delay.

**Definition** kernel.h:4034

[net\_buf\_pool](structnet__buf__pool.md)

Network buffer pool representation.

**Definition** net\_buf.h:1078

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** net\_buf.h:1006

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [classic](dir_28cc012f073a9d41ddbe6a63c5d8e2de.md)
- [rfcomm.h](rfcomm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
