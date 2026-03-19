---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/usbd__dfu_8h_source.html
original_path: doxygen/html/usbd__dfu_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbd\_dfu.h

[Go to the documentation of this file.](usbd__dfu_8h.md)

1/\*

2 \* Copyright (c) 2024 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

13

14#ifndef ZEPHYR\_INCLUDE\_USB\_CLASS\_USBD\_DFU\_H

15#define ZEPHYR\_INCLUDE\_USB\_CLASS\_USBD\_DFU\_H

16

17#include <[stdint.h](stdint_8h.md)>

18

19/\* DFU Class Subclass \*/

[ 20](usbd__dfu_8h.md#a518e936748d79f70576e082604203ae7)#define USB\_DFU\_SUBCLASS 0x01

21

22/\* DFU Class runtime Protocol \*/

[ 23](usbd__dfu_8h.md#a0f6bc7bb8b073e9a19a6a77524dde1a1)#define USB\_DFU\_PROTOCOL\_RUNTIME 0x01

24

25/\* DFU Class DFU mode Protocol \*/

[ 26](usbd__dfu_8h.md#a501a899e415cb37503f446cc54cb64ed)#define USB\_DFU\_PROTOCOL\_DFU 0x02

27

28/\* DFU Class Specific Requests \*/

[ 29](usbd__dfu_8h.md#a083ab5fb2b7ea064ba0caeeba9ecba73)#define USB\_DFU\_REQ\_DETACH 0x00

[ 30](usbd__dfu_8h.md#a54e31f9cb963e35caaf8049a8116ab52)#define USB\_DFU\_REQ\_DNLOAD 0x01

[ 31](usbd__dfu_8h.md#ac3118cca70abbc4e08a6cb58ce439f71)#define USB\_DFU\_REQ\_UPLOAD 0x02

[ 32](usbd__dfu_8h.md#afebeea3c212557b2c17dbf8549b42681)#define USB\_DFU\_REQ\_GETSTATUS 0x03

[ 33](usbd__dfu_8h.md#a1fb983580f4fc40ceec78b7bb7398126)#define USB\_DFU\_REQ\_CLRSTATUS 0x04

[ 34](usbd__dfu_8h.md#aca55ad0b7ee615c5414aa518c94af345)#define USB\_DFU\_REQ\_GETSTATE 0x05

[ 35](usbd__dfu_8h.md#a9e54b63df02eac63afd493b4ec8ba8dd)#define USB\_DFU\_REQ\_ABORT 0x06

36

37/\* Run-Time DFU Functional Descriptor \*/

[ 38](structusb__dfu__descriptor.md)struct [usb\_dfu\_descriptor](structusb__dfu__descriptor.md) {

[ 39](structusb__dfu__descriptor.md#aaae3ed6f5fc202453e5a295b25c391e0) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bLength](structusb__dfu__descriptor.md#aaae3ed6f5fc202453e5a295b25c391e0);

[ 40](structusb__dfu__descriptor.md#a545d551fdf9612abab9679ad9092fe21) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bDescriptorType](structusb__dfu__descriptor.md#a545d551fdf9612abab9679ad9092fe21);

[ 41](structusb__dfu__descriptor.md#a6eda776c2fa8ad9e92da5a9c0771c017) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bmAttributes](structusb__dfu__descriptor.md#a6eda776c2fa8ad9e92da5a9c0771c017);

[ 42](structusb__dfu__descriptor.md#ab37985af3ea9985ebe57d04eb7b004b6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wDetachTimeOut](structusb__dfu__descriptor.md#ab37985af3ea9985ebe57d04eb7b004b6);

[ 43](structusb__dfu__descriptor.md#a6f28ae6870039d8ba994a2aed1d6b8b9) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [wTransferSize](structusb__dfu__descriptor.md#a6f28ae6870039d8ba994a2aed1d6b8b9);

[ 44](structusb__dfu__descriptor.md#ac917f4ae3b4cda852e7e23a1378cc584) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [bcdDFUVersion](structusb__dfu__descriptor.md#ac917f4ae3b4cda852e7e23a1378cc584);

45} \_\_packed;

46

47/\* DFU Functional Descriptor Type \*/

[ 48](usbd__dfu_8h.md#ae5b7a3271bc417852f829a9d913a0e43)#define USB\_DESC\_DFU\_FUNCTIONAL 0x21

49

50/\* DFU attributes DFU Functional Descriptor \*/

[ 51](usbd__dfu_8h.md#a005e5b7fc18c066ee61ae393a2ba09c7)#define USB\_DFU\_ATTR\_WILL\_DETACH BIT(3)

[ 52](usbd__dfu_8h.md#a645a02847a4ff2b47ce93be8c90168eb)#define USB\_DFU\_ATTR\_MANIFESTATION\_TOLERANT BIT(2)

[ 53](usbd__dfu_8h.md#a40264d92194b790a6b285c1aefa0cc3c)#define USB\_DFU\_ATTR\_CAN\_UPLOAD BIT(1)

[ 54](usbd__dfu_8h.md#a22c5740401995633128679a460d4a2ef)#define USB\_DFU\_ATTR\_CAN\_DNLOAD BIT(0)

55

56/\* DFU Specification release \*/

[ 57](usbd__dfu_8h.md#aa3f88d63fbd9542614b6057da9c133e5)#define USB\_DFU\_VERSION 0x0110

58

59/\* DFU device status \*/

[ 60](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62)enum [usb\_dfu\_status](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62) {

[ 61](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62aa26c163b80b1f6786ca81dadc14b00fb) [ERR\_OK](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62aa26c163b80b1f6786ca81dadc14b00fb) = 0x00,

[ 62](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62a86a37904a04f8a7ddc9831e85d826a5a) [ERR\_TARGET](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62a86a37904a04f8a7ddc9831e85d826a5a) = 0x01,

[ 63](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62a1a945da4703d6f5953ea81519dcaaaad) [ERR\_FILE](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62a1a945da4703d6f5953ea81519dcaaaad) = 0x02,

[ 64](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62a7b2c2fd2edcf9479181e72ee6ef6fffc) [ERR\_WRITE](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62a7b2c2fd2edcf9479181e72ee6ef6fffc) = 0x03,

[ 65](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62a7f528dddca00563b477800a95163a347) [ERR\_ERASE](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62a7f528dddca00563b477800a95163a347) = 0x04,

[ 66](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62aaaefe7b6fd4399eb00ed391833956103) [ERR\_CHECK\_ERASED](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62aaaefe7b6fd4399eb00ed391833956103) = 0x05,

[ 67](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62a97067bf5865840561ec9eba092838e9a) [ERR\_PROG](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62a97067bf5865840561ec9eba092838e9a) = 0x06,

[ 68](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62a7b3dcb9b918d6e5af83b68d4fb767274) [ERR\_VERIFY](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62a7b3dcb9b918d6e5af83b68d4fb767274) = 0x07,

[ 69](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62a8c7d94233447f239b74aeea63cb8e09d) [ERR\_ADDRESS](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62a8c7d94233447f239b74aeea63cb8e09d) = 0x08,

[ 70](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62a1d02e2949a0d4e292140efe5742c79a6) [ERR\_NOTDONE](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62a1d02e2949a0d4e292140efe5742c79a6) = 0x09,

[ 71](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62a4f5e97d0bc125828f2c779c11426367c) [ERR\_FIRMWARE](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62a4f5e97d0bc125828f2c779c11426367c) = 0x0A,

[ 72](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62a98b47a7a9e4e6f1442d76fa668a6ff49) [ERR\_VENDOR](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62a98b47a7a9e4e6f1442d76fa668a6ff49) = 0x0B,

[ 73](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62add41639f9db3a8cc4c0183c039c2b6ed) [ERR\_USBR](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62add41639f9db3a8cc4c0183c039c2b6ed) = 0x0C,

[ 74](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62a6532abde77d62a3154cb1ee22a5bce0b) [ERR\_POR](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62a6532abde77d62a3154cb1ee22a5bce0b) = 0x0D,

[ 75](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62a5c708decdcbd7d8c9fddd8d9e75828a1) [ERR\_UNKNOWN](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62a5c708decdcbd7d8c9fddd8d9e75828a1) = 0x0E,

[ 76](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62a614b66b2b507a2c6343462f94582cecb) [ERR\_STALLEDPKT](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62a614b66b2b507a2c6343462f94582cecb) = 0x0F,

77};

78

79/\* DFU device states \*/

[ 80](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01e)enum [usb\_dfu\_state](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01e) {

[ 81](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01eab7ba8c8ed2c179fec88a9b6aafc663f0) [APP\_IDLE](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01eab7ba8c8ed2c179fec88a9b6aafc663f0) = 0,

[ 82](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01ea1b6cb3fe0a26dce8a6fce9f179aa23ef) [APP\_DETACH](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01ea1b6cb3fe0a26dce8a6fce9f179aa23ef) = 1,

[ 83](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01ea6750bb1bc3aa5e183a24e5f1eebbc134) [DFU\_IDLE](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01ea6750bb1bc3aa5e183a24e5f1eebbc134) = 2,

[ 84](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01eac112f5ac931419fca913cc4791c768cc) [DFU\_DNLOAD\_SYNC](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01eac112f5ac931419fca913cc4791c768cc) = 3,

[ 85](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01ea6c7e0d5ef61f350a4719b0d637dae263) [DFU\_DNBUSY](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01ea6c7e0d5ef61f350a4719b0d637dae263) = 4,

[ 86](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01eaf6596caed39e4fc9a86c86fc48fb04ea) [DFU\_DNLOAD\_IDLE](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01eaf6596caed39e4fc9a86c86fc48fb04ea) = 5,

[ 87](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01eadf68d3fd97017e0caba53637e530fc1d) [DFU\_MANIFEST\_SYNC](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01eadf68d3fd97017e0caba53637e530fc1d) = 6,

[ 88](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01ea7b90825d89b39d39d150336fe251982c) [DFU\_MANIFEST](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01ea7b90825d89b39d39d150336fe251982c) = 7,

[ 89](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01ea5c827ad80eccc0249ee7ada76f36a8ac) [DFU\_MANIFEST\_WAIT\_RST](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01ea5c827ad80eccc0249ee7ada76f36a8ac) = 8,

[ 90](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01eaf56d835eb6704702c3ddf5134402f82a) [DFU\_UPLOAD\_IDLE](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01eaf56d835eb6704702c3ddf5134402f82a) = 9,

[ 91](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01eafc200a88839dcdee3b90417f52b35657) [DFU\_ERROR](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01eafc200a88839dcdee3b90417f52b35657) = 10,

[ 92](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01ea24195d3c70ed2d81039d3a0e306b3c94) [DFU\_STATE\_MAX](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01ea24195d3c70ed2d81039d3a0e306b3c94) = 11,

93};

94

[ 95](structusbd__dfu__image.md)struct [usbd\_dfu\_image](structusbd__dfu__image.md) {

[ 96](structusbd__dfu__image.md#a3e2d6339752919988f3c113ca87a543e) const char \*[name](structusbd__dfu__image.md#a3e2d6339752919988f3c113ca87a543e);

[ 97](structusbd__dfu__image.md#a4df9017274c5094ed49fd8e6964b4379) struct [usb\_if\_descriptor](structusb__if__descriptor.md) \*const [if\_desc](structusbd__dfu__image.md#a4df9017274c5094ed49fd8e6964b4379);

[ 98](structusbd__dfu__image.md#a2aade79d72faef1fe8a6fe846189daf0) void \*const [priv](structusbd__dfu__image.md#a2aade79d72faef1fe8a6fe846189daf0);

[ 99](structusbd__dfu__image.md#aff741ab9145292e9b7a30fe3a93a4615) struct [usbd\_desc\_node](structusbd__desc__node.md) \*const [sd\_nd](structusbd__dfu__image.md#aff741ab9145292e9b7a30fe3a93a4615);

[ 100](structusbd__dfu__image.md#a2202146c73e3b2300200f04eff05c888) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[next\_cb](structusbd__dfu__image.md#a2202146c73e3b2300200f04eff05c888))(void \*const [priv](structusbd__dfu__image.md#a2aade79d72faef1fe8a6fe846189daf0),

101 const enum [usb\_dfu\_state](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01e) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), const enum [usb\_dfu\_state](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01e) next);

[ 102](structusbd__dfu__image.md#a03ee7685c90ac7ec8c2c4d87a6389e62) int (\*[read\_cb](structusbd__dfu__image.md#a03ee7685c90ac7ec8c2c4d87a6389e62))(void \*const [priv](structusbd__dfu__image.md#a2aade79d72faef1fe8a6fe846189daf0),

103 const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) size,

104 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) buf[static CONFIG\_USBD\_DFU\_TRANSFER\_SIZE]);

[ 105](structusbd__dfu__image.md#aad9a4efbf3649373328b6b6b12fa1922) int (\*[write\_cb](structusbd__dfu__image.md#aad9a4efbf3649373328b6b6b12fa1922))(void \*const [priv](structusbd__dfu__image.md#a2aade79d72faef1fe8a6fe846189daf0),

106 const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) block, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) size,

107 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) buf[static CONFIG\_USBD\_DFU\_TRANSFER\_SIZE]);

108};

109

116

[ 152](group__usbd__dfu.md#ga24229d3b70d2e61bb1658c35f0be5070)#define USBD\_DFU\_DEFINE\_IMG(id, iname, ipriv, iread, iwrite, inext) \

153 static \_\_noinit struct usb\_if\_descriptor usbd\_dfu\_iface\_##id; \

154 \

155 USBD\_DESC\_STRING\_DEFINE(usbd\_dfu\_str\_##id, iname, USBD\_DUT\_STRING\_INTERFACE); \

156 \

157 static const STRUCT\_SECTION\_ITERABLE(usbd\_dfu\_image, usbd\_dfu\_image\_##id) = { \

158 .name = iname, \

159 .if\_desc = &usbd\_dfu\_iface\_##id, \

160 .priv = ipriv, \

161 .sd\_nd = &usbd\_dfu\_str\_##id, \

162 .read\_cb = iread, \

163 .write\_cb = iwrite, \

164 .next\_cb = inext, \

165 }

166

170#endif /\* ZEPHYR\_INCLUDE\_USB\_CLASS\_USBD\_DFU\_H \*/

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

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

[usb\_dfu\_descriptor](structusb__dfu__descriptor.md)

**Definition** usbd\_dfu.h:38

[usb\_dfu\_descriptor::bDescriptorType](structusb__dfu__descriptor.md#a545d551fdf9612abab9679ad9092fe21)

uint8\_t bDescriptorType

**Definition** usbd\_dfu.h:40

[usb\_dfu\_descriptor::bmAttributes](structusb__dfu__descriptor.md#a6eda776c2fa8ad9e92da5a9c0771c017)

uint8\_t bmAttributes

**Definition** usbd\_dfu.h:41

[usb\_dfu\_descriptor::wTransferSize](structusb__dfu__descriptor.md#a6f28ae6870039d8ba994a2aed1d6b8b9)

uint16\_t wTransferSize

**Definition** usbd\_dfu.h:43

[usb\_dfu\_descriptor::bLength](structusb__dfu__descriptor.md#aaae3ed6f5fc202453e5a295b25c391e0)

uint8\_t bLength

**Definition** usbd\_dfu.h:39

[usb\_dfu\_descriptor::wDetachTimeOut](structusb__dfu__descriptor.md#ab37985af3ea9985ebe57d04eb7b004b6)

uint16\_t wDetachTimeOut

**Definition** usbd\_dfu.h:42

[usb\_dfu\_descriptor::bcdDFUVersion](structusb__dfu__descriptor.md#ac917f4ae3b4cda852e7e23a1378cc584)

uint16\_t bcdDFUVersion

**Definition** usbd\_dfu.h:44

[usb\_if\_descriptor](structusb__if__descriptor.md)

USB Standard Interface Descriptor defined in spec.

**Definition** usb\_ch9.h:193

[usbd\_desc\_node](structusbd__desc__node.md)

Descriptor node.

**Definition** usbd.h:163

[usbd\_dfu\_image](structusbd__dfu__image.md)

**Definition** usbd\_dfu.h:95

[usbd\_dfu\_image::read\_cb](structusbd__dfu__image.md#a03ee7685c90ac7ec8c2c4d87a6389e62)

int(\* read\_cb)(void \*const priv, const uint32\_t block, const uint16\_t size, uint8\_t buf[static CONFIG\_USBD\_DFU\_TRANSFER\_SIZE])

**Definition** usbd\_dfu.h:102

[usbd\_dfu\_image::next\_cb](structusbd__dfu__image.md#a2202146c73e3b2300200f04eff05c888)

bool(\* next\_cb)(void \*const priv, const enum usb\_dfu\_state state, const enum usb\_dfu\_state next)

**Definition** usbd\_dfu.h:100

[usbd\_dfu\_image::priv](structusbd__dfu__image.md#a2aade79d72faef1fe8a6fe846189daf0)

void \*const priv

**Definition** usbd\_dfu.h:98

[usbd\_dfu\_image::name](structusbd__dfu__image.md#a3e2d6339752919988f3c113ca87a543e)

const char \* name

**Definition** usbd\_dfu.h:96

[usbd\_dfu\_image::if\_desc](structusbd__dfu__image.md#a4df9017274c5094ed49fd8e6964b4379)

struct usb\_if\_descriptor \*const if\_desc

**Definition** usbd\_dfu.h:97

[usbd\_dfu\_image::write\_cb](structusbd__dfu__image.md#aad9a4efbf3649373328b6b6b12fa1922)

int(\* write\_cb)(void \*const priv, const uint32\_t block, const uint16\_t size, const uint8\_t buf[static CONFIG\_USBD\_DFU\_TRANSFER\_SIZE])

**Definition** usbd\_dfu.h:105

[usbd\_dfu\_image::sd\_nd](structusbd__dfu__image.md#aff741ab9145292e9b7a30fe3a93a4615)

struct usbd\_desc\_node \*const sd\_nd

**Definition** usbd\_dfu.h:99

[usb\_dfu\_status](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62)

usb\_dfu\_status

**Definition** usbd\_dfu.h:60

[ERR\_FILE](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62a1a945da4703d6f5953ea81519dcaaaad)

@ ERR\_FILE

**Definition** usbd\_dfu.h:63

[ERR\_NOTDONE](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62a1d02e2949a0d4e292140efe5742c79a6)

@ ERR\_NOTDONE

**Definition** usbd\_dfu.h:70

[ERR\_FIRMWARE](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62a4f5e97d0bc125828f2c779c11426367c)

@ ERR\_FIRMWARE

**Definition** usbd\_dfu.h:71

[ERR\_UNKNOWN](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62a5c708decdcbd7d8c9fddd8d9e75828a1)

@ ERR\_UNKNOWN

**Definition** usbd\_dfu.h:75

[ERR\_STALLEDPKT](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62a614b66b2b507a2c6343462f94582cecb)

@ ERR\_STALLEDPKT

**Definition** usbd\_dfu.h:76

[ERR\_POR](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62a6532abde77d62a3154cb1ee22a5bce0b)

@ ERR\_POR

**Definition** usbd\_dfu.h:74

[ERR\_WRITE](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62a7b2c2fd2edcf9479181e72ee6ef6fffc)

@ ERR\_WRITE

**Definition** usbd\_dfu.h:64

[ERR\_VERIFY](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62a7b3dcb9b918d6e5af83b68d4fb767274)

@ ERR\_VERIFY

**Definition** usbd\_dfu.h:68

[ERR\_ERASE](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62a7f528dddca00563b477800a95163a347)

@ ERR\_ERASE

**Definition** usbd\_dfu.h:65

[ERR\_TARGET](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62a86a37904a04f8a7ddc9831e85d826a5a)

@ ERR\_TARGET

**Definition** usbd\_dfu.h:62

[ERR\_ADDRESS](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62a8c7d94233447f239b74aeea63cb8e09d)

@ ERR\_ADDRESS

**Definition** usbd\_dfu.h:69

[ERR\_PROG](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62a97067bf5865840561ec9eba092838e9a)

@ ERR\_PROG

**Definition** usbd\_dfu.h:67

[ERR\_VENDOR](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62a98b47a7a9e4e6f1442d76fa668a6ff49)

@ ERR\_VENDOR

**Definition** usbd\_dfu.h:72

[ERR\_OK](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62aa26c163b80b1f6786ca81dadc14b00fb)

@ ERR\_OK

**Definition** usbd\_dfu.h:61

[ERR\_CHECK\_ERASED](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62aaaefe7b6fd4399eb00ed391833956103)

@ ERR\_CHECK\_ERASED

**Definition** usbd\_dfu.h:66

[ERR\_USBR](usbd__dfu_8h.md#a3c39293bedc430e245f3f0919cb36e62add41639f9db3a8cc4c0183c039c2b6ed)

@ ERR\_USBR

**Definition** usbd\_dfu.h:73

[usb\_dfu\_state](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01e)

usb\_dfu\_state

**Definition** usbd\_dfu.h:80

[APP\_DETACH](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01ea1b6cb3fe0a26dce8a6fce9f179aa23ef)

@ APP\_DETACH

**Definition** usbd\_dfu.h:82

[DFU\_STATE\_MAX](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01ea24195d3c70ed2d81039d3a0e306b3c94)

@ DFU\_STATE\_MAX

**Definition** usbd\_dfu.h:92

[DFU\_MANIFEST\_WAIT\_RST](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01ea5c827ad80eccc0249ee7ada76f36a8ac)

@ DFU\_MANIFEST\_WAIT\_RST

**Definition** usbd\_dfu.h:89

[DFU\_IDLE](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01ea6750bb1bc3aa5e183a24e5f1eebbc134)

@ DFU\_IDLE

**Definition** usbd\_dfu.h:83

[DFU\_DNBUSY](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01ea6c7e0d5ef61f350a4719b0d637dae263)

@ DFU\_DNBUSY

**Definition** usbd\_dfu.h:85

[DFU\_MANIFEST](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01ea7b90825d89b39d39d150336fe251982c)

@ DFU\_MANIFEST

**Definition** usbd\_dfu.h:88

[APP\_IDLE](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01eab7ba8c8ed2c179fec88a9b6aafc663f0)

@ APP\_IDLE

**Definition** usbd\_dfu.h:81

[DFU\_DNLOAD\_SYNC](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01eac112f5ac931419fca913cc4791c768cc)

@ DFU\_DNLOAD\_SYNC

**Definition** usbd\_dfu.h:84

[DFU\_MANIFEST\_SYNC](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01eadf68d3fd97017e0caba53637e530fc1d)

@ DFU\_MANIFEST\_SYNC

**Definition** usbd\_dfu.h:87

[DFU\_UPLOAD\_IDLE](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01eaf56d835eb6704702c3ddf5134402f82a)

@ DFU\_UPLOAD\_IDLE

**Definition** usbd\_dfu.h:90

[DFU\_DNLOAD\_IDLE](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01eaf6596caed39e4fc9a86c86fc48fb04ea)

@ DFU\_DNLOAD\_IDLE

**Definition** usbd\_dfu.h:86

[DFU\_ERROR](usbd__dfu_8h.md#a9096f7fb11c9d84692bc677d8218d01eafc200a88839dcdee3b90417f52b35657)

@ DFU\_ERROR

**Definition** usbd\_dfu.h:91

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [usb](dir_d8285a9da4e2f530d10dd4c17d446a84.md)
- [class](dir_c68ea25cffcb2672410964c117624aed.md)
- [usbd\_dfu.h](usbd__dfu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
