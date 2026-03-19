---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/drivers_2uart_8h_source.html
original_path: doxygen/html/drivers_2uart_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

25#include <stddef.h>

26

27#include <[zephyr/device.h](device_8h.md)>

28

29#ifdef \_\_cplusplus

30extern "C" {

31#endif

32

[ 34](group__uart__interface.md#ga02552532e171e789efc1b000917a9be0)enum [uart\_line\_ctrl](group__uart__interface.md#ga02552532e171e789efc1b000917a9be0) {

[ 35](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a3fdd02679f4f103190f3c12ab3cda00b) [UART\_LINE\_CTRL\_BAUD\_RATE](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a3fdd02679f4f103190f3c12ab3cda00b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 36](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a205d22bd797ab1c55323dc1ffda75f0d) [UART\_LINE\_CTRL\_RTS](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a205d22bd797ab1c55323dc1ffda75f0d) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 37](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a19e76af9901fc0274a9e27ff40e29e23) [UART\_LINE\_CTRL\_DTR](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a19e76af9901fc0274a9e27ff40e29e23) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 38](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a6d2c438044dd64f5cef07bbe4c6b3e97) [UART\_LINE\_CTRL\_DCD](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a6d2c438044dd64f5cef07bbe4c6b3e97) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

[ 39](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a87d8bedb5c918c182b271884ee42d75c) [UART\_LINE\_CTRL\_DSR](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a87d8bedb5c918c182b271884ee42d75c) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

40};

41

[ 48](group__uart__interface.md#gadeba6c5485e01dfc1c8a6e1c21668a88)enum [uart\_rx\_stop\_reason](group__uart__interface.md#gadeba6c5485e01dfc1c8a6e1c21668a88) {

[ 50](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a442beffc51cdf265bbcb40810a9a6e54) [UART\_ERROR\_OVERRUN](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a442beffc51cdf265bbcb40810a9a6e54) = (1 << 0),

[ 52](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a86d38eac5a46e6659aa765164b833eb5) [UART\_ERROR\_PARITY](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a86d38eac5a46e6659aa765164b833eb5) = (1 << 1),

[ 54](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88af13f72a8c615b4bc570b5a4df573407b) [UART\_ERROR\_FRAMING](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88af13f72a8c615b4bc570b5a4df573407b) = (1 << 2),

[ 62](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a4986147e23cc46ab8c2aa7e151d09571) [UART\_BREAK](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a4986147e23cc46ab8c2aa7e151d09571) = (1 << 3),

[ 72](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88aad8ca4dca9a846560293df71e6b39786) [UART\_ERROR\_COLLISION](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88aad8ca4dca9a846560293df71e6b39786) = (1 << 4),

[ 74](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a412058adbf7668b7051efb8419984d60) [UART\_ERROR\_NOISE](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a412058adbf7668b7051efb8419984d60) = (1 << 5),

75};

76

[ 78](group__uart__interface.md#gab2ab6aacb6e3c43bb26d4274157e5711)enum [uart\_config\_parity](group__uart__interface.md#gab2ab6aacb6e3c43bb26d4274157e5711) {

[ 79](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711a6a23a2ef22fb3b144648b244fff82b8d) [UART\_CFG\_PARITY\_NONE](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711a6a23a2ef22fb3b144648b244fff82b8d),

[ 80](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711a8a618b0a531c8d62809e39eb56eaf5ed) [UART\_CFG\_PARITY\_ODD](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711a8a618b0a531c8d62809e39eb56eaf5ed),

[ 81](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711ac3a4310efe198a1fa7d977a5531486ba) [UART\_CFG\_PARITY\_EVEN](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711ac3a4310efe198a1fa7d977a5531486ba),

[ 82](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711a5ee61c29a32447644ff70385158a11ca) [UART\_CFG\_PARITY\_MARK](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711a5ee61c29a32447644ff70385158a11ca),

[ 83](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711a8dc5306c8ca26321431bcf22ce9b036c) [UART\_CFG\_PARITY\_SPACE](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711a8dc5306c8ca26321431bcf22ce9b036c),

84};

85

