---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/mcs_8h_source.html
original_path: doxygen/html/mcs_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mcs.h

[Go to the documentation of this file.](mcs_8h.md)

1

5/\*

6 \* Copyright (c) 2019 - 2024 Nordic Semiconductor ASA

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10

11#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_MCS\_H\_

12#define ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_MCS\_H\_

13

28

29#include <[zephyr/sys/util.h](util_8h.md)>

30#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

31

32#ifdef \_\_cplusplus

33extern "C" {

34#endif

35

[ 40](group__bt__mcs.md#gab0c40404b2cd37d0a729504aa270e697)#define BT\_MCS\_ERR\_LONG\_VAL\_CHANGED 0x80

41

[ 50](group__bt__mcs.md#ga5d450ac222a491b7d544cc4d3f3ffcf0)#define BT\_MCS\_PLAYBACK\_SPEED\_MIN -128

[ 52](group__bt__mcs.md#ga90e55b0230a11f752b111750e94ace4c)#define BT\_MCS\_PLAYBACK\_SPEED\_QUARTER -128

[ 54](group__bt__mcs.md#ga3bff45add6fbf602ad6bb07b0e64b335)#define BT\_MCS\_PLAYBACK\_SPEED\_HALF -64

[ 56](group__bt__mcs.md#ga68c0eaa632ca581a1ab5ab144b3d7693)#define BT\_MCS\_PLAYBACK\_SPEED\_UNITY 0

[ 58](group__bt__mcs.md#ga05ec8bf9ae813c8a3755b1383030bdf0)#define BT\_MCS\_PLAYBACK\_SPEED\_DOUBLE 64

[ 60](group__bt__mcs.md#gaa3299c597471a809033ec45b2c6f5b3d)#define BT\_MCS\_PLAYBACK\_SPEED\_MAX 127

62

[ 72](group__bt__mcs.md#ga22c0b457d8c6e9ec119fff38205786d3)#define BT\_MCS\_SEEKING\_SPEED\_FACTOR\_MAX 64

[ 74](group__bt__mcs.md#gaf912dcbc70c81a023f8b93a4d4b0e745)#define BT\_MCS\_SEEKING\_SPEED\_FACTOR\_MIN 4

[ 76](group__bt__mcs.md#ga16bdf755d07c99895fa8698f9bd637a0)#define BT\_MCS\_SEEKING\_SPEED\_FACTOR\_ZERO 0

78

[ 84](group__bt__mcs.md#ga1c25a91795472a553286def379fe943b)#define BT\_MCS\_PLAYING\_ORDER\_SINGLE\_ONCE 0X01

[ 86](group__bt__mcs.md#ga4698529b5268ff1c5099f4cc9d8e9966)#define BT\_MCS\_PLAYING\_ORDER\_SINGLE\_REPEAT 0x02

[ 88](group__bt__mcs.md#ga8b8023d46c3ce402a07c9146494ada60)#define BT\_MCS\_PLAYING\_ORDER\_INORDER\_ONCE 0x03

[ 90](group__bt__mcs.md#gaaccf440eb5df01eaa0a255e09cf7b996)#define BT\_MCS\_PLAYING\_ORDER\_INORDER\_REPEAT 0x04

[ 92](group__bt__mcs.md#ga260b73c14b35ee596cacca082b5dc865)#define BT\_MCS\_PLAYING\_ORDER\_OLDEST\_ONCE 0x05

[ 94](group__bt__mcs.md#ga2fb92d553aed2f680321db68ef28035f)#define BT\_MCS\_PLAYING\_ORDER\_OLDEST\_REPEAT 0x06

[ 96](group__bt__mcs.md#gaaa06525a5d53d4bf2312304208dda311)#define BT\_MCS\_PLAYING\_ORDER\_NEWEST\_ONCE 0x07

[ 98](group__bt__mcs.md#ga28a19c78f96b51f0e048395eb4378d61)#define BT\_MCS\_PLAYING\_ORDER\_NEWEST\_REPEAT 0x08

[ 100](group__bt__mcs.md#gaa33a02e34f65021b1b7290edc76b166e)#define BT\_MCS\_PLAYING\_ORDER\_SHUFFLE\_ONCE 0x09

[ 102](group__bt__mcs.md#gaa231c007f0448a5ba3bd61e8528c5b1e)#define BT\_MCS\_PLAYING\_ORDER\_SHUFFLE\_REPEAT 0x0a

104

[ 112](group__bt__mcs.md#ga7102f1909baea2320827ea6b47522bd8)#define BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_SINGLE\_ONCE BIT(0)

[ 114](group__bt__mcs.md#gafecb7edde06dfb97939af93034690cbc)#define BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_SINGLE\_REPEAT BIT(1)

[ 116](group__bt__mcs.md#ga594daa869c6696a4cdd961f8786134a6)#define BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_INORDER\_ONCE BIT(2)

[ 118](group__bt__mcs.md#gac4bcd9b84e28a47dd23d073dd942a9c8)#define BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_INORDER\_REPEAT BIT(3)

[ 120](group__bt__mcs.md#gae1d8c34c8f9ea9fadc4da56d0d127712)#define BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_OLDEST\_ONCE BIT(4)

[ 122](group__bt__mcs.md#ga38bb3aa9a388fa3ae0230cb78cf2d3a5)#define BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_OLDEST\_REPEAT BIT(5)

[ 124](group__bt__mcs.md#gabd77af4da60d1b7531d35bd543cb4df2)#define BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_NEWEST\_ONCE BIT(6)

[ 126](group__bt__mcs.md#ga9bb22c2c7d08032ab1d5c3ae64ce01a8)#define BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_NEWEST\_REPEAT BIT(7)

[ 128](group__bt__mcs.md#ga2c245ad4f76937b366770aa7afe7b684)#define BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_SHUFFLE\_ONCE BIT(8)

[ 130](group__bt__mcs.md#gae5d972a834c1b568f39df91df0febb81)#define BT\_MCS\_PLAYING\_ORDERS\_SUPPORTED\_SHUFFLE\_REPEAT BIT(9)

132

[ 138](group__bt__mcs.md#gaa9c7d92a8aa79b1020c8b593b0edc088)#define BT\_MCS\_MEDIA\_STATE\_INACTIVE 0x00

[ 140](group__bt__mcs.md#gaa33b1ba9ebfd0d226df869cdc35e964c)#define BT\_MCS\_MEDIA\_STATE\_PLAYING 0x01

[ 142](group__bt__mcs.md#gaa5a2768a288fe8058818b5f965c0d8b3)#define BT\_MCS\_MEDIA\_STATE\_PAUSED 0x02

[ 144](group__bt__mcs.md#ga689e83131b6db63fa3a76f428a93714b)#define BT\_MCS\_MEDIA\_STATE\_SEEKING 0x03

146

[ 152](group__bt__mcs.md#ga79c4cf8292a4548bc7b9b06b1ce0f60a)#define BT\_MCS\_OPC\_PLAY 0x01

[ 154](group__bt__mcs.md#ga8b15cb7a8a1429f83e8d1619c37becc6)#define BT\_MCS\_OPC\_PAUSE 0x02

[ 156](group__bt__mcs.md#ga6d49190bae54e66695ea3c856d558049)#define BT\_MCS\_OPC\_FAST\_REWIND 0x03

[ 158](group__bt__mcs.md#ga9ce0d00b1cfc0d3a33762aaed3c1bb75)#define BT\_MCS\_OPC\_FAST\_FORWARD 0x04

[ 163](group__bt__mcs.md#gade874bf59dc08ddb682280b644821e11)#define BT\_MCS\_OPC\_STOP 0x05

164

[ 166](group__bt__mcs.md#gada25cc85988f5988887eab0cf66e4190)#define BT\_MCS\_OPC\_MOVE\_RELATIVE 0x10

167

[ 172](group__bt__mcs.md#ga454775706fe60ccd12e5ab44e6ddacba)#define BT\_MCS\_OPC\_PREV\_SEGMENT 0x20

[ 177](group__bt__mcs.md#ga9cc7b813b933b56b1f60ef0ddf8e39df)#define BT\_MCS\_OPC\_NEXT\_SEGMENT 0x21

[ 182](group__bt__mcs.md#ga6148011e40389bbed998a971f44f834a)#define BT\_MCS\_OPC\_FIRST\_SEGMENT 0x22

[ 187](group__bt__mcs.md#ga08421e4d26d54fe3d40edeb08fd44aac)#define BT\_MCS\_OPC\_LAST\_SEGMENT 0x23

[ 192](group__bt__mcs.md#ga4b91b6e3e3f92619d45ecc2066e97e74)#define BT\_MCS\_OPC\_GOTO\_SEGMENT 0x24

193

[ 195](group__bt__mcs.md#ga88e09cd634c2dd3068f746cc978c1568)#define BT\_MCS\_OPC\_PREV\_TRACK 0x30

[ 197](group__bt__mcs.md#ga06df0d77c7a678ca8f4f01ec64c88de7)#define BT\_MCS\_OPC\_NEXT\_TRACK 0x31

[ 199](group__bt__mcs.md#gaed893751ae2ceae3a1d5c764b9411ecc)#define BT\_MCS\_OPC\_FIRST\_TRACK 0x32

[ 201](group__bt__mcs.md#gacd2e15226d20eb65962d6441c2b7d565)#define BT\_MCS\_OPC\_LAST\_TRACK 0x33

[ 203](group__bt__mcs.md#ga4d5124b9ffc125e31c45c06a12fcc85c)#define BT\_MCS\_OPC\_GOTO\_TRACK 0x34

204

[ 206](group__bt__mcs.md#gab7efc1fb17cc53c376f6f84bf31ef85c)#define BT\_MCS\_OPC\_PREV\_GROUP 0x40

[ 208](group__bt__mcs.md#ga4feb6b16975ae123bc77c08509e0c809)#define BT\_MCS\_OPC\_NEXT\_GROUP 0x41

[ 210](group__bt__mcs.md#ga0b6075379c9abf0911c8a1f2b8d11923)#define BT\_MCS\_OPC\_FIRST\_GROUP 0x42

[ 212](group__bt__mcs.md#gad234093556575ac31985944a483597e8)#define BT\_MCS\_OPC\_LAST\_GROUP 0x43

[ 214](group__bt__mcs.md#ga1911ae5e1285041a77bbd1db773c33b5)#define BT\_MCS\_OPC\_GOTO\_GROUP 0x44

216

[ 218](group__bt__mcs.md#ga4ae0b32e4192ba36b3ad4d6d8354929a)#define BT\_MCS\_OPCODES\_SUPPORTED\_LEN 4

219

[ 225](group__bt__mcs.md#ga82d1bbc5cd67ab30960bca6992116a8f)#define BT\_MCS\_OPC\_SUP\_PLAY BIT(0)

[ 227](group__bt__mcs.md#gabdca574666b964d506d96e01562875f4)#define BT\_MCS\_OPC\_SUP\_PAUSE BIT(1)

[ 229](group__bt__mcs.md#gaaa3b553dc8eb2de610b545f1ce88b067)#define BT\_MCS\_OPC\_SUP\_FAST\_REWIND BIT(2)

[ 231](group__bt__mcs.md#gaa24785ccc713cb2421a55ff48f5f2c45)#define BT\_MCS\_OPC\_SUP\_FAST\_FORWARD BIT(3)

[ 233](group__bt__mcs.md#gaec507c502c53413e510cc30f179befec)#define BT\_MCS\_OPC\_SUP\_STOP BIT(4)

234

[ 236](group__bt__mcs.md#ga3024e1b5a5175d2f45cdc7650bb9f66a)#define BT\_MCS\_OPC\_SUP\_MOVE\_RELATIVE BIT(5)

237

[ 239](group__bt__mcs.md#gae074d9404aa5c8722678d6805fb7636d)#define BT\_MCS\_OPC\_SUP\_PREV\_SEGMENT BIT(6)

[ 241](group__bt__mcs.md#ga416c45a7a2ac8c744c42c19a454d6363)#define BT\_MCS\_OPC\_SUP\_NEXT\_SEGMENT BIT(7)

[ 243](group__bt__mcs.md#ga5434b6409f4300cd86df1f75cb699ad8)#define BT\_MCS\_OPC\_SUP\_FIRST\_SEGMENT BIT(8)

[ 245](group__bt__mcs.md#ga9c4e53c88ea8ea9eb056e9ff37b58dd1)#define BT\_MCS\_OPC\_SUP\_LAST\_SEGMENT BIT(9)

[ 247](group__bt__mcs.md#ga9c576ae9a0ad2200a4b29059e88c6c28)#define BT\_MCS\_OPC\_SUP\_GOTO\_SEGMENT BIT(10)

248

[ 250](group__bt__mcs.md#ga59794af43d1b78a1f1a52fb48769be9c)#define BT\_MCS\_OPC\_SUP\_PREV\_TRACK BIT(11)

[ 252](group__bt__mcs.md#gae213edc6b714f0a1adc744e8ff779ee6)#define BT\_MCS\_OPC\_SUP\_NEXT\_TRACK BIT(12)

[ 254](group__bt__mcs.md#ga7d79bde3dbc9044667fa2bc54cc7cec4)#define BT\_MCS\_OPC\_SUP\_FIRST\_TRACK BIT(13)

[ 256](group__bt__mcs.md#ga8752a8b6ee27919025bb3e5fb4a77c46)#define BT\_MCS\_OPC\_SUP\_LAST\_TRACK BIT(14)

[ 258](group__bt__mcs.md#gaf8573ac7d802252076ef759575baef2f)#define BT\_MCS\_OPC\_SUP\_GOTO\_TRACK BIT(15)

259

[ 261](group__bt__mcs.md#ga4443a0f87750c537a6a39544bbf63111)#define BT\_MCS\_OPC\_SUP\_PREV\_GROUP BIT(16)

[ 263](group__bt__mcs.md#gaeeeff1f344202619794af0de0cda199b)#define BT\_MCS\_OPC\_SUP\_NEXT\_GROUP BIT(17)

[ 265](group__bt__mcs.md#ga57508e39d5a32ebefb0b103f805ec047)#define BT\_MCS\_OPC\_SUP\_FIRST\_GROUP BIT(18)

[ 267](group__bt__mcs.md#ga80bf605e90dee5841d14fdbb9b39f96a)#define BT\_MCS\_OPC\_SUP\_LAST\_GROUP BIT(19)

[ 269](group__bt__mcs.md#ga158df3fd1ae39fc3405e25ba7d056d80)#define BT\_MCS\_OPC\_SUP\_GOTO\_GROUP BIT(20)

271

[ 277](group__bt__mcs.md#ga7507062e3fe2df221cd47546713a0d28)#define BT\_MCS\_OPC\_NTF\_SUCCESS 0x01

[ 279](group__bt__mcs.md#ga72e92f172f03a64d2d4641bcdbdb614f)#define BT\_MCS\_OPC\_NTF\_NOT\_SUPPORTED 0x02

[ 285](group__bt__mcs.md#ga740d7278a770b215ae185441fb43c85b)#define BT\_MCS\_OPC\_NTF\_PLAYER\_INACTIVE 0x03

[ 290](group__bt__mcs.md#gafe5d0665ae8b33428bce16c427eabcc1)#define BT\_MCS\_OPC\_NTF\_CANNOT\_BE\_COMPLETED 0x04

292

[ 300](group__bt__mcs.md#ga5a53ce79494a2ec935a43e2cabb6496c)#define BT\_MCS\_SEARCH\_TYPE\_TRACK\_NAME 0x01

[ 302](group__bt__mcs.md#ga3bbf3a3393fa08a8f797e7e286f4b06f)#define BT\_MCS\_SEARCH\_TYPE\_ARTIST\_NAME 0x02

[ 304](group__bt__mcs.md#gade2b66ace813a9bf91b497fbc1dfb885)#define BT\_MCS\_SEARCH\_TYPE\_ALBUM\_NAME 0x03

[ 306](group__bt__mcs.md#gaf98145eae298cca9e3df1dbcca9118a7)#define BT\_MCS\_SEARCH\_TYPE\_GROUP\_NAME 0x04

[ 308](group__bt__mcs.md#ga2befe4b4b22125a9e24ab4af6eb08f95)#define BT\_MCS\_SEARCH\_TYPE\_EARLIEST\_YEAR 0x05

[ 310](group__bt__mcs.md#gad120d8a4f7130762568b7c6f87a34cd4)#define BT\_MCS\_SEARCH\_TYPE\_LATEST\_YEAR 0x06

[ 312](group__bt__mcs.md#gae4d30046fb1f4d6ffc554fdd95946bf0)#define BT\_MCS\_SEARCH\_TYPE\_GENRE 0x07

[ 314](group__bt__mcs.md#gaa99d74ce6f523185a3522f257647edce)#define BT\_MCS\_SEARCH\_TYPE\_ONLY\_TRACKS 0x08

[ 316](group__bt__mcs.md#gab6f6fb41e61f5b4c257e36cba71f98a2)#define BT\_MCS\_SEARCH\_TYPE\_ONLY\_GROUPS 0x09

318

[ 325](group__bt__mcs.md#gaff47bc210fdd2d4d80a0ce822ca29a67)#define SEARCH\_LEN\_MIN 2

326

[ 328](group__bt__mcs.md#gaf771b17acd202a20450b6ea939ddee3b)#define SEARCH\_LEN\_MAX 64

329

[ 336](group__bt__mcs.md#gab1fad64b6a1edfefce90cd4692576a5d)#define SEARCH\_SCI\_LEN\_MIN 1 /\* An SCI length can be as little as one byte,

337 \* for an SCI that has only the type field.

338 \* (The SCI len is the length of type + param.)

[ 339](group__bt__mcs.md#ga81665fd87487cbaf1c0f90f1e0b2126a) \*/

340

342#define SEARCH\_PARAM\_MAX 62

343

351#define BT\_MCS\_SCP\_NTF\_SUCCESS 0x01

353#define BT\_MCS\_SCP\_NTF\_FAILURE 0x02

355

363#define BT\_MCS\_GROUP\_OBJECT\_TRACK\_TYPE 0x00

365#define BT\_MCS\_GROUP\_OBJECT\_GROUP\_TYPE 0x01

367

368#ifdef \_\_cplusplus

369}

370#endif

371

375

376#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_MCS\_H\_ \*/

[util.h](util_8h.md)

Misc utilities.

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [mcs.h](mcs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
