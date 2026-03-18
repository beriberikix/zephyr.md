---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/pacs_8h.html
original_path: doxygen/html/pacs_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pacs.h File Reference

`#include <[zephyr/bluetooth/audio/audio.h](bluetooth_2audio_2audio_8h_source.md)>`

[Go to the source code of this file.](pacs_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_pacs\_cap](structbt__pacs__cap.md) |
|  | Published Audio Capability structure. [More...](structbt__pacs__cap.md#details) |

| Typedefs | |
| --- | --- |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [bt\_pacs\_cap\_foreach\_func\_t](#a452591f80b6be5d79609b25ade2154a9)) (const struct [bt\_pacs\_cap](structbt__pacs__cap.md) \*cap, void \*user\_data) |
|  | Published Audio Capability iterator callback. |

| Functions | |
| --- | --- |
| void | [bt\_pacs\_cap\_foreach](#a31e2c7e9a4b5b6a291b96832c1218a49) (enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir, [bt\_pacs\_cap\_foreach\_func\_t](#a452591f80b6be5d79609b25ade2154a9) func, void \*user\_data) |
|  | Published Audio Capability iterator. |
| int | [bt\_pacs\_cap\_register](#a251b36d4f5775eea1f69873709f847cc) (enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir, struct [bt\_pacs\_cap](structbt__pacs__cap.md) \*cap) |
|  | Register Published Audio Capability. |
| int | [bt\_pacs\_cap\_unregister](#a4f6015eba63ffc7a9377afe54a290da1) (enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir, struct [bt\_pacs\_cap](structbt__pacs__cap.md) \*cap) |
|  | Unregister Published Audio Capability. |
| int | [bt\_pacs\_set\_location](#aff290fd59bb05012abcf405dbdc72884) (enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir, enum [bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8) location) |
|  | Set the location for an endpoint type. |
| int | [bt\_pacs\_set\_available\_contexts](#a29a1ec26c1e5e82e02eac39e1088332c) (enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir, enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) contexts) |
|  | Set the available contexts for an endpoint type. |
| enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) | [bt\_pacs\_get\_available\_contexts](#a437d824d0a944b6c30db492dbe28514f) (enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir) |
|  | Get the available contexts for an endpoint type. |
| int | [bt\_pacs\_conn\_set\_available\_contexts\_for\_conn](#a12f283d2daf72302a01cefb4a4a8fc70) (struct bt\_conn \*conn, enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir, enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) \*contexts) |
|  | Set the available contexts for a given connection. |
| enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) | [bt\_pacs\_get\_available\_contexts\_for\_conn](#a7b28aa42525344445b20bb90a19441aa) (struct bt\_conn \*conn, enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir) |
|  | Get the available contexts for a given connection. |
| int | [bt\_pacs\_set\_supported\_contexts](#abae9cf025f32ce80b660ebd7f95241b2) (enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir, enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) contexts) |
|  | Set the supported contexts for an endpoint type. |

## Typedef Documentation

## [◆ ](#a452591f80b6be5d79609b25ade2154a9)bt\_pacs\_cap\_foreach\_func\_t

| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* bt\_pacs\_cap\_foreach\_func\_t) (const struct [bt\_pacs\_cap](structbt__pacs__cap.md) \*cap, void \*user\_data) |
| --- |

Published Audio Capability iterator callback.

Parameters
:   | cap | Capability found. |
    | --- | --- |
    | user\_data | Data given. |

Returns
:   true to continue to the next capability
:   false to stop the iteration

## Function Documentation

## [◆ ](#a31e2c7e9a4b5b6a291b96832c1218a49)bt\_pacs\_cap\_foreach()

| void bt\_pacs\_cap\_foreach | ( | enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) | *dir*, |
| --- | --- | --- | --- |
|  |  | [bt\_pacs\_cap\_foreach\_func\_t](#a452591f80b6be5d79609b25ade2154a9) | *func*, |
|  |  | void \* | *user\_data* ) |

Published Audio Capability iterator.

Iterate capabilities with endpoint direction specified.

Parameters
:   | dir | Direction of the endpoint to look capability for. |
    | --- | --- |
    | func | Callback function. |
    | user\_data | Data to pass to the callback. |

## [◆ ](#a251b36d4f5775eea1f69873709f847cc)bt\_pacs\_cap\_register()

| int bt\_pacs\_cap\_register | ( | enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) | *dir*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_pacs\_cap](structbt__pacs__cap.md) \* | *cap* ) |

Register Published Audio Capability.

Register Audio Local Capability.

Parameters
:   | dir | Direction of the endpoint to register capability for. |
    | --- | --- |
    | cap | Capability structure. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#a4f6015eba63ffc7a9377afe54a290da1)bt\_pacs\_cap\_unregister()

| int bt\_pacs\_cap\_unregister | ( | enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) | *dir*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_pacs\_cap](structbt__pacs__cap.md) \* | *cap* ) |

Unregister Published Audio Capability.

Unregister Audio Local Capability.

Parameters
:   | dir | Direction of the endpoint to unregister capability for. |
    | --- | --- |
    | cap | Capability structure. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#a12f283d2daf72302a01cefb4a4a8fc70)bt\_pacs\_conn\_set\_available\_contexts\_for\_conn()

| int bt\_pacs\_conn\_set\_available\_contexts\_for\_conn | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) | *dir*, |
|  |  | enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) \* | *contexts* ) |

Set the available contexts for a given connection.

This function sets the available contexts value for a given `conn` connection object. If the `contexts` parameter is NULL the available contexts value is reset to default. The default value of the available contexts is set using [bt\_pacs\_set\_available\_contexts](#a29a1ec26c1e5e82e02eac39e1088332c) function. The Available Context Value is reset to default on ACL disconnection.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | dir | Direction of the endpoints to change available contexts for. |
    | contexts | The contexts to be set or NULL to reset to default. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#a437d824d0a944b6c30db492dbe28514f)bt\_pacs\_get\_available\_contexts()

| enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) bt\_pacs\_get\_available\_contexts | ( | enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) | *dir* | ) |  |
| --- | --- | --- | --- | --- | --- |

