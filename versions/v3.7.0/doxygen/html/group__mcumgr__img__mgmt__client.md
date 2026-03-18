---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__mcumgr__img__mgmt__client.html
original_path: doxygen/html/group__mcumgr__img__mgmt__client.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

MCUmgr img\_mgmt\_client API

[Operating System Services](group__os__services.md) » [MCUmgr](group__mcumgr.md)

MCUmgr Image management client API.
[More...](#details)

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
| void | [img\_mgmt\_client\_init](#ga1c21618818b5b058e28bdd32360e3838) (struct [img\_mgmt\_client](structimg__mgmt__client.md) \*client, struct [smp\_client\_object](structsmp__client__object.md) \*smp\_client, int image\_list\_size, struct [mcumgr\_image\_data](structmcumgr__image__data.md) \*image\_list) |
|  | Inilialize image group client. |
| int | [img\_mgmt\_client\_upload\_init](#ga99dccccacad33c5e7f91043b483a3884) (struct [img\_mgmt\_client](structimg__mgmt__client.md) \*client, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) image\_size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) image\_num, const char \*image\_hash) |
|  | Initialize image upload. |
| int | [img\_mgmt\_client\_upload](#ga55fddd1f53765ce25e4285e45714ebc1) (struct [img\_mgmt\_client](structimg__mgmt__client.md) \*client, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length, struct [mcumgr\_image\_upload](structmcumgr__image__upload.md) \*res\_buf) |
|  | Upload part of image. |
| int | [img\_mgmt\_client\_state\_write](#gabb1cbc805d8f7e2d8ab94f063f29f9ac) (struct [img\_mgmt\_client](structimg__mgmt__client.md) \*client, char \*hash, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) confirm, struct [mcumgr\_image\_state](structmcumgr__image__state.md) \*res\_buf) |
|  | Write image state. |
| int | [img\_mgmt\_client\_state\_read](#gad1937b33597ddd012fc7d1fd04cf17f8) (struct [img\_mgmt\_client](structimg__mgmt__client.md) \*client, struct [mcumgr\_image\_state](structmcumgr__image__state.md) \*res\_buf) |
|  | Read image state. |
| int | [img\_mgmt\_client\_erase](#ga27ca742a8fc5fc3a96510d73fa85a7a3) (struct [img\_mgmt\_client](structimg__mgmt__client.md) \*client, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) slot) |
|  | Erase selected Image Slot. |

## Detailed Description

MCUmgr Image management client API.

## Function Documentation

## [◆ ](#ga27ca742a8fc5fc3a96510d73fa85a7a3)img\_mgmt\_client\_erase()

| int img\_mgmt\_client\_erase | ( | struct [img\_mgmt\_client](structimg__mgmt__client.md) \* | *client*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *slot* ) |

`#include <[img_mgmt_client.h](img__mgmt__client_8h.md)>`

Erase selected Image Slot.

Parameters
:   | client | IMG mgmt client object |
    | --- | --- |
    | slot | Slot number |

Returns
:   0 on success.
:   [mcumgr\_err\_t](group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5 "mcumgr_err_t") code on failure.

## [◆ ](#ga1c21618818b5b058e28bdd32360e3838)img\_mgmt\_client\_init()

| void img\_mgmt\_client\_init | ( | struct [img\_mgmt\_client](structimg__mgmt__client.md) \* | *client*, |
| --- | --- | --- | --- |
|  |  | struct [smp\_client\_object](structsmp__client__object.md) \* | *smp\_client*, |
|  |  | int | *image\_list\_size*, |
|  |  | struct [mcumgr\_image\_data](structmcumgr__image__data.md) \* | *image\_list* ) |

`#include <[img_mgmt_client.h](img__mgmt__client_8h.md)>`

Inilialize image group client.

Function initializes image group client for given SMP client using supplied image data.

Parameters
:   | client | IMG mgmt client object |
    | --- | --- |
    | smp\_client | SMP client object |
    | image\_list\_size | Length of image\_list buffer. |
    | image\_list | Image list buffer pointer. |

## [◆ ](#gad1937b33597ddd012fc7d1fd04cf17f8)img\_mgmt\_client\_state\_read()

| int img\_mgmt\_client\_state\_read | ( | struct [img\_mgmt\_client](structimg__mgmt__client.md) \* | *client*, |
| --- | --- | --- | --- |
|  |  | struct [mcumgr\_image\_state](structmcumgr__image__state.md) \* | *res\_buf* ) |

`#include <[img_mgmt_client.h](img__mgmt__client_8h.md)>`

Read image state.

Parameters
:   | client | IMG mgmt client object |
    | --- | --- |
    | res\_buf | Pointer for command response structure. |

Returns
:   0 on success.
:   [mcumgr\_err\_t](group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5 "mcumgr_err_t") code on failure.

## [◆ ](#gabb1cbc805d8f7e2d8ab94f063f29f9ac)img\_mgmt\_client\_state\_write()

| int img\_mgmt\_client\_state\_write | ( | struct [img\_mgmt\_client](structimg__mgmt__client.md) \* | *client*, |
| --- | --- | --- | --- |
|  |  | char \* | *hash*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *confirm*, |
|  |  | struct [mcumgr\_image\_state](structmcumgr__image__state.md) \* | *res\_buf* ) |

`#include <[img_mgmt_client.h](img__mgmt__client_8h.md)>`

Write image state.

Parameters
:   | client | IMG mgmt client object |
    | --- | --- |
    | hash | Pointer to Hash (Needed for test). |
    | confirm | Set false for test and true for confirmation. |
    | res\_buf | Pointer for command response structure. |

Returns
:   0 on success.
:   [mcumgr\_err\_t](group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5 "mcumgr_err_t") code on failure.

## [◆ ](#ga55fddd1f53765ce25e4285e45714ebc1)img\_mgmt\_client\_upload()

| int img\_mgmt\_client\_upload | ( | struct [img\_mgmt\_client](structimg__mgmt__client.md) \* | *client*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *length*, |
|  |  | struct [mcumgr\_image\_upload](structmcumgr__image__upload.md) \* | *res\_buf* ) |

`#include <[img_mgmt_client.h](img__mgmt__client_8h.md)>`

Upload part of image.

Parameters
:   | client | IMG mgmt client object |
    | --- | --- |
    | data | Pointer to data. |
    | length | Length of data |
    | res\_buf | Pointer for command response structure. |

Returns
:   0 on success.
:   [mcumgr\_err\_t](group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5 "mcumgr_err_t") code on failure.

## [◆ ](#ga99dccccacad33c5e7f91043b483a3884)img\_mgmt\_client\_upload\_init()

| int img\_mgmt\_client\_upload\_init | ( | struct [img\_mgmt\_client](structimg__mgmt__client.md) \* | *client*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *image\_size*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *image\_num*, |
|  |  | const char \* | *image\_hash* ) |

`#include <[img_mgmt_client.h](img__mgmt__client_8h.md)>`

Initialize image upload.

Parameters
:   | client | IMG mgmt client object |
    | --- | --- |
    | image\_size | Size of image in bytes. |
    | image\_num | Image slot Num. |
    | image\_hash | Pointer to HASH for image must be SHA256 hash of entire upload if present (32 bytes). Use NULL when HASH from image is not available. |

Returns
:   0 on success.
:   [mcumgr\_err\_t](group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5 "mcumgr_err_t") code on failure.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
