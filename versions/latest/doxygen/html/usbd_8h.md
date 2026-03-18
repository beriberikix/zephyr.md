---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/usbd_8h.html
original_path: doxygen/html/usbd_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usbd.h File Reference

New experimental USB device stack APIs and structures.
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/usb/usb_ch9.h](usb__ch9_8h_source.md)>`  
`#include <[zephyr/net/buf.h](net_2buf_8h_source.md)>`  
`#include <[zephyr/sys/byteorder.h](sys_2byteorder_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`  
`#include <[zephyr/logging/log.h](log_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`

[Go to the source code of this file.](usbd_8h_source.md)

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
| #define | [USB\_BSTRING\_LENGTH](group__usbd__api.md#gac3d58cfa3f92b1811e9ed136c4450906)([s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)) |
| #define | [USB\_STRING\_DESCRIPTOR\_LENGTH](group__usbd__api.md#gaef85e50556291fa93cbf72b01529b4a8)([s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)) |
| #define | [USBD\_NUMOF\_INTERFACES\_MAX](group__usbd__api.md#gaf8aadd499f7e0438acac4a7f36645d49)   16U |
| #define | [USBD\_CCTX\_REGISTERED](group__usbd__api.md#ga588b9e156a49d3b0358bee185cdeebee)   0 |
|  | USB Class instance registered flag. |
| #define | [USBD\_DEVICE\_DEFINE](group__usbd__api.md#gaa202fc8ae1e5585abedbde733e63ccb7)(device\_name, uhc\_dev, vid, pid) |
| #define | [USBD\_CONFIGURATION\_DEFINE](group__usbd__api.md#ga5db99c7ff31ff9ef893f219d209128c7)(name, attrib, power) |
| #define | [USBD\_DESC\_LANG\_DEFINE](group__usbd__api.md#gaec816a27118bcb289ab4840fcd22888e)(name) |
|  | Create a string descriptor node and language string descriptor. |
| #define | [USBD\_DESC\_STRING\_DEFINE](group__usbd__api.md#gaf800e2040ac30844cab463c13d1fcdf8)(d\_name, d\_string, d\_utype) |
| #define | [USBD\_DESC\_MANUFACTURER\_DEFINE](group__usbd__api.md#ga18b1321daf1173a3cb0bc61a0d9beb34)(d\_name, d\_string) |
|  | Create a string descriptor node and manufacturer string descriptor. |
| #define | [USBD\_DESC\_PRODUCT\_DEFINE](group__usbd__api.md#gaa5e43f9eac8f91d3896ea5e19baed031)(d\_name, d\_string) |
|  | Create a string descriptor node and product string descriptor. |
| #define | [USBD\_DESC\_SERIAL\_NUMBER\_DEFINE](group__usbd__api.md#ga98e3b788b4bc38d0ac199a67fdc302d0)(d\_name, d\_string) |
|  | Create a string descriptor node and serial number string descriptor. |
| #define | [USBD\_DEFINE\_CLASS](group__usbd__api.md#gaab136394168b115c0e061261651c4146)(class\_name, class\_api, class\_data) |
| #define | [VENDOR\_REQ\_DEFINE](group__usbd__api.md#ga54ca08c74ae715281381d878f828727e)(\_reqs, \_len) |
|  | Helper to declare request table of [usbd\_cctx\_vendor\_req](structusbd__cctx__vendor__req.md "Vendor Requests Table."). |
| #define | [USBD\_VENDOR\_REQ](group__usbd__api.md#ga464933a8332c11d15c92914aa1790e10)(\_reqs...) |
|  | Helper to declare supported vendor requests. |

