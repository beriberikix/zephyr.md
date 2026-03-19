---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/usbd_8h.html
original_path: doxygen/html/usbd_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbd.h File Reference

New experimental USB device stack APIs and structures.
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/usb/bos.h](bos_8h_source.md)>`  
`#include <[zephyr/usb/usb_ch9.h](usb__ch9_8h_source.md)>`  
`#include <[zephyr/usb/usbd_msg.h](usbd__msg_8h_source.md)>`  
`#include <[zephyr/drivers/usb/udc_buf.h](udc__buf_8h_source.md)>`  
`#include <[zephyr/sys/byteorder.h](sys_2byteorder_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`  
`#include <[zephyr/logging/log.h](log_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`

[Go to the source code of this file.](usbd_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [usbd\_str\_desc\_data](structusbd__str__desc__data.md) |
|  | Used internally to keep descriptors in order. [More...](structusbd__str__desc__data.md#details) |
| struct | [usbd\_vreq\_node](structusbd__vreq__node.md) |
|  | USBD vendor request node. [More...](structusbd__vreq__node.md#details) |
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
| #define | [USB\_BSTRING\_LENGTH](group__usbd__api.md#gac3d58cfa3f92b1811e9ed136c4450906)([s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)) |
| #define | [USB\_STRING\_DESCRIPTOR\_LENGTH](group__usbd__api.md#gaef85e50556291fa93cbf72b01529b4a8)([s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)) |
| #define | [USBD\_NUMOF\_INTERFACES\_MAX](group__usbd__api.md#gaf8aadd499f7e0438acac4a7f36645d49)   16U |
| #define | [USBD\_CCTX\_REGISTERED](group__usbd__api.md#ga588b9e156a49d3b0358bee185cdeebee)   0 |
|  | USB Class instance registered flag. |
| #define | [USBD\_DEVICE\_DEFINE](group__usbd__api.md#ga26777805f749f29efa882f9bf391473a)(device\_name, udc\_dev, vid, pid) |
|  | Define USB device context structure. |
| #define | [USBD\_CONFIGURATION\_DEFINE](group__usbd__api.md#ga2d98fd68eff66f36522688f3de527586)(name, attrib, power, desc\_nd) |
|  | Define USB device configuration. |
| #define | [USBD\_DESC\_LANG\_DEFINE](group__usbd__api.md#gaec816a27118bcb289ab4840fcd22888e)(name) |
|  | Create a string descriptor node and language string descriptor. |
| #define | [USBD\_DESC\_STRING\_DEFINE](group__usbd__api.md#gaf800e2040ac30844cab463c13d1fcdf8)(d\_name, d\_string, d\_utype) |
|  | Create a string descriptor. |
| #define | [USBD\_DESC\_MANUFACTURER\_DEFINE](group__usbd__api.md#ga18b1321daf1173a3cb0bc61a0d9beb34)(d\_name, d\_string) |
|  | Create a string descriptor node and manufacturer string descriptor. |
| #define | [USBD\_DESC\_PRODUCT\_DEFINE](group__usbd__api.md#gaa5e43f9eac8f91d3896ea5e19baed031)(d\_name, d\_string) |
|  | Create a string descriptor node and product string descriptor. |
| #define | [USBD\_DESC\_SERIAL\_NUMBER\_DEFINE](group__usbd__api.md#ga26af7f93205dc78eeb60a3c09aa7b2d3)(d\_name) |
|  | Create a string descriptor node and serial number string descriptor. |
| #define | [USBD\_DESC\_CONFIG\_DEFINE](group__usbd__api.md#ga45dc8df18f6fdf72edfd21f35d3046db)(d\_name, d\_string) |
|  | Create a string descriptor node for configuration descriptor. |
| #define | [USBD\_DESC\_BOS\_DEFINE](group__usbd__api.md#ga620a5aa567dc4de7d5d1ef6b0cd9e937)(name, len, subset) |
|  | Define BOS Device Capability descriptor node. |
| #define | [USBD\_VREQUEST\_DEFINE](group__usbd__api.md#ga0bdfa97d67ee62aa32af5fad2670a8a0)(name, vcode, vto\_host, vto\_dev) |
|  | Define a vendor request with recipient device. |
| #define | [USBD\_DESC\_BOS\_VREQ\_DEFINE](group__usbd__api.md#ga0481d759856a0dc4b937335e8768eedd)(name, len, subset, vcode, vto\_host, vto\_dev) |
|  | Define BOS Device Capability descriptor node with vendor request. |
| #define | [USBD\_DEFINE\_CLASS](group__usbd__api.md#gaaebebc77106848d8d62016936399776a)(class\_name, class\_api, class\_priv, class\_v\_reqs) |
|  | Define USB device support class data. |
| #define | [VENDOR\_REQ\_DEFINE](group__usbd__api.md#ga54ca08c74ae715281381d878f828727e)(\_reqs, \_len) |
|  | Helper to declare request table of [usbd\_cctx\_vendor\_req](structusbd__cctx__vendor__req.md "Vendor Requests Table."). |
| #define | [USBD\_VENDOR\_REQ](group__usbd__api.md#ga464933a8332c11d15c92914aa1790e10)(\_reqs...) |
|  | Helper to declare supported vendor requests. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [usbd\_msg\_cb\_t](group__usbd__api.md#ga2cd074cefff922b0816de37935d9646e)) (struct [usbd\_context](structusbd__context.md) \*const ctx, const struct [usbd\_msg](structusbd__msg.md) \*const msg) |
|  | Callback type definition for USB device message delivery. |

| Enumerations | |
| --- | --- |
| enum | [usbd\_ch9\_state](group__usbd__api.md#ga95fb708d8a54eaa3ce0acc4e65519bbc) { [USBD\_STATE\_DEFAULT](group__usbd__api.md#gga95fb708d8a54eaa3ce0acc4e65519bbca978c707d313eb49b70bc62dfae304048) = 0 , [USBD\_STATE\_ADDRESS](group__usbd__api.md#gga95fb708d8a54eaa3ce0acc4e65519bbca985f06c5505c5684a98954f15701cc9d) , [USBD\_STATE\_CONFIGURED](group__usbd__api.md#gga95fb708d8a54eaa3ce0acc4e65519bbca44c1920b09ea1062ea4d7ac31a846509) } |
|  | USB device support middle layer runtime state. [More...](group__usbd__api.md#ga95fb708d8a54eaa3ce0acc4e65519bbc) |
| enum | [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) { [USBD\_SPEED\_FS](group__usbd__api.md#gga2f2da3d634530f08cd59d408c811ad71a30b20b0839dff88b038e680b55f382d7) , [USBD\_SPEED\_HS](group__usbd__api.md#gga2f2da3d634530f08cd59d408c811ad71abaf4bdba11db59d804d753e6fac92266) , [USBD\_SPEED\_SS](group__usbd__api.md#gga2f2da3d634530f08cd59d408c811ad71a195490bdfa76ffca418e8bf2f3d3c96a) } |
|  | USB device speed. [More...](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) |

| Functions | |
| --- | --- |
| static struct [usbd\_context](structusbd__context.md) \* | [usbd\_class\_get\_ctx](group__usbd__api.md#gaf97c68e75420bd5a1085c047577fd5a7) (const struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data) |
|  | Get the USB device runtime context under which the class is registered. |
| static void \* | [usbd\_class\_get\_private](group__usbd__api.md#ga2e511d0341b4e1bd57fb4420512eeeb5) (const struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data) |
|  | Get class implementation private data. |
| int | [usbd\_add\_descriptor](group__usbd__api.md#ga33d0cef23d4b6c62b79b41559427b584) (struct [usbd\_context](structusbd__context.md) \*uds\_ctx, struct [usbd\_desc\_node](structusbd__desc__node.md) \*dn) |
|  | Add common USB descriptor. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [usbd\_str\_desc\_get\_idx](group__usbd__api.md#gab023ab276eb68c644895483344d33948) (const struct [usbd\_desc\_node](structusbd__desc__node.md) \*const desc\_nd) |
|  | Get USB string descriptor index from descriptor node. |
| void | [usbd\_remove\_descriptor](group__usbd__api.md#ga3146ee636b84c6d319365716f5741363) (struct [usbd\_desc\_node](structusbd__desc__node.md) \*const desc\_nd) |
|  | Remove USB string descriptor. |
| int | [usbd\_add\_configuration](group__usbd__api.md#ga5f4b69609f9a8f00a9e0fea4dffce1c4) (struct [usbd\_context](structusbd__context.md) \*uds\_ctx, const enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) speed, struct [usbd\_config\_node](structusbd__config__node.md) \*cd) |
|  | Add a USB device configuration. |
| int | [usbd\_register\_class](group__usbd__api.md#ga4a837040e9d02c5773d69a6cf6c35960) (struct [usbd\_context](structusbd__context.md) \*uds\_ctx, const char \*name, const enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) speed, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cfg) |
|  | Register an USB class instance. |
| int | [usbd\_register\_all\_classes](group__usbd__api.md#ga06541b17f5afc917cc5154bd4d816ec3) (struct [usbd\_context](structusbd__context.md) \*uds\_ctx, const enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) speed, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cfg, const char \*const blocklist[]) |
|  | Register all available USB class instances. |
| int | [usbd\_unregister\_class](group__usbd__api.md#ga1ae7a7a04f4ec1206d352d5c6401c51b) (struct [usbd\_context](structusbd__context.md) \*uds\_ctx, const char \*name, const enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) speed, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cfg) |
|  | Unregister an USB class instance. |
| int | [usbd\_unregister\_all\_classes](group__usbd__api.md#ga2996b5f6df459c8a179fc6c22f944063) (struct [usbd\_context](structusbd__context.md) \*uds\_ctx, const enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) speed, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cfg) |
|  | Unregister all available USB class instances. |
| int | [usbd\_msg\_register\_cb](group__usbd__api.md#ga2ebe08b8bf5ff3b64c4df1fcb346cf38) (struct [usbd\_context](structusbd__context.md) \*const uds\_ctx, const [usbd\_msg\_cb\_t](group__usbd__api.md#ga2cd074cefff922b0816de37935d9646e) cb) |
|  | Register USB notification message callback. |
| int | [usbd\_init](group__usbd__api.md#ga78e5f07af641f9610cc32255efe1680f) (struct [usbd\_context](structusbd__context.md) \*uds\_ctx) |
|  | Initialize USB device. |
| int | [usbd\_enable](group__usbd__api.md#ga1a40fc13129e9218ca63ab3ca70d8d68) (struct [usbd\_context](structusbd__context.md) \*uds\_ctx) |
|  | Enable the USB device support and registered class instances. |
| int | [usbd\_disable](group__usbd__api.md#gaaa21e9f33175b7d2434e54e1b3d2799b) (struct [usbd\_context](structusbd__context.md) \*uds\_ctx) |
|  | Disable the USB device support. |
| int | [usbd\_shutdown](group__usbd__api.md#ga37585e0124a4d0d8cf6e65f13325eaf0) (struct [usbd\_context](structusbd__context.md) \*const uds\_ctx) |
|  | Shutdown the USB device support. |
| int | [usbd\_ep\_set\_halt](group__usbd__api.md#ga176f42b2dd221c0de28ad9122a7d2693) (struct [usbd\_context](structusbd__context.md) \*uds\_ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Halt endpoint. |
| int | [usbd\_ep\_clear\_halt](group__usbd__api.md#ga03729a4e9add3a55a7c3c2c8666a53a7) (struct [usbd\_context](structusbd__context.md) \*uds\_ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Clear endpoint halt. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [usbd\_ep\_is\_halted](group__usbd__api.md#ga94cb8465b7bf85457f29e84b5b8ddfe9) (struct [usbd\_context](structusbd__context.md) \*uds\_ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Checks whether the endpoint is halted. |
| struct [net\_buf](structnet__buf.md) \* | [usbd\_ep\_buf\_alloc](group__usbd__api.md#ga6c671d49c811b0af6b809f5940cd6d70) (const struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, const [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Allocate buffer for USB device request. |
| int | [usbd\_ep\_ctrl\_enqueue](group__usbd__api.md#ga967d507d82d912119a732fd230bd561e) (struct [usbd\_context](structusbd__context.md) \*const uds\_ctx, struct [net\_buf](structnet__buf.md) \*const buf) |
|  | Queue USB device control request. |
| int | [usbd\_ep\_enqueue](group__usbd__api.md#gaabf8333a7aefc4428f38e79a7264e383) (const struct [usbd\_class\_data](structusbd__class__data.md) \*const c\_data, struct [net\_buf](structnet__buf.md) \*const buf) |
|  | Queue USB device request. |
| int | [usbd\_ep\_dequeue](group__usbd__api.md#ga1534058a609794e1d080aed98fcf5823) (struct [usbd\_context](structusbd__context.md) \*uds\_ctx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Remove all USB device controller requests from endpoint queue. |
| int | [usbd\_ep\_buf\_free](group__usbd__api.md#ga8aa454c24495f2a462eae53b78c488dc) (struct [usbd\_context](structusbd__context.md) \*uds\_ctx, struct [net\_buf](structnet__buf.md) \*buf) |
|  | Free USB device request buffer. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [usbd\_is\_suspended](group__usbd__api.md#ga5f7a5af958f7de8893e04ff2b7748c7e) (struct [usbd\_context](structusbd__context.md) \*uds\_ctx) |
|  | Checks whether the USB device controller is suspended. |
| int | [usbd\_wakeup\_request](group__usbd__api.md#ga34086553e74795ffdc000349e61a3c8b) (struct [usbd\_context](structusbd__context.md) \*uds\_ctx) |
|  | Initiate the USB remote wakeup (TBD). |
| void | [usbd\_self\_powered](group__usbd__api.md#ga9056e1f01b64ddd26db6a5ee45439e22) (struct [usbd\_context](structusbd__context.md) \*uds\_ctx, const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) status) |
|  | Set the self-powered status of the USB device. |
| enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) | [usbd\_bus\_speed](group__usbd__api.md#gab4a0d05a8f183f7479ad33ee29e8a611) (const struct [usbd\_context](structusbd__context.md) \*const uds\_ctx) |
|  | Get actual device speed. |
| enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) | [usbd\_caps\_speed](group__usbd__api.md#gaab7c4692a30b58aa76b03b9e50460856) (const struct [usbd\_context](structusbd__context.md) \*const uds\_ctx) |
|  | Get highest speed supported by the controller. |
| int | [usbd\_device\_set\_bcd\_usb](group__usbd__api.md#gacb704bd4f396887c859932b2ab6b4991) (struct [usbd\_context](structusbd__context.md) \*const uds\_ctx, const enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) speed, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bcd) |
|  | Set USB device descriptor value bcdUSB. |
| int | [usbd\_device\_set\_vid](group__usbd__api.md#ga06aa9f954b6765e07494753bb4fa42d4) (struct [usbd\_context](structusbd__context.md) \*const uds\_ctx, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vid) |
|  | Set USB device descriptor value idVendor. |
| int | [usbd\_device\_set\_pid](group__usbd__api.md#ga44719fc03a50c70d75ce65e1d2f77a04) (struct [usbd\_context](structusbd__context.md) \*const uds\_ctx, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) pid) |
|  | Set USB device descriptor value idProduct. |
| int | [usbd\_device\_set\_bcd\_device](group__usbd__api.md#gafda88e8a71c52addbe76ebeb874a8af5) (struct [usbd\_context](structusbd__context.md) \*const uds\_ctx, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bcd) |
|  | Set USB device descriptor value bcdDevice. |
| int | [usbd\_device\_set\_code\_triple](group__usbd__api.md#ga83a58b50bec680513eabd3bb7075b511) (struct [usbd\_context](structusbd__context.md) \*const uds\_ctx, const enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) speed, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) base\_class, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) subclass, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) protocol) |
|  | Set USB device descriptor code triple Base Class, SubClass, and Protocol. |
| int | [usbd\_config\_attrib\_rwup](group__usbd__api.md#ga2b803f8ac10d9375a74949cd2c2f3136) (struct [usbd\_context](structusbd__context.md) \*const uds\_ctx, const enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) speed, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cfg, const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Setup USB device configuration attribute Remote Wakeup. |
| int | [usbd\_config\_attrib\_self](group__usbd__api.md#ga8b0fff68bc6ce9d8ec4a7dfd59f0eade) (struct [usbd\_context](structusbd__context.md) \*const uds\_ctx, const enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) speed, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cfg, const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Setup USB device configuration attribute Self-powered. |
| int | [usbd\_config\_maxpower](group__usbd__api.md#ga59fc1ea6d943d26b0207bb6060e18f08) (struct [usbd\_context](structusbd__context.md) \*const uds\_ctx, const enum [usbd\_speed](group__usbd__api.md#ga2f2da3d634530f08cd59d408c811ad71) speed, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cfg, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) power) |
|  | Setup USB device configuration power consumption. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [usbd\_can\_detect\_vbus](group__usbd__api.md#ga5ea40d893980e24294e82d22855b407c) (struct [usbd\_context](structusbd__context.md) \*const uds\_ctx) |
|  | Check that the controller can detect the VBUS state change. |
| int | [usbd\_device\_register\_vreq](group__usbd__api.md#gaaebba63d8a8b78a1f06c1a5a476cd306) (struct [usbd\_context](structusbd__context.md) \*const uds\_ctx, struct [usbd\_vreq\_node](structusbd__vreq__node.md) \*const vreq\_nd) |
|  | Register an USB vendor request with recipient device. |

## Detailed Description

New experimental USB device stack APIs and structures.

This file contains the USB device stack APIs and structures.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [usb](dir_d8285a9da4e2f530d10dd4c17d446a84.md)
- [usbd.h](usbd_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
