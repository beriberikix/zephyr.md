---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/usb__device_8h.html
original_path: doxygen/html/usb__device_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usb\_device.h File Reference

USB device core layer APIs and structures.
[More...](#details)

`#include <[zephyr/drivers/usb/usb_dc.h](usb__dc_8h_source.md)>`  
`#include <[zephyr/usb/usb_ch9.h](usb__ch9_8h_source.md)>`  
`#include <[zephyr/logging/log.h](log_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`

[Go to the source code of this file.](usb__device_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [usb\_ep\_cfg\_data](structusb__ep__cfg__data.md) |
|  | USB Endpoint Configuration. [More...](structusb__ep__cfg__data.md#details) |
| struct | [usb\_interface\_cfg\_data](structusb__interface__cfg__data.md) |
|  | USB Interface Configuration. [More...](structusb__interface__cfg__data.md#details) |
| struct | [usb\_cfg\_data](structusb__cfg__data.md) |
|  | USB device configuration. [More...](structusb__cfg__data.md#details) |

| Macros | |
| --- | --- |
| #define | [USBD\_DEVICE\_DESCR\_DEFINE](#a95efe03ee4bbfa4d9b0c3932b8ddfe31)(p) |
| #define | [USBD\_CLASS\_DESCR\_DEFINE](#a9403c2bd43e638b4d5634288dfb6574b)(p, instance) |
| #define | [USBD\_MISC\_DESCR\_DEFINE](#a6ff803fe6831ca99e3e9543dd1d2f37d)(p) |
| #define | [USBD\_USER\_DESCR\_DEFINE](#a76a98dcc6ca0284195d61bb928197e38)(p) |
| #define | [USBD\_STRING\_DESCR\_DEFINE](#acb8451e935bab6c8fe2f7eea97a8ae6f)(p) |
| #define | [USBD\_STRING\_DESCR\_USER\_DEFINE](#a5bc3e0d5484c0c54e5996d99ebedc51b)(p) |
| #define | [USBD\_TERM\_DESCR\_DEFINE](#a2ad0dd7628d3038c32809e6850baf23f)(p) |
| #define | [USBD\_DEFINE\_CFG\_DATA](#a5db8e2eb30dd2afc51dbb9e08fbc07c6)(name) |
| #define | [USBD\_CFG\_DATA\_DEFINE](#a99b3c84f3988ccf277e41b3c52c4a51a)(p, name) |
| #define | [USB\_MAX\_CTRL\_MPS](#a3d01cf3cbbd08db3d6cfcfb45062b961)   64 |
|  | maximum packet size (MPS) for EP 0 |
| #define | [USB\_MAX\_FS\_BULK\_MPS](#a07bbd07466b47a0c498f26e25932392f)   64 |
|  | full speed MPS for bulk EP |
| #define | [USB\_MAX\_FS\_INT\_MPS](#ae88dc2d0b2a21779d8c353cd63ae3455)   64 |
|  | full speed MPS for interrupt EP |
| #define | [USB\_MAX\_FS\_ISO\_MPS](#ae45dfb00deef73b2a142576bf136b062)   1023 |
|  | full speed MPS for isochronous EP |
| #define | [USB\_TRANS\_READ](group____usb__device__core__api.md#gabb531b022f5d2d859227a7b35d593d80)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) /\*\* Read transfer flag \*/ |
| #define | [USB\_TRANS\_WRITE](group____usb__device__core__api.md#ga163ee39a47b0a3d9fe3697cc4f24e787)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) /\*\* Write transfer flag \*/ |
| #define | [USB\_TRANS\_NO\_ZLP](group____usb__device__core__api.md#ga81c618544f27e0dc0e556021b0418c40)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) /\*\* No zero-length packet flag \*/ |

| Typedefs | |
| --- | --- |
| typedef void(\* | [usb\_ep\_callback](group____usb__device__core__api.md#ga9a45db26a9be295640ed122533427725)) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, enum [usb\_dc\_ep\_cb\_status\_code](group____usb__device__controller__api.md#gaf7f083f61e1406e7d41513113dccd3bd) cb\_status) |
|  | Callback function signature for the USB Endpoint status. |
| typedef int(\* | [usb\_request\_handler](group____usb__device__core__api.md#gaddacbff094a41c885c3041af72fa6804)) (struct [usb\_setup\_packet](structusb__setup__packet.md) \*setup, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*transfer\_len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*payload\_data) |
|  | Callback function signature for class specific requests. |
| typedef void(\* | [usb\_interface\_config](group____usb__device__core__api.md#ga3439af9464471b3acdc21f4359efb53a)) (struct [usb\_desc\_header](structusb__desc__header.md) \*head, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bInterfaceNumber) |
|  | Function for interface runtime configuration. |
| typedef void(\* | [usb\_transfer\_callback](group____usb__device__core__api.md#ga2e599eb20f647d9bb2369d76a7dc51db)) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, int tsize, void \*priv) |
|  | Callback function signature for transfer completion. |

| Functions | |
| --- | --- |
| int | [usb\_set\_config](group____usb__device__core__api.md#ga28783e727e35db1a651309a7f9f5444a) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*usb\_descriptor) |
|  | Configure USB controller. |
| int | [usb\_deconfig](group____usb__device__core__api.md#ga2d485c77055dd975f3170fbaea7f2bdf) (void) |
|  | Deconfigure USB controller. |
| int | [usb\_enable](group____usb__device__core__api.md#gad1fa5e491d93c2bd1fe7967c12148902) ([usb\_dc\_status\_callback](group____usb__device__controller__api.md#ga2ddb0b059b4e1e76473ed7f56d0cf2ee) status\_cb) |
|  | Enable the USB subsystem and associated hardware. |
| int | [usb\_disable](group____usb__device__core__api.md#ga65723c9469a12c87e5554169396f8e76) (void) |
|  | Disable the USB device. |
| int | [usb\_write](group____usb__device__core__api.md#ga6d4b568f2f3aac4f099c35393fb601b3) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data\_len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*bytes\_ret) |
|  | Write data to the specified endpoint. |
| int | [usb\_read](group____usb__device__core__api.md#gab2c21738baa839b483654d1d5baf2981) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) max\_data\_len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*ret\_bytes) |
|  | Read data from the specified endpoint. |
| int | [usb\_ep\_set\_stall](group____usb__device__core__api.md#gaaf206afaf32bde1b8d77d04bc6ec091f) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Set STALL condition on the specified endpoint. |
| int | [usb\_ep\_clear\_stall](group____usb__device__core__api.md#gae7bc410d0db8a6d2142992153bb1424d) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Clears STALL condition on the specified endpoint. |
| int | [usb\_ep\_read\_wait](group____usb__device__core__api.md#ga4c919f7e993f80150bdde2d7fab254ee) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) max\_data\_len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*read\_bytes) |
|  | Read data from the specified endpoint. |
| int | [usb\_ep\_read\_continue](group____usb__device__core__api.md#gaab17b8c523ac211ff308c8dc774ba092) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Continue reading data from the endpoint. |
| void | [usb\_transfer\_ep\_callback](group____usb__device__core__api.md#ga3485c3d1c3fa7259de32fd57d303bc77) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, enum [usb\_dc\_ep\_cb\_status\_code](group____usb__device__controller__api.md#gaf7f083f61e1406e7d41513113dccd3bd)) |
|  | Transfer management endpoint callback. |
| int | [usb\_transfer](group____usb__device__core__api.md#ga27c3040dca474b5b45e6bea63a500cce) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) dlen, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [usb\_transfer\_callback](group____usb__device__core__api.md#ga2e599eb20f647d9bb2369d76a7dc51db) cb, void \*priv) |
|  | Start a transfer. |
| int | [usb\_transfer\_sync](group____usb__device__core__api.md#ga1060e3a473a7f0bc71763a413e91ab56) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) dlen, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Start a transfer and block-wait for completion. |
| void | [usb\_cancel\_transfer](group____usb__device__core__api.md#gab399dc4a43a99c927ee7588a57c49211) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Cancel any ongoing transfer on the specified endpoint. |
| void | [usb\_cancel\_transfers](group____usb__device__core__api.md#ga758a63b22c48d2ae9d025adb92ed5925) (void) |
|  | Cancel all ongoing transfers. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [usb\_transfer\_is\_busy](group____usb__device__core__api.md#ga6292a473cffc1f8683da902c2a85d653) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Check that transfer is ongoing for the endpoint. |
| int | [usb\_wakeup\_request](group____usb__device__core__api.md#ga7d67c8d49b52fb33818d654ca647c1e5) (void) |
|  | Start the USB remote wakeup procedure. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [usb\_get\_remote\_wakeup\_status](group____usb__device__core__api.md#ga577018c415eec38ef5038cdb2f45ed2f) (void) |
|  | Get status of the USB remote wakeup feature. |

## Detailed Description

USB device core layer APIs and structures.

This file contains the USB device core layer APIs and structures.

## Macro Definition Documentation

## [◆ ](#a3d01cf3cbbd08db3d6cfcfb45062b961)USB\_MAX\_CTRL\_MPS

| #define USB\_MAX\_CTRL\_MPS   64 |
| --- |

maximum packet size (MPS) for EP 0

## [◆ ](#a07bbd07466b47a0c498f26e25932392f)USB\_MAX\_FS\_BULK\_MPS

| #define USB\_MAX\_FS\_BULK\_MPS   64 |
| --- |

full speed MPS for bulk EP

## [◆ ](#ae88dc2d0b2a21779d8c353cd63ae3455)USB\_MAX\_FS\_INT\_MPS

| #define USB\_MAX\_FS\_INT\_MPS   64 |
| --- |

full speed MPS for interrupt EP

## [◆ ](#ae45dfb00deef73b2a142576bf136b062)USB\_MAX\_FS\_ISO\_MPS

| #define USB\_MAX\_FS\_ISO\_MPS   1023 |
| --- |

full speed MPS for isochronous EP

## [◆ ](#a99b3c84f3988ccf277e41b3c52c4a51a)USBD\_CFG\_DATA\_DEFINE

| #define USBD\_CFG\_DATA\_DEFINE | ( |  | *p*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

**Value:**

\_\_DEPRECATED\_MACRO \

static \_\_in\_section(\_usb\_cfg\_data, static, p##\_name) \_\_used \_\_aligned(4)

## [◆ ](#a9403c2bd43e638b4d5634288dfb6574b)USBD\_CLASS\_DESCR\_DEFINE

| #define USBD\_CLASS\_DESCR\_DEFINE | ( |  | *p*, |
| --- | --- | --- | --- |
|  |  |  | *instance* ) |

**Value:**

static \_\_in\_section(usb, descriptor\_##p.1, instance) \_\_used \_\_aligned(1)

## [◆ ](#a5db8e2eb30dd2afc51dbb9e08fbc07c6)USBD\_DEFINE\_CFG\_DATA

| #define USBD\_DEFINE\_CFG\_DATA | ( |  | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

static [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([usb\_cfg\_data](structusb__cfg__data.md), name)

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

[usb\_cfg\_data](structusb__cfg__data.md)

USB device configuration.

**Definition** usb\_device.h:175

## [◆ ](#a95efe03ee4bbfa4d9b0c3932b8ddfe31)USBD\_DEVICE\_DESCR\_DEFINE

| #define USBD\_DEVICE\_DESCR\_DEFINE | ( |  | *p* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

static \_\_in\_section(usb, descriptor\_##p, 0) \_\_used \_\_aligned(1)

## [◆ ](#a6ff803fe6831ca99e3e9543dd1d2f37d)USBD\_MISC\_DESCR\_DEFINE

| #define USBD\_MISC\_DESCR\_DEFINE | ( |  | *p* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

static \_\_in\_section(usb, descriptor\_##p, 2) \_\_used \_\_aligned(1)

## [◆ ](#acb8451e935bab6c8fe2f7eea97a8ae6f)USBD\_STRING\_DESCR\_DEFINE

| #define USBD\_STRING\_DESCR\_DEFINE | ( |  | *p* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

static \_\_in\_section(usb, descriptor\_##p, 4) \_\_used \_\_aligned(1)

## [◆ ](#a5bc3e0d5484c0c54e5996d99ebedc51b)USBD\_STRING\_DESCR\_USER\_DEFINE

| #define USBD\_STRING\_DESCR\_USER\_DEFINE | ( |  | *p* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

static \_\_in\_section(usb, descriptor\_##p, 5) \_\_used \_\_aligned(1)

## [◆ ](#a2ad0dd7628d3038c32809e6850baf23f)USBD\_TERM\_DESCR\_DEFINE

| #define USBD\_TERM\_DESCR\_DEFINE | ( |  | *p* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

static \_\_in\_section(usb, descriptor\_##p, 6) \_\_used \_\_aligned(1)

## [◆ ](#a76a98dcc6ca0284195d61bb928197e38)USBD\_USER\_DESCR\_DEFINE

| #define USBD\_USER\_DESCR\_DEFINE | ( |  | *p* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

static \_\_in\_section(usb, descriptor\_##p, 3) \_\_used \_\_aligned(1)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [usb](dir_d8285a9da4e2f530d10dd4c17d446a84.md)
- [usb\_device.h](usb__device_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
