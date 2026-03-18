---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/img__mgmt__client_8h.html
original_path: doxygen/html/img__mgmt__client_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

img\_mgmt\_client.h File Reference

`#include <[inttypes.h](inttypes_8h_source.md)>`  
`#include <[zephyr/mgmt/mcumgr/grp/img_mgmt/img_mgmt.h](img__mgmt_8h_source.md)>`  
`#include <[zephyr/mgmt/mcumgr/smp/smp_client.h](smp__client_8h_source.md)>`

[Go to the source code of this file.](img__mgmt__client_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [mcumgr\_image\_list\_flags](structmcumgr__image__list__flags.md) |
|  | Image list flags. [More...](structmcumgr__image__list__flags.md#details) |
| struct | [mcumgr\_image\_data](structmcumgr__image__data.md) |
|  | Image list data. [More...](structmcumgr__image__data.md#details) |
| struct | [mcumgr\_image\_state](structmcumgr__image__state.md) |
|  | MCUmgr Image list response. [More...](structmcumgr__image__state.md#details) |
| struct | [mcumgr\_image\_upload](structmcumgr__image__upload.md) |
|  | MCUmgr Image upload response. [More...](structmcumgr__image__upload.md#details) |
| struct | [img\_gr\_upload](structimg__gr__upload.md) |
|  | IMG mgmt client upload structure. [More...](structimg__gr__upload.md#details) |
| struct | [img\_mgmt\_client](structimg__mgmt__client.md) |
|  | IMG mgmt client object. [More...](structimg__mgmt__client.md#details) |

| Functions | |
| --- | --- |
| void | [img\_mgmt\_client\_init](group__mcumgr__img__mgmt__client.md#ga1c21618818b5b058e28bdd32360e3838) (struct [img\_mgmt\_client](structimg__mgmt__client.md) \*client, struct [smp\_client\_object](structsmp__client__object.md) \*smp\_client, int image\_list\_size, struct [mcumgr\_image\_data](structmcumgr__image__data.md) \*image\_list) |
|  | Inilialize image group client. |
| int | [img\_mgmt\_client\_upload\_init](group__mcumgr__img__mgmt__client.md#ga99dccccacad33c5e7f91043b483a3884) (struct [img\_mgmt\_client](structimg__mgmt__client.md) \*client, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) image\_size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) image\_num, const char \*image\_hash) |
|  | Initialize image upload. |
| int | [img\_mgmt\_client\_upload](group__mcumgr__img__mgmt__client.md#ga55fddd1f53765ce25e4285e45714ebc1) (struct [img\_mgmt\_client](structimg__mgmt__client.md) \*client, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length, struct [mcumgr\_image\_upload](structmcumgr__image__upload.md) \*res\_buf) |
|  | Upload part of image. |
| int | [img\_mgmt\_client\_state\_write](group__mcumgr__img__mgmt__client.md#gabb1cbc805d8f7e2d8ab94f063f29f9ac) (struct [img\_mgmt\_client](structimg__mgmt__client.md) \*client, char \*hash, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) confirm, struct [mcumgr\_image\_state](structmcumgr__image__state.md) \*res\_buf) |
|  | Write image state. |
| int | [img\_mgmt\_client\_state\_read](group__mcumgr__img__mgmt__client.md#gad1937b33597ddd012fc7d1fd04cf17f8) (struct [img\_mgmt\_client](structimg__mgmt__client.md) \*client, struct [mcumgr\_image\_state](structmcumgr__image__state.md) \*res\_buf) |
|  | Read image state. |
| int | [img\_mgmt\_client\_erase](group__mcumgr__img__mgmt__client.md#ga27ca742a8fc5fc3a96510d73fa85a7a3) (struct [img\_mgmt\_client](structimg__mgmt__client.md) \*client, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) slot) |
|  | Erase selected Image Slot. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [grp](dir_75a5d043a2b1048bf3665f6cb87645f5.md)
- [img\_mgmt](dir_731c1b2142dfc9d7fee3a06aa394438e.md)
- [img\_mgmt\_client.h](img__mgmt__client_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
