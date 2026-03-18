---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__bt__bap__unicast__server.html
original_path: doxygen/html/group__bt__bap__unicast__server.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

BAP Unicast Server APIs

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Basic Audio Profile](group__bt__bap.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_bap\_unicast\_server\_cb](structbt__bap__unicast__server__cb.md) |
|  | Unicast Server callback structure. [More...](structbt__bap__unicast__server__cb.md#details) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [bt\_bap\_ep\_func\_t](#gab571883c431267fc9a9f892de3c864f1)) (struct bt\_bap\_ep \*ep, void \*user\_data) |
|  | The callback function called for each endpoint. |

| Functions | |
| --- | --- |
| int | [bt\_bap\_unicast\_server\_register\_cb](#ga7669133936bc13f7ab38817db9ce69c0) (const struct [bt\_bap\_unicast\_server\_cb](structbt__bap__unicast__server__cb.md) \*cb) |
|  | Register unicast server callbacks. |
| int | [bt\_bap\_unicast\_server\_unregister\_cb](#gadf984f12bdeadcfc814dc2fc770cb7bf) (const struct [bt\_bap\_unicast\_server\_cb](structbt__bap__unicast__server__cb.md) \*cb) |
|  | Unregister unicast server callbacks. |
| void | [bt\_bap\_unicast\_server\_foreach\_ep](#ga4614a504d47cf732b09d4f22302d3239) (struct bt\_conn \*conn, [bt\_bap\_ep\_func\_t](#gab571883c431267fc9a9f892de3c864f1) func, void \*user\_data) |
|  | Iterate through all endpoints of the given connection. |
| int | [bt\_bap\_unicast\_server\_config\_ase](#gaf0f06f2536d1e108691fba87b234a7f4) (struct bt\_conn \*conn, struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, const struct [bt\_audio\_codec\_qos\_pref](structbt__audio__codec__qos__pref.md) \*qos\_pref) |
|  | Initialize and configure a new ASE. |

## Detailed Description

## Typedef Documentation

## [◆ ](#gab571883c431267fc9a9f892de3c864f1)bt\_bap\_ep\_func\_t

| typedef void(\* bt\_bap\_ep\_func\_t) (struct bt\_bap\_ep \*ep, void \*user\_data) |
| --- |

`#include <[bap.h](bap_8h.md)>`

The callback function called for each endpoint.

Parameters
:   | ep | The structure object with endpoint info. |
    | --- | --- |
    | user\_data | Data to pass to the function. |

## Function Documentation

## [◆ ](#gaf0f06f2536d1e108691fba87b234a7f4)bt\_bap\_unicast\_server\_config\_ase()

| int bt\_bap\_unicast\_server\_config\_ase | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_bap\_stream](structbt__bap__stream.md) \* | *stream*, |
|  |  | struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \* | *codec\_cfg*, |
|  |  | const struct [bt\_audio\_codec\_qos\_pref](structbt__audio__codec__qos__pref.md) \* | *qos\_pref* ) |

`#include <[bap.h](bap_8h.md)>`

Initialize and configure a new ASE.

Parameters
:   | conn | Connection object |
    | --- | --- |
    | stream | Configured stream object to be attached to the ASE |
    | codec\_cfg | Codec configuration |
    | qos\_pref | Audio Stream Quality of Service Preference |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga4614a504d47cf732b09d4f22302d3239)bt\_bap\_unicast\_server\_foreach\_ep()

| void bt\_bap\_unicast\_server\_foreach\_ep | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | [bt\_bap\_ep\_func\_t](#gab571883c431267fc9a9f892de3c864f1) | *func*, |
|  |  | void \* | *user\_data* ) |

`#include <[bap.h](bap_8h.md)>`

Iterate through all endpoints of the given connection.

Parameters
:   | conn | Connection object |
    | --- | --- |
    | func | Function to call for each endpoint. |
    | user\_data | Data to pass to the callback function. |

## [◆ ](#ga7669133936bc13f7ab38817db9ce69c0)bt\_bap\_unicast\_server\_register\_cb()

| int bt\_bap\_unicast\_server\_register\_cb | ( | const struct [bt\_bap\_unicast\_server\_cb](structbt__bap__unicast__server__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bap.h](bap_8h.md)>`

Register unicast server callbacks.

Only one callback structure can be registered, and attempting to registering more than one will result in an error.

Parameters
:   | cb | Unicast server callback structure. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gadf984f12bdeadcfc814dc2fc770cb7bf)bt\_bap\_unicast\_server\_unregister\_cb()

| int bt\_bap\_unicast\_server\_unregister\_cb | ( | const struct [bt\_bap\_unicast\_server\_cb](structbt__bap__unicast__server__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bap.h](bap_8h.md)>`

Unregister unicast server callbacks.

May only unregister a callback structure that has previously been registered by [bt\_bap\_unicast\_server\_register\_cb()](#ga7669133936bc13f7ab38817db9ce69c0).

Parameters
:   | cb | Unicast server callback structure. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
