---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/bluetooth_2audio_2audio_8h_source.html
original_path: doxygen/html/bluetooth_2audio_2audio_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

audio.h

[Go to the documentation of this file.](bluetooth_2audio_2audio_8h.md)

1

5

6/\*

7 \* Copyright (c) 2020 Intel Corporation

8 \* Copyright (c) 2020-2024 Nordic Semiconductor ASA

9 \*

10 \* SPDX-License-Identifier: Apache-2.0

11 \*/

12#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_AUDIO\_H\_

13#define ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_AUDIO\_H\_

14

21

22#include <[stdbool.h](stdbool_8h.md)>

23#include <stddef.h>

24#include <[stdint.h](stdint_8h.md)>

25

26#include <zephyr/autoconf.h>

27#include <[zephyr/bluetooth/audio/lc3.h](lc3_8h.md)>

28#include <[zephyr/bluetooth/bluetooth.h](bluetooth_2bluetooth_8h.md)>

29#include <[zephyr/bluetooth/buf.h](bluetooth_2buf_8h.md)>

30#include <[zephyr/bluetooth/conn.h](conn_8h.md)>

31#include <[zephyr/bluetooth/gatt.h](gatt_8h.md)>

32#include <[zephyr/bluetooth/hci.h](hci_8h.md)>

33#include <[zephyr/bluetooth/iso.h](iso_8h.md)>

34#include <[zephyr/sys/atomic.h](sys_2atomic_8h.md)>

35#include <[zephyr/sys/util.h](sys_2util_8h.md)>

36#include <[zephyr/sys/util\_macro.h](util__macro_8h.md)>

37

38#ifdef \_\_cplusplus

39extern "C" {

40#endif

41

[ 43](group__bt__audio.md#ga18dd9f4a4af7716dd01497309ff9c87c)#define BT\_AUDIO\_BROADCAST\_ID\_SIZE 3

[ 45](group__bt__audio.md#ga3ed5ba09ab4c1ab7a59f8a1b4deee791)#define BT\_AUDIO\_BROADCAST\_ID\_MAX 0xFFFFFFU

[ 47](group__bt__audio.md#ga663ab7bf74d56f36ee6cc80b369cbc16)#define BT\_AUDIO\_PD\_PREF\_NONE 0x000000U

[ 49](group__bt__audio.md#gaaa0414a4baef5a867fd1c6b1865d2dbc)#define BT\_AUDIO\_PD\_MAX 0xFFFFFFU

[ 51](group__bt__audio.md#ga4a5fd440b96f4e4acbb791badef8c255)#define BT\_AUDIO\_RTN\_PREF\_NONE 0xFFU

[ 53](group__bt__audio.md#gaa3bf677a479a90793f28a5a3ed69c7e0)#define BT\_AUDIO\_BROADCAST\_NAME\_LEN\_MIN 4

[ 55](group__bt__audio.md#gaa2fafcbb6a826c3f4cee16ebb545dad6)#define BT\_AUDIO\_BROADCAST\_NAME\_LEN\_MAX 128

56

[ 58](group__bt__audio.md#gab6e5f793d514626deca21940d35d8f21)#define BT\_AUDIO\_LANG\_SIZE 3

59

[ 66](group__bt__audio.md#gaf58823a56eb36cfd22e582ab1ea3d015)enum [bt\_audio\_codec\_cap\_type](group__bt__audio.md#gaf58823a56eb36cfd22e582ab1ea3d015) {

[ 68](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015af68f3f5665446de9b71c2f70e7aa762b) [BT\_AUDIO\_CODEC\_CAP\_TYPE\_FREQ](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015af68f3f5665446de9b71c2f70e7aa762b) = 0x01,

69

[ 71](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015a4a90a37cd6d8ca9d1ed984e4a122d510) [BT\_AUDIO\_CODEC\_CAP\_TYPE\_DURATION](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015a4a90a37cd6d8ca9d1ed984e4a122d510) = 0x02,

72

[ 74](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015a0cd3a3d31febc9e30137e9e21d4f7191) [BT\_AUDIO\_CODEC\_CAP\_TYPE\_CHAN\_COUNT](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015a0cd3a3d31febc9e30137e9e21d4f7191) = 0x03,

75

[ 77](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015ad074bed5f79946e2388584336d30cf46) [BT\_AUDIO\_CODEC\_CAP\_TYPE\_FRAME\_LEN](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015ad074bed5f79946e2388584336d30cf46) = 0x04,

78

[ 80](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015acba980896f080ac2ba81d1b66305bb41) [BT\_AUDIO\_CODEC\_CAP\_TYPE\_FRAME\_COUNT](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015acba980896f080ac2ba81d1b66305bb41) = 0x05,

81};

82

[ 84](group__bt__audio.md#gaafc1106d5d305874ee2f540c850ff5b4)enum [bt\_audio\_codec\_cap\_freq](group__bt__audio.md#gaafc1106d5d305874ee2f540c850ff5b4) {

[ 86](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a3d821d03771805107707f47dcdb71f83) [BT\_AUDIO\_CODEC\_CAP\_FREQ\_8KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a3d821d03771805107707f47dcdb71f83) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

87

[ 89](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a562c38a59cded025183a0f95d4a63c81) [BT\_AUDIO\_CODEC\_CAP\_FREQ\_11KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a562c38a59cded025183a0f95d4a63c81) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

90

[ 92](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4acfef6825ac865b1e590e7959a9270361) [BT\_AUDIO\_CODEC\_CAP\_FREQ\_16KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4acfef6825ac865b1e590e7959a9270361) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

93

[ 95](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ad7440157cf8864dfc5fd854482f3a982) [BT\_AUDIO\_CODEC\_CAP\_FREQ\_22KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ad7440157cf8864dfc5fd854482f3a982) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

96

[ 98](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4acf9ff8842d72d56d27eae692e4c4b956) [BT\_AUDIO\_CODEC\_CAP\_FREQ\_24KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4acf9ff8842d72d56d27eae692e4c4b956) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

99

[ 101](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a822ff105ab495c126c21d73bd90cbd9c) [BT\_AUDIO\_CODEC\_CAP\_FREQ\_32KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a822ff105ab495c126c21d73bd90cbd9c) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

102

[ 104](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ad28396f4b5a71d7c196e1a27bd17f8c3) [BT\_AUDIO\_CODEC\_CAP\_FREQ\_44KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ad28396f4b5a71d7c196e1a27bd17f8c3) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6),

105

[ 107](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a91ec17ee96b8e56e31ab545e5e8abe91) [BT\_AUDIO\_CODEC\_CAP\_FREQ\_48KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a91ec17ee96b8e56e31ab545e5e8abe91) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7),

108

[ 110](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a25cc72bd630446f5154c54402058a211) [BT\_AUDIO\_CODEC\_CAP\_FREQ\_88KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a25cc72bd630446f5154c54402058a211) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8),

111

[ 113](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ae802fea402f207238613275917846663) [BT\_AUDIO\_CODEC\_CAP\_FREQ\_96KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ae802fea402f207238613275917846663) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9),

114

[ 116](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a031d159eadf7ea1ba6b00b03bef26d2b) [BT\_AUDIO\_CODEC\_CAP\_FREQ\_176KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a031d159eadf7ea1ba6b00b03bef26d2b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10),

117

[ 119](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a0de8d0351153650c1b48934053e18890) [BT\_AUDIO\_CODEC\_CAP\_FREQ\_192KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a0de8d0351153650c1b48934053e18890) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11),

120

[ 122](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ae5ddc4504b7077e90be56f34ad8647c2) [BT\_AUDIO\_CODEC\_CAP\_FREQ\_384KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ae5ddc4504b7077e90be56f34ad8647c2) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12),

123

[ 125](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4adaaa42a6bb0c01d3819c604b6d5bbf02) [BT\_AUDIO\_CODEC\_CAP\_FREQ\_ANY](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4adaaa42a6bb0c01d3819c604b6d5bbf02) =

126 ([BT\_AUDIO\_CODEC\_CAP\_FREQ\_8KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a3d821d03771805107707f47dcdb71f83) | [BT\_AUDIO\_CODEC\_CAP\_FREQ\_11KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a562c38a59cded025183a0f95d4a63c81) |

127 [BT\_AUDIO\_CODEC\_CAP\_FREQ\_16KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4acfef6825ac865b1e590e7959a9270361) | [BT\_AUDIO\_CODEC\_CAP\_FREQ\_22KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ad7440157cf8864dfc5fd854482f3a982) |

128 [BT\_AUDIO\_CODEC\_CAP\_FREQ\_24KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4acf9ff8842d72d56d27eae692e4c4b956) | [BT\_AUDIO\_CODEC\_CAP\_FREQ\_32KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a822ff105ab495c126c21d73bd90cbd9c) |

129 [BT\_AUDIO\_CODEC\_CAP\_FREQ\_44KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ad28396f4b5a71d7c196e1a27bd17f8c3) | [BT\_AUDIO\_CODEC\_CAP\_FREQ\_48KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a91ec17ee96b8e56e31ab545e5e8abe91) |

130 [BT\_AUDIO\_CODEC\_CAP\_FREQ\_88KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a25cc72bd630446f5154c54402058a211) | [BT\_AUDIO\_CODEC\_CAP\_FREQ\_96KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ae802fea402f207238613275917846663) |

131 [BT\_AUDIO\_CODEC\_CAP\_FREQ\_176KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a031d159eadf7ea1ba6b00b03bef26d2b) | [BT\_AUDIO\_CODEC\_CAP\_FREQ\_192KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a0de8d0351153650c1b48934053e18890) |

132 [BT\_AUDIO\_CODEC\_CAP\_FREQ\_384KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ae5ddc4504b7077e90be56f34ad8647c2)),

133};

134

[ 136](group__bt__audio.md#gaf37e8e19f956afb3c3a413cbaa1a21f5)enum [bt\_audio\_codec\_cap\_frame\_dur](group__bt__audio.md#gaf37e8e19f956afb3c3a413cbaa1a21f5) {

[ 138](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a340878058d0beabeade33e0f3893d441) [BT\_AUDIO\_CODEC\_CAP\_DURATION\_7\_5](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a340878058d0beabeade33e0f3893d441) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

139

[ 141](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5afd423ac4270ff0df8ca6df7f5e4c799b) [BT\_AUDIO\_CODEC\_CAP\_DURATION\_10](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5afd423ac4270ff0df8ca6df7f5e4c799b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

142

[ 144](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a81d28ce43d69d4625e9a73b37c70347a) [BT\_AUDIO\_CODEC\_CAP\_DURATION\_ANY](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a81d28ce43d69d4625e9a73b37c70347a) =

145 ([BT\_AUDIO\_CODEC\_CAP\_DURATION\_7\_5](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a340878058d0beabeade33e0f3893d441) | [BT\_AUDIO\_CODEC\_CAP\_DURATION\_10](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5afd423ac4270ff0df8ca6df7f5e4c799b)),

146

[ 153](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a7ab1c63639cf93fdf2c2dfdf43424e91) [BT\_AUDIO\_CODEC\_CAP\_DURATION\_PREFER\_7\_5](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a7ab1c63639cf93fdf2c2dfdf43424e91) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

154

[ 161](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a9744473b3a29074c24cf0bbff35a5d8e) [BT\_AUDIO\_CODEC\_CAP\_DURATION\_PREFER\_10](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a9744473b3a29074c24cf0bbff35a5d8e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

162};

163

[ 165](group__bt__audio.md#gae695b5d17359967703f2509db1671fa5)enum [bt\_audio\_codec\_cap\_chan\_count](group__bt__audio.md#gae695b5d17359967703f2509db1671fa5) {

[ 167](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a1558716b36042597515df18ff277f8bc) [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_1](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a1558716b36042597515df18ff277f8bc) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

168

[ 170](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a13b236d93eb9c7516fdcf527313e16cd) [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_2](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a13b236d93eb9c7516fdcf527313e16cd) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

171

[ 173](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a17da27ec39a79c341c82549df891cb39) [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_3](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a17da27ec39a79c341c82549df891cb39) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

174

[ 176](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a0fdfa6bf69b104f04d22e4f968969ac2) [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_4](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a0fdfa6bf69b104f04d22e4f968969ac2) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

177

[ 179](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5ad08bc2ea0347a1ee8fd411a023b7ca51) [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_5](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5ad08bc2ea0347a1ee8fd411a023b7ca51) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

180

[ 182](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5af9f9dd0cac39793793e5c8c5e50b11b8) [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_6](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5af9f9dd0cac39793793e5c8c5e50b11b8) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

183

[ 185](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a86ef227772c7751b4ae75529e2a57b82) [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_7](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a86ef227772c7751b4ae75529e2a57b82) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6),

186

[ 188](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a50afa60bdd53172fab7a376ce374d943) [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_8](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a50afa60bdd53172fab7a376ce374d943) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7),

189

[ 191](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5aaf6f7179310c64b93b300ecfc29e4219) [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_ANY](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5aaf6f7179310c64b93b300ecfc29e4219) =

192 ([BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_1](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a1558716b36042597515df18ff277f8bc) | [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_2](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a13b236d93eb9c7516fdcf527313e16cd) |

193 [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_3](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a17da27ec39a79c341c82549df891cb39) | [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_4](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a0fdfa6bf69b104f04d22e4f968969ac2) |

194 [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_5](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5ad08bc2ea0347a1ee8fd411a023b7ca51) | [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_6](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5af9f9dd0cac39793793e5c8c5e50b11b8) |

195 [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_7](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a86ef227772c7751b4ae75529e2a57b82) | [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_8](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a50afa60bdd53172fab7a376ce374d943)),

196};

197

[ 199](group__bt__audio.md#gac1251f8a35b5e343eeeff87f22f8ab10)#define BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_MIN 1

[ 201](group__bt__audio.md#gad91341739d394f92ffc4988b614f47b6)#define BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_MAX 8

202

[ 213](group__bt__audio.md#ga8f835266fabd6461216fe13e1b3b3a0f)#define BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_SUPPORT(...) \

214 ((enum bt\_audio\_codec\_cap\_chan\_count)((FOR\_EACH(BIT, (|), \_\_VA\_ARGS\_\_)) >> 1))

215

[ 217](structbt__audio__codec__octets__per__codec__frame.md)struct [bt\_audio\_codec\_octets\_per\_codec\_frame](structbt__audio__codec__octets__per__codec__frame.md) {

[ 219](structbt__audio__codec__octets__per__codec__frame.md#aa8b234fa137273cd16230ebabc5f8ef4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [min](structbt__audio__codec__octets__per__codec__frame.md#aa8b234fa137273cd16230ebabc5f8ef4);

[ 221](structbt__audio__codec__octets__per__codec__frame.md#ae09686799077b13e78b856b1e7e63b6a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max](structbt__audio__codec__octets__per__codec__frame.md#ae09686799077b13e78b856b1e7e63b6a);

222};

223

[ 230](group__bt__audio.md#ga9230ec4d7518bd243207ba2decb1a974)enum [bt\_audio\_codec\_cfg\_type](group__bt__audio.md#ga9230ec4d7518bd243207ba2decb1a974) {

[ 232](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974a49849b389d553535ea222c9ae63bccc3) [BT\_AUDIO\_CODEC\_CFG\_FREQ](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974a49849b389d553535ea222c9ae63bccc3) = 0x01,

233

[ 235](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974a8e2fae97b1565b0fa0ff988a47928223) [BT\_AUDIO\_CODEC\_CFG\_DURATION](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974a8e2fae97b1565b0fa0ff988a47928223) = 0x02,

236

[ 238](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974ad53deb048fb0ce4d4428df4f477718b2) [BT\_AUDIO\_CODEC\_CFG\_CHAN\_ALLOC](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974ad53deb048fb0ce4d4428df4f477718b2) = 0x03,

239

[ 241](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974a85d41856175c11b1193ebdd58b83d6e2) [BT\_AUDIO\_CODEC\_CFG\_FRAME\_LEN](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974a85d41856175c11b1193ebdd58b83d6e2) = 0x04,

242

[ 244](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974abbc2279f5d029278d9367f08a1152aa8) [BT\_AUDIO\_CODEC\_CFG\_FRAME\_BLKS\_PER\_SDU](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974abbc2279f5d029278d9367f08a1152aa8) = 0x05,

245};

246

[ 248](group__bt__audio.md#ga8e99fb678cc011bb8c9f6e1858bae0d7)enum [bt\_audio\_codec\_cfg\_freq](group__bt__audio.md#ga8e99fb678cc011bb8c9f6e1858bae0d7) {

[ 250](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a7018d3fb612d4730b880ef0bb2d20b9a) [BT\_AUDIO\_CODEC\_CFG\_FREQ\_8KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a7018d3fb612d4730b880ef0bb2d20b9a) = 0x01,

251

[ 253](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aa8d8018b050a8c029b4b60c706d771f8) [BT\_AUDIO\_CODEC\_CFG\_FREQ\_11KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aa8d8018b050a8c029b4b60c706d771f8) = 0x02,

254

[ 256](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7ab097ae9f9ad963fee64e61eaf2663245) [BT\_AUDIO\_CODEC\_CFG\_FREQ\_16KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7ab097ae9f9ad963fee64e61eaf2663245) = 0x03,

257

[ 259](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a68f8411a83f60ec4c6bb9fa65fdd7048) [BT\_AUDIO\_CODEC\_CFG\_FREQ\_22KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a68f8411a83f60ec4c6bb9fa65fdd7048) = 0x04,

260

[ 262](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a0d6d0f278628681f8ef5dc3797bf5275) [BT\_AUDIO\_CODEC\_CFG\_FREQ\_24KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a0d6d0f278628681f8ef5dc3797bf5275) = 0x05,

263

[ 265](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a3ce97404475ad182125ad64aba66077e) [BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a3ce97404475ad182125ad64aba66077e) = 0x06,

266

[ 268](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aa701e855c950fdcdd66d4dbaaf75fb84) [BT\_AUDIO\_CODEC\_CFG\_FREQ\_44KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aa701e855c950fdcdd66d4dbaaf75fb84) = 0x07,

269

[ 271](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a2b7163ba4c486167d3e81c2aa4216f11) [BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a2b7163ba4c486167d3e81c2aa4216f11) = 0x08,

272

[ 274](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aff685ebe62909eea8512b7deac0df409) [BT\_AUDIO\_CODEC\_CFG\_FREQ\_88KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aff685ebe62909eea8512b7deac0df409) = 0x09,

275

[ 277](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a79e7a473d3f7d6803f3b8b7843c40c60) [BT\_AUDIO\_CODEC\_CFG\_FREQ\_96KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a79e7a473d3f7d6803f3b8b7843c40c60) = 0x0a,

278

[ 280](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a85037a2eb4a64376a0a436ab43263126) [BT\_AUDIO\_CODEC\_CFG\_FREQ\_176KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a85037a2eb4a64376a0a436ab43263126) = 0x0b,

281

[ 283](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aa85a51db272ef019e5cce5ec3982f8c7) [BT\_AUDIO\_CODEC\_CFG\_FREQ\_192KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aa85a51db272ef019e5cce5ec3982f8c7) = 0x0c,

284

[ 286](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a44cccbd3e7afc25f964b3c2c571d4be4) [BT\_AUDIO\_CODEC\_CFG\_FREQ\_384KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a44cccbd3e7afc25f964b3c2c571d4be4) = 0x0d,

287};

288

[ 290](group__bt__audio.md#ga83701b5eadfcbc9b84dc0b1a85ebeb74)enum [bt\_audio\_codec\_cfg\_frame\_dur](group__bt__audio.md#ga83701b5eadfcbc9b84dc0b1a85ebeb74) {

[ 292](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ad2491c0ded7c7f489bdeffe024463272) [BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ad2491c0ded7c7f489bdeffe024463272) = 0x00,

293

[ 295](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ab6a0dd3bbe587ff5ba110675a01514a7) [BT\_AUDIO\_CODEC\_CFG\_DURATION\_10](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ab6a0dd3bbe587ff5ba110675a01514a7) = 0x01,

296};

297

[ 303](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3)enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) {

[ 305](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a3cfcfa76adc5effdc1aa95d75e5da37a) [BT\_AUDIO\_CONTEXT\_TYPE\_PROHIBITED](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a3cfcfa76adc5effdc1aa95d75e5da37a) = 0,

[ 310](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3aad96be1265bd1be4c937c687335e33f5) [BT\_AUDIO\_CONTEXT\_TYPE\_UNSPECIFIED](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3aad96be1265bd1be4c937c687335e33f5) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 315](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a8a6262c1cf4e4591a7b92b4f8f329f9e) [BT\_AUDIO\_CONTEXT\_TYPE\_CONVERSATIONAL](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a8a6262c1cf4e4591a7b92b4f8f329f9e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 317](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a43d67936976a5c041027d15d66c21a5e) [BT\_AUDIO\_CONTEXT\_TYPE\_MEDIA](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a43d67936976a5c041027d15d66c21a5e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 322](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a652ad83b9eb524c62933bf87a8ecb730) [BT\_AUDIO\_CONTEXT\_TYPE\_GAME](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a652ad83b9eb524c62933bf87a8ecb730) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

[ 324](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a2e3af6f4ca620f91d9266257f842ddd4) [BT\_AUDIO\_CONTEXT\_TYPE\_INSTRUCTIONAL](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a2e3af6f4ca620f91d9266257f842ddd4) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

[ 326](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a7e208290ddc2f92ac78ff4a22b20ca7e) [BT\_AUDIO\_CONTEXT\_TYPE\_VOICE\_ASSISTANTS](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a7e208290ddc2f92ac78ff4a22b20ca7e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

[ 331](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a42c80228bda513d5a59d4d836e73bd55) [BT\_AUDIO\_CONTEXT\_TYPE\_LIVE](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a42c80228bda513d5a59d4d836e73bd55) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6),

[ 336](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a6956a9e43433e2800fd36c7022e039d9) [BT\_AUDIO\_CONTEXT\_TYPE\_SOUND\_EFFECTS](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a6956a9e43433e2800fd36c7022e039d9) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7),

[ 341](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a06df6f713bb68b197be75bf821d5d377) [BT\_AUDIO\_CONTEXT\_TYPE\_NOTIFICATIONS](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a06df6f713bb68b197be75bf821d5d377) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8),

[ 346](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a422bb29f035583b7319456a679f880b3) [BT\_AUDIO\_CONTEXT\_TYPE\_RINGTONE](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a422bb29f035583b7319456a679f880b3) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9),

[ 351](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a915d05a728f3e083f290766a970dabb6) [BT\_AUDIO\_CONTEXT\_TYPE\_ALERTS](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a915d05a728f3e083f290766a970dabb6) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10),

[ 353](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a132abd2f9ac7be62d1306efc6bc8b7d1) [BT\_AUDIO\_CONTEXT\_TYPE\_EMERGENCY\_ALARM](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a132abd2f9ac7be62d1306efc6bc8b7d1) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11),

354};

355

[ 359](group__bt__audio.md#ga6320f86aab9b227385bdf52a9ff3985b)#define BT\_AUDIO\_CONTEXT\_TYPE\_ANY (BT\_AUDIO\_CONTEXT\_TYPE\_UNSPECIFIED | \

360 BT\_AUDIO\_CONTEXT\_TYPE\_CONVERSATIONAL | \

361 BT\_AUDIO\_CONTEXT\_TYPE\_MEDIA | \

362 BT\_AUDIO\_CONTEXT\_TYPE\_GAME | \

363 BT\_AUDIO\_CONTEXT\_TYPE\_INSTRUCTIONAL | \

364 BT\_AUDIO\_CONTEXT\_TYPE\_VOICE\_ASSISTANTS | \

365 BT\_AUDIO\_CONTEXT\_TYPE\_LIVE | \

366 BT\_AUDIO\_CONTEXT\_TYPE\_SOUND\_EFFECTS | \

367 BT\_AUDIO\_CONTEXT\_TYPE\_NOTIFICATIONS | \

368 BT\_AUDIO\_CONTEXT\_TYPE\_RINGTONE | \

369 BT\_AUDIO\_CONTEXT\_TYPE\_ALERTS | \

370 BT\_AUDIO\_CONTEXT\_TYPE\_EMERGENCY\_ALARM)

371

[ 378](group__bt__audio.md#ga6d4aff1f93dc0b902e4b5d1355f15760)enum [bt\_audio\_parental\_rating](group__bt__audio.md#ga6d4aff1f93dc0b902e4b5d1355f15760) {

[ 380](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760aecf628bbd76651215232c8bfed04aa2c) [BT\_AUDIO\_PARENTAL\_RATING\_NO\_RATING](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760aecf628bbd76651215232c8bfed04aa2c) = 0x00,

[ 382](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760ad6bba6a3b9537fcf913f798ab9a525f1) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_ANY](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760ad6bba6a3b9537fcf913f798ab9a525f1) = 0x01,

[ 384](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a8a8476abac3a569bd470a5237642c526) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_5\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a8a8476abac3a569bd470a5237642c526) = 0x02,

