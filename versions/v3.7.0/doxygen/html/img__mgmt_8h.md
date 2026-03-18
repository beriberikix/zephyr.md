---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/img__mgmt_8h.html
original_path: doxygen/html/img__mgmt_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

img\_mgmt.h File Reference

`#include <[inttypes.h](inttypes_8h_source.md)>`  
`#include <[zephyr/mgmt/mcumgr/mgmt/mgmt.h](mgmt_8h_source.md)>`  
`#include <[zephyr/mgmt/mcumgr/smp/smp.h](mgmt_2mcumgr_2smp_2smp_8h_source.md)>`  
`#include <bootutil/image.h>`  
`#include <zcbor_common.h>`

[Go to the source code of this file.](img__mgmt_8h_source.md)

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
| #define | [IMG\_MGMT\_DATA\_SHA\_LEN](group__mcumgr__img__mgmt.md#ga70168b0d707c15658fd09b02c361a64c)   32 /\* SHA256 \*/ |
| #define | [IMG\_MGMT\_STATE\_F\_PENDING](group__mcumgr__img__mgmt.md#ga459776db5ce7bbfebae5e74aef4067ef)   0x01 |
|  | Image state flags. |
| #define | [IMG\_MGMT\_STATE\_F\_CONFIRMED](group__mcumgr__img__mgmt.md#ga581c2626a47ca249ecbcc42edb7a59c2)   0x02 |
| #define | [IMG\_MGMT\_STATE\_F\_ACTIVE](group__mcumgr__img__mgmt.md#ga2a11cfad9698b0460b846fa079234c03)   0x04 |
| #define | [IMG\_MGMT\_STATE\_F\_PERMANENT](group__mcumgr__img__mgmt.md#gae47e88131d96901e70b2b67ea43ceb4a)   0x08 |
| #define | [IMG\_MGMT\_VER\_MAX\_STR\_LEN](group__mcumgr__img__mgmt.md#ga57a5c429be5a3860981007e9728db181)   ([sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)("255.255.65535.4294967295")) |
| #define | [IMG\_MGMT\_SWAP\_TYPE\_NONE](group__mcumgr__img__mgmt.md#ga55e68ef4a5caa3c68987af438ebe8236)   0 |
|  | Swap Types for image management state machine. |
| #define | [IMG\_MGMT\_SWAP\_TYPE\_TEST](group__mcumgr__img__mgmt.md#ga71a0715be72de416f3d4744f4763a241)   1 |
| #define | [IMG\_MGMT\_SWAP\_TYPE\_PERM](group__mcumgr__img__mgmt.md#ga69c51ca39c8d33db392e2353873aac43)   2 |
| #define | [IMG\_MGMT\_SWAP\_TYPE\_REVERT](group__mcumgr__img__mgmt.md#ga43a9afd49822eda7b640d3adb9219f10)   3 |
| #define | [IMG\_MGMT\_SWAP\_TYPE\_UNKNOWN](group__mcumgr__img__mgmt.md#ga35a8dd8ca661f2a602bc04d4ae6361a6)   255 |
| #define | [IMG\_MGMT\_ID\_STATE](group__mcumgr__img__mgmt.md#ga19396c2690a0d40f625792ab644e7d17)   0 |
|  | Command IDs for image management group. |
| #define | [IMG\_MGMT\_ID\_UPLOAD](group__mcumgr__img__mgmt.md#ga70541d06c76224a631f493023e05a73a)   1 |
| #define | [IMG\_MGMT\_ID\_FILE](group__mcumgr__img__mgmt.md#ga90225baf3e08859f294d9aaaf2012e6b)   2 |
| #define | [IMG\_MGMT\_ID\_CORELIST](group__mcumgr__img__mgmt.md#ga46e9a83aab777da2591d4c7cb701b5cd)   3 |
| #define | [IMG\_MGMT\_ID\_CORELOAD](group__mcumgr__img__mgmt.md#ga22af869af6cbdde12f2cbc811fe7d443)   4 |
| #define | [IMG\_MGMT\_ID\_ERASE](group__mcumgr__img__mgmt.md#gaf7de4c1d77bc29eea4b3d46382bd954f)   5 |
| #define | [IMG\_MGMT\_UPLOAD\_ACTION\_SET\_RC\_RSN](group__mcumgr__img__mgmt.md#ga56e01e5bfa9fdd9bf6ebdc0dc3ac19ba)(action, rsn) |
| #define | [IMG\_MGMT\_UPLOAD\_ACTION\_RC\_RSN](group__mcumgr__img__mgmt.md#gaee07bacea29269e24ca15a2e1716390d)(action) |

