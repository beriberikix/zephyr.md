---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/group__bt__bap__unicast__client.html
original_path: doxygen/html/group__bt__bap__unicast__client.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

BAP Unicast Client APIs

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Basic Audio Profile](group__bt__bap.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_bap\_unicast\_group\_stream\_param](structbt__bap__unicast__group__stream__param.md) |
|  | Parameter struct for each stream in the unicast group. [More...](structbt__bap__unicast__group__stream__param.md#details) |
| struct | [bt\_bap\_unicast\_group\_stream\_pair\_param](structbt__bap__unicast__group__stream__pair__param.md) |
|  | Parameter struct for the unicast group functions. [More...](structbt__bap__unicast__group__stream__pair__param.md#details) |
| struct | [bt\_bap\_unicast\_group\_param](structbt__bap__unicast__group__param.md) |
|  | Parameters for the creating unicast groups with [bt\_bap\_unicast\_group\_create()](#gaafd53b5f45d998b44e94a1b58e93ba21). [More...](structbt__bap__unicast__group__param.md#details) |
| struct | [bt\_bap\_unicast\_client\_cb](structbt__bap__unicast__client__cb.md) |
|  | Unicast Client callback structure. [More...](structbt__bap__unicast__client__cb.md#details) |

| Typedefs | |
| --- | --- |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [bt\_bap\_unicast\_group\_foreach\_stream\_func\_t](#gaf0e5a38208e90176292e745933b5e29e)) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, void \*user\_data) |
|  | Callback function for [bt\_bap\_unicast\_group\_foreach\_stream()](#gad608ee07c8a50abf586a3bc31921f032). |

| Functions | |
| --- | --- |
| int | [bt\_bap\_unicast\_group\_create](#gaafd53b5f45d998b44e94a1b58e93ba21) (struct [bt\_bap\_unicast\_group\_param](structbt__bap__unicast__group__param.md) \*param, struct bt\_bap\_unicast\_group \*\*unicast\_group) |
|  | Create unicast group. |
| int | [bt\_bap\_unicast\_group\_reconfig](#gacd684504c8127ff4f8d038cc06718e5e) (struct bt\_bap\_unicast\_group \*unicast\_group, const struct [bt\_bap\_unicast\_group\_param](structbt__bap__unicast__group__param.md) \*param) |
|  | Reconfigure unicast group. |
| int | [bt\_bap\_unicast\_group\_add\_streams](#ga9cc792cd1eaaa79d56f3df0e2341cbf6) (struct bt\_bap\_unicast\_group \*unicast\_group, struct [bt\_bap\_unicast\_group\_stream\_pair\_param](structbt__bap__unicast__group__stream__pair__param.md) params[], [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) num\_param) |
|  | Add streams to a unicast group as a unicast client. |
| int | [bt\_bap\_unicast\_group\_delete](#ga34dbdce6133f8366df453ec937fb47d2) (struct bt\_bap\_unicast\_group \*unicast\_group) |
|  | Delete audio unicast group. |
| int | [bt\_bap\_unicast\_group\_foreach\_stream](#gad608ee07c8a50abf586a3bc31921f032) (struct bt\_bap\_unicast\_group \*unicast\_group, [bt\_bap\_unicast\_group\_foreach\_stream\_func\_t](#gaf0e5a38208e90176292e745933b5e29e) func, void \*user\_data) |
|  | Iterate through all streams in a unicast group. |
| int | [bt\_bap\_unicast\_client\_register\_cb](#gade70f04ae1a828b43b3b44fa8933f674) (struct [bt\_bap\_unicast\_client\_cb](structbt__bap__unicast__client__cb.md) \*cb) |
|  | Register unicast client callbacks. |
| int | [bt\_bap\_unicast\_client\_discover](#gacef9c88f66762e8de19303d20dafa0bb) (struct bt\_conn \*conn, enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) dir) |
|  | Discover remote capabilities and endpoints. |

## Detailed Description

## Typedef Documentation

## [◆ ](#gaf0e5a38208e90176292e745933b5e29e)bt\_bap\_unicast\_group\_foreach\_stream\_func\_t

| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* bt\_bap\_unicast\_group\_foreach\_stream\_func\_t) (struct [bt\_bap\_stream](structbt__bap__stream.md) \*stream, void \*user\_data) |
| --- |

`#include <[zephyr/bluetooth/audio/bap.h](bap_8h.md)>`

Callback function for [bt\_bap\_unicast\_group\_foreach\_stream()](#gad608ee07c8a50abf586a3bc31921f032).

Parameters
:   | stream | The audio stream |
    | --- | --- |
    | user\_data | User data |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | Stop iterating. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | Continue iterating. |

## Function Documentation

## [◆ ](#gacef9c88f66762e8de19303d20dafa0bb)bt\_bap\_unicast\_client\_discover()

| int bt\_bap\_unicast\_client\_discover | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) | *dir* ) |

`#include <[zephyr/bluetooth/audio/bap.h](bap_8h.md)>`

Discover remote capabilities and endpoints.

This procedure is used by a client to discover remote capabilities and endpoints and notifies via params callback.

Parameters
:   | conn | Connection object |
    | --- | --- |
    | dir | The type of remote endpoints and capabilities to discover. |

## [◆ ](#gade70f04ae1a828b43b3b44fa8933f674)bt\_bap\_unicast\_client\_register\_cb()

| int bt\_bap\_unicast\_client\_register\_cb | ( | struct [bt\_bap\_unicast\_client\_cb](structbt__bap__unicast__client__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/audio/bap.h](bap_8h.md)>`

Register unicast client callbacks.

Only one callback structure can be registered, and attempting to registering more than one will result in an error.

Parameters
:   | cb | Unicast client callback structure. |
    | --- | --- |

Return values
:   | 0 | Success |
    | --- | --- |
    | -EINVAL | `cb` is NULL. |
    | -EEXIST | `cb` is already registered. |

## [◆ ](#ga9cc792cd1eaaa79d56f3df0e2341cbf6)bt\_bap\_unicast\_group\_add\_streams()

| int bt\_bap\_unicast\_group\_add\_streams | ( | struct bt\_bap\_unicast\_group \* | *unicast\_group*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_bap\_unicast\_group\_stream\_pair\_param](structbt__bap__unicast__group__stream__pair__param.md) | *params*[], |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *num\_param* ) |

`#include <[zephyr/bluetooth/audio/bap.h](bap_8h.md)>`

Add streams to a unicast group as a unicast client.

This function can be used to add additional streams to a bt\_bap\_unicast\_group.

This can be called at any time before any of the streams in the group has been started (see [bt\_bap\_stream\_ops.started()](structbt__bap__stream__ops.md#a7f595e37d40b94510bf09c1f82b479f3 "Stream started callback.")). This can also be called after the streams have been stopped (see [bt\_bap\_stream\_ops.stopped()](structbt__bap__stream__ops.md#ab50ea295069a2cd1ab6f4353052262f5 "Stream stopped callback.")).

Once a stream has been added to a unicast group, it cannot be removed. To remove a stream from a group, the group must be deleted with [bt\_bap\_unicast\_group\_delete()](#ga34dbdce6133f8366df453ec937fb47d2), but this will require all streams in the group to be released first.

Parameters
:   | unicast\_group | Pointer to the unicast group |
    | --- | --- |
    | params | Array of stream parameters with streams being added to the group. |
    | num\_param | Number of parameters in `params`. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gaafd53b5f45d998b44e94a1b58e93ba21)bt\_bap\_unicast\_group\_create()

| int bt\_bap\_unicast\_group\_create | ( | struct [bt\_bap\_unicast\_group\_param](structbt__bap__unicast__group__param.md) \* | *param*, |
| --- | --- | --- | --- |
|  |  | struct bt\_bap\_unicast\_group \*\* | *unicast\_group* ) |

`#include <[zephyr/bluetooth/audio/bap.h](bap_8h.md)>`

Create unicast group.

Create a new audio unicast group with one or more audio streams as a unicast client. All streams shall share the same framing. All streams in the same direction shall share the same interval and latency (see [bt\_bap\_qos\_cfg](structbt__bap__qos__cfg.md "bt_bap_qos_cfg")).

Parameters
:   | [in] | param | The unicast group create parameters. |
    | --- | --- | --- |
    | [out] | unicast\_group | Pointer to the unicast group created. |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#ga34dbdce6133f8366df453ec937fb47d2)bt\_bap\_unicast\_group\_delete()

| int bt\_bap\_unicast\_group\_delete | ( | struct bt\_bap\_unicast\_group \* | *unicast\_group* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/bluetooth/audio/bap.h](bap_8h.md)>`

Delete audio unicast group.

Delete a audio unicast group as a client. All streams in the group shall be in the idle or configured state.

Parameters
:   | unicast\_group | Pointer to the unicast group to delete |
    | --- | --- |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#gad608ee07c8a50abf586a3bc31921f032)bt\_bap\_unicast\_group\_foreach\_stream()

| int bt\_bap\_unicast\_group\_foreach\_stream | ( | struct bt\_bap\_unicast\_group \* | *unicast\_group*, |
| --- | --- | --- | --- |
|  |  | [bt\_bap\_unicast\_group\_foreach\_stream\_func\_t](#gaf0e5a38208e90176292e745933b5e29e) | *func*, |
|  |  | void \* | *user\_data* ) |

`#include <[zephyr/bluetooth/audio/bap.h](bap_8h.md)>`

Iterate through all streams in a unicast group.

Parameters
:   | unicast\_group | The unicast group |
    | --- | --- |
    | func | The callback function |
    | user\_data | User specified data that sent to the callback function |

Return values
:   | 0 | Success (even if no streams exists in the group). |
    | --- | --- |
    | -ECANCELED | Iteration was stopped by the callback function before complete. |
    | -EINVAL | `unicast_group` or `func` were NULL. |

## [◆ ](#gacd684504c8127ff4f8d038cc06718e5e)bt\_bap\_unicast\_group\_reconfig()

| int bt\_bap\_unicast\_group\_reconfig | ( | struct bt\_bap\_unicast\_group \* | *unicast\_group*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_bap\_unicast\_group\_param](structbt__bap__unicast__group__param.md) \* | *param* ) |

`#include <[zephyr/bluetooth/audio/bap.h](bap_8h.md)>`

Reconfigure unicast group.

Reconfigure a unicast group with one or more audio streams as a unicast client. All streams shall share the same framing. All streams in the same direction shall share the same interval and latency (see [bt\_bap\_qos\_cfg](structbt__bap__qos__cfg.md "bt_bap_qos_cfg")). All streams in `param` shall already belong to `unicast_group`. Use [bt\_bap\_unicast\_group\_add\_streams()](#ga9cc792cd1eaaa79d56f3df0e2341cbf6) to add additional streams.

Parameters
:   | unicast\_group | Pointer to the unicast group created. |
    | --- | --- |
    | param | The unicast group reconfigure parameters. |

Returns
:   Zero on success or (negative) error code otherwise.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