| Enumerations | |
| --- | --- |
| enum | [usbd\_desc\_usage\_type](group__usbd__api.md#gaa7ed6f04fd7058c422f5ebc378f1a3da) {     [USBD\_DUT\_STRING\_LANG](group__usbd__api.md#ggaa7ed6f04fd7058c422f5ebc378f1a3daa984cc2f845e2e2bcc83d2e9f0138e3bd) , [USBD\_DUT\_STRING\_MANUFACTURER](group__usbd__api.md#ggaa7ed6f04fd7058c422f5ebc378f1a3daa25eb10630b10db28f9f97aa0b81f3c4e) , [USBD\_DUT\_STRING\_PRODUCT](group__usbd__api.md#ggaa7ed6f04fd7058c422f5ebc378f1a3daa67c8a16639167a0a7a6f615d5aa6b73e) , [USBD\_DUT\_STRING\_SERIAL\_NUMBER](group__usbd__api.md#ggaa7ed6f04fd7058c422f5ebc378f1a3daac4fff2e4994a473899aea6ed8a0ec782) ,     [USBD\_DUT\_STRING\_INTERFACE](group__usbd__api.md#ggaa7ed6f04fd7058c422f5ebc378f1a3daaa4dd69c222492b1f12b3993c4640c80d)   } |
| enum | [usbd\_ch9\_state](group__usbd__api.md#ga95fb708d8a54eaa3ce0acc4e65519bbc) { [USBD\_STATE\_DEFAULT](group__usbd__api.md#gga95fb708d8a54eaa3ce0acc4e65519bbca978c707d313eb49b70bc62dfae304048) = 0 , [USBD\_STATE\_ADDRESS](group__usbd__api.md#gga95fb708d8a54eaa3ce0acc4e65519bbca985f06c5505c5684a98954f15701cc9d) , [USBD\_STATE\_CONFIGURED](group__usbd__api.md#gga95fb708d8a54eaa3ce0acc4e65519bbca44c1920b09ea1062ea4d7ac31a846509) } |
|  | USB device support middle layer runtime state. [More...](group__usbd__api.md#ga95fb708d8a54eaa3ce0acc4e65519bbc) |

| Functions | |
| --- | --- |
| int | [usbd\_add\_descriptor](group__usbd__api.md#ga0280dbaf6f15e4bc789279b8d93bfff8) (struct [usbd\_contex](structusbd__contex.md) \*uds\_ctx, struct [usbd\_desc\_node](structusbd__desc__node.md) \*dn) |
|  | Add common USB descriptor. |
| int | [usbd\_add\_configuration](group__usbd__api.md#gae1472960a22e84a49865639dff5816a0) (struct [usbd\_contex](structusbd__contex.md) \*uds\_ctx, struct [usbd\_config\_node](structusbd__config__node.md) \*cd) |
|  | Add a USB device configuration. |
| int | [usbd\_register\_class](group__usbd__api.md#ga3640cb8425961a8038c225e1daea34a3) (struct [usbd\_contex](structusbd__contex.md) \*uds\_ctx, const char \*name, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cfg) |
|  | Register an USB class instance. |
| int | [usbd\_unregister\_class](group__usbd__api.md#gadf7cc0edc2d046f0b50e65fcc007f982) (struct [usbd\_contex](structusbd__contex.md) \*uds\_ctx, const char \*name, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cfg) |
|  | Unregister an USB class instance. |
| int | [usbd\_init](group__usbd__api.md#gaf3cd6c12317f9d94ee98f2809d2a0e04) (struct [usbd\_contex](structusbd__contex.md) \*uds\_ctx) |
|  | Initialize USB device. |
| int | [usbd\_enable](group__usbd__api.md#gaa7ee71917824e90177f61a86eb992817) (struct [usbd\_contex](structusbd__contex.md) \*uds\_ctx) |
|  | Enable the USB device support and registered class instances. |
| int | [usbd\_disable](group__usbd__api.md#gaa3112af9fb2f5f1ee55cc71a64c6e369) (struct [usbd\_contex](structusbd__contex.md) \*uds\_ctx) |
|  | Disable the USB device support. |
| int | [usbd\_shutdown](group__usbd__api.md#gaa7656f656182e727531e531344c960df) (struct [usbd\_contex](structusbd__contex.md) \*const uds\_ctx) |
|  | Shutdown the USB device support. |
| int | [usbd\_ep\_set\_halt](group__usbd__api.md#ga0730043c2fd89b56db6e7457b639968d) (struct [usbd\_contex](structusbd__contex.md) \*uds\_ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Halt endpoint. |
| int | [usbd\_ep\_clear\_halt](group__usbd__api.md#ga197697880c7c625ea212893b2fe7ef8b) (struct [usbd\_contex](structusbd__contex.md) \*uds\_ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Clear endpoint halt. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [usbd\_ep\_is\_halted](group__usbd__api.md#ga9292b393ef17fd61ea42b2f28fdd57ee) (struct [usbd\_contex](structusbd__contex.md) \*uds\_ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Checks whether the endpoint is halted. |
| struct [net\_buf](structnet__buf.md) \* | [usbd\_ep\_ctrl\_buf\_alloc](group__usbd__api.md#ga59b0cb83b05e0a44db9c6a36171d524f) (struct [usbd\_contex](structusbd__contex.md) \*const uds\_ctx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, const [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Allocate buffer for USB device control request. |
| struct [net\_buf](structnet__buf.md) \* | [usbd\_ep\_buf\_alloc](group__usbd__api.md#ga940f38e4db1dfc7ba6514ecf95dc9e5b) (const struct [usbd\_class\_node](structusbd__class__node.md) \*const c\_nd, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, const [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Allocate buffer for USB device request. |
| int | [usbd\_ep\_ctrl\_enqueue](group__usbd__api.md#ga52acb4fb74e3737b446b6704c6925d70) (struct [usbd\_contex](structusbd__contex.md) \*const uds\_ctx, struct [net\_buf](structnet__buf.md) \*const buf) |
|  | Queue USB device control request. |
| int | [usbd\_ep\_enqueue](group__usbd__api.md#ga19ecdc00918dbec14fdbcf847b6f4dce) (const struct [usbd\_class\_node](structusbd__class__node.md) \*const c\_nd, struct [net\_buf](structnet__buf.md) \*const buf) |
|  | Queue USB device request. |
| int | [usbd\_ep\_dequeue](group__usbd__api.md#ga0d1d7f59822674c201147b50a1dbdb96) (struct [usbd\_contex](structusbd__contex.md) \*uds\_ctx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Remove all USB device controller requests from endpoint queue. |
| int | [usbd\_ep\_buf\_free](group__usbd__api.md#ga2bfd230a2e0b74954ebce112816e6193) (struct [usbd\_contex](structusbd__contex.md) \*uds\_ctx, struct [net\_buf](structnet__buf.md) \*buf) |
|  | Free USB device request buffer. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [usbd\_is\_suspended](group__usbd__api.md#ga832e3147aba9297bad263b2a3817e1e4) (struct [usbd\_contex](structusbd__contex.md) \*uds\_ctx) |
|  | Checks whether the USB device controller is suspended. |
| int | [usbd\_wakeup\_request](group__usbd__api.md#ga4d440313da931d4504919b8fe2783419) (struct [usbd\_contex](structusbd__contex.md) \*uds\_ctx) |
|  | Initiate the USB remote wakeup (TBD). |
| int | [usbd\_device\_set\_bcd](group__usbd__api.md#gaa191663f3703bd631e51009adbc22d87) (struct [usbd\_contex](structusbd__contex.md) \*const uds\_ctx, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bcd) |
|  | Set USB device descriptor value bcdUSB. |
| int | [usbd\_device\_set\_vid](group__usbd__api.md#ga791a561a3d96698a1a7337723adc8e53) (struct [usbd\_contex](structusbd__contex.md) \*const uds\_ctx, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vid) |
|  | Set USB device descriptor value idVendor. |
| int | [usbd\_device\_set\_pid](group__usbd__api.md#gad3612c1c4276783df11b144e72662306) (struct [usbd\_contex](structusbd__contex.md) \*const uds\_ctx, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) pid) |
|  | Set USB device descriptor value idProduct. |
| int | [usbd\_device\_set\_code\_triple](group__usbd__api.md#gad8d784ae06463afe51f312dad8a4718d) (struct [usbd\_contex](structusbd__contex.md) \*const uds\_ctx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) base\_class, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) subclass, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) protocol) |
|  | Set USB device descriptor code triple Base Class, SubClass, and Protocol. |
| int | [usbd\_config\_attrib\_rwup](group__usbd__api.md#ga6488af53f4ed5355406ef319a8d1b195) (struct [usbd\_contex](structusbd__contex.md) \*const uds\_ctx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cfg, const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Setup USB device configuration attribute Remote Wakeup. |
| int | [usbd\_config\_attrib\_self](group__usbd__api.md#ga7c8dd76553545c77ff6e0f4c41d33357) (struct [usbd\_contex](structusbd__contex.md) \*const uds\_ctx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cfg, const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Setup USB device configuration attribute Self-powered. |
| int | [usbd\_config\_maxpower](group__usbd__api.md#gac907ba549e8d799a328cc992d76e3825) (struct [usbd\_contex](structusbd__contex.md) \*const uds\_ctx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) cfg, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) power) |
|  | Setup USB device configuration power consumption. |

## Detailed Description

New experimental USB device stack APIs and structures.

This file contains the USB device stack APIs and structures.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [usb](dir_d8285a9da4e2f530d10dd4c17d446a84.md)
- [usbd.h](usbd_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