[ 386](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760accb959ba21c1238c70c594b5cdc3ebdc) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_6\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760accb959ba21c1238c70c594b5cdc3ebdc) = 0x03,

[ 388](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a69508e569059bde1fed1b3fb3db1547a) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_7\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a69508e569059bde1fed1b3fb3db1547a) = 0x04,

[ 390](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a9ed111f80d0671bb8b4e0a304ff0b0e4) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_8\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a9ed111f80d0671bb8b4e0a304ff0b0e4) = 0x05,

[ 392](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760aaabe26ebaa4b84684005440176ad86dd) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_9\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760aaabe26ebaa4b84684005440176ad86dd) = 0x06,

[ 394](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a4210d67d4506f8b9defb5fae32ae30d2) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_10\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a4210d67d4506f8b9defb5fae32ae30d2) = 0x07,

[ 396](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760ac402ee4c06b92f0cc36774cf409cbbd0) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_11\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760ac402ee4c06b92f0cc36774cf409cbbd0) = 0x08,

[ 398](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760ac68caf6719391afbef79e0c579dc96e7) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_12\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760ac68caf6719391afbef79e0c579dc96e7) = 0x09,

[ 400](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760aa680247699538d256111e18af1a2d15d) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_13\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760aa680247699538d256111e18af1a2d15d) = 0x0A,

[ 402](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760aef216d59983eccb86e90c493b8c17d86) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_14\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760aef216d59983eccb86e90c493b8c17d86) = 0x0B,

[ 404](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a3fe7bc3216a458ec3e5c6e177f43c077) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_15\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a3fe7bc3216a458ec3e5c6e177f43c077) = 0x0C,

[ 406](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a779c5dd14e5f88e8e6bb247dc66d9c92) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_16\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a779c5dd14e5f88e8e6bb247dc66d9c92) = 0x0D,

[ 408](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a7d0794fe6796f19ff7e58819728751ff) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_17\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a7d0794fe6796f19ff7e58819728751ff) = 0x0E,

[ 410](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a22167e0c033c176f592a447b14c30071) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_18\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a22167e0c033c176f592a447b14c30071) = 0x0F

411};

412

