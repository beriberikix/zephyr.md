---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/rfcomm_8h_source.html
original_path: doxygen/html/rfcomm_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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

20#include <[zephyr/bluetooth/buf.h](buf_8h.md)>

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

[ 107](structbt__rfcomm__dlc.md#a29b3c942a1d434214637e5d00b68fb33) struct [k\_sem](structk__sem.md) [tx\_credits](structbt__rfcomm__dlc.md#a29b3c942a1d434214637e5d00b68fb33);

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

159enum {

[ 160](group__bt__rfcomm.md#gga61637d261987529c219dcd1179ed1711aa16395c45811836119468c7d68cdf8e3) [BT\_RFCOMM\_RPN\_BAUD\_RATE\_2400](group__bt__rfcomm.md#gga61637d261987529c219dcd1179ed1711aa16395c45811836119468c7d68cdf8e3) = 0x0,

[ 161](group__bt__rfcomm.md#gga61637d261987529c219dcd1179ed1711a59c1506cbc6c7fdd5a36788d8ef39c60) [BT\_RFCOMM\_RPN\_BAUD\_RATE\_4800](group__bt__rfcomm.md#gga61637d261987529c219dcd1179ed1711a59c1506cbc6c7fdd5a36788d8ef39c60) = 0x1,

[ 162](group__bt__rfcomm.md#gga61637d261987529c219dcd1179ed1711a69c572ab3be43441a49faf2253a47593) [BT\_RFCOMM\_RPN\_BAUD\_RATE\_7200](group__bt__rfcomm.md#gga61637d261987529c219dcd1179ed1711a69c572ab3be43441a49faf2253a47593) = 0x2,

[ 163](group__bt__rfcomm.md#gga61637d261987529c219dcd1179ed1711a9c6a80ed27f57ac5dc0d3547d53002b9) [BT\_RFCOMM\_RPN\_BAUD\_RATE\_9600](group__bt__rfcomm.md#gga61637d261987529c219dcd1179ed1711a9c6a80ed27f57ac5dc0d3547d53002b9) = 0x3,

[ 164](group__bt__rfcomm.md#gga61637d261987529c219dcd1179ed1711a62dff7e4366dd199a587fc70a716606c) [BT\_RFCOMM\_RPN\_BAUD\_RATE\_19200](group__bt__rfcomm.md#gga61637d261987529c219dcd1179ed1711a62dff7e4366dd199a587fc70a716606c) = 0x4,

[ 165](group__bt__rfcomm.md#gga61637d261987529c219dcd1179ed1711a8b9599a9fb16f3117a8a7197b08b32a5) [BT\_RFCOMM\_RPN\_BAUD\_RATE\_38400](group__bt__rfcomm.md#gga61637d261987529c219dcd1179ed1711a8b9599a9fb16f3117a8a7197b08b32a5) = 0x5,

[ 166](group__bt__rfcomm.md#gga61637d261987529c219dcd1179ed1711adab0850dc108831ba7d1a7c8ac8d0048) [BT\_RFCOMM\_RPN\_BAUD\_RATE\_57600](group__bt__rfcomm.md#gga61637d261987529c219dcd1179ed1711adab0850dc108831ba7d1a7c8ac8d0048) = 0x6,

[ 167](group__bt__rfcomm.md#gga61637d261987529c219dcd1179ed1711af6e5a7d8af8654726bfacdd6f29e8e33) [BT\_RFCOMM\_RPN\_BAUD\_RATE\_115200](group__bt__rfcomm.md#gga61637d261987529c219dcd1179ed1711af6e5a7d8af8654726bfacdd6f29e8e33) = 0x7,

[ 168](group__bt__rfcomm.md#gga61637d261987529c219dcd1179ed1711a8b3417a1fe245ec0323e53ddcaff1760) [BT\_RFCOMM\_RPN\_BAUD\_RATE\_230400](group__bt__rfcomm.md#gga61637d261987529c219dcd1179ed1711a8b3417a1fe245ec0323e53ddcaff1760) = 0x8

169};

170

172enum {

[ 173](group__bt__rfcomm.md#gga15600feb01d876e319e1d5f93991592ba5f1673591e5000a115e245bd03ecf1d1) [BT\_RFCOMM\_RPN\_DATA\_BITS\_5](group__bt__rfcomm.md#gga15600feb01d876e319e1d5f93991592ba5f1673591e5000a115e245bd03ecf1d1) = 0x0,

[ 174](group__bt__rfcomm.md#gga15600feb01d876e319e1d5f93991592ba71dfabec6fec6ac77ee8705a5bbcf3bc) [BT\_RFCOMM\_RPN\_DATA\_BITS\_6](group__bt__rfcomm.md#gga15600feb01d876e319e1d5f93991592ba71dfabec6fec6ac77ee8705a5bbcf3bc) = 0x1,

[ 175](group__bt__rfcomm.md#gga15600feb01d876e319e1d5f93991592ba5fd45643d1d17830ee62d4306ab53867) [BT\_RFCOMM\_RPN\_DATA\_BITS\_7](group__bt__rfcomm.md#gga15600feb01d876e319e1d5f93991592ba5fd45643d1d17830ee62d4306ab53867) = 0x2,

[ 176](group__bt__rfcomm.md#gga15600feb01d876e319e1d5f93991592bada0317ee756dc6887917cb47057e2f83) [BT\_RFCOMM\_RPN\_DATA\_BITS\_8](group__bt__rfcomm.md#gga15600feb01d876e319e1d5f93991592bada0317ee756dc6887917cb47057e2f83) = 0x3

177};

178

180enum {

[ 181](group__bt__rfcomm.md#ggabe97ddd372c3b0b44a9b78539ddf9ffcab59060e62e8df130c857d3873159c339) [BT\_RFCOMM\_RPN\_STOP\_BITS\_1](group__bt__rfcomm.md#ggabe97ddd372c3b0b44a9b78539ddf9ffcab59060e62e8df130c857d3873159c339) = 0,

[ 182](group__bt__rfcomm.md#ggabe97ddd372c3b0b44a9b78539ddf9ffca69c2bfefd90f2cea4b157c00b7b460b6) [BT\_RFCOMM\_RPN\_STOP\_BITS\_1\_5](group__bt__rfcomm.md#ggabe97ddd372c3b0b44a9b78539ddf9ffca69c2bfefd90f2cea4b157c00b7b460b6) = 1

183};

184

186enum {

[ 187](group__bt__rfcomm.md#ggad1794db284f7b39f4816f04f21ed3f4ba137092626a52e1d2e8fada8d8594a90b) [BT\_RFCOMM\_RPN\_PARITY\_NONE](group__bt__rfcomm.md#ggad1794db284f7b39f4816f04f21ed3f4ba137092626a52e1d2e8fada8d8594a90b) = 0x0,

[ 188](group__bt__rfcomm.md#ggad1794db284f7b39f4816f04f21ed3f4ba365e32b5820a0921611325d7c61dd169) [BT\_RFCOMM\_RPN\_PARITY\_ODD](group__bt__rfcomm.md#ggad1794db284f7b39f4816f04f21ed3f4ba365e32b5820a0921611325d7c61dd169) = 0x1,

[ 189](group__bt__rfcomm.md#ggad1794db284f7b39f4816f04f21ed3f4ba376c5d59c7fea34b79ad4d9cd9e66e18) [BT\_RFCOMM\_RPN\_PARITY\_EVEN](group__bt__rfcomm.md#ggad1794db284f7b39f4816f04f21ed3f4ba376c5d59c7fea34b79ad4d9cd9e66e18) = 0x3,

[ 190](group__bt__rfcomm.md#ggad1794db284f7b39f4816f04f21ed3f4ba43d7b78c72b589f51a2811176d816fc9) [BT\_RFCOMM\_RPN\_PARITY\_MARK](group__bt__rfcomm.md#ggad1794db284f7b39f4816f04f21ed3f4ba43d7b78c72b589f51a2811176d816fc9) = 0x5,

[ 191](group__bt__rfcomm.md#ggad1794db284f7b39f4816f04f21ed3f4ba5466e7f23ce5550bffada30ff15658e1) [BT\_RFCOMM\_RPN\_PARITY\_SPACE](group__bt__rfcomm.md#ggad1794db284f7b39f4816f04f21ed3f4ba5466e7f23ce5550bffada30ff15658e1) = 0x7

192};

193

[ 202](group__bt__rfcomm.md#gacbb625b129afb33fceafe5ddf61c839a)#define BT\_RFCOMM\_SET\_LINE\_SETTINGS(data, stop, parity) ((data & 0x3) | \

203 ((stop & 0x1) << 2) | \

204 ((parity & 0x7) << 3))

205

[ 206](group__bt__rfcomm.md#gaef902e774d1a6279a117968a32cc5878)#define BT\_RFCOMM\_RPN\_FLOW\_NONE 0x00

[ 207](group__bt__rfcomm.md#ga90ab80687e32da0f8164292cd63b0623)#define BT\_RFCOMM\_RPN\_XON\_CHAR 0x11

[ 208](group__bt__rfcomm.md#gacdca9e597689b3de20b1df3616ad523c)#define BT\_RFCOMM\_RPN\_XOFF\_CHAR 0x13

209

210/\* Set 1 to all the param mask except reserved \*/

[ 211](group__bt__rfcomm.md#ga71099379ed90d3d6ce9d4c1eed3be827)#define BT\_RFCOMM\_RPN\_PARAM\_MASK\_ALL 0x3f7f

212

[ 214](structbt__rfcomm__rpn.md)struct [bt\_rfcomm\_rpn](structbt__rfcomm__rpn.md) {

[ 215](structbt__rfcomm__rpn.md#afacd73edbb63e3ade9573100967faffa) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dlci](structbt__rfcomm__rpn.md#afacd73edbb63e3ade9573100967faffa);

[ 216](structbt__rfcomm__rpn.md#aad2f64edcb82e864293869474d20fa81) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [baud\_rate](structbt__rfcomm__rpn.md#aad2f64edcb82e864293869474d20fa81);

[ 217](structbt__rfcomm__rpn.md#acd61f81d3de1fe4da58fd5ee0d4e5e77) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [line\_settings](structbt__rfcomm__rpn.md#acd61f81d3de1fe4da58fd5ee0d4e5e77);

[ 218](structbt__rfcomm__rpn.md#ae0db46df73fae846cb53f8a0cf01350a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flow\_control](structbt__rfcomm__rpn.md#ae0db46df73fae846cb53f8a0cf01350a);

[ 219](structbt__rfcomm__rpn.md#ae637cd243e9b016231b5071e171b6b54) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [xon\_char](structbt__rfcomm__rpn.md#ae637cd243e9b016231b5071e171b6b54);

[ 220](structbt__rfcomm__rpn.md#adc651e1ac74d616fd03b07a647139296) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [xoff\_char](structbt__rfcomm__rpn.md#adc651e1ac74d616fd03b07a647139296);

[ 221](structbt__rfcomm__rpn.md#a9eaac13558a5be2fed82084e0bb7a20a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [param\_mask](structbt__rfcomm__rpn.md#a9eaac13558a5be2fed82084e0bb7a20a);

222} \_\_packed;

223

[ 234](group__bt__rfcomm.md#gafd0ffcff41e233f74dc2726e889f5401)int [bt\_rfcomm\_server\_register](group__bt__rfcomm.md#gafd0ffcff41e233f74dc2726e889f5401)(struct [bt\_rfcomm\_server](structbt__rfcomm__server.md) \*server);

235

[ 248](group__bt__rfcomm.md#ga2fb8e3ce2a39d0a3c5bea9b3c24a7ab7)int [bt\_rfcomm\_dlc\_connect](group__bt__rfcomm.md#ga2fb8e3ce2a39d0a3c5bea9b3c24a7ab7)(struct bt\_conn \*conn, struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \*dlc,

249 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel);

250

[ 261](group__bt__rfcomm.md#ga593841aef52027598977b7b2bbd0237d)int [bt\_rfcomm\_dlc\_send](group__bt__rfcomm.md#ga593841aef52027598977b7b2bbd0237d)(struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \*dlc, struct [net\_buf](structnet__buf.md) \*buf);

262

[ 272](group__bt__rfcomm.md#ga998328b021ec53f7e291ab76856ffa18)int [bt\_rfcomm\_dlc\_disconnect](group__bt__rfcomm.md#ga998328b021ec53f7e291ab76856ffa18)(struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \*dlc);

273

[ 281](group__bt__rfcomm.md#gaed05e67dc975d94e1209372d5817077a)struct [net\_buf](structnet__buf.md) \*[bt\_rfcomm\_create\_pdu](group__bt__rfcomm.md#gaed05e67dc975d94e1209372d5817077a)(struct [net\_buf\_pool](structnet__buf__pool.md) \*pool);

282

[ 291](group__bt__rfcomm.md#gab38378db71d7f4631e47742ce4a5c59d)int [bt\_rfcomm\_send\_rpn\_cmd](group__bt__rfcomm.md#gab38378db71d7f4631e47742ce4a5c59d)(struct [bt\_rfcomm\_dlc](structbt__rfcomm__dlc.md) \*dlc, struct [bt\_rfcomm\_rpn](structbt__rfcomm__rpn.md) \*rpn);

292

293#ifdef \_\_cplusplus

294}

295#endif

296

300

301#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_RFCOMM\_H\_ \*/

[buf.h](buf_8h.md)

Bluetooth data buffer API.

[conn.h](conn_8h.md)

Bluetooth connection handling.

[bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783)

bt\_security\_t

Security level.

**Definition** conn.h:814

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

[bt\_rfcomm\_send\_rpn\_cmd](group__bt__rfcomm.md#gab38378db71d7f4631e47742ce4a5c59d)

int bt\_rfcomm\_send\_rpn\_cmd(struct bt\_rfcomm\_dlc \*dlc, struct bt\_rfcomm\_rpn \*rpn)

Send Remote Port Negotiation command.

[bt\_rfcomm\_create\_pdu](group__bt__rfcomm.md#gaed05e67dc975d94e1209372d5817077a)

struct net\_buf \* bt\_rfcomm\_create\_pdu(struct net\_buf\_pool \*pool)

Allocate the buffer from pool after reserving head room for RFCOMM, L2CAP and ACL headers.

[bt\_rfcomm\_server\_register](group__bt__rfcomm.md#gafd0ffcff41e233f74dc2726e889f5401)

int bt\_rfcomm\_server\_register(struct bt\_rfcomm\_server \*server)

Register RFCOMM server.

[BT\_RFCOMM\_RPN\_DATA\_BITS\_5](group__bt__rfcomm.md#gga15600feb01d876e319e1d5f93991592ba5f1673591e5000a115e245bd03ecf1d1)

@ BT\_RFCOMM\_RPN\_DATA\_BITS\_5

**Definition** rfcomm.h:173

[BT\_RFCOMM\_RPN\_DATA\_BITS\_7](group__bt__rfcomm.md#gga15600feb01d876e319e1d5f93991592ba5fd45643d1d17830ee62d4306ab53867)

@ BT\_RFCOMM\_RPN\_DATA\_BITS\_7

**Definition** rfcomm.h:175

[BT\_RFCOMM\_RPN\_DATA\_BITS\_6](group__bt__rfcomm.md#gga15600feb01d876e319e1d5f93991592ba71dfabec6fec6ac77ee8705a5bbcf3bc)

@ BT\_RFCOMM\_RPN\_DATA\_BITS\_6

**Definition** rfcomm.h:174

[BT\_RFCOMM\_RPN\_DATA\_BITS\_8](group__bt__rfcomm.md#gga15600feb01d876e319e1d5f93991592bada0317ee756dc6887917cb47057e2f83)

@ BT\_RFCOMM\_RPN\_DATA\_BITS\_8

**Definition** rfcomm.h:176

[BT\_RFCOMM\_RPN\_BAUD\_RATE\_4800](group__bt__rfcomm.md#gga61637d261987529c219dcd1179ed1711a59c1506cbc6c7fdd5a36788d8ef39c60)

@ BT\_RFCOMM\_RPN\_BAUD\_RATE\_4800

**Definition** rfcomm.h:161

[BT\_RFCOMM\_RPN\_BAUD\_RATE\_19200](group__bt__rfcomm.md#gga61637d261987529c219dcd1179ed1711a62dff7e4366dd199a587fc70a716606c)

@ BT\_RFCOMM\_RPN\_BAUD\_RATE\_19200

**Definition** rfcomm.h:164

[BT\_RFCOMM\_RPN\_BAUD\_RATE\_7200](group__bt__rfcomm.md#gga61637d261987529c219dcd1179ed1711a69c572ab3be43441a49faf2253a47593)

@ BT\_RFCOMM\_RPN\_BAUD\_RATE\_7200

**Definition** rfcomm.h:162

[BT\_RFCOMM\_RPN\_BAUD\_RATE\_230400](group__bt__rfcomm.md#gga61637d261987529c219dcd1179ed1711a8b3417a1fe245ec0323e53ddcaff1760)

@ BT\_RFCOMM\_RPN\_BAUD\_RATE\_230400

**Definition** rfcomm.h:168

[BT\_RFCOMM\_RPN\_BAUD\_RATE\_38400](group__bt__rfcomm.md#gga61637d261987529c219dcd1179ed1711a8b9599a9fb16f3117a8a7197b08b32a5)

@ BT\_RFCOMM\_RPN\_BAUD\_RATE\_38400

**Definition** rfcomm.h:165

[BT\_RFCOMM\_RPN\_BAUD\_RATE\_9600](group__bt__rfcomm.md#gga61637d261987529c219dcd1179ed1711a9c6a80ed27f57ac5dc0d3547d53002b9)

@ BT\_RFCOMM\_RPN\_BAUD\_RATE\_9600

**Definition** rfcomm.h:163

[BT\_RFCOMM\_RPN\_BAUD\_RATE\_2400](group__bt__rfcomm.md#gga61637d261987529c219dcd1179ed1711aa16395c45811836119468c7d68cdf8e3)

@ BT\_RFCOMM\_RPN\_BAUD\_RATE\_2400

**Definition** rfcomm.h:160

[BT\_RFCOMM\_RPN\_BAUD\_RATE\_57600](group__bt__rfcomm.md#gga61637d261987529c219dcd1179ed1711adab0850dc108831ba7d1a7c8ac8d0048)

@ BT\_RFCOMM\_RPN\_BAUD\_RATE\_57600

**Definition** rfcomm.h:166

[BT\_RFCOMM\_RPN\_BAUD\_RATE\_115200](group__bt__rfcomm.md#gga61637d261987529c219dcd1179ed1711af6e5a7d8af8654726bfacdd6f29e8e33)

@ BT\_RFCOMM\_RPN\_BAUD\_RATE\_115200

**Definition** rfcomm.h:167

[BT\_RFCOMM\_ROLE\_INITIATOR](group__bt__rfcomm.md#ggaa70d7971435dc7e6421372d7385811b2a20601c2b890ee84b83dfc9ed55e07cf8)

@ BT\_RFCOMM\_ROLE\_INITIATOR

**Definition** rfcomm.h:95

[BT\_RFCOMM\_ROLE\_ACCEPTOR](group__bt__rfcomm.md#ggaa70d7971435dc7e6421372d7385811b2aa0b65eed9632ff8ad3235b4c0eae166d)

@ BT\_RFCOMM\_ROLE\_ACCEPTOR

**Definition** rfcomm.h:94

[BT\_RFCOMM\_RPN\_STOP\_BITS\_1\_5](group__bt__rfcomm.md#ggabe97ddd372c3b0b44a9b78539ddf9ffca69c2bfefd90f2cea4b157c00b7b460b6)

@ BT\_RFCOMM\_RPN\_STOP\_BITS\_1\_5

**Definition** rfcomm.h:182

[BT\_RFCOMM\_RPN\_STOP\_BITS\_1](group__bt__rfcomm.md#ggabe97ddd372c3b0b44a9b78539ddf9ffcab59060e62e8df130c857d3873159c339)

@ BT\_RFCOMM\_RPN\_STOP\_BITS\_1

**Definition** rfcomm.h:181

[BT\_RFCOMM\_RPN\_PARITY\_NONE](group__bt__rfcomm.md#ggad1794db284f7b39f4816f04f21ed3f4ba137092626a52e1d2e8fada8d8594a90b)

@ BT\_RFCOMM\_RPN\_PARITY\_NONE

**Definition** rfcomm.h:187

[BT\_RFCOMM\_RPN\_PARITY\_ODD](group__bt__rfcomm.md#ggad1794db284f7b39f4816f04f21ed3f4ba365e32b5820a0921611325d7c61dd169)

@ BT\_RFCOMM\_RPN\_PARITY\_ODD

**Definition** rfcomm.h:188

[BT\_RFCOMM\_RPN\_PARITY\_EVEN](group__bt__rfcomm.md#ggad1794db284f7b39f4816f04f21ed3f4ba376c5d59c7fea34b79ad4d9cd9e66e18)

@ BT\_RFCOMM\_RPN\_PARITY\_EVEN

**Definition** rfcomm.h:189

[BT\_RFCOMM\_RPN\_PARITY\_MARK](group__bt__rfcomm.md#ggad1794db284f7b39f4816f04f21ed3f4ba43d7b78c72b589f51a2811176d816fc9)

@ BT\_RFCOMM\_RPN\_PARITY\_MARK

**Definition** rfcomm.h:190

[BT\_RFCOMM\_RPN\_PARITY\_SPACE](group__bt__rfcomm.md#ggad1794db284f7b39f4816f04f21ed3f4ba5466e7f23ce5550bffada30ff15658e1)

@ BT\_RFCOMM\_RPN\_PARITY\_SPACE

**Definition** rfcomm.h:191

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

[bt\_rfcomm\_rpn](structbt__rfcomm__rpn.md)

RFCOMM Remote Port Negotiation (RPN) structure.

**Definition** rfcomm.h:214

[bt\_rfcomm\_rpn::param\_mask](structbt__rfcomm__rpn.md#a9eaac13558a5be2fed82084e0bb7a20a)

uint16\_t param\_mask

**Definition** rfcomm.h:221

[bt\_rfcomm\_rpn::baud\_rate](structbt__rfcomm__rpn.md#aad2f64edcb82e864293869474d20fa81)

uint8\_t baud\_rate

**Definition** rfcomm.h:216

[bt\_rfcomm\_rpn::line\_settings](structbt__rfcomm__rpn.md#acd61f81d3de1fe4da58fd5ee0d4e5e77)

uint8\_t line\_settings

**Definition** rfcomm.h:217

[bt\_rfcomm\_rpn::xoff\_char](structbt__rfcomm__rpn.md#adc651e1ac74d616fd03b07a647139296)

uint8\_t xoff\_char

**Definition** rfcomm.h:220

[bt\_rfcomm\_rpn::flow\_control](structbt__rfcomm__rpn.md#ae0db46df73fae846cb53f8a0cf01350a)

uint8\_t flow\_control

**Definition** rfcomm.h:218

[bt\_rfcomm\_rpn::xon\_char](structbt__rfcomm__rpn.md#ae637cd243e9b016231b5071e171b6b54)

uint8\_t xon\_char

**Definition** rfcomm.h:219

[bt\_rfcomm\_rpn::dlci](structbt__rfcomm__rpn.md#afacd73edbb63e3ade9573100967faffa)

uint8\_t dlci

**Definition** rfcomm.h:215

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

**Definition** kernel.h:2540

[k\_sem](structk__sem.md)

Semaphore structure.

**Definition** kernel.h:3275

[k\_thread](structk__thread.md)

Thread Structure.

**Definition** thread.h:262

[k\_work\_delayable](structk__work__delayable.md)

A structure used to submit work after a delay.

**Definition** kernel.h:4101

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
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
