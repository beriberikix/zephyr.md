---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/drivers_2uart_8h_source.html
original_path: doxygen/html/drivers_2uart_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

24

25#include <[errno.h](errno_8h.md)>

26#include <stddef.h>

27

28#include <[zephyr/device.h](device_8h.md)>

29

30#ifdef \_\_cplusplus

31extern "C" {

32#endif

33

[ 35](group__uart__interface.md#ga02552532e171e789efc1b000917a9be0)enum [uart\_line\_ctrl](group__uart__interface.md#ga02552532e171e789efc1b000917a9be0) {

[ 36](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a3fdd02679f4f103190f3c12ab3cda00b) [UART\_LINE\_CTRL\_BAUD\_RATE](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a3fdd02679f4f103190f3c12ab3cda00b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 37](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a205d22bd797ab1c55323dc1ffda75f0d) [UART\_LINE\_CTRL\_RTS](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a205d22bd797ab1c55323dc1ffda75f0d) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 38](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a19e76af9901fc0274a9e27ff40e29e23) [UART\_LINE\_CTRL\_DTR](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a19e76af9901fc0274a9e27ff40e29e23) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 39](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a6d2c438044dd64f5cef07bbe4c6b3e97) [UART\_LINE\_CTRL\_DCD](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a6d2c438044dd64f5cef07bbe4c6b3e97) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

[ 40](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a87d8bedb5c918c182b271884ee42d75c) [UART\_LINE\_CTRL\_DSR](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a87d8bedb5c918c182b271884ee42d75c) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

41};

42

[ 49](group__uart__interface.md#gadeba6c5485e01dfc1c8a6e1c21668a88)enum [uart\_rx\_stop\_reason](group__uart__interface.md#gadeba6c5485e01dfc1c8a6e1c21668a88) {

[ 51](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a442beffc51cdf265bbcb40810a9a6e54) [UART\_ERROR\_OVERRUN](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a442beffc51cdf265bbcb40810a9a6e54) = (1 << 0),

[ 53](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a86d38eac5a46e6659aa765164b833eb5) [UART\_ERROR\_PARITY](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a86d38eac5a46e6659aa765164b833eb5) = (1 << 1),

[ 55](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88af13f72a8c615b4bc570b5a4df573407b) [UART\_ERROR\_FRAMING](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88af13f72a8c615b4bc570b5a4df573407b) = (1 << 2),

[ 63](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a4986147e23cc46ab8c2aa7e151d09571) [UART\_BREAK](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a4986147e23cc46ab8c2aa7e151d09571) = (1 << 3),

[ 73](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88aad8ca4dca9a846560293df71e6b39786) [UART\_ERROR\_COLLISION](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88aad8ca4dca9a846560293df71e6b39786) = (1 << 4),

[ 75](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a412058adbf7668b7051efb8419984d60) [UART\_ERROR\_NOISE](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a412058adbf7668b7051efb8419984d60) = (1 << 5),

76};

77

[ 79](group__uart__interface.md#gab2ab6aacb6e3c43bb26d4274157e5711)enum [uart\_config\_parity](group__uart__interface.md#gab2ab6aacb6e3c43bb26d4274157e5711) {

[ 80](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711a6a23a2ef22fb3b144648b244fff82b8d) [UART\_CFG\_PARITY\_NONE](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711a6a23a2ef22fb3b144648b244fff82b8d),

[ 81](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711a8a618b0a531c8d62809e39eb56eaf5ed) [UART\_CFG\_PARITY\_ODD](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711a8a618b0a531c8d62809e39eb56eaf5ed),

[ 82](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711ac3a4310efe198a1fa7d977a5531486ba) [UART\_CFG\_PARITY\_EVEN](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711ac3a4310efe198a1fa7d977a5531486ba),

[ 83](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711a5ee61c29a32447644ff70385158a11ca) [UART\_CFG\_PARITY\_MARK](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711a5ee61c29a32447644ff70385158a11ca),

[ 84](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711a8dc5306c8ca26321431bcf22ce9b036c) [UART\_CFG\_PARITY\_SPACE](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711a8dc5306c8ca26321431bcf22ce9b036c),

85};

86

