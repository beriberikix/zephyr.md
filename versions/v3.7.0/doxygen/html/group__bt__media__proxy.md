---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__bt__media__proxy.html
original_path: doxygen/html/group__bt__media__proxy.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Media Proxy

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

Media proxy module.
[More...](#details)

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
| #define | [MEDIA\_PROXY\_OPCODES\_SUPPORTED\_LEN](#ga22c2599cd62a263a01c06c9bd9fff054)   4 |
|  | Media player supported opcodes length. |

| Functions | |
| --- | --- |
| int | [media\_proxy\_ctrl\_register](#ga352228fb77498b61205a22b0f3a75c8e) (struct [media\_proxy\_ctrl\_cbs](structmedia__proxy__ctrl__cbs.md) \*ctrl\_cbs) |
|  | Register a controller with the media\_proxy. |
| int | [media\_proxy\_ctrl\_discover\_player](#ga5aaa486e0c3663e21477984e54642ed1) (struct bt\_conn \*conn) |
|  | Discover a remote media player. |
| int | [media\_proxy\_ctrl\_get\_player\_name](#ga2261222d8581ed86e91a276b13359126) (struct media\_player \*player) |
|  | Read Media Player Name. |
| int | [media\_proxy\_ctrl\_get\_icon\_id](#ga5efccb39cdb97eed476e0c0bff461ec1) (struct media\_player \*player) |
|  | Read Icon Object ID. |
| int | [media\_proxy\_ctrl\_get\_icon\_url](#gab6df6fe71c8273eca855eb3be27290dd) (struct media\_player \*player) |
|  | Read Icon URL. |
| int | [media\_proxy\_ctrl\_get\_track\_title](#gabfbb49e79204130cb004f217af771b80) (struct media\_player \*player) |
|  | Read Track Title. |
| int | [media\_proxy\_ctrl\_get\_track\_duration](#ga488441418a8f2d358092019bbfe16788) (struct media\_player \*player) |
|  | Read Track Duration. |
| int | [media\_proxy\_ctrl\_get\_track\_position](#gae0bb75feb49a68b495150c6fba2f21a7) (struct media\_player \*player) |
|  | Read Track Position. |
| int | [media\_proxy\_ctrl\_set\_track\_position](#ga776bb5f16cf1f4f6cc3842aabd86b781) (struct media\_player \*player, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) position) |
|  | Set Track Position. |
| int | [media\_proxy\_ctrl\_get\_playback\_speed](#ga2d64a23b3f881579a603a04baeb64088) (struct media\_player \*player) |
|  | Get Playback Speed. |
| int | [media\_proxy\_ctrl\_set\_playback\_speed](#gabafbc857c3e6befe98e339acb58f17fb) (struct media\_player \*player, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) speed) |
|  | Set Playback Speed. |
| int | [media\_proxy\_ctrl\_get\_seeking\_speed](#ga817ca4ab611e214493fbc918036def0f) (struct media\_player \*player) |
|  | Get Seeking Speed. |
| int | [media\_proxy\_ctrl\_get\_track\_segments\_id](#ga1afcc097cb36c4f11141b82ce28e8126) (struct media\_player \*player) |
|  | Read Current Track Segments Object ID. |
| int | [media\_proxy\_ctrl\_get\_current\_track\_id](#gaebe7e3683041e28bef40df75cc991dea) (struct media\_player \*player) |
|  | Read Current Track Object ID. |
| int | [media\_proxy\_ctrl\_set\_current\_track\_id](#gaea6adacedaded10f7c2c0f91b7159f74) (struct media\_player \*player, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Set Current Track Object ID. |
| int | [media\_proxy\_ctrl\_get\_next\_track\_id](#gae32da32bd504061801730805729242e1) (struct media\_player \*player) |
|  | Read Next Track Object ID. |
| int | [media\_proxy\_ctrl\_set\_next\_track\_id](#ga43b797717fb9b36b94a606dfabeb0fa7) (struct media\_player \*player, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Set Next Track Object ID. |
| int | [media\_proxy\_ctrl\_get\_parent\_group\_id](#ga12dc878be39814660900ba875e13e537) (struct media\_player \*player) |
|  | Read Parent Group Object ID. |
| int | [media\_proxy\_ctrl\_get\_current\_group\_id](#ga2ae50a1988305b4247ff0af796b6d93e) (struct media\_player \*player) |
|  | Read Current Group Object ID. |
| int | [media\_proxy\_ctrl\_set\_current\_group\_id](#gae496885d0124f4e3fc2c0f203fcff118) (struct media\_player \*player, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Set Current Group Object ID. |
| int | [media\_proxy\_ctrl\_get\_playing\_order](#ga2f93bcde2460c6638880f8e6631eb68e) (struct media\_player \*player) |
|  | Read Playing Order. |
| int | [media\_proxy\_ctrl\_set\_playing\_order](#gaa4040e97100f6e70527e6ad201309bbe) (struct media\_player \*player, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) order) |
|  | Set Playing Order. |
| int | [media\_proxy\_ctrl\_get\_playing\_orders\_supported](#ga030899757b79251f1d5a1055f65fe989) (struct media\_player \*player) |
|  | Read Playing Orders Supported. |
| int | [media\_proxy\_ctrl\_get\_media\_state](#ga9433aaf24776c30557ea694795e75b3e) (struct media\_player \*player) |
|  | Read Media State. |
| int | [media\_proxy\_ctrl\_send\_command](#ga590762e7272b99fb8ac50a7841424670) (struct media\_player \*player, const struct [mpl\_cmd](structmpl__cmd.md) \*command) |
|  | Send Command. |
| int | [media\_proxy\_ctrl\_get\_commands\_supported](#ga15804287093b20d4a1616380729b33c8) (struct media\_player \*player) |
|  | Read Commands Supported. |
| int | [media\_proxy\_ctrl\_send\_search](#ga052c3fabac4a44ee2802ddd4a6c5c9ac) (struct media\_player \*player, const struct [mpl\_search](structmpl__search.md) \*search) |
|  | Set Search. |
| int | [media\_proxy\_ctrl\_get\_search\_results\_id](#ga580a0c9fa47460be59f0571ee11a41b4) (struct media\_player \*player) |
|  | Read Search Results Object ID. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [media\_proxy\_ctrl\_get\_content\_ctrl\_id](#ga23488e77985a04216ec7c7fa785f09fc) (struct media\_player \*player) |
|  | Read Content Control ID. |
| int | [media\_proxy\_pl\_register](#gac75e27a4a5e169481723cd6b39678274) (struct [media\_proxy\_pl\_calls](structmedia__proxy__pl__calls.md) \*pl\_calls) |
|  | Register a player with the media proxy. |
| int | [media\_proxy\_pl\_init](#gab0b10b3de5674f2172e1a2f779cbe8d5) (void) |
|  | Initialize player. |
| struct bt\_ots \* | [bt\_mcs\_get\_ots](#gaf535f1ab028407432ef890d278d936e0) (void) |
|  | Get the pointer of the Object Transfer Service used by the Media Control Service. |
| void | [media\_proxy\_pl\_name\_cb](#ga0a70dc60a4d6acbcc58e220b75dad92a) (const char \*name) |
|  | Player name changed callback. |
| void | [media\_proxy\_pl\_icon\_url\_cb](#gadd348a8d5aff193f7a9113a759e85b1d) (const char \*url) |
|  | Player icon URL changed callback. |
| void | [media\_proxy\_pl\_track\_changed\_cb](#ga4a93a18cb0b75cb16828243f0d37b4b4) (void) |
|  | Track changed callback. |
| void | [media\_proxy\_pl\_track\_title\_cb](#ga9489b517e4baa215f0b7b59243cee11c) (char \*title) |
|  | Track title callback. |
| void | [media\_proxy\_pl\_track\_duration\_cb](#ga7b0f9633a5322557b91ea97eafac9f34) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) duration) |
|  | Track duration callback. |
| void | [media\_proxy\_pl\_track\_position\_cb](#ga61d494d7e149cfa2c3f9546c1e3b99bd) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) position) |
|  | Track position callback. |
| void | [media\_proxy\_pl\_playback\_speed\_cb](#ga17c2ca149050e1382eb556f6dcccad21) ([int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) speed) |
|  | Playback speed callback. |
| void | [media\_proxy\_pl\_seeking\_speed\_cb](#gaeaf89f4b760870896ed42687562971ca) ([int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) speed) |
|  | Seeking speed callback. |
| void | [media\_proxy\_pl\_current\_track\_id\_cb](#gadcad4efdd714159d5d9611bbf74d5fae) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Current track object ID callback. |
| void | [media\_proxy\_pl\_next\_track\_id\_cb](#gaf0bd3447e64b6128710c07461766a0c9) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Next track object ID callback. |
| void | [media\_proxy\_pl\_parent\_group\_id\_cb](#ga64730f46b87cf9089aff65b6be12f42d) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Parent group object ID callback. |
| void | [media\_proxy\_pl\_current\_group\_id\_cb](#gad02f2924e1aa765c04cbbc6441e7d063) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Current group object ID callback. |
| void | [media\_proxy\_pl\_playing\_order\_cb](#ga96e8156b0267f3d55ee52ab307d81985) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) order) |
|  | Playing order callback. |
| void | [media\_proxy\_pl\_media\_state\_cb](#ga842d7951a04702d6f819de44c47b9cac) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Media state callback. |
| void | [media\_proxy\_pl\_command\_cb](#ga694e83401835149833024cf094b98cd1) (const struct [mpl\_cmd\_ntf](structmpl__cmd__ntf.md) \*cmd\_ntf) |
|  | Command callback. |
| void | [media\_proxy\_pl\_commands\_supported\_cb](#ga70ea8a24a4e853a191e0947e1c2d1145) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) opcodes) |
|  | Commands supported callback. |
| void | [media\_proxy\_pl\_search\_cb](#ga8c0d75f61120047bacd0b933534e1b41) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) result\_code) |
|  | Search callback. |
| void | [media\_proxy\_pl\_search\_results\_id\_cb](#ga35896de266f2a2bd101279e4ce9900c7) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) id) |
|  | Search Results object ID callback. |

| Playback speed parameters | |
| --- | --- |
| All values from -128 to 127 allowed, only some defined | |
| #define | [MEDIA\_PROXY\_PLAYBACK\_SPEED\_MIN](#ga61732644eecad1442d5cedbda8f8cc08)   -128 |
|  | Minimum playback speed, resulting in 25 % speed. |
| #define | [MEDIA\_PROXY\_PLAYBACK\_SPEED\_QUARTER](#ga5462f8d5ce98cc33a131b2e7b5548c41)   -128 |
|  | Quarter playback speed, resulting in 25 % speed. |
| #define | [MEDIA\_PROXY\_PLAYBACK\_SPEED\_HALF](#ga4c765363c2a5b0d9800864859746ae33)   -64 |
|  | Half playback speed, resulting in 50 % speed. |
| #define | [MEDIA\_PROXY\_PLAYBACK\_SPEED\_UNITY](#ga6d8854bd54dcbb657f0ba545ec231368)   0 |
|  | Unity playback speed, resulting in 100 % speed. |
| #define | [MEDIA\_PROXY\_PLAYBACK\_SPEED\_DOUBLE](#gaa53d906340c0b2adb314945f5299464e)   64 |
|  | Double playback speed, resulting in 200 % speed. |
| #define | [MEDIA\_PROXY\_PLAYBACK\_SPEED\_MAX](#gaaccc9d75f96b5fe2de101b119a516d36)   127 |
|  | Max playback speed, resulting in 395.7 % speed (nearly 400 %). |

| Seeking speed factors | |
| --- | --- |
| The allowed values for seeking speed are the range -64 to -4 (endpoints included), the value 0, and the range 4 to 64 (endpoints included). | |
| #define | [MEDIA\_PROXY\_SEEKING\_SPEED\_FACTOR\_MAX](#gaa6aa7a6e98631152b4bd77b60c78d58a)   64 |
|  | Maximum seeking speed - Can be negated. |
| #define | [MEDIA\_PROXY\_SEEKING\_SPEED\_FACTOR\_MIN](#ga67c1069fa01425ad6cd8f36438b71826)   4 |
|  | Minimum seeking speed - Can be negated. |
| #define | [MEDIA\_PROXY\_SEEKING\_SPEED\_FACTOR\_ZERO](#ga58495e58bf84235efcee89289fc992c2)   0 |
|  | No seeking. |

| Playing orders | |
| --- | --- |
| #define | [MEDIA\_PROXY\_PLAYING\_ORDER\_SINGLE\_ONCE](#ga8e721b49c361d2395bd8eb740d43e282)   0x01 |
|  | A single track is played once; there is no next track. |
| #define | [MEDIA\_PROXY\_PLAYING\_ORDER\_SINGLE\_REPEAT](#gadf5f0c15cb88cd92f49db1b57dbd2c18)   0x02 |
|  | A single track is played repeatedly; the next track is the current track. |
| #define | [MEDIA\_PROXY\_PLAYING\_ORDER\_INORDER\_ONCE](#ga63055a150b93f06e076b97abb6f6f682)   0x03 |
|  | The tracks within a group are played once in track order. |
| #define | [MEDIA\_PROXY\_PLAYING\_ORDER\_INORDER\_REPEAT](#ga437068b9d90404cc68d41faaedfac9a8)   0x04 |
|  | The tracks within a group are played in track order repeatedly. |
| #define | [MEDIA\_PROXY\_PLAYING\_ORDER\_OLDEST\_ONCE](#ga48a33dd8fbb8a8ab162c18bc0e9b7531)   0x05 |
|  | The tracks within a group are played once only from the oldest first. |
| #define | [MEDIA\_PROXY\_PLAYING\_ORDER\_OLDEST\_REPEAT](#ga63a33c4e3267ab39ab5892fb5b0bbe89)   0x06 |
|  | The tracks within a group are played from the oldest first repeatedly. |
| #define | [MEDIA\_PROXY\_PLAYING\_ORDER\_NEWEST\_ONCE](#gac344111e2b043cdfbcb9ac272622b16f)   0x07 |
|  | The tracks within a group are played once only from the newest first. |
| #define | [MEDIA\_PROXY\_PLAYING\_ORDER\_NEWEST\_REPEAT](#gaf10b815dc579dc67b1f092e0a85c51d9)   0x08 |
|  | The tracks within a group are played from the newest first repeatedly. |
| #define | [MEDIA\_PROXY\_PLAYING\_ORDER\_SHUFFLE\_ONCE](#gae152374af5d567cf65d6d7b236b792a4)   0x09 |
|  | The tracks within a group are played in random order once. |
| #define | [MEDIA\_PROXY\_PLAYING\_ORDER\_SHUFFLE\_REPEAT](#ga45161ec08b67e4d3bd59efa45027f3aa)   0x0a |
|  | The tracks within a group are played in random order repeatedly. |

| Playing orders supported | |
| --- | --- |
| A bitmap, in the same order as the playing orders above.  Note that playing order 1 corresponds to bit 0, and so on. | |
| #define | [MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_SINGLE\_ONCE](#ga55b5a00ea9ec849e7c495463e5f1869d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | A single track is played once; there is no next track. |
| #define | [MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_SINGLE\_REPEAT](#ga465a82ace21a0e88356eccaf038f58e9)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | A single track is played repeatedly; the next track is the current track. |
| #define | [MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_INORDER\_ONCE](#ga8fee464b8e17fffc4361972df15062af)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | The tracks within a group are played once in track order. |
| #define | [MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_INORDER\_REPEAT](#ga7faeff14de245ea670ca447b0adc4820)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | The tracks within a group are played in track order repeatedly. |
| #define | [MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_OLDEST\_ONCE](#gae3d848fc0b9117fe9bc51327627ac635)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | The tracks within a group are played once only from the oldest first. |
| #define | [MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_OLDEST\_REPEAT](#ga7fa415d845dd1fefc8bdb74532878131)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | The tracks within a group are played from the oldest first repeatedly. |
| #define | [MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_NEWEST\_ONCE](#ga334f9e16ea7a52bfb6357ad619e3601b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | The tracks within a group are played once only from the newest first. |
| #define | [MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_NEWEST\_REPEAT](#gaaf5f08e2dd624e2bb1bd9b72ab4b2b33)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
|  | The tracks within a group are played from the newest first repeatedly. |
| #define | [MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_SHUFFLE\_ONCE](#ga3e998cda3e91f1c9fbb8496a748bcf12)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
|  | The tracks within a group are played in random order once. |
| #define | [MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_SHUFFLE\_REPEAT](#ga4f0689fe1fc0ac2b3f9b9ef4ed1afb8b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
|  | The tracks within a group are played in random order repeatedly. |

| Media player states | |
| --- | --- |
| #define | [MEDIA\_PROXY\_STATE\_INACTIVE](#gab8c465e0e63898e53c39171b89d668c9)   0x00 |
|  | The current track is invalid, and no track has been selected. |
| #define | [MEDIA\_PROXY\_STATE\_PLAYING](#ga1967c76b290f1d20515740cf7139f49c)   0x01 |
|  | The media player is playing the current track. |
| #define | [MEDIA\_PROXY\_STATE\_PAUSED](#ga85325d7ff75ec05275a875d7d5540a6c)   0x02 |
|  | The current track is paused. |
| #define | [MEDIA\_PROXY\_STATE\_SEEKING](#gaa207ee7666ab18c40e5b1d2a6ed7f034)   0x03 |
|  | The current track is fast forwarding or fast rewinding. |
| #define | [MEDIA\_PROXY\_STATE\_LAST](#gab0c8f3510109f18ef6445f035b27cbe9)   0x04 |
|  | Used internally as the last state value. |

| Media player command opcodes | |
| --- | --- |
| #define | [MEDIA\_PROXY\_OP\_PLAY](#gadd400bc6900abe1956d4de4efb212683)   0x01 |
|  | Start playing the current track. |
| #define | [MEDIA\_PROXY\_OP\_PAUSE](#ga69bcb42294e8cd1eb062bbe19399a3df)   0x02 |
|  | Pause playing the current track. |
| #define | [MEDIA\_PROXY\_OP\_FAST\_REWIND](#gabc2b497b95728325208e28db6d5cf4f8)   0x03 |
|  | Fast rewind the current track. |
| #define | [MEDIA\_PROXY\_OP\_FAST\_FORWARD](#gac0c0730bcf6592c5d2c61d21d09efb2b)   0x04 |
|  | Fast forward the current track. |
| #define | [MEDIA\_PROXY\_OP\_STOP](#gaf3707d44c7a3305ba896c0257b2109b3)   0x05 |
|  | Stop current activity and return to the paused state and set the current track position to the start of the current track. |
| #define | [MEDIA\_PROXY\_OP\_MOVE\_RELATIVE](#gaceb240f7f21074b6b7f9ed1e9d645cb0)   0x10 |
|  | Set a new current track position relative to the current track position. |
| #define | [MEDIA\_PROXY\_OP\_PREV\_SEGMENT](#ga7846fa5da200e0d921056b410e60677e)   0x20 |
|  | Set the current track position to the starting position of the previous segment of the current track. |
| #define | [MEDIA\_PROXY\_OP\_NEXT\_SEGMENT](#gada5e3114b2b00f4ea27adf884f49429e)   0x21 |
|  | Set the current track position to the starting position of the next segment of the current track. |
| #define | [MEDIA\_PROXY\_OP\_FIRST\_SEGMENT](#gac2e5c8e2cadd05092fa186f05ae74e57)   0x22 |
|  | Set the current track position to the starting position of the first segment of the current track. |
| #define | [MEDIA\_PROXY\_OP\_LAST\_SEGMENT](#ga3f317208b9d8495c498325a4d37d41ad)   0x23 |
|  | Set the current track position to the starting position of the last segment of the current track. |
| #define | [MEDIA\_PROXY\_OP\_GOTO\_SEGMENT](#gab3bbf7eb7c562bc6a5148c75eb99ada5)   0x24 |
|  | Set the current track position to the starting position of the nth segment of the current track. |
| #define | [MEDIA\_PROXY\_OP\_PREV\_TRACK](#ga1b7db568fc3153c29ed4e951d95bee8e)   0x30 |
|  | Set the current track to the previous track based on the playing order. |
| #define | [MEDIA\_PROXY\_OP\_NEXT\_TRACK](#gaae4cc32663f02bf96d1dcbbc8453e40b)   0x31 |
|  | Set the current track to the next track based on the playing order. |
| #define | [MEDIA\_PROXY\_OP\_FIRST\_TRACK](#ga5c272e2e9b24ce92a7df7373d1b002cc)   0x32 |
|  | Set the current track to the first track based on the playing order. |
| #define | [MEDIA\_PROXY\_OP\_LAST\_TRACK](#ga72614d9a2fa4c938f1c7055bc219c8bc)   0x33 |
|  | Set the current track to the last track based on the playing order. |
| #define | [MEDIA\_PROXY\_OP\_GOTO\_TRACK](#gaf2f100d41413b14c5dbd8f2641a13bb0)   0x34 |
|  | Set the current track to the nth track based on the playing order. |
| #define | [MEDIA\_PROXY\_OP\_PREV\_GROUP](#gae15386adcfe1c5ca56eac7d0292dffd0)   0x40 |
|  | Set the current group to the previous group in the sequence of groups. |
| #define | [MEDIA\_PROXY\_OP\_NEXT\_GROUP](#ga3cf10acf1ef8b7d3252eb37cb4e35f97)   0x41 |
|  | Set the current group to the next group in the sequence of groups. |
| #define | [MEDIA\_PROXY\_OP\_FIRST\_GROUP](#ga5eb0a22c257e370cd76d73f7fa9e342c)   0x42 |
|  | Set the current group to the first group in the sequence of groups. |
| #define | [MEDIA\_PROXY\_OP\_LAST\_GROUP](#gaa6ac8f8bf674c0ffec22bd061e9be3dc)   0x43 |
|  | Set the current group to the last group in the sequence of groups. |
| #define | [MEDIA\_PROXY\_OP\_GOTO\_GROUP](#ga139d2ced243a6ff47d8335583974a0da)   0x44 |
|  | Set the current group to the nth group in the sequence of groups. |
| #define | [MEDIA\_PROXY\_OP\_SUP\_PLAY](#gafe30bb1287b9a44655d76364d4832eac)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Media player supported command opcodes. |
| #define | [MEDIA\_PROXY\_OP\_SUP\_PAUSE](#gaec37a692c28ca90c8053db9de2a6c44f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Support the Pause opcode. |
| #define | [MEDIA\_PROXY\_OP\_SUP\_FAST\_REWIND](#ga99952473bafd76f6ceaf141307510f28)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Support the Fast Rewind opcode. |
| #define | [MEDIA\_PROXY\_OP\_SUP\_FAST\_FORWARD](#ga05453105bc3d1579110e908b794e3ac5)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Support the Fast Forward opcode. |
| #define | [MEDIA\_PROXY\_OP\_SUP\_STOP](#ga060ff676a0b2f249a26aaf61147b68e8)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Support the Stop opcode. |
| #define | [MEDIA\_PROXY\_OP\_SUP\_MOVE\_RELATIVE](#ga03c393a29c68529e4dd9038e3947468b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | Support the Move Relative opcode. |
| #define | [MEDIA\_PROXY\_OP\_SUP\_PREV\_SEGMENT](#ga3d39700e21cbdf2906321c8899e0b626)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | Support the Previous Segment opcode. |
| #define | [MEDIA\_PROXY\_OP\_SUP\_NEXT\_SEGMENT](#ga26ae64ece06a1f6f8dd7eb2c9965a4b6)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
|  | Support the Next Segment opcode. |
| #define | [MEDIA\_PROXY\_OP\_SUP\_FIRST\_SEGMENT](#ga916ce95086dfeb127e124a8c5d530371)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
|  | Support the First Segment opcode. |
| #define | [MEDIA\_PROXY\_OP\_SUP\_LAST\_SEGMENT](#gaf193ea0b4a34e3981f2f45d3b9c228a2)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
|  | Support the Last Segment opcode. |
| #define | [MEDIA\_PROXY\_OP\_SUP\_GOTO\_SEGMENT](#ga7af591de387958f5c187ba8d0e834247)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
|  | Support the Goto Segment opcode. |
| #define | [MEDIA\_PROXY\_OP\_SUP\_PREV\_TRACK](#gafe8bab8f90281e5894e5f79f32449e63)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
|  | Support the Previous Track opcode. |
| #define | [MEDIA\_PROXY\_OP\_SUP\_NEXT\_TRACK](#gafc061bc953b0338aded4cef681f9e963)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
|  | Support the Next Track opcode. |
| #define | [MEDIA\_PROXY\_OP\_SUP\_FIRST\_TRACK](#ga6e1d53fedf09bd95bcf112495dcfd64f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
|  | Support the First Track opcode. |
| #define | [MEDIA\_PROXY\_OP\_SUP\_LAST\_TRACK](#gaf43188bb438b9a766d07cd2fa900e079)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
|  | Support the Last Track opcode. |
| #define | [MEDIA\_PROXY\_OP\_SUP\_GOTO\_TRACK](#gad2364a0ef8c54bd9fa3372edddae32b0)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15) |
|  | Support the Goto Track opcode. |
| #define | [MEDIA\_PROXY\_OP\_SUP\_PREV\_GROUP](#ga496060d673b48e045a5a2a57aa82bddc)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(16) |
|  | Support the Previous Group opcode. |
| #define | [MEDIA\_PROXY\_OP\_SUP\_NEXT\_GROUP](#ga324dae538f28e818eea79c83aaa0b22c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(17) |
|  | Support the Next Group opcode. |
| #define | [MEDIA\_PROXY\_OP\_SUP\_FIRST\_GROUP](#ga716af4c6eb702729ec4f9ff9ccc49b32)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(18) |
|  | Support the First Group opcode. |
| #define | [MEDIA\_PROXY\_OP\_SUP\_LAST\_GROUP](#gac944825600367a41e8213dfd9de569a3)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(19) |
|  | Support the Last Group opcode. |
| #define | [MEDIA\_PROXY\_OP\_SUP\_GOTO\_GROUP](#gaec8b6d2d684c81b9da9fee870e0258c2)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(20) |
|  | Support the Goto Group opcode. |

| Media player command result codes | |
| --- | --- |
| #define | [MEDIA\_PROXY\_CMD\_SUCCESS](#gaa56458b11f4cb78f1265ea8538774108)   0x01 |
|  | Action requested by the opcode write was completed successfully. |
| #define | [MEDIA\_PROXY\_CMD\_NOT\_SUPPORTED](#ga1637459cd6eaf9d4d63a04d1facc29b7)   0x02 |
|  | An invalid or unsupported opcode was used for the Media Control Point write. |
| #define | [MEDIA\_PROXY\_CMD\_PLAYER\_INACTIVE](#ga7d0595796a80348b570add74c6dfa14e)   0x03 |
|  | The Media Player State characteristic value is Inactive when the opcode is received or the result of the requested action of the opcode results in the Media Player State characteristic being set to Inactive. |
| #define | [MEDIA\_PROXY\_CMD\_CANNOT\_BE\_COMPLETED](#gaf2c68cb2ac32973b85594660d43688dd)   0x04 |
|  | The requested action of any Media Control Point write cannot be completed successfully because of a condition within the player. |

| Search operation type values | |
| --- | --- |
| #define | [MEDIA\_PROXY\_SEARCH\_TYPE\_TRACK\_NAME](#ga8be6fd8d9bb08836bea1c3f0d2e577ea)   0x01 |
|  | Search for Track Name. |
| #define | [MEDIA\_PROXY\_SEARCH\_TYPE\_ARTIST\_NAME](#gaf0dbc19f843a444076d8886b1a05709b)   0x02 |
|  | Search for Artist Name. |
| #define | [MEDIA\_PROXY\_SEARCH\_TYPE\_ALBUM\_NAME](#ga1f0fb19dea467e90afd670ed9af0c092)   0x03 |
|  | Search for Album Name. |
| #define | [MEDIA\_PROXY\_SEARCH\_TYPE\_GROUP\_NAME](#gaca10de7253c1cdcf5e0c6544de33c116)   0x04 |
|  | Search for Group Name. |
| #define | [MEDIA\_PROXY\_SEARCH\_TYPE\_EARLIEST\_YEAR](#ga28b1d7de2174e3714786cb369232f339)   0x05 |
|  | Search for Earliest Year. |
| #define | [MEDIA\_PROXY\_SEARCH\_TYPE\_LATEST\_YEAR](#ga01fb087af00bf492d19cc19adcaa9dea)   0x06 |
|  | Search for Latest Year. |
| #define | [MEDIA\_PROXY\_SEARCH\_TYPE\_GENRE](#ga55c3a003881a75ce964e23fc3b0cea8e)   0x07 |
|  | Search for Genre. |
| #define | [MEDIA\_PROXY\_SEARCH\_TYPE\_ONLY\_TRACKS](#gad758e14fbe978ffd95364a6fb27eab40)   0x08 |
|  | Search for Tracks only. |
| #define | [MEDIA\_PROXY\_SEARCH\_TYPE\_ONLY\_GROUPS](#ga25270f6c90daaace6a80f3255aaaf7fd)   0x09 |
|  | Search for Groups only. |

| Search notification result codes | |
| --- | --- |
| #define | [MEDIA\_PROXY\_SEARCH\_SUCCESS](#ga2627f632efab868adddeebb59243497c)   0x01 |
|  | Search request was accepted; search has started. |
| #define | [MEDIA\_PROXY\_SEARCH\_FAILURE](#gaf406225a87c697d784c5a429e89d2354)   0x02 |
|  | Search request was invalid; no search started. |

| Group object object types | |
| --- | --- |
| #define | [MEDIA\_PROXY\_GROUP\_OBJECT\_TRACK\_TYPE](#ga7412b20ea355713443b7165f077b0a0d)   0x00 |
|  | Group object type is track. |
| #define | [MEDIA\_PROXY\_GROUP\_OBJECT\_GROUP\_TYPE](#ga63abba926894a45e187e3f4e4610cb35)   0x01 |
|  | Group object type is group. |

## Detailed Description

Media proxy module.

Since
:   3.0

Version
:   0.8.0

The media proxy module is the connection point between media players and media controllers.

A media player has (access to) media content and knows how to navigate and play this content. A media controller reads or gets information from a player and controls the player by setting player parameters and giving the player commands.

The media proxy module allows media player implementations to make themselves available to media controllers. And it allows controllers to access, and get updates from, any player.

The media proxy module allows both local and remote control of local player instances: A media controller may be a local application, or it may be a Media Control Service relaying requests from a remote Media Control Client. There may be either local or remote control, or both, or even multiple instances of each.

## Macro Definition Documentation

## [◆ ](#gaf2c68cb2ac32973b85594660d43688dd)MEDIA\_PROXY\_CMD\_CANNOT\_BE\_COMPLETED

| #define MEDIA\_PROXY\_CMD\_CANNOT\_BE\_COMPLETED   0x04 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

The requested action of any Media Control Point write cannot be completed successfully because of a condition within the player.

## [◆ ](#ga1637459cd6eaf9d4d63a04d1facc29b7)MEDIA\_PROXY\_CMD\_NOT\_SUPPORTED

| #define MEDIA\_PROXY\_CMD\_NOT\_SUPPORTED   0x02 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

An invalid or unsupported opcode was used for the Media Control Point write.

## [◆ ](#ga7d0595796a80348b570add74c6dfa14e)MEDIA\_PROXY\_CMD\_PLAYER\_INACTIVE

| #define MEDIA\_PROXY\_CMD\_PLAYER\_INACTIVE   0x03 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

The Media Player State characteristic value is Inactive when the opcode is received or the result of the requested action of the opcode results in the Media Player State characteristic being set to Inactive.

## [◆ ](#gaa56458b11f4cb78f1265ea8538774108)MEDIA\_PROXY\_CMD\_SUCCESS

| #define MEDIA\_PROXY\_CMD\_SUCCESS   0x01 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Action requested by the opcode write was completed successfully.

## [◆ ](#ga63abba926894a45e187e3f4e4610cb35)MEDIA\_PROXY\_GROUP\_OBJECT\_GROUP\_TYPE

| #define MEDIA\_PROXY\_GROUP\_OBJECT\_GROUP\_TYPE   0x01 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Group object type is group.

## [◆ ](#ga7412b20ea355713443b7165f077b0a0d)MEDIA\_PROXY\_GROUP\_OBJECT\_TRACK\_TYPE

| #define MEDIA\_PROXY\_GROUP\_OBJECT\_TRACK\_TYPE   0x00 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Group object type is track.

## [◆ ](#gac0c0730bcf6592c5d2c61d21d09efb2b)MEDIA\_PROXY\_OP\_FAST\_FORWARD

| #define MEDIA\_PROXY\_OP\_FAST\_FORWARD   0x04 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Fast forward the current track.

## [◆ ](#gabc2b497b95728325208e28db6d5cf4f8)MEDIA\_PROXY\_OP\_FAST\_REWIND

| #define MEDIA\_PROXY\_OP\_FAST\_REWIND   0x03 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Fast rewind the current track.

## [◆ ](#ga5eb0a22c257e370cd76d73f7fa9e342c)MEDIA\_PROXY\_OP\_FIRST\_GROUP

| #define MEDIA\_PROXY\_OP\_FIRST\_GROUP   0x42 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Set the current group to the first group in the sequence of groups.

## [◆ ](#gac2e5c8e2cadd05092fa186f05ae74e57)MEDIA\_PROXY\_OP\_FIRST\_SEGMENT

| #define MEDIA\_PROXY\_OP\_FIRST\_SEGMENT   0x22 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Set the current track position to the starting position of the first segment of the current track.

## [◆ ](#ga5c272e2e9b24ce92a7df7373d1b002cc)MEDIA\_PROXY\_OP\_FIRST\_TRACK

| #define MEDIA\_PROXY\_OP\_FIRST\_TRACK   0x32 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Set the current track to the first track based on the playing order.

## [◆ ](#ga139d2ced243a6ff47d8335583974a0da)MEDIA\_PROXY\_OP\_GOTO\_GROUP

| #define MEDIA\_PROXY\_OP\_GOTO\_GROUP   0x44 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Set the current group to the nth group in the sequence of groups.

## [◆ ](#gab3bbf7eb7c562bc6a5148c75eb99ada5)MEDIA\_PROXY\_OP\_GOTO\_SEGMENT

| #define MEDIA\_PROXY\_OP\_GOTO\_SEGMENT   0x24 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Set the current track position to the starting position of the nth segment of the current track.

## [◆ ](#gaf2f100d41413b14c5dbd8f2641a13bb0)MEDIA\_PROXY\_OP\_GOTO\_TRACK

| #define MEDIA\_PROXY\_OP\_GOTO\_TRACK   0x34 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Set the current track to the nth track based on the playing order.

## [◆ ](#gaa6ac8f8bf674c0ffec22bd061e9be3dc)MEDIA\_PROXY\_OP\_LAST\_GROUP

| #define MEDIA\_PROXY\_OP\_LAST\_GROUP   0x43 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Set the current group to the last group in the sequence of groups.

## [◆ ](#ga3f317208b9d8495c498325a4d37d41ad)MEDIA\_PROXY\_OP\_LAST\_SEGMENT

| #define MEDIA\_PROXY\_OP\_LAST\_SEGMENT   0x23 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Set the current track position to the starting position of the last segment of the current track.

## [◆ ](#ga72614d9a2fa4c938f1c7055bc219c8bc)MEDIA\_PROXY\_OP\_LAST\_TRACK

| #define MEDIA\_PROXY\_OP\_LAST\_TRACK   0x33 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Set the current track to the last track based on the playing order.

## [◆ ](#gaceb240f7f21074b6b7f9ed1e9d645cb0)MEDIA\_PROXY\_OP\_MOVE\_RELATIVE

| #define MEDIA\_PROXY\_OP\_MOVE\_RELATIVE   0x10 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Set a new current track position relative to the current track position.

## [◆ ](#ga3cf10acf1ef8b7d3252eb37cb4e35f97)MEDIA\_PROXY\_OP\_NEXT\_GROUP

| #define MEDIA\_PROXY\_OP\_NEXT\_GROUP   0x41 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Set the current group to the next group in the sequence of groups.

## [◆ ](#gada5e3114b2b00f4ea27adf884f49429e)MEDIA\_PROXY\_OP\_NEXT\_SEGMENT

| #define MEDIA\_PROXY\_OP\_NEXT\_SEGMENT   0x21 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Set the current track position to the starting position of the next segment of the current track.

## [◆ ](#gaae4cc32663f02bf96d1dcbbc8453e40b)MEDIA\_PROXY\_OP\_NEXT\_TRACK

| #define MEDIA\_PROXY\_OP\_NEXT\_TRACK   0x31 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Set the current track to the next track based on the playing order.

## [◆ ](#ga69bcb42294e8cd1eb062bbe19399a3df)MEDIA\_PROXY\_OP\_PAUSE

| #define MEDIA\_PROXY\_OP\_PAUSE   0x02 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Pause playing the current track.

## [◆ ](#gadd400bc6900abe1956d4de4efb212683)MEDIA\_PROXY\_OP\_PLAY

| #define MEDIA\_PROXY\_OP\_PLAY   0x01 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Start playing the current track.

## [◆ ](#gae15386adcfe1c5ca56eac7d0292dffd0)MEDIA\_PROXY\_OP\_PREV\_GROUP

| #define MEDIA\_PROXY\_OP\_PREV\_GROUP   0x40 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Set the current group to the previous group in the sequence of groups.

## [◆ ](#ga7846fa5da200e0d921056b410e60677e)MEDIA\_PROXY\_OP\_PREV\_SEGMENT

| #define MEDIA\_PROXY\_OP\_PREV\_SEGMENT   0x20 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Set the current track position to the starting position of the previous segment of the current track.

## [◆ ](#ga1b7db568fc3153c29ed4e951d95bee8e)MEDIA\_PROXY\_OP\_PREV\_TRACK

| #define MEDIA\_PROXY\_OP\_PREV\_TRACK   0x30 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Set the current track to the previous track based on the playing order.

## [◆ ](#gaf3707d44c7a3305ba896c0257b2109b3)MEDIA\_PROXY\_OP\_STOP

| #define MEDIA\_PROXY\_OP\_STOP   0x05 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Stop current activity and return to the paused state and set the current track position to the start of the current track.

## [◆ ](#ga05453105bc3d1579110e908b794e3ac5)MEDIA\_PROXY\_OP\_SUP\_FAST\_FORWARD

| #define MEDIA\_PROXY\_OP\_SUP\_FAST\_FORWARD   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Support the Fast Forward opcode.

## [◆ ](#ga99952473bafd76f6ceaf141307510f28)MEDIA\_PROXY\_OP\_SUP\_FAST\_REWIND

| #define MEDIA\_PROXY\_OP\_SUP\_FAST\_REWIND   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Support the Fast Rewind opcode.

## [◆ ](#ga716af4c6eb702729ec4f9ff9ccc49b32)MEDIA\_PROXY\_OP\_SUP\_FIRST\_GROUP

| #define MEDIA\_PROXY\_OP\_SUP\_FIRST\_GROUP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(18) |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Support the First Group opcode.

## [◆ ](#ga916ce95086dfeb127e124a8c5d530371)MEDIA\_PROXY\_OP\_SUP\_FIRST\_SEGMENT

| #define MEDIA\_PROXY\_OP\_SUP\_FIRST\_SEGMENT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Support the First Segment opcode.

## [◆ ](#ga6e1d53fedf09bd95bcf112495dcfd64f)MEDIA\_PROXY\_OP\_SUP\_FIRST\_TRACK

| #define MEDIA\_PROXY\_OP\_SUP\_FIRST\_TRACK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Support the First Track opcode.

## [◆ ](#gaec8b6d2d684c81b9da9fee870e0258c2)MEDIA\_PROXY\_OP\_SUP\_GOTO\_GROUP

| #define MEDIA\_PROXY\_OP\_SUP\_GOTO\_GROUP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(20) |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Support the Goto Group opcode.

## [◆ ](#ga7af591de387958f5c187ba8d0e834247)MEDIA\_PROXY\_OP\_SUP\_GOTO\_SEGMENT

| #define MEDIA\_PROXY\_OP\_SUP\_GOTO\_SEGMENT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Support the Goto Segment opcode.

## [◆ ](#gad2364a0ef8c54bd9fa3372edddae32b0)MEDIA\_PROXY\_OP\_SUP\_GOTO\_TRACK

| #define MEDIA\_PROXY\_OP\_SUP\_GOTO\_TRACK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15) |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Support the Goto Track opcode.

## [◆ ](#gac944825600367a41e8213dfd9de569a3)MEDIA\_PROXY\_OP\_SUP\_LAST\_GROUP

| #define MEDIA\_PROXY\_OP\_SUP\_LAST\_GROUP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(19) |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Support the Last Group opcode.

## [◆ ](#gaf193ea0b4a34e3981f2f45d3b9c228a2)MEDIA\_PROXY\_OP\_SUP\_LAST\_SEGMENT

| #define MEDIA\_PROXY\_OP\_SUP\_LAST\_SEGMENT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Support the Last Segment opcode.

## [◆ ](#gaf43188bb438b9a766d07cd2fa900e079)MEDIA\_PROXY\_OP\_SUP\_LAST\_TRACK

| #define MEDIA\_PROXY\_OP\_SUP\_LAST\_TRACK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Support the Last Track opcode.

## [◆ ](#ga03c393a29c68529e4dd9038e3947468b)MEDIA\_PROXY\_OP\_SUP\_MOVE\_RELATIVE

| #define MEDIA\_PROXY\_OP\_SUP\_MOVE\_RELATIVE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Support the Move Relative opcode.

## [◆ ](#ga324dae538f28e818eea79c83aaa0b22c)MEDIA\_PROXY\_OP\_SUP\_NEXT\_GROUP

| #define MEDIA\_PROXY\_OP\_SUP\_NEXT\_GROUP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(17) |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Support the Next Group opcode.

## [◆ ](#ga26ae64ece06a1f6f8dd7eb2c9965a4b6)MEDIA\_PROXY\_OP\_SUP\_NEXT\_SEGMENT

| #define MEDIA\_PROXY\_OP\_SUP\_NEXT\_SEGMENT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Support the Next Segment opcode.

## [◆ ](#gafc061bc953b0338aded4cef681f9e963)MEDIA\_PROXY\_OP\_SUP\_NEXT\_TRACK

| #define MEDIA\_PROXY\_OP\_SUP\_NEXT\_TRACK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Support the Next Track opcode.

## [◆ ](#gaec37a692c28ca90c8053db9de2a6c44f)MEDIA\_PROXY\_OP\_SUP\_PAUSE

| #define MEDIA\_PROXY\_OP\_SUP\_PAUSE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Support the Pause opcode.

## [◆ ](#gafe30bb1287b9a44655d76364d4832eac)MEDIA\_PROXY\_OP\_SUP\_PLAY

| #define MEDIA\_PROXY\_OP\_SUP\_PLAY   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Media player supported command opcodes.

Support the Play opcode

## [◆ ](#ga496060d673b48e045a5a2a57aa82bddc)MEDIA\_PROXY\_OP\_SUP\_PREV\_GROUP

| #define MEDIA\_PROXY\_OP\_SUP\_PREV\_GROUP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(16) |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Support the Previous Group opcode.

## [◆ ](#ga3d39700e21cbdf2906321c8899e0b626)MEDIA\_PROXY\_OP\_SUP\_PREV\_SEGMENT

| #define MEDIA\_PROXY\_OP\_SUP\_PREV\_SEGMENT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Support the Previous Segment opcode.

## [◆ ](#gafe8bab8f90281e5894e5f79f32449e63)MEDIA\_PROXY\_OP\_SUP\_PREV\_TRACK

| #define MEDIA\_PROXY\_OP\_SUP\_PREV\_TRACK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Support the Previous Track opcode.

## [◆ ](#ga060ff676a0b2f249a26aaf61147b68e8)MEDIA\_PROXY\_OP\_SUP\_STOP

| #define MEDIA\_PROXY\_OP\_SUP\_STOP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Support the Stop opcode.

## [◆ ](#ga22c2599cd62a263a01c06c9bd9fff054)MEDIA\_PROXY\_OPCODES\_SUPPORTED\_LEN

| #define MEDIA\_PROXY\_OPCODES\_SUPPORTED\_LEN   4 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Media player supported opcodes length.

## [◆ ](#gaa53d906340c0b2adb314945f5299464e)MEDIA\_PROXY\_PLAYBACK\_SPEED\_DOUBLE

| #define MEDIA\_PROXY\_PLAYBACK\_SPEED\_DOUBLE   64 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Double playback speed, resulting in 200 % speed.

## [◆ ](#ga4c765363c2a5b0d9800864859746ae33)MEDIA\_PROXY\_PLAYBACK\_SPEED\_HALF

| #define MEDIA\_PROXY\_PLAYBACK\_SPEED\_HALF   -64 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Half playback speed, resulting in 50 % speed.

## [◆ ](#gaaccc9d75f96b5fe2de101b119a516d36)MEDIA\_PROXY\_PLAYBACK\_SPEED\_MAX

| #define MEDIA\_PROXY\_PLAYBACK\_SPEED\_MAX   127 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Max playback speed, resulting in 395.7 % speed (nearly 400 %).

## [◆ ](#ga61732644eecad1442d5cedbda8f8cc08)MEDIA\_PROXY\_PLAYBACK\_SPEED\_MIN

| #define MEDIA\_PROXY\_PLAYBACK\_SPEED\_MIN   -128 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Minimum playback speed, resulting in 25 % speed.

## [◆ ](#ga5462f8d5ce98cc33a131b2e7b5548c41)MEDIA\_PROXY\_PLAYBACK\_SPEED\_QUARTER

| #define MEDIA\_PROXY\_PLAYBACK\_SPEED\_QUARTER   -128 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Quarter playback speed, resulting in 25 % speed.

## [◆ ](#ga6d8854bd54dcbb657f0ba545ec231368)MEDIA\_PROXY\_PLAYBACK\_SPEED\_UNITY

| #define MEDIA\_PROXY\_PLAYBACK\_SPEED\_UNITY   0 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Unity playback speed, resulting in 100 % speed.

## [◆ ](#ga63055a150b93f06e076b97abb6f6f682)MEDIA\_PROXY\_PLAYING\_ORDER\_INORDER\_ONCE

| #define MEDIA\_PROXY\_PLAYING\_ORDER\_INORDER\_ONCE   0x03 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

The tracks within a group are played once in track order.

## [◆ ](#ga437068b9d90404cc68d41faaedfac9a8)MEDIA\_PROXY\_PLAYING\_ORDER\_INORDER\_REPEAT

| #define MEDIA\_PROXY\_PLAYING\_ORDER\_INORDER\_REPEAT   0x04 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

The tracks within a group are played in track order repeatedly.

## [◆ ](#gac344111e2b043cdfbcb9ac272622b16f)MEDIA\_PROXY\_PLAYING\_ORDER\_NEWEST\_ONCE

| #define MEDIA\_PROXY\_PLAYING\_ORDER\_NEWEST\_ONCE   0x07 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

The tracks within a group are played once only from the newest first.

## [◆ ](#gaf10b815dc579dc67b1f092e0a85c51d9)MEDIA\_PROXY\_PLAYING\_ORDER\_NEWEST\_REPEAT

| #define MEDIA\_PROXY\_PLAYING\_ORDER\_NEWEST\_REPEAT   0x08 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

The tracks within a group are played from the newest first repeatedly.

## [◆ ](#ga48a33dd8fbb8a8ab162c18bc0e9b7531)MEDIA\_PROXY\_PLAYING\_ORDER\_OLDEST\_ONCE

| #define MEDIA\_PROXY\_PLAYING\_ORDER\_OLDEST\_ONCE   0x05 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

The tracks within a group are played once only from the oldest first.

## [◆ ](#ga63a33c4e3267ab39ab5892fb5b0bbe89)MEDIA\_PROXY\_PLAYING\_ORDER\_OLDEST\_REPEAT

| #define MEDIA\_PROXY\_PLAYING\_ORDER\_OLDEST\_REPEAT   0x06 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

The tracks within a group are played from the oldest first repeatedly.

## [◆ ](#gae152374af5d567cf65d6d7b236b792a4)MEDIA\_PROXY\_PLAYING\_ORDER\_SHUFFLE\_ONCE

| #define MEDIA\_PROXY\_PLAYING\_ORDER\_SHUFFLE\_ONCE   0x09 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

The tracks within a group are played in random order once.

## [◆ ](#ga45161ec08b67e4d3bd59efa45027f3aa)MEDIA\_PROXY\_PLAYING\_ORDER\_SHUFFLE\_REPEAT

| #define MEDIA\_PROXY\_PLAYING\_ORDER\_SHUFFLE\_REPEAT   0x0a |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

The tracks within a group are played in random order repeatedly.

## [◆ ](#ga8e721b49c361d2395bd8eb740d43e282)MEDIA\_PROXY\_PLAYING\_ORDER\_SINGLE\_ONCE

| #define MEDIA\_PROXY\_PLAYING\_ORDER\_SINGLE\_ONCE   0x01 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

A single track is played once; there is no next track.

## [◆ ](#gadf5f0c15cb88cd92f49db1b57dbd2c18)MEDIA\_PROXY\_PLAYING\_ORDER\_SINGLE\_REPEAT

| #define MEDIA\_PROXY\_PLAYING\_ORDER\_SINGLE\_REPEAT   0x02 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

A single track is played repeatedly; the next track is the current track.

## [◆ ](#ga8fee464b8e17fffc4361972df15062af)MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_INORDER\_ONCE

| #define MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_INORDER\_ONCE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

The tracks within a group are played once in track order.

## [◆ ](#ga7faeff14de245ea670ca447b0adc4820)MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_INORDER\_REPEAT

| #define MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_INORDER\_REPEAT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

The tracks within a group are played in track order repeatedly.

## [◆ ](#ga334f9e16ea7a52bfb6357ad619e3601b)MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_NEWEST\_ONCE

| #define MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_NEWEST\_ONCE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

The tracks within a group are played once only from the newest first.

## [◆ ](#gaaf5f08e2dd624e2bb1bd9b72ab4b2b33)MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_NEWEST\_REPEAT

| #define MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_NEWEST\_REPEAT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

The tracks within a group are played from the newest first repeatedly.

## [◆ ](#gae3d848fc0b9117fe9bc51327627ac635)MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_OLDEST\_ONCE

| #define MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_OLDEST\_ONCE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

The tracks within a group are played once only from the oldest first.

## [◆ ](#ga7fa415d845dd1fefc8bdb74532878131)MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_OLDEST\_REPEAT

| #define MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_OLDEST\_REPEAT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

The tracks within a group are played from the oldest first repeatedly.

## [◆ ](#ga3e998cda3e91f1c9fbb8496a748bcf12)MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_SHUFFLE\_ONCE

| #define MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_SHUFFLE\_ONCE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

The tracks within a group are played in random order once.

## [◆ ](#ga4f0689fe1fc0ac2b3f9b9ef4ed1afb8b)MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_SHUFFLE\_REPEAT

| #define MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_SHUFFLE\_REPEAT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

The tracks within a group are played in random order repeatedly.

## [◆ ](#ga55b5a00ea9ec849e7c495463e5f1869d)MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_SINGLE\_ONCE

| #define MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_SINGLE\_ONCE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

A single track is played once; there is no next track.

## [◆ ](#ga465a82ace21a0e88356eccaf038f58e9)MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_SINGLE\_REPEAT

| #define MEDIA\_PROXY\_PLAYING\_ORDERS\_SUPPORTED\_SINGLE\_REPEAT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

A single track is played repeatedly; the next track is the current track.

## [◆ ](#gaf406225a87c697d784c5a429e89d2354)MEDIA\_PROXY\_SEARCH\_FAILURE

| #define MEDIA\_PROXY\_SEARCH\_FAILURE   0x02 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Search request was invalid; no search started.

## [◆ ](#ga2627f632efab868adddeebb59243497c)MEDIA\_PROXY\_SEARCH\_SUCCESS

| #define MEDIA\_PROXY\_SEARCH\_SUCCESS   0x01 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Search request was accepted; search has started.

## [◆ ](#ga1f0fb19dea467e90afd670ed9af0c092)MEDIA\_PROXY\_SEARCH\_TYPE\_ALBUM\_NAME

| #define MEDIA\_PROXY\_SEARCH\_TYPE\_ALBUM\_NAME   0x03 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Search for Album Name.

## [◆ ](#gaf0dbc19f843a444076d8886b1a05709b)MEDIA\_PROXY\_SEARCH\_TYPE\_ARTIST\_NAME

| #define MEDIA\_PROXY\_SEARCH\_TYPE\_ARTIST\_NAME   0x02 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Search for Artist Name.

## [◆ ](#ga28b1d7de2174e3714786cb369232f339)MEDIA\_PROXY\_SEARCH\_TYPE\_EARLIEST\_YEAR

| #define MEDIA\_PROXY\_SEARCH\_TYPE\_EARLIEST\_YEAR   0x05 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Search for Earliest Year.

## [◆ ](#ga55c3a003881a75ce964e23fc3b0cea8e)MEDIA\_PROXY\_SEARCH\_TYPE\_GENRE

| #define MEDIA\_PROXY\_SEARCH\_TYPE\_GENRE   0x07 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Search for Genre.

## [◆ ](#gaca10de7253c1cdcf5e0c6544de33c116)MEDIA\_PROXY\_SEARCH\_TYPE\_GROUP\_NAME

| #define MEDIA\_PROXY\_SEARCH\_TYPE\_GROUP\_NAME   0x04 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Search for Group Name.

## [◆ ](#ga01fb087af00bf492d19cc19adcaa9dea)MEDIA\_PROXY\_SEARCH\_TYPE\_LATEST\_YEAR

| #define MEDIA\_PROXY\_SEARCH\_TYPE\_LATEST\_YEAR   0x06 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Search for Latest Year.

## [◆ ](#ga25270f6c90daaace6a80f3255aaaf7fd)MEDIA\_PROXY\_SEARCH\_TYPE\_ONLY\_GROUPS

| #define MEDIA\_PROXY\_SEARCH\_TYPE\_ONLY\_GROUPS   0x09 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Search for Groups only.

## [◆ ](#gad758e14fbe978ffd95364a6fb27eab40)MEDIA\_PROXY\_SEARCH\_TYPE\_ONLY\_TRACKS

| #define MEDIA\_PROXY\_SEARCH\_TYPE\_ONLY\_TRACKS   0x08 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Search for Tracks only.

## [◆ ](#ga8be6fd8d9bb08836bea1c3f0d2e577ea)MEDIA\_PROXY\_SEARCH\_TYPE\_TRACK\_NAME

| #define MEDIA\_PROXY\_SEARCH\_TYPE\_TRACK\_NAME   0x01 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Search for Track Name.

## [◆ ](#gaa6aa7a6e98631152b4bd77b60c78d58a)MEDIA\_PROXY\_SEEKING\_SPEED\_FACTOR\_MAX

| #define MEDIA\_PROXY\_SEEKING\_SPEED\_FACTOR\_MAX   64 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Maximum seeking speed - Can be negated.

## [◆ ](#ga67c1069fa01425ad6cd8f36438b71826)MEDIA\_PROXY\_SEEKING\_SPEED\_FACTOR\_MIN

| #define MEDIA\_PROXY\_SEEKING\_SPEED\_FACTOR\_MIN   4 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Minimum seeking speed - Can be negated.

## [◆ ](#ga58495e58bf84235efcee89289fc992c2)MEDIA\_PROXY\_SEEKING\_SPEED\_FACTOR\_ZERO

| #define MEDIA\_PROXY\_SEEKING\_SPEED\_FACTOR\_ZERO   0 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

No seeking.

## [◆ ](#gab8c465e0e63898e53c39171b89d668c9)MEDIA\_PROXY\_STATE\_INACTIVE

| #define MEDIA\_PROXY\_STATE\_INACTIVE   0x00 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

The current track is invalid, and no track has been selected.

## [◆ ](#gab0c8f3510109f18ef6445f035b27cbe9)MEDIA\_PROXY\_STATE\_LAST

| #define MEDIA\_PROXY\_STATE\_LAST   0x04 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Used internally as the last state value.

## [◆ ](#ga85325d7ff75ec05275a875d7d5540a6c)MEDIA\_PROXY\_STATE\_PAUSED

| #define MEDIA\_PROXY\_STATE\_PAUSED   0x02 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

The current track is paused.

The media player has a current track, but it is not being played

## [◆ ](#ga1967c76b290f1d20515740cf7139f49c)MEDIA\_PROXY\_STATE\_PLAYING

| #define MEDIA\_PROXY\_STATE\_PLAYING   0x01 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

The media player is playing the current track.

## [◆ ](#gaa207ee7666ab18c40e5b1d2a6ed7f034)MEDIA\_PROXY\_STATE\_SEEKING

| #define MEDIA\_PROXY\_STATE\_SEEKING   0x03 |
| --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

The current track is fast forwarding or fast rewinding.

## Function Documentation

## [◆ ](#gaf535f1ab028407432ef890d278d936e0)bt\_mcs\_get\_ots()

| struct bt\_ots \* bt\_mcs\_get\_ots | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Get the pointer of the Object Transfer Service used by the Media Control Service.

TODO: Find best location for this call, and move this one also

## [◆ ](#ga5aaa486e0c3663e21477984e54642ed1)media\_proxy\_ctrl\_discover\_player()

| int media\_proxy\_ctrl\_discover\_player | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Discover a remote media player.

Discover a remote media player instance. The remote player instance will be discovered, and accessed, using Bluetooth, via the media control client and a remote media control service. This call will start a GATT discovery of the Media Control Service on the peer, and setup handles and subscriptions.

This shall be called once before any other actions can be executed for the remote player. The remote player instance will be returned in the discover\_player() callback.

Parameters
:   | conn | The connection to do discovery for |
    | --- | --- |

Returns
:   0 if success, errno on failure

## [◆ ](#ga15804287093b20d4a1616380729b33c8)media\_proxy\_ctrl\_get\_commands\_supported()

| int media\_proxy\_ctrl\_get\_commands\_supported | ( | struct media\_player \* | *player* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Read Commands Supported.

Read a bitmap containing the media player's supported command opcodes.

Parameters
:   | player | Media player instance pointer |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga23488e77985a04216ec7c7fa785f09fc)media\_proxy\_ctrl\_get\_content\_ctrl\_id()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) media\_proxy\_ctrl\_get\_content\_ctrl\_id | ( | struct media\_player \* | *player* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Read Content Control ID.

The content control ID identifies a content control service on a device, and links it to the corresponding audio stream.

Parameters
:   | player | Media player instance pointer |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga2ae50a1988305b4247ff0af796b6d93e)media\_proxy\_ctrl\_get\_current\_group\_id()

| int media\_proxy\_ctrl\_get\_current\_group\_id | ( | struct media\_player \* | *player* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Read Current Group Object ID.

Get an ID (48 bit) that can be used to retrieve the Current Track Object from an Object Transfer Service

See the Media Control Service spec v1.0 sections 3.14 and 4.4 for a description of the Current Group Object.

Requires Object Transfer Service

Parameters
:   | player | Media player instance pointer |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#gaebe7e3683041e28bef40df75cc991dea)media\_proxy\_ctrl\_get\_current\_track\_id()

| int media\_proxy\_ctrl\_get\_current\_track\_id | ( | struct media\_player \* | *player* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Read Current Track Object ID.

Get an ID (48 bit) that can be used to retrieve the Current Track Object from an Object Transfer Service

See the Media Control Service spec v1.0 sections 3.11 and 4.3 for a description of the Current Track Object.

Requires Object Transfer Service

Parameters
:   | player | Media player instance pointer |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga5efccb39cdb97eed476e0c0bff461ec1)media\_proxy\_ctrl\_get\_icon\_id()

| int media\_proxy\_ctrl\_get\_icon\_id | ( | struct media\_player \* | *player* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Read Icon Object ID.

Get an ID (48 bit) that can be used to retrieve the Icon Object from an Object Transfer Service

See the Media Control Service spec v1.0 sections 3.2 and 4.1 for a description of the Icon Object.

Requires Object Transfer Service

Parameters
:   | player | Media player instance pointer |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#gab6df6fe71c8273eca855eb3be27290dd)media\_proxy\_ctrl\_get\_icon\_url()

| int media\_proxy\_ctrl\_get\_icon\_url | ( | struct media\_player \* | *player* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Read Icon URL.

Get a URL to the media player's icon.

Parameters
:   | player | Media player instance pointer |
    | --- | --- |

## [◆ ](#ga9433aaf24776c30557ea694795e75b3e)media\_proxy\_ctrl\_get\_media\_state()

| int media\_proxy\_ctrl\_get\_media\_state | ( | struct media\_player \* | *player* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Read Media State.

Read the media player's state

Parameters
:   | player | Media player instance pointer |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#gae32da32bd504061801730805729242e1)media\_proxy\_ctrl\_get\_next\_track\_id()

| int media\_proxy\_ctrl\_get\_next\_track\_id | ( | struct media\_player \* | *player* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Read Next Track Object ID.

Get an ID (48 bit) that can be used to retrieve the Next Track Object from an Object Transfer Service

Requires Object Transfer Service

Parameters
:   | player | Media player instance pointer |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga12dc878be39814660900ba875e13e537)media\_proxy\_ctrl\_get\_parent\_group\_id()

| int media\_proxy\_ctrl\_get\_parent\_group\_id | ( | struct media\_player \* | *player* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Read Parent Group Object ID.

Get an ID (48 bit) that can be used to retrieve the Parent Track Object from an Object Transfer Service

The parent group is the parent of the current group.

See the Media Control Service spec v1.0 sections 3.14 and 4.4 for a description of the Current Track Object.

Requires Object Transfer Service

Parameters
:   | player | Media player instance pointer |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga2d64a23b3f881579a603a04baeb64088)media\_proxy\_ctrl\_get\_playback\_speed()

| int media\_proxy\_ctrl\_get\_playback\_speed | ( | struct media\_player \* | *player* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Get Playback Speed.

The playback speed parameter is related to the actual playback speed as follows: actual playback speed = 2^(speed\_parameter/64)

A speed parameter of 0 corresponds to unity speed playback (i.e. playback at "normal" speed). A speed parameter of -128 corresponds to playback at one fourth of normal speed, 127 corresponds to playback at almost four times the normal speed.

Parameters
:   | player | Media player instance pointer |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga2261222d8581ed86e91a276b13359126)media\_proxy\_ctrl\_get\_player\_name()

| int media\_proxy\_ctrl\_get\_player\_name | ( | struct media\_player \* | *player* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Read Media Player Name.

Parameters
:   | player | Media player instance pointer |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga2f93bcde2460c6638880f8e6631eb68e)media\_proxy\_ctrl\_get\_playing\_order()

| int media\_proxy\_ctrl\_get\_playing\_order | ( | struct media\_player \* | *player* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Read Playing Order.

Parameters
:   | player | Media player instance pointer |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga030899757b79251f1d5a1055f65fe989)media\_proxy\_ctrl\_get\_playing\_orders\_supported()

| int media\_proxy\_ctrl\_get\_playing\_orders\_supported | ( | struct media\_player \* | *player* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Read Playing Orders Supported.

Read a bitmap containing the media player's supported playing orders.

Parameters
:   | player | Media player instance pointer |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga580a0c9fa47460be59f0571ee11a41b4)media\_proxy\_ctrl\_get\_search\_results\_id()

| int media\_proxy\_ctrl\_get\_search\_results\_id | ( | struct media\_player \* | *player* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Read Search Results Object ID.

Get an ID (48 bit) that can be used to retrieve the Search Results Object from an Object Transfer Service

The search results object is a group object. The search results object only exists if a successful search operation has been done.

Requires Object Transfer Service

Parameters
:   | player | Media player instance pointer |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga817ca4ab611e214493fbc918036def0f)media\_proxy\_ctrl\_get\_seeking\_speed()

| int media\_proxy\_ctrl\_get\_seeking\_speed | ( | struct media\_player \* | *player* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Get Seeking Speed.

The seeking speed gives the speed with which the player is seeking. It is a factor, relative to real-time playback speed - a factor four means seeking happens at four times the real-time playback speed. Positive values are for forward seeking, negative values for backwards seeking.

The seeking speed is not settable - a non-zero seeking speed is the result of "fast rewind" of "fast forward" commands.

Parameters
:   | player | Media player instance pointer |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga488441418a8f2d358092019bbfe16788)media\_proxy\_ctrl\_get\_track\_duration()

| int media\_proxy\_ctrl\_get\_track\_duration | ( | struct media\_player \* | *player* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Read Track Duration.

The duration of a track is measured in hundredths of a second.

Parameters
:   | player | Media player instance pointer |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#gae0bb75feb49a68b495150c6fba2f21a7)media\_proxy\_ctrl\_get\_track\_position()

| int media\_proxy\_ctrl\_get\_track\_position | ( | struct media\_player \* | *player* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Read Track Position.

The position of the player (the playing position) is measured in hundredths of a second from the beginning of the track

Parameters
:   | player | Media player instance pointer |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga1afcc097cb36c4f11141b82ce28e8126)media\_proxy\_ctrl\_get\_track\_segments\_id()

| int media\_proxy\_ctrl\_get\_track\_segments\_id | ( | struct media\_player \* | *player* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Read Current Track Segments Object ID.

Get an ID (48 bit) that can be used to retrieve the Current Track Segments Object from an Object Transfer Service

See the Media Control Service spec v1.0 sections 3.10 and 4.2 for a description of the Track Segments Object.

Requires Object Transfer Service

Parameters
:   | player | Media player instance pointer |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#gabfbb49e79204130cb004f217af771b80)media\_proxy\_ctrl\_get\_track\_title()

| int media\_proxy\_ctrl\_get\_track\_title | ( | struct media\_player \* | *player* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Read Track Title.

Parameters
:   | player | Media player instance pointer |
    | --- | --- |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga352228fb77498b61205a22b0f3a75c8e)media\_proxy\_ctrl\_register()

| int media\_proxy\_ctrl\_register | ( | struct [media\_proxy\_ctrl\_cbs](structmedia__proxy__ctrl__cbs.md) \* | *ctrl\_cbs* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Register a controller with the media\_proxy.

Parameters
:   | ctrl\_cbs | Callbacks to the controller |
    | --- | --- |

Returns
:   0 if success, errno on failure

## [◆ ](#ga590762e7272b99fb8ac50a7841424670)media\_proxy\_ctrl\_send\_command()

| int media\_proxy\_ctrl\_send\_command | ( | struct media\_player \* | *player*, |
| --- | --- | --- | --- |
|  |  | const struct [mpl\_cmd](structmpl__cmd.md) \* | *command* ) |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Send Command.

Send a command to the media player. Commands may cause the media player to change its state May result in two callbacks - one for the actual sending of the command to the player, one for the result of the command from the player.

Parameters
:   | player | Media player instance pointer |
    | --- | --- |
    | command | The command to send |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga052c3fabac4a44ee2802ddd4a6c5c9ac)media\_proxy\_ctrl\_send\_search()

| int media\_proxy\_ctrl\_send\_search | ( | struct media\_player \* | *player*, |
| --- | --- | --- | --- |
|  |  | const struct [mpl\_search](structmpl__search.md) \* | *search* ) |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Set Search.

Write a search to the media player. If the search is successful, the search results will be available as a group object in the Object Transfer Service (OTS).

May result in up to three callbacks

- one for the actual sending of the search to the player
- one for the result code for the search from the player
- if the search is successful, one for the search results object ID in the OTs

Requires Object Transfer Service

Parameters
:   | player | Media player instance pointer |
    | --- | --- |
    | search | The search to write |

Returns
:   0 if success, errno on failure.

## [◆ ](#gae496885d0124f4e3fc2c0f203fcff118)media\_proxy\_ctrl\_set\_current\_group\_id()

| int media\_proxy\_ctrl\_set\_current\_group\_id | ( | struct media\_player \* | *player*, |
| --- | --- | --- | --- |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *id* ) |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Set Current Group Object ID.

Change the player's current group to the group given by the ID, and the current track to the first track in that group.

Requires Object Transfer Service

Parameters
:   | player | Media player instance pointer |
    | --- | --- |
    | id | The ID of a group object |

Returns
:   0 if success, errno on failure.

## [◆ ](#gaea6adacedaded10f7c2c0f91b7159f74)media\_proxy\_ctrl\_set\_current\_track\_id()

| int media\_proxy\_ctrl\_set\_current\_track\_id | ( | struct media\_player \* | *player*, |
| --- | --- | --- | --- |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *id* ) |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Set Current Track Object ID.

Change the player's current track to the track given by the ID. (Behaves similarly to the goto track command.)

Requires Object Transfer Service

Parameters
:   | player | Media player instance pointer |
    | --- | --- |
    | id | The ID of a track object |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga43b797717fb9b36b94a606dfabeb0fa7)media\_proxy\_ctrl\_set\_next\_track\_id()

| int media\_proxy\_ctrl\_set\_next\_track\_id | ( | struct media\_player \* | *player*, |
| --- | --- | --- | --- |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *id* ) |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Set Next Track Object ID.

Change the player's next track to the track given by the ID.

Requires Object Transfer Service

Parameters
:   | player | Media player instance pointer |
    | --- | --- |
    | id | The ID of a track object |

Returns
:   0 if success, errno on failure.

## [◆ ](#gabafbc857c3e6befe98e339acb58f17fb)media\_proxy\_ctrl\_set\_playback\_speed()

| int media\_proxy\_ctrl\_set\_playback\_speed | ( | struct media\_player \* | *player*, |
| --- | --- | --- | --- |
|  |  | [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | *speed* ) |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Set Playback Speed.

See the get\_playback\_speed() function for an explanation of the playback speed parameter.

Note that the media player may not support all possible values of the playback speed parameter. If the value given is not supported, and is higher than the current value, the player should set the playback speed to the next higher supported value. (And correspondingly to the next lower supported value for given values lower than the current value.)

Parameters
:   | player | Media player instance pointer |
    | --- | --- |
    | speed | The playback speed parameter to set |

Returns
:   0 if success, errno on failure.

## [◆ ](#gaa4040e97100f6e70527e6ad201309bbe)media\_proxy\_ctrl\_set\_playing\_order()

| int media\_proxy\_ctrl\_set\_playing\_order | ( | struct media\_player \* | *player*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *order* ) |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Set Playing Order.

Set the media player's playing order

Parameters
:   | player | Media player instance pointer |
    | --- | --- |
    | order | The playing order to set |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga776bb5f16cf1f4f6cc3842aabd86b781)media\_proxy\_ctrl\_set\_track\_position()

| int media\_proxy\_ctrl\_set\_track\_position | ( | struct media\_player \* | *player*, |
| --- | --- | --- | --- |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *position* ) |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Set Track Position.

Set the playing position of the media player in the current track. The position is given in hundredths of a second, from the beginning of the track of the track for positive values, and (backwards) from the end of the track for negative values.

Parameters
:   | player | Media player instance pointer |
    | --- | --- |
    | position | The track position to set |

Returns
:   0 if success, errno on failure.

## [◆ ](#ga694e83401835149833024cf094b98cd1)media\_proxy\_pl\_command\_cb()

| void media\_proxy\_pl\_command\_cb | ( | const struct [mpl\_cmd\_ntf](structmpl__cmd__ntf.md) \* | *cmd\_ntf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Command callback.

To be called when a command has been sent, to notify whether the command was successfully performed or not. See the MEDIA\_PROXY\_CMD\_\* result code defines.

Parameters
:   | cmd\_ntf | The result of the command |
    | --- | --- |

## [◆ ](#ga70ea8a24a4e853a191e0947e1c2d1145)media\_proxy\_pl\_commands\_supported\_cb()

| void media\_proxy\_pl\_commands\_supported\_cb | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *opcodes* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Commands supported callback.

To be called when the set of commands supported is changed

Parameters
:   | opcodes | The supported commands opcodes |
    | --- | --- |

## [◆ ](#gad02f2924e1aa765c04cbbc6441e7d063)media\_proxy\_pl\_current\_group\_id\_cb()

| void media\_proxy\_pl\_current\_group\_id\_cb | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Current group object ID callback.

To be called when the ID of the current group is changed

Parameters
:   | id | The ID of the current group object in the OTS |
    | --- | --- |

## [◆ ](#gadcad4efdd714159d5d9611bbf74d5fae)media\_proxy\_pl\_current\_track\_id\_cb()

| void media\_proxy\_pl\_current\_track\_id\_cb | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Current track object ID callback.

To be called when the ID of the current track is changed (e.g. due to a track change).

Parameters
:   | id | The ID of the current track object in the OTS |
    | --- | --- |

## [◆ ](#gadd348a8d5aff193f7a9113a759e85b1d)media\_proxy\_pl\_icon\_url\_cb()

| void media\_proxy\_pl\_icon\_url\_cb | ( | const char \* | *url* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Player icon URL changed callback.

To be called when the player's icon URL is changed.

Parameters
:   | url | The URL of the player's icon |
    | --- | --- |

## [◆ ](#gab0b10b3de5674f2172e1a2f779cbe8d5)media\_proxy\_pl\_init()

| int media\_proxy\_pl\_init | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Initialize player.

TODO: Move to player header file

## [◆ ](#ga842d7951a04702d6f819de44c47b9cac)media\_proxy\_pl\_media\_state\_cb()

| void media\_proxy\_pl\_media\_state\_cb | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *state* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Media state callback.

To be called when the media state is changed

Parameters
:   | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | The media player's state |
    | --- | --- |

## [◆ ](#ga0a70dc60a4d6acbcc58e220b75dad92a)media\_proxy\_pl\_name\_cb()

| void media\_proxy\_pl\_name\_cb | ( | const char \* | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Player name changed callback.

To be called when the player's name is changed.

Parameters
:   | name | The name of the player |
    | --- | --- |

## [◆ ](#gaf0bd3447e64b6128710c07461766a0c9)media\_proxy\_pl\_next\_track\_id\_cb()

| void media\_proxy\_pl\_next\_track\_id\_cb | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Next track object ID callback.

To be called when the ID of the current track is changes

Parameters
:   | id | The ID of the next track object in the OTS |
    | --- | --- |

## [◆ ](#ga64730f46b87cf9089aff65b6be12f42d)media\_proxy\_pl\_parent\_group\_id\_cb()

| void media\_proxy\_pl\_parent\_group\_id\_cb | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Parent group object ID callback.

To be called when the ID of the parent group is changed

Parameters
:   | id | The ID of the parent group object in the OTS |
    | --- | --- |

## [◆ ](#ga17c2ca149050e1382eb556f6dcccad21)media\_proxy\_pl\_playback\_speed\_cb()

| void media\_proxy\_pl\_playback\_speed\_cb | ( | [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | *speed* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Playback speed callback.

To be called when the playback speed is changed.

Parameters
:   | speed | The playback speed parameter |
    | --- | --- |

## [◆ ](#ga96e8156b0267f3d55ee52ab307d81985)media\_proxy\_pl\_playing\_order\_cb()

| void media\_proxy\_pl\_playing\_order\_cb | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *order* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Playing order callback.

To be called when the playing order is changed

Parameters
:   | order | The playing order |
    | --- | --- |

## [◆ ](#gac75e27a4a5e169481723cd6b39678274)media\_proxy\_pl\_register()

| int media\_proxy\_pl\_register | ( | struct [media\_proxy\_pl\_calls](structmedia__proxy__pl__calls.md) \* | *pl\_calls* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Register a player with the media proxy.

Register a player with the media proxy module, for use by media controllers.

The media proxy may call any non-NULL function pointers in the supplied [media\_proxy\_pl\_calls](structmedia__proxy__pl__calls.md "Available calls in a player, that the media proxy can call.") structure.

Parameters
:   | pl\_calls | Function pointers to the media player's calls |
    | --- | --- |

Returns
:   0 if success, errno on failure

## [◆ ](#ga8c0d75f61120047bacd0b933534e1b41)media\_proxy\_pl\_search\_cb()

| void media\_proxy\_pl\_search\_cb | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *result\_code* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Search callback.

To be called when a search has been set to notify whether the search was successfully performed or not. See the MEDIA\_PROXY\_SEARCH\_\* result code defines.

The actual results of the search, if successful, can be found in the search results object.

Parameters
:   | result\_code | The result (success or failure) of the search |
    | --- | --- |

## [◆ ](#ga35896de266f2a2bd101279e4ce9900c7)media\_proxy\_pl\_search\_results\_id\_cb()

| void media\_proxy\_pl\_search\_results\_id\_cb | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Search Results object ID callback.

To be called when the ID of the search results is changed (typically as the result of a new successful search).

Parameters
:   | id | The ID of the search results object in the OTS |
    | --- | --- |

## [◆ ](#gaeaf89f4b760870896ed42687562971ca)media\_proxy\_pl\_seeking\_speed\_cb()

| void media\_proxy\_pl\_seeking\_speed\_cb | ( | [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | *speed* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Seeking speed callback.

To be called when the seeking speed is changed.

Parameters
:   | speed | The seeking speed factor |
    | --- | --- |

## [◆ ](#ga4a93a18cb0b75cb16828243f0d37b4b4)media\_proxy\_pl\_track\_changed\_cb()

| void media\_proxy\_pl\_track\_changed\_cb | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Track changed callback.

To be called when the player's current track is changed

## [◆ ](#ga7b0f9633a5322557b91ea97eafac9f34)media\_proxy\_pl\_track\_duration\_cb()

| void media\_proxy\_pl\_track\_duration\_cb | ( | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *duration* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Track duration callback.

To be called when the current track's duration is changed (e.g. due to a track change)

The track duration is given in hundredths of a second.

Parameters
:   | duration | The track duration |
    | --- | --- |

## [◆ ](#ga61d494d7e149cfa2c3f9546c1e3b99bd)media\_proxy\_pl\_track\_position\_cb()

| void media\_proxy\_pl\_track\_position\_cb | ( | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *position* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Track position callback.

To be called when the media player's position in the track is changed, or when the player is paused or similar.

Exception: This callback should not be called when the position changes during regular playback, i.e. while the player is playing and playback happens at a constant speed.

The track position is given in hundredths of a second from the start of the track.

Parameters
:   | position | The media player's position in the track |
    | --- | --- |

## [◆ ](#ga9489b517e4baa215f0b7b59243cee11c)media\_proxy\_pl\_track\_title\_cb()

| void media\_proxy\_pl\_track\_title\_cb | ( | char \* | *title* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[media_proxy.h](media__proxy_8h.md)>`

Track title callback.

To be called when the player's current track is changed

Parameters
:   | title | The title of the track |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
