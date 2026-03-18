---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__has__client__cb.html
original_path: doxygen/html/structbt__has__client__cb.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_has\_client\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Hearing Access Service (HAS)](group__bt__has.md)

Hearing Access Service Client callback structure.
[More...](#details)

`#include <[has.h](has_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [discover](#acf35d62cce0c2181e2eefd8c43e3b568) )(struct bt\_conn \*conn, int err, struct bt\_has \*has, enum [bt\_has\_hearing\_aid\_type](group__bt__has.md#gaa9572a32f912c8fe529b510aa23f4540) type, enum [bt\_has\_capabilities](group__bt__has.md#ga50d470390967317cb84b17fd450546a4) caps) |
|  | Callback function for bt\_has\_discover. |
| void(\* | [preset\_switch](#a4217754818ad047f287aceda8326bf99) )(struct bt\_has \*has, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index) |
|  | Callback function for Hearing Access Service active preset changes. |
| void(\* | [preset\_read\_rsp](#a50759c76add5f4f76e23e742ae3ebe1b) )(struct bt\_has \*has, int err, const struct [bt\_has\_preset\_record](structbt__has__preset__record.md) \*record, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) is\_last) |
|  | Callback function for presets read operation. |
| void(\* | [preset\_update](#aa54cf5f268e542947ffb30531b7702ba) )(struct bt\_has \*has, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index\_prev, const struct [bt\_has\_preset\_record](structbt__has__preset__record.md) \*record, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) is\_last) |
|  | Callback function for preset update notifications. |
| void(\* | [preset\_deleted](#a1c28e7b5542100ce93727ac097cc6dee) )(struct bt\_has \*has, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) is\_last) |
|  | Callback function for preset deletion notifications. |
| void(\* | [preset\_availability](#a903397650915f3335dd2b8cd4f51d293) )(struct bt\_has \*has, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) available, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) is\_last) |
|  | Callback function for preset availability notifications. |

## Detailed Description

Hearing Access Service Client callback structure.

## Field Documentation

## [◆ ](#acf35d62cce0c2181e2eefd8c43e3b568)discover

| void(\* bt\_has\_client\_cb::discover) (struct bt\_conn \*conn, int err, struct bt\_has \*has, enum [bt\_has\_hearing\_aid\_type](group__bt__has.md#gaa9572a32f912c8fe529b510aa23f4540) type, enum [bt\_has\_capabilities](group__bt__has.md#ga50d470390967317cb84b17fd450546a4) caps) |
| --- |

Callback function for bt\_has\_discover.

This callback is called when discovery procedure is complete.

Parameters
:   | conn | Bluetooth connection object. |
    | --- | --- |
    | err | 0 on success, ATT error or negative errno otherwise. |
    | has | Pointer to the Hearing Access Service object or NULL on errors. |
    | type | Hearing Aid type. |
    | caps | Hearing Aid capabilities. |

## [◆ ](#a903397650915f3335dd2b8cd4f51d293)preset\_availability

| void(\* bt\_has\_client\_cb::preset\_availability) (struct bt\_has \*has, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) available, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) is\_last) |
| --- |

Callback function for preset availability notifications.

The callback is called when the preset availability change is notified by the remote server.

Parameters
:   | has | Pointer to the Hearing Access Service object. |
    | --- | --- |
    | index | Preset index. |
    | available | True if available, false otherwise. |
    | is\_last | True if preset list update operation can be considered concluded. |

## [◆ ](#a1c28e7b5542100ce93727ac097cc6dee)preset\_deleted

| void(\* bt\_has\_client\_cb::preset\_deleted) (struct bt\_has \*has, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) is\_last) |
| --- |

Callback function for preset deletion notifications.

The callback is called when the preset has been deleted by the remote server.

Parameters
:   | has | Pointer to the Hearing Access Service object. |
    | --- | --- |
    | index | Preset index. |
    | is\_last | True if preset list update operation can be considered concluded. |

## [◆ ](#a50759c76add5f4f76e23e742ae3ebe1b)preset\_read\_rsp

| void(\* bt\_has\_client\_cb::preset\_read\_rsp) (struct bt\_has \*has, int err, const struct [bt\_has\_preset\_record](structbt__has__preset__record.md) \*record, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) is\_last) |
| --- |

Callback function for presets read operation.

The callback is called when the preset read response is sent by the remote server. The record object as well as its members are temporary and must be copied to in order to cache its information.

Parameters
:   | has | Pointer to the Hearing Access Service object. |
    | --- | --- |
    | err | 0 on success, ATT error or negative errno otherwise. |
    | record | Preset record or NULL on errors. |
    | is\_last | True if Read Presets operation can be considered concluded. |

## [◆ ](#a4217754818ad047f287aceda8326bf99)preset\_switch

| void(\* bt\_has\_client\_cb::preset\_switch) (struct bt\_has \*has, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index) |
| --- |

Callback function for Hearing Access Service active preset changes.

Optional callback called when the active preset is changed by the remote server when the preset switch procedure is complete. The callback must be set to receive active preset changes and enable support for switching presets. If the callback is not set, the Active Index and Control Point characteristics will not be discovered by [bt\_has\_client\_discover](group__bt__has.md#gaf3765300072b0a6d1ee45699e710d4da "bt_has_client_discover").

Parameters
:   | has | Pointer to the Hearing Access Service object. |
    | --- | --- |
    | err | 0 on success, ATT error or negative errno otherwise. |
    | index | Active preset index. |

## [◆ ](#aa54cf5f268e542947ffb30531b7702ba)preset\_update

| void(\* bt\_has\_client\_cb::preset\_update) (struct bt\_has \*has, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) index\_prev, const struct [bt\_has\_preset\_record](structbt__has__preset__record.md) \*record, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) is\_last) |
| --- |

Callback function for preset update notifications.

The callback is called when the preset record update is notified by the remote server. The record object as well as its objects are temporary and must be copied to in order to cache its information.

Parameters
:   | has | Pointer to the Hearing Access Service object. |
    | --- | --- |
    | index\_prev | Index of the previous preset in the list. |
    | record | Preset record. |
    | is\_last | True if preset list update operation can be considered concluded. |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[has.h](has_8h_source.md)

- [bt\_has\_client\_cb](structbt__has__client__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
