---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__usbd__api.html
original_path: doxygen/html/group__usbd__api.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

USB device core API

[Connectivity](group__connectivity.md) » [USB](group__usb.md)

New USB device stack core API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [usbd\_desc\_node](structusbd__desc__node.md) |
|  | Descriptor node. [More...](structusbd__desc__node.md#details) |
| struct | [usbd\_config\_node](structusbd__config__node.md) |
|  | Device configuration node. [More...](structusbd__config__node.md#details) |
| struct | [usbd\_ch9\_data](structusbd__ch9__data.md) |
|  | USB device support middle layer runtime data. [More...](structusbd__ch9__data.md#details) |
| struct | [usbd\_status](structusbd__status.md) |
|  | USB device support status. [More...](structusbd__status.md#details) |
| struct | [usbd\_contex](structusbd__contex.md) |
|  | USB device support runtime context. [More...](structusbd__contex.md#details) |
| struct | [usbd\_cctx\_vendor\_req](structusbd__cctx__vendor__req.md) |
|  | Vendor Requests Table. [More...](structusbd__cctx__vendor__req.md#details) |
| struct | [usbd\_class\_api](structusbd__class__api.md) |
|  | USB device support class instance API. [More...](structusbd__class__api.md#details) |
| struct | [usbd\_class\_data](structusbd__class__data.md) |
|  | USB device support class data. [More...](structusbd__class__data.md#details) |
| struct | [usbd\_class\_node](structusbd__class__node.md) |

| Macros | |
| --- | --- |
| #define | [USB\_BSTRING\_LENGTH](#gac3d58cfa3f92b1811e9ed136c4450906)([s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)) |
| #define | [USB\_STRING\_DESCRIPTOR\_LENGTH](#gaef85e50556291fa93cbf72b01529b4a8)([s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)) |
| #define | [USBD\_NUMOF\_INTERFACES\_MAX](#gaf8aadd499f7e0438acac4a7f36645d49)   16U |
| #define | [USBD\_CCTX\_REGISTERED](#ga588b9e156a49d3b0358bee185cdeebee)   0 |
|  | USB Class instance registered flag. |
| #define | [USBD\_DEVICE\_DEFINE](#gaa202fc8ae1e5585abedbde733e63ccb7)(device\_name, uhc\_dev, vid, pid) |
| #define | [USBD\_CONFIGURATION\_DEFINE](#ga5db99c7ff31ff9ef893f219d209128c7)(name, attrib, power) |
| #define | [USBD\_DESC\_LANG\_DEFINE](#gaec816a27118bcb289ab4840fcd22888e)(name) |
|  | Create a string descriptor node and language string descriptor. |
| #define | [USBD\_DESC\_STRING\_DEFINE](#gaf800e2040ac30844cab463c13d1fcdf8)(d\_name, d\_string, d\_utype) |
| #define | [USBD\_DESC\_MANUFACTURER\_DEFINE](#ga18b1321daf1173a3cb0bc61a0d9beb34)(d\_name, d\_string) |
|  | Create a string descriptor node and manufacturer string descriptor. |
| #define | [USBD\_DESC\_PRODUCT\_DEFINE](#gaa5e43f9eac8f91d3896ea5e19baed031)(d\_name, d\_string) |
|  | Create a string descriptor node and product string descriptor. |
| #define | [USBD\_DESC\_SERIAL\_NUMBER\_DEFINE](#ga98e3b788b4bc38d0ac199a67fdc302d0)(d\_name, d\_string) |
|  | Create a string descriptor node and serial number string descriptor. |
| #define | [USBD\_DEFINE\_CLASS](#gaab136394168b115c0e061261651c4146)(class\_name, class\_api, class\_data) |
| #define | [VENDOR\_REQ\_DEFINE](#ga54ca08c74ae715281381d878f828727e)(\_reqs, \_len) |
|  | Helper to declare request table of [usbd\_cctx\_vendor\_req](structusbd__cctx__vendor__req.md "Vendor Requests Table."). |
| #define | [USBD\_VENDOR\_REQ](#ga464933a8332c11d15c92914aa1790e10)(\_reqs...) |
|  | Helper to declare supported vendor requests. |

| Enumerations | |
| --- | --- |
| enum | [usbd\_desc\_usage\_type](#gaa7ed6f04fd7058c422f5ebc378f1a3da) {     [USBD\_DUT\_STRING\_LANG](#ggaa7ed6f04fd7058c422f5ebc378f1a3daa984cc2f845e2e2bcc83d2e9f0138e3bd) , [USBD\_DUT\_STRING\_MANUFACTURER](#ggaa7ed6f04fd7058c422f5ebc378f1a3daa25eb10630b10db28f9f97aa0b81f3c4e) , [USBD\_DUT\_STRING\_PRODUCT](#ggaa7ed6f04fd7058c422f5ebc378f1a3daa67c8a16639167a0a7a6f615d5aa6b73e) , [USBD\_DUT\_STRING\_SERIAL\_NUMBER](#ggaa7ed6f04fd7058c422f5ebc378f1a3daac4fff2e4994a473899aea6ed8a0ec782) ,     [USBD\_DUT\_STRING\_INTERFACE](#ggaa7ed6f04fd7058c422f5ebc378f1a3daaa4dd69c222492b1f12b3993c4640c80d)   } |
| enum | [usbd\_ch9\_state](#ga95fb708d8a54eaa3ce0acc4e65519bbc) { [USBD\_STATE\_DEFAULT](#gga95fb708d8a54eaa3ce0acc4e65519bbca978c707d313eb49b70bc62dfae304048) = 0 , [USBD\_STATE\_ADDRESS](#gga95fb708d8a54eaa3ce0acc4e65519bbca985f06c5505c5684a98954f15701cc9d) , [USBD\_STATE\_CONFIGURED](#gga95fb708d8a54eaa3ce0acc4e65519bbca44c1920b09ea1062ea4d7ac31a846509) } |
|  | USB device support middle layer runtime state. [More...](#ga95fb708d8a54eaa3ce0acc4e65519bbc) |

| Functions | |
| --- | --- |
| int | [usbd\_add\_descriptor](#ga0280dbaf6f15e4bc789279b8d93bfff8) (struct [usbd\_contex](structusbd__contex.md) \*uds\_ctx, struct [usbd\_desc\_node](structusbd__desc__node.md) \*dn) |
|  | Add common USB descriptor. |
| int | [usbd\_add\_configuration](#gae1472960a22e84a49865639dff5816a0) (struct [usbd\_contex](structusbd__contex.md) \*uds\_ctx, struct [usbd\_config\_node](structusbd__config__node.md) \*cd) |
|  | Add a USB device configuration. |
| int | [usbd\_register\_class](#ga3640cb8425961a8038c225e1daea34a3) (struct [usbd\_contex](structusbd__contex.md) \*uds\_ctx, const char \*name, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cfg) |
|  | Register an USB class instance. |
| int | [usbd\_unregister\_class](#gadf7cc0edc2d046f0b50e65fcc007f982) (struct [usbd\_contex](structusbd__contex.md) \*uds\_ctx, const char \*name, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cfg) |
|  | Unregister an USB class instance. |
| int | [usbd\_init](#gaf3cd6c12317f9d94ee98f2809d2a0e04) (struct [usbd\_contex](structusbd__contex.md) \*uds\_ctx) |
|  | Initialize USB device. |
| int | [usbd\_enable](#gaa7ee71917824e90177f61a86eb992817) (struct [usbd\_contex](structusbd__contex.md) \*uds\_ctx) |
|  | Enable the USB device support and registered class instances. |
| int | [usbd\_disable](#gaa3112af9fb2f5f1ee55cc71a64c6e369) (struct [usbd\_contex](structusbd__contex.md) \*uds\_ctx) |
|  | Disable the USB device support. |
| int | [usbd\_shutdown](#gaa7656f656182e727531e531344c960df) (struct [usbd\_contex](structusbd__contex.md) \*const uds\_ctx) |
|  | Shutdown the USB device support. |
| int | [usbd\_ep\_set\_halt](#ga0730043c2fd89b56db6e7457b639968d) (struct [usbd\_contex](structusbd__contex.md) \*uds\_ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Halt endpoint. |
| int | [usbd\_ep\_clear\_halt](#ga197697880c7c625ea212893b2fe7ef8b) (struct [usbd\_contex](structusbd__contex.md) \*uds\_ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Clear endpoint halt. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [usbd\_ep\_is\_halted](#ga9292b393ef17fd61ea42b2f28fdd57ee) (struct [usbd\_contex](structusbd__contex.md) \*uds\_ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Checks whether the endpoint is halted. |
| struct [net\_buf](structnet__buf.md) \* | [usbd\_ep\_ctrl\_buf\_alloc](#ga59b0cb83b05e0a44db9c6a36171d524f) (struct [usbd\_contex](structusbd__contex.md) \*const uds\_ctx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, const [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Allocate buffer for USB device control request. |
| struct [net\_buf](structnet__buf.md) \* | [usbd\_ep\_buf\_alloc](#ga940f38e4db1dfc7ba6514ecf95dc9e5b) (const struct [usbd\_class\_node](structusbd__class__node.md) \*const c\_nd, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, const [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Allocate buffer for USB device request. |
| int | [usbd\_ep\_ctrl\_enqueue](#ga52acb4fb74e3737b446b6704c6925d70) (struct [usbd\_contex](structusbd__contex.md) \*const uds\_ctx, struct [net\_buf](structnet__buf.md) \*const buf) |
|  | Queue USB device control request. |
| int | [usbd\_ep\_enqueue](#ga19ecdc00918dbec14fdbcf847b6f4dce) (const struct [usbd\_class\_node](structusbd__class__node.md) \*const c\_nd, struct [net\_buf](structnet__buf.md) \*const buf) |
|  | Queue USB device request. |
| int | [usbd\_ep\_dequeue](#ga0d1d7f59822674c201147b50a1dbdb96) (struct [usbd\_contex](structusbd__contex.md) \*uds\_ctx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Remove all USB device controller requests from endpoint queue. |
| int | [usbd\_ep\_buf\_free](#ga2bfd230a2e0b74954ebce112816e6193) (struct [usbd\_contex](structusbd__contex.md) \*uds\_ctx, struct [net\_buf](structnet__buf.md) \*buf) |
|  | Free USB device request buffer. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [usbd\_is\_suspended](#ga832e3147aba9297bad263b2a3817e1e4) (struct [usbd\_contex](structusbd__contex.md) \*uds\_ctx) |
|  | Checks whether the USB device controller is suspended. |
| int | [usbd\_wakeup\_request](#ga4d440313da931d4504919b8fe2783419) (struct [usbd\_contex](structusbd__contex.md) \*uds\_ctx) |
|  | Initiate the USB remote wakeup (TBD). |
| int | [usbd\_device\_set\_bcd](#gaa191663f3703bd631e51009adbc22d87) (struct [usbd\_contex](structusbd__contex.md) \*const uds\_ctx, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bcd) |
|  | Set USB device descriptor value bcdUSB. |
| int | [usbd\_device\_set\_vid](#ga791a561a3d96698a1a7337723adc8e53) (struct [usbd\_contex](structusbd__contex.md) \*const uds\_ctx, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vid) |
|  | Set USB device descriptor value idVendor. |
| int | [usbd\_device\_set\_pid](#gad3612c1c4276783df11b144e72662306) (struct [usbd\_contex](structusbd__contex.md) \*const uds\_ctx, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) pid) |
|  | Set USB device descriptor value idProduct. |
| int | [usbd\_device\_set\_code\_triple](#gad8d784ae06463afe51f312dad8a4718d) (struct [usbd\_contex](structusbd__contex.md) \*const uds\_ctx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) base\_class, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) subclass, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) protocol) |
|  | Set USB device descriptor code triple Base Class, SubClass, and Protocol. |
| int | [usbd\_config\_attrib\_rwup](#ga6488af53f4ed5355406ef319a8d1b195) (struct [usbd\_contex](structusbd__contex.md) \*const uds\_ctx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cfg, const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Setup USB device configuration attribute Remote Wakeup. |
| int | [usbd\_config\_attrib\_self](#ga7c8dd76553545c77ff6e0f4c41d33357) (struct [usbd\_contex](structusbd__contex.md) \*const uds\_ctx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cfg, const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Setup USB device configuration attribute Self-powered. |
| int | [usbd\_config\_maxpower](#gac907ba549e8d799a328cc992d76e3825) (struct [usbd\_contex](structusbd__contex.md) \*const uds\_ctx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cfg, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) power) |
|  | Setup USB device configuration power consumption. |

## Detailed Description

New USB device stack core API.

## Macro Definition Documentation

## [◆ ](#gac3d58cfa3f92b1811e9ed136c4450906)USB\_BSTRING\_LENGTH

| #define USB\_BSTRING\_LENGTH | ( |  | *[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbd.h](usbd_8h.md)>`

**Value:**

(sizeof([s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)) \* 2 - 2)

[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)

irp nz macro MOVR cc s mov cc s endm endr irp aw macro LDR aa s

**Definition** asm-macro-32-bit-gnu.h:17

## [◆ ](#gaef85e50556291fa93cbf72b01529b4a8)USB\_STRING\_DESCRIPTOR\_LENGTH

| #define USB\_STRING\_DESCRIPTOR\_LENGTH | ( |  | *[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbd.h](usbd_8h.md)>`

**Value:**

(sizeof([s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)) \* 2)

## [◆ ](#ga588b9e156a49d3b0358bee185cdeebee)USBD\_CCTX\_REGISTERED

| #define USBD\_CCTX\_REGISTERED   0 |
| --- |

`#include <[usbd.h](usbd_8h.md)>`

USB Class instance registered flag.

## [◆ ](#ga5db99c7ff31ff9ef893f219d209128c7)USBD\_CONFIGURATION\_DEFINE

| #define USBD\_CONFIGURATION\_DEFINE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *attrib*, |
|  |  |  | *power* ) |

`#include <[usbd.h](usbd_8h.md)>`

**Value:**

static struct [usb\_cfg\_descriptor](structusb__cfg__descriptor.md) \

cfg\_desc\_##name = { \

.bLength = sizeof(struct [usb\_cfg\_descriptor](structusb__cfg__descriptor.md)), \

.bDescriptorType = [USB\_DESC\_CONFIGURATION](usb__ch9_8h.md#a7764131f2e59070eb032bd9d68d32620), \

.wTotalLength = 0, \

.bNumInterfaces = 0, \

.bConfigurationValue = 1, \

.iConfiguration = 0, \

.bmAttributes = [USB\_SCD\_RESERVED](usb__ch9_8h.md#a2a8b7c42705cd1e0fd0aecb0028cb2ba) | (attrib), \

.bMaxPower = (power), \

}; \

BUILD\_ASSERT((power) < 256, "Too much power"); \

static struct [usbd\_config\_node](structusbd__config__node.md) name = { \

.desc = &cfg\_desc\_##name, \

}

[usb\_cfg\_descriptor](structusb__cfg__descriptor.md)

USB Standard Configuration Descriptor defined in spec.

**Definition** usb\_ch9.h:167

[usbd\_config\_node](structusbd__config__node.md)

Device configuration node.

**Definition** usbd.h:98

[USB\_SCD\_RESERVED](usb__ch9_8h.md#a2a8b7c42705cd1e0fd0aecb0028cb2ba)

#define USB\_SCD\_RESERVED

USB Standard Configuration Descriptor Characteristics from Table 9-10.

**Definition** usb\_ch9.h:238

[USB\_DESC\_CONFIGURATION](usb__ch9_8h.md#a7764131f2e59070eb032bd9d68d32620)

#define USB\_DESC\_CONFIGURATION

**Definition** usb\_ch9.h:110

## [◆ ](#gaab136394168b115c0e061261651c4146)USBD\_DEFINE\_CLASS

| #define USBD\_DEFINE\_CLASS | ( |  | *class\_name*, |
| --- | --- | --- | --- |
|  |  |  | *class\_api*, |
|  |  |  | *class\_data* ) |

`#include <[usbd.h](usbd_8h.md)>`

**Value:**

static [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([usbd\_class\_node](structusbd__class__node.md), class\_name) = { \

.name = [STRINGIFY](common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(class\_name), \

.api = class\_api, \

.data = class\_data, \

}

[STRINGIFY](common_8h.md#a4689212d5a549893cabb9d7782eecfb6)

#define STRINGIFY(s)

**Definition** common.h:134

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

[usbd\_class\_node](structusbd__class__node.md)

**Definition** usbd.h:273

## [◆ ](#gaec816a27118bcb289ab4840fcd22888e)USBD\_DESC\_LANG\_DEFINE

| #define USBD\_DESC\_LANG\_DEFINE | ( |  | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbd.h](usbd_8h.md)>`

**Value:**

static struct [usb\_string\_descriptor](structusb__string__descriptor.md) \

string\_desc\_##name = { \

.bLength = sizeof(struct [usb\_string\_descriptor](structusb__string__descriptor.md)), \

.bDescriptorType = [USB\_DESC\_STRING](usb__ch9_8h.md#a6a5678b964f3a9b4ba2f52e9a51bebf5), \

.bString = [sys\_cpu\_to\_le16](sys_2byteorder_8h.md#ae7f653c0bca81809b53d8a91854ca4c9)(0x0409), \

}; \

static struct [usbd\_desc\_node](structusbd__desc__node.md) name = { \

.idx = 0, \

.utype = [USBD\_DUT\_STRING\_LANG](#ggaa7ed6f04fd7058c422f5ebc378f1a3daa984cc2f845e2e2bcc83d2e9f0138e3bd), \

.desc = &string\_desc\_##name, \

}

[USBD\_DUT\_STRING\_LANG](#ggaa7ed6f04fd7058c422f5ebc378f1a3daa984cc2f845e2e2bcc83d2e9f0138e3bd)

@ USBD\_DUT\_STRING\_LANG

**Definition** usbd.h:62

[usb\_string\_descriptor](structusb__string__descriptor.md)

USB Unicode (UTF16LE) String Descriptor defined in spec.

**Definition** usb\_ch9.h:219

[usbd\_desc\_node](structusbd__desc__node.md)

Descriptor node.

**Definition** usbd.h:75

[sys\_cpu\_to\_le16](sys_2byteorder_8h.md#ae7f653c0bca81809b53d8a91854ca4c9)

#define sys\_cpu\_to\_le16(val)

Convert 16-bit integer from host endianness to little-endian.

**Definition** byteorder.h:257

[USB\_DESC\_STRING](usb__ch9_8h.md#a6a5678b964f3a9b4ba2f52e9a51bebf5)

#define USB\_DESC\_STRING

**Definition** usb\_ch9.h:111

Create a string descriptor node and language string descriptor.

This macro defines a descriptor node and a string descriptor that, when added to the device context, is automatically used as the language string descriptor zero. Both descriptor node and descriptor are defined with static-storage-class specifier. Default and currently only supported language ID is 0x0409 English (United States). If string descriptors are used, it is necessary to add this descriptor as the first one to the USB device context.

Parameters
:   | name | Language string descriptor node identifier. |
    | --- | --- |

## [◆ ](#ga18b1321daf1173a3cb0bc61a0d9beb34)USBD\_DESC\_MANUFACTURER\_DEFINE

| #define USBD\_DESC\_MANUFACTURER\_DEFINE | ( |  | *d\_name*, |
| --- | --- | --- | --- |
|  |  |  | *d\_string* ) |

`#include <[usbd.h](usbd_8h.md)>`

**Value:**

[USBD\_DESC\_STRING\_DEFINE](#gaf800e2040ac30844cab463c13d1fcdf8)(d\_name, d\_string, [USBD\_DUT\_STRING\_MANUFACTURER](#ggaa7ed6f04fd7058c422f5ebc378f1a3daa25eb10630b10db28f9f97aa0b81f3c4e))

[USBD\_DESC\_STRING\_DEFINE](#gaf800e2040ac30844cab463c13d1fcdf8)

#define USBD\_DESC\_STRING\_DEFINE(d\_name, d\_string, d\_utype)

**Definition** usbd.h:351

[USBD\_DUT\_STRING\_MANUFACTURER](#ggaa7ed6f04fd7058c422f5ebc378f1a3daa25eb10630b10db28f9f97aa0b81f3c4e)

@ USBD\_DUT\_STRING\_MANUFACTURER

**Definition** usbd.h:63

Create a string descriptor node and manufacturer string descriptor.

This macro defines a descriptor node and a string descriptor that, when added to the device context, is automatically used as the manufacturer string descriptor. Both descriptor node and descriptor are defined with static-storage-class specifier.

Parameters
:   | d\_name | String descriptor node identifier. |
    | --- | --- |
    | d\_string | ASCII7 encoded manufacturer string literal |

## [◆ ](#gaa5e43f9eac8f91d3896ea5e19baed031)USBD\_DESC\_PRODUCT\_DEFINE

| #define USBD\_DESC\_PRODUCT\_DEFINE | ( |  | *d\_name*, |
| --- | --- | --- | --- |
|  |  |  | *d\_string* ) |

`#include <[usbd.h](usbd_8h.md)>`

**Value:**

[USBD\_DESC\_STRING\_DEFINE](#gaf800e2040ac30844cab463c13d1fcdf8)(d\_name, d\_string, [USBD\_DUT\_STRING\_PRODUCT](#ggaa7ed6f04fd7058c422f5ebc378f1a3daa67c8a16639167a0a7a6f615d5aa6b73e))

[USBD\_DUT\_STRING\_PRODUCT](#ggaa7ed6f04fd7058c422f5ebc378f1a3daa67c8a16639167a0a7a6f615d5aa6b73e)

@ USBD\_DUT\_STRING\_PRODUCT

**Definition** usbd.h:64

Create a string descriptor node and product string descriptor.

This macro defines a descriptor node and a string descriptor that, when added to the device context, is automatically used as the product string descriptor. Both descriptor node and descriptor are defined with static-storage-class specifier.

Parameters
:   | d\_name | String descriptor node identifier. |
    | --- | --- |
    | d\_string | ASCII7 encoded product string literal |

## [◆ ](#ga98e3b788b4bc38d0ac199a67fdc302d0)USBD\_DESC\_SERIAL\_NUMBER\_DEFINE

| #define USBD\_DESC\_SERIAL\_NUMBER\_DEFINE | ( |  | *d\_name*, |
| --- | --- | --- | --- |
|  |  |  | *d\_string* ) |

`#include <[usbd.h](usbd_8h.md)>`

**Value:**

[USBD\_DESC\_STRING\_DEFINE](#gaf800e2040ac30844cab463c13d1fcdf8)(d\_name, d\_string, [USBD\_DUT\_STRING\_SERIAL\_NUMBER](#ggaa7ed6f04fd7058c422f5ebc378f1a3daac4fff2e4994a473899aea6ed8a0ec782))

[USBD\_DUT\_STRING\_SERIAL\_NUMBER](#ggaa7ed6f04fd7058c422f5ebc378f1a3daac4fff2e4994a473899aea6ed8a0ec782)

@ USBD\_DUT\_STRING\_SERIAL\_NUMBER

**Definition** usbd.h:65

Create a string descriptor node and serial number string descriptor.

This macro defines a descriptor node and a string descriptor that, when added to the device context, is automatically used as the serial number string descriptor. The string literal parameter is used as a placeholder, the unique number is obtained from hwinfo. Both descriptor node and descriptor are defined with static-storage-class specifier.

Parameters
:   | d\_name | String descriptor node identifier. |
    | --- | --- |
    | d\_string | ASCII7 encoded serial number string literal placeholder |

## [◆ ](#gaf800e2040ac30844cab463c13d1fcdf8)USBD\_DESC\_STRING\_DEFINE

| #define USBD\_DESC\_STRING\_DEFINE | ( |  | *d\_name*, |
| --- | --- | --- | --- |
|  |  |  | *d\_string*, |
|  |  |  | *d\_utype* ) |

`#include <[usbd.h](usbd_8h.md)>`

**Value:**

struct usb\_string\_descriptor\_##d\_name { \

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bLength; \

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bDescriptorType; \

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bString[[USB\_BSTRING\_LENGTH](#gac3d58cfa3f92b1811e9ed136c4450906)(d\_string)]; \

} \_\_packed; \

static struct usb\_string\_descriptor\_##d\_name \

string\_desc\_##d\_name = { \

.bLength = [USB\_STRING\_DESCRIPTOR\_LENGTH](#gaef85e50556291fa93cbf72b01529b4a8)(d\_string), \

.bDescriptorType = [USB\_DESC\_STRING](usb__ch9_8h.md#a6a5678b964f3a9b4ba2f52e9a51bebf5), \

.bString = d\_string, \

}; \

static struct usbd\_desc\_node d\_name = { \

.utype = d\_utype, \

.desc = &string\_desc\_##d\_name, \

}

[USB\_BSTRING\_LENGTH](#gac3d58cfa3f92b1811e9ed136c4450906)

#define USB\_BSTRING\_LENGTH(s)

**Definition** usbd.h:46

[USB\_STRING\_DESCRIPTOR\_LENGTH](#gaef85e50556291fa93cbf72b01529b4a8)

#define USB\_STRING\_DESCRIPTOR\_LENGTH(s)

**Definition** usbd.h:58

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

## [◆ ](#gaa202fc8ae1e5585abedbde733e63ccb7)USBD\_DEVICE\_DEFINE

| #define USBD\_DEVICE\_DEFINE | ( |  | *device\_name*, |
| --- | --- | --- | --- |
|  |  |  | *uhc\_dev*, |
|  |  |  | *vid*, |
|  |  |  | *pid* ) |

`#include <[usbd.h](usbd_8h.md)>`

**Value:**

static struct [usb\_device\_descriptor](structusb__device__descriptor.md) \

desc\_##device\_name = { \

.bLength = sizeof(struct [usb\_device\_descriptor](structusb__device__descriptor.md)), \

.bDescriptorType = [USB\_DESC\_DEVICE](usb__ch9_8h.md#aefeff68c3a236749d1105d94ed9bad68), \

.bcdUSB = [sys\_cpu\_to\_le16](sys_2byteorder_8h.md#ae7f653c0bca81809b53d8a91854ca4c9)([USB\_SRN\_2\_0](usb__ch9_8h.md#a14527f51ba0e1634b3b477c80e7ae31f)), \

.bDeviceClass = [USB\_BCC\_MISCELLANEOUS](usb__ch9_8h.md#a62bf5e94c7c36c9d1d94438d7a12a482), \

.bDeviceSubClass = 2, \

.bDeviceProtocol = 1, \

.bMaxPacketSize0 = [USB\_CONTROL\_EP\_MPS](usb__ch9_8h.md#a8c4dd61ae766f50c9398c9753b4156b5), \

.idVendor = vid, \

.idProduct = pid, \

.bcdDevice = [sys\_cpu\_to\_le16](sys_2byteorder_8h.md#ae7f653c0bca81809b53d8a91854ca4c9)([USB\_BCD\_DRN](usb__ch9_8h.md#a2f6e90e87d7a1d53418ce084a293e6fc)), \

.iManufacturer = 0, \

.iProduct = 0, \

.iSerialNumber = 0, \

.bNumConfigurations = 0, \

}; \

static [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([usbd\_contex](structusbd__contex.md), device\_name) = { \

.name = [STRINGIFY](common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(device\_name), \

.dev = uhc\_dev, \

.desc = &desc\_##device\_name, \

}

[usb\_device\_descriptor](structusb__device__descriptor.md)

USB Standard Device Descriptor defined in spec.

**Definition** usb\_ch9.h:149

[usbd\_contex](structusbd__contex.md)

USB device support runtime context.

**Definition** usbd.h:163

[USB\_SRN\_2\_0](usb__ch9_8h.md#a14527f51ba0e1634b3b477c80e7ae31f)

#define USB\_SRN\_2\_0

**Definition** usb\_ch9.h:256

[USB\_BCD\_DRN](usb__ch9_8h.md#a2f6e90e87d7a1d53418ce084a293e6fc)

#define USB\_BCD\_DRN

USB Device release number (bcdDevice Descriptor field).

**Definition** usb\_ch9.h:262

[USB\_BCC\_MISCELLANEOUS](usb__ch9_8h.md#a62bf5e94c7c36c9d1d94438d7a12a482)

#define USB\_BCC\_MISCELLANEOUS

**Definition** usb\_ch9.h:250

[USB\_CONTROL\_EP\_MPS](usb__ch9_8h.md#a8c4dd61ae766f50c9398c9753b4156b5)

#define USB\_CONTROL\_EP\_MPS

USB Control Endpoints maximum packet size (MPS).

**Definition** usb\_ch9.h:272

[USB\_DESC\_DEVICE](usb__ch9_8h.md#aefeff68c3a236749d1105d94ed9bad68)

#define USB\_DESC\_DEVICE

Descriptor Types defined in spec.

**Definition** usb\_ch9.h:109

## [◆ ](#gaf8aadd499f7e0438acac4a7f36645d49)USBD\_NUMOF\_INTERFACES\_MAX

| #define USBD\_NUMOF\_INTERFACES\_MAX   16U |
| --- |

`#include <[usbd.h](usbd_8h.md)>`

## [◆ ](#ga464933a8332c11d15c92914aa1790e10)USBD\_VENDOR\_REQ

| #define USBD\_VENDOR\_REQ | ( |  | *\_reqs...* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbd.h](usbd_8h.md)>`

**Value:**

[VENDOR\_REQ\_DEFINE](#ga54ca08c74ae715281381d878f828727e)((([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) []) { \_reqs }), \

sizeof(([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) []) { \_reqs }))

[VENDOR\_REQ\_DEFINE](#ga54ca08c74ae715281381d878f828727e)

#define VENDOR\_REQ\_DEFINE(\_reqs, \_len)

Helper to declare request table of usbd\_cctx\_vendor\_req.

**Definition** usbd.h:423

Helper to declare supported vendor requests.

Parameters
:   | \_reqs | Variable number of vendor requests |
    | --- | --- |

## [◆ ](#ga54ca08c74ae715281381d878f828727e)VENDOR\_REQ\_DEFINE

| #define VENDOR\_REQ\_DEFINE | ( |  | *\_reqs*, |
| --- | --- | --- | --- |
|  |  |  | *\_len* ) |

`#include <[usbd.h](usbd_8h.md)>`

**Value:**

{ \

.reqs = (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)(\_reqs), \

.len = (\_len), \

}

Helper to declare request table of [usbd\_cctx\_vendor\_req](structusbd__cctx__vendor__req.md "Vendor Requests Table.").

Parameters
:   | \_reqs | Pointer to the vendor request field |
    | --- | --- |
    | \_len | Number of supported vendor requests |

## Enumeration Type Documentation

## [◆ ](#ga95fb708d8a54eaa3ce0acc4e65519bbc)usbd\_ch9\_state

| enum [usbd\_ch9\_state](#ga95fb708d8a54eaa3ce0acc4e65519bbc) |
| --- |

`#include <[usbd.h](usbd_8h.md)>`

USB device support middle layer runtime state.

Part of USB device states without suspended and powered states, as it is better to track them separately.

| Enumerator | |
| --- | --- |
| USBD\_STATE\_DEFAULT |  |
| USBD\_STATE\_ADDRESS |  |
| USBD\_STATE\_CONFIGURED |  |

## [◆ ](#gaa7ed6f04fd7058c422f5ebc378f1a3da)usbd\_desc\_usage\_type

| enum [usbd\_desc\_usage\_type](#gaa7ed6f04fd7058c422f5ebc378f1a3da) |
| --- |

`#include <[usbd.h](usbd_8h.md)>`

| Enumerator | |
| --- | --- |
| USBD\_DUT\_STRING\_LANG |  |
| USBD\_DUT\_STRING\_MANUFACTURER |  |
| USBD\_DUT\_STRING\_PRODUCT |  |
| USBD\_DUT\_STRING\_SERIAL\_NUMBER |  |
| USBD\_DUT\_STRING\_INTERFACE |  |

## Function Documentation

## [◆ ](#gae1472960a22e84a49865639dff5816a0)usbd\_add\_configuration()

| int usbd\_add\_configuration | ( | struct [usbd\_contex](structusbd__contex.md) \* | *uds\_ctx*, |
| --- | --- | --- | --- |
|  |  | struct [usbd\_config\_node](structusbd__config__node.md) \* | *cd* ) |

`#include <[usbd.h](usbd_8h.md)>`

Add a USB device configuration.

Parameters
:   | [in] | uds\_ctx | Pointer to USB device support context |
    | --- | --- | --- |
    | [in] | cd | Pointer to USB configuration node |

Returns
:   0 on success, other values on fail.

## [◆ ](#ga0280dbaf6f15e4bc789279b8d93bfff8)usbd\_add\_descriptor()

| int usbd\_add\_descriptor | ( | struct [usbd\_contex](structusbd__contex.md) \* | *uds\_ctx*, |
| --- | --- | --- | --- |
|  |  | struct [usbd\_desc\_node](structusbd__desc__node.md) \* | *dn* ) |

`#include <[usbd.h](usbd_8h.md)>`

Add common USB descriptor.

Add common descriptor like string or bos.

Parameters
:   | [in] | uds\_ctx | Pointer to USB device support context |
    | --- | --- | --- |
    | [in] | dn | Pointer to USB descriptor node |

Returns
:   0 on success, other values on fail.

## [◆ ](#ga6488af53f4ed5355406ef319a8d1b195)usbd\_config\_attrib\_rwup()

| int usbd\_config\_attrib\_rwup | ( | struct [usbd\_contex](structusbd__contex.md) \*const | *uds\_ctx*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *cfg*, |
|  |  | const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* ) |

`#include <[usbd.h](usbd_8h.md)>`

Setup USB device configuration attribute Remote Wakeup.

Parameters
:   | [in] | uds\_ctx | Pointer to USB device support context |
    | --- | --- | --- |
    | [in] | cfg | Configuration number |
    | [in] | enable | Sets attribute if true, clears it otherwise |

Returns
:   0 on success, other values on fail.

## [◆ ](#ga7c8dd76553545c77ff6e0f4c41d33357)usbd\_config\_attrib\_self()

| int usbd\_config\_attrib\_self | ( | struct [usbd\_contex](structusbd__contex.md) \*const | *uds\_ctx*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *cfg*, |
|  |  | const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* ) |

`#include <[usbd.h](usbd_8h.md)>`

Setup USB device configuration attribute Self-powered.

Parameters
:   | [in] | uds\_ctx | Pointer to USB device support context |
    | --- | --- | --- |
    | [in] | cfg | Configuration number |
    | [in] | enable | Sets attribute if true, clears it otherwise |

Returns
:   0 on success, other values on fail.

## [◆ ](#gac907ba549e8d799a328cc992d76e3825)usbd\_config\_maxpower()

| int usbd\_config\_maxpower | ( | struct [usbd\_contex](structusbd__contex.md) \*const | *uds\_ctx*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *cfg*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *power* ) |

`#include <[usbd.h](usbd_8h.md)>`

Setup USB device configuration power consumption.

Parameters
:   | [in] | uds\_ctx | Pointer to USB device support context |
    | --- | --- | --- |
    | [in] | cfg | Configuration number |
    | [in] | power | Maximum power consumption value (bMaxPower) |

Returns
:   0 on success, other values on fail.

## [◆ ](#gaa191663f3703bd631e51009adbc22d87)usbd\_device\_set\_bcd()

| int usbd\_device\_set\_bcd | ( | struct [usbd\_contex](structusbd__contex.md) \*const | *uds\_ctx*, |
| --- | --- | --- | --- |
|  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *bcd* ) |

`#include <[usbd.h](usbd_8h.md)>`

Set USB device descriptor value bcdUSB.

Parameters
:   | [in] | uds\_ctx | Pointer to USB device support context |
    | --- | --- | --- |
    | [in] | bcd | bcdUSB value |

Returns
:   0 on success, other values on fail.

## [◆ ](#gad8d784ae06463afe51f312dad8a4718d)usbd\_device\_set\_code\_triple()

| int usbd\_device\_set\_code\_triple | ( | struct [usbd\_contex](structusbd__contex.md) \*const | *uds\_ctx*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *base\_class*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *subclass*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *protocol* ) |

`#include <[usbd.h](usbd_8h.md)>`

Set USB device descriptor code triple Base Class, SubClass, and Protocol.

Parameters
:   | [in] | uds\_ctx | Pointer to USB device support context |
    | --- | --- | --- |
    | [in] | base\_class | bDeviceClass value |
    | [in] | subclass | bDeviceSubClass value |
    | [in] | protocol | bDeviceProtocol value |

Returns
:   0 on success, other values on fail.

## [◆ ](#gad3612c1c4276783df11b144e72662306)usbd\_device\_set\_pid()

| int usbd\_device\_set\_pid | ( | struct [usbd\_contex](structusbd__contex.md) \*const | *uds\_ctx*, |
| --- | --- | --- | --- |
|  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *pid* ) |

`#include <[usbd.h](usbd_8h.md)>`

Set USB device descriptor value idProduct.

Parameters
:   | [in] | uds\_ctx | Pointer to USB device support context |
    | --- | --- | --- |
    | [in] | pid | idProduct value |

Returns
:   0 on success, other values on fail.

## [◆ ](#ga791a561a3d96698a1a7337723adc8e53)usbd\_device\_set\_vid()

| int usbd\_device\_set\_vid | ( | struct [usbd\_contex](structusbd__contex.md) \*const | *uds\_ctx*, |
| --- | --- | --- | --- |
|  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *vid* ) |

`#include <[usbd.h](usbd_8h.md)>`

Set USB device descriptor value idVendor.

Parameters
:   | [in] | uds\_ctx | Pointer to USB device support context |
    | --- | --- | --- |
    | [in] | vid | idVendor value |

Returns
:   0 on success, other values on fail.

## [◆ ](#gaa3112af9fb2f5f1ee55cc71a64c6e369)usbd\_disable()

| int usbd\_disable | ( | struct [usbd\_contex](structusbd__contex.md) \* | *uds\_ctx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbd.h](usbd_8h.md)>`

Disable the USB device support.

This function disables the USB device support.

Parameters
:   | [in] | uds\_ctx | Pointer to USB device support context |
    | --- | --- | --- |

Returns
:   0 on success, other values on fail.

## [◆ ](#gaa7ee71917824e90177f61a86eb992817)usbd\_enable()

| int usbd\_enable | ( | struct [usbd\_contex](structusbd__contex.md) \* | *uds\_ctx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbd.h](usbd_8h.md)>`

Enable the USB device support and registered class instances.

This function enables the USB device support.

Parameters
:   | [in] | uds\_ctx | Pointer to USB device support context |
    | --- | --- | --- |

Returns
:   0 on success, other values on fail.

## [◆ ](#ga940f38e4db1dfc7ba6514ecf95dc9e5b)usbd\_ep\_buf\_alloc()

| struct [net\_buf](structnet__buf.md) \* usbd\_ep\_buf\_alloc | ( | const struct [usbd\_class\_node](structusbd__class__node.md) \*const | *c\_nd*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ep*, |
|  |  | const [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[usbd.h](usbd_8h.md)>`

Allocate buffer for USB device request.

Allocate a new buffer from controller's driver buffer pool.

Parameters
:   | [in] | c\_nd | Pointer to USB device class node |
    | --- | --- | --- |
    | [in] | ep | Endpoint address |
    | [in] | size | Size of the request buffer |

Returns
:   pointer to allocated request or NULL on error.

## [◆ ](#ga2bfd230a2e0b74954ebce112816e6193)usbd\_ep\_buf\_free()

| int usbd\_ep\_buf\_free | ( | struct [usbd\_contex](structusbd__contex.md) \* | *uds\_ctx*, |
| --- | --- | --- | --- |
|  |  | struct [net\_buf](structnet__buf.md) \* | *buf* ) |

`#include <[usbd.h](usbd_8h.md)>`

Free USB device request buffer.

Put the buffer back into the request buffer pool.

Parameters
:   | [in] | uds\_ctx | Pointer to USB device support context |
    | --- | --- | --- |
    | [in] | buf | Pointer to UDC request buffer |

Returns
:   0 on success, all other values should be treated as error.

## [◆ ](#ga197697880c7c625ea212893b2fe7ef8b)usbd\_ep\_clear\_halt()

| int usbd\_ep\_clear\_halt | ( | struct [usbd\_contex](structusbd__contex.md) \* | *uds\_ctx*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ep* ) |

`#include <[usbd.h](usbd_8h.md)>`

Clear endpoint halt.

Parameters
:   | [in] | uds\_ctx | Pointer to USB device support context |
    | --- | --- | --- |
    | [in] | ep | Endpoint address |

Returns
:   0 on success, or error from [udc\_ep\_clear\_halt()](group__udc__api.md#gadec9c8af89b28984028fd8e0b1a8c776 "Clear endpoint halt.")

## [◆ ](#ga59b0cb83b05e0a44db9c6a36171d524f)usbd\_ep\_ctrl\_buf\_alloc()

| struct [net\_buf](structnet__buf.md) \* usbd\_ep\_ctrl\_buf\_alloc | ( | struct [usbd\_contex](structusbd__contex.md) \*const | *uds\_ctx*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ep*, |
|  |  | const [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[usbd.h](usbd_8h.md)>`

Allocate buffer for USB device control request.

Allocate a new buffer from controller's driver buffer pool.

Parameters
:   | [in] | uds\_ctx | Pointer to USB device support context |
    | --- | --- | --- |
    | [in] | ep | Endpoint address |
    | [in] | size | Size of the request buffer |

Returns
:   pointer to allocated request or NULL on error.

## [◆ ](#ga52acb4fb74e3737b446b6704c6925d70)usbd\_ep\_ctrl\_enqueue()

| int usbd\_ep\_ctrl\_enqueue | ( | struct [usbd\_contex](structusbd__contex.md) \*const | *uds\_ctx*, |
| --- | --- | --- | --- |
|  |  | struct [net\_buf](structnet__buf.md) \*const | *buf* ) |

`#include <[usbd.h](usbd_8h.md)>`

Queue USB device control request.

Add control request to the queue.

Parameters
:   | [in] | uds\_ctx | Pointer to USB device support context |
    | --- | --- | --- |
    | [in] | buf | Pointer to UDC request buffer |

Returns
:   0 on success, all other values should be treated as error.

## [◆ ](#ga0d1d7f59822674c201147b50a1dbdb96)usbd\_ep\_dequeue()

| int usbd\_ep\_dequeue | ( | struct [usbd\_contex](structusbd__contex.md) \* | *uds\_ctx*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ep* ) |

`#include <[usbd.h](usbd_8h.md)>`

Remove all USB device controller requests from endpoint queue.

Parameters
:   | [in] | uds\_ctx | Pointer to USB device support context |
    | --- | --- | --- |
    | [in] | ep | Endpoint address |

Returns
:   0 on success, or error from [udc\_ep\_dequeue()](group__udc__api.md#ga6e6fb62fb8ebceca7e8e6b590c32efc2 "Remove all USB device controller requests from endpoint queue.")

## [◆ ](#ga19ecdc00918dbec14fdbcf847b6f4dce)usbd\_ep\_enqueue()

| int usbd\_ep\_enqueue | ( | const struct [usbd\_class\_node](structusbd__class__node.md) \*const | *c\_nd*, |
| --- | --- | --- | --- |
|  |  | struct [net\_buf](structnet__buf.md) \*const | *buf* ) |

`#include <[usbd.h](usbd_8h.md)>`

Queue USB device request.

Add request to the queue.

Parameters
:   | [in] | c\_nd | Pointer to USB device class node |
    | --- | --- | --- |
    | [in] | buf | Pointer to UDC request buffer |

Returns
:   0 on success, or error from [udc\_ep\_enqueue()](group__udc__api.md#gacb2dc96353f1cffcc3d5e9710133fc0d "Queue USB device controller request.")

## [◆ ](#ga9292b393ef17fd61ea42b2f28fdd57ee)usbd\_ep\_is\_halted()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) usbd\_ep\_is\_halted | ( | struct [usbd\_contex](structusbd__contex.md) \* | *uds\_ctx*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ep* ) |

`#include <[usbd.h](usbd_8h.md)>`

Checks whether the endpoint is halted.

Parameters
:   | [in] | uds\_ctx | Pointer to USB device support context |
    | --- | --- | --- |
    | [in] | ep | Endpoint address |

Returns
:   true if endpoint is halted, false otherwise

## [◆ ](#ga0730043c2fd89b56db6e7457b639968d)usbd\_ep\_set\_halt()

| int usbd\_ep\_set\_halt | ( | struct [usbd\_contex](structusbd__contex.md) \* | *uds\_ctx*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ep* ) |

`#include <[usbd.h](usbd_8h.md)>`

Halt endpoint.

Parameters
:   | [in] | uds\_ctx | Pointer to USB device support context |
    | --- | --- | --- |
    | [in] | ep | Endpoint address |

Returns
:   0 on success, or error from [udc\_ep\_set\_halt()](group__udc__api.md#ga19488ec4c93d81592bb5ffccfc1eadc4 "Halt endpoint.")

## [◆ ](#gaf3cd6c12317f9d94ee98f2809d2a0e04)usbd\_init()

| int usbd\_init | ( | struct [usbd\_contex](structusbd__contex.md) \* | *uds\_ctx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbd.h](usbd_8h.md)>`

Initialize USB device.

Initialize USB device descriptors and configuration, initialize USB device controller. Class instances should be registered before they are involved. However, the stack should also initialize without registered instances, even if the host would complain about missing interfaces.

Parameters
:   | [in] | uds\_ctx | Pointer to USB device support context |
    | --- | --- | --- |

Returns
:   0 on success, other values on fail.

## [◆ ](#ga832e3147aba9297bad263b2a3817e1e4)usbd\_is\_suspended()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) usbd\_is\_suspended | ( | struct [usbd\_contex](structusbd__contex.md) \* | *uds\_ctx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbd.h](usbd_8h.md)>`

Checks whether the USB device controller is suspended.

Parameters
:   | [in] | uds\_ctx | Pointer to USB device support context |
    | --- | --- | --- |

Returns
:   true if endpoint is halted, false otherwise

## [◆ ](#ga3640cb8425961a8038c225e1daea34a3)usbd\_register\_class()

| int usbd\_register\_class | ( | struct [usbd\_contex](structusbd__contex.md) \* | *uds\_ctx*, |
| --- | --- | --- | --- |
|  |  | const char \* | *name*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *cfg* ) |

`#include <[usbd.h](usbd_8h.md)>`

Register an USB class instance.

An USB class implementation can have one or more instances. To identify the instances we use device drivers API. Device names have a prefix derived from the name of the class, for example CDC\_ACM for CDC ACM class instance, and can also be easily identified in the shell. Class instance can only be registered when the USB device stack is disabled. Registered instances are initialized at initialization of the USB device stack, and the interface descriptors of each instance are adapted to the whole context.

Parameters
:   | [in] | uds\_ctx | Pointer to USB device support context |
    | --- | --- | --- |
    | [in] | name | Class instance name |
    | [in] | cfg | Configuration value (similar to bConfigurationValue) |

Returns
:   0 on success, other values on fail.

## [◆ ](#gaa7656f656182e727531e531344c960df)usbd\_shutdown()

| int usbd\_shutdown | ( | struct [usbd\_contex](structusbd__contex.md) \*const | *uds\_ctx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbd.h](usbd_8h.md)>`

Shutdown the USB device support.

This function completely disables the USB device support.

Parameters
:   | [in] | uds\_ctx | Pointer to USB device support context |
    | --- | --- | --- |

Returns
:   0 on success, other values on fail.

## [◆ ](#gadf7cc0edc2d046f0b50e65fcc007f982)usbd\_unregister\_class()

| int usbd\_unregister\_class | ( | struct [usbd\_contex](structusbd__contex.md) \* | *uds\_ctx*, |
| --- | --- | --- | --- |
|  |  | const char \* | *name*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *cfg* ) |

`#include <[usbd.h](usbd_8h.md)>`

Unregister an USB class instance.

USB class instance will be removed and will not appear on the next start of the stack. Instance can only be unregistered when the USB device stack is disabled.

Parameters
:   | [in] | uds\_ctx | Pointer to USB device support context |
    | --- | --- | --- |
    | [in] | name | Class instance name |
    | [in] | cfg | Configuration value (similar to bConfigurationValue) |

Returns
:   0 on success, other values on fail.

## [◆ ](#ga4d440313da931d4504919b8fe2783419)usbd\_wakeup\_request()

| int usbd\_wakeup\_request | ( | struct [usbd\_contex](structusbd__contex.md) \* | *uds\_ctx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbd.h](usbd_8h.md)>`

Initiate the USB remote wakeup (TBD).

Returns
:   0 on success, other values on fail.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
