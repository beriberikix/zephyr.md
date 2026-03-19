---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/usbd_8h_source.html
original_path: doxygen/html/usbd_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbd.h

[Go to the documentation of this file.](usbd_8h.md)

1/\*

2 \* Copyright (c) 2022 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

13

14#ifndef ZEPHYR\_INCLUDE\_USBD\_H\_

15#define ZEPHYR\_INCLUDE\_USBD\_H\_

16

17#include <[zephyr/device.h](device_8h.md)>

18#include <[zephyr/usb/bos.h](bos_8h.md)>

19#include <[zephyr/usb/usb\_ch9.h](usb__ch9_8h.md)>

20#include <[zephyr/usb/usbd\_msg.h](usbd__msg_8h.md)>

21#include <[zephyr/drivers/usb/udc\_buf.h](udc__buf_8h.md)>

22#include <[zephyr/sys/byteorder.h](sys_2byteorder_8h.md)>

23#include <[zephyr/sys/slist.h](slist_8h.md)>

24#include <[zephyr/logging/log.h](log_8h.md)>

25#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

26

27#ifdef \_\_cplusplus

28extern "C" {

29#endif

30

39

40/\*

41 \* The USB Unicode bString is encoded in UTF16LE, which means it takes up

42 \* twice the amount of bytes than the same string encoded in ASCII7.

43 \* Use this macro to determine the length of the bString array.

44 \*

45 \* bString length without null character:

46 \* bString\_length = (sizeof(initializer\_string) - 1) \* 2

47 \* or:

48 \* bString\_length = sizeof(initializer\_string) \* 2 - 2

49 \*/

[ 50](group__usbd__api.md#gac3d58cfa3f92b1811e9ed136c4450906)#define USB\_BSTRING\_LENGTH(s) (sizeof(s) \* 2 - 2)

51

52/\*

53 \* The length of the string descriptor (bLength) is calculated from the

54 \* size of the two octets bLength and bDescriptorType plus the

55 \* length of the UTF16LE string:

56 \*

57 \* bLength = 2 + bString\_length

58 \* bLength = 2 + sizeof(initializer\_string) \* 2 - 2

59 \* bLength = sizeof(initializer\_string) \* 2

60 \* Use this macro to determine the bLength of the string descriptor.

61 \*/

[ 62](group__usbd__api.md#gaef85e50556291fa93cbf72b01529b4a8)#define USB\_STRING\_DESCRIPTOR\_LENGTH(s) (sizeof(s) \* 2)

63

67enum usbd\_str\_desc\_utype {

68 USBD\_DUT\_STRING\_LANG,

69 USBD\_DUT\_STRING\_MANUFACTURER,

70 USBD\_DUT\_STRING\_PRODUCT,

71 USBD\_DUT\_STRING\_SERIAL\_NUMBER,

72 USBD\_DUT\_STRING\_CONFIG,

73 USBD\_DUT\_STRING\_INTERFACE,

74};

75

76enum usbd\_bos\_desc\_utype {

77 USBD\_DUT\_BOS\_NONE,

78};

80

[ 84](structusbd__str__desc__data.md)struct [usbd\_str\_desc\_data](structusbd__str__desc__data.md) {

[ 86](structusbd__str__desc__data.md#a0654953d15160cc19cad86a407f655cb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [idx](structusbd__str__desc__data.md#a0654953d15160cc19cad86a407f655cb);

[ 88](structusbd__str__desc__data.md#a2e6dfc9cbbd44457113899db988a84ca) enum usbd\_str\_desc\_utype [utype](structusbd__str__desc__data.md#a2e6dfc9cbbd44457113899db988a84ca) : 8;

[ 90](structusbd__str__desc__data.md#ad4d7c291f95973d20ff522b8a5ef65a0) unsigned int [ascii7](structusbd__str__desc__data.md#ad4d7c291f95973d20ff522b8a5ef65a0) : 1;

[ 92](structusbd__str__desc__data.md#a40459d114a339841e1f9c14b0d036fe8) unsigned int [use\_hwinfo](structusbd__str__desc__data.md#a40459d114a339841e1f9c14b0d036fe8) : 1;

93};

94

[ 98](structusbd__bos__desc__data.md)struct [usbd\_bos\_desc\_data](structusbd__bos__desc__data.md) {

[ 100](structusbd__bos__desc__data.md#a084578c905400488e5ce73c71f8aaf00) enum usbd\_bos\_desc\_utype [utype](structusbd__bos__desc__data.md#a084578c905400488e5ce73c71f8aaf00) : 8;

101};

102

[ 109](structusbd__desc__node.md)struct [usbd\_desc\_node](structusbd__desc__node.md) {

[ 111](structusbd__desc__node.md#a9f1941cd036c01387d8ad9a4aceb595a) [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) [node](structusbd__desc__node.md#a9f1941cd036c01387d8ad9a4aceb595a);

112 union {

[ 113](structusbd__desc__node.md#ae34fee200f7fd78355addafe79789cb4) struct [usbd\_str\_desc\_data](structusbd__str__desc__data.md) [str](structusbd__desc__node.md#ae34fee200f7fd78355addafe79789cb4);

[ 114](structusbd__desc__node.md#afd65079b8b969fa4101a3f9f662c7b6b) struct [usbd\_bos\_desc\_data](structusbd__bos__desc__data.md) [bos](structusbd__desc__node.md#afd65079b8b969fa4101a3f9f662c7b6b);

115 };

[ 117](structusbd__desc__node.md#ac437b472e012e8fdec049f28e9f88944) const void \*const [ptr](structusbd__desc__node.md#ac437b472e012e8fdec049f28e9f88944);

[ 119](structusbd__desc__node.md#ad71ef74fd7fe43a8117704553a3be01c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bLength](structusbd__desc__node.md#ad71ef74fd7fe43a8117704553a3be01c);

[ 121](structusbd__desc__node.md#a786e2911b5ec7d6c908c148be4d27f5f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDescriptorType](structusbd__desc__node.md#a786e2911b5ec7d6c908c148be4d27f5f);

122};

123

[ 132](structusbd__config__node.md)struct [usbd\_config\_node](structusbd__config__node.md) {

[ 134](structusbd__config__node.md#a003a8d9132b319f54583263c4da1e060) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structusbd__config__node.md#a003a8d9132b319f54583263c4da1e060);

[ 136](structusbd__config__node.md#a55081d79ab3e6b41a091b3f65d7d2d87) void \*[desc](structusbd__config__node.md#a55081d79ab3e6b41a091b3f65d7d2d87);

[ 138](structusbd__config__node.md#a19203885a9698861f849bd0fd57cb37f) struct [usbd\_desc\_node](structusbd__desc__node.md) \*[str\_desc\_nd](structusbd__config__node.md#a19203885a9698861f849bd0fd57cb37f);

[ 140](structusbd__config__node.md#a00493162af2344d3d39f834b4834ef78) [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) [class\_list](structusbd__config__node.md#a00493162af2344d3d39f834b4834ef78);

141};

142

143/\* TODO: Kconfig option USBD\_NUMOF\_INTERFACES\_MAX? \*/

[ 144](group__usbd__api.md#gaf8aadd499f7e0438acac4a7f36645d49)#define USBD\_NUMOF\_INTERFACES\_MAX 16U

145

[ 152](group__usbd__api.md#ga95fb708d8a54eaa3ce0acc4e65519bbc)enum [usbd\_ch9\_state](group__usbd__api.md#ga95fb708d8a54eaa3ce0acc4e65519bbc) {

[ 153](group__usbd__api.md#gga95fb708d8a54eaa3ce0acc4e65519bbca978c707d313eb49b70bc62dfae304048) [USBD\_STATE\_DEFAULT](group__usbd__api.md#gga95fb708d8a54eaa3ce0acc4e65519bbca978c707d313eb49b70bc62dfae304048) = 0,

[ 154](group__usbd__api.md#gga95fb708d8a54eaa3ce0acc4e65519bbca985f06c5505c5684a98954f15701cc9d) [USBD\_STATE\_ADDRESS](group__usbd__api.md#gga95fb708d8a54eaa3ce0acc4e65519bbca985f06c5505c5684a98954f15701cc9d),

[ 155](group__usbd__api.md#gga95fb708d8a54eaa3ce0acc4e65519bbca44c1920b09ea1062ea4d7ac31a846509) [USBD\_STATE\_CONFIGURED](group__usbd__api.md#gga95fb708d8a54eaa3ce0acc4e65519bbca44c1920b09ea1062ea4d7ac31a846509),

156};

157

158

[ 162](structusbd__ch9__data.md)struct [usbd\_ch9\_data](structusbd__ch9__data.md) {

[ 164](structusbd__ch9__data.md#a85f96c69cede5b51c1f9739a4ae67f4d) struct [usb\_setup\_packet](structusb__setup__packet.md) [setup](structusbd__ch9__data.md#a85f96c69cede5b51c1f9739a4ae67f4d);

[ 166](structusbd__ch9__data.md#a095a2a98f19ea40e8bd1bf65eed77dac) int [ctrl\_type](structusbd__ch9__data.md#a095a2a98f19ea40e8bd1bf65eed77dac);

[ 168](structusbd__ch9__data.md#a70d1a1be0aab6167ca4f4580b9c65eff) enum [usbd\_ch9\_state](group__usbd__api.md#ga95fb708d8a54eaa3ce0acc4e65519bbc) [state](structusbd__ch9__data.md#a70d1a1be0aab6167ca4f4580b9c65eff);

[ 170](structusbd__ch9__data.md#a504360b7cb11240a2fda68344f2e3b62) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ep\_halt](structusbd__ch9__data.md#a504360b7cb11240a2fda68344f2e3b62);

[ 172](structusbd__ch9__data.md#a1f759fb0d758e50c4589b6b6b1fd2a24) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [configuration](structusbd__ch9__data.md#a1f759fb0d758e50c4589b6b6b1fd2a24);

[ 174](structusbd__ch9__data.md#a6ab6f611fd1eff8d6fde0617c587fefb) bool [post\_status](structusbd__ch9__data.md#a6ab6f611fd1eff8d6fde0617c587fefb);

[ 176](structusbd__ch9__data.md#a8f831eca1974b8411072f8102c444d45) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [alternate](structusbd__ch9__data.md#a8f831eca1974b8411072f8102c444d45)[[USBD\_NUMOF\_INTERFACES\_MAX](group__usbd__api.md#gaf8aadd499f7e0438acac4a7f36645d49)];

177};

178

[ 182](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71)enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) {

[ 184](group__usbd__api.md#gga2f2da3d634530f08cd59d408c811ad71a30b20b0839dff88b038e680b55f382d7) [USBD\_SPEED\_FS](group__usbd__api.md#gga2f2da3d634530f08cd59d408c811ad71a30b20b0839dff88b038e680b55f382d7),

[ 186](group__usbd__api.md#gga2f2da3d634530f08cd59d408c811ad71abaf4bdba11db59d804d753e6fac92266) [USBD\_SPEED\_HS](group__usbd__api.md#gga2f2da3d634530f08cd59d408c811ad71abaf4bdba11db59d804d753e6fac92266),

[ 188](group__usbd__api.md#gga2f2da3d634530f08cd59d408c811ad71a195490bdfa76ffca418e8bf2f3d3c96a) [USBD\_SPEED\_SS](group__usbd__api.md#gga2f2da3d634530f08cd59d408c811ad71a195490bdfa76ffca418e8bf2f3d3c96a),

189};

190

[ 194](structusbd__status.md)struct [usbd\_status](structusbd__status.md) {

[ 196](structusbd__status.md#a78de12245d08ecc71e09d5519fe0e857) unsigned int [initialized](structusbd__status.md#a78de12245d08ecc71e09d5519fe0e857) : 1;

[ 198](structusbd__status.md#a2382fcb655fe51e0bcf83f85aa182ba3) unsigned int [enabled](structusbd__status.md#a2382fcb655fe51e0bcf83f85aa182ba3) : 1;

[ 200](structusbd__status.md#afb67cfda187e40229f842c93aa09f0ba) unsigned int [suspended](structusbd__status.md#afb67cfda187e40229f842c93aa09f0ba) : 1;

[ 202](structusbd__status.md#a113085892967cf7c9cb70131b320d61a) unsigned int [rwup](structusbd__status.md#a113085892967cf7c9cb70131b320d61a) : 1;

[ 204](structusbd__status.md#a295009d25826732ba9eebd7735d93d23) enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) [speed](structusbd__status.md#a295009d25826732ba9eebd7735d93d23) : 2;

205};

206

207struct [usbd\_context](structusbd__context.md);

208

[ 220](group__usbd__api.md#ga2cd074cefff922b0816de37935d9646e)typedef void (\*[usbd\_msg\_cb\_t](group__usbd__api.md#ga2cd074cefff922b0816de37935d9646e))(struct [usbd\_context](structusbd__context.md) \*const ctx,

221 const struct [usbd\_msg](structusbd__msg.md) \*const msg);

222

[ 229](structusbd__context.md)struct [usbd\_context](structusbd__context.md) {

[ 231](structusbd__context.md#ade73c224b256007bf2d68bd1205ceb6e) const char \*[name](structusbd__context.md#ade73c224b256007bf2d68bd1205ceb6e);

[ 233](structusbd__context.md#a8ff2a4303b73db67eeabdd999736b3a6) struct [k\_mutex](structk__mutex.md) [mutex](structusbd__context.md#a8ff2a4303b73db67eeabdd999736b3a6);

[ 235](structusbd__context.md#a52c2cc6118b46fbcbc7a495df61f6b6c) const struct [device](structdevice.md) \*[dev](structusbd__context.md#a52c2cc6118b46fbcbc7a495df61f6b6c);

[ 237](structusbd__context.md#a300ab0384b3d4e7f3d7d188a27a78be3) [usbd\_msg\_cb\_t](group__usbd__api.md#ga2cd074cefff922b0816de37935d9646e) [msg\_cb](structusbd__context.md#a300ab0384b3d4e7f3d7d188a27a78be3);

[ 239](structusbd__context.md#a4fb1545ec02e7d38766cee9940edc1eb) struct [usbd\_ch9\_data](structusbd__ch9__data.md) [ch9\_data](structusbd__context.md#a4fb1545ec02e7d38766cee9940edc1eb);

[ 241](structusbd__context.md#adf8dd86f2784cc69ce6da314adc00b72) [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) [descriptors](structusbd__context.md#adf8dd86f2784cc69ce6da314adc00b72);

[ 243](structusbd__context.md#a8c7d153a73859dd8ba25265f059f7495) [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) [fs\_configs](structusbd__context.md#a8c7d153a73859dd8ba25265f059f7495);

[ 245](structusbd__context.md#a4a6bd413d06328ffa5db089e35157376) [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) [hs\_configs](structusbd__context.md#a4a6bd413d06328ffa5db089e35157376);

[ 247](structusbd__context.md#a3acad44126b6c3d56823ef7408332087) struct [usbd\_status](structusbd__status.md) [status](structusbd__context.md#a3acad44126b6c3d56823ef7408332087);

[ 249](structusbd__context.md#a193420cc196f115cbd6947b10d542ee5) void \*[fs\_desc](structusbd__context.md#a193420cc196f115cbd6947b10d542ee5);

[ 251](structusbd__context.md#a250e2f82c7239ce81b104b6ef3c16857) void \*[hs\_desc](structusbd__context.md#a250e2f82c7239ce81b104b6ef3c16857);

252};

253

[ 257](structusbd__cctx__vendor__req.md)struct [usbd\_cctx\_vendor\_req](structusbd__cctx__vendor__req.md) {

[ 259](structusbd__cctx__vendor__req.md#a2ddf3ce0c1c0a6d788b7ef30cf8d67ea) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[reqs](structusbd__cctx__vendor__req.md#a2ddf3ce0c1c0a6d788b7ef30cf8d67ea);

[ 261](structusbd__cctx__vendor__req.md#a3b5e99bff9dbfa023a4e6a5b4a69abd0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structusbd__cctx__vendor__req.md#a3b5e99bff9dbfa023a4e6a5b4a69abd0);

262};

263

[ 265](group__usbd__api.md#ga588b9e156a49d3b0358bee185cdeebee)#define USBD\_CCTX\_REGISTERED 0

266

267struct [usbd\_class\_data](structusbd__class__data.md);

268

[ 272](structusbd__class__api.md)struct [usbd\_class\_api](structusbd__class__api.md) {

[ 274](structusbd__class__api.md#a09475f1b29f482e548b6bc168dcd19e7) void (\*[feature\_halt](structusbd__class__api.md#a09475f1b29f482e548b6bc168dcd19e7))(struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data,

275 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, bool halted);

276

[ 278](structusbd__class__api.md#a11d09e35f9d4c4d6b18e12bf4ea241b0) void (\*[update](structusbd__class__api.md#a11d09e35f9d4c4d6b18e12bf4ea241b0))(struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data,

279 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) iface, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) alternate);

280

[ 282](structusbd__class__api.md#ab37dd5f2bf4029f149e69046702626a1) int (\*[control\_to\_dev](structusbd__class__api.md#ab37dd5f2bf4029f149e69046702626a1))(struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data,

283 const struct [usb\_setup\_packet](structusb__setup__packet.md) \*const setup,

284 const struct [net\_buf](structnet__buf.md) \*const buf);

285

[ 287](structusbd__class__api.md#ac52356c07c26a3bcb1025cd6778ca8ef) int (\*[control\_to\_host](structusbd__class__api.md#ac52356c07c26a3bcb1025cd6778ca8ef))(struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data,

288 const struct [usb\_setup\_packet](structusb__setup__packet.md) \*const setup,

289 struct [net\_buf](structnet__buf.md) \*const buf);

290

[ 292](structusbd__class__api.md#a70425718fd34534fd976240340b4496d) int (\*[request](structusbd__class__api.md#a70425718fd34534fd976240340b4496d))(struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data,

293 struct [net\_buf](structnet__buf.md) \*buf, int err);

294

[ 296](structusbd__class__api.md#a598afe76b5c2f9e75a049fe785393e04) void (\*[suspended](structusbd__class__api.md#a598afe76b5c2f9e75a049fe785393e04))(struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data);

297

[ 299](structusbd__class__api.md#ae6f3a658e5768f5d6672cd0e5f2d24a5) void (\*[resumed](structusbd__class__api.md#ae6f3a658e5768f5d6672cd0e5f2d24a5))(struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data);

300

[ 302](structusbd__class__api.md#a488b102936b5cd3e4095578119b71510) void (\*[sof](structusbd__class__api.md#a488b102936b5cd3e4095578119b71510))(struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data);

303

[ 305](structusbd__class__api.md#ab42f61db338471f0c5260576680409e9) void (\*[enable](structusbd__class__api.md#ab42f61db338471f0c5260576680409e9))(struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data);

306

[ 308](structusbd__class__api.md#afd43bfa4aab664c50648aa59a0c713de) void (\*[disable](structusbd__class__api.md#afd43bfa4aab664c50648aa59a0c713de))(struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data);

309

[ 311](structusbd__class__api.md#a7d749f007d70e30f76aa121067b7a5c6) int (\*[init](structusbd__class__api.md#a7d749f007d70e30f76aa121067b7a5c6))(struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data);

312

[ 314](structusbd__class__api.md#a5ca5bc6d3f5220bd3658d9398e09016e) void (\*[shutdown](structusbd__class__api.md#a5ca5bc6d3f5220bd3658d9398e09016e))(struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data);

315

[ 317](structusbd__class__api.md#a9d6ecb2a5ff55427502ba7ad8f96a146) void \*(\*get\_desc)(struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data,

318 const enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) speed);

319};

320

[ 324](structusbd__class__data.md)struct [usbd\_class\_data](structusbd__class__data.md) {

[ 326](structusbd__class__data.md#ad251371b0e401fb2bffd6aaa1ff49063) const char \*[name](structusbd__class__data.md#ad251371b0e401fb2bffd6aaa1ff49063);

[ 328](structusbd__class__data.md#a111a803092fd389a500fb99bfc71b29a) struct [usbd\_context](structusbd__context.md) \*[uds\_ctx](structusbd__class__data.md#a111a803092fd389a500fb99bfc71b29a);

[ 330](structusbd__class__data.md#a9109af3e25c499d4ef1f0746bf6a20cc) const struct [usbd\_class\_api](structusbd__class__api.md) \*[api](structusbd__class__data.md#a9109af3e25c499d4ef1f0746bf6a20cc);

[ 332](structusbd__class__data.md#a32db83ecf80e1ac9e4d5deda54581deb) const struct [usbd\_cctx\_vendor\_req](structusbd__cctx__vendor__req.md) \*[v\_reqs](structusbd__class__data.md#a32db83ecf80e1ac9e4d5deda54581deb);

[ 334](structusbd__class__data.md#a10bb5b9af6098fbbc86fd00ef54e84e1) void \*[priv](structusbd__class__data.md#a10bb5b9af6098fbbc86fd00ef54e84e1);

335};

336

345struct usbd\_class\_node {

347 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

349 struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data;

353 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ep\_assigned;

357 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ep\_active;

359 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) iface\_bm;

361 [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90);

362};

363

365

[ 376](group__usbd__api.md#gaf97c68e75420bd5a1085c047577fd5a7)static inline struct [usbd\_context](structusbd__context.md) \*[usbd\_class\_get\_ctx](group__usbd__api.md#gaf97c68e75420bd5a1085c047577fd5a7)(const struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data)

377{

378 return c\_data->[uds\_ctx](structusbd__class__data.md#a111a803092fd389a500fb99bfc71b29a);

379}

380

[ 391](group__usbd__api.md#ga2e511d0341b4e1bd57fb4420512eeeb5)static inline void \*[usbd\_class\_get\_private](group__usbd__api.md#ga2e511d0341b4e1bd57fb4420512eeeb5)(const struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data)

392{

393 return c\_data->[priv](structusbd__class__data.md#a10bb5b9af6098fbbc86fd00ef54e84e1);

394}

395

[ 416](group__usbd__api.md#ga26777805f749f29efa882f9bf391473a)#define USBD\_DEVICE\_DEFINE(device\_name, udc\_dev, vid, pid) \

417 static struct usb\_device\_descriptor \

418 fs\_desc\_##device\_name = { \

419 .bLength = sizeof(struct usb\_device\_descriptor), \

420 .bDescriptorType = USB\_DESC\_DEVICE, \

421 .bcdUSB = sys\_cpu\_to\_le16(USB\_SRN\_2\_0), \

422 .bDeviceClass = USB\_BCC\_MISCELLANEOUS, \

423 .bDeviceSubClass = 2, \

424 .bDeviceProtocol = 1, \

425 .bMaxPacketSize0 = USB\_CONTROL\_EP\_MPS, \

426 .idVendor = vid, \

427 .idProduct = pid, \

428 .bcdDevice = sys\_cpu\_to\_le16(USB\_BCD\_DRN), \

429 .iManufacturer = 0, \

430 .iProduct = 0, \

431 .iSerialNumber = 0, \

432 .bNumConfigurations = 0, \

433 }; \

434 static struct usb\_device\_descriptor \

435 hs\_desc\_##device\_name = { \

436 .bLength = sizeof(struct usb\_device\_descriptor), \

437 .bDescriptorType = USB\_DESC\_DEVICE, \

438 .bcdUSB = sys\_cpu\_to\_le16(USB\_SRN\_2\_0), \

439 .bDeviceClass = USB\_BCC\_MISCELLANEOUS, \

440 .bDeviceSubClass = 2, \

441 .bDeviceProtocol = 1, \

442 .bMaxPacketSize0 = 64, \

443 .idVendor = vid, \

444 .idProduct = pid, \

445 .bcdDevice = sys\_cpu\_to\_le16(USB\_BCD\_DRN), \

446 .iManufacturer = 0, \

447 .iProduct = 0, \

448 .iSerialNumber = 0, \

449 .bNumConfigurations = 0, \

450 }; \

451 static STRUCT\_SECTION\_ITERABLE(usbd\_context, device\_name) = { \

452 .name = STRINGIFY(device\_name), \

453 .dev = udc\_dev, \

454 .fs\_desc = &fs\_desc\_##device\_name, \

455 .hs\_desc = &hs\_desc\_##device\_name, \

456 }

457

[ 475](group__usbd__api.md#ga2d98fd68eff66f36522688f3de527586)#define USBD\_CONFIGURATION\_DEFINE(name, attrib, power, desc\_nd) \

476 static struct usb\_cfg\_descriptor \

477 cfg\_desc\_##name = { \

478 .bLength = sizeof(struct usb\_cfg\_descriptor), \

479 .bDescriptorType = USB\_DESC\_CONFIGURATION, \

480 .wTotalLength = 0, \

481 .bNumInterfaces = 0, \

482 .bConfigurationValue = 1, \

483 .iConfiguration = 0, \

484 .bmAttributes = USB\_SCD\_RESERVED | (attrib), \

485 .bMaxPower = (power), \

486 }; \

487 BUILD\_ASSERT((power) < 256, "Too much power"); \

488 static struct usbd\_config\_node name = { \

489 .desc = &cfg\_desc\_##name, \

490 .str\_desc\_nd = desc\_nd, \

491 }

492

[ 506](group__usbd__api.md#gaec816a27118bcb289ab4840fcd22888e)#define USBD\_DESC\_LANG\_DEFINE(name) \

507 static uint16\_t langid\_##name = sys\_cpu\_to\_le16(0x0409); \

508 static struct usbd\_desc\_node name = { \

509 .str = { \

510 .idx = 0, \

511 .utype = USBD\_DUT\_STRING\_LANG, \

512 }, \

513 .ptr = &langid\_##name, \

514 .bLength = sizeof(struct usb\_string\_descriptor), \

515 .bDescriptorType = USB\_DESC\_STRING, \

516 }

517

[ 529](group__usbd__api.md#gaf800e2040ac30844cab463c13d1fcdf8)#define USBD\_DESC\_STRING\_DEFINE(d\_name, d\_string, d\_utype) \

530 static uint8\_t ascii\_##d\_name[USB\_BSTRING\_LENGTH(d\_string)] = d\_string; \

531 static struct usbd\_desc\_node d\_name = { \

532 .str = { \

533 .utype = d\_utype, \

534 .ascii7 = true, \

535 }, \

536 .ptr = &ascii\_##d\_name, \

537 .bLength = USB\_STRING\_DESCRIPTOR\_LENGTH(d\_string), \

538 .bDescriptorType = USB\_DESC\_STRING, \

539 }

540

[ 552](group__usbd__api.md#ga18b1321daf1173a3cb0bc61a0d9beb34)#define USBD\_DESC\_MANUFACTURER\_DEFINE(d\_name, d\_string) \

553 USBD\_DESC\_STRING\_DEFINE(d\_name, d\_string, USBD\_DUT\_STRING\_MANUFACTURER)

554

[ 566](group__usbd__api.md#gaa5e43f9eac8f91d3896ea5e19baed031)#define USBD\_DESC\_PRODUCT\_DEFINE(d\_name, d\_string) \

567 USBD\_DESC\_STRING\_DEFINE(d\_name, d\_string, USBD\_DUT\_STRING\_PRODUCT)

568

[ 579](group__usbd__api.md#ga26af7f93205dc78eeb60a3c09aa7b2d3)#define USBD\_DESC\_SERIAL\_NUMBER\_DEFINE(d\_name) \

580 static struct usbd\_desc\_node d\_name = { \

581 .str = { \

582 .utype = USBD\_DUT\_STRING\_SERIAL\_NUMBER, \

583 .ascii7 = true, \

584 .use\_hwinfo = true, \

585 }, \

586 .bDescriptorType = USB\_DESC\_STRING, \

587 }

588

[ 598](group__usbd__api.md#ga45dc8df18f6fdf72edfd21f35d3046db)#define USBD\_DESC\_CONFIG\_DEFINE(d\_name, d\_string) \

599 USBD\_DESC\_STRING\_DEFINE(d\_name, d\_string, USBD\_DUT\_STRING\_CONFIG)

600

[ 611](group__usbd__api.md#ga620a5aa567dc4de7d5d1ef6b0cd9e937)#define USBD\_DESC\_BOS\_DEFINE(name, len, subset) \

612 static struct usbd\_desc\_node name = { \

613 .bos = { \

614 .utype = USBD\_DUT\_BOS\_NONE, \

615 }, \

616 .ptr = subset, \

617 .bLength = len, \

618 .bDescriptorType = USB\_DESC\_BOS, \

619 }

620

[ 632](group__usbd__api.md#gaaebebc77106848d8d62016936399776a)#define USBD\_DEFINE\_CLASS(class\_name, class\_api, class\_priv, class\_v\_reqs) \

633 static struct usbd\_class\_data class\_name = { \

634 .name = STRINGIFY(class\_name), \

635 .api = class\_api, \

636 .v\_reqs = class\_v\_reqs, \

637 .priv = class\_priv, \

638 }; \

639 static STRUCT\_SECTION\_ITERABLE\_ALTERNATE( \

640 usbd\_class\_fs, usbd\_class\_node, class\_name##\_fs) = { \

641 .c\_data = &class\_name, \

642 }; \

643 static STRUCT\_SECTION\_ITERABLE\_ALTERNATE( \

644 usbd\_class\_hs, usbd\_class\_node, class\_name##\_hs) = { \

645 .c\_data = &class\_name, \

646 }

647

[ 653](group__usbd__api.md#ga54ca08c74ae715281381d878f828727e)#define VENDOR\_REQ\_DEFINE(\_reqs, \_len) \

654 { \

655 .reqs = (const uint8\_t \*)(\_reqs), \

656 .len = (\_len), \

657 }

658

[ 663](group__usbd__api.md#ga464933a8332c11d15c92914aa1790e10)#define USBD\_VENDOR\_REQ(\_reqs...) \

664 VENDOR\_REQ\_DEFINE(((uint8\_t []) { \_reqs }), \

665 sizeof((uint8\_t []) { \_reqs }))

666

667

[ 678](group__usbd__api.md#ga33d0cef23d4b6c62b79b41559427b584)int [usbd\_add\_descriptor](group__usbd__api.md#ga33d0cef23d4b6c62b79b41559427b584)(struct [usbd\_context](structusbd__context.md) \*uds\_ctx,

679 struct [usbd\_desc\_node](structusbd__desc__node.md) \*dn);

680

[ 688](group__usbd__api.md#gab023ab276eb68c644895483344d33948)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [usbd\_str\_desc\_get\_idx](group__usbd__api.md#gab023ab276eb68c644895483344d33948)(const struct [usbd\_desc\_node](structusbd__desc__node.md) \*const desc\_nd);

689

[ 697](group__usbd__api.md#ga3146ee636b84c6d319365716f5741363)void [usbd\_remove\_descriptor](group__usbd__api.md#ga3146ee636b84c6d319365716f5741363)(struct [usbd\_desc\_node](structusbd__desc__node.md) \*const desc\_nd);

698

[ 708](group__usbd__api.md#ga5f4b69609f9a8f00a9e0fea4dffce1c4)int [usbd\_add\_configuration](group__usbd__api.md#ga5f4b69609f9a8f00a9e0fea4dffce1c4)(struct [usbd\_context](structusbd__context.md) \*uds\_ctx,

709 const enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) speed,

710 struct [usbd\_config\_node](structusbd__config__node.md) \*cd);

711

[ 733](group__usbd__api.md#ga4a837040e9d02c5773d69a6cf6c35960)int [usbd\_register\_class](group__usbd__api.md#ga4a837040e9d02c5773d69a6cf6c35960)(struct [usbd\_context](structusbd__context.md) \*uds\_ctx,

734 const char \*[name](structusbd__context.md#ade73c224b256007bf2d68bd1205ceb6e),

735 const enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) speed, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cfg);

736

[ 753](group__usbd__api.md#ga4382a5b4888baf65045faea0b88723f3)int [usbd\_register\_all\_classes](group__usbd__api.md#ga4382a5b4888baf65045faea0b88723f3)(struct [usbd\_context](structusbd__context.md) \*uds\_ctx,

754 const enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) speed, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cfg);

755

[ 770](group__usbd__api.md#ga1ae7a7a04f4ec1206d352d5c6401c51b)int [usbd\_unregister\_class](group__usbd__api.md#ga1ae7a7a04f4ec1206d352d5c6401c51b)(struct [usbd\_context](structusbd__context.md) \*uds\_ctx,

771 const char \*[name](structusbd__context.md#ade73c224b256007bf2d68bd1205ceb6e),

772 const enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) speed, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cfg);

773

[ 786](group__usbd__api.md#ga2996b5f6df459c8a179fc6c22f944063)int [usbd\_unregister\_all\_classes](group__usbd__api.md#ga2996b5f6df459c8a179fc6c22f944063)(struct [usbd\_context](structusbd__context.md) \*uds\_ctx,

787 const enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) speed, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cfg);

788

[ 797](group__usbd__api.md#ga2ebe08b8bf5ff3b64c4df1fcb346cf38)int [usbd\_msg\_register\_cb](group__usbd__api.md#ga2ebe08b8bf5ff3b64c4df1fcb346cf38)(struct [usbd\_context](structusbd__context.md) \*const uds\_ctx,

798 const [usbd\_msg\_cb\_t](group__usbd__api.md#ga2cd074cefff922b0816de37935d9646e) cb);

799

[ 813](group__usbd__api.md#ga78e5f07af641f9610cc32255efe1680f)int [usbd\_init](group__usbd__api.md#ga78e5f07af641f9610cc32255efe1680f)(struct [usbd\_context](structusbd__context.md) \*uds\_ctx);

814

[ 824](group__usbd__api.md#ga1a40fc13129e9218ca63ab3ca70d8d68)int [usbd\_enable](group__usbd__api.md#ga1a40fc13129e9218ca63ab3ca70d8d68)(struct [usbd\_context](structusbd__context.md) \*uds\_ctx);

825

[ 835](group__usbd__api.md#gaaa21e9f33175b7d2434e54e1b3d2799b)int [usbd\_disable](group__usbd__api.md#gaaa21e9f33175b7d2434e54e1b3d2799b)(struct [usbd\_context](structusbd__context.md) \*uds\_ctx);

836

[ 846](group__usbd__api.md#ga37585e0124a4d0d8cf6e65f13325eaf0)int [usbd\_shutdown](group__usbd__api.md#ga37585e0124a4d0d8cf6e65f13325eaf0)(struct [usbd\_context](structusbd__context.md) \*const uds\_ctx);

847

[ 856](group__usbd__api.md#ga176f42b2dd221c0de28ad9122a7d2693)int [usbd\_ep\_set\_halt](group__usbd__api.md#ga176f42b2dd221c0de28ad9122a7d2693)(struct [usbd\_context](structusbd__context.md) \*uds\_ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep);

857

[ 866](group__usbd__api.md#ga03729a4e9add3a55a7c3c2c8666a53a7)int [usbd\_ep\_clear\_halt](group__usbd__api.md#ga03729a4e9add3a55a7c3c2c8666a53a7)(struct [usbd\_context](structusbd__context.md) \*uds\_ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep);

867

[ 876](group__usbd__api.md#ga94cb8465b7bf85457f29e84b5b8ddfe9)bool [usbd\_ep\_is\_halted](group__usbd__api.md#ga94cb8465b7bf85457f29e84b5b8ddfe9)(struct [usbd\_context](structusbd__context.md) \*uds\_ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep);

877

[ 889](group__usbd__api.md#ga6c671d49c811b0af6b809f5940cd6d70)struct [net\_buf](structnet__buf.md) \*[usbd\_ep\_buf\_alloc](group__usbd__api.md#ga6c671d49c811b0af6b809f5940cd6d70)(const struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data,

890 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, const size\_t [size](structnet__buf.md#a1522d81a002804223e25300a6961f527));

891

[ 902](group__usbd__api.md#ga967d507d82d912119a732fd230bd561e)int [usbd\_ep\_ctrl\_enqueue](group__usbd__api.md#ga967d507d82d912119a732fd230bd561e)(struct [usbd\_context](structusbd__context.md) \*const uds\_ctx,

903 struct [net\_buf](structnet__buf.md) \*const buf);

904

[ 915](group__usbd__api.md#gaabf8333a7aefc4428f38e79a7264e383)int [usbd\_ep\_enqueue](group__usbd__api.md#gaabf8333a7aefc4428f38e79a7264e383)(const struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data,

916 struct [net\_buf](structnet__buf.md) \*const buf);

917

[ 926](group__usbd__api.md#ga1534058a609794e1d080aed98fcf5823)int [usbd\_ep\_dequeue](group__usbd__api.md#ga1534058a609794e1d080aed98fcf5823)(struct [usbd\_context](structusbd__context.md) \*uds\_ctx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep);

927

[ 938](group__usbd__api.md#ga8aa454c24495f2a462eae53b78c488dc)int [usbd\_ep\_buf\_free](group__usbd__api.md#ga8aa454c24495f2a462eae53b78c488dc)(struct [usbd\_context](structusbd__context.md) \*uds\_ctx, struct [net\_buf](structnet__buf.md) \*buf);

939

[ 947](group__usbd__api.md#ga5f7a5af958f7de8893e04ff2b7748c7e)bool [usbd\_is\_suspended](group__usbd__api.md#ga5f7a5af958f7de8893e04ff2b7748c7e)(struct [usbd\_context](structusbd__context.md) \*uds\_ctx);

948

[ 954](group__usbd__api.md#ga34086553e74795ffdc000349e61a3c8b)int [usbd\_wakeup\_request](group__usbd__api.md#ga34086553e74795ffdc000349e61a3c8b)(struct [usbd\_context](structusbd__context.md) \*uds\_ctx);

955

[ 963](group__usbd__api.md#gab4a0d05a8f183f7479ad33ee29e8a611)enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) [usbd\_bus\_speed](group__usbd__api.md#gab4a0d05a8f183f7479ad33ee29e8a611)(const struct [usbd\_context](structusbd__context.md) \*const uds\_ctx);

964

[ 972](group__usbd__api.md#gaab7c4692a30b58aa76b03b9e50460856)enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) [usbd\_caps\_speed](group__usbd__api.md#gaab7c4692a30b58aa76b03b9e50460856)(const struct [usbd\_context](structusbd__context.md) \*const uds\_ctx);

973

[ 983](group__usbd__api.md#gacb704bd4f396887c859932b2ab6b4991)int [usbd\_device\_set\_bcd\_usb](group__usbd__api.md#gacb704bd4f396887c859932b2ab6b4991)(struct [usbd\_context](structusbd__context.md) \*const uds\_ctx,

984 const enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) speed, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bcd);

985

[ 994](group__usbd__api.md#ga06aa9f954b6765e07494753bb4fa42d4)int [usbd\_device\_set\_vid](group__usbd__api.md#ga06aa9f954b6765e07494753bb4fa42d4)(struct [usbd\_context](structusbd__context.md) \*const uds\_ctx,

995 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vid);

996

[ 1005](group__usbd__api.md#ga44719fc03a50c70d75ce65e1d2f77a04)int [usbd\_device\_set\_pid](group__usbd__api.md#ga44719fc03a50c70d75ce65e1d2f77a04)(struct [usbd\_context](structusbd__context.md) \*const uds\_ctx,

1006 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) pid);

1007

[ 1016](group__usbd__api.md#gafda88e8a71c52addbe76ebeb874a8af5)int [usbd\_device\_set\_bcd\_device](group__usbd__api.md#gafda88e8a71c52addbe76ebeb874a8af5)(struct [usbd\_context](structusbd__context.md) \*const uds\_ctx,

1017 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bcd);

1018

[ 1030](group__usbd__api.md#ga83a58b50bec680513eabd3bb7075b511)int [usbd\_device\_set\_code\_triple](group__usbd__api.md#ga83a58b50bec680513eabd3bb7075b511)(struct [usbd\_context](structusbd__context.md) \*const uds\_ctx,

1031 const enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) speed,

1032 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) base\_class,

1033 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) subclass, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) protocol);

1034

[ 1045](group__usbd__api.md#ga2b803f8ac10d9375a74949cd2c2f3136)int [usbd\_config\_attrib\_rwup](group__usbd__api.md#ga2b803f8ac10d9375a74949cd2c2f3136)(struct [usbd\_context](structusbd__context.md) \*const uds\_ctx,

1046 const enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) speed,

1047 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cfg, const bool enable);

1048

[ 1059](group__usbd__api.md#ga8b0fff68bc6ce9d8ec4a7dfd59f0eade)int [usbd\_config\_attrib\_self](group__usbd__api.md#ga8b0fff68bc6ce9d8ec4a7dfd59f0eade)(struct [usbd\_context](structusbd__context.md) \*const uds\_ctx,

1060 const enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) speed,

1061 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cfg, const bool enable);

1062

[ 1073](group__usbd__api.md#ga59fc1ea6d943d26b0207bb6060e18f08)int [usbd\_config\_maxpower](group__usbd__api.md#ga59fc1ea6d943d26b0207bb6060e18f08)(struct [usbd\_context](structusbd__context.md) \*const uds\_ctx,

1074 const enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) speed,

1075 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cfg, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) power);

1076

[ 1089](group__usbd__api.md#ga5ea40d893980e24294e82d22855b407c)bool [usbd\_can\_detect\_vbus](group__usbd__api.md#ga5ea40d893980e24294e82d22855b407c)(struct [usbd\_context](structusbd__context.md) \*const uds\_ctx);

1090

1094

1095#ifdef \_\_cplusplus

1096}

1097#endif

1098

1099#endif /\* ZEPHYR\_INCLUDE\_USBD\_H\_ \*/

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[bos.h](bos_8h.md)

[device.h](device_8h.md)

[sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98)

struct \_dnode sys\_dnode\_t

Doubly-linked list node structure.

**Definition** dlist.h:54

[sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683)

struct \_dnode sys\_dlist\_t

Doubly-linked list structure.

**Definition** dlist.h:50

[sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8)

struct \_slist sys\_slist\_t

Single-linked list structure.

**Definition** slist.h:49

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[usbd\_ep\_clear\_halt](group__usbd__api.md#ga03729a4e9add3a55a7c3c2c8666a53a7)

int usbd\_ep\_clear\_halt(struct usbd\_context \*uds\_ctx, uint8\_t ep)

Clear endpoint halt.

[usbd\_device\_set\_vid](group__usbd__api.md#ga06aa9f954b6765e07494753bb4fa42d4)

int usbd\_device\_set\_vid(struct usbd\_context \*const uds\_ctx, const uint16\_t vid)

Set USB device descriptor value idVendor.

[usbd\_ep\_dequeue](group__usbd__api.md#ga1534058a609794e1d080aed98fcf5823)

int usbd\_ep\_dequeue(struct usbd\_context \*uds\_ctx, const uint8\_t ep)

Remove all USB device controller requests from endpoint queue.

[usbd\_ep\_set\_halt](group__usbd__api.md#ga176f42b2dd221c0de28ad9122a7d2693)

int usbd\_ep\_set\_halt(struct usbd\_context \*uds\_ctx, uint8\_t ep)

Halt endpoint.

[usbd\_enable](group__usbd__api.md#ga1a40fc13129e9218ca63ab3ca70d8d68)

int usbd\_enable(struct usbd\_context \*uds\_ctx)

Enable the USB device support and registered class instances.

[usbd\_unregister\_class](group__usbd__api.md#ga1ae7a7a04f4ec1206d352d5c6401c51b)

int usbd\_unregister\_class(struct usbd\_context \*uds\_ctx, const char \*name, const enum usbd\_speed speed, uint8\_t cfg)

Unregister an USB class instance.

[usbd\_unregister\_all\_classes](group__usbd__api.md#ga2996b5f6df459c8a179fc6c22f944063)

int usbd\_unregister\_all\_classes(struct usbd\_context \*uds\_ctx, const enum usbd\_speed speed, uint8\_t cfg)

Unregister all available USB class instances.

[usbd\_config\_attrib\_rwup](group__usbd__api.md#ga2b803f8ac10d9375a74949cd2c2f3136)

int usbd\_config\_attrib\_rwup(struct usbd\_context \*const uds\_ctx, const enum usbd\_speed speed, const uint8\_t cfg, const bool enable)

Setup USB device configuration attribute Remote Wakeup.

[usbd\_msg\_cb\_t](group__usbd__api.md#ga2cd074cefff922b0816de37935d9646e)

void(\* usbd\_msg\_cb\_t)(struct usbd\_context \*const ctx, const struct usbd\_msg \*const msg)

Callback type definition for USB device message delivery.

**Definition** usbd.h:220

[usbd\_class\_get\_private](group__usbd__api.md#ga2e511d0341b4e1bd57fb4420512eeeb5)

static void \* usbd\_class\_get\_private(const struct usbd\_class\_data \*const c\_data)

Get class implementation private data.

**Definition** usbd.h:391

[usbd\_msg\_register\_cb](group__usbd__api.md#ga2ebe08b8bf5ff3b64c4df1fcb346cf38)

int usbd\_msg\_register\_cb(struct usbd\_context \*const uds\_ctx, const usbd\_msg\_cb\_t cb)

Register USB notification message callback.

[usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71)

usbd\_speed

USB device speed.

**Definition** usbd.h:182

[usbd\_remove\_descriptor](group__usbd__api.md#ga3146ee636b84c6d319365716f5741363)

void usbd\_remove\_descriptor(struct usbd\_desc\_node \*const desc\_nd)

Remove USB string descriptor.

[usbd\_add\_descriptor](group__usbd__api.md#ga33d0cef23d4b6c62b79b41559427b584)

int usbd\_add\_descriptor(struct usbd\_context \*uds\_ctx, struct usbd\_desc\_node \*dn)

Add common USB descriptor.

[usbd\_wakeup\_request](group__usbd__api.md#ga34086553e74795ffdc000349e61a3c8b)

int usbd\_wakeup\_request(struct usbd\_context \*uds\_ctx)

Initiate the USB remote wakeup (TBD).

[usbd\_shutdown](group__usbd__api.md#ga37585e0124a4d0d8cf6e65f13325eaf0)

int usbd\_shutdown(struct usbd\_context \*const uds\_ctx)

Shutdown the USB device support.

[usbd\_register\_all\_classes](group__usbd__api.md#ga4382a5b4888baf65045faea0b88723f3)

int usbd\_register\_all\_classes(struct usbd\_context \*uds\_ctx, const enum usbd\_speed speed, uint8\_t cfg)

Register all available USB class instances.

[usbd\_device\_set\_pid](group__usbd__api.md#ga44719fc03a50c70d75ce65e1d2f77a04)

int usbd\_device\_set\_pid(struct usbd\_context \*const uds\_ctx, const uint16\_t pid)

Set USB device descriptor value idProduct.

[usbd\_register\_class](group__usbd__api.md#ga4a837040e9d02c5773d69a6cf6c35960)

int usbd\_register\_class(struct usbd\_context \*uds\_ctx, const char \*name, const enum usbd\_speed speed, uint8\_t cfg)

Register an USB class instance.

[usbd\_config\_maxpower](group__usbd__api.md#ga59fc1ea6d943d26b0207bb6060e18f08)

int usbd\_config\_maxpower(struct usbd\_context \*const uds\_ctx, const enum usbd\_speed speed, const uint8\_t cfg, const uint8\_t power)

Setup USB device configuration power consumption.

[usbd\_can\_detect\_vbus](group__usbd__api.md#ga5ea40d893980e24294e82d22855b407c)

bool usbd\_can\_detect\_vbus(struct usbd\_context \*const uds\_ctx)

Check that the controller can detect the VBUS state change.

[usbd\_add\_configuration](group__usbd__api.md#ga5f4b69609f9a8f00a9e0fea4dffce1c4)

int usbd\_add\_configuration(struct usbd\_context \*uds\_ctx, const enum usbd\_speed speed, struct usbd\_config\_node \*cd)

Add a USB device configuration.

[usbd\_is\_suspended](group__usbd__api.md#ga5f7a5af958f7de8893e04ff2b7748c7e)

bool usbd\_is\_suspended(struct usbd\_context \*uds\_ctx)

Checks whether the USB device controller is suspended.

[usbd\_ep\_buf\_alloc](group__usbd__api.md#ga6c671d49c811b0af6b809f5940cd6d70)

struct net\_buf \* usbd\_ep\_buf\_alloc(const struct usbd\_class\_data \*const c\_data, const uint8\_t ep, const size\_t size)

Allocate buffer for USB device request.

[usbd\_init](group__usbd__api.md#ga78e5f07af641f9610cc32255efe1680f)

int usbd\_init(struct usbd\_context \*uds\_ctx)

Initialize USB device.

[usbd\_device\_set\_code\_triple](group__usbd__api.md#ga83a58b50bec680513eabd3bb7075b511)

int usbd\_device\_set\_code\_triple(struct usbd\_context \*const uds\_ctx, const enum usbd\_speed speed, const uint8\_t base\_class, const uint8\_t subclass, const uint8\_t protocol)

Set USB device descriptor code triple Base Class, SubClass, and Protocol.

[usbd\_ep\_buf\_free](group__usbd__api.md#ga8aa454c24495f2a462eae53b78c488dc)

int usbd\_ep\_buf\_free(struct usbd\_context \*uds\_ctx, struct net\_buf \*buf)

Free USB device request buffer.

[usbd\_config\_attrib\_self](group__usbd__api.md#ga8b0fff68bc6ce9d8ec4a7dfd59f0eade)

int usbd\_config\_attrib\_self(struct usbd\_context \*const uds\_ctx, const enum usbd\_speed speed, const uint8\_t cfg, const bool enable)

Setup USB device configuration attribute Self-powered.

[usbd\_ep\_is\_halted](group__usbd__api.md#ga94cb8465b7bf85457f29e84b5b8ddfe9)

bool usbd\_ep\_is\_halted(struct usbd\_context \*uds\_ctx, uint8\_t ep)

Checks whether the endpoint is halted.

[usbd\_ch9\_state](group__usbd__api.md#ga95fb708d8a54eaa3ce0acc4e65519bbc)

usbd\_ch9\_state

USB device support middle layer runtime state.

**Definition** usbd.h:152

[usbd\_ep\_ctrl\_enqueue](group__usbd__api.md#ga967d507d82d912119a732fd230bd561e)

int usbd\_ep\_ctrl\_enqueue(struct usbd\_context \*const uds\_ctx, struct net\_buf \*const buf)

Queue USB device control request.

[usbd\_disable](group__usbd__api.md#gaaa21e9f33175b7d2434e54e1b3d2799b)

int usbd\_disable(struct usbd\_context \*uds\_ctx)

Disable the USB device support.

[usbd\_caps\_speed](group__usbd__api.md#gaab7c4692a30b58aa76b03b9e50460856)

enum usbd\_speed usbd\_caps\_speed(const struct usbd\_context \*const uds\_ctx)

Get highest speed supported by the controller.

[usbd\_ep\_enqueue](group__usbd__api.md#gaabf8333a7aefc4428f38e79a7264e383)

int usbd\_ep\_enqueue(const struct usbd\_class\_data \*const c\_data, struct net\_buf \*const buf)

Queue USB device request.

[usbd\_str\_desc\_get\_idx](group__usbd__api.md#gab023ab276eb68c644895483344d33948)

uint8\_t usbd\_str\_desc\_get\_idx(const struct usbd\_desc\_node \*const desc\_nd)

Get USB string descriptor index from descriptor node.

[usbd\_bus\_speed](group__usbd__api.md#gab4a0d05a8f183f7479ad33ee29e8a611)

enum usbd\_speed usbd\_bus\_speed(const struct usbd\_context \*const uds\_ctx)

Get actual device speed.

[usbd\_device\_set\_bcd\_usb](group__usbd__api.md#gacb704bd4f396887c859932b2ab6b4991)

int usbd\_device\_set\_bcd\_usb(struct usbd\_context \*const uds\_ctx, const enum usbd\_speed speed, const uint16\_t bcd)

Set USB device descriptor value bcdUSB.

[USBD\_NUMOF\_INTERFACES\_MAX](group__usbd__api.md#gaf8aadd499f7e0438acac4a7f36645d49)

#define USBD\_NUMOF\_INTERFACES\_MAX

**Definition** usbd.h:144

[usbd\_class\_get\_ctx](group__usbd__api.md#gaf97c68e75420bd5a1085c047577fd5a7)

static struct usbd\_context \* usbd\_class\_get\_ctx(const struct usbd\_class\_data \*const c\_data)

Get the USB device runtime context under which the class is registered.

**Definition** usbd.h:376

[usbd\_device\_set\_bcd\_device](group__usbd__api.md#gafda88e8a71c52addbe76ebeb874a8af5)

int usbd\_device\_set\_bcd\_device(struct usbd\_context \*const uds\_ctx, const uint16\_t bcd)

Set USB device descriptor value bcdDevice.

[USBD\_SPEED\_SS](group__usbd__api.md#gga2f2da3d634530f08cd59d408c811ad71a195490bdfa76ffca418e8bf2f3d3c96a)

@ USBD\_SPEED\_SS

Device supports or is connected to a super speed bus.

**Definition** usbd.h:188

[USBD\_SPEED\_FS](group__usbd__api.md#gga2f2da3d634530f08cd59d408c811ad71a30b20b0839dff88b038e680b55f382d7)

@ USBD\_SPEED\_FS

Device supports or is connected to a full speed bus.

**Definition** usbd.h:184

[USBD\_SPEED\_HS](group__usbd__api.md#gga2f2da3d634530f08cd59d408c811ad71abaf4bdba11db59d804d753e6fac92266)

@ USBD\_SPEED\_HS

Device supports or is connected to a high speed bus.

**Definition** usbd.h:186

[USBD\_STATE\_CONFIGURED](group__usbd__api.md#gga95fb708d8a54eaa3ce0acc4e65519bbca44c1920b09ea1062ea4d7ac31a846509)

@ USBD\_STATE\_CONFIGURED

**Definition** usbd.h:155

[USBD\_STATE\_DEFAULT](group__usbd__api.md#gga95fb708d8a54eaa3ce0acc4e65519bbca978c707d313eb49b70bc62dfae304048)

@ USBD\_STATE\_DEFAULT

**Definition** usbd.h:153

[USBD\_STATE\_ADDRESS](group__usbd__api.md#gga95fb708d8a54eaa3ce0acc4e65519bbca985f06c5505c5684a98954f15701cc9d)

@ USBD\_STATE\_ADDRESS

**Definition** usbd.h:154

[log.h](log_8h.md)

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[slist.h](slist_8h.md)

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

**Definition** device.h:412

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:2994

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** net\_buf.h:1006

[net\_buf::size](structnet__buf.md#a1522d81a002804223e25300a6961f527)

uint16\_t size

Amount of data that this buffer can store.

**Definition** net\_buf.h:1038

[usb\_setup\_packet](structusb__setup__packet.md)

USB Setup Data packet defined in spec.

**Definition** usb\_ch9.h:40

[usbd\_bos\_desc\_data](structusbd__bos__desc__data.md)

USBD BOS Device Capability descriptor data.

**Definition** usbd.h:98

[usbd\_bos\_desc\_data::utype](structusbd__bos__desc__data.md#a084578c905400488e5ce73c71f8aaf00)

enum usbd\_bos\_desc\_utype utype

Descriptor usage type (not bDescriptorType).

**Definition** usbd.h:100

[usbd\_cctx\_vendor\_req](structusbd__cctx__vendor__req.md)

Vendor Requests Table.

**Definition** usbd.h:257

[usbd\_cctx\_vendor\_req::reqs](structusbd__cctx__vendor__req.md#a2ddf3ce0c1c0a6d788b7ef30cf8d67ea)

const uint8\_t \* reqs

Array of vendor requests supported by the class.

**Definition** usbd.h:259

[usbd\_cctx\_vendor\_req::len](structusbd__cctx__vendor__req.md#a3b5e99bff9dbfa023a4e6a5b4a69abd0)

uint8\_t len

Length of the array.

**Definition** usbd.h:261

[usbd\_ch9\_data](structusbd__ch9__data.md)

USB device support middle layer runtime data.

**Definition** usbd.h:162

[usbd\_ch9\_data::ctrl\_type](structusbd__ch9__data.md#a095a2a98f19ea40e8bd1bf65eed77dac)

int ctrl\_type

Control type, internally used for stage verification.

**Definition** usbd.h:166

[usbd\_ch9\_data::configuration](structusbd__ch9__data.md#a1f759fb0d758e50c4589b6b6b1fd2a24)

uint8\_t configuration

USB device stack selected configuration.

**Definition** usbd.h:172

[usbd\_ch9\_data::ep\_halt](structusbd__ch9__data.md#a504360b7cb11240a2fda68344f2e3b62)

uint32\_t ep\_halt

Halted endpoints bitmap.

**Definition** usbd.h:170

[usbd\_ch9\_data::post\_status](structusbd__ch9__data.md#a6ab6f611fd1eff8d6fde0617c587fefb)

bool post\_status

Post status stage work required, e.g.

**Definition** usbd.h:174

[usbd\_ch9\_data::state](structusbd__ch9__data.md#a70d1a1be0aab6167ca4f4580b9c65eff)

enum usbd\_ch9\_state state

Protocol state of the USB device stack.

**Definition** usbd.h:168

[usbd\_ch9\_data::setup](structusbd__ch9__data.md#a85f96c69cede5b51c1f9739a4ae67f4d)

struct usb\_setup\_packet setup

Setup packet, up-to-date for the respective control request.

**Definition** usbd.h:164

[usbd\_ch9\_data::alternate](structusbd__ch9__data.md#a8f831eca1974b8411072f8102c444d45)

uint8\_t alternate[16U]

Array to track interfaces alternate settings.

**Definition** usbd.h:176

[usbd\_class\_api](structusbd__class__api.md)

USB device support class instance API.

**Definition** usbd.h:272

[usbd\_class\_api::feature\_halt](structusbd__class__api.md#a09475f1b29f482e548b6bc168dcd19e7)

void(\* feature\_halt)(struct usbd\_class\_data \*const c\_data, uint8\_t ep, bool halted)

Feature halt state update handler.

**Definition** usbd.h:274

[usbd\_class\_api::update](structusbd__class__api.md#a11d09e35f9d4c4d6b18e12bf4ea241b0)

void(\* update)(struct usbd\_class\_data \*const c\_data, uint8\_t iface, uint8\_t alternate)

Configuration update handler.

**Definition** usbd.h:278

[usbd\_class\_api::sof](structusbd__class__api.md#a488b102936b5cd3e4095578119b71510)

void(\* sof)(struct usbd\_class\_data \*const c\_data)

Start of Frame.

**Definition** usbd.h:302

[usbd\_class\_api::suspended](structusbd__class__api.md#a598afe76b5c2f9e75a049fe785393e04)

void(\* suspended)(struct usbd\_class\_data \*const c\_data)

USB power management handler suspended.

**Definition** usbd.h:296

[usbd\_class\_api::shutdown](structusbd__class__api.md#a5ca5bc6d3f5220bd3658d9398e09016e)

void(\* shutdown)(struct usbd\_class\_data \*const c\_data)

Shutdown of the class implementation.

**Definition** usbd.h:314

[usbd\_class\_api::request](structusbd__class__api.md#a70425718fd34534fd976240340b4496d)

int(\* request)(struct usbd\_class\_data \*const c\_data, struct net\_buf \*buf, int err)

Endpoint request completion event handler.

**Definition** usbd.h:292

[usbd\_class\_api::init](structusbd__class__api.md#a7d749f007d70e30f76aa121067b7a5c6)

int(\* init)(struct usbd\_class\_data \*const c\_data)

Initialization of the class implementation.

**Definition** usbd.h:311

[usbd\_class\_api::control\_to\_dev](structusbd__class__api.md#ab37dd5f2bf4029f149e69046702626a1)

int(\* control\_to\_dev)(struct usbd\_class\_data \*const c\_data, const struct usb\_setup\_packet \*const setup, const struct net\_buf \*const buf)

USB control request handler to device.

**Definition** usbd.h:282

[usbd\_class\_api::enable](structusbd__class__api.md#ab42f61db338471f0c5260576680409e9)

void(\* enable)(struct usbd\_class\_data \*const c\_data)

Class associated configuration is selected.

**Definition** usbd.h:305

[usbd\_class\_api::control\_to\_host](structusbd__class__api.md#ac52356c07c26a3bcb1025cd6778ca8ef)

int(\* control\_to\_host)(struct usbd\_class\_data \*const c\_data, const struct usb\_setup\_packet \*const setup, struct net\_buf \*const buf)

USB control request handler to host.

**Definition** usbd.h:287

[usbd\_class\_api::resumed](structusbd__class__api.md#ae6f3a658e5768f5d6672cd0e5f2d24a5)

void(\* resumed)(struct usbd\_class\_data \*const c\_data)

USB power management handler resumed.

**Definition** usbd.h:299

[usbd\_class\_api::disable](structusbd__class__api.md#afd43bfa4aab664c50648aa59a0c713de)

void(\* disable)(struct usbd\_class\_data \*const c\_data)

Class associated configuration is disabled.

**Definition** usbd.h:308

[usbd\_class\_data](structusbd__class__data.md)

USB device support class data.

**Definition** usbd.h:324

[usbd\_class\_data::priv](structusbd__class__data.md#a10bb5b9af6098fbbc86fd00ef54e84e1)

void \* priv

Pointer to private data.

**Definition** usbd.h:334

[usbd\_class\_data::uds\_ctx](structusbd__class__data.md#a111a803092fd389a500fb99bfc71b29a)

struct usbd\_context \* uds\_ctx

Pointer to USB device stack context structure.

**Definition** usbd.h:328

[usbd\_class\_data::v\_reqs](structusbd__class__data.md#a32db83ecf80e1ac9e4d5deda54581deb)

const struct usbd\_cctx\_vendor\_req \* v\_reqs

Supported vendor request table, can be NULL.

**Definition** usbd.h:332

[usbd\_class\_data::api](structusbd__class__data.md#a9109af3e25c499d4ef1f0746bf6a20cc)

const struct usbd\_class\_api \* api

Pointer to device support class API.

**Definition** usbd.h:330

[usbd\_class\_data::name](structusbd__class__data.md#ad251371b0e401fb2bffd6aaa1ff49063)

const char \* name

Name of the USB device class instance.

**Definition** usbd.h:326

[usbd\_config\_node](structusbd__config__node.md)

Device configuration node.

**Definition** usbd.h:132

[usbd\_config\_node::node](structusbd__config__node.md#a003a8d9132b319f54583263c4da1e060)

sys\_snode\_t node

slist node struct

**Definition** usbd.h:134

[usbd\_config\_node::class\_list](structusbd__config__node.md#a00493162af2344d3d39f834b4834ef78)

sys\_slist\_t class\_list

List of registered classes (functions).

**Definition** usbd.h:140

[usbd\_config\_node::str\_desc\_nd](structusbd__config__node.md#a19203885a9698861f849bd0fd57cb37f)

struct usbd\_desc\_node \* str\_desc\_nd

Optional pointer to string descriptor node.

**Definition** usbd.h:138

[usbd\_config\_node::desc](structusbd__config__node.md#a55081d79ab3e6b41a091b3f65d7d2d87)

void \* desc

Pointer to configuration descriptor.

**Definition** usbd.h:136

[usbd\_context](structusbd__context.md)

USB device support runtime context.

**Definition** usbd.h:229

[usbd\_context::fs\_desc](structusbd__context.md#a193420cc196f115cbd6947b10d542ee5)

void \* fs\_desc

Pointer to Full-Speed device descriptor.

**Definition** usbd.h:249

[usbd\_context::hs\_desc](structusbd__context.md#a250e2f82c7239ce81b104b6ef3c16857)

void \* hs\_desc

Pointer to High-Speed device descriptor.

**Definition** usbd.h:251

[usbd\_context::msg\_cb](structusbd__context.md#a300ab0384b3d4e7f3d7d188a27a78be3)

usbd\_msg\_cb\_t msg\_cb

Notification message recipient callback.

**Definition** usbd.h:237

[usbd\_context::status](structusbd__context.md#a3acad44126b6c3d56823ef7408332087)

struct usbd\_status status

Status of the USB device support.

**Definition** usbd.h:247

[usbd\_context::hs\_configs](structusbd__context.md#a4a6bd413d06328ffa5db089e35157376)

sys\_slist\_t hs\_configs

slist to manage High-Speed device configurations

**Definition** usbd.h:245

[usbd\_context::ch9\_data](structusbd__context.md#a4fb1545ec02e7d38766cee9940edc1eb)

struct usbd\_ch9\_data ch9\_data

Middle layer runtime data.

**Definition** usbd.h:239

[usbd\_context::dev](structusbd__context.md#a52c2cc6118b46fbcbc7a495df61f6b6c)

const struct device \* dev

Pointer to UDC device.

**Definition** usbd.h:235

[usbd\_context::fs\_configs](structusbd__context.md#a8c7d153a73859dd8ba25265f059f7495)

sys\_slist\_t fs\_configs

slist to manage Full-Speed device configurations

**Definition** usbd.h:243

[usbd\_context::mutex](structusbd__context.md#a8ff2a4303b73db67eeabdd999736b3a6)

struct k\_mutex mutex

Access mutex.

**Definition** usbd.h:233

[usbd\_context::name](structusbd__context.md#ade73c224b256007bf2d68bd1205ceb6e)

const char \* name

Name of the USB device.

**Definition** usbd.h:231

[usbd\_context::descriptors](structusbd__context.md#adf8dd86f2784cc69ce6da314adc00b72)

sys\_dlist\_t descriptors

slist to manage descriptors like string, BOS

**Definition** usbd.h:241

[usbd\_desc\_node](structusbd__desc__node.md)

Descriptor node.

**Definition** usbd.h:109

[usbd\_desc\_node::bDescriptorType](structusbd__desc__node.md#a786e2911b5ec7d6c908c148be4d27f5f)

uint8\_t bDescriptorType

Descriptor type.

**Definition** usbd.h:121

[usbd\_desc\_node::node](structusbd__desc__node.md#a9f1941cd036c01387d8ad9a4aceb595a)

sys\_dnode\_t node

slist node struct

**Definition** usbd.h:111

[usbd\_desc\_node::ptr](structusbd__desc__node.md#ac437b472e012e8fdec049f28e9f88944)

const void \*const ptr

Opaque pointer to a descriptor payload.

**Definition** usbd.h:117

[usbd\_desc\_node::bLength](structusbd__desc__node.md#ad71ef74fd7fe43a8117704553a3be01c)

uint8\_t bLength

Descriptor size in bytes.

**Definition** usbd.h:119

[usbd\_desc\_node::str](structusbd__desc__node.md#ae34fee200f7fd78355addafe79789cb4)

struct usbd\_str\_desc\_data str

**Definition** usbd.h:113

[usbd\_desc\_node::bos](structusbd__desc__node.md#afd65079b8b969fa4101a3f9f662c7b6b)

struct usbd\_bos\_desc\_data bos

**Definition** usbd.h:114

[usbd\_msg](structusbd__msg.md)

USB device message.

**Definition** usbd\_msg.h:82

[usbd\_status](structusbd__status.md)

USB device support status.

**Definition** usbd.h:194

[usbd\_status::rwup](structusbd__status.md#a113085892967cf7c9cb70131b320d61a)

unsigned int rwup

USB remote wake-up feature is enabled.

**Definition** usbd.h:202

[usbd\_status::enabled](structusbd__status.md#a2382fcb655fe51e0bcf83f85aa182ba3)

unsigned int enabled

USB device support is enabled.

**Definition** usbd.h:198

[usbd\_status::speed](structusbd__status.md#a295009d25826732ba9eebd7735d93d23)

enum usbd\_speed speed

USB device speed.

**Definition** usbd.h:204

[usbd\_status::initialized](structusbd__status.md#a78de12245d08ecc71e09d5519fe0e857)

unsigned int initialized

USB device support is initialized.

**Definition** usbd.h:196

[usbd\_status::suspended](structusbd__status.md#afb67cfda187e40229f842c93aa09f0ba)

unsigned int suspended

USB device is suspended.

**Definition** usbd.h:200

[usbd\_str\_desc\_data](structusbd__str__desc__data.md)

Used internally to keep descriptors in order.

**Definition** usbd.h:84

[usbd\_str\_desc\_data::idx](structusbd__str__desc__data.md#a0654953d15160cc19cad86a407f655cb)

uint8\_t idx

Descriptor index, required for string descriptors.

**Definition** usbd.h:86

[usbd\_str\_desc\_data::utype](structusbd__str__desc__data.md#a2e6dfc9cbbd44457113899db988a84ca)

enum usbd\_str\_desc\_utype utype

Descriptor usage type (not bDescriptorType).

**Definition** usbd.h:88

[usbd\_str\_desc\_data::use\_hwinfo](structusbd__str__desc__data.md#a40459d114a339841e1f9c14b0d036fe8)

unsigned int use\_hwinfo

Device stack obtains SerialNumber using the HWINFO API.

**Definition** usbd.h:92

[usbd\_str\_desc\_data::ascii7](structusbd__str__desc__data.md#ad4d7c291f95973d20ff522b8a5ef65a0)

unsigned int ascii7

The string descriptor is in ASCII7 format.

**Definition** usbd.h:90

[byteorder.h](sys_2byteorder_8h.md)

Byte order helpers.

[iterable\_sections.h](sys_2iterable__sections_8h.md)

[udc\_buf.h](udc__buf_8h.md)

Buffers for USB device support.

[usb\_ch9.h](usb__ch9_8h.md)

USB Chapter 9 structures and definitions.

[usbd\_msg.h](usbd__msg_8h.md)

USB support message types and structure.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [usb](dir_d8285a9da4e2f530d10dd4c17d446a84.md)
- [usbd.h](usbd_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
