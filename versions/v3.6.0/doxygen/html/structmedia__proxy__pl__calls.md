---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structmedia__proxy__pl__calls.html
original_path: doxygen/html/structmedia__proxy__pl__calls.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

media\_proxy\_pl\_calls Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Media Proxy](group__bt__media__proxy.md)

Available calls in a player, that the media proxy can call.
[More...](#details)

`#include <[media_proxy.h](media__proxy_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const char \*(\* | [get\_player\_name](#a2946f7572e12ffabc5f6ba2f562d52cf) )(void) |
|  | Read Media Player Name. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)(\* | [get\_icon\_id](#ad1215725454c6b76dcdc197a275c03cf) )(void) |
|  | Read Icon Object ID. |
| const char \*(\* | [get\_icon\_url](#a319dd309f94c45292613ab9caa0e399b) )(void) |
|  | Read Icon URL. |
| const char \*(\* | [get\_track\_title](#af9fc0af545c8c28f8f4dbf8c6afb4acf) )(void) |
|  | Read Track Title. |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)(\* | [get\_track\_duration](#a1b852ccc45a6ee1174b9d58df3b599b6) )(void) |
|  | Read Track Duration. |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)(\* | [get\_track\_position](#a11ea1cf984a7d11ac7e61405df84ee06) )(void) |
|  | Read Track Position. |
| void(\* | [set\_track\_position](#a001ae07161b8a6c7dfc9c2e471f229e5) )([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) position) |
|  | Set Track Position. |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)(\* | [get\_playback\_speed](#ae1006d5c684e12e1e1c927f71aa93930) )(void) |
|  | Get Playback Speed. |
| void(\* | [set\_playback\_speed](#a7535dad9be2f4b83c8a7c55fccc8a7af) )([int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) speed) |
|  | Set Playback Speed. |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)(\* | [get\_seeking\_speed](#aebf24b582cf33786f2dc17765d858a15) )(void) |
|  | Get Seeking Speed. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)(\* | [get\_track\_segments\_id](#a86a71b788b54a4e7c966f162fcab6433) )(void) |
|  | Read Current Track Segments Object ID. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)(\* | [get\_current\_track\_id](#a7f19bd75114835d151ff5b26733ed450) )(void) |
|  | Read Current Track Object ID. |
| void(\* | [set\_current\_track\_id](#a422cec33063313a9aab86baf0bd65ef1) )([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Set Current Track Object ID. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)(\* | [get\_next\_track\_id](#af939a96fbcfe474dfcdcfb353ae0aac5) )(void) |
|  | Read Next Track Object ID. |
| void(\* | [set\_next\_track\_id](#acbf8dc9dcc8fbaba44d436310c92f3a9) )([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Set Next Track Object ID. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)(\* | [get\_parent\_group\_id](#a1409764199d47d0c27d07e13c8fa8f68) )(void) |
|  | Read Parent Group Object ID. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)(\* | [get\_current\_group\_id](#a98b02d4689cd5e279f43094f3ca09339) )(void) |
|  | Read Current Group Object ID. |
| void(\* | [set\_current\_group\_id](#a5049e21965e7fd08aaeafcbedf76809c) )([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Set Current Group Object ID. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)(\* | [get\_playing\_order](#a98989105d01265de4b268b623a26df2e) )(void) |
|  | Read Playing Order. |
| void(\* | [set\_playing\_order](#ad6fad92957146aeaf1bec0e56606da72) )([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) order) |
|  | Set Playing Order. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)(\* | [get\_playing\_orders\_supported](#a9b733c3187cc032ef6644a16ffd3f7c9) )(void) |
|  | Read Playing Orders Supported. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)(\* | [get\_media\_state](#a6a339aa7ee564acacffd2637eeb8e7ea) )(void) |
|  | Read Media State. |
| void(\* | [send\_command](#abae1ff89136b93ce4dee5dbe12e6791d) )(const struct [mpl\_cmd](structmpl__cmd.md) \*command) |
|  | Send Command. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* | [get\_commands\_supported](#ae0a4457fcc35d32541f2557698d5aa83) )(void) |
|  | Read Commands Supported. |
| void(\* | [send\_search](#a416ca20a05a66f4ce28635159173f064) )(const struct [mpl\_search](structmpl__search.md) \*search) |
|  | Set Search. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)(\* | [get\_search\_results\_id](#adf4003ba8ef1a5c38b75876f864564c5) )(void) |
|  | Read Search Results Object ID. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)(\* | [get\_content\_ctrl\_id](#a64bc23cc61e69b1b6c4050f76a9bc674) )(void) |
|  | Read Content Control ID. |

## Detailed Description

Available calls in a player, that the media proxy can call.

Given by a player when registering.

## Field Documentation

## [◆ ](#ae0a4457fcc35d32541f2557698d5aa83)get\_commands\_supported

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* media\_proxy\_pl\_calls::get\_commands\_supported) (void) |
| --- |

Read Commands Supported.

Read a bitmap containing the media player's supported command opcodes. See the MEDIA\_PROXY\_OP\_SUP\_\* defines.

Returns
:   The media player's supported command opcodes

## [◆ ](#a64bc23cc61e69b1b6c4050f76a9bc674)get\_content\_ctrl\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)(\* media\_proxy\_pl\_calls::get\_content\_ctrl\_id) (void) |
| --- |

Read Content Control ID.

The content control ID identifies a content control service on a device, and links it to the corresponding audio stream.

Returns
:   The content control ID for the media player

## [◆ ](#a98b02d4689cd5e279f43094f3ca09339)get\_current\_group\_id

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)(\* media\_proxy\_pl\_calls::get\_current\_group\_id) (void) |
| --- |

Read Current Group Object ID.

Get an ID (48 bit) that can be used to retrieve the Current Track Object from an Object Transfer Service

See the Media Control Service spec v1.0 sections 3.14 and 4.4 for a description of the Current Group Object.

Returns
:   The Current Group Object ID

## [◆ ](#a7f19bd75114835d151ff5b26733ed450)get\_current\_track\_id

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)(\* media\_proxy\_pl\_calls::get\_current\_track\_id) (void) |
| --- |

Read Current Track Object ID.

Get an ID (48 bit) that can be used to retrieve the Current Track Object from an Object Transfer Service

See the Media Control Service spec v1.0 sections 3.11 and 4.3 for a description of the Current Track Object.

Returns
:   The Current Track Object ID

## [◆ ](#ad1215725454c6b76dcdc197a275c03cf)get\_icon\_id

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)(\* media\_proxy\_pl\_calls::get\_icon\_id) (void) |
| --- |

Read Icon Object ID.

Get an ID (48 bit) that can be used to retrieve the Icon Object from an Object Transfer Service

See the Media Control Service spec v1.0 sections 3.2 and 4.1 for a description of the Icon Object.

Returns
:   The Icon Object ID

## [◆ ](#a319dd309f94c45292613ab9caa0e399b)get\_icon\_url

| const char \*(\* media\_proxy\_pl\_calls::get\_icon\_url) (void) |
| --- |

Read Icon URL.

Get a URL to the media player's icon.

Returns
:   The URL of the Icon

## [◆ ](#a6a339aa7ee564acacffd2637eeb8e7ea)get\_media\_state

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)(\* media\_proxy\_pl\_calls::get\_media\_state) (void) |
| --- |

Read Media State.

Read the media player's state See the MEDIA\_PROXY\_MEDIA\_STATE\_\* defines.

Returns
:   The media player's state

## [◆ ](#af939a96fbcfe474dfcdcfb353ae0aac5)get\_next\_track\_id

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)(\* media\_proxy\_pl\_calls::get\_next\_track\_id) (void) |
| --- |

Read Next Track Object ID.

Get an ID (48 bit) that can be used to retrieve the Next Track Object from an Object Transfer Service

Returns
:   The Next Track Object ID

## [◆ ](#a1409764199d47d0c27d07e13c8fa8f68)get\_parent\_group\_id

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)(\* media\_proxy\_pl\_calls::get\_parent\_group\_id) (void) |
| --- |

Read Parent Group Object ID.

Get an ID (48 bit) that can be used to retrieve the Parent Track Object from an Object Transfer Service

The parent group is the parent of the current group.

See the Media Control Service spec v1.0 sections 3.14 and 4.4 for a description of the Current Track Object.

Returns
:   The Current Group Object ID

## [◆ ](#ae1006d5c684e12e1e1c927f71aa93930)get\_playback\_speed

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)(\* media\_proxy\_pl\_calls::get\_playback\_speed) (void) |
| --- |

Get Playback Speed.

The playback speed parameter is related to the actual playback speed as follows: actual playback speed = 2^(speed\_parameter/64)

A speed parameter of 0 corresponds to unity speed playback (i.e. playback at "normal" speed). A speed parameter of -128 corresponds to playback at one fourth of normal speed, 127 corresponds to playback at almost four times the normal speed.

Returns
:   The playback speed parameter

## [◆ ](#a2946f7572e12ffabc5f6ba2f562d52cf)get\_player\_name

| const char \*(\* media\_proxy\_pl\_calls::get\_player\_name) (void) |
| --- |

Read Media Player Name.

Returns
:   The name of the media player

## [◆ ](#a98989105d01265de4b268b623a26df2e)get\_playing\_order

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)(\* media\_proxy\_pl\_calls::get\_playing\_order) (void) |
| --- |

Read Playing Order.

return The media player's current playing order

## [◆ ](#a9b733c3187cc032ef6644a16ffd3f7c9)get\_playing\_orders\_supported

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)(\* media\_proxy\_pl\_calls::get\_playing\_orders\_supported) (void) |
| --- |

Read Playing Orders Supported.

Read a bitmap containing the media player's supported playing orders. See the MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_\* defines.

Returns
:   The media player's supported playing orders

## [◆ ](#adf4003ba8ef1a5c38b75876f864564c5)get\_search\_results\_id

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)(\* media\_proxy\_pl\_calls::get\_search\_results\_id) (void) |
| --- |

Read Search Results Object ID.

Get an ID (48 bit) that can be used to retrieve the Search Results Object from an Object Transfer Service

The search results object is a group object. The search results object only exists if a successful search operation has been done.

Returns
:   The Search Results Object ID

## [◆ ](#aebf24b582cf33786f2dc17765d858a15)get\_seeking\_speed

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)(\* media\_proxy\_pl\_calls::get\_seeking\_speed) (void) |
| --- |

Get Seeking Speed.

The seeking speed gives the speed with which the player is seeking. It is a factor, relative to real-time playback speed - a factor four means seeking happens at four times the real-time playback speed. Positive values are for forward seeking, negative values for backwards seeking.

The seeking speed is not settable - a non-zero seeking speed is the result of "fast rewind" of "fast forward" commands.

Returns
:   The seeking speed factor

## [◆ ](#a1b852ccc45a6ee1174b9d58df3b599b6)get\_track\_duration

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)(\* media\_proxy\_pl\_calls::get\_track\_duration) (void) |
| --- |

Read Track Duration.

The duration of a track is measured in hundredths of a second.

Returns
:   The duration of the current track

## [◆ ](#a11ea1cf984a7d11ac7e61405df84ee06)get\_track\_position

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)(\* media\_proxy\_pl\_calls::get\_track\_position) (void) |
| --- |

Read Track Position.

The position of the player (the playing position) is measured in hundredths of a second from the beginning of the track

Returns
:   The position of the player in the current track

## [◆ ](#a86a71b788b54a4e7c966f162fcab6433)get\_track\_segments\_id

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)(\* media\_proxy\_pl\_calls::get\_track\_segments\_id) (void) |
| --- |

Read Current Track Segments Object ID.

Get an ID (48 bit) that can be used to retrieve the Current Track Segments Object from an Object Transfer Service

See the Media Control Service spec v1.0 sections 3.10 and 4.2 for a description of the Track Segments Object.

Returns
:   Current The Track Segments Object ID

## [◆ ](#af9fc0af545c8c28f8f4dbf8c6afb4acf)get\_track\_title

| const char \*(\* media\_proxy\_pl\_calls::get\_track\_title) (void) |
| --- |

Read Track Title.

Returns
:   The title of the current track

## [◆ ](#abae1ff89136b93ce4dee5dbe12e6791d)send\_command

| void(\* media\_proxy\_pl\_calls::send\_command) (const struct [mpl\_cmd](structmpl__cmd.md) \*command) |
| --- |

Send Command.

Send a command to the media player. For command opcodes (play, pause, ...) - see the MEDIA\_PROXY\_OP\_\* defines.

Parameters
:   | command | The command to send |
    | --- | --- |

## [◆ ](#a416ca20a05a66f4ce28635159173f064)send\_search

| void(\* media\_proxy\_pl\_calls::send\_search) (const struct [mpl\_search](structmpl__search.md) \*search) |
| --- |

Set Search.

Write a search to the media player. (For the formatting of a search, see the Media Control Service spec and the [mcs.h](mcs_8h.md) file.)

Parameters
:   | search | The search to write |
    | --- | --- |

## [◆ ](#a5049e21965e7fd08aaeafcbedf76809c)set\_current\_group\_id

| void(\* media\_proxy\_pl\_calls::set\_current\_group\_id) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
| --- |

Set Current Group Object ID.

Change the player's current group to the group given by the ID, and the current track to the first track in that group.

Parameters
:   | id | The ID of a group object |
    | --- | --- |

## [◆ ](#a422cec33063313a9aab86baf0bd65ef1)set\_current\_track\_id

| void(\* media\_proxy\_pl\_calls::set\_current\_track\_id) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
| --- |

Set Current Track Object ID.

Change the player's current track to the track given by the ID. (Behaves similarly to the goto track command.)

Parameters
:   | id | The ID of a track object |
    | --- | --- |

## [◆ ](#acbf8dc9dcc8fbaba44d436310c92f3a9)set\_next\_track\_id

| void(\* media\_proxy\_pl\_calls::set\_next\_track\_id) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
| --- |

Set Next Track Object ID.

Change the player's next track to the track given by the ID.

Parameters
:   | id | The ID of a track object |
    | --- | --- |

## [◆ ](#a7535dad9be2f4b83c8a7c55fccc8a7af)set\_playback\_speed

| void(\* media\_proxy\_pl\_calls::set\_playback\_speed) ([int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) speed) |
| --- |

Set Playback Speed.

See the [get\_playback\_speed()](#ae1006d5c684e12e1e1c927f71aa93930) function for an explanation of the playback speed parameter.

Note that the media player may not support all possible values of the playback speed parameter. If the value given is not supported, and is higher than the current value, the player should set the playback speed to the next higher supported value. (And correspondingly to the next lower supported value for given values lower than the current value.)

Parameters
:   | speed | The playback speed parameter to set |
    | --- | --- |

## [◆ ](#ad6fad92957146aeaf1bec0e56606da72)set\_playing\_order

| void(\* media\_proxy\_pl\_calls::set\_playing\_order) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) order) |
| --- |

Set Playing Order.

Set the media player's playing order. See the MEDIA\_PROXY\_PLAYING\_ORDER\_\* defines.

Parameters
:   | order | The playing order to set |
    | --- | --- |

## [◆ ](#a001ae07161b8a6c7dfc9c2e471f229e5)set\_track\_position

| void(\* media\_proxy\_pl\_calls::set\_track\_position) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) position) |
| --- |

Set Track Position.

Set the playing position of the media player in the current track. The position is given in in hundredths of a second, from the beginning of the track of the track for positive values, and (backwards) from the end of the track for negative values.

Parameters
:   | position | The player position to set |
    | --- | --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[media\_proxy.h](media__proxy_8h_source.md)

- [media\_proxy\_pl\_calls](structmedia__proxy__pl__calls.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
