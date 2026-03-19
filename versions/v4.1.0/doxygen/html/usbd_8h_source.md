---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/usbd_8h_source.html
original_path: doxygen/html/usbd_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

64struct [usbd\_context](structusbd__context.md);

65

69enum usbd\_str\_desc\_utype {

70 USBD\_DUT\_STRING\_LANG,

71 USBD\_DUT\_STRING\_MANUFACTURER,

72 USBD\_DUT\_STRING\_PRODUCT,

73 USBD\_DUT\_STRING\_SERIAL\_NUMBER,

74 USBD\_DUT\_STRING\_CONFIG,

75 USBD\_DUT\_STRING\_INTERFACE,

76};

77

78enum usbd\_bos\_desc\_utype {

79 USBD\_DUT\_BOS\_NONE,

80 USBD\_DUT\_BOS\_VREQ,

81};

83

[ 87](structusbd__str__desc__data.md)struct [usbd\_str\_desc\_data](structusbd__str__desc__data.md) {

[ 89](structusbd__str__desc__data.md#a0654953d15160cc19cad86a407f655cb) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [idx](structusbd__str__desc__data.md#a0654953d15160cc19cad86a407f655cb);

[ 91](structusbd__str__desc__data.md#a2e6dfc9cbbd44457113899db988a84ca) enum usbd\_str\_desc\_utype [utype](structusbd__str__desc__data.md#a2e6dfc9cbbd44457113899db988a84ca) : 8;

[ 93](structusbd__str__desc__data.md#ad4d7c291f95973d20ff522b8a5ef65a0) unsigned int [ascii7](structusbd__str__desc__data.md#ad4d7c291f95973d20ff522b8a5ef65a0) : 1;

[ 95](structusbd__str__desc__data.md#a40459d114a339841e1f9c14b0d036fe8) unsigned int [use\_hwinfo](structusbd__str__desc__data.md#a40459d114a339841e1f9c14b0d036fe8) : 1;

96};

97

[ 131](structusbd__vreq__node.md)struct [usbd\_vreq\_node](structusbd__vreq__node.md) {

[ 133](structusbd__vreq__node.md#a3c68346e2f871b22fb6c3b282ddfdccb) [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) [node](structusbd__vreq__node.md#a3c68346e2f871b22fb6c3b282ddfdccb);

[ 135](structusbd__vreq__node.md#a91fe4c5cf5ccad89e81380a332a8f955) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [code](structusbd__vreq__node.md#a91fe4c5cf5ccad89e81380a332a8f955);

[ 137](structusbd__vreq__node.md#a976d236a26a47cd17316c8174e2ad04a) int (\*[to\_host](structusbd__vreq__node.md#a976d236a26a47cd17316c8174e2ad04a))(const struct [usbd\_context](structusbd__context.md) \*const ctx,

138 const struct [usb\_setup\_packet](structusb__setup__packet.md) \*const setup,

139 struct [net\_buf](structnet__buf.md) \*const buf);

[ 141](structusbd__vreq__node.md#ae69e3dd3b4cdc7deb1ccdd9d9ebe4ec3) int (\*[to\_dev](structusbd__vreq__node.md#ae69e3dd3b4cdc7deb1ccdd9d9ebe4ec3))(const struct [usbd\_context](structusbd__context.md) \*const ctx,

142 const struct [usb\_setup\_packet](structusb__setup__packet.md) \*const setup,

143 const struct [net\_buf](structnet__buf.md) \*const buf);

144};

145

[ 149](structusbd__bos__desc__data.md)struct [usbd\_bos\_desc\_data](structusbd__bos__desc__data.md) {

[ 151](structusbd__bos__desc__data.md#a084578c905400488e5ce73c71f8aaf00) enum usbd\_bos\_desc\_utype [utype](structusbd__bos__desc__data.md#a084578c905400488e5ce73c71f8aaf00) : 8;

152 union {

[ 153](structusbd__bos__desc__data.md#a2d8570c88670c4fbf2d79bb989da01d9) struct [usbd\_vreq\_node](structusbd__vreq__node.md) \*const [vreq\_nd](structusbd__bos__desc__data.md#a2d8570c88670c4fbf2d79bb989da01d9);

154 };

155};

156

[ 163](structusbd__desc__node.md)struct [usbd\_desc\_node](structusbd__desc__node.md) {

[ 165](structusbd__desc__node.md#a9f1941cd036c01387d8ad9a4aceb595a) [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) [node](structusbd__desc__node.md#a9f1941cd036c01387d8ad9a4aceb595a);

166 union {

[ 167](structusbd__desc__node.md#ae34fee200f7fd78355addafe79789cb4) struct [usbd\_str\_desc\_data](structusbd__str__desc__data.md) [str](structusbd__desc__node.md#ae34fee200f7fd78355addafe79789cb4);

[ 168](structusbd__desc__node.md#afd65079b8b969fa4101a3f9f662c7b6b) struct [usbd\_bos\_desc\_data](structusbd__bos__desc__data.md) [bos](structusbd__desc__node.md#afd65079b8b969fa4101a3f9f662c7b6b);

169 };

[ 171](structusbd__desc__node.md#ac437b472e012e8fdec049f28e9f88944) const void \*const [ptr](structusbd__desc__node.md#ac437b472e012e8fdec049f28e9f88944);

[ 173](structusbd__desc__node.md#ad71ef74fd7fe43a8117704553a3be01c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bLength](structusbd__desc__node.md#ad71ef74fd7fe43a8117704553a3be01c);

[ 175](structusbd__desc__node.md#a786e2911b5ec7d6c908c148be4d27f5f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDescriptorType](structusbd__desc__node.md#a786e2911b5ec7d6c908c148be4d27f5f);

176};

177

[ 186](structusbd__config__node.md)struct [usbd\_config\_node](structusbd__config__node.md) {

[ 188](structusbd__config__node.md#a003a8d9132b319f54583263c4da1e060) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structusbd__config__node.md#a003a8d9132b319f54583263c4da1e060);

[ 190](structusbd__config__node.md#a55081d79ab3e6b41a091b3f65d7d2d87) void \*[desc](structusbd__config__node.md#a55081d79ab3e6b41a091b3f65d7d2d87);

[ 192](structusbd__config__node.md#a19203885a9698861f849bd0fd57cb37f) struct [usbd\_desc\_node](structusbd__desc__node.md) \*[str\_desc\_nd](structusbd__config__node.md#a19203885a9698861f849bd0fd57cb37f);

[ 194](structusbd__config__node.md#a00493162af2344d3d39f834b4834ef78) [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) [class\_list](structusbd__config__node.md#a00493162af2344d3d39f834b4834ef78);

195};

196

197/\* TODO: Kconfig option USBD\_NUMOF\_INTERFACES\_MAX? \*/

[ 198](group__usbd__api.md#gaf8aadd499f7e0438acac4a7f36645d49)#define USBD\_NUMOF\_INTERFACES\_MAX 16U

199

[ 206](group__usbd__api.md#ga95fb708d8a54eaa3ce0acc4e65519bbc)enum [usbd\_ch9\_state](group__usbd__api.md#ga95fb708d8a54eaa3ce0acc4e65519bbc) {

[ 207](group__usbd__api.md#gga95fb708d8a54eaa3ce0acc4e65519bbca978c707d313eb49b70bc62dfae304048) [USBD\_STATE\_DEFAULT](group__usbd__api.md#gga95fb708d8a54eaa3ce0acc4e65519bbca978c707d313eb49b70bc62dfae304048) = 0,

[ 208](group__usbd__api.md#gga95fb708d8a54eaa3ce0acc4e65519bbca985f06c5505c5684a98954f15701cc9d) [USBD\_STATE\_ADDRESS](group__usbd__api.md#gga95fb708d8a54eaa3ce0acc4e65519bbca985f06c5505c5684a98954f15701cc9d),

[ 209](group__usbd__api.md#gga95fb708d8a54eaa3ce0acc4e65519bbca44c1920b09ea1062ea4d7ac31a846509) [USBD\_STATE\_CONFIGURED](group__usbd__api.md#gga95fb708d8a54eaa3ce0acc4e65519bbca44c1920b09ea1062ea4d7ac31a846509),

210};

211

212

[ 216](structusbd__ch9__data.md)struct [usbd\_ch9\_data](structusbd__ch9__data.md) {

[ 218](structusbd__ch9__data.md#a85f96c69cede5b51c1f9739a4ae67f4d) struct [usb\_setup\_packet](structusb__setup__packet.md) [setup](structusbd__ch9__data.md#a85f96c69cede5b51c1f9739a4ae67f4d);

[ 220](structusbd__ch9__data.md#a095a2a98f19ea40e8bd1bf65eed77dac) int [ctrl\_type](structusbd__ch9__data.md#a095a2a98f19ea40e8bd1bf65eed77dac);

[ 222](structusbd__ch9__data.md#a70d1a1be0aab6167ca4f4580b9c65eff) enum [usbd\_ch9\_state](group__usbd__api.md#ga95fb708d8a54eaa3ce0acc4e65519bbc) [state](structusbd__ch9__data.md#a70d1a1be0aab6167ca4f4580b9c65eff);

[ 224](structusbd__ch9__data.md#a504360b7cb11240a2fda68344f2e3b62) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ep\_halt](structusbd__ch9__data.md#a504360b7cb11240a2fda68344f2e3b62);

[ 226](structusbd__ch9__data.md#a1f759fb0d758e50c4589b6b6b1fd2a24) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [configuration](structusbd__ch9__data.md#a1f759fb0d758e50c4589b6b6b1fd2a24);

[ 228](structusbd__ch9__data.md#a6ab6f611fd1eff8d6fde0617c587fefb) bool [post\_status](structusbd__ch9__data.md#a6ab6f611fd1eff8d6fde0617c587fefb);

[ 230](structusbd__ch9__data.md#a8f831eca1974b8411072f8102c444d45) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [alternate](structusbd__ch9__data.md#a8f831eca1974b8411072f8102c444d45)[[USBD\_NUMOF\_INTERFACES\_MAX](group__usbd__api.md#gaf8aadd499f7e0438acac4a7f36645d49)];

231};

232

[ 236](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71)enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) {

[ 238](group__usbd__api.md#gga2f2da3d634530f08cd59d408c811ad71a30b20b0839dff88b038e680b55f382d7) [USBD\_SPEED\_FS](group__usbd__api.md#gga2f2da3d634530f08cd59d408c811ad71a30b20b0839dff88b038e680b55f382d7),

[ 240](group__usbd__api.md#gga2f2da3d634530f08cd59d408c811ad71abaf4bdba11db59d804d753e6fac92266) [USBD\_SPEED\_HS](group__usbd__api.md#gga2f2da3d634530f08cd59d408c811ad71abaf4bdba11db59d804d753e6fac92266),

[ 242](group__usbd__api.md#gga2f2da3d634530f08cd59d408c811ad71a195490bdfa76ffca418e8bf2f3d3c96a) [USBD\_SPEED\_SS](group__usbd__api.md#gga2f2da3d634530f08cd59d408c811ad71a195490bdfa76ffca418e8bf2f3d3c96a),

243};

244

[ 248](structusbd__status.md)struct [usbd\_status](structusbd__status.md) {

[ 250](structusbd__status.md#a78de12245d08ecc71e09d5519fe0e857) unsigned int [initialized](structusbd__status.md#a78de12245d08ecc71e09d5519fe0e857) : 1;

[ 252](structusbd__status.md#a2382fcb655fe51e0bcf83f85aa182ba3) unsigned int [enabled](structusbd__status.md#a2382fcb655fe51e0bcf83f85aa182ba3) : 1;

[ 254](structusbd__status.md#afb67cfda187e40229f842c93aa09f0ba) unsigned int [suspended](structusbd__status.md#afb67cfda187e40229f842c93aa09f0ba) : 1;

[ 256](structusbd__status.md#a113085892967cf7c9cb70131b320d61a) unsigned int [rwup](structusbd__status.md#a113085892967cf7c9cb70131b320d61a) : 1;

[ 258](structusbd__status.md#ae4107cb4f379cce8c0472a98483705b8) unsigned int [self\_powered](structusbd__status.md#ae4107cb4f379cce8c0472a98483705b8) : 1;

[ 260](structusbd__status.md#a295009d25826732ba9eebd7735d93d23) enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) [speed](structusbd__status.md#a295009d25826732ba9eebd7735d93d23) : 2;

261};

262

[ 274](group__usbd__api.md#ga2cd074cefff922b0816de37935d9646e)typedef void (\*[usbd\_msg\_cb\_t](group__usbd__api.md#ga2cd074cefff922b0816de37935d9646e))(struct [usbd\_context](structusbd__context.md) \*const ctx,

275 const struct [usbd\_msg](structusbd__msg.md) \*const msg);

276

[ 283](structusbd__context.md)struct [usbd\_context](structusbd__context.md) {

[ 285](structusbd__context.md#ade73c224b256007bf2d68bd1205ceb6e) const char \*[name](structusbd__context.md#ade73c224b256007bf2d68bd1205ceb6e);

[ 287](structusbd__context.md#a8ff2a4303b73db67eeabdd999736b3a6) struct [k\_mutex](structk__mutex.md) [mutex](structusbd__context.md#a8ff2a4303b73db67eeabdd999736b3a6);

[ 289](structusbd__context.md#a52c2cc6118b46fbcbc7a495df61f6b6c) const struct [device](structdevice.md) \*[dev](structusbd__context.md#a52c2cc6118b46fbcbc7a495df61f6b6c);

[ 291](structusbd__context.md#a300ab0384b3d4e7f3d7d188a27a78be3) [usbd\_msg\_cb\_t](group__usbd__api.md#ga2cd074cefff922b0816de37935d9646e) [msg\_cb](structusbd__context.md#a300ab0384b3d4e7f3d7d188a27a78be3);

[ 293](structusbd__context.md#a4fb1545ec02e7d38766cee9940edc1eb) struct [usbd\_ch9\_data](structusbd__ch9__data.md) [ch9\_data](structusbd__context.md#a4fb1545ec02e7d38766cee9940edc1eb);

[ 295](structusbd__context.md#adf8dd86f2784cc69ce6da314adc00b72) [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) [descriptors](structusbd__context.md#adf8dd86f2784cc69ce6da314adc00b72);

[ 297](structusbd__context.md#a8c7d153a73859dd8ba25265f059f7495) [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) [fs\_configs](structusbd__context.md#a8c7d153a73859dd8ba25265f059f7495);

[ 299](structusbd__context.md#a4a6bd413d06328ffa5db089e35157376) [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) [hs\_configs](structusbd__context.md#a4a6bd413d06328ffa5db089e35157376);

[ 301](structusbd__context.md#a6b463c6c01230bc68c50ba5bb5550e99) [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) [vreqs](structusbd__context.md#a6b463c6c01230bc68c50ba5bb5550e99);

[ 303](structusbd__context.md#a3acad44126b6c3d56823ef7408332087) struct [usbd\_status](structusbd__status.md) [status](structusbd__context.md#a3acad44126b6c3d56823ef7408332087);

[ 305](structusbd__context.md#a193420cc196f115cbd6947b10d542ee5) void \*[fs\_desc](structusbd__context.md#a193420cc196f115cbd6947b10d542ee5);

[ 307](structusbd__context.md#a250e2f82c7239ce81b104b6ef3c16857) void \*[hs\_desc](structusbd__context.md#a250e2f82c7239ce81b104b6ef3c16857);

308};

309

[ 313](structusbd__cctx__vendor__req.md)struct [usbd\_cctx\_vendor\_req](structusbd__cctx__vendor__req.md) {

[ 315](structusbd__cctx__vendor__req.md#a2ddf3ce0c1c0a6d788b7ef30cf8d67ea) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[reqs](structusbd__cctx__vendor__req.md#a2ddf3ce0c1c0a6d788b7ef30cf8d67ea);

[ 317](structusbd__cctx__vendor__req.md#a3b5e99bff9dbfa023a4e6a5b4a69abd0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structusbd__cctx__vendor__req.md#a3b5e99bff9dbfa023a4e6a5b4a69abd0);

318};

319

[ 321](group__usbd__api.md#ga588b9e156a49d3b0358bee185cdeebee)#define USBD\_CCTX\_REGISTERED 0

322

323struct [usbd\_class\_data](structusbd__class__data.md);

324

[ 328](structusbd__class__api.md)struct [usbd\_class\_api](structusbd__class__api.md) {

[ 330](structusbd__class__api.md#a09475f1b29f482e548b6bc168dcd19e7) void (\*[feature\_halt](structusbd__class__api.md#a09475f1b29f482e548b6bc168dcd19e7))(struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data,

331 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, bool halted);

332

[ 334](structusbd__class__api.md#a11d09e35f9d4c4d6b18e12bf4ea241b0) void (\*[update](structusbd__class__api.md#a11d09e35f9d4c4d6b18e12bf4ea241b0))(struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data,

335 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) iface, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) alternate);

336

[ 338](structusbd__class__api.md#ab37dd5f2bf4029f149e69046702626a1) int (\*[control\_to\_dev](structusbd__class__api.md#ab37dd5f2bf4029f149e69046702626a1))(struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data,

339 const struct [usb\_setup\_packet](structusb__setup__packet.md) \*const setup,

340 const struct [net\_buf](structnet__buf.md) \*const buf);

341

[ 343](structusbd__class__api.md#ac52356c07c26a3bcb1025cd6778ca8ef) int (\*[control\_to\_host](structusbd__class__api.md#ac52356c07c26a3bcb1025cd6778ca8ef))(struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data,

344 const struct [usb\_setup\_packet](structusb__setup__packet.md) \*const setup,

345 struct [net\_buf](structnet__buf.md) \*const buf);

346

[ 348](structusbd__class__api.md#a70425718fd34534fd976240340b4496d) int (\*[request](structusbd__class__api.md#a70425718fd34534fd976240340b4496d))(struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data,

349 struct [net\_buf](structnet__buf.md) \*buf, int err);

350

[ 352](structusbd__class__api.md#a598afe76b5c2f9e75a049fe785393e04) void (\*[suspended](structusbd__class__api.md#a598afe76b5c2f9e75a049fe785393e04))(struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data);

353

[ 355](structusbd__class__api.md#ae6f3a658e5768f5d6672cd0e5f2d24a5) void (\*[resumed](structusbd__class__api.md#ae6f3a658e5768f5d6672cd0e5f2d24a5))(struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data);

356

[ 358](structusbd__class__api.md#a488b102936b5cd3e4095578119b71510) void (\*[sof](structusbd__class__api.md#a488b102936b5cd3e4095578119b71510))(struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data);

359

[ 361](structusbd__class__api.md#ab42f61db338471f0c5260576680409e9) void (\*[enable](structusbd__class__api.md#ab42f61db338471f0c5260576680409e9))(struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data);

362

[ 364](structusbd__class__api.md#afd43bfa4aab664c50648aa59a0c713de) void (\*[disable](structusbd__class__api.md#afd43bfa4aab664c50648aa59a0c713de))(struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data);

365

[ 367](structusbd__class__api.md#a7d749f007d70e30f76aa121067b7a5c6) int (\*[init](structusbd__class__api.md#a7d749f007d70e30f76aa121067b7a5c6))(struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data);

368

[ 370](structusbd__class__api.md#a5ca5bc6d3f5220bd3658d9398e09016e) void (\*[shutdown](structusbd__class__api.md#a5ca5bc6d3f5220bd3658d9398e09016e))(struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data);

371

[ 373](structusbd__class__api.md#a9d6ecb2a5ff55427502ba7ad8f96a146) void \*(\*get\_desc)(struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data,

374 const enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) speed);

375};

376

[ 380](structusbd__class__data.md)struct [usbd\_class\_data](structusbd__class__data.md) {

[ 382](structusbd__class__data.md#ad251371b0e401fb2bffd6aaa1ff49063) const char \*[name](structusbd__class__data.md#ad251371b0e401fb2bffd6aaa1ff49063);

[ 384](structusbd__class__data.md#a111a803092fd389a500fb99bfc71b29a) struct [usbd\_context](structusbd__context.md) \*[uds\_ctx](structusbd__class__data.md#a111a803092fd389a500fb99bfc71b29a);

[ 386](structusbd__class__data.md#a9109af3e25c499d4ef1f0746bf6a20cc) const struct [usbd\_class\_api](structusbd__class__api.md) \*[api](structusbd__class__data.md#a9109af3e25c499d4ef1f0746bf6a20cc);

[ 388](structusbd__class__data.md#a32db83ecf80e1ac9e4d5deda54581deb) const struct [usbd\_cctx\_vendor\_req](structusbd__cctx__vendor__req.md) \*[v\_reqs](structusbd__class__data.md#a32db83ecf80e1ac9e4d5deda54581deb);

[ 390](structusbd__class__data.md#a10bb5b9af6098fbbc86fd00ef54e84e1) void \*[priv](structusbd__class__data.md#a10bb5b9af6098fbbc86fd00ef54e84e1);

391};

392

401struct usbd\_class\_node {

403 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

405 struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data;

409 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ep\_assigned;

413 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ep\_active;

415 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) iface\_bm;

417 [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90);

418};

419

421

[ 432](group__usbd__api.md#gaf97c68e75420bd5a1085c047577fd5a7)static inline struct [usbd\_context](structusbd__context.md) \*[usbd\_class\_get\_ctx](group__usbd__api.md#gaf97c68e75420bd5a1085c047577fd5a7)(const struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data)

433{

434 return c\_data->[uds\_ctx](structusbd__class__data.md#a111a803092fd389a500fb99bfc71b29a);

435}

436

[ 447](group__usbd__api.md#ga2e511d0341b4e1bd57fb4420512eeeb5)static inline void \*[usbd\_class\_get\_private](group__usbd__api.md#ga2e511d0341b4e1bd57fb4420512eeeb5)(const struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data)

448{

449 return c\_data->[priv](structusbd__class__data.md#a10bb5b9af6098fbbc86fd00ef54e84e1);

450}

451

[ 472](group__usbd__api.md#ga26777805f749f29efa882f9bf391473a)#define USBD\_DEVICE\_DEFINE(device\_name, udc\_dev, vid, pid) \

473 static struct usb\_device\_descriptor \

474 fs\_desc\_##device\_name = { \

475 .bLength = sizeof(struct usb\_device\_descriptor), \

476 .bDescriptorType = USB\_DESC\_DEVICE, \

477 .bcdUSB = sys\_cpu\_to\_le16(USB\_SRN\_2\_0), \

478 .bDeviceClass = USB\_BCC\_MISCELLANEOUS, \

479 .bDeviceSubClass = 2, \

480 .bDeviceProtocol = 1, \

481 .bMaxPacketSize0 = USB\_CONTROL\_EP\_MPS, \

482 .idVendor = vid, \

483 .idProduct = pid, \

484 .bcdDevice = sys\_cpu\_to\_le16(USB\_BCD\_DRN), \

485 .iManufacturer = 0, \

486 .iProduct = 0, \

487 .iSerialNumber = 0, \

488 .bNumConfigurations = 0, \

489 }; \

490 static struct usb\_device\_descriptor \

491 hs\_desc\_##device\_name = { \

492 .bLength = sizeof(struct usb\_device\_descriptor), \

493 .bDescriptorType = USB\_DESC\_DEVICE, \

494 .bcdUSB = sys\_cpu\_to\_le16(USB\_SRN\_2\_0), \

495 .bDeviceClass = USB\_BCC\_MISCELLANEOUS, \

496 .bDeviceSubClass = 2, \

497 .bDeviceProtocol = 1, \

498 .bMaxPacketSize0 = 64, \

499 .idVendor = vid, \

500 .idProduct = pid, \

501 .bcdDevice = sys\_cpu\_to\_le16(USB\_BCD\_DRN), \

502 .iManufacturer = 0, \

503 .iProduct = 0, \

504 .iSerialNumber = 0, \

505 .bNumConfigurations = 0, \

506 }; \

507 static STRUCT\_SECTION\_ITERABLE(usbd\_context, device\_name) = { \

508 .name = STRINGIFY(device\_name), \

509 .dev = udc\_dev, \

510 .fs\_desc = &fs\_desc\_##device\_name, \

511 .hs\_desc = &hs\_desc\_##device\_name, \

512 }

513

[ 531](group__usbd__api.md#ga2d98fd68eff66f36522688f3de527586)#define USBD\_CONFIGURATION\_DEFINE(name, attrib, power, desc\_nd) \

532 static struct usb\_cfg\_descriptor \

533 cfg\_desc\_##name = { \

534 .bLength = sizeof(struct usb\_cfg\_descriptor), \

535 .bDescriptorType = USB\_DESC\_CONFIGURATION, \

536 .wTotalLength = 0, \

537 .bNumInterfaces = 0, \

538 .bConfigurationValue = 1, \

539 .iConfiguration = 0, \

540 .bmAttributes = USB\_SCD\_RESERVED | (attrib), \

541 .bMaxPower = (power), \

542 }; \

543 BUILD\_ASSERT((power) < 256, "Too much power"); \

544 static struct usbd\_config\_node name = { \

545 .desc = &cfg\_desc\_##name, \

546 .str\_desc\_nd = desc\_nd, \

547 }

548

[ 562](group__usbd__api.md#gaec816a27118bcb289ab4840fcd22888e)#define USBD\_DESC\_LANG\_DEFINE(name) \

563 static uint16\_t langid\_##name = sys\_cpu\_to\_le16(0x0409); \

564 static struct usbd\_desc\_node name = { \

565 .str = { \

566 .idx = 0, \

567 .utype = USBD\_DUT\_STRING\_LANG, \

568 }, \

569 .ptr = &langid\_##name, \

570 .bLength = sizeof(struct usb\_string\_descriptor), \

571 .bDescriptorType = USB\_DESC\_STRING, \

572 }

573

[ 585](group__usbd__api.md#gaf800e2040ac30844cab463c13d1fcdf8)#define USBD\_DESC\_STRING\_DEFINE(d\_name, d\_string, d\_utype) \

586 static uint8\_t ascii\_##d\_name[USB\_BSTRING\_LENGTH(d\_string)] = d\_string; \

587 static struct usbd\_desc\_node d\_name = { \

588 .str = { \

589 .utype = d\_utype, \

590 .ascii7 = true, \

591 }, \

592 .ptr = &ascii\_##d\_name, \

593 .bLength = USB\_STRING\_DESCRIPTOR\_LENGTH(d\_string), \

594 .bDescriptorType = USB\_DESC\_STRING, \

595 }

596

[ 608](group__usbd__api.md#ga18b1321daf1173a3cb0bc61a0d9beb34)#define USBD\_DESC\_MANUFACTURER\_DEFINE(d\_name, d\_string) \

609 USBD\_DESC\_STRING\_DEFINE(d\_name, d\_string, USBD\_DUT\_STRING\_MANUFACTURER)

610

[ 622](group__usbd__api.md#gaa5e43f9eac8f91d3896ea5e19baed031)#define USBD\_DESC\_PRODUCT\_DEFINE(d\_name, d\_string) \

623 USBD\_DESC\_STRING\_DEFINE(d\_name, d\_string, USBD\_DUT\_STRING\_PRODUCT)

624

[ 635](group__usbd__api.md#ga26af7f93205dc78eeb60a3c09aa7b2d3)#define USBD\_DESC\_SERIAL\_NUMBER\_DEFINE(d\_name) \

636 static struct usbd\_desc\_node d\_name = { \

637 .str = { \

638 .utype = USBD\_DUT\_STRING\_SERIAL\_NUMBER, \

639 .ascii7 = true, \

640 .use\_hwinfo = true, \

641 }, \

642 .bDescriptorType = USB\_DESC\_STRING, \

643 }

644

[ 654](group__usbd__api.md#ga45dc8df18f6fdf72edfd21f35d3046db)#define USBD\_DESC\_CONFIG\_DEFINE(d\_name, d\_string) \

655 USBD\_DESC\_STRING\_DEFINE(d\_name, d\_string, USBD\_DUT\_STRING\_CONFIG)

656

[ 667](group__usbd__api.md#ga620a5aa567dc4de7d5d1ef6b0cd9e937)#define USBD\_DESC\_BOS\_DEFINE(name, len, subset) \

668 static struct usbd\_desc\_node name = { \

669 .bos = { \

670 .utype = USBD\_DUT\_BOS\_NONE, \

671 }, \

672 .ptr = subset, \

673 .bLength = len, \

674 .bDescriptorType = USB\_DESC\_BOS, \

675 }

676

[ 685](group__usbd__api.md#ga0bdfa97d67ee62aa32af5fad2670a8a0)#define USBD\_VREQUEST\_DEFINE(name, vcode, vto\_host, vto\_dev) \

686 static struct usbd\_vreq\_node name = { \

687 .code = vcode, \

688 .to\_host = vto\_host, \

689 .to\_dev = vto\_dev, \

690 }

691

[ 708](group__usbd__api.md#ga0481d759856a0dc4b937335e8768eedd)#define USBD\_DESC\_BOS\_VREQ\_DEFINE(name, len, subset, vcode, vto\_host, vto\_dev) \

709 USBD\_VREQUEST\_DEFINE(vreq\_nd\_##name, vcode, vto\_host, vto\_dev); \

710 static struct usbd\_desc\_node name = { \

711 .bos = { \

712 .utype = USBD\_DUT\_BOS\_VREQ, \

713 .vreq\_nd = &vreq\_nd\_##name, \

714 }, \

715 .ptr = subset, \

716 .bLength = len, \

717 .bDescriptorType = USB\_DESC\_BOS, \

718 }

719

[ 731](group__usbd__api.md#gaaebebc77106848d8d62016936399776a)#define USBD\_DEFINE\_CLASS(class\_name, class\_api, class\_priv, class\_v\_reqs) \

732 static struct usbd\_class\_data class\_name = { \

733 .name = STRINGIFY(class\_name), \

734 .api = class\_api, \

735 .v\_reqs = class\_v\_reqs, \

736 .priv = class\_priv, \

737 }; \

738 static STRUCT\_SECTION\_ITERABLE\_ALTERNATE( \

739 usbd\_class\_fs, usbd\_class\_node, class\_name##\_fs) = { \

740 .c\_data = &class\_name, \

741 }; \

742 static STRUCT\_SECTION\_ITERABLE\_ALTERNATE( \

743 usbd\_class\_hs, usbd\_class\_node, class\_name##\_hs) = { \

744 .c\_data = &class\_name, \

745 }

746

[ 752](group__usbd__api.md#ga54ca08c74ae715281381d878f828727e)#define VENDOR\_REQ\_DEFINE(\_reqs, \_len) \

753 { \

754 .reqs = (const uint8\_t \*)(\_reqs), \

755 .len = (\_len), \

756 }

757

[ 762](group__usbd__api.md#ga464933a8332c11d15c92914aa1790e10)#define USBD\_VENDOR\_REQ(\_reqs...) \

763 VENDOR\_REQ\_DEFINE(((uint8\_t []) { \_reqs }), \

764 sizeof((uint8\_t []) { \_reqs }))

765

766

[ 777](group__usbd__api.md#ga33d0cef23d4b6c62b79b41559427b584)int [usbd\_add\_descriptor](group__usbd__api.md#ga33d0cef23d4b6c62b79b41559427b584)(struct [usbd\_context](structusbd__context.md) \*uds\_ctx,

778 struct [usbd\_desc\_node](structusbd__desc__node.md) \*dn);

779

[ 787](group__usbd__api.md#gab023ab276eb68c644895483344d33948)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [usbd\_str\_desc\_get\_idx](group__usbd__api.md#gab023ab276eb68c644895483344d33948)(const struct [usbd\_desc\_node](structusbd__desc__node.md) \*const desc\_nd);

788

[ 796](group__usbd__api.md#ga3146ee636b84c6d319365716f5741363)void [usbd\_remove\_descriptor](group__usbd__api.md#ga3146ee636b84c6d319365716f5741363)(struct [usbd\_desc\_node](structusbd__desc__node.md) \*const desc\_nd);

797

[ 807](group__usbd__api.md#ga5f4b69609f9a8f00a9e0fea4dffce1c4)int [usbd\_add\_configuration](group__usbd__api.md#ga5f4b69609f9a8f00a9e0fea4dffce1c4)(struct [usbd\_context](structusbd__context.md) \*uds\_ctx,

808 const enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) speed,

809 struct [usbd\_config\_node](structusbd__config__node.md) \*cd);

810

[ 832](group__usbd__api.md#ga4a837040e9d02c5773d69a6cf6c35960)int [usbd\_register\_class](group__usbd__api.md#ga4a837040e9d02c5773d69a6cf6c35960)(struct [usbd\_context](structusbd__context.md) \*uds\_ctx,

833 const char \*[name](structusbd__context.md#ade73c224b256007bf2d68bd1205ceb6e),

834 const enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) speed, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cfg);

835

[ 867](group__usbd__api.md#ga06541b17f5afc917cc5154bd4d816ec3)int [usbd\_register\_all\_classes](group__usbd__api.md#ga06541b17f5afc917cc5154bd4d816ec3)(struct [usbd\_context](structusbd__context.md) \*uds\_ctx,

868 const enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) speed, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cfg,

869 const char \*const blocklist[]);

870

[ 885](group__usbd__api.md#ga1ae7a7a04f4ec1206d352d5c6401c51b)int [usbd\_unregister\_class](group__usbd__api.md#ga1ae7a7a04f4ec1206d352d5c6401c51b)(struct [usbd\_context](structusbd__context.md) \*uds\_ctx,

886 const char \*[name](structusbd__context.md#ade73c224b256007bf2d68bd1205ceb6e),

887 const enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) speed, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cfg);

888

[ 901](group__usbd__api.md#ga2996b5f6df459c8a179fc6c22f944063)int [usbd\_unregister\_all\_classes](group__usbd__api.md#ga2996b5f6df459c8a179fc6c22f944063)(struct [usbd\_context](structusbd__context.md) \*uds\_ctx,

902 const enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) speed, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cfg);

903

[ 912](group__usbd__api.md#ga2ebe08b8bf5ff3b64c4df1fcb346cf38)int [usbd\_msg\_register\_cb](group__usbd__api.md#ga2ebe08b8bf5ff3b64c4df1fcb346cf38)(struct [usbd\_context](structusbd__context.md) \*const uds\_ctx,

913 const [usbd\_msg\_cb\_t](group__usbd__api.md#ga2cd074cefff922b0816de37935d9646e) cb);

914

[ 928](group__usbd__api.md#ga78e5f07af641f9610cc32255efe1680f)int [usbd\_init](group__usbd__api.md#ga78e5f07af641f9610cc32255efe1680f)(struct [usbd\_context](structusbd__context.md) \*uds\_ctx);

929

[ 939](group__usbd__api.md#ga1a40fc13129e9218ca63ab3ca70d8d68)int [usbd\_enable](group__usbd__api.md#ga1a40fc13129e9218ca63ab3ca70d8d68)(struct [usbd\_context](structusbd__context.md) \*uds\_ctx);

940

[ 950](group__usbd__api.md#gaaa21e9f33175b7d2434e54e1b3d2799b)int [usbd\_disable](group__usbd__api.md#gaaa21e9f33175b7d2434e54e1b3d2799b)(struct [usbd\_context](structusbd__context.md) \*uds\_ctx);

951

[ 961](group__usbd__api.md#ga37585e0124a4d0d8cf6e65f13325eaf0)int [usbd\_shutdown](group__usbd__api.md#ga37585e0124a4d0d8cf6e65f13325eaf0)(struct [usbd\_context](structusbd__context.md) \*const uds\_ctx);

962

[ 971](group__usbd__api.md#ga176f42b2dd221c0de28ad9122a7d2693)int [usbd\_ep\_set\_halt](group__usbd__api.md#ga176f42b2dd221c0de28ad9122a7d2693)(struct [usbd\_context](structusbd__context.md) \*uds\_ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep);

972

[ 981](group__usbd__api.md#ga03729a4e9add3a55a7c3c2c8666a53a7)int [usbd\_ep\_clear\_halt](group__usbd__api.md#ga03729a4e9add3a55a7c3c2c8666a53a7)(struct [usbd\_context](structusbd__context.md) \*uds\_ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep);

982

[ 991](group__usbd__api.md#ga94cb8465b7bf85457f29e84b5b8ddfe9)bool [usbd\_ep\_is\_halted](group__usbd__api.md#ga94cb8465b7bf85457f29e84b5b8ddfe9)(struct [usbd\_context](structusbd__context.md) \*uds\_ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep);

992

[ 1004](group__usbd__api.md#ga6c671d49c811b0af6b809f5940cd6d70)struct [net\_buf](structnet__buf.md) \*[usbd\_ep\_buf\_alloc](group__usbd__api.md#ga6c671d49c811b0af6b809f5940cd6d70)(const struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data,

1005 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, const size\_t [size](structnet__buf.md#a1522d81a002804223e25300a6961f527));

1006

[ 1017](group__usbd__api.md#ga967d507d82d912119a732fd230bd561e)int [usbd\_ep\_ctrl\_enqueue](group__usbd__api.md#ga967d507d82d912119a732fd230bd561e)(struct [usbd\_context](structusbd__context.md) \*const uds\_ctx,

1018 struct [net\_buf](structnet__buf.md) \*const buf);

1019

[ 1030](group__usbd__api.md#gaabf8333a7aefc4428f38e79a7264e383)int [usbd\_ep\_enqueue](group__usbd__api.md#gaabf8333a7aefc4428f38e79a7264e383)(const struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data,

1031 struct [net\_buf](structnet__buf.md) \*const buf);

1032

[ 1041](group__usbd__api.md#ga1534058a609794e1d080aed98fcf5823)int [usbd\_ep\_dequeue](group__usbd__api.md#ga1534058a609794e1d080aed98fcf5823)(struct [usbd\_context](structusbd__context.md) \*uds\_ctx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep);

1042

[ 1053](group__usbd__api.md#ga8aa454c24495f2a462eae53b78c488dc)int [usbd\_ep\_buf\_free](group__usbd__api.md#ga8aa454c24495f2a462eae53b78c488dc)(struct [usbd\_context](structusbd__context.md) \*uds\_ctx, struct [net\_buf](structnet__buf.md) \*buf);

1054

[ 1062](group__usbd__api.md#ga5f7a5af958f7de8893e04ff2b7748c7e)bool [usbd\_is\_suspended](group__usbd__api.md#ga5f7a5af958f7de8893e04ff2b7748c7e)(struct [usbd\_context](structusbd__context.md) \*uds\_ctx);

1063

[ 1069](group__usbd__api.md#ga34086553e74795ffdc000349e61a3c8b)int [usbd\_wakeup\_request](group__usbd__api.md#ga34086553e74795ffdc000349e61a3c8b)(struct [usbd\_context](structusbd__context.md) \*uds\_ctx);

1070

[ 1080](group__usbd__api.md#ga9056e1f01b64ddd26db6a5ee45439e22)void [usbd\_self\_powered](group__usbd__api.md#ga9056e1f01b64ddd26db6a5ee45439e22)(struct [usbd\_context](structusbd__context.md) \*uds\_ctx, const bool status);

1081

[ 1089](group__usbd__api.md#gab4a0d05a8f183f7479ad33ee29e8a611)enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) [usbd\_bus\_speed](group__usbd__api.md#gab4a0d05a8f183f7479ad33ee29e8a611)(const struct [usbd\_context](structusbd__context.md) \*const uds\_ctx);

1090

[ 1098](group__usbd__api.md#gaab7c4692a30b58aa76b03b9e50460856)enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) [usbd\_caps\_speed](group__usbd__api.md#gaab7c4692a30b58aa76b03b9e50460856)(const struct [usbd\_context](structusbd__context.md) \*const uds\_ctx);

1099

[ 1109](group__usbd__api.md#gacb704bd4f396887c859932b2ab6b4991)int [usbd\_device\_set\_bcd\_usb](group__usbd__api.md#gacb704bd4f396887c859932b2ab6b4991)(struct [usbd\_context](structusbd__context.md) \*const uds\_ctx,

1110 const enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) speed, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bcd);

1111

[ 1120](group__usbd__api.md#ga06aa9f954b6765e07494753bb4fa42d4)int [usbd\_device\_set\_vid](group__usbd__api.md#ga06aa9f954b6765e07494753bb4fa42d4)(struct [usbd\_context](structusbd__context.md) \*const uds\_ctx,

1121 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vid);

1122

[ 1131](group__usbd__api.md#ga44719fc03a50c70d75ce65e1d2f77a04)int [usbd\_device\_set\_pid](group__usbd__api.md#ga44719fc03a50c70d75ce65e1d2f77a04)(struct [usbd\_context](structusbd__context.md) \*const uds\_ctx,

1132 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) pid);

1133

[ 1142](group__usbd__api.md#gafda88e8a71c52addbe76ebeb874a8af5)int [usbd\_device\_set\_bcd\_device](group__usbd__api.md#gafda88e8a71c52addbe76ebeb874a8af5)(struct [usbd\_context](structusbd__context.md) \*const uds\_ctx,

1143 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bcd);

1144

[ 1156](group__usbd__api.md#ga83a58b50bec680513eabd3bb7075b511)int [usbd\_device\_set\_code\_triple](group__usbd__api.md#ga83a58b50bec680513eabd3bb7075b511)(struct [usbd\_context](structusbd__context.md) \*const uds\_ctx,

1157 const enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) speed,

1158 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) base\_class,

1159 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) subclass, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) protocol);

1160

[ 1171](group__usbd__api.md#ga2b803f8ac10d9375a74949cd2c2f3136)int [usbd\_config\_attrib\_rwup](group__usbd__api.md#ga2b803f8ac10d9375a74949cd2c2f3136)(struct [usbd\_context](structusbd__context.md) \*const uds\_ctx,

1172 const enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) speed,

1173 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cfg, const bool enable);

1174

[ 1185](group__usbd__api.md#ga8b0fff68bc6ce9d8ec4a7dfd59f0eade)int [usbd\_config\_attrib\_self](group__usbd__api.md#ga8b0fff68bc6ce9d8ec4a7dfd59f0eade)(struct [usbd\_context](structusbd__context.md) \*const uds\_ctx,

1186 const enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) speed,

1187 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cfg, const bool enable);

1188

[ 1199](group__usbd__api.md#ga59fc1ea6d943d26b0207bb6060e18f08)int [usbd\_config\_maxpower](group__usbd__api.md#ga59fc1ea6d943d26b0207bb6060e18f08)(struct [usbd\_context](structusbd__context.md) \*const uds\_ctx,

1200 const enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) speed,

1201 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cfg, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) power);

1202

[ 1215](group__usbd__api.md#ga5ea40d893980e24294e82d22855b407c)bool [usbd\_can\_detect\_vbus](group__usbd__api.md#ga5ea40d893980e24294e82d22855b407c)(struct [usbd\_context](structusbd__context.md) \*const uds\_ctx);

1216

[ 1228](group__usbd__api.md#gaaebba63d8a8b78a1f06c1a5a476cd306)int [usbd\_device\_register\_vreq](group__usbd__api.md#gaaebba63d8a8b78a1f06c1a5a476cd306)(struct [usbd\_context](structusbd__context.md) \*const uds\_ctx,

1229 struct [usbd\_vreq\_node](structusbd__vreq__node.md) \*const vreq\_nd);

1230

1234

1235#ifdef \_\_cplusplus

1236}

1237#endif

1238

1239#endif /\* ZEPHYR\_INCLUDE\_USBD\_H\_ \*/

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

[usbd\_register\_all\_classes](group__usbd__api.md#ga06541b17f5afc917cc5154bd4d816ec3)

int usbd\_register\_all\_classes(struct usbd\_context \*uds\_ctx, const enum usbd\_speed speed, uint8\_t cfg, const char \*const blocklist[])

Register all available USB class instances.

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

**Definition** usbd.h:274

[usbd\_class\_get\_private](group__usbd__api.md#ga2e511d0341b4e1bd57fb4420512eeeb5)

static void \* usbd\_class\_get\_private(const struct usbd\_class\_data \*const c\_data)

Get class implementation private data.

**Definition** usbd.h:447

[usbd\_msg\_register\_cb](group__usbd__api.md#ga2ebe08b8bf5ff3b64c4df1fcb346cf38)

int usbd\_msg\_register\_cb(struct usbd\_context \*const uds\_ctx, const usbd\_msg\_cb\_t cb)

Register USB notification message callback.

[usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71)

usbd\_speed

USB device speed.

**Definition** usbd.h:236

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

[usbd\_self\_powered](group__usbd__api.md#ga9056e1f01b64ddd26db6a5ee45439e22)

void usbd\_self\_powered(struct usbd\_context \*uds\_ctx, const bool status)

Set the self-powered status of the USB device.

[usbd\_ep\_is\_halted](group__usbd__api.md#ga94cb8465b7bf85457f29e84b5b8ddfe9)

bool usbd\_ep\_is\_halted(struct usbd\_context \*uds\_ctx, uint8\_t ep)

Checks whether the endpoint is halted.

[usbd\_ch9\_state](group__usbd__api.md#ga95fb708d8a54eaa3ce0acc4e65519bbc)

usbd\_ch9\_state

USB device support middle layer runtime state.

**Definition** usbd.h:206

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

[usbd\_device\_register\_vreq](group__usbd__api.md#gaaebba63d8a8b78a1f06c1a5a476cd306)

int usbd\_device\_register\_vreq(struct usbd\_context \*const uds\_ctx, struct usbd\_vreq\_node \*const vreq\_nd)

Register an USB vendor request with recipient device.

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

**Definition** usbd.h:198

[usbd\_class\_get\_ctx](group__usbd__api.md#gaf97c68e75420bd5a1085c047577fd5a7)

static struct usbd\_context \* usbd\_class\_get\_ctx(const struct usbd\_class\_data \*const c\_data)

Get the USB device runtime context under which the class is registered.

**Definition** usbd.h:432

[usbd\_device\_set\_bcd\_device](group__usbd__api.md#gafda88e8a71c52addbe76ebeb874a8af5)

int usbd\_device\_set\_bcd\_device(struct usbd\_context \*const uds\_ctx, const uint16\_t bcd)

Set USB device descriptor value bcdDevice.

[USBD\_SPEED\_SS](group__usbd__api.md#gga2f2da3d634530f08cd59d408c811ad71a195490bdfa76ffca418e8bf2f3d3c96a)

@ USBD\_SPEED\_SS

Device supports or is connected to a super speed bus.

**Definition** usbd.h:242

[USBD\_SPEED\_FS](group__usbd__api.md#gga2f2da3d634530f08cd59d408c811ad71a30b20b0839dff88b038e680b55f382d7)

@ USBD\_SPEED\_FS

Device supports or is connected to a full speed bus.

**Definition** usbd.h:238

[USBD\_SPEED\_HS](group__usbd__api.md#gga2f2da3d634530f08cd59d408c811ad71abaf4bdba11db59d804d753e6fac92266)

@ USBD\_SPEED\_HS

Device supports or is connected to a high speed bus.

**Definition** usbd.h:240

[USBD\_STATE\_CONFIGURED](group__usbd__api.md#gga95fb708d8a54eaa3ce0acc4e65519bbca44c1920b09ea1062ea4d7ac31a846509)

@ USBD\_STATE\_CONFIGURED

**Definition** usbd.h:209

[USBD\_STATE\_DEFAULT](group__usbd__api.md#gga95fb708d8a54eaa3ce0acc4e65519bbca978c707d313eb49b70bc62dfae304048)

@ USBD\_STATE\_DEFAULT

**Definition** usbd.h:207

[USBD\_STATE\_ADDRESS](group__usbd__api.md#gga95fb708d8a54eaa3ce0acc4e65519bbca985f06c5505c5684a98954f15701cc9d)

@ USBD\_STATE\_ADDRESS

**Definition** usbd.h:208

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

**Definition** device.h:453

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

[usb\_setup\_packet](structusb__setup__packet.md)

USB Setup Data packet defined in spec.

**Definition** usb\_ch9.h:40

[usbd\_bos\_desc\_data](structusbd__bos__desc__data.md)

USBD BOS Device Capability descriptor data.

**Definition** usbd.h:149

[usbd\_bos\_desc\_data::utype](structusbd__bos__desc__data.md#a084578c905400488e5ce73c71f8aaf00)

enum usbd\_bos\_desc\_utype utype

Descriptor usage type (not bDescriptorType).

**Definition** usbd.h:151

[usbd\_bos\_desc\_data::vreq\_nd](structusbd__bos__desc__data.md#a2d8570c88670c4fbf2d79bb989da01d9)

struct usbd\_vreq\_node \*const vreq\_nd

**Definition** usbd.h:153

[usbd\_cctx\_vendor\_req](structusbd__cctx__vendor__req.md)

Vendor Requests Table.

**Definition** usbd.h:313

[usbd\_cctx\_vendor\_req::reqs](structusbd__cctx__vendor__req.md#a2ddf3ce0c1c0a6d788b7ef30cf8d67ea)

const uint8\_t \* reqs

Array of vendor requests supported by the class.

**Definition** usbd.h:315

[usbd\_cctx\_vendor\_req::len](structusbd__cctx__vendor__req.md#a3b5e99bff9dbfa023a4e6a5b4a69abd0)

uint8\_t len

Length of the array.

**Definition** usbd.h:317

[usbd\_ch9\_data](structusbd__ch9__data.md)

USB device support middle layer runtime data.

**Definition** usbd.h:216

[usbd\_ch9\_data::ctrl\_type](structusbd__ch9__data.md#a095a2a98f19ea40e8bd1bf65eed77dac)

int ctrl\_type

Control type, internally used for stage verification.

**Definition** usbd.h:220

[usbd\_ch9\_data::configuration](structusbd__ch9__data.md#a1f759fb0d758e50c4589b6b6b1fd2a24)

uint8\_t configuration

USB device stack selected configuration.

**Definition** usbd.h:226

[usbd\_ch9\_data::ep\_halt](structusbd__ch9__data.md#a504360b7cb11240a2fda68344f2e3b62)

uint32\_t ep\_halt

Halted endpoints bitmap.

**Definition** usbd.h:224

[usbd\_ch9\_data::post\_status](structusbd__ch9__data.md#a6ab6f611fd1eff8d6fde0617c587fefb)

bool post\_status

Post status stage work required, e.g.

**Definition** usbd.h:228

[usbd\_ch9\_data::state](structusbd__ch9__data.md#a70d1a1be0aab6167ca4f4580b9c65eff)

enum usbd\_ch9\_state state

Protocol state of the USB device stack.

**Definition** usbd.h:222

[usbd\_ch9\_data::setup](structusbd__ch9__data.md#a85f96c69cede5b51c1f9739a4ae67f4d)

struct usb\_setup\_packet setup

Setup packet, up-to-date for the respective control request.

**Definition** usbd.h:218

[usbd\_ch9\_data::alternate](structusbd__ch9__data.md#a8f831eca1974b8411072f8102c444d45)

uint8\_t alternate[16U]

Array to track interfaces alternate settings.

**Definition** usbd.h:230

[usbd\_class\_api](structusbd__class__api.md)

USB device support class instance API.

**Definition** usbd.h:328

[usbd\_class\_api::feature\_halt](structusbd__class__api.md#a09475f1b29f482e548b6bc168dcd19e7)

void(\* feature\_halt)(struct usbd\_class\_data \*const c\_data, uint8\_t ep, bool halted)

Feature halt state update handler.

**Definition** usbd.h:330

[usbd\_class\_api::update](structusbd__class__api.md#a11d09e35f9d4c4d6b18e12bf4ea241b0)

void(\* update)(struct usbd\_class\_data \*const c\_data, uint8\_t iface, uint8\_t alternate)

Configuration update handler.

**Definition** usbd.h:334

[usbd\_class\_api::sof](structusbd__class__api.md#a488b102936b5cd3e4095578119b71510)

void(\* sof)(struct usbd\_class\_data \*const c\_data)

Start of Frame.

**Definition** usbd.h:358

[usbd\_class\_api::suspended](structusbd__class__api.md#a598afe76b5c2f9e75a049fe785393e04)

void(\* suspended)(struct usbd\_class\_data \*const c\_data)

USB power management handler suspended.

**Definition** usbd.h:352

[usbd\_class\_api::shutdown](structusbd__class__api.md#a5ca5bc6d3f5220bd3658d9398e09016e)

void(\* shutdown)(struct usbd\_class\_data \*const c\_data)

Shutdown of the class implementation.

**Definition** usbd.h:370

[usbd\_class\_api::request](structusbd__class__api.md#a70425718fd34534fd976240340b4496d)

int(\* request)(struct usbd\_class\_data \*const c\_data, struct net\_buf \*buf, int err)

Endpoint request completion event handler.

**Definition** usbd.h:348

[usbd\_class\_api::init](structusbd__class__api.md#a7d749f007d70e30f76aa121067b7a5c6)

int(\* init)(struct usbd\_class\_data \*const c\_data)

Initialization of the class implementation.

**Definition** usbd.h:367

[usbd\_class\_api::control\_to\_dev](structusbd__class__api.md#ab37dd5f2bf4029f149e69046702626a1)

int(\* control\_to\_dev)(struct usbd\_class\_data \*const c\_data, const struct usb\_setup\_packet \*const setup, const struct net\_buf \*const buf)

USB control request handler to device.

**Definition** usbd.h:338

[usbd\_class\_api::enable](structusbd__class__api.md#ab42f61db338471f0c5260576680409e9)

void(\* enable)(struct usbd\_class\_data \*const c\_data)

Class associated configuration is selected.

**Definition** usbd.h:361

[usbd\_class\_api::control\_to\_host](structusbd__class__api.md#ac52356c07c26a3bcb1025cd6778ca8ef)

int(\* control\_to\_host)(struct usbd\_class\_data \*const c\_data, const struct usb\_setup\_packet \*const setup, struct net\_buf \*const buf)

USB control request handler to host.

**Definition** usbd.h:343

[usbd\_class\_api::resumed](structusbd__class__api.md#ae6f3a658e5768f5d6672cd0e5f2d24a5)

void(\* resumed)(struct usbd\_class\_data \*const c\_data)

USB power management handler resumed.

**Definition** usbd.h:355

[usbd\_class\_api::disable](structusbd__class__api.md#afd43bfa4aab664c50648aa59a0c713de)

void(\* disable)(struct usbd\_class\_data \*const c\_data)

Class associated configuration is disabled.

**Definition** usbd.h:364

[usbd\_class\_data](structusbd__class__data.md)

USB device support class data.

**Definition** usbd.h:380

[usbd\_class\_data::priv](structusbd__class__data.md#a10bb5b9af6098fbbc86fd00ef54e84e1)

void \* priv

Pointer to private data.

**Definition** usbd.h:390

[usbd\_class\_data::uds\_ctx](structusbd__class__data.md#a111a803092fd389a500fb99bfc71b29a)

struct usbd\_context \* uds\_ctx

Pointer to USB device stack context structure.

**Definition** usbd.h:384

[usbd\_class\_data::v\_reqs](structusbd__class__data.md#a32db83ecf80e1ac9e4d5deda54581deb)

const struct usbd\_cctx\_vendor\_req \* v\_reqs

Supported vendor request table, can be NULL.

**Definition** usbd.h:388

[usbd\_class\_data::api](structusbd__class__data.md#a9109af3e25c499d4ef1f0746bf6a20cc)

const struct usbd\_class\_api \* api

Pointer to device support class API.

**Definition** usbd.h:386

[usbd\_class\_data::name](structusbd__class__data.md#ad251371b0e401fb2bffd6aaa1ff49063)

const char \* name

Name of the USB device class instance.

**Definition** usbd.h:382

[usbd\_config\_node](structusbd__config__node.md)

Device configuration node.

**Definition** usbd.h:186

[usbd\_config\_node::node](structusbd__config__node.md#a003a8d9132b319f54583263c4da1e060)

sys\_snode\_t node

slist node struct

**Definition** usbd.h:188

[usbd\_config\_node::class\_list](structusbd__config__node.md#a00493162af2344d3d39f834b4834ef78)

sys\_slist\_t class\_list

List of registered classes (functions).

**Definition** usbd.h:194

[usbd\_config\_node::str\_desc\_nd](structusbd__config__node.md#a19203885a9698861f849bd0fd57cb37f)

struct usbd\_desc\_node \* str\_desc\_nd

Optional pointer to string descriptor node.

**Definition** usbd.h:192

[usbd\_config\_node::desc](structusbd__config__node.md#a55081d79ab3e6b41a091b3f65d7d2d87)

void \* desc

Pointer to configuration descriptor.

**Definition** usbd.h:190

[usbd\_context](structusbd__context.md)

USB device support runtime context.

**Definition** usbd.h:283

[usbd\_context::fs\_desc](structusbd__context.md#a193420cc196f115cbd6947b10d542ee5)

void \* fs\_desc

Pointer to Full-Speed device descriptor.

**Definition** usbd.h:305

[usbd\_context::hs\_desc](structusbd__context.md#a250e2f82c7239ce81b104b6ef3c16857)

void \* hs\_desc

Pointer to High-Speed device descriptor.

**Definition** usbd.h:307

[usbd\_context::msg\_cb](structusbd__context.md#a300ab0384b3d4e7f3d7d188a27a78be3)

usbd\_msg\_cb\_t msg\_cb

Notification message recipient callback.

**Definition** usbd.h:291

[usbd\_context::status](structusbd__context.md#a3acad44126b6c3d56823ef7408332087)

struct usbd\_status status

Status of the USB device support.

**Definition** usbd.h:303

[usbd\_context::hs\_configs](structusbd__context.md#a4a6bd413d06328ffa5db089e35157376)

sys\_slist\_t hs\_configs

slist to manage High-Speed device configurations

**Definition** usbd.h:299

[usbd\_context::ch9\_data](structusbd__context.md#a4fb1545ec02e7d38766cee9940edc1eb)

struct usbd\_ch9\_data ch9\_data

Middle layer runtime data.

**Definition** usbd.h:293

[usbd\_context::dev](structusbd__context.md#a52c2cc6118b46fbcbc7a495df61f6b6c)

const struct device \* dev

Pointer to UDC device.

**Definition** usbd.h:289

[usbd\_context::vreqs](structusbd__context.md#a6b463c6c01230bc68c50ba5bb5550e99)

sys\_dlist\_t vreqs

dlist to manage vendor requests with recipient device

**Definition** usbd.h:301

[usbd\_context::fs\_configs](structusbd__context.md#a8c7d153a73859dd8ba25265f059f7495)

sys\_slist\_t fs\_configs

slist to manage Full-Speed device configurations

**Definition** usbd.h:297

[usbd\_context::mutex](structusbd__context.md#a8ff2a4303b73db67eeabdd999736b3a6)

struct k\_mutex mutex

Access mutex.

**Definition** usbd.h:287

[usbd\_context::name](structusbd__context.md#ade73c224b256007bf2d68bd1205ceb6e)

const char \* name

Name of the USB device.

**Definition** usbd.h:285

[usbd\_context::descriptors](structusbd__context.md#adf8dd86f2784cc69ce6da314adc00b72)

sys\_dlist\_t descriptors

slist to manage descriptors like string, BOS

**Definition** usbd.h:295

[usbd\_desc\_node](structusbd__desc__node.md)

Descriptor node.

**Definition** usbd.h:163

[usbd\_desc\_node::bDescriptorType](structusbd__desc__node.md#a786e2911b5ec7d6c908c148be4d27f5f)

uint8\_t bDescriptorType

Descriptor type.

**Definition** usbd.h:175

[usbd\_desc\_node::node](structusbd__desc__node.md#a9f1941cd036c01387d8ad9a4aceb595a)

sys\_dnode\_t node

slist node struct

**Definition** usbd.h:165

[usbd\_desc\_node::ptr](structusbd__desc__node.md#ac437b472e012e8fdec049f28e9f88944)

const void \*const ptr

Opaque pointer to a descriptor payload.

**Definition** usbd.h:171

[usbd\_desc\_node::bLength](structusbd__desc__node.md#ad71ef74fd7fe43a8117704553a3be01c)

uint8\_t bLength

Descriptor size in bytes.

**Definition** usbd.h:173

[usbd\_desc\_node::str](structusbd__desc__node.md#ae34fee200f7fd78355addafe79789cb4)

struct usbd\_str\_desc\_data str

**Definition** usbd.h:167

[usbd\_desc\_node::bos](structusbd__desc__node.md#afd65079b8b969fa4101a3f9f662c7b6b)

struct usbd\_bos\_desc\_data bos

**Definition** usbd.h:168

[usbd\_msg](structusbd__msg.md)

USB device message.

**Definition** usbd\_msg.h:88

[usbd\_status](structusbd__status.md)

USB device support status.

**Definition** usbd.h:248

[usbd\_status::rwup](structusbd__status.md#a113085892967cf7c9cb70131b320d61a)

unsigned int rwup

USB remote wake-up feature is enabled.

**Definition** usbd.h:256

[usbd\_status::enabled](structusbd__status.md#a2382fcb655fe51e0bcf83f85aa182ba3)

unsigned int enabled

USB device support is enabled.

**Definition** usbd.h:252

[usbd\_status::speed](structusbd__status.md#a295009d25826732ba9eebd7735d93d23)

enum usbd\_speed speed

USB device speed.

**Definition** usbd.h:260

[usbd\_status::initialized](structusbd__status.md#a78de12245d08ecc71e09d5519fe0e857)

unsigned int initialized

USB device support is initialized.

**Definition** usbd.h:250

[usbd\_status::self\_powered](structusbd__status.md#ae4107cb4f379cce8c0472a98483705b8)

unsigned int self\_powered

USB device is self-powered.

**Definition** usbd.h:258

[usbd\_status::suspended](structusbd__status.md#afb67cfda187e40229f842c93aa09f0ba)

unsigned int suspended

USB device is suspended.

**Definition** usbd.h:254

[usbd\_str\_desc\_data](structusbd__str__desc__data.md)

Used internally to keep descriptors in order.

**Definition** usbd.h:87

[usbd\_str\_desc\_data::idx](structusbd__str__desc__data.md#a0654953d15160cc19cad86a407f655cb)

uint8\_t idx

Descriptor index, required for string descriptors.

**Definition** usbd.h:89

[usbd\_str\_desc\_data::utype](structusbd__str__desc__data.md#a2e6dfc9cbbd44457113899db988a84ca)

enum usbd\_str\_desc\_utype utype

Descriptor usage type (not bDescriptorType).

**Definition** usbd.h:91

[usbd\_str\_desc\_data::use\_hwinfo](structusbd__str__desc__data.md#a40459d114a339841e1f9c14b0d036fe8)

unsigned int use\_hwinfo

Device stack obtains SerialNumber using the HWINFO API.

**Definition** usbd.h:95

[usbd\_str\_desc\_data::ascii7](structusbd__str__desc__data.md#ad4d7c291f95973d20ff522b8a5ef65a0)

unsigned int ascii7

The string descriptor is in ASCII7 format.

**Definition** usbd.h:93

[usbd\_vreq\_node](structusbd__vreq__node.md)

USBD vendor request node.

**Definition** usbd.h:131

[usbd\_vreq\_node::node](structusbd__vreq__node.md#a3c68346e2f871b22fb6c3b282ddfdccb)

sys\_dnode\_t node

Node information for the dlist.

**Definition** usbd.h:133

[usbd\_vreq\_node::code](structusbd__vreq__node.md#a91fe4c5cf5ccad89e81380a332a8f955)

const uint8\_t code

Vendor code (bRequest value).

**Definition** usbd.h:135

[usbd\_vreq\_node::to\_host](structusbd__vreq__node.md#a976d236a26a47cd17316c8174e2ad04a)

int(\* to\_host)(const struct usbd\_context \*const ctx, const struct usb\_setup\_packet \*const setup, struct net\_buf \*const buf)

Vendor request callback for device-to-host direction.

**Definition** usbd.h:137

[usbd\_vreq\_node::to\_dev](structusbd__vreq__node.md#ae69e3dd3b4cdc7deb1ccdd9d9ebe4ec3)

int(\* to\_dev)(const struct usbd\_context \*const ctx, const struct usb\_setup\_packet \*const setup, const struct net\_buf \*const buf)

Vendor request callback for host-to-device direction.

**Definition** usbd.h:141

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
