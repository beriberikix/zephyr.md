---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/rfcomm_8h_source.html
original_path: doxygen/html/rfcomm_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

22

23#ifdef \_\_cplusplus

24extern "C" {

25#endif

26

27/\* RFCOMM channels (1-30): pre-allocated for profiles to avoid conflicts \*/

28enum {

[ 29](group__bt__rfcomm.md#gga93cf332ee53fee74395e6273b9f97052aa62985d89ab11a130eed284d98b7b1e4) [BT\_RFCOMM\_CHAN\_HFP\_HF](group__bt__rfcomm.md#gga93cf332ee53fee74395e6273b9f97052aa62985d89ab11a130eed284d98b7b1e4) = 1,

[ 30](group__bt__rfcomm.md#gga93cf332ee53fee74395e6273b9f97052ac7f345a01b4d9aca4c2a879dce05e0dd) [BT\_RFCOMM\_CHAN\_HFP\_AG](group__bt__rfcomm.md#gga93cf332ee53fee74395e6273b9f97052ac7f345a01b4d9aca4c2a879dce05e0dd),

[ 31](group__bt__rfcomm.md#gga93cf332ee53fee74395e6273b9f97052adc095ec30d3edf16ef95ece5b3c1104b) [BT\_RFCOMM\_CHAN\_HSP\_AG](group__bt__rfcomm.md#gga93cf332ee53fee74395e6273b9f97052adc095ec30d3edf16ef95ece5b3c1104b),

[ 32](group__bt__rfcomm.md#gga93cf332ee53fee74395e6273b9f97052aaf92af85143e2a0430d5a99c9a0d3c25) [BT\_RFCOMM\_CHAN\_HSP\_HS](group__bt__rfcomm.md#gga93cf332ee53fee74395e6273b9f97052aaf92af85143e2a0430d5a99c9a0d3c25),

[ 33](group__bt__rfcomm.md#gga93cf332ee53fee74395e6273b9f97052a05cfd05b25c785acb72916b723141495) [BT\_RFCOMM\_CHAN\_SPP](group__bt__rfcomm.md#gga93cf332ee53fee74395e6273b9f97052a05cfd05b25c785acb72916b723141495),

34};

35

36struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md);

37

[ 39](structbt__rfcomm__dlc__ops.md)struct [bt\_rfcomm\_dlc\_ops](structbt__rfcomm__dlc__ops.md) {

[ 47](structbt__rfcomm__dlc__ops.md#aba1719c36e7a1dc9705994bcdf134e28) void (\*[connected](structbt__rfcomm__dlc__ops.md#aba1719c36e7a1dc9705994bcdf134e28))(struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \*dlc);

48

[ 57](structbt__rfcomm__dlc__ops.md#a4eeaf7b5db6c93e846a72797e6612d30) void (\*[disconnected](structbt__rfcomm__dlc__ops.md#a4eeaf7b5db6c93e846a72797e6612d30))(struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \*dlc);

58

[ 64](structbt__rfcomm__dlc__ops.md#a4a4e29065b267f0370df5ea602223d0a) void (\*[recv](structbt__rfcomm__dlc__ops.md#a4a4e29065b267f0370df5ea602223d0a))(struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \*dlc, struct [net\_buf](structnet__buf.md) \*buf);

65};

66

[ 69](group__bt__rfcomm.md#gaa70d7971435dc7e6421372d7385811b2)typedef enum [bt\_rfcomm\_role](group__bt__rfcomm.md#gaa70d7971435dc7e6421372d7385811b2) {

[ 70](group__bt__rfcomm.md#ggaa70d7971435dc7e6421372d7385811b2aa0b65eed9632ff8ad3235b4c0eae166d) [BT\_RFCOMM\_ROLE\_ACCEPTOR](group__bt__rfcomm.md#ggaa70d7971435dc7e6421372d7385811b2aa0b65eed9632ff8ad3235b4c0eae166d),

[ 71](group__bt__rfcomm.md#ggaa70d7971435dc7e6421372d7385811b2a20601c2b890ee84b83dfc9ed55e07cf8) [BT\_RFCOMM\_ROLE\_INITIATOR](group__bt__rfcomm.md#ggaa70d7971435dc7e6421372d7385811b2a20601c2b890ee84b83dfc9ed55e07cf8)

[ 72](group__bt__rfcomm.md#ga11f290d34ad631afaa10caf2cefd72b9)} \_\_packed [bt\_rfcomm\_role\_t](group__bt__rfcomm.md#ga11f290d34ad631afaa10caf2cefd72b9);

73

[ 75](structbt__rfcomm__dlc.md)struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) {

76 /\* Response Timeout eXpired (RTX) timer \*/

[ 77](structbt__rfcomm__dlc.md#a82bcf4d9e08dba8d610e92b45abb9ac2) struct [k\_work\_delayable](structk__work__delayable.md) [rtx\_work](structbt__rfcomm__dlc.md#a82bcf4d9e08dba8d610e92b45abb9ac2);

78

79 /\* Queue for outgoing data \*/

[ 80](structbt__rfcomm__dlc.md#a194bfdb88a7fcfcf9cfee6fe878bdee8) struct [k\_fifo](structk__fifo.md) [tx\_queue](structbt__rfcomm__dlc.md#a194bfdb88a7fcfcf9cfee6fe878bdee8);

81

82 /\* TX credits, Reuse as a binary sem for MSC FC if CFC is not enabled \*/

[ 83](structbt__rfcomm__dlc.md#a29b3c942a1d434214637e5d00b68fb33) struct k\_sem [tx\_credits](structbt__rfcomm__dlc.md#a29b3c942a1d434214637e5d00b68fb33);

84

[ 85](structbt__rfcomm__dlc.md#af134e53ac7db47f18de810dbeacdc500) struct bt\_rfcomm\_session \*[session](structbt__rfcomm__dlc.md#af134e53ac7db47f18de810dbeacdc500);

[ 86](structbt__rfcomm__dlc.md#a0054c0b539b947688555b5663c585bb7) struct [bt\_rfcomm\_dlc\_ops](structbt__rfcomm__dlc__ops.md) \*[ops](structbt__rfcomm__dlc.md#a0054c0b539b947688555b5663c585bb7);

87 struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \*\_next;

88

[ 89](structbt__rfcomm__dlc.md#ab298ebd444566533018eabdc5a69c8ba) [bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783) [required\_sec\_level](structbt__rfcomm__dlc.md#ab298ebd444566533018eabdc5a69c8ba);

[ 90](structbt__rfcomm__dlc.md#a984c80865ff8f6b6bc19d3a978e279d0) [bt\_rfcomm\_role\_t](group__bt__rfcomm.md#ga11f290d34ad631afaa10caf2cefd72b9) [role](structbt__rfcomm__dlc.md#a984c80865ff8f6b6bc19d3a978e279d0);

91

[ 92](structbt__rfcomm__dlc.md#a2334abbaacad9b98c2cb2c5650644854) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [mtu](structbt__rfcomm__dlc.md#a2334abbaacad9b98c2cb2c5650644854);

[ 93](structbt__rfcomm__dlc.md#a20d9d284da592d268efbecf29313aed8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dlci](structbt__rfcomm__dlc.md#a20d9d284da592d268efbecf29313aed8);

[ 94](structbt__rfcomm__dlc.md#ac7f484917494af6a355500cc181ed4ec) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state](structbt__rfcomm__dlc.md#ac7f484917494af6a355500cc181ed4ec);

[ 95](structbt__rfcomm__dlc.md#ac946b1f3f017a9ef50a8079aa5846df3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rx\_credit](structbt__rfcomm__dlc.md#ac946b1f3f017a9ef50a8079aa5846df3);

96

97 /\* Stack & kernel data for TX thread \*/

[ 98](structbt__rfcomm__dlc.md#aef7415017cc80c20031804494290675d) struct [k\_thread](structk__thread.md) [tx\_thread](structbt__rfcomm__dlc.md#aef7415017cc80c20031804494290675d);

[ 99](structbt__rfcomm__dlc.md#ac97ff9933fb9449e7c8fa008e727227f) [K\_KERNEL\_STACK\_MEMBER](structbt__rfcomm__dlc.md#ac97ff9933fb9449e7c8fa008e727227f)(stack, 256);

100};

101

[ 102](structbt__rfcomm__server.md)struct [bt\_rfcomm\_server](structbt__rfcomm__server.md) {

[ 104](structbt__rfcomm__server.md#a30b22ea64c0fdd7130e8aaa79519e776) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel](structbt__rfcomm__server.md#a30b22ea64c0fdd7130e8aaa79519e776);

105

[ 116](structbt__rfcomm__server.md#a7bcb6da4cd4265c9c3b6439ec8e3a957) int (\*[accept](structbt__rfcomm__server.md#a7bcb6da4cd4265c9c3b6439ec8e3a957))(struct bt\_conn \*conn, struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \*\*dlc);

117

118 struct [bt\_rfcomm\_server](structbt__rfcomm__server.md) \*\_next;

119};

120

[ 131](group__bt__rfcomm.md#gafd0ffcff41e233f74dc2726e889f5401)int [bt\_rfcomm\_server\_register](group__bt__rfcomm.md#gafd0ffcff41e233f74dc2726e889f5401)(struct [bt\_rfcomm\_server](structbt__rfcomm__server.md) \*server);

132

[ 145](group__bt__rfcomm.md#ga2fb8e3ce2a39d0a3c5bea9b3c24a7ab7)int [bt\_rfcomm\_dlc\_connect](group__bt__rfcomm.md#ga2fb8e3ce2a39d0a3c5bea9b3c24a7ab7)(struct bt\_conn \*conn, struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \*dlc,

146 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [channel](structbt__rfcomm__server.md#a30b22ea64c0fdd7130e8aaa79519e776));

147

[ 158](group__bt__rfcomm.md#ga593841aef52027598977b7b2bbd0237d)int [bt\_rfcomm\_dlc\_send](group__bt__rfcomm.md#ga593841aef52027598977b7b2bbd0237d)(struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \*dlc, struct [net\_buf](structnet__buf.md) \*buf);

159

[ 169](group__bt__rfcomm.md#ga998328b021ec53f7e291ab76856ffa18)int [bt\_rfcomm\_dlc\_disconnect](group__bt__rfcomm.md#ga998328b021ec53f7e291ab76856ffa18)(struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \*dlc);

170

[ 178](group__bt__rfcomm.md#gaed05e67dc975d94e1209372d5817077a)struct [net\_buf](structnet__buf.md) \*[bt\_rfcomm\_create\_pdu](group__bt__rfcomm.md#gaed05e67dc975d94e1209372d5817077a)(struct [net\_buf\_pool](structnet__buf__pool.md) \*pool);

179

180#ifdef \_\_cplusplus

181}

182#endif

183

187

188#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_RFCOMM\_H\_ \*/

[buf.h](bluetooth_2buf_8h.md)

Bluetooth data buffer API.

[conn.h](conn_8h.md)

Bluetooth connection handling.

[bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783)

bt\_security\_t

Security level.

**Definition** conn.h:352

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

**Definition** rfcomm.h:69

[bt\_rfcomm\_create\_pdu](group__bt__rfcomm.md#gaed05e67dc975d94e1209372d5817077a)

struct net\_buf \* bt\_rfcomm\_create\_pdu(struct net\_buf\_pool \*pool)

Allocate the buffer from pool after reserving head room for RFCOMM, L2CAP and ACL headers.

[bt\_rfcomm\_server\_register](group__bt__rfcomm.md#gafd0ffcff41e233f74dc2726e889f5401)

int bt\_rfcomm\_server\_register(struct bt\_rfcomm\_server \*server)

Register RFCOMM server.

[BT\_RFCOMM\_CHAN\_SPP](group__bt__rfcomm.md#gga93cf332ee53fee74395e6273b9f97052a05cfd05b25c785acb72916b723141495)

@ BT\_RFCOMM\_CHAN\_SPP

**Definition** rfcomm.h:33

[BT\_RFCOMM\_CHAN\_HFP\_HF](group__bt__rfcomm.md#gga93cf332ee53fee74395e6273b9f97052aa62985d89ab11a130eed284d98b7b1e4)

@ BT\_RFCOMM\_CHAN\_HFP\_HF

**Definition** rfcomm.h:29

[BT\_RFCOMM\_CHAN\_HSP\_HS](group__bt__rfcomm.md#gga93cf332ee53fee74395e6273b9f97052aaf92af85143e2a0430d5a99c9a0d3c25)

@ BT\_RFCOMM\_CHAN\_HSP\_HS

**Definition** rfcomm.h:32

[BT\_RFCOMM\_CHAN\_HFP\_AG](group__bt__rfcomm.md#gga93cf332ee53fee74395e6273b9f97052ac7f345a01b4d9aca4c2a879dce05e0dd)

@ BT\_RFCOMM\_CHAN\_HFP\_AG

**Definition** rfcomm.h:30

[BT\_RFCOMM\_CHAN\_HSP\_AG](group__bt__rfcomm.md#gga93cf332ee53fee74395e6273b9f97052adc095ec30d3edf16ef95ece5b3c1104b)

@ BT\_RFCOMM\_CHAN\_HSP\_AG

**Definition** rfcomm.h:31

[BT\_RFCOMM\_ROLE\_INITIATOR](group__bt__rfcomm.md#ggaa70d7971435dc7e6421372d7385811b2a20601c2b890ee84b83dfc9ed55e07cf8)

@ BT\_RFCOMM\_ROLE\_INITIATOR

**Definition** rfcomm.h:71

[BT\_RFCOMM\_ROLE\_ACCEPTOR](group__bt__rfcomm.md#ggaa70d7971435dc7e6421372d7385811b2aa0b65eed9632ff8ad3235b4c0eae166d)

@ BT\_RFCOMM\_ROLE\_ACCEPTOR

**Definition** rfcomm.h:70

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[bt\_rfcomm\_dlc\_ops](structbt__rfcomm__dlc__ops.md)

RFCOMM DLC operations structure.

**Definition** rfcomm.h:39

[bt\_rfcomm\_dlc\_ops::recv](structbt__rfcomm__dlc__ops.md#a4a4e29065b267f0370df5ea602223d0a)

void(\* recv)(struct bt\_rfcomm\_dlc \*dlc, struct net\_buf \*buf)

DLC recv callback.

**Definition** rfcomm.h:64

[bt\_rfcomm\_dlc\_ops::disconnected](structbt__rfcomm__dlc__ops.md#a4eeaf7b5db6c93e846a72797e6612d30)

void(\* disconnected)(struct bt\_rfcomm\_dlc \*dlc)

DLC disconnected callback.

**Definition** rfcomm.h:57

[bt\_rfcomm\_dlc\_ops::connected](structbt__rfcomm__dlc__ops.md#aba1719c36e7a1dc9705994bcdf134e28)

void(\* connected)(struct bt\_rfcomm\_dlc \*dlc)

DLC connected callback.

**Definition** rfcomm.h:47

[bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md)

RFCOMM DLC structure.

**Definition** rfcomm.h:75

[bt\_rfcomm\_dlc::ops](structbt__rfcomm__dlc.md#a0054c0b539b947688555b5663c585bb7)

struct bt\_rfcomm\_dlc\_ops \* ops

**Definition** rfcomm.h:86

[bt\_rfcomm\_dlc::tx\_queue](structbt__rfcomm__dlc.md#a194bfdb88a7fcfcf9cfee6fe878bdee8)

struct k\_fifo tx\_queue

**Definition** rfcomm.h:80

[bt\_rfcomm\_dlc::dlci](structbt__rfcomm__dlc.md#a20d9d284da592d268efbecf29313aed8)

uint8\_t dlci

**Definition** rfcomm.h:93

[bt\_rfcomm\_dlc::mtu](structbt__rfcomm__dlc.md#a2334abbaacad9b98c2cb2c5650644854)

uint16\_t mtu

**Definition** rfcomm.h:92

[bt\_rfcomm\_dlc::tx\_credits](structbt__rfcomm__dlc.md#a29b3c942a1d434214637e5d00b68fb33)

struct k\_sem tx\_credits

**Definition** rfcomm.h:83

[bt\_rfcomm\_dlc::rtx\_work](structbt__rfcomm__dlc.md#a82bcf4d9e08dba8d610e92b45abb9ac2)

struct k\_work\_delayable rtx\_work

**Definition** rfcomm.h:77

[bt\_rfcomm\_dlc::role](structbt__rfcomm__dlc.md#a984c80865ff8f6b6bc19d3a978e279d0)

bt\_rfcomm\_role\_t role

**Definition** rfcomm.h:90

[bt\_rfcomm\_dlc::required\_sec\_level](structbt__rfcomm__dlc.md#ab298ebd444566533018eabdc5a69c8ba)

bt\_security\_t required\_sec\_level

**Definition** rfcomm.h:89

[bt\_rfcomm\_dlc::state](structbt__rfcomm__dlc.md#ac7f484917494af6a355500cc181ed4ec)

uint8\_t state

**Definition** rfcomm.h:94

[bt\_rfcomm\_dlc::rx\_credit](structbt__rfcomm__dlc.md#ac946b1f3f017a9ef50a8079aa5846df3)

uint8\_t rx\_credit

**Definition** rfcomm.h:95

[bt\_rfcomm\_dlc::K\_KERNEL\_STACK\_MEMBER](structbt__rfcomm__dlc.md#ac97ff9933fb9449e7c8fa008e727227f)

K\_KERNEL\_STACK\_MEMBER(stack, 256)

[bt\_rfcomm\_dlc::tx\_thread](structbt__rfcomm__dlc.md#aef7415017cc80c20031804494290675d)

struct k\_thread tx\_thread

**Definition** rfcomm.h:98

[bt\_rfcomm\_dlc::session](structbt__rfcomm__dlc.md#af134e53ac7db47f18de810dbeacdc500)

struct bt\_rfcomm\_session \* session

**Definition** rfcomm.h:85

[bt\_rfcomm\_server](structbt__rfcomm__server.md)

**Definition** rfcomm.h:102

[bt\_rfcomm\_server::channel](structbt__rfcomm__server.md#a30b22ea64c0fdd7130e8aaa79519e776)

uint8\_t channel

Server Channel.

**Definition** rfcomm.h:104

[bt\_rfcomm\_server::accept](structbt__rfcomm__server.md#a7bcb6da4cd4265c9c3b6439ec8e3a957)

int(\* accept)(struct bt\_conn \*conn, struct bt\_rfcomm\_dlc \*\*dlc)

Server accept callback.

**Definition** rfcomm.h:116

[k\_fifo](structk__fifo.md)

**Definition** kernel.h:2374

[k\_thread](structk__thread.md)

Thread Structure.

**Definition** thread.h:250

[k\_work\_delayable](structk__work__delayable.md)

A structure used to submit work after a delay.

**Definition** kernel.h:3889

[net\_buf\_pool](structnet__buf__pool.md)

Network buffer pool representation.

**Definition** buf.h:976

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** buf.h:910

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [rfcomm.h](rfcomm_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
