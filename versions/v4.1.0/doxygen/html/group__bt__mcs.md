---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__bt__mcs.html
original_path: doxygen/html/group__bt__mcs.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Media Control Service (MCS)

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

Media Control Service (MCS).
[More...](#details)

| Macros | |
| --- | --- |
| #define | [BT\_MCS\_ERR\_LONG\_VAL\_CHANGED](#gab0c40404b2cd37d0a729504aa270e697)   0x80 |
|  | A characteristic value has changed while a Read Long Value Characteristic sub-procedure is in progress. |
| #define | [BT\_MCS\_OPCODES\_SUPPORTED\_LEN](#ga4ae0b32e4192ba36b3ad4d6d8354929a)   4 |
|  | Media control point supported opcodes length. |
| #define | [SEARCH\_LEN\_MIN](#gaff47bc210fdd2d4d80a0ce822ca29a67)   2 |
|  | Search control point minimum length. |
| #define | [SEARCH\_LEN\_MAX](#gaf771b17acd202a20450b6ea939ddee3b)   64 |
|  | Search control point maximum length. |
| #define | [SEARCH\_SCI\_LEN\_MIN](#gab1fad64b6a1edfefce90cd4692576a5d) |
|  | Search control point item (SCI) minimum length. |
| #define | [SEARCH\_PARAM\_MAX](#ga81665fd87487cbaf1c0f90f1e0b2126a)   62 |
|  | Search parameters maximum length. |

| Playback speeds | |
| --- | --- |
| The playback speed (s) is calculated by the value of 2 to the power of p divided by 64.  All values from -128 to 127 allowed, only some examples defined. | |
| #define | [BT\_MCS\_PLAYBACK\_SPEED\_MIN](#ga5d450ac222a491b7d544cc4d3f3ffcf0)   -128 |
|  | Minimum playback speed, resulting in 25 % speed. |
| #define | [BT\_MCS\_PLAYBACK\_SPEED\_QUARTER](#ga90e55b0230a11f752b111750e94ace4c)   -128 |
|  | Quarter playback speed, resulting in 25 % speed. |
| #define | [BT\_MCS\_PLAYBACK\_SPEED\_HALF](#ga3bff45add6fbf602ad6bb07b0e64b335)   -64 |
|  | Half playback speed, resulting in 50 % speed. |
| #define | [BT\_MCS\_PLAYBACK\_SPEED\_UNITY](#ga68c0eaa632ca581a1ab5ab144b3d7693)   0 |
|  | Unity playback speed, resulting in 100 % speed. |
| #define | [BT\_MCS\_PLAYBACK\_SPEED\_DOUBLE](#ga05ec8bf9ae813c8a3755b1383030bdf0)   64 |
|  | Double playback speed, resulting in 200 % speed. |
| #define | [BT\_MCS\_PLAYBACK\_SPEED\_MAX](#gaa3299c597471a809033ec45b2c6f5b3d)   127 |
|  | Max playback speed, resulting in 395.7 % speed (nearly 400 %). |

| Seeking speed | |
| --- | --- |
| The allowed values for seeking speed are the range -64 to -4 (endpoints included), the value 0, and the range 4 to 64 (endpoints included). | |
| #define | [BT\_MCS\_SEEKING\_SPEED\_FACTOR\_MAX](#ga22c0b457d8c6e9ec119fff38205786d3)   64 |
|  | Maximum seeking speed - Can be negated. |
| #define | [BT\_MCS\_SEEKING\_SPEED\_FACTOR\_MIN](#gaf912dcbc70c81a023f8b93a4d4b0e745)   4 |
|  | Minimum seeking speed - Can be negated. |
| #define | [BT\_MCS\_SEEKING\_SPEED\_FACTOR\_ZERO](#ga16bdf755d07c99895fa8698f9bd637a0)   0 |
|  | No seeking. |

| Playing orders | |
| --- | --- |
| #define | [BT\_MCS\_PLAYING\_ORDER\_SINGLE\_ONCE](#ga1c25a91795472a553286def379fe943b)   0X01 |
|  | A single track is played once; there is no next track. |
| #define | [BT\_MCS\_PLAYING\_ORDER\_SINGLE\_REPEAT](#ga4698529b5268ff1c5099f4cc9d8e9966)   0x02 |
|  | A single track is played repeatedly; the next track is the current track. |
| #define | [BT\_MCS\_PLAYING\_ORDER\_INORDER\_ONCE](#ga8b8023d46c3ce402a07c9146494ada60)   0x03 |
|  | The tracks within a group are played once in track order. |
| #define | [BT\_MCS\_PLAYING\_ORDER\_INORDER\_REPEAT](#gaaccf440eb5df01eaa0a255e09cf7b996)   0x04 |
|  | The tracks within a group are played in track order repeatedly. |
| #define | [BT\_MCS\_PLAYING\_ORDER\_OLDEST\_ONCE](#ga260b73c14b35ee596cacca082b5dc865)   0x05 |
|  | The tracks within a group are played once only from the oldest first. |
| #define | [BT\_MCS\_PLAYING\_ORDER\_OLDEST\_REPEAT](#ga2fb92d553aed2f680321db68ef28035f)   0x06 |
|  | The tracks within a group are played from the oldest first repeatedly. |
| #define | [BT\_MCS\_PLAYING\_ORDER\_NEWEST\_ONCE](#gaaa06525a5d53d4bf2312304208dda311)   0x07 |
|  | The tracks within a group are played once only from the newest first. |
| #define | [BT\_MCS\_PLAYING\_ORDER\_NEWEST\_REPEAT](#ga28a19c78f96b51f0e048395eb4378d61)   0x08 |
|  | The tracks within a group are played from the newest first repeatedly. |
| #define | [BT\_MCS\_PLAYING\_ORDER\_SHUFFLE\_ONCE](#gaa33a02e34f65021b1b7290edc76b166e)   0x09 |
|  | The tracks within a group are played in random order once. |
| #define | [BT\_MCS\_PLAYING\_ORDER\_SHUFFLE\_REPEAT](#gaa231c007f0448a5ba3bd61e8528c5b1e)   0x0a |
|  | The tracks within a group are played in random order repeatedly. |

| Playing orders supported | |
| --- | --- |
| A bitmap, in the same order as the playing orders above.  Note that playing order 1 corresponds to bit 0, and so on. | |
| #define | [BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_SINGLE\_ONCE](#ga7102f1909baea2320827ea6b47522bd8)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | A single track is played once; there is no next track. |
| #define | [BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_SINGLE\_REPEAT](#gafecb7edde06dfb97939af93034690cbc)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | A single track is played repeatedly; the next track is the current track. |
| #define | [BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_INORDER\_ONCE](#ga594daa869c6696a4cdd961f8786134a6)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | The tracks within a group are played once in track order. |
| #define | [BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_INORDER\_REPEAT](#gac4bcd9b84e28a47dd23d073dd942a9c8)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | The tracks within a group are played in track order repeatedly. |
| #define | [BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_OLDEST\_ONCE](#gae1d8c34c8f9ea9fadc4da56d0d127712)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | The tracks within a group are played once only from the oldest first. |
| #define | [BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_OLDEST\_REPEAT](#ga38bb3aa9a388fa3ae0230cb78cf2d3a5)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | The tracks within a group are played from the oldest first repeatedly. |
| #define | [BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_NEWEST\_ONCE](#gabd77af4da60d1b7531d35bd543cb4df2)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | The tracks within a group are played once only from the newest first. |
| #define | [BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_NEWEST\_REPEAT](#ga9bb22c2c7d08032ab1d5c3ae64ce01a8)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
|  | The tracks within a group are played from the newest first repeatedly. |
| #define | [BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_SHUFFLE\_ONCE](#ga2c245ad4f76937b366770aa7afe7b684)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
|  | The tracks within a group are played in random order once. |
| #define | [BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_SHUFFLE\_REPEAT](#gae5d972a834c1b568f39df91df0febb81)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
|  | The tracks within a group are played in random order repeatedly. |

| Media states | |
| --- | --- |
| #define | [BT\_MCS\_MEDIA\_STATE\_INACTIVE](#gaa9c7d92a8aa79b1020c8b593b0edc088)   0x00 |
|  | The current track is invalid, and no track has been selected. |
| #define | [BT\_MCS\_MEDIA\_STATE\_PLAYING](#gaa33b1ba9ebfd0d226df869cdc35e964c)   0x01 |
|  | The media player is playing the current track. |
| #define | [BT\_MCS\_MEDIA\_STATE\_PAUSED](#gaa5a2768a288fe8058818b5f965c0d8b3)   0x02 |
|  | The current track is paused. |
| #define | [BT\_MCS\_MEDIA\_STATE\_SEEKING](#ga689e83131b6db63fa3a76f428a93714b)   0x03 |
|  | The current track is fast forwarding or fast rewinding. |

| Media control point opcodes | |
| --- | --- |
| #define | [BT\_MCS\_OPC\_PLAY](#ga79c4cf8292a4548bc7b9b06b1ce0f60a)   0x01 |
|  | Start playing the current track. |
| #define | [BT\_MCS\_OPC\_PAUSE](#ga8b15cb7a8a1429f83e8d1619c37becc6)   0x02 |
|  | Pause playing the current track. |
| #define | [BT\_MCS\_OPC\_FAST\_REWIND](#ga6d49190bae54e66695ea3c856d558049)   0x03 |
|  | Fast rewind the current track. |
| #define | [BT\_MCS\_OPC\_FAST\_FORWARD](#ga9ce0d00b1cfc0d3a33762aaed3c1bb75)   0x04 |
|  | Fast forward the current track. |
| #define | [BT\_MCS\_OPC\_STOP](#gade874bf59dc08ddb682280b644821e11)   0x05 |
|  | Stop current activity and return to the paused state and set the current track position to the start of the current track. |
| #define | [BT\_MCS\_OPC\_MOVE\_RELATIVE](#gada25cc85988f5988887eab0cf66e4190)   0x10 |
|  | Set a new current track position relative to the current track position. |
| #define | [BT\_MCS\_OPC\_PREV\_SEGMENT](#ga454775706fe60ccd12e5ab44e6ddacba)   0x20 |
|  | Set the current track position to the starting position of the previous segment of the current track. |
| #define | [BT\_MCS\_OPC\_NEXT\_SEGMENT](#ga9cc7b813b933b56b1f60ef0ddf8e39df)   0x21 |
|  | Set the current track position to the starting position of the next segment of the current track. |
| #define | [BT\_MCS\_OPC\_FIRST\_SEGMENT](#ga6148011e40389bbed998a971f44f834a)   0x22 |
|  | Set the current track position to the starting position of the first segment of the current track. |
| #define | [BT\_MCS\_OPC\_LAST\_SEGMENT](#ga08421e4d26d54fe3d40edeb08fd44aac)   0x23 |
|  | Set the current track position to the starting position of the last segment of the current track. |
| #define | [BT\_MCS\_OPC\_GOTO\_SEGMENT](#ga4b91b6e3e3f92619d45ecc2066e97e74)   0x24 |
|  | Set the current track position to the starting position of the nth segment of the current track. |
| #define | [BT\_MCS\_OPC\_PREV\_TRACK](#ga88e09cd634c2dd3068f746cc978c1568)   0x30 |
|  | Set the current track to the previous track based on the playing order. |
| #define | [BT\_MCS\_OPC\_NEXT\_TRACK](#ga06df0d77c7a678ca8f4f01ec64c88de7)   0x31 |
|  | Set the current track to the next track based on the playing order. |
| #define | [BT\_MCS\_OPC\_FIRST\_TRACK](#gaed893751ae2ceae3a1d5c764b9411ecc)   0x32 |
|  | Set the current track to the first track based on the playing order. |
| #define | [BT\_MCS\_OPC\_LAST\_TRACK](#gacd2e15226d20eb65962d6441c2b7d565)   0x33 |
|  | Set the current track to the last track based on the playing order. |
| #define | [BT\_MCS\_OPC\_GOTO\_TRACK](#ga4d5124b9ffc125e31c45c06a12fcc85c)   0x34 |
|  | Set the current track to the nth track based on the playing order. |
| #define | [BT\_MCS\_OPC\_PREV\_GROUP](#gab7efc1fb17cc53c376f6f84bf31ef85c)   0x40 |
|  | Set the current group to the previous group in the sequence of groups. |
| #define | [BT\_MCS\_OPC\_NEXT\_GROUP](#ga4feb6b16975ae123bc77c08509e0c809)   0x41 |
|  | Set the current group to the next group in the sequence of groups. |
| #define | [BT\_MCS\_OPC\_FIRST\_GROUP](#ga0b6075379c9abf0911c8a1f2b8d11923)   0x42 |
|  | Set the current group to the first group in the sequence of groups. |
| #define | [BT\_MCS\_OPC\_LAST\_GROUP](#gad234093556575ac31985944a483597e8)   0x43 |
|  | Set the current group to the last group in the sequence of groups. |
| #define | [BT\_MCS\_OPC\_GOTO\_GROUP](#ga1911ae5e1285041a77bbd1db773c33b5)   0x44 |
|  | Set the current group to the nth group in the sequence of groups. |

| Media control point supported opcodes values | |
| --- | --- |
| #define | [BT\_MCS\_OPC\_SUP\_PLAY](#ga82d1bbc5cd67ab30960bca6992116a8f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Support the Play opcode. |
| #define | [BT\_MCS\_OPC\_SUP\_PAUSE](#gabdca574666b964d506d96e01562875f4)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Support the Pause opcode. |
| #define | [BT\_MCS\_OPC\_SUP\_FAST\_REWIND](#gaaa3b553dc8eb2de610b545f1ce88b067)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Support the Fast Rewind opcode. |
| #define | [BT\_MCS\_OPC\_SUP\_FAST\_FORWARD](#gaa24785ccc713cb2421a55ff48f5f2c45)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Support the Fast Forward opcode. |
| #define | [BT\_MCS\_OPC\_SUP\_STOP](#gaec507c502c53413e510cc30f179befec)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Support the Stop opcode. |
| #define | [BT\_MCS\_OPC\_SUP\_MOVE\_RELATIVE](#ga3024e1b5a5175d2f45cdc7650bb9f66a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | Support the Move Relative opcode. |
| #define | [BT\_MCS\_OPC\_SUP\_PREV\_SEGMENT](#gae074d9404aa5c8722678d6805fb7636d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | Support the Previous Segment opcode. |
| #define | [BT\_MCS\_OPC\_SUP\_NEXT\_SEGMENT](#ga416c45a7a2ac8c744c42c19a454d6363)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
|  | Support the Next Segment opcode. |
| #define | [BT\_MCS\_OPC\_SUP\_FIRST\_SEGMENT](#ga5434b6409f4300cd86df1f75cb699ad8)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
|  | Support the First Segment opcode. |
| #define | [BT\_MCS\_OPC\_SUP\_LAST\_SEGMENT](#ga9c4e53c88ea8ea9eb056e9ff37b58dd1)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
|  | Support the Last Segment opcode. |
| #define | [BT\_MCS\_OPC\_SUP\_GOTO\_SEGMENT](#ga9c576ae9a0ad2200a4b29059e88c6c28)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
|  | Support the Goto Segment opcode. |
| #define | [BT\_MCS\_OPC\_SUP\_PREV\_TRACK](#ga59794af43d1b78a1f1a52fb48769be9c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
|  | Support the Previous Track opcode. |
| #define | [BT\_MCS\_OPC\_SUP\_NEXT\_TRACK](#gae213edc6b714f0a1adc744e8ff779ee6)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
|  | Support the Next Track opcode. |
| #define | [BT\_MCS\_OPC\_SUP\_FIRST\_TRACK](#ga7d79bde3dbc9044667fa2bc54cc7cec4)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
|  | Support the First Track opcode. |
| #define | [BT\_MCS\_OPC\_SUP\_LAST\_TRACK](#ga8752a8b6ee27919025bb3e5fb4a77c46)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
|  | Support the Last Track opcode. |
| #define | [BT\_MCS\_OPC\_SUP\_GOTO\_TRACK](#gaf8573ac7d802252076ef759575baef2f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15) |
|  | Support the Goto Track opcode. |
| #define | [BT\_MCS\_OPC\_SUP\_PREV\_GROUP](#ga4443a0f87750c537a6a39544bbf63111)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(16) |
|  | Support the Previous Group opcode. |
| #define | [BT\_MCS\_OPC\_SUP\_NEXT\_GROUP](#gaeeeff1f344202619794af0de0cda199b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(17) |
|  | Support the Next Group opcode. |
| #define | [BT\_MCS\_OPC\_SUP\_FIRST\_GROUP](#ga57508e39d5a32ebefb0b103f805ec047)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(18) |
|  | Support the First Group opcode. |
| #define | [BT\_MCS\_OPC\_SUP\_LAST\_GROUP](#ga80bf605e90dee5841d14fdbb9b39f96a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(19) |
|  | Support the Last Group opcode. |
| #define | [BT\_MCS\_OPC\_SUP\_GOTO\_GROUP](#ga158df3fd1ae39fc3405e25ba7d056d80)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(20) |
|  | Support the Goto Group opcode. |

| Media control point notification result codes | |
| --- | --- |
| #define | [BT\_MCS\_OPC\_NTF\_SUCCESS](#ga7507062e3fe2df221cd47546713a0d28)   0x01 |
|  | Action requested by the opcode write was completed successfully. |
| #define | [BT\_MCS\_OPC\_NTF\_NOT\_SUPPORTED](#ga72e92f172f03a64d2d4641bcdbdb614f)   0x02 |
|  | An invalid or unsupported opcode was used for the Media Control Point write. |
| #define | [BT\_MCS\_OPC\_NTF\_PLAYER\_INACTIVE](#ga740d7278a770b215ae185441fb43c85b)   0x03 |
|  | The Media Player State characteristic value is Inactive when the opcode is received or the result of the requested action of the opcode results in the Media Player State characteristic being set to Inactive. |
| #define | [BT\_MCS\_OPC\_NTF\_CANNOT\_BE\_COMPLETED](#gafe5d0665ae8b33428bce16c427eabcc1)   0x04 |
|  | The requested action of any Media Control Point write cannot be completed successfully because of a condition within the player. |

| Search control point type values | |
| --- | --- |
| Reference: Media Control Service spec v1.0 section 3.20.2 | |
| #define | [BT\_MCS\_SEARCH\_TYPE\_TRACK\_NAME](#ga5a53ce79494a2ec935a43e2cabb6496c)   0x01 |
|  | Search for Track Name. |
| #define | [BT\_MCS\_SEARCH\_TYPE\_ARTIST\_NAME](#ga3bbf3a3393fa08a8f797e7e286f4b06f)   0x02 |
|  | Search for Artist Name. |
| #define | [BT\_MCS\_SEARCH\_TYPE\_ALBUM\_NAME](#gade2b66ace813a9bf91b497fbc1dfb885)   0x03 |
|  | Search for Album Name. |
| #define | [BT\_MCS\_SEARCH\_TYPE\_GROUP\_NAME](#gaf98145eae298cca9e3df1dbcca9118a7)   0x04 |
|  | Search for Group Name. |
| #define | [BT\_MCS\_SEARCH\_TYPE\_EARLIEST\_YEAR](#ga2befe4b4b22125a9e24ab4af6eb08f95)   0x05 |
|  | Search for Earliest Year. |
| #define | [BT\_MCS\_SEARCH\_TYPE\_LATEST\_YEAR](#gad120d8a4f7130762568b7c6f87a34cd4)   0x06 |
|  | Search for Latest Year. |
| #define | [BT\_MCS\_SEARCH\_TYPE\_GENRE](#gae4d30046fb1f4d6ffc554fdd95946bf0)   0x07 |
|  | Search for Genre. |
| #define | [BT\_MCS\_SEARCH\_TYPE\_ONLY\_TRACKS](#gaa99d74ce6f523185a3522f257647edce)   0x08 |
|  | Search for Tracks only. |
| #define | [BT\_MCS\_SEARCH\_TYPE\_ONLY\_GROUPS](#gab6f6fb41e61f5b4c257e36cba71f98a2)   0x09 |
|  | Search for Groups only. |

| Search notification result codes | |
| --- | --- |
| Reference: Media Control Service spec v1.0 section 3.20.2 | |
| #define | [BT\_MCS\_SCP\_NTF\_SUCCESS](#gaa292c3bb4b5eeb62d5e8e6cb72e69908)   0x01 |
|  | Search request was accepted; search has started. |
| #define | [BT\_MCS\_SCP\_NTF\_FAILURE](#ga0a7769ba43b5b5b20cdbce71a129fcef)   0x02 |
|  | Search request was invalid; no search started. |

| Group object object types | |
| --- | --- |
| Reference: Media Control Service spec v1.0 section 4.4.1 | |
| #define | [BT\_MCS\_GROUP\_OBJECT\_TRACK\_TYPE](#gab6f895d3001c6e896c0d9aa9fb11bbc1)   0x00 |
|  | Group object type is track. |
| #define | [BT\_MCS\_GROUP\_OBJECT\_GROUP\_TYPE](#gad7a15680dcf289dfe68b3d8c5f8c9d91)   0x01 |
|  | Group object type is group. |

## Detailed Description

Media Control Service (MCS).

Since
:   3.0

Version
:   0.8.0

Definitions and types related to the Media Control Service and Media Control Profile specifications.

## Macro Definition Documentation

## [◆ ](#gab0c40404b2cd37d0a729504aa270e697)BT\_MCS\_ERR\_LONG\_VAL\_CHANGED

| #define BT\_MCS\_ERR\_LONG\_VAL\_CHANGED   0x80 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

A characteristic value has changed while a Read Long Value Characteristic sub-procedure is in progress.

## [◆ ](#gad7a15680dcf289dfe68b3d8c5f8c9d91)BT\_MCS\_GROUP\_OBJECT\_GROUP\_TYPE

| #define BT\_MCS\_GROUP\_OBJECT\_GROUP\_TYPE   0x01 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Group object type is group.

## [◆ ](#gab6f895d3001c6e896c0d9aa9fb11bbc1)BT\_MCS\_GROUP\_OBJECT\_TRACK\_TYPE

| #define BT\_MCS\_GROUP\_OBJECT\_TRACK\_TYPE   0x00 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Group object type is track.

## [◆ ](#gaa9c7d92a8aa79b1020c8b593b0edc088)BT\_MCS\_MEDIA\_STATE\_INACTIVE

| #define BT\_MCS\_MEDIA\_STATE\_INACTIVE   0x00 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

The current track is invalid, and no track has been selected.

## [◆ ](#gaa5a2768a288fe8058818b5f965c0d8b3)BT\_MCS\_MEDIA\_STATE\_PAUSED

| #define BT\_MCS\_MEDIA\_STATE\_PAUSED   0x02 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

The current track is paused.

The media player has a current track, but it is not being played

## [◆ ](#gaa33b1ba9ebfd0d226df869cdc35e964c)BT\_MCS\_MEDIA\_STATE\_PLAYING

| #define BT\_MCS\_MEDIA\_STATE\_PLAYING   0x01 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

The media player is playing the current track.

## [◆ ](#ga689e83131b6db63fa3a76f428a93714b)BT\_MCS\_MEDIA\_STATE\_SEEKING

| #define BT\_MCS\_MEDIA\_STATE\_SEEKING   0x03 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

The current track is fast forwarding or fast rewinding.

## [◆ ](#ga9ce0d00b1cfc0d3a33762aaed3c1bb75)BT\_MCS\_OPC\_FAST\_FORWARD

| #define BT\_MCS\_OPC\_FAST\_FORWARD   0x04 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Fast forward the current track.

## [◆ ](#ga6d49190bae54e66695ea3c856d558049)BT\_MCS\_OPC\_FAST\_REWIND

| #define BT\_MCS\_OPC\_FAST\_REWIND   0x03 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Fast rewind the current track.

## [◆ ](#ga0b6075379c9abf0911c8a1f2b8d11923)BT\_MCS\_OPC\_FIRST\_GROUP

| #define BT\_MCS\_OPC\_FIRST\_GROUP   0x42 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Set the current group to the first group in the sequence of groups.

## [◆ ](#ga6148011e40389bbed998a971f44f834a)BT\_MCS\_OPC\_FIRST\_SEGMENT

| #define BT\_MCS\_OPC\_FIRST\_SEGMENT   0x22 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Set the current track position to the starting position of the first segment of the current track.

## [◆ ](#gaed893751ae2ceae3a1d5c764b9411ecc)BT\_MCS\_OPC\_FIRST\_TRACK

| #define BT\_MCS\_OPC\_FIRST\_TRACK   0x32 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Set the current track to the first track based on the playing order.

## [◆ ](#ga1911ae5e1285041a77bbd1db773c33b5)BT\_MCS\_OPC\_GOTO\_GROUP

| #define BT\_MCS\_OPC\_GOTO\_GROUP   0x44 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Set the current group to the nth group in the sequence of groups.

## [◆ ](#ga4b91b6e3e3f92619d45ecc2066e97e74)BT\_MCS\_OPC\_GOTO\_SEGMENT

| #define BT\_MCS\_OPC\_GOTO\_SEGMENT   0x24 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Set the current track position to the starting position of the nth segment of the current track.

## [◆ ](#ga4d5124b9ffc125e31c45c06a12fcc85c)BT\_MCS\_OPC\_GOTO\_TRACK

| #define BT\_MCS\_OPC\_GOTO\_TRACK   0x34 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Set the current track to the nth track based on the playing order.

## [◆ ](#gad234093556575ac31985944a483597e8)BT\_MCS\_OPC\_LAST\_GROUP

| #define BT\_MCS\_OPC\_LAST\_GROUP   0x43 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Set the current group to the last group in the sequence of groups.

## [◆ ](#ga08421e4d26d54fe3d40edeb08fd44aac)BT\_MCS\_OPC\_LAST\_SEGMENT

| #define BT\_MCS\_OPC\_LAST\_SEGMENT   0x23 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Set the current track position to the starting position of the last segment of the current track.

## [◆ ](#gacd2e15226d20eb65962d6441c2b7d565)BT\_MCS\_OPC\_LAST\_TRACK

| #define BT\_MCS\_OPC\_LAST\_TRACK   0x33 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Set the current track to the last track based on the playing order.

## [◆ ](#gada25cc85988f5988887eab0cf66e4190)BT\_MCS\_OPC\_MOVE\_RELATIVE

| #define BT\_MCS\_OPC\_MOVE\_RELATIVE   0x10 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Set a new current track position relative to the current track position.

## [◆ ](#ga4feb6b16975ae123bc77c08509e0c809)BT\_MCS\_OPC\_NEXT\_GROUP

| #define BT\_MCS\_OPC\_NEXT\_GROUP   0x41 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Set the current group to the next group in the sequence of groups.

## [◆ ](#ga9cc7b813b933b56b1f60ef0ddf8e39df)BT\_MCS\_OPC\_NEXT\_SEGMENT

| #define BT\_MCS\_OPC\_NEXT\_SEGMENT   0x21 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Set the current track position to the starting position of the next segment of the current track.

## [◆ ](#ga06df0d77c7a678ca8f4f01ec64c88de7)BT\_MCS\_OPC\_NEXT\_TRACK

| #define BT\_MCS\_OPC\_NEXT\_TRACK   0x31 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Set the current track to the next track based on the playing order.

## [◆ ](#gafe5d0665ae8b33428bce16c427eabcc1)BT\_MCS\_OPC\_NTF\_CANNOT\_BE\_COMPLETED

| #define BT\_MCS\_OPC\_NTF\_CANNOT\_BE\_COMPLETED   0x04 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

The requested action of any Media Control Point write cannot be completed successfully because of a condition within the player.

## [◆ ](#ga72e92f172f03a64d2d4641bcdbdb614f)BT\_MCS\_OPC\_NTF\_NOT\_SUPPORTED

| #define BT\_MCS\_OPC\_NTF\_NOT\_SUPPORTED   0x02 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

An invalid or unsupported opcode was used for the Media Control Point write.

## [◆ ](#ga740d7278a770b215ae185441fb43c85b)BT\_MCS\_OPC\_NTF\_PLAYER\_INACTIVE

| #define BT\_MCS\_OPC\_NTF\_PLAYER\_INACTIVE   0x03 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

The Media Player State characteristic value is Inactive when the opcode is received or the result of the requested action of the opcode results in the Media Player State characteristic being set to Inactive.

## [◆ ](#ga7507062e3fe2df221cd47546713a0d28)BT\_MCS\_OPC\_NTF\_SUCCESS

| #define BT\_MCS\_OPC\_NTF\_SUCCESS   0x01 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Action requested by the opcode write was completed successfully.

## [◆ ](#ga8b15cb7a8a1429f83e8d1619c37becc6)BT\_MCS\_OPC\_PAUSE

| #define BT\_MCS\_OPC\_PAUSE   0x02 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Pause playing the current track.

## [◆ ](#ga79c4cf8292a4548bc7b9b06b1ce0f60a)BT\_MCS\_OPC\_PLAY

| #define BT\_MCS\_OPC\_PLAY   0x01 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Start playing the current track.

## [◆ ](#gab7efc1fb17cc53c376f6f84bf31ef85c)BT\_MCS\_OPC\_PREV\_GROUP

| #define BT\_MCS\_OPC\_PREV\_GROUP   0x40 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Set the current group to the previous group in the sequence of groups.

## [◆ ](#ga454775706fe60ccd12e5ab44e6ddacba)BT\_MCS\_OPC\_PREV\_SEGMENT

| #define BT\_MCS\_OPC\_PREV\_SEGMENT   0x20 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Set the current track position to the starting position of the previous segment of the current track.

## [◆ ](#ga88e09cd634c2dd3068f746cc978c1568)BT\_MCS\_OPC\_PREV\_TRACK

| #define BT\_MCS\_OPC\_PREV\_TRACK   0x30 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Set the current track to the previous track based on the playing order.

## [◆ ](#gade874bf59dc08ddb682280b644821e11)BT\_MCS\_OPC\_STOP

| #define BT\_MCS\_OPC\_STOP   0x05 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Stop current activity and return to the paused state and set the current track position to the start of the current track.

## [◆ ](#gaa24785ccc713cb2421a55ff48f5f2c45)BT\_MCS\_OPC\_SUP\_FAST\_FORWARD

| #define BT\_MCS\_OPC\_SUP\_FAST\_FORWARD   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Support the Fast Forward opcode.

## [◆ ](#gaaa3b553dc8eb2de610b545f1ce88b067)BT\_MCS\_OPC\_SUP\_FAST\_REWIND

| #define BT\_MCS\_OPC\_SUP\_FAST\_REWIND   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Support the Fast Rewind opcode.

## [◆ ](#ga57508e39d5a32ebefb0b103f805ec047)BT\_MCS\_OPC\_SUP\_FIRST\_GROUP

| #define BT\_MCS\_OPC\_SUP\_FIRST\_GROUP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(18) |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Support the First Group opcode.

## [◆ ](#ga5434b6409f4300cd86df1f75cb699ad8)BT\_MCS\_OPC\_SUP\_FIRST\_SEGMENT

| #define BT\_MCS\_OPC\_SUP\_FIRST\_SEGMENT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Support the First Segment opcode.

## [◆ ](#ga7d79bde3dbc9044667fa2bc54cc7cec4)BT\_MCS\_OPC\_SUP\_FIRST\_TRACK

| #define BT\_MCS\_OPC\_SUP\_FIRST\_TRACK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Support the First Track opcode.

## [◆ ](#ga158df3fd1ae39fc3405e25ba7d056d80)BT\_MCS\_OPC\_SUP\_GOTO\_GROUP

| #define BT\_MCS\_OPC\_SUP\_GOTO\_GROUP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(20) |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Support the Goto Group opcode.

## [◆ ](#ga9c576ae9a0ad2200a4b29059e88c6c28)BT\_MCS\_OPC\_SUP\_GOTO\_SEGMENT

| #define BT\_MCS\_OPC\_SUP\_GOTO\_SEGMENT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Support the Goto Segment opcode.

## [◆ ](#gaf8573ac7d802252076ef759575baef2f)BT\_MCS\_OPC\_SUP\_GOTO\_TRACK

| #define BT\_MCS\_OPC\_SUP\_GOTO\_TRACK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15) |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Support the Goto Track opcode.

## [◆ ](#ga80bf605e90dee5841d14fdbb9b39f96a)BT\_MCS\_OPC\_SUP\_LAST\_GROUP

| #define BT\_MCS\_OPC\_SUP\_LAST\_GROUP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(19) |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Support the Last Group opcode.

## [◆ ](#ga9c4e53c88ea8ea9eb056e9ff37b58dd1)BT\_MCS\_OPC\_SUP\_LAST\_SEGMENT

| #define BT\_MCS\_OPC\_SUP\_LAST\_SEGMENT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Support the Last Segment opcode.

## [◆ ](#ga8752a8b6ee27919025bb3e5fb4a77c46)BT\_MCS\_OPC\_SUP\_LAST\_TRACK

| #define BT\_MCS\_OPC\_SUP\_LAST\_TRACK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Support the Last Track opcode.

## [◆ ](#ga3024e1b5a5175d2f45cdc7650bb9f66a)BT\_MCS\_OPC\_SUP\_MOVE\_RELATIVE

| #define BT\_MCS\_OPC\_SUP\_MOVE\_RELATIVE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Support the Move Relative opcode.

## [◆ ](#gaeeeff1f344202619794af0de0cda199b)BT\_MCS\_OPC\_SUP\_NEXT\_GROUP

| #define BT\_MCS\_OPC\_SUP\_NEXT\_GROUP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(17) |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Support the Next Group opcode.

## [◆ ](#ga416c45a7a2ac8c744c42c19a454d6363)BT\_MCS\_OPC\_SUP\_NEXT\_SEGMENT

| #define BT\_MCS\_OPC\_SUP\_NEXT\_SEGMENT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Support the Next Segment opcode.

## [◆ ](#gae213edc6b714f0a1adc744e8ff779ee6)BT\_MCS\_OPC\_SUP\_NEXT\_TRACK

| #define BT\_MCS\_OPC\_SUP\_NEXT\_TRACK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Support the Next Track opcode.

## [◆ ](#gabdca574666b964d506d96e01562875f4)BT\_MCS\_OPC\_SUP\_PAUSE

| #define BT\_MCS\_OPC\_SUP\_PAUSE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Support the Pause opcode.

## [◆ ](#ga82d1bbc5cd67ab30960bca6992116a8f)BT\_MCS\_OPC\_SUP\_PLAY

| #define BT\_MCS\_OPC\_SUP\_PLAY   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Support the Play opcode.

## [◆ ](#ga4443a0f87750c537a6a39544bbf63111)BT\_MCS\_OPC\_SUP\_PREV\_GROUP

| #define BT\_MCS\_OPC\_SUP\_PREV\_GROUP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(16) |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Support the Previous Group opcode.

## [◆ ](#gae074d9404aa5c8722678d6805fb7636d)BT\_MCS\_OPC\_SUP\_PREV\_SEGMENT

| #define BT\_MCS\_OPC\_SUP\_PREV\_SEGMENT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Support the Previous Segment opcode.

## [◆ ](#ga59794af43d1b78a1f1a52fb48769be9c)BT\_MCS\_OPC\_SUP\_PREV\_TRACK

| #define BT\_MCS\_OPC\_SUP\_PREV\_TRACK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Support the Previous Track opcode.

## [◆ ](#gaec507c502c53413e510cc30f179befec)BT\_MCS\_OPC\_SUP\_STOP

| #define BT\_MCS\_OPC\_SUP\_STOP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Support the Stop opcode.

## [◆ ](#ga4ae0b32e4192ba36b3ad4d6d8354929a)BT\_MCS\_OPCODES\_SUPPORTED\_LEN

| #define BT\_MCS\_OPCODES\_SUPPORTED\_LEN   4 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Media control point supported opcodes length.

## [◆ ](#ga05ec8bf9ae813c8a3755b1383030bdf0)BT\_MCS\_PLAYBACK\_SPEED\_DOUBLE

| #define BT\_MCS\_PLAYBACK\_SPEED\_DOUBLE   64 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Double playback speed, resulting in 200 % speed.

## [◆ ](#ga3bff45add6fbf602ad6bb07b0e64b335)BT\_MCS\_PLAYBACK\_SPEED\_HALF

| #define BT\_MCS\_PLAYBACK\_SPEED\_HALF   -64 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Half playback speed, resulting in 50 % speed.

## [◆ ](#gaa3299c597471a809033ec45b2c6f5b3d)BT\_MCS\_PLAYBACK\_SPEED\_MAX

| #define BT\_MCS\_PLAYBACK\_SPEED\_MAX   127 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Max playback speed, resulting in 395.7 % speed (nearly 400 %).

## [◆ ](#ga5d450ac222a491b7d544cc4d3f3ffcf0)BT\_MCS\_PLAYBACK\_SPEED\_MIN

| #define BT\_MCS\_PLAYBACK\_SPEED\_MIN   -128 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Minimum playback speed, resulting in 25 % speed.

## [◆ ](#ga90e55b0230a11f752b111750e94ace4c)BT\_MCS\_PLAYBACK\_SPEED\_QUARTER

| #define BT\_MCS\_PLAYBACK\_SPEED\_QUARTER   -128 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Quarter playback speed, resulting in 25 % speed.

## [◆ ](#ga68c0eaa632ca581a1ab5ab144b3d7693)BT\_MCS\_PLAYBACK\_SPEED\_UNITY

| #define BT\_MCS\_PLAYBACK\_SPEED\_UNITY   0 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Unity playback speed, resulting in 100 % speed.

## [◆ ](#ga8b8023d46c3ce402a07c9146494ada60)BT\_MCS\_PLAYING\_ORDER\_INORDER\_ONCE

| #define BT\_MCS\_PLAYING\_ORDER\_INORDER\_ONCE   0x03 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

The tracks within a group are played once in track order.

## [◆ ](#gaaccf440eb5df01eaa0a255e09cf7b996)BT\_MCS\_PLAYING\_ORDER\_INORDER\_REPEAT

| #define BT\_MCS\_PLAYING\_ORDER\_INORDER\_REPEAT   0x04 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

The tracks within a group are played in track order repeatedly.

## [◆ ](#gaaa06525a5d53d4bf2312304208dda311)BT\_MCS\_PLAYING\_ORDER\_NEWEST\_ONCE

| #define BT\_MCS\_PLAYING\_ORDER\_NEWEST\_ONCE   0x07 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

The tracks within a group are played once only from the newest first.

## [◆ ](#ga28a19c78f96b51f0e048395eb4378d61)BT\_MCS\_PLAYING\_ORDER\_NEWEST\_REPEAT

| #define BT\_MCS\_PLAYING\_ORDER\_NEWEST\_REPEAT   0x08 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

The tracks within a group are played from the newest first repeatedly.

## [◆ ](#ga260b73c14b35ee596cacca082b5dc865)BT\_MCS\_PLAYING\_ORDER\_OLDEST\_ONCE

| #define BT\_MCS\_PLAYING\_ORDER\_OLDEST\_ONCE   0x05 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

The tracks within a group are played once only from the oldest first.

## [◆ ](#ga2fb92d553aed2f680321db68ef28035f)BT\_MCS\_PLAYING\_ORDER\_OLDEST\_REPEAT

| #define BT\_MCS\_PLAYING\_ORDER\_OLDEST\_REPEAT   0x06 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

The tracks within a group are played from the oldest first repeatedly.

## [◆ ](#gaa33a02e34f65021b1b7290edc76b166e)BT\_MCS\_PLAYING\_ORDER\_SHUFFLE\_ONCE

| #define BT\_MCS\_PLAYING\_ORDER\_SHUFFLE\_ONCE   0x09 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

The tracks within a group are played in random order once.

## [◆ ](#gaa231c007f0448a5ba3bd61e8528c5b1e)BT\_MCS\_PLAYING\_ORDER\_SHUFFLE\_REPEAT

| #define BT\_MCS\_PLAYING\_ORDER\_SHUFFLE\_REPEAT   0x0a |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

The tracks within a group are played in random order repeatedly.

## [◆ ](#ga1c25a91795472a553286def379fe943b)BT\_MCS\_PLAYING\_ORDER\_SINGLE\_ONCE

| #define BT\_MCS\_PLAYING\_ORDER\_SINGLE\_ONCE   0X01 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

A single track is played once; there is no next track.

## [◆ ](#ga4698529b5268ff1c5099f4cc9d8e9966)BT\_MCS\_PLAYING\_ORDER\_SINGLE\_REPEAT

| #define BT\_MCS\_PLAYING\_ORDER\_SINGLE\_REPEAT   0x02 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

A single track is played repeatedly; the next track is the current track.

## [◆ ](#ga594daa869c6696a4cdd961f8786134a6)BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_INORDER\_ONCE

| #define BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_INORDER\_ONCE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

The tracks within a group are played once in track order.

## [◆ ](#gac4bcd9b84e28a47dd23d073dd942a9c8)BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_INORDER\_REPEAT

| #define BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_INORDER\_REPEAT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

The tracks within a group are played in track order repeatedly.

## [◆ ](#gabd77af4da60d1b7531d35bd543cb4df2)BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_NEWEST\_ONCE

| #define BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_NEWEST\_ONCE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

The tracks within a group are played once only from the newest first.

## [◆ ](#ga9bb22c2c7d08032ab1d5c3ae64ce01a8)BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_NEWEST\_REPEAT

| #define BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_NEWEST\_REPEAT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

The tracks within a group are played from the newest first repeatedly.

## [◆ ](#gae1d8c34c8f9ea9fadc4da56d0d127712)BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_OLDEST\_ONCE

| #define BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_OLDEST\_ONCE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

The tracks within a group are played once only from the oldest first.

## [◆ ](#ga38bb3aa9a388fa3ae0230cb78cf2d3a5)BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_OLDEST\_REPEAT

| #define BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_OLDEST\_REPEAT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

The tracks within a group are played from the oldest first repeatedly.

## [◆ ](#ga2c245ad4f76937b366770aa7afe7b684)BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_SHUFFLE\_ONCE

| #define BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_SHUFFLE\_ONCE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

The tracks within a group are played in random order once.

## [◆ ](#gae5d972a834c1b568f39df91df0febb81)BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_SHUFFLE\_REPEAT

| #define BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_SHUFFLE\_REPEAT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

The tracks within a group are played in random order repeatedly.

## [◆ ](#ga7102f1909baea2320827ea6b47522bd8)BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_SINGLE\_ONCE

| #define BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_SINGLE\_ONCE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

A single track is played once; there is no next track.

## [◆ ](#gafecb7edde06dfb97939af93034690cbc)BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_SINGLE\_REPEAT

| #define BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_SINGLE\_REPEAT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

A single track is played repeatedly; the next track is the current track.

## [◆ ](#ga0a7769ba43b5b5b20cdbce71a129fcef)BT\_MCS\_SCP\_NTF\_FAILURE

| #define BT\_MCS\_SCP\_NTF\_FAILURE   0x02 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Search request was invalid; no search started.

## [◆ ](#gaa292c3bb4b5eeb62d5e8e6cb72e69908)BT\_MCS\_SCP\_NTF\_SUCCESS

| #define BT\_MCS\_SCP\_NTF\_SUCCESS   0x01 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Search request was accepted; search has started.

## [◆ ](#gade2b66ace813a9bf91b497fbc1dfb885)BT\_MCS\_SEARCH\_TYPE\_ALBUM\_NAME

| #define BT\_MCS\_SEARCH\_TYPE\_ALBUM\_NAME   0x03 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Search for Album Name.

## [◆ ](#ga3bbf3a3393fa08a8f797e7e286f4b06f)BT\_MCS\_SEARCH\_TYPE\_ARTIST\_NAME

| #define BT\_MCS\_SEARCH\_TYPE\_ARTIST\_NAME   0x02 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Search for Artist Name.

## [◆ ](#ga2befe4b4b22125a9e24ab4af6eb08f95)BT\_MCS\_SEARCH\_TYPE\_EARLIEST\_YEAR

| #define BT\_MCS\_SEARCH\_TYPE\_EARLIEST\_YEAR   0x05 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Search for Earliest Year.

## [◆ ](#gae4d30046fb1f4d6ffc554fdd95946bf0)BT\_MCS\_SEARCH\_TYPE\_GENRE

| #define BT\_MCS\_SEARCH\_TYPE\_GENRE   0x07 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Search for Genre.

## [◆ ](#gaf98145eae298cca9e3df1dbcca9118a7)BT\_MCS\_SEARCH\_TYPE\_GROUP\_NAME

| #define BT\_MCS\_SEARCH\_TYPE\_GROUP\_NAME   0x04 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Search for Group Name.

## [◆ ](#gad120d8a4f7130762568b7c6f87a34cd4)BT\_MCS\_SEARCH\_TYPE\_LATEST\_YEAR

| #define BT\_MCS\_SEARCH\_TYPE\_LATEST\_YEAR   0x06 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Search for Latest Year.

## [◆ ](#gab6f6fb41e61f5b4c257e36cba71f98a2)BT\_MCS\_SEARCH\_TYPE\_ONLY\_GROUPS

| #define BT\_MCS\_SEARCH\_TYPE\_ONLY\_GROUPS   0x09 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Search for Groups only.

## [◆ ](#gaa99d74ce6f523185a3522f257647edce)BT\_MCS\_SEARCH\_TYPE\_ONLY\_TRACKS

| #define BT\_MCS\_SEARCH\_TYPE\_ONLY\_TRACKS   0x08 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Search for Tracks only.

## [◆ ](#ga5a53ce79494a2ec935a43e2cabb6496c)BT\_MCS\_SEARCH\_TYPE\_TRACK\_NAME

| #define BT\_MCS\_SEARCH\_TYPE\_TRACK\_NAME   0x01 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Search for Track Name.

## [◆ ](#ga22c0b457d8c6e9ec119fff38205786d3)BT\_MCS\_SEEKING\_SPEED\_FACTOR\_MAX

| #define BT\_MCS\_SEEKING\_SPEED\_FACTOR\_MAX   64 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Maximum seeking speed - Can be negated.

## [◆ ](#gaf912dcbc70c81a023f8b93a4d4b0e745)BT\_MCS\_SEEKING\_SPEED\_FACTOR\_MIN

| #define BT\_MCS\_SEEKING\_SPEED\_FACTOR\_MIN   4 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Minimum seeking speed - Can be negated.

## [◆ ](#ga16bdf755d07c99895fa8698f9bd637a0)BT\_MCS\_SEEKING\_SPEED\_FACTOR\_ZERO

| #define BT\_MCS\_SEEKING\_SPEED\_FACTOR\_ZERO   0 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

No seeking.

## [◆ ](#gaf771b17acd202a20450b6ea939ddee3b)SEARCH\_LEN\_MAX

| #define SEARCH\_LEN\_MAX   64 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Search control point maximum length.

## [◆ ](#gaff47bc210fdd2d4d80a0ce822ca29a67)SEARCH\_LEN\_MIN

| #define SEARCH\_LEN\_MIN   2 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Search control point minimum length.

At least one search control item (SCI), consisting of the length octet and the type octet. (The \* parameter field may be empty.)

## [◆ ](#ga81665fd87487cbaf1c0f90f1e0b2126a)SEARCH\_PARAM\_MAX

| #define SEARCH\_PARAM\_MAX   62 |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

Search parameters maximum length.

## [◆ ](#gab1fad64b6a1edfefce90cd4692576a5d)SEARCH\_SCI\_LEN\_MIN

| #define SEARCH\_SCI\_LEN\_MIN |
| --- |

`#include <[mcs.h](mcs_8h.md)>`

**Value:**

1 /\* An SCI length can be as little as one byte,

\* for an SCI that has only the type field.

\* (The SCI len is the length of type + param.)

\*/

Search control point item (SCI) minimum length.

An SCI length can be as little as one byte, for an SCI that has only the type field. (The SCI len is the length of type + param.)

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