Get the available contexts for an endpoint type.

Parameters
:   | dir | Direction of the endpoints to get contexts for. |
    | --- | --- |

Returns
:   Bitmask of available contexts.

## [◆ ](#a7b28aa42525344445b20bb90a19441aa)bt\_pacs\_get\_available\_contexts\_for\_conn()

| enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) bt\_pacs\_get\_available\_contexts\_for\_conn | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) | *dir* ) |

Get the available contexts for a given connection.

This server function returns the available contexts value for a given `conn` connection object. The value returned is the one set with [bt\_pacs\_conn\_set\_available\_contexts\_for\_conn](#a12f283d2daf72302a01cefb4a4a8fc70) function or the default value set with [bt\_pacs\_set\_available\_contexts](#a29a1ec26c1e5e82e02eac39e1088332c) function.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | dir | Direction of the endpoints to get contexts for. |

Returns
:   Bitmask of available contexts.

Return values
:   | [BT\_AUDIO\_CONTEXT\_TYPE\_PROHIBITED](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a3cfcfa76adc5effdc1aa95d75e5da37a) | if `conn` or `dir` are invalid |
    | --- | --- |

## [◆ ](#a29a1ec26c1e5e82e02eac39e1088332c)bt\_pacs\_set\_available\_contexts()

| int bt\_pacs\_set\_available\_contexts | ( | enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) | *dir*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) | *contexts* ) |

Set the available contexts for an endpoint type.

Parameters
:   | dir | Direction of the endpoints to change available contexts for. |
    | --- | --- |
    | contexts | The contexts to be set. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#aff290fd59bb05012abcf405dbdc72884)bt\_pacs\_set\_location()

| int bt\_pacs\_set\_location | ( | enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) | *dir*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8) | *location* ) |

Set the location for an endpoint type.

Parameters
:   | dir | Direction of the endpoints to change location for. |
    | --- | --- |
    | location | The location to be set. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#abae9cf025f32ce80b660ebd7f95241b2)bt\_pacs\_set\_supported\_contexts()

| int bt\_pacs\_set\_supported\_contexts | ( | enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) | *dir*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) | *contexts* ) |

Set the supported contexts for an endpoint type.

Parameters
:   | dir | Direction of the endpoints to change available contexts for. |
    | --- | --- |
    | contexts | The contexts to be set. |

Returns
:   0 in case of success or negative value in case of error.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [pacs.h](pacs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
