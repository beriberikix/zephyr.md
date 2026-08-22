---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/iso_8h_source.html
original_path: doxygen/html/iso_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

iso.h

[Go to the documentation of this file.](iso_8h.md)

1

5

6/\*

7 \* Copyright (c) 2020 Intel Corporation

8 \* Copyright (c) 2021-2025 Nordic Semiconductor ASA

9 \*

10 \* SPDX-License-Identifier: Apache-2.0

11 \*/

12#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_ISO\_H\_

13#define ZEPHYR\_INCLUDE\_BLUETOOTH\_ISO\_H\_

14

25

26#include <[stdint.h](stdint_8h.md)>

27#include <stddef.h>

28

29#include <[zephyr/bluetooth/addr.h](addr_8h.md)>

30#include <[zephyr/bluetooth/bluetooth.h](bluetooth_2bluetooth_8h.md)>

31#include <[zephyr/bluetooth/buf.h](buf_8h.md)>

32#include <[zephyr/bluetooth/conn.h](conn_8h.md)>

33#include <[zephyr/bluetooth/hci.h](hci_8h.md)>

34#include <[zephyr/net\_buf.h](net__buf_8h.md)>

35#include <[zephyr/sys/atomic.h](sys_2atomic_8h.md)>

36#include <[zephyr/sys/slist.h](slist_8h.md)>

37#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

38#include <[zephyr/sys/slist.h](slist_8h.md)>

39

40#ifdef \_\_cplusplus

