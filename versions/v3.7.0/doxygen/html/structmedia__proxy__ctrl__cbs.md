---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structmedia__proxy__ctrl__cbs.html
original_path: doxygen/html/structmedia__proxy__ctrl__cbs.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

media\_proxy\_ctrl\_cbs Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Media Proxy](group__bt__media__proxy.md)

Callbacks to a controller, from the media proxy.
[More...](#details)

`#include <[media_proxy.h](media__proxy_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [local\_player\_instance](#af2cd0f93aadd451f1b358e2d2d6a0049) )(struct media\_player \*player, int err) |
|  | Media Player Instance callback. |
| void(\* | [player\_name\_recv](#a94b5ec6bc20299b722bd0e2cb28aed5e) )(struct media\_player \*player, int err, const char \*name) |
|  | Media Player Name receive callback. |
| void(\* | [icon\_id\_recv](#aaa7ba216e604be1c447a93231a0857d0) )(struct media\_player \*player, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Media Player Icon Object ID receive callback. |
| void(\* | [icon\_url\_recv](#a53c4809b7a10b9057f565411429d691b) )(struct media\_player \*player, int err, const char \*url) |
|  | Media Player Icon URL receive callback. |
| void(\* | [track\_changed\_recv](#ade71f132ef66c7bfd13b1b1f3200681d) )(struct media\_player \*player, int err) |
|  | Track changed receive callback. |
| void(\* | [track\_title\_recv](#ac1afc71ed04faa87e644d095ef14946f) )(struct media\_player \*player, int err, const char \*title) |
|  | Track Title receive callback. |
| void(\* | [track\_duration\_recv](#a85c0bfc83bb26c74b11b5cb8182ff1e0) )(struct media\_player \*player, int err, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) duration) |
|  | Track Duration receive callback. |
| void(\* | [track\_position\_recv](#a6aa029523978e02dc1c8c7ff798e2433) )(struct media\_player \*player, int err, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) position) |
|  | Track Position receive callback. |
| void(\* | [track\_position\_write](#a54f9f50e3b8f99b586a2c522a67da213) )(struct media\_player \*player, int err, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) position) |
|  | Track Position write callback. |
| void(\* | [playback\_speed\_recv](#a5eb1466e8ba100c9d3cb12f097328b9e) )(struct media\_player \*player, int err, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) speed) |
|  | Playback Speed receive callback. |
| void(\* | [playback\_speed\_write](#ad84d5caca4be208bd5e5d93f5c801ddf) )(struct media\_player \*player, int err, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) speed) |
|  | Playback Speed write callback. |
| void(\* | [seeking\_speed\_recv](#a2ba0e73f7e67c38f5abe555305753d0f) )(struct media\_player \*player, int err, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) speed) |
|  | Seeking Speed receive callback. |
| void(\* | [track\_segments\_id\_recv](#aa7e7f7724689844491a4885544fc450c) )(struct media\_player \*player, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Track Segments Object ID receive callback. |
| void(\* | [current\_track\_id\_recv](#aa3c2bd1734c6235eb2026915dbebc6c2) )(struct media\_player \*player, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Current Track Object ID receive callback. |
| void(\* | [current\_track\_id\_write](#a66f35a59821f53f4ed9aa7dea0e4d654) )(struct media\_player \*player, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Current Track Object ID write callback. |
| void(\* | [next\_track\_id\_recv](#a5692c0d142977b8ec7a4ffb765fd0687) )(struct media\_player \*player, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Next Track Object ID receive callback. |
| void(\* | [next\_track\_id\_write](#a08b6fe1079b759de1f5a9f7751a22f21) )(struct media\_player \*player, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Next Track Object ID write callback. |
| void(\* | [parent\_group\_id\_recv](#a3c2b39bc46f8b2a7155c14dd430add8e) )(struct media\_player \*player, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Parent Group Object ID receive callback. |
| void(\* | [current\_group\_id\_recv](#a858a8854259c8e7a09164b916fae309a) )(struct media\_player \*player, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Current Group Object ID receive callback. |
| void(\* | [current\_group\_id\_write](#ad1a65519a958aa27091a2ba41260db04) )(struct media\_player \*player, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Current Group Object ID write callback. |
| void(\* | [playing\_order\_recv](#a92a3b0e3254d6b26e0d18476dce3b01e) )(struct media\_player \*player, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) order) |
|  | Playing Order receive callback. |
| void(\* | [playing\_order\_write](#a67cf70c9b72a87b03009f1da0a8980f2) )(struct media\_player \*player, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) order) |
|  | Playing Order write callback. |
| void(\* | [playing\_orders\_supported\_recv](#a85182342b606c78127f2690ac1beab7d) )(struct media\_player \*player, int err, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) orders) |
|  | Playing Orders Supported receive callback. |
| void(\* | [media\_state\_recv](#ad4199644afcf356a565b884129ca0cf3) )(struct media\_player \*player, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Media State receive callback. |
| void(\* | [command\_send](#a89bb28499c989a9a2ad13d40dda6c6db) )(struct media\_player \*player, int err, const struct [mpl\_cmd](structmpl__cmd.md) \*[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)) |
|  | Command send callback. |
| void(\* | [command\_recv](#a90481b6563033a4520b85307e07e2e3a) )(struct media\_player \*player, int err, const struct [mpl\_cmd\_ntf](structmpl__cmd__ntf.md) \*result) |
|  | Command result receive callback. |
| void(\* | [commands\_supported\_recv](#a06fadb043fd0a795f872063b7950d414) )(struct media\_player \*player, int err, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) opcodes) |
|  | Commands supported receive callback. |
| void(\* | [search\_send](#aee4a556023d56c3a0d4c2036b3bc0799) )(struct media\_player \*player, int err, const struct [mpl\_search](structmpl__search.md) \*search) |
|  | Search send callback. |
| void(\* | [search\_recv](#a0678ad4950c6f526c78d2143e9b7c385) )(struct media\_player \*player, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) result\_code) |
|  | Search result code receive callback. |
| void(\* | [search\_results\_id\_recv](#af067e55ef7f676ad3c05f838160ed21e) )(struct media\_player \*player, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Search Results Object ID receive callback See also [media\_proxy\_ctrl\_get\_search\_results\_id()](group__bt__media__proxy.md#ga580a0c9fa47460be59f0571ee11a41b4 "Read Search Results Object ID."). |
| void(\* | [content\_ctrl\_id\_recv](#a08f3f55a5b56d1ede9141013fe456119) )(struct media\_player \*player, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ccid) |
|  | Content Control ID receive callback. |

## Detailed Description

Callbacks to a controller, from the media proxy.

Given by a controller when registering

## Field Documentation

## [◆ ](#a90481b6563033a4520b85307e07e2e3a)command\_recv

| void(\* media\_proxy\_ctrl\_cbs::command\_recv) (struct media\_player \*player, int err, const struct [mpl\_cmd\_ntf](structmpl__cmd__ntf.md) \*result) |
| --- |

Command result receive callback.

Called when a command result has been received See also [media\_proxy\_ctrl\_send\_command()](group__bt__media__proxy.md#ga590762e7272b99fb8ac50a7841424670 "Send Command.")

Parameters
:   | player | Media player instance pointer |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |
    | result | The result received |

## [◆ ](#a89bb28499c989a9a2ad13d40dda6c6db)command\_send

| void(\* media\_proxy\_ctrl\_cbs::command\_send) (struct media\_player \*player, int err, const struct [mpl\_cmd](structmpl__cmd.md) \*[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)) |
| --- |

Command send callback.

Called when a command has been sent See also [media\_proxy\_ctrl\_send\_command()](group__bt__media__proxy.md#ga590762e7272b99fb8ac50a7841424670 "Send Command.")

Parameters
:   | player | Media player instance pointer |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |
    | [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615 "Execute a display list command by co-processor engine.") | The command sent |

## [◆ ](#a06fadb043fd0a795f872063b7950d414)commands\_supported\_recv

| void(\* media\_proxy\_ctrl\_cbs::commands\_supported\_recv) (struct media\_player \*player, int err, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) opcodes) |
| --- |

Commands supported receive callback.

Called when the Commands Supported is read or changed See also [media\_proxy\_ctrl\_get\_commands\_supported()](group__bt__media__proxy.md#ga15804287093b20d4a1616380729b33c8 "Read Commands Supported.")

Parameters
:   | player | Media player instance pointer |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |
    | opcodes | The supported command opcodes (bitmap) |

## [◆ ](#a08f3f55a5b56d1ede9141013fe456119)content\_ctrl\_id\_recv

| void(\* media\_proxy\_ctrl\_cbs::content\_ctrl\_id\_recv) (struct media\_player \*player, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ccid) |
| --- |

Content Control ID receive callback.

Called when the Content Control ID is read See also [media\_proxy\_ctrl\_get\_content\_ctrl\_id()](group__bt__media__proxy.md#ga23488e77985a04216ec7c7fa785f09fc "Read Content Control ID.")

Parameters
:   | player | Media player instance pointer |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |
    | ccid | The content control ID |

## [◆ ](#a858a8854259c8e7a09164b916fae309a)current\_group\_id\_recv

| void(\* media\_proxy\_ctrl\_cbs::current\_group\_id\_recv) (struct media\_player \*player, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
| --- |

Current Group Object ID receive callback.

Called when the Current Group Object ID is read or changed See also [media\_proxy\_ctrl\_get\_current\_group\_id()](group__bt__media__proxy.md#ga2ae50a1988305b4247ff0af796b6d93e "Read Current Group Object ID.") and [media\_proxy\_ctrl\_set\_current\_group\_id()](group__bt__media__proxy.md#gae496885d0124f4e3fc2c0f203fcff118 "Set Current Group Object ID.")

Parameters
:   | player | Media player instance pointer |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |
    | id | The ID of the current group object in Object Transfer Service (48 bits) |

## [◆ ](#ad1a65519a958aa27091a2ba41260db04)current\_group\_id\_write

| void(\* media\_proxy\_ctrl\_cbs::current\_group\_id\_write) (struct media\_player \*player, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
| --- |

Current Group Object ID write callback.

Called when the Current Group Object ID is written See also [media\_proxy\_ctrl\_set\_current\_group\_id()](group__bt__media__proxy.md#gae496885d0124f4e3fc2c0f203fcff118 "Set Current Group Object ID.")

Parameters
:   | player | Media player instance pointer |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |
    | id | The ID (48 bits) attempted to write |

## [◆ ](#aa3c2bd1734c6235eb2026915dbebc6c2)current\_track\_id\_recv

| void(\* media\_proxy\_ctrl\_cbs::current\_track\_id\_recv) (struct media\_player \*player, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
| --- |

Current Track Object ID receive callback.

Called when the Current Track Object ID is read or changed See also [media\_proxy\_ctrl\_get\_current\_track\_id()](group__bt__media__proxy.md#gaebe7e3683041e28bef40df75cc991dea "Read Current Track Object ID.") and [media\_proxy\_ctrl\_set\_current\_track\_id()](group__bt__media__proxy.md#gaea6adacedaded10f7c2c0f91b7159f74 "Set Current Track Object ID.")

Parameters
:   | player | Media player instance pointer |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |
    | id | The ID of the current track object in Object Transfer Service (48 bits) |

## [◆ ](#a66f35a59821f53f4ed9aa7dea0e4d654)current\_track\_id\_write

| void(\* media\_proxy\_ctrl\_cbs::current\_track\_id\_write) (struct media\_player \*player, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
| --- |

Current Track Object ID write callback.

Called when the Current Track Object ID is written See also [media\_proxy\_ctrl\_set\_current\_track\_id()](group__bt__media__proxy.md#gaea6adacedaded10f7c2c0f91b7159f74 "Set Current Track Object ID.")

Parameters
:   | player | Media player instance pointer |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |
    | id | The ID (48 bits) attempted to write |

## [◆ ](#aaa7ba216e604be1c447a93231a0857d0)icon\_id\_recv

| void(\* media\_proxy\_ctrl\_cbs::icon\_id\_recv) (struct media\_player \*player, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
| --- |

Media Player Icon Object ID receive callback.

Called when the Media Player Icon Object ID is read See also [media\_proxy\_ctrl\_get\_icon\_id()](group__bt__media__proxy.md#ga5efccb39cdb97eed476e0c0bff461ec1 "Read Icon Object ID.")

Parameters
:   | player | Media player instance pointer |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |
    | id | The ID of the Icon object in the Object Transfer Service (48 bits) |

## [◆ ](#a53c4809b7a10b9057f565411429d691b)icon\_url\_recv

| void(\* media\_proxy\_ctrl\_cbs::icon\_url\_recv) (struct media\_player \*player, int err, const char \*url) |
| --- |

Media Player Icon URL receive callback.

Called when the Media Player Icon URL is read See also [media\_proxy\_ctrl\_get\_icon\_url()](group__bt__media__proxy.md#gab6df6fe71c8273eca855eb3be27290dd "Read Icon URL.")

Parameters
:   | player | Media player instance pointer |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |
    | url | The URL of the icon |

## [◆ ](#af2cd0f93aadd451f1b358e2d2d6a0049)local\_player\_instance

| void(\* media\_proxy\_ctrl\_cbs::local\_player\_instance) (struct media\_player \*player, int err) |
| --- |

Media Player Instance callback.

Called when the local Media Player instance is registered or read (TODO). Also called if the local player instance is already registered when the controller is registered. Provides the controller with the pointer to the local player instance.

Parameters
:   | player | Media player instance pointer |
    | --- | --- |
    | err | Error value. 0 on success, or errno on negative value. |

## [◆ ](#ad4199644afcf356a565b884129ca0cf3)media\_state\_recv

| void(\* media\_proxy\_ctrl\_cbs::media\_state\_recv) (struct media\_player \*player, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
| --- |

Media State receive callback.

Called when the Media State is read or changed See also [media\_proxy\_ctrl\_get\_media\_state()](group__bt__media__proxy.md#ga9433aaf24776c30557ea694795e75b3e "Read Media State.") and [media\_proxy\_ctrl\_send\_command()](group__bt__media__proxy.md#ga590762e7272b99fb8ac50a7841424670 "Send Command.")

Parameters
:   | player | Media player instance pointer |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |
    | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | The media player state |

## [◆ ](#a5692c0d142977b8ec7a4ffb765fd0687)next\_track\_id\_recv

| void(\* media\_proxy\_ctrl\_cbs::next\_track\_id\_recv) (struct media\_player \*player, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
| --- |

Next Track Object ID receive callback.

Called when the Next Track Object ID is read or changed See also [media\_proxy\_ctrl\_get\_next\_track\_id()](group__bt__media__proxy.md#gae32da32bd504061801730805729242e1 "Read Next Track Object ID.") and [media\_proxy\_ctrl\_set\_next\_track\_id()](group__bt__media__proxy.md#ga43b797717fb9b36b94a606dfabeb0fa7 "Set Next Track Object ID.")

Parameters
:   | player | Media player instance pointer |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |
    | id | The ID of the next track object in Object Transfer Service (48 bits) |

## [◆ ](#a08b6fe1079b759de1f5a9f7751a22f21)next\_track\_id\_write

| void(\* media\_proxy\_ctrl\_cbs::next\_track\_id\_write) (struct media\_player \*player, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
| --- |

Next Track Object ID write callback.

Called when the Next Track Object ID is written See also [media\_proxy\_ctrl\_set\_next\_track\_id()](group__bt__media__proxy.md#ga43b797717fb9b36b94a606dfabeb0fa7 "Set Next Track Object ID.")

Parameters
:   | player | Media player instance pointer |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |
    | id | The ID (48 bits) attempted to write |

## [◆ ](#a3c2b39bc46f8b2a7155c14dd430add8e)parent\_group\_id\_recv

| void(\* media\_proxy\_ctrl\_cbs::parent\_group\_id\_recv) (struct media\_player \*player, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
| --- |

Parent Group Object ID receive callback.

Called when the Parent Group Object ID is read or changed See also [media\_proxy\_ctrl\_get\_parent\_group\_id()](group__bt__media__proxy.md#ga12dc878be39814660900ba875e13e537 "Read Parent Group Object ID.")

Parameters
:   | player | Media player instance pointer |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |
    | id | The ID of the parent group object in Object Transfer Service (48 bits) |

## [◆ ](#a5eb1466e8ba100c9d3cb12f097328b9e)playback\_speed\_recv

| void(\* media\_proxy\_ctrl\_cbs::playback\_speed\_recv) (struct media\_player \*player, int err, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) speed) |
| --- |

Playback Speed receive callback.

Called when the Playback Speed is read or changed See also [media\_proxy\_ctrl\_get\_playback\_speed()](group__bt__media__proxy.md#ga2d64a23b3f881579a603a04baeb64088 "Get Playback Speed.") and [media\_proxy\_ctrl\_set\_playback\_speed()](group__bt__media__proxy.md#gabafbc857c3e6befe98e339acb58f17fb "Set Playback Speed.")

Parameters
:   | player | Media player instance pointer |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |
    | speed | The playback speed parameter |

## [◆ ](#ad84d5caca4be208bd5e5d93f5c801ddf)playback\_speed\_write

| void(\* media\_proxy\_ctrl\_cbs::playback\_speed\_write) (struct media\_player \*player, int err, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) speed) |
| --- |

Playback Speed write callback.

Called when the Playback Speed is written See also [media\_proxy\_ctrl\_set\_playback\_speed()](group__bt__media__proxy.md#gabafbc857c3e6befe98e339acb58f17fb "Set Playback Speed.")

Parameters
:   | player | Media player instance pointer |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |
    | speed | The playback speed parameter attempted to write |

## [◆ ](#a94b5ec6bc20299b722bd0e2cb28aed5e)player\_name\_recv

| void(\* media\_proxy\_ctrl\_cbs::player\_name\_recv) (struct media\_player \*player, int err, const char \*name) |
| --- |

Media Player Name receive callback.

Called when the Media Player Name is read or changed See also media\_proxy\_ctrl\_name\_get()

Parameters
:   | player | Media player instance pointer |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |
    | name | The name of the media player |

## [◆ ](#a92a3b0e3254d6b26e0d18476dce3b01e)playing\_order\_recv

| void(\* media\_proxy\_ctrl\_cbs::playing\_order\_recv) (struct media\_player \*player, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) order) |
| --- |

Playing Order receive callback.

Called when the Playing Order is read or changed See also [media\_proxy\_ctrl\_get\_playing\_order()](group__bt__media__proxy.md#ga2f93bcde2460c6638880f8e6631eb68e "Read Playing Order.") and [media\_proxy\_ctrl\_set\_playing\_order()](group__bt__media__proxy.md#gaa4040e97100f6e70527e6ad201309bbe "Set Playing Order.")

Parameters
:   | player | Media player instance pointer |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |
    | order | The playing order |

## [◆ ](#a67cf70c9b72a87b03009f1da0a8980f2)playing\_order\_write

| void(\* media\_proxy\_ctrl\_cbs::playing\_order\_write) (struct media\_player \*player, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) order) |
| --- |

Playing Order write callback.

Called when the Playing Order is written See also [media\_proxy\_ctrl\_set\_playing\_order()](group__bt__media__proxy.md#gaa4040e97100f6e70527e6ad201309bbe "Set Playing Order.")

Parameters
:   | player | Media player instance pointer |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |
    | order | The playing order attempted to write |

## [◆ ](#a85182342b606c78127f2690ac1beab7d)playing\_orders\_supported\_recv

| void(\* media\_proxy\_ctrl\_cbs::playing\_orders\_supported\_recv) (struct media\_player \*player, int err, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) orders) |
| --- |

Playing Orders Supported receive callback.

Called when the Playing Orders Supported is read See also [media\_proxy\_ctrl\_get\_playing\_orders\_supported()](group__bt__media__proxy.md#ga030899757b79251f1d5a1055f65fe989 "Read Playing Orders Supported.")

Parameters
:   | player | Media player instance pointer |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |
    | orders | The playing orders supported |

## [◆ ](#a0678ad4950c6f526c78d2143e9b7c385)search\_recv

| void(\* media\_proxy\_ctrl\_cbs::search\_recv) (struct media\_player \*player, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) result\_code) |
| --- |

Search result code receive callback.

Called when a search result code has been received See also [media\_proxy\_ctrl\_send\_search()](group__bt__media__proxy.md#ga052c3fabac4a44ee2802ddd4a6c5c9ac "Set Search.")

The search result code tells whether the search was successful or not. For a successful search, the actual results of the search (i.e. what was found as a result of the search)can be accessed using the Search Results Object ID. The Search Results Object ID has a separate callback - [search\_results\_id\_recv()](#af067e55ef7f676ad3c05f838160ed21e).

Parameters
:   | player | Media player instance pointer |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |
    | result\_code | Search result code |

## [◆ ](#af067e55ef7f676ad3c05f838160ed21e)search\_results\_id\_recv

| void(\* media\_proxy\_ctrl\_cbs::search\_results\_id\_recv) (struct media\_player \*player, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
| --- |

Search Results Object ID receive callback See also [media\_proxy\_ctrl\_get\_search\_results\_id()](group__bt__media__proxy.md#ga580a0c9fa47460be59f0571ee11a41b4 "Read Search Results Object ID.").

Called when the Search Results Object ID is read or changed

Parameters
:   | player | Media player instance pointer |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |
    | id | The ID of the search results object in Object Transfer Service (48 bits) |

## [◆ ](#aee4a556023d56c3a0d4c2036b3bc0799)search\_send

| void(\* media\_proxy\_ctrl\_cbs::search\_send) (struct media\_player \*player, int err, const struct [mpl\_search](structmpl__search.md) \*search) |
| --- |

Search send callback.

Called when a search has been sent See also [media\_proxy\_ctrl\_send\_search()](group__bt__media__proxy.md#ga052c3fabac4a44ee2802ddd4a6c5c9ac "Set Search.")

Parameters
:   | player | Media player instance pointer |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |
    | search | The search sent |

## [◆ ](#a2ba0e73f7e67c38f5abe555305753d0f)seeking\_speed\_recv

| void(\* media\_proxy\_ctrl\_cbs::seeking\_speed\_recv) (struct media\_player \*player, int err, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) speed) |
| --- |

Seeking Speed receive callback.

Called when the Seeking Speed is read or changed See also [media\_proxy\_ctrl\_get\_seeking\_speed()](group__bt__media__proxy.md#ga817ca4ab611e214493fbc918036def0f "Get Seeking Speed.")

Parameters
:   | player | Media player instance pointer |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |
    | speed | The seeking speed factor |

## [◆ ](#ade71f132ef66c7bfd13b1b1f3200681d)track\_changed\_recv

| void(\* media\_proxy\_ctrl\_cbs::track\_changed\_recv) (struct media\_player \*player, int err) |
| --- |

Track changed receive callback.

Called when the Current Track is changed

Parameters
:   | player | Media player instance pointer |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |

## [◆ ](#a85c0bfc83bb26c74b11b5cb8182ff1e0)track\_duration\_recv

| void(\* media\_proxy\_ctrl\_cbs::track\_duration\_recv) (struct media\_player \*player, int err, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) duration) |
| --- |

Track Duration receive callback.

Called when the Track Duration is read or changed See also [media\_proxy\_ctrl\_get\_track\_duration()](group__bt__media__proxy.md#ga488441418a8f2d358092019bbfe16788 "Read Track Duration.")

Parameters
:   | player | Media player instance pointer |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |
    | duration | The duration of the current track |

## [◆ ](#a6aa029523978e02dc1c8c7ff798e2433)track\_position\_recv

| void(\* media\_proxy\_ctrl\_cbs::track\_position\_recv) (struct media\_player \*player, int err, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) position) |
| --- |

Track Position receive callback.

Called when the Track Position is read or changed See also [media\_proxy\_ctrl\_get\_track\_position()](group__bt__media__proxy.md#gae0bb75feb49a68b495150c6fba2f21a7 "Read Track Position.") and [media\_proxy\_ctrl\_set\_track\_position()](group__bt__media__proxy.md#ga776bb5f16cf1f4f6cc3842aabd86b781 "Set Track Position.")

Parameters
:   | player | Media player instance pointer |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |
    | position | The player's position in the track |

## [◆ ](#a54f9f50e3b8f99b586a2c522a67da213)track\_position\_write

| void(\* media\_proxy\_ctrl\_cbs::track\_position\_write) (struct media\_player \*player, int err, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) position) |
| --- |

Track Position write callback.

Called when the Track Position is written See also [media\_proxy\_ctrl\_set\_track\_position()](group__bt__media__proxy.md#ga776bb5f16cf1f4f6cc3842aabd86b781 "Set Track Position.").

Parameters
:   | player | Media player instance pointer |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |
    | position | The position given attempted to write |

## [◆ ](#aa7e7f7724689844491a4885544fc450c)track\_segments\_id\_recv

| void(\* media\_proxy\_ctrl\_cbs::track\_segments\_id\_recv) (struct media\_player \*player, int err, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
| --- |

Track Segments Object ID receive callback.

Called when the Track Segments Object ID is read See also [media\_proxy\_ctrl\_get\_track\_segments\_id()](group__bt__media__proxy.md#ga1afcc097cb36c4f11141b82ce28e8126 "Read Current Track Segments Object ID.")

Parameters
:   | player | Media player instance pointer |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |
    | id | The ID of the track segments object in Object Transfer Service (48 bits) |

## [◆ ](#ac1afc71ed04faa87e644d095ef14946f)track\_title\_recv

| void(\* media\_proxy\_ctrl\_cbs::track\_title\_recv) (struct media\_player \*player, int err, const char \*title) |
| --- |

Track Title receive callback.

Called when the Track Title is read or changed See also [media\_proxy\_ctrl\_get\_track\_title()](group__bt__media__proxy.md#gabfbb49e79204130cb004f217af771b80 "Read Track Title.")

Parameters
:   | player | Media player instance pointer |
    | --- | --- |
    | err | Error value. 0 on success, GATT error on positive value or errno on negative value. |
    | title | The title of the current track |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[media\_proxy.h](media__proxy_8h_source.md)

- [media\_proxy\_ctrl\_cbs](structmedia__proxy__ctrl__cbs.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
