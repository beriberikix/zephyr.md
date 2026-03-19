---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__bt__pacs.html
original_path: doxygen/html/group__bt__pacs.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Published Audio Capabilities Service (PACS)

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

Published Audio Capabilities Service (PACS).
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [bt\_pacs\_cap](structbt__pacs__cap.md) |
|  | Published Audio Capability structure. [More...](structbt__pacs__cap.md#details) |
| struct | [bt\_pacs\_register\_param](structbt__pacs__register__param.md) |
|  | Structure for registering PACS. [More...](structbt__pacs__register__param.md#details) |

| Typedefs | |
| --- | --- |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [bt\_pacs\_cap\_foreach\_func\_t](#ga452591f80b6be5d79609b25ade2154a9)) (const struct [bt\_pacs\_cap](structbt__pacs__cap.md) \*cap, void \*user\_data) |
|  | Published Audio Capability iterator callback. |

| Functions | |
| --- | --- |
| void | [bt\_pacs\_cap\_foreach](#ga31e2c7e9a4b5b6a291b96832c1218a49) (enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir, [bt\_pacs\_cap\_foreach\_func\_t](#ga452591f80b6be5d79609b25ade2154a9) func, void \*user\_data) |
|  | Published Audio Capability iterator. |
| int | [bt\_pacs\_register](#gac77a3dd5015058145b51db5fef2c9485) (const struct [bt\_pacs\_register\_param](structbt__pacs__register__param.md) \*param) |
|  | Register the Published Audio Capability Service instance. |
| int | [bt\_pacs\_unregister](#gac23d3c4e850394194871e8daaa44545b) (void) |
|  | Unregister the Published Audio Capability Service instance. |
| int | [bt\_pacs\_cap\_register](#ga251b36d4f5775eea1f69873709f847cc) (enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir, struct [bt\_pacs\_cap](structbt__pacs__cap.md) \*cap) |
|  | Register Published Audio Capability. |
| int | [bt\_pacs\_cap\_unregister](#ga4f6015eba63ffc7a9377afe54a290da1) (enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir, struct [bt\_pacs\_cap](structbt__pacs__cap.md) \*cap) |
|  | Unregister Published Audio Capability. |
| int | [bt\_pacs\_set\_location](#gaff290fd59bb05012abcf405dbdc72884) (enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir, enum [bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8) location) |
|  | Set the location for an endpoint type. |
| int | [bt\_pacs\_set\_available\_contexts](#ga29a1ec26c1e5e82e02eac39e1088332c) (enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir, enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) contexts) |
|  | Set the available contexts for an endpoint type. |
| enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) | [bt\_pacs\_get\_available\_contexts](#ga437d824d0a944b6c30db492dbe28514f) (enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir) |
|  | Get the available contexts for an endpoint type. |
| int | [bt\_pacs\_conn\_set\_available\_contexts\_for\_conn](#ga12f283d2daf72302a01cefb4a4a8fc70) (struct bt\_conn \*conn, enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir, enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) \*contexts) |
|  | Set the available contexts for a given connection. |
| enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) | [bt\_pacs\_get\_available\_contexts\_for\_conn](#ga7b28aa42525344445b20bb90a19441aa) (struct bt\_conn \*conn, enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir) |
|  | Get the available contexts for a given connection. |
| int | [bt\_pacs\_set\_supported\_contexts](#gabae9cf025f32ce80b660ebd7f95241b2) (enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir, enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) contexts) |
|  | Set the supported contexts for an endpoint type. |

## Detailed Description

Published Audio Capabilities Service (PACS).

Since
:   3.0

Version
:   0.8.0

The Published Audio Capabilities Service (PACS) is used to expose capabilities to remote devices.

## Typedef Documentation

## [◆ ](#ga452591f80b6be5d79609b25ade2154a9)bt\_pacs\_cap\_foreach\_func\_t

| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* bt\_pacs\_cap\_foreach\_func\_t) (const struct [bt\_pacs\_cap](structbt__pacs__cap.md) \*cap, void \*user\_data) |
| --- |

`#include <[pacs.h](pacs_8h.md)>`

Published Audio Capability iterator callback.

Parameters
:   | cap | Capability found. |
    | --- | --- |
    | user\_data | Data given. |

Returns
:   true to continue to the next capability
:   false to stop the iteration

## Function Documentation

## [◆ ](#ga31e2c7e9a4b5b6a291b96832c1218a49)bt\_pacs\_cap\_foreach()

| void bt\_pacs\_cap\_foreach | ( | enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) | *dir*, |
| --- | --- | --- | --- |
|  |  | [bt\_pacs\_cap\_foreach\_func\_t](#ga452591f80b6be5d79609b25ade2154a9) | *func*, |
|  |  | void \* | *user\_data* ) |

`#include <[pacs.h](pacs_8h.md)>`

Published Audio Capability iterator.

Iterate capabilities with endpoint direction specified.

Parameters
:   | dir | Direction of the endpoint to look capability for. |
    | --- | --- |
    | func | Callback function. |
    | user\_data | Data to pass to the callback. |

## [◆ ](#ga251b36d4f5775eea1f69873709f847cc)bt\_pacs\_cap\_register()

| int bt\_pacs\_cap\_register | ( | enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) | *dir*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_pacs\_cap](structbt__pacs__cap.md) \* | *cap* ) |

`#include <[pacs.h](pacs_8h.md)>`

Register Published Audio Capability.

Register Audio Local Capability.

Parameters
:   | dir | Direction of the endpoint to register capability for. |
    | --- | --- |
    | cap | Capability structure. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga4f6015eba63ffc7a9377afe54a290da1)bt\_pacs\_cap\_unregister()

| int bt\_pacs\_cap\_unregister | ( | enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) | *dir*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_pacs\_cap](structbt__pacs__cap.md) \* | *cap* ) |

`#include <[pacs.h](pacs_8h.md)>`

Unregister Published Audio Capability.

Unregister Audio Local Capability.

Parameters
:   | dir | Direction of the endpoint to unregister capability for. |
    | --- | --- |
    | cap | Capability structure. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga12f283d2daf72302a01cefb4a4a8fc70)bt\_pacs\_conn\_set\_available\_contexts\_for\_conn()

| int bt\_pacs\_conn\_set\_available\_contexts\_for\_conn | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) | *dir*, |
|  |  | enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) \* | *contexts* ) |

`#include <[pacs.h](pacs_8h.md)>`

Set the available contexts for a given connection.

This function sets the available contexts value for a given `conn` connection object. If the `contexts` parameter is NULL the available contexts value is reset to default. The default value of the available contexts is set using [bt\_pacs\_set\_available\_contexts](#ga29a1ec26c1e5e82e02eac39e1088332c) function. The Available Context Value is reset to default on ACL disconnection.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | dir | Direction of the endpoints to change available contexts for. |
    | contexts | The contexts to be set or NULL to reset to default. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga437d824d0a944b6c30db492dbe28514f)bt\_pacs\_get\_available\_contexts()

| enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) bt\_pacs\_get\_available\_contexts | ( | enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) | *dir* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pacs.h](pacs_8h.md)>`

Get the available contexts for an endpoint type.

Parameters
:   | dir | Direction of the endpoints to get contexts for. |
    | --- | --- |

Returns
:   Bitmask of available contexts.

## [◆ ](#ga7b28aa42525344445b20bb90a19441aa)bt\_pacs\_get\_available\_contexts\_for\_conn()

| enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) bt\_pacs\_get\_available\_contexts\_for\_conn | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) | *dir* ) |

`#include <[pacs.h](pacs_8h.md)>`

