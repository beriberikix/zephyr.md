---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__usbd__api.html
original_path: doxygen/html/group__usbd__api.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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
| struct | [usbd\_str\_desc\_data](structusbd__str__desc__data.md) |
|  | Used internally to keep descriptors in order. [More...](structusbd__str__desc__data.md#details) |
| struct | [usbd\_bos\_desc\_data](structusbd__bos__desc__data.md) |
|  | USBD BOS Device Capability descriptor data. [More...](structusbd__bos__desc__data.md#details) |
| struct | [usbd\_desc\_node](structusbd__desc__node.md) |
|  | Descriptor node. [More...](structusbd__desc__node.md#details) |
| struct | [usbd\_config\_node](structusbd__config__node.md) |
|  | Device configuration node. [More...](structusbd__config__node.md#details) |
| struct | [usbd\_ch9\_data](structusbd__ch9__data.md) |
|  | USB device support middle layer runtime data. [More...](structusbd__ch9__data.md#details) |
| struct | [usbd\_status](structusbd__status.md) |
|  | USB device support status. [More...](structusbd__status.md#details) |
| struct | [usbd\_context](structusbd__context.md) |
|  | USB device support runtime context. [More...](structusbd__context.md#details) |
| struct | [usbd\_cctx\_vendor\_req](structusbd__cctx__vendor__req.md) |
|  | Vendor Requests Table. [More...](structusbd__cctx__vendor__req.md#details) |
| struct | [usbd\_class\_api](structusbd__class__api.md) |
|  | USB device support class instance API. [More...](structusbd__class__api.md#details) |
| struct | [usbd\_class\_data](structusbd__class__data.md) |
|  | USB device support class data. [More...](structusbd__class__data.md#details) |

| Macros | |
| --- | --- |
| #define | [USB\_BSTRING\_LENGTH](#gac3d58cfa3f92b1811e9ed136c4450906)([s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)) |
| #define | [USB\_STRING\_DESCRIPTOR\_LENGTH](#gaef85e50556291fa93cbf72b01529b4a8)([s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)) |
| #define | [USBD\_NUMOF\_INTERFACES\_MAX](#gaf8aadd499f7e0438acac4a7f36645d49)   16U |
| #define | [USBD\_CCTX\_REGISTERED](#ga588b9e156a49d3b0358bee185cdeebee)   0 |
|  | USB Class instance registered flag. |
| #define | [USBD\_DEVICE\_DEFINE](#ga26777805f749f29efa882f9bf391473a)(device\_name, udc\_dev, vid, pid) |
|  | Define USB device context structure. |
| #define | [USBD\_CONFIGURATION\_DEFINE](#ga2d98fd68eff66f36522688f3de527586)(name, attrib, power, desc\_nd) |
|  | Define USB device configuration. |
| #define | [USBD\_DESC\_LANG\_DEFINE](#gaec816a27118bcb289ab4840fcd22888e)(name) |
|  | Create a string descriptor node and language string descriptor. |
| #define | [USBD\_DESC\_STRING\_DEFINE](#gaf800e2040ac30844cab463c13d1fcdf8)(d\_name, d\_string, d\_utype) |
|  | Create a string descriptor. |
| #define | [USBD\_DESC\_MANUFACTURER\_DEFINE](#ga18b1321daf1173a3cb0bc61a0d9beb34)(d\_name, d\_string) |
|  | Create a string descriptor node and manufacturer string descriptor. |
| #define | [USBD\_DESC\_PRODUCT\_DEFINE](#gaa5e43f9eac8f91d3896ea5e19baed031)(d\_name, d\_string) |
|  | Create a string descriptor node and product string descriptor. |
| #define | [USBD\_DESC\_SERIAL\_NUMBER\_DEFINE](#ga26af7f93205dc78eeb60a3c09aa7b2d3)(d\_name) |
|  | Create a string descriptor node and serial number string descriptor. |
| #define | [USBD\_DESC\_CONFIG\_DEFINE](#ga45dc8df18f6fdf72edfd21f35d3046db)(d\_name, d\_string) |
|  | Create a string descriptor node for configuration descriptor. |
| #define | [USBD\_DESC\_BOS\_DEFINE](#ga620a5aa567dc4de7d5d1ef6b0cd9e937)(name, len, subset) |
|  | Define BOS Device Capability descriptor node. |
| #define | [USBD\_DEFINE\_CLASS](#gaaebebc77106848d8d62016936399776a)(class\_name, class\_api, class\_priv, class\_v\_reqs) |
|  | Define USB device support class data. |
| #define | [VENDOR\_REQ\_DEFINE](#ga54ca08c74ae715281381d878f828727e)(\_reqs, \_len) |
|  | Helper to declare request table of [usbd\_cctx\_vendor\_req](structusbd__cctx__vendor__req.md "Vendor Requests Table."). |
| #define | [USBD\_VENDOR\_REQ](#ga464933a8332c11d15c92914aa1790e10)(\_reqs...) |
|  | Helper to declare supported vendor requests. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [usbd\_msg\_cb\_t](#ga2cd074cefff922b0816de37935d9646e)) (struct [usbd\_context](structusbd__context.md) \*const ctx, const struct [usbd\_msg](structusbd__msg.md) \*const msg) |
|  | Callback type definition for USB device message delivery. |

| Enumerations | |
| --- | --- |
| enum | [usbd\_ch9\_state](#ga95fb708d8a54eaa3ce0acc4e65519bbc) { [USBD\_STATE\_DEFAULT](#gga95fb708d8a54eaa3ce0acc4e65519bbca978c707d313eb49b70bc62dfae304048) = 0 , [USBD\_STATE\_ADDRESS](#gga95fb708d8a54eaa3ce0acc4e65519bbca985f06c5505c5684a98954f15701cc9d) , [USBD\_STATE\_CONFIGURED](#gga95fb708d8a54eaa3ce0acc4e65519bbca44c1920b09ea1062ea4d7ac31a846509) } |
|  | USB device support middle layer runtime state. [More...](#ga95fb708d8a54eaa3ce0acc4e65519bbc) |
| enum | [usbd\_speed](#ga2f2da3d634530f08cd59d408c811ad71) { [USBD\_SPEED\_FS](#gga2f2da3d634530f08cd59d408c811ad71a30b20b0839dff88b038e680b55f382d7) , [USBD\_SPEED\_HS](#gga2f2da3d634530f08cd59d408c811ad71abaf4bdba11db59d804d753e6fac92266) , [USBD\_SPEED\_SS](#gga2f2da3d634530f08cd59d408c811ad71a195490bdfa76ffca418e8bf2f3d3c96a) } |
|  | USB device speed. [More...](#ga2f2da3d634530f08cd59d408c811ad71) |

| Functions | |
| --- | --- |
| static struct [usbd\_context](structusbd__context.md) \* | [usbd\_class\_get\_ctx](#gaf97c68e75420bd5a1085c047577fd5a7) (const struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data) |
|  | Get the USB device runtime context under which the class is registered. |
| static void \* | [usbd\_class\_get\_private](#ga2e511d0341b4e1bd57fb4420512eeeb5) (const struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data) |
|  | Get class implementation private data. |
| int | [usbd\_add\_descriptor](#ga33d0cef23d4b6c62b79b41559427b584) (struct [usbd\_context](structusbd__context.md) \*uds\_ctx, struct [usbd\_desc\_node](structusbd__desc__node.md) \*dn) |
|  | Add common USB descriptor. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [usbd\_str\_desc\_get\_idx](#gab023ab276eb68c644895483344d33948) (const struct [usbd\_desc\_node](structusbd__desc__node.md) \*const desc\_nd) |
|  | Get USB string descriptor index from descriptor node. |
| void | [usbd\_remove\_descriptor](#ga3146ee636b84c6d319365716f5741363) (struct [usbd\_desc\_node](structusbd__desc__node.md) \*const desc\_nd) |
|  | Remove USB string descriptor. |
| int | [usbd\_add\_configuration](#ga5f4b69609f9a8f00a9e0fea4dffce1c4) (struct [usbd\_context](structusbd__context.md) \*uds\_ctx, const enum [usbd\_speed](#ga2f2da3d634530f08cd59d408c811ad71) speed, struct [usbd\_config\_node](structusbd__config__node.md) \*cd) |
|  | Add a USB device configuration. |
| int | [usbd\_register\_class](#ga4a837040e9d02c5773d69a6cf6c35960) (struct [usbd\_context](structusbd__context.md) \*uds\_ctx, const char \*name, const enum [usbd\_speed](#ga2f2da3d634530f08cd59d408c811ad71) speed, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cfg) |
|  | Register an USB class instance. |
| int | [usbd\_register\_all\_classes](#ga4382a5b4888baf65045faea0b88723f3) (struct [usbd\_context](structusbd__context.md) \*uds\_ctx, const enum [usbd\_speed](#ga2f2da3d634530f08cd59d408c811ad71) speed, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cfg) |
|  | Register all available USB class instances. |
| int | [usbd\_unregister\_class](#ga1ae7a7a04f4ec1206d352d5c6401c51b) (struct [usbd\_context](structusbd__context.md) \*uds\_ctx, const char \*name, const enum [usbd\_speed](#ga2f2da3d634530f08cd59d408c811ad71) speed, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cfg) |
|  | Unregister an USB class instance. |
| int | [usbd\_unregister\_all\_classes](#ga2996b5f6df459c8a179fc6c22f944063) (struct [usbd\_context](structusbd__context.md) \*uds\_ctx, const enum [usbd\_speed](#ga2f2da3d634530f08cd59d408c811ad71) speed, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cfg) |
|  | Unregister all available USB class instances. |
| int | [usbd\_msg\_register\_cb](#ga2ebe08b8bf5ff3b64c4df1fcb346cf38) (struct [usbd\_context](structusbd__context.md) \*const uds\_ctx, const [usbd\_msg\_cb\_t](#ga2cd074cefff922b0816de37935d9646e) cb) |
|  | Register USB notification message callback. |
| int | [usbd\_init](#ga78e5f07af641f9610cc32255efe1680f) (struct [usbd\_context](structusbd__context.md) \*uds\_ctx) |
|  | Initialize USB device. |
| int | [usbd\_enable](#ga1a40fc13129e9218ca63ab3ca70d8d68) (struct [usbd\_context](structusbd__context.md) \*uds\_ctx) |
|  | Enable the USB device support and registered class instances. |
| int | [usbd\_disable](#gaaa21e9f33175b7d2434e54e1b3d2799b) (struct [usbd\_context](structusbd__context.md) \*uds\_ctx) |
|  | Disable the USB device support. |
| int | [usbd\_shutdown](#ga37585e0124a4d0d8cf6e65f13325eaf0) (struct [usbd\_context](structusbd__context.md) \*const uds\_ctx) |
|  | Shutdown the USB device support. |
| int | [usbd\_ep\_set\_halt](#ga176f42b2dd221c0de28ad9122a7d2693) (struct [usbd\_context](structusbd__context.md) \*uds\_ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Halt endpoint. |
| int | [usbd\_ep\_clear\_halt](#ga03729a4e9add3a55a7c3c2c8666a53a7) (struct [usbd\_context](structusbd__context.md) \*uds\_ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Clear endpoint halt. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [usbd\_ep\_is\_halted](#ga94cb8465b7bf85457f29e84b5b8ddfe9) (struct [usbd\_context](structusbd__context.md) \*uds\_ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Checks whether the endpoint is halted. |
| struct [net\_buf](structnet__buf.md) \* | [usbd\_ep\_buf\_alloc](#ga6c671d49c811b0af6b809f5940cd6d70) (const struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, const [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Allocate buffer for USB device request. |
| int | [usbd\_ep\_ctrl\_enqueue](#ga967d507d82d912119a732fd230bd561e) (struct [usbd\_context](structusbd__context.md) \*const uds\_ctx, struct [net\_buf](structnet__buf.md) \*const buf) |
|  | Queue USB device control request. |
| int | [usbd\_ep\_enqueue](#gaabf8333a7aefc4428f38e79a7264e383) (const struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data, struct [net\_buf](structnet__buf.md) \*const buf) |
|  | Queue USB device request. |
| int | [usbd\_ep\_dequeue](#ga1534058a609794e1d080aed98fcf5823) (struct [usbd\_context](structusbd__context.md) \*uds\_ctx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Remove all USB device controller requests from endpoint queue. |
| int | [usbd\_ep\_buf\_free](#ga8aa454c24495f2a462eae53b78c488dc) (struct [usbd\_context](structusbd__context.md) \*uds\_ctx, struct [net\_buf](structnet__buf.md) \*buf) |
|  | Free USB device request buffer. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [usbd\_is\_suspended](#ga5f7a5af958f7de8893e04ff2b7748c7e) (struct [usbd\_context](structusbd__context.md) \*uds\_ctx) |
|  | Checks whether the USB device controller is suspended. |
| int | [usbd\_wakeup\_request](#ga34086553e74795ffdc000349e61a3c8b) (struct [usbd\_context](structusbd__context.md) \*uds\_ctx) |
|  | Initiate the USB remote wakeup (TBD). |
| enum [usbd\_speed](#ga2f2da3d634530f08cd59d408c811ad71) | [usbd\_bus\_speed](#gab4a0d05a8f183f7479ad33ee29e8a611) (const struct [usbd\_context](structusbd__context.md) \*const uds\_ctx) |
|  | Get actual device speed. |
| enum [usbd\_speed](#ga2f2da3d634530f08cd59d408c811ad71) | [usbd\_caps\_speed](#gaab7c4692a30b58aa76b03b9e50460856) (const struct [usbd\_context](structusbd__context.md) \*const uds\_ctx) |
|  | Get highest speed supported by the controller. |
| int | [usbd\_device\_set\_bcd\_usb](#gacb704bd4f396887c859932b2ab6b4991) (struct [usbd\_context](structusbd__context.md) \*const uds\_ctx, const enum [usbd\_speed](#ga2f2da3d634530f08cd59d408c811ad71) speed, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bcd) |
|  | Set USB device descriptor value bcdUSB. |
| int | [usbd\_device\_set\_vid](#ga06aa9f954b6765e07494753bb4fa42d4) (struct [usbd\_context](structusbd__context.md) \*const uds\_ctx, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vid) |
|  | Set USB device descriptor value idVendor. |
| int | [usbd\_device\_set\_pid](#ga44719fc03a50c70d75ce65e1d2f77a04) (struct [usbd\_context](structusbd__context.md) \*const uds\_ctx, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) pid) |
|  | Set USB device descriptor value idProduct. |
| int | [usbd\_device\_set\_bcd\_device](#gafda88e8a71c52addbe76ebeb874a8af5) (struct [usbd\_context](structusbd__context.md) \*const uds\_ctx, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bcd) |
|  | Set USB device descriptor value bcdDevice. |
| int | [usbd\_device\_set\_code\_triple](#ga83a58b50bec680513eabd3bb7075b511) (struct [usbd\_context](structusbd__context.md) \*const uds\_ctx, const enum [usbd\_speed](#ga2f2da3d634530f08cd59d408c811ad71) speed, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) base\_class, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) subclass, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) protocol) |
|  | Set USB device descriptor code triple Base Class, SubClass, and Protocol. |
| int | [usbd\_config\_attrib\_rwup](#ga2b803f8ac10d9375a74949cd2c2f3136) (struct [usbd\_context](structusbd__context.md) \*const uds\_ctx, const enum [usbd\_speed](#ga2f2da3d634530f08cd59d408c811ad71) speed, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cfg, const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Setup USB device configuration attribute Remote Wakeup. |
| int | [usbd\_config\_attrib\_self](#ga8b0fff68bc6ce9d8ec4a7dfd59f0eade) (struct [usbd\_context](structusbd__context.md) \*const uds\_ctx, const enum [usbd\_speed](#ga2f2da3d634530f08cd59d408c811ad71) speed, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cfg, const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Setup USB device configuration attribute Self-powered. |
| int | [usbd\_config\_maxpower](#ga59fc1ea6d943d26b0207bb6060e18f08) (struct [usbd\_context](structusbd__context.md) \*const uds\_ctx, const enum [usbd\_speed](#ga2f2da3d634530f08cd59d408c811ad71) speed, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cfg, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) power) |
|  | Setup USB device configuration power consumption. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [usbd\_can\_detect\_vbus](#ga5ea40d893980e24294e82d22855b407c) (struct [usbd\_context](structusbd__context.md) \*const uds\_ctx) |
|  | Check that the controller can detect the VBUS state change. |

## Detailed Description

New USB device stack core API.

Since
:   3.3

Version
:   0.1.0

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

## [◆ ](#ga2d98fd68eff66f36522688f3de527586)USBD\_CONFIGURATION\_DEFINE

| #define USBD\_CONFIGURATION\_DEFINE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *attrib*, |
|  |  |  | *power*, |
|  |  |  | *desc\_nd* ) |

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

.[str\_desc\_nd](structusbd__config__node.md#a19203885a9698861f849bd0fd57cb37f) = desc\_nd, \

}

[usb\_cfg\_descriptor](structusb__cfg__descriptor.md)

USB Standard Configuration Descriptor defined in spec.

**Definition** usb\_ch9.h:181

[usbd\_config\_node](structusbd__config__node.md)

Device configuration node.

**Definition** usbd.h:132

[usbd\_config\_node::str\_desc\_nd](structusbd__config__node.md#a19203885a9698861f849bd0fd57cb37f)

struct usbd\_desc\_node \* str\_desc\_nd

Optional pointer to string descriptor node.

**Definition** usbd.h:138

[USB\_SCD\_RESERVED](usb__ch9_8h.md#a2a8b7c42705cd1e0fd0aecb0028cb2ba)

#define USB\_SCD\_RESERVED

USB Standard Configuration Descriptor Characteristics from Table 9-10.

**Definition** usb\_ch9.h:252

[USB\_DESC\_CONFIGURATION](usb__ch9_8h.md#a7764131f2e59070eb032bd9d68d32620)

#define USB\_DESC\_CONFIGURATION

**Definition** usb\_ch9.h:111

Define USB device configuration.

USB device requires at least one configuration instance per supported speed. `attrib` is a combination of [USB\_SCD\_SELF\_POWERED](usb__ch9_8h.md#a0122c49a39e67e2443e491132aa0ecfd) or [USB\_SCD\_REMOTE\_WAKEUP](usb__ch9_8h.md#aa1fa7548e67cc2755d91b68fd1545088), depending on which characteristic the USB device should have in this configuration.

Parameters
:   | name | Configuration name |
    | --- | --- |
    | attrib | Configuration characteristics. Attributes can also be updated with [usbd\_config\_attrib\_rwup()](#ga2b803f8ac10d9375a74949cd2c2f3136) and [usbd\_config\_attrib\_self()](#ga8b0fff68bc6ce9d8ec4a7dfd59f0eade) |
    | power | bMaxPower value in 2 mA units. This value can also be set with [usbd\_config\_maxpower()](#ga59fc1ea6d943d26b0207bb6060e18f08) |
    | desc\_nd | Address of the string descriptor node used to describe the configuration, see [USBD\_DESC\_CONFIG\_DEFINE()](#ga45dc8df18f6fdf72edfd21f35d3046db). String descriptors are optional and the parameter can be NULL. |

## [◆ ](#gaaebebc77106848d8d62016936399776a)USBD\_DEFINE\_CLASS

| #define USBD\_DEFINE\_CLASS | ( |  | *class\_name*, |
| --- | --- | --- | --- |
|  |  |  | *class\_api*, |
|  |  |  | *class\_priv*, |
|  |  |  | *class\_v\_reqs* ) |

`#include <[usbd.h](usbd_8h.md)>`

**Value:**

static struct [usbd\_class\_data](structusbd__class__data.md) class\_name = { \

.name = [STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(class\_name), \

.api = class\_api, \

.v\_reqs = class\_v\_reqs, \

.priv = class\_priv, \

}; \

static [STRUCT\_SECTION\_ITERABLE\_ALTERNATE](group__iterable__section__apis.md#gae08ef16db3e04967fdca69a19ca4c70b)( \

usbd\_class\_fs, usbd\_class\_node, class\_name##\_fs) = { \

.c\_data = &class\_name, \

}; \

static [STRUCT\_SECTION\_ITERABLE\_ALTERNATE](group__iterable__section__apis.md#gae08ef16db3e04967fdca69a19ca4c70b)( \

usbd\_class\_hs, usbd\_class\_node, class\_name##\_hs) = { \

.c\_data = &class\_name, \

}

[STRUCT\_SECTION\_ITERABLE\_ALTERNATE](group__iterable__section__apis.md#gae08ef16db3e04967fdca69a19ca4c70b)

#define STRUCT\_SECTION\_ITERABLE\_ALTERNATE(secname, struct\_type, varname)

Defines a new element of alternate data type for an iterable section.

**Definition** iterable\_sections.h:188

[STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)

#define STRINGIFY(s)

**Definition** common.h:134

[usbd\_class\_data](structusbd__class__data.md)

USB device support class data.

**Definition** usbd.h:324

Define USB device support class data.

Macro defines class (function) data, as well as corresponding node structures used internally by the stack.

Parameters
:   | class\_name | Class name |
    | --- | --- |
    | class\_api | Pointer to struct [usbd\_class\_api](structusbd__class__api.md "USB device support class instance API.") |
    | class\_priv | Class private data |
    | class\_v\_reqs | Pointer to struct [usbd\_cctx\_vendor\_req](structusbd__cctx__vendor__req.md "Vendor Requests Table.") |

## [◆ ](#ga620a5aa567dc4de7d5d1ef6b0cd9e937)USBD\_DESC\_BOS\_DEFINE

| #define USBD\_DESC\_BOS\_DEFINE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *len*, |
|  |  |  | *subset* ) |

`#include <[usbd.h](usbd_8h.md)>`

**Value:**

static struct [usbd\_desc\_node](structusbd__desc__node.md) name = { \

.bos = { \

.utype = USBD\_DUT\_BOS\_NONE, \

}, \

.ptr = subset, \

.bLength = len, \

.bDescriptorType = [USB\_DESC\_BOS](usb__ch9_8h.md#a9f6e306632b56036d4dd7cc2430bcec9), \

}

[usbd\_desc\_node](structusbd__desc__node.md)

Descriptor node.

**Definition** usbd.h:109

[USB\_DESC\_BOS](usb__ch9_8h.md#a9f6e306632b56036d4dd7cc2430bcec9)

#define USB\_DESC\_BOS

**Definition** usb\_ch9.h:122

Define BOS Device Capability descriptor node.

The application defines a BOS capability descriptor node for descriptors such as USB 2.0 Extension Descriptor.

Parameters
:   | name | Descriptor node identifier |
    | --- | --- |
    | len | Device Capability descriptor length |
    | subset | Pointer to a Device Capability descriptor |

## [◆ ](#ga45dc8df18f6fdf72edfd21f35d3046db)USBD\_DESC\_CONFIG\_DEFINE

| #define USBD\_DESC\_CONFIG\_DEFINE | ( |  | *d\_name*, |
| --- | --- | --- | --- |
|  |  |  | *d\_string* ) |

`#include <[usbd.h](usbd_8h.md)>`

**Value:**

[USBD\_DESC\_STRING\_DEFINE](#gaf800e2040ac30844cab463c13d1fcdf8)(d\_name, d\_string, USBD\_DUT\_STRING\_CONFIG)

[USBD\_DESC\_STRING\_DEFINE](#gaf800e2040ac30844cab463c13d1fcdf8)

#define USBD\_DESC\_STRING\_DEFINE(d\_name, d\_string, d\_utype)

Create a string descriptor.

**Definition** usbd.h:529

Create a string descriptor node for configuration descriptor.

This macro defines a descriptor node whose address can be used as an argument for the [USBD\_CONFIGURATION\_DEFINE()](#ga2d98fd68eff66f36522688f3de527586) macro.

Parameters
:   | d\_name | String descriptor node identifier. |
    | --- | --- |
    | d\_string | ASCII7 encoded configuration description string literal |

## [◆ ](#gaec816a27118bcb289ab4840fcd22888e)USBD\_DESC\_LANG\_DEFINE

| #define USBD\_DESC\_LANG\_DEFINE | ( |  | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbd.h](usbd_8h.md)>`

**Value:**

static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) langid\_##name = [sys\_cpu\_to\_le16](sys_2byteorder_8h.md#ae7f653c0bca81809b53d8a91854ca4c9)(0x0409); \

static struct [usbd\_desc\_node](structusbd__desc__node.md) name = { \

.str = { \

.idx = 0, \

.utype = USBD\_DUT\_STRING\_LANG, \

}, \

.ptr = &langid\_##name, \

.[bLength](structusbd__desc__node.md#ad71ef74fd7fe43a8117704553a3be01c) = sizeof(struct [usb\_string\_descriptor](structusb__string__descriptor.md)), \

.bDescriptorType = [USB\_DESC\_STRING](usb__ch9_8h.md#a6a5678b964f3a9b4ba2f52e9a51bebf5), \

}

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[usb\_string\_descriptor](structusb__string__descriptor.md)

USB Unicode (UTF16LE) String Descriptor defined in spec.

**Definition** usb\_ch9.h:233

[usbd\_desc\_node::bLength](structusbd__desc__node.md#ad71ef74fd7fe43a8117704553a3be01c)

uint8\_t bLength

Descriptor size in bytes.

**Definition** usbd.h:119

[sys\_cpu\_to\_le16](sys_2byteorder_8h.md#ae7f653c0bca81809b53d8a91854ca4c9)

#define sys\_cpu\_to\_le16(val)

Convert 16-bit integer from host endianness to little-endian.

**Definition** byteorder.h:266

[USB\_DESC\_STRING](usb__ch9_8h.md#a6a5678b964f3a9b4ba2f52e9a51bebf5)

#define USB\_DESC\_STRING

**Definition** usb\_ch9.h:112

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

[USBD\_DESC\_STRING\_DEFINE](#gaf800e2040ac30844cab463c13d1fcdf8)(d\_name, d\_string, USBD\_DUT\_STRING\_MANUFACTURER)

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

[USBD\_DESC\_STRING\_DEFINE](#gaf800e2040ac30844cab463c13d1fcdf8)(d\_name, d\_string, USBD\_DUT\_STRING\_PRODUCT)

Create a string descriptor node and product string descriptor.

This macro defines a descriptor node and a string descriptor that, when added to the device context, is automatically used as the product string descriptor. Both descriptor node and descriptor are defined with static-storage-class specifier.

Parameters
:   | d\_name | String descriptor node identifier. |
    | --- | --- |
    | d\_string | ASCII7 encoded product string literal |

## [◆ ](#ga26af7f93205dc78eeb60a3c09aa7b2d3)USBD\_DESC\_SERIAL\_NUMBER\_DEFINE

| #define USBD\_DESC\_SERIAL\_NUMBER\_DEFINE | ( |  | *d\_name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbd.h](usbd_8h.md)>`

**Value:**

static struct [usbd\_desc\_node](structusbd__desc__node.md) d\_name = { \

.str = { \

.utype = USBD\_DUT\_STRING\_SERIAL\_NUMBER, \

.ascii7 = true, \

.use\_hwinfo = true, \

}, \

.bDescriptorType = [USB\_DESC\_STRING](usb__ch9_8h.md#a6a5678b964f3a9b4ba2f52e9a51bebf5), \

}

Create a string descriptor node and serial number string descriptor.

This macro defines a descriptor node that, when added to the device context, is automatically used as the serial number string descriptor. A valid serial number is generated from HWID (HWINFO= whenever this string descriptor is requested.

Parameters
:   | d\_name | String descriptor node identifier. |
    | --- | --- |

## [◆ ](#gaf800e2040ac30844cab463c13d1fcdf8)USBD\_DESC\_STRING\_DEFINE

| #define USBD\_DESC\_STRING\_DEFINE | ( |  | *d\_name*, |
| --- | --- | --- | --- |
|  |  |  | *d\_string*, |
|  |  |  | *d\_utype* ) |

`#include <[usbd.h](usbd_8h.md)>`

**Value:**

static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ascii\_##d\_name[[USB\_BSTRING\_LENGTH](#gac3d58cfa3f92b1811e9ed136c4450906)(d\_string)] = d\_string; \

static struct [usbd\_desc\_node](structusbd__desc__node.md) d\_name = { \

.str = { \

.utype = d\_utype, \

.ascii7 = true, \

}, \

.ptr = &ascii\_##d\_name, \

.[bLength](structusbd__desc__node.md#ad71ef74fd7fe43a8117704553a3be01c) = [USB\_STRING\_DESCRIPTOR\_LENGTH](#gaef85e50556291fa93cbf72b01529b4a8)(d\_string), \

.bDescriptorType = [USB\_DESC\_STRING](usb__ch9_8h.md#a6a5678b964f3a9b4ba2f52e9a51bebf5), \

}

[USB\_BSTRING\_LENGTH](#gac3d58cfa3f92b1811e9ed136c4450906)

#define USB\_BSTRING\_LENGTH(s)

**Definition** usbd.h:50

[USB\_STRING\_DESCRIPTOR\_LENGTH](#gaef85e50556291fa93cbf72b01529b4a8)

#define USB\_STRING\_DESCRIPTOR\_LENGTH(s)

**Definition** usbd.h:62

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

Create a string descriptor.

This macro defines a descriptor node and a string descriptor. The string literal passed to the macro should be in the ASCII7 format. It is converted to UTF16LE format on the host request.

Parameters
:   | d\_name | Internal string descriptor node identifier name |
    | --- | --- |
    | d\_string | ASCII7 encoded string literal |
    | d\_utype | String descriptor usage type |

## [◆ ](#ga26777805f749f29efa882f9bf391473a)USBD\_DEVICE\_DEFINE

| #define USBD\_DEVICE\_DEFINE | ( |  | *device\_name*, |
| --- | --- | --- | --- |
|  |  |  | *udc\_dev*, |
|  |  |  | *vid*, |
|  |  |  | *pid* ) |

`#include <[usbd.h](usbd_8h.md)>`

**Value:**

static struct [usb\_device\_descriptor](structusb__device__descriptor.md) \

fs\_desc\_##device\_name = { \

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

static struct [usb\_device\_descriptor](structusb__device__descriptor.md) \

hs\_desc\_##device\_name = { \

.bLength = sizeof(struct [usb\_device\_descriptor](structusb__device__descriptor.md)), \

.bDescriptorType = [USB\_DESC\_DEVICE](usb__ch9_8h.md#aefeff68c3a236749d1105d94ed9bad68), \

.bcdUSB = [sys\_cpu\_to\_le16](sys_2byteorder_8h.md#ae7f653c0bca81809b53d8a91854ca4c9)([USB\_SRN\_2\_0](usb__ch9_8h.md#a14527f51ba0e1634b3b477c80e7ae31f)), \

.bDeviceClass = [USB\_BCC\_MISCELLANEOUS](usb__ch9_8h.md#a62bf5e94c7c36c9d1d94438d7a12a482), \

.bDeviceSubClass = 2, \

.bDeviceProtocol = 1, \

.bMaxPacketSize0 = 64, \

.idVendor = vid, \

.idProduct = pid, \

.bcdDevice = [sys\_cpu\_to\_le16](sys_2byteorder_8h.md#ae7f653c0bca81809b53d8a91854ca4c9)([USB\_BCD\_DRN](usb__ch9_8h.md#a2f6e90e87d7a1d53418ce084a293e6fc)), \

.iManufacturer = 0, \

.iProduct = 0, \

.iSerialNumber = 0, \

.bNumConfigurations = 0, \

}; \

static [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)(usbd\_context, device\_name) = { \

.name = [STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(device\_name), \

.dev = udc\_dev, \

.fs\_desc = &fs\_desc\_##device\_name, \

.hs\_desc = &hs\_desc\_##device\_name, \

}

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

[usb\_device\_descriptor](structusb__device__descriptor.md)

USB Standard Device Descriptor defined in spec.

**Definition** usb\_ch9.h:150

[USB\_SRN\_2\_0](usb__ch9_8h.md#a14527f51ba0e1634b3b477c80e7ae31f)

#define USB\_SRN\_2\_0

**Definition** usb\_ch9.h:270

[USB\_BCD\_DRN](usb__ch9_8h.md#a2f6e90e87d7a1d53418ce084a293e6fc)

#define USB\_BCD\_DRN

USB Device release number (bcdDevice Descriptor field).

**Definition** usb\_ch9.h:277

[USB\_BCC\_MISCELLANEOUS](usb__ch9_8h.md#a62bf5e94c7c36c9d1d94438d7a12a482)

#define USB\_BCC\_MISCELLANEOUS

**Definition** usb\_ch9.h:264

[USB\_CONTROL\_EP\_MPS](usb__ch9_8h.md#a8c4dd61ae766f50c9398c9753b4156b5)

#define USB\_CONTROL\_EP\_MPS

USB Control Endpoints maximum packet size (MPS).

**Definition** usb\_ch9.h:292

[USB\_DESC\_DEVICE](usb__ch9_8h.md#aefeff68c3a236749d1105d94ed9bad68)

#define USB\_DESC\_DEVICE

Descriptor Types defined in spec.

**Definition** usb\_ch9.h:110

Define USB device context structure.

Macro defines a USB device structure needed by the stack to manage its properties and runtime data. The `vid` and `pid` parameters can also be changed using [usbd\_device\_set\_vid()](#ga06aa9f954b6765e07494753bb4fa42d4) and [usbd\_device\_set\_pid()](#ga44719fc03a50c70d75ce65e1d2f77a04).

Example of use:

[USBD\_DEVICE\_DEFINE](#ga26777805f749f29efa882f9bf391473a)(sample\_usbd,

[DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(zephyr\_udc0)),

YOUR\_VID, YOUR\_PID);

[DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)

#define DEVICE\_DT\_GET(node\_id)

Get a device reference from a devicetree node identifier.

**Definition** device.h:255

[DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)

#define DT\_NODELABEL(label)

Get a node identifier for a node label.

**Definition** devicetree.h:196

[USBD\_DEVICE\_DEFINE](#ga26777805f749f29efa882f9bf391473a)

#define USBD\_DEVICE\_DEFINE(device\_name, udc\_dev, vid, pid)

Define USB device context structure.

**Definition** usbd.h:416

Parameters
:   | device\_name | USB device context name |
    | --- | --- |
    | udc\_dev | Pointer to UDC device structure |
    | vid | Vendor ID |
    | pid | Product ID |

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

**Definition** usbd.h:653

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

## Typedef Documentation

## [◆ ](#ga2cd074cefff922b0816de37935d9646e)usbd\_msg\_cb\_t

| typedef void(\* usbd\_msg\_cb\_t) (struct [usbd\_context](structusbd__context.md) \*const ctx, const struct [usbd\_msg](structusbd__msg.md) \*const msg) |
| --- |

`#include <[usbd.h](usbd_8h.md)>`

Callback type definition for USB device message delivery.

The implementation uses the system workqueue, and a callback provided and registered by the application. The application callback is called in the context of the system workqueue. Notification messages are stored in a queue and delivered to the callback in sequence.

Parameters
:   | [in] | ctx | Pointer to USB device support context |
    | --- | --- | --- |
    | [in] | msg | Pointer to USB device message |

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

## [◆ ](#ga2f2da3d634530f08cd59d408c811ad71)usbd\_speed

| enum [usbd\_speed](#ga2f2da3d634530f08cd59d408c811ad71) |
| --- |

`#include <[usbd.h](usbd_8h.md)>`

USB device speed.

| Enumerator | |
| --- | --- |
| USBD\_SPEED\_FS | Device supports or is connected to a full speed bus. |
| USBD\_SPEED\_HS | Device supports or is connected to a high speed bus. |
| USBD\_SPEED\_SS | Device supports or is connected to a super speed bus. |

## Function Documentation

## [◆ ](#ga5f4b69609f9a8f00a9e0fea4dffce1c4)usbd\_add\_configuration()

| int usbd\_add\_configuration | ( | struct [usbd\_context](structusbd__context.md) \* | *uds\_ctx*, |
| --- | --- | --- | --- |
|  |  | const enum [usbd\_speed](#ga2f2da3d634530f08cd59d408c811ad71) | *speed*, |
|  |  | struct [usbd\_config\_node](structusbd__config__node.md) \* | *cd* ) |

`#include <[usbd.h](usbd_8h.md)>`

Add a USB device configuration.

Parameters
:   | [in] | uds\_ctx | Pointer to USB device support context |
    | --- | --- | --- |
    | [in] | speed | Speed at which this configuration operates |
    | [in] | cd | Pointer to USB configuration node |

Returns
:   0 on success, other values on fail.

## [◆ ](#ga33d0cef23d4b6c62b79b41559427b584)usbd\_add\_descriptor()

| int usbd\_add\_descriptor | ( | struct [usbd\_context](structusbd__context.md) \* | *uds\_ctx*, |
| --- | --- | --- | --- |
|  |  | struct [usbd\_desc\_node](structusbd__desc__node.md) \* | *dn* ) |

`#include <[usbd.h](usbd_8h.md)>`

Add common USB descriptor.

Add common descriptor like string or BOS Device Capability.

Parameters
:   | [in] | uds\_ctx | Pointer to USB device support context |
    | --- | --- | --- |
    | [in] | dn | Pointer to USB descriptor node |

Returns
:   0 on success, other values on fail.

## [◆ ](#gab4a0d05a8f183f7479ad33ee29e8a611)usbd\_bus\_speed()

| enum [usbd\_speed](#ga2f2da3d634530f08cd59d408c811ad71) usbd\_bus\_speed | ( | const struct [usbd\_context](structusbd__context.md) \*const | *uds\_ctx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbd.h](usbd_8h.md)>`

Get actual device speed.

Parameters
:   | [in] | uds\_ctx | Pointer to a device context |
    | --- | --- | --- |

Returns
:   Actual device speed

## [◆ ](#ga5ea40d893980e24294e82d22855b407c)usbd\_can\_detect\_vbus()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) usbd\_can\_detect\_vbus | ( | struct [usbd\_context](structusbd__context.md) \*const | *uds\_ctx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbd.h](usbd_8h.md)>`

Check that the controller can detect the VBUS state change.

This can be used in a generic application to explicitly handle the VBUS detected event after [usbd\_init()](#ga78e5f07af641f9610cc32255efe1680f). For example, to call [usbd\_enable()](#ga1a40fc13129e9218ca63ab3ca70d8d68) after a short delay to give the PMIC time to detect the bus, or to handle cases where [usbd\_enable()](#ga1a40fc13129e9218ca63ab3ca70d8d68) can only be called after a VBUS detected event.

Parameters
:   | [in] | uds\_ctx | Pointer to USB device support context |
    | --- | --- | --- |

Returns
:   true if controller can detect VBUS state change, false otherwise

## [◆ ](#gaab7c4692a30b58aa76b03b9e50460856)usbd\_caps\_speed()

| enum [usbd\_speed](#ga2f2da3d634530f08cd59d408c811ad71) usbd\_caps\_speed | ( | const struct [usbd\_context](structusbd__context.md) \*const | *uds\_ctx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbd.h](usbd_8h.md)>`

Get highest speed supported by the controller.

Parameters
:   | [in] | uds\_ctx | Pointer to a device context |
    | --- | --- | --- |

Returns
:   Highest supported speed

## [◆ ](#gaf97c68e75420bd5a1085c047577fd5a7)usbd\_class\_get\_ctx()

| | struct [usbd\_context](structusbd__context.md) \* usbd\_class\_get\_ctx | ( | const struct [usbd\_class\_data](structusbd__class__data.md) \*const | *c\_data* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[usbd.h](usbd_8h.md)>`

Get the USB device runtime context under which the class is registered.

The class implementation must use this function and not access the members of the struct directly.

Parameters
:   | [in] | c\_data | Pointer to USB device class data |
    | --- | --- | --- |

Returns
:   Pointer to USB device runtime context

## [◆ ](#ga2e511d0341b4e1bd57fb4420512eeeb5)usbd\_class\_get\_private()

| | void \* usbd\_class\_get\_private | ( | const struct [usbd\_class\_data](structusbd__class__data.md) \*const | *c\_data* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[usbd.h](usbd_8h.md)>`

Get class implementation private data.

The class implementation must use this function and not access the members of the struct directly.

Parameters
:   | [in] | c\_data | Pointer to USB device class data |
    | --- | --- | --- |

Returns
:   Pointer to class implementation private data

## [◆ ](#ga2b803f8ac10d9375a74949cd2c2f3136)usbd\_config\_attrib\_rwup()

| int usbd\_config\_attrib\_rwup | ( | struct [usbd\_context](structusbd__context.md) \*const | *uds\_ctx*, |
| --- | --- | --- | --- |
|  |  | const enum [usbd\_speed](#ga2f2da3d634530f08cd59d408c811ad71) | *speed*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *cfg*, |
|  |  | const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* ) |

`#include <[usbd.h](usbd_8h.md)>`

Setup USB device configuration attribute Remote Wakeup.

Parameters
:   | [in] | uds\_ctx | Pointer to USB device support context |
    | --- | --- | --- |
    | [in] | speed | Configuration speed |
    | [in] | cfg | Configuration number |
    | [in] | enable | Sets attribute if true, clears it otherwise |

Returns
:   0 on success, other values on fail.

## [◆ ](#ga8b0fff68bc6ce9d8ec4a7dfd59f0eade)usbd\_config\_attrib\_self()

| int usbd\_config\_attrib\_self | ( | struct [usbd\_context](structusbd__context.md) \*const | *uds\_ctx*, |
| --- | --- | --- | --- |
|  |  | const enum [usbd\_speed](#ga2f2da3d634530f08cd59d408c811ad71) | *speed*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *cfg*, |
|  |  | const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* ) |

`#include <[usbd.h](usbd_8h.md)>`

Setup USB device configuration attribute Self-powered.

Parameters
:   | [in] | uds\_ctx | Pointer to USB device support context |
    | --- | --- | --- |
    | [in] | speed | Configuration speed |
    | [in] | cfg | Configuration number |
    | [in] | enable | Sets attribute if true, clears it otherwise |

Returns
:   0 on success, other values on fail.

## [◆ ](#ga59fc1ea6d943d26b0207bb6060e18f08)usbd\_config\_maxpower()

| int usbd\_config\_maxpower | ( | struct [usbd\_context](structusbd__context.md) \*const | *uds\_ctx*, |
| --- | --- | --- | --- |
|  |  | const enum [usbd\_speed](#ga2f2da3d634530f08cd59d408c811ad71) | *speed*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *cfg*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *power* ) |

`#include <[usbd.h](usbd_8h.md)>`

Setup USB device configuration power consumption.

Parameters
:   | [in] | uds\_ctx | Pointer to USB device support context |
    | --- | --- | --- |
    | [in] | speed | Configuration speed |
    | [in] | cfg | Configuration number |
    | [in] | power | Maximum power consumption value (bMaxPower) |

Returns
:   0 on success, other values on fail.

## [◆ ](#gafda88e8a71c52addbe76ebeb874a8af5)usbd\_device\_set\_bcd\_device()

| int usbd\_device\_set\_bcd\_device | ( | struct [usbd\_context](structusbd__context.md) \*const | *uds\_ctx*, |
| --- | --- | --- | --- |
|  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *bcd* ) |

`#include <[usbd.h](usbd_8h.md)>`

Set USB device descriptor value bcdDevice.

Parameters
:   | [in] | uds\_ctx | Pointer to USB device support context |
    | --- | --- | --- |
    | [in] | bcd | bcdDevice value |

Returns
:   0 on success, other values on fail.

## [◆ ](#gacb704bd4f396887c859932b2ab6b4991)usbd\_device\_set\_bcd\_usb()

| int usbd\_device\_set\_bcd\_usb | ( | struct [usbd\_context](structusbd__context.md) \*const | *uds\_ctx*, |
| --- | --- | --- | --- |
|  |  | const enum [usbd\_speed](#ga2f2da3d634530f08cd59d408c811ad71) | *speed*, |
|  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *bcd* ) |

`#include <[usbd.h](usbd_8h.md)>`

Set USB device descriptor value bcdUSB.

Parameters
:   | [in] | uds\_ctx | Pointer to USB device support context |
    | --- | --- | --- |
    | [in] | speed | Speed for which the bcdUSB should be set |
    | [in] | bcd | bcdUSB value |

Returns
:   0 on success, other values on fail.

## [◆ ](#ga83a58b50bec680513eabd3bb7075b511)usbd\_device\_set\_code\_triple()

| int usbd\_device\_set\_code\_triple | ( | struct [usbd\_context](structusbd__context.md) \*const | *uds\_ctx*, |
| --- | --- | --- | --- |
|  |  | const enum [usbd\_speed](#ga2f2da3d634530f08cd59d408c811ad71) | *speed*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *base\_class*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *subclass*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *protocol* ) |

`#include <[usbd.h](usbd_8h.md)>`

Set USB device descriptor code triple Base Class, SubClass, and Protocol.

Parameters
:   | [in] | uds\_ctx | Pointer to USB device support context |
    | --- | --- | --- |
    | [in] | speed | Speed for which the code triple should be set |
    | [in] | base\_class | bDeviceClass value |
    | [in] | subclass | bDeviceSubClass value |
    | [in] | protocol | bDeviceProtocol value |

Returns
:   0 on success, other values on fail.

## [◆ ](#ga44719fc03a50c70d75ce65e1d2f77a04)usbd\_device\_set\_pid()

| int usbd\_device\_set\_pid | ( | struct [usbd\_context](structusbd__context.md) \*const | *uds\_ctx*, |
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

## [◆ ](#ga06aa9f954b6765e07494753bb4fa42d4)usbd\_device\_set\_vid()

| int usbd\_device\_set\_vid | ( | struct [usbd\_context](structusbd__context.md) \*const | *uds\_ctx*, |
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

## [◆ ](#gaaa21e9f33175b7d2434e54e1b3d2799b)usbd\_disable()

| int usbd\_disable | ( | struct [usbd\_context](structusbd__context.md) \* | *uds\_ctx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbd.h](usbd_8h.md)>`

Disable the USB device support.

This function disables the USB device support.

Parameters
:   | [in] | uds\_ctx | Pointer to USB device support context |
    | --- | --- | --- |

Returns
:   0 on success, other values on fail.

## [◆ ](#ga1a40fc13129e9218ca63ab3ca70d8d68)usbd\_enable()

| int usbd\_enable | ( | struct [usbd\_context](structusbd__context.md) \* | *uds\_ctx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbd.h](usbd_8h.md)>`

Enable the USB device support and registered class instances.

This function enables the USB device support.

Parameters
:   | [in] | uds\_ctx | Pointer to USB device support context |
    | --- | --- | --- |

Returns
:   0 on success, other values on fail.

## [◆ ](#ga6c671d49c811b0af6b809f5940cd6d70)usbd\_ep\_buf\_alloc()

| struct [net\_buf](structnet__buf.md) \* usbd\_ep\_buf\_alloc | ( | const struct [usbd\_class\_data](structusbd__class__data.md) \*const | *c\_data*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ep*, |
|  |  | const [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[usbd.h](usbd_8h.md)>`

Allocate buffer for USB device request.

Allocate a new buffer from controller's driver buffer pool.

Parameters
:   | [in] | c\_data | Pointer to USB device class data |
    | --- | --- | --- |
    | [in] | ep | Endpoint address |
    | [in] | size | Size of the request buffer |

Returns
:   pointer to allocated request or NULL on error.

## [◆ ](#ga8aa454c24495f2a462eae53b78c488dc)usbd\_ep\_buf\_free()

| int usbd\_ep\_buf\_free | ( | struct [usbd\_context](structusbd__context.md) \* | *uds\_ctx*, |
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

## [◆ ](#ga03729a4e9add3a55a7c3c2c8666a53a7)usbd\_ep\_clear\_halt()

| int usbd\_ep\_clear\_halt | ( | struct [usbd\_context](structusbd__context.md) \* | *uds\_ctx*, |
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

## [◆ ](#ga967d507d82d912119a732fd230bd561e)usbd\_ep\_ctrl\_enqueue()

| int usbd\_ep\_ctrl\_enqueue | ( | struct [usbd\_context](structusbd__context.md) \*const | *uds\_ctx*, |
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

## [◆ ](#ga1534058a609794e1d080aed98fcf5823)usbd\_ep\_dequeue()

| int usbd\_ep\_dequeue | ( | struct [usbd\_context](structusbd__context.md) \* | *uds\_ctx*, |
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

## [◆ ](#gaabf8333a7aefc4428f38e79a7264e383)usbd\_ep\_enqueue()

| int usbd\_ep\_enqueue | ( | const struct [usbd\_class\_data](structusbd__class__data.md) \*const | *c\_data*, |
| --- | --- | --- | --- |
|  |  | struct [net\_buf](structnet__buf.md) \*const | *buf* ) |

`#include <[usbd.h](usbd_8h.md)>`

Queue USB device request.

Add request to the queue.

Parameters
:   | [in] | c\_data | Pointer to USB device class data |
    | --- | --- | --- |
    | [in] | buf | Pointer to UDC request buffer |

Returns
:   0 on success, or error from [udc\_ep\_enqueue()](group__udc__api.md#gacb2dc96353f1cffcc3d5e9710133fc0d "Queue USB device controller request.")

## [◆ ](#ga94cb8465b7bf85457f29e84b5b8ddfe9)usbd\_ep\_is\_halted()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) usbd\_ep\_is\_halted | ( | struct [usbd\_context](structusbd__context.md) \* | *uds\_ctx*, |
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

## [◆ ](#ga176f42b2dd221c0de28ad9122a7d2693)usbd\_ep\_set\_halt()

| int usbd\_ep\_set\_halt | ( | struct [usbd\_context](structusbd__context.md) \* | *uds\_ctx*, |
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

## [◆ ](#ga78e5f07af641f9610cc32255efe1680f)usbd\_init()

| int usbd\_init | ( | struct [usbd\_context](structusbd__context.md) \* | *uds\_ctx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbd.h](usbd_8h.md)>`

Initialize USB device.

Initialize USB device descriptors and configuration, initialize USB device controller. Class instances should be registered before they are involved. However, the stack should also initialize without registered instances, even if the host would complain about missing interfaces.

Parameters
:   | [in] | uds\_ctx | Pointer to USB device support context |
    | --- | --- | --- |

Returns
:   0 on success, other values on fail.

## [◆ ](#ga5f7a5af958f7de8893e04ff2b7748c7e)usbd\_is\_suspended()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) usbd\_is\_suspended | ( | struct [usbd\_context](structusbd__context.md) \* | *uds\_ctx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbd.h](usbd_8h.md)>`

Checks whether the USB device controller is suspended.

Parameters
:   | [in] | uds\_ctx | Pointer to USB device support context |
    | --- | --- | --- |

Returns
:   true if endpoint is halted, false otherwise

## [◆ ](#ga2ebe08b8bf5ff3b64c4df1fcb346cf38)usbd\_msg\_register\_cb()

| int usbd\_msg\_register\_cb | ( | struct [usbd\_context](structusbd__context.md) \*const | *uds\_ctx*, |
| --- | --- | --- | --- |
|  |  | const [usbd\_msg\_cb\_t](#ga2cd074cefff922b0816de37935d9646e) | *cb* ) |

`#include <[usbd.h](usbd_8h.md)>`

Register USB notification message callback.

Parameters
:   | [in] | uds\_ctx | Pointer to USB device support context |
    | --- | --- | --- |
    | [in] | cb | Pointer to message callback function |

Returns
:   0 on success, other values on fail.

## [◆ ](#ga4382a5b4888baf65045faea0b88723f3)usbd\_register\_all\_classes()

| int usbd\_register\_all\_classes | ( | struct [usbd\_context](structusbd__context.md) \* | *uds\_ctx*, |
| --- | --- | --- | --- |
|  |  | const enum [usbd\_speed](#ga2f2da3d634530f08cd59d408c811ad71) | *speed*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *cfg* ) |

`#include <[usbd.h](usbd_8h.md)>`

Register all available USB class instances.

Register all available instances. Like usbd\_register\_class, but does not take the instance name and instead registers all available instances.

Note
:   This cannot be combined. If your application calls usbd\_register\_class for any device, configuration number, or instance, either usbd\_register\_class or this function will fail.

Parameters
:   | [in] | uds\_ctx | Pointer to USB device support context |
    | --- | --- | --- |
    | [in] | speed | Configuration speed |
    | [in] | cfg | Configuration value (bConfigurationValue) |

Returns
:   0 on success, other values on fail.

## [◆ ](#ga4a837040e9d02c5773d69a6cf6c35960)usbd\_register\_class()

| int usbd\_register\_class | ( | struct [usbd\_context](structusbd__context.md) \* | *uds\_ctx*, |
| --- | --- | --- | --- |
|  |  | const char \* | *name*, |
|  |  | const enum [usbd\_speed](#ga2f2da3d634530f08cd59d408c811ad71) | *speed*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *cfg* ) |

`#include <[usbd.h](usbd_8h.md)>`

Register an USB class instance.

An USB class implementation can have one or more instances. To identify the instances we use device drivers API. Device names have a prefix derived from the name of the class, for example CDC\_ACM for CDC ACM class instance, and can also be easily identified in the shell. Class instance can only be registered when the USB device stack is disabled. Registered instances are initialized at initialization of the USB device stack, and the interface descriptors of each instance are adapted to the whole context.

Parameters
:   | [in] | uds\_ctx | Pointer to USB device support context |
    | --- | --- | --- |
    | [in] | name | Class instance name |
    | [in] | speed | Configuration speed |
    | [in] | cfg | Configuration value (bConfigurationValue) |

Returns
:   0 on success, other values on fail.

## [◆ ](#ga3146ee636b84c6d319365716f5741363)usbd\_remove\_descriptor()

| void usbd\_remove\_descriptor | ( | struct [usbd\_desc\_node](structusbd__desc__node.md) \*const | *desc\_nd* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbd.h](usbd_8h.md)>`

Remove USB string descriptor.

Remove linked USB string descriptor from any list.

Parameters
:   | [in] | desc\_nd | Pointer to USB descriptor node |
    | --- | --- | --- |

## [◆ ](#ga37585e0124a4d0d8cf6e65f13325eaf0)usbd\_shutdown()

| int usbd\_shutdown | ( | struct [usbd\_context](structusbd__context.md) \*const | *uds\_ctx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbd.h](usbd_8h.md)>`

Shutdown the USB device support.

This function completely disables the USB device support.

Parameters
:   | [in] | uds\_ctx | Pointer to USB device support context |
    | --- | --- | --- |

Returns
:   0 on success, other values on fail.

## [◆ ](#gab023ab276eb68c644895483344d33948)usbd\_str\_desc\_get\_idx()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) usbd\_str\_desc\_get\_idx | ( | const struct [usbd\_desc\_node](structusbd__desc__node.md) \*const | *desc\_nd* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbd.h](usbd_8h.md)>`

Get USB string descriptor index from descriptor node.

Parameters
:   | [in] | desc\_nd | Pointer to USB descriptor node |
    | --- | --- | --- |

Returns
:   Descriptor index, 0 if descriptor is not part of any device

## [◆ ](#ga2996b5f6df459c8a179fc6c22f944063)usbd\_unregister\_all\_classes()

| int usbd\_unregister\_all\_classes | ( | struct [usbd\_context](structusbd__context.md) \* | *uds\_ctx*, |
| --- | --- | --- | --- |
|  |  | const enum [usbd\_speed](#ga2f2da3d634530f08cd59d408c811ad71) | *speed*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *cfg* ) |

`#include <[usbd.h](usbd_8h.md)>`

Unregister all available USB class instances.

Unregister all available instances. Like usbd\_unregister\_class, but does not take the instance name and instead unregisters all available instances.

Parameters
:   | [in] | uds\_ctx | Pointer to USB device support context |
    | --- | --- | --- |
    | [in] | speed | Configuration speed |
    | [in] | cfg | Configuration value (bConfigurationValue) |

Returns
:   0 on success, other values on fail.

## [◆ ](#ga1ae7a7a04f4ec1206d352d5c6401c51b)usbd\_unregister\_class()

| int usbd\_unregister\_class | ( | struct [usbd\_context](structusbd__context.md) \* | *uds\_ctx*, |
| --- | --- | --- | --- |
|  |  | const char \* | *name*, |
|  |  | const enum [usbd\_speed](#ga2f2da3d634530f08cd59d408c811ad71) | *speed*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *cfg* ) |

`#include <[usbd.h](usbd_8h.md)>`

Unregister an USB class instance.

USB class instance will be removed and will not appear on the next start of the stack. Instance can only be unregistered when the USB device stack is disabled.

Parameters
:   | [in] | uds\_ctx | Pointer to USB device support context |
    | --- | --- | --- |
    | [in] | name | Class instance name |
    | [in] | speed | Configuration speed |
    | [in] | cfg | Configuration value (bConfigurationValue) |

Returns
:   0 on success, other values on fail.

## [◆ ](#ga34086553e74795ffdc000349e61a3c8b)usbd\_wakeup\_request()

| int usbd\_wakeup\_request | ( | struct [usbd\_context](structusbd__context.md) \* | *uds\_ctx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usbd.h](usbd_8h.md)>`

Initiate the USB remote wakeup (TBD).

Returns
:   0 on success, other values on fail.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
