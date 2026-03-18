---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/has_8h.html
original_path: doxygen/html/has_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

has.h File Reference

`#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h_source.md)>`  
`#include <[zephyr/bluetooth/bluetooth.h](bluetooth_8h_source.md)>`  
`#include <[zephyr/sys/util.h](util_8h_source.md)>`

[Go to the source code of this file.](has_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_has\_features\_param](structbt__has__features__param.md) |
|  | Structure for registering features of a Hearing Access Service instance. [More...](structbt__has__features__param.md#details) |
| struct | [bt\_has\_preset\_record](structbt__has__preset__record.md) |
|  | Preset record definition. [More...](structbt__has__preset__record.md#details) |
| struct | [bt\_has\_client\_cb](structbt__has__client__cb.md) |
|  | Hearing Access Service Client callback structure. [More...](structbt__has__client__cb.md#details) |
| struct | [bt\_has\_preset\_ops](structbt__has__preset__ops.md) |
|  | Preset operations structure. [More...](structbt__has__preset__ops.md#details) |
| struct | [bt\_has\_preset\_register\_param](structbt__has__preset__register__param.md) |
|  | Register structure for preset. [More...](structbt__has__preset__register__param.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_HAS\_PRESET\_INDEX\_NONE](group__bt__has.md#ga462679b8b5c91762c6d1daf03c5675d0)   0x00 |
|  | Preset index definitions. |
| #define | [BT\_HAS\_PRESET\_INDEX\_FIRST](group__bt__has.md#ga38df8301e78111dc1e6241594a9bf8c3)   0x01 |
| #define | [BT\_HAS\_PRESET\_INDEX\_LAST](group__bt__has.md#ga2e1b80739eeb56d8e0b7779c3d488faa)   0xFF |
| #define | [BT\_HAS\_PRESET\_NAME\_MIN](group__bt__has.md#gacbc29958c09b26a81e02893cd5914074)   1 |
|  | Preset name minimum length. |
| #define | [BT\_HAS\_PRESET\_NAME\_MAX](group__bt__has.md#gae133807f12d0d7a1ecd1f8dda24c7f09)   40 |
|  | Preset name maximum length. |

| Typedefs | |
| --- | --- |
| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)(\* | [bt\_has\_preset\_func\_t](group__bt__has.md#ga4b8e97b1aeed16ac8356953ca4008ec6)) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index, enum [bt\_has\_properties](group__bt__has.md#ga7b8913a9f9bc4d5c066582780adcf274) properties, const char \*name, void \*user\_data) |
|  | Preset iterator callback. |

| Enumerations | |
| --- | --- |
| enum | [bt\_has\_hearing\_aid\_type](group__bt__has.md#gaa9572a32f912c8fe529b510aa23f4540) { [BT\_HAS\_HEARING\_AID\_TYPE\_BINAURAL](group__bt__has.md#ggaa9572a32f912c8fe529b510aa23f4540a5bc91d6bcba7e140cc642715ccc9879c) = 0x00 , [BT\_HAS\_HEARING\_AID\_TYPE\_MONAURAL](group__bt__has.md#ggaa9572a32f912c8fe529b510aa23f4540a4b711ff711e81a22b7e80f7dc8a4aae8) = 0x01 , [BT\_HAS\_HEARING\_AID\_TYPE\_BANDED](group__bt__has.md#ggaa9572a32f912c8fe529b510aa23f4540af9e7c56173aeeb593f9e12a0e3366a0b) = 0x02 } |
|  | Hearing Aid device type. [More...](group__bt__has.md#gaa9572a32f912c8fe529b510aa23f4540) |
| enum | [bt\_has\_properties](group__bt__has.md#ga7b8913a9f9bc4d5c066582780adcf274) { [BT\_HAS\_PROP\_NONE](group__bt__has.md#gga7b8913a9f9bc4d5c066582780adcf274a70645a9bfc628425b93b0aa6ce539173) = 0 , [BT\_HAS\_PROP\_WRITABLE](group__bt__has.md#gga7b8913a9f9bc4d5c066582780adcf274ad479ec0e277e2e894d0056965b484e09) = BIT(0) , [BT\_HAS\_PROP\_AVAILABLE](group__bt__has.md#gga7b8913a9f9bc4d5c066582780adcf274ad10fb0dd29c8e7a7c733f87c92bfee59) = BIT(1) } |
|  | Preset Properties values. [More...](group__bt__has.md#ga7b8913a9f9bc4d5c066582780adcf274) |
| enum | [bt\_has\_capabilities](group__bt__has.md#ga50d470390967317cb84b17fd450546a4) { [BT\_HAS\_PRESET\_SUPPORT](group__bt__has.md#gga50d470390967317cb84b17fd450546a4a885520fe7fa533b6ea79db7ebeeed258) = BIT(0) } |
|  | Hearing Aid device capablilities. [More...](group__bt__has.md#ga50d470390967317cb84b17fd450546a4) |
| enum | { [BT\_HAS\_PRESET\_ITER\_STOP](group__bt__has.md#ggaeb9b1dcf3e33fac6c44aa952c478f917af9ea42147bbce222b024fb922c52daaa) = 0 , [BT\_HAS\_PRESET\_ITER\_CONTINUE](group__bt__has.md#ggaeb9b1dcf3e33fac6c44aa952c478f917a5acb1c7f3113a21e19e4a37fd8e099bf) } |

| Functions | |
| --- | --- |
| int | [bt\_has\_client\_cb\_register](group__bt__has.md#ga9bc61dfc710070fb136120944c0776b9) (const struct [bt\_has\_client\_cb](structbt__has__client__cb.md) \*cb) |
|  | Registers the callbacks used by the Hearing Access Service client. |
| int | [bt\_has\_client\_discover](group__bt__has.md#gaf3765300072b0a6d1ee45699e710d4da) (struct bt\_conn \*conn) |
|  | Discover Hearing Access Service on a remote device. |
| int | [bt\_has\_client\_conn\_get](group__bt__has.md#ga8303b5fb2558a35bb2cb06cd5788e636) (const struct bt\_has \*has, struct bt\_conn \*\*conn) |
|  | Get the Bluetooth connection object of the service object. |
| int | [bt\_has\_client\_presets\_read](group__bt__has.md#ga54ef9918e4fb458b7416ffb94acca808) (struct bt\_has \*has, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) max\_count) |
|  | Read Preset Records. |
| int | [bt\_has\_client\_preset\_set](group__bt__has.md#ga4a228ee29a26346867a6427f81816336) (struct bt\_has \*has, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sync) |
|  | Set Active Preset. |
| int | [bt\_has\_client\_preset\_next](group__bt__has.md#ga66943cb5275ca660f2eab11e37708d81) (struct bt\_has \*has, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sync) |
|  | Activate Next Preset. |
| int | [bt\_has\_client\_preset\_prev](group__bt__has.md#ga3a564b18ce6cbc7a5af970474ddf25a2) (struct bt\_has \*has, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sync) |
|  | Activate Previous Preset. |
| int | [bt\_has\_register](group__bt__has.md#gac39ca2d72273bd591618d186b48c20b0) (const struct [bt\_has\_features\_param](structbt__has__features__param.md) \*features) |
|  | Register the Hearing Access Service instance. |
| int | [bt\_has\_preset\_register](group__bt__has.md#gadf0a488721910633fa2b54b2c7645bd9) (const struct [bt\_has\_preset\_register\_param](structbt__has__preset__register__param.md) \*param) |
|  | Register preset. |
| int | [bt\_has\_preset\_unregister](group__bt__has.md#ga39f9ac2f94b1febe8e834ae54e110e90) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index) |
|  | Unregister Preset. |
| int | [bt\_has\_preset\_available](group__bt__has.md#gacaa997913949b6ea98c5c6233fefdc52) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index) |
|  | Set the preset as available. |
| int | [bt\_has\_preset\_unavailable](group__bt__has.md#gabe523e1aefc789ad0031e3c0efb27379) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index) |
|  | Set the preset as unavailable. |
| void | [bt\_has\_preset\_foreach](group__bt__has.md#ga8e366c90dc240acc6d4b40d087154eba) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index, [bt\_has\_preset\_func\_t](group__bt__has.md#ga4b8e97b1aeed16ac8356953ca4008ec6) func, void \*user\_data) |
|  | Preset iterator. |
| int | [bt\_has\_preset\_active\_set](group__bt__has.md#ga2c0fe62baa63b72703d6f553f1de072b) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index) |
|  | Set active preset. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_has\_preset\_active\_get](group__bt__has.md#gae1787671fac3b7873c5994adc7d19b20) (void) |
|  | Get active preset. |
| static int | [bt\_has\_preset\_active\_clear](group__bt__has.md#ga715cfe5bd08fbd4557ee6052b38f27de) (void) |
|  | Clear out active preset. |
| int | [bt\_has\_preset\_name\_change](group__bt__has.md#ga6f06adc529a500fcfcfea2ae89ea60d5) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index, const char \*name) |
|  | Change the Preset Name. |
| int | [bt\_has\_features\_set](group__bt__has.md#ga7e37a89b1bf0a732045276cf6b922956) (const struct [bt\_has\_features\_param](structbt__has__features__param.md) \*features) |
|  | Change the Hearing Aid Features. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [has.h](has_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