Get the available contexts for a given connection.

This server function returns the available contexts value for a given `conn` connection object. The value returned is the one set with [bt\_pacs\_conn\_set\_available\_contexts\_for\_conn](#ga12f283d2daf72302a01cefb4a4a8fc70) function or the default value set with [bt\_pacs\_set\_available\_contexts](#ga29a1ec26c1e5e82e02eac39e1088332c) function.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | dir | Direction of the endpoints to get contexts for. |

Returns
:   Bitmask of available contexts.

Return values
:   | [BT\_AUDIO\_CONTEXT\_TYPE\_PROHIBITED](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a3cfcfa76adc5effdc1aa95d75e5da37a "Prohibited.") | if `conn` or `dir` are invalid |
    | --- | --- |

## [◆ ](#gac77a3dd5015058145b51db5fef2c9485)bt\_pacs\_register()

| int bt\_pacs\_register | ( | const struct [bt\_pacs\_register\_param](structbt__pacs__register__param.md) \* | *param* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pacs.h](pacs_8h.md)>`

Register the Published Audio Capability Service instance.

Parameters
:   | param | PACS register parameters. |
    | --- | --- |

Return values
:   | 0 | Success |
    | --- | --- |
    | -EINVAL | `param` is NULL or bad combination of values in `param` |
    | -EALREADY | Already registered |
    | -ENOEXEC | Request was rejected by GATT |

## [◆ ](#ga29a1ec26c1e5e82e02eac39e1088332c)bt\_pacs\_set\_available\_contexts()

| int bt\_pacs\_set\_available\_contexts | ( | enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) | *dir*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) | *contexts* ) |

`#include <[pacs.h](pacs_8h.md)>`

Set the available contexts for an endpoint type.

Parameters
:   | dir | Direction of the endpoints to change available contexts for. |
    | --- | --- |
    | contexts | The contexts to be set. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gaff290fd59bb05012abcf405dbdc72884)bt\_pacs\_set\_location()

| int bt\_pacs\_set\_location | ( | enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) | *dir*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8) | *location* ) |

`#include <[pacs.h](pacs_8h.md)>`

Set the location for an endpoint type.

Parameters
:   | dir | Direction of the endpoints to change location for. |
    | --- | --- |
    | location | The location to be set. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gabae9cf025f32ce80b660ebd7f95241b2)bt\_pacs\_set\_supported\_contexts()

| int bt\_pacs\_set\_supported\_contexts | ( | enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) | *dir*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) | *contexts* ) |

`#include <[pacs.h](pacs_8h.md)>`

Set the supported contexts for an endpoint type.

Parameters
:   | dir | Direction of the endpoints to change available contexts for. |
    | --- | --- |
    | contexts | The contexts to be set. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gac23d3c4e850394194871e8daaa44545b)bt\_pacs\_unregister()

| int bt\_pacs\_unregister | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pacs.h](pacs_8h.md)>`

Unregister the Published Audio Capability Service instance.

Returns
:   0 in case of success or negative value in case of error.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