[ 414](group__bt__audio.md#ga16d403ec4db7be997682331ad365ff5f)enum [bt\_audio\_active\_state](group__bt__audio.md#ga16d403ec4db7be997682331ad365ff5f) {

[ 416](group__bt__audio.md#gga16d403ec4db7be997682331ad365ff5fade27604ea8fd592aa5d0958e2ccde4f3) [BT\_AUDIO\_ACTIVE\_STATE\_DISABLED](group__bt__audio.md#gga16d403ec4db7be997682331ad365ff5fade27604ea8fd592aa5d0958e2ccde4f3) = 0x00,

[ 418](group__bt__audio.md#gga16d403ec4db7be997682331ad365ff5fa6d062944e9c49001666769601ba1c940) [BT\_AUDIO\_ACTIVE\_STATE\_ENABLED](group__bt__audio.md#gga16d403ec4db7be997682331ad365ff5fa6d062944e9c49001666769601ba1c940) = 0x01,

419};

420

[ 422](group__bt__audio.md#ga207fbf0fbca9b24cba02c7f1d184e7f5)enum [bt\_audio\_assisted\_listening\_stream](group__bt__audio.md#ga207fbf0fbca9b24cba02c7f1d184e7f5) {

[ 424](group__bt__audio.md#gga207fbf0fbca9b24cba02c7f1d184e7f5ab1714206feaa04b3be586ddb33ed5285) [BT\_AUDIO\_ASSISTED\_LISTENING\_STREAM\_UNSPECIFIED](group__bt__audio.md#gga207fbf0fbca9b24cba02c7f1d184e7f5ab1714206feaa04b3be586ddb33ed5285) = 0x00,

425};

426

[ 432](group__bt__audio.md#gab53d0dd62bceff97cf8eed7d8cf80354)enum [bt\_audio\_metadata\_type](group__bt__audio.md#gab53d0dd62bceff97cf8eed7d8cf80354) {

[ 443](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354aac28d2a0dc883affa60b7a70f678ed9a) [BT\_AUDIO\_METADATA\_TYPE\_PREF\_CONTEXT](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354aac28d2a0dc883affa60b7a70f678ed9a) = 0x01,

444

[ 455](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a95f128b11584ee22100ae65ce751dbaa) [BT\_AUDIO\_METADATA\_TYPE\_STREAM\_CONTEXT](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a95f128b11584ee22100ae65ce751dbaa) = 0x02,

456

[ 458](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a02f91ea7fb6be631687d843ad7bf4ac7) [BT\_AUDIO\_METADATA\_TYPE\_PROGRAM\_INFO](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a02f91ea7fb6be631687d843ad7bf4ac7) = 0x03,

459

[ 466](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354af38d342d907c3903121a03bb8394efb1) [BT\_AUDIO\_METADATA\_TYPE\_LANG](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354af38d342d907c3903121a03bb8394efb1) = 0x04,

467

[ 469](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a37b5552e04734392dc6c6eb9e19b377b) [BT\_AUDIO\_METADATA\_TYPE\_CCID\_LIST](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a37b5552e04734392dc6c6eb9e19b377b) = 0x05,

470

[ 476](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a7a83f397dc5dbe6e6d60a994cccdc613) [BT\_AUDIO\_METADATA\_TYPE\_PARENTAL\_RATING](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a7a83f397dc5dbe6e6d60a994cccdc613) = 0x06,

477

[ 479](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a58971ea21b5045e56a0e1ca838358922) [BT\_AUDIO\_METADATA\_TYPE\_PROGRAM\_INFO\_URI](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a58971ea21b5045e56a0e1ca838358922) = 0x07,

480

[ 486](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354af220c40d351ec5e236cd41a5944da5fc) [BT\_AUDIO\_METADATA\_TYPE\_AUDIO\_STATE](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354af220c40d351ec5e236cd41a5944da5fc) = 0x08,

487

[ 489](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a4b9cc5b82a1dbfc3db69bb12747443f1) [BT\_AUDIO\_METADATA\_TYPE\_BROADCAST\_IMMEDIATE](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a4b9cc5b82a1dbfc3db69bb12747443f1) = 0x09,

490

[ 496](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a40aad5cb3574e6e4e7bc955bc12760bf) [BT\_AUDIO\_METADATA\_TYPE\_ASSISTED\_LISTENING\_STREAM](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a40aad5cb3574e6e4e7bc955bc12760bf) = 0x0A,

497

[ 499](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354ada34d453c8ce75a155c59c371a67d8a6) [BT\_AUDIO\_METADATA\_TYPE\_BROADCAST\_NAME](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354ada34d453c8ce75a155c59c371a67d8a6) = 0x0B,

500

[ 502](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a0b5a8cd34bad81ac53c657c3cd9ddb39) [BT\_AUDIO\_METADATA\_TYPE\_EXTENDED](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a0b5a8cd34bad81ac53c657c3cd9ddb39) = 0xFE,

503

[ 505](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a30fbc4a159e64174b22f195f29012286) [BT\_AUDIO\_METADATA\_TYPE\_VENDOR](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a30fbc4a159e64174b22f195f29012286) = 0xFF,

506};

507

[ 513](group__bt__audio.md#ga86a7e9ca661a3b13b7c59d41d206156e)#define BT\_AUDIO\_METADATA\_TYPE\_IS\_KNOWN(\_type) \

514 (IN\_RANGE((\_type), BT\_AUDIO\_METADATA\_TYPE\_PREF\_CONTEXT, \

515 BT\_AUDIO\_METADATA\_TYPE\_BROADCAST\_IMMEDIATE) || \

516 (\_type) == BT\_AUDIO\_METADATA\_TYPE\_EXTENDED || (\_type) == BT\_AUDIO\_METADATA\_TYPE\_VENDOR)

517

[ 523](group__bt__audio.md#ga41db714fa87e85896a52427399633bb4)#define BT\_AUDIO\_UNICAST\_ANNOUNCEMENT\_GENERAL 0x00

[ 525](group__bt__audio.md#ga56c14acb7f182a413fdecac4e271c5cc)#define BT\_AUDIO\_UNICAST\_ANNOUNCEMENT\_TARGETED 0x01

527

[ 536](group__bt__audio.md#gaddc49e39465798ae4c0cbe345e0b50d7)#define BT\_AUDIO\_CODEC\_DATA(\_type, \_bytes...) \

537 (sizeof((uint8\_t)\_type) + sizeof((uint8\_t[]){\_bytes})), (\_type), \_bytes

538

[ 548](group__bt__audio.md#gaefed7a013e282c63c9b5cbbdcdc67448)#define BT\_AUDIO\_CODEC\_CFG(\_id, \_cid, \_vid, \_data, \_meta) \

549 ((struct bt\_audio\_codec\_cfg){ \

550 /\* Use HCI data path as default, can be overwritten by application \*/ \

551 .path\_id = BT\_ISO\_DATA\_PATH\_HCI, \

552 .ctlr\_transcode = false, \

553 .id = \_id, \

554 .cid = \_cid, \

555 .vid = \_vid, \

556 .data\_len = sizeof((uint8\_t[])\_data), \

557 .data = \_data, \

558 .meta\_len = sizeof((uint8\_t[])\_meta), \

559 .meta = \_meta, \

560 })

561

[ 571](group__bt__audio.md#ga6b99f589f6cdcd9e48a83f729a7a4698)#define BT\_AUDIO\_CODEC\_CAP(\_id, \_cid, \_vid, \_data, \_meta) \

572 ((struct bt\_audio\_codec\_cap){ \

573 /\* Use HCI data path as default, can be overwritten by application \*/ \

574 .path\_id = BT\_ISO\_DATA\_PATH\_HCI, \

575 .ctlr\_transcode = false, \

576 .id = (\_id), \

577 .cid = (\_cid), \

578 .vid = (\_vid), \

579 .data\_len = sizeof((uint8\_t[])\_data), \

580 .data = \_data, \

581 .meta\_len = sizeof((uint8\_t[])\_meta), \

582 .meta = \_meta, \

583 })

584

[ 590](group__bt__audio.md#ga61230848c02098352320fe751332c4e8)enum [bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8) {

[ 592](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a8f476de613cdcb2f9f677d40291aa5df) [BT\_AUDIO\_LOCATION\_MONO\_AUDIO](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a8f476de613cdcb2f9f677d40291aa5df) = 0,

[ 594](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ac658188fa6f1b4f248a149d0bde1e41b) [BT\_AUDIO\_LOCATION\_FRONT\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ac658188fa6f1b4f248a149d0bde1e41b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 596](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a26d5ba460642bcf7fb2fc950082b70b3) [BT\_AUDIO\_LOCATION\_FRONT\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a26d5ba460642bcf7fb2fc950082b70b3) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 598](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a06b34e67c9931f8b26562218cba51337) [BT\_AUDIO\_LOCATION\_FRONT\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a06b34e67c9931f8b26562218cba51337) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 600](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ac4c09f948266f2c9c65b3bc16da2f3f6) [BT\_AUDIO\_LOCATION\_LOW\_FREQ\_EFFECTS\_1](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ac4c09f948266f2c9c65b3bc16da2f3f6) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

[ 602](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a96906ff7918b0a3e3e7efe73a08d9896) [BT\_AUDIO\_LOCATION\_BACK\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a96906ff7918b0a3e3e7efe73a08d9896) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

[ 604](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a43f5070c2b4d39c38fa7900595d9b1aa) [BT\_AUDIO\_LOCATION\_BACK\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a43f5070c2b4d39c38fa7900595d9b1aa) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

[ 606](group__bt__audio.md#gga61230848c02098352320fe751332c4e8af02a9d46877b742e8730bbf3dd6ad22e) [BT\_AUDIO\_LOCATION\_FRONT\_LEFT\_OF\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8af02a9d46877b742e8730bbf3dd6ad22e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6),

[ 608](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a725707ae4703a1f9b970de5b1e4e5692) [BT\_AUDIO\_LOCATION\_FRONT\_RIGHT\_OF\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a725707ae4703a1f9b970de5b1e4e5692) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7),

[ 610](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ae22cd1e458d8ff503741bf48262c7983) [BT\_AUDIO\_LOCATION\_BACK\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ae22cd1e458d8ff503741bf48262c7983) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8),

[ 612](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a0c304bdd529ad66acb71001caa1b361b) [BT\_AUDIO\_LOCATION\_LOW\_FREQ\_EFFECTS\_2](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a0c304bdd529ad66acb71001caa1b361b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9),

[ 614](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ab8e52c69b894e382f0f09cc370337064) [BT\_AUDIO\_LOCATION\_SIDE\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ab8e52c69b894e382f0f09cc370337064) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10),

[ 616](group__bt__audio.md#gga61230848c02098352320fe751332c4e8aa01ad94f71defd158d8cfe25936341cd) [BT\_AUDIO\_LOCATION\_SIDE\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8aa01ad94f71defd158d8cfe25936341cd) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11),

[ 618](group__bt__audio.md#gga61230848c02098352320fe751332c4e8aa093e6218e213eac5677766e01f5c1c9) [BT\_AUDIO\_LOCATION\_TOP\_FRONT\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8aa093e6218e213eac5677766e01f5c1c9) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12),

[ 620](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a60b154a216d8e029deac7305500eaf2d) [BT\_AUDIO\_LOCATION\_TOP\_FRONT\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a60b154a216d8e029deac7305500eaf2d) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13),

[ 622](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ac32ed6f456be2fb2d9af2c7b255f3a4e) [BT\_AUDIO\_LOCATION\_TOP\_FRONT\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ac32ed6f456be2fb2d9af2c7b255f3a4e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14),

[ 624](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a555361fafade3bfb27dc713666757a1f) [BT\_AUDIO\_LOCATION\_TOP\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a555361fafade3bfb27dc713666757a1f) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15),

[ 626](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a07e699c28bd847de3d85645dceb2ff06) [BT\_AUDIO\_LOCATION\_TOP\_BACK\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a07e699c28bd847de3d85645dceb2ff06) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(16),

[ 628](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a8e81b80f732b0037493712b4baa21a69) [BT\_AUDIO\_LOCATION\_TOP\_BACK\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a8e81b80f732b0037493712b4baa21a69) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(17),

[ 630](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ae846b2f4186b46d3690c71071c41c7d6) [BT\_AUDIO\_LOCATION\_TOP\_SIDE\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ae846b2f4186b46d3690c71071c41c7d6) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(18),

[ 632](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a1cf8dea66e42f75ca85ba55124829a59) [BT\_AUDIO\_LOCATION\_TOP\_SIDE\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a1cf8dea66e42f75ca85ba55124829a59) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(19),

[ 634](group__bt__audio.md#gga61230848c02098352320fe751332c4e8aebae1f0f2537a806672820fb74eba5dd) [BT\_AUDIO\_LOCATION\_TOP\_BACK\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8aebae1f0f2537a806672820fb74eba5dd) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(20),

[ 636](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ad0be8f720f03feb18a23e77f0eff6376) [BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ad0be8f720f03feb18a23e77f0eff6376) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(21),

[ 638](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ac1e355baee6ca0907356d72f0d4edb29) [BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ac1e355baee6ca0907356d72f0d4edb29) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(22),

[ 640](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a33d0f7c266f21fd086386f8c29ee31e8) [BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a33d0f7c266f21fd086386f8c29ee31e8) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(23),

[ 642](group__bt__audio.md#gga61230848c02098352320fe751332c4e8acba90183626ad85c21692b7edd87133d) [BT\_AUDIO\_LOCATION\_FRONT\_LEFT\_WIDE](group__bt__audio.md#gga61230848c02098352320fe751332c4e8acba90183626ad85c21692b7edd87133d) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(24),

[ 644](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a8649be1d5b7e8b312fc3374039cc0a71) [BT\_AUDIO\_LOCATION\_FRONT\_RIGHT\_WIDE](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a8649be1d5b7e8b312fc3374039cc0a71) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(25),

[ 646](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a568a581c0ad653177f5d148d04bef0b6) [BT\_AUDIO\_LOCATION\_LEFT\_SURROUND](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a568a581c0ad653177f5d148d04bef0b6) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(26),

[ 648](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a97954db823b6c6bed660ff2717600a5e) [BT\_AUDIO\_LOCATION\_RIGHT\_SURROUND](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a97954db823b6c6bed660ff2717600a5e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(27),

649};

650

[ 654](group__bt__audio.md#ga90688f158fe999ed3aa9c759c8245fcc)#define BT\_AUDIO\_LOCATION\_ANY (BT\_AUDIO\_LOCATION\_FRONT\_LEFT | \

655 BT\_AUDIO\_LOCATION\_FRONT\_RIGHT | \

656 BT\_AUDIO\_LOCATION\_FRONT\_CENTER | \

657 BT\_AUDIO\_LOCATION\_LOW\_FREQ\_EFFECTS\_1 | \

658 BT\_AUDIO\_LOCATION\_BACK\_LEFT | \

659 BT\_AUDIO\_LOCATION\_BACK\_RIGHT | \

660 BT\_AUDIO\_LOCATION\_FRONT\_LEFT\_OF\_CENTER | \

661 BT\_AUDIO\_LOCATION\_FRONT\_RIGHT\_OF\_CENTER | \

662 BT\_AUDIO\_LOCATION\_BACK\_CENTER | \

663 BT\_AUDIO\_LOCATION\_LOW\_FREQ\_EFFECTS\_2 | \

664 BT\_AUDIO\_LOCATION\_SIDE\_LEFT | \

665 BT\_AUDIO\_LOCATION\_SIDE\_RIGHT | \

666 BT\_AUDIO\_LOCATION\_TOP\_FRONT\_LEFT | \

667 BT\_AUDIO\_LOCATION\_TOP\_FRONT\_RIGHT | \

668 BT\_AUDIO\_LOCATION\_TOP\_FRONT\_CENTER | \

669 BT\_AUDIO\_LOCATION\_TOP\_CENTER | \

670 BT\_AUDIO\_LOCATION\_TOP\_BACK\_LEFT | \

671 BT\_AUDIO\_LOCATION\_TOP\_BACK\_RIGHT | \

672 BT\_AUDIO\_LOCATION\_TOP\_SIDE\_LEFT | \

673 BT\_AUDIO\_LOCATION\_TOP\_SIDE\_RIGHT | \

674 BT\_AUDIO\_LOCATION\_TOP\_BACK\_CENTER | \

675 BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_CENTER | \

676 BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_LEFT | \

677 BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_RIGHT | \

678 BT\_AUDIO\_LOCATION\_FRONT\_LEFT\_WIDE | \

679 BT\_AUDIO\_LOCATION\_FRONT\_RIGHT\_WIDE | \

680 BT\_AUDIO\_LOCATION\_LEFT\_SURROUND | \

681 BT\_AUDIO\_LOCATION\_RIGHT\_SURROUND)

682

[ 684](structbt__audio__codec__cap.md)struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) {

[ 690](structbt__audio__codec__cap.md#a822a06f815091cc580ca2e5bbb3126f7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [path\_id](structbt__audio__codec__cap.md#a822a06f815091cc580ca2e5bbb3126f7);

[ 696](structbt__audio__codec__cap.md#a900a77db09e72de61d4ff652c6dbb10b) bool [ctlr\_transcode](structbt__audio__codec__cap.md#a900a77db09e72de61d4ff652c6dbb10b);

[ 698](structbt__audio__codec__cap.md#ae3892731e7ca05f3ec426c70f0d9e1a9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [id](structbt__audio__codec__cap.md#ae3892731e7ca05f3ec426c70f0d9e1a9);

[ 700](structbt__audio__codec__cap.md#a763222d12a87958a5ba806303f98829a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [cid](structbt__audio__codec__cap.md#a763222d12a87958a5ba806303f98829a);

[ 702](structbt__audio__codec__cap.md#a3b91269e16a3d63b3128a527caa5e3ff) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [vid](structbt__audio__codec__cap.md#a3b91269e16a3d63b3128a527caa5e3ff);

703#if CONFIG\_BT\_AUDIO\_CODEC\_CAP\_MAX\_DATA\_SIZE > 0 || defined(\_\_DOXYGEN\_\_)

[ 705](structbt__audio__codec__cap.md#acf3e22c6db1533fff7015acbc7eca196) size\_t [data\_len](structbt__audio__codec__cap.md#acf3e22c6db1533fff7015acbc7eca196);

[ 707](structbt__audio__codec__cap.md#a455638aac9167d288a1e7a9fccabc49d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structbt__audio__codec__cap.md#a455638aac9167d288a1e7a9fccabc49d)[CONFIG\_BT\_AUDIO\_CODEC\_CAP\_MAX\_DATA\_SIZE];

708#endif /\* CONFIG\_BT\_AUDIO\_CODEC\_CAP\_MAX\_DATA\_SIZE > 0 \*/

709#if defined(CONFIG\_BT\_AUDIO\_CODEC\_CAP\_MAX\_METADATA\_SIZE) || defined(\_\_DOXYGEN\_\_)

[ 711](structbt__audio__codec__cap.md#afe806521d5aac36e9f6c6a0598500a8f) size\_t [meta\_len](structbt__audio__codec__cap.md#afe806521d5aac36e9f6c6a0598500a8f);

[ 713](structbt__audio__codec__cap.md#acec4f5e31752d81d4dbf441223e7f44c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [meta](structbt__audio__codec__cap.md#acec4f5e31752d81d4dbf441223e7f44c)[CONFIG\_BT\_AUDIO\_CODEC\_CAP\_MAX\_METADATA\_SIZE];

714#endif /\* CONFIG\_BT\_AUDIO\_CODEC\_CAP\_MAX\_METADATA\_SIZE \*/

715};

716

[ 718](structbt__audio__codec__cfg.md)struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) {

[ 724](structbt__audio__codec__cfg.md#a9386056bb02908407c9e3aad48abbd87) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [path\_id](structbt__audio__codec__cfg.md#a9386056bb02908407c9e3aad48abbd87);

[ 730](structbt__audio__codec__cfg.md#a9e2c8081950a0830ffc270245ab308c1) bool [ctlr\_transcode](structbt__audio__codec__cfg.md#a9e2c8081950a0830ffc270245ab308c1);

[ 732](structbt__audio__codec__cfg.md#aa2f99ec31ff3eb9b7b738bc8a1170f20) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [id](structbt__audio__codec__cfg.md#aa2f99ec31ff3eb9b7b738bc8a1170f20);

[ 734](structbt__audio__codec__cfg.md#a664e21bcd6002b21d4b1b53d866db32d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [cid](structbt__audio__codec__cfg.md#a664e21bcd6002b21d4b1b53d866db32d);

[ 736](structbt__audio__codec__cfg.md#a2996ab3f6ae1cab09ff5e3329b42468e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [vid](structbt__audio__codec__cfg.md#a2996ab3f6ae1cab09ff5e3329b42468e);

737#if CONFIG\_BT\_AUDIO\_CODEC\_CFG\_MAX\_DATA\_SIZE > 0 || defined(\_\_DOXYGEN\_\_)

[ 739](structbt__audio__codec__cfg.md#a8a5a789e9993a48ce4c83a2156c1f43c) size\_t [data\_len](structbt__audio__codec__cfg.md#a8a5a789e9993a48ce4c83a2156c1f43c);

[ 741](structbt__audio__codec__cfg.md#ad3709d5321f6faeb392452cb3b21023b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structbt__audio__codec__cfg.md#ad3709d5321f6faeb392452cb3b21023b)[CONFIG\_BT\_AUDIO\_CODEC\_CFG\_MAX\_DATA\_SIZE];

742#endif /\* CONFIG\_BT\_AUDIO\_CODEC\_CFG\_MAX\_DATA\_SIZE > 0 \*/

743#if CONFIG\_BT\_AUDIO\_CODEC\_CFG\_MAX\_METADATA\_SIZE > 0 || defined(\_\_DOXYGEN\_\_)

[ 745](structbt__audio__codec__cfg.md#a1e69a5c017e9571b50aba721f86876fb) size\_t [meta\_len](structbt__audio__codec__cfg.md#a1e69a5c017e9571b50aba721f86876fb);

[ 747](structbt__audio__codec__cfg.md#a4f84974ea14b773ad8e2fd7c0ffa0c7f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [meta](structbt__audio__codec__cfg.md#a4f84974ea14b773ad8e2fd7c0ffa0c7f)[CONFIG\_BT\_AUDIO\_CODEC\_CFG\_MAX\_METADATA\_SIZE];

748#endif /\* CONFIG\_BT\_AUDIO\_CODEC\_CFG\_MAX\_METADATA\_SIZE > 0 \*/

749};

750

[ 765](group__bt__audio.md#gafd8574b16141162c95653f0aa2bf6ff7)int [bt\_audio\_data\_parse](group__bt__audio.md#gafd8574b16141162c95653f0aa2bf6ff7)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ltv[], size\_t size,

766 bool (\*func)(struct [bt\_data](structbt__data.md) \*data, void \*user\_data), void \*user\_data);

767

[ 783](group__bt__audio.md#gabbd1b9c46caa9a19de6c95b08c31e5b5)int [bt\_audio\_data\_get\_val](group__bt__audio.md#gabbd1b9c46caa9a19de6c95b08c31e5b5)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ltv\_data[], size\_t size, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type,

784 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*data);

785

[ 793](group__bt__audio.md#ga87415f8dddd38b3f5641c96e9722a44a)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bt\_audio\_get\_chan\_count](group__bt__audio.md#ga87415f8dddd38b3f5641c96e9722a44a)(enum [bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8) chan\_allocation);

794

[ 796](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f)enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) {

[ 803](group__bt__audio.md#gga5bd899fb5e4d844058184913866e462fa2adba49daa32ac7b040c3294f047ceb8) [BT\_AUDIO\_DIR\_SINK](group__bt__audio.md#gga5bd899fb5e4d844058184913866e462fa2adba49daa32ac7b040c3294f047ceb8) = 0x01,

[ 810](group__bt__audio.md#gga5bd899fb5e4d844058184913866e462fa868695a31ebf95402a4bae2469f3aa6c) [BT\_AUDIO\_DIR\_SOURCE](group__bt__audio.md#gga5bd899fb5e4d844058184913866e462fa868695a31ebf95402a4bae2469f3aa6c) = 0x02,

811};

812

821

[ 830](group__bt__audio__codec__cfg.md#ga2e557fe726a49dc99754da16f7cc60af)int [bt\_audio\_codec\_cfg\_freq\_to\_freq\_hz](group__bt__audio__codec__cfg.md#ga2e557fe726a49dc99754da16f7cc60af)(enum [bt\_audio\_codec\_cfg\_freq](group__bt__audio.md#ga8e99fb678cc011bb8c9f6e1858bae0d7) freq);

831

[ 840](group__bt__audio__codec__cfg.md#ga99ab4f6d2a18f2a9b4e3da47f63fc9e0)int [bt\_audio\_codec\_cfg\_freq\_hz\_to\_freq](group__bt__audio__codec__cfg.md#ga99ab4f6d2a18f2a9b4e3da47f63fc9e0)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) freq\_hz);

841

[ 852](group__bt__audio__codec__cfg.md#gad8525a57d35e3e34ea591f7e20e2512d)int [bt\_audio\_codec\_cfg\_get\_freq](group__bt__audio__codec__cfg.md#gad8525a57d35e3e34ea591f7e20e2512d)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg);

853

[ 864](group__bt__audio__codec__cfg.md#gac119989d5dcfa36becf4edd0ae7c6138)int [bt\_audio\_codec\_cfg\_set\_freq](group__bt__audio__codec__cfg.md#gac119989d5dcfa36becf4edd0ae7c6138)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

865 enum [bt\_audio\_codec\_cfg\_freq](group__bt__audio.md#ga8e99fb678cc011bb8c9f6e1858bae0d7) freq);

866

[ 875](group__bt__audio__codec__cfg.md#ga225e05df1f0d1efb709c972187901495)int [bt\_audio\_codec\_cfg\_frame\_dur\_to\_frame\_dur\_us](group__bt__audio__codec__cfg.md#ga225e05df1f0d1efb709c972187901495)(enum [bt\_audio\_codec\_cfg\_frame\_dur](group__bt__audio.md#ga83701b5eadfcbc9b84dc0b1a85ebeb74) frame\_dur);

876

[ 885](group__bt__audio__codec__cfg.md#ga0782a3d9254fb76b441c6c2492571556)int [bt\_audio\_codec\_cfg\_frame\_dur\_us\_to\_frame\_dur](group__bt__audio__codec__cfg.md#ga0782a3d9254fb76b441c6c2492571556)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) frame\_dur\_us);

886

[ 897](group__bt__audio__codec__cfg.md#ga2dd3afe41b22e989fb46614f89550007)int [bt\_audio\_codec\_cfg\_get\_frame\_dur](group__bt__audio__codec__cfg.md#ga2dd3afe41b22e989fb46614f89550007)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg);

898

[ 909](group__bt__audio__codec__cfg.md#ga7d8306f98cb00f06e68a1df417825f0d)int [bt\_audio\_codec\_cfg\_set\_frame\_dur](group__bt__audio__codec__cfg.md#ga7d8306f98cb00f06e68a1df417825f0d)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

910 enum [bt\_audio\_codec\_cfg\_frame\_dur](group__bt__audio.md#ga83701b5eadfcbc9b84dc0b1a85ebeb74) frame\_dur);

911

[ 932](group__bt__audio__codec__cfg.md#gae712e0f8e84aeb4ad2528da34907e29d)int [bt\_audio\_codec\_cfg\_get\_chan\_allocation](group__bt__audio__codec__cfg.md#gae712e0f8e84aeb4ad2528da34907e29d)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

933 enum [bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8) \*chan\_allocation,

934 bool fallback\_to\_default);

935

[ 946](group__bt__audio__codec__cfg.md#gafbbcd69fac18ed0201a5e0156209b049)int [bt\_audio\_codec\_cfg\_set\_chan\_allocation](group__bt__audio__codec__cfg.md#gafbbcd69fac18ed0201a5e0156209b049)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

947 enum [bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8) chan\_allocation);

948

[ 968](group__bt__audio__codec__cfg.md#ga503be053422217502d6108b045791e02)int [bt\_audio\_codec\_cfg\_get\_octets\_per\_frame](group__bt__audio__codec__cfg.md#ga503be053422217502d6108b045791e02)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg);

969

[ 980](group__bt__audio__codec__cfg.md#ga866cdec28194056dc9e274d0436b45c2)int [bt\_audio\_codec\_cfg\_set\_octets\_per\_frame](group__bt__audio__codec__cfg.md#ga866cdec28194056dc9e274d0436b45c2)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

981 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) octets\_per\_frame);

982

[ 1003](group__bt__audio__codec__cfg.md#gadba0723f9d8a9546b659fba139051374)int [bt\_audio\_codec\_cfg\_get\_frame\_blocks\_per\_sdu](group__bt__audio__codec__cfg.md#gadba0723f9d8a9546b659fba139051374)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1004 bool fallback\_to\_default);

1005

[ 1016](group__bt__audio__codec__cfg.md#gac9cf20bafbe24b34034bfb6ee7aaf03e)int [bt\_audio\_codec\_cfg\_set\_frame\_blocks\_per\_sdu](group__bt__audio__codec__cfg.md#gac9cf20bafbe24b34034bfb6ee7aaf03e)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1017 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) frame\_blocks);

1018

[ 1030](group__bt__audio__codec__cfg.md#ga707c679db0193197b56acabfb08f8d1f)int [bt\_audio\_codec\_cfg\_get\_val](group__bt__audio__codec__cfg.md#ga707c679db0193197b56acabfb08f8d1f)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1031 enum [bt\_audio\_codec\_cfg\_type](group__bt__audio.md#ga9230ec4d7518bd243207ba2decb1a974) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*data);

1032

[ 1045](group__bt__audio__codec__cfg.md#gab10f22938780530b1d1b95695382902e)int [bt\_audio\_codec\_cfg\_set\_val](group__bt__audio__codec__cfg.md#gab10f22938780530b1d1b95695382902e)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1046 enum [bt\_audio\_codec\_cfg\_type](group__bt__audio.md#ga9230ec4d7518bd243207ba2decb1a974) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data,

1047 size\_t data\_len);

1048

[ 1060](group__bt__audio__codec__cfg.md#gad3857d0ca008854df5966501caa261ba)int [bt\_audio\_codec\_cfg\_unset\_val](group__bt__audio__codec__cfg.md#gad3857d0ca008854df5966501caa261ba)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1061 enum [bt\_audio\_codec\_cfg\_type](group__bt__audio.md#ga9230ec4d7518bd243207ba2decb1a974) type);

1062

[ 1075](group__bt__audio__codec__cfg.md#gae98335e87394a491b4a311d867a5e32d)int [bt\_audio\_codec\_cfg\_meta\_get\_val](group__bt__audio__codec__cfg.md#gae98335e87394a491b4a311d867a5e32d)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type,

1076 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*data);

1077

[ 1090](group__bt__audio__codec__cfg.md#ga3e24c2ba8de502600e647cb2f84e3ec4)int [bt\_audio\_codec\_cfg\_meta\_set\_val](group__bt__audio__codec__cfg.md#ga3e24c2ba8de502600e647cb2f84e3ec4)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1091 enum [bt\_audio\_metadata\_type](group__bt__audio.md#gab53d0dd62bceff97cf8eed7d8cf80354) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data,

1092 size\_t data\_len);

1093

[ 1105](group__bt__audio__codec__cfg.md#gab46f830daa1d9a907f47eb2a9eed7337)int [bt\_audio\_codec\_cfg\_meta\_unset\_val](group__bt__audio__codec__cfg.md#gab46f830daa1d9a907f47eb2a9eed7337)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1106 enum [bt\_audio\_metadata\_type](group__bt__audio.md#gab53d0dd62bceff97cf8eed7d8cf80354) type);

[ 1122](group__bt__audio__codec__cfg.md#gaea087663426a49bb6ff4859800aecb84)int [bt\_audio\_codec\_cfg\_meta\_get\_pref\_context](group__bt__audio__codec__cfg.md#gaea087663426a49bb6ff4859800aecb84)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1123 bool fallback\_to\_default);

1124

[ 1135](group__bt__audio__codec__cfg.md#gab40bad609f17d24e7e0e9ffcebe4e912)int [bt\_audio\_codec\_cfg\_meta\_set\_pref\_context](group__bt__audio__codec__cfg.md#gab40bad609f17d24e7e0e9ffcebe4e912)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1136 enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) ctx);

1137

[ 1150](group__bt__audio__codec__cfg.md#ga4cc4e1bb941206e7f1541a57fc92b8e9)int [bt\_audio\_codec\_cfg\_meta\_get\_stream\_context](group__bt__audio__codec__cfg.md#ga4cc4e1bb941206e7f1541a57fc92b8e9)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg);

1151

[ 1162](group__bt__audio__codec__cfg.md#ga5cd2af1bb44c6eb5bafe824f005a77f0)int [bt\_audio\_codec\_cfg\_meta\_set\_stream\_context](group__bt__audio__codec__cfg.md#ga5cd2af1bb44c6eb5bafe824f005a77f0)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1163 enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) ctx);

1164

[ 1177](group__bt__audio__codec__cfg.md#ga03284b8474d65443d7ecc8bdfc6f04c6)int [bt\_audio\_codec\_cfg\_meta\_get\_program\_info](group__bt__audio__codec__cfg.md#ga03284b8474d65443d7ecc8bdfc6f04c6)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1178 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*program\_info);

1179

[ 1191](group__bt__audio__codec__cfg.md#ga2ca9e616d20d7513c60ce905f046ac7b)int [bt\_audio\_codec\_cfg\_meta\_set\_program\_info](group__bt__audio__codec__cfg.md#ga2ca9e616d20d7513c60ce905f046ac7b)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1192 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*program\_info, size\_t program\_info\_len);

1193

[ 1207](group__bt__audio__codec__cfg.md#ga55e3cbaeacf15fcb1f24a16eb28db99c)int [bt\_audio\_codec\_cfg\_meta\_get\_lang](group__bt__audio__codec__cfg.md#ga55e3cbaeacf15fcb1f24a16eb28db99c)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1208 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*lang);

1209

[ 1220](group__bt__audio__codec__cfg.md#ga54b7eadf072c397879c1dababa2a3be0)int [bt\_audio\_codec\_cfg\_meta\_set\_lang](group__bt__audio__codec__cfg.md#ga54b7eadf072c397879c1dababa2a3be0)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1221 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) lang[[BT\_AUDIO\_LANG\_SIZE](group__bt__audio.md#gab6e5f793d514626deca21940d35d8f21)]);

1222

[ 1235](group__bt__audio__codec__cfg.md#gaa0f9b9f608c7af881d5a928a3ae397b2)int [bt\_audio\_codec\_cfg\_meta\_get\_ccid\_list](group__bt__audio__codec__cfg.md#gaa0f9b9f608c7af881d5a928a3ae397b2)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1236 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*ccid\_list);

1237

[ 1249](group__bt__audio__codec__cfg.md#ga59716b95fcea3404ff8c078564b0e29c)int [bt\_audio\_codec\_cfg\_meta\_set\_ccid\_list](group__bt__audio__codec__cfg.md#ga59716b95fcea3404ff8c078564b0e29c)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1250 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*ccid\_list, size\_t ccid\_list\_len);

1251

[ 1264](group__bt__audio__codec__cfg.md#gaf0eecb02a05f0cc2b75ae9fb32c03913)int [bt\_audio\_codec\_cfg\_meta\_get\_parental\_rating](group__bt__audio__codec__cfg.md#gaf0eecb02a05f0cc2b75ae9fb32c03913)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg);

1265

[ 1276](group__bt__audio__codec__cfg.md#gab5d8b5877de4fe16c0e06a1d4f0d15ce)int [bt\_audio\_codec\_cfg\_meta\_set\_parental\_rating](group__bt__audio__codec__cfg.md#gab5d8b5877de4fe16c0e06a1d4f0d15ce)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1277 enum [bt\_audio\_parental\_rating](group__bt__audio.md#ga6d4aff1f93dc0b902e4b5d1355f15760) parental\_rating);

1278

[ 1291](group__bt__audio__codec__cfg.md#ga6bdbc0a0b929fdbdc75db479aec858df)int [bt\_audio\_codec\_cfg\_meta\_get\_program\_info\_uri](group__bt__audio__codec__cfg.md#ga6bdbc0a0b929fdbdc75db479aec858df)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1292 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*program\_info\_uri);

1293

[ 1305](group__bt__audio__codec__cfg.md#ga99163729034e816eaef7195505d5ae20)int [bt\_audio\_codec\_cfg\_meta\_set\_program\_info\_uri](group__bt__audio__codec__cfg.md#ga99163729034e816eaef7195505d5ae20)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1306 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*program\_info\_uri,

1307 size\_t program\_info\_uri\_len);

1308

[ 1321](group__bt__audio__codec__cfg.md#ga0fd6e6baf1b4f22d60768aaed6f42e8e)int [bt\_audio\_codec\_cfg\_meta\_get\_audio\_active\_state](group__bt__audio__codec__cfg.md#ga0fd6e6baf1b4f22d60768aaed6f42e8e)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg);

1322

[ 1333](group__bt__audio__codec__cfg.md#gaf869e7ce0c9dd467fb03e8503d36c58a)int [bt\_audio\_codec\_cfg\_meta\_set\_audio\_active\_state](group__bt__audio__codec__cfg.md#gaf869e7ce0c9dd467fb03e8503d36c58a)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1334 enum [bt\_audio\_active\_state](group__bt__audio.md#ga16d403ec4db7be997682331ad365ff5f) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

1335

[ 1347](group__bt__audio__codec__cfg.md#ga66143aa7dcc726e06a12660b8f90fc5a)int [bt\_audio\_codec\_cfg\_meta\_get\_bcast\_audio\_immediate\_rend\_flag](group__bt__audio__codec__cfg.md#ga66143aa7dcc726e06a12660b8f90fc5a)(

1348 const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg);

1349

[ 1359](group__bt__audio__codec__cfg.md#gaede61b65d2037c7fbf6c4c4e090990be)int [bt\_audio\_codec\_cfg\_meta\_set\_bcast\_audio\_immediate\_rend\_flag](group__bt__audio__codec__cfg.md#gaede61b65d2037c7fbf6c4c4e090990be)(

1360 struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg);

1361

[ 1374](group__bt__audio__codec__cfg.md#ga22ae14fce65b757e31f391c4bdcae328)int [bt\_audio\_codec\_cfg\_meta\_get\_assisted\_listening\_stream](group__bt__audio__codec__cfg.md#ga22ae14fce65b757e31f391c4bdcae328)(

1375 const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg);

1376

[ 1387](group__bt__audio__codec__cfg.md#ga67d83559cbe6cfab235f2e588cbc398c)int [bt\_audio\_codec\_cfg\_meta\_set\_assisted\_listening\_stream](group__bt__audio__codec__cfg.md#ga67d83559cbe6cfab235f2e588cbc398c)(

1388 struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, enum [bt\_audio\_assisted\_listening\_stream](group__bt__audio.md#ga207fbf0fbca9b24cba02c7f1d184e7f5) val);

1389

[ 1402](group__bt__audio__codec__cfg.md#ga5d80babcd6f381014e1fae98a755e1d3)int [bt\_audio\_codec\_cfg\_meta\_get\_broadcast\_name](group__bt__audio__codec__cfg.md#ga5d80babcd6f381014e1fae98a755e1d3)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1403 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*broadcast\_name);

1404

[ 1416](group__bt__audio__codec__cfg.md#ga4f5cbacebedc8d7df02d1c47b140bf3c)int [bt\_audio\_codec\_cfg\_meta\_set\_broadcast\_name](group__bt__audio__codec__cfg.md#ga4f5cbacebedc8d7df02d1c47b140bf3c)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1417 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*broadcast\_name,

1418 size\_t broadcast\_name\_len);

1419

[ 1432](group__bt__audio__codec__cfg.md#ga1f76f82bff63b876eb761a0bf0377428)int [bt\_audio\_codec\_cfg\_meta\_get\_extended](group__bt__audio__codec__cfg.md#ga1f76f82bff63b876eb761a0bf0377428)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1433 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*extended\_meta);

1434

[ 1446](group__bt__audio__codec__cfg.md#gade9cb53287ab3356fb57ba8a454a3aad)int [bt\_audio\_codec\_cfg\_meta\_set\_extended](group__bt__audio__codec__cfg.md#gade9cb53287ab3356fb57ba8a454a3aad)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1447 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*extended\_meta, size\_t extended\_meta\_len);

1448

[ 1461](group__bt__audio__codec__cfg.md#ga4a4982e3bd0e8c944b584196ef146f6c)int [bt\_audio\_codec\_cfg\_meta\_get\_vendor](group__bt__audio__codec__cfg.md#ga4a4982e3bd0e8c944b584196ef146f6c)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1462 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*vendor\_meta);

1463

[ 1475](group__bt__audio__codec__cfg.md#ga6935d1c40b3178b0c8fa877ee93d1e53)int [bt\_audio\_codec\_cfg\_meta\_set\_vendor](group__bt__audio__codec__cfg.md#ga6935d1c40b3178b0c8fa877ee93d1e53)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1476 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*vendor\_meta, size\_t vendor\_meta\_len); /\* End of bt\_audio\_codec\_cfg \*/

1478

1488

[ 1500](group__bt__audio__codec__cap.md#gac3bf5dd414271bb1dcbc6590994cff6b)int [bt\_audio\_codec\_cap\_get\_val](group__bt__audio__codec__cap.md#gac3bf5dd414271bb1dcbc6590994cff6b)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1501 enum [bt\_audio\_codec\_cap\_type](group__bt__audio.md#gaf58823a56eb36cfd22e582ab1ea3d015) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*data);

1502

[ 1515](group__bt__audio__codec__cap.md#ga0c2c816b0b2b85aa5dd38f21caceea40)int [bt\_audio\_codec\_cap\_set\_val](group__bt__audio__codec__cap.md#ga0c2c816b0b2b85aa5dd38f21caceea40)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1516 enum [bt\_audio\_codec\_cap\_type](group__bt__audio.md#gaf58823a56eb36cfd22e582ab1ea3d015) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data,

1517 size\_t data\_len);

1518

[ 1530](group__bt__audio__codec__cap.md#gabc9962212ad65339ff02ba1389d5f9f8)int [bt\_audio\_codec\_cap\_unset\_val](group__bt__audio__codec__cap.md#gabc9962212ad65339ff02ba1389d5f9f8)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1531 enum [bt\_audio\_codec\_cap\_type](group__bt__audio.md#gaf58823a56eb36cfd22e582ab1ea3d015) type);

1532

[ 1544](group__bt__audio__codec__cap.md#gaa1dbf81c437c983af0144bf62433666c)int [bt\_audio\_codec\_cap\_get\_freq](group__bt__audio__codec__cap.md#gaa1dbf81c437c983af0144bf62433666c)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap);

1545

[ 1556](group__bt__audio__codec__cap.md#gac0655c0bd6552ab8a265076d7d0cd1b2)int [bt\_audio\_codec\_cap\_set\_freq](group__bt__audio__codec__cap.md#gac0655c0bd6552ab8a265076d7d0cd1b2)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1557 enum [bt\_audio\_codec\_cap\_freq](group__bt__audio.md#gaafc1106d5d305874ee2f540c850ff5b4) freq);

1558

[ 1569](group__bt__audio__codec__cap.md#ga12336de7d908bda94427caee4dc080e0)int [bt\_audio\_codec\_cap\_get\_frame\_dur](group__bt__audio__codec__cap.md#ga12336de7d908bda94427caee4dc080e0)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap);

1570

[ 1581](group__bt__audio__codec__cap.md#ga53e5df6cc4cfbed12b59a6a506657772)int [bt\_audio\_codec\_cap\_set\_frame\_dur](group__bt__audio__codec__cap.md#ga53e5df6cc4cfbed12b59a6a506657772)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1582 enum [bt\_audio\_codec\_cap\_frame\_dur](group__bt__audio.md#gaf37e8e19f956afb3c3a413cbaa1a21f5) frame\_dur);

1583

[ 1596](group__bt__audio__codec__cap.md#ga63d5e083f03ec06939ee1cd0355c8c2a)int [bt\_audio\_codec\_cap\_get\_supported\_audio\_chan\_counts](group__bt__audio__codec__cap.md#ga63d5e083f03ec06939ee1cd0355c8c2a)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1597 bool fallback\_to\_default);

1598

[ 1609](group__bt__audio__codec__cap.md#gaf6b2717823f9f3136237ed6a6515449e)int [bt\_audio\_codec\_cap\_set\_supported\_audio\_chan\_counts](group__bt__audio__codec__cap.md#gaf6b2717823f9f3136237ed6a6515449e)(

1610 struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, enum [bt\_audio\_codec\_cap\_chan\_count](group__bt__audio.md#gae695b5d17359967703f2509db1671fa5) chan\_count);

1611

[ 1623](group__bt__audio__codec__cap.md#gaa949089f2c6c143041e6cb61338e0ddc)int [bt\_audio\_codec\_cap\_get\_octets\_per\_frame](group__bt__audio__codec__cap.md#gaa949089f2c6c143041e6cb61338e0ddc)(

1624 const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1625 struct [bt\_audio\_codec\_octets\_per\_codec\_frame](structbt__audio__codec__octets__per__codec__frame.md) \*codec\_frame);

1626

[ 1637](group__bt__audio__codec__cap.md#gac1c42460cd3c55bbfbd467f84ab2d78d)int [bt\_audio\_codec\_cap\_set\_octets\_per\_frame](group__bt__audio__codec__cap.md#gac1c42460cd3c55bbfbd467f84ab2d78d)(

1638 struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1639 const struct [bt\_audio\_codec\_octets\_per\_codec\_frame](structbt__audio__codec__octets__per__codec__frame.md) \*codec\_frame);

1640

[ 1653](group__bt__audio__codec__cap.md#ga194d938896ee65601bdce96d68c84885)int [bt\_audio\_codec\_cap\_get\_max\_codec\_frames\_per\_sdu](group__bt__audio__codec__cap.md#ga194d938896ee65601bdce96d68c84885)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1654 bool fallback\_to\_default);

1655

[ 1666](group__bt__audio__codec__cap.md#ga3785bc41f56f8f2a09248396dadb31da)int [bt\_audio\_codec\_cap\_set\_max\_codec\_frames\_per\_sdu](group__bt__audio__codec__cap.md#ga3785bc41f56f8f2a09248396dadb31da)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1667 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) codec\_frames\_per\_sdu);

1668

[ 1680](group__bt__audio__codec__cap.md#ga5c2ecbb4d0cef26dd2cc5d023e70a163)int [bt\_audio\_codec\_cap\_meta\_get\_val](group__bt__audio__codec__cap.md#ga5c2ecbb4d0cef26dd2cc5d023e70a163)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type,

1681 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*data);

1682

[ 1695](group__bt__audio__codec__cap.md#ga1fdfd8c36f4131bcf4ffd2b7f176b631)int [bt\_audio\_codec\_cap\_meta\_set\_val](group__bt__audio__codec__cap.md#ga1fdfd8c36f4131bcf4ffd2b7f176b631)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1696 enum [bt\_audio\_metadata\_type](group__bt__audio.md#gab53d0dd62bceff97cf8eed7d8cf80354) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data,

1697 size\_t data\_len);

1698

[ 1710](group__bt__audio__codec__cap.md#ga40848f5375d1e58622c580112c282f2e)int [bt\_audio\_codec\_cap\_meta\_unset\_val](group__bt__audio__codec__cap.md#ga40848f5375d1e58622c580112c282f2e)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1711 enum [bt\_audio\_metadata\_type](group__bt__audio.md#gab53d0dd62bceff97cf8eed7d8cf80354) type);

1712

[ 1725](group__bt__audio__codec__cap.md#gaaa8c6783241b1b70349354b3e36c696c)int [bt\_audio\_codec\_cap\_meta\_get\_pref\_context](group__bt__audio__codec__cap.md#gaaa8c6783241b1b70349354b3e36c696c)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap);

1726

[ 1737](group__bt__audio__codec__cap.md#ga7fe0d4553d6accf5c89645cbf86149bf)int [bt\_audio\_codec\_cap\_meta\_set\_pref\_context](group__bt__audio__codec__cap.md#ga7fe0d4553d6accf5c89645cbf86149bf)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1738 enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) ctx);

1739

[ 1752](group__bt__audio__codec__cap.md#ga88ee657b5bd3f847bb75c9620ddb142f)int [bt\_audio\_codec\_cap\_meta\_get\_stream\_context](group__bt__audio__codec__cap.md#ga88ee657b5bd3f847bb75c9620ddb142f)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap);

1753

[ 1764](group__bt__audio__codec__cap.md#ga5cc7f360049c38c8de631ea33dbc44ab)int [bt\_audio\_codec\_cap\_meta\_set\_stream\_context](group__bt__audio__codec__cap.md#ga5cc7f360049c38c8de631ea33dbc44ab)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1765 enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) ctx);

1766

[ 1779](group__bt__audio__codec__cap.md#ga33725c3b2c06d6c22030bb5a77d702b0)int [bt\_audio\_codec\_cap\_meta\_get\_program\_info](group__bt__audio__codec__cap.md#ga33725c3b2c06d6c22030bb5a77d702b0)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1780 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*program\_info);

1781

[ 1793](group__bt__audio__codec__cap.md#ga43d2ec3a4d621c26843de82db7fd2189)int [bt\_audio\_codec\_cap\_meta\_set\_program\_info](group__bt__audio__codec__cap.md#ga43d2ec3a4d621c26843de82db7fd2189)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1794 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*program\_info, size\_t program\_info\_len);

1795

[ 1809](group__bt__audio__codec__cap.md#gafb631b55b69b256c60b9cf3c7f418ff8)int [bt\_audio\_codec\_cap\_meta\_get\_lang](group__bt__audio__codec__cap.md#gafb631b55b69b256c60b9cf3c7f418ff8)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1810 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*lang);

1811

[ 1822](group__bt__audio__codec__cap.md#ga8182b2bed20449b8581b89677893c130)int [bt\_audio\_codec\_cap\_meta\_set\_lang](group__bt__audio__codec__cap.md#ga8182b2bed20449b8581b89677893c130)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1823 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) lang[[BT\_AUDIO\_LANG\_SIZE](group__bt__audio.md#gab6e5f793d514626deca21940d35d8f21)]);

1824

[ 1837](group__bt__audio__codec__cap.md#ga3095dea36e60e75cbfe786d3c2f11866)int [bt\_audio\_codec\_cap\_meta\_get\_ccid\_list](group__bt__audio__codec__cap.md#ga3095dea36e60e75cbfe786d3c2f11866)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1838 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*ccid\_list);

1839

[ 1851](group__bt__audio__codec__cap.md#ga00a8ad22713dab761c81d1b8481c037d)int [bt\_audio\_codec\_cap\_meta\_set\_ccid\_list](group__bt__audio__codec__cap.md#ga00a8ad22713dab761c81d1b8481c037d)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1852 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*ccid\_list, size\_t ccid\_list\_len);

1853

[ 1866](group__bt__audio__codec__cap.md#gab34d0369ce08efcd407d33956d32632e)int [bt\_audio\_codec\_cap\_meta\_get\_parental\_rating](group__bt__audio__codec__cap.md#gab34d0369ce08efcd407d33956d32632e)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap);

1867

[ 1878](group__bt__audio__codec__cap.md#ga5e267dfad978cd3d52be9c31a4fac0be)int [bt\_audio\_codec\_cap\_meta\_set\_parental\_rating](group__bt__audio__codec__cap.md#ga5e267dfad978cd3d52be9c31a4fac0be)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1879 enum [bt\_audio\_parental\_rating](group__bt__audio.md#ga6d4aff1f93dc0b902e4b5d1355f15760) parental\_rating);

1880

[ 1893](group__bt__audio__codec__cap.md#gadb39b0ee1f65cdd2457fdf2c3142c040)int [bt\_audio\_codec\_cap\_meta\_get\_program\_info\_uri](group__bt__audio__codec__cap.md#gadb39b0ee1f65cdd2457fdf2c3142c040)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1894 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*program\_info\_uri);

1895

[ 1907](group__bt__audio__codec__cap.md#gafbb0d6282d989e8bc70caada2845b337)int [bt\_audio\_codec\_cap\_meta\_set\_program\_info\_uri](group__bt__audio__codec__cap.md#gafbb0d6282d989e8bc70caada2845b337)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1908 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*program\_info\_uri,

1909 size\_t program\_info\_uri\_len);

1910

[ 1923](group__bt__audio__codec__cap.md#ga88bb1da63b7ea0f95dd236aa1024cfb8)int [bt\_audio\_codec\_cap\_meta\_get\_audio\_active\_state](group__bt__audio__codec__cap.md#ga88bb1da63b7ea0f95dd236aa1024cfb8)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap);

1924

[ 1935](group__bt__audio__codec__cap.md#gacd3de0306a22d1a1d9ba09b4ac4f4e09)int [bt\_audio\_codec\_cap\_meta\_set\_audio\_active\_state](group__bt__audio__codec__cap.md#gacd3de0306a22d1a1d9ba09b4ac4f4e09)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1936 enum [bt\_audio\_active\_state](group__bt__audio.md#ga16d403ec4db7be997682331ad365ff5f) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

1937

[ 1949](group__bt__audio__codec__cap.md#gab4ccc7cb7d779acb20185ae808dd8bbe)int [bt\_audio\_codec\_cap\_meta\_get\_bcast\_audio\_immediate\_rend\_flag](group__bt__audio__codec__cap.md#gab4ccc7cb7d779acb20185ae808dd8bbe)(

1950 const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap);

1951

[ 1961](group__bt__audio__codec__cap.md#gaa1d382b4fa53f7cbe8426df53a3317ce)int [bt\_audio\_codec\_cap\_meta\_set\_bcast\_audio\_immediate\_rend\_flag](group__bt__audio__codec__cap.md#gaa1d382b4fa53f7cbe8426df53a3317ce)(

1962 struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap);

1963

[ 1976](group__bt__audio__codec__cap.md#ga4f1ea56f2c1c21420f078d35081ceee5)int [bt\_audio\_codec\_cap\_meta\_get\_assisted\_listening\_stream](group__bt__audio__codec__cap.md#ga4f1ea56f2c1c21420f078d35081ceee5)(

1977 const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap);

1978

[ 1989](group__bt__audio__codec__cap.md#ga3346db1f59cb35b9b9e5255424adb6e4)int [bt\_audio\_codec\_cap\_meta\_set\_assisted\_listening\_stream](group__bt__audio__codec__cap.md#ga3346db1f59cb35b9b9e5255424adb6e4)(

1990 struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, enum [bt\_audio\_assisted\_listening\_stream](group__bt__audio.md#ga207fbf0fbca9b24cba02c7f1d184e7f5) val);

1991

[ 2004](group__bt__audio__codec__cap.md#ga3c8df3fe79f0bb96c4e15e7c2502bf89)int [bt\_audio\_codec\_cap\_meta\_get\_broadcast\_name](group__bt__audio__codec__cap.md#ga3c8df3fe79f0bb96c4e15e7c2502bf89)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

2005 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*broadcast\_name);

2006

[ 2018](group__bt__audio__codec__cap.md#ga461add2808a1eca8993222d2b31d5a5f)int [bt\_audio\_codec\_cap\_meta\_set\_broadcast\_name](group__bt__audio__codec__cap.md#ga461add2808a1eca8993222d2b31d5a5f)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

2019 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*broadcast\_name,

2020 size\_t broadcast\_name\_len);

[ 2033](group__bt__audio__codec__cap.md#ga69aecd7e98f90a5162ff8ea3373b43d4)int [bt\_audio\_codec\_cap\_meta\_get\_extended](group__bt__audio__codec__cap.md#ga69aecd7e98f90a5162ff8ea3373b43d4)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

2034 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*extended\_meta);

2035

[ 2047](group__bt__audio__codec__cap.md#gac00aabc7329027852a7caf5cdff2bc26)int [bt\_audio\_codec\_cap\_meta\_set\_extended](group__bt__audio__codec__cap.md#gac00aabc7329027852a7caf5cdff2bc26)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

2048 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*extended\_meta, size\_t extended\_meta\_len);

2049

[ 2062](group__bt__audio__codec__cap.md#gab8c80a0f55041f026d453fd88cdeb727)int [bt\_audio\_codec\_cap\_meta\_get\_vendor](group__bt__audio__codec__cap.md#gab8c80a0f55041f026d453fd88cdeb727)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

2063 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*vendor\_meta);

2064

[ 2076](group__bt__audio__codec__cap.md#ga1f06789782541beab9aab4914f91bb57)int [bt\_audio\_codec\_cap\_meta\_set\_vendor](group__bt__audio__codec__cap.md#ga1f06789782541beab9aab4914f91bb57)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

2077 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*vendor\_meta, size\_t vendor\_meta\_len);

2078 /\* End of bt\_audio\_codec\_cap \*/

2080

2089

[ 2099](group__bt__audio__to__str.md#ga26436fc678423ff1cf3543d381359d0f)static inline char \*[bt\_audio\_context\_bit\_to\_str](group__bt__audio__to__str.md#ga26436fc678423ff1cf3543d381359d0f)(enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) context)

2100{

2101 switch (context) {

2102 case [BT\_AUDIO\_CONTEXT\_TYPE\_PROHIBITED](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a3cfcfa76adc5effdc1aa95d75e5da37a):

2103 return "Prohibited";

2104 case [BT\_AUDIO\_CONTEXT\_TYPE\_UNSPECIFIED](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3aad96be1265bd1be4c937c687335e33f5):

2105 return "Unspecified";

2106 case [BT\_AUDIO\_CONTEXT\_TYPE\_CONVERSATIONAL](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a8a6262c1cf4e4591a7b92b4f8f329f9e):

2107 return "Conversational";

2108 case [BT\_AUDIO\_CONTEXT\_TYPE\_MEDIA](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a43d67936976a5c041027d15d66c21a5e):

2109 return "Media";

2110 case [BT\_AUDIO\_CONTEXT\_TYPE\_GAME](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a652ad83b9eb524c62933bf87a8ecb730):

2111 return "Game";

2112 case [BT\_AUDIO\_CONTEXT\_TYPE\_INSTRUCTIONAL](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a2e3af6f4ca620f91d9266257f842ddd4):

2113 return "Instructional";

2114 case [BT\_AUDIO\_CONTEXT\_TYPE\_VOICE\_ASSISTANTS](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a7e208290ddc2f92ac78ff4a22b20ca7e):

2115 return "Voice assistant";

2116 case [BT\_AUDIO\_CONTEXT\_TYPE\_LIVE](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a42c80228bda513d5a59d4d836e73bd55):

2117 return "Live";

2118 case [BT\_AUDIO\_CONTEXT\_TYPE\_SOUND\_EFFECTS](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a6956a9e43433e2800fd36c7022e039d9):

2119 return "Sound effects";

2120 case [BT\_AUDIO\_CONTEXT\_TYPE\_NOTIFICATIONS](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a06df6f713bb68b197be75bf821d5d377):

2121 return "Notifications";

2122 case [BT\_AUDIO\_CONTEXT\_TYPE\_RINGTONE](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a422bb29f035583b7319456a679f880b3):

2123 return "Ringtone";

2124 case [BT\_AUDIO\_CONTEXT\_TYPE\_ALERTS](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a915d05a728f3e083f290766a970dabb6):

2125 return "Alerts";

2126 case [BT\_AUDIO\_CONTEXT\_TYPE\_EMERGENCY\_ALARM](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a132abd2f9ac7be62d1306efc6bc8b7d1):

2127 return "Emergency alarm";

2128 default:

2129 return "Unknown context";

2130 }

2131}

2132

[ 2140](group__bt__audio__to__str.md#ga6926c4e8bda0874769177a903276c072)static inline char \*[bt\_audio\_parental\_rating\_to\_str](group__bt__audio__to__str.md#ga6926c4e8bda0874769177a903276c072)(enum [bt\_audio\_parental\_rating](group__bt__audio.md#ga6d4aff1f93dc0b902e4b5d1355f15760) parental\_rating)

2141{

2142 switch (parental\_rating) {

2143 case [BT\_AUDIO\_PARENTAL\_RATING\_NO\_RATING](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760aecf628bbd76651215232c8bfed04aa2c):

2144 return "No rating";

2145 case [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_ANY](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760ad6bba6a3b9537fcf913f798ab9a525f1):

2146 return "Any";

2147 case [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_5\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a8a8476abac3a569bd470a5237642c526):

2148 return "Age 5 or above";

2149 case [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_6\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760accb959ba21c1238c70c594b5cdc3ebdc):

2150 return "Age 6 or above";

2151 case [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_7\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a69508e569059bde1fed1b3fb3db1547a):

2152 return "Age 7 or above";

2153 case [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_8\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a9ed111f80d0671bb8b4e0a304ff0b0e4):

2154 return "Age 8 or above";

2155 case [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_9\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760aaabe26ebaa4b84684005440176ad86dd):

2156 return "Age 9 or above";

2157 case [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_10\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a4210d67d4506f8b9defb5fae32ae30d2):

2158 return "Age 10 or above";

2159 case [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_11\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760ac402ee4c06b92f0cc36774cf409cbbd0):

2160 return "Age 11 or above";

2161 case [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_12\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760ac68caf6719391afbef79e0c579dc96e7):

2162 return "Age 12 or above";

2163 case [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_13\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760aa680247699538d256111e18af1a2d15d):

2164 return "Age 13 or above";

2165 case [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_14\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760aef216d59983eccb86e90c493b8c17d86):

2166 return "Age 14 or above";

2167 case [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_15\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a3fe7bc3216a458ec3e5c6e177f43c077):

2168 return "Age 15 or above";

2169 case [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_16\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a779c5dd14e5f88e8e6bb247dc66d9c92):

2170 return "Age 16 or above";

2171 case [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_17\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a7d0794fe6796f19ff7e58819728751ff):

2172 return "Age 17 or above";

2173 case [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_18\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a22167e0c033c176f592a447b14c30071):

2174 return "Age 18 or above";

2175 default:

2176 return "Unknown rating";

2177 }

2178}

2179

[ 2187](group__bt__audio__to__str.md#ga1dd5865429e2438e0d4f88e891eda975)static inline char \*[bt\_audio\_active\_state\_to\_str](group__bt__audio__to__str.md#ga1dd5865429e2438e0d4f88e891eda975)(enum [bt\_audio\_active\_state](group__bt__audio.md#ga16d403ec4db7be997682331ad365ff5f) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90))

2188{

2189 switch ([state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) {

2190 case [BT\_AUDIO\_ACTIVE\_STATE\_DISABLED](group__bt__audio.md#gga16d403ec4db7be997682331ad365ff5fade27604ea8fd592aa5d0958e2ccde4f3):

2191 return "Disabled";

2192 case [BT\_AUDIO\_ACTIVE\_STATE\_ENABLED](group__bt__audio.md#gga16d403ec4db7be997682331ad365ff5fa6d062944e9c49001666769601ba1c940):

2193 return "Enabled";

2194 default:

2195 return "Unknown active state";

2196 }

2197}

2198

[ 2208](group__bt__audio__to__str.md#gadd3bac4f1f1b334cb60f5783fdc15c14)static inline char \*[bt\_audio\_codec\_cap\_freq\_bit\_to\_str](group__bt__audio__to__str.md#gadd3bac4f1f1b334cb60f5783fdc15c14)(enum [bt\_audio\_codec\_cap\_freq](group__bt__audio.md#gaafc1106d5d305874ee2f540c850ff5b4) freq)

2209{

2210 switch (freq) {

2211 case [BT\_AUDIO\_CODEC\_CAP\_FREQ\_8KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a3d821d03771805107707f47dcdb71f83):

2212 return "8000 Hz";

2213 case [BT\_AUDIO\_CODEC\_CAP\_FREQ\_11KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a562c38a59cded025183a0f95d4a63c81):

2214 return "11025 Hz";

2215 case [BT\_AUDIO\_CODEC\_CAP\_FREQ\_16KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4acfef6825ac865b1e590e7959a9270361):

2216 return "16000 Hz";

2217 case [BT\_AUDIO\_CODEC\_CAP\_FREQ\_22KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ad7440157cf8864dfc5fd854482f3a982):

2218 return "22050 Hz";

2219 case [BT\_AUDIO\_CODEC\_CAP\_FREQ\_24KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4acf9ff8842d72d56d27eae692e4c4b956):

2220 return "24000 Hz";

2221 case [BT\_AUDIO\_CODEC\_CAP\_FREQ\_32KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a822ff105ab495c126c21d73bd90cbd9c):

2222 return "32000 Hz";

2223 case [BT\_AUDIO\_CODEC\_CAP\_FREQ\_44KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ad28396f4b5a71d7c196e1a27bd17f8c3):

2224 return "44100 Hz";

2225 case [BT\_AUDIO\_CODEC\_CAP\_FREQ\_48KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a91ec17ee96b8e56e31ab545e5e8abe91):

2226 return "48000 Hz";

2227 case [BT\_AUDIO\_CODEC\_CAP\_FREQ\_88KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a25cc72bd630446f5154c54402058a211):

2228 return "88200 Hz";

2229 case [BT\_AUDIO\_CODEC\_CAP\_FREQ\_96KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ae802fea402f207238613275917846663):

2230 return "96000 Hz";

2231 case [BT\_AUDIO\_CODEC\_CAP\_FREQ\_176KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a031d159eadf7ea1ba6b00b03bef26d2b):

2232 return "176400 Hz";

2233 case [BT\_AUDIO\_CODEC\_CAP\_FREQ\_192KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a0de8d0351153650c1b48934053e18890):

2234 return "192000 Hz";

2235 case [BT\_AUDIO\_CODEC\_CAP\_FREQ\_384KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ae5ddc4504b7077e90be56f34ad8647c2):

2236 return "384000 Hz";

2237 default:

2238 return "Unknown supported frequency";

2239 }

2240}

2241

2251static inline char \*

[ 2252](group__bt__audio__to__str.md#ga6b9cc74dafcf03056862ae9823bce58d)[bt\_audio\_codec\_cap\_frame\_dur\_bit\_to\_str](group__bt__audio__to__str.md#ga6b9cc74dafcf03056862ae9823bce58d)(enum [bt\_audio\_codec\_cap\_frame\_dur](group__bt__audio.md#gaf37e8e19f956afb3c3a413cbaa1a21f5) frame\_dur)

2253{

2254 switch (frame\_dur) {

2255 case [BT\_AUDIO\_CODEC\_CAP\_DURATION\_7\_5](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a340878058d0beabeade33e0f3893d441):

2256 return "7.5 ms";

2257 case [BT\_AUDIO\_CODEC\_CAP\_DURATION\_10](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5afd423ac4270ff0df8ca6df7f5e4c799b):

2258 return "10 ms";

2259 case [BT\_AUDIO\_CODEC\_CAP\_DURATION\_PREFER\_7\_5](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a7ab1c63639cf93fdf2c2dfdf43424e91):

2260 return "7.5 ms preferred";

2261 case [BT\_AUDIO\_CODEC\_CAP\_DURATION\_PREFER\_10](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a9744473b3a29074c24cf0bbff35a5d8e):

2262 return "10 ms preferred";

2263 default:

2264 return "Unknown frame duration";

2265 }

2266}

2267

2277static inline char \*

[ 2278](group__bt__audio__to__str.md#ga795742ed8d91e2b675fbcdaeee7a71ec)[bt\_audio\_codec\_cap\_chan\_count\_bit\_to\_str](group__bt__audio__to__str.md#ga795742ed8d91e2b675fbcdaeee7a71ec)(enum [bt\_audio\_codec\_cap\_chan\_count](group__bt__audio.md#gae695b5d17359967703f2509db1671fa5) chan\_count)

2279{

2280 switch (chan\_count) {

2281 case [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_1](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a1558716b36042597515df18ff277f8bc):

2282 return "1 channel";

2283 case [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_2](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a13b236d93eb9c7516fdcf527313e16cd):

2284 return "2 channels";

2285 case [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_3](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a17da27ec39a79c341c82549df891cb39):

2286 return "3 channels";

2287 case [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_4](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a0fdfa6bf69b104f04d22e4f968969ac2):

2288 return "4 channels";

2289 case [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_5](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5ad08bc2ea0347a1ee8fd411a023b7ca51):

2290 return "5 channels";

2291 case [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_6](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5af9f9dd0cac39793793e5c8c5e50b11b8):

2292 return "6 channels";

2293 case [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_7](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a86ef227772c7751b4ae75529e2a57b82):

2294 return "7 channels";

2295 case [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_8](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a50afa60bdd53172fab7a376ce374d943):

2296 return "8 channels";

2297 default:

2298 return "Unknown channel count";

2299 }

2300}

2301

[ 2311](group__bt__audio__to__str.md#gaa1b9f7166fd6e6797da65d9537357324)static inline char \*[bt\_audio\_location\_bit\_to\_str](group__bt__audio__to__str.md#gaa1b9f7166fd6e6797da65d9537357324)(enum [bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8) location)

2312{

2313 switch (location) {

2314 case [BT\_AUDIO\_LOCATION\_MONO\_AUDIO](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a8f476de613cdcb2f9f677d40291aa5df):

2315 return "Mono";

2316 case [BT\_AUDIO\_LOCATION\_FRONT\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ac658188fa6f1b4f248a149d0bde1e41b):

2317 return "Front left";

2318 case [BT\_AUDIO\_LOCATION\_FRONT\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a26d5ba460642bcf7fb2fc950082b70b3):

2319 return "Front right";

2320 case [BT\_AUDIO\_LOCATION\_FRONT\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a06b34e67c9931f8b26562218cba51337):

2321 return "Front center";

2322 case [BT\_AUDIO\_LOCATION\_LOW\_FREQ\_EFFECTS\_1](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ac4c09f948266f2c9c65b3bc16da2f3f6):

2323 return "Low frequency effects 1";

2324 case [BT\_AUDIO\_LOCATION\_BACK\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a96906ff7918b0a3e3e7efe73a08d9896):

2325 return "Back left";

2326 case [BT\_AUDIO\_LOCATION\_BACK\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a43f5070c2b4d39c38fa7900595d9b1aa):

2327 return "Back right";

2328 case [BT\_AUDIO\_LOCATION\_FRONT\_LEFT\_OF\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8af02a9d46877b742e8730bbf3dd6ad22e):

2329 return "Front left of center";

2330 case [BT\_AUDIO\_LOCATION\_FRONT\_RIGHT\_OF\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a725707ae4703a1f9b970de5b1e4e5692):

2331 return "Front right of center";

2332 case [BT\_AUDIO\_LOCATION\_BACK\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ae22cd1e458d8ff503741bf48262c7983):

2333 return "Back center";

2334 case [BT\_AUDIO\_LOCATION\_LOW\_FREQ\_EFFECTS\_2](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a0c304bdd529ad66acb71001caa1b361b):

2335 return "Low frequency effects 2";

2336 case [BT\_AUDIO\_LOCATION\_SIDE\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ab8e52c69b894e382f0f09cc370337064):

2337 return "Side left";

2338 case [BT\_AUDIO\_LOCATION\_SIDE\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8aa01ad94f71defd158d8cfe25936341cd):

2339 return "Side right";

2340 case [BT\_AUDIO\_LOCATION\_TOP\_FRONT\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8aa093e6218e213eac5677766e01f5c1c9):

2341 return "Top front left";

2342 case [BT\_AUDIO\_LOCATION\_TOP\_FRONT\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a60b154a216d8e029deac7305500eaf2d):

2343 return "Top front right";

2344 case [BT\_AUDIO\_LOCATION\_TOP\_FRONT\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ac32ed6f456be2fb2d9af2c7b255f3a4e):

2345 return "Top front center";

2346 case [BT\_AUDIO\_LOCATION\_TOP\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a555361fafade3bfb27dc713666757a1f):

2347 return "Top center";

2348 case [BT\_AUDIO\_LOCATION\_TOP\_BACK\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a07e699c28bd847de3d85645dceb2ff06):

2349 return "Top back left";

2350 case [BT\_AUDIO\_LOCATION\_TOP\_BACK\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a8e81b80f732b0037493712b4baa21a69):

2351 return "Top back right";

2352 case [BT\_AUDIO\_LOCATION\_TOP\_SIDE\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ae846b2f4186b46d3690c71071c41c7d6):

2353 return "Top side left";

2354 case [BT\_AUDIO\_LOCATION\_TOP\_SIDE\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a1cf8dea66e42f75ca85ba55124829a59):

2355 return "Top side right";

2356 case [BT\_AUDIO\_LOCATION\_TOP\_BACK\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8aebae1f0f2537a806672820fb74eba5dd):

2357 return "Top back center";

2358 case [BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ad0be8f720f03feb18a23e77f0eff6376):

2359 return "Bottom front center";

2360 case [BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ac1e355baee6ca0907356d72f0d4edb29):

2361 return "Bottom front left";

2362 case [BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a33d0f7c266f21fd086386f8c29ee31e8):

2363 return "Bottom front right";

2364 case [BT\_AUDIO\_LOCATION\_FRONT\_LEFT\_WIDE](group__bt__audio.md#gga61230848c02098352320fe751332c4e8acba90183626ad85c21692b7edd87133d):

2365 return "Front left wide";

2366 case [BT\_AUDIO\_LOCATION\_FRONT\_RIGHT\_WIDE](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a8649be1d5b7e8b312fc3374039cc0a71):

2367 return "Front right wde";

2368 case [BT\_AUDIO\_LOCATION\_LEFT\_SURROUND](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a568a581c0ad653177f5d148d04bef0b6):

2369 return "Left surround";

2370 case [BT\_AUDIO\_LOCATION\_RIGHT\_SURROUND](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a97954db823b6c6bed660ff2717600a5e):

2371 return "Right surround";

2372 default:

2373 return "Unknown location";

2374 }

2375}

2376 /\* End of bt\_audio\_to\_str \*/

2378#ifdef \_\_cplusplus

2379}

2380#endif

2381 /\* end of bt\_audio \*/

2383

2384#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_H\_ \*/

[bluetooth.h](bluetooth_2bluetooth_8h.md)

Bluetooth subsystem core APIs.

[buf.h](bluetooth_2buf_8h.md)

Bluetooth data buffer API.

[conn.h](conn_8h.md)

Bluetooth connection handling.

[gatt.h](gatt_8h.md)

Generic Attribute Profile handling.

[bt\_audio\_codec\_cap\_meta\_set\_ccid\_list](group__bt__audio__codec__cap.md#ga00a8ad22713dab761c81d1b8481c037d)

int bt\_audio\_codec\_cap\_meta\_set\_ccid\_list(struct bt\_audio\_codec\_cap \*codec\_cap, const uint8\_t \*ccid\_list, size\_t ccid\_list\_len)

Set the CCID list of a codec capability metadata.

[bt\_audio\_codec\_cap\_set\_val](group__bt__audio__codec__cap.md#ga0c2c816b0b2b85aa5dd38f21caceea40)

int bt\_audio\_codec\_cap\_set\_val(struct bt\_audio\_codec\_cap \*codec\_cap, enum bt\_audio\_codec\_cap\_type type, const uint8\_t \*data, size\_t data\_len)

Set or add a specific codec capability value.

[bt\_audio\_codec\_cap\_get\_frame\_dur](group__bt__audio__codec__cap.md#ga12336de7d908bda94427caee4dc080e0)

int bt\_audio\_codec\_cap\_get\_frame\_dur(const struct bt\_audio\_codec\_cap \*codec\_cap)

Extract the frequency from a codec capability.

[bt\_audio\_codec\_cap\_get\_max\_codec\_frames\_per\_sdu](group__bt__audio__codec__cap.md#ga194d938896ee65601bdce96d68c84885)

int bt\_audio\_codec\_cap\_get\_max\_codec\_frames\_per\_sdu(const struct bt\_audio\_codec\_cap \*codec\_cap, bool fallback\_to\_default)

Extract the maximum codec frames per SDU from a codec capability.

[bt\_audio\_codec\_cap\_meta\_set\_vendor](group__bt__audio__codec__cap.md#ga1f06789782541beab9aab4914f91bb57)

int bt\_audio\_codec\_cap\_meta\_set\_vendor(struct bt\_audio\_codec\_cap \*codec\_cap, const uint8\_t \*vendor\_meta, size\_t vendor\_meta\_len)

Set the vendor specific metadata of a codec capability metadata.

[bt\_audio\_codec\_cap\_meta\_set\_val](group__bt__audio__codec__cap.md#ga1fdfd8c36f4131bcf4ffd2b7f176b631)

int bt\_audio\_codec\_cap\_meta\_set\_val(struct bt\_audio\_codec\_cap \*codec\_cap, enum bt\_audio\_metadata\_type type, const uint8\_t \*data, size\_t data\_len)

Set or add a specific codec capability metadata value.

[bt\_audio\_codec\_cap\_meta\_get\_ccid\_list](group__bt__audio__codec__cap.md#ga3095dea36e60e75cbfe786d3c2f11866)

int bt\_audio\_codec\_cap\_meta\_get\_ccid\_list(const struct bt\_audio\_codec\_cap \*codec\_cap, const uint8\_t \*\*ccid\_list)

Extract CCID list.

[bt\_audio\_codec\_cap\_meta\_set\_assisted\_listening\_stream](group__bt__audio__codec__cap.md#ga3346db1f59cb35b9b9e5255424adb6e4)

int bt\_audio\_codec\_cap\_meta\_set\_assisted\_listening\_stream(struct bt\_audio\_codec\_cap \*codec\_cap, enum bt\_audio\_assisted\_listening\_stream val)

Set the assisted listening stream value of a codec capability metadata.

[bt\_audio\_codec\_cap\_meta\_get\_program\_info](group__bt__audio__codec__cap.md#ga33725c3b2c06d6c22030bb5a77d702b0)

int bt\_audio\_codec\_cap\_meta\_get\_program\_info(const struct bt\_audio\_codec\_cap \*codec\_cap, const uint8\_t \*\*program\_info)

Extract program info.

[bt\_audio\_codec\_cap\_set\_max\_codec\_frames\_per\_sdu](group__bt__audio__codec__cap.md#ga3785bc41f56f8f2a09248396dadb31da)

int bt\_audio\_codec\_cap\_set\_max\_codec\_frames\_per\_sdu(struct bt\_audio\_codec\_cap \*codec\_cap, uint8\_t codec\_frames\_per\_sdu)

Set the maximum codec frames per SDU of a codec capability.

[bt\_audio\_codec\_cap\_meta\_get\_broadcast\_name](group__bt__audio__codec__cap.md#ga3c8df3fe79f0bb96c4e15e7c2502bf89)

int bt\_audio\_codec\_cap\_meta\_get\_broadcast\_name(const struct bt\_audio\_codec\_cap \*codec\_cap, const uint8\_t \*\*broadcast\_name)

Extract broadcast name.

[bt\_audio\_codec\_cap\_meta\_unset\_val](group__bt__audio__codec__cap.md#ga40848f5375d1e58622c580112c282f2e)

int bt\_audio\_codec\_cap\_meta\_unset\_val(struct bt\_audio\_codec\_cap \*codec\_cap, enum bt\_audio\_metadata\_type type)

Unset a specific codec capability metadata value.

[bt\_audio\_codec\_cap\_meta\_set\_program\_info](group__bt__audio__codec__cap.md#ga43d2ec3a4d621c26843de82db7fd2189)

int bt\_audio\_codec\_cap\_meta\_set\_program\_info(struct bt\_audio\_codec\_cap \*codec\_cap, const uint8\_t \*program\_info, size\_t program\_info\_len)

Set the program info of a codec capability metadata.

[bt\_audio\_codec\_cap\_meta\_set\_broadcast\_name](group__bt__audio__codec__cap.md#ga461add2808a1eca8993222d2b31d5a5f)

int bt\_audio\_codec\_cap\_meta\_set\_broadcast\_name(struct bt\_audio\_codec\_cap \*codec\_cap, const uint8\_t \*broadcast\_name, size\_t broadcast\_name\_len)

Set the broadcast name of a codec capability metadata.

[bt\_audio\_codec\_cap\_meta\_get\_assisted\_listening\_stream](group__bt__audio__codec__cap.md#ga4f1ea56f2c1c21420f078d35081ceee5)

int bt\_audio\_codec\_cap\_meta\_get\_assisted\_listening\_stream(const struct bt\_audio\_codec\_cap \*codec\_cap)

Extract assisted listening stream.

[bt\_audio\_codec\_cap\_set\_frame\_dur](group__bt__audio__codec__cap.md#ga53e5df6cc4cfbed12b59a6a506657772)

int bt\_audio\_codec\_cap\_set\_frame\_dur(struct bt\_audio\_codec\_cap \*codec\_cap, enum bt\_audio\_codec\_cap\_frame\_dur frame\_dur)

Set the frame duration of a codec capability.

[bt\_audio\_codec\_cap\_meta\_get\_val](group__bt__audio__codec__cap.md#ga5c2ecbb4d0cef26dd2cc5d023e70a163)

int bt\_audio\_codec\_cap\_meta\_get\_val(const struct bt\_audio\_codec\_cap \*codec\_cap, uint8\_t type, const uint8\_t \*\*data)

Lookup a specific metadata value based on type.

[bt\_audio\_codec\_cap\_meta\_set\_stream\_context](group__bt__audio__codec__cap.md#ga5cc7f360049c38c8de631ea33dbc44ab)

int bt\_audio\_codec\_cap\_meta\_set\_stream\_context(struct bt\_audio\_codec\_cap \*codec\_cap, enum bt\_audio\_context ctx)

Set the stream context of a codec capability metadata.

[bt\_audio\_codec\_cap\_meta\_set\_parental\_rating](group__bt__audio__codec__cap.md#ga5e267dfad978cd3d52be9c31a4fac0be)

int bt\_audio\_codec\_cap\_meta\_set\_parental\_rating(struct bt\_audio\_codec\_cap \*codec\_cap, enum bt\_audio\_parental\_rating parental\_rating)

Set the parental rating of a codec capability metadata.

[bt\_audio\_codec\_cap\_get\_supported\_audio\_chan\_counts](group__bt__audio__codec__cap.md#ga63d5e083f03ec06939ee1cd0355c8c2a)

int bt\_audio\_codec\_cap\_get\_supported\_audio\_chan\_counts(const struct bt\_audio\_codec\_cap \*codec\_cap, bool fallback\_to\_default)

Extract the frequency from a codec capability.

[bt\_audio\_codec\_cap\_meta\_get\_extended](group__bt__audio__codec__cap.md#ga69aecd7e98f90a5162ff8ea3373b43d4)

int bt\_audio\_codec\_cap\_meta\_get\_extended(const struct bt\_audio\_codec\_cap \*codec\_cap, const uint8\_t \*\*extended\_meta)

Extract extended metadata.

[bt\_audio\_codec\_cap\_meta\_set\_pref\_context](group__bt__audio__codec__cap.md#ga7fe0d4553d6accf5c89645cbf86149bf)

int bt\_audio\_codec\_cap\_meta\_set\_pref\_context(struct bt\_audio\_codec\_cap \*codec\_cap, enum bt\_audio\_context ctx)

Set the preferred context of a codec capability metadata.

[bt\_audio\_codec\_cap\_meta\_set\_lang](group__bt__audio__codec__cap.md#ga8182b2bed20449b8581b89677893c130)

int bt\_audio\_codec\_cap\_meta\_set\_lang(struct bt\_audio\_codec\_cap \*codec\_cap, const uint8\_t lang[3])

Set the language of a codec capability metadata.

[bt\_audio\_codec\_cap\_meta\_get\_audio\_active\_state](group__bt__audio__codec__cap.md#ga88bb1da63b7ea0f95dd236aa1024cfb8)

int bt\_audio\_codec\_cap\_meta\_get\_audio\_active\_state(const struct bt\_audio\_codec\_cap \*codec\_cap)

Extract audio active state.

[bt\_audio\_codec\_cap\_meta\_get\_stream\_context](group__bt__audio__codec__cap.md#ga88ee657b5bd3f847bb75c9620ddb142f)

int bt\_audio\_codec\_cap\_meta\_get\_stream\_context(const struct bt\_audio\_codec\_cap \*codec\_cap)

Extract stream contexts.

[bt\_audio\_codec\_cap\_meta\_set\_bcast\_audio\_immediate\_rend\_flag](group__bt__audio__codec__cap.md#gaa1d382b4fa53f7cbe8426df53a3317ce)

int bt\_audio\_codec\_cap\_meta\_set\_bcast\_audio\_immediate\_rend\_flag(struct bt\_audio\_codec\_cap \*codec\_cap)

Set the broadcast audio immediate rendering flag of a codec capability metadata.

[bt\_audio\_codec\_cap\_get\_freq](group__bt__audio__codec__cap.md#gaa1dbf81c437c983af0144bf62433666c)

int bt\_audio\_codec\_cap\_get\_freq(const struct bt\_audio\_codec\_cap \*codec\_cap)

Extract the frequency from a codec capability.

[bt\_audio\_codec\_cap\_get\_octets\_per\_frame](group__bt__audio__codec__cap.md#gaa949089f2c6c143041e6cb61338e0ddc)

int bt\_audio\_codec\_cap\_get\_octets\_per\_frame(const struct bt\_audio\_codec\_cap \*codec\_cap, struct bt\_audio\_codec\_octets\_per\_codec\_frame \*codec\_frame)

Extract the supported octets per codec frame from a codec capability.

[bt\_audio\_codec\_cap\_meta\_get\_pref\_context](group__bt__audio__codec__cap.md#gaaa8c6783241b1b70349354b3e36c696c)

int bt\_audio\_codec\_cap\_meta\_get\_pref\_context(const struct bt\_audio\_codec\_cap \*codec\_cap)

Extract preferred contexts.

[bt\_audio\_codec\_cap\_meta\_get\_parental\_rating](group__bt__audio__codec__cap.md#gab34d0369ce08efcd407d33956d32632e)

int bt\_audio\_codec\_cap\_meta\_get\_parental\_rating(const struct bt\_audio\_codec\_cap \*codec\_cap)

Extract parental rating.

[bt\_audio\_codec\_cap\_meta\_get\_bcast\_audio\_immediate\_rend\_flag](group__bt__audio__codec__cap.md#gab4ccc7cb7d779acb20185ae808dd8bbe)

int bt\_audio\_codec\_cap\_meta\_get\_bcast\_audio\_immediate\_rend\_flag(const struct bt\_audio\_codec\_cap \*codec\_cap)

Extract broadcast audio immediate rendering flag.

[bt\_audio\_codec\_cap\_meta\_get\_vendor](group__bt__audio__codec__cap.md#gab8c80a0f55041f026d453fd88cdeb727)

int bt\_audio\_codec\_cap\_meta\_get\_vendor(const struct bt\_audio\_codec\_cap \*codec\_cap, const uint8\_t \*\*vendor\_meta)

Extract vendor specific metadata.

[bt\_audio\_codec\_cap\_unset\_val](group__bt__audio__codec__cap.md#gabc9962212ad65339ff02ba1389d5f9f8)

int bt\_audio\_codec\_cap\_unset\_val(struct bt\_audio\_codec\_cap \*codec\_cap, enum bt\_audio\_codec\_cap\_type type)

Unset a specific codec capability value.

[bt\_audio\_codec\_cap\_meta\_set\_extended](group__bt__audio__codec__cap.md#gac00aabc7329027852a7caf5cdff2bc26)

int bt\_audio\_codec\_cap\_meta\_set\_extended(struct bt\_audio\_codec\_cap \*codec\_cap, const uint8\_t \*extended\_meta, size\_t extended\_meta\_len)

Set the extended metadata of a codec capability metadata.

[bt\_audio\_codec\_cap\_set\_freq](group__bt__audio__codec__cap.md#gac0655c0bd6552ab8a265076d7d0cd1b2)

int bt\_audio\_codec\_cap\_set\_freq(struct bt\_audio\_codec\_cap \*codec\_cap, enum bt\_audio\_codec\_cap\_freq freq)

Set the supported frequencies of a codec capability.

[bt\_audio\_codec\_cap\_set\_octets\_per\_frame](group__bt__audio__codec__cap.md#gac1c42460cd3c55bbfbd467f84ab2d78d)

int bt\_audio\_codec\_cap\_set\_octets\_per\_frame(struct bt\_audio\_codec\_cap \*codec\_cap, const struct bt\_audio\_codec\_octets\_per\_codec\_frame \*codec\_frame)

Set the octets per codec frame of a codec capability.

[bt\_audio\_codec\_cap\_get\_val](group__bt__audio__codec__cap.md#gac3bf5dd414271bb1dcbc6590994cff6b)

int bt\_audio\_codec\_cap\_get\_val(const struct bt\_audio\_codec\_cap \*codec\_cap, enum bt\_audio\_codec\_cap\_type type, const uint8\_t \*\*data)

Lookup a specific value based on type.

[bt\_audio\_codec\_cap\_meta\_set\_audio\_active\_state](group__bt__audio__codec__cap.md#gacd3de0306a22d1a1d9ba09b4ac4f4e09)

int bt\_audio\_codec\_cap\_meta\_set\_audio\_active\_state(struct bt\_audio\_codec\_cap \*codec\_cap, enum bt\_audio\_active\_state state)

Set the audio active state of a codec capability metadata.

[bt\_audio\_codec\_cap\_meta\_get\_program\_info\_uri](group__bt__audio__codec__cap.md#gadb39b0ee1f65cdd2457fdf2c3142c040)

int bt\_audio\_codec\_cap\_meta\_get\_program\_info\_uri(const struct bt\_audio\_codec\_cap \*codec\_cap, const uint8\_t \*\*program\_info\_uri)

Extract program info URI.

[bt\_audio\_codec\_cap\_set\_supported\_audio\_chan\_counts](group__bt__audio__codec__cap.md#gaf6b2717823f9f3136237ed6a6515449e)

int bt\_audio\_codec\_cap\_set\_supported\_audio\_chan\_counts(struct bt\_audio\_codec\_cap \*codec\_cap, enum bt\_audio\_codec\_cap\_chan\_count chan\_count)

Set the channel count of a codec capability.

[bt\_audio\_codec\_cap\_meta\_get\_lang](group__bt__audio__codec__cap.md#gafb631b55b69b256c60b9cf3c7f418ff8)

int bt\_audio\_codec\_cap\_meta\_get\_lang(const struct bt\_audio\_codec\_cap \*codec\_cap, const uint8\_t \*\*lang)

Extract language.

[bt\_audio\_codec\_cap\_meta\_set\_program\_info\_uri](group__bt__audio__codec__cap.md#gafbb0d6282d989e8bc70caada2845b337)

int bt\_audio\_codec\_cap\_meta\_set\_program\_info\_uri(struct bt\_audio\_codec\_cap \*codec\_cap, const uint8\_t \*program\_info\_uri, size\_t program\_info\_uri\_len)

Set the program info URI of a codec capability metadata.

[bt\_audio\_codec\_cfg\_meta\_get\_program\_info](group__bt__audio__codec__cfg.md#ga03284b8474d65443d7ecc8bdfc6f04c6)

int bt\_audio\_codec\_cfg\_meta\_get\_program\_info(const struct bt\_audio\_codec\_cfg \*codec\_cfg, const uint8\_t \*\*program\_info)

Extract program info.

[bt\_audio\_codec\_cfg\_frame\_dur\_us\_to\_frame\_dur](group__bt__audio__codec__cfg.md#ga0782a3d9254fb76b441c6c2492571556)

int bt\_audio\_codec\_cfg\_frame\_dur\_us\_to\_frame\_dur(uint32\_t frame\_dur\_us)

Convert frame duration in microseconds to assigned numbers frame duration.

[bt\_audio\_codec\_cfg\_meta\_get\_audio\_active\_state](group__bt__audio__codec__cfg.md#ga0fd6e6baf1b4f22d60768aaed6f42e8e)

int bt\_audio\_codec\_cfg\_meta\_get\_audio\_active\_state(const struct bt\_audio\_codec\_cfg \*codec\_cfg)

Extract audio active state.

[bt\_audio\_codec\_cfg\_meta\_get\_extended](group__bt__audio__codec__cfg.md#ga1f76f82bff63b876eb761a0bf0377428)

int bt\_audio\_codec\_cfg\_meta\_get\_extended(const struct bt\_audio\_codec\_cfg \*codec\_cfg, const uint8\_t \*\*extended\_meta)

Extract extended metadata.

[bt\_audio\_codec\_cfg\_frame\_dur\_to\_frame\_dur\_us](group__bt__audio__codec__cfg.md#ga225e05df1f0d1efb709c972187901495)

int bt\_audio\_codec\_cfg\_frame\_dur\_to\_frame\_dur\_us(enum bt\_audio\_codec\_cfg\_frame\_dur frame\_dur)

Convert assigned numbers frame duration to duration in microseconds.

[bt\_audio\_codec\_cfg\_meta\_get\_assisted\_listening\_stream](group__bt__audio__codec__cfg.md#ga22ae14fce65b757e31f391c4bdcae328)

int bt\_audio\_codec\_cfg\_meta\_get\_assisted\_listening\_stream(const struct bt\_audio\_codec\_cfg \*codec\_cfg)

Extract assisted listening stream.

[bt\_audio\_codec\_cfg\_meta\_set\_program\_info](group__bt__audio__codec__cfg.md#ga2ca9e616d20d7513c60ce905f046ac7b)

int bt\_audio\_codec\_cfg\_meta\_set\_program\_info(struct bt\_audio\_codec\_cfg \*codec\_cfg, const uint8\_t \*program\_info, size\_t program\_info\_len)

Set the program info of a codec configuration metadata.

[bt\_audio\_codec\_cfg\_get\_frame\_dur](group__bt__audio__codec__cfg.md#ga2dd3afe41b22e989fb46614f89550007)

int bt\_audio\_codec\_cfg\_get\_frame\_dur(const struct bt\_audio\_codec\_cfg \*codec\_cfg)

Extract frame duration from BT codec config.

[bt\_audio\_codec\_cfg\_freq\_to\_freq\_hz](group__bt__audio__codec__cfg.md#ga2e557fe726a49dc99754da16f7cc60af)

int bt\_audio\_codec\_cfg\_freq\_to\_freq\_hz(enum bt\_audio\_codec\_cfg\_freq freq)

Convert assigned numbers frequency to frequency value.

[bt\_audio\_codec\_cfg\_meta\_set\_val](group__bt__audio__codec__cfg.md#ga3e24c2ba8de502600e647cb2f84e3ec4)

int bt\_audio\_codec\_cfg\_meta\_set\_val(struct bt\_audio\_codec\_cfg \*codec\_cfg, enum bt\_audio\_metadata\_type type, const uint8\_t \*data, size\_t data\_len)

Set or add a specific codec configuration metadata value.

[bt\_audio\_codec\_cfg\_meta\_get\_vendor](group__bt__audio__codec__cfg.md#ga4a4982e3bd0e8c944b584196ef146f6c)

int bt\_audio\_codec\_cfg\_meta\_get\_vendor(const struct bt\_audio\_codec\_cfg \*codec\_cfg, const uint8\_t \*\*vendor\_meta)

Extract vendor specific metadata.

[bt\_audio\_codec\_cfg\_meta\_get\_stream\_context](group__bt__audio__codec__cfg.md#ga4cc4e1bb941206e7f1541a57fc92b8e9)

int bt\_audio\_codec\_cfg\_meta\_get\_stream\_context(const struct bt\_audio\_codec\_cfg \*codec\_cfg)

Extract stream contexts.

[bt\_audio\_codec\_cfg\_meta\_set\_broadcast\_name](group__bt__audio__codec__cfg.md#ga4f5cbacebedc8d7df02d1c47b140bf3c)

int bt\_audio\_codec\_cfg\_meta\_set\_broadcast\_name(struct bt\_audio\_codec\_cfg \*codec\_cfg, const uint8\_t \*broadcast\_name, size\_t broadcast\_name\_len)

Set the broadcast name of a codec configuration metadata.

[bt\_audio\_codec\_cfg\_get\_octets\_per\_frame](group__bt__audio__codec__cfg.md#ga503be053422217502d6108b045791e02)

int bt\_audio\_codec\_cfg\_get\_octets\_per\_frame(const struct bt\_audio\_codec\_cfg \*codec\_cfg)

Extract frame size in octets from BT codec config.

[bt\_audio\_codec\_cfg\_meta\_set\_lang](group__bt__audio__codec__cfg.md#ga54b7eadf072c397879c1dababa2a3be0)

int bt\_audio\_codec\_cfg\_meta\_set\_lang(struct bt\_audio\_codec\_cfg \*codec\_cfg, const uint8\_t lang[3])

Set the language of a codec configuration metadata.

[bt\_audio\_codec\_cfg\_meta\_get\_lang](group__bt__audio__codec__cfg.md#ga55e3cbaeacf15fcb1f24a16eb28db99c)

int bt\_audio\_codec\_cfg\_meta\_get\_lang(const struct bt\_audio\_codec\_cfg \*codec\_cfg, const uint8\_t \*\*lang)

Extract language.

[bt\_audio\_codec\_cfg\_meta\_set\_ccid\_list](group__bt__audio__codec__cfg.md#ga59716b95fcea3404ff8c078564b0e29c)

int bt\_audio\_codec\_cfg\_meta\_set\_ccid\_list(struct bt\_audio\_codec\_cfg \*codec\_cfg, const uint8\_t \*ccid\_list, size\_t ccid\_list\_len)

Set the CCID list of a codec configuration metadata.

[bt\_audio\_codec\_cfg\_meta\_set\_stream\_context](group__bt__audio__codec__cfg.md#ga5cd2af1bb44c6eb5bafe824f005a77f0)

int bt\_audio\_codec\_cfg\_meta\_set\_stream\_context(struct bt\_audio\_codec\_cfg \*codec\_cfg, enum bt\_audio\_context ctx)

Set the stream context of a codec configuration metadata.

[bt\_audio\_codec\_cfg\_meta\_get\_broadcast\_name](group__bt__audio__codec__cfg.md#ga5d80babcd6f381014e1fae98a755e1d3)

int bt\_audio\_codec\_cfg\_meta\_get\_broadcast\_name(const struct bt\_audio\_codec\_cfg \*codec\_cfg, const uint8\_t \*\*broadcast\_name)

Extract broadcast name.

[bt\_audio\_codec\_cfg\_meta\_get\_bcast\_audio\_immediate\_rend\_flag](group__bt__audio__codec__cfg.md#ga66143aa7dcc726e06a12660b8f90fc5a)

int bt\_audio\_codec\_cfg\_meta\_get\_bcast\_audio\_immediate\_rend\_flag(const struct bt\_audio\_codec\_cfg \*codec\_cfg)

Extract broadcast audio immediate rendering flag.

[bt\_audio\_codec\_cfg\_meta\_set\_assisted\_listening\_stream](group__bt__audio__codec__cfg.md#ga67d83559cbe6cfab235f2e588cbc398c)

int bt\_audio\_codec\_cfg\_meta\_set\_assisted\_listening\_stream(struct bt\_audio\_codec\_cfg \*codec\_cfg, enum bt\_audio\_assisted\_listening\_stream val)

Set the assisted listening stream value of a codec configuration metadata.

[bt\_audio\_codec\_cfg\_meta\_set\_vendor](group__bt__audio__codec__cfg.md#ga6935d1c40b3178b0c8fa877ee93d1e53)

int bt\_audio\_codec\_cfg\_meta\_set\_vendor(struct bt\_audio\_codec\_cfg \*codec\_cfg, const uint8\_t \*vendor\_meta, size\_t vendor\_meta\_len)

Set the vendor specific metadata of a codec configuration metadata.

[bt\_audio\_codec\_cfg\_meta\_get\_program\_info\_uri](group__bt__audio__codec__cfg.md#ga6bdbc0a0b929fdbdc75db479aec858df)

int bt\_audio\_codec\_cfg\_meta\_get\_program\_info\_uri(const struct bt\_audio\_codec\_cfg \*codec\_cfg, const uint8\_t \*\*program\_info\_uri)

Extract program info URI.

[bt\_audio\_codec\_cfg\_get\_val](group__bt__audio__codec__cfg.md#ga707c679db0193197b56acabfb08f8d1f)

int bt\_audio\_codec\_cfg\_get\_val(const struct bt\_audio\_codec\_cfg \*codec\_cfg, enum bt\_audio\_codec\_cfg\_type type, const uint8\_t \*\*data)

Lookup a specific codec configuration value.

[bt\_audio\_codec\_cfg\_set\_frame\_dur](group__bt__audio__codec__cfg.md#ga7d8306f98cb00f06e68a1df417825f0d)

int bt\_audio\_codec\_cfg\_set\_frame\_dur(struct bt\_audio\_codec\_cfg \*codec\_cfg, enum bt\_audio\_codec\_cfg\_frame\_dur frame\_dur)

Set the frame duration of a codec configuration.

[bt\_audio\_codec\_cfg\_set\_octets\_per\_frame](group__bt__audio__codec__cfg.md#ga866cdec28194056dc9e274d0436b45c2)

int bt\_audio\_codec\_cfg\_set\_octets\_per\_frame(struct bt\_audio\_codec\_cfg \*codec\_cfg, uint16\_t octets\_per\_frame)

Set the octets per codec frame of a codec configuration.

[bt\_audio\_codec\_cfg\_meta\_set\_program\_info\_uri](group__bt__audio__codec__cfg.md#ga99163729034e816eaef7195505d5ae20)

int bt\_audio\_codec\_cfg\_meta\_set\_program\_info\_uri(struct bt\_audio\_codec\_cfg \*codec\_cfg, const uint8\_t \*program\_info\_uri, size\_t program\_info\_uri\_len)

Set the program info URI of a codec configuration metadata.

[bt\_audio\_codec\_cfg\_freq\_hz\_to\_freq](group__bt__audio__codec__cfg.md#ga99ab4f6d2a18f2a9b4e3da47f63fc9e0)

int bt\_audio\_codec\_cfg\_freq\_hz\_to\_freq(uint32\_t freq\_hz)

Convert frequency value to assigned numbers frequency.

[bt\_audio\_codec\_cfg\_meta\_get\_ccid\_list](group__bt__audio__codec__cfg.md#gaa0f9b9f608c7af881d5a928a3ae397b2)

int bt\_audio\_codec\_cfg\_meta\_get\_ccid\_list(const struct bt\_audio\_codec\_cfg \*codec\_cfg, const uint8\_t \*\*ccid\_list)

Extract CCID list.

[bt\_audio\_codec\_cfg\_set\_val](group__bt__audio__codec__cfg.md#gab10f22938780530b1d1b95695382902e)

int bt\_audio\_codec\_cfg\_set\_val(struct bt\_audio\_codec\_cfg \*codec\_cfg, enum bt\_audio\_codec\_cfg\_type type, const uint8\_t \*data, size\_t data\_len)

Set or add a specific codec configuration value.

[bt\_audio\_codec\_cfg\_meta\_set\_pref\_context](group__bt__audio__codec__cfg.md#gab40bad609f17d24e7e0e9ffcebe4e912)

int bt\_audio\_codec\_cfg\_meta\_set\_pref\_context(struct bt\_audio\_codec\_cfg \*codec\_cfg, enum bt\_audio\_context ctx)

Set the preferred context of a codec configuration metadata.

[bt\_audio\_codec\_cfg\_meta\_unset\_val](group__bt__audio__codec__cfg.md#gab46f830daa1d9a907f47eb2a9eed7337)

int bt\_audio\_codec\_cfg\_meta\_unset\_val(struct bt\_audio\_codec\_cfg \*codec\_cfg, enum bt\_audio\_metadata\_type type)

Unset a specific codec configuration metadata value.

[bt\_audio\_codec\_cfg\_meta\_set\_parental\_rating](group__bt__audio__codec__cfg.md#gab5d8b5877de4fe16c0e06a1d4f0d15ce)

int bt\_audio\_codec\_cfg\_meta\_set\_parental\_rating(struct bt\_audio\_codec\_cfg \*codec\_cfg, enum bt\_audio\_parental\_rating parental\_rating)

Set the parental rating of a codec configuration metadata.

[bt\_audio\_codec\_cfg\_set\_freq](group__bt__audio__codec__cfg.md#gac119989d5dcfa36becf4edd0ae7c6138)

int bt\_audio\_codec\_cfg\_set\_freq(struct bt\_audio\_codec\_cfg \*codec\_cfg, enum bt\_audio\_codec\_cfg\_freq freq)

Set the frequency of a codec configuration.

[bt\_audio\_codec\_cfg\_set\_frame\_blocks\_per\_sdu](group__bt__audio__codec__cfg.md#gac9cf20bafbe24b34034bfb6ee7aaf03e)

int bt\_audio\_codec\_cfg\_set\_frame\_blocks\_per\_sdu(struct bt\_audio\_codec\_cfg \*codec\_cfg, uint8\_t frame\_blocks)

Set the frame blocks per SDU of a codec configuration.

[bt\_audio\_codec\_cfg\_unset\_val](group__bt__audio__codec__cfg.md#gad3857d0ca008854df5966501caa261ba)

int bt\_audio\_codec\_cfg\_unset\_val(struct bt\_audio\_codec\_cfg \*codec\_cfg, enum bt\_audio\_codec\_cfg\_type type)

Unset a specific codec configuration value.

[bt\_audio\_codec\_cfg\_get\_freq](group__bt__audio__codec__cfg.md#gad8525a57d35e3e34ea591f7e20e2512d)

int bt\_audio\_codec\_cfg\_get\_freq(const struct bt\_audio\_codec\_cfg \*codec\_cfg)

Extract the frequency from a codec configuration.

[bt\_audio\_codec\_cfg\_get\_frame\_blocks\_per\_sdu](group__bt__audio__codec__cfg.md#gadba0723f9d8a9546b659fba139051374)

int bt\_audio\_codec\_cfg\_get\_frame\_blocks\_per\_sdu(const struct bt\_audio\_codec\_cfg \*codec\_cfg, bool fallback\_to\_default)

Extract number of audio frame blocks in each SDU from BT codec config.

[bt\_audio\_codec\_cfg\_meta\_set\_extended](group__bt__audio__codec__cfg.md#gade9cb53287ab3356fb57ba8a454a3aad)

int bt\_audio\_codec\_cfg\_meta\_set\_extended(struct bt\_audio\_codec\_cfg \*codec\_cfg, const uint8\_t \*extended\_meta, size\_t extended\_meta\_len)

Set the extended metadata of a codec configuration metadata.

[bt\_audio\_codec\_cfg\_get\_chan\_allocation](group__bt__audio__codec__cfg.md#gae712e0f8e84aeb4ad2528da34907e29d)

int bt\_audio\_codec\_cfg\_get\_chan\_allocation(const struct bt\_audio\_codec\_cfg \*codec\_cfg, enum bt\_audio\_location \*chan\_allocation, bool fallback\_to\_default)

Extract channel allocation from BT codec config.

[bt\_audio\_codec\_cfg\_meta\_get\_val](group__bt__audio__codec__cfg.md#gae98335e87394a491b4a311d867a5e32d)

int bt\_audio\_codec\_cfg\_meta\_get\_val(const struct bt\_audio\_codec\_cfg \*codec\_cfg, uint8\_t type, const uint8\_t \*\*data)

Lookup a specific metadata value based on type.

[bt\_audio\_codec\_cfg\_meta\_get\_pref\_context](group__bt__audio__codec__cfg.md#gaea087663426a49bb6ff4859800aecb84)

int bt\_audio\_codec\_cfg\_meta\_get\_pref\_context(const struct bt\_audio\_codec\_cfg \*codec\_cfg, bool fallback\_to\_default)

Extract preferred contexts.

[bt\_audio\_codec\_cfg\_meta\_set\_bcast\_audio\_immediate\_rend\_flag](group__bt__audio__codec__cfg.md#gaede61b65d2037c7fbf6c4c4e090990be)

int bt\_audio\_codec\_cfg\_meta\_set\_bcast\_audio\_immediate\_rend\_flag(struct bt\_audio\_codec\_cfg \*codec\_cfg)

Set the broadcast audio immediate rendering flag of a codec configuration metadata.

[bt\_audio\_codec\_cfg\_meta\_get\_parental\_rating](group__bt__audio__codec__cfg.md#gaf0eecb02a05f0cc2b75ae9fb32c03913)

int bt\_audio\_codec\_cfg\_meta\_get\_parental\_rating(const struct bt\_audio\_codec\_cfg \*codec\_cfg)

Extract parental rating.

[bt\_audio\_codec\_cfg\_meta\_set\_audio\_active\_state](group__bt__audio__codec__cfg.md#gaf869e7ce0c9dd467fb03e8503d36c58a)

int bt\_audio\_codec\_cfg\_meta\_set\_audio\_active\_state(struct bt\_audio\_codec\_cfg \*codec\_cfg, enum bt\_audio\_active\_state state)

Set the audio active state of a codec configuration metadata.

[bt\_audio\_codec\_cfg\_set\_chan\_allocation](group__bt__audio__codec__cfg.md#gafbbcd69fac18ed0201a5e0156209b049)

int bt\_audio\_codec\_cfg\_set\_chan\_allocation(struct bt\_audio\_codec\_cfg \*codec\_cfg, enum bt\_audio\_location chan\_allocation)

Set the channel allocation of a codec configuration.

[bt\_audio\_active\_state\_to\_str](group__bt__audio__to__str.md#ga1dd5865429e2438e0d4f88e891eda975)

static char \* bt\_audio\_active\_state\_to\_str(enum bt\_audio\_active\_state state)

Returns a string representation of a bt\_audio\_active\_state value.

**Definition** audio.h:2187

[bt\_audio\_context\_bit\_to\_str](group__bt__audio__to__str.md#ga26436fc678423ff1cf3543d381359d0f)

static char \* bt\_audio\_context\_bit\_to\_str(enum bt\_audio\_context context)

Returns a string representation of a specific bt\_audio\_context bit.

**Definition** audio.h:2099

[bt\_audio\_parental\_rating\_to\_str](group__bt__audio__to__str.md#ga6926c4e8bda0874769177a903276c072)

static char \* bt\_audio\_parental\_rating\_to\_str(enum bt\_audio\_parental\_rating parental\_rating)

Returns a string representation of a bt\_audio\_parental\_rating value.

**Definition** audio.h:2140

[bt\_audio\_codec\_cap\_frame\_dur\_bit\_to\_str](group__bt__audio__to__str.md#ga6b9cc74dafcf03056862ae9823bce58d)

static char \* bt\_audio\_codec\_cap\_frame\_dur\_bit\_to\_str(enum bt\_audio\_codec\_cap\_frame\_dur frame\_dur)

Returns a string representation of a specific bt\_audio\_codec\_cap\_frame\_dur bit.

**Definition** audio.h:2252

[bt\_audio\_codec\_cap\_chan\_count\_bit\_to\_str](group__bt__audio__to__str.md#ga795742ed8d91e2b675fbcdaeee7a71ec)

static char \* bt\_audio\_codec\_cap\_chan\_count\_bit\_to\_str(enum bt\_audio\_codec\_cap\_chan\_count chan\_count)

Returns a string representation of a specific bt\_audio\_codec\_cap\_chan\_count bit.

**Definition** audio.h:2278

[bt\_audio\_location\_bit\_to\_str](group__bt__audio__to__str.md#gaa1b9f7166fd6e6797da65d9537357324)

static char \* bt\_audio\_location\_bit\_to\_str(enum bt\_audio\_location location)

Returns a string representation of a specific bt\_audio\_location bit.

**Definition** audio.h:2311

[bt\_audio\_codec\_cap\_freq\_bit\_to\_str](group__bt__audio__to__str.md#gadd3bac4f1f1b334cb60f5783fdc15c14)

static char \* bt\_audio\_codec\_cap\_freq\_bit\_to\_str(enum bt\_audio\_codec\_cap\_freq freq)

Returns a string representation of a specific bt\_audio\_codec\_cap\_freq bit.

**Definition** audio.h:2208

[bt\_audio\_active\_state](group__bt__audio.md#ga16d403ec4db7be997682331ad365ff5f)

bt\_audio\_active\_state

Audio Active State defined by the Generic Audio assigned numbers (bluetooth.com).

**Definition** audio.h:414

[bt\_audio\_assisted\_listening\_stream](group__bt__audio.md#ga207fbf0fbca9b24cba02c7f1d184e7f5)

bt\_audio\_assisted\_listening\_stream

Assisted Listening Stream defined by the Generic Audio assigned numbers (bluetooth....

**Definition** audio.h:422

[bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f)

bt\_audio\_dir

Audio direction from the perspective of the BAP Unicast Server / BAP Broadcast Sink.

**Definition** audio.h:796

[bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8)

bt\_audio\_location

Location values for BT Audio.

**Definition** audio.h:590

[bt\_audio\_parental\_rating](group__bt__audio.md#ga6d4aff1f93dc0b902e4b5d1355f15760)

bt\_audio\_parental\_rating

Parental rating defined by the Generic Audio assigned numbers (bluetooth.com).

**Definition** audio.h:378

[bt\_audio\_codec\_cfg\_frame\_dur](group__bt__audio.md#ga83701b5eadfcbc9b84dc0b1a85ebeb74)

bt\_audio\_codec\_cfg\_frame\_dur

Codec configuration frame duration.

**Definition** audio.h:290

[bt\_audio\_get\_chan\_count](group__bt__audio.md#ga87415f8dddd38b3f5641c96e9722a44a)

uint8\_t bt\_audio\_get\_chan\_count(enum bt\_audio\_location chan\_allocation)

Function to get the number of channels from the channel allocation.

[bt\_audio\_codec\_cfg\_freq](group__bt__audio.md#ga8e99fb678cc011bb8c9f6e1858bae0d7)

bt\_audio\_codec\_cfg\_freq

Codec configuration sampling freqency.

**Definition** audio.h:248

[bt\_audio\_codec\_cfg\_type](group__bt__audio.md#ga9230ec4d7518bd243207ba2decb1a974)

bt\_audio\_codec\_cfg\_type

Codec configuration types.

**Definition** audio.h:230

[bt\_audio\_codec\_cap\_freq](group__bt__audio.md#gaafc1106d5d305874ee2f540c850ff5b4)

bt\_audio\_codec\_cap\_freq

Supported frequencies bitfield.

**Definition** audio.h:84

[bt\_audio\_metadata\_type](group__bt__audio.md#gab53d0dd62bceff97cf8eed7d8cf80354)

bt\_audio\_metadata\_type

Codec metadata type IDs.

**Definition** audio.h:432

[BT\_AUDIO\_LANG\_SIZE](group__bt__audio.md#gab6e5f793d514626deca21940d35d8f21)

#define BT\_AUDIO\_LANG\_SIZE

Size of the stream language value, e.g.

**Definition** audio.h:58

[bt\_audio\_data\_get\_val](group__bt__audio.md#gabbd1b9c46caa9a19de6c95b08c31e5b5)

int bt\_audio\_data\_get\_val(const uint8\_t ltv\_data[], size\_t size, uint8\_t type, const uint8\_t \*\*data)

Get the value of a specific data type in an length-type-value data array.

[bt\_audio\_codec\_cap\_chan\_count](group__bt__audio.md#gae695b5d17359967703f2509db1671fa5)

bt\_audio\_codec\_cap\_chan\_count

Supported audio capabilities channel count bitfield.

**Definition** audio.h:165

[bt\_audio\_codec\_cap\_frame\_dur](group__bt__audio.md#gaf37e8e19f956afb3c3a413cbaa1a21f5)

bt\_audio\_codec\_cap\_frame\_dur

Supported frame durations bitfield.

**Definition** audio.h:136

[bt\_audio\_codec\_cap\_type](group__bt__audio.md#gaf58823a56eb36cfd22e582ab1ea3d015)

bt\_audio\_codec\_cap\_type

Codec capability types.

**Definition** audio.h:66

[bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3)

bt\_audio\_context

Audio Context Type for Generic Audio.

**Definition** audio.h:303

[bt\_audio\_data\_parse](group__bt__audio.md#gafd8574b16141162c95653f0aa2bf6ff7)

int bt\_audio\_data\_parse(const uint8\_t ltv[], size\_t size, bool(\*func)(struct bt\_data \*data, void \*user\_data), void \*user\_data)

Helper for parsing length-type-value data.

[BT\_AUDIO\_ACTIVE\_STATE\_ENABLED](group__bt__audio.md#gga16d403ec4db7be997682331ad365ff5fa6d062944e9c49001666769601ba1c940)

@ BT\_AUDIO\_ACTIVE\_STATE\_ENABLED

Audio data is being transmitted.

**Definition** audio.h:418

[BT\_AUDIO\_ACTIVE\_STATE\_DISABLED](group__bt__audio.md#gga16d403ec4db7be997682331ad365ff5fade27604ea8fd592aa5d0958e2ccde4f3)

@ BT\_AUDIO\_ACTIVE\_STATE\_DISABLED

No audio data is being transmitted.

**Definition** audio.h:416

[BT\_AUDIO\_ASSISTED\_LISTENING\_STREAM\_UNSPECIFIED](group__bt__audio.md#gga207fbf0fbca9b24cba02c7f1d184e7f5ab1714206feaa04b3be586ddb33ed5285)

@ BT\_AUDIO\_ASSISTED\_LISTENING\_STREAM\_UNSPECIFIED

Unspecified audio enhancement.

**Definition** audio.h:424

[BT\_AUDIO\_DIR\_SINK](group__bt__audio.md#gga5bd899fb5e4d844058184913866e462fa2adba49daa32ac7b040c3294f047ceb8)

@ BT\_AUDIO\_DIR\_SINK

Audio direction sink.

**Definition** audio.h:803

[BT\_AUDIO\_DIR\_SOURCE](group__bt__audio.md#gga5bd899fb5e4d844058184913866e462fa868695a31ebf95402a4bae2469f3aa6c)

@ BT\_AUDIO\_DIR\_SOURCE

Audio direction source.

**Definition** audio.h:810

[BT\_AUDIO\_LOCATION\_FRONT\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a06b34e67c9931f8b26562218cba51337)

@ BT\_AUDIO\_LOCATION\_FRONT\_CENTER

Front Center.

**Definition** audio.h:598

[BT\_AUDIO\_LOCATION\_TOP\_BACK\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a07e699c28bd847de3d85645dceb2ff06)

@ BT\_AUDIO\_LOCATION\_TOP\_BACK\_LEFT

Top Back Left.

**Definition** audio.h:626

[BT\_AUDIO\_LOCATION\_LOW\_FREQ\_EFFECTS\_2](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a0c304bdd529ad66acb71001caa1b361b)

@ BT\_AUDIO\_LOCATION\_LOW\_FREQ\_EFFECTS\_2

Low Frequency Effects 2.

**Definition** audio.h:612

[BT\_AUDIO\_LOCATION\_TOP\_SIDE\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a1cf8dea66e42f75ca85ba55124829a59)

@ BT\_AUDIO\_LOCATION\_TOP\_SIDE\_RIGHT

Top Side Right.

**Definition** audio.h:632

[BT\_AUDIO\_LOCATION\_FRONT\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a26d5ba460642bcf7fb2fc950082b70b3)

@ BT\_AUDIO\_LOCATION\_FRONT\_RIGHT

Front Right.

**Definition** audio.h:596

[BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a33d0f7c266f21fd086386f8c29ee31e8)

@ BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_RIGHT

Bottom Front Right.

**Definition** audio.h:640

[BT\_AUDIO\_LOCATION\_BACK\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a43f5070c2b4d39c38fa7900595d9b1aa)

@ BT\_AUDIO\_LOCATION\_BACK\_RIGHT

Back Right.

**Definition** audio.h:604

[BT\_AUDIO\_LOCATION\_TOP\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a555361fafade3bfb27dc713666757a1f)

@ BT\_AUDIO\_LOCATION\_TOP\_CENTER

Top Center.

**Definition** audio.h:624

[BT\_AUDIO\_LOCATION\_LEFT\_SURROUND](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a568a581c0ad653177f5d148d04bef0b6)

@ BT\_AUDIO\_LOCATION\_LEFT\_SURROUND

Left Surround.

**Definition** audio.h:646

[BT\_AUDIO\_LOCATION\_TOP\_FRONT\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a60b154a216d8e029deac7305500eaf2d)

@ BT\_AUDIO\_LOCATION\_TOP\_FRONT\_RIGHT

Top Front Right.

**Definition** audio.h:620

[BT\_AUDIO\_LOCATION\_FRONT\_RIGHT\_OF\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a725707ae4703a1f9b970de5b1e4e5692)

@ BT\_AUDIO\_LOCATION\_FRONT\_RIGHT\_OF\_CENTER

Front Right of Center.

**Definition** audio.h:608

[BT\_AUDIO\_LOCATION\_FRONT\_RIGHT\_WIDE](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a8649be1d5b7e8b312fc3374039cc0a71)

@ BT\_AUDIO\_LOCATION\_FRONT\_RIGHT\_WIDE

Front Right Wide.

**Definition** audio.h:644

[BT\_AUDIO\_LOCATION\_TOP\_BACK\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a8e81b80f732b0037493712b4baa21a69)

@ BT\_AUDIO\_LOCATION\_TOP\_BACK\_RIGHT

Top Back Right.

**Definition** audio.h:628

[BT\_AUDIO\_LOCATION\_MONO\_AUDIO](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a8f476de613cdcb2f9f677d40291aa5df)

@ BT\_AUDIO\_LOCATION\_MONO\_AUDIO

Mono Audio (no specified Audio Location).

**Definition** audio.h:592

[BT\_AUDIO\_LOCATION\_BACK\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a96906ff7918b0a3e3e7efe73a08d9896)

@ BT\_AUDIO\_LOCATION\_BACK\_LEFT

Back Left.

**Definition** audio.h:602

[BT\_AUDIO\_LOCATION\_RIGHT\_SURROUND](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a97954db823b6c6bed660ff2717600a5e)

@ BT\_AUDIO\_LOCATION\_RIGHT\_SURROUND

Right Surround.

**Definition** audio.h:648

[BT\_AUDIO\_LOCATION\_SIDE\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8aa01ad94f71defd158d8cfe25936341cd)

@ BT\_AUDIO\_LOCATION\_SIDE\_RIGHT

Side Right.

**Definition** audio.h:616

[BT\_AUDIO\_LOCATION\_TOP\_FRONT\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8aa093e6218e213eac5677766e01f5c1c9)

@ BT\_AUDIO\_LOCATION\_TOP\_FRONT\_LEFT

Top Front Left.

**Definition** audio.h:618

[BT\_AUDIO\_LOCATION\_SIDE\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ab8e52c69b894e382f0f09cc370337064)

@ BT\_AUDIO\_LOCATION\_SIDE\_LEFT

Side Left.

**Definition** audio.h:614

[BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ac1e355baee6ca0907356d72f0d4edb29)

@ BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_LEFT

Bottom Front Left.

**Definition** audio.h:638

[BT\_AUDIO\_LOCATION\_TOP\_FRONT\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ac32ed6f456be2fb2d9af2c7b255f3a4e)

@ BT\_AUDIO\_LOCATION\_TOP\_FRONT\_CENTER

Top Front Center.

**Definition** audio.h:622

[BT\_AUDIO\_LOCATION\_LOW\_FREQ\_EFFECTS\_1](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ac4c09f948266f2c9c65b3bc16da2f3f6)

@ BT\_AUDIO\_LOCATION\_LOW\_FREQ\_EFFECTS\_1

Low Frequency Effects 1.

**Definition** audio.h:600

[BT\_AUDIO\_LOCATION\_FRONT\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ac658188fa6f1b4f248a149d0bde1e41b)

@ BT\_AUDIO\_LOCATION\_FRONT\_LEFT

Front Left.

**Definition** audio.h:594

[BT\_AUDIO\_LOCATION\_FRONT\_LEFT\_WIDE](group__bt__audio.md#gga61230848c02098352320fe751332c4e8acba90183626ad85c21692b7edd87133d)

@ BT\_AUDIO\_LOCATION\_FRONT\_LEFT\_WIDE

Front Left Wide.

**Definition** audio.h:642

[BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ad0be8f720f03feb18a23e77f0eff6376)

@ BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_CENTER

Bottom Front Center.

**Definition** audio.h:636

[BT\_AUDIO\_LOCATION\_BACK\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ae22cd1e458d8ff503741bf48262c7983)

@ BT\_AUDIO\_LOCATION\_BACK\_CENTER

Back Center.

**Definition** audio.h:610

[BT\_AUDIO\_LOCATION\_TOP\_SIDE\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ae846b2f4186b46d3690c71071c41c7d6)

@ BT\_AUDIO\_LOCATION\_TOP\_SIDE\_LEFT

Top Side Left.

**Definition** audio.h:630

[BT\_AUDIO\_LOCATION\_TOP\_BACK\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8aebae1f0f2537a806672820fb74eba5dd)

@ BT\_AUDIO\_LOCATION\_TOP\_BACK\_CENTER

Top Back Center.

**Definition** audio.h:634

[BT\_AUDIO\_LOCATION\_FRONT\_LEFT\_OF\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8af02a9d46877b742e8730bbf3dd6ad22e)

@ BT\_AUDIO\_LOCATION\_FRONT\_LEFT\_OF\_CENTER

Front Left of Center.

**Definition** audio.h:606

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_18\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a22167e0c033c176f592a447b14c30071)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_18\_OR\_ABOVE

Recommended for listeners of age 18 and above.

**Definition** audio.h:410

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_15\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a3fe7bc3216a458ec3e5c6e177f43c077)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_15\_OR\_ABOVE

Recommended for listeners of age 15 and above.

**Definition** audio.h:404

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_10\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a4210d67d4506f8b9defb5fae32ae30d2)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_10\_OR\_ABOVE

Recommended for listeners of age 10 and above.

**Definition** audio.h:394

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_7\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a69508e569059bde1fed1b3fb3db1547a)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_7\_OR\_ABOVE

Recommended for listeners of age 7 and above.

**Definition** audio.h:388

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_16\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a779c5dd14e5f88e8e6bb247dc66d9c92)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_16\_OR\_ABOVE

Recommended for listeners of age 16 and above.

**Definition** audio.h:406

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_17\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a7d0794fe6796f19ff7e58819728751ff)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_17\_OR\_ABOVE

Recommended for listeners of age 17 and above.

**Definition** audio.h:408

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_5\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a8a8476abac3a569bd470a5237642c526)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_5\_OR\_ABOVE

Recommended for listeners of age 5 and above.

**Definition** audio.h:384

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_8\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a9ed111f80d0671bb8b4e0a304ff0b0e4)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_8\_OR\_ABOVE

Recommended for listeners of age 8 and above.

**Definition** audio.h:390

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_13\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760aa680247699538d256111e18af1a2d15d)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_13\_OR\_ABOVE

Recommended for listeners of age 13 and above.

**Definition** audio.h:400

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_9\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760aaabe26ebaa4b84684005440176ad86dd)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_9\_OR\_ABOVE

Recommended for listeners of age 9 and above.

**Definition** audio.h:392

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_11\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760ac402ee4c06b92f0cc36774cf409cbbd0)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_11\_OR\_ABOVE

Recommended for listeners of age 11 and above.

**Definition** audio.h:396

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_12\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760ac68caf6719391afbef79e0c579dc96e7)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_12\_OR\_ABOVE

Recommended for listeners of age 12 and above.

**Definition** audio.h:398

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_6\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760accb959ba21c1238c70c594b5cdc3ebdc)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_6\_OR\_ABOVE

Recommended for listeners of age 6 and above.

**Definition** audio.h:386

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_ANY](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760ad6bba6a3b9537fcf913f798ab9a525f1)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_ANY

For all ages.

**Definition** audio.h:382

[BT\_AUDIO\_PARENTAL\_RATING\_NO\_RATING](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760aecf628bbd76651215232c8bfed04aa2c)

@ BT\_AUDIO\_PARENTAL\_RATING\_NO\_RATING

No rating.

**Definition** audio.h:380

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_14\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760aef216d59983eccb86e90c493b8c17d86)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_14\_OR\_ABOVE

Recommended for listeners of age 14 and above.

**Definition** audio.h:402

[BT\_AUDIO\_CODEC\_CFG\_DURATION\_10](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ab6a0dd3bbe587ff5ba110675a01514a7)

@ BT\_AUDIO\_CODEC\_CFG\_DURATION\_10

10 msec Frame Duration configuration

**Definition** audio.h:295

[BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ad2491c0ded7c7f489bdeffe024463272)

@ BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5

7.5 msec Frame Duration configuration

**Definition** audio.h:292

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_24KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a0d6d0f278628681f8ef5dc3797bf5275)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_24KHZ

24 Khz codec sampling frequency

**Definition** audio.h:262

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a2b7163ba4c486167d3e81c2aa4216f11)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ

48 Khz codec sampling frequency

**Definition** audio.h:271

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a3ce97404475ad182125ad64aba66077e)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ

32 Khz codec sampling frequency

**Definition** audio.h:265

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_384KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a44cccbd3e7afc25f964b3c2c571d4be4)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_384KHZ

384 Khz codec sampling frequency

**Definition** audio.h:286

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_22KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a68f8411a83f60ec4c6bb9fa65fdd7048)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_22KHZ

22.05 Khz codec sampling frequency

**Definition** audio.h:259

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_8KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a7018d3fb612d4730b880ef0bb2d20b9a)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_8KHZ

8 Khz codec sampling frequency

**Definition** audio.h:250

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_96KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a79e7a473d3f7d6803f3b8b7843c40c60)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_96KHZ

96 Khz codec sampling frequency

**Definition** audio.h:277

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_176KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a85037a2eb4a64376a0a436ab43263126)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_176KHZ

176.4 Khz codec sampling frequency

**Definition** audio.h:280

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_44KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aa701e855c950fdcdd66d4dbaaf75fb84)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_44KHZ

44.1 Khz codec sampling frequency

**Definition** audio.h:268

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_192KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aa85a51db272ef019e5cce5ec3982f8c7)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_192KHZ

192 Khz codec sampling frequency

**Definition** audio.h:283

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_11KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aa8d8018b050a8c029b4b60c706d771f8)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_11KHZ

11.025 Khz codec sampling frequency

**Definition** audio.h:253

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_16KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7ab097ae9f9ad963fee64e61eaf2663245)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_16KHZ

16 Khz codec sampling frequency

**Definition** audio.h:256

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_88KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aff685ebe62909eea8512b7deac0df409)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_88KHZ

88.2 Khz codec sampling frequency

**Definition** audio.h:274

[BT\_AUDIO\_CODEC\_CFG\_FREQ](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974a49849b389d553535ea222c9ae63bccc3)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ

Sampling frequency.

**Definition** audio.h:232

[BT\_AUDIO\_CODEC\_CFG\_FRAME\_LEN](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974a85d41856175c11b1193ebdd58b83d6e2)

@ BT\_AUDIO\_CODEC\_CFG\_FRAME\_LEN

Octets per codec frame.

**Definition** audio.h:241

[BT\_AUDIO\_CODEC\_CFG\_DURATION](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974a8e2fae97b1565b0fa0ff988a47928223)

@ BT\_AUDIO\_CODEC\_CFG\_DURATION

Frame duration.

**Definition** audio.h:235

[BT\_AUDIO\_CODEC\_CFG\_FRAME\_BLKS\_PER\_SDU](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974abbc2279f5d029278d9367f08a1152aa8)

@ BT\_AUDIO\_CODEC\_CFG\_FRAME\_BLKS\_PER\_SDU

Codec frame blocks per SDU.

**Definition** audio.h:244

[BT\_AUDIO\_CODEC\_CFG\_CHAN\_ALLOC](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974ad53deb048fb0ce4d4428df4f477718b2)

@ BT\_AUDIO\_CODEC\_CFG\_CHAN\_ALLOC

Audio channel allocation.

**Definition** audio.h:238

[BT\_AUDIO\_CODEC\_CAP\_FREQ\_176KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a031d159eadf7ea1ba6b00b03bef26d2b)

@ BT\_AUDIO\_CODEC\_CAP\_FREQ\_176KHZ

176.4 Khz sampling frequency

**Definition** audio.h:116

[BT\_AUDIO\_CODEC\_CAP\_FREQ\_192KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a0de8d0351153650c1b48934053e18890)

@ BT\_AUDIO\_CODEC\_CAP\_FREQ\_192KHZ

192 Khz sampling frequency

**Definition** audio.h:119

[BT\_AUDIO\_CODEC\_CAP\_FREQ\_88KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a25cc72bd630446f5154c54402058a211)

@ BT\_AUDIO\_CODEC\_CAP\_FREQ\_88KHZ

88.2 Khz sampling frequency

**Definition** audio.h:110

[BT\_AUDIO\_CODEC\_CAP\_FREQ\_8KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a3d821d03771805107707f47dcdb71f83)

@ BT\_AUDIO\_CODEC\_CAP\_FREQ\_8KHZ

8 Khz sampling frequency

**Definition** audio.h:86

[BT\_AUDIO\_CODEC\_CAP\_FREQ\_11KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a562c38a59cded025183a0f95d4a63c81)

@ BT\_AUDIO\_CODEC\_CAP\_FREQ\_11KHZ

11.025 Khz sampling frequency

**Definition** audio.h:89

[BT\_AUDIO\_CODEC\_CAP\_FREQ\_32KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a822ff105ab495c126c21d73bd90cbd9c)

@ BT\_AUDIO\_CODEC\_CAP\_FREQ\_32KHZ

32 Khz sampling frequency

**Definition** audio.h:101

[BT\_AUDIO\_CODEC\_CAP\_FREQ\_48KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a91ec17ee96b8e56e31ab545e5e8abe91)

@ BT\_AUDIO\_CODEC\_CAP\_FREQ\_48KHZ

48 Khz sampling frequency

**Definition** audio.h:107

[BT\_AUDIO\_CODEC\_CAP\_FREQ\_24KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4acf9ff8842d72d56d27eae692e4c4b956)

@ BT\_AUDIO\_CODEC\_CAP\_FREQ\_24KHZ

24 Khz sampling frequency

**Definition** audio.h:98

[BT\_AUDIO\_CODEC\_CAP\_FREQ\_16KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4acfef6825ac865b1e590e7959a9270361)

@ BT\_AUDIO\_CODEC\_CAP\_FREQ\_16KHZ

16 Khz sampling frequency

**Definition** audio.h:92

[BT\_AUDIO\_CODEC\_CAP\_FREQ\_44KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ad28396f4b5a71d7c196e1a27bd17f8c3)

@ BT\_AUDIO\_CODEC\_CAP\_FREQ\_44KHZ

44.1 Khz sampling frequency

**Definition** audio.h:104

[BT\_AUDIO\_CODEC\_CAP\_FREQ\_22KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ad7440157cf8864dfc5fd854482f3a982)

@ BT\_AUDIO\_CODEC\_CAP\_FREQ\_22KHZ

22.05 Khz sampling frequency

**Definition** audio.h:95

[BT\_AUDIO\_CODEC\_CAP\_FREQ\_ANY](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4adaaa42a6bb0c01d3819c604b6d5bbf02)

@ BT\_AUDIO\_CODEC\_CAP\_FREQ\_ANY

Any frequency capability.

**Definition** audio.h:125

[BT\_AUDIO\_CODEC\_CAP\_FREQ\_384KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ae5ddc4504b7077e90be56f34ad8647c2)

@ BT\_AUDIO\_CODEC\_CAP\_FREQ\_384KHZ

384 Khz sampling frequency

**Definition** audio.h:122

[BT\_AUDIO\_CODEC\_CAP\_FREQ\_96KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ae802fea402f207238613275917846663)

@ BT\_AUDIO\_CODEC\_CAP\_FREQ\_96KHZ

96 Khz sampling frequency

**Definition** audio.h:113

[BT\_AUDIO\_METADATA\_TYPE\_PROGRAM\_INFO](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a02f91ea7fb6be631687d843ad7bf4ac7)

@ BT\_AUDIO\_METADATA\_TYPE\_PROGRAM\_INFO

UTF-8 encoded title or summary of stream content.

**Definition** audio.h:458

[BT\_AUDIO\_METADATA\_TYPE\_EXTENDED](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a0b5a8cd34bad81ac53c657c3cd9ddb39)

@ BT\_AUDIO\_METADATA\_TYPE\_EXTENDED

Extended metadata.

**Definition** audio.h:502

[BT\_AUDIO\_METADATA\_TYPE\_VENDOR](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a30fbc4a159e64174b22f195f29012286)

@ BT\_AUDIO\_METADATA\_TYPE\_VENDOR

Vendor specific metadata.

**Definition** audio.h:505

[BT\_AUDIO\_METADATA\_TYPE\_CCID\_LIST](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a37b5552e04734392dc6c6eb9e19b377b)

@ BT\_AUDIO\_METADATA\_TYPE\_CCID\_LIST

Array of 8-bit CCID values.

**Definition** audio.h:469

[BT\_AUDIO\_METADATA\_TYPE\_ASSISTED\_LISTENING\_STREAM](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a40aad5cb3574e6e4e7bc955bc12760bf)

@ BT\_AUDIO\_METADATA\_TYPE\_ASSISTED\_LISTENING\_STREAM

Assisted listening stream.

**Definition** audio.h:496

[BT\_AUDIO\_METADATA\_TYPE\_BROADCAST\_IMMEDIATE](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a4b9cc5b82a1dbfc3db69bb12747443f1)

@ BT\_AUDIO\_METADATA\_TYPE\_BROADCAST\_IMMEDIATE

Broadcast Audio Immediate Rendering flag.

**Definition** audio.h:489

[BT\_AUDIO\_METADATA\_TYPE\_PROGRAM\_INFO\_URI](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a58971ea21b5045e56a0e1ca838358922)

@ BT\_AUDIO\_METADATA\_TYPE\_PROGRAM\_INFO\_URI

UTF-8 encoded URI for additional Program information.

**Definition** audio.h:479

[BT\_AUDIO\_METADATA\_TYPE\_PARENTAL\_RATING](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a7a83f397dc5dbe6e6d60a994cccdc613)

@ BT\_AUDIO\_METADATA\_TYPE\_PARENTAL\_RATING

Parental rating.

**Definition** audio.h:476

[BT\_AUDIO\_METADATA\_TYPE\_STREAM\_CONTEXT](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a95f128b11584ee22100ae65ce751dbaa)

@ BT\_AUDIO\_METADATA\_TYPE\_STREAM\_CONTEXT

Streaming audio context.

**Definition** audio.h:455

[BT\_AUDIO\_METADATA\_TYPE\_PREF\_CONTEXT](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354aac28d2a0dc883affa60b7a70f678ed9a)

@ BT\_AUDIO\_METADATA\_TYPE\_PREF\_CONTEXT

Preferred audio context.

**Definition** audio.h:443

[BT\_AUDIO\_METADATA\_TYPE\_BROADCAST\_NAME](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354ada34d453c8ce75a155c59c371a67d8a6)

@ BT\_AUDIO\_METADATA\_TYPE\_BROADCAST\_NAME

UTF-8 encoded Broadcast name.

**Definition** audio.h:499

[BT\_AUDIO\_METADATA\_TYPE\_AUDIO\_STATE](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354af220c40d351ec5e236cd41a5944da5fc)

@ BT\_AUDIO\_METADATA\_TYPE\_AUDIO\_STATE

Audio active state.

**Definition** audio.h:486

[BT\_AUDIO\_METADATA\_TYPE\_LANG](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354af38d342d907c3903121a03bb8394efb1)

@ BT\_AUDIO\_METADATA\_TYPE\_LANG

Language.

**Definition** audio.h:466

[BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_4](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a0fdfa6bf69b104f04d22e4f968969ac2)

@ BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_4

Supporting 4 channel.

**Definition** audio.h:176

[BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_2](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a13b236d93eb9c7516fdcf527313e16cd)

@ BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_2

Supporting 2 channel.

**Definition** audio.h:170

[BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_1](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a1558716b36042597515df18ff277f8bc)

@ BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_1

Supporting 1 channel.

**Definition** audio.h:167

[BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_3](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a17da27ec39a79c341c82549df891cb39)

@ BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_3

Supporting 3 channel.

**Definition** audio.h:173

[BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_8](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a50afa60bdd53172fab7a376ce374d943)

@ BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_8

Supporting 8 channel.

**Definition** audio.h:188

[BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_7](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a86ef227772c7751b4ae75529e2a57b82)

@ BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_7

Supporting 7 channel.

**Definition** audio.h:185

[BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_ANY](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5aaf6f7179310c64b93b300ecfc29e4219)

@ BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_ANY

Supporting all channels.

**Definition** audio.h:191

[BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_5](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5ad08bc2ea0347a1ee8fd411a023b7ca51)

@ BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_5

Supporting 5 channel.

**Definition** audio.h:179

[BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_6](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5af9f9dd0cac39793793e5c8c5e50b11b8)

@ BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_6

Supporting 6 channel.

**Definition** audio.h:182

[BT\_AUDIO\_CODEC\_CAP\_DURATION\_7\_5](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a340878058d0beabeade33e0f3893d441)

@ BT\_AUDIO\_CODEC\_CAP\_DURATION\_7\_5

7.5 msec frame duration capability

**Definition** audio.h:138

[BT\_AUDIO\_CODEC\_CAP\_DURATION\_PREFER\_7\_5](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a7ab1c63639cf93fdf2c2dfdf43424e91)

@ BT\_AUDIO\_CODEC\_CAP\_DURATION\_PREFER\_7\_5

7.5 msec preferred frame duration capability.

**Definition** audio.h:153

[BT\_AUDIO\_CODEC\_CAP\_DURATION\_ANY](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a81d28ce43d69d4625e9a73b37c70347a)

@ BT\_AUDIO\_CODEC\_CAP\_DURATION\_ANY

Any frame duration capability.

**Definition** audio.h:144

[BT\_AUDIO\_CODEC\_CAP\_DURATION\_PREFER\_10](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a9744473b3a29074c24cf0bbff35a5d8e)

@ BT\_AUDIO\_CODEC\_CAP\_DURATION\_PREFER\_10

10 msec preferred frame duration capability

**Definition** audio.h:161

[BT\_AUDIO\_CODEC\_CAP\_DURATION\_10](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5afd423ac4270ff0df8ca6df7f5e4c799b)

@ BT\_AUDIO\_CODEC\_CAP\_DURATION\_10

10 msec frame duration capability

**Definition** audio.h:141

[BT\_AUDIO\_CODEC\_CAP\_TYPE\_CHAN\_COUNT](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015a0cd3a3d31febc9e30137e9e21d4f7191)

@ BT\_AUDIO\_CODEC\_CAP\_TYPE\_CHAN\_COUNT

Supported audio channel counts.

**Definition** audio.h:74

[BT\_AUDIO\_CODEC\_CAP\_TYPE\_DURATION](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015a4a90a37cd6d8ca9d1ed984e4a122d510)

@ BT\_AUDIO\_CODEC\_CAP\_TYPE\_DURATION

Supported frame durations.

**Definition** audio.h:71

[BT\_AUDIO\_CODEC\_CAP\_TYPE\_FRAME\_COUNT](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015acba980896f080ac2ba81d1b66305bb41)

@ BT\_AUDIO\_CODEC\_CAP\_TYPE\_FRAME\_COUNT

Supported maximum codec frames per SDU.

**Definition** audio.h:80

[BT\_AUDIO\_CODEC\_CAP\_TYPE\_FRAME\_LEN](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015ad074bed5f79946e2388584336d30cf46)

@ BT\_AUDIO\_CODEC\_CAP\_TYPE\_FRAME\_LEN

Supported octets per codec frame.

**Definition** audio.h:77

[BT\_AUDIO\_CODEC\_CAP\_TYPE\_FREQ](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015af68f3f5665446de9b71c2f70e7aa762b)

@ BT\_AUDIO\_CODEC\_CAP\_TYPE\_FREQ

Supported sampling frequencies.

**Definition** audio.h:68

[BT\_AUDIO\_CONTEXT\_TYPE\_NOTIFICATIONS](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a06df6f713bb68b197be75bf821d5d377)

@ BT\_AUDIO\_CONTEXT\_TYPE\_NOTIFICATIONS

Notification and reminder sounds; attention-seeking audio, for example, in beeps signaling the arriva...

**Definition** audio.h:341

[BT\_AUDIO\_CONTEXT\_TYPE\_EMERGENCY\_ALARM](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a132abd2f9ac7be62d1306efc6bc8b7d1)

@ BT\_AUDIO\_CONTEXT\_TYPE\_EMERGENCY\_ALARM

Emergency alarm Emergency sounds, for example, fire alarms or other urgent alerts.

**Definition** audio.h:353

[BT\_AUDIO\_CONTEXT\_TYPE\_INSTRUCTIONAL](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a2e3af6f4ca620f91d9266257f842ddd4)

@ BT\_AUDIO\_CONTEXT\_TYPE\_INSTRUCTIONAL

Instructional audio, for example, in navigation, announcements, or user guidance.

**Definition** audio.h:324

[BT\_AUDIO\_CONTEXT\_TYPE\_PROHIBITED](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a3cfcfa76adc5effdc1aa95d75e5da37a)

@ BT\_AUDIO\_CONTEXT\_TYPE\_PROHIBITED

Prohibited.

**Definition** audio.h:305

[BT\_AUDIO\_CONTEXT\_TYPE\_RINGTONE](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a422bb29f035583b7319456a679f880b3)

@ BT\_AUDIO\_CONTEXT\_TYPE\_RINGTONE

Alerts the user to an incoming call, for example, an incoming telephony or video call,...

**Definition** audio.h:346

[BT\_AUDIO\_CONTEXT\_TYPE\_LIVE](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a42c80228bda513d5a59d4d836e73bd55)

@ BT\_AUDIO\_CONTEXT\_TYPE\_LIVE

Live audio, for example, from a microphone where audio is perceived both through a direct acoustic pa...

**Definition** audio.h:331

[BT\_AUDIO\_CONTEXT\_TYPE\_MEDIA](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a43d67936976a5c041027d15d66c21a5e)

@ BT\_AUDIO\_CONTEXT\_TYPE\_MEDIA

Media, for example, music playback, radio, podcast or movie soundtrack, or tv audio.

**Definition** audio.h:317

[BT\_AUDIO\_CONTEXT\_TYPE\_GAME](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a652ad83b9eb524c62933bf87a8ecb730)

@ BT\_AUDIO\_CONTEXT\_TYPE\_GAME

Audio associated with video gaming, for example gaming media; gaming effects; music and in-game voice...

**Definition** audio.h:322

[BT\_AUDIO\_CONTEXT\_TYPE\_SOUND\_EFFECTS](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a6956a9e43433e2800fd36c7022e039d9)

@ BT\_AUDIO\_CONTEXT\_TYPE\_SOUND\_EFFECTS

Sound effects including keyboard and touch feedback; menu and user interface sounds; and other system...

**Definition** audio.h:336

[BT\_AUDIO\_CONTEXT\_TYPE\_VOICE\_ASSISTANTS](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a7e208290ddc2f92ac78ff4a22b20ca7e)

@ BT\_AUDIO\_CONTEXT\_TYPE\_VOICE\_ASSISTANTS

Man-machine communication, for example, with voice recognition or virtual assistants.

**Definition** audio.h:326

[BT\_AUDIO\_CONTEXT\_TYPE\_CONVERSATIONAL](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a8a6262c1cf4e4591a7b92b4f8f329f9e)

@ BT\_AUDIO\_CONTEXT\_TYPE\_CONVERSATIONAL

Conversation between humans, for example, in telephony or video calls, including traditional cellular...

**Definition** audio.h:315

[BT\_AUDIO\_CONTEXT\_TYPE\_ALERTS](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a915d05a728f3e083f290766a970dabb6)

@ BT\_AUDIO\_CONTEXT\_TYPE\_ALERTS

Alarms and timers; immediate alerts, for example, in a critical battery alarm, timer expiry or alarm ...

**Definition** audio.h:351

[BT\_AUDIO\_CONTEXT\_TYPE\_UNSPECIFIED](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3aad96be1265bd1be4c937c687335e33f5)

@ BT\_AUDIO\_CONTEXT\_TYPE\_UNSPECIFIED

Identifies audio where the use case context does not match any other defined value,...

**Definition** audio.h:310

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[hci.h](hci_8h.md)

[iso.h](iso_8h.md)

Bluetooth ISO handling.

[lc3.h](lc3_8h.md)

Bluetooth LC3 codec handling.

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[stdbool.h](stdbool_8h.md)

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[bt\_audio\_codec\_cap](structbt__audio__codec__cap.md)

Codec capability structure.

**Definition** audio.h:684

[bt\_audio\_codec\_cap::vid](structbt__audio__codec__cap.md#a3b91269e16a3d63b3128a527caa5e3ff)

uint16\_t vid

Codec Company Vendor ID.

**Definition** audio.h:702

[bt\_audio\_codec\_cap::data](structbt__audio__codec__cap.md#a455638aac9167d288a1e7a9fccabc49d)

uint8\_t data[CONFIG\_BT\_AUDIO\_CODEC\_CAP\_MAX\_DATA\_SIZE]

Codec Specific Capabilities Data.

**Definition** audio.h:707

[bt\_audio\_codec\_cap::cid](structbt__audio__codec__cap.md#a763222d12a87958a5ba806303f98829a)

uint16\_t cid

Codec Company ID.

**Definition** audio.h:700

[bt\_audio\_codec\_cap::path\_id](structbt__audio__codec__cap.md#a822a06f815091cc580ca2e5bbb3126f7)

uint8\_t path\_id

Data path ID.

**Definition** audio.h:690

[bt\_audio\_codec\_cap::ctlr\_transcode](structbt__audio__codec__cap.md#a900a77db09e72de61d4ff652c6dbb10b)

bool ctlr\_transcode

Whether or not the local controller should transcode.

**Definition** audio.h:696

[bt\_audio\_codec\_cap::meta](structbt__audio__codec__cap.md#acec4f5e31752d81d4dbf441223e7f44c)

uint8\_t meta[CONFIG\_BT\_AUDIO\_CODEC\_CAP\_MAX\_METADATA\_SIZE]

Codec Specific Capabilities Metadata.

**Definition** audio.h:713

[bt\_audio\_codec\_cap::data\_len](structbt__audio__codec__cap.md#acf3e22c6db1533fff7015acbc7eca196)

size\_t data\_len

Codec Specific Capabilities Data count.

**Definition** audio.h:705

[bt\_audio\_codec\_cap::id](structbt__audio__codec__cap.md#ae3892731e7ca05f3ec426c70f0d9e1a9)

uint8\_t id

Codec ID.

**Definition** audio.h:698

[bt\_audio\_codec\_cap::meta\_len](structbt__audio__codec__cap.md#afe806521d5aac36e9f6c6a0598500a8f)

size\_t meta\_len

Codec Specific Capabilities Metadata count.

**Definition** audio.h:711

[bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md)

Codec specific configuration structure.

**Definition** audio.h:718

[bt\_audio\_codec\_cfg::meta\_len](structbt__audio__codec__cfg.md#a1e69a5c017e9571b50aba721f86876fb)

size\_t meta\_len

Codec Specific Capabilities Metadata count.

**Definition** audio.h:745

[bt\_audio\_codec\_cfg::vid](structbt__audio__codec__cfg.md#a2996ab3f6ae1cab09ff5e3329b42468e)

uint16\_t vid

Codec Company Vendor ID.

**Definition** audio.h:736

[bt\_audio\_codec\_cfg::meta](structbt__audio__codec__cfg.md#a4f84974ea14b773ad8e2fd7c0ffa0c7f)

uint8\_t meta[CONFIG\_BT\_AUDIO\_CODEC\_CFG\_MAX\_METADATA\_SIZE]

Codec Specific Capabilities Metadata.

**Definition** audio.h:747

[bt\_audio\_codec\_cfg::cid](structbt__audio__codec__cfg.md#a664e21bcd6002b21d4b1b53d866db32d)

uint16\_t cid

Codec Company ID.

**Definition** audio.h:734

[bt\_audio\_codec\_cfg::data\_len](structbt__audio__codec__cfg.md#a8a5a789e9993a48ce4c83a2156c1f43c)

size\_t data\_len

Codec Specific Capabilities Data count.

**Definition** audio.h:739

[bt\_audio\_codec\_cfg::path\_id](structbt__audio__codec__cfg.md#a9386056bb02908407c9e3aad48abbd87)

uint8\_t path\_id

Data path ID.

**Definition** audio.h:724

[bt\_audio\_codec\_cfg::ctlr\_transcode](structbt__audio__codec__cfg.md#a9e2c8081950a0830ffc270245ab308c1)

bool ctlr\_transcode

Whether or not the local controller should transcode.

**Definition** audio.h:730

[bt\_audio\_codec\_cfg::id](structbt__audio__codec__cfg.md#aa2f99ec31ff3eb9b7b738bc8a1170f20)

uint8\_t id

Codec ID.

**Definition** audio.h:732

[bt\_audio\_codec\_cfg::data](structbt__audio__codec__cfg.md#ad3709d5321f6faeb392452cb3b21023b)

uint8\_t data[CONFIG\_BT\_AUDIO\_CODEC\_CFG\_MAX\_DATA\_SIZE]

Codec Specific Capabilities Data.

**Definition** audio.h:741

[bt\_audio\_codec\_octets\_per\_codec\_frame](structbt__audio__codec__octets__per__codec__frame.md)

struct to hold minimum and maximum supported codec frame sizes

**Definition** audio.h:217

[bt\_audio\_codec\_octets\_per\_codec\_frame::min](structbt__audio__codec__octets__per__codec__frame.md#aa8b234fa137273cd16230ebabc5f8ef4)

uint16\_t min

Minimum number of octets supported per codec frame.

**Definition** audio.h:219

[bt\_audio\_codec\_octets\_per\_codec\_frame::max](structbt__audio__codec__octets__per__codec__frame.md#ae09686799077b13e78b856b1e7e63b6a)

uint16\_t max

Maximum number of octets supported per codec frame.

**Definition** audio.h:221

[bt\_data](structbt__data.md)

Bluetooth data.

**Definition** bluetooth.h:456

[atomic.h](sys_2atomic_8h.md)

[util.h](sys_2util_8h.md)

Misc utilities.

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [audio.h](bluetooth_2audio_2audio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
