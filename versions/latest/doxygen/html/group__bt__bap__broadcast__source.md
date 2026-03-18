---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__bt__bap__broadcast__source.html
original_path: doxygen/html/group__bt__bap__broadcast__source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

BAP Broadcast Source APIs

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Basic Audio Profile](group__bt__bap.md) | [Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Basic Audio Profile](group__bt__bap.md) » [BAP Broadcast APIs](group__bt__bap__broadcast.md)

BAP Broadcast Source APIs.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [bt\_bap\_broadcast\_source\_stream\_param](structbt__bap__broadcast__source__stream__param.md) |
|  | Broadcast Source stream parameters. [More...](structbt__bap__broadcast__source__stream__param.md#details) |
| struct | [bt\_bap\_broadcast\_source\_subgroup\_param](structbt__bap__broadcast__source__subgroup__param.md) |
|  | Broadcast Source subgroup parameters. [More...](structbt__bap__broadcast__source__subgroup__param.md#details) |
| struct | [bt\_bap\_broadcast\_source\_param](structbt__bap__broadcast__source__param.md) |
|  | Broadcast Source create parameters. [More...](structbt__bap__broadcast__source__param.md#details) |

| Functions | |
| --- | --- |
| int | [bt\_bap\_broadcast\_source\_create](#gacdebfc435eebd47cf9cd05099a5f78e0) (struct [bt\_bap\_broadcast\_source\_param](structbt__bap__broadcast__source__param.md) \*param, struct bt\_bap\_broadcast\_source \*\*source) |
|  | Create audio broadcast source. |
| int | [bt\_bap\_broadcast\_source\_reconfig](#gabecaa9db7be5cb03ed997ba478878d40) (struct bt\_bap\_broadcast\_source \*source, struct [bt\_bap\_broadcast\_source\_param](structbt__bap__broadcast__source__param.md) \*param) |
|  | Reconfigure audio broadcast source. |
| int | [bt\_bap\_broadcast\_source\_update\_metadata](#gaff2cfdadbff3ebe1e2efb660dee56f02) (struct bt\_bap\_broadcast\_source \*source, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) meta[], [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) meta\_len) |
|  | Modify the metadata of an audio broadcast source. |
| int | [bt\_bap\_broadcast\_source\_start](#gac4640f5207599d51c1a63ff47f3c1d5a) (struct bt\_bap\_broadcast\_source \*source, struct bt\_le\_ext\_adv \*adv) |
|  | Start audio broadcast source. |
| int | [bt\_bap\_broadcast\_source\_stop](#ga36a885581eec5cab8b3f652db19b9aba) (struct bt\_bap\_broadcast\_source \*source) |
|  | Stop audio broadcast source. |
| int | [bt\_bap\_broadcast\_source\_delete](#ga12e0a4856115a8eb297fe2d1fc130155) (struct bt\_bap\_broadcast\_source \*source) |
|  | Delete audio broadcast source. |
| int | [bt\_bap\_broadcast\_source\_get\_id](#ga118bc35af0b1db024e7aada5da65b796) (struct bt\_bap\_broadcast\_source \*source, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*const broadcast\_id) |
|  | Get the broadcast ID of a broadcast source. |
| int | [bt\_bap\_broadcast\_source\_get\_base](#gafe07e4c6962858500fcf66415a173be8) (struct bt\_bap\_broadcast\_source \*source, struct [net\_buf\_simple](structnet__buf__simple.md) \*base\_buf) |
|  | Get the Broadcast Audio Stream Endpoint of a broadcast source. |

## Detailed Description

BAP Broadcast Source APIs.

## Function Documentation

## [◆ ](#gacdebfc435eebd47cf9cd05099a5f78e0)bt\_bap\_broadcast\_source\_create()

| int bt\_bap\_broadcast\_source\_create | ( | struct [bt\_bap\_broadcast\_source\_param](structbt__bap__broadcast__source__param.md) \* | *param*, |
| --- | --- | --- | --- |
|  |  | struct bt\_bap\_broadcast\_source \*\* | *source* ) |

`#include <[bap.h](bap_8h.md)>`

Create audio broadcast source.

Create a new audio broadcast source with one or more audio streams.

The broadcast source will be visible for scanners once this has been called, and the device will advertise audio announcements.

No audio data can be sent until [bt\_bap\_broadcast\_source\_start()](#gac4640f5207599d51c1a63ff47f3c1d5a) has been called and no audio information (BIGInfo) will be visible to scanners (see [bt\_le\_per\_adv\_sync\_cb](structbt__le__per__adv__sync__cb.md "bt_le_per_adv_sync_cb")).

Parameters
:   | [in] | param | Pointer to parameters used to create the broadcast source. |
    | --- | --- | --- |
    | [out] | source | Pointer to the broadcast source created |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#ga12e0a4856115a8eb297fe2d1fc130155)bt\_bap\_broadcast\_source\_delete()

| int bt\_bap\_broadcast\_source\_delete | ( | struct bt\_bap\_broadcast\_source \* | *source* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bap.h](bap_8h.md)>`

Delete audio broadcast source.

Delete an audio broadcast source. The broadcast source will stop advertising entirely, and the source can no longer be used.

Parameters
:   | source | Pointer to the broadcast source |
    | --- | --- |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#gafe07e4c6962858500fcf66415a173be8)bt\_bap\_broadcast\_source\_get\_base()

| int bt\_bap\_broadcast\_source\_get\_base | ( | struct bt\_bap\_broadcast\_source \* | *source*, |
| --- | --- | --- | --- |
|  |  | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *base\_buf* ) |

`#include <[bap.h](bap_8h.md)>`

Get the Broadcast Audio Stream Endpoint of a broadcast source.

This will encode the BASE of a broadcast source into a buffer, that can be used for advertisement. The encoded BASE will thus be encoded as little-endian. The BASE shall be put into the periodic advertising data (see [bt\_le\_per\_adv\_set\_data()](group__bt__gap.md#gafd0e7ccca93a8347a4ca6cca88e77899 "Set or update the periodic advertising data.")).

See table 3.15 in the Basic Audio Profile v1.0.1 for the structure.

Parameters
:   | source | Pointer to the broadcast source. |
    | --- | --- |
    | base\_buf | Pointer to a buffer where the BASE will be inserted. |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#ga118bc35af0b1db024e7aada5da65b796)bt\_bap\_broadcast\_source\_get\_id()

| int bt\_bap\_broadcast\_source\_get\_id | ( | struct bt\_bap\_broadcast\_source \* | *source*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*const | *broadcast\_id* ) |

`#include <[bap.h](bap_8h.md)>`

Get the broadcast ID of a broadcast source.

This will return the 3-octet broadcast ID that should be advertised in the extended advertising data with [BT\_UUID\_BROADCAST\_AUDIO\_VAL](group__bt__uuid.md#ga0c67f9e1a5fef34fd1fddc539e20119b "BT_UUID_BROADCAST_AUDIO_VAL") as [BT\_DATA\_SVC\_DATA16](group__bt__gap__defines.md#ga76990dda919688b369decaf9d3606b32 "BT_DATA_SVC_DATA16").

See table 3.14 in the Basic Audio Profile v1.0.1 for the structure.

Parameters
:   | [in] | source | Pointer to the broadcast source. |
    | --- | --- | --- |
    | [out] | broadcast\_id | Pointer to the 3-octet broadcast ID. |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#gabecaa9db7be5cb03ed997ba478878d40)bt\_bap\_broadcast\_source\_reconfig()

| int bt\_bap\_broadcast\_source\_reconfig | ( | struct bt\_bap\_broadcast\_source \* | *source*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_bap\_broadcast\_source\_param](structbt__bap__broadcast__source__param.md) \* | *param* ) |

`#include <[bap.h](bap_8h.md)>`

Reconfigure audio broadcast source.

Reconfigure an audio broadcast source with a new codec and codec quality of service parameters. This can only be done when the source is stopped.

Since this may modify the Broadcast Audio Source Endpoint (BASE), [bt\_bap\_broadcast\_source\_get\_base()](#gafe07e4c6962858500fcf66415a173be8) should be called after this to get the new BASE information.

If the `param.params_count` is smaller than the number of subgroups that have been created in the Broadcast Source, only the first `param.params_count` subgroups are updated. If a stream exist in a subgroup not part of `param`, then that stream is left as is (i.e. it is not removed; the only way to remove a stream from a Broadcast Source is to recreate the Broadcast Source).

Parameters
:   | source | Pointer to the broadcast source |
    | --- | --- |
    | param | Pointer to parameters used to reconfigure the broadcast source. |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#gac4640f5207599d51c1a63ff47f3c1d5a)bt\_bap\_broadcast\_source\_start()

| int bt\_bap\_broadcast\_source\_start | ( | struct bt\_bap\_broadcast\_source \* | *source*, |
| --- | --- | --- | --- |
|  |  | struct bt\_le\_ext\_adv \* | *adv* ) |

`#include <[bap.h](bap_8h.md)>`

Start audio broadcast source.

Start an audio broadcast source with one or more audio streams. The broadcast source will start advertising BIGInfo, and audio data can be streamed.

Parameters
:   | source | Pointer to the broadcast source |
    | --- | --- |
    | adv | Pointer to an extended advertising set with periodic advertising configured. |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#ga36a885581eec5cab8b3f652db19b9aba)bt\_bap\_broadcast\_source\_stop()

| int bt\_bap\_broadcast\_source\_stop | ( | struct bt\_bap\_broadcast\_source \* | *source* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bap.h](bap_8h.md)>`

Stop audio broadcast source.

Stop an audio broadcast source. The broadcast source will stop advertising BIGInfo, and audio data can no longer be streamed.

Parameters
:   | source | Pointer to the broadcast source |
    | --- | --- |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#gaff2cfdadbff3ebe1e2efb660dee56f02)bt\_bap\_broadcast\_source\_update\_metadata()

| int bt\_bap\_broadcast\_source\_update\_metadata | ( | struct bt\_bap\_broadcast\_source \* | *source*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *meta*[], |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *meta\_len* ) |

`#include <[bap.h](bap_8h.md)>`

Modify the metadata of an audio broadcast source.

Modify the metadata an audio broadcast source. This can only be done when the source is started. To update the metadata in the stopped state, use [bt\_bap\_broadcast\_source\_reconfig()](#gabecaa9db7be5cb03ed997ba478878d40).

Parameters
:   | source | Pointer to the broadcast source. |
    | --- | --- |
    | meta | Metadata. |
    | meta\_len | Length of metadata. |

Returns
:   Zero on success or (negative) error code otherwise.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
