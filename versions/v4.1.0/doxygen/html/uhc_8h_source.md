---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/uhc_8h_source.html
original_path: doxygen/html/uhc_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uhc.h

[Go to the documentation of this file.](uhc_8h.md)

1/\*

2 \* Copyright (c) 2022 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_UHC\_H

13#define ZEPHYR\_INCLUDE\_UHC\_H

14

15#include <[zephyr/kernel.h](kernel_8h.md)>

16#include <[zephyr/device.h](device_8h.md)>

17#include <[zephyr/net\_buf.h](net__buf_8h.md)>

18#include <[zephyr/usb/usb\_ch9.h](usb__ch9_8h.md)>

19#include <[zephyr/sys/dlist.h](dlist_8h.md)>

20

29

[ 31](group__uhc__api.md#ga7127ac2a46b577f2aa1bb9a650e62a3f)enum [usb\_device\_state](group__uhc__api.md#ga7127ac2a46b577f2aa1bb9a650e62a3f) {

[ 32](group__uhc__api.md#gga7127ac2a46b577f2aa1bb9a650e62a3fa70367cdc7b5d7d1f3ab046391f50df9d) [USB\_STATE\_NOTCONNECTED](group__uhc__api.md#gga7127ac2a46b577f2aa1bb9a650e62a3fa70367cdc7b5d7d1f3ab046391f50df9d),

[ 33](group__uhc__api.md#gga7127ac2a46b577f2aa1bb9a650e62a3fabb0f4a1c2f62f028bec1d0b55b5d5554) [USB\_STATE\_DEFAULT](group__uhc__api.md#gga7127ac2a46b577f2aa1bb9a650e62a3fabb0f4a1c2f62f028bec1d0b55b5d5554),

[ 34](group__uhc__api.md#gga7127ac2a46b577f2aa1bb9a650e62a3fad7f0841a21d3179c13f19d3ae8a8e3b6) [USB\_STATE\_ADDRESSED](group__uhc__api.md#gga7127ac2a46b577f2aa1bb9a650e62a3fad7f0841a21d3179c13f19d3ae8a8e3b6),

[ 35](group__uhc__api.md#gga7127ac2a46b577f2aa1bb9a650e62a3fa6566e87fb6d54f2da5b7564743df7a47) [USB\_STATE\_CONFIGURED](group__uhc__api.md#gga7127ac2a46b577f2aa1bb9a650e62a3fa6566e87fb6d54f2da5b7564743df7a47),

36};

37

[ 41](group__uhc__api.md#ga59ba7bbb99177a622f3c073fc48b7bc5)enum [usb\_device\_speed](group__uhc__api.md#ga59ba7bbb99177a622f3c073fc48b7bc5) {

[ 43](group__uhc__api.md#gga59ba7bbb99177a622f3c073fc48b7bc5ac9755ae6b86f8148054fd6a342c74acc) [USB\_SPEED\_UNKNOWN](group__uhc__api.md#gga59ba7bbb99177a622f3c073fc48b7bc5ac9755ae6b86f8148054fd6a342c74acc),

[ 45](group__uhc__api.md#gga59ba7bbb99177a622f3c073fc48b7bc5a46c4232a37347ac22ac14b240abddbdc) [USB\_SPEED\_SPEED\_LS](group__uhc__api.md#gga59ba7bbb99177a622f3c073fc48b7bc5a46c4232a37347ac22ac14b240abddbdc),

[ 47](group__uhc__api.md#gga59ba7bbb99177a622f3c073fc48b7bc5a8cd687699d8afb4d818595d70b189e27) [USB\_SPEED\_SPEED\_FS](group__uhc__api.md#gga59ba7bbb99177a622f3c073fc48b7bc5a8cd687699d8afb4d818595d70b189e27),

[ 49](group__uhc__api.md#gga59ba7bbb99177a622f3c073fc48b7bc5aab0ef8e9a798d70fd3c93e68785c0968) [USB\_SPEED\_SPEED\_HS](group__uhc__api.md#gga59ba7bbb99177a622f3c073fc48b7bc5aab0ef8e9a798d70fd3c93e68785c0968),

[ 51](group__uhc__api.md#gga59ba7bbb99177a622f3c073fc48b7bc5a36e25f2ed5532d6a281abaf521583fcc) [USB\_SPEED\_SPEED\_SS](group__uhc__api.md#gga59ba7bbb99177a622f3c073fc48b7bc5a36e25f2ed5532d6a281abaf521583fcc),

52};

53

[ 54](group__uhc__api.md#ga1b1ec49cb7649ece6ec5a31dac3e2537)#define UHC\_INTERFACES\_MAX 32

55

[ 56](structusb__host__interface.md)struct [usb\_host\_interface](structusb__host__interface.md) {

[ 57](structusb__host__interface.md#aa0170523367f9e1459a9ba897c0d88bf) struct [usb\_desc\_header](structusb__desc__header.md) \*[dhp](structusb__host__interface.md#aa0170523367f9e1459a9ba897c0d88bf);

[ 58](structusb__host__interface.md#a4405cdfb6aa6fbbcd2ac27148b9ebea6) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [alternate](structusb__host__interface.md#a4405cdfb6aa6fbbcd2ac27148b9ebea6);

59};

60

[ 61](structusb__host__ep.md)struct [usb\_host\_ep](structusb__host__ep.md) {

[ 62](structusb__host__ep.md#a25e9c4004ab03927476093ed4d167dbd) struct [usb\_ep\_descriptor](structusb__ep__descriptor.md) \*[desc](structusb__host__ep.md#a25e9c4004ab03927476093ed4d167dbd);

63};

64

[ 68](structusb__device.md)struct [usb\_device](structusb__device.md) {

[ 70](structusb__device.md#a0215608e40123de4a3a79ca440c6c593) [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) [node](structusb__device.md#a0215608e40123de4a3a79ca440c6c593);

[ 72](structusb__device.md#a72ee0e53efd86c91e0cea6c7e873d5ce) void \*[ctx](structusb__device.md#a72ee0e53efd86c91e0cea6c7e873d5ce);

[ 74](structusb__device.md#a4203b2cfd65f70096a43a20c7c37de27) struct [k\_mutex](structk__mutex.md) [mutex](structusb__device.md#a4203b2cfd65f70096a43a20c7c37de27);

[ 76](structusb__device.md#a24be9609d416d3a184fdedbefa298490) struct [usb\_device\_descriptor](structusb__device__descriptor.md) [dev\_desc](structusb__device.md#a24be9609d416d3a184fdedbefa298490);

[ 78](structusb__device.md#aa75bbea6a879460b39216453323d177f) enum [usb\_device\_state](group__uhc__api.md#ga7127ac2a46b577f2aa1bb9a650e62a3f) [state](structusb__device.md#aa75bbea6a879460b39216453323d177f);

[ 80](structusb__device.md#a1b3f4becfd9fbfae80074fc2e76ea6a8) enum [usb\_device\_speed](group__uhc__api.md#ga59ba7bbb99177a622f3c073fc48b7bc5) [speed](structusb__device.md#a1b3f4becfd9fbfae80074fc2e76ea6a8);

[ 82](structusb__device.md#a101d30facb781bd410581fc6c2d3fa59) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [actual\_cfg](structusb__device.md#a101d30facb781bd410581fc6c2d3fa59);

[ 84](structusb__device.md#aa9062a5b9da663863e6d51ef2e04197b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [addr](structusb__device.md#aa9062a5b9da663863e6d51ef2e04197b);

[ 86](structusb__device.md#ac98af9fb0d5bba21bc8037a8fcfb3126) void \*[cfg\_desc](structusb__device.md#ac98af9fb0d5bba21bc8037a8fcfb3126);

[ 88](structusb__device.md#a5cccbb483d91032f4a7f25f88270747f) struct [usb\_host\_interface](structusb__host__interface.md) [ifaces](structusb__device.md#a5cccbb483d91032f4a7f25f88270747f)[[UHC\_INTERFACES\_MAX](group__uhc__api.md#ga1b1ec49cb7649ece6ec5a31dac3e2537) + 1];

[ 90](structusb__device.md#a658b9992a472574b1d88e49b7fea478d) struct [usb\_host\_ep](structusb__host__ep.md) [ep\_out](structusb__device.md#a658b9992a472574b1d88e49b7fea478d)[16];

[ 92](structusb__device.md#ad3091acb2a713b9e66c595bbf4a736a5) struct [usb\_host\_ep](structusb__host__ep.md) [ep\_in](structusb__device.md#ad3091acb2a713b9e66c595bbf4a736a5)[16];

93};

94

[ 98](group__uhc__api.md#gaef9b0703714676c1f7bd1cad57f49bc8)enum [uhc\_control\_stage](group__uhc__api.md#gaef9b0703714676c1f7bd1cad57f49bc8) {

[ 99](group__uhc__api.md#ggaef9b0703714676c1f7bd1cad57f49bc8a3f3c131b3a97a552d2917bbddcd9afc8) [UHC\_CONTROL\_STAGE\_SETUP](group__uhc__api.md#ggaef9b0703714676c1f7bd1cad57f49bc8a3f3c131b3a97a552d2917bbddcd9afc8) = 0,

[ 100](group__uhc__api.md#ggaef9b0703714676c1f7bd1cad57f49bc8a2179067786eb86aad804d0aead9d71a5) [UHC\_CONTROL\_STAGE\_DATA](group__uhc__api.md#ggaef9b0703714676c1f7bd1cad57f49bc8a2179067786eb86aad804d0aead9d71a5),

[ 101](group__uhc__api.md#ggaef9b0703714676c1f7bd1cad57f49bc8a7bd9f0423e9f50266905c3736e12468f) [UHC\_CONTROL\_STAGE\_STATUS](group__uhc__api.md#ggaef9b0703714676c1f7bd1cad57f49bc8a7bd9f0423e9f50266905c3736e12468f),

102};

103

[ 114](structuhc__transfer.md)struct [uhc\_transfer](structuhc__transfer.md) {

[ 116](structuhc__transfer.md#ae1fcb0b866e3d7c5b5ea9dff6221f37d) [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) [node](structuhc__transfer.md#ae1fcb0b866e3d7c5b5ea9dff6221f37d);

[ 118](structuhc__transfer.md#af5e8080b91078a1c9f8ff269c72d70e9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [setup\_pkt](structuhc__transfer.md#af5e8080b91078a1c9f8ff269c72d70e9)[8];

[ 120](structuhc__transfer.md#a170385b08171659f05ac7112faf8e587) struct [net\_buf](structnet__buf.md) \*[buf](structuhc__transfer.md#a170385b08171659f05ac7112faf8e587);

[ 122](structuhc__transfer.md#aaf664844dc9f1871cce3d38516c042ef) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ep](structuhc__transfer.md#aaf664844dc9f1871cce3d38516c042ef);

[ 124](structuhc__transfer.md#a61a6c74cc7c026404ccf42d1164765b8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [mps](structuhc__transfer.md#a61a6c74cc7c026404ccf42d1164765b8);

[ 126](structuhc__transfer.md#af6d6de482f092e4f85679722ad609cbf) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [interval](structuhc__transfer.md#af6d6de482f092e4f85679722ad609cbf);

[ 128](structuhc__transfer.md#a23e4115c774134ccd143189b0f4f2460) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [start\_frame](structuhc__transfer.md#a23e4115c774134ccd143189b0f4f2460);

[ 130](structuhc__transfer.md#ad2b246c850c3b30f7d2b58fc9a47008b) unsigned int [queued](structuhc__transfer.md#ad2b246c850c3b30f7d2b58fc9a47008b) : 1;

[ 132](structuhc__transfer.md#a9983482be9724e281e56c978ce27d93f) unsigned int [stage](structuhc__transfer.md#a9983482be9724e281e56c978ce27d93f) : 2;

[ 134](structuhc__transfer.md#a81a8a80809420787f4c0ab232a24a514) struct [usb\_device](structusb__device.md) \*[udev](structuhc__transfer.md#a81a8a80809420787f4c0ab232a24a514);

[ 136](structuhc__transfer.md#ad4d80a3f20cdec7dd2237a98054dd287) void \*[cb](structuhc__transfer.md#ad4d80a3f20cdec7dd2237a98054dd287);

[ 138](structuhc__transfer.md#a0f2d4a735ce224260d100dc756b1900f) void \*[priv](structuhc__transfer.md#a0f2d4a735ce224260d100dc756b1900f);

[ 140](structuhc__transfer.md#a11f002f91b1039c226b7c9feb8223e11) int [err](structuhc__transfer.md#a11f002f91b1039c226b7c9feb8223e11);

141};

142

[ 146](group__uhc__api.md#gabaf69c1e69fe0fb3d912b92daf8754eb)enum [uhc\_event\_type](group__uhc__api.md#gabaf69c1e69fe0fb3d912b92daf8754eb) {

[ 148](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebae0a316b8f60df97f30f54630f6847f70) [UHC\_EVT\_DEV\_CONNECTED\_LS](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebae0a316b8f60df97f30f54630f6847f70),

[ 150](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754eba98d87b3c737c234918fed0ce4589f4ce) [UHC\_EVT\_DEV\_CONNECTED\_FS](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754eba98d87b3c737c234918fed0ce4589f4ce),

[ 152](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754eba923b6cfe57c254e22b57eab88c84b67f) [UHC\_EVT\_DEV\_CONNECTED\_HS](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754eba923b6cfe57c254e22b57eab88c84b67f),

[ 154](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebab7c4181ad631b127cc50605f7864bc30) [UHC\_EVT\_DEV\_REMOVED](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebab7c4181ad631b127cc50605f7864bc30),

[ 156](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebafb131548cc66e748e562ee88df274ab3) [UHC\_EVT\_RESETED](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebafb131548cc66e748e562ee88df274ab3),

[ 158](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebab28885b8210133d4f0c2b532561c9c7a) [UHC\_EVT\_SUSPENDED](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebab28885b8210133d4f0c2b532561c9c7a),

[ 160](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebad874caf1d7338081d185634e12f69848) [UHC\_EVT\_RESUMED](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebad874caf1d7338081d185634e12f69848),

[ 162](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebaa616f846752aacb8029f9b21747c656e) [UHC\_EVT\_RWUP](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebaa616f846752aacb8029f9b21747c656e),

[ 164](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754eba5cdc8afb59f760c4dc9b2de314d05483) [UHC\_EVT\_EP\_REQUEST](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754eba5cdc8afb59f760c4dc9b2de314d05483),

[ 169](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebae5970877eb9b6426132d8955cdeb26d7) [UHC\_EVT\_ERROR](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebae5970877eb9b6426132d8955cdeb26d7),

170};

171

[ 180](structuhc__event.md)struct [uhc\_event](structuhc__event.md) {

[ 182](structuhc__event.md#acd04587fac14f9a8a91b75642f5b2e82) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structuhc__event.md#acd04587fac14f9a8a91b75642f5b2e82);

[ 184](structuhc__event.md#a30fddbbe0f15a16320fba3cb4fd81d84) enum [uhc\_event\_type](group__uhc__api.md#gabaf69c1e69fe0fb3d912b92daf8754eb) [type](structuhc__event.md#a30fddbbe0f15a16320fba3cb4fd81d84);

185 union {

[ 187](structuhc__event.md#a5d7e1cc1bcb25e10f009ac3a8acd94b6) int [status](structuhc__event.md#a5d7e1cc1bcb25e10f009ac3a8acd94b6);

[ 189](structuhc__event.md#a03f3cebee6edfaf620a98c198a70dbd0) struct [uhc\_transfer](structuhc__transfer.md) \*[xfer](structuhc__event.md#a03f3cebee6edfaf620a98c198a70dbd0);

190 };

[ 192](structuhc__event.md#a055be3fd47e16bc48498163be3e55d09) const struct [device](structdevice.md) \*[dev](structuhc__event.md#a055be3fd47e16bc48498163be3e55d09);

193};

194

[ 206](group__uhc__api.md#ga3cda056094ceef79dd62ad9c6852daf9)typedef int (\*[uhc\_event\_cb\_t](group__uhc__api.md#ga3cda056094ceef79dd62ad9c6852daf9))(const struct [device](structdevice.md) \*dev,

207 const struct [uhc\_event](structuhc__event.md) \*const event);

208

[ 214](structuhc__device__caps.md)struct [uhc\_device\_caps](structuhc__device__caps.md) {

[ 216](structuhc__device__caps.md#ab526337af28d25728780cb48dc43e722) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [hs](structuhc__device__caps.md#ab526337af28d25728780cb48dc43e722) : 1;

217};

218

[ 222](group__uhc__api.md#ga09ad6fc9251212fa0dffececb767ff9e)#define UHC\_STATUS\_INITIALIZED 0

[ 226](group__uhc__api.md#ga230e104bd7be1d4b83b2d31ee72ac3c4)#define UHC\_STATUS\_ENABLED 1

227

[ 234](structuhc__data.md)struct [uhc\_data](structuhc__data.md) {

[ 236](structuhc__data.md#ac2a48d1d6692931807e8985799c5bdb0) struct [uhc\_device\_caps](structuhc__device__caps.md) [caps](structuhc__data.md#ac2a48d1d6692931807e8985799c5bdb0);

[ 238](structuhc__data.md#a08772cdd5b42bd11ca4a06a75df846e9) struct [k\_mutex](structk__mutex.md) [mutex](structuhc__data.md#a08772cdd5b42bd11ca4a06a75df846e9);

[ 240](structuhc__data.md#a32eec449ffbe5e6c262c907e6e6b475a) [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) [ctrl\_xfers](structuhc__data.md#a32eec449ffbe5e6c262c907e6e6b475a);

[ 242](structuhc__data.md#ac6214566324740c34a8bba42515d1d32) [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) [bulk\_xfers](structuhc__data.md#ac6214566324740c34a8bba42515d1d32);

[ 244](structuhc__data.md#afd1a0828a0ca3e397dba09fe38fd8050) [uhc\_event\_cb\_t](group__uhc__api.md#ga3cda056094ceef79dd62ad9c6852daf9) [event\_cb](structuhc__data.md#afd1a0828a0ca3e397dba09fe38fd8050);

[ 246](structuhc__data.md#a9f4904633f530748c8e3b2ac3ad0563f) const void \*[event\_ctx](structuhc__data.md#a9f4904633f530748c8e3b2ac3ad0563f);

[ 248](structuhc__data.md#a10852f2523cc733541cc9ea51706559f) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [status](structuhc__data.md#a10852f2523cc733541cc9ea51706559f);

[ 250](structuhc__data.md#a294120f6cf8563cb9564c51fcf56d883) void \*[priv](structuhc__data.md#a294120f6cf8563cb9564c51fcf56d883);

251};

252

[ 260](group__uhc__api.md#ga3251967d36b67169d7892a615323c14e)static inline bool [uhc\_is\_initialized](group__uhc__api.md#ga3251967d36b67169d7892a615323c14e)(const struct [device](structdevice.md) \*dev)

261{

262 struct [uhc\_data](structuhc__data.md) \*data = dev->[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e);

263

264 return [atomic\_test\_bit](group__atomic__apis.md#ga190ddc108f45e7649689753c08658eae)(&data->[status](structuhc__data.md#a10852f2523cc733541cc9ea51706559f), [UHC\_STATUS\_INITIALIZED](group__uhc__api.md#ga09ad6fc9251212fa0dffececb767ff9e));

265}

266

[ 274](group__uhc__api.md#ga09b71dc5c334f09fb92cf37e2ecf51eb)static inline bool [uhc\_is\_enabled](group__uhc__api.md#ga09b71dc5c334f09fb92cf37e2ecf51eb)(const struct [device](structdevice.md) \*dev)

275{

276 struct [uhc\_data](structuhc__data.md) \*data = dev->[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e);

277

278 return [atomic\_test\_bit](group__atomic__apis.md#ga190ddc108f45e7649689753c08658eae)(&data->[status](structuhc__data.md#a10852f2523cc733541cc9ea51706559f), [UHC\_STATUS\_ENABLED](group__uhc__api.md#ga230e104bd7be1d4b83b2d31ee72ac3c4));

279}

280

284struct uhc\_api {

285 int (\*lock)(const struct device \*dev);

286 int (\*unlock)(const struct device \*dev);

287

288 int (\*init)(const struct device \*dev);

289 int (\*enable)(const struct device \*dev);

290 int (\*disable)(const struct device \*dev);

291 int (\*[shutdown](posix_2sys_2socket_8h.md#a8dadddc96fee56a9f8b0904aca02eab2))(const struct device \*dev);

292

293 int (\*bus\_reset)(const struct device \*dev);

294 int (\*sof\_enable)(const struct device \*dev);

295 int (\*bus\_suspend)(const struct device \*dev);

296 int (\*bus\_resume)(const struct device \*dev);

297

298 int (\*ep\_enqueue)(const struct device \*dev,

299 struct uhc\_transfer \*const xfer);

300 int (\*ep\_dequeue)(const struct device \*dev,

301 struct uhc\_transfer \*const xfer);

302};

306

[ 318](group__uhc__api.md#ga4ceb0400168cd53201f0dde5f596452f)static inline int [uhc\_bus\_reset](group__uhc__api.md#ga4ceb0400168cd53201f0dde5f596452f)(const struct [device](structdevice.md) \*dev)

319{

320 const struct uhc\_api \*api = dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

321 int ret;

322

323 api->lock(dev);

324 ret = api->bus\_reset(dev);

325 api->unlock(dev);

326

327 return ret;

328}

329

[ 340](group__uhc__api.md#gafe55e97cbf31d163b10616c03da39414)static inline int [uhc\_sof\_enable](group__uhc__api.md#gafe55e97cbf31d163b10616c03da39414)(const struct [device](structdevice.md) \*dev)

341{

342 const struct uhc\_api \*api = dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

343 int ret;

344

345 api->lock(dev);

346 ret = api->sof\_enable(dev);

347 api->unlock(dev);

348

349 return ret;

350}

351

[ 363](group__uhc__api.md#ga897081ff02dab4377c68bcba343f492c)static inline int [uhc\_bus\_suspend](group__uhc__api.md#ga897081ff02dab4377c68bcba343f492c)(const struct [device](structdevice.md) \*dev)

364{

365 const struct uhc\_api \*api = dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

366 int ret;

367

368 api->lock(dev);

369 ret = api->bus\_suspend(dev);

370 api->unlock(dev);

371

372 return ret;

373}

374

[ 386](group__uhc__api.md#ga6669bc2ac56395b38292fa796b99bfd9)static inline int [uhc\_bus\_resume](group__uhc__api.md#ga6669bc2ac56395b38292fa796b99bfd9)(const struct [device](structdevice.md) \*dev)

387{

388 const struct uhc\_api \*api = dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

389 int ret;

390

391 api->lock(dev);

392 ret = api->bus\_resume(dev);

393 api->unlock(dev);

394

395 return ret;

396}

397

[ 413](group__uhc__api.md#gab5a2df4d176d4c85751c3158b63e366b)struct [uhc\_transfer](structuhc__transfer.md) \*[uhc\_xfer\_alloc](group__uhc__api.md#gab5a2df4d176d4c85751c3158b63e366b)(const struct [device](structdevice.md) \*dev,

414 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ep](structuhc__transfer.md#aaf664844dc9f1871cce3d38516c042ef),

415 struct [usb\_device](structusb__device.md) \*const [udev](structuhc__transfer.md#a81a8a80809420787f4c0ab232a24a514),

416 void \*const [cb](structuhc__transfer.md#ad4d80a3f20cdec7dd2237a98054dd287),

417 void \*const cb\_priv);

418

[ 433](group__uhc__api.md#ga75c2142698a15c547ab76ab76c89c177)struct [uhc\_transfer](structuhc__transfer.md) \*[uhc\_xfer\_alloc\_with\_buf](group__uhc__api.md#ga75c2142698a15c547ab76ab76c89c177)(const struct [device](structdevice.md) \*dev,

434 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ep](structuhc__transfer.md#aaf664844dc9f1871cce3d38516c042ef),

435 struct [usb\_device](structusb__device.md) \*const [udev](structuhc__transfer.md#a81a8a80809420787f4c0ab232a24a514),

436 void \*const [cb](structuhc__transfer.md#ad4d80a3f20cdec7dd2237a98054dd287),

437 void \*const cb\_priv,

438 size\_t size);

439

[ 450](group__uhc__api.md#gab2f6328e8051559edccc05ae3552f4f9)int [uhc\_xfer\_free](group__uhc__api.md#gab2f6328e8051559edccc05ae3552f4f9)(const struct [device](structdevice.md) \*dev,

451 struct [uhc\_transfer](structuhc__transfer.md) \*const xfer);

452

[ 464](group__uhc__api.md#ga779dbd7ee8ac5fce487e087706791ea7)int [uhc\_xfer\_buf\_add](group__uhc__api.md#ga779dbd7ee8ac5fce487e087706791ea7)(const struct [device](structdevice.md) \*dev,

465 struct [uhc\_transfer](structuhc__transfer.md) \*const xfer,

466 struct [net\_buf](structnet__buf.md) \*[buf](structuhc__transfer.md#a170385b08171659f05ac7112faf8e587));

[ 478](group__uhc__api.md#gab4f7439fab8c57e203862bc408a6e46b)struct [net\_buf](structnet__buf.md) \*[uhc\_xfer\_buf\_alloc](group__uhc__api.md#gab4f7439fab8c57e203862bc408a6e46b)(const struct [device](structdevice.md) \*dev,

479 const size\_t [size](structnet__buf.md#a1522d81a002804223e25300a6961f527));

480

[ 489](group__uhc__api.md#gac4bd26a85f8abc2006ecf2622669d615)void [uhc\_xfer\_buf\_free](group__uhc__api.md#gac4bd26a85f8abc2006ecf2622669d615)(const struct [device](structdevice.md) \*dev, struct [net\_buf](structnet__buf.md) \*const buf);

490

[ 503](group__uhc__api.md#ga7a07b598c00d53393e15f6dae5cf1c4a)int [uhc\_ep\_enqueue](group__uhc__api.md#ga7a07b598c00d53393e15f6dae5cf1c4a)(const struct [device](structdevice.md) \*dev, struct [uhc\_transfer](structuhc__transfer.md) \*const xfer);

504

[ 516](group__uhc__api.md#ga7c362cba29e0181ffcc8f70060100e62)int [uhc\_ep\_dequeue](group__uhc__api.md#ga7c362cba29e0181ffcc8f70060100e62)(const struct [device](structdevice.md) \*dev, struct [uhc\_transfer](structuhc__transfer.md) \*const xfer);

517

[ 531](group__uhc__api.md#ga97beb6e3b3d4ad1b0b7664eae473e1be)int [uhc\_init](group__uhc__api.md#ga97beb6e3b3d4ad1b0b7664eae473e1be)(const struct [device](structdevice.md) \*dev,

532 [uhc\_event\_cb\_t](group__uhc__api.md#ga3cda056094ceef79dd62ad9c6852daf9) event\_cb, const void \*const event\_ctx);

533

[ 546](group__uhc__api.md#gafe94b7f9e32aada9634166ebb2115c2f)int [uhc\_enable](group__uhc__api.md#gafe94b7f9e32aada9634166ebb2115c2f)(const struct [device](structdevice.md) \*dev);

547

[ 558](group__uhc__api.md#ga9ec92df4497588adbf8da6f0777a4afd)int [uhc\_disable](group__uhc__api.md#ga9ec92df4497588adbf8da6f0777a4afd)(const struct [device](structdevice.md) \*dev);

559

[ 571](group__uhc__api.md#gac6d1feb9481882a711e58c3e55e915cb)int [uhc\_shutdown](group__uhc__api.md#gac6d1feb9481882a711e58c3e55e915cb)(const struct [device](structdevice.md) \*dev);

572

[ 583](group__uhc__api.md#ga8796569eba96260ce332e611fb520033)static inline struct [uhc\_device\_caps](structuhc__device__caps.md) [uhc\_caps](group__uhc__api.md#ga8796569eba96260ce332e611fb520033)(const struct [device](structdevice.md) \*dev)

584{

585 struct [uhc\_data](structuhc__data.md) \*data = dev->[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e);

586

587 return data->[caps](structuhc__data.md#ac2a48d1d6692931807e8985799c5bdb0);

588}

589

[ 600](group__uhc__api.md#ga4468d1460d79dc30b2605e36ba478e40)static inline const void \*[uhc\_get\_event\_ctx](group__uhc__api.md#ga4468d1460d79dc30b2605e36ba478e40)(const struct [device](structdevice.md) \*dev)

601{

602 struct [uhc\_data](structuhc__data.md) \*data = dev->[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e);

603

604 return data->[event\_ctx](structuhc__data.md#a9f4904633f530748c8e3b2ac3ad0563f);

605}

606

610

611#endif /\* ZEPHYR\_INCLUDE\_UHC\_H \*/

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[device.h](device_8h.md)

[dlist.h](dlist_8h.md)

[atomic\_test\_bit](group__atomic__apis.md#ga190ddc108f45e7649689753c08658eae)

static bool atomic\_test\_bit(const atomic\_t \*target, int bit)

Atomically get and test a bit.

**Definition** atomic.h:127

[sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98)

struct \_dnode sys\_dnode\_t

Doubly-linked list node structure.

**Definition** dlist.h:54

[sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683)

struct \_dnode sys\_dlist\_t

Doubly-linked list structure.

**Definition** dlist.h:50

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[UHC\_STATUS\_INITIALIZED](group__uhc__api.md#ga09ad6fc9251212fa0dffececb767ff9e)

#define UHC\_STATUS\_INITIALIZED

Controller is initialized by uhc\_init().

**Definition** uhc.h:222

[uhc\_is\_enabled](group__uhc__api.md#ga09b71dc5c334f09fb92cf37e2ecf51eb)

static bool uhc\_is\_enabled(const struct device \*dev)

Checks whether the controller is enabled.

**Definition** uhc.h:274

[UHC\_INTERFACES\_MAX](group__uhc__api.md#ga1b1ec49cb7649ece6ec5a31dac3e2537)

#define UHC\_INTERFACES\_MAX

**Definition** uhc.h:54

[UHC\_STATUS\_ENABLED](group__uhc__api.md#ga230e104bd7be1d4b83b2d31ee72ac3c4)

#define UHC\_STATUS\_ENABLED

Controller is enabled and all API functions are available.

**Definition** uhc.h:226

[uhc\_is\_initialized](group__uhc__api.md#ga3251967d36b67169d7892a615323c14e)

static bool uhc\_is\_initialized(const struct device \*dev)

Checks whether the controller is initialized.

**Definition** uhc.h:260

[uhc\_event\_cb\_t](group__uhc__api.md#ga3cda056094ceef79dd62ad9c6852daf9)

int(\* uhc\_event\_cb\_t)(const struct device \*dev, const struct uhc\_event \*const event)

Callback to submit UHC event to higher layer.

**Definition** uhc.h:206

[uhc\_get\_event\_ctx](group__uhc__api.md#ga4468d1460d79dc30b2605e36ba478e40)

static const void \* uhc\_get\_event\_ctx(const struct device \*dev)

Get pointer to higher layer context.

**Definition** uhc.h:600

[uhc\_bus\_reset](group__uhc__api.md#ga4ceb0400168cd53201f0dde5f596452f)

static int uhc\_bus\_reset(const struct device \*dev)

Reset USB bus.

**Definition** uhc.h:318

[usb\_device\_speed](group__uhc__api.md#ga59ba7bbb99177a622f3c073fc48b7bc5)

usb\_device\_speed

USB device operating speed.

**Definition** uhc.h:41

[uhc\_bus\_resume](group__uhc__api.md#ga6669bc2ac56395b38292fa796b99bfd9)

static int uhc\_bus\_resume(const struct device \*dev)

Resume USB bus.

**Definition** uhc.h:386

[usb\_device\_state](group__uhc__api.md#ga7127ac2a46b577f2aa1bb9a650e62a3f)

usb\_device\_state

USB device state.

**Definition** uhc.h:31

[uhc\_xfer\_alloc\_with\_buf](group__uhc__api.md#ga75c2142698a15c547ab76ab76c89c177)

struct uhc\_transfer \* uhc\_xfer\_alloc\_with\_buf(const struct device \*dev, const uint8\_t ep, struct usb\_device \*const udev, void \*const cb, void \*const cb\_priv, size\_t size)

Allocate UHC transfer with buffer.

[uhc\_xfer\_buf\_add](group__uhc__api.md#ga779dbd7ee8ac5fce487e087706791ea7)

int uhc\_xfer\_buf\_add(const struct device \*dev, struct uhc\_transfer \*const xfer, struct net\_buf \*buf)

Add UHC transfer buffer.

[uhc\_ep\_enqueue](group__uhc__api.md#ga7a07b598c00d53393e15f6dae5cf1c4a)

int uhc\_ep\_enqueue(const struct device \*dev, struct uhc\_transfer \*const xfer)

Queue USB host controller transfer.

[uhc\_ep\_dequeue](group__uhc__api.md#ga7c362cba29e0181ffcc8f70060100e62)

int uhc\_ep\_dequeue(const struct device \*dev, struct uhc\_transfer \*const xfer)

Remove a USB host controller transfers from queue.

[uhc\_caps](group__uhc__api.md#ga8796569eba96260ce332e611fb520033)

static struct uhc\_device\_caps uhc\_caps(const struct device \*dev)

Get USB host controller capabilities.

**Definition** uhc.h:583

[uhc\_bus\_suspend](group__uhc__api.md#ga897081ff02dab4377c68bcba343f492c)

static int uhc\_bus\_suspend(const struct device \*dev)

Suspend USB bus.

**Definition** uhc.h:363

[uhc\_init](group__uhc__api.md#ga97beb6e3b3d4ad1b0b7664eae473e1be)

int uhc\_init(const struct device \*dev, uhc\_event\_cb\_t event\_cb, const void \*const event\_ctx)

Initialize USB host controller.

[uhc\_disable](group__uhc__api.md#ga9ec92df4497588adbf8da6f0777a4afd)

int uhc\_disable(const struct device \*dev)

Disable USB host controller.

[uhc\_xfer\_free](group__uhc__api.md#gab2f6328e8051559edccc05ae3552f4f9)

int uhc\_xfer\_free(const struct device \*dev, struct uhc\_transfer \*const xfer)

Free UHC transfer and any buffers.

[uhc\_xfer\_buf\_alloc](group__uhc__api.md#gab4f7439fab8c57e203862bc408a6e46b)

struct net\_buf \* uhc\_xfer\_buf\_alloc(const struct device \*dev, const size\_t size)

Allocate UHC transfer buffer.

[uhc\_xfer\_alloc](group__uhc__api.md#gab5a2df4d176d4c85751c3158b63e366b)

struct uhc\_transfer \* uhc\_xfer\_alloc(const struct device \*dev, const uint8\_t ep, struct usb\_device \*const udev, void \*const cb, void \*const cb\_priv)

Allocate UHC transfer.

[uhc\_event\_type](group__uhc__api.md#gabaf69c1e69fe0fb3d912b92daf8754eb)

uhc\_event\_type

USB host controller event types.

**Definition** uhc.h:146

[uhc\_xfer\_buf\_free](group__uhc__api.md#gac4bd26a85f8abc2006ecf2622669d615)

void uhc\_xfer\_buf\_free(const struct device \*dev, struct net\_buf \*const buf)

Free UHC request buffer.

[uhc\_shutdown](group__uhc__api.md#gac6d1feb9481882a711e58c3e55e915cb)

int uhc\_shutdown(const struct device \*dev)

Poweroff USB host controller.

[uhc\_control\_stage](group__uhc__api.md#gaef9b0703714676c1f7bd1cad57f49bc8)

uhc\_control\_stage

USB control transfer stage.

**Definition** uhc.h:98

[uhc\_sof\_enable](group__uhc__api.md#gafe55e97cbf31d163b10616c03da39414)

static int uhc\_sof\_enable(const struct device \*dev)

Enable Start of Frame generator.

**Definition** uhc.h:340

[uhc\_enable](group__uhc__api.md#gafe94b7f9e32aada9634166ebb2115c2f)

int uhc\_enable(const struct device \*dev)

Enable USB host controller.

[USB\_SPEED\_SPEED\_SS](group__uhc__api.md#gga59ba7bbb99177a622f3c073fc48b7bc5a36e25f2ed5532d6a281abaf521583fcc)

@ USB\_SPEED\_SPEED\_SS

Super speed.

**Definition** uhc.h:51

[USB\_SPEED\_SPEED\_LS](group__uhc__api.md#gga59ba7bbb99177a622f3c073fc48b7bc5a46c4232a37347ac22ac14b240abddbdc)

@ USB\_SPEED\_SPEED\_LS

Low speed.

**Definition** uhc.h:45

[USB\_SPEED\_SPEED\_FS](group__uhc__api.md#gga59ba7bbb99177a622f3c073fc48b7bc5a8cd687699d8afb4d818595d70b189e27)

@ USB\_SPEED\_SPEED\_FS

Full speed.

**Definition** uhc.h:47

[USB\_SPEED\_SPEED\_HS](group__uhc__api.md#gga59ba7bbb99177a622f3c073fc48b7bc5aab0ef8e9a798d70fd3c93e68785c0968)

@ USB\_SPEED\_SPEED\_HS

High speed.

**Definition** uhc.h:49

[USB\_SPEED\_UNKNOWN](group__uhc__api.md#gga59ba7bbb99177a622f3c073fc48b7bc5ac9755ae6b86f8148054fd6a342c74acc)

@ USB\_SPEED\_UNKNOWN

Device is probably not connected.

**Definition** uhc.h:43

[USB\_STATE\_CONFIGURED](group__uhc__api.md#gga7127ac2a46b577f2aa1bb9a650e62a3fa6566e87fb6d54f2da5b7564743df7a47)

@ USB\_STATE\_CONFIGURED

**Definition** uhc.h:35

[USB\_STATE\_NOTCONNECTED](group__uhc__api.md#gga7127ac2a46b577f2aa1bb9a650e62a3fa70367cdc7b5d7d1f3ab046391f50df9d)

@ USB\_STATE\_NOTCONNECTED

**Definition** uhc.h:32

[USB\_STATE\_DEFAULT](group__uhc__api.md#gga7127ac2a46b577f2aa1bb9a650e62a3fabb0f4a1c2f62f028bec1d0b55b5d5554)

@ USB\_STATE\_DEFAULT

**Definition** uhc.h:33

[USB\_STATE\_ADDRESSED](group__uhc__api.md#gga7127ac2a46b577f2aa1bb9a650e62a3fad7f0841a21d3179c13f19d3ae8a8e3b6)

@ USB\_STATE\_ADDRESSED

**Definition** uhc.h:34

[UHC\_EVT\_EP\_REQUEST](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754eba5cdc8afb59f760c4dc9b2de314d05483)

@ UHC\_EVT\_EP\_REQUEST

Endpoint request result event.

**Definition** uhc.h:164

[UHC\_EVT\_DEV\_CONNECTED\_HS](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754eba923b6cfe57c254e22b57eab88c84b67f)

@ UHC\_EVT\_DEV\_CONNECTED\_HS

High speed device connected.

**Definition** uhc.h:152

[UHC\_EVT\_DEV\_CONNECTED\_FS](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754eba98d87b3c737c234918fed0ce4589f4ce)

@ UHC\_EVT\_DEV\_CONNECTED\_FS

Full speed device connected.

**Definition** uhc.h:150

[UHC\_EVT\_RWUP](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebaa616f846752aacb8029f9b21747c656e)

@ UHC\_EVT\_RWUP

Remote wakeup signal.

**Definition** uhc.h:162

[UHC\_EVT\_SUSPENDED](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebab28885b8210133d4f0c2b532561c9c7a)

@ UHC\_EVT\_SUSPENDED

Bus suspend operation finished.

**Definition** uhc.h:158

[UHC\_EVT\_DEV\_REMOVED](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebab7c4181ad631b127cc50605f7864bc30)

@ UHC\_EVT\_DEV\_REMOVED

Device (peripheral) removed.

**Definition** uhc.h:154

[UHC\_EVT\_RESUMED](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebad874caf1d7338081d185634e12f69848)

@ UHC\_EVT\_RESUMED

Bus resume operation finished.

**Definition** uhc.h:160

[UHC\_EVT\_DEV\_CONNECTED\_LS](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebae0a316b8f60df97f30f54630f6847f70)

@ UHC\_EVT\_DEV\_CONNECTED\_LS

Low speed device connected.

**Definition** uhc.h:148

[UHC\_EVT\_ERROR](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebae5970877eb9b6426132d8955cdeb26d7)

@ UHC\_EVT\_ERROR

Non-correctable error event, requires attention from higher levels or application.

**Definition** uhc.h:169

[UHC\_EVT\_RESETED](group__uhc__api.md#ggabaf69c1e69fe0fb3d912b92daf8754ebafb131548cc66e748e562ee88df274ab3)

@ UHC\_EVT\_RESETED

Bus reset operation finished.

**Definition** uhc.h:156

[UHC\_CONTROL\_STAGE\_DATA](group__uhc__api.md#ggaef9b0703714676c1f7bd1cad57f49bc8a2179067786eb86aad804d0aead9d71a5)

@ UHC\_CONTROL\_STAGE\_DATA

**Definition** uhc.h:100

[UHC\_CONTROL\_STAGE\_SETUP](group__uhc__api.md#ggaef9b0703714676c1f7bd1cad57f49bc8a3f3c131b3a97a552d2917bbddcd9afc8)

@ UHC\_CONTROL\_STAGE\_SETUP

**Definition** uhc.h:99

[UHC\_CONTROL\_STAGE\_STATUS](group__uhc__api.md#ggaef9b0703714676c1f7bd1cad57f49bc8a7bd9f0423e9f50266905c3736e12468f)

@ UHC\_CONTROL\_STAGE\_STATUS

**Definition** uhc.h:101

[kernel.h](kernel_8h.md)

Public kernel APIs.

[net\_buf.h](net__buf_8h.md)

Buffer management.

[shutdown](posix_2sys_2socket_8h.md#a8dadddc96fee56a9f8b0904aca02eab2)

int shutdown(int sock, int how)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:463

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:459

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:3025

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** net\_buf.h:1006

[net\_buf::size](structnet__buf.md#a1522d81a002804223e25300a6961f527)

uint16\_t size

Amount of data that this buffer can store.

**Definition** net\_buf.h:1038

[uhc\_data](structuhc__data.md)

Common UHC driver data structure.

**Definition** uhc.h:234

[uhc\_data::mutex](structuhc__data.md#a08772cdd5b42bd11ca4a06a75df846e9)

struct k\_mutex mutex

Driver access mutex.

**Definition** uhc.h:238

[uhc\_data::status](structuhc__data.md#a10852f2523cc733541cc9ea51706559f)

atomic\_t status

USB host controller status.

**Definition** uhc.h:248

[uhc\_data::priv](structuhc__data.md#a294120f6cf8563cb9564c51fcf56d883)

void \* priv

Driver private data.

**Definition** uhc.h:250

[uhc\_data::ctrl\_xfers](structuhc__data.md#a32eec449ffbe5e6c262c907e6e6b475a)

sys\_dlist\_t ctrl\_xfers

dlist for control transfers

**Definition** uhc.h:240

[uhc\_data::event\_ctx](structuhc__data.md#a9f4904633f530748c8e3b2ac3ad0563f)

const void \* event\_ctx

Opaque pointer to store higher layer context.

**Definition** uhc.h:246

[uhc\_data::caps](structuhc__data.md#ac2a48d1d6692931807e8985799c5bdb0)

struct uhc\_device\_caps caps

Controller capabilities.

**Definition** uhc.h:236

[uhc\_data::bulk\_xfers](structuhc__data.md#ac6214566324740c34a8bba42515d1d32)

sys\_dlist\_t bulk\_xfers

dlist for bulk transfers

**Definition** uhc.h:242

[uhc\_data::event\_cb](structuhc__data.md#afd1a0828a0ca3e397dba09fe38fd8050)

uhc\_event\_cb\_t event\_cb

Callback to submit an UHC event to upper layer.

**Definition** uhc.h:244

[uhc\_device\_caps](structuhc__device__caps.md)

USB host controller capabilities.

**Definition** uhc.h:214

[uhc\_device\_caps::hs](structuhc__device__caps.md#ab526337af28d25728780cb48dc43e722)

uint32\_t hs

USB high speed capable controller.

**Definition** uhc.h:216

[uhc\_event](structuhc__event.md)

USB host controller event.

**Definition** uhc.h:180

[uhc\_event::xfer](structuhc__event.md#a03f3cebee6edfaf620a98c198a70dbd0)

struct uhc\_transfer \* xfer

Pointer to request used only for UHC\_EVT\_EP\_REQUEST.

**Definition** uhc.h:189

[uhc\_event::dev](structuhc__event.md#a055be3fd47e16bc48498163be3e55d09)

const struct device \* dev

Pointer to controller's device struct.

**Definition** uhc.h:192

[uhc\_event::type](structuhc__event.md#a30fddbbe0f15a16320fba3cb4fd81d84)

enum uhc\_event\_type type

Event type.

**Definition** uhc.h:184

[uhc\_event::status](structuhc__event.md#a5d7e1cc1bcb25e10f009ac3a8acd94b6)

int status

Event status value, if any.

**Definition** uhc.h:187

[uhc\_event::node](structuhc__event.md#acd04587fac14f9a8a91b75642f5b2e82)

sys\_snode\_t node

slist node for the message queue

**Definition** uhc.h:182

[uhc\_transfer](structuhc__transfer.md)

UHC endpoint buffer info.

**Definition** uhc.h:114

[uhc\_transfer::priv](structuhc__transfer.md#a0f2d4a735ce224260d100dc756b1900f)

void \* priv

Pointer to completion callback private data.

**Definition** uhc.h:138

[uhc\_transfer::err](structuhc__transfer.md#a11f002f91b1039c226b7c9feb8223e11)

int err

Transfer result, 0 on success, other values on error.

**Definition** uhc.h:140

[uhc\_transfer::buf](structuhc__transfer.md#a170385b08171659f05ac7112faf8e587)

struct net\_buf \* buf

Transfer data buffer.

**Definition** uhc.h:120

[uhc\_transfer::start\_frame](structuhc__transfer.md#a23e4115c774134ccd143189b0f4f2460)

uint16\_t start\_frame

Start frame, used for periodic transfers only.

**Definition** uhc.h:128

[uhc\_transfer::mps](structuhc__transfer.md#a61a6c74cc7c026404ccf42d1164765b8)

uint16\_t mps

Maximum packet size.

**Definition** uhc.h:124

[uhc\_transfer::udev](structuhc__transfer.md#a81a8a80809420787f4c0ab232a24a514)

struct usb\_device \* udev

Pointer to USB device.

**Definition** uhc.h:134

[uhc\_transfer::stage](structuhc__transfer.md#a9983482be9724e281e56c978ce27d93f)

unsigned int stage

Control stage status, up to the driver to use it or not.

**Definition** uhc.h:132

[uhc\_transfer::ep](structuhc__transfer.md#aaf664844dc9f1871cce3d38516c042ef)

uint8\_t ep

Endpoint to which request is associated.

**Definition** uhc.h:122

[uhc\_transfer::queued](structuhc__transfer.md#ad2b246c850c3b30f7d2b58fc9a47008b)

unsigned int queued

Flag marks request buffer is queued.

**Definition** uhc.h:130

[uhc\_transfer::cb](structuhc__transfer.md#ad4d80a3f20cdec7dd2237a98054dd287)

void \* cb

Pointer to transfer completion callback (opaque for the UHC).

**Definition** uhc.h:136

[uhc\_transfer::node](structuhc__transfer.md#ae1fcb0b866e3d7c5b5ea9dff6221f37d)

sys\_dnode\_t node

dlist node

**Definition** uhc.h:116

[uhc\_transfer::setup\_pkt](structuhc__transfer.md#af5e8080b91078a1c9f8ff269c72d70e9)

uint8\_t setup\_pkt[8]

Control transfer setup packet.

**Definition** uhc.h:118

[uhc\_transfer::interval](structuhc__transfer.md#af6d6de482f092e4f85679722ad609cbf)

uint16\_t interval

Interval, used for periodic transfers only.

**Definition** uhc.h:126

[usb\_desc\_header](structusb__desc__header.md)

Header of an USB descriptor.

**Definition** usb\_ch9.h:144

[usb\_device\_descriptor](structusb__device__descriptor.md)

USB Standard Device Descriptor defined in spec.

**Definition** usb\_ch9.h:150

[usb\_device](structusb__device.md)

Host representation of a USB device.

**Definition** uhc.h:68

[usb\_device::node](structusb__device.md#a0215608e40123de4a3a79ca440c6c593)

sys\_dnode\_t node

dlist node

**Definition** uhc.h:70

[usb\_device::actual\_cfg](structusb__device.md#a101d30facb781bd410581fc6c2d3fa59)

uint8\_t actual\_cfg

Actual active device configuration.

**Definition** uhc.h:82

[usb\_device::speed](structusb__device.md#a1b3f4becfd9fbfae80074fc2e76ea6a8)

enum usb\_device\_speed speed

Device speed.

**Definition** uhc.h:80

[usb\_device::dev\_desc](structusb__device.md#a24be9609d416d3a184fdedbefa298490)

struct usb\_device\_descriptor dev\_desc

USB device descriptor.

**Definition** uhc.h:76

[usb\_device::mutex](structusb__device.md#a4203b2cfd65f70096a43a20c7c37de27)

struct k\_mutex mutex

Device mutex.

**Definition** uhc.h:74

[usb\_device::ifaces](structusb__device.md#a5cccbb483d91032f4a7f25f88270747f)

struct usb\_host\_interface ifaces[32+1]

Pointers to device interfaces.

**Definition** uhc.h:88

[usb\_device::ep\_out](structusb__device.md#a658b9992a472574b1d88e49b7fea478d)

struct usb\_host\_ep ep\_out[16]

Pointers to device OUT endpoints.

**Definition** uhc.h:90

[usb\_device::ctx](structusb__device.md#a72ee0e53efd86c91e0cea6c7e873d5ce)

void \* ctx

An opaque pointer to the host context to which this device belongs.

**Definition** uhc.h:72

[usb\_device::state](structusb__device.md#aa75bbea6a879460b39216453323d177f)

enum usb\_device\_state state

Device state.

**Definition** uhc.h:78

[usb\_device::addr](structusb__device.md#aa9062a5b9da663863e6d51ef2e04197b)

uint8\_t addr

Device address.

**Definition** uhc.h:84

[usb\_device::cfg\_desc](structusb__device.md#ac98af9fb0d5bba21bc8037a8fcfb3126)

void \* cfg\_desc

Pointer to actual device configuration descriptor.

**Definition** uhc.h:86

[usb\_device::ep\_in](structusb__device.md#ad3091acb2a713b9e66c595bbf4a736a5)

struct usb\_host\_ep ep\_in[16]

Pointers to device IN endpoints.

**Definition** uhc.h:92

[usb\_ep\_descriptor](structusb__ep__descriptor.md)

USB Standard Endpoint Descriptor defined in spec.

**Definition** usb\_ch9.h:220

[usb\_host\_ep](structusb__host__ep.md)

**Definition** uhc.h:61

[usb\_host\_ep::desc](structusb__host__ep.md#a25e9c4004ab03927476093ed4d167dbd)

struct usb\_ep\_descriptor \* desc

**Definition** uhc.h:62

[usb\_host\_interface](structusb__host__interface.md)

**Definition** uhc.h:56

[usb\_host\_interface::alternate](structusb__host__interface.md#a4405cdfb6aa6fbbcd2ac27148b9ebea6)

uint8\_t alternate

**Definition** uhc.h:58

[usb\_host\_interface::dhp](structusb__host__interface.md#aa0170523367f9e1459a9ba897c0d88bf)

struct usb\_desc\_header \* dhp

**Definition** uhc.h:57

[usb\_ch9.h](usb__ch9_8h.md)

USB Chapter 9 structures and definitions.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [usb](dir_8780870c85d3e97051f07cf376f058af.md)
- [uhc.h](uhc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
