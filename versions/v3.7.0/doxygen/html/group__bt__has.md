---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__bt__has.html
original_path: doxygen/html/group__bt__has.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Hearing Access Service (HAS)

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

Hearing Access Service (HAS).
[More...](#details)

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
| #define | [BT\_HAS\_PRESET\_NAME\_MIN](#gacbc29958c09b26a81e02893cd5914074)   1 |
|  | Preset name minimum length. |
| #define | [BT\_HAS\_PRESET\_NAME\_MAX](#gae133807f12d0d7a1ecd1f8dda24c7f09)   40 |
|  | Preset name maximum length. |

| Typedefs | |
| --- | --- |
| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)(\* | [bt\_has\_preset\_func\_t](#ga4b8e97b1aeed16ac8356953ca4008ec6)) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index, enum [bt\_has\_properties](#ga7b8913a9f9bc4d5c066582780adcf274) properties, const char \*name, void \*user\_data) |
|  | Preset iterator callback. |

| Enumerations | |
| --- | --- |
| enum | [bt\_has\_hearing\_aid\_type](#gaa9572a32f912c8fe529b510aa23f4540) { [BT\_HAS\_HEARING\_AID\_TYPE\_BINAURAL](#ggaa9572a32f912c8fe529b510aa23f4540a5bc91d6bcba7e140cc642715ccc9879c) = 0x00 , [BT\_HAS\_HEARING\_AID\_TYPE\_MONAURAL](#ggaa9572a32f912c8fe529b510aa23f4540a4b711ff711e81a22b7e80f7dc8a4aae8) = 0x01 , [BT\_HAS\_HEARING\_AID\_TYPE\_BANDED](#ggaa9572a32f912c8fe529b510aa23f4540af9e7c56173aeeb593f9e12a0e3366a0b) = 0x02 } |
|  | Hearing Aid device type. [More...](#gaa9572a32f912c8fe529b510aa23f4540) |
| enum | [bt\_has\_properties](#ga7b8913a9f9bc4d5c066582780adcf274) { [BT\_HAS\_PROP\_NONE](#gga7b8913a9f9bc4d5c066582780adcf274a70645a9bfc628425b93b0aa6ce539173) = 0 , [BT\_HAS\_PROP\_WRITABLE](#gga7b8913a9f9bc4d5c066582780adcf274ad479ec0e277e2e894d0056965b484e09) = BIT(0) , [BT\_HAS\_PROP\_AVAILABLE](#gga7b8913a9f9bc4d5c066582780adcf274ad10fb0dd29c8e7a7c733f87c92bfee59) = BIT(1) } |
|  | Preset Properties values. [More...](#ga7b8913a9f9bc4d5c066582780adcf274) |
| enum | [bt\_has\_capabilities](#ga50d470390967317cb84b17fd450546a4) { [BT\_HAS\_PRESET\_SUPPORT](#gga50d470390967317cb84b17fd450546a4a885520fe7fa533b6ea79db7ebeeed258) = BIT(0) } |
|  | Hearing Aid device capabilities. [More...](#ga50d470390967317cb84b17fd450546a4) |
| enum | { [BT\_HAS\_PRESET\_ITER\_STOP](#ggaeb9b1dcf3e33fac6c44aa952c478f917af9ea42147bbce222b024fb922c52daaa) = 0 , [BT\_HAS\_PRESET\_ITER\_CONTINUE](#ggaeb9b1dcf3e33fac6c44aa952c478f917a5acb1c7f3113a21e19e4a37fd8e099bf) } |
|  | Enum for return values for [bt\_has\_preset\_func\_t](#ga4b8e97b1aeed16ac8356953ca4008ec6) functions. [More...](#gaeb9b1dcf3e33fac6c44aa952c478f917) |

| Functions | |
| --- | --- |
| int | [bt\_has\_client\_cb\_register](#ga9bc61dfc710070fb136120944c0776b9) (const struct [bt\_has\_client\_cb](structbt__has__client__cb.md) \*cb) |
|  | Registers the callbacks used by the Hearing Access Service client. |
| int | [bt\_has\_client\_discover](#gaf3765300072b0a6d1ee45699e710d4da) (struct bt\_conn \*conn) |
|  | Discover Hearing Access Service on a remote device. |
| int | [bt\_has\_client\_conn\_get](#ga8303b5fb2558a35bb2cb06cd5788e636) (const struct bt\_has \*has, struct bt\_conn \*\*conn) |
|  | Get the Bluetooth connection object of the service object. |
| int | [bt\_has\_client\_presets\_read](#ga54ef9918e4fb458b7416ffb94acca808) (struct bt\_has \*has, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) max\_count) |
|  | Read Preset Records. |
| int | [bt\_has\_client\_preset\_set](#ga4a228ee29a26346867a6427f81816336) (struct bt\_has \*has, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sync) |
|  | Set Active Preset. |
| int | [bt\_has\_client\_preset\_next](#ga66943cb5275ca660f2eab11e37708d81) (struct bt\_has \*has, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sync) |
|  | Activate Next Preset. |
| int | [bt\_has\_client\_preset\_prev](#ga3a564b18ce6cbc7a5af970474ddf25a2) (struct bt\_has \*has, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sync) |
|  | Activate Previous Preset. |
| int | [bt\_has\_register](#gac39ca2d72273bd591618d186b48c20b0) (const struct [bt\_has\_features\_param](structbt__has__features__param.md) \*features) |
|  | Register the Hearing Access Service instance. |
| int | [bt\_has\_preset\_register](#gadf0a488721910633fa2b54b2c7645bd9) (const struct [bt\_has\_preset\_register\_param](structbt__has__preset__register__param.md) \*param) |
|  | Register preset. |
| int | [bt\_has\_preset\_unregister](#ga39f9ac2f94b1febe8e834ae54e110e90) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index) |
|  | Unregister Preset. |
| int | [bt\_has\_preset\_available](#gacaa997913949b6ea98c5c6233fefdc52) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index) |
|  | Set the preset as available. |
| int | [bt\_has\_preset\_unavailable](#gabe523e1aefc789ad0031e3c0efb27379) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index) |
|  | Set the preset as unavailable. |
| void | [bt\_has\_preset\_foreach](#ga8e366c90dc240acc6d4b40d087154eba) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index, [bt\_has\_preset\_func\_t](#ga4b8e97b1aeed16ac8356953ca4008ec6) func, void \*user\_data) |
|  | Preset iterator. |
| int | [bt\_has\_preset\_active\_set](#ga2c0fe62baa63b72703d6f553f1de072b) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index) |
|  | Set active preset. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_has\_preset\_active\_get](#gae1787671fac3b7873c5994adc7d19b20) (void) |
|  | Get active preset. |
| static int | [bt\_has\_preset\_active\_clear](#ga715cfe5bd08fbd4557ee6052b38f27de) (void) |
|  | Clear out active preset. |
| int | [bt\_has\_preset\_name\_change](#ga6f06adc529a500fcfcfea2ae89ea60d5) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index, const char \*name) |
|  | Change the Preset Name. |
| int | [bt\_has\_features\_set](#ga7e37a89b1bf0a732045276cf6b922956) (const struct [bt\_has\_features\_param](structbt__has__features__param.md) \*features) |
|  | Change the Hearing Aid Features. |

| Preset index definitions | |
| --- | --- |
| #define | [BT\_HAS\_PRESET\_INDEX\_NONE](#ga462679b8b5c91762c6d1daf03c5675d0)   0x00 |
|  | No index. |
| #define | [BT\_HAS\_PRESET\_INDEX\_FIRST](#ga38df8301e78111dc1e6241594a9bf8c3)   0x01 |
|  | First preset index. |
| #define | [BT\_HAS\_PRESET\_INDEX\_LAST](#ga2e1b80739eeb56d8e0b7779c3d488faa)   0xFF |
|  | Last preset index. |

## Detailed Description

Hearing Access Service (HAS).

Since
:   3.1

Version
:   0.8.0

The Hearing Access Service is used to identify a hearing aid and optionally to control hearing aid presets.

## Macro Definition Documentation

## [◆ ](#ga38df8301e78111dc1e6241594a9bf8c3)BT\_HAS\_PRESET\_INDEX\_FIRST

| #define BT\_HAS\_PRESET\_INDEX\_FIRST   0x01 |
| --- |

`#include <[has.h](has_8h.md)>`

First preset index.

## [◆ ](#ga2e1b80739eeb56d8e0b7779c3d488faa)BT\_HAS\_PRESET\_INDEX\_LAST

| #define BT\_HAS\_PRESET\_INDEX\_LAST   0xFF |
| --- |

`#include <[has.h](has_8h.md)>`

Last preset index.

## [◆ ](#ga462679b8b5c91762c6d1daf03c5675d0)BT\_HAS\_PRESET\_INDEX\_NONE

| #define BT\_HAS\_PRESET\_INDEX\_NONE   0x00 |
| --- |

`#include <[has.h](has_8h.md)>`

No index.

## [◆ ](#gae133807f12d0d7a1ecd1f8dda24c7f09)BT\_HAS\_PRESET\_NAME\_MAX

| #define BT\_HAS\_PRESET\_NAME\_MAX   40 |
| --- |

`#include <[has.h](has_8h.md)>`

Preset name maximum length.

## [◆ ](#gacbc29958c09b26a81e02893cd5914074)BT\_HAS\_PRESET\_NAME\_MIN

| #define BT\_HAS\_PRESET\_NAME\_MIN   1 |
| --- |

`#include <[has.h](has_8h.md)>`

Preset name minimum length.

## Typedef Documentation

## [◆ ](#ga4b8e97b1aeed16ac8356953ca4008ec6)bt\_has\_preset\_func\_t

| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)(\* bt\_has\_preset\_func\_t) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index, enum [bt\_has\_properties](#ga7b8913a9f9bc4d5c066582780adcf274) properties, const char \*name, void \*user\_data) |
| --- |

`#include <[has.h](has_8h.md)>`

Preset iterator callback.

Parameters
:   | index | The index of preset found. |
    | --- | --- |
    | properties | Preset properties. |
    | name | Preset name. |
    | user\_data | Data given. |

Returns
:   BT\_HAS\_PRESET\_ITER\_CONTINUE if should continue to the next preset.
:   BT\_HAS\_PRESET\_ITER\_STOP to stop.

## Enumeration Type Documentation

## [◆ ](#gaeb9b1dcf3e33fac6c44aa952c478f917)anonymous enum

| anonymous enum |
| --- |

`#include <[has.h](has_8h.md)>`

Enum for return values for [bt\_has\_preset\_func\_t](#ga4b8e97b1aeed16ac8356953ca4008ec6) functions.

| Enumerator | |
| --- | --- |
| BT\_HAS\_PRESET\_ITER\_STOP | Stop iterating. |
| BT\_HAS\_PRESET\_ITER\_CONTINUE | Continue iterating. |

## [◆ ](#ga50d470390967317cb84b17fd450546a4)bt\_has\_capabilities

| enum [bt\_has\_capabilities](#ga50d470390967317cb84b17fd450546a4) |
| --- |

`#include <[has.h](has_8h.md)>`

Hearing Aid device capabilities.

| Enumerator | |
| --- | --- |
| BT\_HAS\_PRESET\_SUPPORT | Indicate support for presets. |

## [◆ ](#gaa9572a32f912c8fe529b510aa23f4540)bt\_has\_hearing\_aid\_type

| enum [bt\_has\_hearing\_aid\_type](#gaa9572a32f912c8fe529b510aa23f4540) |
| --- |

`#include <[has.h](has_8h.md)>`

Hearing Aid device type.

| Enumerator | |
| --- | --- |
| BT\_HAS\_HEARING\_AID\_TYPE\_BINAURAL | Two hearing aids that form a Coordinated Set, one for the right ear and one for the left ear of the user.  Typically used by a user with bilateral hearing loss. |
| BT\_HAS\_HEARING\_AID\_TYPE\_MONAURAL | A single hearing aid for the left or the right ear.  Typically used by a user with unilateral hearing loss. |
| BT\_HAS\_HEARING\_AID\_TYPE\_BANDED | Two hearing aids with a connection to one another that expose a single Bluetooth radio interface. |

## [◆ ](#ga7b8913a9f9bc4d5c066582780adcf274)bt\_has\_properties

| enum [bt\_has\_properties](#ga7b8913a9f9bc4d5c066582780adcf274) |
| --- |

`#include <[has.h](has_8h.md)>`

Preset Properties values.

| Enumerator | |
| --- | --- |
| BT\_HAS\_PROP\_NONE | No properties set. |
| BT\_HAS\_PROP\_WRITABLE | Preset name can be written by the client. |
| BT\_HAS\_PROP\_AVAILABLE | Preset availability. |

## Function Documentation

## [◆ ](#ga9bc61dfc710070fb136120944c0776b9)bt\_has\_client\_cb\_register()

| int bt\_has\_client\_cb\_register | ( | const struct [bt\_has\_client\_cb](structbt__has__client__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[has.h](has_8h.md)>`

Registers the callbacks used by the Hearing Access Service client.

Parameters
:   | cb | The callback structure. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga8303b5fb2558a35bb2cb06cd5788e636)bt\_has\_client\_conn\_get()

| int bt\_has\_client\_conn\_get | ( | const struct bt\_has \* | *has*, |
| --- | --- | --- | --- |
|  |  | struct bt\_conn \*\* | *conn* ) |

`#include <[has.h](has_8h.md)>`

Get the Bluetooth connection object of the service object.

The caller gets a new reference to the connection object which must be released with [bt\_conn\_unref()](group__bt__conn.md#ga4b18c6b22a9f02be0d7d078b2ce51ff6 "Decrement a connection's reference count.") once done using the object.

Parameters
:   | [in] | has | Pointer to the Hearing Access Service object. |
    | --- | --- | --- |
    | [out] | conn | Connection object. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gaf3765300072b0a6d1ee45699e710d4da)bt\_has\_client\_discover()

| int bt\_has\_client\_discover | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[has.h](has_8h.md)>`

Discover Hearing Access Service on a remote device.

Client method to find a Hearing Access Service on a server identified by `conn`. The [bt\_has\_client\_cb::discover](structbt__has__client__cb.md#acf35d62cce0c2181e2eefd8c43e3b568 "bt_has_client_cb::discover") callback will be called when the discovery procedure is complete to provide user a [Hearing Access Service (HAS)](group__bt__has.md "Hearing Access Service (HAS)") object.

Parameters
:   | conn | Bluetooth connection object. |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga66943cb5275ca660f2eab11e37708d81)bt\_has\_client\_preset\_next()

| int bt\_has\_client\_preset\_next | ( | struct bt\_has \* | *has*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *sync* ) |

`#include <[has.h](has_8h.md)>`

Activate Next Preset.

Client procedure to set next available preset as active. The status is returned in the [bt\_has\_client\_cb::preset\_switch](structbt__has__client__cb.md#a4217754818ad047f287aceda8326bf99 "bt_has_client_cb::preset_switch") callback.

Parameters
:   | has | Pointer to the Hearing Access Service object. |
    | --- | --- |
    | sync | Request active preset synchronization in set. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga3a564b18ce6cbc7a5af970474ddf25a2)bt\_has\_client\_preset\_prev()

| int bt\_has\_client\_preset\_prev | ( | struct bt\_has \* | *has*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *sync* ) |

`#include <[has.h](has_8h.md)>`

Activate Previous Preset.

Client procedure to set previous available preset as active. The status is returned in the [bt\_has\_client\_cb::preset\_switch](structbt__has__client__cb.md#a4217754818ad047f287aceda8326bf99 "bt_has_client_cb::preset_switch") callback.

Parameters
:   | has | Pointer to the Hearing Access Service object. |
    | --- | --- |
    | sync | Request active preset synchronization in set. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga4a228ee29a26346867a6427f81816336)bt\_has\_client\_preset\_set()

| int bt\_has\_client\_preset\_set | ( | struct bt\_has \* | *has*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *index*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *sync* ) |

`#include <[has.h](has_8h.md)>`

Set Active Preset.

Client procedure to set preset identified by `index` as active. The status is returned in the [bt\_has\_client\_cb::preset\_switch](structbt__has__client__cb.md#a4217754818ad047f287aceda8326bf99 "bt_has_client_cb::preset_switch") callback.

Parameters
:   | has | Pointer to the Hearing Access Service object. |
    | --- | --- |
    | index | Preset index to activate. |
    | sync | Request active preset synchronization in set. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga54ef9918e4fb458b7416ffb94acca808)bt\_has\_client\_presets\_read()

| int bt\_has\_client\_presets\_read | ( | struct bt\_has \* | *has*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *index*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *max\_count* ) |

`#include <[has.h](has_8h.md)>`

Read Preset Records.

Client method to read up to `max_count` presets starting from given `index`. The preset records are returned in the [bt\_has\_client\_cb::preset\_read\_rsp](structbt__has__client__cb.md#a50759c76add5f4f76e23e742ae3ebe1b "bt_has_client_cb::preset_read_rsp") callback (called once for each preset).

Parameters
:   | has | Pointer to the Hearing Access Service object. |
    | --- | --- |
    | index | The index to start with. |
    | max\_count | Maximum number of presets to read. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga7e37a89b1bf0a732045276cf6b922956)bt\_has\_features\_set()

| int bt\_has\_features\_set | ( | const struct [bt\_has\_features\_param](structbt__has__features__param.md) \* | *features* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[has.h](has_8h.md)>`

Change the Hearing Aid Features.

Change the hearing aid features.

Parameters
:   | features | The features to be set. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga715cfe5bd08fbd4557ee6052b38f27de)bt\_has\_preset\_active\_clear()

| | int bt\_has\_preset\_active\_clear | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[has.h](has_8h.md)>`

Clear out active preset.

Used by server to deactivate currently active preset.

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gae1787671fac3b7873c5994adc7d19b20)bt\_has\_preset\_active\_get()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_has\_preset\_active\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[has.h](has_8h.md)>`

Get active preset.

Function used to get the currently active preset index.

Returns
:   Active preset index.

## [◆ ](#ga2c0fe62baa63b72703d6f553f1de072b)bt\_has\_preset\_active\_set()

| int bt\_has\_preset\_active\_set | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *index* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[has.h](has_8h.md)>`

Set active preset.

Function used to set the preset identified by the `index` as the active preset. The preset index will be notified to peer devices.

Parameters
:   | index | Preset index. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gacaa997913949b6ea98c5c6233fefdc52)bt\_has\_preset\_available()

| int bt\_has\_preset\_available | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *index* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[has.h](has_8h.md)>`

Set the preset as available.

Set the [BT\_HAS\_PROP\_AVAILABLE](#gga7b8913a9f9bc4d5c066582780adcf274ad10fb0dd29c8e7a7c733f87c92bfee59) property bit. This will notify preset availability to peer devices. Only available preset can be selected as active preset.

Parameters
:   | index | The index of preset that's became available. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga8e366c90dc240acc6d4b40d087154eba)bt\_has\_preset\_foreach()

| void bt\_has\_preset\_foreach | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *index*, |
| --- | --- | --- | --- |
|  |  | [bt\_has\_preset\_func\_t](#ga4b8e97b1aeed16ac8356953ca4008ec6) | *func*, |
|  |  | void \* | *user\_data* ) |

`#include <[has.h](has_8h.md)>`

Preset iterator.

Iterate presets. Optionally, match non-zero index if given.

Parameters
:   | index | Preset index, passing [BT\_HAS\_PRESET\_INDEX\_NONE](#ga462679b8b5c91762c6d1daf03c5675d0) skips index matching. |
    | --- | --- |
    | func | Callback function. |
    | user\_data | Data to pass to the callback. |

## [◆ ](#ga6f06adc529a500fcfcfea2ae89ea60d5)bt\_has\_preset\_name\_change()

| int bt\_has\_preset\_name\_change | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *index*, |
| --- | --- | --- | --- |
|  |  | const char \* | *name* ) |

`#include <[has.h](has_8h.md)>`

Change the Preset Name.

Change the name of the preset identified by `index`.

Parameters
:   | index | The index of the preset to change the name of. |
    | --- | --- |
    | name | Name to write. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gadf0a488721910633fa2b54b2c7645bd9)bt\_has\_preset\_register()

| int bt\_has\_preset\_register | ( | const struct [bt\_has\_preset\_register\_param](structbt__has__preset__register__param.md) \* | *param* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[has.h](has_8h.md)>`

Register preset.

Register preset. The preset will be a added to the list of exposed preset records. This symbol is linkable if `CONFIG_BT_HAS_PRESET_COUNT` is non-zero.

Parameters
:   | param | Preset registration parameter. |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#gabe523e1aefc789ad0031e3c0efb27379)bt\_has\_preset\_unavailable()

| int bt\_has\_preset\_unavailable | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *index* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[has.h](has_8h.md)>`

Set the preset as unavailable.

Clear the [BT\_HAS\_PROP\_AVAILABLE](#gga7b8913a9f9bc4d5c066582780adcf274ad10fb0dd29c8e7a7c733f87c92bfee59) property bit. This will notify preset availability to peer devices. Unavailable preset cannot be selected as active preset.

Parameters
:   | index | The index of preset that's became unavailable. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga39f9ac2f94b1febe8e834ae54e110e90)bt\_has\_preset\_unregister()

| int bt\_has\_preset\_unregister | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *index* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[has.h](has_8h.md)>`

Unregister Preset.

Unregister preset. The preset will be removed from the list of preset records.

Parameters
:   | index | The index of preset that's being requested to unregister. |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#gac39ca2d72273bd591618d186b48c20b0)bt\_has\_register()

| int bt\_has\_register | ( | const struct [bt\_has\_features\_param](structbt__has__features__param.md) \* | *features* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[has.h](has_8h.md)>`

Register the Hearing Access Service instance.

Parameters
:   | features | Hearing Access Service register parameters. |
    | --- | --- |

Returns
:   0 if success, errno on failure.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