41extern "C" {

42#endif

43

[ 47](group__bt__iso.md#ga15c9cafd39e89f07eef115e147741098)#define BT\_ISO\_CHAN\_SEND\_RESERVE BT\_BUF\_ISO\_SIZE(0)

48

[ 57](group__bt__iso.md#ga3c0af738d118341da7d370aaa48a89d1)#define BT\_ISO\_SDU\_BUF\_SIZE(mtu) BT\_BUF\_ISO\_SIZE(mtu)

58

[ 67](group__bt__iso.md#ga01b975b441fa5d8f039562ab66857bbf)#define BT\_ISO\_BIS\_INDEX\_BIT(x) (BIT((x) - 1))

68

[ 70](group__bt__iso.md#gadd421c69edccfd695d728ded5feb6862)#define BT\_ISO\_DATA\_PATH\_HCI 0x00

71

[ 73](group__bt__iso.md#ga4f0cc6262171fbee9d0ef173123b8f3d)#define BT\_ISO\_SDU\_INTERVAL\_UNKNOWN 0x000000U

[ 75](group__bt__iso.md#ga9f26e30d05e571d3fc33dec8ae693e45)#define BT\_ISO\_DATA\_PATH\_VS\_ID\_MIN 0x01

[ 77](group__bt__iso.md#gae5e1f7c86165b26fc6d93bc922676f9a)#define BT\_ISO\_DATA\_PATH\_VS\_ID\_MAX 0xFE

[ 79](group__bt__iso.md#ga29bf2b36a4ab4e1325f626bbcf52a9a6)#define BT\_ISO\_CONTROLLER\_DELAY\_MIN 0x000000

[ 81](group__bt__iso.md#gae6ba7c8ea447112bcd7798d0351a9a91)#define BT\_ISO\_CONTROLLER\_DELAY\_MAX 0x3D0900

[ 83](group__bt__iso.md#ga8122de88b6e5423dca653b1f0a484316)#define BT\_ISO\_SDU\_INTERVAL\_MIN 0x0000FFU

[ 85](group__bt__iso.md#ga077eb6d219bba947d363e2cce8e0080c)#define BT\_ISO\_SDU\_INTERVAL\_MAX 0x0FFFFFU

[ 87](group__bt__iso.md#ga5cc5e9fd5e7af83eeaab8fe2fd16b9de)#define BT\_ISO\_ISO\_INTERVAL\_MIN 0x0004U

[ 89](group__bt__iso.md#gabc381a7f565061ec91d23b7783521da3)#define BT\_ISO\_ISO\_INTERVAL\_MAX 0x0C80U

[ 91](group__bt__iso.md#ga77ae350543eb05617c590c0ad9cb0048)#define BT\_ISO\_LATENCY\_MIN 0x0005

[ 93](group__bt__iso.md#gad5e89d05d8706509d8d9d8dac40e3347)#define BT\_ISO\_LATENCY\_MAX 0x0FA0

[ 95](group__bt__iso.md#ga6275e8d805e2366522a78f18ca47ac19)#define BT\_ISO\_PACKING\_SEQUENTIAL 0x00

[ 97](group__bt__iso.md#ga35b037fcce858857642b4c54bae8dd79)#define BT\_ISO\_PACKING\_INTERLEAVED 0x01

[ 99](group__bt__iso.md#ga696a81180ae25aa686a53b73e352c9d2)#define BT\_ISO\_FRAMING\_UNFRAMED 0x00

[ 101](group__bt__iso.md#ga8f9aba389529ad2a3667ca378e99de2b)#define BT\_ISO\_FRAMING\_FRAMED 0x01

[ 103](group__bt__iso.md#gae9dc30b300e2c309d646e3227e8cc00e)#define BT\_ISO\_MAX\_GROUP\_ISO\_COUNT 0x1F

[ 105](group__bt__iso.md#ga4cc5565eeda9a3661d49d485637d1db2)#define BT\_ISO\_MIN\_SDU 0x0001

[ 107](group__bt__iso.md#gaa5d5588e7229db16219b0c44921bbcf7)#define BT\_ISO\_MAX\_SDU 0x0FFF

[ 109](group__bt__iso.md#ga4e29d5966f959114754d62a8763c8c1e)#define BT\_ISO\_CONNECTED\_PDU\_MIN 0x0000U

[ 111](group__bt__iso.md#gaee766ff789f1bf01f75c88112ddd2afa)#define BT\_ISO\_BROADCAST\_PDU\_MIN 0x0001U

[ 113](group__bt__iso.md#ga88fb5690cd1cab4e5e8d5c025cc1af00)#define BT\_ISO\_PDU\_MAX 0x00FBU

[ 115](group__bt__iso.md#ga2905cddfa456fc846f0c8025487b404d)#define BT\_ISO\_BN\_MIN 0x01U

[ 117](group__bt__iso.md#gac05f4f51ea04962679f616bb167b724d)#define BT\_ISO\_BN\_MAX 0x0FU

[ 119](group__bt__iso.md#ga2d3bde6b34f6b15474926ed97ad11d98)#define BT\_ISO\_FT\_MIN 0x01U

[ 121](group__bt__iso.md#ga011c9d5840658fd0ef244f47893ec70e)#define BT\_ISO\_FT\_MAX 0xFFU

[ 123](group__bt__iso.md#ga3eba4c20b4203b0323b14178522e6159)#define BT\_ISO\_NSE\_MIN 0x01U

[ 125](group__bt__iso.md#gab7637d96bde7a41123b34f487eec3436)#define BT\_ISO\_NSE\_MAX 0x1FU

[ 127](group__bt__iso.md#gaa1bd6484a248a6fb5abc31202e5076d4)#define BT\_ISO\_SYNC\_TIMEOUT\_MIN 0x000A

[ 129](group__bt__iso.md#gaeb66806b649bf828afbd83d15c9823eb)#define BT\_ISO\_SYNC\_TIMEOUT\_MAX 0x4000

[ 131](group__bt__iso.md#ga47802144b8523b3d46af9ef97e744bbd)#define BT\_ISO\_SYNC\_MSE\_ANY 0x00

[ 133](group__bt__iso.md#gafef299e43e0f58ac23e1a1e75ccd0163)#define BT\_ISO\_SYNC\_MSE\_MIN 0x01

[ 135](group__bt__iso.md#gafd6e7b48394d6f6c8ddd485927b02b4b)#define BT\_ISO\_SYNC\_MSE\_MAX 0x1F

[ 137](group__bt__iso.md#ga1b52aba83eff5d6ae14169d1d3afa1a7)#define BT\_ISO\_CONNECTED\_RTN\_MAX 0xFF

[ 139](group__bt__iso.md#ga3a579a5d752d4b19dcb668dd7ef27333)#define BT\_ISO\_BROADCAST\_RTN\_MAX 0x1E

[ 141](group__bt__iso.md#ga5551cab9896764eec39b8e6102e561e5)#define BT\_ISO\_BROADCAST\_CODE\_SIZE 16

[ 143](group__bt__iso.md#ga0333b406b29a0a3c355db4f52815ff1a)#define BT\_ISO\_BIS\_INDEX\_MIN 0x01

[ 145](group__bt__iso.md#ga834652af6ceef1824799ab0bfa0e426f)#define BT\_ISO\_BIS\_INDEX\_MAX 0x1F

[ 147](group__bt__iso.md#ga52df7bd114b77872c084e28ca86e0b2e)#define BT\_ISO\_IRC\_MIN 0x01U

[ 149](group__bt__iso.md#ga0f412f1593bcdcfa2b323b285bd508a4)#define BT\_ISO\_IRC\_MAX 0x0FU

[ 151](group__bt__iso.md#ga3f19aaa432290d67fdf4911d1d044dd8)#define BT\_ISO\_PTO\_MIN 0x00U

[ 153](group__bt__iso.md#ga27e812e35a1f12329310851eb9c056f2)#define BT\_ISO\_PTO\_MAX 0x0FU

[ 155](group__bt__iso.md#ga4fb7985aa35292671abe881c1570c445)#define BT\_ISO\_SUBINTERVAL\_NONE 0x00000000U

[ 157](group__bt__iso.md#ga8085b01de2d1facb666215282690d674)#define BT\_ISO\_SUBINTERVAL\_UNKNOWN 0xFFFFFFFFU

158

[ 164](group__bt__iso.md#ga9becee6d629b8f54f55d2264b6d1baef)#define BT\_ISO\_VALID\_BIS\_BITFIELD(\_bis\_bitfield) \

165 ((\_bis\_bitfield) != 0U && (\_bis\_bitfield) <= BIT\_MASK(BT\_ISO\_BIS\_INDEX\_MAX))

166

[ 171](group__bt__iso.md#gaf2925460cc22cc4220dc376bcbee6201)enum [bt\_iso\_state](group__bt__iso.md#gaf2925460cc22cc4220dc376bcbee6201) {

[ 173](group__bt__iso.md#ggaf2925460cc22cc4220dc376bcbee6201af392f8825090c7beb304efc860a1911d) [BT\_ISO\_STATE\_DISCONNECTED](group__bt__iso.md#ggaf2925460cc22cc4220dc376bcbee6201af392f8825090c7beb304efc860a1911d),

[ 175](group__bt__iso.md#ggaf2925460cc22cc4220dc376bcbee6201a3ff6aa78bb7ed364b46c1457555aaba5) [BT\_ISO\_STATE\_ENCRYPT\_PENDING](group__bt__iso.md#ggaf2925460cc22cc4220dc376bcbee6201a3ff6aa78bb7ed364b46c1457555aaba5),

[ 177](group__bt__iso.md#ggaf2925460cc22cc4220dc376bcbee6201a4cb48a0a2a2ac37bbab5eded1bc3fd22) [BT\_ISO\_STATE\_CONNECTING](group__bt__iso.md#ggaf2925460cc22cc4220dc376bcbee6201a4cb48a0a2a2ac37bbab5eded1bc3fd22),

[ 179](group__bt__iso.md#ggaf2925460cc22cc4220dc376bcbee6201acfa2a00a1c203418768ce789cd0cec7d) [BT\_ISO\_STATE\_CONNECTED](group__bt__iso.md#ggaf2925460cc22cc4220dc376bcbee6201acfa2a00a1c203418768ce789cd0cec7d),

[ 181](group__bt__iso.md#ggaf2925460cc22cc4220dc376bcbee6201aebc34f9c32f1cd5e3197c7edaf657340) [BT\_ISO\_STATE\_DISCONNECTING](group__bt__iso.md#ggaf2925460cc22cc4220dc376bcbee6201aebc34f9c32f1cd5e3197c7edaf657340),

182};

183

184

[ 188](group__bt__iso.md#gafcbd720c67c6a6e5f1cae1395e1e06f0)enum [bt\_iso\_chan\_type](group__bt__iso.md#gafcbd720c67c6a6e5f1cae1395e1e06f0) {

[ 189](group__bt__iso.md#ggafcbd720c67c6a6e5f1cae1395e1e06f0a58579ee03e3769501536826248758f17) [BT\_ISO\_CHAN\_TYPE\_NONE](group__bt__iso.md#ggafcbd720c67c6a6e5f1cae1395e1e06f0a58579ee03e3769501536826248758f17),

[ 190](group__bt__iso.md#ggafcbd720c67c6a6e5f1cae1395e1e06f0a46a0148a474b297d38d67fb18bdb410a) [BT\_ISO\_CHAN\_TYPE\_CENTRAL](group__bt__iso.md#ggafcbd720c67c6a6e5f1cae1395e1e06f0a46a0148a474b297d38d67fb18bdb410a),

[ 191](group__bt__iso.md#ggafcbd720c67c6a6e5f1cae1395e1e06f0aa8b51a9ebacbaaac90956d7a9a816edb) [BT\_ISO\_CHAN\_TYPE\_PERIPHERAL](group__bt__iso.md#ggafcbd720c67c6a6e5f1cae1395e1e06f0aa8b51a9ebacbaaac90956d7a9a816edb),

[ 192](group__bt__iso.md#ggafcbd720c67c6a6e5f1cae1395e1e06f0a63fb0b72a274afd24ff6b0d04d28910b) [BT\_ISO\_CHAN\_TYPE\_BROADCASTER](group__bt__iso.md#ggafcbd720c67c6a6e5f1cae1395e1e06f0a63fb0b72a274afd24ff6b0d04d28910b),

[ 193](group__bt__iso.md#ggafcbd720c67c6a6e5f1cae1395e1e06f0a725ae4b23a26a8569f5abb6a1e8134c2) [BT\_ISO\_CHAN\_TYPE\_SYNC\_RECEIVER](group__bt__iso.md#ggafcbd720c67c6a6e5f1cae1395e1e06f0a725ae4b23a26a8569f5abb6a1e8134c2)

194};

195

[ 197](structbt__iso__chan.md)struct [bt\_iso\_chan](structbt__iso__chan.md) {

[ 199](structbt__iso__chan.md#a7fd728385a3aec11be8883bdee8aedea) struct bt\_conn \*[iso](structbt__iso__chan.md#a7fd728385a3aec11be8883bdee8aedea);

[ 201](structbt__iso__chan.md#a214fe133602ac8dcfaaec7f372e12da8) struct [bt\_iso\_chan\_ops](structbt__iso__chan__ops.md) \*[ops](structbt__iso__chan.md#a214fe133602ac8dcfaaec7f372e12da8);

[ 203](structbt__iso__chan.md#abe94fca71506bd590d9ef4465258914d) struct [bt\_iso\_chan\_qos](structbt__iso__chan__qos.md) \*[qos](structbt__iso__chan.md#abe94fca71506bd590d9ef4465258914d);

[ 205](structbt__iso__chan.md#a2b0fc7180d1983ee4a415c5331bed93d) enum [bt\_iso\_state](group__bt__iso.md#gaf2925460cc22cc4220dc376bcbee6201) [state](structbt__iso__chan.md#a2b0fc7180d1983ee4a415c5331bed93d);

206#if (defined(CONFIG\_BT\_SMP) && defined(CONFIG\_BT\_ISO\_UNICAST)) || defined(\_\_DOXYGEN\_\_)

[ 217](structbt__iso__chan.md#a75347e4f16e715be06298ccf36c8521c) [bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783) [required\_sec\_level](structbt__iso__chan.md#a75347e4f16e715be06298ccf36c8521c);

218#endif /\* CONFIG\_BT\_SMP && CONFIG\_BT\_ISO\_UNICAST \*/

[ 220](structbt__iso__chan.md#aba7bf6dcad93b121c46daa6ad473a51c) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structbt__iso__chan.md#aba7bf6dcad93b121c46daa6ad473a51c);

221};

222

[ 224](structbt__iso__chan__io__qos.md)struct [bt\_iso\_chan\_io\_qos](structbt__iso__chan__io__qos.md) {

[ 230](structbt__iso__chan__io__qos.md#ae52611dc326b6777620ff7aa43f566e9) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sdu](structbt__iso__chan__io__qos.md#ae52611dc326b6777620ff7aa43f566e9);

[ 236](structbt__iso__chan__io__qos.md#a2180a4f82e4cdf5288b7f67701a16ad6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__iso__chan__io__qos.md#a2180a4f82e4cdf5288b7f67701a16ad6);

[ 242](structbt__iso__chan__io__qos.md#a5106bfd09f6be52604e7c7f0e3390684) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rtn](structbt__iso__chan__io__qos.md#a5106bfd09f6be52604e7c7f0e3390684);

243

244#if defined(CONFIG\_BT\_ISO\_TEST\_PARAMS) || defined(\_\_DOXYGEN\_\_)

[ 254](structbt__iso__chan__io__qos.md#ae9e7678a63030353eea65152d89464cd) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_pdu](structbt__iso__chan__io__qos.md#ae9e7678a63030353eea65152d89464cd);

255

[ 261](structbt__iso__chan__io__qos.md#ac64a3ce7282ac8bc5b5420a46417b22c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [burst\_number](structbt__iso__chan__io__qos.md#ac64a3ce7282ac8bc5b5420a46417b22c);

262#endif /\* CONFIG\_BT\_ISO\_TEST\_PARAMS \*/

263};

264

[ 266](structbt__iso__chan__qos.md)struct [bt\_iso\_chan\_qos](structbt__iso__chan__qos.md) {

[ 274](structbt__iso__chan__qos.md#ac231434d1798f431c4fbac5a759784a5) struct [bt\_iso\_chan\_io\_qos](structbt__iso__chan__io__qos.md) \*[rx](structbt__iso__chan__qos.md#ac231434d1798f431c4fbac5a759784a5);

[ 283](structbt__iso__chan__qos.md#a47a99a6ccfa5f1e0c9fb859e66d2e9e3) struct [bt\_iso\_chan\_io\_qos](structbt__iso__chan__io__qos.md) \*[tx](structbt__iso__chan__qos.md#a47a99a6ccfa5f1e0c9fb859e66d2e9e3);

284

285#if defined(CONFIG\_BT\_ISO\_TEST\_PARAMS) || defined(\_\_DOXYGEN\_\_)

[ 293](structbt__iso__chan__qos.md#a4c6bfa577f8cbd724ed2561850fd6255) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_subevents](structbt__iso__chan__qos.md#a4c6bfa577f8cbd724ed2561850fd6255);

294#endif /\* CONFIG\_BT\_ISO\_TEST\_PARAMS \*/

295};

296

[ 298](structbt__iso__chan__path.md)struct [bt\_iso\_chan\_path](structbt__iso__chan__path.md) {

[ 305](structbt__iso__chan__path.md#a5e4fb798376489a38a87e4052ff85550) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pid](structbt__iso__chan__path.md#a5e4fb798376489a38a87e4052ff85550);

[ 311](structbt__iso__chan__path.md#a519c884281207d1165a61ccfb7fbcdf4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [format](structbt__iso__chan__path.md#a519c884281207d1165a61ccfb7fbcdf4);

[ 313](structbt__iso__chan__path.md#a95db7917f7b9e90a33f494233c3266eb) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [cid](structbt__iso__chan__path.md#a95db7917f7b9e90a33f494233c3266eb);

[ 315](structbt__iso__chan__path.md#aebc12293ba0b10a87f1852e2a3e53a23) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [vid](structbt__iso__chan__path.md#aebc12293ba0b10a87f1852e2a3e53a23);

[ 321](structbt__iso__chan__path.md#adaed07de7e09263e3e941817eeb44258) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [delay](structbt__iso__chan__path.md#adaed07de7e09263e3e941817eeb44258);

[ 323](structbt__iso__chan__path.md#a0da75c4911a197fed7fd7f17c76dddae) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cc\_len](structbt__iso__chan__path.md#a0da75c4911a197fed7fd7f17c76dddae);

[ 329](structbt__iso__chan__path.md#acba5454d02460e8c2d51851677e310bb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[cc](structbt__iso__chan__path.md#acba5454d02460e8c2d51851677e310bb);

330};

331

333enum {

[ 335](group__bt__iso.md#gga2c62af103a71aa8f5f8aa103b1245866a143de2c153179b3c40aca51c016e6382) [BT\_ISO\_FLAGS\_VALID](group__bt__iso.md#gga2c62af103a71aa8f5f8aa103b1245866a143de2c153179b3c40aca51c016e6382) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

336

[ 342](group__bt__iso.md#gga2c62af103a71aa8f5f8aa103b1245866a5f0aa6e3150819821f800dd7376e2218) [BT\_ISO\_FLAGS\_ERROR](group__bt__iso.md#gga2c62af103a71aa8f5f8aa103b1245866a5f0aa6e3150819821f800dd7376e2218) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

343

[ 345](group__bt__iso.md#gga2c62af103a71aa8f5f8aa103b1245866a5e87d48b6e96275744590194b75396ff) [BT\_ISO\_FLAGS\_LOST](group__bt__iso.md#gga2c62af103a71aa8f5f8aa103b1245866a5e87d48b6e96275744590194b75396ff) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

346

[ 353](group__bt__iso.md#gga2c62af103a71aa8f5f8aa103b1245866a96f645c1c14593370fd6e0443b019a23) [BT\_ISO\_FLAGS\_TS](group__bt__iso.md#gga2c62af103a71aa8f5f8aa103b1245866a96f645c1c14593370fd6e0443b019a23) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3)

354};

355

[ 357](structbt__iso__recv__info.md)struct [bt\_iso\_recv\_info](structbt__iso__recv__info.md) {

[ 363](structbt__iso__recv__info.md#a4bf778ae9be39eb4a740c2eb9670d98a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ts](structbt__iso__recv__info.md#a4bf778ae9be39eb4a740c2eb9670d98a);

364

[ 366](structbt__iso__recv__info.md#a7c5b950df0359bb561140d0c2726fae6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [seq\_num](structbt__iso__recv__info.md#a7c5b950df0359bb561140d0c2726fae6);

367

[ 369](structbt__iso__recv__info.md#a0a7842fcb3251ed89b99fde43ba235a5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](structbt__iso__recv__info.md#a0a7842fcb3251ed89b99fde43ba235a5);

370};

371

[ 373](structbt__iso__tx__info.md)struct [bt\_iso\_tx\_info](structbt__iso__tx__info.md) {

[ 375](structbt__iso__tx__info.md#ac8a6a4c073e4df1553d32339a6e4b051) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ts](structbt__iso__tx__info.md#ac8a6a4c073e4df1553d32339a6e4b051);

376

[ 378](structbt__iso__tx__info.md#a0cff6aa2893fdc11160e4327afebed13) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [offset](structbt__iso__tx__info.md#a0cff6aa2893fdc11160e4327afebed13);

379

[ 381](structbt__iso__tx__info.md#a2791edea2f4f4459acc24c8dbaa33ded) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [seq\_num](structbt__iso__tx__info.md#a2791edea2f4f4459acc24c8dbaa33ded);

382};

383

384

386struct bt\_iso\_cig;

387

[ 389](structbt__iso__cig__param.md)struct [bt\_iso\_cig\_param](structbt__iso__cig__param.md) {

[ 391](structbt__iso__cig__param.md#a841dee850f3161bd8e904376792c8ad7) struct [bt\_iso\_chan](structbt__iso__chan.md) \*\*[cis\_channels](structbt__iso__cig__param.md#a841dee850f3161bd8e904376792c8ad7);

392

[ 398](structbt__iso__cig__param.md#a69c12b704b9897d88b71bc96bd2d3024) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_cis](structbt__iso__cig__param.md#a69c12b704b9897d88b71bc96bd2d3024);

399

[ 405](structbt__iso__cig__param.md#ad7349213bab902a68c726da51fac2306) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [c\_to\_p\_interval](structbt__iso__cig__param.md#ad7349213bab902a68c726da51fac2306);

406

[ 412](structbt__iso__cig__param.md#a36d2eaa4fd3e08988d4c49ca0902a882) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [p\_to\_c\_interval](structbt__iso__cig__param.md#a36d2eaa4fd3e08988d4c49ca0902a882);

413

[ 421](structbt__iso__cig__param.md#aeffe10e87d81285196e931dcad2882ba) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [c\_to\_p\_latency](structbt__iso__cig__param.md#aeffe10e87d81285196e931dcad2882ba);

422

[ 430](structbt__iso__cig__param.md#ad1725e09a397e83d1cc88ebd3a60ed93) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [p\_to\_c\_latency](structbt__iso__cig__param.md#ad1725e09a397e83d1cc88ebd3a60ed93);

431

[ 439](structbt__iso__cig__param.md#a83fdc5374f341a421e1394b08297cdff) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sca](structbt__iso__cig__param.md#a83fdc5374f341a421e1394b08297cdff);

440

[ 446](structbt__iso__cig__param.md#a3908eadf3080731cb891e803162d321c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packing](structbt__iso__cig__param.md#a3908eadf3080731cb891e803162d321c);

447

[ 453](structbt__iso__cig__param.md#a4a09f9f6e7a8db17c3037c9f1761b18a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [framing](structbt__iso__cig__param.md#a4a09f9f6e7a8db17c3037c9f1761b18a);

454

455#if defined(CONFIG\_BT\_ISO\_TEST\_PARAMS) || defined(\_\_DOXYGEN\_\_)

[ 464](structbt__iso__cig__param.md#aadc3762f3fec3127014378fe58c5b684) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [c\_to\_p\_ft](structbt__iso__cig__param.md#aadc3762f3fec3127014378fe58c5b684);

465

[ 474](structbt__iso__cig__param.md#ab222cdb0af475180dd715b4f5658dc65) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [p\_to\_c\_ft](structbt__iso__cig__param.md#ab222cdb0af475180dd715b4f5658dc65);

475

[ 483](structbt__iso__cig__param.md#a85641a8f01d63b4221c013815c055526) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [iso\_interval](structbt__iso__cig__param.md#a85641a8f01d63b4221c013815c055526);

484#endif /\* CONFIG\_BT\_ISO\_TEST\_PARAMS \*/

485};

486

[ 488](structbt__iso__connect__param.md)struct [bt\_iso\_connect\_param](structbt__iso__connect__param.md) {

[ 490](structbt__iso__connect__param.md#ad004956584d2d065d8c0c52959f350d5) struct [bt\_iso\_chan](structbt__iso__chan.md) \*[iso\_chan](structbt__iso__connect__param.md#ad004956584d2d065d8c0c52959f350d5);

491

[ 493](structbt__iso__connect__param.md#aba2f3838e03a1e31699a4623ba93d372) struct bt\_conn \*[acl](structbt__iso__connect__param.md#aba2f3838e03a1e31699a4623ba93d372);

494};

495

497struct bt\_iso\_big;

498

[ 500](structbt__iso__big__create__param.md)struct [bt\_iso\_big\_create\_param](structbt__iso__big__create__param.md) {

[ 502](structbt__iso__big__create__param.md#a7548bbb75f240a70435cb86a48846d0a) struct [bt\_iso\_chan](structbt__iso__chan.md) \*\*[bis\_channels](structbt__iso__big__create__param.md#a7548bbb75f240a70435cb86a48846d0a);

503

[ 509](structbt__iso__big__create__param.md#a8ae9c225798e9f5b72fe0b8c3b6f2cf0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_bis](structbt__iso__big__create__param.md#a8ae9c225798e9f5b72fe0b8c3b6f2cf0);

510

[ 516](structbt__iso__big__create__param.md#a7aaef1f7a78ae1088886a78739fd6849) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [interval](structbt__iso__big__create__param.md#a7aaef1f7a78ae1088886a78739fd6849);

517

[ 525](structbt__iso__big__create__param.md#ab847021da2e604036cecf90483e12132) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [latency](structbt__iso__big__create__param.md#ab847021da2e604036cecf90483e12132);

526

[ 532](structbt__iso__big__create__param.md#ad478d7b36fb34b8e57a25ae0029e4c51) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [packing](structbt__iso__big__create__param.md#ad478d7b36fb34b8e57a25ae0029e4c51);

533

[ 539](structbt__iso__big__create__param.md#aab0e9f66cb10643e72d6382718ed4c0d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [framing](structbt__iso__big__create__param.md#aab0e9f66cb10643e72d6382718ed4c0d);

540

[ 542](structbt__iso__big__create__param.md#a1288fa2a8f6bb3e2ab26729e245277e1) bool [encryption](structbt__iso__big__create__param.md#a1288fa2a8f6bb3e2ab26729e245277e1);

543

[ 556](structbt__iso__big__create__param.md#aaee9af5a21b2f9812f9635c526f3a923) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bcode](structbt__iso__big__create__param.md#aaee9af5a21b2f9812f9635c526f3a923)[[BT\_ISO\_BROADCAST\_CODE\_SIZE](group__bt__iso.md#ga5551cab9896764eec39b8e6102e561e5)];

557

558#if defined(CONFIG\_BT\_ISO\_TEST\_PARAMS) || defined(\_\_DOXYGEN\_\_)

[ 566](structbt__iso__big__create__param.md#ad931ff1f19f92c29c40d934346498e79) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [irc](structbt__iso__big__create__param.md#ad931ff1f19f92c29c40d934346498e79);

567

[ 575](structbt__iso__big__create__param.md#affce506bd271d9b0e497160c163c5798) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pto](structbt__iso__big__create__param.md#affce506bd271d9b0e497160c163c5798);

576

[ 584](structbt__iso__big__create__param.md#a63cd16824e9d09e29d3c7e135b08d932) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [iso\_interval](structbt__iso__big__create__param.md#a63cd16824e9d09e29d3c7e135b08d932);

585#endif /\* CONFIG\_BT\_ISO\_TEST\_PARAMS \*/

586};

587

[ 589](structbt__iso__big__sync__param.md)struct [bt\_iso\_big\_sync\_param](structbt__iso__big__sync__param.md) {

[ 591](structbt__iso__big__sync__param.md#ac56d7206c3434837a52059716355adad) struct [bt\_iso\_chan](structbt__iso__chan.md) \*\*[bis\_channels](structbt__iso__big__sync__param.md#ac56d7206c3434837a52059716355adad);

592

[ 598](structbt__iso__big__sync__param.md#a96cd109e9f5820531635d48e88b4bff8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_bis](structbt__iso__big__sync__param.md#a96cd109e9f5820531635d48e88b4bff8);

599

[ 608](structbt__iso__big__sync__param.md#a14b03509daf760edbead86659f733136) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [bis\_bitfield](structbt__iso__big__sync__param.md#a14b03509daf760edbead86659f733136);

609

[ 620](structbt__iso__big__sync__param.md#a16b332b4a0f373cb21e5da6e6e383b9e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [mse](structbt__iso__big__sync__param.md#a16b332b4a0f373cb21e5da6e6e383b9e);

621

[ 627](structbt__iso__big__sync__param.md#a8e344870fc0e380e6588eb90c7ef72f9) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sync\_timeout](structbt__iso__big__sync__param.md#a8e344870fc0e380e6588eb90c7ef72f9);

628

[ 630](structbt__iso__big__sync__param.md#a8e5cffe8960477e7f64707d7dd4191f6) bool [encryption](structbt__iso__big__sync__param.md#a8e5cffe8960477e7f64707d7dd4191f6);

631

[ 644](structbt__iso__big__sync__param.md#aaecdeabed10b90e84b618dac1129a9dc) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bcode](structbt__iso__big__sync__param.md#aaecdeabed10b90e84b618dac1129a9dc)[[BT\_ISO\_BROADCAST\_CODE\_SIZE](group__bt__iso.md#ga5551cab9896764eec39b8e6102e561e5)];

645};

646

[ 648](structbt__iso__biginfo.md)struct [bt\_iso\_biginfo](structbt__iso__biginfo.md) {

[ 650](structbt__iso__biginfo.md#aa7dbfd342eecf8ffc2fce9d3fa7209ea) const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*[addr](structbt__iso__biginfo.md#aa7dbfd342eecf8ffc2fce9d3fa7209ea);

651

[ 653](structbt__iso__biginfo.md#a78e0a53f920980081d7b0702b02cf386) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sid](structbt__iso__biginfo.md#a78e0a53f920980081d7b0702b02cf386);

654

[ 656](structbt__iso__biginfo.md#a10eb24596a4353da3feb0d30fed35ae7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_bis](structbt__iso__biginfo.md#a10eb24596a4353da3feb0d30fed35ae7);

657

[ 659](structbt__iso__biginfo.md#a24eb83f7b54e9f949cc07e9955b4a8b8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [sub\_evt\_count](structbt__iso__biginfo.md#a24eb83f7b54e9f949cc07e9955b4a8b8);

660

[ 662](structbt__iso__biginfo.md#afe96caf570314731f6c543b40d7def9a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [iso\_interval](structbt__iso__biginfo.md#afe96caf570314731f6c543b40d7def9a);

663

[ 665](structbt__iso__biginfo.md#ad114dd97500d12242da77e8522133953) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [burst\_number](structbt__iso__biginfo.md#ad114dd97500d12242da77e8522133953);

666

[ 668](structbt__iso__biginfo.md#a4efb91dc2f249e41c65cd0dcbfe45bad) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [offset](structbt__iso__biginfo.md#a4efb91dc2f249e41c65cd0dcbfe45bad);

669

[ 671](structbt__iso__biginfo.md#a8458f6d6ebe936212d928caca61b13bd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rep\_count](structbt__iso__biginfo.md#a8458f6d6ebe936212d928caca61b13bd);

672

[ 674](structbt__iso__biginfo.md#af356aa29aa82c8deb63a9f47e54070a1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_pdu](structbt__iso__biginfo.md#af356aa29aa82c8deb63a9f47e54070a1);

675

[ 677](structbt__iso__biginfo.md#a4a6d6cdea56a69a0b3b3fd021489750d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sdu\_interval](structbt__iso__biginfo.md#a4a6d6cdea56a69a0b3b3fd021489750d);

678

[ 680](structbt__iso__biginfo.md#a9fddcb74f3de7eb857583a0179427f84) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_sdu](structbt__iso__biginfo.md#a9fddcb74f3de7eb857583a0179427f84);

681

[ 683](structbt__iso__biginfo.md#a2cbaf6a89e8aaf62c7048e04523e57d4) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__iso__biginfo.md#a2cbaf6a89e8aaf62c7048e04523e57d4);

684

[ 686](structbt__iso__biginfo.md#a1084c209d122d2d13244b77659ce28dd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [framing](structbt__iso__biginfo.md#a1084c209d122d2d13244b77659ce28dd);

687

[ 689](structbt__iso__biginfo.md#a7d54ecb896c0d6bc590311d5d5a3ac7b) bool [encryption](structbt__iso__biginfo.md#a7d54ecb896c0d6bc590311d5d5a3ac7b);

690};

691

[ 693](structbt__iso__chan__ops.md)struct [bt\_iso\_chan\_ops](structbt__iso__chan__ops.md) {

[ 705](structbt__iso__chan__ops.md#a6b0e51770158da7b728e1084a8e44504) void (\*[connected](structbt__iso__chan__ops.md#a6b0e51770158da7b728e1084a8e44504))(struct [bt\_iso\_chan](structbt__iso__chan.md) \*chan);

706

[ 725](structbt__iso__chan__ops.md#a7bf9fe04f42bacd59f623aa28a3b0665) void (\*[disconnected](structbt__iso__chan__ops.md#a2069849352019362e5dc7d68f835f359))(struct [bt\_iso\_chan](structbt__iso__chan.md) \*chan, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason);

726

737 struct [net\_buf](structnet__buf.md) \*(\*alloc\_buf)(struct [bt\_iso\_chan](structbt__iso__chan.md) \*chan);

738

[ 749](structbt__iso__chan__ops.md#a6d5d9423fff83f8f337f97b3fc018f39) void (\*[recv](structbt__iso__chan__ops.md#a6d5d9423fff83f8f337f97b3fc018f39))(struct [bt\_iso\_chan](structbt__iso__chan.md) \*chan, const struct [bt\_iso\_recv\_info](structbt__iso__recv__info.md) \*info,

750 struct [net\_buf](structnet__buf.md) \*buf);

751

[ 762](structbt__iso__chan__ops.md#a048954070628229b8aacd373de1fb236) void (\*[sent](structbt__iso__chan__ops.md#a048954070628229b8aacd373de1fb236))(struct [bt\_iso\_chan](structbt__iso__chan.md) \*chan);

763};

764

[ 766](structbt__iso__accept__info.md)struct [bt\_iso\_accept\_info](structbt__iso__accept__info.md) {

[ 768](structbt__iso__accept__info.md#a4225ccc90f1e17e26ce61fe398f506d1) struct bt\_conn \*[acl](structbt__iso__accept__info.md#a4225ccc90f1e17e26ce61fe398f506d1);

769

[ 775](structbt__iso__accept__info.md#a88002043a67c89c8d518ebdf92cf8847) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cig\_id](structbt__iso__accept__info.md#a88002043a67c89c8d518ebdf92cf8847);

776

[ 782](structbt__iso__accept__info.md#a688809132997c37a6fe2529498a4ee0e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cis\_id](structbt__iso__accept__info.md#a688809132997c37a6fe2529498a4ee0e);

783};

784

[ 786](structbt__iso__server.md)struct [bt\_iso\_server](structbt__iso__server.md) {

787#if defined(CONFIG\_BT\_SMP) || defined(\_\_DOXYGEN\_\_)

[ 793](structbt__iso__server.md#a43b53fd63d4deaa1c5599499eec29c99) [bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783) [sec\_level](structbt__iso__server.md#a43b53fd63d4deaa1c5599499eec29c99);

794#endif /\* CONFIG\_BT\_SMP \*/

795

[ 806](structbt__iso__server.md#ae67a000ae524cba53b6bda503568ba38) int (\*[accept](structbt__iso__server.md#ae67a000ae524cba53b6bda503568ba38))(const struct [bt\_iso\_accept\_info](structbt__iso__accept__info.md) \*info, struct [bt\_iso\_chan](structbt__iso__chan.md) \*\*chan);

807};

808

[ 820](group__bt__iso.md#gaff0e52777b2140519c63b54b9618bca8)int [bt\_iso\_server\_register](group__bt__iso.md#gaff0e52777b2140519c63b54b9618bca8)(struct [bt\_iso\_server](structbt__iso__server.md) \*server);

821

[ 831](group__bt__iso.md#ga0ed72a4f7a418ae5aa3bb4f48fd5c9e6)int [bt\_iso\_server\_unregister](group__bt__iso.md#ga0ed72a4f7a418ae5aa3bb4f48fd5c9e6)(struct [bt\_iso\_server](structbt__iso__server.md) \*server);

832

[ 847](group__bt__iso.md#gaea03fc251206f18de320506064c1631f)int [bt\_iso\_cig\_create](group__bt__iso.md#gaea03fc251206f18de320506064c1631f)(const struct [bt\_iso\_cig\_param](structbt__iso__cig__param.md) \*param, struct bt\_iso\_cig \*\*out\_cig);

848

[ 869](group__bt__iso.md#ga98f557c183a82066b81f0265c225bebe)int [bt\_iso\_cig\_reconfigure](group__bt__iso.md#ga98f557c183a82066b81f0265c225bebe)(struct bt\_iso\_cig \*cig, const struct [bt\_iso\_cig\_param](structbt__iso__cig__param.md) \*param);

870

[ 880](group__bt__iso.md#gad4b6a7286593ff099117113b6ca996f8)int [bt\_iso\_cig\_terminate](group__bt__iso.md#gad4b6a7286593ff099117113b6ca996f8)(struct bt\_iso\_cig \*cig);

881

[ 919](group__bt__iso.md#ga98953a261f3699b62cd19ab4977e0b4c)int [bt\_iso\_chan\_connect](group__bt__iso.md#ga98953a261f3699b62cd19ab4977e0b4c)(const struct [bt\_iso\_connect\_param](structbt__iso__connect__param.md) \*param, size\_t count);

920

[ 940](group__bt__iso.md#ga94c5c788b099284219e5a303b4b8ea69)int [bt\_iso\_chan\_disconnect](group__bt__iso.md#ga94c5c788b099284219e5a303b4b8ea69)(struct [bt\_iso\_chan](structbt__iso__chan.md) \*chan);

941

[ 961](group__bt__iso.md#ga0dbb89a133011a833be7d18161471c6a)int [bt\_iso\_chan\_send](group__bt__iso.md#ga0dbb89a133011a833be7d18161471c6a)(struct [bt\_iso\_chan](structbt__iso__chan.md) \*chan, struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seq\_num);

962

[ 985](group__bt__iso.md#gab75b817770e3b685920587afde39d6cd)int [bt\_iso\_chan\_send\_ts](group__bt__iso.md#gab75b817770e3b685920587afde39d6cd)(struct [bt\_iso\_chan](structbt__iso__chan.md) \*chan, struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seq\_num,

986 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ts);

987

[ 1009](group__bt__iso.md#gaa74c762451cfb5d04ffcd8d396a75447)int [bt\_iso\_setup\_data\_path](group__bt__iso.md#gaa74c762451cfb5d04ffcd8d396a75447)(const struct [bt\_iso\_chan](structbt__iso__chan.md) \*chan, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dir,

1010 const struct [bt\_iso\_chan\_path](structbt__iso__chan__path.md) \*path);

1011

[ 1050](group__bt__iso.md#ga53be464e005392676830feeddd8cdc22)int [bt\_iso\_remove\_data\_path](group__bt__iso.md#ga53be464e005392676830feeddd8cdc22)(const struct [bt\_iso\_chan](structbt__iso__chan.md) \*chan, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dir);

1051

[ 1053](structbt__iso__unicast__tx__info.md)struct [bt\_iso\_unicast\_tx\_info](structbt__iso__unicast__tx__info.md) {

[ 1055](structbt__iso__unicast__tx__info.md#a14548ee24fad8a26287aa0daba451a47) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [latency](structbt__iso__unicast__tx__info.md#a14548ee24fad8a26287aa0daba451a47);

1056

[ 1058](structbt__iso__unicast__tx__info.md#aaf1f623eac2f84ca06082776179b71c5) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flush\_timeout](structbt__iso__unicast__tx__info.md#aaf1f623eac2f84ca06082776179b71c5);

1059

[ 1061](structbt__iso__unicast__tx__info.md#afe7dce9255613e5e2939d3719c720822) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_pdu](structbt__iso__unicast__tx__info.md#afe7dce9255613e5e2939d3719c720822);

1062

[ 1064](structbt__iso__unicast__tx__info.md#a3134e0bdb663ad7184e23531504233a5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__iso__unicast__tx__info.md#a3134e0bdb663ad7184e23531504233a5);

1065

[ 1067](structbt__iso__unicast__tx__info.md#ab4ea9d5bb535d29ae9406e948d8707a9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bn](structbt__iso__unicast__tx__info.md#ab4ea9d5bb535d29ae9406e948d8707a9);

1068

[ 1073](structbt__iso__unicast__tx__info.md#a7bed74a67bb73f6919d2817d82bcf996) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_sdu](structbt__iso__unicast__tx__info.md#a7bed74a67bb73f6919d2817d82bcf996);

1074

[ 1079](structbt__iso__unicast__tx__info.md#adc91f9c200199400a84322a58d28a933) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sdu\_interval](structbt__iso__unicast__tx__info.md#adc91f9c200199400a84322a58d28a933);

1080};

1081

[ 1083](structbt__iso__unicast__info.md)struct [bt\_iso\_unicast\_info](structbt__iso__unicast__info.md) {

[ 1085](structbt__iso__unicast__info.md#a029c450e2324bbc6ee8fda6d1d10deef) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cig\_sync\_delay](structbt__iso__unicast__info.md#a029c450e2324bbc6ee8fda6d1d10deef);

1086

[ 1088](structbt__iso__unicast__info.md#acbc8c068907eba204d369cf76f4f112d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cis\_sync\_delay](structbt__iso__unicast__info.md#acbc8c068907eba204d369cf76f4f112d);

1089

[ 1096](structbt__iso__unicast__info.md#a4d53dc6adc8d5519cf74982aa5031e74) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [subinterval](structbt__iso__unicast__info.md#a4d53dc6adc8d5519cf74982aa5031e74);

1097

[ 1099](structbt__iso__unicast__info.md#a4fc402b934ae8aa65493df01c88cae34) struct [bt\_iso\_unicast\_tx\_info](structbt__iso__unicast__tx__info.md) [central](structbt__iso__unicast__info.md#a4fc402b934ae8aa65493df01c88cae34);

1100

[ 1102](structbt__iso__unicast__info.md#a03b084fefcab049efbe1a609a59d9c54) struct [bt\_iso\_unicast\_tx\_info](structbt__iso__unicast__tx__info.md) [peripheral](structbt__iso__unicast__info.md#a03b084fefcab049efbe1a609a59d9c54);

1103};

1104

[ 1106](structbt__iso__broadcaster__info.md)struct [bt\_iso\_broadcaster\_info](structbt__iso__broadcaster__info.md) {

[ 1108](structbt__iso__broadcaster__info.md#a577370ab24ebd4d80db4d8ffdb918483) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sync\_delay](structbt__iso__broadcaster__info.md#a577370ab24ebd4d80db4d8ffdb918483);

1109

[ 1111](structbt__iso__broadcaster__info.md#a71388f9b64510ab91c3147f05f775aeb) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [latency](structbt__iso__broadcaster__info.md#a71388f9b64510ab91c3147f05f775aeb);

1112

[ 1114](structbt__iso__broadcaster__info.md#a9f93161fb7f81d5eb3a55f955be1b85d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pto](structbt__iso__broadcaster__info.md#a9f93161fb7f81d5eb3a55f955be1b85d);

1115

[ 1117](structbt__iso__broadcaster__info.md#aa57b6e08cf4d3d154762c8c43de0f2cf) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_pdu](structbt__iso__broadcaster__info.md#aa57b6e08cf4d3d154762c8c43de0f2cf);

1118

[ 1120](structbt__iso__broadcaster__info.md#a3d4e44a1da54e5ca0f2002ca3f6e7a13) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__iso__broadcaster__info.md#a3d4e44a1da54e5ca0f2002ca3f6e7a13);

1121

[ 1123](structbt__iso__broadcaster__info.md#ab3cb80e6b362e093e6924ab11b8737e9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bn](structbt__iso__broadcaster__info.md#ab3cb80e6b362e093e6924ab11b8737e9);

1124

[ 1126](structbt__iso__broadcaster__info.md#ac1feade59bbad1e08418e1808619f775) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [irc](structbt__iso__broadcaster__info.md#ac1feade59bbad1e08418e1808619f775);

1127};

1128

[ 1130](structbt__iso__sync__receiver__info.md)struct [bt\_iso\_sync\_receiver\_info](structbt__iso__sync__receiver__info.md) {

[ 1132](structbt__iso__sync__receiver__info.md#a24bad4231eb214a2c95b1da9ba59c284) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [latency](structbt__iso__sync__receiver__info.md#a24bad4231eb214a2c95b1da9ba59c284);

1133

[ 1135](structbt__iso__sync__receiver__info.md#a80ac6e529491156109955219569fdec6) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pto](structbt__iso__sync__receiver__info.md#a80ac6e529491156109955219569fdec6);

1136

[ 1138](structbt__iso__sync__receiver__info.md#a40ff5a4d691a75802f211a63b1e12303) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_pdu](structbt__iso__sync__receiver__info.md#a40ff5a4d691a75802f211a63b1e12303);

1139

[ 1141](structbt__iso__sync__receiver__info.md#a8be50f8c6d76515ac290407959eaf0e1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bn](structbt__iso__sync__receiver__info.md#a8be50f8c6d76515ac290407959eaf0e1);

1142

[ 1144](structbt__iso__sync__receiver__info.md#a6185a7ac123be930650da6dc84c0c1e0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [irc](structbt__iso__sync__receiver__info.md#a6185a7ac123be930650da6dc84c0c1e0);

1145};

1146

[ 1148](structbt__iso__info.md)struct [bt\_iso\_info](structbt__iso__info.md) {

[ 1150](structbt__iso__info.md#af01766b8eed556ca165222d19ff05838) enum [bt\_iso\_chan\_type](group__bt__iso.md#gafcbd720c67c6a6e5f1cae1395e1e06f0) [type](structbt__iso__info.md#af01766b8eed556ca165222d19ff05838);

1151

[ 1153](structbt__iso__info.md#a53c6c8eee63cd674d54dc1d40aa33a43) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [iso\_interval](structbt__iso__info.md#a53c6c8eee63cd674d54dc1d40aa33a43);

1154

[ 1156](structbt__iso__info.md#a02554d9114dc3e34305a8e986d906cbe) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_subevent](structbt__iso__info.md#a02554d9114dc3e34305a8e986d906cbe);

1157

[ 1164](structbt__iso__info.md#a4ead7e3c5ab496b6cfc2becfaddb3746) bool [can\_send](structbt__iso__info.md#a4ead7e3c5ab496b6cfc2becfaddb3746);

1165

[ 1172](structbt__iso__info.md#a9e00edb4e09bae39a37956011ccca353) bool [can\_recv](structbt__iso__info.md#a9e00edb4e09bae39a37956011ccca353);

1173

1175 union {

1176#if defined(CONFIG\_BT\_ISO\_UNICAST) || defined(\_\_DOXYGEN\_\_)

[ 1184](structbt__iso__info.md#a423474bd89ecdc614e6dfb8ea84db27e) struct [bt\_iso\_unicast\_info](structbt__iso__unicast__info.md) [unicast](structbt__iso__info.md#a423474bd89ecdc614e6dfb8ea84db27e);

1185#endif /\* CONFIG\_BT\_ISO\_UNICAST \*/

1186#if defined(CONFIG\_BT\_ISO\_BROADCASTER) || defined(\_\_DOXYGEN\_\_)

[ 1193](structbt__iso__info.md#a94e8132738697efa39857612399385b8) struct [bt\_iso\_broadcaster\_info](structbt__iso__broadcaster__info.md) [broadcaster](structbt__iso__info.md#a94e8132738697efa39857612399385b8);

1194#endif /\* CONFIG\_BT\_ISO\_BROADCASTER \*/

1195#if defined(CONFIG\_BT\_ISO\_SYNC\_RECEIVER) || defined(\_\_DOXYGEN\_\_)

[ 1202](structbt__iso__info.md#ac1edf09109a5e40a4f675281a7d9e300) struct [bt\_iso\_sync\_receiver\_info](structbt__iso__sync__receiver__info.md) [sync\_receiver](structbt__iso__info.md#ac1edf09109a5e40a4f675281a7d9e300);

1203#endif /\* CONFIG\_BT\_ISO\_SYNC\_RECEIVER \*/

1204 };

1205};

1206

[ 1215](group__bt__iso.md#ga75e58ed5bfa48f84000f1ce974d649c6)int [bt\_iso\_chan\_get\_info](group__bt__iso.md#ga75e58ed5bfa48f84000f1ce974d649c6)(const struct [bt\_iso\_chan](structbt__iso__chan.md) \*chan, struct [bt\_iso\_info](structbt__iso__info.md) \*info);

1216

[ 1232](group__bt__iso.md#gaa3942147fdeebc36039cc35c4e984411)int [bt\_iso\_chan\_get\_tx\_sync](group__bt__iso.md#gaa3942147fdeebc36039cc35c4e984411)(const struct [bt\_iso\_chan](structbt__iso__chan.md) \*chan, struct [bt\_iso\_tx\_info](structbt__iso__tx__info.md) \*info);

1233

[ 1239](structbt__iso__big__cb.md)struct [bt\_iso\_big\_cb](structbt__iso__big__cb.md) {

[ 1245](structbt__iso__big__cb.md#ac84e00545dbb330311482eb5abd4a78b) void (\*[started](structbt__iso__big__cb.md#ac84e00545dbb330311482eb5abd4a78b))(struct bt\_iso\_big \*big);

1246

[ 1253](structbt__iso__big__cb.md#a43d6ee745f7852460f843ced33c777c2) void (\*[stopped](structbt__iso__big__cb.md#a43d6ee745f7852460f843ced33c777c2))(struct bt\_iso\_big \*big, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) reason);

1254

1256 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) \_node;

1257};

1258

[ 1268](group__bt__iso.md#ga8a01a56e4a4555ed65a67065facfca76)int [bt\_iso\_big\_register\_cb](group__bt__iso.md#ga8a01a56e4a4555ed65a67065facfca76)(struct [bt\_iso\_big\_cb](structbt__iso__big__cb.md) \*cb);

1269

[ 1281](group__bt__iso.md#gac9937316382d257493c7d0359f1341f5)int [bt\_iso\_big\_create](group__bt__iso.md#gac9937316382d257493c7d0359f1341f5)(struct bt\_le\_ext\_adv \*padv, struct [bt\_iso\_big\_create\_param](structbt__iso__big__create__param.md) \*param,

1282 struct bt\_iso\_big \*\*out\_big);

1283

[ 1291](group__bt__iso.md#gab9c06a86bf5cc023f5f9bd16c5d3265b)int [bt\_iso\_big\_terminate](group__bt__iso.md#gab9c06a86bf5cc023f5f9bd16c5d3265b)(struct bt\_iso\_big \*big);

1292

[ 1302](group__bt__iso.md#ga790cfeb8516020f317802e019dca4754)int [bt\_iso\_big\_sync](group__bt__iso.md#ga790cfeb8516020f317802e019dca4754)(struct bt\_le\_per\_adv\_sync \*sync, struct [bt\_iso\_big\_sync\_param](structbt__iso__big__sync__param.md) \*param,

1303 struct bt\_iso\_big \*\*out\_big);

1304

1305#ifdef \_\_cplusplus

1306}

1307#endif

1308

1312

1313#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_ISO\_H\_ \*/

[addr.h](addr_8h.md)

Bluetooth device address definitions and utilities.

[bluetooth.h](bluetooth_2bluetooth_8h.md)

Bluetooth subsystem core APIs.

[buf.h](buf_8h.md)

Bluetooth data buffer API.

[conn.h](conn_8h.md)

Bluetooth connection handling.

[bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783)

bt\_security\_t

Security level.

**Definition** conn.h:814

[bt\_iso\_chan\_send](group__bt__iso.md#ga0dbb89a133011a833be7d18161471c6a)

int bt\_iso\_chan\_send(struct bt\_iso\_chan \*chan, struct net\_buf \*buf, uint16\_t seq\_num)

Send data to ISO channel without timestamp.

[bt\_iso\_server\_unregister](group__bt__iso.md#ga0ed72a4f7a418ae5aa3bb4f48fd5c9e6)

int bt\_iso\_server\_unregister(struct bt\_iso\_server \*server)

Unregister ISO server.

[bt\_iso\_remove\_data\_path](group__bt__iso.md#ga53be464e005392676830feeddd8cdc22)

int bt\_iso\_remove\_data\_path(const struct bt\_iso\_chan \*chan, uint8\_t dir)

Removes the ISO data path for a ISO channel.

[BT\_ISO\_BROADCAST\_CODE\_SIZE](group__bt__iso.md#ga5551cab9896764eec39b8e6102e561e5)

#define BT\_ISO\_BROADCAST\_CODE\_SIZE

Broadcast code size.

**Definition** iso.h:141

[bt\_iso\_chan\_get\_info](group__bt__iso.md#ga75e58ed5bfa48f84000f1ce974d649c6)

int bt\_iso\_chan\_get\_info(const struct bt\_iso\_chan \*chan, struct bt\_iso\_info \*info)

Get ISO channel info.

[bt\_iso\_big\_sync](group__bt__iso.md#ga790cfeb8516020f317802e019dca4754)

int bt\_iso\_big\_sync(struct bt\_le\_per\_adv\_sync \*sync, struct bt\_iso\_big\_sync\_param \*param, struct bt\_iso\_big \*\*out\_big)

Creates a BIG as a receiver.

[bt\_iso\_big\_register\_cb](group__bt__iso.md#ga8a01a56e4a4555ed65a67065facfca76)

int bt\_iso\_big\_register\_cb(struct bt\_iso\_big\_cb \*cb)

Registers callbacks for Broadcast Sources.

[bt\_iso\_chan\_disconnect](group__bt__iso.md#ga94c5c788b099284219e5a303b4b8ea69)

int bt\_iso\_chan\_disconnect(struct bt\_iso\_chan \*chan)

Disconnect connected ISO channel.

[bt\_iso\_chan\_connect](group__bt__iso.md#ga98953a261f3699b62cd19ab4977e0b4c)

int bt\_iso\_chan\_connect(const struct bt\_iso\_connect\_param \*param, size\_t count)

Connect ISO channels on ACL connections.

[bt\_iso\_cig\_reconfigure](group__bt__iso.md#ga98f557c183a82066b81f0265c225bebe)

int bt\_iso\_cig\_reconfigure(struct bt\_iso\_cig \*cig, const struct bt\_iso\_cig\_param \*param)

Reconfigure a CIG as a central.

[bt\_iso\_chan\_get\_tx\_sync](group__bt__iso.md#gaa3942147fdeebc36039cc35c4e984411)

int bt\_iso\_chan\_get\_tx\_sync(const struct bt\_iso\_chan \*chan, struct bt\_iso\_tx\_info \*info)

Get ISO transmission timing info.

[bt\_iso\_setup\_data\_path](group__bt__iso.md#gaa74c762451cfb5d04ffcd8d396a75447)

int bt\_iso\_setup\_data\_path(const struct bt\_iso\_chan \*chan, uint8\_t dir, const struct bt\_iso\_chan\_path \*path)

Sets up the ISO data path for a ISO channel.

[bt\_iso\_chan\_send\_ts](group__bt__iso.md#gab75b817770e3b685920587afde39d6cd)

int bt\_iso\_chan\_send\_ts(struct bt\_iso\_chan \*chan, struct net\_buf \*buf, uint16\_t seq\_num, uint32\_t ts)

Send data to ISO channel with timestamp.

[bt\_iso\_big\_terminate](group__bt__iso.md#gab9c06a86bf5cc023f5f9bd16c5d3265b)

int bt\_iso\_big\_terminate(struct bt\_iso\_big \*big)

Terminates a BIG as a broadcaster or receiver.

[bt\_iso\_big\_create](group__bt__iso.md#gac9937316382d257493c7d0359f1341f5)

int bt\_iso\_big\_create(struct bt\_le\_ext\_adv \*padv, struct bt\_iso\_big\_create\_param \*param, struct bt\_iso\_big \*\*out\_big)

Creates a BIG as a broadcaster.

[bt\_iso\_cig\_terminate](group__bt__iso.md#gad4b6a7286593ff099117113b6ca996f8)

int bt\_iso\_cig\_terminate(struct bt\_iso\_cig \*cig)

Terminates a CIG as a central.

[bt\_iso\_cig\_create](group__bt__iso.md#gaea03fc251206f18de320506064c1631f)

int bt\_iso\_cig\_create(const struct bt\_iso\_cig\_param \*param, struct bt\_iso\_cig \*\*out\_cig)

Creates a CIG as a central.

[bt\_iso\_state](group__bt__iso.md#gaf2925460cc22cc4220dc376bcbee6201)

bt\_iso\_state

Life-span states of ISO channel.

**Definition** iso.h:171

[bt\_iso\_chan\_type](group__bt__iso.md#gafcbd720c67c6a6e5f1cae1395e1e06f0)

bt\_iso\_chan\_type

ISO Channel Type.

**Definition** iso.h:188

[bt\_iso\_server\_register](group__bt__iso.md#gaff0e52777b2140519c63b54b9618bca8)

int bt\_iso\_server\_register(struct bt\_iso\_server \*server)

Register ISO server.

[BT\_ISO\_FLAGS\_VALID](group__bt__iso.md#gga2c62af103a71aa8f5f8aa103b1245866a143de2c153179b3c40aca51c016e6382)

@ BT\_ISO\_FLAGS\_VALID

The ISO packet is valid.

**Definition** iso.h:335

[BT\_ISO\_FLAGS\_LOST](group__bt__iso.md#gga2c62af103a71aa8f5f8aa103b1245866a5e87d48b6e96275744590194b75396ff)

@ BT\_ISO\_FLAGS\_LOST

The ISO packet was lost.

**Definition** iso.h:345

[BT\_ISO\_FLAGS\_ERROR](group__bt__iso.md#gga2c62af103a71aa8f5f8aa103b1245866a5f0aa6e3150819821f800dd7376e2218)

@ BT\_ISO\_FLAGS\_ERROR

The ISO packet may possibly contain errors.

**Definition** iso.h:342

[BT\_ISO\_FLAGS\_TS](group__bt__iso.md#gga2c62af103a71aa8f5f8aa103b1245866a96f645c1c14593370fd6e0443b019a23)

@ BT\_ISO\_FLAGS\_TS

Timestamp is valid.

**Definition** iso.h:353

[BT\_ISO\_STATE\_ENCRYPT\_PENDING](group__bt__iso.md#ggaf2925460cc22cc4220dc376bcbee6201a3ff6aa78bb7ed364b46c1457555aaba5)

@ BT\_ISO\_STATE\_ENCRYPT\_PENDING

Channel is pending ACL encryption before connecting.

**Definition** iso.h:175

[BT\_ISO\_STATE\_CONNECTING](group__bt__iso.md#ggaf2925460cc22cc4220dc376bcbee6201a4cb48a0a2a2ac37bbab5eded1bc3fd22)

@ BT\_ISO\_STATE\_CONNECTING

Channel in connecting state.

**Definition** iso.h:177

[BT\_ISO\_STATE\_CONNECTED](group__bt__iso.md#ggaf2925460cc22cc4220dc376bcbee6201acfa2a00a1c203418768ce789cd0cec7d)

@ BT\_ISO\_STATE\_CONNECTED

Channel ready for upper layer traffic on it.

**Definition** iso.h:179

[BT\_ISO\_STATE\_DISCONNECTING](group__bt__iso.md#ggaf2925460cc22cc4220dc376bcbee6201aebc34f9c32f1cd5e3197c7edaf657340)

@ BT\_ISO\_STATE\_DISCONNECTING

Channel in disconnecting state.

**Definition** iso.h:181

[BT\_ISO\_STATE\_DISCONNECTED](group__bt__iso.md#ggaf2925460cc22cc4220dc376bcbee6201af392f8825090c7beb304efc860a1911d)

@ BT\_ISO\_STATE\_DISCONNECTED

Channel disconnected.

**Definition** iso.h:173

[BT\_ISO\_CHAN\_TYPE\_CENTRAL](group__bt__iso.md#ggafcbd720c67c6a6e5f1cae1395e1e06f0a46a0148a474b297d38d67fb18bdb410a)

@ BT\_ISO\_CHAN\_TYPE\_CENTRAL

Connected as central.

**Definition** iso.h:190

[BT\_ISO\_CHAN\_TYPE\_NONE](group__bt__iso.md#ggafcbd720c67c6a6e5f1cae1395e1e06f0a58579ee03e3769501536826248758f17)

@ BT\_ISO\_CHAN\_TYPE\_NONE

No channel type.

**Definition** iso.h:189

[BT\_ISO\_CHAN\_TYPE\_BROADCASTER](group__bt__iso.md#ggafcbd720c67c6a6e5f1cae1395e1e06f0a63fb0b72a274afd24ff6b0d04d28910b)

@ BT\_ISO\_CHAN\_TYPE\_BROADCASTER

Isochronous broadcaster.

**Definition** iso.h:192

[BT\_ISO\_CHAN\_TYPE\_SYNC\_RECEIVER](group__bt__iso.md#ggafcbd720c67c6a6e5f1cae1395e1e06f0a725ae4b23a26a8569f5abb6a1e8134c2)

@ BT\_ISO\_CHAN\_TYPE\_SYNC\_RECEIVER

Synchronized receiver.

**Definition** iso.h:193

[BT\_ISO\_CHAN\_TYPE\_PERIPHERAL](group__bt__iso.md#ggafcbd720c67c6a6e5f1cae1395e1e06f0aa8b51a9ebacbaaac90956d7a9a816edb)

@ BT\_ISO\_CHAN\_TYPE\_PERIPHERAL

Connected as peripheral.

**Definition** iso.h:191

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[hci.h](hci_8h.md)

[net\_buf.h](net__buf_8h.md)

Buffer management.

[slist.h](slist_8h.md)

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[bt\_addr\_le\_t](structbt__addr__le__t.md)

Bluetooth LE Device Address.

**Definition** addr.h:49

[bt\_iso\_accept\_info](structbt__iso__accept__info.md)

ISO Accept Info Structure.

**Definition** iso.h:766

[bt\_iso\_accept\_info::acl](structbt__iso__accept__info.md#a4225ccc90f1e17e26ce61fe398f506d1)

struct bt\_conn \* acl

The ACL connection that is requesting authorization.

**Definition** iso.h:768

[bt\_iso\_accept\_info::cis\_id](structbt__iso__accept__info.md#a688809132997c37a6fe2529498a4ee0e)

uint8\_t cis\_id

The ID of the connected isochronous stream (CIS) on the central.

**Definition** iso.h:782

[bt\_iso\_accept\_info::cig\_id](structbt__iso__accept__info.md#a88002043a67c89c8d518ebdf92cf8847)

uint8\_t cig\_id

The ID of the connected isochronous group (CIG) on the central.

**Definition** iso.h:775

[bt\_iso\_big\_cb](structbt__iso__big__cb.md)

Struct to hold the Broadcast Isochronous Group callbacks.

**Definition** iso.h:1239

[bt\_iso\_big\_cb::stopped](structbt__iso__big__cb.md#a43d6ee745f7852460f843ced33c777c2)

void(\* stopped)(struct bt\_iso\_big \*big, uint8\_t reason)

The BIG has stopped and none of the streams are ready for data.

**Definition** iso.h:1253

[bt\_iso\_big\_cb::started](structbt__iso__big__cb.md#ac84e00545dbb330311482eb5abd4a78b)

void(\* started)(struct bt\_iso\_big \*big)

The BIG has started and all of the streams are ready for data.

**Definition** iso.h:1245

[bt\_iso\_big\_create\_param](structbt__iso__big__create__param.md)

Broadcast Isochronous Group (BIG) creation parameters.

**Definition** iso.h:500

[bt\_iso\_big\_create\_param::encryption](structbt__iso__big__create__param.md#a1288fa2a8f6bb3e2ab26729e245277e1)

bool encryption

Whether or not to encrypt the streams.

**Definition** iso.h:542

[bt\_iso\_big\_create\_param::iso\_interval](structbt__iso__big__create__param.md#a63cd16824e9d09e29d3c7e135b08d932)

uint16\_t iso\_interval

ISO interval.

**Definition** iso.h:584

[bt\_iso\_big\_create\_param::bis\_channels](structbt__iso__big__create__param.md#a7548bbb75f240a70435cb86a48846d0a)

struct bt\_iso\_chan \*\* bis\_channels

Array of pointers to BIS channels.

**Definition** iso.h:502

[bt\_iso\_big\_create\_param::interval](structbt__iso__big__create__param.md#a7aaef1f7a78ae1088886a78739fd6849)

uint32\_t interval

Channel interval in us.

**Definition** iso.h:516

[bt\_iso\_big\_create\_param::num\_bis](structbt__iso__big__create__param.md#a8ae9c225798e9f5b72fe0b8c3b6f2cf0)

uint8\_t num\_bis

Number of channels in bis\_channels.

**Definition** iso.h:509

[bt\_iso\_big\_create\_param::framing](structbt__iso__big__create__param.md#aab0e9f66cb10643e72d6382718ed4c0d)

uint8\_t framing

Channel framing mode.

**Definition** iso.h:539

[bt\_iso\_big\_create\_param::bcode](structbt__iso__big__create__param.md#aaee9af5a21b2f9812f9635c526f3a923)

uint8\_t bcode[16]

Broadcast code.

**Definition** iso.h:556

[bt\_iso\_big\_create\_param::latency](structbt__iso__big__create__param.md#ab847021da2e604036cecf90483e12132)

uint16\_t latency

Channel Latency in ms.

**Definition** iso.h:525

[bt\_iso\_big\_create\_param::packing](structbt__iso__big__create__param.md#ad478d7b36fb34b8e57a25ae0029e4c51)

uint8\_t packing

Channel packing mode.

**Definition** iso.h:532

[bt\_iso\_big\_create\_param::irc](structbt__iso__big__create__param.md#ad931ff1f19f92c29c40d934346498e79)

uint8\_t irc

Immediate Repetition Count.

**Definition** iso.h:566

[bt\_iso\_big\_create\_param::pto](structbt__iso__big__create__param.md#affce506bd271d9b0e497160c163c5798)

uint8\_t pto

Pre-transmission offset.

**Definition** iso.h:575

[bt\_iso\_big\_sync\_param](structbt__iso__big__sync__param.md)

Broadcast Isochronous Group (BIG) Sync Parameters.

**Definition** iso.h:589

[bt\_iso\_big\_sync\_param::bis\_bitfield](structbt__iso__big__sync__param.md#a14b03509daf760edbead86659f733136)

uint32\_t bis\_bitfield

Bitfield of the BISes to sync to.

**Definition** iso.h:608

[bt\_iso\_big\_sync\_param::mse](structbt__iso__big__sync__param.md#a16b332b4a0f373cb21e5da6e6e383b9e)

uint32\_t mse

Maximum subevents.

**Definition** iso.h:620

[bt\_iso\_big\_sync\_param::sync\_timeout](structbt__iso__big__sync__param.md#a8e344870fc0e380e6588eb90c7ef72f9)

uint16\_t sync\_timeout

Synchronization timeout for the BIG (N \* 10 MS).

**Definition** iso.h:627

[bt\_iso\_big\_sync\_param::encryption](structbt__iso__big__sync__param.md#a8e5cffe8960477e7f64707d7dd4191f6)

bool encryption

Whether or not the streams of the BIG are encrypted.

**Definition** iso.h:630

[bt\_iso\_big\_sync\_param::num\_bis](structbt__iso__big__sync__param.md#a96cd109e9f5820531635d48e88b4bff8)

uint8\_t num\_bis

Number channels in bis\_channels.

**Definition** iso.h:598

[bt\_iso\_big\_sync\_param::bcode](structbt__iso__big__sync__param.md#aaecdeabed10b90e84b618dac1129a9dc)

uint8\_t bcode[16]

Broadcast code.

**Definition** iso.h:644

[bt\_iso\_big\_sync\_param::bis\_channels](structbt__iso__big__sync__param.md#ac56d7206c3434837a52059716355adad)

struct bt\_iso\_chan \*\* bis\_channels

Array of pointers to BIS channels.

**Definition** iso.h:591

[bt\_iso\_biginfo](structbt__iso__biginfo.md)

Broadcast Isochronous Group (BIG) information.

**Definition** iso.h:648

[bt\_iso\_biginfo::framing](structbt__iso__biginfo.md#a1084c209d122d2d13244b77659ce28dd)

uint8\_t framing

Channel framing mode.

**Definition** iso.h:686

[bt\_iso\_biginfo::num\_bis](structbt__iso__biginfo.md#a10eb24596a4353da3feb0d30fed35ae7)

uint8\_t num\_bis

Number of BISes in the BIG.

**Definition** iso.h:656

[bt\_iso\_biginfo::sub\_evt\_count](structbt__iso__biginfo.md#a24eb83f7b54e9f949cc07e9955b4a8b8)

uint8\_t sub\_evt\_count

Maximum number of subevents in each isochronous event.

**Definition** iso.h:659

[bt\_iso\_biginfo::phy](structbt__iso__biginfo.md#a2cbaf6a89e8aaf62c7048e04523e57d4)

uint8\_t phy

Channel PHY.

**Definition** iso.h:683

[bt\_iso\_biginfo::sdu\_interval](structbt__iso__biginfo.md#a4a6d6cdea56a69a0b3b3fd021489750d)

uint32\_t sdu\_interval

The interval, in microseconds, of periodic SDUs.

**Definition** iso.h:677

[bt\_iso\_biginfo::offset](structbt__iso__biginfo.md#a4efb91dc2f249e41c65cd0dcbfe45bad)

uint8\_t offset

Offset used for pre-transmissions.

**Definition** iso.h:668

[bt\_iso\_biginfo::sid](structbt__iso__biginfo.md#a78e0a53f920980081d7b0702b02cf386)

uint8\_t sid

Advertiser SID.

**Definition** iso.h:653

[bt\_iso\_biginfo::encryption](structbt__iso__biginfo.md#a7d54ecb896c0d6bc590311d5d5a3ac7b)

bool encryption

Whether or not the BIG is encrypted.

**Definition** iso.h:689

[bt\_iso\_biginfo::rep\_count](structbt__iso__biginfo.md#a8458f6d6ebe936212d928caca61b13bd)

uint8\_t rep\_count

The number of times a payload is transmitted in a BIS event.

**Definition** iso.h:671

[bt\_iso\_biginfo::max\_sdu](structbt__iso__biginfo.md#a9fddcb74f3de7eb857583a0179427f84)

uint16\_t max\_sdu

Maximum size of an SDU, in octets.

**Definition** iso.h:680

[bt\_iso\_biginfo::addr](structbt__iso__biginfo.md#aa7dbfd342eecf8ffc2fce9d3fa7209ea)

const bt\_addr\_le\_t \* addr

Address of the advertiser.

**Definition** iso.h:650

[bt\_iso\_biginfo::burst\_number](structbt__iso__biginfo.md#ad114dd97500d12242da77e8522133953)

uint8\_t burst\_number

The number of new payloads in each BIS event.

**Definition** iso.h:665

[bt\_iso\_biginfo::max\_pdu](structbt__iso__biginfo.md#af356aa29aa82c8deb63a9f47e54070a1)

uint16\_t max\_pdu

Maximum size, in octets, of the payload.

**Definition** iso.h:674

[bt\_iso\_biginfo::iso\_interval](structbt__iso__biginfo.md#afe96caf570314731f6c543b40d7def9a)

uint16\_t iso\_interval

Interval between two BIG anchor point (N \* 1.25 ms).

**Definition** iso.h:662

[bt\_iso\_broadcaster\_info](structbt__iso__broadcaster__info.md)

ISO Broadcaster Info Structure.

**Definition** iso.h:1106

[bt\_iso\_broadcaster\_info::phy](structbt__iso__broadcaster__info.md#a3d4e44a1da54e5ca0f2002ca3f6e7a13)

uint8\_t phy

The transport PHY.

**Definition** iso.h:1120

[bt\_iso\_broadcaster\_info::sync\_delay](structbt__iso__broadcaster__info.md#a577370ab24ebd4d80db4d8ffdb918483)

uint32\_t sync\_delay

The maximum time in us for all PDUs of all BIS in a BIG event.

**Definition** iso.h:1108

[bt\_iso\_broadcaster\_info::latency](structbt__iso__broadcaster__info.md#a71388f9b64510ab91c3147f05f775aeb)

uint32\_t latency

The transport latency in us.

**Definition** iso.h:1111

[bt\_iso\_broadcaster\_info::pto](structbt__iso__broadcaster__info.md#a9f93161fb7f81d5eb3a55f955be1b85d)

uint32\_t pto

Pre-transmission offset (N \* 1.25 ms).

**Definition** iso.h:1114

[bt\_iso\_broadcaster\_info::max\_pdu](structbt__iso__broadcaster__info.md#aa57b6e08cf4d3d154762c8c43de0f2cf)

uint16\_t max\_pdu

The maximum PDU size in octets.

**Definition** iso.h:1117

[bt\_iso\_broadcaster\_info::bn](structbt__iso__broadcaster__info.md#ab3cb80e6b362e093e6924ab11b8737e9)

uint8\_t bn

The burst number.

**Definition** iso.h:1123

[bt\_iso\_broadcaster\_info::irc](structbt__iso__broadcaster__info.md#ac1feade59bbad1e08418e1808619f775)

uint8\_t irc

Number of times a payload is transmitted in a BIS event.

**Definition** iso.h:1126

[bt\_iso\_chan\_io\_qos](structbt__iso__chan__io__qos.md)

ISO Channel IO QoS structure.

**Definition** iso.h:224

[bt\_iso\_chan\_io\_qos::phy](structbt__iso__chan__io__qos.md#a2180a4f82e4cdf5288b7f67701a16ad6)

uint8\_t phy

Channel PHY - See the bt\_gap\_le\_phy values.

**Definition** iso.h:236

[bt\_iso\_chan\_io\_qos::rtn](structbt__iso__chan__io__qos.md#a5106bfd09f6be52604e7c7f0e3390684)

uint8\_t rtn

Channel Retransmission Number.

**Definition** iso.h:242

[bt\_iso\_chan\_io\_qos::burst\_number](structbt__iso__chan__io__qos.md#ac64a3ce7282ac8bc5b5420a46417b22c)

uint8\_t burst\_number

Burst number.

**Definition** iso.h:261

[bt\_iso\_chan\_io\_qos::sdu](structbt__iso__chan__io__qos.md#ae52611dc326b6777620ff7aa43f566e9)

uint16\_t sdu

Channel SDU.

**Definition** iso.h:230

[bt\_iso\_chan\_io\_qos::max\_pdu](structbt__iso__chan__io__qos.md#ae9e7678a63030353eea65152d89464cd)

uint16\_t max\_pdu

Maximum PDU size.

**Definition** iso.h:254

[bt\_iso\_chan\_ops](structbt__iso__chan__ops.md)

ISO Channel operations structure.

**Definition** iso.h:693

[bt\_iso\_chan\_ops::sent](structbt__iso__chan__ops.md#a048954070628229b8aacd373de1fb236)

void(\* sent)(struct bt\_iso\_chan \*chan)

Channel sent callback.

**Definition** iso.h:762

[bt\_iso\_chan\_ops::disconnected](structbt__iso__chan__ops.md#a2069849352019362e5dc7d68f835f359)

void(\* disconnected)(struct bt\_iso\_chan \*chan, uint8\_t reason)

Channel disconnected callback.

**Definition** iso.h:725

[bt\_iso\_chan\_ops::connected](structbt__iso__chan__ops.md#a6b0e51770158da7b728e1084a8e44504)

void(\* connected)(struct bt\_iso\_chan \*chan)

Channel connected callback.

**Definition** iso.h:705

[bt\_iso\_chan\_ops::recv](structbt__iso__chan__ops.md#a6d5d9423fff83f8f337f97b3fc018f39)

void(\* recv)(struct bt\_iso\_chan \*chan, const struct bt\_iso\_recv\_info \*info, struct net\_buf \*buf)

Channel recv callback.

**Definition** iso.h:749

[bt\_iso\_chan\_path](structbt__iso__chan__path.md)

ISO Channel Data Path structure.

**Definition** iso.h:298

[bt\_iso\_chan\_path::cc\_len](structbt__iso__chan__path.md#a0da75c4911a197fed7fd7f17c76dddae)

uint8\_t cc\_len

Codec Configuration length.

**Definition** iso.h:323

[bt\_iso\_chan\_path::format](structbt__iso__chan__path.md#a519c884281207d1165a61ccfb7fbcdf4)

uint8\_t format

Coding Format.

**Definition** iso.h:311

[bt\_iso\_chan\_path::pid](structbt__iso__chan__path.md#a5e4fb798376489a38a87e4052ff85550)

uint8\_t pid

Default path ID.

**Definition** iso.h:305

[bt\_iso\_chan\_path::cid](structbt__iso__chan__path.md#a95db7917f7b9e90a33f494233c3266eb)

uint16\_t cid

Company ID.

**Definition** iso.h:313

[bt\_iso\_chan\_path::cc](structbt__iso__chan__path.md#acba5454d02460e8c2d51851677e310bb)

uint8\_t \* cc

Pointer to an array containing the Codec Configuration.

**Definition** iso.h:329

[bt\_iso\_chan\_path::delay](structbt__iso__chan__path.md#adaed07de7e09263e3e941817eeb44258)

uint32\_t delay

Controller Delay in microseconds.

**Definition** iso.h:321

[bt\_iso\_chan\_path::vid](structbt__iso__chan__path.md#aebc12293ba0b10a87f1852e2a3e53a23)

uint16\_t vid

Vendor-defined Codec ID.

**Definition** iso.h:315

[bt\_iso\_chan\_qos](structbt__iso__chan__qos.md)

ISO Channel QoS structure.

**Definition** iso.h:266

[bt\_iso\_chan\_qos::tx](structbt__iso__chan__qos.md#a47a99a6ccfa5f1e0c9fb859e66d2e9e3)

struct bt\_iso\_chan\_io\_qos \* tx

Channel Transmission QoS.

**Definition** iso.h:283

[bt\_iso\_chan\_qos::num\_subevents](structbt__iso__chan__qos.md#a4c6bfa577f8cbd724ed2561850fd6255)

uint8\_t num\_subevents

Number of subevents.

**Definition** iso.h:293

[bt\_iso\_chan\_qos::rx](structbt__iso__chan__qos.md#ac231434d1798f431c4fbac5a759784a5)

struct bt\_iso\_chan\_io\_qos \* rx

Channel Receiving QoS.

**Definition** iso.h:274

[bt\_iso\_chan](structbt__iso__chan.md)

ISO Channel structure.

**Definition** iso.h:197

[bt\_iso\_chan::ops](structbt__iso__chan.md#a214fe133602ac8dcfaaec7f372e12da8)

struct bt\_iso\_chan\_ops \* ops

Channel operations reference.

**Definition** iso.h:201

[bt\_iso\_chan::state](structbt__iso__chan.md#a2b0fc7180d1983ee4a415c5331bed93d)

enum bt\_iso\_state state

Channel state.

**Definition** iso.h:205

[bt\_iso\_chan::required\_sec\_level](structbt__iso__chan.md#a75347e4f16e715be06298ccf36c8521c)

bt\_security\_t required\_sec\_level

The required security level of the channel.

**Definition** iso.h:217

[bt\_iso\_chan::iso](structbt__iso__chan.md#a7fd728385a3aec11be8883bdee8aedea)

struct bt\_conn \* iso

Channel connection reference.

**Definition** iso.h:199

[bt\_iso\_chan::node](structbt__iso__chan.md#aba7bf6dcad93b121c46daa6ad473a51c)

sys\_snode\_t node

**Definition** iso.h:220

[bt\_iso\_chan::qos](structbt__iso__chan.md#abe94fca71506bd590d9ef4465258914d)

struct bt\_iso\_chan\_qos \* qos

Channel QoS reference.

**Definition** iso.h:203

[bt\_iso\_cig\_param](structbt__iso__cig__param.md)

Connected Isochronous Group (CIG) parameters.

**Definition** iso.h:389

[bt\_iso\_cig\_param::p\_to\_c\_interval](structbt__iso__cig__param.md#a36d2eaa4fd3e08988d4c49ca0902a882)

uint32\_t p\_to\_c\_interval

Channel interval in us for SDUs sent from Peripheral to Central.

**Definition** iso.h:412

[bt\_iso\_cig\_param::packing](structbt__iso__cig__param.md#a3908eadf3080731cb891e803162d321c)

uint8\_t packing

Channel packing mode.

**Definition** iso.h:446

[bt\_iso\_cig\_param::framing](structbt__iso__cig__param.md#a4a09f9f6e7a8db17c3037c9f1761b18a)

uint8\_t framing

Channel framing mode.

**Definition** iso.h:453

[bt\_iso\_cig\_param::num\_cis](structbt__iso__cig__param.md#a69c12b704b9897d88b71bc96bd2d3024)

uint8\_t num\_cis

Number of channels in cis\_channels.

**Definition** iso.h:398

[bt\_iso\_cig\_param::sca](structbt__iso__cig__param.md#a83fdc5374f341a421e1394b08297cdff)

uint8\_t sca

Channel peripherals sleep clock accuracy Only for CIS.

**Definition** iso.h:439

[bt\_iso\_cig\_param::cis\_channels](structbt__iso__cig__param.md#a841dee850f3161bd8e904376792c8ad7)

struct bt\_iso\_chan \*\* cis\_channels

Array of pointers to CIS channels.

**Definition** iso.h:391

[bt\_iso\_cig\_param::iso\_interval](structbt__iso__cig__param.md#a85641a8f01d63b4221c013815c055526)

uint16\_t iso\_interval

ISO interval.

**Definition** iso.h:483

[bt\_iso\_cig\_param::c\_to\_p\_ft](structbt__iso__cig__param.md#aadc3762f3fec3127014378fe58c5b684)

uint8\_t c\_to\_p\_ft

Central to Peripheral flush timeout.

**Definition** iso.h:464

[bt\_iso\_cig\_param::p\_to\_c\_ft](structbt__iso__cig__param.md#ab222cdb0af475180dd715b4f5658dc65)

uint8\_t p\_to\_c\_ft

Peripheral to Central flush timeout.

**Definition** iso.h:474

[bt\_iso\_cig\_param::p\_to\_c\_latency](structbt__iso__cig__param.md#ad1725e09a397e83d1cc88ebd3a60ed93)

uint16\_t p\_to\_c\_latency

Channel Latency in ms for SDUs sent from Peripheral to Central.

**Definition** iso.h:430

[bt\_iso\_cig\_param::c\_to\_p\_interval](structbt__iso__cig__param.md#ad7349213bab902a68c726da51fac2306)

uint32\_t c\_to\_p\_interval

Channel interval in us for SDUs sent from Central to Peripheral.

**Definition** iso.h:405

[bt\_iso\_cig\_param::c\_to\_p\_latency](structbt__iso__cig__param.md#aeffe10e87d81285196e931dcad2882ba)

uint16\_t c\_to\_p\_latency

Channel Latency in ms for SDUs sent from Central to Peripheral.

**Definition** iso.h:421

[bt\_iso\_connect\_param](structbt__iso__connect__param.md)

ISO connection parameters structure.

**Definition** iso.h:488

[bt\_iso\_connect\_param::acl](structbt__iso__connect__param.md#aba2f3838e03a1e31699a4623ba93d372)

struct bt\_conn \* acl

The ACL connection.

**Definition** iso.h:493

[bt\_iso\_connect\_param::iso\_chan](structbt__iso__connect__param.md#ad004956584d2d065d8c0c52959f350d5)

struct bt\_iso\_chan \* iso\_chan

The ISO channel to connect.

**Definition** iso.h:490

[bt\_iso\_info](structbt__iso__info.md)

ISO channel Info Structure.

**Definition** iso.h:1148

[bt\_iso\_info::max\_subevent](structbt__iso__info.md#a02554d9114dc3e34305a8e986d906cbe)

uint8\_t max\_subevent

The maximum number of subevents in each ISO event.

**Definition** iso.h:1156

[bt\_iso\_info::unicast](structbt__iso__info.md#a423474bd89ecdc614e6dfb8ea84db27e)

struct bt\_iso\_unicast\_info unicast

Unicast specific Info.

**Definition** iso.h:1184

[bt\_iso\_info::can\_send](structbt__iso__info.md#a4ead7e3c5ab496b6cfc2becfaddb3746)

bool can\_send

True if the channel is able to send data.

**Definition** iso.h:1164

[bt\_iso\_info::iso\_interval](structbt__iso__info.md#a53c6c8eee63cd674d54dc1d40aa33a43)

uint16\_t iso\_interval

The ISO interval (N \* 1.25 ms).

**Definition** iso.h:1153

[bt\_iso\_info::broadcaster](structbt__iso__info.md#a94e8132738697efa39857612399385b8)

struct bt\_iso\_broadcaster\_info broadcaster

Broadcaster specific Info.

**Definition** iso.h:1193

[bt\_iso\_info::can\_recv](structbt__iso__info.md#a9e00edb4e09bae39a37956011ccca353)

bool can\_recv

True if the channel is able to recv data.

**Definition** iso.h:1172

[bt\_iso\_info::sync\_receiver](structbt__iso__info.md#ac1edf09109a5e40a4f675281a7d9e300)

struct bt\_iso\_sync\_receiver\_info sync\_receiver

Sync receiver specific Info.

**Definition** iso.h:1202

[bt\_iso\_info::type](structbt__iso__info.md#af01766b8eed556ca165222d19ff05838)

enum bt\_iso\_chan\_type type

Channel Type.

**Definition** iso.h:1150

[bt\_iso\_recv\_info](structbt__iso__recv__info.md)

ISO Meta Data structure for received ISO packets.

**Definition** iso.h:357

[bt\_iso\_recv\_info::flags](structbt__iso__recv__info.md#a0a7842fcb3251ed89b99fde43ba235a5)

uint8\_t flags

ISO packet flags bitfield (BT\_ISO\_FLAGS\_\*).

**Definition** iso.h:369

[bt\_iso\_recv\_info::ts](structbt__iso__recv__info.md#a4bf778ae9be39eb4a740c2eb9670d98a)

uint32\_t ts

ISO timestamp.

**Definition** iso.h:363

[bt\_iso\_recv\_info::seq\_num](structbt__iso__recv__info.md#a7c5b950df0359bb561140d0c2726fae6)

uint16\_t seq\_num

ISO packet sequence number of the first fragment in the SDU.

**Definition** iso.h:366

[bt\_iso\_server](structbt__iso__server.md)

ISO Server structure.

**Definition** iso.h:786

[bt\_iso\_server::sec\_level](structbt__iso__server.md#a43b53fd63d4deaa1c5599499eec29c99)

bt\_security\_t sec\_level

Required minimum security level.

**Definition** iso.h:793

[bt\_iso\_server::accept](structbt__iso__server.md#ae67a000ae524cba53b6bda503568ba38)

int(\* accept)(const struct bt\_iso\_accept\_info \*info, struct bt\_iso\_chan \*\*chan)

Server accept callback.

**Definition** iso.h:806

[bt\_iso\_sync\_receiver\_info](structbt__iso__sync__receiver__info.md)

ISO Synchronized Receiver Info Structure.

**Definition** iso.h:1130

[bt\_iso\_sync\_receiver\_info::latency](structbt__iso__sync__receiver__info.md#a24bad4231eb214a2c95b1da9ba59c284)

uint32\_t latency

The transport latency in us.

**Definition** iso.h:1132

[bt\_iso\_sync\_receiver\_info::max\_pdu](structbt__iso__sync__receiver__info.md#a40ff5a4d691a75802f211a63b1e12303)

uint16\_t max\_pdu

The maximum PDU size in octets.

**Definition** iso.h:1138

[bt\_iso\_sync\_receiver\_info::irc](structbt__iso__sync__receiver__info.md#a6185a7ac123be930650da6dc84c0c1e0)

uint8\_t irc

Number of times a payload is transmitted in a BIS event.

**Definition** iso.h:1144

[bt\_iso\_sync\_receiver\_info::pto](structbt__iso__sync__receiver__info.md#a80ac6e529491156109955219569fdec6)

uint32\_t pto

Pre-transmission offset (N \* 1.25 ms).

**Definition** iso.h:1135

[bt\_iso\_sync\_receiver\_info::bn](structbt__iso__sync__receiver__info.md#a8be50f8c6d76515ac290407959eaf0e1)

uint8\_t bn

The burst number.

**Definition** iso.h:1141

[bt\_iso\_tx\_info](structbt__iso__tx__info.md)

ISO Meta Data structure for transmitted ISO packets.

**Definition** iso.h:373

[bt\_iso\_tx\_info::offset](structbt__iso__tx__info.md#a0cff6aa2893fdc11160e4327afebed13)

uint32\_t offset

Time offset, in microseconds.

**Definition** iso.h:378

[bt\_iso\_tx\_info::seq\_num](structbt__iso__tx__info.md#a2791edea2f4f4459acc24c8dbaa33ded)

uint16\_t seq\_num

Packet sequence number.

**Definition** iso.h:381

[bt\_iso\_tx\_info::ts](structbt__iso__tx__info.md#ac8a6a4c073e4df1553d32339a6e4b051)

uint32\_t ts

CIG reference point or BIG anchor point of a transmitted SDU, in microseconds.

**Definition** iso.h:375

[bt\_iso\_unicast\_info](structbt__iso__unicast__info.md)

ISO Unicast Info Structure.

**Definition** iso.h:1083

[bt\_iso\_unicast\_info::cig\_sync\_delay](structbt__iso__unicast__info.md#a029c450e2324bbc6ee8fda6d1d10deef)

uint32\_t cig\_sync\_delay

The maximum time in us for all PDUs of all CIS in a CIG event.

**Definition** iso.h:1085

[bt\_iso\_unicast\_info::peripheral](structbt__iso__unicast__info.md#a03b084fefcab049efbe1a609a59d9c54)

struct bt\_iso\_unicast\_tx\_info peripheral

TX information for the peripheral to central data.

**Definition** iso.h:1102

[bt\_iso\_unicast\_info::subinterval](structbt__iso__unicast__info.md#a4d53dc6adc8d5519cf74982aa5031e74)

uint32\_t subinterval

The subinterval in microseconds.

**Definition** iso.h:1096

[bt\_iso\_unicast\_info::central](structbt__iso__unicast__info.md#a4fc402b934ae8aa65493df01c88cae34)

struct bt\_iso\_unicast\_tx\_info central

TX information for the central to peripheral data path.

**Definition** iso.h:1099

[bt\_iso\_unicast\_info::cis\_sync\_delay](structbt__iso__unicast__info.md#acbc8c068907eba204d369cf76f4f112d)

uint32\_t cis\_sync\_delay

The maximum time in us for all PDUs of this CIS in a CIG event.

**Definition** iso.h:1088

[bt\_iso\_unicast\_tx\_info](structbt__iso__unicast__tx__info.md)

ISO Unicast TX Info Structure.

**Definition** iso.h:1053

[bt\_iso\_unicast\_tx\_info::latency](structbt__iso__unicast__tx__info.md#a14548ee24fad8a26287aa0daba451a47)

uint32\_t latency

The transport latency in us.

**Definition** iso.h:1055

[bt\_iso\_unicast\_tx\_info::phy](structbt__iso__unicast__tx__info.md#a3134e0bdb663ad7184e23531504233a5)

uint8\_t phy

The transport PHY.

**Definition** iso.h:1064

[bt\_iso\_unicast\_tx\_info::max\_sdu](structbt__iso__unicast__tx__info.md#a7bed74a67bb73f6919d2817d82bcf996)

uint16\_t max\_sdu

The maximum SDU size in octets.

**Definition** iso.h:1073

[bt\_iso\_unicast\_tx\_info::flush\_timeout](structbt__iso__unicast__tx__info.md#aaf1f623eac2f84ca06082776179b71c5)

uint32\_t flush\_timeout

The flush timeout (N \* 1.25 ms).

**Definition** iso.h:1058

[bt\_iso\_unicast\_tx\_info::bn](structbt__iso__unicast__tx__info.md#ab4ea9d5bb535d29ae9406e948d8707a9)

uint8\_t bn

The burst number.

**Definition** iso.h:1067

[bt\_iso\_unicast\_tx\_info::sdu\_interval](structbt__iso__unicast__tx__info.md#adc91f9c200199400a84322a58d28a933)

uint32\_t sdu\_interval

The SDU interval in microseconds.

**Definition** iso.h:1079

[bt\_iso\_unicast\_tx\_info::max\_pdu](structbt__iso__unicast__tx__info.md#afe7dce9255613e5e2939d3719c720822)

uint16\_t max\_pdu

The maximum PDU size in octets.

**Definition** iso.h:1061

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** net\_buf.h:1006

[atomic.h](sys_2atomic_8h.md)

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [iso.h](iso_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
