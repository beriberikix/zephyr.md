---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/l2cap_8h_source.html
original_path: doxygen/html/l2cap_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

l2cap.h

[Go to the documentation of this file.](l2cap_8h.md)

1

4

5/\*

6 \* Copyright (c) 2015-2016 Intel Corporation

7 \* Copyright (c) 2023 Nordic Semiconductor

8 \*

9 \* SPDX-License-Identifier: Apache-2.0

10 \*/

11#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_L2CAP\_H\_

12#define ZEPHYR\_INCLUDE\_BLUETOOTH\_L2CAP\_H\_

13

20

21#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

22

23#include <[zephyr/sys/atomic.h](atomic_8h.md)>

24#include <[zephyr/bluetooth/buf.h](bluetooth_2buf_8h.md)>

25#include <[zephyr/bluetooth/conn.h](conn_8h.md)>

26#include <[zephyr/bluetooth/hci.h](hci_8h.md)>

27

28#ifdef \_\_cplusplus

29extern "C" {

30#endif

31

[ 33](group__bt__l2cap.md#gab33b91052026973180356640b7310659)#define BT\_L2CAP\_HDR\_SIZE 4

34

[ 36](group__bt__l2cap.md#ga45ef5aee4ed4dd705cad6d234562c660)#define BT\_L2CAP\_TX\_MTU (CONFIG\_BT\_L2CAP\_TX\_MTU)

37

[ 39](group__bt__l2cap.md#ga6e458a1758e5012755f3b97f8348c966)#define BT\_L2CAP\_RX\_MTU (CONFIG\_BT\_BUF\_ACL\_RX\_SIZE - BT\_L2CAP\_HDR\_SIZE)

40

[ 48](group__bt__l2cap.md#gab95b119de4757588074e367a90a7136a)#define BT\_L2CAP\_BUF\_SIZE(mtu) BT\_BUF\_ACL\_SIZE(BT\_L2CAP\_HDR\_SIZE + (mtu))

49

[ 51](group__bt__l2cap.md#ga967c4c3f9b9beba1d0ce8516c5d1c659)#define BT\_L2CAP\_SDU\_HDR\_SIZE 2

52

[ 61](group__bt__l2cap.md#gaa6fcd053d918db7005bc058501c2a598)#define BT\_L2CAP\_SDU\_TX\_MTU (BT\_L2CAP\_TX\_MTU - BT\_L2CAP\_SDU\_HDR\_SIZE)

62

[ 73](group__bt__l2cap.md#ga13b93a8f09157fbcf739fa4949840efe)#define BT\_L2CAP\_SDU\_RX\_MTU (BT\_L2CAP\_RX\_MTU - BT\_L2CAP\_SDU\_HDR\_SIZE)

74

[ 84](group__bt__l2cap.md#ga1c76618c32bbe86b18fd8663760fb220)#define BT\_L2CAP\_SDU\_BUF\_SIZE(mtu) BT\_L2CAP\_BUF\_SIZE(BT\_L2CAP\_SDU\_HDR\_SIZE + (mtu))

85

86struct [bt\_l2cap\_chan](structbt__l2cap__chan.md);

87

[ 93](group__bt__l2cap.md#ga88baae9c159f3de4ccb34fd0e3cc8c3b)typedef void (\*[bt\_l2cap\_chan\_destroy\_t](group__bt__l2cap.md#ga88baae9c159f3de4ccb34fd0e3cc8c3b))(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan);

94

[ 107](group__bt__l2cap.md#ga642436bdf29f79495763b10231c6b25b)typedef enum [bt\_l2cap\_chan\_state](group__bt__l2cap.md#ga642436bdf29f79495763b10231c6b25b) {

[ 109](group__bt__l2cap.md#gga642436bdf29f79495763b10231c6b25ba1dc4c69537acf13a8c00dfca5acfb83c) [BT\_L2CAP\_DISCONNECTED](group__bt__l2cap.md#gga642436bdf29f79495763b10231c6b25ba1dc4c69537acf13a8c00dfca5acfb83c),

[ 111](group__bt__l2cap.md#gga642436bdf29f79495763b10231c6b25bac2a46c646c8739e8b129b89698eae7cd) [BT\_L2CAP\_CONNECTING](group__bt__l2cap.md#gga642436bdf29f79495763b10231c6b25bac2a46c646c8739e8b129b89698eae7cd),

[ 113](group__bt__l2cap.md#gga642436bdf29f79495763b10231c6b25ba3167a1b491cb9b97ebe51f66c209f064) [BT\_L2CAP\_CONFIG](group__bt__l2cap.md#gga642436bdf29f79495763b10231c6b25ba3167a1b491cb9b97ebe51f66c209f064),

[ 115](group__bt__l2cap.md#gga642436bdf29f79495763b10231c6b25ba3adc86576ca2db5a7f74030d11699b68) [BT\_L2CAP\_CONNECTED](group__bt__l2cap.md#gga642436bdf29f79495763b10231c6b25ba3adc86576ca2db5a7f74030d11699b68),

[ 117](group__bt__l2cap.md#gga642436bdf29f79495763b10231c6b25ba7a24502cfb06df715f58ad2e088cb7e8) [BT\_L2CAP\_DISCONNECTING](group__bt__l2cap.md#gga642436bdf29f79495763b10231c6b25ba7a24502cfb06df715f58ad2e088cb7e8),

118

[ 119](group__bt__l2cap.md#ga5a80330e52ea0fa4ee3266094570bb16)} \_\_packed [bt\_l2cap\_chan\_state\_t](group__bt__l2cap.md#ga5a80330e52ea0fa4ee3266094570bb16);

120

[ 122](group__bt__l2cap.md#ga371a747c8939a1156111dc03c774015c)typedef enum [bt\_l2cap\_chan\_status](group__bt__l2cap.md#ga371a747c8939a1156111dc03c774015c) {

[ 124](group__bt__l2cap.md#gga371a747c8939a1156111dc03c774015ca89aea3cf3d9a004ffd53eae602666fd5) [BT\_L2CAP\_STATUS\_OUT](group__bt__l2cap.md#gga371a747c8939a1156111dc03c774015ca89aea3cf3d9a004ffd53eae602666fd5),

125

[ 131](group__bt__l2cap.md#gga371a747c8939a1156111dc03c774015ca82d4e553f4298d00c27045949663208e) [BT\_L2CAP\_STATUS\_SHUTDOWN](group__bt__l2cap.md#gga371a747c8939a1156111dc03c774015ca82d4e553f4298d00c27045949663208e),

132

[ 134](group__bt__l2cap.md#gga371a747c8939a1156111dc03c774015caea6cc7cae26d69926e7def91242650af) [BT\_L2CAP\_STATUS\_ENCRYPT\_PENDING](group__bt__l2cap.md#gga371a747c8939a1156111dc03c774015caea6cc7cae26d69926e7def91242650af),

135

136 /\* Total number of status - must be at the end of the enum \*/

[ 137](group__bt__l2cap.md#gga371a747c8939a1156111dc03c774015ca91bd77f9889b59ba5b0005a51016ba2c) [BT\_L2CAP\_NUM\_STATUS](group__bt__l2cap.md#gga371a747c8939a1156111dc03c774015ca91bd77f9889b59ba5b0005a51016ba2c),

[ 138](group__bt__l2cap.md#ga3a1a88a8e87aefe9bea1dd01aa193b42)} \_\_packed [bt\_l2cap\_chan\_status\_t](group__bt__l2cap.md#ga3a1a88a8e87aefe9bea1dd01aa193b42);

139

[ 141](structbt__l2cap__chan.md)struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) {

[ 143](structbt__l2cap__chan.md#a007a7ef11a00c0dff22cd64961260d3d) struct bt\_conn \*[conn](structbt__l2cap__chan.md#a007a7ef11a00c0dff22cd64961260d3d);

[ 145](structbt__l2cap__chan.md#a3e370744f17ca4cff200cc0a2ee1a74b) const struct [bt\_l2cap\_chan\_ops](structbt__l2cap__chan__ops.md) \*[ops](structbt__l2cap__chan.md#a3e370744f17ca4cff200cc0a2ee1a74b);

[ 146](structbt__l2cap__chan.md#a123ae4bb1db6f4b41561b3d4691b1c02) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structbt__l2cap__chan.md#a123ae4bb1db6f4b41561b3d4691b1c02);

[ 147](structbt__l2cap__chan.md#ac0fbde11b35e0b6b424970e73c945a40) [bt\_l2cap\_chan\_destroy\_t](group__bt__l2cap.md#ga88baae9c159f3de4ccb34fd0e3cc8c3b) [destroy](structbt__l2cap__chan.md#ac0fbde11b35e0b6b424970e73c945a40);

148

[ 149](structbt__l2cap__chan.md#a7603e2c212e0522a1ffca2198224a994) [ATOMIC\_DEFINE](group__atomic__apis.md#ga249c575db9764486197709b327f7370e)([status](structbt__l2cap__chan.md#a7603e2c212e0522a1ffca2198224a994), [BT\_L2CAP\_NUM\_STATUS](group__bt__l2cap.md#gga371a747c8939a1156111dc03c774015ca91bd77f9889b59ba5b0005a51016ba2c));

150};

151

[ 153](structbt__l2cap__le__endpoint.md)struct [bt\_l2cap\_le\_endpoint](structbt__l2cap__le__endpoint.md) {

[ 155](structbt__l2cap__le__endpoint.md#aeee85135541b17bede098891b820c63f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [cid](structbt__l2cap__le__endpoint.md#aeee85135541b17bede098891b820c63f);

[ 157](structbt__l2cap__le__endpoint.md#a598f0c7f0ad4cc029013358d35ce9dc2) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [mtu](structbt__l2cap__le__endpoint.md#a598f0c7f0ad4cc029013358d35ce9dc2);

[ 159](structbt__l2cap__le__endpoint.md#aa9e4f21e48eda61a3d0b777ee13c2599) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [mps](structbt__l2cap__le__endpoint.md#aa9e4f21e48eda61a3d0b777ee13c2599);

[ 161](structbt__l2cap__le__endpoint.md#a834561b4a8857253bdfc3d0d2c1033f5) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [init\_credits](structbt__l2cap__le__endpoint.md#a834561b4a8857253bdfc3d0d2c1033f5);

[ 163](structbt__l2cap__le__endpoint.md#ab3f475c383791731c595845c80c27edf) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [credits](structbt__l2cap__le__endpoint.md#ab3f475c383791731c595845c80c27edf);

164};

165

[ 167](structbt__l2cap__le__chan.md)struct [bt\_l2cap\_le\_chan](structbt__l2cap__le__chan.md) {

[ 169](structbt__l2cap__le__chan.md#a980126cabc3824ab623d634d91f7d761) struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) [chan](structbt__l2cap__le__chan.md#a980126cabc3824ab623d634d91f7d761);

[ 182](structbt__l2cap__le__chan.md#a95808ad9bcd910b65bee31fa6bd4b638) struct [bt\_l2cap\_le\_endpoint](structbt__l2cap__le__endpoint.md) [rx](structbt__l2cap__le__chan.md#a95808ad9bcd910b65bee31fa6bd4b638);

183

[ 185](structbt__l2cap__le__chan.md#a55d8ce850f365ac7ab7ff450ecb61f23) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pending\_rx\_mtu](structbt__l2cap__le__chan.md#a55d8ce850f365ac7ab7ff450ecb61f23);

186

[ 194](structbt__l2cap__le__chan.md#a059f98cebf6f43a05937ac82815009e7) struct [bt\_l2cap\_le\_endpoint](structbt__l2cap__le__endpoint.md) [tx](structbt__l2cap__le__chan.md#a059f98cebf6f43a05937ac82815009e7);

195#if defined(CONFIG\_BT\_L2CAP\_DYNAMIC\_CHANNEL)

197 struct [k\_fifo](structk__fifo.md) tx\_queue;

199 struct [net\_buf](structnet__buf.md) \*tx\_buf;

201 struct [k\_work\_delayable](structk__work__delayable.md) tx\_work;

203 struct [net\_buf](structnet__buf.md) \*\_sdu;

204 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \_sdu\_len;

205#if defined(CONFIG\_BT\_L2CAP\_SEG\_RECV)

206 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \_sdu\_len\_done;

207#endif /\* CONFIG\_BT\_L2CAP\_SEG\_RECV \*/

208

209 struct [k\_work](structk__work.md) rx\_work;

210 struct [k\_fifo](structk__fifo.md) rx\_queue;

211

212 [bt\_l2cap\_chan\_state\_t](group__bt__l2cap.md#ga5a80330e52ea0fa4ee3266094570bb16) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90);

214 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) psm;

216 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ident;

217 [bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783) required\_sec\_level;

218

219 /\* Response Timeout eXpired (RTX) timer \*/

220 struct [k\_work\_delayable](structk__work__delayable.md) rtx\_work;

221 struct [k\_work\_sync](structk__work__sync.md) rtx\_sync;

222#endif

223};

224

[ 234](group__bt__l2cap.md#gac936761e661a5c65d65ee9b4c185679b)#define BT\_L2CAP\_LE\_CHAN(\_ch) CONTAINER\_OF(\_ch, struct bt\_l2cap\_le\_chan, chan)

235

[ 237](structbt__l2cap__br__endpoint.md)struct [bt\_l2cap\_br\_endpoint](structbt__l2cap__br__endpoint.md) {

[ 239](structbt__l2cap__br__endpoint.md#acbe4f6cc15bb20703fca53e7084b2ea7) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [cid](structbt__l2cap__br__endpoint.md#acbe4f6cc15bb20703fca53e7084b2ea7);

[ 241](structbt__l2cap__br__endpoint.md#aaeb46128990fe08c926d34049bbc2d6a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [mtu](structbt__l2cap__br__endpoint.md#aaeb46128990fe08c926d34049bbc2d6a);

242};

243

[ 245](structbt__l2cap__br__chan.md)struct [bt\_l2cap\_br\_chan](structbt__l2cap__br__chan.md) {

[ 247](structbt__l2cap__br__chan.md#a28ed2b2541697390c325c706d4ad8f0b) struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) [chan](structbt__l2cap__br__chan.md#a28ed2b2541697390c325c706d4ad8f0b);

[ 249](structbt__l2cap__br__chan.md#a00d49d2d73f2dafdc73a9f7b9393b98d) struct [bt\_l2cap\_br\_endpoint](structbt__l2cap__br__endpoint.md) [rx](structbt__l2cap__br__chan.md#a00d49d2d73f2dafdc73a9f7b9393b98d);

[ 251](structbt__l2cap__br__chan.md#a67aec1f3bef3afe689c164185bd77f98) struct [bt\_l2cap\_br\_endpoint](structbt__l2cap__br__endpoint.md) [tx](structbt__l2cap__br__chan.md#a67aec1f3bef3afe689c164185bd77f98);

252 /\* For internal use only \*/

[ 253](structbt__l2cap__br__chan.md#a09ded589b7e1571fc5d021ceafa68b5f) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [flags](structbt__l2cap__br__chan.md#a09ded589b7e1571fc5d021ceafa68b5f)[1];

254

[ 255](structbt__l2cap__br__chan.md#a556858a2e539bd4d5ed2ae66f392dc74) [bt\_l2cap\_chan\_state\_t](group__bt__l2cap.md#ga5a80330e52ea0fa4ee3266094570bb16) [state](structbt__l2cap__br__chan.md#a556858a2e539bd4d5ed2ae66f392dc74);

[ 257](structbt__l2cap__br__chan.md#a1ca3ed81f6f8edafc2993941de4c9771) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [psm](structbt__l2cap__br__chan.md#a1ca3ed81f6f8edafc2993941de4c9771);

[ 259](structbt__l2cap__br__chan.md#ace996412a41a168c37d60d5e4096dc94) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ident](structbt__l2cap__br__chan.md#ace996412a41a168c37d60d5e4096dc94);

[ 260](structbt__l2cap__br__chan.md#a19bb2e243fb616b73d8b082df7c4a394) [bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783) [required\_sec\_level](structbt__l2cap__br__chan.md#a19bb2e243fb616b73d8b082df7c4a394);

261

262 /\* Response Timeout eXpired (RTX) timer \*/

[ 263](structbt__l2cap__br__chan.md#a0e637544c14d7d2b0ccd2af5424555fb) struct [k\_work\_delayable](structk__work__delayable.md) [rtx\_work](structbt__l2cap__br__chan.md#a0e637544c14d7d2b0ccd2af5424555fb);

[ 264](structbt__l2cap__br__chan.md#a21224ab26501eca21aaed468681d6274) struct [k\_work\_sync](structk__work__sync.md) [rtx\_sync](structbt__l2cap__br__chan.md#a21224ab26501eca21aaed468681d6274);

265};

266

[ 268](structbt__l2cap__chan__ops.md)struct [bt\_l2cap\_chan\_ops](structbt__l2cap__chan__ops.md) {

[ 276](structbt__l2cap__chan__ops.md#a3a4dd75a11c9867adcade6d288dec2de) void (\*[connected](structbt__l2cap__chan__ops.md#a3a4dd75a11c9867adcade6d288dec2de))(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan);

277

[ 286](structbt__l2cap__chan__ops.md#a2e5fcc77a5174de6e3933bb6a14e4ad3) void (\*[disconnected](structbt__l2cap__chan__ops.md#a2e5fcc77a5174de6e3933bb6a14e4ad3))(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan);

287

[ 303](structbt__l2cap__chan__ops.md#ab973539dd8b5e3ab115042a03362f141) void (\*[encrypt\_change](structbt__l2cap__chan__ops.md#a12f3290f9bd04fb5fe562c620dff6984))(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hci\_status);

304

316 struct [net\_buf](structnet__buf.md) \*(\*alloc\_seg)(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan);

317

330 struct [net\_buf](structnet__buf.md) \*(\*alloc\_buf)(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan);

331

[ 345](structbt__l2cap__chan__ops.md#a0ab419d3c52c08e0dfda236466d7cadd) int (\*[recv](structbt__l2cap__chan__ops.md#a0ab419d3c52c08e0dfda236466d7cadd))(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan, struct [net\_buf](structnet__buf.md) \*buf);

346

[ 356](structbt__l2cap__chan__ops.md#a770c09f3fb10c9d1e069333d22803d1a) void (\*[sent](structbt__l2cap__chan__ops.md#a770c09f3fb10c9d1e069333d22803d1a))(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan);

357

[ 366](structbt__l2cap__chan__ops.md#a4be7fadf07368750cc33cf034d3073e7) void (\*[status](structbt__l2cap__chan__ops.md#a4be7fadf07368750cc33cf034d3073e7))(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan, [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*[status](structbt__l2cap__chan__ops.md#a4be7fadf07368750cc33cf034d3073e7));

367

368 /\* @brief Channel released callback

369 \*

370 \* If this callback is set it is called when the stack has release all

371 \* references to the channel object.

372 \*/

[ 373](structbt__l2cap__chan__ops.md#a6d974d0e472626cb1e5cd898a3dcbca6) void (\*[released](structbt__l2cap__chan__ops.md#a6d974d0e472626cb1e5cd898a3dcbca6))(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan);

374

[ 383](structbt__l2cap__chan__ops.md#afba426353897bc3a57c936a98acab839) void (\*[reconfigured](structbt__l2cap__chan__ops.md#afba426353897bc3a57c936a98acab839))(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan);

384

385#if defined(CONFIG\_BT\_L2CAP\_SEG\_RECV)

[ 417](structbt__l2cap__chan__ops.md#a7759a713038d74748952d5f2eb712429) void (\*[seg\_recv](structbt__l2cap__chan__ops.md#a7759a713038d74748952d5f2eb712429))(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan, size\_t sdu\_len,

418 [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) seg\_offset, struct [net\_buf\_simple](structnet__buf__simple.md) \*seg);

419#endif /\* CONFIG\_BT\_L2CAP\_SEG\_RECV \*/

420};

421

[ 425](group__bt__l2cap.md#ga281232ec622c626c0be2be23bae18d8d)#define BT\_L2CAP\_CHAN\_SEND\_RESERVE (BT\_L2CAP\_BUF\_SIZE(0))

426

[ 430](group__bt__l2cap.md#gabdb3983d3862f6654a1653dd45c4157d)#define BT\_L2CAP\_SDU\_CHAN\_SEND\_RESERVE (BT\_L2CAP\_SDU\_BUF\_SIZE(0))

431

[ 433](structbt__l2cap__server.md)struct [bt\_l2cap\_server](structbt__l2cap__server.md) {

[ 447](structbt__l2cap__server.md#a07925dda8566ee7518b1809725e1b110) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [psm](structbt__l2cap__server.md#a07925dda8566ee7518b1809725e1b110);

448

[ 450](structbt__l2cap__server.md#a9f082abf679a397264a7b51fa4400852) [bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783) [sec\_level](structbt__l2cap__server.md#a9f082abf679a397264a7b51fa4400852);

451

[ 466](structbt__l2cap__server.md#ad31a1908f7dc733f9497164ccabba2af) int (\*[accept](structbt__l2cap__server.md#ad31a1908f7dc733f9497164ccabba2af))(struct bt\_conn \*conn, struct [bt\_l2cap\_server](structbt__l2cap__server.md) \*server,

467 struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*\*chan);

468

[ 469](structbt__l2cap__server.md#a76b478140d6a57038eb389eac91442c0) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structbt__l2cap__server.md#a76b478140d6a57038eb389eac91442c0);

470};

471

[ 491](group__bt__l2cap.md#ga1a5e8c81c086872d7fb8da5329f982c6)int [bt\_l2cap\_server\_register](group__bt__l2cap.md#ga1a5e8c81c086872d7fb8da5329f982c6)(struct [bt\_l2cap\_server](structbt__l2cap__server.md) \*server);

492

[ 503](group__bt__l2cap.md#ga5b0ae2abd714f46e6bb2394bce33e613)int [bt\_l2cap\_br\_server\_register](group__bt__l2cap.md#ga5b0ae2abd714f46e6bb2394bce33e613)(struct [bt\_l2cap\_server](structbt__l2cap__server.md) \*server);

504

[ 517](group__bt__l2cap.md#gaebc2d157fb5f013722e9c332b3d81804)int [bt\_l2cap\_ecred\_chan\_connect](group__bt__l2cap.md#gaebc2d157fb5f013722e9c332b3d81804)(struct bt\_conn \*[conn](structbt__l2cap__chan.md#a007a7ef11a00c0dff22cd64961260d3d),

518 struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*\*chans, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) psm);

519

[ 532](group__bt__l2cap.md#ga05d28a51d9fba08d609287957ea4c7ec)int [bt\_l2cap\_ecred\_chan\_reconfigure](group__bt__l2cap.md#ga05d28a51d9fba08d609287957ea4c7ec)(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*\*chans, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mtu);

533

[ 552](group__bt__l2cap.md#ga3c3cfb4b151c808c0a3d2562a5c26a20)int [bt\_l2cap\_chan\_connect](group__bt__l2cap.md#ga3c3cfb4b151c808c0a3d2562a5c26a20)(struct bt\_conn \*[conn](structbt__l2cap__chan.md#a007a7ef11a00c0dff22cd64961260d3d), struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan,

553 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) psm);

554

[ 566](group__bt__l2cap.md#ga7165f82a05e3a19d6b2baf0ba292a3fe)int [bt\_l2cap\_chan\_disconnect](group__bt__l2cap.md#ga7165f82a05e3a19d6b2baf0ba292a3fe)(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan);

567

[ 605](group__bt__l2cap.md#ga97b7909749667f910f83e6fcb54495c3)int [bt\_l2cap\_chan\_send](group__bt__l2cap.md#ga97b7909749667f910f83e6fcb54495c3)(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan, struct [net\_buf](structnet__buf.md) \*buf);

606

[ 628](group__bt__l2cap.md#ga9bc950a929fc2bdb1463c268cea478b6)int [bt\_l2cap\_chan\_give\_credits](group__bt__l2cap.md#ga9bc950a929fc2bdb1463c268cea478b6)(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) additional\_credits);

629

[ 642](group__bt__l2cap.md#gad53f5fc31314121ff84e740879eae3cf)int [bt\_l2cap\_chan\_recv\_complete](group__bt__l2cap.md#gad53f5fc31314121ff84e740879eae3cf)(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan,

643 struct [net\_buf](structnet__buf.md) \*buf);

644

645#ifdef \_\_cplusplus

646}

647#endif

648

652

653#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_L2CAP\_H\_ \*/

[atomic.h](atomic_8h.md)

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[buf.h](bluetooth_2buf_8h.md)

Bluetooth data buffer API.

[conn.h](conn_8h.md)

Bluetooth connection handling.

[ATOMIC\_DEFINE](group__atomic__apis.md#ga249c575db9764486197709b327f7370e)

#define ATOMIC\_DEFINE(name, num\_bits)

Define an array of atomic variables.

**Definition** atomic.h:111

[bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783)

bt\_security\_t

Security level.

**Definition** conn.h:352

[bt\_l2cap\_ecred\_chan\_reconfigure](group__bt__l2cap.md#ga05d28a51d9fba08d609287957ea4c7ec)

int bt\_l2cap\_ecred\_chan\_reconfigure(struct bt\_l2cap\_chan \*\*chans, uint16\_t mtu)

Reconfigure Enhanced Credit Based L2CAP channels.

[bt\_l2cap\_server\_register](group__bt__l2cap.md#ga1a5e8c81c086872d7fb8da5329f982c6)

int bt\_l2cap\_server\_register(struct bt\_l2cap\_server \*server)

Register L2CAP server.

[bt\_l2cap\_chan\_status](group__bt__l2cap.md#ga371a747c8939a1156111dc03c774015c)

bt\_l2cap\_chan\_status

Status of L2CAP channel.

**Definition** l2cap.h:122

[bt\_l2cap\_chan\_status\_t](group__bt__l2cap.md#ga3a1a88a8e87aefe9bea1dd01aa193b42)

enum bt\_l2cap\_chan\_status bt\_l2cap\_chan\_status\_t

Status of L2CAP channel.

[bt\_l2cap\_chan\_connect](group__bt__l2cap.md#ga3c3cfb4b151c808c0a3d2562a5c26a20)

int bt\_l2cap\_chan\_connect(struct bt\_conn \*conn, struct bt\_l2cap\_chan \*chan, uint16\_t psm)

Connect L2CAP channel.

[bt\_l2cap\_chan\_state\_t](group__bt__l2cap.md#ga5a80330e52ea0fa4ee3266094570bb16)

enum bt\_l2cap\_chan\_state bt\_l2cap\_chan\_state\_t

Life-span states of L2CAP CoC channel.

[bt\_l2cap\_br\_server\_register](group__bt__l2cap.md#ga5b0ae2abd714f46e6bb2394bce33e613)

int bt\_l2cap\_br\_server\_register(struct bt\_l2cap\_server \*server)

Register L2CAP server on BR/EDR oriented connection.

[bt\_l2cap\_chan\_state](group__bt__l2cap.md#ga642436bdf29f79495763b10231c6b25b)

bt\_l2cap\_chan\_state

Life-span states of L2CAP CoC channel.

**Definition** l2cap.h:107

[bt\_l2cap\_chan\_disconnect](group__bt__l2cap.md#ga7165f82a05e3a19d6b2baf0ba292a3fe)

int bt\_l2cap\_chan\_disconnect(struct bt\_l2cap\_chan \*chan)

Disconnect L2CAP channel.

[bt\_l2cap\_chan\_destroy\_t](group__bt__l2cap.md#ga88baae9c159f3de4ccb34fd0e3cc8c3b)

void(\* bt\_l2cap\_chan\_destroy\_t)(struct bt\_l2cap\_chan \*chan)

Channel destroy callback.

**Definition** l2cap.h:93

[bt\_l2cap\_chan\_send](group__bt__l2cap.md#ga97b7909749667f910f83e6fcb54495c3)

int bt\_l2cap\_chan\_send(struct bt\_l2cap\_chan \*chan, struct net\_buf \*buf)

Send data to L2CAP channel.

[bt\_l2cap\_chan\_give\_credits](group__bt__l2cap.md#ga9bc950a929fc2bdb1463c268cea478b6)

int bt\_l2cap\_chan\_give\_credits(struct bt\_l2cap\_chan \*chan, uint16\_t additional\_credits)

Give credits to the remote.

[bt\_l2cap\_chan\_recv\_complete](group__bt__l2cap.md#gad53f5fc31314121ff84e740879eae3cf)

int bt\_l2cap\_chan\_recv\_complete(struct bt\_l2cap\_chan \*chan, struct net\_buf \*buf)

Complete receiving L2CAP channel data.

[bt\_l2cap\_ecred\_chan\_connect](group__bt__l2cap.md#gaebc2d157fb5f013722e9c332b3d81804)

int bt\_l2cap\_ecred\_chan\_connect(struct bt\_conn \*conn, struct bt\_l2cap\_chan \*\*chans, uint16\_t psm)

Connect Enhanced Credit Based L2CAP channels.

[BT\_L2CAP\_STATUS\_SHUTDOWN](group__bt__l2cap.md#gga371a747c8939a1156111dc03c774015ca82d4e553f4298d00c27045949663208e)

@ BT\_L2CAP\_STATUS\_SHUTDOWN

Channel shutdown status.

**Definition** l2cap.h:131

[BT\_L2CAP\_STATUS\_OUT](group__bt__l2cap.md#gga371a747c8939a1156111dc03c774015ca89aea3cf3d9a004ffd53eae602666fd5)

@ BT\_L2CAP\_STATUS\_OUT

Channel can send at least one PDU.

**Definition** l2cap.h:124

[BT\_L2CAP\_NUM\_STATUS](group__bt__l2cap.md#gga371a747c8939a1156111dc03c774015ca91bd77f9889b59ba5b0005a51016ba2c)

@ BT\_L2CAP\_NUM\_STATUS

**Definition** l2cap.h:137

[BT\_L2CAP\_STATUS\_ENCRYPT\_PENDING](group__bt__l2cap.md#gga371a747c8939a1156111dc03c774015caea6cc7cae26d69926e7def91242650af)

@ BT\_L2CAP\_STATUS\_ENCRYPT\_PENDING

Channel encryption pending status.

**Definition** l2cap.h:134

[BT\_L2CAP\_DISCONNECTED](group__bt__l2cap.md#gga642436bdf29f79495763b10231c6b25ba1dc4c69537acf13a8c00dfca5acfb83c)

@ BT\_L2CAP\_DISCONNECTED

Channel disconnected.

**Definition** l2cap.h:109

[BT\_L2CAP\_CONFIG](group__bt__l2cap.md#gga642436bdf29f79495763b10231c6b25ba3167a1b491cb9b97ebe51f66c209f064)

@ BT\_L2CAP\_CONFIG

Channel in config state, BR/EDR specific.

**Definition** l2cap.h:113

[BT\_L2CAP\_CONNECTED](group__bt__l2cap.md#gga642436bdf29f79495763b10231c6b25ba3adc86576ca2db5a7f74030d11699b68)

@ BT\_L2CAP\_CONNECTED

Channel ready for upper layer traffic on it.

**Definition** l2cap.h:115

[BT\_L2CAP\_DISCONNECTING](group__bt__l2cap.md#gga642436bdf29f79495763b10231c6b25ba7a24502cfb06df715f58ad2e088cb7e8)

@ BT\_L2CAP\_DISCONNECTING

Channel in disconnecting state.

**Definition** l2cap.h:117

[BT\_L2CAP\_CONNECTING](group__bt__l2cap.md#gga642436bdf29f79495763b10231c6b25bac2a46c646c8739e8b129b89698eae7cd)

@ BT\_L2CAP\_CONNECTING

Channel in connecting state.

**Definition** l2cap.h:111

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[hci.h](hci_8h.md)

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f)

\_\_INTPTR\_TYPE\_\_ off\_t

**Definition** types.h:36

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[bt\_l2cap\_br\_chan](structbt__l2cap__br__chan.md)

BREDR L2CAP Channel structure.

**Definition** l2cap.h:245

[bt\_l2cap\_br\_chan::rx](structbt__l2cap__br__chan.md#a00d49d2d73f2dafdc73a9f7b9393b98d)

struct bt\_l2cap\_br\_endpoint rx

Channel Receiving Endpoint.

**Definition** l2cap.h:249

[bt\_l2cap\_br\_chan::flags](structbt__l2cap__br__chan.md#a09ded589b7e1571fc5d021ceafa68b5f)

atomic\_t flags[1]

**Definition** l2cap.h:253

[bt\_l2cap\_br\_chan::rtx\_work](structbt__l2cap__br__chan.md#a0e637544c14d7d2b0ccd2af5424555fb)

struct k\_work\_delayable rtx\_work

**Definition** l2cap.h:263

[bt\_l2cap\_br\_chan::required\_sec\_level](structbt__l2cap__br__chan.md#a19bb2e243fb616b73d8b082df7c4a394)

bt\_security\_t required\_sec\_level

**Definition** l2cap.h:260

[bt\_l2cap\_br\_chan::psm](structbt__l2cap__br__chan.md#a1ca3ed81f6f8edafc2993941de4c9771)

uint16\_t psm

Remote PSM to be connected.

**Definition** l2cap.h:257

[bt\_l2cap\_br\_chan::rtx\_sync](structbt__l2cap__br__chan.md#a21224ab26501eca21aaed468681d6274)

struct k\_work\_sync rtx\_sync

**Definition** l2cap.h:264

[bt\_l2cap\_br\_chan::chan](structbt__l2cap__br__chan.md#a28ed2b2541697390c325c706d4ad8f0b)

struct bt\_l2cap\_chan chan

Common L2CAP channel reference object.

**Definition** l2cap.h:247

[bt\_l2cap\_br\_chan::state](structbt__l2cap__br__chan.md#a556858a2e539bd4d5ed2ae66f392dc74)

bt\_l2cap\_chan\_state\_t state

**Definition** l2cap.h:255

[bt\_l2cap\_br\_chan::tx](structbt__l2cap__br__chan.md#a67aec1f3bef3afe689c164185bd77f98)

struct bt\_l2cap\_br\_endpoint tx

Channel Transmission Endpoint.

**Definition** l2cap.h:251

[bt\_l2cap\_br\_chan::ident](structbt__l2cap__br__chan.md#ace996412a41a168c37d60d5e4096dc94)

uint8\_t ident

Helps match request context during CoC.

**Definition** l2cap.h:259

[bt\_l2cap\_br\_endpoint](structbt__l2cap__br__endpoint.md)

BREDR L2CAP Endpoint structure.

**Definition** l2cap.h:237

[bt\_l2cap\_br\_endpoint::mtu](structbt__l2cap__br__endpoint.md#aaeb46128990fe08c926d34049bbc2d6a)

uint16\_t mtu

Endpoint Maximum Transmission Unit.

**Definition** l2cap.h:241

[bt\_l2cap\_br\_endpoint::cid](structbt__l2cap__br__endpoint.md#acbe4f6cc15bb20703fca53e7084b2ea7)

uint16\_t cid

Endpoint Channel Identifier (CID).

**Definition** l2cap.h:239

[bt\_l2cap\_chan\_ops](structbt__l2cap__chan__ops.md)

L2CAP Channel operations structure.

**Definition** l2cap.h:268

[bt\_l2cap\_chan\_ops::recv](structbt__l2cap__chan__ops.md#a0ab419d3c52c08e0dfda236466d7cadd)

int(\* recv)(struct bt\_l2cap\_chan \*chan, struct net\_buf \*buf)

Channel recv callback.

**Definition** l2cap.h:345

[bt\_l2cap\_chan\_ops::encrypt\_change](structbt__l2cap__chan__ops.md#a12f3290f9bd04fb5fe562c620dff6984)

void(\* encrypt\_change)(struct bt\_l2cap\_chan \*chan, uint8\_t hci\_status)

Channel encrypt\_change callback.

**Definition** l2cap.h:303

[bt\_l2cap\_chan\_ops::disconnected](structbt__l2cap__chan__ops.md#a2e5fcc77a5174de6e3933bb6a14e4ad3)

void(\* disconnected)(struct bt\_l2cap\_chan \*chan)

Channel disconnected callback.

**Definition** l2cap.h:286

[bt\_l2cap\_chan\_ops::connected](structbt__l2cap__chan__ops.md#a3a4dd75a11c9867adcade6d288dec2de)

void(\* connected)(struct bt\_l2cap\_chan \*chan)

Channel connected callback.

**Definition** l2cap.h:276

[bt\_l2cap\_chan\_ops::status](structbt__l2cap__chan__ops.md#a4be7fadf07368750cc33cf034d3073e7)

void(\* status)(struct bt\_l2cap\_chan \*chan, atomic\_t \*status)

Channel status callback.

**Definition** l2cap.h:366

[bt\_l2cap\_chan\_ops::released](structbt__l2cap__chan__ops.md#a6d974d0e472626cb1e5cd898a3dcbca6)

void(\* released)(struct bt\_l2cap\_chan \*chan)

**Definition** l2cap.h:373

[bt\_l2cap\_chan\_ops::sent](structbt__l2cap__chan__ops.md#a770c09f3fb10c9d1e069333d22803d1a)

void(\* sent)(struct bt\_l2cap\_chan \*chan)

Channel sent callback.

**Definition** l2cap.h:356

[bt\_l2cap\_chan\_ops::seg\_recv](structbt__l2cap__chan__ops.md#a7759a713038d74748952d5f2eb712429)

void(\* seg\_recv)(struct bt\_l2cap\_chan \*chan, size\_t sdu\_len, off\_t seg\_offset, struct net\_buf\_simple \*seg)

Handle L2CAP segments directly.

**Definition** l2cap.h:417

[bt\_l2cap\_chan\_ops::reconfigured](structbt__l2cap__chan__ops.md#afba426353897bc3a57c936a98acab839)

void(\* reconfigured)(struct bt\_l2cap\_chan \*chan)

Channel reconfigured callback.

**Definition** l2cap.h:383

[bt\_l2cap\_chan](structbt__l2cap__chan.md)

L2CAP Channel structure.

**Definition** l2cap.h:141

[bt\_l2cap\_chan::conn](structbt__l2cap__chan.md#a007a7ef11a00c0dff22cd64961260d3d)

struct bt\_conn \* conn

Channel connection reference.

**Definition** l2cap.h:143

[bt\_l2cap\_chan::node](structbt__l2cap__chan.md#a123ae4bb1db6f4b41561b3d4691b1c02)

sys\_snode\_t node

**Definition** l2cap.h:146

[bt\_l2cap\_chan::ops](structbt__l2cap__chan.md#a3e370744f17ca4cff200cc0a2ee1a74b)

const struct bt\_l2cap\_chan\_ops \* ops

Channel operations reference.

**Definition** l2cap.h:145

[bt\_l2cap\_chan::status](structbt__l2cap__chan.md#a7603e2c212e0522a1ffca2198224a994)

atomic\_t status[ATOMIC\_BITMAP\_SIZE(BT\_L2CAP\_NUM\_STATUS)]

**Definition** l2cap.h:149

[bt\_l2cap\_chan::destroy](structbt__l2cap__chan.md#ac0fbde11b35e0b6b424970e73c945a40)

bt\_l2cap\_chan\_destroy\_t destroy

**Definition** l2cap.h:147

[bt\_l2cap\_le\_chan](structbt__l2cap__le__chan.md)

LE L2CAP Channel structure.

**Definition** l2cap.h:167

[bt\_l2cap\_le\_chan::tx](structbt__l2cap__le__chan.md#a059f98cebf6f43a05937ac82815009e7)

struct bt\_l2cap\_le\_endpoint tx

Channel Transmission Endpoint.

**Definition** l2cap.h:194

[bt\_l2cap\_le\_chan::pending\_rx\_mtu](structbt__l2cap__le__chan.md#a55d8ce850f365ac7ab7ff450ecb61f23)

uint16\_t pending\_rx\_mtu

Pending RX MTU on ECFC reconfigure, used internally by stack.

**Definition** l2cap.h:185

[bt\_l2cap\_le\_chan::rx](structbt__l2cap__le__chan.md#a95808ad9bcd910b65bee31fa6bd4b638)

struct bt\_l2cap\_le\_endpoint rx

Channel Receiving Endpoint.

**Definition** l2cap.h:182

[bt\_l2cap\_le\_chan::chan](structbt__l2cap__le__chan.md#a980126cabc3824ab623d634d91f7d761)

struct bt\_l2cap\_chan chan

Common L2CAP channel reference object.

**Definition** l2cap.h:169

[bt\_l2cap\_le\_endpoint](structbt__l2cap__le__endpoint.md)

LE L2CAP Endpoint structure.

**Definition** l2cap.h:153

[bt\_l2cap\_le\_endpoint::mtu](structbt__l2cap__le__endpoint.md#a598f0c7f0ad4cc029013358d35ce9dc2)

uint16\_t mtu

Endpoint Maximum Transmission Unit.

**Definition** l2cap.h:157

[bt\_l2cap\_le\_endpoint::init\_credits](structbt__l2cap__le__endpoint.md#a834561b4a8857253bdfc3d0d2c1033f5)

uint16\_t init\_credits

Endpoint initial credits.

**Definition** l2cap.h:161

[bt\_l2cap\_le\_endpoint::mps](structbt__l2cap__le__endpoint.md#aa9e4f21e48eda61a3d0b777ee13c2599)

uint16\_t mps

Endpoint Maximum PDU payload Size.

**Definition** l2cap.h:159

[bt\_l2cap\_le\_endpoint::credits](structbt__l2cap__le__endpoint.md#ab3f475c383791731c595845c80c27edf)

atomic\_t credits

Endpoint credits.

**Definition** l2cap.h:163

[bt\_l2cap\_le\_endpoint::cid](structbt__l2cap__le__endpoint.md#aeee85135541b17bede098891b820c63f)

uint16\_t cid

Endpoint Channel Identifier (CID).

**Definition** l2cap.h:155

[bt\_l2cap\_server](structbt__l2cap__server.md)

L2CAP Server structure.

**Definition** l2cap.h:433

[bt\_l2cap\_server::psm](structbt__l2cap__server.md#a07925dda8566ee7518b1809725e1b110)

uint16\_t psm

Server PSM.

**Definition** l2cap.h:447

[bt\_l2cap\_server::node](structbt__l2cap__server.md#a76b478140d6a57038eb389eac91442c0)

sys\_snode\_t node

**Definition** l2cap.h:469

[bt\_l2cap\_server::sec\_level](structbt__l2cap__server.md#a9f082abf679a397264a7b51fa4400852)

bt\_security\_t sec\_level

Required minimum security level.

**Definition** l2cap.h:450

[bt\_l2cap\_server::accept](structbt__l2cap__server.md#ad31a1908f7dc733f9497164ccabba2af)

int(\* accept)(struct bt\_conn \*conn, struct bt\_l2cap\_server \*server, struct bt\_l2cap\_chan \*\*chan)

Server accept callback.

**Definition** l2cap.h:466

[k\_fifo](structk__fifo.md)

**Definition** kernel.h:2374

[k\_work\_delayable](structk__work__delayable.md)

A structure used to submit work after a delay.

**Definition** kernel.h:3889

[k\_work\_sync](structk__work__sync.md)

A structure holding internal state for a pending synchronous operation on a work item or queue.

**Definition** kernel.h:3972

[k\_work](structk__work.md)

A structure used to submit work.

**Definition** kernel.h:3861

[net\_buf\_simple](structnet__buf__simple.md)

Simple network buffer representation.

**Definition** buf.h:87

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** buf.h:910

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [l2cap.h](l2cap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
