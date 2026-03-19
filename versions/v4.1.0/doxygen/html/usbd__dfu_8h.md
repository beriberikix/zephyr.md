---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/usbd__dfu_8h.html
original_path: doxygen/html/usbd__dfu_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbd\_dfu.h File Reference

USB Device Firmware Upgrade (DFU) public header.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`

[Go to the source code of this file.](usbd__dfu_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [usb\_dfu\_descriptor](structusb__dfu__descriptor.md) |
| struct | [usbd\_dfu\_image](structusbd__dfu__image.md) |

| Macros | |
| --- | --- |
| #define | [USB\_DFU\_SUBCLASS](#a518e936748d79f70576e082604203ae7)   0x01 |
| #define | [USB\_DFU\_PROTOCOL\_RUNTIME](#a0f6bc7bb8b073e9a19a6a77524dde1a1)   0x01 |
| #define | [USB\_DFU\_PROTOCOL\_DFU](#a501a899e415cb37503f446cc54cb64ed)   0x02 |
| #define | [USB\_DFU\_REQ\_DETACH](#a083ab5fb2b7ea064ba0caeeba9ecba73)   0x00 |
| #define | [USB\_DFU\_REQ\_DNLOAD](#a54e31f9cb963e35caaf8049a8116ab52)   0x01 |
| #define | [USB\_DFU\_REQ\_UPLOAD](#ac3118cca70abbc4e08a6cb58ce439f71)   0x02 |
| #define | [USB\_DFU\_REQ\_GETSTATUS](#afebeea3c212557b2c17dbf8549b42681)   0x03 |
| #define | [USB\_DFU\_REQ\_CLRSTATUS](#a1fb983580f4fc40ceec78b7bb7398126)   0x04 |
| #define | [USB\_DFU\_REQ\_GETSTATE](#aca55ad0b7ee615c5414aa518c94af345)   0x05 |
| #define | [USB\_DFU\_REQ\_ABORT](#a9e54b63df02eac63afd493b4ec8ba8dd)   0x06 |
| #define | [USB\_DESC\_DFU\_FUNCTIONAL](#ae5b7a3271bc417852f829a9d913a0e43)   0x21 |
| #define | [USB\_DFU\_ATTR\_WILL\_DETACH](#a005e5b7fc18c066ee61ae393a2ba09c7)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [USB\_DFU\_ATTR\_MANIFESTATION\_TOLERANT](#a645a02847a4ff2b47ce93be8c90168eb)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [USB\_DFU\_ATTR\_CAN\_UPLOAD](#a40264d92194b790a6b285c1aefa0cc3c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [USB\_DFU\_ATTR\_CAN\_DNLOAD](#a22c5740401995633128679a460d4a2ef)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [USB\_DFU\_VERSION](#aa3f88d63fbd9542614b6057da9c133e5)   0x0110 |
| #define | [USBD\_DFU\_DEFINE\_IMG](group__usbd__dfu.md#ga24229d3b70d2e61bb1658c35f0be5070)(id, iname, ipriv, iread, iwrite, inext) |
|  | Define USB DFU image. |

| Enumerations | |
| --- | --- |
| enum | [usb\_dfu\_status](#a3c39293bedc430e245f3f0919cb36e62) {     [ERR\_OK](#a3c39293bedc430e245f3f0919cb36e62aa26c163b80b1f6786ca81dadc14b00fb) = 0x00 , [ERR\_TARGET](#a3c39293bedc430e245f3f0919cb36e62a86a37904a04f8a7ddc9831e85d826a5a) = 0x01 , [ERR\_FILE](#a3c39293bedc430e245f3f0919cb36e62a1a945da4703d6f5953ea81519dcaaaad) = 0x02 , [ERR\_WRITE](#a3c39293bedc430e245f3f0919cb36e62a7b2c2fd2edcf9479181e72ee6ef6fffc) = 0x03 ,     [ERR\_ERASE](#a3c39293bedc430e245f3f0919cb36e62a7f528dddca00563b477800a95163a347) = 0x04 , [ERR\_CHECK\_ERASED](#a3c39293bedc430e245f3f0919cb36e62aaaefe7b6fd4399eb00ed391833956103) = 0x05 , [ERR\_PROG](#a3c39293bedc430e245f3f0919cb36e62a97067bf5865840561ec9eba092838e9a) = 0x06 , [ERR\_VERIFY](#a3c39293bedc430e245f3f0919cb36e62a7b3dcb9b918d6e5af83b68d4fb767274) = 0x07 ,     [ERR\_ADDRESS](#a3c39293bedc430e245f3f0919cb36e62a8c7d94233447f239b74aeea63cb8e09d) = 0x08 , [ERR\_NOTDONE](#a3c39293bedc430e245f3f0919cb36e62a1d02e2949a0d4e292140efe5742c79a6) = 0x09 , [ERR\_FIRMWARE](#a3c39293bedc430e245f3f0919cb36e62a4f5e97d0bc125828f2c779c11426367c) = 0x0A , [ERR\_VENDOR](#a3c39293bedc430e245f3f0919cb36e62a98b47a7a9e4e6f1442d76fa668a6ff49) = 0x0B ,     [ERR\_USBR](#a3c39293bedc430e245f3f0919cb36e62add41639f9db3a8cc4c0183c039c2b6ed) = 0x0C , [ERR\_POR](#a3c39293bedc430e245f3f0919cb36e62a6532abde77d62a3154cb1ee22a5bce0b) = 0x0D , [ERR\_UNKNOWN](#a3c39293bedc430e245f3f0919cb36e62a5c708decdcbd7d8c9fddd8d9e75828a1) = 0x0E , [ERR\_STALLEDPKT](#a3c39293bedc430e245f3f0919cb36e62a614b66b2b507a2c6343462f94582cecb) = 0x0F   } |
| enum | [usb\_dfu\_state](#a9096f7fb11c9d84692bc677d8218d01e) {     [APP\_IDLE](#a9096f7fb11c9d84692bc677d8218d01eab7ba8c8ed2c179fec88a9b6aafc663f0) = 0 , [APP\_DETACH](#a9096f7fb11c9d84692bc677d8218d01ea1b6cb3fe0a26dce8a6fce9f179aa23ef) = 1 , [DFU\_IDLE](#a9096f7fb11c9d84692bc677d8218d01ea6750bb1bc3aa5e183a24e5f1eebbc134) = 2 , [DFU\_DNLOAD\_SYNC](#a9096f7fb11c9d84692bc677d8218d01eac112f5ac931419fca913cc4791c768cc) = 3 ,     [DFU\_DNBUSY](#a9096f7fb11c9d84692bc677d8218d01ea6c7e0d5ef61f350a4719b0d637dae263) = 4 , [DFU\_DNLOAD\_IDLE](#a9096f7fb11c9d84692bc677d8218d01eaf6596caed39e4fc9a86c86fc48fb04ea) = 5 , [DFU\_MANIFEST\_SYNC](#a9096f7fb11c9d84692bc677d8218d01eadf68d3fd97017e0caba53637e530fc1d) = 6 , [DFU\_MANIFEST](#a9096f7fb11c9d84692bc677d8218d01ea7b90825d89b39d39d150336fe251982c) = 7 ,     [DFU\_MANIFEST\_WAIT\_RST](#a9096f7fb11c9d84692bc677d8218d01ea5c827ad80eccc0249ee7ada76f36a8ac) = 8 , [DFU\_UPLOAD\_IDLE](#a9096f7fb11c9d84692bc677d8218d01eaf56d835eb6704702c3ddf5134402f82a) = 9 , [DFU\_ERROR](#a9096f7fb11c9d84692bc677d8218d01eafc200a88839dcdee3b90417f52b35657) = 10 , [DFU\_STATE\_MAX](#a9096f7fb11c9d84692bc677d8218d01ea24195d3c70ed2d81039d3a0e306b3c94) = 11   } |

## Detailed Description

USB Device Firmware Upgrade (DFU) public header.

Header exposes API for registering DFU images.

## Macro Definition Documentation

## [◆ ](#ae5b7a3271bc417852f829a9d913a0e43)USB\_DESC\_DFU\_FUNCTIONAL

| #define USB\_DESC\_DFU\_FUNCTIONAL   0x21 |
| --- |

## [◆ ](#a22c5740401995633128679a460d4a2ef)USB\_DFU\_ATTR\_CAN\_DNLOAD

| #define USB\_DFU\_ATTR\_CAN\_DNLOAD   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a40264d92194b790a6b285c1aefa0cc3c)USB\_DFU\_ATTR\_CAN\_UPLOAD

| #define USB\_DFU\_ATTR\_CAN\_UPLOAD   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a645a02847a4ff2b47ce93be8c90168eb)USB\_DFU\_ATTR\_MANIFESTATION\_TOLERANT

| #define USB\_DFU\_ATTR\_MANIFESTATION\_TOLERANT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#a005e5b7fc18c066ee61ae393a2ba09c7)USB\_DFU\_ATTR\_WILL\_DETACH

| #define USB\_DFU\_ATTR\_WILL\_DETACH   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

## [◆ ](#a501a899e415cb37503f446cc54cb64ed)USB\_DFU\_PROTOCOL\_DFU

| #define USB\_DFU\_PROTOCOL\_DFU   0x02 |
| --- |

## [◆ ](#a0f6bc7bb8b073e9a19a6a77524dde1a1)USB\_DFU\_PROTOCOL\_RUNTIME

| #define USB\_DFU\_PROTOCOL\_RUNTIME   0x01 |
| --- |

## [◆ ](#a9e54b63df02eac63afd493b4ec8ba8dd)USB\_DFU\_REQ\_ABORT

| #define USB\_DFU\_REQ\_ABORT   0x06 |
| --- |

## [◆ ](#a1fb983580f4fc40ceec78b7bb7398126)USB\_DFU\_REQ\_CLRSTATUS

| #define USB\_DFU\_REQ\_CLRSTATUS   0x04 |
| --- |

## [◆ ](#a083ab5fb2b7ea064ba0caeeba9ecba73)USB\_DFU\_REQ\_DETACH

| #define USB\_DFU\_REQ\_DETACH   0x00 |
| --- |

## [◆ ](#a54e31f9cb963e35caaf8049a8116ab52)USB\_DFU\_REQ\_DNLOAD

| #define USB\_DFU\_REQ\_DNLOAD   0x01 |
| --- |

## [◆ ](#aca55ad0b7ee615c5414aa518c94af345)USB\_DFU\_REQ\_GETSTATE

| #define USB\_DFU\_REQ\_GETSTATE   0x05 |
| --- |

## [◆ ](#afebeea3c212557b2c17dbf8549b42681)USB\_DFU\_REQ\_GETSTATUS

| #define USB\_DFU\_REQ\_GETSTATUS   0x03 |
| --- |

## [◆ ](#ac3118cca70abbc4e08a6cb58ce439f71)USB\_DFU\_REQ\_UPLOAD

| #define USB\_DFU\_REQ\_UPLOAD   0x02 |
| --- |

## [◆ ](#a518e936748d79f70576e082604203ae7)USB\_DFU\_SUBCLASS

| #define USB\_DFU\_SUBCLASS   0x01 |
| --- |

## [◆ ](#aa3f88d63fbd9542614b6057da9c133e5)USB\_DFU\_VERSION

| #define USB\_DFU\_VERSION   0x0110 |
| --- |

## Enumeration Type Documentation

## [◆ ](#a9096f7fb11c9d84692bc677d8218d01e)usb\_dfu\_state

| enum [usb\_dfu\_state](#a9096f7fb11c9d84692bc677d8218d01e) |
| --- |

| Enumerator | |
| --- | --- |
| APP\_IDLE |  |
| APP\_DETACH |  |
| DFU\_IDLE |  |
| DFU\_DNLOAD\_SYNC |  |
| DFU\_DNBUSY |  |
| DFU\_DNLOAD\_IDLE |  |
| DFU\_MANIFEST\_SYNC |  |
| DFU\_MANIFEST |  |
| DFU\_MANIFEST\_WAIT\_RST |  |
| DFU\_UPLOAD\_IDLE |  |
| DFU\_ERROR |  |
| DFU\_STATE\_MAX |  |

## [◆ ](#a3c39293bedc430e245f3f0919cb36e62)usb\_dfu\_status

| enum [usb\_dfu\_status](#a3c39293bedc430e245f3f0919cb36e62) |
| --- |

| Enumerator | |
| --- | --- |
| ERR\_OK |  |
| ERR\_TARGET |  |
| ERR\_FILE |  |
| ERR\_WRITE |  |
| ERR\_ERASE |  |
| ERR\_CHECK\_ERASED |  |
| ERR\_PROG |  |
| ERR\_VERIFY |  |
| ERR\_ADDRESS |  |
| ERR\_NOTDONE |  |
| ERR\_FIRMWARE |  |
| ERR\_VENDOR |  |
| ERR\_USBR |  |
| ERR\_POR |  |
| ERR\_UNKNOWN |  |
| ERR\_STALLEDPKT |  |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [usb](dir_d8285a9da4e2f530d10dd4c17d446a84.md)
- [class](dir_c68ea25cffcb2672410964c117624aed.md)
- [usbd\_dfu.h](usbd__dfu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
