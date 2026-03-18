---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__mcumgr__img__mgmt.html
original_path: doxygen/html/group__mcumgr__img__mgmt.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

MCUmgr img\_mgmt API

[Operating System Services](group__os__services.md) » [MCUmgr](group__mcumgr.md)

MCUmgr img\_mgmt API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [img\_mgmt\_upload\_req](structimg__mgmt__upload__req.md) |
|  | Represents an individual upload request. [More...](structimg__mgmt__upload__req.md#details) |
| struct | [img\_mgmt\_state](structimg__mgmt__state.md) |
|  | Global state for upload in progress. [More...](structimg__mgmt__state.md#details) |
| struct | [img\_mgmt\_upload\_action](structimg__mgmt__upload__action.md) |
|  | Describes what to do during processing of an upload request. [More...](structimg__mgmt__upload__action.md#details) |

| Macros | |
| --- | --- |
| #define | [IMG\_MGMT\_DATA\_SHA\_LEN](#ga70168b0d707c15658fd09b02c361a64c)   32 /\* SHA256 \*/ |
| #define | [IMG\_MGMT\_STATE\_F\_PENDING](#ga459776db5ce7bbfebae5e74aef4067ef)   0x01 |
|  | Image state flags. |
| #define | [IMG\_MGMT\_STATE\_F\_CONFIRMED](#ga581c2626a47ca249ecbcc42edb7a59c2)   0x02 |
| #define | [IMG\_MGMT\_STATE\_F\_ACTIVE](#ga2a11cfad9698b0460b846fa079234c03)   0x04 |
| #define | [IMG\_MGMT\_STATE\_F\_PERMANENT](#gae47e88131d96901e70b2b67ea43ceb4a)   0x08 |
| #define | [IMG\_MGMT\_VER\_MAX\_STR\_LEN](#ga57a5c429be5a3860981007e9728db181)   ([sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)("255.255.65535.4294967295")) |
| #define | [IMG\_MGMT\_SWAP\_TYPE\_NONE](#ga55e68ef4a5caa3c68987af438ebe8236)   0 |
|  | Swap Types for image management state machine. |
| #define | [IMG\_MGMT\_SWAP\_TYPE\_TEST](#ga71a0715be72de416f3d4744f4763a241)   1 |
| #define | [IMG\_MGMT\_SWAP\_TYPE\_PERM](#ga69c51ca39c8d33db392e2353873aac43)   2 |
| #define | [IMG\_MGMT\_SWAP\_TYPE\_REVERT](#ga43a9afd49822eda7b640d3adb9219f10)   3 |
| #define | [IMG\_MGMT\_SWAP\_TYPE\_UNKNOWN](#ga35a8dd8ca661f2a602bc04d4ae6361a6)   255 |
| #define | [IMG\_MGMT\_ID\_STATE](#ga19396c2690a0d40f625792ab644e7d17)   0 |
|  | Command IDs for image management group. |
| #define | [IMG\_MGMT\_ID\_UPLOAD](#ga70541d06c76224a631f493023e05a73a)   1 |
| #define | [IMG\_MGMT\_ID\_FILE](#ga90225baf3e08859f294d9aaaf2012e6b)   2 |
| #define | [IMG\_MGMT\_ID\_CORELIST](#ga46e9a83aab777da2591d4c7cb701b5cd)   3 |
| #define | [IMG\_MGMT\_ID\_CORELOAD](#ga22af869af6cbdde12f2cbc811fe7d443)   4 |
| #define | [IMG\_MGMT\_ID\_ERASE](#gaf7de4c1d77bc29eea4b3d46382bd954f)   5 |
| #define | [IMG\_MGMT\_UPLOAD\_ACTION\_SET\_RC\_RSN](#ga56e01e5bfa9fdd9bf6ebdc0dc3ac19ba)(action, rsn) |
| #define | [IMG\_MGMT\_UPLOAD\_ACTION\_RC\_RSN](#gaee07bacea29269e24ca15a2e1716390d)(action) |

| Enumerations | |
| --- | --- |
| enum | [img\_mgmt\_err\_code\_t](#ga669286d96816e0e99792f407752c81a5) {     [IMG\_MGMT\_ERR\_OK](#gga669286d96816e0e99792f407752c81a5a7db18fe6cb5913fec882dc515d8bb7a0) = 0 , [IMG\_MGMT\_ERR\_UNKNOWN](#gga669286d96816e0e99792f407752c81a5a8f1bd00b3e00f070b07269fdddd2c8fe) , [IMG\_MGMT\_ERR\_FLASH\_CONFIG\_QUERY\_FAIL](#gga669286d96816e0e99792f407752c81a5a5b4301665ef0c9818fcd3174908e5063) , [IMG\_MGMT\_ERR\_NO\_IMAGE](#gga669286d96816e0e99792f407752c81a5a360155fc7e541080a7b80bee6ec9dbb6) ,     [IMG\_MGMT\_ERR\_NO\_TLVS](#gga669286d96816e0e99792f407752c81a5a598c03b99a2be60cf4847fa2f32c5d10) , [IMG\_MGMT\_ERR\_INVALID\_TLV](#gga669286d96816e0e99792f407752c81a5a4725027793b17187474089fde35730cb) , [IMG\_MGMT\_ERR\_TLV\_MULTIPLE\_HASHES\_FOUND](#gga669286d96816e0e99792f407752c81a5aced7bb74d51b7dd7ff922cf555722276) , [IMG\_MGMT\_ERR\_TLV\_INVALID\_SIZE](#gga669286d96816e0e99792f407752c81a5a967c4f0b3d33d925e28f076c8cc3ed5c) ,     [IMG\_MGMT\_ERR\_HASH\_NOT\_FOUND](#gga669286d96816e0e99792f407752c81a5a5d89dde479611276e6956706ee357c6e) , [IMG\_MGMT\_ERR\_NO\_FREE\_SLOT](#gga669286d96816e0e99792f407752c81a5a0d16138a65766047e4917022068832fa) , [IMG\_MGMT\_ERR\_FLASH\_OPEN\_FAILED](#gga669286d96816e0e99792f407752c81a5a8253896c206d8f3ba486466555662071) , [IMG\_MGMT\_ERR\_FLASH\_READ\_FAILED](#gga669286d96816e0e99792f407752c81a5a9a09d73602a77e112a95fa977e9b0355) ,     [IMG\_MGMT\_ERR\_FLASH\_WRITE\_FAILED](#gga669286d96816e0e99792f407752c81a5adf54010236b4e6bb4669cdeeb4a6979f) , [IMG\_MGMT\_ERR\_FLASH\_ERASE\_FAILED](#gga669286d96816e0e99792f407752c81a5a869d0aa27c38187fdb73d36397dcef3c) , [IMG\_MGMT\_ERR\_INVALID\_SLOT](#gga669286d96816e0e99792f407752c81a5a7c0f0cda8165d0acf5fc2a072a5c5cc5) , [IMG\_MGMT\_ERR\_NO\_FREE\_MEMORY](#gga669286d96816e0e99792f407752c81a5ab75ac303b054a02e99a0ed9726c988de) ,     [IMG\_MGMT\_ERR\_FLASH\_CONTEXT\_ALREADY\_SET](#gga669286d96816e0e99792f407752c81a5af1eac867913981a4d8f1f2d64108706e) , [IMG\_MGMT\_ERR\_FLASH\_CONTEXT\_NOT\_SET](#gga669286d96816e0e99792f407752c81a5a9e4c9f1a79f645130ef9a8aa09b8b544) , [IMG\_MGMT\_ERR\_FLASH\_AREA\_DEVICE\_NULL](#gga669286d96816e0e99792f407752c81a5a6c1c103d76e1f16fda77525ba136e9b2) , [IMG\_MGMT\_ERR\_INVALID\_PAGE\_OFFSET](#gga669286d96816e0e99792f407752c81a5a857b6ecc22e5f54834638aa604cce6bf) ,     [IMG\_MGMT\_ERR\_INVALID\_OFFSET](#gga669286d96816e0e99792f407752c81a5a8a94dfe1aca340c4337fe92554ede4b0) , [IMG\_MGMT\_ERR\_INVALID\_LENGTH](#gga669286d96816e0e99792f407752c81a5a227b2b3be93cf963ce034b9cb817d0ca) , [IMG\_MGMT\_ERR\_INVALID\_IMAGE\_HEADER](#gga669286d96816e0e99792f407752c81a5acfdb28d59643e70db86abfa72c2833b7) , [IMG\_MGMT\_ERR\_INVALID\_IMAGE\_HEADER\_MAGIC](#gga669286d96816e0e99792f407752c81a5a5606b72a7bf61832b92c77e729e02093) ,     [IMG\_MGMT\_ERR\_INVALID\_HASH](#gga669286d96816e0e99792f407752c81a5a4b2994e51eadae6cb43c3683d6e223b6) , [IMG\_MGMT\_ERR\_INVALID\_FLASH\_ADDRESS](#gga669286d96816e0e99792f407752c81a5a27502b76efcc09ef01cfbe777a9e8086) , [IMG\_MGMT\_ERR\_VERSION\_GET\_FAILED](#gga669286d96816e0e99792f407752c81a5ae710879342357f27c9705989f572b82f) , [IMG\_MGMT\_ERR\_CURRENT\_VERSION\_IS\_NEWER](#gga669286d96816e0e99792f407752c81a5a37ad5efbaacdcb708a65674a4dc83d85) ,     [IMG\_MGMT\_ERR\_IMAGE\_ALREADY\_PENDING](#gga669286d96816e0e99792f407752c81a5af55239776b4b5a5eead0440fb3b884b3) , [IMG\_MGMT\_ERR\_INVALID\_IMAGE\_VECTOR\_TABLE](#gga669286d96816e0e99792f407752c81a5a3a8d3005c72273ee065c34396d3fd2f7) , [IMG\_MGMT\_ERR\_INVALID\_IMAGE\_TOO\_LARGE](#gga669286d96816e0e99792f407752c81a5ab258cd53a5cc13e2376662690703f54b) , [IMG\_MGMT\_ERR\_INVALID\_IMAGE\_DATA\_OVERRUN](#gga669286d96816e0e99792f407752c81a5a92ab3773cdbd00b42fb59865e958069b) ,     [IMG\_MGMT\_ERR\_IMAGE\_CONFIRMATION\_DENIED](#gga669286d96816e0e99792f407752c81a5ae2413b0ade3185b91ae085af397adabf) , [IMG\_MGMT\_ERR\_IMAGE\_SETTING\_TEST\_TO\_ACTIVE\_DENIED](#gga669286d96816e0e99792f407752c81a5ab195578794ddc6cffa5e056ee34350a8) , [IMG\_MGMT\_ERR\_ACTIVE\_SLOT\_NOT\_KNOWN](#gga669286d96816e0e99792f407752c81a5a3220405113525f3d5af068b8bf2a80f6)   } |
|  | Command result codes for image management group. [More...](#ga669286d96816e0e99792f407752c81a5) |
| enum | [img\_mgmt\_id\_upload\_t](#ga1d239fef127e65b11b71360eadfa1ede) { [IMG\_MGMT\_ID\_UPLOAD\_STATUS\_START](#gga1d239fef127e65b11b71360eadfa1edeaff49286e379bd39781a563c1e52c6c8c) = 0 , [IMG\_MGMT\_ID\_UPLOAD\_STATUS\_ONGOING](#gga1d239fef127e65b11b71360eadfa1edea7cf567b16af18752316fde6444e23a21) , [IMG\_MGMT\_ID\_UPLOAD\_STATUS\_COMPLETE](#gga1d239fef127e65b11b71360eadfa1edeab106874625a50d626e55130e91d37bf2) } |
|  | IMG\_MGMT\_ID\_UPLOAD statuses. [More...](#ga1d239fef127e65b11b71360eadfa1ede) |

| Functions | |
| --- | --- |
| int | [img\_mgmt\_read\_info](#ga60ae88823a561160b1ddc406382e4ac3) (int image\_slot, struct image\_version \*ver, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*hash, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
| int | [img\_mgmt\_my\_version](#gae9cfa02e5f171d68287cdb0d7d4c0610) (struct image\_version \*ver) |
|  | Get the image version of the currently running application. |
| int | [img\_mgmt\_ver\_str](#ga5199849b6d8847c6a1260254940db95b) (const struct image\_version \*ver, char \*dst) |
|  | Format version string from struct image\_version. |
| int | [img\_mgmt\_active\_slot](#gab35c8adf2e5e2c941ecbaf3c03101e55) (int image) |
|  | Get active, running application slot number for an image. |
| int | [img\_mgmt\_active\_image](#gab6a92433b859fce18b58e6110fa5f489) (void) |
|  | Get active image number. |
| int | [img\_mgmt\_slot\_in\_use](#ga90de2da23bcd650ca59219fdfd4f55a1) (int slot) |
|  | Check if the image slot is in use. |
| int | [img\_mgmt\_state\_any\_pending](#ga3e496199d0ea4aa1b3f51e59bb7473f0) (void) |
|  | Check if any slot is in MCUboot pending state. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [img\_mgmt\_state\_flags](#ga42475389b4e31d5f35ea58873527e948) (int query\_slot) |
|  | Returns state flags set to slot. |
| int | [img\_mgmt\_state\_set\_pending](#ga7e529fa76ddb3d3bf4a527cb11fa9c89) (int slot, int permanent) |
|  | Sets the pending flag for the specified image slot. |
| int | [img\_mgmt\_state\_confirm](#gaed0b945d2f83daf63d850b232a2cfea8) (void) |
|  | Confirms the current image state. |
| int | [img\_mgmt\_vercmp](#ga6c9124cc59c99769908cdf83f58e1bf1) (const struct image\_version \*a, const struct image\_version \*b) |
|  | Compares two image version numbers in a semver-compatible way. |

| Variables | |
| --- | --- |
| int | [boot\_current\_slot](#ga0d6bb8877516ca486c318fa12c129138) |
| struct [img\_mgmt\_state](structimg__mgmt__state.md) | [g\_img\_mgmt\_state](#gad3dce7b70ce3338588003a021eec1ab6) |

## Detailed Description

MCUmgr img\_mgmt API.

## Macro Definition Documentation

## [◆ ](#ga70168b0d707c15658fd09b02c361a64c)IMG\_MGMT\_DATA\_SHA\_LEN

| #define IMG\_MGMT\_DATA\_SHA\_LEN   32 /\* SHA256 \*/ |
| --- |

`#include <[img_mgmt.h](img__mgmt_8h.md)>`

## [◆ ](#ga46e9a83aab777da2591d4c7cb701b5cd)IMG\_MGMT\_ID\_CORELIST

| #define IMG\_MGMT\_ID\_CORELIST   3 |
| --- |

`#include <[img_mgmt.h](img__mgmt_8h.md)>`

## [◆ ](#ga22af869af6cbdde12f2cbc811fe7d443)IMG\_MGMT\_ID\_CORELOAD

| #define IMG\_MGMT\_ID\_CORELOAD   4 |
| --- |

`#include <[img_mgmt.h](img__mgmt_8h.md)>`

## [◆ ](#gaf7de4c1d77bc29eea4b3d46382bd954f)IMG\_MGMT\_ID\_ERASE

| #define IMG\_MGMT\_ID\_ERASE   5 |
| --- |

`#include <[img_mgmt.h](img__mgmt_8h.md)>`

## [◆ ](#ga90225baf3e08859f294d9aaaf2012e6b)IMG\_MGMT\_ID\_FILE

| #define IMG\_MGMT\_ID\_FILE   2 |
| --- |

`#include <[img_mgmt.h](img__mgmt_8h.md)>`

## [◆ ](#ga19396c2690a0d40f625792ab644e7d17)IMG\_MGMT\_ID\_STATE

| #define IMG\_MGMT\_ID\_STATE   0 |
| --- |

`#include <[img_mgmt.h](img__mgmt_8h.md)>`

Command IDs for image management group.

## [◆ ](#ga70541d06c76224a631f493023e05a73a)IMG\_MGMT\_ID\_UPLOAD

| #define IMG\_MGMT\_ID\_UPLOAD   1 |
| --- |

`#include <[img_mgmt.h](img__mgmt_8h.md)>`

## [◆ ](#ga2a11cfad9698b0460b846fa079234c03)IMG\_MGMT\_STATE\_F\_ACTIVE

| #define IMG\_MGMT\_STATE\_F\_ACTIVE   0x04 |
| --- |

`#include <[img_mgmt.h](img__mgmt_8h.md)>`

## [◆ ](#ga581c2626a47ca249ecbcc42edb7a59c2)IMG\_MGMT\_STATE\_F\_CONFIRMED

| #define IMG\_MGMT\_STATE\_F\_CONFIRMED   0x02 |
| --- |

`#include <[img_mgmt.h](img__mgmt_8h.md)>`

## [◆ ](#ga459776db5ce7bbfebae5e74aef4067ef)IMG\_MGMT\_STATE\_F\_PENDING

| #define IMG\_MGMT\_STATE\_F\_PENDING   0x01 |
| --- |

`#include <[img_mgmt.h](img__mgmt_8h.md)>`

Image state flags.

## [◆ ](#gae47e88131d96901e70b2b67ea43ceb4a)IMG\_MGMT\_STATE\_F\_PERMANENT

| #define IMG\_MGMT\_STATE\_F\_PERMANENT   0x08 |
| --- |

`#include <[img_mgmt.h](img__mgmt_8h.md)>`

## [◆ ](#ga55e68ef4a5caa3c68987af438ebe8236)IMG\_MGMT\_SWAP\_TYPE\_NONE

| #define IMG\_MGMT\_SWAP\_TYPE\_NONE   0 |
| --- |

`#include <[img_mgmt.h](img__mgmt_8h.md)>`

Swap Types for image management state machine.

## [◆ ](#ga69c51ca39c8d33db392e2353873aac43)IMG\_MGMT\_SWAP\_TYPE\_PERM

| #define IMG\_MGMT\_SWAP\_TYPE\_PERM   2 |
| --- |

`#include <[img_mgmt.h](img__mgmt_8h.md)>`

## [◆ ](#ga43a9afd49822eda7b640d3adb9219f10)IMG\_MGMT\_SWAP\_TYPE\_REVERT

| #define IMG\_MGMT\_SWAP\_TYPE\_REVERT   3 |
| --- |

`#include <[img_mgmt.h](img__mgmt_8h.md)>`

## [◆ ](#ga71a0715be72de416f3d4744f4763a241)IMG\_MGMT\_SWAP\_TYPE\_TEST

| #define IMG\_MGMT\_SWAP\_TYPE\_TEST   1 |
| --- |

`#include <[img_mgmt.h](img__mgmt_8h.md)>`

## [◆ ](#ga35a8dd8ca661f2a602bc04d4ae6361a6)IMG\_MGMT\_SWAP\_TYPE\_UNKNOWN

| #define IMG\_MGMT\_SWAP\_TYPE\_UNKNOWN   255 |
| --- |

`#include <[img_mgmt.h](img__mgmt_8h.md)>`

## [◆ ](#gaee07bacea29269e24ca15a2e1716390d)IMG\_MGMT\_UPLOAD\_ACTION\_RC\_RSN

| #define IMG\_MGMT\_UPLOAD\_ACTION\_RC\_RSN | ( |  | *action* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[img_mgmt.h](img__mgmt_8h.md)>`

**Value:**

NULL

## [◆ ](#ga56e01e5bfa9fdd9bf6ebdc0dc3ac19ba)IMG\_MGMT\_UPLOAD\_ACTION\_SET\_RC\_RSN

| #define IMG\_MGMT\_UPLOAD\_ACTION\_SET\_RC\_RSN | ( |  | *action*, |
| --- | --- | --- | --- |
|  |  |  | *rsn* ) |

`#include <[img_mgmt.h](img__mgmt_8h.md)>`

## [◆ ](#ga57a5c429be5a3860981007e9728db181)IMG\_MGMT\_VER\_MAX\_STR\_LEN

| #define IMG\_MGMT\_VER\_MAX\_STR\_LEN   ([sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)("255.255.65535.4294967295")) |
| --- |

`#include <[img_mgmt.h](img__mgmt_8h.md)>`

## Enumeration Type Documentation

## [◆ ](#ga669286d96816e0e99792f407752c81a5)img\_mgmt\_err\_code\_t

| enum [img\_mgmt\_err\_code\_t](#ga669286d96816e0e99792f407752c81a5) |
| --- |

`#include <[img_mgmt.h](img__mgmt_8h.md)>`

Command result codes for image management group.

| Enumerator | |
| --- | --- |
| IMG\_MGMT\_ERR\_OK | No error, this is implied if there is no ret value in the response. |
| IMG\_MGMT\_ERR\_UNKNOWN | Unknown error occurred. |
| IMG\_MGMT\_ERR\_FLASH\_CONFIG\_QUERY\_FAIL | Failed to query flash area configuration. |
| IMG\_MGMT\_ERR\_NO\_IMAGE | There is no image in the slot. |
| IMG\_MGMT\_ERR\_NO\_TLVS | The image in the slot has no TLVs (tag, length, value). |
| IMG\_MGMT\_ERR\_INVALID\_TLV | The image in the slot has an invalid TLV type and/or length. |
| IMG\_MGMT\_ERR\_TLV\_MULTIPLE\_HASHES\_FOUND | The image in the slot has multiple hash TLVs, which is invalid. |
| IMG\_MGMT\_ERR\_TLV\_INVALID\_SIZE | The image in the slot has an invalid TLV size. |
| IMG\_MGMT\_ERR\_HASH\_NOT\_FOUND | The image in the slot does not have a hash TLV, which is required. |
| IMG\_MGMT\_ERR\_NO\_FREE\_SLOT | There is no free slot to place the image. |
| IMG\_MGMT\_ERR\_FLASH\_OPEN\_FAILED | Flash area opening failed. |
| IMG\_MGMT\_ERR\_FLASH\_READ\_FAILED | Flash area reading failed. |
| IMG\_MGMT\_ERR\_FLASH\_WRITE\_FAILED | Flash area writing failed. |
| IMG\_MGMT\_ERR\_FLASH\_ERASE\_FAILED | Flash area erase failed. |
| IMG\_MGMT\_ERR\_INVALID\_SLOT | The provided slot is not valid. |
| IMG\_MGMT\_ERR\_NO\_FREE\_MEMORY | Insufficient heap memory (malloc failed). |
| IMG\_MGMT\_ERR\_FLASH\_CONTEXT\_ALREADY\_SET | The flash context is already set. |
| IMG\_MGMT\_ERR\_FLASH\_CONTEXT\_NOT\_SET | The flash context is not set. |
| IMG\_MGMT\_ERR\_FLASH\_AREA\_DEVICE\_NULL | The device for the flash area is NULL. |
| IMG\_MGMT\_ERR\_INVALID\_PAGE\_OFFSET | The offset for a page number is invalid. |
| IMG\_MGMT\_ERR\_INVALID\_OFFSET | The offset parameter was not provided and is required. |
| IMG\_MGMT\_ERR\_INVALID\_LENGTH | The length parameter was not provided and is required. |
| IMG\_MGMT\_ERR\_INVALID\_IMAGE\_HEADER | The image length is smaller than the size of an image header. |
| IMG\_MGMT\_ERR\_INVALID\_IMAGE\_HEADER\_MAGIC | The image header magic value does not match the expected value. |
| IMG\_MGMT\_ERR\_INVALID\_HASH | The hash parameter provided is not valid. |
| IMG\_MGMT\_ERR\_INVALID\_FLASH\_ADDRESS | The image load address does not match the address of the flash area. |
| IMG\_MGMT\_ERR\_VERSION\_GET\_FAILED | Failed to get version of currently running application. |
| IMG\_MGMT\_ERR\_CURRENT\_VERSION\_IS\_NEWER | The currently running application is newer than the version being uploaded. |
| IMG\_MGMT\_ERR\_IMAGE\_ALREADY\_PENDING | There is already an image operating pending. |
| IMG\_MGMT\_ERR\_INVALID\_IMAGE\_VECTOR\_TABLE | The image vector table is invalid. |
| IMG\_MGMT\_ERR\_INVALID\_IMAGE\_TOO\_LARGE | The image it too large to fit. |
| IMG\_MGMT\_ERR\_INVALID\_IMAGE\_DATA\_OVERRUN | The amount of data sent is larger than the provided image size. |
| IMG\_MGMT\_ERR\_IMAGE\_CONFIRMATION\_DENIED | Confirmation of image has been denied. |
| IMG\_MGMT\_ERR\_IMAGE\_SETTING\_TEST\_TO\_ACTIVE\_DENIED | Setting test to active slot is not allowed. |
| IMG\_MGMT\_ERR\_ACTIVE\_SLOT\_NOT\_KNOWN | Current active slot for image cannot be determined. |

## [◆ ](#ga1d239fef127e65b11b71360eadfa1ede)img\_mgmt\_id\_upload\_t

| enum [img\_mgmt\_id\_upload\_t](#ga1d239fef127e65b11b71360eadfa1ede) |
| --- |

`#include <[img_mgmt.h](img__mgmt_8h.md)>`

IMG\_MGMT\_ID\_UPLOAD statuses.

| Enumerator | |
| --- | --- |
| IMG\_MGMT\_ID\_UPLOAD\_STATUS\_START |  |
| IMG\_MGMT\_ID\_UPLOAD\_STATUS\_ONGOING |  |
| IMG\_MGMT\_ID\_UPLOAD\_STATUS\_COMPLETE |  |

## Function Documentation

## [◆ ](#gab6a92433b859fce18b58e6110fa5f489)img\_mgmt\_active\_image()

| int img\_mgmt\_active\_image | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[img_mgmt.h](img__mgmt_8h.md)>`

Get active image number.

Gets 0 based number for running application.

Returns
:   Non-negative image number.

## [◆ ](#gab35c8adf2e5e2c941ecbaf3c03101e55)img\_mgmt\_active\_slot()

| int img\_mgmt\_active\_slot | ( | int | *image* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[img_mgmt.h](img__mgmt_8h.md)>`

Get active, running application slot number for an image.

Parameters
:   | image | image number to get active slot for. |
    | --- | --- |

Returns
:   Non-negative slot number

## [◆ ](#gae9cfa02e5f171d68287cdb0d7d4c0610)img\_mgmt\_my\_version()

| int img\_mgmt\_my\_version | ( | struct image\_version \* | *ver* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[img_mgmt.h](img__mgmt_8h.md)>`

Get the image version of the currently running application.

Parameters
:   | ver | output buffer for an image version information object. |
    | --- | --- |

Returns
:   0 on success, non-zero on failure.

## [◆ ](#ga60ae88823a561160b1ddc406382e4ac3)img\_mgmt\_read\_info()

| int img\_mgmt\_read\_info | ( | int | *image\_slot*, |
| --- | --- | --- | --- |
|  |  | struct image\_version \* | *ver*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *hash*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *flags* ) |

`#include <[img_mgmt.h](img__mgmt_8h.md)>`

## [◆ ](#ga90de2da23bcd650ca59219fdfd4f55a1)img\_mgmt\_slot\_in\_use()

| int img\_mgmt\_slot\_in\_use | ( | int | *slot* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[img_mgmt.h](img__mgmt_8h.md)>`

Check if the image slot is in use.

The check is based on MCUboot flags, not image contents. This means that slot with image in it, but no bootable flags set, is considered empty. Active slot is always in use.

Parameters
:   | slot | slot number |
    | --- | --- |

Returns
:   0 if slot is not used, non-0 otherwise.

## [◆ ](#ga3e496199d0ea4aa1b3f51e59bb7473f0)img\_mgmt\_state\_any\_pending()

| int img\_mgmt\_state\_any\_pending | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[img_mgmt.h](img__mgmt_8h.md)>`

Check if any slot is in MCUboot pending state.

Function returns 1 if slot 0 or slot 1 is in MCUboot pending state, which means that it has been either marked for test or confirmed.

Returns
:   1 if there's pending DFU otherwise 0.

## [◆ ](#gaed0b945d2f83daf63d850b232a2cfea8)img\_mgmt\_state\_confirm()

| int img\_mgmt\_state\_confirm | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[img_mgmt.h](img__mgmt_8h.md)>`

Confirms the current image state.

Prevents a fallback from occurring on the next reboot if the active image is currently being tested.

Returns
:   0 on success, non-zero on failure

## [◆ ](#ga42475389b4e31d5f35ea58873527e948)img\_mgmt\_state\_flags()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) img\_mgmt\_state\_flags | ( | int | *query\_slot* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[img_mgmt.h](img__mgmt_8h.md)>`

Returns state flags set to slot.

Flags are translated from MCUboot image state flags. Returned value is zero if no flags are set or a combination of: IMG\_MGMT\_STATE\_F\_PENDING IMG\_MGMT\_STATE\_F\_CONFIRMED IMG\_MGMT\_STATE\_F\_ACTIVE IMG\_MGMT\_STATE\_F\_PERMANENT

Parameters
:   | query\_slot | slot number |
    | --- | --- |

Returns
:   return the state flags.

## [◆ ](#ga7e529fa76ddb3d3bf4a527cb11fa9c89)img\_mgmt\_state\_set\_pending()

| int img\_mgmt\_state\_set\_pending | ( | int | *slot*, |
| --- | --- | --- | --- |
|  |  | int | *permanent* ) |

`#include <[img_mgmt.h](img__mgmt_8h.md)>`

Sets the pending flag for the specified image slot.

Sets specified image slot to be used as active slot during next boot, either for test or permanently. Non-permanent image will be reverted unless image confirms itself during next boot.

Parameters
:   | slot | slot number |
    | --- | --- |
    | permanent | permanent or test only |

Returns
:   0 on success, non-zero on failure

## [◆ ](#ga5199849b6d8847c6a1260254940db95b)img\_mgmt\_ver\_str()

| int img\_mgmt\_ver\_str | ( | const struct image\_version \* | *ver*, |
| --- | --- | --- | --- |
|  |  | char \* | *dst* ) |

`#include <[img_mgmt.h](img__mgmt_8h.md)>`

Format version string from struct image\_version.

Parameters
:   | ver | pointer to image\_version object |
    | --- | --- |
    | dst | output buffer for image version string |

Returns
:   Non-negative on success, negative value on error.

## [◆ ](#ga6c9124cc59c99769908cdf83f58e1bf1)img\_mgmt\_vercmp()

| int img\_mgmt\_vercmp | ( | const struct image\_version \* | *a*, |
| --- | --- | --- | --- |
|  |  | const struct image\_version \* | *b* ) |

`#include <[img_mgmt.h](img__mgmt_8h.md)>`

Compares two image version numbers in a semver-compatible way.

Parameters
:   | a | The first version to compare |
    | --- | --- |
    | b | The second version to compare |

Returns
:   -1 if a < b
:   0 if a = b
:   1 if a > b

## Variable Documentation

## [◆ ](#ga0d6bb8877516ca486c318fa12c129138)boot\_current\_slot

| | int boot\_current\_slot | | --- | | extern |
| --- | --- | --- |

`#include <[img_mgmt.h](img__mgmt_8h.md)>`

## [◆ ](#gad3dce7b70ce3338588003a021eec1ab6)g\_img\_mgmt\_state

| | struct [img\_mgmt\_state](structimg__mgmt__state.md) g\_img\_mgmt\_state | | --- | | extern |
| --- | --- | --- |

`#include <[img_mgmt.h](img__mgmt_8h.md)>`

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