| Enumerations | |
| --- | --- |
| enum | [img\_mgmt\_err\_code\_t](group__mcumgr__img__mgmt.md#ga669286d96816e0e99792f407752c81a5) {     [IMG\_MGMT\_ERR\_OK](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a7db18fe6cb5913fec882dc515d8bb7a0) = 0 , [IMG\_MGMT\_ERR\_UNKNOWN](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a8f1bd00b3e00f070b07269fdddd2c8fe) , [IMG\_MGMT\_ERR\_FLASH\_CONFIG\_QUERY\_FAIL](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a5b4301665ef0c9818fcd3174908e5063) , [IMG\_MGMT\_ERR\_NO\_IMAGE](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a360155fc7e541080a7b80bee6ec9dbb6) ,     [IMG\_MGMT\_ERR\_NO\_TLVS](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a598c03b99a2be60cf4847fa2f32c5d10) , [IMG\_MGMT\_ERR\_INVALID\_TLV](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a4725027793b17187474089fde35730cb) , [IMG\_MGMT\_ERR\_TLV\_MULTIPLE\_HASHES\_FOUND](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5aced7bb74d51b7dd7ff922cf555722276) , [IMG\_MGMT\_ERR\_TLV\_INVALID\_SIZE](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a967c4f0b3d33d925e28f076c8cc3ed5c) ,     [IMG\_MGMT\_ERR\_HASH\_NOT\_FOUND](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a5d89dde479611276e6956706ee357c6e) , [IMG\_MGMT\_ERR\_NO\_FREE\_SLOT](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a0d16138a65766047e4917022068832fa) , [IMG\_MGMT\_ERR\_FLASH\_OPEN\_FAILED](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a8253896c206d8f3ba486466555662071) , [IMG\_MGMT\_ERR\_FLASH\_READ\_FAILED](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a9a09d73602a77e112a95fa977e9b0355) ,     [IMG\_MGMT\_ERR\_FLASH\_WRITE\_FAILED](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5adf54010236b4e6bb4669cdeeb4a6979f) , [IMG\_MGMT\_ERR\_FLASH\_ERASE\_FAILED](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a869d0aa27c38187fdb73d36397dcef3c) , [IMG\_MGMT\_ERR\_INVALID\_SLOT](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a7c0f0cda8165d0acf5fc2a072a5c5cc5) , [IMG\_MGMT\_ERR\_NO\_FREE\_MEMORY](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5ab75ac303b054a02e99a0ed9726c988de) ,     [IMG\_MGMT\_ERR\_FLASH\_CONTEXT\_ALREADY\_SET](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5af1eac867913981a4d8f1f2d64108706e) , [IMG\_MGMT\_ERR\_FLASH\_CONTEXT\_NOT\_SET](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a9e4c9f1a79f645130ef9a8aa09b8b544) , [IMG\_MGMT\_ERR\_FLASH\_AREA\_DEVICE\_NULL](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a6c1c103d76e1f16fda77525ba136e9b2) , [IMG\_MGMT\_ERR\_INVALID\_PAGE\_OFFSET](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a857b6ecc22e5f54834638aa604cce6bf) ,     [IMG\_MGMT\_ERR\_INVALID\_OFFSET](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a8a94dfe1aca340c4337fe92554ede4b0) , [IMG\_MGMT\_ERR\_INVALID\_LENGTH](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a227b2b3be93cf963ce034b9cb817d0ca) , [IMG\_MGMT\_ERR\_INVALID\_IMAGE\_HEADER](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5acfdb28d59643e70db86abfa72c2833b7) , [IMG\_MGMT\_ERR\_INVALID\_IMAGE\_HEADER\_MAGIC](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a5606b72a7bf61832b92c77e729e02093) ,     [IMG\_MGMT\_ERR\_INVALID\_HASH](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a4b2994e51eadae6cb43c3683d6e223b6) , [IMG\_MGMT\_ERR\_INVALID\_FLASH\_ADDRESS](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a27502b76efcc09ef01cfbe777a9e8086) , [IMG\_MGMT\_ERR\_VERSION\_GET\_FAILED](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5ae710879342357f27c9705989f572b82f) , [IMG\_MGMT\_ERR\_CURRENT\_VERSION\_IS\_NEWER](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a37ad5efbaacdcb708a65674a4dc83d85) ,     [IMG\_MGMT\_ERR\_IMAGE\_ALREADY\_PENDING](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5af55239776b4b5a5eead0440fb3b884b3) , [IMG\_MGMT\_ERR\_INVALID\_IMAGE\_VECTOR\_TABLE](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a3a8d3005c72273ee065c34396d3fd2f7) , [IMG\_MGMT\_ERR\_INVALID\_IMAGE\_TOO\_LARGE](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5ab258cd53a5cc13e2376662690703f54b) , [IMG\_MGMT\_ERR\_INVALID\_IMAGE\_DATA\_OVERRUN](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a92ab3773cdbd00b42fb59865e958069b) ,     [IMG\_MGMT\_ERR\_IMAGE\_CONFIRMATION\_DENIED](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5ae2413b0ade3185b91ae085af397adabf) , [IMG\_MGMT\_ERR\_IMAGE\_SETTING\_TEST\_TO\_ACTIVE\_DENIED](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5ab195578794ddc6cffa5e056ee34350a8) , [IMG\_MGMT\_ERR\_ACTIVE\_SLOT\_NOT\_KNOWN](group__mcumgr__img__mgmt.md#gga669286d96816e0e99792f407752c81a5a3220405113525f3d5af068b8bf2a80f6)   } |
|  | Command result codes for image management group. [More...](group__mcumgr__img__mgmt.md#ga669286d96816e0e99792f407752c81a5) |
| enum | [img\_mgmt\_id\_upload\_t](group__mcumgr__img__mgmt.md#ga1d239fef127e65b11b71360eadfa1ede) { [IMG\_MGMT\_ID\_UPLOAD\_STATUS\_START](group__mcumgr__img__mgmt.md#gga1d239fef127e65b11b71360eadfa1edeaff49286e379bd39781a563c1e52c6c8c) = 0 , [IMG\_MGMT\_ID\_UPLOAD\_STATUS\_ONGOING](group__mcumgr__img__mgmt.md#gga1d239fef127e65b11b71360eadfa1edea7cf567b16af18752316fde6444e23a21) , [IMG\_MGMT\_ID\_UPLOAD\_STATUS\_COMPLETE](group__mcumgr__img__mgmt.md#gga1d239fef127e65b11b71360eadfa1edeab106874625a50d626e55130e91d37bf2) } |
|  | IMG\_MGMT\_ID\_UPLOAD statuses. [More...](group__mcumgr__img__mgmt.md#ga1d239fef127e65b11b71360eadfa1ede) |

| Functions | |
| --- | --- |
| int | [img\_mgmt\_read\_info](group__mcumgr__img__mgmt.md#ga60ae88823a561160b1ddc406382e4ac3) (int image\_slot, struct image\_version \*ver, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*hash, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
| int | [img\_mgmt\_my\_version](group__mcumgr__img__mgmt.md#gae9cfa02e5f171d68287cdb0d7d4c0610) (struct image\_version \*ver) |
|  | Get the image version of the currently running application. |
| int | [img\_mgmt\_ver\_str](group__mcumgr__img__mgmt.md#ga5199849b6d8847c6a1260254940db95b) (const struct image\_version \*ver, char \*dst) |
|  | Format version string from struct image\_version. |
| int | [img\_mgmt\_active\_slot](group__mcumgr__img__mgmt.md#gab35c8adf2e5e2c941ecbaf3c03101e55) (int image) |
|  | Get active, running application slot number for an image. |
| int | [img\_mgmt\_active\_image](group__mcumgr__img__mgmt.md#gab6a92433b859fce18b58e6110fa5f489) (void) |
|  | Get active image number. |
| int | [img\_mgmt\_slot\_in\_use](group__mcumgr__img__mgmt.md#ga90de2da23bcd650ca59219fdfd4f55a1) (int slot) |
|  | Check if the image slot is in use. |
| int | [img\_mgmt\_state\_any\_pending](group__mcumgr__img__mgmt.md#ga3e496199d0ea4aa1b3f51e59bb7473f0) (void) |
|  | Check if any slot is in MCUboot pending state. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [img\_mgmt\_state\_flags](group__mcumgr__img__mgmt.md#ga42475389b4e31d5f35ea58873527e948) (int query\_slot) |
|  | Returns state flags set to slot. |
| int | [img\_mgmt\_state\_set\_pending](group__mcumgr__img__mgmt.md#ga7e529fa76ddb3d3bf4a527cb11fa9c89) (int slot, int permanent) |
|  | Sets the pending flag for the specified image slot. |
| int | [img\_mgmt\_state\_confirm](group__mcumgr__img__mgmt.md#gaed0b945d2f83daf63d850b232a2cfea8) (void) |
|  | Confirms the current image state. |
| int | [img\_mgmt\_vercmp](group__mcumgr__img__mgmt.md#ga6c9124cc59c99769908cdf83f58e1bf1) (const struct image\_version \*a, const struct image\_version \*b) |
|  | Compares two image version numbers in a semver-compatible way. |

| Variables | |
| --- | --- |
| int | [boot\_current\_slot](group__mcumgr__img__mgmt.md#ga0d6bb8877516ca486c318fa12c129138) |
| struct [img\_mgmt\_state](structimg__mgmt__state.md) | [g\_img\_mgmt\_state](group__mcumgr__img__mgmt.md#gad3dce7b70ce3338588003a021eec1ab6) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [grp](dir_75a5d043a2b1048bf3665f6cb87645f5.md)
- [img\_mgmt](dir_731c1b2142dfc9d7fee3a06aa394438e.md)
- [img\_mgmt.h](img__mgmt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
