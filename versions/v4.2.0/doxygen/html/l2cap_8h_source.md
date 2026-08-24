---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/l2cap_8h_source.html
original_path: doxygen/html/l2cap_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
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

21#include <stddef.h>

22#include <[stdint.h](stdint_8h.md)>

23

24#include <[zephyr/bluetooth/buf.h](buf_8h.md)>

25#include <[zephyr/bluetooth/conn.h](conn_8h.md)>

26#include <[zephyr/bluetooth/hci.h](hci_8h.md)>

27#include <[zephyr/kernel.h](kernel_8h.md)>

28#include <[zephyr/net\_buf.h](net__buf_8h.md)>

29#include <[zephyr/sys/atomic.h](sys_2atomic_8h.md)>

30#include <[zephyr/sys/slist.h](slist_8h.md)>

31#include <[zephyr/sys/util.h](sys_2util_8h.md)>

32#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

33

34#ifdef \_\_cplusplus

35extern "C" {

36#endif

37

[ 39](group__bt__l2cap.md#gab33b91052026973180356640b7310659)#define BT\_L2CAP\_HDR\_SIZE 4

40

[ 42](group__bt__l2cap.md#ga45ef5aee4ed4dd705cad6d234562c660)#define BT\_L2CAP\_TX\_MTU (CONFIG\_BT\_L2CAP\_TX\_MTU)

43

[ 45](group__bt__l2cap.md#ga6e458a1758e5012755f3b97f8348c966)#define BT\_L2CAP\_RX\_MTU (CONFIG\_BT\_BUF\_ACL\_RX\_SIZE - BT\_L2CAP\_HDR\_SIZE)

46

[ 54](group__bt__l2cap.md#gab95b119de4757588074e367a90a7136a)#define BT\_L2CAP\_BUF\_SIZE(mtu) BT\_BUF\_ACL\_SIZE(BT\_L2CAP\_HDR\_SIZE + (mtu))

55

[ 57](group__bt__l2cap.md#ga967c4c3f9b9beba1d0ce8516c5d1c659)#define BT\_L2CAP\_SDU\_HDR\_SIZE 2

58

[ 67](group__bt__l2cap.md#gaa6fcd053d918db7005bc058501c2a598)#define BT\_L2CAP\_SDU\_TX\_MTU (BT\_L2CAP\_TX\_MTU - BT\_L2CAP\_SDU\_HDR\_SIZE)

68

[ 79](group__bt__l2cap.md#ga13b93a8f09157fbcf739fa4949840efe)#define BT\_L2CAP\_SDU\_RX\_MTU (BT\_L2CAP\_RX\_MTU - BT\_L2CAP\_SDU\_HDR\_SIZE)

80

[ 90](group__bt__l2cap.md#ga1c76618c32bbe86b18fd8663760fb220)#define BT\_L2CAP\_SDU\_BUF\_SIZE(mtu) BT\_L2CAP\_BUF\_SIZE(BT\_L2CAP\_SDU\_HDR\_SIZE + (mtu))

91

[ 101](group__bt__l2cap.md#gac201afc0f1f55b89a023f03162ba57fe)#define BT\_L2CAP\_ECRED\_MIN\_MTU 64

102

[ 112](group__bt__l2cap.md#ga11933f5a909578f0768f60ce0c8e4c86)#define BT\_L2CAP\_ECRED\_MIN\_MPS 64

113

[ 126](group__bt__l2cap.md#gaf4c98aa3e9f5293b2ff693fb69dc71c9)#define BT\_L2CAP\_ECRED\_CHAN\_MAX\_PER\_REQ 5

127

128struct [bt\_l2cap\_chan](structbt__l2cap__chan.md);

129

[ 135](group__bt__l2cap.md#ga88baae9c159f3de4ccb34fd0e3cc8c3b)typedef void (\*[bt\_l2cap\_chan\_destroy\_t](group__bt__l2cap.md#ga88baae9c159f3de4ccb34fd0e3cc8c3b))(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan);

136

[ 149](group__bt__l2cap.md#ga642436bdf29f79495763b10231c6b25b)typedef enum [bt\_l2cap\_chan\_state](group__bt__l2cap.md#ga642436bdf29f79495763b10231c6b25b) {

[ 151](group__bt__l2cap.md#gga642436bdf29f79495763b10231c6b25ba1dc4c69537acf13a8c00dfca5acfb83c) [BT\_L2CAP\_DISCONNECTED](group__bt__l2cap.md#gga642436bdf29f79495763b10231c6b25ba1dc4c69537acf13a8c00dfca5acfb83c),

[ 153](group__bt__l2cap.md#gga642436bdf29f79495763b10231c6b25bac2a46c646c8739e8b129b89698eae7cd) [BT\_L2CAP\_CONNECTING](group__bt__l2cap.md#gga642436bdf29f79495763b10231c6b25bac2a46c646c8739e8b129b89698eae7cd),

[ 155](group__bt__l2cap.md#gga642436bdf29f79495763b10231c6b25ba3167a1b491cb9b97ebe51f66c209f064) [BT\_L2CAP\_CONFIG](group__bt__l2cap.md#gga642436bdf29f79495763b10231c6b25ba3167a1b491cb9b97ebe51f66c209f064),

[ 157](group__bt__l2cap.md#gga642436bdf29f79495763b10231c6b25ba3adc86576ca2db5a7f74030d11699b68) [BT\_L2CAP\_CONNECTED](group__bt__l2cap.md#gga642436bdf29f79495763b10231c6b25ba3adc86576ca2db5a7f74030d11699b68),

[ 159](group__bt__l2cap.md#gga642436bdf29f79495763b10231c6b25ba7a24502cfb06df715f58ad2e088cb7e8) [BT\_L2CAP\_DISCONNECTING](group__bt__l2cap.md#gga642436bdf29f79495763b10231c6b25ba7a24502cfb06df715f58ad2e088cb7e8),

160

[ 161](group__bt__l2cap.md#ga5a80330e52ea0fa4ee3266094570bb16)} \_\_packed [bt\_l2cap\_chan\_state\_t](group__bt__l2cap.md#ga5a80330e52ea0fa4ee3266094570bb16);

162

[ 164](group__bt__l2cap.md#ga371a747c8939a1156111dc03c774015c)typedef enum [bt\_l2cap\_chan\_status](group__bt__l2cap.md#ga371a747c8939a1156111dc03c774015c) {

[ 166](group__bt__l2cap.md#gga371a747c8939a1156111dc03c774015ca89aea3cf3d9a004ffd53eae602666fd5) [BT\_L2CAP\_STATUS\_OUT](group__bt__l2cap.md#gga371a747c8939a1156111dc03c774015ca89aea3cf3d9a004ffd53eae602666fd5),

167

[ 173](group__bt__l2cap.md#gga371a747c8939a1156111dc03c774015ca82d4e553f4298d00c27045949663208e) [BT\_L2CAP\_STATUS\_SHUTDOWN](group__bt__l2cap.md#gga371a747c8939a1156111dc03c774015ca82d4e553f4298d00c27045949663208e),

174

[ 176](group__bt__l2cap.md#gga371a747c8939a1156111dc03c774015caea6cc7cae26d69926e7def91242650af) [BT\_L2CAP\_STATUS\_ENCRYPT\_PENDING](group__bt__l2cap.md#gga371a747c8939a1156111dc03c774015caea6cc7cae26d69926e7def91242650af),

177

178 /\* Total number of status - must be at the end of the enum \*/

[ 179](group__bt__l2cap.md#gga371a747c8939a1156111dc03c774015ca91bd77f9889b59ba5b0005a51016ba2c) [BT\_L2CAP\_NUM\_STATUS](group__bt__l2cap.md#gga371a747c8939a1156111dc03c774015ca91bd77f9889b59ba5b0005a51016ba2c),

[ 180](group__bt__l2cap.md#ga3a1a88a8e87aefe9bea1dd01aa193b42)} \_\_packed [bt\_l2cap\_chan\_status\_t](group__bt__l2cap.md#ga3a1a88a8e87aefe9bea1dd01aa193b42);

181

[ 183](structbt__l2cap__chan.md)struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) {

[ 185](structbt__l2cap__chan.md#a007a7ef11a00c0dff22cd64961260d3d) struct bt\_conn \*[conn](structbt__l2cap__chan.md#a007a7ef11a00c0dff22cd64961260d3d);

[ 187](structbt__l2cap__chan.md#a3e370744f17ca4cff200cc0a2ee1a74b) const struct [bt\_l2cap\_chan\_ops](structbt__l2cap__chan__ops.md) \*[ops](structbt__l2cap__chan.md#a3e370744f17ca4cff200cc0a2ee1a74b);

[ 188](structbt__l2cap__chan.md#a123ae4bb1db6f4b41561b3d4691b1c02) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structbt__l2cap__chan.md#a123ae4bb1db6f4b41561b3d4691b1c02);

[ 189](structbt__l2cap__chan.md#ac0fbde11b35e0b6b424970e73c945a40) [bt\_l2cap\_chan\_destroy\_t](group__bt__l2cap.md#ga88baae9c159f3de4ccb34fd0e3cc8c3b) [destroy](structbt__l2cap__chan.md#ac0fbde11b35e0b6b424970e73c945a40);

190

[ 191](structbt__l2cap__chan.md#a7603e2c212e0522a1ffca2198224a994) [ATOMIC\_DEFINE](group__atomic__apis.md#ga249c575db9764486197709b327f7370e)([status](structbt__l2cap__chan.md#a7603e2c212e0522a1ffca2198224a994), [BT\_L2CAP\_NUM\_STATUS](group__bt__l2cap.md#gga371a747c8939a1156111dc03c774015ca91bd77f9889b59ba5b0005a51016ba2c));

192};

193

[ 195](structbt__l2cap__le__endpoint.md)struct [bt\_l2cap\_le\_endpoint](structbt__l2cap__le__endpoint.md) {

[ 197](structbt__l2cap__le__endpoint.md#aeee85135541b17bede098891b820c63f) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [cid](structbt__l2cap__le__endpoint.md#aeee85135541b17bede098891b820c63f);

[ 199](structbt__l2cap__le__endpoint.md#a598f0c7f0ad4cc029013358d35ce9dc2) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [mtu](structbt__l2cap__le__endpoint.md#a598f0c7f0ad4cc029013358d35ce9dc2);

[ 201](structbt__l2cap__le__endpoint.md#aa9e4f21e48eda61a3d0b777ee13c2599) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [mps](structbt__l2cap__le__endpoint.md#aa9e4f21e48eda61a3d0b777ee13c2599);

[ 203](structbt__l2cap__le__endpoint.md#ab3f475c383791731c595845c80c27edf) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [credits](structbt__l2cap__le__endpoint.md#ab3f475c383791731c595845c80c27edf);

204};

205

[ 207](structbt__l2cap__le__chan.md)struct [bt\_l2cap\_le\_chan](structbt__l2cap__le__chan.md) {

[ 209](structbt__l2cap__le__chan.md#a980126cabc3824ab623d634d91f7d761) struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) [chan](structbt__l2cap__le__chan.md#a980126cabc3824ab623d634d91f7d761);

[ 222](structbt__l2cap__le__chan.md#a95808ad9bcd910b65bee31fa6bd4b638) struct [bt\_l2cap\_le\_endpoint](structbt__l2cap__le__endpoint.md) [rx](structbt__l2cap__le__chan.md#a95808ad9bcd910b65bee31fa6bd4b638);

223

[ 225](structbt__l2cap__le__chan.md#a55d8ce850f365ac7ab7ff450ecb61f23) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pending\_rx\_mtu](structbt__l2cap__le__chan.md#a55d8ce850f365ac7ab7ff450ecb61f23);

226

[ 234](structbt__l2cap__le__chan.md#a059f98cebf6f43a05937ac82815009e7) struct [bt\_l2cap\_le\_endpoint](structbt__l2cap__le__endpoint.md) [tx](structbt__l2cap__le__chan.md#a059f98cebf6f43a05937ac82815009e7);

[ 236](structbt__l2cap__le__chan.md#a716ea69cb7261076023d0cf6384b3ebb) struct [k\_fifo](structk__fifo.md) [tx\_queue](structbt__l2cap__le__chan.md#a716ea69cb7261076023d0cf6384b3ebb);

237#if defined(CONFIG\_BT\_L2CAP\_DYNAMIC\_CHANNEL)

239 struct [net\_buf](structnet__buf.md) \*\_sdu;

240 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \_sdu\_len;

241#if defined(CONFIG\_BT\_L2CAP\_SEG\_RECV)

242 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \_sdu\_len\_done;

243#endif /\* CONFIG\_BT\_L2CAP\_SEG\_RECV \*/

244

245 struct [k\_work](structk__work.md) rx\_work;

246 struct [k\_fifo](structk__fifo.md) rx\_queue;

247

248 [bt\_l2cap\_chan\_state\_t](group__bt__l2cap.md#ga5a80330e52ea0fa4ee3266094570bb16) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90);

250 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) psm;

252 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ident;

253 [bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783) required\_sec\_level;

254

255 /\* Response Timeout eXpired (RTX) timer \*/

256 struct [k\_work\_delayable](structk__work__delayable.md) rtx\_work;

257 struct [k\_work\_sync](structk__work__sync.md) rtx\_sync;

258#endif

259

261 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \_pdu\_ready;

263 [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \_pdu\_ready\_lock;

265 size\_t \_pdu\_remaining;

266};

267

[ 277](group__bt__l2cap.md#gac936761e661a5c65d65ee9b4c185679b)#define BT\_L2CAP\_LE\_CHAN(\_ch) CONTAINER\_OF(\_ch, struct bt\_l2cap\_le\_chan, chan)

278

[ 280](group__bt__l2cap.md#gae8b0ef3d8fbadc2e50759f3409196478)#define BT\_L2CAP\_BR\_LINK\_MODE\_BASIC 0x00

[ 282](group__bt__l2cap.md#ga9e524a5a8037eb8d7b6fbdd841635baa)#define BT\_L2CAP\_BR\_LINK\_MODE\_RET 0x01

[ 284](group__bt__l2cap.md#ga1c203f6b730bbb5f045d72a2875e9b75)#define BT\_L2CAP\_BR\_LINK\_MODE\_FC 0x02

[ 286](group__bt__l2cap.md#gacd3f015557ae273dba9255377350b55a)#define BT\_L2CAP\_BR\_LINK\_MODE\_ERET 0x03

[ 288](group__bt__l2cap.md#gaee76903b4b152d0c91fceee162abe8b4)#define BT\_L2CAP\_BR\_LINK\_MODE\_STREAM 0x04

289

[ 291](group__bt__l2cap.md#ga180d1d5cc2cab3d04836fcb556c06463)#define BT\_L2CAP\_BR\_FCS\_NO 0x00

[ 293](group__bt__l2cap.md#ga6e9cfa54d0a08ab33ba420e8ff099dba)#define BT\_L2CAP\_BR\_FCS\_16BIT 0x01

294

[ 296](structbt__l2cap__br__endpoint.md)struct [bt\_l2cap\_br\_endpoint](structbt__l2cap__br__endpoint.md) {

[ 298](structbt__l2cap__br__endpoint.md#acbe4f6cc15bb20703fca53e7084b2ea7) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [cid](structbt__l2cap__br__endpoint.md#acbe4f6cc15bb20703fca53e7084b2ea7);

[ 300](structbt__l2cap__br__endpoint.md#aaeb46128990fe08c926d34049bbc2d6a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [mtu](structbt__l2cap__br__endpoint.md#aaeb46128990fe08c926d34049bbc2d6a);

301#if defined(CONFIG\_BT\_L2CAP\_RET\_FC) || defined(\_\_DOXYGEN\_\_)

[ 305](structbt__l2cap__br__endpoint.md#af49eacd8794e580adc285d95613547f6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mode](structbt__l2cap__br__endpoint.md#af49eacd8794e580adc285d95613547f6);

[ 315](structbt__l2cap__br__endpoint.md#af64e45ea279960b3db213c9ad3e1828c) bool [optional](structbt__l2cap__br__endpoint.md#af64e45ea279960b3db213c9ad3e1828c);

[ 323](structbt__l2cap__br__endpoint.md#a8c66377adf1681079fa446b05eff7e8a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_transmit](structbt__l2cap__br__endpoint.md#a8c66377adf1681079fa446b05eff7e8a);

[ 330](structbt__l2cap__br__endpoint.md#ae5cdb992cd40ce925863e05c7f647f5e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [ret\_timeout](structbt__l2cap__br__endpoint.md#ae5cdb992cd40ce925863e05c7f647f5e);

[ 335](structbt__l2cap__br__endpoint.md#a4f272e96d31b00a3e50d8dcbc2303c57) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [monitor\_timeout](structbt__l2cap__br__endpoint.md#a4f272e96d31b00a3e50d8dcbc2303c57);

[ 337](structbt__l2cap__br__endpoint.md#ab5789c43d09f18f89bffdd829af90a7b) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [mps](structbt__l2cap__br__endpoint.md#ab5789c43d09f18f89bffdd829af90a7b);

[ 343](structbt__l2cap__br__endpoint.md#a2b27b7017ddc68d5b8a597d4be45074c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_window](structbt__l2cap__br__endpoint.md#a2b27b7017ddc68d5b8a597d4be45074c);

[ 354](structbt__l2cap__br__endpoint.md#ac63ef5c2ae54fbcce9380a379a551595) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [fcs](structbt__l2cap__br__endpoint.md#ac63ef5c2ae54fbcce9380a379a551595);

[ 361](structbt__l2cap__br__endpoint.md#aba3184618ab6e8a3db1808041d3a0f8d) bool [extended\_control](structbt__l2cap__br__endpoint.md#aba3184618ab6e8a3db1808041d3a0f8d);

362#endif /\* CONFIG\_BT\_L2CAP\_RET\_FC \*/

363};

364

[ 366](structbt__l2cap__br__window.md)struct [bt\_l2cap\_br\_window](structbt__l2cap__br__window.md) {

[ 367](structbt__l2cap__br__window.md#acff85df74b031445a69c75cad1765e90) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structbt__l2cap__br__window.md#acff85df74b031445a69c75cad1765e90);

368

[ 370](structbt__l2cap__br__window.md#afb66e50f934e763680200ce209ca940c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [tx\_seq](structbt__l2cap__br__window.md#afb66e50f934e763680200ce209ca940c);

[ 372](structbt__l2cap__br__window.md#a781e76efc763c70a9c716f4737fb9243) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [len](structbt__l2cap__br__window.md#a781e76efc763c70a9c716f4737fb9243);

[ 374](structbt__l2cap__br__window.md#a3332cc2a424d1e2d1438232594b81a95) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structbt__l2cap__br__window.md#a3332cc2a424d1e2d1438232594b81a95);

[ 376](structbt__l2cap__br__window.md#ab7bb9eb3949b37973228630b8acacd2f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [transmit\_counter](structbt__l2cap__br__window.md#ab7bb9eb3949b37973228630b8acacd2f);

[ 378](structbt__l2cap__br__window.md#ac2deea3f4fd7893408412ff6599c1a1a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sar](structbt__l2cap__br__window.md#ac2deea3f4fd7893408412ff6599c1a1a);

[ 380](structbt__l2cap__br__window.md#a39456c041bd7d8badde949008835f891) bool [srej](structbt__l2cap__br__window.md#a39456c041bd7d8badde949008835f891);

381 /\* Save PDU state \*/

[ 382](structbt__l2cap__br__window.md#a65acb18fd339978960419ffb2c95111e) struct [net\_buf\_simple\_state](structnet__buf__simple__state.md) [sdu\_state](structbt__l2cap__br__window.md#a65acb18fd339978960419ffb2c95111e);

[ 384](structbt__l2cap__br__window.md#affc53286b080a6914935577ffc15959c) struct [net\_buf](structnet__buf.md) \*[sdu](structbt__l2cap__br__window.md#affc53286b080a6914935577ffc15959c);

[ 386](structbt__l2cap__br__window.md#a3b0a68d77f21c9b02dec816f2c37a479) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sdu\_total\_len](structbt__l2cap__br__window.md#a3b0a68d77f21c9b02dec816f2c37a479);

387};

388

[ 390](structbt__l2cap__br__chan.md)struct [bt\_l2cap\_br\_chan](structbt__l2cap__br__chan.md) {

[ 392](structbt__l2cap__br__chan.md#a28ed2b2541697390c325c706d4ad8f0b) struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) [chan](structbt__l2cap__br__chan.md#a28ed2b2541697390c325c706d4ad8f0b);

[ 394](structbt__l2cap__br__chan.md#a00d49d2d73f2dafdc73a9f7b9393b98d) struct [bt\_l2cap\_br\_endpoint](structbt__l2cap__br__endpoint.md) [rx](structbt__l2cap__br__chan.md#a00d49d2d73f2dafdc73a9f7b9393b98d);

[ 396](structbt__l2cap__br__chan.md#a67aec1f3bef3afe689c164185bd77f98) struct [bt\_l2cap\_br\_endpoint](structbt__l2cap__br__endpoint.md) [tx](structbt__l2cap__br__chan.md#a67aec1f3bef3afe689c164185bd77f98);

397 /\* For internal use only \*/

[ 398](structbt__l2cap__br__chan.md#a09ded589b7e1571fc5d021ceafa68b5f) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [flags](structbt__l2cap__br__chan.md#a09ded589b7e1571fc5d021ceafa68b5f)[1];

399

[ 400](structbt__l2cap__br__chan.md#a556858a2e539bd4d5ed2ae66f392dc74) [bt\_l2cap\_chan\_state\_t](group__bt__l2cap.md#ga5a80330e52ea0fa4ee3266094570bb16) [state](structbt__l2cap__br__chan.md#a556858a2e539bd4d5ed2ae66f392dc74);

[ 402](structbt__l2cap__br__chan.md#a1ca3ed81f6f8edafc2993941de4c9771) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [psm](structbt__l2cap__br__chan.md#a1ca3ed81f6f8edafc2993941de4c9771);

[ 404](structbt__l2cap__br__chan.md#ace996412a41a168c37d60d5e4096dc94) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ident](structbt__l2cap__br__chan.md#ace996412a41a168c37d60d5e4096dc94);

[ 405](structbt__l2cap__br__chan.md#a19bb2e243fb616b73d8b082df7c4a394) [bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783) [required\_sec\_level](structbt__l2cap__br__chan.md#a19bb2e243fb616b73d8b082df7c4a394);

406

407 /\* Response Timeout eXpired (RTX) timer \*/

[ 408](structbt__l2cap__br__chan.md#a0e637544c14d7d2b0ccd2af5424555fb) struct [k\_work\_delayable](structk__work__delayable.md) [rtx\_work](structbt__l2cap__br__chan.md#a0e637544c14d7d2b0ccd2af5424555fb);

[ 409](structbt__l2cap__br__chan.md#a21224ab26501eca21aaed468681d6274) struct [k\_work\_sync](structk__work__sync.md) [rtx\_sync](structbt__l2cap__br__chan.md#a21224ab26501eca21aaed468681d6274);

410

412 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \_pdu\_ready;

414 [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \_pdu\_ready\_lock;

416 [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \_pdu\_tx\_queue;

417

418#if defined(CONFIG\_BT\_L2CAP\_RET\_FC) || defined(\_\_DOXYGEN\_\_)

420 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \_sdu\_total\_len;

421

423 size\_t \_pdu\_remaining;

424

426 struct [net\_buf](structnet__buf.md) \*\_pdu\_buf;

427

429 [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) \_pdu\_outstanding;

430

432 struct [net\_buf\_simple\_state](structnet__buf__simple__state.md) \_pdu\_state;

433

435 struct [k\_fifo](structk__fifo.md) \_free\_tx\_win;

436

[ 438](structbt__l2cap__br__chan.md#a96cb3a6bb3f3c97372c314eb1bfca32b) struct [bt\_l2cap\_br\_window](structbt__l2cap__br__window.md) [tx\_win](structbt__l2cap__br__chan.md#a96cb3a6bb3f3c97372c314eb1bfca32b)[CONFIG\_BT\_L2CAP\_MAX\_WINDOW\_SIZE];

439

441 struct [net\_buf](structnet__buf.md) \*\_sdu;

443 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \_sdu\_len;

444#if defined(CONFIG\_BT\_L2CAP\_SEG\_RECV) || defined(\_\_DOXYGEN\_\_)

445 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \_sdu\_len\_done;

446#endif /\* CONFIG\_BT\_L2CAP\_SEG\_RECV \*/

[ 454](structbt__l2cap__br__chan.md#ad4c352f1d43dce110ddf47c665b7ae17) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [tx\_seq](structbt__l2cap__br__chan.md#ad4c352f1d43dce110ddf47c665b7ae17);

[ 458](structbt__l2cap__br__chan.md#a6e559e94251ce9ef1c7d139695adf7ef) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [next\_tx\_seq](structbt__l2cap__br__chan.md#a6e559e94251ce9ef1c7d139695adf7ef);

[ 462](structbt__l2cap__br__chan.md#ae48194e987caf3153738f3027ec7022d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [expected\_ack\_seq](structbt__l2cap__br__chan.md#ae48194e987caf3153738f3027ec7022d);

[ 470](structbt__l2cap__br__chan.md#afa3dcfc293485a09d76a67c30ee0acf8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [req\_seq](structbt__l2cap__br__chan.md#afa3dcfc293485a09d76a67c30ee0acf8);

[ 473](structbt__l2cap__br__chan.md#a734b9699538989fa8e5cec11eb84609e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [expected\_tx\_seq](structbt__l2cap__br__chan.md#a734b9699538989fa8e5cec11eb84609e);

[ 478](structbt__l2cap__br__chan.md#aa1fd44c5eb136e1fbd0f46f09d5fde0a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [buffer\_seq](structbt__l2cap__br__chan.md#aa1fd44c5eb136e1fbd0f46f09d5fde0a);

479

[ 483](structbt__l2cap__br__chan.md#a3f9621b9d02b70f1dc9492520ff7cd03) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [retry\_count](structbt__l2cap__br__chan.md#a3f9621b9d02b70f1dc9492520ff7cd03);

[ 485](structbt__l2cap__br__chan.md#a97266be01c9ee7e5f64f182173d50418) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [srej\_save\_req\_seq](structbt__l2cap__br__chan.md#a97266be01c9ee7e5f64f182173d50418);

486

[ 488](structbt__l2cap__br__chan.md#a6a1788de2f5c037b46070a65c2a1111d) struct [k\_work\_delayable](structk__work__delayable.md) [ret\_work](structbt__l2cap__br__chan.md#a6a1788de2f5c037b46070a65c2a1111d);

[ 490](structbt__l2cap__br__chan.md#ac887d3192240594de4d6cb8d4af9553b) struct [k\_work\_delayable](structk__work__delayable.md) [monitor\_work](structbt__l2cap__br__chan.md#ac887d3192240594de4d6cb8d4af9553b);

491#endif /\* CONFIG\_BT\_L2CAP\_RET\_FC \*/

492};

493

[ 498](structbt__l2cap__chan__ops.md)struct [bt\_l2cap\_chan\_ops](structbt__l2cap__chan__ops.md) {

[ 506](structbt__l2cap__chan__ops.md#a3a4dd75a11c9867adcade6d288dec2de) void (\*[connected](structbt__l2cap__chan__ops.md#a3a4dd75a11c9867adcade6d288dec2de))(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan);

507

[ 516](structbt__l2cap__chan__ops.md#a2e5fcc77a5174de6e3933bb6a14e4ad3) void (\*[disconnected](structbt__l2cap__chan__ops.md#a2e5fcc77a5174de6e3933bb6a14e4ad3))(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan);

517

[ 533](structbt__l2cap__chan__ops.md#ab973539dd8b5e3ab115042a03362f141) void (\*[encrypt\_change](structbt__l2cap__chan__ops.md#a12f3290f9bd04fb5fe562c620dff6984))(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) hci\_status);

534

546 struct [net\_buf](structnet__buf.md) \*(\*alloc\_seg)(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan);

547

560 struct [net\_buf](structnet__buf.md) \*(\*alloc\_buf)(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan);

561

[ 584](structbt__l2cap__chan__ops.md#a0ab419d3c52c08e0dfda236466d7cadd) int (\*[recv](structbt__l2cap__chan__ops.md#a0ab419d3c52c08e0dfda236466d7cadd))(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan, struct [net\_buf](structnet__buf.md) \*buf);

585

[ 595](structbt__l2cap__chan__ops.md#a770c09f3fb10c9d1e069333d22803d1a) void (\*[sent](structbt__l2cap__chan__ops.md#a770c09f3fb10c9d1e069333d22803d1a))(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan);

596

[ 605](structbt__l2cap__chan__ops.md#a4be7fadf07368750cc33cf034d3073e7) void (\*[status](structbt__l2cap__chan__ops.md#a4be7fadf07368750cc33cf034d3073e7))(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan, [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) \*[status](structbt__l2cap__chan__ops.md#a4be7fadf07368750cc33cf034d3073e7));

606

607 /\* @brief Channel released callback

608 \*

609 \* If this callback is set it is called when the stack has release all

610 \* references to the channel object.

611 \*/

[ 612](structbt__l2cap__chan__ops.md#a6d974d0e472626cb1e5cd898a3dcbca6) void (\*[released](structbt__l2cap__chan__ops.md#a6d974d0e472626cb1e5cd898a3dcbca6))(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan);

613

[ 622](structbt__l2cap__chan__ops.md#afba426353897bc3a57c936a98acab839) void (\*[reconfigured](structbt__l2cap__chan__ops.md#afba426353897bc3a57c936a98acab839))(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan);

623

624#if defined(CONFIG\_BT\_L2CAP\_SEG\_RECV)

[ 656](structbt__l2cap__chan__ops.md#a7759a713038d74748952d5f2eb712429) void (\*[seg\_recv](structbt__l2cap__chan__ops.md#a7759a713038d74748952d5f2eb712429))(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan, size\_t sdu\_len,

657 [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) seg\_offset, struct [net\_buf\_simple](structnet__buf__simple.md) \*seg);

658#endif /\* CONFIG\_BT\_L2CAP\_SEG\_RECV \*/

659};

660

[ 664](group__bt__l2cap.md#ga281232ec622c626c0be2be23bae18d8d)#define BT\_L2CAP\_CHAN\_SEND\_RESERVE (BT\_L2CAP\_BUF\_SIZE(0))

665

[ 669](group__bt__l2cap.md#gabdb3983d3862f6654a1653dd45c4157d)#define BT\_L2CAP\_SDU\_CHAN\_SEND\_RESERVE (BT\_L2CAP\_SDU\_BUF\_SIZE(0))

670

[ 672](structbt__l2cap__server.md)struct [bt\_l2cap\_server](structbt__l2cap__server.md) {

[ 702](structbt__l2cap__server.md#a07925dda8566ee7518b1809725e1b110) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [psm](structbt__l2cap__server.md#a07925dda8566ee7518b1809725e1b110);

703

[ 705](structbt__l2cap__server.md#a9f082abf679a397264a7b51fa4400852) [bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783) [sec\_level](structbt__l2cap__server.md#a9f082abf679a397264a7b51fa4400852);

706

[ 724](structbt__l2cap__server.md#ad31a1908f7dc733f9497164ccabba2af) int (\*[accept](structbt__l2cap__server.md#ad31a1908f7dc733f9497164ccabba2af))(struct bt\_conn \*conn, struct [bt\_l2cap\_server](structbt__l2cap__server.md) \*server,

725 struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*\*chan);

726

[ 727](structbt__l2cap__server.md#a76b478140d6a57038eb389eac91442c0) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structbt__l2cap__server.md#a76b478140d6a57038eb389eac91442c0);

728};

729

[ 749](group__bt__l2cap.md#ga1a5e8c81c086872d7fb8da5329f982c6)int [bt\_l2cap\_server\_register](group__bt__l2cap.md#ga1a5e8c81c086872d7fb8da5329f982c6)(struct [bt\_l2cap\_server](structbt__l2cap__server.md) \*server);

750

[ 770](group__bt__l2cap.md#ga5b0ae2abd714f46e6bb2394bce33e613)int [bt\_l2cap\_br\_server\_register](group__bt__l2cap.md#ga5b0ae2abd714f46e6bb2394bce33e613)(struct [bt\_l2cap\_server](structbt__l2cap__server.md) \*server);

771

[ 787](group__bt__l2cap.md#gaebc2d157fb5f013722e9c332b3d81804)int [bt\_l2cap\_ecred\_chan\_connect](group__bt__l2cap.md#gaebc2d157fb5f013722e9c332b3d81804)(struct bt\_conn \*[conn](structbt__l2cap__chan.md#a007a7ef11a00c0dff22cd64961260d3d),

788 struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*\*chans, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) psm);

789

[ 802](group__bt__l2cap.md#ga05d28a51d9fba08d609287957ea4c7ec)int [bt\_l2cap\_ecred\_chan\_reconfigure](group__bt__l2cap.md#ga05d28a51d9fba08d609287957ea4c7ec)(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*\*chans, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mtu);

803

[ 847](group__bt__l2cap.md#ga67e13b0048eb68ef35c315a5276d832d)int [bt\_l2cap\_ecred\_chan\_reconfigure\_explicit](group__bt__l2cap.md#ga67e13b0048eb68ef35c315a5276d832d)(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*\*chans, size\_t chan\_count,

848 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mtu, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mps);

849

[ 871](group__bt__l2cap.md#ga3c3cfb4b151c808c0a3d2562a5c26a20)int [bt\_l2cap\_chan\_connect](group__bt__l2cap.md#ga3c3cfb4b151c808c0a3d2562a5c26a20)(struct bt\_conn \*[conn](structbt__l2cap__chan.md#a007a7ef11a00c0dff22cd64961260d3d), struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan,

872 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) psm);

873

[ 885](group__bt__l2cap.md#ga7165f82a05e3a19d6b2baf0ba292a3fe)int [bt\_l2cap\_chan\_disconnect](group__bt__l2cap.md#ga7165f82a05e3a19d6b2baf0ba292a3fe)(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan);

886

[ 931](group__bt__l2cap.md#ga97b7909749667f910f83e6fcb54495c3)int [bt\_l2cap\_chan\_send](group__bt__l2cap.md#ga97b7909749667f910f83e6fcb54495c3)(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan, struct [net\_buf](structnet__buf.md) \*buf);

932

[ 954](group__bt__l2cap.md#ga9bc950a929fc2bdb1463c268cea478b6)int [bt\_l2cap\_chan\_give\_credits](group__bt__l2cap.md#ga9bc950a929fc2bdb1463c268cea478b6)(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) additional\_credits);

955

[ 968](group__bt__l2cap.md#gad53f5fc31314121ff84e740879eae3cf)int [bt\_l2cap\_chan\_recv\_complete](group__bt__l2cap.md#gad53f5fc31314121ff84e740879eae3cf)(struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan,

969 struct [net\_buf](structnet__buf.md) \*buf);

970

971#ifdef \_\_cplusplus

972}

973#endif

974

978

979#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_L2CAP\_H\_ \*/

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[buf.h](buf_8h.md)

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

**Definition** conn.h:814

[bt\_l2cap\_ecred\_chan\_reconfigure](group__bt__l2cap.md#ga05d28a51d9fba08d609287957ea4c7ec)

int bt\_l2cap\_ecred\_chan\_reconfigure(struct bt\_l2cap\_chan \*\*chans, uint16\_t mtu)

Reconfigure Enhanced Credit Based L2CAP channels.

[bt\_l2cap\_server\_register](group__bt__l2cap.md#ga1a5e8c81c086872d7fb8da5329f982c6)

int bt\_l2cap\_server\_register(struct bt\_l2cap\_server \*server)

Register L2CAP server.

[bt\_l2cap\_chan\_status](group__bt__l2cap.md#ga371a747c8939a1156111dc03c774015c)

bt\_l2cap\_chan\_status

Status of L2CAP channel.

**Definition** l2cap.h:164

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

**Definition** l2cap.h:149

[bt\_l2cap\_ecred\_chan\_reconfigure\_explicit](group__bt__l2cap.md#ga67e13b0048eb68ef35c315a5276d832d)

int bt\_l2cap\_ecred\_chan\_reconfigure\_explicit(struct bt\_l2cap\_chan \*\*chans, size\_t chan\_count, uint16\_t mtu, uint16\_t mps)

Reconfigure Enhanced Credit Based L2CAP channels.

[bt\_l2cap\_chan\_disconnect](group__bt__l2cap.md#ga7165f82a05e3a19d6b2baf0ba292a3fe)

int bt\_l2cap\_chan\_disconnect(struct bt\_l2cap\_chan \*chan)

Disconnect L2CAP channel.

[bt\_l2cap\_chan\_destroy\_t](group__bt__l2cap.md#ga88baae9c159f3de4ccb34fd0e3cc8c3b)

void(\* bt\_l2cap\_chan\_destroy\_t)(struct bt\_l2cap\_chan \*chan)

Channel destroy callback.

**Definition** l2cap.h:135

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

**Definition** l2cap.h:173

[BT\_L2CAP\_STATUS\_OUT](group__bt__l2cap.md#gga371a747c8939a1156111dc03c774015ca89aea3cf3d9a004ffd53eae602666fd5)

@ BT\_L2CAP\_STATUS\_OUT

Channel can send at least one PDU.

**Definition** l2cap.h:166

[BT\_L2CAP\_NUM\_STATUS](group__bt__l2cap.md#gga371a747c8939a1156111dc03c774015ca91bd77f9889b59ba5b0005a51016ba2c)

@ BT\_L2CAP\_NUM\_STATUS

**Definition** l2cap.h:179

[BT\_L2CAP\_STATUS\_ENCRYPT\_PENDING](group__bt__l2cap.md#gga371a747c8939a1156111dc03c774015caea6cc7cae26d69926e7def91242650af)

@ BT\_L2CAP\_STATUS\_ENCRYPT\_PENDING

Channel encryption pending status.

**Definition** l2cap.h:176

[BT\_L2CAP\_DISCONNECTED](group__bt__l2cap.md#gga642436bdf29f79495763b10231c6b25ba1dc4c69537acf13a8c00dfca5acfb83c)

@ BT\_L2CAP\_DISCONNECTED

Channel disconnected.

**Definition** l2cap.h:151

[BT\_L2CAP\_CONFIG](group__bt__l2cap.md#gga642436bdf29f79495763b10231c6b25ba3167a1b491cb9b97ebe51f66c209f064)

@ BT\_L2CAP\_CONFIG

Channel in config state, BR/EDR specific.

**Definition** l2cap.h:155

[BT\_L2CAP\_CONNECTED](group__bt__l2cap.md#gga642436bdf29f79495763b10231c6b25ba3adc86576ca2db5a7f74030d11699b68)

@ BT\_L2CAP\_CONNECTED

Channel ready for upper layer traffic on it.

**Definition** l2cap.h:157

[BT\_L2CAP\_DISCONNECTING](group__bt__l2cap.md#gga642436bdf29f79495763b10231c6b25ba7a24502cfb06df715f58ad2e088cb7e8)

@ BT\_L2CAP\_DISCONNECTING

Channel in disconnecting state.

**Definition** l2cap.h:159

[BT\_L2CAP\_CONNECTING](group__bt__l2cap.md#gga642436bdf29f79495763b10231c6b25bac2a46c646c8739e8b129b89698eae7cd)

@ BT\_L2CAP\_CONNECTING

Channel in connecting state.

**Definition** l2cap.h:153

[sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8)

struct \_slist sys\_slist\_t

Single-linked list structure.

**Definition** slist.h:49

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[hci.h](hci_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f)

\_\_INTPTR\_TYPE\_\_ off\_t

**Definition** types.h:36

[net\_buf.h](net__buf_8h.md)

Buffer management.

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[slist.h](slist_8h.md)

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[bt\_l2cap\_br\_chan](structbt__l2cap__br__chan.md)

BREDR L2CAP Channel structure.

**Definition** l2cap.h:390

[bt\_l2cap\_br\_chan::rx](structbt__l2cap__br__chan.md#a00d49d2d73f2dafdc73a9f7b9393b98d)

struct bt\_l2cap\_br\_endpoint rx

Channel Receiving Endpoint.

**Definition** l2cap.h:394

[bt\_l2cap\_br\_chan::flags](structbt__l2cap__br__chan.md#a09ded589b7e1571fc5d021ceafa68b5f)

atomic\_t flags[1]

**Definition** l2cap.h:398

[bt\_l2cap\_br\_chan::rtx\_work](structbt__l2cap__br__chan.md#a0e637544c14d7d2b0ccd2af5424555fb)

struct k\_work\_delayable rtx\_work

**Definition** l2cap.h:408

[bt\_l2cap\_br\_chan::required\_sec\_level](structbt__l2cap__br__chan.md#a19bb2e243fb616b73d8b082df7c4a394)

bt\_security\_t required\_sec\_level

**Definition** l2cap.h:405

[bt\_l2cap\_br\_chan::psm](structbt__l2cap__br__chan.md#a1ca3ed81f6f8edafc2993941de4c9771)

uint16\_t psm

Remote PSM to be connected.

**Definition** l2cap.h:402

[bt\_l2cap\_br\_chan::rtx\_sync](structbt__l2cap__br__chan.md#a21224ab26501eca21aaed468681d6274)

struct k\_work\_sync rtx\_sync

**Definition** l2cap.h:409

[bt\_l2cap\_br\_chan::chan](structbt__l2cap__br__chan.md#a28ed2b2541697390c325c706d4ad8f0b)

struct bt\_l2cap\_chan chan

Common L2CAP channel reference object.

**Definition** l2cap.h:392

[bt\_l2cap\_br\_chan::retry\_count](structbt__l2cap__br__chan.md#a3f9621b9d02b70f1dc9492520ff7cd03)

uint16\_t retry\_count

**Definition** l2cap.h:483

[bt\_l2cap\_br\_chan::state](structbt__l2cap__br__chan.md#a556858a2e539bd4d5ed2ae66f392dc74)

bt\_l2cap\_chan\_state\_t state

**Definition** l2cap.h:400

[bt\_l2cap\_br\_chan::tx](structbt__l2cap__br__chan.md#a67aec1f3bef3afe689c164185bd77f98)

struct bt\_l2cap\_br\_endpoint tx

Channel Transmission Endpoint.

**Definition** l2cap.h:396

[bt\_l2cap\_br\_chan::ret\_work](structbt__l2cap__br__chan.md#a6a1788de2f5c037b46070a65c2a1111d)

struct k\_work\_delayable ret\_work

**Definition** l2cap.h:488

[bt\_l2cap\_br\_chan::next\_tx\_seq](structbt__l2cap__br__chan.md#a6e559e94251ce9ef1c7d139695adf7ef)

uint16\_t next\_tx\_seq

**Definition** l2cap.h:458

[bt\_l2cap\_br\_chan::expected\_tx\_seq](structbt__l2cap__br__chan.md#a734b9699538989fa8e5cec11eb84609e)

uint16\_t expected\_tx\_seq

**Definition** l2cap.h:473

[bt\_l2cap\_br\_chan::tx\_win](structbt__l2cap__br__chan.md#a96cb3a6bb3f3c97372c314eb1bfca32b)

struct bt\_l2cap\_br\_window tx\_win[CONFIG\_BT\_L2CAP\_MAX\_WINDOW\_SIZE]

**Definition** l2cap.h:438

[bt\_l2cap\_br\_chan::srej\_save\_req\_seq](structbt__l2cap__br__chan.md#a97266be01c9ee7e5f64f182173d50418)

uint16\_t srej\_save\_req\_seq

**Definition** l2cap.h:485

[bt\_l2cap\_br\_chan::buffer\_seq](structbt__l2cap__br__chan.md#aa1fd44c5eb136e1fbd0f46f09d5fde0a)

uint16\_t buffer\_seq

**Definition** l2cap.h:478

[bt\_l2cap\_br\_chan::monitor\_work](structbt__l2cap__br__chan.md#ac887d3192240594de4d6cb8d4af9553b)

struct k\_work\_delayable monitor\_work

**Definition** l2cap.h:490

[bt\_l2cap\_br\_chan::ident](structbt__l2cap__br__chan.md#ace996412a41a168c37d60d5e4096dc94)

uint8\_t ident

Helps match request context during CoC.

**Definition** l2cap.h:404

[bt\_l2cap\_br\_chan::tx\_seq](structbt__l2cap__br__chan.md#ad4c352f1d43dce110ddf47c665b7ae17)

uint16\_t tx\_seq

**Definition** l2cap.h:454

[bt\_l2cap\_br\_chan::expected\_ack\_seq](structbt__l2cap__br__chan.md#ae48194e987caf3153738f3027ec7022d)

uint16\_t expected\_ack\_seq

**Definition** l2cap.h:462

[bt\_l2cap\_br\_chan::req\_seq](structbt__l2cap__br__chan.md#afa3dcfc293485a09d76a67c30ee0acf8)

uint16\_t req\_seq

**Definition** l2cap.h:470

[bt\_l2cap\_br\_endpoint](structbt__l2cap__br__endpoint.md)

BREDR L2CAP Endpoint structure.

**Definition** l2cap.h:296

[bt\_l2cap\_br\_endpoint::max\_window](structbt__l2cap__br__endpoint.md#a2b27b7017ddc68d5b8a597d4be45074c)

uint16\_t max\_window

Endpoint Maximum Window Size MAX supported window size is configured by @kconfig{BT\_L2CAP\_MAX\_WINDOW\_...

**Definition** l2cap.h:343

[bt\_l2cap\_br\_endpoint::monitor\_timeout](structbt__l2cap__br__endpoint.md#a4f272e96d31b00a3e50d8dcbc2303c57)

uint16\_t monitor\_timeout

Endpoint Monitor Timeout The field is configured by @kconfig{BT\_L2CAP\_BR\_MONITOR\_TIMEOUT}...

**Definition** l2cap.h:335

[bt\_l2cap\_br\_endpoint::max\_transmit](structbt__l2cap__br__endpoint.md#a8c66377adf1681079fa446b05eff7e8a)

uint8\_t max\_transmit

Endpoint Maximum Transmit The field is used to set the max retransmission count.

**Definition** l2cap.h:323

[bt\_l2cap\_br\_endpoint::mtu](structbt__l2cap__br__endpoint.md#aaeb46128990fe08c926d34049bbc2d6a)

uint16\_t mtu

Endpoint Maximum Transmission Unit.

**Definition** l2cap.h:300

[bt\_l2cap\_br\_endpoint::mps](structbt__l2cap__br__endpoint.md#ab5789c43d09f18f89bffdd829af90a7b)

uint16\_t mps

Endpoint Maximum PDU payload Size.

**Definition** l2cap.h:337

[bt\_l2cap\_br\_endpoint::extended\_control](structbt__l2cap__br__endpoint.md#aba3184618ab6e8a3db1808041d3a0f8d)

bool extended\_control

Endpoint Extended Control.

**Definition** l2cap.h:361

[bt\_l2cap\_br\_endpoint::fcs](structbt__l2cap__br__endpoint.md#ac63ef5c2ae54fbcce9380a379a551595)

uint8\_t fcs

Endpoint FCS Type The value is defined as BT\_L2CAP\_BR\_FCS\_\* The default setting should be BT\_L2CAP\_BR...

**Definition** l2cap.h:354

[bt\_l2cap\_br\_endpoint::cid](structbt__l2cap__br__endpoint.md#acbe4f6cc15bb20703fca53e7084b2ea7)

uint16\_t cid

Endpoint Channel Identifier (CID).

**Definition** l2cap.h:298

[bt\_l2cap\_br\_endpoint::ret\_timeout](structbt__l2cap__br__endpoint.md#ae5cdb992cd40ce925863e05c7f647f5e)

uint16\_t ret\_timeout

Endpoint Retransmission Timeout The field is configured by @kconfig{BT\_L2CAP\_BR\_RET\_TIMEOUT}...

**Definition** l2cap.h:330

[bt\_l2cap\_br\_endpoint::mode](structbt__l2cap__br__endpoint.md#af49eacd8794e580adc285d95613547f6)

uint8\_t mode

Endpoint Link Mode.

**Definition** l2cap.h:305

[bt\_l2cap\_br\_endpoint::optional](structbt__l2cap__br__endpoint.md#af64e45ea279960b3db213c9ad3e1828c)

bool optional

Whether Endpoint Link Mode is optional If the optional is true, the mode could be changed according t...

**Definition** l2cap.h:315

[bt\_l2cap\_br\_window](structbt__l2cap__br__window.md)

I-Frame transmission window for none BASIC mode L2cap connected channel.

**Definition** l2cap.h:366

[bt\_l2cap\_br\_window::data](structbt__l2cap__br__window.md#a3332cc2a424d1e2d1438232594b81a95)

uint8\_t \* data

data address

**Definition** l2cap.h:374

[bt\_l2cap\_br\_window::srej](structbt__l2cap__br__window.md#a39456c041bd7d8badde949008835f891)

bool srej

srej flag

**Definition** l2cap.h:380

[bt\_l2cap\_br\_window::sdu\_total\_len](structbt__l2cap__br__window.md#a3b0a68d77f21c9b02dec816f2c37a479)

uint16\_t sdu\_total\_len

**Definition** l2cap.h:386

[bt\_l2cap\_br\_window::sdu\_state](structbt__l2cap__br__window.md#a65acb18fd339978960419ffb2c95111e)

struct net\_buf\_simple\_state sdu\_state

**Definition** l2cap.h:382

[bt\_l2cap\_br\_window::len](structbt__l2cap__br__window.md#a781e76efc763c70a9c716f4737fb9243)

uint16\_t len

data len

**Definition** l2cap.h:372

[bt\_l2cap\_br\_window::transmit\_counter](structbt__l2cap__br__window.md#ab7bb9eb3949b37973228630b8acacd2f)

uint8\_t transmit\_counter

Transmit Counter.

**Definition** l2cap.h:376

[bt\_l2cap\_br\_window::sar](structbt__l2cap__br__window.md#ac2deea3f4fd7893408412ff6599c1a1a)

uint8\_t sar

SAR flag.

**Definition** l2cap.h:378

[bt\_l2cap\_br\_window::node](structbt__l2cap__br__window.md#acff85df74b031445a69c75cad1765e90)

sys\_snode\_t node

**Definition** l2cap.h:367

[bt\_l2cap\_br\_window::tx\_seq](structbt__l2cap__br__window.md#afb66e50f934e763680200ce209ca940c)

uint16\_t tx\_seq

tx seq

**Definition** l2cap.h:370

[bt\_l2cap\_br\_window::sdu](structbt__l2cap__br__window.md#affc53286b080a6914935577ffc15959c)

struct net\_buf \* sdu

**Definition** l2cap.h:384

[bt\_l2cap\_chan\_ops](structbt__l2cap__chan__ops.md)

L2CAP Channel operations structure.

**Definition** l2cap.h:498

[bt\_l2cap\_chan\_ops::recv](structbt__l2cap__chan__ops.md#a0ab419d3c52c08e0dfda236466d7cadd)

int(\* recv)(struct bt\_l2cap\_chan \*chan, struct net\_buf \*buf)

Channel recv callback.

**Definition** l2cap.h:584

[bt\_l2cap\_chan\_ops::encrypt\_change](structbt__l2cap__chan__ops.md#a12f3290f9bd04fb5fe562c620dff6984)

void(\* encrypt\_change)(struct bt\_l2cap\_chan \*chan, uint8\_t hci\_status)

Channel encrypt\_change callback.

**Definition** l2cap.h:533

[bt\_l2cap\_chan\_ops::disconnected](structbt__l2cap__chan__ops.md#a2e5fcc77a5174de6e3933bb6a14e4ad3)

void(\* disconnected)(struct bt\_l2cap\_chan \*chan)

Channel disconnected callback.

**Definition** l2cap.h:516

[bt\_l2cap\_chan\_ops::connected](structbt__l2cap__chan__ops.md#a3a4dd75a11c9867adcade6d288dec2de)

void(\* connected)(struct bt\_l2cap\_chan \*chan)

Channel connected callback.

**Definition** l2cap.h:506

[bt\_l2cap\_chan\_ops::status](structbt__l2cap__chan__ops.md#a4be7fadf07368750cc33cf034d3073e7)

void(\* status)(struct bt\_l2cap\_chan \*chan, atomic\_t \*status)

Channel status callback.

**Definition** l2cap.h:605

[bt\_l2cap\_chan\_ops::released](structbt__l2cap__chan__ops.md#a6d974d0e472626cb1e5cd898a3dcbca6)

void(\* released)(struct bt\_l2cap\_chan \*chan)

**Definition** l2cap.h:612

[bt\_l2cap\_chan\_ops::sent](structbt__l2cap__chan__ops.md#a770c09f3fb10c9d1e069333d22803d1a)

void(\* sent)(struct bt\_l2cap\_chan \*chan)

Channel sent callback.

**Definition** l2cap.h:595

[bt\_l2cap\_chan\_ops::seg\_recv](structbt__l2cap__chan__ops.md#a7759a713038d74748952d5f2eb712429)

void(\* seg\_recv)(struct bt\_l2cap\_chan \*chan, size\_t sdu\_len, off\_t seg\_offset, struct net\_buf\_simple \*seg)

Handle L2CAP segments directly.

**Definition** l2cap.h:656

[bt\_l2cap\_chan\_ops::reconfigured](structbt__l2cap__chan__ops.md#afba426353897bc3a57c936a98acab839)

void(\* reconfigured)(struct bt\_l2cap\_chan \*chan)

Channel reconfigured callback.

**Definition** l2cap.h:622

[bt\_l2cap\_chan](structbt__l2cap__chan.md)

L2CAP Channel structure.

**Definition** l2cap.h:183

[bt\_l2cap\_chan::conn](structbt__l2cap__chan.md#a007a7ef11a00c0dff22cd64961260d3d)

struct bt\_conn \* conn

Channel connection reference.

**Definition** l2cap.h:185

[bt\_l2cap\_chan::node](structbt__l2cap__chan.md#a123ae4bb1db6f4b41561b3d4691b1c02)

sys\_snode\_t node

**Definition** l2cap.h:188

[bt\_l2cap\_chan::ops](structbt__l2cap__chan.md#a3e370744f17ca4cff200cc0a2ee1a74b)

const struct bt\_l2cap\_chan\_ops \* ops

Channel operations reference.

**Definition** l2cap.h:187

[bt\_l2cap\_chan::status](structbt__l2cap__chan.md#a7603e2c212e0522a1ffca2198224a994)

atomic\_t status[ATOMIC\_BITMAP\_SIZE(BT\_L2CAP\_NUM\_STATUS)]

**Definition** l2cap.h:191

[bt\_l2cap\_chan::destroy](structbt__l2cap__chan.md#ac0fbde11b35e0b6b424970e73c945a40)

bt\_l2cap\_chan\_destroy\_t destroy

**Definition** l2cap.h:189

[bt\_l2cap\_le\_chan](structbt__l2cap__le__chan.md)

LE L2CAP Channel structure.

**Definition** l2cap.h:207

[bt\_l2cap\_le\_chan::tx](structbt__l2cap__le__chan.md#a059f98cebf6f43a05937ac82815009e7)

struct bt\_l2cap\_le\_endpoint tx

Channel Transmission Endpoint.

**Definition** l2cap.h:234

[bt\_l2cap\_le\_chan::pending\_rx\_mtu](structbt__l2cap__le__chan.md#a55d8ce850f365ac7ab7ff450ecb61f23)

uint16\_t pending\_rx\_mtu

Pending RX MTU on ECFC reconfigure, used internally by stack.

**Definition** l2cap.h:225

[bt\_l2cap\_le\_chan::tx\_queue](structbt__l2cap__le__chan.md#a716ea69cb7261076023d0cf6384b3ebb)

struct k\_fifo tx\_queue

Channel Transmission queue (for SDUs).

**Definition** l2cap.h:236

[bt\_l2cap\_le\_chan::rx](structbt__l2cap__le__chan.md#a95808ad9bcd910b65bee31fa6bd4b638)

struct bt\_l2cap\_le\_endpoint rx

Channel Receiving Endpoint.

**Definition** l2cap.h:222

[bt\_l2cap\_le\_chan::chan](structbt__l2cap__le__chan.md#a980126cabc3824ab623d634d91f7d761)

struct bt\_l2cap\_chan chan

Common L2CAP channel reference object.

**Definition** l2cap.h:209

[bt\_l2cap\_le\_endpoint](structbt__l2cap__le__endpoint.md)

LE L2CAP Endpoint structure.

**Definition** l2cap.h:195

[bt\_l2cap\_le\_endpoint::mtu](structbt__l2cap__le__endpoint.md#a598f0c7f0ad4cc029013358d35ce9dc2)

uint16\_t mtu

Endpoint Maximum Transmission Unit.

**Definition** l2cap.h:199

[bt\_l2cap\_le\_endpoint::mps](structbt__l2cap__le__endpoint.md#aa9e4f21e48eda61a3d0b777ee13c2599)

uint16\_t mps

Endpoint Maximum PDU payload Size.

**Definition** l2cap.h:201

[bt\_l2cap\_le\_endpoint::credits](structbt__l2cap__le__endpoint.md#ab3f475c383791731c595845c80c27edf)

atomic\_t credits

Endpoint credits.

**Definition** l2cap.h:203

[bt\_l2cap\_le\_endpoint::cid](structbt__l2cap__le__endpoint.md#aeee85135541b17bede098891b820c63f)

uint16\_t cid

Endpoint Channel Identifier (CID).

**Definition** l2cap.h:197

[bt\_l2cap\_server](structbt__l2cap__server.md)

L2CAP Server structure.

**Definition** l2cap.h:672

[bt\_l2cap\_server::psm](structbt__l2cap__server.md#a07925dda8566ee7518b1809725e1b110)

uint16\_t psm

Server PSM.

**Definition** l2cap.h:702

[bt\_l2cap\_server::node](structbt__l2cap__server.md#a76b478140d6a57038eb389eac91442c0)

sys\_snode\_t node

**Definition** l2cap.h:727

[bt\_l2cap\_server::sec\_level](structbt__l2cap__server.md#a9f082abf679a397264a7b51fa4400852)

bt\_security\_t sec\_level

Required minimum security level.

**Definition** l2cap.h:705

[bt\_l2cap\_server::accept](structbt__l2cap__server.md#ad31a1908f7dc733f9497164ccabba2af)

int(\* accept)(struct bt\_conn \*conn, struct bt\_l2cap\_server \*server, struct bt\_l2cap\_chan \*\*chan)

Server accept callback.

**Definition** l2cap.h:724

[k\_fifo](structk__fifo.md)

**Definition** kernel.h:2540

[k\_work\_delayable](structk__work__delayable.md)

A structure used to submit work after a delay.

**Definition** kernel.h:4101

[k\_work\_sync](structk__work__sync.md)

A structure holding internal state for a pending synchronous operation on a work item or queue.

**Definition** kernel.h:4184

[k\_work](structk__work.md)

A structure used to submit work.

**Definition** kernel.h:4073

[net\_buf\_simple\_state](structnet__buf__simple__state.md)

Parsing state of a buffer.

**Definition** net\_buf.h:950

[net\_buf\_simple](structnet__buf__simple.md)

Simple network buffer representation.

**Definition** net\_buf.h:89

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** net\_buf.h:1006

[atomic.h](sys_2atomic_8h.md)

[util.h](sys_2util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [l2cap.h](l2cap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
