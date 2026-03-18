---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/drivers_2uart_8h_source.html
original_path: doxygen/html/drivers_2uart_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uart.h

[Go to the documentation of this file.](drivers_2uart_8h.md)

1/\*

2 \* Copyright (c) 2018-2019 Nordic Semiconductor ASA

3 \* Copyright (c) 2015 Wind River Systems, Inc.

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

12

13#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_UART\_H\_

14#define ZEPHYR\_INCLUDE\_DRIVERS\_UART\_H\_

15

22

23#include <[errno.h](errno_8h.md)>

24#include <stddef.h>

25

26#include <[zephyr/device.h](device_8h.md)>

27

28#ifdef \_\_cplusplus

29extern "C" {

30#endif

31

[ 33](group__uart__interface.md#ga02552532e171e789efc1b000917a9be0)enum [uart\_line\_ctrl](group__uart__interface.md#ga02552532e171e789efc1b000917a9be0) {

[ 34](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a3fdd02679f4f103190f3c12ab3cda00b) [UART\_LINE\_CTRL\_BAUD\_RATE](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a3fdd02679f4f103190f3c12ab3cda00b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 35](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a205d22bd797ab1c55323dc1ffda75f0d) [UART\_LINE\_CTRL\_RTS](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a205d22bd797ab1c55323dc1ffda75f0d) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 36](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a19e76af9901fc0274a9e27ff40e29e23) [UART\_LINE\_CTRL\_DTR](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a19e76af9901fc0274a9e27ff40e29e23) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 37](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a6d2c438044dd64f5cef07bbe4c6b3e97) [UART\_LINE\_CTRL\_DCD](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a6d2c438044dd64f5cef07bbe4c6b3e97) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

[ 38](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a87d8bedb5c918c182b271884ee42d75c) [UART\_LINE\_CTRL\_DSR](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a87d8bedb5c918c182b271884ee42d75c) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

39};

40

[ 47](group__uart__interface.md#gadeba6c5485e01dfc1c8a6e1c21668a88)enum [uart\_rx\_stop\_reason](group__uart__interface.md#gadeba6c5485e01dfc1c8a6e1c21668a88) {

[ 49](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a442beffc51cdf265bbcb40810a9a6e54) [UART\_ERROR\_OVERRUN](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a442beffc51cdf265bbcb40810a9a6e54) = (1 << 0),

[ 51](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a86d38eac5a46e6659aa765164b833eb5) [UART\_ERROR\_PARITY](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a86d38eac5a46e6659aa765164b833eb5) = (1 << 1),

[ 53](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88af13f72a8c615b4bc570b5a4df573407b) [UART\_ERROR\_FRAMING](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88af13f72a8c615b4bc570b5a4df573407b) = (1 << 2),

[ 61](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a4986147e23cc46ab8c2aa7e151d09571) [UART\_BREAK](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a4986147e23cc46ab8c2aa7e151d09571) = (1 << 3),

[ 71](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88aad8ca4dca9a846560293df71e6b39786) [UART\_ERROR\_COLLISION](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88aad8ca4dca9a846560293df71e6b39786) = (1 << 4),

[ 73](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a412058adbf7668b7051efb8419984d60) [UART\_ERROR\_NOISE](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a412058adbf7668b7051efb8419984d60) = (1 << 5),

74};

75

[ 77](group__uart__interface.md#gab2ab6aacb6e3c43bb26d4274157e5711)enum [uart\_config\_parity](group__uart__interface.md#gab2ab6aacb6e3c43bb26d4274157e5711) {

[ 78](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711a6a23a2ef22fb3b144648b244fff82b8d) [UART\_CFG\_PARITY\_NONE](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711a6a23a2ef22fb3b144648b244fff82b8d),

[ 79](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711a8a618b0a531c8d62809e39eb56eaf5ed) [UART\_CFG\_PARITY\_ODD](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711a8a618b0a531c8d62809e39eb56eaf5ed),

[ 80](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711ac3a4310efe198a1fa7d977a5531486ba) [UART\_CFG\_PARITY\_EVEN](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711ac3a4310efe198a1fa7d977a5531486ba),

[ 81](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711a5ee61c29a32447644ff70385158a11ca) [UART\_CFG\_PARITY\_MARK](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711a5ee61c29a32447644ff70385158a11ca),

[ 82](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711a8dc5306c8ca26321431bcf22ce9b036c) [UART\_CFG\_PARITY\_SPACE](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711a8dc5306c8ca26321431bcf22ce9b036c),

83};

84