[ 88](group__uart__interface.md#gafc1aecb863e2456d73b78a49fcbad72e)enum [uart\_config\_stop\_bits](group__uart__interface.md#gafc1aecb863e2456d73b78a49fcbad72e) {

[ 89](group__uart__interface.md#ggafc1aecb863e2456d73b78a49fcbad72ea308c660590a9fd16143806e8bef002af) [UART\_CFG\_STOP\_BITS\_0\_5](group__uart__interface.md#ggafc1aecb863e2456d73b78a49fcbad72ea308c660590a9fd16143806e8bef002af),

[ 90](group__uart__interface.md#ggafc1aecb863e2456d73b78a49fcbad72ea73024f1618eb04385bf488214c635e58) [UART\_CFG\_STOP\_BITS\_1](group__uart__interface.md#ggafc1aecb863e2456d73b78a49fcbad72ea73024f1618eb04385bf488214c635e58),

[ 91](group__uart__interface.md#ggafc1aecb863e2456d73b78a49fcbad72ea1da47ec95b6a6eee65abef3d6d84f9ad) [UART\_CFG\_STOP\_BITS\_1\_5](group__uart__interface.md#ggafc1aecb863e2456d73b78a49fcbad72ea1da47ec95b6a6eee65abef3d6d84f9ad),

[ 92](group__uart__interface.md#ggafc1aecb863e2456d73b78a49fcbad72eae180ecebc76516e89669e1d16bfb31c6) [UART\_CFG\_STOP\_BITS\_2](group__uart__interface.md#ggafc1aecb863e2456d73b78a49fcbad72eae180ecebc76516e89669e1d16bfb31c6),

93};

94

[ 96](group__uart__interface.md#gab9f7de744a68a311330576d7da02c44a)enum [uart\_config\_data\_bits](group__uart__interface.md#gab9f7de744a68a311330576d7da02c44a) {

[ 97](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aa1b0545c2d1970e67d697b62510bfbe27) [UART\_CFG\_DATA\_BITS\_5](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aa1b0545c2d1970e67d697b62510bfbe27),

[ 98](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aac6e0f3c0479164c34144d0e6e28298e4) [UART\_CFG\_DATA\_BITS\_6](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aac6e0f3c0479164c34144d0e6e28298e4),

[ 99](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aa6120eb8f668b257c8c2dd0dc9cf0c913) [UART\_CFG\_DATA\_BITS\_7](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aa6120eb8f668b257c8c2dd0dc9cf0c913),

[ 100](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aa23f55bdb24b4016c8c23c518e981df97) [UART\_CFG\_DATA\_BITS\_8](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aa23f55bdb24b4016c8c23c518e981df97),

[ 101](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aaf3b601af696d8841fe79871ca3e41e5f) [UART\_CFG\_DATA\_BITS\_9](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aaf3b601af696d8841fe79871ca3e41e5f),

102};

103

[ 111](group__uart__interface.md#ga8e2f1b4a8d60d7a6c24835d1b26f99e8)enum [uart\_config\_flow\_control](group__uart__interface.md#ga8e2f1b4a8d60d7a6c24835d1b26f99e8) {

[ 112](group__uart__interface.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a546b28db6f8bfc26266e8f7d6b8ff973) [UART\_CFG\_FLOW\_CTRL\_NONE](group__uart__interface.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a546b28db6f8bfc26266e8f7d6b8ff973),

[ 113](group__uart__interface.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8ad682bfe14a9f0860d1fdc3e8e9d56f86) [UART\_CFG\_FLOW\_CTRL\_RTS\_CTS](group__uart__interface.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8ad682bfe14a9f0860d1fdc3e8e9d56f86),

[ 114](group__uart__interface.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a0efc5de86bf80119f750cf372814309f) [UART\_CFG\_FLOW\_CTRL\_DTR\_DSR](group__uart__interface.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a0efc5de86bf80119f750cf372814309f),

[ 115](group__uart__interface.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a9675cc80d44e980b66e99bc8548f085c) [UART\_CFG\_FLOW\_CTRL\_RS485](group__uart__interface.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a9675cc80d44e980b66e99bc8548f085c),

116};

117

[ 121](structuart__config.md)struct [uart\_config](structuart__config.md) {

[ 122](structuart__config.md#ab532159a689e8f38c2465ce2d1fef354) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [baudrate](structuart__config.md#ab532159a689e8f38c2465ce2d1fef354);

[ 123](structuart__config.md#a9371728729252797880de052aae01089) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [parity](structuart__config.md#a9371728729252797880de052aae01089);

[ 124](structuart__config.md#a7b98cd63c531110dc3dc99e94db73642) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [stop\_bits](structuart__config.md#a7b98cd63c531110dc3dc99e94db73642);

[ 125](structuart__config.md#a93ee24cf6669fb4cfece78a53d3ec6c5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data\_bits](structuart__config.md#a93ee24cf6669fb4cfece78a53d3ec6c5);

[ 126](structuart__config.md#af259c5efab532920b5cce7ae57f6af5e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flow\_ctrl](structuart__config.md#af259c5efab532920b5cce7ae57f6af5e);

127};

128

133

[ 141](group__uart__interrupt.md#gad7a26b1a1d6212d7d39c05c8ad4ec926)typedef void (\*[uart\_irq\_callback\_user\_data\_t](group__uart__interrupt.md#gad7a26b1a1d6212d7d39c05c8ad4ec926))(const struct [device](structdevice.md) \*dev,

142 void \*user\_data);

143

[ 149](group__uart__interrupt.md#ga6750414923953c84fb1e19177ec74ae0)typedef void (\*[uart\_irq\_config\_func\_t](group__uart__interrupt.md#ga6750414923953c84fb1e19177ec74ae0))(const struct [device](structdevice.md) \*dev);

150

159

[ 207](group__uart__async.md#gaf0c9513cbafa36d86b4c83f2b6a03dcd)enum [uart\_event\_type](group__uart__async.md#gaf0c9513cbafa36d86b4c83f2b6a03dcd) {

[ 209](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda4b5cdf863d8b6e5cd7b58f611808a6e4) [UART\_TX\_DONE](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda4b5cdf863d8b6e5cd7b58f611808a6e4),

[ 217](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0abcf565ba1011815285bb3845f8d5a1) [UART\_TX\_ABORTED](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0abcf565ba1011815285bb3845f8d5a1),

[ 228](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7) [UART\_RX\_RDY](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7),

[ 240](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0d250f372702526f1bce6d4dfe166abe) [UART\_RX\_BUF\_REQUEST](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0d250f372702526f1bce6d4dfe166abe),

[ 244](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcdab2d152bd84f659d4fc4060df29811b48) [UART\_RX\_BUF\_RELEASED](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcdab2d152bd84f659d4fc4060df29811b48),

[ 252](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcdaa8ff5629c002a61bc3bdf5baa2ebc203) [UART\_RX\_DISABLED](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcdaa8ff5629c002a61bc3bdf5baa2ebc203),

[ 258](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda05b81ddf74d208aeabace6ac90ae52dd) [UART\_RX\_STOPPED](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda05b81ddf74d208aeabace6ac90ae52dd),

259};

260

[ 262](structuart__event__tx.md)struct [uart\_event\_tx](structuart__event__tx.md) {

[ 264](structuart__event__tx.md#a314a676a4050b2438b6f41485656bdbd) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structuart__event__tx.md#a314a676a4050b2438b6f41485656bdbd);

[ 266](structuart__event__tx.md#a7d844b2c0833d24accf82d58ee3408ff) size\_t [len](structuart__event__tx.md#a7d844b2c0833d24accf82d58ee3408ff);

267};

268

[ 275](structuart__event__rx.md)struct [uart\_event\_rx](structuart__event__rx.md) {

[ 277](structuart__event__rx.md#a2d9dfa9d9b25ff976cf2e937c72eb245) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structuart__event__rx.md#a2d9dfa9d9b25ff976cf2e937c72eb245);

[ 279](structuart__event__rx.md#aa483e719298c30b9f5e6c57d3d161281) size\_t [offset](structuart__event__rx.md#aa483e719298c30b9f5e6c57d3d161281);

[ 281](structuart__event__rx.md#a96414b96e63503336f8cf0d2249cd3bd) size\_t [len](structuart__event__rx.md#a96414b96e63503336f8cf0d2249cd3bd);

282};

283

[ 285](structuart__event__rx__buf.md)struct [uart\_event\_rx\_buf](structuart__event__rx__buf.md) {

[ 287](structuart__event__rx__buf.md#a2547c84b742f454cfedf1de6d433297b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structuart__event__rx__buf.md#a2547c84b742f454cfedf1de6d433297b);

288};

289

[ 291](structuart__event__rx__stop.md)struct [uart\_event\_rx\_stop](structuart__event__rx__stop.md) {

[ 293](structuart__event__rx__stop.md#a96fbae85208d9b3ea0382e7e236a932d) enum [uart\_rx\_stop\_reason](group__uart__interface.md#gadeba6c5485e01dfc1c8a6e1c21668a88) [reason](structuart__event__rx__stop.md#a96fbae85208d9b3ea0382e7e236a932d);

[ 295](structuart__event__rx__stop.md#a1b361c8b7e17d1304a475235e734db48) struct [uart\_event\_rx](structuart__event__rx.md) [data](structuart__event__rx__stop.md#a1b361c8b7e17d1304a475235e734db48);

296};

297

[ 299](structuart__event.md)struct [uart\_event](structuart__event.md) {

[ 301](structuart__event.md#a2fb82a30e414a74943067cd0784f4b44) enum [uart\_event\_type](group__uart__async.md#gaf0c9513cbafa36d86b4c83f2b6a03dcd) [type](structuart__event.md#a2fb82a30e414a74943067cd0784f4b44);

[ 303](unionuart__event_1_1uart__event__data.md) union [uart\_event\_data](unionuart__event_1_1uart__event__data.md) {

[ 305](unionuart__event_1_1uart__event__data.md#a79fb6b799d5574c6aa38a211e020035f) struct [uart\_event\_tx](structuart__event__tx.md) [tx](unionuart__event_1_1uart__event__data.md#a79fb6b799d5574c6aa38a211e020035f);

[ 307](unionuart__event_1_1uart__event__data.md#afac00624290b8fe5cf7b59516567b972) struct [uart\_event\_rx](structuart__event__rx.md) [rx](unionuart__event_1_1uart__event__data.md#afac00624290b8fe5cf7b59516567b972);

[ 309](unionuart__event_1_1uart__event__data.md#ac03cdaeccba5f693337fa19299101863) struct [uart\_event\_rx\_buf](structuart__event__rx__buf.md) [rx\_buf](unionuart__event_1_1uart__event__data.md#ac03cdaeccba5f693337fa19299101863);

[ 311](unionuart__event_1_1uart__event__data.md#aad7488a2a3d91cea0ea874a08d7b88f6) struct [uart\_event\_rx\_stop](structuart__event__rx__stop.md) [rx\_stop](unionuart__event_1_1uart__event__data.md#aad7488a2a3d91cea0ea874a08d7b88f6);

[ 312](structuart__event.md#a07e3eebb7642ab52c73baba514704c69) } [data](structuart__event.md#a07e3eebb7642ab52c73baba514704c69);

313};

314

[ 324](group__uart__async.md#ga00b7c98a4da3ea3675d0a40c5dacb136)typedef void (\*[uart\_callback\_t](group__uart__async.md#ga00b7c98a4da3ea3675d0a40c5dacb136))(const struct [device](structdevice.md) \*dev,

325 struct [uart\_event](structuart__event.md) \*evt, void \*user\_data);

326

330

336

338\_\_subsystem struct uart\_driver\_api {

339

340#ifdef CONFIG\_UART\_ASYNC\_API

341

342 int (\*callback\_set)(const struct [device](structdevice.md) \*dev,

343 [uart\_callback\_t](group__uart__async.md#ga00b7c98a4da3ea3675d0a40c5dacb136) callback,

344 void \*user\_data);

345

346 int (\*tx)(const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t len,

347 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout);

348 int (\*tx\_abort)(const struct [device](structdevice.md) \*dev);

349

350 int (\*rx\_enable)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t len,

351 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout);

352 int (\*rx\_buf\_rsp)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t len);

353 int (\*rx\_disable)(const struct [device](structdevice.md) \*dev);

354

355#ifdef CONFIG\_UART\_WIDE\_DATA

356 int (\*tx\_u16)(const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*buf,

357 size\_t len, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout);

358 int (\*rx\_enable\_u16)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*buf,

359 size\_t len, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout);

360 int (\*rx\_buf\_rsp\_u16)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*buf,

361 size\_t len);

362#endif

363

364#endif

365

367 int (\*poll\_in)(const struct [device](structdevice.md) \*dev, unsigned char \*p\_char);

368 void (\*poll\_out)(const struct [device](structdevice.md) \*dev, unsigned char out\_char);

369

370#ifdef CONFIG\_UART\_WIDE\_DATA

371 int (\*poll\_in\_u16)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*p\_u16);

372 void (\*poll\_out\_u16)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) out\_u16);

373#endif

374

376 int (\*err\_check)(const struct [device](structdevice.md) \*dev);

377

378#ifdef CONFIG\_UART\_USE\_RUNTIME\_CONFIGURE

380 int (\*configure)(const struct [device](structdevice.md) \*dev,

381 const struct [uart\_config](structuart__config.md) \*cfg);

382 int (\*config\_get)(const struct [device](structdevice.md) \*dev, struct [uart\_config](structuart__config.md) \*cfg);

383#endif

384

385#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

386

388 int (\*fifo\_fill)(const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*tx\_data,

389 int len);

390

391#ifdef CONFIG\_UART\_WIDE\_DATA

392 int (\*fifo\_fill\_u16)(const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*tx\_data,

393 int len);

394#endif

395

397 int (\*fifo\_read)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rx\_data,

398 const int size);

399

400#ifdef CONFIG\_UART\_WIDE\_DATA

401 int (\*fifo\_read\_u16)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*rx\_data,

402 const int size);

403#endif

404

406 void (\*irq\_tx\_enable)(const struct [device](structdevice.md) \*dev);

407

409 void (\*irq\_tx\_disable)(const struct [device](structdevice.md) \*dev);

410

412 int (\*irq\_tx\_ready)(const struct [device](structdevice.md) \*dev);

413

415 void (\*irq\_rx\_enable)(const struct [device](structdevice.md) \*dev);

416

418 void (\*irq\_rx\_disable)(const struct [device](structdevice.md) \*dev);

419

421 int (\*irq\_tx\_complete)(const struct [device](structdevice.md) \*dev);

422

424 int (\*irq\_rx\_ready)(const struct [device](structdevice.md) \*dev);

425

427 void (\*irq\_err\_enable)(const struct [device](structdevice.md) \*dev);

428

430 void (\*irq\_err\_disable)(const struct [device](structdevice.md) \*dev);

431

433 int (\*irq\_is\_pending)(const struct [device](structdevice.md) \*dev);

434

436 int (\*irq\_update)(const struct [device](structdevice.md) \*dev);

437

439 void (\*irq\_callback\_set)(const struct [device](structdevice.md) \*dev,

440 [uart\_irq\_callback\_user\_data\_t](group__uart__interrupt.md#gad7a26b1a1d6212d7d39c05c8ad4ec926) cb,

441 void \*user\_data);

442

443#endif

444

445#ifdef CONFIG\_UART\_LINE\_CTRL

446 int (\*line\_ctrl\_set)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ctrl,

447 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val);

448 int (\*line\_ctrl\_get)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ctrl,

449 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*val);

450#endif

451

452#ifdef CONFIG\_UART\_DRV\_CMD

453 int (\*drv\_cmd)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) p);

454#endif

455

456};

457

459

[ 469](group__uart__interface.md#ga22ea20fd8e07153b3b71cc9416f5462f)\_\_syscall int [uart\_err\_check](group__uart__interface.md#ga22ea20fd8e07153b3b71cc9416f5462f)(const struct [device](structdevice.md) \*dev);

470

471static inline int z\_impl\_uart\_err\_check(const struct [device](structdevice.md) \*dev)

472{

473 const struct uart\_driver\_api \*api =

474 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

475

476 if (api->err\_check == NULL) {

477 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

478 }

479

480 return api->err\_check(dev);

481}

482

487

[ 506](group__uart__polling.md#gae81ac8cc976a20d774cfbda09e9c983d)\_\_syscall int [uart\_poll\_in](group__uart__polling.md#gae81ac8cc976a20d774cfbda09e9c983d)(const struct [device](structdevice.md) \*dev, unsigned char \*p\_char);

507

508static inline int z\_impl\_uart\_poll\_in(const struct [device](structdevice.md) \*dev,

509 unsigned char \*p\_char)

510{

511 const struct uart\_driver\_api \*api =

512 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

513

514 if (api->poll\_in == NULL) {

515 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

516 }

517

518 return api->poll\_in(dev, p\_char);

519}

520

[ 540](group__uart__polling.md#gaad39c1358019bfdcb919da7982743553)\_\_syscall int [uart\_poll\_in\_u16](group__uart__polling.md#gaad39c1358019bfdcb919da7982743553)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*p\_u16);

541

542static inline int z\_impl\_uart\_poll\_in\_u16(const struct [device](structdevice.md) \*dev,

543 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*p\_u16)

544{

545#ifdef CONFIG\_UART\_WIDE\_DATA

546 const struct uart\_driver\_api \*api =

547 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

548

549 if (api->poll\_in\_u16 == NULL) {

550 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

551 }

552

553 return api->poll\_in\_u16(dev, p\_u16);

554#else

555 ARG\_UNUSED(dev);

556 ARG\_UNUSED(p\_u16);

557 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

558#endif

559}

560

[ 575](group__uart__polling.md#ga06ba27ba772a7a18462b8cdbc7f9353c)\_\_syscall void [uart\_poll\_out](group__uart__polling.md#ga06ba27ba772a7a18462b8cdbc7f9353c)(const struct [device](structdevice.md) \*dev,

576 unsigned char out\_char);

577

578static inline void z\_impl\_uart\_poll\_out(const struct [device](structdevice.md) \*dev,

579 unsigned char out\_char)

580{

581 const struct uart\_driver\_api \*api =

582 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

583

584 api->poll\_out(dev, out\_char);

585}

586

[ 601](group__uart__polling.md#ga8faa3f58b9098c97e288e9c5f3367fd9)\_\_syscall void [uart\_poll\_out\_u16](group__uart__polling.md#ga8faa3f58b9098c97e288e9c5f3367fd9)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) out\_u16);

602

603static inline void z\_impl\_uart\_poll\_out\_u16(const struct [device](structdevice.md) \*dev,

604 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) out\_u16)

605{

606#ifdef CONFIG\_UART\_WIDE\_DATA

607 const struct uart\_driver\_api \*api =

608 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

609

610 api->poll\_out\_u16(dev, out\_u16);

611#else

612 ARG\_UNUSED(dev);

613 ARG\_UNUSED(out\_u16);

614#endif

615}

616

620

[ 635](group__uart__interface.md#gaa0b75777b879af10543f7e8f463ff9a2)\_\_syscall int [uart\_configure](group__uart__interface.md#gaa0b75777b879af10543f7e8f463ff9a2)(const struct [device](structdevice.md) \*dev,

636 const struct [uart\_config](structuart__config.md) \*cfg);

637

638static inline int z\_impl\_uart\_configure(const struct [device](structdevice.md) \*dev,

639 const struct [uart\_config](structuart__config.md) \*cfg)

640{

641#ifdef CONFIG\_UART\_USE\_RUNTIME\_CONFIGURE

642 const struct uart\_driver\_api \*api =

643 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

644

645 if (api->configure == NULL) {

646 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

647 }

648 return api->configure(dev, cfg);

649#else

650 ARG\_UNUSED(dev);

651 ARG\_UNUSED(cfg);

652 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

653#endif

654}

655

[ 670](group__uart__interface.md#ga81dfc5f2134de8e4acb5f063512cf703)\_\_syscall int [uart\_config\_get](group__uart__interface.md#ga81dfc5f2134de8e4acb5f063512cf703)(const struct [device](structdevice.md) \*dev,

671 struct [uart\_config](structuart__config.md) \*cfg);

672

673static inline int z\_impl\_uart\_config\_get(const struct [device](structdevice.md) \*dev,

674 struct [uart\_config](structuart__config.md) \*cfg)

675{

676#ifdef CONFIG\_UART\_USE\_RUNTIME\_CONFIGURE

677 const struct uart\_driver\_api \*api =

678 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

679

680 if (api->config\_get == NULL) {

681 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

682 }

683

684 return api->config\_get(dev, cfg);

685#else

686 ARG\_UNUSED(dev);

687 ARG\_UNUSED(cfg);

688 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

689#endif

690}

691

696

[ 717](group__uart__interrupt.md#gafe42e4719eada7e25904bc9ebfe87791)static inline int [uart\_fifo\_fill](group__uart__interrupt.md#gafe42e4719eada7e25904bc9ebfe87791)(const struct [device](structdevice.md) \*dev,

718 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*tx\_data,

719 int size)

720{

721#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

722 const struct uart\_driver\_api \*api =

723 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

724

725 if (api->fifo\_fill == NULL) {

726 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

727 }

728

729 return api->fifo\_fill(dev, tx\_data, size);

730#else

731 ARG\_UNUSED(dev);

732 ARG\_UNUSED(tx\_data);

733 ARG\_UNUSED(size);

734 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

735#endif

736}

737

[ 758](group__uart__interrupt.md#gaa89f58818d8428ad6a11abf692c54c0d)static inline int [uart\_fifo\_fill\_u16](group__uart__interrupt.md#gaa89f58818d8428ad6a11abf692c54c0d)(const struct [device](structdevice.md) \*dev,

759 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*tx\_data,

760 int size)

761{

762#if defined(CONFIG\_UART\_INTERRUPT\_DRIVEN) && defined(CONFIG\_UART\_WIDE\_DATA)

763 const struct uart\_driver\_api \*api =

764 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

765

766 if (api->fifo\_fill\_u16 == NULL) {

767 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

768 }

769

770 return api->fifo\_fill\_u16(dev, tx\_data, size);

771#else

772 ARG\_UNUSED(dev);

773 ARG\_UNUSED(tx\_data);

774 ARG\_UNUSED(size);

775 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

776#endif

777}

778

[ 800](group__uart__interrupt.md#gab10942076ac47ecff29e924098049398)static inline int [uart\_fifo\_read](group__uart__interrupt.md#gab10942076ac47ecff29e924098049398)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rx\_data,

801 const int size)

802{

803#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

804 const struct uart\_driver\_api \*api =

805 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

806

807 if (api->fifo\_read == NULL) {

808 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

809 }

810

811 return api->fifo\_read(dev, rx\_data, size);

812#else

813 ARG\_UNUSED(dev);

814 ARG\_UNUSED(rx\_data);

815 ARG\_UNUSED(size);

816 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

817#endif

818}

819

[ 841](group__uart__interrupt.md#ga4a3c25dad2290f1f40e4b847e3b83f64)static inline int [uart\_fifo\_read\_u16](group__uart__interrupt.md#ga4a3c25dad2290f1f40e4b847e3b83f64)(const struct [device](structdevice.md) \*dev,

842 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*rx\_data,

843 const int size)

844{

845#if defined(CONFIG\_UART\_INTERRUPT\_DRIVEN) && defined(CONFIG\_UART\_WIDE\_DATA)

846 const struct uart\_driver\_api \*api =

847 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

848

849 if (api->fifo\_read\_u16 == NULL) {

850 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

851 }

852

853 return api->fifo\_read\_u16(dev, rx\_data, size);

854#else

855 ARG\_UNUSED(dev);

856 ARG\_UNUSED(rx\_data);

857 ARG\_UNUSED(size);

858 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

859#endif

860}

861

[ 867](group__uart__interrupt.md#ga9cbd6e33dce6a5b06233cf10077e19cc)\_\_syscall void [uart\_irq\_tx\_enable](group__uart__interrupt.md#ga9cbd6e33dce6a5b06233cf10077e19cc)(const struct [device](structdevice.md) \*dev);

868

869static inline void z\_impl\_uart\_irq\_tx\_enable(const struct [device](structdevice.md) \*dev)

870{

871#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

872 const struct uart\_driver\_api \*api =

873 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

874

875 if (api->irq\_tx\_enable != NULL) {

876 api->irq\_tx\_enable(dev);

877 }

878#else

879 ARG\_UNUSED(dev);

880#endif

881}

882

[ 888](group__uart__interrupt.md#gaf8a5bc26cd7c32e7bc6516c6f873c45a)\_\_syscall void [uart\_irq\_tx\_disable](group__uart__interrupt.md#gaf8a5bc26cd7c32e7bc6516c6f873c45a)(const struct [device](structdevice.md) \*dev);

889

890static inline void z\_impl\_uart\_irq\_tx\_disable(const struct [device](structdevice.md) \*dev)

891{

892#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

893 const struct uart\_driver\_api \*api =

894 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

895

896 if (api->irq\_tx\_disable != NULL) {

897 api->irq\_tx\_disable(dev);

898 }

899#else

900 ARG\_UNUSED(dev);

901#endif

902}

903

[ 922](group__uart__interrupt.md#ga5e126b5f19549eb7f5b785b98ebe7638)static inline int [uart\_irq\_tx\_ready](group__uart__interrupt.md#ga5e126b5f19549eb7f5b785b98ebe7638)(const struct [device](structdevice.md) \*dev)

923{

924#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

925 const struct uart\_driver\_api \*api =

926 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

927

928 if (api->irq\_tx\_ready == NULL) {

929 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

930 }

931

932 return api->irq\_tx\_ready(dev);

933#else

934 ARG\_UNUSED(dev);

935 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

936#endif

937}

938

[ 944](group__uart__interrupt.md#ga4ec3ae3974da2b3ab94ae7b835d17bad)\_\_syscall void [uart\_irq\_rx\_enable](group__uart__interrupt.md#ga4ec3ae3974da2b3ab94ae7b835d17bad)(const struct [device](structdevice.md) \*dev);

945

946static inline void z\_impl\_uart\_irq\_rx\_enable(const struct [device](structdevice.md) \*dev)

947{

948#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

949 const struct uart\_driver\_api \*api =

950 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

951

952 if (api->irq\_rx\_enable != NULL) {

953 api->irq\_rx\_enable(dev);

954 }

955#else

956 ARG\_UNUSED(dev);

957#endif

958}

959

[ 965](group__uart__interrupt.md#gaa759d7935fdd9ab6ca0761f161389a29)\_\_syscall void [uart\_irq\_rx\_disable](group__uart__interrupt.md#gaa759d7935fdd9ab6ca0761f161389a29)(const struct [device](structdevice.md) \*dev);

966

967static inline void z\_impl\_uart\_irq\_rx\_disable(const struct [device](structdevice.md) \*dev)

968{

969#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

970 const struct uart\_driver\_api \*api =

971 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

972

973 if (api->irq\_rx\_disable != NULL) {

974 api->irq\_rx\_disable(dev);

975 }

976#else

977 ARG\_UNUSED(dev);

978#endif

979}

980

[ 1000](group__uart__interrupt.md#ga917935a13bf6a5d1e32ef34339e96455)static inline int [uart\_irq\_tx\_complete](group__uart__interrupt.md#ga917935a13bf6a5d1e32ef34339e96455)(const struct [device](structdevice.md) \*dev)

1001{

1002#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

1003 const struct uart\_driver\_api \*api =

1004 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1005

1006 if (api->irq\_tx\_complete == NULL) {

1007 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1008 }

1009 return api->irq\_tx\_complete(dev);

1010#else

1011 ARG\_UNUSED(dev);

1012 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

1013#endif

1014}

1015

[ 1036](group__uart__interrupt.md#gad04073b1b8e3de13b43ae1194561377b)static inline int [uart\_irq\_rx\_ready](group__uart__interrupt.md#gad04073b1b8e3de13b43ae1194561377b)(const struct [device](structdevice.md) \*dev)

1037{

1038#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

1039 const struct uart\_driver\_api \*api =

1040 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1041

1042 if (api->irq\_rx\_ready == NULL) {

1043 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1044 }

1045 return api->irq\_rx\_ready(dev);

1046#else

1047 ARG\_UNUSED(dev);

1048 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

1049#endif

1050}

1051

[ 1056](group__uart__interrupt.md#ga7c24daae3326bc2959ea13a2be79969f)\_\_syscall void [uart\_irq\_err\_enable](group__uart__interrupt.md#ga7c24daae3326bc2959ea13a2be79969f)(const struct [device](structdevice.md) \*dev);

1057

1058static inline void z\_impl\_uart\_irq\_err\_enable(const struct [device](structdevice.md) \*dev)

1059{

1060#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

1061 const struct uart\_driver\_api \*api =

1062 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1063

1064 if (api->irq\_err\_enable) {

1065 api->irq\_err\_enable(dev);

1066 }

1067#else

1068 ARG\_UNUSED(dev);

1069#endif

1070}

1071

[ 1077](group__uart__interrupt.md#gaaf8a88361807e204f7227fbd1d0e75b2)\_\_syscall void [uart\_irq\_err\_disable](group__uart__interrupt.md#gaaf8a88361807e204f7227fbd1d0e75b2)(const struct [device](structdevice.md) \*dev);

1078

1079static inline void z\_impl\_uart\_irq\_err\_disable(const struct [device](structdevice.md) \*dev)

1080{

1081#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

1082 const struct uart\_driver\_api \*api =

1083 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1084

1085 if (api->irq\_err\_disable) {

1086 api->irq\_err\_disable(dev);

1087 }

1088#else

1089 ARG\_UNUSED(dev);

1090#endif

1091}

1092

[ 1103](group__uart__interrupt.md#ga11ccae917c8b5fd76aaabdb047125f6a)\_\_syscall int [uart\_irq\_is\_pending](group__uart__interrupt.md#ga11ccae917c8b5fd76aaabdb047125f6a)(const struct [device](structdevice.md) \*dev);

1104

1105static inline int z\_impl\_uart\_irq\_is\_pending(const struct [device](structdevice.md) \*dev)

1106{

1107#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

1108 const struct uart\_driver\_api \*api =

1109 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1110

1111 if (api->irq\_is\_pending == NULL) {

1112 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1113 }

1114 return api->irq\_is\_pending(dev);

1115#else

1116 ARG\_UNUSED(dev);

1117 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

1118#endif

1119}

1120

[ 1146](group__uart__interrupt.md#gac5241e000d482c40b2a4856c58c106a6)\_\_syscall int [uart\_irq\_update](group__uart__interrupt.md#gac5241e000d482c40b2a4856c58c106a6)(const struct [device](structdevice.md) \*dev);

1147

1148static inline int z\_impl\_uart\_irq\_update(const struct [device](structdevice.md) \*dev)

1149{

1150#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

1151 const struct uart\_driver\_api \*api =

1152 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1153

1154 if (api->irq\_update == NULL) {

1155 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1156 }

1157 return api->irq\_update(dev);

1158#else

1159 ARG\_UNUSED(dev);

1160 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

1161#endif

1162}

1163

[ 1179](group__uart__interrupt.md#gaf469966a56d1fc9f50108201597ee0a0)static inline int [uart\_irq\_callback\_user\_data\_set](group__uart__interrupt.md#gaf469966a56d1fc9f50108201597ee0a0)(const struct [device](structdevice.md) \*dev,

1180 [uart\_irq\_callback\_user\_data\_t](group__uart__interrupt.md#gad7a26b1a1d6212d7d39c05c8ad4ec926) cb,

1181 void \*user\_data)

1182{

1183#ifdef CONFIG\_UART\_INTERRUPT\_DRIVEN

1184 const struct uart\_driver\_api \*api =

1185 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1186

1187 if ((api != NULL) && (api->irq\_callback\_set != NULL)) {

1188 api->irq\_callback\_set(dev, cb, user\_data);

1189 return 0;

1190 } else {

1191 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1192 }

1193#else

1194 ARG\_UNUSED(dev);

1195 ARG\_UNUSED(cb);

1196 ARG\_UNUSED(user\_data);

1197 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

1198#endif

1199}

1200

[ 1214](group__uart__interrupt.md#ga5f7af3f7f0d9155349ea3b4fad78956c)static inline int [uart\_irq\_callback\_set](group__uart__interrupt.md#ga5f7af3f7f0d9155349ea3b4fad78956c)(const struct [device](structdevice.md) \*dev,

1215 [uart\_irq\_callback\_user\_data\_t](group__uart__interrupt.md#gad7a26b1a1d6212d7d39c05c8ad4ec926) cb)

1216{

1217 return [uart\_irq\_callback\_user\_data\_set](group__uart__interrupt.md#gaf469966a56d1fc9f50108201597ee0a0)(dev, cb, NULL);

1218}

1219

1223

1228

[ 1244](group__uart__async.md#gad33e627ed8729409b14e92453e53459c)static inline int [uart\_callback\_set](group__uart__async.md#gad33e627ed8729409b14e92453e53459c)(const struct [device](structdevice.md) \*dev,

1245 [uart\_callback\_t](group__uart__async.md#ga00b7c98a4da3ea3675d0a40c5dacb136) callback,

1246 void \*user\_data)

1247{

1248#ifdef CONFIG\_UART\_ASYNC\_API

1249 const struct uart\_driver\_api \*api =

1250 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1251

1252 if (api->callback\_set == NULL) {

1253 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1254 }

1255

1256 return api->callback\_set(dev, callback, user\_data);

1257#else

1258 ARG\_UNUSED(dev);

1259 ARG\_UNUSED(callback);

1260 ARG\_UNUSED(user\_data);

1261 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

1262#endif

1263}

1264

[ 1282](group__uart__async.md#gaf99f32ce2e2d9beb32a2f2e5a26320dc)\_\_syscall int [uart\_tx](group__uart__async.md#gaf99f32ce2e2d9beb32a2f2e5a26320dc)(const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf,

1283 size\_t len,

1284 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout);

1285

1286static inline int z\_impl\_uart\_tx(const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf,

1287 size\_t len, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout)

1288

1289{

1290#ifdef CONFIG\_UART\_ASYNC\_API

1291 const struct uart\_driver\_api \*api =

1292 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1293

1294 return api->tx(dev, buf, len, timeout);

1295#else

1296 ARG\_UNUSED(dev);

1297 ARG\_UNUSED(buf);

1298 ARG\_UNUSED(len);

1299 ARG\_UNUSED(timeout);

1300 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

1301#endif

1302}

1303

[ 1321](group__uart__async.md#gab0ea611cd072fa459a6f1780ce62c9e3)\_\_syscall int [uart\_tx\_u16](group__uart__async.md#gab0ea611cd072fa459a6f1780ce62c9e3)(const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*buf,

1322 size\_t len, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout);

1323

1324static inline int z\_impl\_uart\_tx\_u16(const struct [device](structdevice.md) \*dev,

1325 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*buf,

1326 size\_t len, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout)

1327

1328{

1329#if defined(CONFIG\_UART\_ASYNC\_API) && defined(CONFIG\_UART\_WIDE\_DATA)

1330 const struct uart\_driver\_api \*api =

1331 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1332

1333 return api->tx\_u16(dev, buf, len, timeout);

1334#else

1335 ARG\_UNUSED(dev);

1336 ARG\_UNUSED(buf);

1337 ARG\_UNUSED(len);

1338 ARG\_UNUSED(timeout);

1339 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

1340#endif

1341}

1342

[ 1355](group__uart__async.md#gaa8a26d3ea685fb98030ea03613be6280)\_\_syscall int [uart\_tx\_abort](group__uart__async.md#gaa8a26d3ea685fb98030ea03613be6280)(const struct [device](structdevice.md) \*dev);

1356

1357static inline int z\_impl\_uart\_tx\_abort(const struct [device](structdevice.md) \*dev)

1358{

1359#ifdef CONFIG\_UART\_ASYNC\_API

1360 const struct uart\_driver\_api \*api =

1361 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1362

1363 return api->tx\_abort(dev);

1364#else

1365 ARG\_UNUSED(dev);

1366 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

1367#endif

1368}

1369

[ 1391](group__uart__async.md#ga902e18c2a727ed2988e1b6caa6a444b8)\_\_syscall int [uart\_rx\_enable](group__uart__async.md#ga902e18c2a727ed2988e1b6caa6a444b8)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf,

1392 size\_t len,

1393 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout);

1394

1395static inline int z\_impl\_uart\_rx\_enable(const struct [device](structdevice.md) \*dev,

1396 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf,

1397 size\_t len, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout)

1398{

1399#ifdef CONFIG\_UART\_ASYNC\_API

1400 const struct uart\_driver\_api \*api =

1401 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1402

1403 return api->rx\_enable(dev, buf, len, timeout);

1404#else

1405 ARG\_UNUSED(dev);

1406 ARG\_UNUSED(buf);

1407 ARG\_UNUSED(len);

1408 ARG\_UNUSED(timeout);

1409 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

1410#endif

1411}

1412

[ 1434](group__uart__async.md#ga12d91846133351a85fa471fa90f2a0fd)\_\_syscall int [uart\_rx\_enable\_u16](group__uart__async.md#ga12d91846133351a85fa471fa90f2a0fd)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*buf,

1435 size\_t len, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout);

1436

1437static inline int z\_impl\_uart\_rx\_enable\_u16(const struct [device](structdevice.md) \*dev,

1438 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*buf, size\_t len,

1439 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout)

1440{

1441#if defined(CONFIG\_UART\_ASYNC\_API) && defined(CONFIG\_UART\_WIDE\_DATA)

1442 const struct uart\_driver\_api \*api =

1443 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1444

1445 return api->rx\_enable\_u16(dev, buf, len, timeout);

1446#else

1447 ARG\_UNUSED(dev);

1448 ARG\_UNUSED(buf);

1449 ARG\_UNUSED(len);

1450 ARG\_UNUSED(timeout);

1451 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

1452#endif

1453}

1454

[ 1475](group__uart__async.md#ga3970fe2818e214b0814ea8b73a816a6a)static inline int [uart\_rx\_buf\_rsp](group__uart__async.md#ga3970fe2818e214b0814ea8b73a816a6a)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf,

1476 size\_t len)

1477{

1478#ifdef CONFIG\_UART\_ASYNC\_API

1479 const struct uart\_driver\_api \*api =

1480 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1481

1482 return api->rx\_buf\_rsp(dev, buf, len);

1483#else

1484 ARG\_UNUSED(dev);

1485 ARG\_UNUSED(buf);

1486 ARG\_UNUSED(len);

1487 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

1488#endif

1489}

1490

[ 1512](group__uart__async.md#ga778bcfc30be853c8d320f295b34c17c0)static inline int [uart\_rx\_buf\_rsp\_u16](group__uart__async.md#ga778bcfc30be853c8d320f295b34c17c0)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*buf,

1513 size\_t len)

1514{

1515#if defined(CONFIG\_UART\_ASYNC\_API) && defined(CONFIG\_UART\_WIDE\_DATA)

1516 const struct uart\_driver\_api \*api =

1517 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1518

1519 return api->rx\_buf\_rsp\_u16(dev, buf, len);

1520#else

1521 ARG\_UNUSED(dev);

1522 ARG\_UNUSED(buf);

1523 ARG\_UNUSED(len);

1524 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

1525#endif

1526}

1527

[ 1543](group__uart__async.md#gafd4753bee51b230091a3c6ddb26ea734)\_\_syscall int [uart\_rx\_disable](group__uart__async.md#gafd4753bee51b230091a3c6ddb26ea734)(const struct [device](structdevice.md) \*dev);

1544

1545static inline int z\_impl\_uart\_rx\_disable(const struct [device](structdevice.md) \*dev)

1546{

1547#ifdef CONFIG\_UART\_ASYNC\_API

1548 const struct uart\_driver\_api \*api =

1549 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1550

1551 return api->rx\_disable(dev);

1552#else

1553 ARG\_UNUSED(dev);

1554 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

1555#endif

1556}

1557

1561

[ 1574](group__uart__interface.md#gab039414b41145dc8d31349836da91263)\_\_syscall int [uart\_line\_ctrl\_set](group__uart__interface.md#gab039414b41145dc8d31349836da91263)(const struct [device](structdevice.md) \*dev,

1575 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ctrl, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val);

1576

1577static inline int z\_impl\_uart\_line\_ctrl\_set(const struct [device](structdevice.md) \*dev,

1578 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ctrl, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val)

1579{

1580#ifdef CONFIG\_UART\_LINE\_CTRL

1581 const struct uart\_driver\_api \*api =

1582 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1583

1584 if (api->line\_ctrl\_set == NULL) {

1585 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1586 }

1587 return api->line\_ctrl\_set(dev, ctrl, val);

1588#else

1589 ARG\_UNUSED(dev);

1590 ARG\_UNUSED(ctrl);

1591 ARG\_UNUSED(val);

1592 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

1593#endif

1594}

1595

[ 1608](group__uart__interface.md#gafda8a550284a54c8e1d6b6638de978e5)\_\_syscall int [uart\_line\_ctrl\_get](group__uart__interface.md#gafda8a550284a54c8e1d6b6638de978e5)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ctrl,

1609 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*val);

1610

1611static inline int z\_impl\_uart\_line\_ctrl\_get(const struct [device](structdevice.md) \*dev,

1612 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ctrl, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*val)

1613{

1614#ifdef CONFIG\_UART\_LINE\_CTRL

1615 const struct uart\_driver\_api \*api =

1616 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1617

1618 if (api->line\_ctrl\_get == NULL) {

1619 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1620 }

1621 return api->line\_ctrl\_get(dev, ctrl, val);

1622#else

1623 ARG\_UNUSED(dev);

1624 ARG\_UNUSED(ctrl);

1625 ARG\_UNUSED(val);

1626 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

1627#endif

1628}

1629

[ 1645](group__uart__interface.md#gaa8683398e5d709b513509d08841ed51b)\_\_syscall int [uart\_drv\_cmd](group__uart__interface.md#gaa8683398e5d709b513509d08841ed51b)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) p);

1646

1647static inline int z\_impl\_uart\_drv\_cmd(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),

1648 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) p)

1649{

1650#ifdef CONFIG\_UART\_DRV\_CMD

1651 const struct uart\_driver\_api \*api =

1652 (const struct uart\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1653

1654 if (api->drv\_cmd == NULL) {

1655 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

1656 }

1657 return api->drv\_cmd(dev, [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), p);

1658#else

1659 ARG\_UNUSED(dev);

1660 ARG\_UNUSED([cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615));

1661 ARG\_UNUSED(p);

1662 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

1663#endif

1664}

1665

1666#ifdef \_\_cplusplus

1667}

1668#endif

1669

1673

1674#include <zephyr/syscalls/uart.h>

1675

1676#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_UART\_H\_ \*/

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

**Definition** errno.h:82

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:114

[uart\_callback\_t](group__uart__async.md#ga00b7c98a4da3ea3675d0a40c5dacb136)

void(\* uart\_callback\_t)(const struct device \*dev, struct uart\_event \*evt, void \*user\_data)

Define the application callback function signature for uart\_callback\_set() function.

**Definition** uart.h:324

[uart\_rx\_enable\_u16](group__uart__async.md#ga12d91846133351a85fa471fa90f2a0fd)

int uart\_rx\_enable\_u16(const struct device \*dev, uint16\_t \*buf, size\_t len, int32\_t timeout)

Start receiving wide data through UART.

[uart\_rx\_buf\_rsp](group__uart__async.md#ga3970fe2818e214b0814ea8b73a816a6a)

static int uart\_rx\_buf\_rsp(const struct device \*dev, uint8\_t \*buf, size\_t len)

Provide receive buffer in response to UART\_RX\_BUF\_REQUEST event.

**Definition** uart.h:1475

[uart\_rx\_buf\_rsp\_u16](group__uart__async.md#ga778bcfc30be853c8d320f295b34c17c0)

static int uart\_rx\_buf\_rsp\_u16(const struct device \*dev, uint16\_t \*buf, size\_t len)

Provide wide data receive buffer in response to UART\_RX\_BUF\_REQUEST event.

**Definition** uart.h:1512

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

**Definition** uart.h:1244

[uart\_event\_type](group__uart__async.md#gaf0c9513cbafa36d86b4c83f2b6a03dcd)

uart\_event\_type

Types of events passed to callback in UART\_ASYNC\_API.

**Definition** uart.h:207

[uart\_tx](group__uart__async.md#gaf99f32ce2e2d9beb32a2f2e5a26320dc)

int uart\_tx(const struct device \*dev, const uint8\_t \*buf, size\_t len, int32\_t timeout)

Send given number of bytes from buffer through UART.

[uart\_rx\_disable](group__uart__async.md#gafd4753bee51b230091a3c6ddb26ea734)

int uart\_rx\_disable(const struct device \*dev)

Disable RX.

[UART\_RX\_STOPPED](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda05b81ddf74d208aeabace6ac90ae52dd)

@ UART\_RX\_STOPPED

RX has stopped due to external event.

**Definition** uart.h:258

[UART\_TX\_ABORTED](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0abcf565ba1011815285bb3845f8d5a1)

@ UART\_TX\_ABORTED

Transmitting aborted due to timeout or uart\_tx\_abort call.

**Definition** uart.h:217

[UART\_RX\_BUF\_REQUEST](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0d250f372702526f1bce6d4dfe166abe)

@ UART\_RX\_BUF\_REQUEST

Driver requests next buffer for continuous reception.

**Definition** uart.h:240

[UART\_TX\_DONE](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda4b5cdf863d8b6e5cd7b58f611808a6e4)

@ UART\_TX\_DONE

Whole TX buffer was transmitted.

**Definition** uart.h:209

[UART\_RX\_RDY](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7)

@ UART\_RX\_RDY

Received data is ready for processing.

**Definition** uart.h:228

[UART\_RX\_DISABLED](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcdaa8ff5629c002a61bc3bdf5baa2ebc203)

@ UART\_RX\_DISABLED

RX has been disabled and can be reenabled.

**Definition** uart.h:252

[UART\_RX\_BUF\_RELEASED](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcdab2d152bd84f659d4fc4060df29811b48)

@ UART\_RX\_BUF\_RELEASED

Buffer is no longer used by UART driver.

**Definition** uart.h:244

[uart\_line\_ctrl](group__uart__interface.md#ga02552532e171e789efc1b000917a9be0)

uart\_line\_ctrl

Line control signals.

**Definition** uart.h:35

[uart\_err\_check](group__uart__interface.md#ga22ea20fd8e07153b3b71cc9416f5462f)

int uart\_err\_check(const struct device \*dev)

Check whether an error was detected.

[uart\_config\_get](group__uart__interface.md#ga81dfc5f2134de8e4acb5f063512cf703)

int uart\_config\_get(const struct device \*dev, struct uart\_config \*cfg)

Get UART configuration.

[uart\_config\_flow\_control](group__uart__interface.md#ga8e2f1b4a8d60d7a6c24835d1b26f99e8)

uart\_config\_flow\_control

Hardware flow control options.

**Definition** uart.h:111

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

**Definition** uart.h:79

[uart\_config\_data\_bits](group__uart__interface.md#gab9f7de744a68a311330576d7da02c44a)

uart\_config\_data\_bits

Number of data bits.

**Definition** uart.h:96

[uart\_rx\_stop\_reason](group__uart__interface.md#gadeba6c5485e01dfc1c8a6e1c21668a88)

uart\_rx\_stop\_reason

Reception stop reasons.

**Definition** uart.h:49

[uart\_config\_stop\_bits](group__uart__interface.md#gafc1aecb863e2456d73b78a49fcbad72e)

uart\_config\_stop\_bits

Number of stop bits.

**Definition** uart.h:88

[uart\_line\_ctrl\_get](group__uart__interface.md#gafda8a550284a54c8e1d6b6638de978e5)

int uart\_line\_ctrl\_get(const struct device \*dev, uint32\_t ctrl, uint32\_t \*val)

Retrieve line control for UART.

[UART\_LINE\_CTRL\_DTR](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a19e76af9901fc0274a9e27ff40e29e23)

@ UART\_LINE\_CTRL\_DTR

Data Terminal Ready (DTR).

**Definition** uart.h:38

[UART\_LINE\_CTRL\_RTS](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a205d22bd797ab1c55323dc1ffda75f0d)

@ UART\_LINE\_CTRL\_RTS

Request To Send (RTS).

**Definition** uart.h:37

[UART\_LINE\_CTRL\_BAUD\_RATE](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a3fdd02679f4f103190f3c12ab3cda00b)

@ UART\_LINE\_CTRL\_BAUD\_RATE

Baud rate.

**Definition** uart.h:36

[UART\_LINE\_CTRL\_DCD](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a6d2c438044dd64f5cef07bbe4c6b3e97)

@ UART\_LINE\_CTRL\_DCD

Data Carrier Detect (DCD).

**Definition** uart.h:39

[UART\_LINE\_CTRL\_DSR](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a87d8bedb5c918c182b271884ee42d75c)

@ UART\_LINE\_CTRL\_DSR

Data Set Ready (DSR).

**Definition** uart.h:40

[UART\_CFG\_FLOW\_CTRL\_DTR\_DSR](group__uart__interface.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a0efc5de86bf80119f750cf372814309f)

@ UART\_CFG\_FLOW\_CTRL\_DTR\_DSR

DTR/DSR flow control.

**Definition** uart.h:114

[UART\_CFG\_FLOW\_CTRL\_NONE](group__uart__interface.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a546b28db6f8bfc26266e8f7d6b8ff973)

@ UART\_CFG\_FLOW\_CTRL\_NONE

No flow control.

**Definition** uart.h:112

[UART\_CFG\_FLOW\_CTRL\_RS485](group__uart__interface.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a9675cc80d44e980b66e99bc8548f085c)

@ UART\_CFG\_FLOW\_CTRL\_RS485

RS485 flow control.

**Definition** uart.h:115

[UART\_CFG\_FLOW\_CTRL\_RTS\_CTS](group__uart__interface.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8ad682bfe14a9f0860d1fdc3e8e9d56f86)

@ UART\_CFG\_FLOW\_CTRL\_RTS\_CTS

RTS/CTS flow control.

**Definition** uart.h:113

[UART\_CFG\_PARITY\_MARK](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711a5ee61c29a32447644ff70385158a11ca)

@ UART\_CFG\_PARITY\_MARK

Mark parity.

**Definition** uart.h:83

[UART\_CFG\_PARITY\_NONE](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711a6a23a2ef22fb3b144648b244fff82b8d)

@ UART\_CFG\_PARITY\_NONE

No parity.

**Definition** uart.h:80

[UART\_CFG\_PARITY\_ODD](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711a8a618b0a531c8d62809e39eb56eaf5ed)

@ UART\_CFG\_PARITY\_ODD

Odd parity.

**Definition** uart.h:81

[UART\_CFG\_PARITY\_SPACE](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711a8dc5306c8ca26321431bcf22ce9b036c)

@ UART\_CFG\_PARITY\_SPACE

Space parity.

**Definition** uart.h:84

[UART\_CFG\_PARITY\_EVEN](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711ac3a4310efe198a1fa7d977a5531486ba)

@ UART\_CFG\_PARITY\_EVEN

Even parity.

**Definition** uart.h:82

[UART\_CFG\_DATA\_BITS\_5](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aa1b0545c2d1970e67d697b62510bfbe27)

@ UART\_CFG\_DATA\_BITS\_5

5 data bits

**Definition** uart.h:97

[UART\_CFG\_DATA\_BITS\_8](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aa23f55bdb24b4016c8c23c518e981df97)

@ UART\_CFG\_DATA\_BITS\_8

8 data bits

**Definition** uart.h:100

[UART\_CFG\_DATA\_BITS\_7](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aa6120eb8f668b257c8c2dd0dc9cf0c913)

@ UART\_CFG\_DATA\_BITS\_7

7 data bits

**Definition** uart.h:99

[UART\_CFG\_DATA\_BITS\_6](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aac6e0f3c0479164c34144d0e6e28298e4)

@ UART\_CFG\_DATA\_BITS\_6

6 data bits

**Definition** uart.h:98

[UART\_CFG\_DATA\_BITS\_9](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aaf3b601af696d8841fe79871ca3e41e5f)

@ UART\_CFG\_DATA\_BITS\_9

9 data bits

**Definition** uart.h:101

[UART\_ERROR\_NOISE](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a412058adbf7668b7051efb8419984d60)

@ UART\_ERROR\_NOISE

Noise error.

**Definition** uart.h:75

[UART\_ERROR\_OVERRUN](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a442beffc51cdf265bbcb40810a9a6e54)

@ UART\_ERROR\_OVERRUN

Overrun error.

**Definition** uart.h:51

[UART\_BREAK](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a4986147e23cc46ab8c2aa7e151d09571)

@ UART\_BREAK

Break interrupt.

**Definition** uart.h:63

[UART\_ERROR\_PARITY](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a86d38eac5a46e6659aa765164b833eb5)

@ UART\_ERROR\_PARITY

Parity error.

**Definition** uart.h:53

[UART\_ERROR\_COLLISION](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88aad8ca4dca9a846560293df71e6b39786)

@ UART\_ERROR\_COLLISION

Collision error.

**Definition** uart.h:73

[UART\_ERROR\_FRAMING](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88af13f72a8c615b4bc570b5a4df573407b)

@ UART\_ERROR\_FRAMING

Framing error.

**Definition** uart.h:55

[UART\_CFG\_STOP\_BITS\_1\_5](group__uart__interface.md#ggafc1aecb863e2456d73b78a49fcbad72ea1da47ec95b6a6eee65abef3d6d84f9ad)

@ UART\_CFG\_STOP\_BITS\_1\_5

1.5 stop bits

**Definition** uart.h:91

[UART\_CFG\_STOP\_BITS\_0\_5](group__uart__interface.md#ggafc1aecb863e2456d73b78a49fcbad72ea308c660590a9fd16143806e8bef002af)

@ UART\_CFG\_STOP\_BITS\_0\_5

0.5 stop bit

**Definition** uart.h:89

[UART\_CFG\_STOP\_BITS\_1](group__uart__interface.md#ggafc1aecb863e2456d73b78a49fcbad72ea73024f1618eb04385bf488214c635e58)

@ UART\_CFG\_STOP\_BITS\_1

1 stop bit

**Definition** uart.h:90

[UART\_CFG\_STOP\_BITS\_2](group__uart__interface.md#ggafc1aecb863e2456d73b78a49fcbad72eae180ecebc76516e89669e1d16bfb31c6)

@ UART\_CFG\_STOP\_BITS\_2

2 stop bits

**Definition** uart.h:92

[uart\_irq\_is\_pending](group__uart__interrupt.md#ga11ccae917c8b5fd76aaabdb047125f6a)

int uart\_irq\_is\_pending(const struct device \*dev)

Check if any IRQs is pending.

[uart\_fifo\_read\_u16](group__uart__interrupt.md#ga4a3c25dad2290f1f40e4b847e3b83f64)

static int uart\_fifo\_read\_u16(const struct device \*dev, uint16\_t \*rx\_data, const int size)

Read wide data from FIFO.

**Definition** uart.h:841

[uart\_irq\_rx\_enable](group__uart__interrupt.md#ga4ec3ae3974da2b3ab94ae7b835d17bad)

void uart\_irq\_rx\_enable(const struct device \*dev)

Enable RX interrupt.

[uart\_irq\_tx\_ready](group__uart__interrupt.md#ga5e126b5f19549eb7f5b785b98ebe7638)

static int uart\_irq\_tx\_ready(const struct device \*dev)

Check if UART TX buffer can accept a new char.

**Definition** uart.h:922

[uart\_irq\_callback\_set](group__uart__interrupt.md#ga5f7af3f7f0d9155349ea3b4fad78956c)

static int uart\_irq\_callback\_set(const struct device \*dev, uart\_irq\_callback\_user\_data\_t cb)

Set the IRQ callback function pointer (legacy).

**Definition** uart.h:1214

[uart\_irq\_config\_func\_t](group__uart__interrupt.md#ga6750414923953c84fb1e19177ec74ae0)

void(\* uart\_irq\_config\_func\_t)(const struct device \*dev)

For configuring IRQ on each individual UART device.

**Definition** uart.h:149

[uart\_irq\_err\_enable](group__uart__interrupt.md#ga7c24daae3326bc2959ea13a2be79969f)

void uart\_irq\_err\_enable(const struct device \*dev)

Enable error interrupt.

[uart\_irq\_tx\_complete](group__uart__interrupt.md#ga917935a13bf6a5d1e32ef34339e96455)

static int uart\_irq\_tx\_complete(const struct device \*dev)

Check if UART TX block finished transmission.

**Definition** uart.h:1000

[uart\_irq\_tx\_enable](group__uart__interrupt.md#ga9cbd6e33dce6a5b06233cf10077e19cc)

void uart\_irq\_tx\_enable(const struct device \*dev)

Enable TX interrupt in IER.

[uart\_irq\_rx\_disable](group__uart__interrupt.md#gaa759d7935fdd9ab6ca0761f161389a29)

void uart\_irq\_rx\_disable(const struct device \*dev)

Disable RX interrupt.

[uart\_fifo\_fill\_u16](group__uart__interrupt.md#gaa89f58818d8428ad6a11abf692c54c0d)

static int uart\_fifo\_fill\_u16(const struct device \*dev, const uint16\_t \*tx\_data, int size)

Fill FIFO with wide data.

**Definition** uart.h:758

[uart\_irq\_err\_disable](group__uart__interrupt.md#gaaf8a88361807e204f7227fbd1d0e75b2)

void uart\_irq\_err\_disable(const struct device \*dev)

Disable error interrupt.

[uart\_fifo\_read](group__uart__interrupt.md#gab10942076ac47ecff29e924098049398)

static int uart\_fifo\_read(const struct device \*dev, uint8\_t \*rx\_data, const int size)

Read data from FIFO.

**Definition** uart.h:800

[uart\_irq\_update](group__uart__interrupt.md#gac5241e000d482c40b2a4856c58c106a6)

int uart\_irq\_update(const struct device \*dev)

Start processing interrupts in ISR.

[uart\_irq\_rx\_ready](group__uart__interrupt.md#gad04073b1b8e3de13b43ae1194561377b)

static int uart\_irq\_rx\_ready(const struct device \*dev)

Check if UART RX buffer has a received char.

**Definition** uart.h:1036

[uart\_irq\_callback\_user\_data\_t](group__uart__interrupt.md#gad7a26b1a1d6212d7d39c05c8ad4ec926)

void(\* uart\_irq\_callback\_user\_data\_t)(const struct device \*dev, void \*user\_data)

Define the application callback function signature for uart\_irq\_callback\_user\_data\_set() function.

**Definition** uart.h:141

[uart\_irq\_callback\_user\_data\_set](group__uart__interrupt.md#gaf469966a56d1fc9f50108201597ee0a0)

static int uart\_irq\_callback\_user\_data\_set(const struct device \*dev, uart\_irq\_callback\_user\_data\_t cb, void \*user\_data)

Set the IRQ callback function pointer.

**Definition** uart.h:1179

[uart\_irq\_tx\_disable](group__uart__interrupt.md#gaf8a5bc26cd7c32e7bc6516c6f873c45a)

void uart\_irq\_tx\_disable(const struct device \*dev)

Disable TX interrupt in IER.

[uart\_fifo\_fill](group__uart__interrupt.md#gafe42e4719eada7e25904bc9ebfe87791)

static int uart\_fifo\_fill(const struct device \*dev, const uint8\_t \*tx\_data, int size)

Fill FIFO with data.

**Definition** uart.h:717

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

**Definition** device.h:403

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:409

[uart\_config](structuart__config.md)

UART controller configuration structure.

**Definition** uart.h:121

[uart\_config::stop\_bits](structuart__config.md#a7b98cd63c531110dc3dc99e94db73642)

uint8\_t stop\_bits

Stop bits, use uart\_config\_stop\_bits.

**Definition** uart.h:124

[uart\_config::parity](structuart__config.md#a9371728729252797880de052aae01089)

uint8\_t parity

Parity bit, use uart\_config\_parity.

**Definition** uart.h:123

[uart\_config::data\_bits](structuart__config.md#a93ee24cf6669fb4cfece78a53d3ec6c5)

uint8\_t data\_bits

Data bits, use uart\_config\_data\_bits.

**Definition** uart.h:125

[uart\_config::baudrate](structuart__config.md#ab532159a689e8f38c2465ce2d1fef354)

uint32\_t baudrate

Baudrate setting in bps.

**Definition** uart.h:122

[uart\_config::flow\_ctrl](structuart__config.md#af259c5efab532920b5cce7ae57f6af5e)

uint8\_t flow\_ctrl

Flow control setting, use uart\_config\_flow\_control.

**Definition** uart.h:126

[uart\_event\_rx\_buf](structuart__event__rx__buf.md)

UART RX buffer released event data.

**Definition** uart.h:285

[uart\_event\_rx\_buf::buf](structuart__event__rx__buf.md#a2547c84b742f454cfedf1de6d433297b)

uint8\_t \* buf

Pointer to buffer that is no longer in use.

**Definition** uart.h:287

[uart\_event\_rx\_stop](structuart__event__rx__stop.md)

UART RX stopped data.

**Definition** uart.h:291

[uart\_event\_rx\_stop::data](structuart__event__rx__stop.md#a1b361c8b7e17d1304a475235e734db48)

struct uart\_event\_rx data

Last received data.

**Definition** uart.h:295

[uart\_event\_rx\_stop::reason](structuart__event__rx__stop.md#a96fbae85208d9b3ea0382e7e236a932d)

enum uart\_rx\_stop\_reason reason

Reason why receiving stopped.

**Definition** uart.h:293

[uart\_event\_rx](structuart__event__rx.md)

UART RX event data.

**Definition** uart.h:275

[uart\_event\_rx::buf](structuart__event__rx.md#a2d9dfa9d9b25ff976cf2e937c72eb245)

uint8\_t \* buf

Pointer to current buffer.

**Definition** uart.h:277

[uart\_event\_rx::len](structuart__event__rx.md#a96414b96e63503336f8cf0d2249cd3bd)

size\_t len

Number of new bytes received.

**Definition** uart.h:281

[uart\_event\_rx::offset](structuart__event__rx.md#aa483e719298c30b9f5e6c57d3d161281)

size\_t offset

Currently received data offset in bytes.

**Definition** uart.h:279

[uart\_event\_tx](structuart__event__tx.md)

UART TX event data.

**Definition** uart.h:262

[uart\_event\_tx::buf](structuart__event__tx.md#a314a676a4050b2438b6f41485656bdbd)

const uint8\_t \* buf

Pointer to current buffer.

**Definition** uart.h:264

[uart\_event\_tx::len](structuart__event__tx.md#a7d844b2c0833d24accf82d58ee3408ff)

size\_t len

Number of bytes sent.

**Definition** uart.h:266

[uart\_event](structuart__event.md)

Structure containing information about current event.

**Definition** uart.h:299

[uart\_event::data](structuart__event.md#a07e3eebb7642ab52c73baba514704c69)

union uart\_event::uart\_event\_data data

[uart\_event::type](structuart__event.md#a2fb82a30e414a74943067cd0784f4b44)

enum uart\_event\_type type

Type of event.

**Definition** uart.h:301

[uart\_event::uart\_event\_data](unionuart__event_1_1uart__event__data.md)

Event data.

**Definition** uart.h:303

[uart\_event::uart\_event\_data::tx](unionuart__event_1_1uart__event__data.md#a79fb6b799d5574c6aa38a211e020035f)

struct uart\_event\_tx tx

UART\_TX\_DONE and UART\_TX\_ABORTED events data.

**Definition** uart.h:305

[uart\_event::uart\_event\_data::rx\_stop](unionuart__event_1_1uart__event__data.md#aad7488a2a3d91cea0ea874a08d7b88f6)

struct uart\_event\_rx\_stop rx\_stop

UART\_RX\_STOPPED event data.

**Definition** uart.h:311

[uart\_event::uart\_event\_data::rx\_buf](unionuart__event_1_1uart__event__data.md#ac03cdaeccba5f693337fa19299101863)

struct uart\_event\_rx\_buf rx\_buf

UART\_RX\_BUF\_RELEASED event data.

**Definition** uart.h:309

[uart\_event::uart\_event\_data::rx](unionuart__event_1_1uart__event__data.md#afac00624290b8fe5cf7b59516567b972)

struct uart\_event\_rx rx

UART\_RX\_RDY event data.

**Definition** uart.h:307

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [uart.h](drivers_2uart_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
