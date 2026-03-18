---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/usb__ch9_8h.html
original_path: doxygen/html/usb__ch9_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usb\_ch9.h File Reference

USB Chapter 9 structures and definitions.
[More...](#details)

`#include <zephyr/version.h>`  
`#include <[zephyr/sys/util.h](util_8h_source.md)>`  
`#include <[zephyr/math/ilog2.h](ilog2_8h_source.md)>`  
`#include <[zephyr/usb/class/usb_hub.h](usb__hub_8h_source.md)>`

[Go to the source code of this file.](usb__ch9_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [usb\_req\_type\_field](structusb__req__type__field.md) |
| struct | [usb\_setup\_packet](structusb__setup__packet.md) |
|  | USB Setup Data packet defined in spec. [More...](structusb__setup__packet.md#details) |
| struct | [usb\_desc\_header](structusb__desc__header.md) |
|  | Header of an USB descriptor. [More...](structusb__desc__header.md#details) |
| struct | [usb\_device\_descriptor](structusb__device__descriptor.md) |
|  | USB Standard Device Descriptor defined in spec. [More...](structusb__device__descriptor.md#details) |
| struct | [usb\_device\_qualifier\_descriptor](structusb__device__qualifier__descriptor.md) |
|  | USB Device Qualifier Descriptor defined in spec. [More...](structusb__device__qualifier__descriptor.md#details) |
| struct | [usb\_cfg\_descriptor](structusb__cfg__descriptor.md) |
|  | USB Standard Configuration Descriptor defined in spec. [More...](structusb__cfg__descriptor.md#details) |
| struct | [usb\_if\_descriptor](structusb__if__descriptor.md) |
|  | USB Standard Interface Descriptor defined in spec. [More...](structusb__if__descriptor.md#details) |
| struct | [usb\_ep\_desc\_bmattr](structusb__ep__desc__bmattr.md) |
| struct | [usb\_ep\_descriptor](structusb__ep__descriptor.md) |
|  | USB Standard Endpoint Descriptor defined in spec. [More...](structusb__ep__descriptor.md#details) |
| struct | [usb\_string\_descriptor](structusb__string__descriptor.md) |
|  | USB Unicode (UTF16LE) String Descriptor defined in spec. [More...](structusb__string__descriptor.md#details) |
| struct | [usb\_association\_descriptor](structusb__association__descriptor.md) |
|  | USB Association Descriptor defined in USB 3 spec. [More...](structusb__association__descriptor.md#details) |

| Macros | |
| --- | --- |
| #define | [USB\_REQTYPE\_DIR\_TO\_DEVICE](#a3e431a6f30304833b6aa45a454c8bdbd)   0 |
|  | USB Setup packet RequestType Direction values (from Table 9-2). |
| #define | [USB\_REQTYPE\_DIR\_TO\_HOST](#aa080957f00a9459f9f7c533da893b31f)   1 |
| #define | [USB\_REQTYPE\_TYPE\_STANDARD](#a9529fae2802d82fd37d4ad58ab9d6f67)   0 |
|  | USB Setup packet RequestType Type values (from Table 9-2). |
| #define | [USB\_REQTYPE\_TYPE\_CLASS](#abaeb448434207462bcb312973a013f3d)   1 |
| #define | [USB\_REQTYPE\_TYPE\_VENDOR](#ad06cc151ffddfeba7bc99b819101d11d)   2 |
| #define | [USB\_REQTYPE\_TYPE\_RESERVED](#ab43bb12a355f38ea09a1dee177619b78)   3 |
| #define | [USB\_REQTYPE\_RECIPIENT\_DEVICE](#ab71be1695c56514626b15d3790e3d934)   0 |
|  | USB Setup packet RequestType Recipient values (from Table 9-2). |
| #define | [USB\_REQTYPE\_RECIPIENT\_INTERFACE](#a8c2c0646290270444df73b1319232ea7)   1 |
| #define | [USB\_REQTYPE\_RECIPIENT\_ENDPOINT](#a32154b80a8d73dfb4e261d31a8d351fa)   2 |
| #define | [USB\_REQTYPE\_RECIPIENT\_OTHER](#a2e07a8841cf9d67dc0c60badc00761b0)   3 |
| #define | [USB\_REQTYPE\_GET\_DIR](#ab9c7b95bb1467f3d116432ac9194e92d)(bmRequestType) |
|  | Get data transfer direction from bmRequestType. |
| #define | [USB\_REQTYPE\_GET\_TYPE](#a18dd1450e8fe287b2de1f8871274a3b9)(bmRequestType) |
|  | Get request type from bmRequestType. |
| #define | [USB\_REQTYPE\_GET\_RECIPIENT](#a933742b41b1da36545639df1a08c0db5)(bmRequestType) |
|  | Get request recipient from bmRequestType. |
| #define | [USB\_SREQ\_GET\_STATUS](#afffb7748ffdb525572e407024df9a201)   0x00 |
|  | USB Standard Request Codes defined in spec. |
| #define | [USB\_SREQ\_CLEAR\_FEATURE](#a16d58595c13caa66989d63343de6bccb)   0x01 |
| #define | [USB\_SREQ\_SET\_FEATURE](#ac1ef5c9fe1f3107f1a55560f81b6e25a)   0x03 |
| #define | [USB\_SREQ\_SET\_ADDRESS](#ac20c25ea20acac5d0f4484e3d9a5c759)   0x05 |
| #define | [USB\_SREQ\_GET\_DESCRIPTOR](#ab3b49f2eb21dcd597ca73ea62bfa5523)   0x06 |
| #define | [USB\_SREQ\_SET\_DESCRIPTOR](#ac95699668d43a49f1dd17ee86220984c)   0x07 |
| #define | [USB\_SREQ\_GET\_CONFIGURATION](#a505c325ea65c44f9df6df87bef30f5ee)   0x08 |
| #define | [USB\_SREQ\_SET\_CONFIGURATION](#a0f87cedfecf77bba9c52514684a13bf3)   0x09 |
| #define | [USB\_SREQ\_GET\_INTERFACE](#a26034252f1f8ddc5d7793e1ff3974764)   0x0A |
| #define | [USB\_SREQ\_SET\_INTERFACE](#acf5ea7c90528a4d9d86c279318a6cb52)   0x0B |
| #define | [USB\_SREQ\_SYNCH\_FRAME](#a390ddf7167cc081fd3d3f24f09967d06)   0x0C |
| #define | [USB\_DESC\_DEVICE](#aefeff68c3a236749d1105d94ed9bad68)   1 |
|  | Descriptor Types defined in spec. |
| #define | [USB\_DESC\_CONFIGURATION](#a7764131f2e59070eb032bd9d68d32620)   2 |
| #define | [USB\_DESC\_STRING](#a6a5678b964f3a9b4ba2f52e9a51bebf5)   3 |
| #define | [USB\_DESC\_INTERFACE](#ab98b6a1b7ec1dc4adcbd188c3a38f69f)   4 |
| #define | [USB\_DESC\_ENDPOINT](#a1428ae675c4b17d84b91eda705fe0498)   5 |
| #define | [USB\_DESC\_DEVICE\_QUALIFIER](#aae4580f7a31247f2bce47af2f27b3a64)   6 |
| #define | [USB\_DESC\_OTHER\_SPEED](#a3a8acce20fbea73ab685bb55a4a6356d)   7 |
| #define | [USB\_DESC\_INTERFACE\_POWER](#a075dd47d721cfd6cdf804f3cdf0feae1)   8 |
| #define | [USB\_DESC\_OTG](#a162988e9c51e1094635a553999f52d51)   9 |
|  | Additional Descriptor Types defined in USB 3 spec. |
| #define | [USB\_DESC\_DEBUG](#a0a7ab16adb76e6b9af587a82d5a7fbb3)   10 |
| #define | [USB\_DESC\_INTERFACE\_ASSOC](#ac84354aa0bfec12d3e21e72d29caf48b)   11 |
| #define | [USB\_DESC\_BOS](#a9f6e306632b56036d4dd7cc2430bcec9)   15 |
| #define | [USB\_DESC\_DEVICE\_CAPABILITY](#a8ff1997b326965664d90926658af7e98)   16 |
| #define | [USB\_DESC\_CS\_DEVICE](#a4ee3b5be16342ce919483c66cc701cb4)   0x21 |
|  | Class-Specific Descriptor Types as defined by USB Common Class Specification. |
| #define | [USB\_DESC\_CS\_CONFIGURATION](#a7221e0186e4e17a624b739d1807c161d)   0x22 |
| #define | [USB\_DESC\_CS\_STRING](#a0a89e53a56fcadd9f7b9e08e4d9ef5f8)   0x23 |
| #define | [USB\_DESC\_CS\_INTERFACE](#ae47a98df81bbd33336e11c3742418217)   0x24 |
| #define | [USB\_DESC\_CS\_ENDPOINT](#a3222223114b6d7ecea051a862fb685e2)   0x25 |
| #define | [USB\_SFS\_ENDPOINT\_HALT](#a78ee83859d881216f702a349e9c5133b)   0x00 |
|  | USB Standard Feature Selectors defined in spec. |
| #define | [USB\_SFS\_REMOTE\_WAKEUP](#a954bd576fddb8178e15bb3081733e49c)   0x01 |
| #define | [USB\_SFS\_TEST\_MODE](#ae2a2cf879eace08bf86d330b39578792)   0x02 |
| #define | [USB\_GET\_STATUS\_SELF\_POWERED](#a9dd608d5ce8d45fdd76bad3df4fdf34d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Bits used for GetStatus response defined in spec. |
| #define | [USB\_GET\_STATUS\_REMOTE\_WAKEUP](#a6d896f4f58e13f87f8e74af6909fada9)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [USB\_SCD\_RESERVED](#a2a8b7c42705cd1e0fd0aecb0028cb2ba)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
|  | USB Standard Configuration Descriptor Characteristics from Table 9-10. |
| #define | [USB\_SCD\_SELF\_POWERED](#a0122c49a39e67e2443e491132aa0ecfd)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| #define | [USB\_SCD\_REMOTE\_WAKEUP](#aa1fa7548e67cc2755d91b68fd1545088)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| #define | [USB\_BCC\_AUDIO](#ae7de426be60abc372396692f11a0d087)   0x01 |
|  | USB Defined Base Class Codes from [https://www.usb.org/defined-class-codes](https://www.usb.org/defined-class-codes). |
| #define | [USB\_BCC\_CDC\_CONTROL](#a1d41de530a4da0ac75ff9bb875fe037e)   0x02 |
| #define | [USB\_BCC\_HID](#ad5904a6d6835614adc9ab914778da4a4)   0x03 |
| #define | [USB\_BCC\_MASS\_STORAGE](#ab0c954d8432828c1a8baa63514053cf3)   0x08 |
| #define | [USB\_BCC\_CDC\_DATA](#a83fa62678f36459d11f9cec677990d44)   0x0A |
| #define | [USB\_BCC\_VIDEO](#a96a42b56555daa525605e124d50ecac6)   0x0E |
| #define | [USB\_BCC\_WIRELESS\_CONTROLLER](#a960d92dd43d279b6def9a0cca3d88dc2)   0xE0 |
| #define | [USB\_BCC\_MISCELLANEOUS](#a62bf5e94c7c36c9d1d94438d7a12a482)   0xEF |
| #define | [USB\_BCC\_APPLICATION](#a732af05b87cb1c53dbc7496a0da6434e)   0xFE |
| #define | [USB\_BCC\_VENDOR](#ac016944fd71362ce3924ec92cbd8f35b)   0xFF |
| #define | [USB\_SRN\_1\_1](#a0aadee41a18ac57c3ff4cd8af79c954c)   0x0110 |
|  | USB Specification Release Numbers (bcdUSB Descriptor field). |
| #define | [USB\_SRN\_2\_0](#a14527f51ba0e1634b3b477c80e7ae31f)   0x0200 |
| #define | [USB\_SRN\_2\_0\_1](#a08c992901c6007e9a2e0e4a493358653)   0x0201 |
| #define | [USB\_SRN\_2\_1](#aa39f04e0a9ad954389f19ba55ca16954)   0x0210 |
| #define | [USB\_DEC\_TO\_BCD](#aa021c46e7c0e127c513adbac04bc77ba)(dec) |
| #define | [USB\_BCD\_DRN](#a2f6e90e87d7a1d53418ce084a293e6fc) |
|  | USB Device release number (bcdDevice Descriptor field). |
| #define | [USB\_GET\_DESCRIPTOR\_TYPE](#a2916665797ca49936ed0572fb3b39a81)(wValue) |
|  | Macro to obtain descriptor type from USB\_SREQ\_GET\_DESCRIPTOR request. |
| #define | [USB\_GET\_DESCRIPTOR\_INDEX](#a653a141a5084536362396149e81b6b9a)(wValue) |
|  | Macro to obtain descriptor index from USB\_SREQ\_GET\_DESCRIPTOR request. |
| #define | [USB\_CONTROL\_EP\_MPS](#a8c4dd61ae766f50c9398c9753b4156b5)   64U |
|  | USB Control Endpoints maximum packet size (MPS). |
| #define | [USB\_EP\_DIR\_MASK](#afb744cb324e47124f93424a47d874b2a)   ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
|  | USB endpoint direction mask. |
| #define | [USB\_EP\_DIR\_IN](#aae8411e95f26738326bc25a0161dde99)   ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
|  | USB IN endpoint direction. |
| #define | [USB\_EP\_DIR\_OUT](#a0510b0a04d9cef144e4d9793310abccf)   0U |
|  | USB OUT endpoint direction. |
| #define | [USB\_EP\_GET\_IDX](#a4fd2505dba51e8f198276a032d3f0523)(ep) |
|  | Get endpoint index (number) from endpoint address. |
| #define | [USB\_EP\_GET\_DIR](#aa974862712344d5d806d521a87549284)(ep) |
|  | Get direction based on endpoint address. |
| #define | [USB\_EP\_GET\_ADDR](#aa5963d81b4b5bee364fb0078229c71cf)(idx, dir) |
|  | Get endpoint address from endpoint index and direction. |
| #define | [USB\_EP\_DIR\_IS\_IN](#a495d790dfb00609ce029631f40d0a422)(ep) |
|  | True if the endpoint is an IN endpoint. |
| #define | [USB\_EP\_DIR\_IS\_OUT](#a1734aa980e0f135ddc7873bb1a60c1a1)(ep) |
|  | True if the endpoint is an OUT endpoint. |
| #define | [USB\_CONTROL\_EP\_OUT](#a9af36e318a50a982ebf826ef1d9e384e)   ([USB\_EP\_DIR\_OUT](#a0510b0a04d9cef144e4d9793310abccf) | 0U) |
|  | USB Control Endpoints OUT address. |
| #define | [USB\_CONTROL\_EP\_IN](#ad907649f48bf773b010ce8fa36639b99)   ([USB\_EP\_DIR\_IN](#aae8411e95f26738326bc25a0161dde99) | 0U) |
|  | USB Control Endpoints IN address. |
| #define | [USB\_EP\_TRANSFER\_TYPE\_MASK](#a619c400cb86d083c38d59366bf18ee0c)   0x3U |
|  | USB endpoint transfer type mask. |
| #define | [USB\_EP\_TYPE\_CONTROL](#a1cecaf205acbc73308396af4f540c012)   0U |
|  | USB endpoint transfer type control. |
| #define | [USB\_EP\_TYPE\_ISO](#ad128f0d04114e8a5d40a943bb58eb7d2)   1U |
|  | USB endpoint transfer type isochronous. |
| #define | [USB\_EP\_TYPE\_BULK](#a89eb27133e7e106c3637039f6f49d187)   2U |
|  | USB endpoint transfer type bulk. |
| #define | [USB\_EP\_TYPE\_INTERRUPT](#a904b4eef8e7bcab363757e19832617ee)   3U |
|  | USB endpoint transfer type interrupt. |
| #define | [USB\_FS\_INT\_EP\_INTERVAL](#a3530fe35c97b660a43bcbd573015a14a)(us) |
|  | Calculate full speed interrupt endpoint bInterval from a value in microseconds. |
| #define | [USB\_HS\_INT\_EP\_INTERVAL](#aac29193abaef01df1c81566a9029c92f)(us) |
|  | Calculate high speed interrupt endpoint bInterval from a value in microseconds. |
| #define | [USB\_FS\_ISO\_EP\_INTERVAL](#a00508417f5da453f39a8aac96cbba673)(us) |
|  | Calculate high speed isochronous endpoint bInterval from a value in microseconds. |
| #define | [USB\_HS\_ISO\_EP\_INTERVAL](#ae4facc67e3acfcc97d6e9529968ea7ca)(us) |
|  | Calculate high speed isochronous endpoint bInterval from a value in microseconds. |

| Functions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [usb\_reqtype\_is\_to\_host](#a88dd2eb9cd06e825eb5de6a8ad38c97c) (const struct [usb\_setup\_packet](structusb__setup__packet.md) \*setup) |
|  | Check if request transfer direction is to host. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [usb\_reqtype\_is\_to\_device](#a7542609be1ae1730be4e14d4242d9696) (const struct [usb\_setup\_packet](structusb__setup__packet.md) \*setup) |
|  | Check if request transfer direction is to device. |

## Detailed Description

USB Chapter 9 structures and definitions.

This file contains the USB Chapter 9 structures definitions and follows, with few exceptions, the USB Specification 2.0.

## Macro Definition Documentation

## [◆ ](#a732af05b87cb1c53dbc7496a0da6434e)USB\_BCC\_APPLICATION

| #define USB\_BCC\_APPLICATION   0xFE |
| --- |

## [◆ ](#ae7de426be60abc372396692f11a0d087)USB\_BCC\_AUDIO

| #define USB\_BCC\_AUDIO   0x01 |
| --- |

USB Defined Base Class Codes from [https://www.usb.org/defined-class-codes](https://www.usb.org/defined-class-codes).

## [◆ ](#a1d41de530a4da0ac75ff9bb875fe037e)USB\_BCC\_CDC\_CONTROL

| #define USB\_BCC\_CDC\_CONTROL   0x02 |
| --- |

## [◆ ](#a83fa62678f36459d11f9cec677990d44)USB\_BCC\_CDC\_DATA

| #define USB\_BCC\_CDC\_DATA   0x0A |
| --- |

## [◆ ](#ad5904a6d6835614adc9ab914778da4a4)USB\_BCC\_HID

| #define USB\_BCC\_HID   0x03 |
| --- |

## [◆ ](#ab0c954d8432828c1a8baa63514053cf3)USB\_BCC\_MASS\_STORAGE

| #define USB\_BCC\_MASS\_STORAGE   0x08 |
| --- |

## [◆ ](#a62bf5e94c7c36c9d1d94438d7a12a482)USB\_BCC\_MISCELLANEOUS

| #define USB\_BCC\_MISCELLANEOUS   0xEF |
| --- |

## [◆ ](#ac016944fd71362ce3924ec92cbd8f35b)USB\_BCC\_VENDOR

| #define USB\_BCC\_VENDOR   0xFF |
| --- |

## [◆ ](#a96a42b56555daa525605e124d50ecac6)USB\_BCC\_VIDEO

| #define USB\_BCC\_VIDEO   0x0E |
| --- |

## [◆ ](#a960d92dd43d279b6def9a0cca3d88dc2)USB\_BCC\_WIRELESS\_CONTROLLER

| #define USB\_BCC\_WIRELESS\_CONTROLLER   0xE0 |
| --- |

## [◆ ](#a2f6e90e87d7a1d53418ce084a293e6fc)USB\_BCD\_DRN

| #define USB\_BCD\_DRN |
| --- |

**Value:**

([USB\_DEC\_TO\_BCD](#aa021c46e7c0e127c513adbac04bc77ba)(KERNEL\_VERSION\_MAJOR) << 8 | \

USB\_DEC\_TO\_BCD(KERNEL\_VERSION\_MINOR))

[USB\_DEC\_TO\_BCD](#aa021c46e7c0e127c513adbac04bc77ba)

#define USB\_DEC\_TO\_BCD(dec)

**Definition** usb\_ch9.h:274

USB Device release number (bcdDevice Descriptor field).

## [◆ ](#ad907649f48bf773b010ce8fa36639b99)USB\_CONTROL\_EP\_IN

| #define USB\_CONTROL\_EP\_IN   ([USB\_EP\_DIR\_IN](#aae8411e95f26738326bc25a0161dde99) | 0U) |
| --- |

USB Control Endpoints IN address.

## [◆ ](#a8c4dd61ae766f50c9398c9753b4156b5)USB\_CONTROL\_EP\_MPS

| #define USB\_CONTROL\_EP\_MPS   64U |
| --- |

USB Control Endpoints maximum packet size (MPS).

## [◆ ](#a9af36e318a50a982ebf826ef1d9e384e)USB\_CONTROL\_EP\_OUT

| #define USB\_CONTROL\_EP\_OUT   ([USB\_EP\_DIR\_OUT](#a0510b0a04d9cef144e4d9793310abccf) | 0U) |
| --- |

USB Control Endpoints OUT address.

## [◆ ](#aa021c46e7c0e127c513adbac04bc77ba)USB\_DEC\_TO\_BCD

| #define USB\_DEC\_TO\_BCD | ( |  | *dec* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((((dec) / 10) << 4) | ((dec) % 10))

## [◆ ](#a9f6e306632b56036d4dd7cc2430bcec9)USB\_DESC\_BOS

| #define USB\_DESC\_BOS   15 |
| --- |

## [◆ ](#a7764131f2e59070eb032bd9d68d32620)USB\_DESC\_CONFIGURATION

| #define USB\_DESC\_CONFIGURATION   2 |
| --- |

## [◆ ](#a7221e0186e4e17a624b739d1807c161d)USB\_DESC\_CS\_CONFIGURATION

| #define USB\_DESC\_CS\_CONFIGURATION   0x22 |
| --- |

## [◆ ](#a4ee3b5be16342ce919483c66cc701cb4)USB\_DESC\_CS\_DEVICE

| #define USB\_DESC\_CS\_DEVICE   0x21 |
| --- |

Class-Specific Descriptor Types as defined by USB Common Class Specification.

## [◆ ](#a3222223114b6d7ecea051a862fb685e2)USB\_DESC\_CS\_ENDPOINT

| #define USB\_DESC\_CS\_ENDPOINT   0x25 |
| --- |

## [◆ ](#ae47a98df81bbd33336e11c3742418217)USB\_DESC\_CS\_INTERFACE

| #define USB\_DESC\_CS\_INTERFACE   0x24 |
| --- |

## [◆ ](#a0a89e53a56fcadd9f7b9e08e4d9ef5f8)USB\_DESC\_CS\_STRING

| #define USB\_DESC\_CS\_STRING   0x23 |
| --- |

## [◆ ](#a0a7ab16adb76e6b9af587a82d5a7fbb3)USB\_DESC\_DEBUG

| #define USB\_DESC\_DEBUG   10 |
| --- |

## [◆ ](#aefeff68c3a236749d1105d94ed9bad68)USB\_DESC\_DEVICE

| #define USB\_DESC\_DEVICE   1 |
| --- |

Descriptor Types defined in spec.

Table 9-5

## [◆ ](#a8ff1997b326965664d90926658af7e98)USB\_DESC\_DEVICE\_CAPABILITY

| #define USB\_DESC\_DEVICE\_CAPABILITY   16 |
| --- |

## [◆ ](#aae4580f7a31247f2bce47af2f27b3a64)USB\_DESC\_DEVICE\_QUALIFIER

| #define USB\_DESC\_DEVICE\_QUALIFIER   6 |
| --- |

## [◆ ](#a1428ae675c4b17d84b91eda705fe0498)USB\_DESC\_ENDPOINT

| #define USB\_DESC\_ENDPOINT   5 |
| --- |

## [◆ ](#ab98b6a1b7ec1dc4adcbd188c3a38f69f)USB\_DESC\_INTERFACE

| #define USB\_DESC\_INTERFACE   4 |
| --- |

## [◆ ](#ac84354aa0bfec12d3e21e72d29caf48b)USB\_DESC\_INTERFACE\_ASSOC

| #define USB\_DESC\_INTERFACE\_ASSOC   11 |
| --- |

## [◆ ](#a075dd47d721cfd6cdf804f3cdf0feae1)USB\_DESC\_INTERFACE\_POWER

| #define USB\_DESC\_INTERFACE\_POWER   8 |
| --- |

## [◆ ](#a162988e9c51e1094635a553999f52d51)USB\_DESC\_OTG

| #define USB\_DESC\_OTG   9 |
| --- |

Additional Descriptor Types defined in USB 3 spec.

Table 9-5

## [◆ ](#a3a8acce20fbea73ab685bb55a4a6356d)USB\_DESC\_OTHER\_SPEED

| #define USB\_DESC\_OTHER\_SPEED   7 |
| --- |

## [◆ ](#a6a5678b964f3a9b4ba2f52e9a51bebf5)USB\_DESC\_STRING

| #define USB\_DESC\_STRING   3 |
| --- |

## [◆ ](#aae8411e95f26738326bc25a0161dde99)USB\_EP\_DIR\_IN

| #define USB\_EP\_DIR\_IN   ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

USB IN endpoint direction.

## [◆ ](#a495d790dfb00609ce029631f40d0a422)USB\_EP\_DIR\_IS\_IN

| #define USB\_EP\_DIR\_IS\_IN | ( |  | *ep* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([USB\_EP\_GET\_DIR](#aa974862712344d5d806d521a87549284)(ep) == [USB\_EP\_DIR\_IN](#aae8411e95f26738326bc25a0161dde99))

[USB\_EP\_GET\_DIR](#aa974862712344d5d806d521a87549284)

#define USB\_EP\_GET\_DIR(ep)

Get direction based on endpoint address.

**Definition** usb\_ch9.h:307

[USB\_EP\_DIR\_IN](#aae8411e95f26738326bc25a0161dde99)

#define USB\_EP\_DIR\_IN

USB IN endpoint direction.

**Definition** usb\_ch9.h:293

True if the endpoint is an IN endpoint.

## [◆ ](#a1734aa980e0f135ddc7873bb1a60c1a1)USB\_EP\_DIR\_IS\_OUT

| #define USB\_EP\_DIR\_IS\_OUT | ( |  | *ep* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([USB\_EP\_GET\_DIR](#aa974862712344d5d806d521a87549284)(ep) == [USB\_EP\_DIR\_OUT](#a0510b0a04d9cef144e4d9793310abccf))

[USB\_EP\_DIR\_OUT](#a0510b0a04d9cef144e4d9793310abccf)

#define USB\_EP\_DIR\_OUT

USB OUT endpoint direction.

**Definition** usb\_ch9.h:296

True if the endpoint is an OUT endpoint.

## [◆ ](#afb744cb324e47124f93424a47d874b2a)USB\_EP\_DIR\_MASK

| #define USB\_EP\_DIR\_MASK   ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

USB endpoint direction mask.

## [◆ ](#a0510b0a04d9cef144e4d9793310abccf)USB\_EP\_DIR\_OUT

| #define USB\_EP\_DIR\_OUT   0U |
| --- |

USB OUT endpoint direction.

## [◆ ](#aa5963d81b4b5bee364fb0078229c71cf)USB\_EP\_GET\_ADDR

| #define USB\_EP\_GET\_ADDR | ( |  | *idx*, |
| --- | --- | --- | --- |
|  |  |  | *dir* ) |

**Value:**

((idx) | ((dir) & [USB\_EP\_DIR\_MASK](#afb744cb324e47124f93424a47d874b2a)))

[USB\_EP\_DIR\_MASK](#afb744cb324e47124f93424a47d874b2a)

#define USB\_EP\_DIR\_MASK

USB endpoint direction mask.

**Definition** usb\_ch9.h:290

Get endpoint address from endpoint index and direction.

## [◆ ](#aa974862712344d5d806d521a87549284)USB\_EP\_GET\_DIR

| #define USB\_EP\_GET\_DIR | ( |  | *ep* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((ep) & [USB\_EP\_DIR\_MASK](#afb744cb324e47124f93424a47d874b2a))

Get direction based on endpoint address.

## [◆ ](#a4fd2505dba51e8f198276a032d3f0523)USB\_EP\_GET\_IDX

| #define USB\_EP\_GET\_IDX | ( |  | *ep* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((ep) & [~USB\_EP\_DIR\_MASK](#afb744cb324e47124f93424a47d874b2a))

Get endpoint index (number) from endpoint address.

## [◆ ](#a619c400cb86d083c38d59366bf18ee0c)USB\_EP\_TRANSFER\_TYPE\_MASK

| #define USB\_EP\_TRANSFER\_TYPE\_MASK   0x3U |
| --- |

USB endpoint transfer type mask.

## [◆ ](#a89eb27133e7e106c3637039f6f49d187)USB\_EP\_TYPE\_BULK

| #define USB\_EP\_TYPE\_BULK   2U |
| --- |

USB endpoint transfer type bulk.

## [◆ ](#a1cecaf205acbc73308396af4f540c012)USB\_EP\_TYPE\_CONTROL

| #define USB\_EP\_TYPE\_CONTROL   0U |
| --- |

USB endpoint transfer type control.

## [◆ ](#a904b4eef8e7bcab363757e19832617ee)USB\_EP\_TYPE\_INTERRUPT

| #define USB\_EP\_TYPE\_INTERRUPT   3U |
| --- |

USB endpoint transfer type interrupt.

## [◆ ](#ad128f0d04114e8a5d40a943bb58eb7d2)USB\_EP\_TYPE\_ISO

| #define USB\_EP\_TYPE\_ISO   1U |
| --- |

USB endpoint transfer type isochronous.

## [◆ ](#a3530fe35c97b660a43bcbd573015a14a)USB\_FS\_INT\_EP\_INTERVAL

| #define USB\_FS\_INT\_EP\_INTERVAL | ( |  | *us* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[CLAMP](group__sys-util.md#gad6e7d4f6ba5a77f9ee3c04026f1c2b67)(((us) / 1000U), 1U, 255U)

[CLAMP](group__sys-util.md#gad6e7d4f6ba5a77f9ee3c04026f1c2b67)

#define CLAMP(val, low, high)

Clamp a value to a given range.

**Definition** util.h:407

Calculate full speed interrupt endpoint bInterval from a value in microseconds.

## [◆ ](#a00508417f5da453f39a8aac96cbba673)USB\_FS\_ISO\_EP\_INTERVAL

| #define USB\_FS\_ISO\_EP\_INTERVAL | ( |  | *us* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[CLAMP](group__sys-util.md#gad6e7d4f6ba5a77f9ee3c04026f1c2b67)(((us) / 1000U), 1U, 16U)

Calculate high speed isochronous endpoint bInterval from a value in microseconds.

## [◆ ](#a653a141a5084536362396149e81b6b9a)USB\_GET\_DESCRIPTOR\_INDEX

| #define USB\_GET\_DESCRIPTOR\_INDEX | ( |  | *wValue* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))(wValue))

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

Macro to obtain descriptor index from USB\_SREQ\_GET\_DESCRIPTOR request.

## [◆ ](#a2916665797ca49936ed0572fb3b39a81)USB\_GET\_DESCRIPTOR\_TYPE

| #define USB\_GET\_DESCRIPTOR\_TYPE | ( |  | *wValue* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))((wValue) >> 8))

Macro to obtain descriptor type from USB\_SREQ\_GET\_DESCRIPTOR request.

## [◆ ](#a6d896f4f58e13f87f8e74af6909fada9)USB\_GET\_STATUS\_REMOTE\_WAKEUP

| #define USB\_GET\_STATUS\_REMOTE\_WAKEUP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a9dd608d5ce8d45fdd76bad3df4fdf34d)USB\_GET\_STATUS\_SELF\_POWERED

| #define USB\_GET\_STATUS\_SELF\_POWERED   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

Bits used for GetStatus response defined in spec.

Figure 9-4

## [◆ ](#aac29193abaef01df1c81566a9029c92f)USB\_HS\_INT\_EP\_INTERVAL

| #define USB\_HS\_INT\_EP\_INTERVAL | ( |  | *us* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[CLAMP](group__sys-util.md#gad6e7d4f6ba5a77f9ee3c04026f1c2b67)(([ilog2](ilog2_8h.md#a2696c6303d4c53b65a3a7f7ff771d5eb)((us) / 125U) + 1U), 1U, 16U)

[ilog2](ilog2_8h.md#a2696c6303d4c53b65a3a7f7ff771d5eb)

#define ilog2(n)

Calculate integer log2.

**Definition** ilog2.h:93

Calculate high speed interrupt endpoint bInterval from a value in microseconds.

## [◆ ](#ae4facc67e3acfcc97d6e9529968ea7ca)USB\_HS\_ISO\_EP\_INTERVAL

| #define USB\_HS\_ISO\_EP\_INTERVAL | ( |  | *us* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[CLAMP](group__sys-util.md#gad6e7d4f6ba5a77f9ee3c04026f1c2b67)(([ilog2](ilog2_8h.md#a2696c6303d4c53b65a3a7f7ff771d5eb)((us) / 125U) + 1U), 1U, 16U)

Calculate high speed isochronous endpoint bInterval from a value in microseconds.

## [◆ ](#a3e431a6f30304833b6aa45a454c8bdbd)USB\_REQTYPE\_DIR\_TO\_DEVICE

| #define USB\_REQTYPE\_DIR\_TO\_DEVICE   0 |
| --- |

USB Setup packet RequestType Direction values (from Table 9-2).

## [◆ ](#aa080957f00a9459f9f7c533da893b31f)USB\_REQTYPE\_DIR\_TO\_HOST

| #define USB\_REQTYPE\_DIR\_TO\_HOST   1 |
| --- |

## [◆ ](#ab9c7b95bb1467f3d116432ac9194e92d)USB\_REQTYPE\_GET\_DIR

| #define USB\_REQTYPE\_GET\_DIR | ( |  | *bmRequestType* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((bmRequestType) >> 7) & 0x01U)

Get data transfer direction from bmRequestType.

## [◆ ](#a933742b41b1da36545639df1a08c0db5)USB\_REQTYPE\_GET\_RECIPIENT

| #define USB\_REQTYPE\_GET\_RECIPIENT | ( |  | *bmRequestType* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((bmRequestType) & 0x1FU)

Get request recipient from bmRequestType.

## [◆ ](#a18dd1450e8fe287b2de1f8871274a3b9)USB\_REQTYPE\_GET\_TYPE

| #define USB\_REQTYPE\_GET\_TYPE | ( |  | *bmRequestType* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((bmRequestType) >> 5) & 0x03U)

Get request type from bmRequestType.

## [◆ ](#ab71be1695c56514626b15d3790e3d934)USB\_REQTYPE\_RECIPIENT\_DEVICE

| #define USB\_REQTYPE\_RECIPIENT\_DEVICE   0 |
| --- |

USB Setup packet RequestType Recipient values (from Table 9-2).

## [◆ ](#a32154b80a8d73dfb4e261d31a8d351fa)USB\_REQTYPE\_RECIPIENT\_ENDPOINT

| #define USB\_REQTYPE\_RECIPIENT\_ENDPOINT   2 |
| --- |

## [◆ ](#a8c2c0646290270444df73b1319232ea7)USB\_REQTYPE\_RECIPIENT\_INTERFACE

| #define USB\_REQTYPE\_RECIPIENT\_INTERFACE   1 |
| --- |

## [◆ ](#a2e07a8841cf9d67dc0c60badc00761b0)USB\_REQTYPE\_RECIPIENT\_OTHER

| #define USB\_REQTYPE\_RECIPIENT\_OTHER   3 |
| --- |

## [◆ ](#abaeb448434207462bcb312973a013f3d)USB\_REQTYPE\_TYPE\_CLASS

| #define USB\_REQTYPE\_TYPE\_CLASS   1 |
| --- |

## [◆ ](#ab43bb12a355f38ea09a1dee177619b78)USB\_REQTYPE\_TYPE\_RESERVED

| #define USB\_REQTYPE\_TYPE\_RESERVED   3 |
| --- |

## [◆ ](#a9529fae2802d82fd37d4ad58ab9d6f67)USB\_REQTYPE\_TYPE\_STANDARD

| #define USB\_REQTYPE\_TYPE\_STANDARD   0 |
| --- |

USB Setup packet RequestType Type values (from Table 9-2).

## [◆ ](#ad06cc151ffddfeba7bc99b819101d11d)USB\_REQTYPE\_TYPE\_VENDOR

| #define USB\_REQTYPE\_TYPE\_VENDOR   2 |
| --- |

## [◆ ](#aa1fa7548e67cc2755d91b68fd1545088)USB\_SCD\_REMOTE\_WAKEUP

| #define USB\_SCD\_REMOTE\_WAKEUP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

## [◆ ](#a2a8b7c42705cd1e0fd0aecb0028cb2ba)USB\_SCD\_RESERVED

| #define USB\_SCD\_RESERVED   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

USB Standard Configuration Descriptor Characteristics from Table 9-10.

## [◆ ](#a0122c49a39e67e2443e491132aa0ecfd)USB\_SCD\_SELF\_POWERED

| #define USB\_SCD\_SELF\_POWERED   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

## [◆ ](#a78ee83859d881216f702a349e9c5133b)USB\_SFS\_ENDPOINT\_HALT

| #define USB\_SFS\_ENDPOINT\_HALT   0x00 |
| --- |

USB Standard Feature Selectors defined in spec.

Table 9-6

## [◆ ](#a954bd576fddb8178e15bb3081733e49c)USB\_SFS\_REMOTE\_WAKEUP

| #define USB\_SFS\_REMOTE\_WAKEUP   0x01 |
| --- |

## [◆ ](#ae2a2cf879eace08bf86d330b39578792)USB\_SFS\_TEST\_MODE

| #define USB\_SFS\_TEST\_MODE   0x02 |
| --- |

## [◆ ](#a16d58595c13caa66989d63343de6bccb)USB\_SREQ\_CLEAR\_FEATURE

| #define USB\_SREQ\_CLEAR\_FEATURE   0x01 |
| --- |

## [◆ ](#a505c325ea65c44f9df6df87bef30f5ee)USB\_SREQ\_GET\_CONFIGURATION

| #define USB\_SREQ\_GET\_CONFIGURATION   0x08 |
| --- |

## [◆ ](#ab3b49f2eb21dcd597ca73ea62bfa5523)USB\_SREQ\_GET\_DESCRIPTOR

| #define USB\_SREQ\_GET\_DESCRIPTOR   0x06 |
| --- |

## [◆ ](#a26034252f1f8ddc5d7793e1ff3974764)USB\_SREQ\_GET\_INTERFACE

| #define USB\_SREQ\_GET\_INTERFACE   0x0A |
| --- |

## [◆ ](#afffb7748ffdb525572e407024df9a201)USB\_SREQ\_GET\_STATUS

| #define USB\_SREQ\_GET\_STATUS   0x00 |
| --- |

USB Standard Request Codes defined in spec.

Table 9-4

## [◆ ](#ac20c25ea20acac5d0f4484e3d9a5c759)USB\_SREQ\_SET\_ADDRESS

| #define USB\_SREQ\_SET\_ADDRESS   0x05 |
| --- |

## [◆ ](#a0f87cedfecf77bba9c52514684a13bf3)USB\_SREQ\_SET\_CONFIGURATION

| #define USB\_SREQ\_SET\_CONFIGURATION   0x09 |
| --- |

## [◆ ](#ac95699668d43a49f1dd17ee86220984c)USB\_SREQ\_SET\_DESCRIPTOR

| #define USB\_SREQ\_SET\_DESCRIPTOR   0x07 |
| --- |

## [◆ ](#ac1ef5c9fe1f3107f1a55560f81b6e25a)USB\_SREQ\_SET\_FEATURE

| #define USB\_SREQ\_SET\_FEATURE   0x03 |
| --- |

## [◆ ](#acf5ea7c90528a4d9d86c279318a6cb52)USB\_SREQ\_SET\_INTERFACE

| #define USB\_SREQ\_SET\_INTERFACE   0x0B |
| --- |

## [◆ ](#a390ddf7167cc081fd3d3f24f09967d06)USB\_SREQ\_SYNCH\_FRAME

| #define USB\_SREQ\_SYNCH\_FRAME   0x0C |
| --- |

## [◆ ](#a0aadee41a18ac57c3ff4cd8af79c954c)USB\_SRN\_1\_1

| #define USB\_SRN\_1\_1   0x0110 |
| --- |

USB Specification Release Numbers (bcdUSB Descriptor field).

## [◆ ](#a14527f51ba0e1634b3b477c80e7ae31f)USB\_SRN\_2\_0

| #define USB\_SRN\_2\_0   0x0200 |
| --- |

## [◆ ](#a08c992901c6007e9a2e0e4a493358653)USB\_SRN\_2\_0\_1

| #define USB\_SRN\_2\_0\_1   0x0201 |
| --- |

## [◆ ](#aa39f04e0a9ad954389f19ba55ca16954)USB\_SRN\_2\_1

| #define USB\_SRN\_2\_1   0x0210 |
| --- |

## Function Documentation

## [◆ ](#a7542609be1ae1730be4e14d4242d9696)usb\_reqtype\_is\_to\_device()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) usb\_reqtype\_is\_to\_device | ( | const struct [usb\_setup\_packet](structusb__setup__packet.md) \* | *setup* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Check if request transfer direction is to device.

Parameters
:   | setup | Pointer to USB Setup packet |
    | --- | --- |

Returns
:   true If transfer direction is to device

## [◆ ](#a88dd2eb9cd06e825eb5de6a8ad38c97c)usb\_reqtype\_is\_to\_host()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) usb\_reqtype\_is\_to\_host | ( | const struct [usb\_setup\_packet](structusb__setup__packet.md) \* | *setup* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Check if request transfer direction is to host.

Parameters
:   | setup | Pointer to USB Setup packet |
    | --- | --- |

Returns
:   true If transfer direction is to host

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [usb](dir_d8285a9da4e2f530d10dd4c17d446a84.md)
- [usb\_ch9.h](usb__ch9_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