[ 86](group__uart__interface.md#gafc1aecb863e2456d73b78a49fcbad72e)enum [uart\_config\_stop\_bits](group__uart__interface.md#gafc1aecb863e2456d73b78a49fcbad72e) {

[ 87](group__uart__interface.md#ggafc1aecb863e2456d73b78a49fcbad72ea308c660590a9fd16143806e8bef002af) [UART\_CFG\_STOP\_BITS\_0\_5](group__uart__interface.md#ggafc1aecb863e2456d73b78a49fcbad72ea308c660590a9fd16143806e8bef002af),

[ 88](group__uart__interface.md#ggafc1aecb863e2456d73b78a49fcbad72ea73024f1618eb04385bf488214c635e58) [UART\_CFG\_STOP\_BITS\_1](group__uart__interface.md#ggafc1aecb863e2456d73b78a49fcbad72ea73024f1618eb04385bf488214c635e58),

[ 89](group__uart__interface.md#ggafc1aecb863e2456d73b78a49fcbad72ea1da47ec95b6a6eee65abef3d6d84f9ad) [UART\_CFG\_STOP\_BITS\_1\_5](group__uart__interface.md#ggafc1aecb863e2456d73b78a49fcbad72ea1da47ec95b6a6eee65abef3d6d84f9ad),

[ 90](group__uart__interface.md#ggafc1aecb863e2456d73b78a49fcbad72eae180ecebc76516e89669e1d16bfb31c6) [UART\_CFG\_STOP\_BITS\_2](group__uart__interface.md#ggafc1aecb863e2456d73b78a49fcbad72eae180ecebc76516e89669e1d16bfb31c6),

91};

92

[ 94](group__uart__interface.md#gab9f7de744a68a311330576d7da02c44a)enum [uart\_config\_data\_bits](group__uart__interface.md#gab9f7de744a68a311330576d7da02c44a) {

[ 95](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aa1b0545c2d1970e67d697b62510bfbe27) [UART\_CFG\_DATA\_BITS\_5](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aa1b0545c2d1970e67d697b62510bfbe27),

[ 96](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aac6e0f3c0479164c34144d0e6e28298e4) [UART\_CFG\_DATA\_BITS\_6](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aac6e0f3c0479164c34144d0e6e28298e4),

[ 97](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aa6120eb8f668b257c8c2dd0dc9cf0c913) [UART\_CFG\_DATA\_BITS\_7](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aa6120eb8f668b257c8c2dd0dc9cf0c913),

[ 98](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aa23f55bdb24b4016c8c23c518e981df97) [UART\_CFG\_DATA\_BITS\_8](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aa23f55bdb24b4016c8c23c518e981df97),

[ 99](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aaf3b601af696d8841fe79871ca3e41e5f) [UART\_CFG\_DATA\_BITS\_9](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aaf3b601af696d8841fe79871ca3e41e5f),

100};

101

[ 109](group__uart__interface.md#ga8e2f1b4a8d60d7a6c24835d1b26f99e8)enum [uart\_config\_flow\_control](group__uart__interface.md#ga8e2f1b4a8d60d7a6c24835d1b26f99e8) {

[ 110](group__uart__interface.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a546b28db6f8bfc26266e8f7d6b8ff973) [UART\_CFG\_FLOW\_CTRL\_NONE](group__uart__interface.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a546b28db6f8bfc26266e8f7d6b8ff973),

[ 111](group__uart__interface.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8ad682bfe14a9f0860d1fdc3e8e9d56f86) [UART\_CFG\_FLOW\_CTRL\_RTS\_CTS](group__uart__interface.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8ad682bfe14a9f0860d1fdc3e8e9d56f86),

[ 112](group__uart__interface.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a0efc5de86bf80119f750cf372814309f) [UART\_CFG\_FLOW\_CTRL\_DTR\_DSR](group__uart__interface.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a0efc5de86bf80119f750cf372814309f),

[ 113](group__uart__interface.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a9675cc80d44e980b66e99bc8548f085c) [UART\_CFG\_FLOW\_CTRL\_RS485](group__uart__interface.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a9675cc80d44e980b66e99bc8548f085c),

114};

115

[ 119](structuart__config.md)struct [uart\_config](structuart__config.md) {

[ 120](structuart__config.md#ab532159a689e8f38c2465ce2d1fef354) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [baudrate](structuart__config.md#ab532159a689e8f38c2465ce2d1fef354);

[ 121](structuart__config.md#a9371728729252797880de052aae01089) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [parity](structuart__config.md#a9371728729252797880de052aae01089);

[ 122](structuart__config.md#a7b98cd63c531110dc3dc99e94db73642) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [stop\_bits](structuart__config.md#a7b98cd63c531110dc3dc99e94db73642);

[ 123](structuart__config.md#a93ee24cf6669fb4cfece78a53d3ec6c5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data\_bits](structuart__config.md#a93ee24cf6669fb4cfece78a53d3ec6c5);

[ 124](structuart__config.md#af259c5efab532920b5cce7ae57f6af5e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flow\_ctrl](structuart__config.md#af259c5efab532920b5cce7ae57f6af5e);

125};

126

131

[ 139](group__uart__interrupt.md#gad7a26b1a1d6212d7d39c05c8ad4ec926)typedef void (\*[uart\_irq\_callback\_user\_data\_t](group__uart__interrupt.md#gad7a26b1a1d6212d7d39c05c8ad4ec926))(const struct [device](structdevice.md) \*dev,

140 void \*user\_data);

141

[ 147](group__uart__interrupt.md#ga6750414923953c84fb1e19177ec74ae0)typedef void (\*[uart\_irq\_config\_func\_t](group__uart__interrupt.md#ga6750414923953c84fb1e19177ec74ae0))(const struct [device](structdevice.md) \*dev);

148

155

[ 203](group__uart__async.md#gaf0c9513cbafa36d86b4c83f2b6a03dcd)enum [uart\_event\_type](group__uart__async.md#gaf0c9513cbafa36d86b4c83f2b6a03dcd) {

[ 205](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda4b5cdf863d8b6e5cd7b58f611808a6e4) [UART\_TX\_DONE](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda4b5cdf863d8b6e5cd7b58f611808a6e4),

[ 213](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0abcf565ba1011815285bb3845f8d5a1) [UART\_TX\_ABORTED](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0abcf565ba1011815285bb3845f8d5a1),

[ 224](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7) [UART\_RX\_RDY](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7),

[ 236](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0d250f372702526f1bce6d4dfe166abe) [UART\_RX\_BUF\_REQUEST](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0d250f372702526f1bce6d4dfe166abe),

[ 240](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcdab2d152bd84f659d4fc4060df29811b48) [UART\_RX\_BUF\_RELEASED](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcdab2d152bd84f659d4fc4060df29811b48),

[ 248](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcdaa8ff5629c002a61bc3bdf5baa2ebc203) [UART\_RX\_DISABLED](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcdaa8ff5629c002a61bc3bdf5baa2ebc203),

[ 254](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda05b81ddf74d208aeabace6ac90ae52dd) [UART\_RX\_STOPPED](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda05b81ddf74d208aeabace6ac90ae52dd),

255};

256

[ 258](structuart__event__tx.md)struct [uart\_event\_tx](structuart__event__tx.md) {

[ 260](structuart__event__tx.md#a314a676a4050b2438b6f41485656bdbd) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structuart__event__tx.md#a314a676a4050b2438b6f41485656bdbd);

[ 262](structuart__event__tx.md#a7d844b2c0833d24accf82d58ee3408ff) size\_t [len](structuart__event__tx.md#a7d844b2c0833d24accf82d58ee3408ff);

263};

264

[ 271](structuart__event__rx.md)struct [uart\_event\_rx](structuart__event__rx.md) {

[ 273](structuart__event__rx.md#a2d9dfa9d9b25ff976cf2e937c72eb245) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structuart__event__rx.md#a2d9dfa9d9b25ff976cf2e937c72eb245);

[ 275](structuart__event__rx.md#aa483e719298c30b9f5e6c57d3d161281) size\_t [offset](structuart__event__rx.md#aa483e719298c30b9f5e6c57d3d161281);

[ 277](structuart__event__rx.md#a96414b96e63503336f8cf0d2249cd3bd) size\_t [len](structuart__event__rx.md#a96414b96e63503336f8cf0d2249cd3bd);

278};

279

[ 281](structuart__event__rx__buf.md)struct [uart\_event\_rx\_buf](structuart__event__rx__buf.md) {

[ 283](structuart__event__rx__buf.md#a2547c84b742f454cfedf1de6d433297b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structuart__event__rx__buf.md#a2547c84b742f454cfedf1de6d433297b);

284};

285

[ 287](structuart__event__rx__stop.md)struct [uart\_event\_rx\_stop](structuart__event__rx__stop.md) {

[ 289](structuart__event__rx__stop.md#a96fbae85208d9b3ea0382e7e236a932d) enum [uart\_rx\_stop\_reason](group__uart__interface.md#gadeba6c5485e01dfc1c8a6e1c21668a88) [reason](structuart__event__rx__stop.md#a96fbae85208d9b3ea0382e7e236a932d);

[ 291](structuart__event__rx__stop.md#a1b361c8b7e17d1304a475235e734db48) struct [uart\_event\_rx](structuart__event__rx.md) [data](structuart__event__rx__stop.md#a1b361c8b7e17d1304a475235e734db48);

292};

293

[ 295](structuart__event.md)struct [uart\_event](structuart__event.md) {

[ 297](structuart__event.md#a2fb82a30e414a74943067cd0784f4b44) enum [uart\_event\_type](group__uart__async.md#gaf0c9513cbafa36d86b4c83f2b6a03dcd) [type](structuart__event.md#a2fb82a30e414a74943067cd0784f4b44);

[ 299](unionuart__event_1_1uart__event__data.md) union [uart\_event\_data](unionuart__event_1_1uart__event__data.md) {

[ 301](unionuart__event_1_1uart__event__data.md#a79fb6b799d5574c6aa38a211e020035f) struct [uart\_event\_tx](structuart__event__tx.md) [tx](unionuart__event_1_1uart__event__data.md#a79fb6b799d5574c6aa38a211e020035f);

[ 303](unionuart__event_1_1uart__event__data.md#afac00624290b8fe5cf7b59516567b972) struct [uart\_event\_rx](structuart__event__rx.md) [rx](unionuart__event_1_1uart__event__data.md#afac00624290b8fe5cf7b59516567b972);

[ 305](unionuart__event_1_1uart__event__data.md#ac03cdaeccba5f693337fa19299101863) struct [uart\_event\_rx\_buf](structuart__event__rx__buf.md) [rx\_buf](unionuart__event_1_1uart__event__data.md#ac03cdaeccba5f693337fa19299101863);

[ 307](unionuart__event_1_1uart__event__data.md#aad7488a2a3d91cea0ea874a08d7b88f6) struct [uart\_event\_rx\_stop](structuart__event__rx__stop.md) [rx\_stop](unionuart__event_1_1uart__event__data.md#aad7488a2a3d91cea0ea874a08d7b88f6);

[ 308](structuart__event.md#a07e3eebb7642ab52c73baba514704c69) } [data](structuart__event.md#a07e3eebb7642ab52c73baba514704c69);

309};

310

[ 320](group__uart__async.md#ga00b7c98a4da3ea3675d0a40c5dacb136)typedef void (\*[uart\_callback\_t](group__uart__async.md#ga00b7c98a4da3ea3675d0a40c5dacb136))(const struct [device](structdevice.md) \*dev,

321 struct [uart\_event](structuart__event.md) \*evt, void \*user\_data);

322

326

332

334\_\_subsystem struct uart\_driver\_api {

335

336#ifdef CONFIG\_UART\_ASYNC\_API

337

338 int (\*callback\_set)(const struct [device](structdevice.md) \*dev,

339 [uart\_callback\_t](group__uart__async.md#ga00b7c98a4da3ea3675d0a40c5dacb136) callback,

340 void \*user\_data);

341

342 int (\*tx)(const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t len,

343 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout);

344 int (\*tx\_abort)(const struct [device](structdevice.md) \*dev);

345

346 int (\*rx\_enable)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t len,

347 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout);

348 int (\*rx\_buf\_rsp)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t len);

349 int (\*rx\_disable)(const struct [device](structdevice.md) \*dev);

350

351#ifdef CONFIG\_UART\_WIDE\_DATA

352 int (\*tx\_u16)(const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*buf,

353 size\_t len, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout);

354 int (\*rx\_enable\_u16)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*buf,

355 size\_t len, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout);

356 int (\*rx\_buf\_rsp\_u16)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*buf,

357 size\_t len);

358#endif

359

360#endif

361

363 int (\*poll\_in)(const struct [device](structdevice.md) \*dev, unsigned char \*p\_char);

364 void (\*poll\_out)(const struct [device](structdevice.md) \*dev, unsigned char out\_char);

365

366#ifdef CONFIG\_UART\_WIDE\_DATA

367 int (\*poll\_in\_u16)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*p\_u16);

368 void (\*poll\_out\_u16)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) out\_u16);

369#endif

370

372 int (\*err\_check)(const struct [device](structdevice.md) \*dev);

373

374#ifdef CONFIG\_UART\_USE\_RUNTIME\_CONFIGURE

376 int (\*configure)(const struct [device](structdevice.md) \*dev,

377 const struct [uart\_config](structuart__config.md) \*cfg);

378 int (\*config\_get)(const struct [device](structdevice.md) \*dev, struct [uart\_config](structuart__config.md) \*cfg);

379#endif

380

381#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

382

384 int (\*fifo\_fill)(const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*tx\_data,

385 int len);

386

387#ifdef CONFIG\_UART\_WIDE\_DATA

388 int (\*fifo\_fill\_u16)(const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*tx\_data,

389 int len);

390#endif

391

393 int (\*fifo\_read)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rx\_data,

394 const int size);

395

396#ifdef CONFIG\_UART\_WIDE\_DATA

397 int (\*fifo\_read\_u16)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*rx\_data,

398 const int size);

399#endif

400

402 void (\*irq\_tx\_enable)(const struct [device](structdevice.md) \*dev);

403

405 void (\*irq\_tx\_disable)(const struct [device](structdevice.md) \*dev);

406

408 int (\*irq\_tx\_ready)(const struct [device](structdevice.md) \*dev);

409

411 void (\*irq\_rx\_enable)(const struct [device](structdevice.md) \*dev);

412

414 void (\*irq\_rx\_disable)(const struct [device](structdevice.md) \*dev);

415

417 int (\*irq\_tx\_complete)(const struct [device](structdevice.md) \*dev);

418

420 int (\*irq\_rx\_ready)(const struct [device](structdevice.md) \*dev);

421

423 void (\*irq\_err\_enable)(const struct [device](structdevice.md) \*dev);

424

426 void (\*irq\_err\_disable)(const struct [device](structdevice.md) \*dev);

427

429 int (\*irq\_is\_pending)(const struct [device](structdevice.md) \*dev);

430

432 int (\*irq\_update)(const struct [device](structdevice.md) \*dev);

433

435 void (\*irq\_callback\_set)(const struct [device](structdevice.md) \*dev,

436 [uart\_irq\_callback\_user\_data\_t](group__uart__interrupt.md#gad7a26b1a1d6212d7d39c05c8ad4ec926) cb,

437 void \*user\_data);

438

439#endif

440

441#ifdef CONFIG\_UART\_LINE\_CTRL

442 int (\*line\_ctrl\_set)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ctrl,

443 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val);

444 int (\*line\_ctrl\_get)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ctrl,

445 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*val);

446#endif

447

448#ifdef CONFIG\_UART\_DRV\_CMD

449 int (\*drv\_cmd)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) p);

450#endif

451

452};

453

455

[ 465](group__uart__interface.md#ga22ea20fd8e07153b3b71cc9416f5462f)\_\_syscall int [uart\_err\_check](group__uart__interface.md#ga22ea20fd8e07153b3b71cc9416f5462f)(const struct [device](structdevice.md) \*dev);

466

467static inline int z\_impl\_uart\_err\_check(const struct [device](structdevice.md) \*dev)

468{

469 const struct uart\_driver\_api \*api =

470 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

471

472 if (api->err\_check == NULL) {

473 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

474 }

475

476 return api->err\_check(dev);

477}

478

483

[ 502](group__uart__polling.md#gae81ac8cc976a20d774cfbda09e9c983d)\_\_syscall int [uart\_poll\_in](group__uart__polling.md#gae81ac8cc976a20d774cfbda09e9c983d)(const struct [device](structdevice.md) \*dev, unsigned char \*p\_char);

503

504static inline int z\_impl\_uart\_poll\_in(const struct [device](structdevice.md) \*dev,

505 unsigned char \*p\_char)

506{

507 const struct uart\_driver\_api \*api =

508 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

509

510 if (api->poll\_in == NULL) {

511 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

512 }

513

514 return api->poll\_in(dev, p\_char);

515}

516

[ 536](group__uart__polling.md#gaad39c1358019bfdcb919da7982743553)\_\_syscall int [uart\_poll\_in\_u16](group__uart__polling.md#gaad39c1358019bfdcb919da7982743553)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*p\_u16);

537

538static inline int z\_impl\_uart\_poll\_in\_u16(const struct [device](structdevice.md) \*dev,

539 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*p\_u16)

540{

541#ifdef CONFIG\_UART\_WIDE\_DATA

542 const struct uart\_driver\_api \*api =

543 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

544

545 if (api->poll\_in\_u16 == NULL) {

546 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

547 }

548

549 return api->poll\_in\_u16(dev, p\_u16);

550#else

551 ARG\_UNUSED(dev);

552 ARG\_UNUSED(p\_u16);

553 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

554#endif

555}

556

[ 571](group__uart__polling.md#ga06ba27ba772a7a18462b8cdbc7f9353c)\_\_syscall void [uart\_poll\_out](group__uart__polling.md#ga06ba27ba772a7a18462b8cdbc7f9353c)(const struct [device](structdevice.md) \*dev,

572 unsigned char out\_char);

573

574static inline void z\_impl\_uart\_poll\_out(const struct [device](structdevice.md) \*dev,

575 unsigned char out\_char)

576{

577 const struct uart\_driver\_api \*api =

578 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

579

580 api->poll\_out(dev, out\_char);

581}

582

[ 597](group__uart__polling.md#ga8faa3f58b9098c97e288e9c5f3367fd9)\_\_syscall void [uart\_poll\_out\_u16](group__uart__polling.md#ga8faa3f58b9098c97e288e9c5f3367fd9)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) out\_u16);

598

599static inline void z\_impl\_uart\_poll\_out\_u16(const struct [device](structdevice.md) \*dev,

600 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) out\_u16)

601{

602#ifdef CONFIG\_UART\_WIDE\_DATA

603 const struct uart\_driver\_api \*api =

604 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

605

606 api->poll\_out\_u16(dev, out\_u16);

607#else

608 ARG\_UNUSED(dev);

609 ARG\_UNUSED(out\_u16);

610#endif

611}

612

616

[ 631](group__uart__interface.md#gaa0b75777b879af10543f7e8f463ff9a2)\_\_syscall int [uart\_configure](group__uart__interface.md#gaa0b75777b879af10543f7e8f463ff9a2)(const struct [device](structdevice.md) \*dev,

632 const struct [uart\_config](structuart__config.md) \*cfg);

633

634static inline int z\_impl\_uart\_configure(const struct [device](structdevice.md) \*dev,

635 const struct [uart\_config](structuart__config.md) \*cfg)

636{

637#ifdef CONFIG\_UART\_USE\_RUNTIME\_CONFIGURE

638 const struct uart\_driver\_api \*api =

639 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

640

641 if (api->configure == NULL) {

642 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

643 }

644 return api->configure(dev, cfg);

645#else

646 ARG\_UNUSED(dev);

647 ARG\_UNUSED(cfg);

648 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

649#endif

650}

651

[ 666](group__uart__interface.md#ga81dfc5f2134de8e4acb5f063512cf703)\_\_syscall int [uart\_config\_get](group__uart__interface.md#ga81dfc5f2134de8e4acb5f063512cf703)(const struct [device](structdevice.md) \*dev,

667 struct [uart\_config](structuart__config.md) \*cfg);

668

669static inline int z\_impl\_uart\_config\_get(const struct [device](structdevice.md) \*dev,

670 struct [uart\_config](structuart__config.md) \*cfg)

671{

672#ifdef CONFIG\_UART\_USE\_RUNTIME\_CONFIGURE

673 const struct uart\_driver\_api \*api =

674 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

675

676 if (api->config\_get == NULL) {

677 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

678 }

679

680 return api->config\_get(dev, cfg);

681#else

682 ARG\_UNUSED(dev);

683 ARG\_UNUSED(cfg);

684 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

685#endif

686}

687

692

[ 713](group__uart__interrupt.md#gafe42e4719eada7e25904bc9ebfe87791)static inline int [uart\_fifo\_fill](group__uart__interrupt.md#gafe42e4719eada7e25904bc9ebfe87791)(const struct [device](structdevice.md) \*dev,

714 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*tx\_data,

715 int size)

716{

717#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

718 const struct uart\_driver\_api \*api =

719 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

720

721 if (api->fifo\_fill == NULL) {

722 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

723 }

724

725 return api->fifo\_fill(dev, tx\_data, size);

726#else

727 ARG\_UNUSED(dev);

728 ARG\_UNUSED(tx\_data);

729 ARG\_UNUSED(size);

730 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

731#endif

732}

733

[ 754](group__uart__interrupt.md#gaa89f58818d8428ad6a11abf692c54c0d)static inline int [uart\_fifo\_fill\_u16](group__uart__interrupt.md#gaa89f58818d8428ad6a11abf692c54c0d)(const struct [device](structdevice.md) \*dev,

755 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*tx\_data,

756 int size)

757{

758#if defined(CONFIG\_UART\_INTERRUPT\_DRIVEN) && defined(CONFIG\_UART\_WIDE\_DATA)

759 const struct uart\_driver\_api \*api =

760 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

761

762 if (api->fifo\_fill\_u16 == NULL) {

763 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

764 }

765

766 return api->fifo\_fill\_u16(dev, tx\_data, size);

767#else

768 ARG\_UNUSED(dev);

769 ARG\_UNUSED(tx\_data);

770 ARG\_UNUSED(size);

771 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

772#endif

773}

774

[ 796](group__uart__interrupt.md#gab10942076ac47ecff29e924098049398)static inline int [uart\_fifo\_read](group__uart__interrupt.md#gab10942076ac47ecff29e924098049398)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rx\_data,

797 const int size)

798{

799#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

800 const struct uart\_driver\_api \*api =

801 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

802

803 if (api->fifo\_read == NULL) {

804 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

805 }

806

807 return api->fifo\_read(dev, rx\_data, size);

808#else

809 ARG\_UNUSED(dev);

810 ARG\_UNUSED(rx\_data);

811 ARG\_UNUSED(size);

812 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

813#endif

814}

815

[ 837](group__uart__interrupt.md#ga4a3c25dad2290f1f40e4b847e3b83f64)static inline int [uart\_fifo\_read\_u16](group__uart__interrupt.md#ga4a3c25dad2290f1f40e4b847e3b83f64)(const struct [device](structdevice.md) \*dev,

838 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*rx\_data,

839 const int size)

840{

841#if defined(CONFIG\_UART\_INTERRUPT\_DRIVEN) && defined(CONFIG\_UART\_WIDE\_DATA)

842 const struct uart\_driver\_api \*api =

843 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

844

845 if (api->fifo\_read\_u16 == NULL) {

846 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

847 }

848

849 return api->fifo\_read\_u16(dev, rx\_data, size);

850#else

851 ARG\_UNUSED(dev);

852 ARG\_UNUSED(rx\_data);

853 ARG\_UNUSED(size);

854 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

855#endif

856}

857

[ 863](group__uart__interrupt.md#ga9cbd6e33dce6a5b06233cf10077e19cc)\_\_syscall void [uart\_irq\_tx\_enable](group__uart__interrupt.md#ga9cbd6e33dce6a5b06233cf10077e19cc)(const struct [device](structdevice.md) \*dev);

864

865static inline void z\_impl\_uart\_irq\_tx\_enable(const struct [device](structdevice.md) \*dev)

866{

867#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

868 const struct uart\_driver\_api \*api =

869 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

870

871 if (api->irq\_tx\_enable != NULL) {

872 api->irq\_tx\_enable(dev);

873 }

874#else

875 ARG\_UNUSED(dev);

876#endif

877}

878

[ 884](group__uart__interrupt.md#gaf8a5bc26cd7c32e7bc6516c6f873c45a)\_\_syscall void [uart\_irq\_tx\_disable](group__uart__interrupt.md#gaf8a5bc26cd7c32e7bc6516c6f873c45a)(const struct [device](structdevice.md) \*dev);

885

886static inline void z\_impl\_uart\_irq\_tx\_disable(const struct [device](structdevice.md) \*dev)

887{

888#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

889 const struct uart\_driver\_api \*api =

890 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

891

892 if (api->irq\_tx\_disable != NULL) {

893 api->irq\_tx\_disable(dev);

894 }

895#else

896 ARG\_UNUSED(dev);

897#endif

898}

899

[ 918](group__uart__interrupt.md#ga5e126b5f19549eb7f5b785b98ebe7638)static inline int [uart\_irq\_tx\_ready](group__uart__interrupt.md#ga5e126b5f19549eb7f5b785b98ebe7638)(const struct [device](structdevice.md) \*dev)

919{

920#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

921 const struct uart\_driver\_api \*api =

922 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

923

924 if (api->irq\_tx\_ready == NULL) {

925 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

926 }

927

928 return api->irq\_tx\_ready(dev);

929#else

930 ARG\_UNUSED(dev);

931 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

932#endif

933}

934

[ 940](group__uart__interrupt.md#ga4ec3ae3974da2b3ab94ae7b835d17bad)\_\_syscall void [uart\_irq\_rx\_enable](group__uart__interrupt.md#ga4ec3ae3974da2b3ab94ae7b835d17bad)(const struct [device](structdevice.md) \*dev);

941

942static inline void z\_impl\_uart\_irq\_rx\_enable(const struct [device](structdevice.md) \*dev)

943{

944#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

945 const struct uart\_driver\_api \*api =

946 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

947

948 if (api->irq\_rx\_enable != NULL) {

949 api->irq\_rx\_enable(dev);

950 }

951#else

952 ARG\_UNUSED(dev);

953#endif

954}

955

[ 961](group__uart__interrupt.md#gaa759d7935fdd9ab6ca0761f161389a29)\_\_syscall void [uart\_irq\_rx\_disable](group__uart__interrupt.md#gaa759d7935fdd9ab6ca0761f161389a29)(const struct [device](structdevice.md) \*dev);

962

963static inline void z\_impl\_uart\_irq\_rx\_disable(const struct [device](structdevice.md) \*dev)

964{

965#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

966 const struct uart\_driver\_api \*api =

967 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

968

969 if (api->irq\_rx\_disable != NULL) {

970 api->irq\_rx\_disable(dev);

971 }

972#else

973 ARG\_UNUSED(dev);

974#endif

975}

976

[ 996](group__uart__interrupt.md#ga917935a13bf6a5d1e32ef34339e96455)static inline int [uart\_irq\_tx\_complete](group__uart__interrupt.md#ga917935a13bf6a5d1e32ef34339e96455)(const struct [device](structdevice.md) \*dev)

997{

998#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

999 const struct uart\_driver\_api \*api =

1000 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1001

1002 if (api->irq\_tx\_complete == NULL) {

1003 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1004 }

1005 return api->irq\_tx\_complete(dev);

1006#else

1007 ARG\_UNUSED(dev);

1008 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

1009#endif

1010}

1011

[ 1032](group__uart__interrupt.md#gad04073b1b8e3de13b43ae1194561377b)static inline int [uart\_irq\_rx\_ready](group__uart__interrupt.md#gad04073b1b8e3de13b43ae1194561377b)(const struct [device](structdevice.md) \*dev)

1033{

1034#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

1035 const struct uart\_driver\_api \*api =

1036 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1037

1038 if (api->irq\_rx\_ready == NULL) {

1039 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1040 }

1041 return api->irq\_rx\_ready(dev);

1042#else

1043 ARG\_UNUSED(dev);

1044 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

1045#endif

1046}

1047

[ 1052](group__uart__interrupt.md#ga7c24daae3326bc2959ea13a2be79969f)\_\_syscall void [uart\_irq\_err\_enable](group__uart__interrupt.md#ga7c24daae3326bc2959ea13a2be79969f)(const struct [device](structdevice.md) \*dev);

1053

1054static inline void z\_impl\_uart\_irq\_err\_enable(const struct [device](structdevice.md) \*dev)

1055{

1056#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

1057 const struct uart\_driver\_api \*api =

1058 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1059

1060 if (api->irq\_err\_enable) {

1061 api->irq\_err\_enable(dev);

1062 }

1063#else

1064 ARG\_UNUSED(dev);

1065#endif

1066}

1067

[ 1073](group__uart__interrupt.md#gaaf8a88361807e204f7227fbd1d0e75b2)\_\_syscall void [uart\_irq\_err\_disable](group__uart__interrupt.md#gaaf8a88361807e204f7227fbd1d0e75b2)(const struct [device](structdevice.md) \*dev);

1074

1075static inline void z\_impl\_uart\_irq\_err\_disable(const struct [device](structdevice.md) \*dev)

1076{

1077#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

1078 const struct uart\_driver\_api \*api =

1079 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1080

1081 if (api->irq\_err\_disable) {

1082 api->irq\_err\_disable(dev);

1083 }

1084#else

1085 ARG\_UNUSED(dev);

1086#endif

1087}

1088

[ 1099](group__uart__interrupt.md#ga11ccae917c8b5fd76aaabdb047125f6a)\_\_syscall int [uart\_irq\_is\_pending](group__uart__interrupt.md#ga11ccae917c8b5fd76aaabdb047125f6a)(const struct [device](structdevice.md) \*dev);

1100

1101static inline int z\_impl\_uart\_irq\_is\_pending(const struct [device](structdevice.md) \*dev)

1102{

1103#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

1104 const struct uart\_driver\_api \*api =

1105 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1106

1107 if (api->irq\_is\_pending == NULL) {

1108 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1109 }

1110 return api->irq\_is\_pending(dev);

1111#else

1112 ARG\_UNUSED(dev);

1113 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

1114#endif

1115}

1116

[ 1142](group__uart__interrupt.md#gac5241e000d482c40b2a4856c58c106a6)\_\_syscall int [uart\_irq\_update](group__uart__interrupt.md#gac5241e000d482c40b2a4856c58c106a6)(const struct [device](structdevice.md) \*dev);

1143

1144static inline int z\_impl\_uart\_irq\_update(const struct [device](structdevice.md) \*dev)

1145{

1146#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

1147 const struct uart\_driver\_api \*api =

1148 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1149

1150 if (api->irq\_update == NULL) {

1151 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1152 }

1153 return api->irq\_update(dev);

1154#else

1155 ARG\_UNUSED(dev);

1156 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

1157#endif

1158}

1159

[ 1175](group__uart__interrupt.md#gaf469966a56d1fc9f50108201597ee0a0)static inline int [uart\_irq\_callback\_user\_data\_set](group__uart__interrupt.md#gaf469966a56d1fc9f50108201597ee0a0)(const struct [device](structdevice.md) \*dev,

1176 [uart\_irq\_callback\_user\_data\_t](group__uart__interrupt.md#gad7a26b1a1d6212d7d39c05c8ad4ec926) cb,

1177 void \*user\_data)

1178{

1179#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

1180 const struct uart\_driver\_api \*api =

1181 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1182

1183 if ((api != NULL) && (api->irq\_callback\_set != NULL)) {

1184 api->irq\_callback\_set(dev, cb, user\_data);

1185 return 0;

1186 } else {

1187 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1188 }

1189#else

1190 ARG\_UNUSED(dev);

1191 ARG\_UNUSED(cb);

1192 ARG\_UNUSED(user\_data);

1193 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

1194#endif

1195}

1196

[ 1210](group__uart__interrupt.md#ga5f7af3f7f0d9155349ea3b4fad78956c)static inline int [uart\_irq\_callback\_set](group__uart__interrupt.md#ga5f7af3f7f0d9155349ea3b4fad78956c)(const struct [device](structdevice.md) \*dev,

1211 [uart\_irq\_callback\_user\_data\_t](group__uart__interrupt.md#gad7a26b1a1d6212d7d39c05c8ad4ec926) cb)

1212{

1213 return [uart\_irq\_callback\_user\_data\_set](group__uart__interrupt.md#gaf469966a56d1fc9f50108201597ee0a0)(dev, cb, NULL);

1214}

1215

1219

1224

[ 1240](group__uart__async.md#gad33e627ed8729409b14e92453e53459c)static inline int [uart\_callback\_set](group__uart__async.md#gad33e627ed8729409b14e92453e53459c)(const struct [device](structdevice.md) \*dev,

1241 [uart\_callback\_t](group__uart__async.md#ga00b7c98a4da3ea3675d0a40c5dacb136) callback,

1242 void \*user\_data)

1243{

1244#ifdef CONFIG\_UART\_ASYNC\_API

1245 const struct uart\_driver\_api \*api =

1246 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1247

1248 if (api->callback\_set == NULL) {

1249 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1250 }

1251

1252 return api->callback\_set(dev, callback, user\_data);

1253#else

1254 ARG\_UNUSED(dev);

1255 ARG\_UNUSED(callback);

1256 ARG\_UNUSED(user\_data);

1257 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

1258#endif

1259}

1260

[ 1278](group__uart__async.md#gaf99f32ce2e2d9beb32a2f2e5a26320dc)\_\_syscall int [uart\_tx](group__uart__async.md#gaf99f32ce2e2d9beb32a2f2e5a26320dc)(const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf,

1279 size\_t len,

1280 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout);

1281

1282static inline int z\_impl\_uart\_tx(const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf,

1283 size\_t len, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout)

1284

1285{

1286#ifdef CONFIG\_UART\_ASYNC\_API

1287 const struct uart\_driver\_api \*api =

1288 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1289

1290 return api->tx(dev, buf, len, timeout);

1291#else

1292 ARG\_UNUSED(dev);

1293 ARG\_UNUSED(buf);

1294 ARG\_UNUSED(len);

1295 ARG\_UNUSED(timeout);

1296 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

1297#endif

1298}

1299

[ 1317](group__uart__async.md#gab0ea611cd072fa459a6f1780ce62c9e3)\_\_syscall int [uart\_tx\_u16](group__uart__async.md#gab0ea611cd072fa459a6f1780ce62c9e3)(const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*buf,

1318 size\_t len, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout);

1319

1320static inline int z\_impl\_uart\_tx\_u16(const struct [device](structdevice.md) \*dev,

1321 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*buf,

1322 size\_t len, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout)

1323

1324{

1325#if defined(CONFIG\_UART\_ASYNC\_API) && defined(CONFIG\_UART\_WIDE\_DATA)

1326 const struct uart\_driver\_api \*api =

1327 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1328

1329 return api->tx\_u16(dev, buf, len, timeout);

1330#else

1331 ARG\_UNUSED(dev);

1332 ARG\_UNUSED(buf);

1333 ARG\_UNUSED(len);

1334 ARG\_UNUSED(timeout);

1335 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

1336#endif

1337}

1338

[ 1351](group__uart__async.md#gaa8a26d3ea685fb98030ea03613be6280)\_\_syscall int [uart\_tx\_abort](group__uart__async.md#gaa8a26d3ea685fb98030ea03613be6280)(const struct [device](structdevice.md) \*dev);

1352

1353static inline int z\_impl\_uart\_tx\_abort(const struct [device](structdevice.md) \*dev)

1354{

1355#ifdef CONFIG\_UART\_ASYNC\_API

1356 const struct uart\_driver\_api \*api =

1357 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1358

1359 return api->tx\_abort(dev);

1360#else

1361 ARG\_UNUSED(dev);

1362 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

1363#endif

1364}

1365

[ 1387](group__uart__async.md#ga902e18c2a727ed2988e1b6caa6a444b8)\_\_syscall int [uart\_rx\_enable](group__uart__async.md#ga902e18c2a727ed2988e1b6caa6a444b8)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf,

1388 size\_t len,

1389 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout);

1390

1391static inline int z\_impl\_uart\_rx\_enable(const struct [device](structdevice.md) \*dev,

1392 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf,

1393 size\_t len, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout)

1394{

1395#ifdef CONFIG\_UART\_ASYNC\_API

1396 const struct uart\_driver\_api \*api =

1397 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1398

1399 return api->rx\_enable(dev, buf, len, timeout);

1400#else

1401 ARG\_UNUSED(dev);

1402 ARG\_UNUSED(buf);

1403 ARG\_UNUSED(len);

1404 ARG\_UNUSED(timeout);

1405 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

1406#endif

1407}

1408

[ 1430](group__uart__async.md#ga12d91846133351a85fa471fa90f2a0fd)\_\_syscall int [uart\_rx\_enable\_u16](group__uart__async.md#ga12d91846133351a85fa471fa90f2a0fd)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*buf,

1431 size\_t len, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout);

1432

1433static inline int z\_impl\_uart\_rx\_enable\_u16(const struct [device](structdevice.md) \*dev,

1434 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*buf, size\_t len,

1435 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout)

1436{

1437#if defined(CONFIG\_UART\_ASYNC\_API) && defined(CONFIG\_UART\_WIDE\_DATA)

1438 const struct uart\_driver\_api \*api =

1439 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1440

1441 return api->rx\_enable\_u16(dev, buf, len, timeout);

1442#else

1443 ARG\_UNUSED(dev);

1444 ARG\_UNUSED(buf);

1445 ARG\_UNUSED(len);

1446 ARG\_UNUSED(timeout);

1447 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

1448#endif

1449}

1450

[ 1471](group__uart__async.md#ga3970fe2818e214b0814ea8b73a816a6a)static inline int [uart\_rx\_buf\_rsp](group__uart__async.md#ga3970fe2818e214b0814ea8b73a816a6a)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf,

1472 size\_t len)

1473{

1474#ifdef CONFIG\_UART\_ASYNC\_API

1475 const struct uart\_driver\_api \*api =

1476 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1477

1478 return api->rx\_buf\_rsp(dev, buf, len);

1479#else

1480 ARG\_UNUSED(dev);

1481 ARG\_UNUSED(buf);

1482 ARG\_UNUSED(len);

1483 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

1484#endif

1485}

1486

[ 1508](group__uart__async.md#ga778bcfc30be853c8d320f295b34c17c0)static inline int [uart\_rx\_buf\_rsp\_u16](group__uart__async.md#ga778bcfc30be853c8d320f295b34c17c0)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*buf,

1509 size\_t len)

1510{

1511#if defined(CONFIG\_UART\_ASYNC\_API) && defined(CONFIG\_UART\_WIDE\_DATA)

1512 const struct uart\_driver\_api \*api =

1513 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1514

1515 return api->rx\_buf\_rsp\_u16(dev, buf, len);

1516#else

1517 ARG\_UNUSED(dev);

1518 ARG\_UNUSED(buf);

1519 ARG\_UNUSED(len);

1520 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

1521#endif

1522}

1523

[ 1539](group__uart__async.md#gafd4753bee51b230091a3c6ddb26ea734)\_\_syscall int [uart\_rx\_disable](group__uart__async.md#gafd4753bee51b230091a3c6ddb26ea734)(const struct [device](structdevice.md) \*dev);

1540

1541static inline int z\_impl\_uart\_rx\_disable(const struct [device](structdevice.md) \*dev)

1542{

1543#ifdef CONFIG\_UART\_ASYNC\_API

1544 const struct uart\_driver\_api \*api =

1545 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1546

1547 return api->rx\_disable(dev);

1548#else

1549 ARG\_UNUSED(dev);

1550 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

1551#endif

1552}

1553

1557

[ 1570](group__uart__interface.md#gab039414b41145dc8d31349836da91263)\_\_syscall int [uart\_line\_ctrl\_set](group__uart__interface.md#gab039414b41145dc8d31349836da91263)(const struct [device](structdevice.md) \*dev,

1571 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ctrl, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val);

1572

1573static inline int z\_impl\_uart\_line\_ctrl\_set(const struct [device](structdevice.md) \*dev,

1574 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ctrl, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val)

1575{

1576#ifdef CONFIG\_UART\_LINE\_CTRL

1577 const struct uart\_driver\_api \*api =

1578 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1579

1580 if (api->line\_ctrl\_set == NULL) {

1581 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1582 }

1583 return api->line\_ctrl\_set(dev, ctrl, val);

1584#else

1585 ARG\_UNUSED(dev);

1586 ARG\_UNUSED(ctrl);

1587 ARG\_UNUSED(val);

1588 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

1589#endif

1590}

1591

[ 1604](group__uart__interface.md#gafda8a550284a54c8e1d6b6638de978e5)\_\_syscall int [uart\_line\_ctrl\_get](group__uart__interface.md#gafda8a550284a54c8e1d6b6638de978e5)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ctrl,

1605 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*val);

1606

1607static inline int z\_impl\_uart\_line\_ctrl\_get(const struct [device](structdevice.md) \*dev,

1608 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ctrl, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*val)

1609{

1610#ifdef CONFIG\_UART\_LINE\_CTRL

1611 const struct uart\_driver\_api \*api =

1612 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1613

1614 if (api->line\_ctrl\_get == NULL) {

1615 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1616 }

1617 return api->line\_ctrl\_get(dev, ctrl, val);

1618#else

1619 ARG\_UNUSED(dev);

1620 ARG\_UNUSED(ctrl);

1621 ARG\_UNUSED(val);

1622 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

1623#endif

1624}

1625

[ 1641](group__uart__interface.md#gaa8683398e5d709b513509d08841ed51b)\_\_syscall int [uart\_drv\_cmd](group__uart__interface.md#gaa8683398e5d709b513509d08841ed51b)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) p);

1642

1643static inline int z\_impl\_uart\_drv\_cmd(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),

1644 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) p)

1645{

1646#ifdef CONFIG\_UART\_DRV\_CMD

1647 const struct uart\_driver\_api \*api =

1648 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1649

1650 if (api->drv\_cmd == NULL) {

1651 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1652 }

1653 return api->drv\_cmd(dev, [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), p);

1654#else

1655 ARG\_UNUSED(dev);

1656 ARG\_UNUSED([cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615));

1657 ARG\_UNUSED(p);

1658 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

1659#endif

1660}

1661

1662#ifdef \_\_cplusplus

1663}

1664#endif

1665

1669

1670#include <syscalls/uart.h>

1671

1672#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_UART\_H\_ \*/

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)

static void cmd(uint32\_t command)

Execute a display list command by co-processor engine.

**Definition** ft8xx\_reference\_api.h:153

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:83

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:115

[uart\_callback\_t](group__uart__async.md#ga00b7c98a4da3ea3675d0a40c5dacb136)

void(\* uart\_callback\_t)(const struct device \*dev, struct uart\_event \*evt, void \*user\_data)

Define the application callback function signature for uart\_callback\_set() function.

**Definition** uart.h:320

[uart\_rx\_enable\_u16](group__uart__async.md#ga12d91846133351a85fa471fa90f2a0fd)

int uart\_rx\_enable\_u16(const struct device \*dev, uint16\_t \*buf, size\_t len, int32\_t timeout)

Start receiving wide data through UART.

[uart\_rx\_buf\_rsp](group__uart__async.md#ga3970fe2818e214b0814ea8b73a816a6a)

static int uart\_rx\_buf\_rsp(const struct device \*dev, uint8\_t \*buf, size\_t len)

Provide receive buffer in response to UART\_RX\_BUF\_REQUEST event.

**Definition** uart.h:1471

[uart\_rx\_buf\_rsp\_u16](group__uart__async.md#ga778bcfc30be853c8d320f295b34c17c0)

static int uart\_rx\_buf\_rsp\_u16(const struct device \*dev, uint16\_t \*buf, size\_t len)

Provide wide data receive buffer in response to UART\_RX\_BUF\_REQUEST event.

**Definition** uart.h:1508

[uart\_rx\_enable](group__uart__async.md#ga902e18c2a727ed2988e1b6caa6a444b8)

int uart\_rx\_enable(const struct device \*dev, uint8\_t \*buf, size\_t len, int32\_t timeout)

Start receiving data through UART.

[uart\_tx\_abort](group__uart__async.md#gaa8a26d3ea685fb98030ea03613be6280)

int uart\_tx\_abort(const struct device \*dev)

Abort current TX transmission.

[uart\_tx\_u16](group__uart__async.md#gab0ea611cd072fa459a6f1780ce62c9e3)

int uart\_tx\_u16(const struct device \*dev, const uint16\_t \*buf, size\_t len, int32\_t timeout)

Send given number of datum from buffer through UART.

[uart\_callback\_set](group__uart__async.md#gad33e627ed8729409b14e92453e53459c)

static int uart\_callback\_set(const struct device \*dev, uart\_callback\_t callback, void \*user\_data)

Set event handler function.

**Definition** uart.h:1240

[uart\_event\_type](group__uart__async.md#gaf0c9513cbafa36d86b4c83f2b6a03dcd)

uart\_event\_type

Types of events passed to callback in UART\_ASYNC\_API.

**Definition** uart.h:203

[uart\_tx](group__uart__async.md#gaf99f32ce2e2d9beb32a2f2e5a26320dc)

int uart\_tx(const struct device \*dev, const uint8\_t \*buf, size\_t len, int32\_t timeout)

Send given number of bytes from buffer through UART.

[uart\_rx\_disable](group__uart__async.md#gafd4753bee51b230091a3c6ddb26ea734)

int uart\_rx\_disable(const struct device \*dev)

Disable RX.

[UART\_RX\_STOPPED](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda05b81ddf74d208aeabace6ac90ae52dd)

@ UART\_RX\_STOPPED

RX has stopped due to external event.

**Definition** uart.h:254

[UART\_TX\_ABORTED](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0abcf565ba1011815285bb3845f8d5a1)

@ UART\_TX\_ABORTED

Transmitting aborted due to timeout or uart\_tx\_abort call.

**Definition** uart.h:213

[UART\_RX\_BUF\_REQUEST](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0d250f372702526f1bce6d4dfe166abe)

@ UART\_RX\_BUF\_REQUEST

Driver requests next buffer for continuous reception.

**Definition** uart.h:236

[UART\_TX\_DONE](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda4b5cdf863d8b6e5cd7b58f611808a6e4)

@ UART\_TX\_DONE

Whole TX buffer was transmitted.

**Definition** uart.h:205

[UART\_RX\_RDY](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7)

@ UART\_RX\_RDY

Received data is ready for processing.

**Definition** uart.h:224

[UART\_RX\_DISABLED](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcdaa8ff5629c002a61bc3bdf5baa2ebc203)

@ UART\_RX\_DISABLED

RX has been disabled and can be reenabled.

**Definition** uart.h:248

[UART\_RX\_BUF\_RELEASED](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcdab2d152bd84f659d4fc4060df29811b48)

@ UART\_RX\_BUF\_RELEASED

Buffer is no longer used by UART driver.

**Definition** uart.h:240

[uart\_line\_ctrl](group__uart__interface.md#ga02552532e171e789efc1b000917a9be0)

uart\_line\_ctrl

Line control signals.

**Definition** uart.h:33

[uart\_err\_check](group__uart__interface.md#ga22ea20fd8e07153b3b71cc9416f5462f)

int uart\_err\_check(const struct device \*dev)

Check whether an error was detected.

[uart\_config\_get](group__uart__interface.md#ga81dfc5f2134de8e4acb5f063512cf703)

int uart\_config\_get(const struct device \*dev, struct uart\_config \*cfg)

Get UART configuration.

[uart\_config\_flow\_control](group__uart__interface.md#ga8e2f1b4a8d60d7a6c24835d1b26f99e8)

uart\_config\_flow\_control

Hardware flow control options.

**Definition** uart.h:109

[uart\_configure](group__uart__interface.md#gaa0b75777b879af10543f7e8f463ff9a2)

int uart\_configure(const struct device \*dev, const struct uart\_config \*cfg)

Set UART configuration.

[uart\_drv\_cmd](group__uart__interface.md#gaa8683398e5d709b513509d08841ed51b)

int uart\_drv\_cmd(const struct device \*dev, uint32\_t cmd, uint32\_t p)

Send extra command to driver.

[uart\_line\_ctrl\_set](group__uart__interface.md#gab039414b41145dc8d31349836da91263)

int uart\_line\_ctrl\_set(const struct device \*dev, uint32\_t ctrl, uint32\_t val)

Manipulate line control for UART.

[uart\_config\_parity](group__uart__interface.md#gab2ab6aacb6e3c43bb26d4274157e5711)

uart\_config\_parity

Parity modes.

**Definition** uart.h:77

[uart\_config\_data\_bits](group__uart__interface.md#gab9f7de744a68a311330576d7da02c44a)

uart\_config\_data\_bits

Number of data bits.

**Definition** uart.h:94

[uart\_rx\_stop\_reason](group__uart__interface.md#gadeba6c5485e01dfc1c8a6e1c21668a88)

uart\_rx\_stop\_reason

Reception stop reasons.

**Definition** uart.h:47

[uart\_config\_stop\_bits](group__uart__interface.md#gafc1aecb863e2456d73b78a49fcbad72e)

uart\_config\_stop\_bits

Number of stop bits.

**Definition** uart.h:86

[uart\_line\_ctrl\_get](group__uart__interface.md#gafda8a550284a54c8e1d6b6638de978e5)

int uart\_line\_ctrl\_get(const struct device \*dev, uint32\_t ctrl, uint32\_t \*val)

Retrieve line control for UART.

[UART\_LINE\_CTRL\_DTR](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a19e76af9901fc0274a9e27ff40e29e23)

@ UART\_LINE\_CTRL\_DTR

Data Terminal Ready (DTR).

**Definition** uart.h:36

[UART\_LINE\_CTRL\_RTS](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a205d22bd797ab1c55323dc1ffda75f0d)

@ UART\_LINE\_CTRL\_RTS

Request To Send (RTS).

**Definition** uart.h:35

[UART\_LINE\_CTRL\_BAUD\_RATE](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a3fdd02679f4f103190f3c12ab3cda00b)

@ UART\_LINE\_CTRL\_BAUD\_RATE

Baud rate.

**Definition** uart.h:34

[UART\_LINE\_CTRL\_DCD](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a6d2c438044dd64f5cef07bbe4c6b3e97)

@ UART\_LINE\_CTRL\_DCD

Data Carrier Detect (DCD).

**Definition** uart.h:37

[UART\_LINE\_CTRL\_DSR](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a87d8bedb5c918c182b271884ee42d75c)

@ UART\_LINE\_CTRL\_DSR

Data Set Ready (DSR).

**Definition** uart.h:38

[UART\_CFG\_FLOW\_CTRL\_DTR\_DSR](group__uart__interface.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a0efc5de86bf80119f750cf372814309f)

@ UART\_CFG\_FLOW\_CTRL\_DTR\_DSR

DTR/DSR flow control.

**Definition** uart.h:112

[UART\_CFG\_FLOW\_CTRL\_NONE](group__uart__interface.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a546b28db6f8bfc26266e8f7d6b8ff973)

@ UART\_CFG\_FLOW\_CTRL\_NONE

No flow control.

**Definition** uart.h:110

[UART\_CFG\_FLOW\_CTRL\_RS485](group__uart__interface.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a9675cc80d44e980b66e99bc8548f085c)

@ UART\_CFG\_FLOW\_CTRL\_RS485

RS485 flow control.

**Definition** uart.h:113

[UART\_CFG\_FLOW\_CTRL\_RTS\_CTS](group__uart__interface.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8ad682bfe14a9f0860d1fdc3e8e9d56f86)

@ UART\_CFG\_FLOW\_CTRL\_RTS\_CTS

RTS/CTS flow control.

**Definition** uart.h:111

[UART\_CFG\_PARITY\_MARK](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711a5ee61c29a32447644ff70385158a11ca)

@ UART\_CFG\_PARITY\_MARK

Mark parity.

**Definition** uart.h:81

[UART\_CFG\_PARITY\_NONE](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711a6a23a2ef22fb3b144648b244fff82b8d)

@ UART\_CFG\_PARITY\_NONE

No parity.

**Definition** uart.h:78

[UART\_CFG\_PARITY\_ODD](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711a8a618b0a531c8d62809e39eb56eaf5ed)

@ UART\_CFG\_PARITY\_ODD

Odd parity.

**Definition** uart.h:79

[UART\_CFG\_PARITY\_SPACE](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711a8dc5306c8ca26321431bcf22ce9b036c)

@ UART\_CFG\_PARITY\_SPACE

Space parity.

**Definition** uart.h:82

[UART\_CFG\_PARITY\_EVEN](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711ac3a4310efe198a1fa7d977a5531486ba)

@ UART\_CFG\_PARITY\_EVEN

Even parity.

**Definition** uart.h:80

[UART\_CFG\_DATA\_BITS\_5](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aa1b0545c2d1970e67d697b62510bfbe27)

@ UART\_CFG\_DATA\_BITS\_5

5 data bits

**Definition** uart.h:95

[UART\_CFG\_DATA\_BITS\_8](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aa23f55bdb24b4016c8c23c518e981df97)

@ UART\_CFG\_DATA\_BITS\_8

8 data bits

**Definition** uart.h:98

[UART\_CFG\_DATA\_BITS\_7](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aa6120eb8f668b257c8c2dd0dc9cf0c913)

@ UART\_CFG\_DATA\_BITS\_7

7 data bits

**Definition** uart.h:97

[UART\_CFG\_DATA\_BITS\_6](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aac6e0f3c0479164c34144d0e6e28298e4)

@ UART\_CFG\_DATA\_BITS\_6

6 data bits

**Definition** uart.h:96

[UART\_CFG\_DATA\_BITS\_9](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aaf3b601af696d8841fe79871ca3e41e5f)

@ UART\_CFG\_DATA\_BITS\_9

9 data bits

**Definition** uart.h:99

[UART\_ERROR\_NOISE](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a412058adbf7668b7051efb8419984d60)

@ UART\_ERROR\_NOISE

Noise error.

**Definition** uart.h:73

[UART\_ERROR\_OVERRUN](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a442beffc51cdf265bbcb40810a9a6e54)

@ UART\_ERROR\_OVERRUN

Overrun error.

**Definition** uart.h:49

[UART\_BREAK](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a4986147e23cc46ab8c2aa7e151d09571)

@ UART\_BREAK

Break interrupt.

**Definition** uart.h:61

[UART\_ERROR\_PARITY](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a86d38eac5a46e6659aa765164b833eb5)

@ UART\_ERROR\_PARITY

Parity error.

**Definition** uart.h:51

[UART\_ERROR\_COLLISION](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88aad8ca4dca9a846560293df71e6b39786)

@ UART\_ERROR\_COLLISION

Collision error.

**Definition** uart.h:71

[UART\_ERROR\_FRAMING](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88af13f72a8c615b4bc570b5a4df573407b)

@ UART\_ERROR\_FRAMING

Framing error.

**Definition** uart.h:53

[UART\_CFG\_STOP\_BITS\_1\_5](group__uart__interface.md#ggafc1aecb863e2456d73b78a49fcbad72ea1da47ec95b6a6eee65abef3d6d84f9ad)

@ UART\_CFG\_STOP\_BITS\_1\_5

1.5 stop bits

**Definition** uart.h:89

[UART\_CFG\_STOP\_BITS\_0\_5](group__uart__interface.md#ggafc1aecb863e2456d73b78a49fcbad72ea308c660590a9fd16143806e8bef002af)

@ UART\_CFG\_STOP\_BITS\_0\_5

0.5 stop bit

**Definition** uart.h:87

[UART\_CFG\_STOP\_BITS\_1](group__uart__interface.md#ggafc1aecb863e2456d73b78a49fcbad72ea73024f1618eb04385bf488214c635e58)

@ UART\_CFG\_STOP\_BITS\_1

1 stop bit

**Definition** uart.h:88

[UART\_CFG\_STOP\_BITS\_2](group__uart__interface.md#ggafc1aecb863e2456d73b78a49fcbad72eae180ecebc76516e89669e1d16bfb31c6)

@ UART\_CFG\_STOP\_BITS\_2

2 stop bits

**Definition** uart.h:90

[uart\_irq\_is\_pending](group__uart__interrupt.md#ga11ccae917c8b5fd76aaabdb047125f6a)

int uart\_irq\_is\_pending(const struct device \*dev)

Check if any IRQs is pending.

[uart\_fifo\_read\_u16](group__uart__interrupt.md#ga4a3c25dad2290f1f40e4b847e3b83f64)

static int uart\_fifo\_read\_u16(const struct device \*dev, uint16\_t \*rx\_data, const int size)

Read wide data from FIFO.

**Definition** uart.h:837

[uart\_irq\_rx\_enable](group__uart__interrupt.md#ga4ec3ae3974da2b3ab94ae7b835d17bad)

void uart\_irq\_rx\_enable(const struct device \*dev)

Enable RX interrupt.

[uart\_irq\_tx\_ready](group__uart__interrupt.md#ga5e126b5f19549eb7f5b785b98ebe7638)

static int uart\_irq\_tx\_ready(const struct device \*dev)

Check if UART TX buffer can accept a new char.

**Definition** uart.h:918

[uart\_irq\_callback\_set](group__uart__interrupt.md#ga5f7af3f7f0d9155349ea3b4fad78956c)

static int uart\_irq\_callback\_set(const struct device \*dev, uart\_irq\_callback\_user\_data\_t cb)

Set the IRQ callback function pointer (legacy).

**Definition** uart.h:1210

[uart\_irq\_config\_func\_t](group__uart__interrupt.md#ga6750414923953c84fb1e19177ec74ae0)

void(\* uart\_irq\_config\_func\_t)(const struct device \*dev)

For configuring IRQ on each individual UART device.

**Definition** uart.h:147

[uart\_irq\_err\_enable](group__uart__interrupt.md#ga7c24daae3326bc2959ea13a2be79969f)

void uart\_irq\_err\_enable(const struct device \*dev)

Enable error interrupt.

[uart\_irq\_tx\_complete](group__uart__interrupt.md#ga917935a13bf6a5d1e32ef34339e96455)

static int uart\_irq\_tx\_complete(const struct device \*dev)

Check if UART TX block finished transmission.

**Definition** uart.h:996

[uart\_irq\_tx\_enable](group__uart__interrupt.md#ga9cbd6e33dce6a5b06233cf10077e19cc)

void uart\_irq\_tx\_enable(const struct device \*dev)

Enable TX interrupt in IER.

[uart\_irq\_rx\_disable](group__uart__interrupt.md#gaa759d7935fdd9ab6ca0761f161389a29)

void uart\_irq\_rx\_disable(const struct device \*dev)

Disable RX interrupt.

[uart\_fifo\_fill\_u16](group__uart__interrupt.md#gaa89f58818d8428ad6a11abf692c54c0d)

static int uart\_fifo\_fill\_u16(const struct device \*dev, const uint16\_t \*tx\_data, int size)

Fill FIFO with wide data.

**Definition** uart.h:754

[uart\_irq\_err\_disable](group__uart__interrupt.md#gaaf8a88361807e204f7227fbd1d0e75b2)

void uart\_irq\_err\_disable(const struct device \*dev)

Disable error interrupt.

[uart\_fifo\_read](group__uart__interrupt.md#gab10942076ac47ecff29e924098049398)

static int uart\_fifo\_read(const struct device \*dev, uint8\_t \*rx\_data, const int size)

Read data from FIFO.

**Definition** uart.h:796

[uart\_irq\_update](group__uart__interrupt.md#gac5241e000d482c40b2a4856c58c106a6)

int uart\_irq\_update(const struct device \*dev)

Start processing interrupts in ISR.

[uart\_irq\_rx\_ready](group__uart__interrupt.md#gad04073b1b8e3de13b43ae1194561377b)

static int uart\_irq\_rx\_ready(const struct device \*dev)

Check if UART RX buffer has a received char.

**Definition** uart.h:1032

[uart\_irq\_callback\_user\_data\_t](group__uart__interrupt.md#gad7a26b1a1d6212d7d39c05c8ad4ec926)

void(\* uart\_irq\_callback\_user\_data\_t)(const struct device \*dev, void \*user\_data)

Define the application callback function signature for uart\_irq\_callback\_user\_data\_set() function.

**Definition** uart.h:139

[uart\_irq\_callback\_user\_data\_set](group__uart__interrupt.md#gaf469966a56d1fc9f50108201597ee0a0)

static int uart\_irq\_callback\_user\_data\_set(const struct device \*dev, uart\_irq\_callback\_user\_data\_t cb, void \*user\_data)

Set the IRQ callback function pointer.

**Definition** uart.h:1175

[uart\_irq\_tx\_disable](group__uart__interrupt.md#gaf8a5bc26cd7c32e7bc6516c6f873c45a)

void uart\_irq\_tx\_disable(const struct device \*dev)

Disable TX interrupt in IER.

[uart\_fifo\_fill](group__uart__interrupt.md#gafe42e4719eada7e25904bc9ebfe87791)

static int uart\_fifo\_fill(const struct device \*dev, const uint8\_t \*tx\_data, int size)

Fill FIFO with data.

**Definition** uart.h:713

[uart\_poll\_out](group__uart__polling.md#ga06ba27ba772a7a18462b8cdbc7f9353c)

void uart\_poll\_out(const struct device \*dev, unsigned char out\_char)

Write a character to the device for output.

[uart\_poll\_out\_u16](group__uart__polling.md#ga8faa3f58b9098c97e288e9c5f3367fd9)

void uart\_poll\_out\_u16(const struct device \*dev, uint16\_t out\_u16)

Write a 16-bit datum to the device for output.

[uart\_poll\_in\_u16](group__uart__polling.md#gaad39c1358019bfdcb919da7982743553)

int uart\_poll\_in\_u16(const struct device \*dev, uint16\_t \*p\_u16)

Read a 16-bit datum from the device for input.

[uart\_poll\_in](group__uart__polling.md#gae81ac8cc976a20d774cfbda09e9c983d)

int uart\_poll\_in(const struct device \*dev, unsigned char \*p\_char)

Read a character from the device for input.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:393

[uart\_config](structuart__config.md)

UART controller configuration structure.

**Definition** uart.h:119

[uart\_config::stop\_bits](structuart__config.md#a7b98cd63c531110dc3dc99e94db73642)

uint8\_t stop\_bits

Stop bits, use uart\_config\_stop\_bits.

**Definition** uart.h:122

[uart\_config::parity](structuart__config.md#a9371728729252797880de052aae01089)

uint8\_t parity

Parity bit, use uart\_config\_parity.

**Definition** uart.h:121

[uart\_config::data\_bits](structuart__config.md#a93ee24cf6669fb4cfece78a53d3ec6c5)

uint8\_t data\_bits

Data bits, use uart\_config\_data\_bits.

**Definition** uart.h:123

[uart\_config::baudrate](structuart__config.md#ab532159a689e8f38c2465ce2d1fef354)

uint32\_t baudrate

Baudrate setting in bps.

**Definition** uart.h:120

[uart\_config::flow\_ctrl](structuart__config.md#af259c5efab532920b5cce7ae57f6af5e)

uint8\_t flow\_ctrl

Flow control setting, use uart\_config\_flow\_control.

**Definition** uart.h:124

[uart\_event\_rx\_buf](structuart__event__rx__buf.md)

UART RX buffer released event data.

**Definition** uart.h:281

[uart\_event\_rx\_buf::buf](structuart__event__rx__buf.md#a2547c84b742f454cfedf1de6d433297b)

uint8\_t \* buf

Pointer to buffer that is no longer in use.

**Definition** uart.h:283

[uart\_event\_rx\_stop](structuart__event__rx__stop.md)

UART RX stopped data.

**Definition** uart.h:287

[uart\_event\_rx\_stop::data](structuart__event__rx__stop.md#a1b361c8b7e17d1304a475235e734db48)

struct uart\_event\_rx data

Last received data.

**Definition** uart.h:291

[uart\_event\_rx\_stop::reason](structuart__event__rx__stop.md#a96fbae85208d9b3ea0382e7e236a932d)

enum uart\_rx\_stop\_reason reason

Reason why receiving stopped.

**Definition** uart.h:289

[uart\_event\_rx](structuart__event__rx.md)

UART RX event data.

**Definition** uart.h:271

[uart\_event\_rx::buf](structuart__event__rx.md#a2d9dfa9d9b25ff976cf2e937c72eb245)

uint8\_t \* buf

Pointer to current buffer.

**Definition** uart.h:273

[uart\_event\_rx::len](structuart__event__rx.md#a96414b96e63503336f8cf0d2249cd3bd)

size\_t len

Number of new bytes received.

**Definition** uart.h:277

[uart\_event\_rx::offset](structuart__event__rx.md#aa483e719298c30b9f5e6c57d3d161281)

size\_t offset

Currently received data offset in bytes.

**Definition** uart.h:275

[uart\_event\_tx](structuart__event__tx.md)

UART TX event data.

**Definition** uart.h:258

[uart\_event\_tx::buf](structuart__event__tx.md#a314a676a4050b2438b6f41485656bdbd)

const uint8\_t \* buf

Pointer to current buffer.

**Definition** uart.h:260

[uart\_event\_tx::len](structuart__event__tx.md#a7d844b2c0833d24accf82d58ee3408ff)

size\_t len

Number of bytes sent.

**Definition** uart.h:262

[uart\_event](structuart__event.md)

Structure containing information about current event.

**Definition** uart.h:295

[uart\_event::data](structuart__event.md#a07e3eebb7642ab52c73baba514704c69)

union uart\_event::uart\_event\_data data

[uart\_event::type](structuart__event.md#a2fb82a30e414a74943067cd0784f4b44)

enum uart\_event\_type type

Type of event.

**Definition** uart.h:297

[uart\_event::uart\_event\_data](unionuart__event_1_1uart__event__data.md)

Event data.

**Definition** uart.h:299

[uart\_event::uart\_event\_data::tx](unionuart__event_1_1uart__event__data.md#a79fb6b799d5574c6aa38a211e020035f)

struct uart\_event\_tx tx

UART\_TX\_DONE and UART\_TX\_ABORTED events data.

**Definition** uart.h:301

[uart\_event::uart\_event\_data::rx\_stop](unionuart__event_1_1uart__event__data.md#aad7488a2a3d91cea0ea874a08d7b88f6)

struct uart\_event\_rx\_stop rx\_stop

UART\_RX\_STOPPED event data.

**Definition** uart.h:307

[uart\_event::uart\_event\_data::rx\_buf](unionuart__event_1_1uart__event__data.md#ac03cdaeccba5f693337fa19299101863)

struct uart\_event\_rx\_buf rx\_buf

UART\_RX\_BUF\_RELEASED event data.

**Definition** uart.h:305

[uart\_event::uart\_event\_data::rx](unionuart__event_1_1uart__event__data.md#afac00624290b8fe5cf7b59516567b972)

struct uart\_event\_rx rx

UART\_RX\_RDY event data.

**Definition** uart.h:303

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [uart.h](drivers_2uart_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