[ 87](group__uart__interface.md#gafc1aecb863e2456d73b78a49fcbad72e)enum [uart\_config\_stop\_bits](group__uart__interface.md#gafc1aecb863e2456d73b78a49fcbad72e) {

[ 88](group__uart__interface.md#ggafc1aecb863e2456d73b78a49fcbad72ea308c660590a9fd16143806e8bef002af) [UART\_CFG\_STOP\_BITS\_0\_5](group__uart__interface.md#ggafc1aecb863e2456d73b78a49fcbad72ea308c660590a9fd16143806e8bef002af),

[ 89](group__uart__interface.md#ggafc1aecb863e2456d73b78a49fcbad72ea73024f1618eb04385bf488214c635e58) [UART\_CFG\_STOP\_BITS\_1](group__uart__interface.md#ggafc1aecb863e2456d73b78a49fcbad72ea73024f1618eb04385bf488214c635e58),

[ 90](group__uart__interface.md#ggafc1aecb863e2456d73b78a49fcbad72ea1da47ec95b6a6eee65abef3d6d84f9ad) [UART\_CFG\_STOP\_BITS\_1\_5](group__uart__interface.md#ggafc1aecb863e2456d73b78a49fcbad72ea1da47ec95b6a6eee65abef3d6d84f9ad),

[ 91](group__uart__interface.md#ggafc1aecb863e2456d73b78a49fcbad72eae180ecebc76516e89669e1d16bfb31c6) [UART\_CFG\_STOP\_BITS\_2](group__uart__interface.md#ggafc1aecb863e2456d73b78a49fcbad72eae180ecebc76516e89669e1d16bfb31c6),

92};

93

[ 95](group__uart__interface.md#gab9f7de744a68a311330576d7da02c44a)enum [uart\_config\_data\_bits](group__uart__interface.md#gab9f7de744a68a311330576d7da02c44a) {

[ 96](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aa1b0545c2d1970e67d697b62510bfbe27) [UART\_CFG\_DATA\_BITS\_5](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aa1b0545c2d1970e67d697b62510bfbe27),

[ 97](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aac6e0f3c0479164c34144d0e6e28298e4) [UART\_CFG\_DATA\_BITS\_6](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aac6e0f3c0479164c34144d0e6e28298e4),

[ 98](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aa6120eb8f668b257c8c2dd0dc9cf0c913) [UART\_CFG\_DATA\_BITS\_7](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aa6120eb8f668b257c8c2dd0dc9cf0c913),

[ 99](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aa23f55bdb24b4016c8c23c518e981df97) [UART\_CFG\_DATA\_BITS\_8](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aa23f55bdb24b4016c8c23c518e981df97),

[ 100](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aaf3b601af696d8841fe79871ca3e41e5f) [UART\_CFG\_DATA\_BITS\_9](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aaf3b601af696d8841fe79871ca3e41e5f),

101};

102

[ 110](group__uart__interface.md#ga8e2f1b4a8d60d7a6c24835d1b26f99e8)enum [uart\_config\_flow\_control](group__uart__interface.md#ga8e2f1b4a8d60d7a6c24835d1b26f99e8) {

[ 111](group__uart__interface.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a546b28db6f8bfc26266e8f7d6b8ff973) [UART\_CFG\_FLOW\_CTRL\_NONE](group__uart__interface.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a546b28db6f8bfc26266e8f7d6b8ff973),

[ 112](group__uart__interface.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8ad682bfe14a9f0860d1fdc3e8e9d56f86) [UART\_CFG\_FLOW\_CTRL\_RTS\_CTS](group__uart__interface.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8ad682bfe14a9f0860d1fdc3e8e9d56f86),

[ 113](group__uart__interface.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a0efc5de86bf80119f750cf372814309f) [UART\_CFG\_FLOW\_CTRL\_DTR\_DSR](group__uart__interface.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a0efc5de86bf80119f750cf372814309f),

[ 114](group__uart__interface.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a9675cc80d44e980b66e99bc8548f085c) [UART\_CFG\_FLOW\_CTRL\_RS485](group__uart__interface.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a9675cc80d44e980b66e99bc8548f085c),

115};

116

[ 120](structuart__config.md)struct [uart\_config](structuart__config.md) {

[ 121](structuart__config.md#ab532159a689e8f38c2465ce2d1fef354) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [baudrate](structuart__config.md#ab532159a689e8f38c2465ce2d1fef354);

[ 122](structuart__config.md#a9371728729252797880de052aae01089) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [parity](structuart__config.md#a9371728729252797880de052aae01089);

[ 123](structuart__config.md#a7b98cd63c531110dc3dc99e94db73642) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [stop\_bits](structuart__config.md#a7b98cd63c531110dc3dc99e94db73642);

[ 124](structuart__config.md#a93ee24cf6669fb4cfece78a53d3ec6c5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data\_bits](structuart__config.md#a93ee24cf6669fb4cfece78a53d3ec6c5);

[ 125](structuart__config.md#af259c5efab532920b5cce7ae57f6af5e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flow\_ctrl](structuart__config.md#af259c5efab532920b5cce7ae57f6af5e);

126};

127

132

[ 140](group__uart__interrupt.md#gad7a26b1a1d6212d7d39c05c8ad4ec926)typedef void (\*[uart\_irq\_callback\_user\_data\_t](group__uart__interrupt.md#gad7a26b1a1d6212d7d39c05c8ad4ec926))(const struct [device](structdevice.md) \*dev,

141 void \*user\_data);

142

151

[ 199](group__uart__async.md#gaf0c9513cbafa36d86b4c83f2b6a03dcd)enum [uart\_event\_type](group__uart__async.md#gaf0c9513cbafa36d86b4c83f2b6a03dcd) {

[ 201](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda4b5cdf863d8b6e5cd7b58f611808a6e4) [UART\_TX\_DONE](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda4b5cdf863d8b6e5cd7b58f611808a6e4),

[ 209](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0abcf565ba1011815285bb3845f8d5a1) [UART\_TX\_ABORTED](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0abcf565ba1011815285bb3845f8d5a1),

[ 220](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7) [UART\_RX\_RDY](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7),

[ 232](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0d250f372702526f1bce6d4dfe166abe) [UART\_RX\_BUF\_REQUEST](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0d250f372702526f1bce6d4dfe166abe),

[ 236](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcdab2d152bd84f659d4fc4060df29811b48) [UART\_RX\_BUF\_RELEASED](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcdab2d152bd84f659d4fc4060df29811b48),

[ 244](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcdaa8ff5629c002a61bc3bdf5baa2ebc203) [UART\_RX\_DISABLED](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcdaa8ff5629c002a61bc3bdf5baa2ebc203),

[ 250](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda05b81ddf74d208aeabace6ac90ae52dd) [UART\_RX\_STOPPED](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda05b81ddf74d208aeabace6ac90ae52dd),

251};

252

[ 254](structuart__event__tx.md)struct [uart\_event\_tx](structuart__event__tx.md) {

[ 256](structuart__event__tx.md#a314a676a4050b2438b6f41485656bdbd) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structuart__event__tx.md#a314a676a4050b2438b6f41485656bdbd);

[ 258](structuart__event__tx.md#a7d844b2c0833d24accf82d58ee3408ff) size\_t [len](structuart__event__tx.md#a7d844b2c0833d24accf82d58ee3408ff);

259};

260

[ 267](structuart__event__rx.md)struct [uart\_event\_rx](structuart__event__rx.md) {

[ 269](structuart__event__rx.md#a2d9dfa9d9b25ff976cf2e937c72eb245) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structuart__event__rx.md#a2d9dfa9d9b25ff976cf2e937c72eb245);

[ 271](structuart__event__rx.md#aa483e719298c30b9f5e6c57d3d161281) size\_t [offset](structuart__event__rx.md#aa483e719298c30b9f5e6c57d3d161281);

[ 273](structuart__event__rx.md#a96414b96e63503336f8cf0d2249cd3bd) size\_t [len](structuart__event__rx.md#a96414b96e63503336f8cf0d2249cd3bd);

274};

275

[ 277](structuart__event__rx__buf.md)struct [uart\_event\_rx\_buf](structuart__event__rx__buf.md) {

[ 279](structuart__event__rx__buf.md#a2547c84b742f454cfedf1de6d433297b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structuart__event__rx__buf.md#a2547c84b742f454cfedf1de6d433297b);

280};

281

[ 283](structuart__event__rx__stop.md)struct [uart\_event\_rx\_stop](structuart__event__rx__stop.md) {

[ 285](structuart__event__rx__stop.md#a96fbae85208d9b3ea0382e7e236a932d) enum [uart\_rx\_stop\_reason](group__uart__interface.md#gadeba6c5485e01dfc1c8a6e1c21668a88) [reason](structuart__event__rx__stop.md#a96fbae85208d9b3ea0382e7e236a932d);

[ 287](structuart__event__rx__stop.md#a1b361c8b7e17d1304a475235e734db48) struct [uart\_event\_rx](structuart__event__rx.md) [data](structuart__event__rx__stop.md#a1b361c8b7e17d1304a475235e734db48);

288};

289

[ 291](structuart__event.md)struct [uart\_event](structuart__event.md) {

[ 293](structuart__event.md#a2fb82a30e414a74943067cd0784f4b44) enum [uart\_event\_type](group__uart__async.md#gaf0c9513cbafa36d86b4c83f2b6a03dcd) [type](structuart__event.md#a2fb82a30e414a74943067cd0784f4b44);

[ 295](unionuart__event_1_1uart__event__data.md) union [uart\_event\_data](unionuart__event_1_1uart__event__data.md) {

[ 297](unionuart__event_1_1uart__event__data.md#a79fb6b799d5574c6aa38a211e020035f) struct [uart\_event\_tx](structuart__event__tx.md) [tx](unionuart__event_1_1uart__event__data.md#a79fb6b799d5574c6aa38a211e020035f);

[ 299](unionuart__event_1_1uart__event__data.md#afac00624290b8fe5cf7b59516567b972) struct [uart\_event\_rx](structuart__event__rx.md) [rx](unionuart__event_1_1uart__event__data.md#afac00624290b8fe5cf7b59516567b972);

[ 301](unionuart__event_1_1uart__event__data.md#ac03cdaeccba5f693337fa19299101863) struct [uart\_event\_rx\_buf](structuart__event__rx__buf.md) [rx\_buf](unionuart__event_1_1uart__event__data.md#ac03cdaeccba5f693337fa19299101863);

[ 303](unionuart__event_1_1uart__event__data.md#aad7488a2a3d91cea0ea874a08d7b88f6) struct [uart\_event\_rx\_stop](structuart__event__rx__stop.md) [rx\_stop](unionuart__event_1_1uart__event__data.md#aad7488a2a3d91cea0ea874a08d7b88f6);

[ 304](structuart__event.md#a07e3eebb7642ab52c73baba514704c69) } [data](structuart__event.md#a07e3eebb7642ab52c73baba514704c69);

305};

306

[ 316](group__uart__async.md#ga00b7c98a4da3ea3675d0a40c5dacb136)typedef void (\*[uart\_callback\_t](group__uart__async.md#ga00b7c98a4da3ea3675d0a40c5dacb136))(const struct [device](structdevice.md) \*dev,

317 struct [uart\_event](structuart__event.md) \*evt, void \*user\_data);

318

322

[ 332](group__uart__interface.md#ga22ea20fd8e07153b3b71cc9416f5462f)\_\_syscall int [uart\_err\_check](group__uart__interface.md#ga22ea20fd8e07153b3b71cc9416f5462f)(const struct [device](structdevice.md) \*dev);

333

338

[ 357](group__uart__polling.md#gae81ac8cc976a20d774cfbda09e9c983d)\_\_syscall int [uart\_poll\_in](group__uart__polling.md#gae81ac8cc976a20d774cfbda09e9c983d)(const struct [device](structdevice.md) \*dev, unsigned char \*p\_char);

358

[ 378](group__uart__polling.md#gaad39c1358019bfdcb919da7982743553)\_\_syscall int [uart\_poll\_in\_u16](group__uart__polling.md#gaad39c1358019bfdcb919da7982743553)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*p\_u16);

379

[ 395](group__uart__polling.md#ga06ba27ba772a7a18462b8cdbc7f9353c)\_\_syscall void [uart\_poll\_out](group__uart__polling.md#ga06ba27ba772a7a18462b8cdbc7f9353c)(const struct [device](structdevice.md) \*dev,

396 unsigned char out\_char);

397

[ 412](group__uart__polling.md#ga8faa3f58b9098c97e288e9c5f3367fd9)\_\_syscall void [uart\_poll\_out\_u16](group__uart__polling.md#ga8faa3f58b9098c97e288e9c5f3367fd9)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) out\_u16);

413

417

[ 432](group__uart__interface.md#gaa0b75777b879af10543f7e8f463ff9a2)\_\_syscall int [uart\_configure](group__uart__interface.md#gaa0b75777b879af10543f7e8f463ff9a2)(const struct [device](structdevice.md) \*dev,

433 const struct [uart\_config](structuart__config.md) \*cfg);

434

[ 449](group__uart__interface.md#ga81dfc5f2134de8e4acb5f063512cf703)\_\_syscall int [uart\_config\_get](group__uart__interface.md#ga81dfc5f2134de8e4acb5f063512cf703)(const struct [device](structdevice.md) \*dev,

450 struct [uart\_config](structuart__config.md) \*cfg);

451

456

[ 477](group__uart__interrupt.md#gafe42e4719eada7e25904bc9ebfe87791)static inline int [uart\_fifo\_fill](group__uart__interrupt.md#gafe42e4719eada7e25904bc9ebfe87791)(const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*tx\_data, int size);

478

[ 499](group__uart__interrupt.md#gaa89f58818d8428ad6a11abf692c54c0d)static inline int [uart\_fifo\_fill\_u16](group__uart__interrupt.md#gaa89f58818d8428ad6a11abf692c54c0d)(const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*tx\_data, int size);

500

[ 522](group__uart__interrupt.md#gab10942076ac47ecff29e924098049398)static inline int [uart\_fifo\_read](group__uart__interrupt.md#gab10942076ac47ecff29e924098049398)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rx\_data, const int size);

523

[ 545](group__uart__interrupt.md#ga4a3c25dad2290f1f40e4b847e3b83f64)static inline int [uart\_fifo\_read\_u16](group__uart__interrupt.md#ga4a3c25dad2290f1f40e4b847e3b83f64)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*rx\_data, const int size);

546

[ 552](group__uart__interrupt.md#ga9cbd6e33dce6a5b06233cf10077e19cc)\_\_syscall void [uart\_irq\_tx\_enable](group__uart__interrupt.md#ga9cbd6e33dce6a5b06233cf10077e19cc)(const struct [device](structdevice.md) \*dev);

553

[ 559](group__uart__interrupt.md#gaf8a5bc26cd7c32e7bc6516c6f873c45a)\_\_syscall void [uart\_irq\_tx\_disable](group__uart__interrupt.md#gaf8a5bc26cd7c32e7bc6516c6f873c45a)(const struct [device](structdevice.md) \*dev);

560

[ 581](group__uart__interrupt.md#ga5e126b5f19549eb7f5b785b98ebe7638)static inline int [uart\_irq\_tx\_ready](group__uart__interrupt.md#ga5e126b5f19549eb7f5b785b98ebe7638)(const struct [device](structdevice.md) \*dev);

582

[ 588](group__uart__interrupt.md#ga4ec3ae3974da2b3ab94ae7b835d17bad)\_\_syscall void [uart\_irq\_rx\_enable](group__uart__interrupt.md#ga4ec3ae3974da2b3ab94ae7b835d17bad)(const struct [device](structdevice.md) \*dev);

589

[ 595](group__uart__interrupt.md#gaa759d7935fdd9ab6ca0761f161389a29)\_\_syscall void [uart\_irq\_rx\_disable](group__uart__interrupt.md#gaa759d7935fdd9ab6ca0761f161389a29)(const struct [device](structdevice.md) \*dev);

596

[ 616](group__uart__interrupt.md#ga917935a13bf6a5d1e32ef34339e96455)static inline int [uart\_irq\_tx\_complete](group__uart__interrupt.md#ga917935a13bf6a5d1e32ef34339e96455)(const struct [device](structdevice.md) \*dev);

617

[ 638](group__uart__interrupt.md#gad04073b1b8e3de13b43ae1194561377b)static inline int [uart\_irq\_rx\_ready](group__uart__interrupt.md#gad04073b1b8e3de13b43ae1194561377b)(const struct [device](structdevice.md) \*dev);

639

[ 645](group__uart__interrupt.md#ga7c24daae3326bc2959ea13a2be79969f)\_\_syscall void [uart\_irq\_err\_enable](group__uart__interrupt.md#ga7c24daae3326bc2959ea13a2be79969f)(const struct [device](structdevice.md) \*dev);

646

[ 652](group__uart__interrupt.md#gaaf8a88361807e204f7227fbd1d0e75b2)\_\_syscall void [uart\_irq\_err\_disable](group__uart__interrupt.md#gaaf8a88361807e204f7227fbd1d0e75b2)(const struct [device](structdevice.md) \*dev);

653

[ 664](group__uart__interrupt.md#ga11ccae917c8b5fd76aaabdb047125f6a)\_\_syscall int [uart\_irq\_is\_pending](group__uart__interrupt.md#ga11ccae917c8b5fd76aaabdb047125f6a)(const struct [device](structdevice.md) \*dev);

665

[ 691](group__uart__interrupt.md#gac5241e000d482c40b2a4856c58c106a6)\_\_syscall int [uart\_irq\_update](group__uart__interrupt.md#gac5241e000d482c40b2a4856c58c106a6)(const struct [device](structdevice.md) \*dev);

692

[ 708](group__uart__interrupt.md#gaf469966a56d1fc9f50108201597ee0a0)static inline int [uart\_irq\_callback\_user\_data\_set](group__uart__interrupt.md#gaf469966a56d1fc9f50108201597ee0a0)(const struct [device](structdevice.md) \*dev,

709 [uart\_irq\_callback\_user\_data\_t](group__uart__interrupt.md#gad7a26b1a1d6212d7d39c05c8ad4ec926) cb,

710 void \*user\_data);

711

[ 725](group__uart__interrupt.md#ga5f7af3f7f0d9155349ea3b4fad78956c)static inline int [uart\_irq\_callback\_set](group__uart__interrupt.md#ga5f7af3f7f0d9155349ea3b4fad78956c)(const struct [device](structdevice.md) \*dev,

726 [uart\_irq\_callback\_user\_data\_t](group__uart__interrupt.md#gad7a26b1a1d6212d7d39c05c8ad4ec926) cb);

727

731

736

[ 752](group__uart__async.md#gad33e627ed8729409b14e92453e53459c)static inline int [uart\_callback\_set](group__uart__async.md#gad33e627ed8729409b14e92453e53459c)(const struct [device](structdevice.md) \*dev,

753 [uart\_callback\_t](group__uart__async.md#ga00b7c98a4da3ea3675d0a40c5dacb136) callback,

754 void \*user\_data);

755

[ 773](group__uart__async.md#gaf99f32ce2e2d9beb32a2f2e5a26320dc)\_\_syscall int [uart\_tx](group__uart__async.md#gaf99f32ce2e2d9beb32a2f2e5a26320dc)(const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf,

774 size\_t len,

775 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout);

776

[ 794](group__uart__async.md#gab0ea611cd072fa459a6f1780ce62c9e3)\_\_syscall int [uart\_tx\_u16](group__uart__async.md#gab0ea611cd072fa459a6f1780ce62c9e3)(const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*buf,

795 size\_t len, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout);

796

[ 809](group__uart__async.md#gaa8a26d3ea685fb98030ea03613be6280)\_\_syscall int [uart\_tx\_abort](group__uart__async.md#gaa8a26d3ea685fb98030ea03613be6280)(const struct [device](structdevice.md) \*dev);

810

[ 832](group__uart__async.md#ga902e18c2a727ed2988e1b6caa6a444b8)\_\_syscall int [uart\_rx\_enable](group__uart__async.md#ga902e18c2a727ed2988e1b6caa6a444b8)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf,

833 size\_t len,

834 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout);

835

[ 857](group__uart__async.md#ga12d91846133351a85fa471fa90f2a0fd)\_\_syscall int [uart\_rx\_enable\_u16](group__uart__async.md#ga12d91846133351a85fa471fa90f2a0fd)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*buf,

858 size\_t len, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout);

859

[ 880](group__uart__async.md#ga3970fe2818e214b0814ea8b73a816a6a)static inline int [uart\_rx\_buf\_rsp](group__uart__async.md#ga3970fe2818e214b0814ea8b73a816a6a)(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf,

881 size\_t len);

882

[ 904](group__uart__async.md#ga778bcfc30be853c8d320f295b34c17c0)static inline int [uart\_rx\_buf\_rsp\_u16](group__uart__async.md#ga778bcfc30be853c8d320f295b34c17c0)(const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*buf,

905 size\_t len);

906

[ 922](group__uart__async.md#gafd4753bee51b230091a3c6ddb26ea734)\_\_syscall int [uart\_rx\_disable](group__uart__async.md#gafd4753bee51b230091a3c6ddb26ea734)(const struct [device](structdevice.md) \*dev);

923

927

[ 940](group__uart__interface.md#gab039414b41145dc8d31349836da91263)\_\_syscall int [uart\_line\_ctrl\_set](group__uart__interface.md#gab039414b41145dc8d31349836da91263)(const struct [device](structdevice.md) \*dev,

941 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ctrl, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val);

942

[ 955](group__uart__interface.md#gafda8a550284a54c8e1d6b6638de978e5)\_\_syscall int [uart\_line\_ctrl\_get](group__uart__interface.md#gafda8a550284a54c8e1d6b6638de978e5)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ctrl,

956 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*val);

957

[ 973](group__uart__interface.md#gaa8683398e5d709b513509d08841ed51b)\_\_syscall int [uart\_drv\_cmd](group__uart__interface.md#gaa8683398e5d709b513509d08841ed51b)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) p);

974

975#ifdef \_\_cplusplus

976}

977#endif

978

982

983#include <[zephyr/drivers/uart/uart\_internal.h](uart__internal_8h.md)>

984#include <zephyr/syscalls/uart.h>

985

986#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_UART\_H\_ \*/

[device.h](device_8h.md)

[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)

static void cmd(uint32\_t command)

Execute a display list command by co-processor engine.

**Definition** ft8xx\_reference\_api.h:153

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[uart\_callback\_t](group__uart__async.md#ga00b7c98a4da3ea3675d0a40c5dacb136)

void(\* uart\_callback\_t)(const struct device \*dev, struct uart\_event \*evt, void \*user\_data)

Define the application callback function signature for uart\_callback\_set() function.

**Definition** uart.h:316

[uart\_rx\_enable\_u16](group__uart__async.md#ga12d91846133351a85fa471fa90f2a0fd)

int uart\_rx\_enable\_u16(const struct device \*dev, uint16\_t \*buf, size\_t len, int32\_t timeout)

Start receiving wide data through UART.

[uart\_rx\_buf\_rsp](group__uart__async.md#ga3970fe2818e214b0814ea8b73a816a6a)

static int uart\_rx\_buf\_rsp(const struct device \*dev, uint8\_t \*buf, size\_t len)

Provide receive buffer in response to UART\_RX\_BUF\_REQUEST event.

[uart\_rx\_buf\_rsp\_u16](group__uart__async.md#ga778bcfc30be853c8d320f295b34c17c0)

static int uart\_rx\_buf\_rsp\_u16(const struct device \*dev, uint16\_t \*buf, size\_t len)

Provide wide data receive buffer in response to UART\_RX\_BUF\_REQUEST event.

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

[uart\_event\_type](group__uart__async.md#gaf0c9513cbafa36d86b4c83f2b6a03dcd)

uart\_event\_type

Types of events passed to callback in UART\_ASYNC\_API.

**Definition** uart.h:199

[uart\_tx](group__uart__async.md#gaf99f32ce2e2d9beb32a2f2e5a26320dc)

int uart\_tx(const struct device \*dev, const uint8\_t \*buf, size\_t len, int32\_t timeout)

Send given number of bytes from buffer through UART.

[uart\_rx\_disable](group__uart__async.md#gafd4753bee51b230091a3c6ddb26ea734)

int uart\_rx\_disable(const struct device \*dev)

Disable RX.

[UART\_RX\_STOPPED](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda05b81ddf74d208aeabace6ac90ae52dd)

@ UART\_RX\_STOPPED

RX has stopped due to external event.

**Definition** uart.h:250

[UART\_TX\_ABORTED](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0abcf565ba1011815285bb3845f8d5a1)

@ UART\_TX\_ABORTED

Transmitting aborted due to timeout or uart\_tx\_abort call.

**Definition** uart.h:209

[UART\_RX\_BUF\_REQUEST](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0d250f372702526f1bce6d4dfe166abe)

@ UART\_RX\_BUF\_REQUEST

Driver requests next buffer for continuous reception.

**Definition** uart.h:232

[UART\_TX\_DONE](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda4b5cdf863d8b6e5cd7b58f611808a6e4)

@ UART\_TX\_DONE

Whole TX buffer was transmitted.

**Definition** uart.h:201

[UART\_RX\_RDY](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7)

@ UART\_RX\_RDY

Received data is ready for processing.

**Definition** uart.h:220

[UART\_RX\_DISABLED](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcdaa8ff5629c002a61bc3bdf5baa2ebc203)

@ UART\_RX\_DISABLED

RX has been disabled and can be reenabled.

**Definition** uart.h:244

[UART\_RX\_BUF\_RELEASED](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcdab2d152bd84f659d4fc4060df29811b48)

@ UART\_RX\_BUF\_RELEASED

Buffer is no longer used by UART driver.

**Definition** uart.h:236

[uart\_line\_ctrl](group__uart__interface.md#ga02552532e171e789efc1b000917a9be0)

uart\_line\_ctrl

Line control signals.

**Definition** uart.h:34

[uart\_err\_check](group__uart__interface.md#ga22ea20fd8e07153b3b71cc9416f5462f)

int uart\_err\_check(const struct device \*dev)

Check whether an error was detected.

[uart\_config\_get](group__uart__interface.md#ga81dfc5f2134de8e4acb5f063512cf703)

int uart\_config\_get(const struct device \*dev, struct uart\_config \*cfg)

Get UART configuration.

[uart\_config\_flow\_control](group__uart__interface.md#ga8e2f1b4a8d60d7a6c24835d1b26f99e8)

uart\_config\_flow\_control

Hardware flow control options.

**Definition** uart.h:110

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

**Definition** uart.h:78

[uart\_config\_data\_bits](group__uart__interface.md#gab9f7de744a68a311330576d7da02c44a)

uart\_config\_data\_bits

Number of data bits.

**Definition** uart.h:95

[uart\_rx\_stop\_reason](group__uart__interface.md#gadeba6c5485e01dfc1c8a6e1c21668a88)

uart\_rx\_stop\_reason

Reception stop reasons.

**Definition** uart.h:48

[uart\_config\_stop\_bits](group__uart__interface.md#gafc1aecb863e2456d73b78a49fcbad72e)

uart\_config\_stop\_bits

Number of stop bits.

**Definition** uart.h:87

[uart\_line\_ctrl\_get](group__uart__interface.md#gafda8a550284a54c8e1d6b6638de978e5)

int uart\_line\_ctrl\_get(const struct device \*dev, uint32\_t ctrl, uint32\_t \*val)

Retrieve line control for UART.

[UART\_LINE\_CTRL\_DTR](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a19e76af9901fc0274a9e27ff40e29e23)

@ UART\_LINE\_CTRL\_DTR

Data Terminal Ready (DTR).

**Definition** uart.h:37

[UART\_LINE\_CTRL\_RTS](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a205d22bd797ab1c55323dc1ffda75f0d)

@ UART\_LINE\_CTRL\_RTS

Request To Send (RTS).

**Definition** uart.h:36

[UART\_LINE\_CTRL\_BAUD\_RATE](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a3fdd02679f4f103190f3c12ab3cda00b)

@ UART\_LINE\_CTRL\_BAUD\_RATE

Baud rate.

**Definition** uart.h:35

[UART\_LINE\_CTRL\_DCD](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a6d2c438044dd64f5cef07bbe4c6b3e97)

@ UART\_LINE\_CTRL\_DCD

Data Carrier Detect (DCD).

**Definition** uart.h:38

[UART\_LINE\_CTRL\_DSR](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a87d8bedb5c918c182b271884ee42d75c)

@ UART\_LINE\_CTRL\_DSR

Data Set Ready (DSR).

**Definition** uart.h:39

[UART\_CFG\_FLOW\_CTRL\_DTR\_DSR](group__uart__interface.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a0efc5de86bf80119f750cf372814309f)

@ UART\_CFG\_FLOW\_CTRL\_DTR\_DSR

DTR/DSR flow control.

**Definition** uart.h:113

[UART\_CFG\_FLOW\_CTRL\_NONE](group__uart__interface.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a546b28db6f8bfc26266e8f7d6b8ff973)

@ UART\_CFG\_FLOW\_CTRL\_NONE

No flow control.

**Definition** uart.h:111

[UART\_CFG\_FLOW\_CTRL\_RS485](group__uart__interface.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a9675cc80d44e980b66e99bc8548f085c)

@ UART\_CFG\_FLOW\_CTRL\_RS485

RS485 flow control.

**Definition** uart.h:114

[UART\_CFG\_FLOW\_CTRL\_RTS\_CTS](group__uart__interface.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8ad682bfe14a9f0860d1fdc3e8e9d56f86)

@ UART\_CFG\_FLOW\_CTRL\_RTS\_CTS

RTS/CTS flow control.

**Definition** uart.h:112

[UART\_CFG\_PARITY\_MARK](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711a5ee61c29a32447644ff70385158a11ca)

@ UART\_CFG\_PARITY\_MARK

Mark parity.

**Definition** uart.h:82

[UART\_CFG\_PARITY\_NONE](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711a6a23a2ef22fb3b144648b244fff82b8d)

@ UART\_CFG\_PARITY\_NONE

No parity.

**Definition** uart.h:79

[UART\_CFG\_PARITY\_ODD](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711a8a618b0a531c8d62809e39eb56eaf5ed)

@ UART\_CFG\_PARITY\_ODD

Odd parity.

**Definition** uart.h:80

[UART\_CFG\_PARITY\_SPACE](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711a8dc5306c8ca26321431bcf22ce9b036c)

@ UART\_CFG\_PARITY\_SPACE

Space parity.

**Definition** uart.h:83

[UART\_CFG\_PARITY\_EVEN](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711ac3a4310efe198a1fa7d977a5531486ba)

@ UART\_CFG\_PARITY\_EVEN

Even parity.

**Definition** uart.h:81

[UART\_CFG\_DATA\_BITS\_5](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aa1b0545c2d1970e67d697b62510bfbe27)

@ UART\_CFG\_DATA\_BITS\_5

5 data bits

**Definition** uart.h:96

[UART\_CFG\_DATA\_BITS\_8](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aa23f55bdb24b4016c8c23c518e981df97)

@ UART\_CFG\_DATA\_BITS\_8

8 data bits

**Definition** uart.h:99

[UART\_CFG\_DATA\_BITS\_7](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aa6120eb8f668b257c8c2dd0dc9cf0c913)

@ UART\_CFG\_DATA\_BITS\_7

7 data bits

**Definition** uart.h:98

[UART\_CFG\_DATA\_BITS\_6](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aac6e0f3c0479164c34144d0e6e28298e4)

@ UART\_CFG\_DATA\_BITS\_6

6 data bits

**Definition** uart.h:97

[UART\_CFG\_DATA\_BITS\_9](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aaf3b601af696d8841fe79871ca3e41e5f)

@ UART\_CFG\_DATA\_BITS\_9

9 data bits

**Definition** uart.h:100

[UART\_ERROR\_NOISE](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a412058adbf7668b7051efb8419984d60)

@ UART\_ERROR\_NOISE

Noise error.

**Definition** uart.h:74

[UART\_ERROR\_OVERRUN](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a442beffc51cdf265bbcb40810a9a6e54)

@ UART\_ERROR\_OVERRUN

Overrun error.

**Definition** uart.h:50

[UART\_BREAK](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a4986147e23cc46ab8c2aa7e151d09571)

@ UART\_BREAK

Break interrupt.

**Definition** uart.h:62

[UART\_ERROR\_PARITY](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a86d38eac5a46e6659aa765164b833eb5)

@ UART\_ERROR\_PARITY

Parity error.

**Definition** uart.h:52

[UART\_ERROR\_COLLISION](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88aad8ca4dca9a846560293df71e6b39786)

@ UART\_ERROR\_COLLISION

Collision error.

**Definition** uart.h:72

[UART\_ERROR\_FRAMING](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88af13f72a8c615b4bc570b5a4df573407b)

@ UART\_ERROR\_FRAMING

Framing error.

**Definition** uart.h:54

[UART\_CFG\_STOP\_BITS\_1\_5](group__uart__interface.md#ggafc1aecb863e2456d73b78a49fcbad72ea1da47ec95b6a6eee65abef3d6d84f9ad)

@ UART\_CFG\_STOP\_BITS\_1\_5

1.5 stop bits

**Definition** uart.h:90

[UART\_CFG\_STOP\_BITS\_0\_5](group__uart__interface.md#ggafc1aecb863e2456d73b78a49fcbad72ea308c660590a9fd16143806e8bef002af)

@ UART\_CFG\_STOP\_BITS\_0\_5

0.5 stop bit

**Definition** uart.h:88

[UART\_CFG\_STOP\_BITS\_1](group__uart__interface.md#ggafc1aecb863e2456d73b78a49fcbad72ea73024f1618eb04385bf488214c635e58)

@ UART\_CFG\_STOP\_BITS\_1

1 stop bit

**Definition** uart.h:89

[UART\_CFG\_STOP\_BITS\_2](group__uart__interface.md#ggafc1aecb863e2456d73b78a49fcbad72eae180ecebc76516e89669e1d16bfb31c6)

@ UART\_CFG\_STOP\_BITS\_2

2 stop bits

**Definition** uart.h:91

[uart\_irq\_is\_pending](group__uart__interrupt.md#ga11ccae917c8b5fd76aaabdb047125f6a)

int uart\_irq\_is\_pending(const struct device \*dev)

Check if any IRQs is pending.

[uart\_fifo\_read\_u16](group__uart__interrupt.md#ga4a3c25dad2290f1f40e4b847e3b83f64)

static int uart\_fifo\_read\_u16(const struct device \*dev, uint16\_t \*rx\_data, const int size)

Read wide data from FIFO.

[uart\_irq\_rx\_enable](group__uart__interrupt.md#ga4ec3ae3974da2b3ab94ae7b835d17bad)

void uart\_irq\_rx\_enable(const struct device \*dev)

Enable RX interrupt.

[uart\_irq\_tx\_ready](group__uart__interrupt.md#ga5e126b5f19549eb7f5b785b98ebe7638)

static int uart\_irq\_tx\_ready(const struct device \*dev)

Check if UART TX buffer can accept bytes.

[uart\_irq\_callback\_set](group__uart__interrupt.md#ga5f7af3f7f0d9155349ea3b4fad78956c)

static int uart\_irq\_callback\_set(const struct device \*dev, uart\_irq\_callback\_user\_data\_t cb)

Set the IRQ callback function pointer (legacy).

[uart\_irq\_err\_enable](group__uart__interrupt.md#ga7c24daae3326bc2959ea13a2be79969f)

void uart\_irq\_err\_enable(const struct device \*dev)

Enable error interrupt.

[uart\_irq\_tx\_complete](group__uart__interrupt.md#ga917935a13bf6a5d1e32ef34339e96455)

static int uart\_irq\_tx\_complete(const struct device \*dev)

Check if UART TX block finished transmission.

[uart\_irq\_tx\_enable](group__uart__interrupt.md#ga9cbd6e33dce6a5b06233cf10077e19cc)

void uart\_irq\_tx\_enable(const struct device \*dev)

Enable TX interrupt in IER.

[uart\_irq\_rx\_disable](group__uart__interrupt.md#gaa759d7935fdd9ab6ca0761f161389a29)

void uart\_irq\_rx\_disable(const struct device \*dev)

Disable RX interrupt.

[uart\_fifo\_fill\_u16](group__uart__interrupt.md#gaa89f58818d8428ad6a11abf692c54c0d)

static int uart\_fifo\_fill\_u16(const struct device \*dev, const uint16\_t \*tx\_data, int size)

Fill FIFO with wide data.

[uart\_irq\_err\_disable](group__uart__interrupt.md#gaaf8a88361807e204f7227fbd1d0e75b2)

void uart\_irq\_err\_disable(const struct device \*dev)

Disable error interrupt.

[uart\_fifo\_read](group__uart__interrupt.md#gab10942076ac47ecff29e924098049398)

static int uart\_fifo\_read(const struct device \*dev, uint8\_t \*rx\_data, const int size)

Read data from FIFO.

[uart\_irq\_update](group__uart__interrupt.md#gac5241e000d482c40b2a4856c58c106a6)

int uart\_irq\_update(const struct device \*dev)

Start processing interrupts in ISR.

[uart\_irq\_rx\_ready](group__uart__interrupt.md#gad04073b1b8e3de13b43ae1194561377b)

static int uart\_irq\_rx\_ready(const struct device \*dev)

Check if UART RX buffer has a received char.

[uart\_irq\_callback\_user\_data\_t](group__uart__interrupt.md#gad7a26b1a1d6212d7d39c05c8ad4ec926)

void(\* uart\_irq\_callback\_user\_data\_t)(const struct device \*dev, void \*user\_data)

Define the application callback function signature for uart\_irq\_callback\_user\_data\_set() function.

**Definition** uart.h:140

[uart\_irq\_callback\_user\_data\_set](group__uart__interrupt.md#gaf469966a56d1fc9f50108201597ee0a0)

static int uart\_irq\_callback\_user\_data\_set(const struct device \*dev, uart\_irq\_callback\_user\_data\_t cb, void \*user\_data)

Set the IRQ callback function pointer.

[uart\_irq\_tx\_disable](group__uart__interrupt.md#gaf8a5bc26cd7c32e7bc6516c6f873c45a)

void uart\_irq\_tx\_disable(const struct device \*dev)

Disable TX interrupt in IER.

[uart\_fifo\_fill](group__uart__interrupt.md#gafe42e4719eada7e25904bc9ebfe87791)

static int uart\_fifo\_fill(const struct device \*dev, const uint8\_t \*tx\_data, int size)

Fill FIFO with data.

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

**Definition** device.h:453

[uart\_config](structuart__config.md)

UART controller configuration structure.

**Definition** uart.h:120

[uart\_config::stop\_bits](structuart__config.md#a7b98cd63c531110dc3dc99e94db73642)

uint8\_t stop\_bits

Stop bits, use uart\_config\_stop\_bits.

**Definition** uart.h:123

[uart\_config::parity](structuart__config.md#a9371728729252797880de052aae01089)

uint8\_t parity

Parity bit, use uart\_config\_parity.

**Definition** uart.h:122

[uart\_config::data\_bits](structuart__config.md#a93ee24cf6669fb4cfece78a53d3ec6c5)

uint8\_t data\_bits

Data bits, use uart\_config\_data\_bits.

**Definition** uart.h:124

[uart\_config::baudrate](structuart__config.md#ab532159a689e8f38c2465ce2d1fef354)

uint32\_t baudrate

Baudrate setting in bps.

**Definition** uart.h:121

[uart\_config::flow\_ctrl](structuart__config.md#af259c5efab532920b5cce7ae57f6af5e)

uint8\_t flow\_ctrl

Flow control setting, use uart\_config\_flow\_control.

**Definition** uart.h:125

[uart\_event\_rx\_buf](structuart__event__rx__buf.md)

UART RX buffer released event data.

**Definition** uart.h:277

[uart\_event\_rx\_buf::buf](structuart__event__rx__buf.md#a2547c84b742f454cfedf1de6d433297b)

uint8\_t \* buf

Pointer to buffer that is no longer in use.

**Definition** uart.h:279

[uart\_event\_rx\_stop](structuart__event__rx__stop.md)

UART RX stopped data.

**Definition** uart.h:283

[uart\_event\_rx\_stop::data](structuart__event__rx__stop.md#a1b361c8b7e17d1304a475235e734db48)

struct uart\_event\_rx data

Last received data.

**Definition** uart.h:287

[uart\_event\_rx\_stop::reason](structuart__event__rx__stop.md#a96fbae85208d9b3ea0382e7e236a932d)

enum uart\_rx\_stop\_reason reason

Reason why receiving stopped.

**Definition** uart.h:285

[uart\_event\_rx](structuart__event__rx.md)

UART RX event data.

**Definition** uart.h:267

[uart\_event\_rx::buf](structuart__event__rx.md#a2d9dfa9d9b25ff976cf2e937c72eb245)

uint8\_t \* buf

Pointer to current buffer.

**Definition** uart.h:269

[uart\_event\_rx::len](structuart__event__rx.md#a96414b96e63503336f8cf0d2249cd3bd)

size\_t len

Number of new bytes received.

**Definition** uart.h:273

[uart\_event\_rx::offset](structuart__event__rx.md#aa483e719298c30b9f5e6c57d3d161281)

size\_t offset

Currently received data offset in bytes.

**Definition** uart.h:271

[uart\_event\_tx](structuart__event__tx.md)

UART TX event data.

**Definition** uart.h:254

[uart\_event\_tx::buf](structuart__event__tx.md#a314a676a4050b2438b6f41485656bdbd)

const uint8\_t \* buf

Pointer to current buffer.

**Definition** uart.h:256

[uart\_event\_tx::len](structuart__event__tx.md#a7d844b2c0833d24accf82d58ee3408ff)

size\_t len

Number of bytes sent.

**Definition** uart.h:258

[uart\_event](structuart__event.md)

Structure containing information about current event.

**Definition** uart.h:291

[uart\_event::data](structuart__event.md#a07e3eebb7642ab52c73baba514704c69)

union uart\_event::uart\_event\_data data

[uart\_event::type](structuart__event.md#a2fb82a30e414a74943067cd0784f4b44)

enum uart\_event\_type type

Type of event.

**Definition** uart.h:293

[uart\_internal.h](uart__internal_8h.md)

Internal APIs for UART drivers.

[uart\_event::uart\_event\_data](unionuart__event_1_1uart__event__data.md)

Event data.

**Definition** uart.h:295

[uart\_event::uart\_event\_data::tx](unionuart__event_1_1uart__event__data.md#a79fb6b799d5574c6aa38a211e020035f)

struct uart\_event\_tx tx

UART\_TX\_DONE and UART\_TX\_ABORTED events data.

**Definition** uart.h:297

[uart\_event::uart\_event\_data::rx\_stop](unionuart__event_1_1uart__event__data.md#aad7488a2a3d91cea0ea874a08d7b88f6)

struct uart\_event\_rx\_stop rx\_stop

UART\_RX\_STOPPED event data.

**Definition** uart.h:303

[uart\_event::uart\_event\_data::rx\_buf](unionuart__event_1_1uart__event__data.md#ac03cdaeccba5f693337fa19299101863)

struct uart\_event\_rx\_buf rx\_buf

UART\_RX\_BUF\_RELEASED event data.

**Definition** uart.h:301

[uart\_event::uart\_event\_data::rx](unionuart__event_1_1uart__event__data.md#afac00624290b8fe5cf7b59516567b972)

struct uart\_event\_rx rx

UART\_RX\_RDY event data.

**Definition** uart.h:299

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [uart.h](drivers_2uart_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
