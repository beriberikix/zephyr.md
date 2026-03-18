---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/usbd_8h_source.html
original_path: doxygen/html/usbd_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

18#include <[zephyr/usb/usb\_ch9.h](usb__ch9_8h.md)>

19#include <[zephyr/net/buf.h](net_2buf_8h.md)>

20#include <[zephyr/sys/byteorder.h](sys_2byteorder_8h.md)>

21#include <[zephyr/sys/slist.h](slist_8h.md)>

22#include <[zephyr/logging/log.h](log_8h.md)>

23#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

24

25#ifdef \_\_cplusplus

26extern "C" {

27#endif

28

35

36/\*

37 \* The USB Unicode bString is encoded in UTF16LE, which means it takes up

38 \* twice the amount of bytes than the same string encoded in ASCII7.

39 \* Use this macro to determine the length of the bString array.

40 \*

41 \* bString length without null character:

42 \* bString\_length = (sizeof(initializer\_string) - 1) \* 2

43 \* or:

44 \* bString\_length = sizeof(initializer\_string) \* 2 - 2

45 \*/

[ 46](group__usbd__api.md#gac3d58cfa3f92b1811e9ed136c4450906)#define USB\_BSTRING\_LENGTH(s) (sizeof(s) \* 2 - 2)

47

48/\*

49 \* The length of the string descriptor (bLength) is calculated from the

50 \* size of the two octets bLength and bDescriptorType plus the

51 \* length of the UTF16LE string:

52 \*

53 \* bLength = 2 + bString\_length

54 \* bLength = 2 + sizeof(initializer\_string) \* 2 - 2

55 \* bLength = sizeof(initializer\_string) \* 2

56 \* Use this macro to determine the bLength of the string descriptor.

57 \*/

[ 58](group__usbd__api.md#gaef85e50556291fa93cbf72b01529b4a8)#define USB\_STRING\_DESCRIPTOR\_LENGTH(s) (sizeof(s) \* 2)

59

60/\* Used internally to keep descriptors in order \*/

[ 61](group__usbd__api.md#gaa7ed6f04fd7058c422f5ebc378f1a3da)enum [usbd\_desc\_usage\_type](group__usbd__api.md#gaa7ed6f04fd7058c422f5ebc378f1a3da) {

[ 62](group__usbd__api.md#ggaa7ed6f04fd7058c422f5ebc378f1a3daa984cc2f845e2e2bcc83d2e9f0138e3bd) [USBD\_DUT\_STRING\_LANG](group__usbd__api.md#ggaa7ed6f04fd7058c422f5ebc378f1a3daa984cc2f845e2e2bcc83d2e9f0138e3bd),

[ 63](group__usbd__api.md#ggaa7ed6f04fd7058c422f5ebc378f1a3daa25eb10630b10db28f9f97aa0b81f3c4e) [USBD\_DUT\_STRING\_MANUFACTURER](group__usbd__api.md#ggaa7ed6f04fd7058c422f5ebc378f1a3daa25eb10630b10db28f9f97aa0b81f3c4e),

[ 64](group__usbd__api.md#ggaa7ed6f04fd7058c422f5ebc378f1a3daa67c8a16639167a0a7a6f615d5aa6b73e) [USBD\_DUT\_STRING\_PRODUCT](group__usbd__api.md#ggaa7ed6f04fd7058c422f5ebc378f1a3daa67c8a16639167a0a7a6f615d5aa6b73e),

[ 65](group__usbd__api.md#ggaa7ed6f04fd7058c422f5ebc378f1a3daac4fff2e4994a473899aea6ed8a0ec782) [USBD\_DUT\_STRING\_SERIAL\_NUMBER](group__usbd__api.md#ggaa7ed6f04fd7058c422f5ebc378f1a3daac4fff2e4994a473899aea6ed8a0ec782),

[ 66](group__usbd__api.md#ggaa7ed6f04fd7058c422f5ebc378f1a3daaa4dd69c222492b1f12b3993c4640c80d) [USBD\_DUT\_STRING\_INTERFACE](group__usbd__api.md#ggaa7ed6f04fd7058c422f5ebc378f1a3daaa4dd69c222492b1f12b3993c4640c80d),

67};

68

[ 75](structusbd__desc__node.md)struct [usbd\_desc\_node](structusbd__desc__node.md) {

[ 77](structusbd__desc__node.md#a9f1941cd036c01387d8ad9a4aceb595a) [sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) [node](structusbd__desc__node.md#a9f1941cd036c01387d8ad9a4aceb595a);

[ 79](structusbd__desc__node.md#a0705a86aa6d7f532eb6be794f2c60d06) unsigned int [idx](structusbd__desc__node.md#a0705a86aa6d7f532eb6be794f2c60d06) : 8;

[ 81](structusbd__desc__node.md#a50e1b8db1dd6a4f3ca541394ad9d9adf) unsigned int [utype](structusbd__desc__node.md#a50e1b8db1dd6a4f3ca541394ad9d9adf) : 8;

[ 83](structusbd__desc__node.md#a266d0936f7684f6a3047e2a6d1875458) unsigned int [utf16le](structusbd__desc__node.md#a266d0936f7684f6a3047e2a6d1875458) : 1;

[ 85](structusbd__desc__node.md#a322537e0b35d0590ba0f4e19ae5bb3ac) unsigned int [custom\_sn](structusbd__desc__node.md#a322537e0b35d0590ba0f4e19ae5bb3ac) : 1;

[ 87](structusbd__desc__node.md#a4d4692341a7785b5a0af762b1810e80f) void \*[desc](structusbd__desc__node.md#a4d4692341a7785b5a0af762b1810e80f);

88};

89

[ 98](structusbd__config__node.md)struct [usbd\_config\_node](structusbd__config__node.md) {

[ 100](structusbd__config__node.md#a003a8d9132b319f54583263c4da1e060) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structusbd__config__node.md#a003a8d9132b319f54583263c4da1e060);

[ 102](structusbd__config__node.md#a55081d79ab3e6b41a091b3f65d7d2d87) void \*[desc](structusbd__config__node.md#a55081d79ab3e6b41a091b3f65d7d2d87);

[ 104](structusbd__config__node.md#a00493162af2344d3d39f834b4834ef78) [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) [class\_list](structusbd__config__node.md#a00493162af2344d3d39f834b4834ef78);

105};

106

107/\* TODO: Kconfig option USBD\_NUMOF\_INTERFACES\_MAX? \*/

[ 108](group__usbd__api.md#gaf8aadd499f7e0438acac4a7f36645d49)#define USBD\_NUMOF\_INTERFACES\_MAX 16U

109

[ 116](group__usbd__api.md#ga95fb708d8a54eaa3ce0acc4e65519bbc)enum [usbd\_ch9\_state](group__usbd__api.md#ga95fb708d8a54eaa3ce0acc4e65519bbc) {

[ 117](group__usbd__api.md#gga95fb708d8a54eaa3ce0acc4e65519bbca978c707d313eb49b70bc62dfae304048) [USBD\_STATE\_DEFAULT](group__usbd__api.md#gga95fb708d8a54eaa3ce0acc4e65519bbca978c707d313eb49b70bc62dfae304048) = 0,

[ 118](group__usbd__api.md#gga95fb708d8a54eaa3ce0acc4e65519bbca985f06c5505c5684a98954f15701cc9d) [USBD\_STATE\_ADDRESS](group__usbd__api.md#gga95fb708d8a54eaa3ce0acc4e65519bbca985f06c5505c5684a98954f15701cc9d),

[ 119](group__usbd__api.md#gga95fb708d8a54eaa3ce0acc4e65519bbca44c1920b09ea1062ea4d7ac31a846509) [USBD\_STATE\_CONFIGURED](group__usbd__api.md#gga95fb708d8a54eaa3ce0acc4e65519bbca44c1920b09ea1062ea4d7ac31a846509),

120};

121

122

[ 126](structusbd__ch9__data.md)struct [usbd\_ch9\_data](structusbd__ch9__data.md) {

[ 128](structusbd__ch9__data.md#a85f96c69cede5b51c1f9739a4ae67f4d) struct [usb\_setup\_packet](structusb__setup__packet.md) [setup](structusbd__ch9__data.md#a85f96c69cede5b51c1f9739a4ae67f4d);

[ 130](structusbd__ch9__data.md#a095a2a98f19ea40e8bd1bf65eed77dac) int [ctrl\_type](structusbd__ch9__data.md#a095a2a98f19ea40e8bd1bf65eed77dac);

[ 132](structusbd__ch9__data.md#a70d1a1be0aab6167ca4f4580b9c65eff) enum [usbd\_ch9\_state](group__usbd__api.md#ga95fb708d8a54eaa3ce0acc4e65519bbc) [state](structusbd__ch9__data.md#a70d1a1be0aab6167ca4f4580b9c65eff);

[ 134](structusbd__ch9__data.md#a504360b7cb11240a2fda68344f2e3b62) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ep\_halt](structusbd__ch9__data.md#a504360b7cb11240a2fda68344f2e3b62);

[ 136](structusbd__ch9__data.md#a1f759fb0d758e50c4589b6b6b1fd2a24) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [configuration](structusbd__ch9__data.md#a1f759fb0d758e50c4589b6b6b1fd2a24);

[ 138](structusbd__ch9__data.md#a6ab6f611fd1eff8d6fde0617c587fefb) bool [post\_status](structusbd__ch9__data.md#a6ab6f611fd1eff8d6fde0617c587fefb);

[ 140](structusbd__ch9__data.md#a8f831eca1974b8411072f8102c444d45) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [alternate](structusbd__ch9__data.md#a8f831eca1974b8411072f8102c444d45)[[USBD\_NUMOF\_INTERFACES\_MAX](group__usbd__api.md#gaf8aadd499f7e0438acac4a7f36645d49)];

141};

142

[ 146](structusbd__status.md)struct [usbd\_status](structusbd__status.md) {

[ 148](structusbd__status.md#a78de12245d08ecc71e09d5519fe0e857) unsigned int [initialized](structusbd__status.md#a78de12245d08ecc71e09d5519fe0e857) : 1;

[ 150](structusbd__status.md#a2382fcb655fe51e0bcf83f85aa182ba3) unsigned int [enabled](structusbd__status.md#a2382fcb655fe51e0bcf83f85aa182ba3) : 1;

[ 152](structusbd__status.md#afb67cfda187e40229f842c93aa09f0ba) unsigned int [suspended](structusbd__status.md#afb67cfda187e40229f842c93aa09f0ba) : 1;

[ 154](structusbd__status.md#a113085892967cf7c9cb70131b320d61a) unsigned int [rwup](structusbd__status.md#a113085892967cf7c9cb70131b320d61a) : 1;

155};

156

[ 163](structusbd__contex.md)struct [usbd\_contex](structusbd__contex.md) {

[ 165](structusbd__contex.md#abba6950f90e08a227c5a124ba1cac794) const char \*[name](structusbd__contex.md#abba6950f90e08a227c5a124ba1cac794);

[ 167](structusbd__contex.md#ac833ce3afb9a9d86c90f35bc33ef617f) struct [k\_mutex](structk__mutex.md) [mutex](structusbd__contex.md#ac833ce3afb9a9d86c90f35bc33ef617f);

[ 169](structusbd__contex.md#abe1919c4098622f9a87f4b2d4caf1c3b) const struct [device](structdevice.md) \*[dev](structusbd__contex.md#abe1919c4098622f9a87f4b2d4caf1c3b);

[ 171](structusbd__contex.md#a7f0d2d526faa553e3f520a58639d271a) struct [usbd\_ch9\_data](structusbd__ch9__data.md) [ch9\_data](structusbd__contex.md#a7f0d2d526faa553e3f520a58639d271a);

[ 173](structusbd__contex.md#a4634c51ab958993e0d2c2cbb192cc105) [sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) [descriptors](structusbd__contex.md#a4634c51ab958993e0d2c2cbb192cc105);

[ 175](structusbd__contex.md#abc0473af6584cd4d4040af7d5f1b522b) [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) [configs](structusbd__contex.md#abc0473af6584cd4d4040af7d5f1b522b);

[ 177](structusbd__contex.md#ae190c2f4e20e91e9ad75ff81012b47c2) struct [usbd\_status](structusbd__status.md) [status](structusbd__contex.md#ae190c2f4e20e91e9ad75ff81012b47c2);

[ 179](structusbd__contex.md#ad2984b7bd687e2c753c1c7497044e9d0) void \*[desc](structusbd__contex.md#ad2984b7bd687e2c753c1c7497044e9d0);

180};

181

[ 185](structusbd__cctx__vendor__req.md)struct [usbd\_cctx\_vendor\_req](structusbd__cctx__vendor__req.md) {

[ 187](structusbd__cctx__vendor__req.md#a2ddf3ce0c1c0a6d788b7ef30cf8d67ea) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[reqs](structusbd__cctx__vendor__req.md#a2ddf3ce0c1c0a6d788b7ef30cf8d67ea);

[ 189](structusbd__cctx__vendor__req.md#a3b5e99bff9dbfa023a4e6a5b4a69abd0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structusbd__cctx__vendor__req.md#a3b5e99bff9dbfa023a4e6a5b4a69abd0);

190};

191

[ 193](group__usbd__api.md#ga588b9e156a49d3b0358bee185cdeebee)#define USBD\_CCTX\_REGISTERED 0

194

195struct [usbd\_class\_node](structusbd__class__node.md);

196

[ 200](structusbd__class__api.md)struct [usbd\_class\_api](structusbd__class__api.md) {

[ 202](structusbd__class__api.md#a90d7370d6d58467b8516dc23fa85da6e) void (\*[feature\_halt](structusbd__class__api.md#a90d7370d6d58467b8516dc23fa85da6e))(struct [usbd\_class\_node](structusbd__class__node.md) \*const node,

203 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, bool halted);

204

[ 206](structusbd__class__api.md#adaa09908b17f85e97f39266f79cb32a8) void (\*[update](structusbd__class__api.md#adaa09908b17f85e97f39266f79cb32a8))(struct [usbd\_class\_node](structusbd__class__node.md) \*const node,

207 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) iface, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) alternate);

208

[ 210](structusbd__class__api.md#a5c7fa1a0d05a8eab486e1ee61cc0b73f) int (\*[control\_to\_dev](structusbd__class__api.md#a5c7fa1a0d05a8eab486e1ee61cc0b73f))(struct [usbd\_class\_node](structusbd__class__node.md) \*const node,

211 const struct [usb\_setup\_packet](structusb__setup__packet.md) \*const setup,

212 const struct [net\_buf](structnet__buf.md) \*const buf);

213

[ 215](structusbd__class__api.md#a5eac92c9ab6ebb6eb61c683f0b289e21) int (\*[control\_to\_host](structusbd__class__api.md#a5eac92c9ab6ebb6eb61c683f0b289e21))(struct [usbd\_class\_node](structusbd__class__node.md) \*const node,

216 const struct [usb\_setup\_packet](structusb__setup__packet.md) \*const setup,

217 struct [net\_buf](structnet__buf.md) \*const buf);

218

[ 220](structusbd__class__api.md#aff8426da1f7dd1f5fa5d27ce135bf0f8) int (\*[request](structusbd__class__api.md#aff8426da1f7dd1f5fa5d27ce135bf0f8))(struct [usbd\_class\_node](structusbd__class__node.md) \*const node,

221 struct [net\_buf](structnet__buf.md) \*buf, int err);

222

[ 224](structusbd__class__api.md#a36bf045b23c0fda4865db2978c94b6d1) void (\*[suspended](structusbd__class__api.md#a36bf045b23c0fda4865db2978c94b6d1))(struct [usbd\_class\_node](structusbd__class__node.md) \*const node);

225

[ 227](structusbd__class__api.md#a26411223bbe266a1cb7015a7ccb5c100) void (\*[resumed](structusbd__class__api.md#a26411223bbe266a1cb7015a7ccb5c100))(struct [usbd\_class\_node](structusbd__class__node.md) \*const node);

228

[ 230](structusbd__class__api.md#a9dd501ae803c5f0e8b4d62f4a57b04ca) void (\*[sof](structusbd__class__api.md#a9dd501ae803c5f0e8b4d62f4a57b04ca))(struct [usbd\_class\_node](structusbd__class__node.md) \*const node);

231

[ 233](structusbd__class__api.md#a03585c10422b27cf7712cc88e99a5fc2) void (\*[enable](structusbd__class__api.md#a03585c10422b27cf7712cc88e99a5fc2))(struct [usbd\_class\_node](structusbd__class__node.md) \*const node);

234

[ 236](structusbd__class__api.md#a3e9c54c768d12341d242cdecd83e96bd) void (\*[disable](structusbd__class__api.md#a3e9c54c768d12341d242cdecd83e96bd))(struct [usbd\_class\_node](structusbd__class__node.md) \*const node);

237

[ 239](structusbd__class__api.md#a20ec6b44ddded48eadffc9a82115766e) int (\*[init](structusbd__class__api.md#a20ec6b44ddded48eadffc9a82115766e))(struct [usbd\_class\_node](structusbd__class__node.md) \*const node);

240

[ 242](structusbd__class__api.md#a11e02db41023c9a4d8e853d1eaddac00) void (\*[shutdown](structusbd__class__api.md#a11e02db41023c9a4d8e853d1eaddac00))(struct [usbd\_class\_node](structusbd__class__node.md) \*const node);

243};

244

[ 248](structusbd__class__data.md)struct [usbd\_class\_data](structusbd__class__data.md) {

[ 250](structusbd__class__data.md#af2560e7d2e9f4fcc70be0a13883594b1) struct [usbd\_contex](structusbd__contex.md) \*[uds\_ctx](structusbd__class__data.md#af2560e7d2e9f4fcc70be0a13883594b1);

[ 254](structusbd__class__data.md#a5b63cc431c007291bf96196b0eefd6c2) void \*[desc](structusbd__class__data.md#a5b63cc431c007291bf96196b0eefd6c2);

[ 256](structusbd__class__data.md#a32db83ecf80e1ac9e4d5deda54581deb) const struct [usbd\_cctx\_vendor\_req](structusbd__cctx__vendor__req.md) \*[v\_reqs](structusbd__class__data.md#a32db83ecf80e1ac9e4d5deda54581deb);

[ 260](structusbd__class__data.md#ab60dc9c68368c5c918ea6d23eacfaf60) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ep\_assigned](structusbd__class__data.md#ab60dc9c68368c5c918ea6d23eacfaf60);

[ 264](structusbd__class__data.md#aad3c8f52393d6135532d25ee8f42950e) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ep\_active](structusbd__class__data.md#aad3c8f52393d6135532d25ee8f42950e);

[ 266](structusbd__class__data.md#ab41348dd230fa882efb8d39260447cb4) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [iface\_bm](structusbd__class__data.md#ab41348dd230fa882efb8d39260447cb4);

[ 268](structusbd__class__data.md#a57718d5c32580352ad7bd49000d01d3b) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [state](structusbd__class__data.md#a57718d5c32580352ad7bd49000d01d3b);

[ 270](structusbd__class__data.md#a10bb5b9af6098fbbc86fd00ef54e84e1) void \*[priv](structusbd__class__data.md#a10bb5b9af6098fbbc86fd00ef54e84e1);

271};

272

[ 273](structusbd__class__node.md)struct [usbd\_class\_node](structusbd__class__node.md) {

[ 275](structusbd__class__node.md#a1bdbe525e21ac5ea6eff30f6159a4406) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structusbd__class__node.md#a1bdbe525e21ac5ea6eff30f6159a4406);

[ 277](structusbd__class__node.md#a06682f9e64f391985b08c5d884903992) const char \*[name](structusbd__class__node.md#a06682f9e64f391985b08c5d884903992);

[ 279](structusbd__class__node.md#a276df79bf269b19875f1c497a36392fb) const struct [usbd\_class\_api](structusbd__class__api.md) \*[api](structusbd__class__node.md#a276df79bf269b19875f1c497a36392fb);

[ 281](structusbd__class__node.md#a53916906d5efce1eeb4024a7b3662553) struct [usbd\_class\_data](structusbd__class__data.md) \*[data](structusbd__class__node.md#a53916906d5efce1eeb4024a7b3662553);

282};

283

[ 284](group__usbd__api.md#gaa202fc8ae1e5585abedbde733e63ccb7)#define USBD\_DEVICE\_DEFINE(device\_name, uhc\_dev, vid, pid) \

285 static struct usb\_device\_descriptor \

286 desc\_##device\_name = { \

287 .bLength = sizeof(struct usb\_device\_descriptor), \

288 .bDescriptorType = USB\_DESC\_DEVICE, \

289 .bcdUSB = sys\_cpu\_to\_le16(USB\_SRN\_2\_0), \

290 .bDeviceClass = USB\_BCC\_MISCELLANEOUS, \

291 .bDeviceSubClass = 2, \

292 .bDeviceProtocol = 1, \

293 .bMaxPacketSize0 = USB\_CONTROL\_EP\_MPS, \

294 .idVendor = vid, \

295 .idProduct = pid, \

296 .bcdDevice = sys\_cpu\_to\_le16(USB\_BCD\_DRN), \

297 .iManufacturer = 0, \

298 .iProduct = 0, \

299 .iSerialNumber = 0, \

300 .bNumConfigurations = 0, \

301 }; \

302 static STRUCT\_SECTION\_ITERABLE(usbd\_contex, device\_name) = { \

303 .name = STRINGIFY(device\_name), \

304 .dev = uhc\_dev, \

305 .desc = &desc\_##device\_name, \

306 }

307

[ 308](group__usbd__api.md#ga5db99c7ff31ff9ef893f219d209128c7)#define USBD\_CONFIGURATION\_DEFINE(name, attrib, power) \

309 static struct usb\_cfg\_descriptor \

310 cfg\_desc\_##name = { \

311 .bLength = sizeof(struct usb\_cfg\_descriptor), \

312 .bDescriptorType = USB\_DESC\_CONFIGURATION, \

313 .wTotalLength = 0, \

314 .bNumInterfaces = 0, \

315 .bConfigurationValue = 1, \

316 .iConfiguration = 0, \

317 .bmAttributes = USB\_SCD\_RESERVED | (attrib), \

318 .bMaxPower = (power), \

319 }; \

320 BUILD\_ASSERT((power) < 256, "Too much power"); \

321 static struct usbd\_config\_node name = { \

322 .desc = &cfg\_desc\_##name, \

323 }

324

[ 338](group__usbd__api.md#gaec816a27118bcb289ab4840fcd22888e)#define USBD\_DESC\_LANG\_DEFINE(name) \

339 static struct usb\_string\_descriptor \

340 string\_desc\_##name = { \

341 .bLength = sizeof(struct usb\_string\_descriptor), \

342 .bDescriptorType = USB\_DESC\_STRING, \

343 .bString = sys\_cpu\_to\_le16(0x0409), \

344 }; \

345 static struct usbd\_desc\_node name = { \

346 .idx = 0, \

347 .utype = USBD\_DUT\_STRING\_LANG, \

348 .desc = &string\_desc\_##name, \

349 }

350

[ 351](group__usbd__api.md#gaf800e2040ac30844cab463c13d1fcdf8)#define USBD\_DESC\_STRING\_DEFINE(d\_name, d\_string, d\_utype) \

352 struct usb\_string\_descriptor\_##d\_name { \

353 uint8\_t bLength; \

354 uint8\_t bDescriptorType; \

355 uint8\_t bString[USB\_BSTRING\_LENGTH(d\_string)]; \

356 } \_\_packed; \

357 static struct usb\_string\_descriptor\_##d\_name \

358 string\_desc\_##d\_name = { \

359 .bLength = USB\_STRING\_DESCRIPTOR\_LENGTH(d\_string), \

360 .bDescriptorType = USB\_DESC\_STRING, \

361 .bString = d\_string, \

362 }; \

363 static struct usbd\_desc\_node d\_name = { \

364 .utype = d\_utype, \

365 .desc = &string\_desc\_##d\_name, \

366 }

367

[ 379](group__usbd__api.md#ga18b1321daf1173a3cb0bc61a0d9beb34)#define USBD\_DESC\_MANUFACTURER\_DEFINE(d\_name, d\_string) \

380 USBD\_DESC\_STRING\_DEFINE(d\_name, d\_string, USBD\_DUT\_STRING\_MANUFACTURER)

381

[ 393](group__usbd__api.md#gaa5e43f9eac8f91d3896ea5e19baed031)#define USBD\_DESC\_PRODUCT\_DEFINE(d\_name, d\_string) \

394 USBD\_DESC\_STRING\_DEFINE(d\_name, d\_string, USBD\_DUT\_STRING\_PRODUCT)

395

[ 408](group__usbd__api.md#ga98e3b788b4bc38d0ac199a67fdc302d0)#define USBD\_DESC\_SERIAL\_NUMBER\_DEFINE(d\_name, d\_string) \

409 USBD\_DESC\_STRING\_DEFINE(d\_name, d\_string, USBD\_DUT\_STRING\_SERIAL\_NUMBER)

410

[ 411](group__usbd__api.md#gaab136394168b115c0e061261651c4146)#define USBD\_DEFINE\_CLASS(class\_name, class\_api, class\_data) \

412 static STRUCT\_SECTION\_ITERABLE(usbd\_class\_node, class\_name) = { \

413 .name = STRINGIFY(class\_name), \

414 .api = class\_api, \

415 .data = class\_data, \

416 }

417

[ 423](group__usbd__api.md#ga54ca08c74ae715281381d878f828727e)#define VENDOR\_REQ\_DEFINE(\_reqs, \_len) \

424 { \

425 .reqs = (const uint8\_t \*)(\_reqs), \

426 .len = (\_len), \

427 }

428

[ 433](group__usbd__api.md#ga464933a8332c11d15c92914aa1790e10)#define USBD\_VENDOR\_REQ(\_reqs...) \

434 VENDOR\_REQ\_DEFINE(((uint8\_t []) { \_reqs }), \

435 sizeof((uint8\_t []) { \_reqs }))

436

437

[ 448](group__usbd__api.md#ga0280dbaf6f15e4bc789279b8d93bfff8)int [usbd\_add\_descriptor](group__usbd__api.md#ga0280dbaf6f15e4bc789279b8d93bfff8)(struct [usbd\_contex](structusbd__contex.md) \*[uds\_ctx](structusbd__class__data.md#af2560e7d2e9f4fcc70be0a13883594b1),

449 struct [usbd\_desc\_node](structusbd__desc__node.md) \*dn);

450

[ 459](group__usbd__api.md#gae1472960a22e84a49865639dff5816a0)int [usbd\_add\_configuration](group__usbd__api.md#gae1472960a22e84a49865639dff5816a0)(struct [usbd\_contex](structusbd__contex.md) \*[uds\_ctx](structusbd__class__data.md#af2560e7d2e9f4fcc70be0a13883594b1),

460 struct [usbd\_config\_node](structusbd__config__node.md) \*cd);

461

[ 482](group__usbd__api.md#ga3640cb8425961a8038c225e1daea34a3)int [usbd\_register\_class](group__usbd__api.md#ga3640cb8425961a8038c225e1daea34a3)(struct [usbd\_contex](structusbd__contex.md) \*[uds\_ctx](structusbd__class__data.md#af2560e7d2e9f4fcc70be0a13883594b1),

483 const char \*name,

484 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cfg);

485

[ 499](group__usbd__api.md#gadf7cc0edc2d046f0b50e65fcc007f982)int [usbd\_unregister\_class](group__usbd__api.md#gadf7cc0edc2d046f0b50e65fcc007f982)(struct [usbd\_contex](structusbd__contex.md) \*[uds\_ctx](structusbd__class__data.md#af2560e7d2e9f4fcc70be0a13883594b1),

500 const char \*name,

501 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cfg);

502

[ 516](group__usbd__api.md#gaf3cd6c12317f9d94ee98f2809d2a0e04)int [usbd\_init](group__usbd__api.md#gaf3cd6c12317f9d94ee98f2809d2a0e04)(struct [usbd\_contex](structusbd__contex.md) \*[uds\_ctx](structusbd__class__data.md#af2560e7d2e9f4fcc70be0a13883594b1));

517

[ 527](group__usbd__api.md#gaa7ee71917824e90177f61a86eb992817)int [usbd\_enable](group__usbd__api.md#gaa7ee71917824e90177f61a86eb992817)(struct [usbd\_contex](structusbd__contex.md) \*[uds\_ctx](structusbd__class__data.md#af2560e7d2e9f4fcc70be0a13883594b1));

528

[ 538](group__usbd__api.md#gaa3112af9fb2f5f1ee55cc71a64c6e369)int [usbd\_disable](group__usbd__api.md#gaa3112af9fb2f5f1ee55cc71a64c6e369)(struct [usbd\_contex](structusbd__contex.md) \*[uds\_ctx](structusbd__class__data.md#af2560e7d2e9f4fcc70be0a13883594b1));

539

[ 549](group__usbd__api.md#gaa7656f656182e727531e531344c960df)int [usbd\_shutdown](group__usbd__api.md#gaa7656f656182e727531e531344c960df)(struct [usbd\_contex](structusbd__contex.md) \*const [uds\_ctx](structusbd__class__data.md#af2560e7d2e9f4fcc70be0a13883594b1));

550

[ 559](group__usbd__api.md#ga0730043c2fd89b56db6e7457b639968d)int [usbd\_ep\_set\_halt](group__usbd__api.md#ga0730043c2fd89b56db6e7457b639968d)(struct [usbd\_contex](structusbd__contex.md) \*[uds\_ctx](structusbd__class__data.md#af2560e7d2e9f4fcc70be0a13883594b1), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep);

560

[ 569](group__usbd__api.md#ga197697880c7c625ea212893b2fe7ef8b)int [usbd\_ep\_clear\_halt](group__usbd__api.md#ga197697880c7c625ea212893b2fe7ef8b)(struct [usbd\_contex](structusbd__contex.md) \*[uds\_ctx](structusbd__class__data.md#af2560e7d2e9f4fcc70be0a13883594b1), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep);

570

[ 579](group__usbd__api.md#ga9292b393ef17fd61ea42b2f28fdd57ee)bool [usbd\_ep\_is\_halted](group__usbd__api.md#ga9292b393ef17fd61ea42b2f28fdd57ee)(struct [usbd\_contex](structusbd__contex.md) \*[uds\_ctx](structusbd__class__data.md#af2560e7d2e9f4fcc70be0a13883594b1), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep);

580

[ 592](group__usbd__api.md#ga59b0cb83b05e0a44db9c6a36171d524f)struct [net\_buf](structnet__buf.md) \*[usbd\_ep\_ctrl\_buf\_alloc](group__usbd__api.md#ga59b0cb83b05e0a44db9c6a36171d524f)(struct [usbd\_contex](structusbd__contex.md) \*const uds\_ctx,

593 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, const size\_t [size](structnet__buf.md#a1522d81a002804223e25300a6961f527));

594

[ 606](group__usbd__api.md#ga940f38e4db1dfc7ba6514ecf95dc9e5b)struct [net\_buf](structnet__buf.md) \*[usbd\_ep\_buf\_alloc](group__usbd__api.md#ga940f38e4db1dfc7ba6514ecf95dc9e5b)(const struct [usbd\_class\_node](structusbd__class__node.md) \*const c\_nd,

607 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, const size\_t [size](structnet__buf.md#a1522d81a002804223e25300a6961f527));

608

[ 619](group__usbd__api.md#ga52acb4fb74e3737b446b6704c6925d70)int [usbd\_ep\_ctrl\_enqueue](group__usbd__api.md#ga52acb4fb74e3737b446b6704c6925d70)(struct [usbd\_contex](structusbd__contex.md) \*const uds\_ctx,

620 struct [net\_buf](structnet__buf.md) \*const buf);

621

[ 632](group__usbd__api.md#ga19ecdc00918dbec14fdbcf847b6f4dce)int [usbd\_ep\_enqueue](group__usbd__api.md#ga19ecdc00918dbec14fdbcf847b6f4dce)(const struct [usbd\_class\_node](structusbd__class__node.md) \*const c\_nd,

633 struct [net\_buf](structnet__buf.md) \*const buf);

634

[ 643](group__usbd__api.md#ga0d1d7f59822674c201147b50a1dbdb96)int [usbd\_ep\_dequeue](group__usbd__api.md#ga0d1d7f59822674c201147b50a1dbdb96)(struct [usbd\_contex](structusbd__contex.md) \*uds\_ctx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep);

644

[ 655](group__usbd__api.md#ga2bfd230a2e0b74954ebce112816e6193)int [usbd\_ep\_buf\_free](group__usbd__api.md#ga2bfd230a2e0b74954ebce112816e6193)(struct [usbd\_contex](structusbd__contex.md) \*uds\_ctx, struct [net\_buf](structnet__buf.md) \*buf);

656

[ 664](group__usbd__api.md#ga832e3147aba9297bad263b2a3817e1e4)bool [usbd\_is\_suspended](group__usbd__api.md#ga832e3147aba9297bad263b2a3817e1e4)(struct [usbd\_contex](structusbd__contex.md) \*uds\_ctx);

665

[ 671](group__usbd__api.md#ga4d440313da931d4504919b8fe2783419)int [usbd\_wakeup\_request](group__usbd__api.md#ga4d440313da931d4504919b8fe2783419)(struct [usbd\_contex](structusbd__contex.md) \*uds\_ctx);

672

[ 681](group__usbd__api.md#gaa191663f3703bd631e51009adbc22d87)int [usbd\_device\_set\_bcd](group__usbd__api.md#gaa191663f3703bd631e51009adbc22d87)(struct [usbd\_contex](structusbd__contex.md) \*const uds\_ctx,

682 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bcd);

683

[ 692](group__usbd__api.md#ga791a561a3d96698a1a7337723adc8e53)int [usbd\_device\_set\_vid](group__usbd__api.md#ga791a561a3d96698a1a7337723adc8e53)(struct [usbd\_contex](structusbd__contex.md) \*const uds\_ctx,

693 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vid);

694

[ 703](group__usbd__api.md#gad3612c1c4276783df11b144e72662306)int [usbd\_device\_set\_pid](group__usbd__api.md#gad3612c1c4276783df11b144e72662306)(struct [usbd\_contex](structusbd__contex.md) \*const uds\_ctx,

704 const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) pid);

705

[ 716](group__usbd__api.md#gad8d784ae06463afe51f312dad8a4718d)int [usbd\_device\_set\_code\_triple](group__usbd__api.md#gad8d784ae06463afe51f312dad8a4718d)(struct [usbd\_contex](structusbd__contex.md) \*const uds\_ctx,

717 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) base\_class,

718 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) subclass, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) protocol);

719

[ 729](group__usbd__api.md#ga6488af53f4ed5355406ef319a8d1b195)int [usbd\_config\_attrib\_rwup](group__usbd__api.md#ga6488af53f4ed5355406ef319a8d1b195)(struct [usbd\_contex](structusbd__contex.md) \*const uds\_ctx,

730 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cfg, const bool enable);

731

[ 741](group__usbd__api.md#ga7c8dd76553545c77ff6e0f4c41d33357)int [usbd\_config\_attrib\_self](group__usbd__api.md#ga7c8dd76553545c77ff6e0f4c41d33357)(struct [usbd\_contex](structusbd__contex.md) \*const uds\_ctx,

742 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cfg, const bool enable);

743

[ 753](group__usbd__api.md#gac907ba549e8d799a328cc992d76e3825)int [usbd\_config\_maxpower](group__usbd__api.md#gac907ba549e8d799a328cc992d76e3825)(struct [usbd\_contex](structusbd__contex.md) \*const uds\_ctx,

754 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cfg, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) power);

758

759#ifdef \_\_cplusplus

760}

761#endif

762

763#endif /\* ZEPHYR\_INCLUDE\_USBD\_H\_ \*/

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[device.h](device_8h.md)

[sys\_dnode\_t](group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98)

struct \_dnode sys\_dnode\_t

Doubly-linked list node structure.

**Definition** dlist.h:55

[sys\_dlist\_t](group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683)

struct \_dnode sys\_dlist\_t

Doubly-linked list structure.

**Definition** dlist.h:51

[sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8)

struct \_slist sys\_slist\_t

Single-linked list structure.

**Definition** slist.h:49

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[usbd\_add\_descriptor](group__usbd__api.md#ga0280dbaf6f15e4bc789279b8d93bfff8)

int usbd\_add\_descriptor(struct usbd\_contex \*uds\_ctx, struct usbd\_desc\_node \*dn)

Add common USB descriptor.

[usbd\_ep\_set\_halt](group__usbd__api.md#ga0730043c2fd89b56db6e7457b639968d)

int usbd\_ep\_set\_halt(struct usbd\_contex \*uds\_ctx, uint8\_t ep)

Halt endpoint.

[usbd\_ep\_dequeue](group__usbd__api.md#ga0d1d7f59822674c201147b50a1dbdb96)

int usbd\_ep\_dequeue(struct usbd\_contex \*uds\_ctx, const uint8\_t ep)

Remove all USB device controller requests from endpoint queue.

[usbd\_ep\_clear\_halt](group__usbd__api.md#ga197697880c7c625ea212893b2fe7ef8b)

int usbd\_ep\_clear\_halt(struct usbd\_contex \*uds\_ctx, uint8\_t ep)

Clear endpoint halt.

[usbd\_ep\_enqueue](group__usbd__api.md#ga19ecdc00918dbec14fdbcf847b6f4dce)

int usbd\_ep\_enqueue(const struct usbd\_class\_node \*const c\_nd, struct net\_buf \*const buf)

Queue USB device request.

[usbd\_ep\_buf\_free](group__usbd__api.md#ga2bfd230a2e0b74954ebce112816e6193)

int usbd\_ep\_buf\_free(struct usbd\_contex \*uds\_ctx, struct net\_buf \*buf)

Free USB device request buffer.

[usbd\_register\_class](group__usbd__api.md#ga3640cb8425961a8038c225e1daea34a3)

int usbd\_register\_class(struct usbd\_contex \*uds\_ctx, const char \*name, uint8\_t cfg)

Register an USB class instance.

[usbd\_wakeup\_request](group__usbd__api.md#ga4d440313da931d4504919b8fe2783419)

int usbd\_wakeup\_request(struct usbd\_contex \*uds\_ctx)

Initiate the USB remote wakeup (TBD).

[usbd\_ep\_ctrl\_enqueue](group__usbd__api.md#ga52acb4fb74e3737b446b6704c6925d70)

int usbd\_ep\_ctrl\_enqueue(struct usbd\_contex \*const uds\_ctx, struct net\_buf \*const buf)

Queue USB device control request.

[usbd\_ep\_ctrl\_buf\_alloc](group__usbd__api.md#ga59b0cb83b05e0a44db9c6a36171d524f)

struct net\_buf \* usbd\_ep\_ctrl\_buf\_alloc(struct usbd\_contex \*const uds\_ctx, const uint8\_t ep, const size\_t size)

Allocate buffer for USB device control request.

[usbd\_config\_attrib\_rwup](group__usbd__api.md#ga6488af53f4ed5355406ef319a8d1b195)

int usbd\_config\_attrib\_rwup(struct usbd\_contex \*const uds\_ctx, const uint8\_t cfg, const bool enable)

Setup USB device configuration attribute Remote Wakeup.

[usbd\_device\_set\_vid](group__usbd__api.md#ga791a561a3d96698a1a7337723adc8e53)

int usbd\_device\_set\_vid(struct usbd\_contex \*const uds\_ctx, const uint16\_t vid)

Set USB device descriptor value idVendor.

[usbd\_config\_attrib\_self](group__usbd__api.md#ga7c8dd76553545c77ff6e0f4c41d33357)

int usbd\_config\_attrib\_self(struct usbd\_contex \*const uds\_ctx, const uint8\_t cfg, const bool enable)

Setup USB device configuration attribute Self-powered.

[usbd\_is\_suspended](group__usbd__api.md#ga832e3147aba9297bad263b2a3817e1e4)

bool usbd\_is\_suspended(struct usbd\_contex \*uds\_ctx)

Checks whether the USB device controller is suspended.

[usbd\_ep\_is\_halted](group__usbd__api.md#ga9292b393ef17fd61ea42b2f28fdd57ee)

bool usbd\_ep\_is\_halted(struct usbd\_contex \*uds\_ctx, uint8\_t ep)

Checks whether the endpoint is halted.

[usbd\_ep\_buf\_alloc](group__usbd__api.md#ga940f38e4db1dfc7ba6514ecf95dc9e5b)

struct net\_buf \* usbd\_ep\_buf\_alloc(const struct usbd\_class\_node \*const c\_nd, const uint8\_t ep, const size\_t size)

Allocate buffer for USB device request.

[usbd\_ch9\_state](group__usbd__api.md#ga95fb708d8a54eaa3ce0acc4e65519bbc)

usbd\_ch9\_state

USB device support middle layer runtime state.

**Definition** usbd.h:116

[usbd\_device\_set\_bcd](group__usbd__api.md#gaa191663f3703bd631e51009adbc22d87)

int usbd\_device\_set\_bcd(struct usbd\_contex \*const uds\_ctx, const uint16\_t bcd)

Set USB device descriptor value bcdUSB.

[usbd\_disable](group__usbd__api.md#gaa3112af9fb2f5f1ee55cc71a64c6e369)

int usbd\_disable(struct usbd\_contex \*uds\_ctx)

Disable the USB device support.

[usbd\_shutdown](group__usbd__api.md#gaa7656f656182e727531e531344c960df)

int usbd\_shutdown(struct usbd\_contex \*const uds\_ctx)

Shutdown the USB device support.

[usbd\_desc\_usage\_type](group__usbd__api.md#gaa7ed6f04fd7058c422f5ebc378f1a3da)

usbd\_desc\_usage\_type

**Definition** usbd.h:61

[usbd\_enable](group__usbd__api.md#gaa7ee71917824e90177f61a86eb992817)

int usbd\_enable(struct usbd\_contex \*uds\_ctx)

Enable the USB device support and registered class instances.

[usbd\_config\_maxpower](group__usbd__api.md#gac907ba549e8d799a328cc992d76e3825)

int usbd\_config\_maxpower(struct usbd\_contex \*const uds\_ctx, const uint8\_t cfg, const uint8\_t power)

Setup USB device configuration power consumption.

[usbd\_device\_set\_pid](group__usbd__api.md#gad3612c1c4276783df11b144e72662306)

int usbd\_device\_set\_pid(struct usbd\_contex \*const uds\_ctx, const uint16\_t pid)

Set USB device descriptor value idProduct.

[usbd\_device\_set\_code\_triple](group__usbd__api.md#gad8d784ae06463afe51f312dad8a4718d)

int usbd\_device\_set\_code\_triple(struct usbd\_contex \*const uds\_ctx, const uint8\_t base\_class, const uint8\_t subclass, const uint8\_t protocol)

Set USB device descriptor code triple Base Class, SubClass, and Protocol.

[usbd\_unregister\_class](group__usbd__api.md#gadf7cc0edc2d046f0b50e65fcc007f982)

int usbd\_unregister\_class(struct usbd\_contex \*uds\_ctx, const char \*name, uint8\_t cfg)

Unregister an USB class instance.

[usbd\_add\_configuration](group__usbd__api.md#gae1472960a22e84a49865639dff5816a0)

int usbd\_add\_configuration(struct usbd\_contex \*uds\_ctx, struct usbd\_config\_node \*cd)

Add a USB device configuration.

[usbd\_init](group__usbd__api.md#gaf3cd6c12317f9d94ee98f2809d2a0e04)

int usbd\_init(struct usbd\_contex \*uds\_ctx)

Initialize USB device.

[USBD\_NUMOF\_INTERFACES\_MAX](group__usbd__api.md#gaf8aadd499f7e0438acac4a7f36645d49)

#define USBD\_NUMOF\_INTERFACES\_MAX

**Definition** usbd.h:108

[USBD\_STATE\_CONFIGURED](group__usbd__api.md#gga95fb708d8a54eaa3ce0acc4e65519bbca44c1920b09ea1062ea4d7ac31a846509)

@ USBD\_STATE\_CONFIGURED

**Definition** usbd.h:119

[USBD\_STATE\_DEFAULT](group__usbd__api.md#gga95fb708d8a54eaa3ce0acc4e65519bbca978c707d313eb49b70bc62dfae304048)

@ USBD\_STATE\_DEFAULT

**Definition** usbd.h:117

[USBD\_STATE\_ADDRESS](group__usbd__api.md#gga95fb708d8a54eaa3ce0acc4e65519bbca985f06c5505c5684a98954f15701cc9d)

@ USBD\_STATE\_ADDRESS

**Definition** usbd.h:118

[USBD\_DUT\_STRING\_MANUFACTURER](group__usbd__api.md#ggaa7ed6f04fd7058c422f5ebc378f1a3daa25eb10630b10db28f9f97aa0b81f3c4e)

@ USBD\_DUT\_STRING\_MANUFACTURER

**Definition** usbd.h:63

[USBD\_DUT\_STRING\_PRODUCT](group__usbd__api.md#ggaa7ed6f04fd7058c422f5ebc378f1a3daa67c8a16639167a0a7a6f615d5aa6b73e)

@ USBD\_DUT\_STRING\_PRODUCT

**Definition** usbd.h:64

[USBD\_DUT\_STRING\_LANG](group__usbd__api.md#ggaa7ed6f04fd7058c422f5ebc378f1a3daa984cc2f845e2e2bcc83d2e9f0138e3bd)

@ USBD\_DUT\_STRING\_LANG

**Definition** usbd.h:62

[USBD\_DUT\_STRING\_INTERFACE](group__usbd__api.md#ggaa7ed6f04fd7058c422f5ebc378f1a3daaa4dd69c222492b1f12b3993c4640c80d)

@ USBD\_DUT\_STRING\_INTERFACE

**Definition** usbd.h:66

[USBD\_DUT\_STRING\_SERIAL\_NUMBER](group__usbd__api.md#ggaa7ed6f04fd7058c422f5ebc378f1a3daac4fff2e4994a473899aea6ed8a0ec782)

@ USBD\_DUT\_STRING\_SERIAL\_NUMBER

**Definition** usbd.h:65

[log.h](log_8h.md)

[buf.h](net_2buf_8h.md)

Buffer management.

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

**Definition** device.h:387

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:2900

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** buf.h:910

[net\_buf::size](structnet__buf.md#a1522d81a002804223e25300a6961f527)

uint16\_t size

Amount of data that this buffer can store.

**Definition** buf.h:942

[usb\_setup\_packet](structusb__setup__packet.md)

USB Setup Data packet defined in spec.

**Definition** usb\_ch9.h:39

[usbd\_cctx\_vendor\_req](structusbd__cctx__vendor__req.md)

Vendor Requests Table.

**Definition** usbd.h:185

[usbd\_cctx\_vendor\_req::reqs](structusbd__cctx__vendor__req.md#a2ddf3ce0c1c0a6d788b7ef30cf8d67ea)

const uint8\_t \* reqs

Array of vendor requests supported by the class.

**Definition** usbd.h:187

[usbd\_cctx\_vendor\_req::len](structusbd__cctx__vendor__req.md#a3b5e99bff9dbfa023a4e6a5b4a69abd0)

uint8\_t len

Length of the array.

**Definition** usbd.h:189

[usbd\_ch9\_data](structusbd__ch9__data.md)

USB device support middle layer runtime data.

**Definition** usbd.h:126

[usbd\_ch9\_data::ctrl\_type](structusbd__ch9__data.md#a095a2a98f19ea40e8bd1bf65eed77dac)

int ctrl\_type

Control type, internally used for stage verification.

**Definition** usbd.h:130

[usbd\_ch9\_data::configuration](structusbd__ch9__data.md#a1f759fb0d758e50c4589b6b6b1fd2a24)

uint8\_t configuration

USB device stack selected configuration.

**Definition** usbd.h:136

[usbd\_ch9\_data::ep\_halt](structusbd__ch9__data.md#a504360b7cb11240a2fda68344f2e3b62)

uint32\_t ep\_halt

Halted endpoints bitmap.

**Definition** usbd.h:134

[usbd\_ch9\_data::post\_status](structusbd__ch9__data.md#a6ab6f611fd1eff8d6fde0617c587fefb)

bool post\_status

Post status stage work required, e.g.

**Definition** usbd.h:138

[usbd\_ch9\_data::state](structusbd__ch9__data.md#a70d1a1be0aab6167ca4f4580b9c65eff)

enum usbd\_ch9\_state state

Protocol state of the USB device stack.

**Definition** usbd.h:132

[usbd\_ch9\_data::setup](structusbd__ch9__data.md#a85f96c69cede5b51c1f9739a4ae67f4d)

struct usb\_setup\_packet setup

Setup packet, up-to-date for the respective control request.

**Definition** usbd.h:128

[usbd\_ch9\_data::alternate](structusbd__ch9__data.md#a8f831eca1974b8411072f8102c444d45)

uint8\_t alternate[16U]

Array to track interfaces alternate settings.

**Definition** usbd.h:140

[usbd\_class\_api](structusbd__class__api.md)

USB device support class instance API.

**Definition** usbd.h:200

[usbd\_class\_api::enable](structusbd__class__api.md#a03585c10422b27cf7712cc88e99a5fc2)

void(\* enable)(struct usbd\_class\_node \*const node)

Class associated configuration is selected.

**Definition** usbd.h:233

[usbd\_class\_api::shutdown](structusbd__class__api.md#a11e02db41023c9a4d8e853d1eaddac00)

void(\* shutdown)(struct usbd\_class\_node \*const node)

Shutdown of the class implementation.

**Definition** usbd.h:242

[usbd\_class\_api::init](structusbd__class__api.md#a20ec6b44ddded48eadffc9a82115766e)

int(\* init)(struct usbd\_class\_node \*const node)

Initialization of the class implementation.

**Definition** usbd.h:239

[usbd\_class\_api::resumed](structusbd__class__api.md#a26411223bbe266a1cb7015a7ccb5c100)

void(\* resumed)(struct usbd\_class\_node \*const node)

USB power management handler resumed.

**Definition** usbd.h:227

[usbd\_class\_api::suspended](structusbd__class__api.md#a36bf045b23c0fda4865db2978c94b6d1)

void(\* suspended)(struct usbd\_class\_node \*const node)

USB power management handler suspended.

**Definition** usbd.h:224

[usbd\_class\_api::disable](structusbd__class__api.md#a3e9c54c768d12341d242cdecd83e96bd)

void(\* disable)(struct usbd\_class\_node \*const node)

Class associated configuration is disabled.

**Definition** usbd.h:236

[usbd\_class\_api::control\_to\_dev](structusbd__class__api.md#a5c7fa1a0d05a8eab486e1ee61cc0b73f)

int(\* control\_to\_dev)(struct usbd\_class\_node \*const node, const struct usb\_setup\_packet \*const setup, const struct net\_buf \*const buf)

USB control request handler to device.

**Definition** usbd.h:210

[usbd\_class\_api::control\_to\_host](structusbd__class__api.md#a5eac92c9ab6ebb6eb61c683f0b289e21)

int(\* control\_to\_host)(struct usbd\_class\_node \*const node, const struct usb\_setup\_packet \*const setup, struct net\_buf \*const buf)

USB control request handler to host.

**Definition** usbd.h:215

[usbd\_class\_api::feature\_halt](structusbd__class__api.md#a90d7370d6d58467b8516dc23fa85da6e)

void(\* feature\_halt)(struct usbd\_class\_node \*const node, uint8\_t ep, bool halted)

Feature halt state update handler.

**Definition** usbd.h:202

[usbd\_class\_api::sof](structusbd__class__api.md#a9dd501ae803c5f0e8b4d62f4a57b04ca)

void(\* sof)(struct usbd\_class\_node \*const node)

Start of Frame.

**Definition** usbd.h:230

[usbd\_class\_api::update](structusbd__class__api.md#adaa09908b17f85e97f39266f79cb32a8)

void(\* update)(struct usbd\_class\_node \*const node, uint8\_t iface, uint8\_t alternate)

Configuration update handler.

**Definition** usbd.h:206

[usbd\_class\_api::request](structusbd__class__api.md#aff8426da1f7dd1f5fa5d27ce135bf0f8)

int(\* request)(struct usbd\_class\_node \*const node, struct net\_buf \*buf, int err)

Endpoint request completion event handler.

**Definition** usbd.h:220

[usbd\_class\_data](structusbd__class__data.md)

USB device support class data.

**Definition** usbd.h:248

[usbd\_class\_data::priv](structusbd__class__data.md#a10bb5b9af6098fbbc86fd00ef54e84e1)

void \* priv

Pointer to private data.

**Definition** usbd.h:270

[usbd\_class\_data::v\_reqs](structusbd__class__data.md#a32db83ecf80e1ac9e4d5deda54581deb)

const struct usbd\_cctx\_vendor\_req \* v\_reqs

Supported vendor request table, can be NULL.

**Definition** usbd.h:256

[usbd\_class\_data::state](structusbd__class__data.md#a57718d5c32580352ad7bd49000d01d3b)

atomic\_t state

Variable to store the state of the class instance.

**Definition** usbd.h:268

[usbd\_class\_data::desc](structusbd__class__data.md#a5b63cc431c007291bf96196b0eefd6c2)

void \* desc

Pointer to a class implementation descriptor that should end with a nil descriptor (bLength = 0 and b...

**Definition** usbd.h:254

[usbd\_class\_data::ep\_active](structusbd__class__data.md#aad3c8f52393d6135532d25ee8f42950e)

uint32\_t ep\_active

Bitmap of the enabled endpoints of the instance.

**Definition** usbd.h:264

[usbd\_class\_data::iface\_bm](structusbd__class__data.md#ab41348dd230fa882efb8d39260447cb4)

uint32\_t iface\_bm

Bitmap of the bInterfaceNumbers of the class instance.

**Definition** usbd.h:266

[usbd\_class\_data::ep\_assigned](structusbd__class__data.md#ab60dc9c68368c5c918ea6d23eacfaf60)

uint32\_t ep\_assigned

Bitmap of all endpoints assigned to the instance.

**Definition** usbd.h:260

[usbd\_class\_data::uds\_ctx](structusbd__class__data.md#af2560e7d2e9f4fcc70be0a13883594b1)

struct usbd\_contex \* uds\_ctx

Pointer to USB device stack context structure.

**Definition** usbd.h:250

[usbd\_class\_node](structusbd__class__node.md)

**Definition** usbd.h:273

[usbd\_class\_node::name](structusbd__class__node.md#a06682f9e64f391985b08c5d884903992)

const char \* name

Name of the USB device class instance.

**Definition** usbd.h:277

[usbd\_class\_node::node](structusbd__class__node.md#a1bdbe525e21ac5ea6eff30f6159a4406)

sys\_snode\_t node

Node information for the slist.

**Definition** usbd.h:275

[usbd\_class\_node::api](structusbd__class__node.md#a276df79bf269b19875f1c497a36392fb)

const struct usbd\_class\_api \* api

Pointer to device support class API.

**Definition** usbd.h:279

[usbd\_class\_node::data](structusbd__class__node.md#a53916906d5efce1eeb4024a7b3662553)

struct usbd\_class\_data \* data

Pointer to USB device support class data.

**Definition** usbd.h:281

[usbd\_config\_node](structusbd__config__node.md)

Device configuration node.

**Definition** usbd.h:98

[usbd\_config\_node::node](structusbd__config__node.md#a003a8d9132b319f54583263c4da1e060)

sys\_snode\_t node

slist node struct

**Definition** usbd.h:100

[usbd\_config\_node::class\_list](structusbd__config__node.md#a00493162af2344d3d39f834b4834ef78)

sys\_slist\_t class\_list

List of registered classes (functions).

**Definition** usbd.h:104

[usbd\_config\_node::desc](structusbd__config__node.md#a55081d79ab3e6b41a091b3f65d7d2d87)

void \* desc

Pointer to configuration descriptor.

**Definition** usbd.h:102

[usbd\_contex](structusbd__contex.md)

USB device support runtime context.

**Definition** usbd.h:163

[usbd\_contex::descriptors](structusbd__contex.md#a4634c51ab958993e0d2c2cbb192cc105)

sys\_dlist\_t descriptors

slist to manage descriptors like string, bos

**Definition** usbd.h:173

[usbd\_contex::ch9\_data](structusbd__contex.md#a7f0d2d526faa553e3f520a58639d271a)

struct usbd\_ch9\_data ch9\_data

Middle layer runtime data.

**Definition** usbd.h:171

[usbd\_contex::name](structusbd__contex.md#abba6950f90e08a227c5a124ba1cac794)

const char \* name

Name of the USB device.

**Definition** usbd.h:165

[usbd\_contex::configs](structusbd__contex.md#abc0473af6584cd4d4040af7d5f1b522b)

sys\_slist\_t configs

slist to manage device configurations

**Definition** usbd.h:175

[usbd\_contex::dev](structusbd__contex.md#abe1919c4098622f9a87f4b2d4caf1c3b)

const struct device \* dev

Pointer to UDC device.

**Definition** usbd.h:169

[usbd\_contex::mutex](structusbd__contex.md#ac833ce3afb9a9d86c90f35bc33ef617f)

struct k\_mutex mutex

Access mutex.

**Definition** usbd.h:167

[usbd\_contex::desc](structusbd__contex.md#ad2984b7bd687e2c753c1c7497044e9d0)

void \* desc

Pointer to device descriptor.

**Definition** usbd.h:179

[usbd\_contex::status](structusbd__contex.md#ae190c2f4e20e91e9ad75ff81012b47c2)

struct usbd\_status status

Status of the USB device support.

**Definition** usbd.h:177

[usbd\_desc\_node](structusbd__desc__node.md)

Descriptor node.

**Definition** usbd.h:75

[usbd\_desc\_node::idx](structusbd__desc__node.md#a0705a86aa6d7f532eb6be794f2c60d06)

unsigned int idx

Descriptor index, required for string descriptors.

**Definition** usbd.h:79

[usbd\_desc\_node::utf16le](structusbd__desc__node.md#a266d0936f7684f6a3047e2a6d1875458)

unsigned int utf16le

If not set, string descriptor must be converted to UTF16LE.

**Definition** usbd.h:83

[usbd\_desc\_node::custom\_sn](structusbd__desc__node.md#a322537e0b35d0590ba0f4e19ae5bb3ac)

unsigned int custom\_sn

If not set, device stack obtains SN using the hwinfo API.

**Definition** usbd.h:85

[usbd\_desc\_node::desc](structusbd__desc__node.md#a4d4692341a7785b5a0af762b1810e80f)

void \* desc

Pointer to a descriptor.

**Definition** usbd.h:87

[usbd\_desc\_node::utype](structusbd__desc__node.md#a50e1b8db1dd6a4f3ca541394ad9d9adf)

unsigned int utype

Descriptor usage type (not bDescriptorType).

**Definition** usbd.h:81

[usbd\_desc\_node::node](structusbd__desc__node.md#a9f1941cd036c01387d8ad9a4aceb595a)

sys\_dnode\_t node

slist node struct

**Definition** usbd.h:77

[usbd\_status](structusbd__status.md)

USB device support status.

**Definition** usbd.h:146

[usbd\_status::rwup](structusbd__status.md#a113085892967cf7c9cb70131b320d61a)

unsigned int rwup

USB remote wake-up feature is enabled.

**Definition** usbd.h:154

[usbd\_status::enabled](structusbd__status.md#a2382fcb655fe51e0bcf83f85aa182ba3)

unsigned int enabled

USB device support is enabled.

**Definition** usbd.h:150

[usbd\_status::initialized](structusbd__status.md#a78de12245d08ecc71e09d5519fe0e857)

unsigned int initialized

USB device support is initialized.

**Definition** usbd.h:148

[usbd\_status::suspended](structusbd__status.md#afb67cfda187e40229f842c93aa09f0ba)

unsigned int suspended

USB device is suspended.

**Definition** usbd.h:152

[byteorder.h](sys_2byteorder_8h.md)

Byte order helpers.

[iterable\_sections.h](sys_2iterable__sections_8h.md)

[usb\_ch9.h](usb__ch9_8h.md)

USB Chapter 9 structures and definitions.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [usb](dir_d8285a9da4e2f530d10dd4c17d446a84.md)
- [usbd.h](usbd_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
