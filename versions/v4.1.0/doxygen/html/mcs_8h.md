---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/mcs_8h.html
original_path: doxygen/html/mcs_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mcs.h File Reference

Bluetooth Media Control Service (MCS) APIs.
[More...](#details)

`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`  
`#include <[zephyr/sys/util_macro.h](util__macro_8h_source.md)>`

[Go to the source code of this file.](mcs_8h_source.md)

| Macros | |
| --- | --- |
| #define | [BT\_MCS\_ERR\_LONG\_VAL\_CHANGED](group__bt__mcs.md#gab0c40404b2cd37d0a729504aa270e697)   0x80 |
|  | A characteristic value has changed while a Read Long Value Characteristic sub-procedure is in progress. |
| #define | [BT\_MCS\_OPCODES\_SUPPORTED\_LEN](group__bt__mcs.md#ga4ae0b32e4192ba36b3ad4d6d8354929a)   4 |
|  | Media control point supported opcodes length. |
| #define | [SEARCH\_LEN\_MIN](group__bt__mcs.md#gaff47bc210fdd2d4d80a0ce822ca29a67)   2 |
|  | Search control point minimum length. |
| #define | [SEARCH\_LEN\_MAX](group__bt__mcs.md#gaf771b17acd202a20450b6ea939ddee3b)   64 |
|  | Search control point maximum length. |
| #define | [SEARCH\_SCI\_LEN\_MIN](group__bt__mcs.md#gab1fad64b6a1edfefce90cd4692576a5d) |
|  | Search control point item (SCI) minimum length. |
| #define | [SEARCH\_PARAM\_MAX](group__bt__mcs.md#ga81665fd87487cbaf1c0f90f1e0b2126a)   62 |
|  | Search parameters maximum length. |
| Playback speeds | |
| The playback speed (s) is calculated by the value of 2 to the power of p divided by 64.  All values from -128 to 127 allowed, only some examples defined. | |
| #define | [BT\_MCS\_PLAYBACK\_SPEED\_MIN](group__bt__mcs.md#ga5d450ac222a491b7d544cc4d3f3ffcf0)   -128 |
|  | Minimum playback speed, resulting in 25 % speed. |
| #define | [BT\_MCS\_PLAYBACK\_SPEED\_QUARTER](group__bt__mcs.md#ga90e55b0230a11f752b111750e94ace4c)   -128 |
|  | Quarter playback speed, resulting in 25 % speed. |
| #define | [BT\_MCS\_PLAYBACK\_SPEED\_HALF](group__bt__mcs.md#ga3bff45add6fbf602ad6bb07b0e64b335)   -64 |
|  | Half playback speed, resulting in 50 % speed. |
| #define | [BT\_MCS\_PLAYBACK\_SPEED\_UNITY](group__bt__mcs.md#ga68c0eaa632ca581a1ab5ab144b3d7693)   0 |
|  | Unity playback speed, resulting in 100 % speed. |
| #define | [BT\_MCS\_PLAYBACK\_SPEED\_DOUBLE](group__bt__mcs.md#ga05ec8bf9ae813c8a3755b1383030bdf0)   64 |
|  | Double playback speed, resulting in 200 % speed. |
| #define | [BT\_MCS\_PLAYBACK\_SPEED\_MAX](group__bt__mcs.md#gaa3299c597471a809033ec45b2c6f5b3d)   127 |
|  | Max playback speed, resulting in 395.7 % speed (nearly 400 %). |
| Seeking speed | |
| The allowed values for seeking speed are the range -64 to -4 (endpoints included), the value 0, and the range 4 to 64 (endpoints included). | |
| #define | [BT\_MCS\_SEEKING\_SPEED\_FACTOR\_MAX](group__bt__mcs.md#ga22c0b457d8c6e9ec119fff38205786d3)   64 |
|  | Maximum seeking speed - Can be negated. |
| #define | [BT\_MCS\_SEEKING\_SPEED\_FACTOR\_MIN](group__bt__mcs.md#gaf912dcbc70c81a023f8b93a4d4b0e745)   4 |
|  | Minimum seeking speed - Can be negated. |
| #define | [BT\_MCS\_SEEKING\_SPEED\_FACTOR\_ZERO](group__bt__mcs.md#ga16bdf755d07c99895fa8698f9bd637a0)   0 |
|  | No seeking. |
| Playing orders | |
| #define | [BT\_MCS\_PLAYING\_ORDER\_SINGLE\_ONCE](group__bt__mcs.md#ga1c25a91795472a553286def379fe943b)   0X01 |
|  | A single track is played once; there is no next track. |
| #define | [BT\_MCS\_PLAYING\_ORDER\_SINGLE\_REPEAT](group__bt__mcs.md#ga4698529b5268ff1c5099f4cc9d8e9966)   0x02 |
|  | A single track is played repeatedly; the next track is the current track. |
| #define | [BT\_MCS\_PLAYING\_ORDER\_INORDER\_ONCE](group__bt__mcs.md#ga8b8023d46c3ce402a07c9146494ada60)   0x03 |
|  | The tracks within a group are played once in track order. |
| #define | [BT\_MCS\_PLAYING\_ORDER\_INORDER\_REPEAT](group__bt__mcs.md#gaaccf440eb5df01eaa0a255e09cf7b996)   0x04 |
|  | The tracks within a group are played in track order repeatedly. |
| #define | [BT\_MCS\_PLAYING\_ORDER\_OLDEST\_ONCE](group__bt__mcs.md#ga260b73c14b35ee596cacca082b5dc865)   0x05 |
|  | The tracks within a group are played once only from the oldest first. |
| #define | [BT\_MCS\_PLAYING\_ORDER\_OLDEST\_REPEAT](group__bt__mcs.md#ga2fb92d553aed2f680321db68ef28035f)   0x06 |
|  | The tracks within a group are played from the oldest first repeatedly. |
| #define | [BT\_MCS\_PLAYING\_ORDER\_NEWEST\_ONCE](group__bt__mcs.md#gaaa06525a5d53d4bf2312304208dda311)   0x07 |
|  | The tracks within a group are played once only from the newest first. |
| #define | [BT\_MCS\_PLAYING\_ORDER\_NEWEST\_REPEAT](group__bt__mcs.md#ga28a19c78f96b51f0e048395eb4378d61)   0x08 |
|  | The tracks within a group are played from the newest first repeatedly. |
| #define | [BT\_MCS\_PLAYING\_ORDER\_SHUFFLE\_ONCE](group__bt__mcs.md#gaa33a02e34f65021b1b7290edc76b166e)   0x09 |
|  | The tracks within a group are played in random order once. |
| #define | [BT\_MCS\_PLAYING\_ORDER\_SHUFFLE\_REPEAT](group__bt__mcs.md#gaa231c007f0448a5ba3bd61e8528c5b1e)   0x0a |
|  | The tracks within a group are played in random order repeatedly. |
| Playing orders supported | |
| A bitmap, in the same order as the playing orders above.  Note that playing order 1 corresponds to bit 0, and so on. | |
| #define | [BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_SINGLE\_ONCE](group__bt__mcs.md#ga7102f1909baea2320827ea6b47522bd8)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | A single track is played once; there is no next track. |
| #define | [BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_SINGLE\_REPEAT](group__bt__mcs.md#gafecb7edde06dfb97939af93034690cbc)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | A single track is played repeatedly; the next track is the current track. |
| #define | [BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_INORDER\_ONCE](group__bt__mcs.md#ga594daa869c6696a4cdd961f8786134a6)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | The tracks within a group are played once in track order. |
| #define | [BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_INORDER\_REPEAT](group__bt__mcs.md#gac4bcd9b84e28a47dd23d073dd942a9c8)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | The tracks within a group are played in track order repeatedly. |
| #define | [BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_OLDEST\_ONCE](group__bt__mcs.md#gae1d8c34c8f9ea9fadc4da56d0d127712)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | The tracks within a group are played once only from the oldest first. |
| #define | [BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_OLDEST\_REPEAT](group__bt__mcs.md#ga38bb3aa9a388fa3ae0230cb78cf2d3a5)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | The tracks within a group are played from the oldest first repeatedly. |
| #define | [BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_NEWEST\_ONCE](group__bt__mcs.md#gabd77af4da60d1b7531d35bd543cb4df2)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | The tracks within a group are played once only from the newest first. |
| #define | [BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_NEWEST\_REPEAT](group__bt__mcs.md#ga9bb22c2c7d08032ab1d5c3ae64ce01a8)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
|  | The tracks within a group are played from the newest first repeatedly. |
| #define | [BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_SHUFFLE\_ONCE](group__bt__mcs.md#ga2c245ad4f76937b366770aa7afe7b684)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
|  | The tracks within a group are played in random order once. |
| #define | [BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_SHUFFLE\_REPEAT](group__bt__mcs.md#gae5d972a834c1b568f39df91df0febb81)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
|  | The tracks within a group are played in random order repeatedly. |
| Media states | |
| #define | [BT\_MCS\_MEDIA\_STATE\_INACTIVE](group__bt__mcs.md#gaa9c7d92a8aa79b1020c8b593b0edc088)   0x00 |
|  | The current track is invalid, and no track has been selected. |
| #define | [BT\_MCS\_MEDIA\_STATE\_PLAYING](group__bt__mcs.md#gaa33b1ba9ebfd0d226df869cdc35e964c)   0x01 |
|  | The media player is playing the current track. |
| #define | [BT\_MCS\_MEDIA\_STATE\_PAUSED](group__bt__mcs.md#gaa5a2768a288fe8058818b5f965c0d8b3)   0x02 |
|  | The current track is paused. |
| #define | [BT\_MCS\_MEDIA\_STATE\_SEEKING](group__bt__mcs.md#ga689e83131b6db63fa3a76f428a93714b)   0x03 |
|  | The current track is fast forwarding or fast rewinding. |
| Media control point opcodes | |
| #define | [BT\_MCS\_OPC\_PLAY](group__bt__mcs.md#ga79c4cf8292a4548bc7b9b06b1ce0f60a)   0x01 |
|  | Start playing the current track. |
| #define | [BT\_MCS\_OPC\_PAUSE](group__bt__mcs.md#ga8b15cb7a8a1429f83e8d1619c37becc6)   0x02 |
|  | Pause playing the current track. |
| #define | [BT\_MCS\_OPC\_FAST\_REWIND](group__bt__mcs.md#ga6d49190bae54e66695ea3c856d558049)   0x03 |
|  | Fast rewind the current track. |
| #define | [BT\_MCS\_OPC\_FAST\_FORWARD](group__bt__mcs.md#ga9ce0d00b1cfc0d3a33762aaed3c1bb75)   0x04 |
|  | Fast forward the current track. |
| #define | [BT\_MCS\_OPC\_STOP](group__bt__mcs.md#gade874bf59dc08ddb682280b644821e11)   0x05 |
|  | Stop current activity and return to the paused state and set the current track position to the start of the current track. |
| #define | [BT\_MCS\_OPC\_MOVE\_RELATIVE](group__bt__mcs.md#gada25cc85988f5988887eab0cf66e4190)   0x10 |
|  | Set a new current track position relative to the current track position. |
| #define | [BT\_MCS\_OPC\_PREV\_SEGMENT](group__bt__mcs.md#ga454775706fe60ccd12e5ab44e6ddacba)   0x20 |
|  | Set the current track position to the starting position of the previous segment of the current track. |
| #define | [BT\_MCS\_OPC\_NEXT\_SEGMENT](group__bt__mcs.md#ga9cc7b813b933b56b1f60ef0ddf8e39df)   0x21 |
|  | Set the current track position to the starting position of the next segment of the current track. |
| #define | [BT\_MCS\_OPC\_FIRST\_SEGMENT](group__bt__mcs.md#ga6148011e40389bbed998a971f44f834a)   0x22 |
|  | Set the current track position to the starting position of the first segment of the current track. |
| #define | [BT\_MCS\_OPC\_LAST\_SEGMENT](group__bt__mcs.md#ga08421e4d26d54fe3d40edeb08fd44aac)   0x23 |
|  | Set the current track position to the starting position of the last segment of the current track. |
| #define | [BT\_MCS\_OPC\_GOTO\_SEGMENT](group__bt__mcs.md#ga4b91b6e3e3f92619d45ecc2066e97e74)   0x24 |
|  | Set the current track position to the starting position of the nth segment of the current track. |
| #define | [BT\_MCS\_OPC\_PREV\_TRACK](group__bt__mcs.md#ga88e09cd634c2dd3068f746cc978c1568)   0x30 |
|  | Set the current track to the previous track based on the playing order. |
| #define | [BT\_MCS\_OPC\_NEXT\_TRACK](group__bt__mcs.md#ga06df0d77c7a678ca8f4f01ec64c88de7)   0x31 |
|  | Set the current track to the next track based on the playing order. |
| #define | [BT\_MCS\_OPC\_FIRST\_TRACK](group__bt__mcs.md#gaed893751ae2ceae3a1d5c764b9411ecc)   0x32 |
|  | Set the current track to the first track based on the playing order. |
| #define | [BT\_MCS\_OPC\_LAST\_TRACK](group__bt__mcs.md#gacd2e15226d20eb65962d6441c2b7d565)   0x33 |
|  | Set the current track to the last track based on the playing order. |
| #define | [BT\_MCS\_OPC\_GOTO\_TRACK](group__bt__mcs.md#ga4d5124b9ffc125e31c45c06a12fcc85c)   0x34 |
|  | Set the current track to the nth track based on the playing order. |
| #define | [BT\_MCS\_OPC\_PREV\_GROUP](group__bt__mcs.md#gab7efc1fb17cc53c376f6f84bf31ef85c)   0x40 |
|  | Set the current group to the previous group in the sequence of groups. |
| #define | [BT\_MCS\_OPC\_NEXT\_GROUP](group__bt__mcs.md#ga4feb6b16975ae123bc77c08509e0c809)   0x41 |
|  | Set the current group to the next group in the sequence of groups. |
| #define | [BT\_MCS\_OPC\_FIRST\_GROUP](group__bt__mcs.md#ga0b6075379c9abf0911c8a1f2b8d11923)   0x42 |
|  | Set the current group to the first group in the sequence of groups. |
| #define | [BT\_MCS\_OPC\_LAST\_GROUP](group__bt__mcs.md#gad234093556575ac31985944a483597e8)   0x43 |
|  | Set the current group to the last group in the sequence of groups. |
| #define | [BT\_MCS\_OPC\_GOTO\_GROUP](group__bt__mcs.md#ga1911ae5e1285041a77bbd1db773c33b5)   0x44 |
|  | Set the current group to the nth group in the sequence of groups. |
| Media control point supported opcodes values | |
| #define | [BT\_MCS\_OPC\_SUP\_PLAY](group__bt__mcs.md#ga82d1bbc5cd67ab30960bca6992116a8f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Support the Play opcode. |
| #define | [BT\_MCS\_OPC\_SUP\_PAUSE](group__bt__mcs.md#gabdca574666b964d506d96e01562875f4)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Support the Pause opcode. |
| #define | [BT\_MCS\_OPC\_SUP\_FAST\_REWIND](group__bt__mcs.md#gaaa3b553dc8eb2de610b545f1ce88b067)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Support the Fast Rewind opcode. |
| #define | [BT\_MCS\_OPC\_SUP\_FAST\_FORWARD](group__bt__mcs.md#gaa24785ccc713cb2421a55ff48f5f2c45)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Support the Fast Forward opcode. |
| #define | [BT\_MCS\_OPC\_SUP\_STOP](group__bt__mcs.md#gaec507c502c53413e510cc30f179befec)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Support the Stop opcode. |
| #define | [BT\_MCS\_OPC\_SUP\_MOVE\_RELATIVE](group__bt__mcs.md#ga3024e1b5a5175d2f45cdc7650bb9f66a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | Support the Move Relative opcode. |
| #define | [BT\_MCS\_OPC\_SUP\_PREV\_SEGMENT](group__bt__mcs.md#gae074d9404aa5c8722678d6805fb7636d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | Support the Previous Segment opcode. |
| #define | [BT\_MCS\_OPC\_SUP\_NEXT\_SEGMENT](group__bt__mcs.md#ga416c45a7a2ac8c744c42c19a454d6363)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
|  | Support the Next Segment opcode. |
| #define | [BT\_MCS\_OPC\_SUP\_FIRST\_SEGMENT](group__bt__mcs.md#ga5434b6409f4300cd86df1f75cb699ad8)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
|  | Support the First Segment opcode. |
| #define | [BT\_MCS\_OPC\_SUP\_LAST\_SEGMENT](group__bt__mcs.md#ga9c4e53c88ea8ea9eb056e9ff37b58dd1)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
|  | Support the Last Segment opcode. |
| #define | [BT\_MCS\_OPC\_SUP\_GOTO\_SEGMENT](group__bt__mcs.md#ga9c576ae9a0ad2200a4b29059e88c6c28)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
|  | Support the Goto Segment opcode. |
| #define | [BT\_MCS\_OPC\_SUP\_PREV\_TRACK](group__bt__mcs.md#ga59794af43d1b78a1f1a52fb48769be9c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
|  | Support the Previous Track opcode. |
| #define | [BT\_MCS\_OPC\_SUP\_NEXT\_TRACK](group__bt__mcs.md#gae213edc6b714f0a1adc744e8ff779ee6)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
|  | Support the Next Track opcode. |
| #define | [BT\_MCS\_OPC\_SUP\_FIRST\_TRACK](group__bt__mcs.md#ga7d79bde3dbc9044667fa2bc54cc7cec4)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) |
|  | Support the First Track opcode. |
| #define | [BT\_MCS\_OPC\_SUP\_LAST\_TRACK](group__bt__mcs.md#ga8752a8b6ee27919025bb3e5fb4a77c46)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14) |
|  | Support the Last Track opcode. |
| #define | [BT\_MCS\_OPC\_SUP\_GOTO\_TRACK](group__bt__mcs.md#gaf8573ac7d802252076ef759575baef2f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15) |
|  | Support the Goto Track opcode. |
| #define | [BT\_MCS\_OPC\_SUP\_PREV\_GROUP](group__bt__mcs.md#ga4443a0f87750c537a6a39544bbf63111)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(16) |
|  | Support the Previous Group opcode. |
| #define | [BT\_MCS\_OPC\_SUP\_NEXT\_GROUP](group__bt__mcs.md#gaeeeff1f344202619794af0de0cda199b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(17) |
|  | Support the Next Group opcode. |
| #define | [BT\_MCS\_OPC\_SUP\_FIRST\_GROUP](group__bt__mcs.md#ga57508e39d5a32ebefb0b103f805ec047)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(18) |
|  | Support the First Group opcode. |
| #define | [BT\_MCS\_OPC\_SUP\_LAST\_GROUP](group__bt__mcs.md#ga80bf605e90dee5841d14fdbb9b39f96a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(19) |
|  | Support the Last Group opcode. |
| #define | [BT\_MCS\_OPC\_SUP\_GOTO\_GROUP](group__bt__mcs.md#ga158df3fd1ae39fc3405e25ba7d056d80)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(20) |
|  | Support the Goto Group opcode. |
| Media control point notification result codes | |
| #define | [BT\_MCS\_OPC\_NTF\_SUCCESS](group__bt__mcs.md#ga7507062e3fe2df221cd47546713a0d28)   0x01 |
|  | Action requested by the opcode write was completed successfully. |
| #define | [BT\_MCS\_OPC\_NTF\_NOT\_SUPPORTED](group__bt__mcs.md#ga72e92f172f03a64d2d4641bcdbdb614f)   0x02 |
|  | An invalid or unsupported opcode was used for the Media Control Point write. |
| #define | [BT\_MCS\_OPC\_NTF\_PLAYER\_INACTIVE](group__bt__mcs.md#ga740d7278a770b215ae185441fb43c85b)   0x03 |
|  | The Media Player State characteristic value is Inactive when the opcode is received or the result of the requested action of the opcode results in the Media Player State characteristic being set to Inactive. |
| #define | [BT\_MCS\_OPC\_NTF\_CANNOT\_BE\_COMPLETED](group__bt__mcs.md#gafe5d0665ae8b33428bce16c427eabcc1)   0x04 |
|  | The requested action of any Media Control Point write cannot be completed successfully because of a condition within the player. |
| Search control point type values | |
| Reference: Media Control Service spec v1.0 section 3.20.2 | |
| #define | [BT\_MCS\_SEARCH\_TYPE\_TRACK\_NAME](group__bt__mcs.md#ga5a53ce79494a2ec935a43e2cabb6496c)   0x01 |
|  | Search for Track Name. |
| #define | [BT\_MCS\_SEARCH\_TYPE\_ARTIST\_NAME](group__bt__mcs.md#ga3bbf3a3393fa08a8f797e7e286f4b06f)   0x02 |
|  | Search for Artist Name. |
| #define | [BT\_MCS\_SEARCH\_TYPE\_ALBUM\_NAME](group__bt__mcs.md#gade2b66ace813a9bf91b497fbc1dfb885)   0x03 |
|  | Search for Album Name. |
| #define | [BT\_MCS\_SEARCH\_TYPE\_GROUP\_NAME](group__bt__mcs.md#gaf98145eae298cca9e3df1dbcca9118a7)   0x04 |
|  | Search for Group Name. |
| #define | [BT\_MCS\_SEARCH\_TYPE\_EARLIEST\_YEAR](group__bt__mcs.md#ga2befe4b4b22125a9e24ab4af6eb08f95)   0x05 |
|  | Search for Earliest Year. |
| #define | [BT\_MCS\_SEARCH\_TYPE\_LATEST\_YEAR](group__bt__mcs.md#gad120d8a4f7130762568b7c6f87a34cd4)   0x06 |
|  | Search for Latest Year. |
| #define | [BT\_MCS\_SEARCH\_TYPE\_GENRE](group__bt__mcs.md#gae4d30046fb1f4d6ffc554fdd95946bf0)   0x07 |
|  | Search for Genre. |
| #define | [BT\_MCS\_SEARCH\_TYPE\_ONLY\_TRACKS](group__bt__mcs.md#gaa99d74ce6f523185a3522f257647edce)   0x08 |
|  | Search for Tracks only. |
| #define | [BT\_MCS\_SEARCH\_TYPE\_ONLY\_GROUPS](group__bt__mcs.md#gab6f6fb41e61f5b4c257e36cba71f98a2)   0x09 |
|  | Search for Groups only. |
| Search notification result codes | |
| Reference: Media Control Service spec v1.0 section 3.20.2 | |
| #define | [BT\_MCS\_SCP\_NTF\_SUCCESS](group__bt__mcs.md#gaa292c3bb4b5eeb62d5e8e6cb72e69908)   0x01 |
|  | Search request was accepted; search has started. |
| #define | [BT\_MCS\_SCP\_NTF\_FAILURE](group__bt__mcs.md#ga0a7769ba43b5b5b20cdbce71a129fcef)   0x02 |
|  | Search request was invalid; no search started. |
| Group object object types | |
| Reference: Media Control Service spec v1.0 section 4.4.1 | |
| #define | [BT\_MCS\_GROUP\_OBJECT\_TRACK\_TYPE](group__bt__mcs.md#gab6f895d3001c6e896c0d9aa9fb11bbc1)   0x00 |
|  | Group object type is track. |
| #define | [BT\_MCS\_GROUP\_OBJECT\_GROUP\_TYPE](group__bt__mcs.md#gad7a15680dcf289dfe68b3d8c5f8c9d91)   0x01 |
|  | Group object type is group. |

## Detailed Description

Bluetooth Media Control Service (MCS) APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [mcs.h](mcs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
