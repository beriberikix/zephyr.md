---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/media__proxy_8h.html
original_path: doxygen/html/media__proxy_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

media\_proxy.h File Reference

Bluetooth Media Proxy APIs.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[zephyr/bluetooth/bluetooth.h](bluetooth_2bluetooth_8h_source.md)>`  
`#include <[zephyr/sys/util_macro.h](util__macro_8h_source.md)>`  
`#include "[mcs.h](mcs_8h_source.md)"`

[Go to the source code of this file.](media__proxy_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [mpl\_cmd](structmpl__cmd.md) |
|  | Media player command. [More...](structmpl__cmd.md#details) |
| struct | [mpl\_cmd\_ntf](structmpl__cmd__ntf.md) |
|  | Media command notification. [More...](structmpl__cmd__ntf.md#details) |
| struct | [mpl\_sci](structmpl__sci.md) |
|  | Search control item. [More...](structmpl__sci.md#details) |
| struct | [mpl\_search](structmpl__search.md) |
|  | Search. [More...](structmpl__search.md#details) |
| struct | [media\_proxy\_ctrl\_cbs](structmedia__proxy__ctrl__cbs.md) |
|  | Callbacks to a controller, from the media proxy. [More...](structmedia__proxy__ctrl__cbs.md#details) |
| struct | [media\_proxy\_pl\_calls](structmedia__proxy__pl__calls.md) |
|  | Available calls in a player, that the media proxy can call. [More...](structmedia__proxy__pl__calls.md#details) |

| Macros | |
| --- | --- |
| #define | [MEDIA\_PROXY\_OPCODES\_SUPPORTED\_LEN](group__bt__media__proxy.md#ga22c2599cd62a263a01c06c9bd9fff054)   4 |
|  | Media player supported opcodes length. |
| Playback speed parameters | |
| All values from -128 to 127 allowed, only some defined | |
| #define | [MEDIA\_PROXY\_PLAYBACK\_SPEED\_MIN](group__bt__media__proxy.md#ga61732644eecad1442d5cedbda8f8cc08)   -128 |
|  | Minimum playback speed, resulting in 25 % speed. |
| #define | [MEDIA\_PROXY\_PLAYBACK\_SPEED\_QUARTER](group__bt__media__proxy.md#ga5462f8d5ce98cc33a131b2e7b5548c41)   -128 |
|  | Quarter playback speed, resulting in 25 % speed. |
| #define | [MEDIA\_PROXY\_PLAYBACK\_SPEED\_HALF](group__bt__media__proxy.md#ga4c765363c2a5b0d9800864859746ae33)   -64 |
|  | Half playback speed, resulting in 50 % speed. |
| #define | [MEDIA\_PROXY\_PLAYBACK\_SPEED\_UNITY](group__bt__media__proxy.md#ga6d8854bd54dcbb657f0ba545ec231368)   0 |
|  | Unity playback speed, resulting in 100 % speed. |
| #define | [MEDIA\_PROXY\_PLAYBACK\_SPEED\_DOUBLE](group__bt__media__proxy.md#gaa53d906340c0b2adb314945f5299464e)   64 |
|  | Double playback speed, resulting in 200 % speed. |
| #define | [MEDIA\_PROXY\_PLAYBACK\_SPEED\_MAX](group__bt__media__proxy.md#gaaccc9d75f96b5fe2de101b119a516d36)   127 |
|  | Max playback speed, resulting in 395.7 % speed (nearly 400 %). |
| Seeking speed factors | |
| The allowed values for seeking speed are the range -64 to -4 (endpoints included), the value 0, and the range 4 to 64 (endpoints included). | |
| #define | [MEDIA\_PROXY\_SEEKING\_SPEED\_FACTOR\_MAX](group__bt__media__proxy.md#gaa6aa7a6e98631152b4bd77b60c78d58a)   64 |
|  | Maximum seeking speed - Can be negated. |
| #define | [MEDIA\_PROXY\_SEEKING\_SPEED\_FACTOR\_MIN](group__bt__media__proxy.md#ga67c1069fa01425ad6cd8f36438b71826)   4 |
|  | Minimum seeking speed - Can be negated. |
| #define | [MEDIA\_PROXY\_SEEKING\_SPEED\_FACTOR\_ZERO](group__bt__media__proxy.md#ga58495e58bf84235efcee89289fc992c2)   0 |
|  | No seeking. |
| Playing orders | |
| #define | [MEDIA\_PROXY\_PLAYING\_ORDER\_SINGLE\_ONCE](group__bt__media__proxy.md#ga8e721b49c361d2395bd8eb740d43e282)   0x01 |
|  | A single track is played once; there is no next track. |
| #define | [MEDIA\_PROXY\_PLAYING\_ORDER\_SINGLE\_REPEAT](group__bt__media__proxy.md#gadf5f0c15cb88cd92f49db1b57dbd2c18)   0x02 |
|  | A single track is played repeatedly; the next track is the current track. |
| #define | [MEDIA\_PROXY\_PLAYING\_ORDER\_INORDER\_ONCE](group__bt__media__proxy.md#ga63055a150b93f06e076b97abb6f6f682)   0x03 |
|  | The tracks within a group are played once in track order. |
| #define | [MEDIA\_PROXY\_PLAYING\_ORDER\_INORDER\_REPEAT](group__bt__media__proxy.md#ga437068b9d90404cc68d41faaedfac9a8)   0x04 |
|  | The tracks within a group are played in track order repeatedly. |
| #define | [MEDIA\_PROXY\_PLAYING\_ORDER\_OLDEST\_ONCE](group__bt__media__proxy.md#ga48a33dd8fbb8a8ab162c18bc0e9b7531)   0x05 |
|  | The tracks within a group are played once only from the oldest first. |
| #define | [MEDIA\_PROXY\_PLAYING\_ORDER\_OLDEST\_REPEAT](group__bt__media__proxy.md#ga63a33c4e3267ab39ab5892fb5b0bbe89)   0x06 |
|  | The tracks within a group are played from the oldest first repeatedly. |
| #define | [MEDIA\_PROXY\_PLAYING\_ORDER\_NEWEST\_ONCE](group__bt__media__proxy.md#gac344111e2b043cdfbcb9ac272622b16f)   0x07 |
|  | The tracks within a group are played once only from the newest first. |
| #define | [MEDIA\_PROXY\_PLAYING\_ORDER\_NEWEST\_REPEAT](group__bt__media__proxy.md#gaf10b815dc579dc67b1f092e0a85c51d9)   0x08 |
|  | The tracks within a group are played from the newest first repeatedly. |
| #define | [MEDIA\_PROXY\_PLAYING\_ORDER\_SHUFFLE\_ONCE](group__bt__media__proxy.md#gae152374af5d567cf65d6d7b236b792a4)   0x09 |
|  | The tracks within a group are played in random order once. |
| #define | [MEDIA\_PROXY\_PLAYING\_ORDER\_SHUFFLE\_REPEAT](group__bt__media__proxy.md#ga45161ec08b67e4d3bd59efa45027f3aa)   0x0a |
|  | The tracks within a group are played in random order repeatedly. |
| Playing orders supported | |
| A bitmap, in the same order as the playing orders above.  Note that playing order 1 corresponds to bit 0, and so on. | |
| #define | [MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_SINGLE\_ONCE](group__bt__media__proxy.md#ga55b5a00ea9ec849e7c495463e5f1869d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | A single track is played once; there is no next track. |
| #define | [MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_SINGLE\_REPEAT](group__bt__media__proxy.md#ga465a82ace21a0e88356eccaf038f58e9)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | A single track is played repeatedly; the next track is the current track. |
| #define | [MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_INORDER\_ONCE](group__bt__media__proxy.md#ga8fee464b8e17fffc4361972df15062af)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | The tracks within a group are played once in track order. |
| #define | [MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_INORDER\_REPEAT](group__bt__media__proxy.md#ga7faeff14de245ea670ca447b0adc4820)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | The tracks within a group are played in track order repeatedly. |
| #define | [MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_OLDEST\_ONCE](group__bt__media__proxy.md#gae3d848fc0b9117fe9bc51327627ac635)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | The tracks within a group are played once only from the oldest first. |
| #define | [MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_OLDEST\_REPEAT](group__bt__media__proxy.md#ga7fa415d845dd1fefc8bdb74532878131)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | The tracks within a group are played from the oldest first repeatedly. |
| #define | [MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_NEWEST\_ONCE](group__bt__media__proxy.md#ga334f9e16ea7a52bfb6357ad619e3601b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | The tracks within a group are played once only from the newest first. |
| #define | [MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_NEWEST\_REPEAT](group__bt__media__proxy.md#gaaf5f08e2dd624e2bb1bd9b72ab4b2b33)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
|  | The tracks within a group are played from the newest first repeatedly. |
| #define | [MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_SHUFFLE\_ONCE](group__bt__media__proxy.md#ga3e998cda3e91f1c9fbb8496a748bcf12)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
|  | The tracks within a group are played in random order once. |
| #define | [MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_SHUFFLE\_REPEAT](group__bt__media__proxy.md#ga4f0689fe1fc0ac2b3f9b9ef4ed1afb8b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
|  | The tracks within a group are played in random order repeatedly. |
| Media player states | |
| #define | [MEDIA\_PROXY\_STATE\_INACTIVE](group__bt__media__proxy.md#gab8c465e0e63898e53c39171b89d668c9)   0x00 |
|  | The current track is invalid, and no track has been selected. |
| #define | [MEDIA\_PROXY\_STATE\_PLAYING](group__bt__media__proxy.md#ga1967c76b290f1d20515740cf7139f49c)   0x01 |
|  | The media player is playing the current track. |
| #define | [MEDIA\_PROXY\_STATE\_PAUSED](group__bt__media__proxy.md#ga85325d7ff75ec05275a875d7d5540a6c)   0x02 |
|  | The current track is paused. |
| #define | [MEDIA\_PROXY\_STATE\_SEEKING](group__bt__media__proxy.md#gaa207ee7666ab18c40e5b1d2a6ed7f034)   0x03 |
|  | The current track is fast forwarding or fast rewinding. |
| #define | [MEDIA\_PROXY\_STATE\_LAST](group__bt__media__proxy.md#gab0c8f3510109f18ef6445f035b27cbe9)   0x04 |
|  | Used internally as the last state value. |
| Media player command opcodes | |
| #define | [MEDIA\_PROXY\_OP\_PLAY](group__bt__media__proxy.md#gadd400bc6900abe1956d4de4efb212683)   0x01 |
|  | Start playing the current track. |
| #define | [MEDIA\_PROXY\_OP\_PAUSE](group__bt__media__proxy.md#ga69bcb42294e8cd1eb062bbe19399a3df)   0x02 |
|  | Pause playing the current track. |
| #define | [MEDIA\_PROXY\_OP\_FAST\_REWIND](group__bt__media__proxy.md#gabc2b497b95728325208e28db6d5cf4f8)   0x03 |
|  | Fast rewind the current track. |
| #define | [MEDIA\_PROXY\_OP\_FAST\_FORWARD](group__bt__media__proxy.md#gac0c0730bcf6592c5d2c61d21d09efb2b)   0x04 |
|  | Fast forward the current track. |
| #define | [MEDIA\_PROXY\_OP\_STOP](group__bt__media__proxy.md#gaf3707d44c7a3305ba896c0257b2109b3)   0x05 |
|  | Stop current activity and return to the paused state and set the current track position to the start of the current track. |
| #define | [MEDIA\_PROXY\_OP\_MOVE\_RELATIVE](group__bt__media__proxy.md#gaceb240f7f21074b6b7f9ed1e9d645cb0)   0x10 |
|  | Set a new current track position relative to the current track position. |
| #define | [MEDIA\_PROXY\_OP\_PREV\_SEGMENT](group__bt__media__proxy.md#ga7846fa5da200e0d921056b410e60677e)   0x20 |
|  | Set the current track position to the starting position of the previous segment of the current track. |
| #define | [MEDIA\_PROXY\_OP\_NEXT\_SEGMENT](group__bt__media__proxy.md#gada5e3114b2b00f4ea27adf884f49429e)   0x21 |
|  | Set the current track position to the starting position of the next segment of the current track. |
| #define | [MEDIA\_PROXY\_OP\_FIRST\_SEGMENT](group__bt__media__proxy.md#gac2e5c8e2cadd05092fa186f05ae74e57)   0x22 |
|  | Set the current track position to the starting position of the first segment of the current track. |
| #define | [MEDIA\_PROXY\_OP\_LAST\_SEGMENT](group__bt__media__proxy.md#ga3f317208b9d8495c498325a4d37d41ad)   0x23 |
|  | Set the current track position to the starting position of the last segment of the current track. |
| #define | [MEDIA\_PROXY\_OP\_GOTO\_SEGMENT](group__bt__media__proxy.md#gab3bbf7eb7c562bc6a5148c75eb99ada5)   0x24 |
|  | Set the current track position to the starting position of the nth segment of the current track. |
| #define | [MEDIA\_PROXY\_OP\_PREV\_TRACK](group__bt__media__proxy.md#ga1b7db568fc3153c29ed4e951d95bee8e)   0x30 |
|  | Set the current track to the previous track based on the playing order. |
| #define | [MEDIA\_PROXY\_OP\_NEXT\_TRACK](group__bt__media__proxy.md#gaae4cc32663f02bf96d1dcbbc8453e40b)   0x31 |
|  | Set the current track to the next track based on the playing order. |
| #define | [MEDIA\_PROXY\_OP\_FIRST\_TRACK](group__bt__media__proxy.md#ga5c272e2e9b24ce92a7df7373d1b002cc)   0x32 |
|  | Set the current track to the first track based on the playing order. |
| #define | [MEDIA\_PROXY\_OP\_LAST\_TRACK](group__bt__media__proxy.md#ga72614d9a2fa4c938f1c7055bc219c8bc)   0x33 |
|  | Set the current track to the last track based on the playing order. |
| #define | [MEDIA\_PROXY\_OP\_GOTO\_TRACK](group__bt__media__proxy.md#gaf2f100d41413b14c5dbd8f2641a13bb0)   0x34 |
|  | Set the current track to the nth track based on the playing order. |
| #define | [MEDIA\_PROXY\_OP\_PREV\_GROUP](group__bt__media__proxy.md#gae15386adcfe1c5ca56eac7d0292dffd0)   0x40 |
|  | Set the current group to the previous group in the sequence of groups. |
| #define | [MEDIA\_PROXY\_OP\_NEXT\_GROUP](group__bt__media__proxy.md#ga3cf10acf1ef8b7d3252eb37cb4e35f97)   0x41 |
|  | Set the current group to the next group in the sequence of groups. |
| #define | [MEDIA\_PROXY\_OP\_FIRST\_GROUP](group__bt__media__proxy.md#ga5eb0a22c257e370cd76d73f7fa9e342c)   0x42 |
|  | Set the current group to the first group in the sequence of groups. |
| #define | [MEDIA\_PROXY\_OP\_LAST\_GROUP](group__bt__media__proxy.md#gaa6ac8f8bf674c0ffec22bd061e9be3dc)   0x43 |
|  | Set the current group to the last group in the sequence of groups. |
| #define | [MEDIA\_PROXY\_OP\_GOTO\_GROUP](group__bt__media__proxy.md#ga139d2ced243a6ff47d8335583974a0da)   0x44 |
|  | Set the current group to the nth group in the sequence of groups. |
|  | |
| #define | [MEDIA\_PROXY\_OP\_SUP\_PLAY](group__bt__media__proxy.md#gafe30bb1287b9a44655d76364d4832eac)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Media player supported command opcodes. |
| #define | [MEDIA\_PROXY\_OP\_SUP\_PAUSE](group__bt__media__proxy.md#gaec37a692c28ca90c8053db9de2a6c44f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Support the Pause opcode. |
| #define | [MEDIA\_PROXY\_OP\_SUP\_FAST\_REWIND](group__bt__media__proxy.md#ga99952473bafd76f6ceaf141307510f28)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Support the Fast Rewind opcode. |
| #define | [MEDIA\_PROXY\_OP\_SUP\_FAST\_FORWARD](group__bt__media__proxy.md#ga05453105bc3d1579110e908b794e3ac5)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Support the Fast Forward opcode. |
| #define | [MEDIA\_PROXY\_OP\_SUP\_STOP](group__bt__media__proxy.md#ga060ff676a0b2f249a26aaf61147b68e8)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Support the Stop opcode. |
| #define | [MEDIA\_PROXY\_OP\_SUP\_MOVE\_RELATIVE](group__bt__media__proxy.md#ga03c393a29c68529e4dd9038e3947468b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | Support the Move Relative opcode. |
| #define | [MEDIA\_PROXY\_OP\_SUP\_PREV\_SEGMENT](group__bt__media__proxy.md#ga3d39700e21cbdf2906321c8899e0b626)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | Support the Previous Segment opcode. |
| #define | [MEDIA\_PROXY\_OP\_SUP\_NEXT\_SEGMENT](group__bt__media__proxy.md#ga26ae64ece06a1f6f8dd7eb2c9965a4b6)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
|  | Support the Next Segment opcode. |
| #define | [MEDIA\_PROXY\_OP\_SUP\_FIRST\_SEGMENT](group__bt__media__proxy.md#ga916ce95086dfeb127e124a8c5d530371)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
|  | Support the First Segment opcode. |
| #define | [MEDIA\_PROXY\_OP\_SUP\_LAST\_SEGMENT](group__bt__media__proxy.md#gaf193ea0b4a34e3981f2f45d3b9c228a2)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
|  | Support the Last Segment opcode. |
| #define | [MEDIA\_PROXY\_OP\_SUP\_GOTO\_SEGMENT](group__bt__media__proxy.md#ga7af591de387958f5c187ba8d0e834247)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
|  | Support the Goto Segment opcode. |
| #define | [MEDIA\_PROXY\_OP\_SUP\_PREV\_TRACK](group__bt__media__proxy.md#gafe8bab8f90281e5894e5f79f32449e63)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
|  | Support the Previous Track opcode. |
| #define | [MEDIA\_PROXY\_OP\_SUP\_NEXT\_TRACK](group__bt__media__proxy.md#gafc061bc953b0338aded4cef681f9e963)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
|  | Support the Next Track opcode. |
| #define | [MEDIA\_PROXY\_OP\_SUP\_FIRST\_TRACK](group__bt__media__proxy.md#ga6e1d53fedf09bd95bcf112495dcfd64f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
|  | Support the First Track opcode. |
| #define | [MEDIA\_PROXY\_OP\_SUP\_LAST\_TRACK](group__bt__media__proxy.md#gaf43188bb438b9a766d07cd2fa900e079)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
|  | Support the Last Track opcode. |
| #define | [MEDIA\_PROXY\_OP\_SUP\_GOTO\_TRACK](group__bt__media__proxy.md#gad2364a0ef8c54bd9fa3372edddae32b0)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15) |
|  | Support the Goto Track opcode. |
| #define | [MEDIA\_PROXY\_OP\_SUP\_PREV\_GROUP](group__bt__media__proxy.md#ga496060d673b48e045a5a2a57aa82bddc)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(16) |
|  | Support the Previous Group opcode. |
| #define | [MEDIA\_PROXY\_OP\_SUP\_NEXT\_GROUP](group__bt__media__proxy.md#ga324dae538f28e818eea79c83aaa0b22c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(17) |
|  | Support the Next Group opcode. |
| #define | [MEDIA\_PROXY\_OP\_SUP\_FIRST\_GROUP](group__bt__media__proxy.md#ga716af4c6eb702729ec4f9ff9ccc49b32)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(18) |
|  | Support the First Group opcode. |
| #define | [MEDIA\_PROXY\_OP\_SUP\_LAST\_GROUP](group__bt__media__proxy.md#gac944825600367a41e8213dfd9de569a3)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(19) |
|  | Support the Last Group opcode. |
| #define | [MEDIA\_PROXY\_OP\_SUP\_GOTO\_GROUP](group__bt__media__proxy.md#gaec8b6d2d684c81b9da9fee870e0258c2)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(20) |
|  | Support the Goto Group opcode. |
| Media player command result codes | |
| #define | [MEDIA\_PROXY\_CMD\_SUCCESS](group__bt__media__proxy.md#gaa56458b11f4cb78f1265ea8538774108)   0x01 |
|  | Action requested by the opcode write was completed successfully. |
| #define | [MEDIA\_PROXY\_CMD\_NOT\_SUPPORTED](group__bt__media__proxy.md#ga1637459cd6eaf9d4d63a04d1facc29b7)   0x02 |
|  | An invalid or unsupported opcode was used for the Media Control Point write. |
| #define | [MEDIA\_PROXY\_CMD\_PLAYER\_INACTIVE](group__bt__media__proxy.md#ga7d0595796a80348b570add74c6dfa14e)   0x03 |
|  | The Media Player State characteristic value is Inactive when the opcode is received or the result of the requested action of the opcode results in the Media Player State characteristic being set to Inactive. |
| #define | [MEDIA\_PROXY\_CMD\_CANNOT\_BE\_COMPLETED](group__bt__media__proxy.md#gaf2c68cb2ac32973b85594660d43688dd)   0x04 |
|  | The requested action of any Media Control Point write cannot be completed successfully because of a condition within the player. |
| Search operation type values | |
| #define | [MEDIA\_PROXY\_SEARCH\_TYPE\_TRACK\_NAME](group__bt__media__proxy.md#ga8be6fd8d9bb08836bea1c3f0d2e577ea)   0x01 |
|  | Search for Track Name. |
| #define | [MEDIA\_PROXY\_SEARCH\_TYPE\_ARTIST\_NAME](group__bt__media__proxy.md#gaf0dbc19f843a444076d8886b1a05709b)   0x02 |
|  | Search for Artist Name. |
| #define | [MEDIA\_PROXY\_SEARCH\_TYPE\_ALBUM\_NAME](group__bt__media__proxy.md#ga1f0fb19dea467e90afd670ed9af0c092)   0x03 |
|  | Search for Album Name. |
| #define | [MEDIA\_PROXY\_SEARCH\_TYPE\_GROUP\_NAME](group__bt__media__proxy.md#gaca10de7253c1cdcf5e0c6544de33c116)   0x04 |
|  | Search for Group Name. |
| #define | [MEDIA\_PROXY\_SEARCH\_TYPE\_EARLIEST\_YEAR](group__bt__media__proxy.md#ga28b1d7de2174e3714786cb369232f339)   0x05 |
|  | Search for Earliest Year. |
| #define | [MEDIA\_PROXY\_SEARCH\_TYPE\_LATEST\_YEAR](group__bt__media__proxy.md#ga01fb087af00bf492d19cc19adcaa9dea)   0x06 |
|  | Search for Latest Year. |
| #define | [MEDIA\_PROXY\_SEARCH\_TYPE\_GENRE](group__bt__media__proxy.md#ga55c3a003881a75ce964e23fc3b0cea8e)   0x07 |
|  | Search for Genre. |
| #define | [MEDIA\_PROXY\_SEARCH\_TYPE\_ONLY\_TRACKS](group__bt__media__proxy.md#gad758e14fbe978ffd95364a6fb27eab40)   0x08 |
|  | Search for Tracks only. |
| #define | [MEDIA\_PROXY\_SEARCH\_TYPE\_ONLY\_GROUPS](group__bt__media__proxy.md#ga25270f6c90daaace6a80f3255aaaf7fd)   0x09 |
|  | Search for Groups only. |
| Search notification result codes | |
| #define | [MEDIA\_PROXY\_SEARCH\_SUCCESS](group__bt__media__proxy.md#ga2627f632efab868adddeebb59243497c)   0x01 |
|  | Search request was accepted; search has started. |
| #define | [MEDIA\_PROXY\_SEARCH\_FAILURE](group__bt__media__proxy.md#gaf406225a87c697d784c5a429e89d2354)   0x02 |
|  | Search request was invalid; no search started. |
| Group object object types | |
| #define | [MEDIA\_PROXY\_GROUP\_OBJECT\_TRACK\_TYPE](group__bt__media__proxy.md#ga7412b20ea355713443b7165f077b0a0d)   0x00 |
|  | Group object type is track. |
| #define | [MEDIA\_PROXY\_GROUP\_OBJECT\_GROUP\_TYPE](group__bt__media__proxy.md#ga63abba926894a45e187e3f4e4610cb35)   0x01 |
|  | Group object type is group. |

| Functions | |
| --- | --- |
| int | [media\_proxy\_ctrl\_register](group__bt__media__proxy.md#ga352228fb77498b61205a22b0f3a75c8e) (struct [media\_proxy\_ctrl\_cbs](structmedia__proxy__ctrl__cbs.md) \*ctrl\_cbs) |
|  | Register a controller with the media\_proxy. |
| int | [media\_proxy\_ctrl\_discover\_player](group__bt__media__proxy.md#ga5aaa486e0c3663e21477984e54642ed1) (struct bt\_conn \*conn) |
|  | Discover a remote media player. |
| int | [media\_proxy\_ctrl\_get\_player\_name](group__bt__media__proxy.md#ga2261222d8581ed86e91a276b13359126) (struct media\_player \*player) |
|  | Read Media Player Name. |
| int | [media\_proxy\_ctrl\_get\_icon\_id](group__bt__media__proxy.md#ga5efccb39cdb97eed476e0c0bff461ec1) (struct media\_player \*player) |
|  | Read Icon Object ID. |
| int | [media\_proxy\_ctrl\_get\_icon\_url](group__bt__media__proxy.md#gab6df6fe71c8273eca855eb3be27290dd) (struct media\_player \*player) |
|  | Read Icon URL. |
| int | [media\_proxy\_ctrl\_get\_track\_title](group__bt__media__proxy.md#gabfbb49e79204130cb004f217af771b80) (struct media\_player \*player) |
|  | Read Track Title. |
| int | [media\_proxy\_ctrl\_get\_track\_duration](group__bt__media__proxy.md#ga488441418a8f2d358092019bbfe16788) (struct media\_player \*player) |
|  | Read Track Duration. |
| int | [media\_proxy\_ctrl\_get\_track\_position](group__bt__media__proxy.md#gae0bb75feb49a68b495150c6fba2f21a7) (struct media\_player \*player) |
|  | Read Track Position. |
| int | [media\_proxy\_ctrl\_set\_track\_position](group__bt__media__proxy.md#ga776bb5f16cf1f4f6cc3842aabd86b781) (struct media\_player \*player, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) position) |
|  | Set Track Position. |
| int | [media\_proxy\_ctrl\_get\_playback\_speed](group__bt__media__proxy.md#ga2d64a23b3f881579a603a04baeb64088) (struct media\_player \*player) |
|  | Get Playback Speed. |
| int | [media\_proxy\_ctrl\_set\_playback\_speed](group__bt__media__proxy.md#gabafbc857c3e6befe98e339acb58f17fb) (struct media\_player \*player, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) speed) |
|  | Set Playback Speed. |
| int | [media\_proxy\_ctrl\_get\_seeking\_speed](group__bt__media__proxy.md#ga817ca4ab611e214493fbc918036def0f) (struct media\_player \*player) |
|  | Get Seeking Speed. |
| int | [media\_proxy\_ctrl\_get\_track\_segments\_id](group__bt__media__proxy.md#ga1afcc097cb36c4f11141b82ce28e8126) (struct media\_player \*player) |
|  | Read Current Track Segments Object ID. |
| int | [media\_proxy\_ctrl\_get\_current\_track\_id](group__bt__media__proxy.md#gaebe7e3683041e28bef40df75cc991dea) (struct media\_player \*player) |
|  | Read Current Track Object ID. |
| int | [media\_proxy\_ctrl\_set\_current\_track\_id](group__bt__media__proxy.md#gaea6adacedaded10f7c2c0f91b7159f74) (struct media\_player \*player, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Set Current Track Object ID. |
| int | [media\_proxy\_ctrl\_get\_next\_track\_id](group__bt__media__proxy.md#gae32da32bd504061801730805729242e1) (struct media\_player \*player) |
|  | Read Next Track Object ID. |
| int | [media\_proxy\_ctrl\_set\_next\_track\_id](group__bt__media__proxy.md#ga43b797717fb9b36b94a606dfabeb0fa7) (struct media\_player \*player, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Set Next Track Object ID. |
| int | [media\_proxy\_ctrl\_get\_parent\_group\_id](group__bt__media__proxy.md#ga12dc878be39814660900ba875e13e537) (struct media\_player \*player) |
|  | Read Parent Group Object ID. |
| int | [media\_proxy\_ctrl\_get\_current\_group\_id](group__bt__media__proxy.md#ga2ae50a1988305b4247ff0af796b6d93e) (struct media\_player \*player) |
|  | Read Current Group Object ID. |
| int | [media\_proxy\_ctrl\_set\_current\_group\_id](group__bt__media__proxy.md#gae496885d0124f4e3fc2c0f203fcff118) (struct media\_player \*player, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Set Current Group Object ID. |
| int | [media\_proxy\_ctrl\_get\_playing\_order](group__bt__media__proxy.md#ga2f93bcde2460c6638880f8e6631eb68e) (struct media\_player \*player) |
|  | Read Playing Order. |
| int | [media\_proxy\_ctrl\_set\_playing\_order](group__bt__media__proxy.md#gaa4040e97100f6e70527e6ad201309bbe) (struct media\_player \*player, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) order) |
|  | Set Playing Order. |
| int | [media\_proxy\_ctrl\_get\_playing\_orders\_supported](group__bt__media__proxy.md#ga030899757b79251f1d5a1055f65fe989) (struct media\_player \*player) |
|  | Read Playing Orders Supported. |
| int | [media\_proxy\_ctrl\_get\_media\_state](group__bt__media__proxy.md#ga9433aaf24776c30557ea694795e75b3e) (struct media\_player \*player) |
|  | Read Media State. |
| int | [media\_proxy\_ctrl\_send\_command](group__bt__media__proxy.md#ga590762e7272b99fb8ac50a7841424670) (struct media\_player \*player, const struct [mpl\_cmd](structmpl__cmd.md) \*command) |
|  | Send Command. |
| int | [media\_proxy\_ctrl\_get\_commands\_supported](group__bt__media__proxy.md#ga15804287093b20d4a1616380729b33c8) (struct media\_player \*player) |
|  | Read Commands Supported. |
| int | [media\_proxy\_ctrl\_send\_search](group__bt__media__proxy.md#ga052c3fabac4a44ee2802ddd4a6c5c9ac) (struct media\_player \*player, const struct [mpl\_search](structmpl__search.md) \*search) |
|  | Set Search. |
| int | [media\_proxy\_ctrl\_get\_search\_results\_id](group__bt__media__proxy.md#ga580a0c9fa47460be59f0571ee11a41b4) (struct media\_player \*player) |
|  | Read Search Results Object ID. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [media\_proxy\_ctrl\_get\_content\_ctrl\_id](group__bt__media__proxy.md#ga23488e77985a04216ec7c7fa785f09fc) (struct media\_player \*player) |
|  | Read Content Control ID. |
| int | [media\_proxy\_pl\_register](group__bt__media__proxy.md#gac75e27a4a5e169481723cd6b39678274) (struct [media\_proxy\_pl\_calls](structmedia__proxy__pl__calls.md) \*pl\_calls) |
|  | Register a player with the media proxy. |
| int | [media\_proxy\_pl\_init](group__bt__media__proxy.md#gab0b10b3de5674f2172e1a2f779cbe8d5) (void) |
|  | Initialize player. |
| struct bt\_ots \* | [bt\_mcs\_get\_ots](group__bt__media__proxy.md#gaf535f1ab028407432ef890d278d936e0) (void) |
|  | Get the pointer of the Object Transfer Service used by the Media Control Service. |
| void | [media\_proxy\_pl\_name\_cb](group__bt__media__proxy.md#ga0a70dc60a4d6acbcc58e220b75dad92a) (const char \*name) |
|  | Player name changed callback. |
| void | [media\_proxy\_pl\_icon\_url\_cb](group__bt__media__proxy.md#gadd348a8d5aff193f7a9113a759e85b1d) (const char \*url) |
|  | Player icon URL changed callback. |
| void | [media\_proxy\_pl\_track\_changed\_cb](group__bt__media__proxy.md#ga4a93a18cb0b75cb16828243f0d37b4b4) (void) |
|  | Track changed callback. |
| void | [media\_proxy\_pl\_track\_title\_cb](group__bt__media__proxy.md#ga9489b517e4baa215f0b7b59243cee11c) (char \*title) |
|  | Track title callback. |
| void | [media\_proxy\_pl\_track\_duration\_cb](group__bt__media__proxy.md#ga7b0f9633a5322557b91ea97eafac9f34) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) duration) |
|  | Track duration callback. |
| void | [media\_proxy\_pl\_track\_position\_cb](group__bt__media__proxy.md#ga61d494d7e149cfa2c3f9546c1e3b99bd) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) position) |
|  | Track position callback. |
| void | [media\_proxy\_pl\_playback\_speed\_cb](group__bt__media__proxy.md#ga17c2ca149050e1382eb556f6dcccad21) ([int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) speed) |
|  | Playback speed callback. |
| void | [media\_proxy\_pl\_seeking\_speed\_cb](group__bt__media__proxy.md#gaeaf89f4b760870896ed42687562971ca) ([int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) speed) |
|  | Seeking speed callback. |
| void | [media\_proxy\_pl\_current\_track\_id\_cb](group__bt__media__proxy.md#gadcad4efdd714159d5d9611bbf74d5fae) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Current track object ID callback. |
| void | [media\_proxy\_pl\_next\_track\_id\_cb](group__bt__media__proxy.md#gaf0bd3447e64b6128710c07461766a0c9) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Next track object ID callback. |
| void | [media\_proxy\_pl\_parent\_group\_id\_cb](group__bt__media__proxy.md#ga64730f46b87cf9089aff65b6be12f42d) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Parent group object ID callback. |
| void | [media\_proxy\_pl\_current\_group\_id\_cb](group__bt__media__proxy.md#gad02f2924e1aa765c04cbbc6441e7d063) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Current group object ID callback. |
| void | [media\_proxy\_pl\_playing\_order\_cb](group__bt__media__proxy.md#ga96e8156b0267f3d55ee52ab307d81985) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) order) |
|  | Playing order callback. |
| void | [media\_proxy\_pl\_media\_state\_cb](group__bt__media__proxy.md#ga842d7951a04702d6f819de44c47b9cac) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Media state callback. |
| void | [media\_proxy\_pl\_command\_cb](group__bt__media__proxy.md#ga694e83401835149833024cf094b98cd1) (const struct [mpl\_cmd\_ntf](structmpl__cmd__ntf.md) \*cmd\_ntf) |
|  | Command callback. |
| void | [media\_proxy\_pl\_commands\_supported\_cb](group__bt__media__proxy.md#ga70ea8a24a4e853a191e0947e1c2d1145) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) opcodes) |
|  | Commands supported callback. |
| void | [media\_proxy\_pl\_search\_cb](group__bt__media__proxy.md#ga8c0d75f61120047bacd0b933534e1b41) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) result\_code) |
|  | Search callback. |
| void | [media\_proxy\_pl\_search\_results\_id\_cb](group__bt__media__proxy.md#ga35896de266f2a2bd101279e4ce9900c7) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Search Results object ID callback. |

## Detailed Description

Bluetooth Media Proxy APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [media\_proxy.h](media__proxy_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
