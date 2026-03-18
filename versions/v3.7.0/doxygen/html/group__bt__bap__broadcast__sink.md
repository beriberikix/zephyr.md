---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__bt__bap__broadcast__sink.html
original_path: doxygen/html/group__bt__bap__broadcast__sink.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

BAP Broadcast Sink APIs

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Basic Audio Profile](group__bt__bap.md) | [Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Basic Audio Profile](group__bt__bap.md) » [BAP Broadcast APIs](group__bt__bap__broadcast.md)

BAP Broadcast Sink APIs.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [bt\_bap\_broadcast\_sink\_cb](structbt__bap__broadcast__sink__cb.md) |
|  | Broadcast Audio Sink callback structure. [More...](structbt__bap__broadcast__sink__cb.md#details) |

| Functions | |
| --- | --- |
| int | [bt\_bap\_broadcast\_sink\_register\_cb](#ga1b83ead634d990e954f233d0208c5a85) (struct [bt\_bap\_broadcast\_sink\_cb](structbt__bap__broadcast__sink__cb.md) \*cb) |
|  | Register Broadcast sink callbacks. |
| int | [bt\_bap\_broadcast\_sink\_create](#ga0637d1957db70ad39e0608ed07e75166) (struct bt\_le\_per\_adv\_sync \*pa\_sync, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) broadcast\_id, struct bt\_bap\_broadcast\_sink \*\*sink) |
|  | Create a Broadcast Sink from a periodic advertising sync. |
| int | [bt\_bap\_broadcast\_sink\_sync](#ga3485ef8527928209274ae0b5351b72b3) (struct bt\_bap\_broadcast\_sink \*sink, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) indexes\_bitfield, struct [bt\_bap\_stream](structbt__bap__stream.md) \*streams[], const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) broadcast\_code[16]) |
|  | Sync to a broadcaster's audio. |
| int | [bt\_bap\_broadcast\_sink\_stop](#ga1020b21bfb4195aeb5823197145b1fe9) (struct bt\_bap\_broadcast\_sink \*sink) |
|  | Stop audio broadcast sink. |
| int | [bt\_bap\_broadcast\_sink\_delete](#ga8b9d6cb409a3671654e053475ada3fda) (struct bt\_bap\_broadcast\_sink \*sink) |
|  | Release a broadcast sink. |

## Detailed Description

BAP Broadcast Sink APIs.

## Function Documentation

## [◆ ](#ga0637d1957db70ad39e0608ed07e75166)bt\_bap\_broadcast\_sink\_create()

| int bt\_bap\_broadcast\_sink\_create | ( | struct bt\_le\_per\_adv\_sync \* | *pa\_sync*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *broadcast\_id*, |
|  |  | struct bt\_bap\_broadcast\_sink \*\* | *sink* ) |

`#include <[bap.h](bap_8h.md)>`

Create a Broadcast Sink from a periodic advertising sync.

This should only be done after verifying that the periodic advertising sync is from a Broadcast Source.

The created Broadcast Sink will need to be supplied to [bt\_bap\_broadcast\_sink\_sync()](#ga3485ef8527928209274ae0b5351b72b3) in order to synchronize to the broadcast audio.

bt\_bap\_broadcast\_sink\_cb.pa\_synced() will be called with the Broadcast Sink object created if this is successful.

Parameters
:   |  | pa\_sync | Pointer to the periodic advertising sync object. |
    | --- | --- | --- |
    |  | broadcast\_id | 24-bit broadcast ID. |
    | [out] | sink | Pointer to the Broadcast Sink created. |

Returns
:   0 in case of success or errno value in case of error.

## [◆ ](#ga8b9d6cb409a3671654e053475ada3fda)bt\_bap\_broadcast\_sink\_delete()

| int bt\_bap\_broadcast\_sink\_delete | ( | struct bt\_bap\_broadcast\_sink \* | *sink* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bap.h](bap_8h.md)>`

Release a broadcast sink.

Once a broadcast sink has been allocated after the pa\_synced callback, it can be deleted using this function. If the sink has synchronized to any broadcast audio streams, these must first be stopped using bt\_bap\_stream\_stop.

Parameters
:   | sink | Pointer to the sink object to delete. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga1b83ead634d990e954f233d0208c5a85)bt\_bap\_broadcast\_sink\_register\_cb()

| int bt\_bap\_broadcast\_sink\_register\_cb | ( | struct [bt\_bap\_broadcast\_sink\_cb](structbt__bap__broadcast__sink__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bap.h](bap_8h.md)>`

Register Broadcast sink callbacks.

It is possible to register multiple struct of callbacks, but a single struct can only be registered once. Registering the same callback multiple times is undefined behavior and may break the stack.

Parameters
:   | cb | Broadcast sink callback structure. |
    | --- | --- |

Return values
:   | 0 | in case of success |
    | --- | --- |
    | -EINVAL | if `cb` is NULL |

## [◆ ](#ga1020b21bfb4195aeb5823197145b1fe9)bt\_bap\_broadcast\_sink\_stop()

| int bt\_bap\_broadcast\_sink\_stop | ( | struct bt\_bap\_broadcast\_sink \* | *sink* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bap.h](bap_8h.md)>`

Stop audio broadcast sink.

Stop an audio broadcast sink. The broadcast sink will stop receiving BIGInfo, and audio data can no longer be streamed.

Parameters
:   | sink | Pointer to the broadcast sink |
    | --- | --- |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#ga3485ef8527928209274ae0b5351b72b3)bt\_bap\_broadcast\_sink\_sync()

| int bt\_bap\_broadcast\_sink\_sync | ( | struct bt\_bap\_broadcast\_sink \* | *sink*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *indexes\_bitfield*, |
|  |  | struct [bt\_bap\_stream](structbt__bap__stream.md) \* | *streams*[], |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *broadcast\_code*[16] ) |

`#include <[bap.h](bap_8h.md)>`

Sync to a broadcaster's audio.

Parameters
:   | sink | Pointer to the sink object from the base\_recv callback. |
    | --- | --- |
    | indexes\_bitfield | Bitfield of the BIS index to sync to. To sync to e.g. BIS index 1 and 2, this should have the value of [BIT(1)](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c "Unsigned integer with bit position n set (signed in assembly language).") | [BIT(2)](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c "Unsigned integer with bit position n set (signed in assembly language)."). |
    | streams | Stream object pointers to be used for the receiver. If multiple BIS indexes shall be synchronized, multiple streams shall be provided. |
    | broadcast\_code | The 16-octet broadcast code. Shall be supplied if the broadcast is encrypted (see [bt\_bap\_broadcast\_sink\_cb::syncable](structbt__bap__broadcast__sink__cb.md#a23390a63acbcf831a177a550d1012047 "bt_bap_broadcast_sink_cb::syncable")). If the value is a string or a the value is less than 16 octets, the remaining octets shall be 0. |

Example: The string "Broadcast Code" shall be [42 72 6F 61 64 63 61 73 74 20 43 6F 64 65 00 00]

Returns
:   0 in case of success or negative value in case of error.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
