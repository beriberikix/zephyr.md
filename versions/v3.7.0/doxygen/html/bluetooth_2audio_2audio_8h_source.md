---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/bluetooth_2audio_2audio_8h_source.html
original_path: doxygen/html/bluetooth_2audio_2audio_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

35#include <[zephyr/sys/util.h](util_8h.md)>

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

[ 51](group__bt__audio.md#ga6eedc1f97491b38fe20b91688c62ffc0)#define BT\_AUDIO\_BROADCAST\_CODE\_SIZE 16

52

[ 54](group__bt__audio.md#gaa3bf677a479a90793f28a5a3ed69c7e0)#define BT\_AUDIO\_BROADCAST\_NAME\_LEN\_MIN 4

[ 56](group__bt__audio.md#gaa2fafcbb6a826c3f4cee16ebb545dad6)#define BT\_AUDIO\_BROADCAST\_NAME\_LEN\_MAX 128

57

[ 59](group__bt__audio.md#gab6e5f793d514626deca21940d35d8f21)#define BT\_AUDIO\_LANG\_SIZE 3

60

[ 67](group__bt__audio.md#gaf58823a56eb36cfd22e582ab1ea3d015)enum [bt\_audio\_codec\_cap\_type](group__bt__audio.md#gaf58823a56eb36cfd22e582ab1ea3d015) {

[ 69](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015af68f3f5665446de9b71c2f70e7aa762b) [BT\_AUDIO\_CODEC\_CAP\_TYPE\_FREQ](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015af68f3f5665446de9b71c2f70e7aa762b) = 0x01,

70

[ 72](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015a4a90a37cd6d8ca9d1ed984e4a122d510) [BT\_AUDIO\_CODEC\_CAP\_TYPE\_DURATION](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015a4a90a37cd6d8ca9d1ed984e4a122d510) = 0x02,

73

[ 75](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015a0cd3a3d31febc9e30137e9e21d4f7191) [BT\_AUDIO\_CODEC\_CAP\_TYPE\_CHAN\_COUNT](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015a0cd3a3d31febc9e30137e9e21d4f7191) = 0x03,

76

[ 78](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015ad074bed5f79946e2388584336d30cf46) [BT\_AUDIO\_CODEC\_CAP\_TYPE\_FRAME\_LEN](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015ad074bed5f79946e2388584336d30cf46) = 0x04,

79

[ 81](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015acba980896f080ac2ba81d1b66305bb41) [BT\_AUDIO\_CODEC\_CAP\_TYPE\_FRAME\_COUNT](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015acba980896f080ac2ba81d1b66305bb41) = 0x05,

82};

83

[ 85](group__bt__audio.md#gaafc1106d5d305874ee2f540c850ff5b4)enum [bt\_audio\_codec\_cap\_freq](group__bt__audio.md#gaafc1106d5d305874ee2f540c850ff5b4) {

[ 87](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a3d821d03771805107707f47dcdb71f83) [BT\_AUDIO\_CODEC\_CAP\_FREQ\_8KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a3d821d03771805107707f47dcdb71f83) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

88

[ 90](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a562c38a59cded025183a0f95d4a63c81) [BT\_AUDIO\_CODEC\_CAP\_FREQ\_11KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a562c38a59cded025183a0f95d4a63c81) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

91

[ 93](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4acfef6825ac865b1e590e7959a9270361) [BT\_AUDIO\_CODEC\_CAP\_FREQ\_16KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4acfef6825ac865b1e590e7959a9270361) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

94

[ 96](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ad7440157cf8864dfc5fd854482f3a982) [BT\_AUDIO\_CODEC\_CAP\_FREQ\_22KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ad7440157cf8864dfc5fd854482f3a982) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

97

[ 99](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4acf9ff8842d72d56d27eae692e4c4b956) [BT\_AUDIO\_CODEC\_CAP\_FREQ\_24KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4acf9ff8842d72d56d27eae692e4c4b956) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

100

[ 102](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a822ff105ab495c126c21d73bd90cbd9c) [BT\_AUDIO\_CODEC\_CAP\_FREQ\_32KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a822ff105ab495c126c21d73bd90cbd9c) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

103

[ 105](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ad28396f4b5a71d7c196e1a27bd17f8c3) [BT\_AUDIO\_CODEC\_CAP\_FREQ\_44KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ad28396f4b5a71d7c196e1a27bd17f8c3) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6),

106

[ 108](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a91ec17ee96b8e56e31ab545e5e8abe91) [BT\_AUDIO\_CODEC\_CAP\_FREQ\_48KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a91ec17ee96b8e56e31ab545e5e8abe91) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7),

109

[ 111](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a25cc72bd630446f5154c54402058a211) [BT\_AUDIO\_CODEC\_CAP\_FREQ\_88KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a25cc72bd630446f5154c54402058a211) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8),

112

[ 114](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ae802fea402f207238613275917846663) [BT\_AUDIO\_CODEC\_CAP\_FREQ\_96KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ae802fea402f207238613275917846663) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9),

115

[ 117](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a031d159eadf7ea1ba6b00b03bef26d2b) [BT\_AUDIO\_CODEC\_CAP\_FREQ\_176KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a031d159eadf7ea1ba6b00b03bef26d2b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10),

118

[ 120](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a0de8d0351153650c1b48934053e18890) [BT\_AUDIO\_CODEC\_CAP\_FREQ\_192KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a0de8d0351153650c1b48934053e18890) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11),

121

[ 123](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ae5ddc4504b7077e90be56f34ad8647c2) [BT\_AUDIO\_CODEC\_CAP\_FREQ\_384KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ae5ddc4504b7077e90be56f34ad8647c2) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12),

124

[ 126](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4adaaa42a6bb0c01d3819c604b6d5bbf02) [BT\_AUDIO\_CODEC\_CAP\_FREQ\_ANY](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4adaaa42a6bb0c01d3819c604b6d5bbf02) =

127 ([BT\_AUDIO\_CODEC\_CAP\_FREQ\_8KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a3d821d03771805107707f47dcdb71f83) | [BT\_AUDIO\_CODEC\_CAP\_FREQ\_11KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a562c38a59cded025183a0f95d4a63c81) |

128 [BT\_AUDIO\_CODEC\_CAP\_FREQ\_16KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4acfef6825ac865b1e590e7959a9270361) | [BT\_AUDIO\_CODEC\_CAP\_FREQ\_22KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ad7440157cf8864dfc5fd854482f3a982) |

129 [BT\_AUDIO\_CODEC\_CAP\_FREQ\_24KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4acf9ff8842d72d56d27eae692e4c4b956) | [BT\_AUDIO\_CODEC\_CAP\_FREQ\_32KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a822ff105ab495c126c21d73bd90cbd9c) |

130 [BT\_AUDIO\_CODEC\_CAP\_FREQ\_44KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ad28396f4b5a71d7c196e1a27bd17f8c3) | [BT\_AUDIO\_CODEC\_CAP\_FREQ\_48KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a91ec17ee96b8e56e31ab545e5e8abe91) |

131 [BT\_AUDIO\_CODEC\_CAP\_FREQ\_88KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a25cc72bd630446f5154c54402058a211) | [BT\_AUDIO\_CODEC\_CAP\_FREQ\_96KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ae802fea402f207238613275917846663) |

132 [BT\_AUDIO\_CODEC\_CAP\_FREQ\_176KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a031d159eadf7ea1ba6b00b03bef26d2b) | [BT\_AUDIO\_CODEC\_CAP\_FREQ\_192KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a0de8d0351153650c1b48934053e18890) |

133 [BT\_AUDIO\_CODEC\_CAP\_FREQ\_384KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ae5ddc4504b7077e90be56f34ad8647c2)),

134};

135

[ 137](group__bt__audio.md#gaf37e8e19f956afb3c3a413cbaa1a21f5)enum [bt\_audio\_codec\_cap\_frame\_dur](group__bt__audio.md#gaf37e8e19f956afb3c3a413cbaa1a21f5) {

[ 139](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a340878058d0beabeade33e0f3893d441) [BT\_AUDIO\_CODEC\_CAP\_DURATION\_7\_5](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a340878058d0beabeade33e0f3893d441) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

140

[ 142](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5afd423ac4270ff0df8ca6df7f5e4c799b) [BT\_AUDIO\_CODEC\_CAP\_DURATION\_10](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5afd423ac4270ff0df8ca6df7f5e4c799b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

143

[ 145](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a81d28ce43d69d4625e9a73b37c70347a) [BT\_AUDIO\_CODEC\_CAP\_DURATION\_ANY](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a81d28ce43d69d4625e9a73b37c70347a) =

146 ([BT\_AUDIO\_CODEC\_CAP\_DURATION\_7\_5](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a340878058d0beabeade33e0f3893d441) | [BT\_AUDIO\_CODEC\_CAP\_DURATION\_10](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5afd423ac4270ff0df8ca6df7f5e4c799b)),

147

[ 154](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a7ab1c63639cf93fdf2c2dfdf43424e91) [BT\_AUDIO\_CODEC\_CAP\_DURATION\_PREFER\_7\_5](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a7ab1c63639cf93fdf2c2dfdf43424e91) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

155

[ 162](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a9744473b3a29074c24cf0bbff35a5d8e) [BT\_AUDIO\_CODEC\_CAP\_DURATION\_PREFER\_10](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a9744473b3a29074c24cf0bbff35a5d8e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

163};

164

[ 166](group__bt__audio.md#gae695b5d17359967703f2509db1671fa5)enum [bt\_audio\_codec\_cap\_chan\_count](group__bt__audio.md#gae695b5d17359967703f2509db1671fa5) {

[ 168](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a1558716b36042597515df18ff277f8bc) [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_1](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a1558716b36042597515df18ff277f8bc) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

169

[ 171](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a13b236d93eb9c7516fdcf527313e16cd) [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_2](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a13b236d93eb9c7516fdcf527313e16cd) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

172

[ 174](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a17da27ec39a79c341c82549df891cb39) [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_3](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a17da27ec39a79c341c82549df891cb39) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

175

[ 177](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a0fdfa6bf69b104f04d22e4f968969ac2) [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_4](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a0fdfa6bf69b104f04d22e4f968969ac2) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

178

[ 180](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5ad08bc2ea0347a1ee8fd411a023b7ca51) [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_5](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5ad08bc2ea0347a1ee8fd411a023b7ca51) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

181

[ 183](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5af9f9dd0cac39793793e5c8c5e50b11b8) [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_6](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5af9f9dd0cac39793793e5c8c5e50b11b8) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

184

[ 186](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a86ef227772c7751b4ae75529e2a57b82) [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_7](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a86ef227772c7751b4ae75529e2a57b82) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6),

187

[ 189](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a50afa60bdd53172fab7a376ce374d943) [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_8](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a50afa60bdd53172fab7a376ce374d943) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7),

190

[ 192](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5aaf6f7179310c64b93b300ecfc29e4219) [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_ANY](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5aaf6f7179310c64b93b300ecfc29e4219) =

193 ([BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_1](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a1558716b36042597515df18ff277f8bc) | [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_2](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a13b236d93eb9c7516fdcf527313e16cd) |

194 [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_3](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a17da27ec39a79c341c82549df891cb39) | [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_4](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a0fdfa6bf69b104f04d22e4f968969ac2) |

195 [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_5](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5ad08bc2ea0347a1ee8fd411a023b7ca51) | [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_6](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5af9f9dd0cac39793793e5c8c5e50b11b8) |

196 [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_7](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a86ef227772c7751b4ae75529e2a57b82) | [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_8](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a50afa60bdd53172fab7a376ce374d943)),

197};

198

[ 200](group__bt__audio.md#gac1251f8a35b5e343eeeff87f22f8ab10)#define BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_MIN 1

[ 202](group__bt__audio.md#gad91341739d394f92ffc4988b614f47b6)#define BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_MAX 8

203

[ 214](group__bt__audio.md#ga8f835266fabd6461216fe13e1b3b3a0f)#define BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_SUPPORT(...) \

215 ((enum bt\_audio\_codec\_cap\_chan\_count)((FOR\_EACH(BIT, (|), \_\_VA\_ARGS\_\_)) >> 1))

216

[ 218](structbt__audio__codec__octets__per__codec__frame.md)struct [bt\_audio\_codec\_octets\_per\_codec\_frame](structbt__audio__codec__octets__per__codec__frame.md) {

[ 220](structbt__audio__codec__octets__per__codec__frame.md#aa8b234fa137273cd16230ebabc5f8ef4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [min](structbt__audio__codec__octets__per__codec__frame.md#aa8b234fa137273cd16230ebabc5f8ef4);

[ 222](structbt__audio__codec__octets__per__codec__frame.md#ae09686799077b13e78b856b1e7e63b6a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max](structbt__audio__codec__octets__per__codec__frame.md#ae09686799077b13e78b856b1e7e63b6a);

223};

224

[ 231](group__bt__audio.md#ga9230ec4d7518bd243207ba2decb1a974)enum [bt\_audio\_codec\_cfg\_type](group__bt__audio.md#ga9230ec4d7518bd243207ba2decb1a974) {

[ 233](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974a49849b389d553535ea222c9ae63bccc3) [BT\_AUDIO\_CODEC\_CFG\_FREQ](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974a49849b389d553535ea222c9ae63bccc3) = 0x01,

234

[ 236](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974a8e2fae97b1565b0fa0ff988a47928223) [BT\_AUDIO\_CODEC\_CFG\_DURATION](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974a8e2fae97b1565b0fa0ff988a47928223) = 0x02,

237

[ 239](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974ad53deb048fb0ce4d4428df4f477718b2) [BT\_AUDIO\_CODEC\_CFG\_CHAN\_ALLOC](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974ad53deb048fb0ce4d4428df4f477718b2) = 0x03,

240

[ 242](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974a85d41856175c11b1193ebdd58b83d6e2) [BT\_AUDIO\_CODEC\_CFG\_FRAME\_LEN](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974a85d41856175c11b1193ebdd58b83d6e2) = 0x04,

243

[ 245](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974abbc2279f5d029278d9367f08a1152aa8) [BT\_AUDIO\_CODEC\_CFG\_FRAME\_BLKS\_PER\_SDU](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974abbc2279f5d029278d9367f08a1152aa8) = 0x05,

246};

247

[ 249](group__bt__audio.md#ga8e99fb678cc011bb8c9f6e1858bae0d7)enum [bt\_audio\_codec\_cfg\_freq](group__bt__audio.md#ga8e99fb678cc011bb8c9f6e1858bae0d7) {

[ 251](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a7018d3fb612d4730b880ef0bb2d20b9a) [BT\_AUDIO\_CODEC\_CFG\_FREQ\_8KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a7018d3fb612d4730b880ef0bb2d20b9a) = 0x01,

252

[ 254](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aa8d8018b050a8c029b4b60c706d771f8) [BT\_AUDIO\_CODEC\_CFG\_FREQ\_11KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aa8d8018b050a8c029b4b60c706d771f8) = 0x02,

255

[ 257](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7ab097ae9f9ad963fee64e61eaf2663245) [BT\_AUDIO\_CODEC\_CFG\_FREQ\_16KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7ab097ae9f9ad963fee64e61eaf2663245) = 0x03,

258

[ 260](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a68f8411a83f60ec4c6bb9fa65fdd7048) [BT\_AUDIO\_CODEC\_CFG\_FREQ\_22KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a68f8411a83f60ec4c6bb9fa65fdd7048) = 0x04,

261

[ 263](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a0d6d0f278628681f8ef5dc3797bf5275) [BT\_AUDIO\_CODEC\_CFG\_FREQ\_24KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a0d6d0f278628681f8ef5dc3797bf5275) = 0x05,

264

[ 266](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a3ce97404475ad182125ad64aba66077e) [BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a3ce97404475ad182125ad64aba66077e) = 0x06,

267

[ 269](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aa701e855c950fdcdd66d4dbaaf75fb84) [BT\_AUDIO\_CODEC\_CFG\_FREQ\_44KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aa701e855c950fdcdd66d4dbaaf75fb84) = 0x07,

270

[ 272](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a2b7163ba4c486167d3e81c2aa4216f11) [BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a2b7163ba4c486167d3e81c2aa4216f11) = 0x08,

273

[ 275](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aff685ebe62909eea8512b7deac0df409) [BT\_AUDIO\_CODEC\_CFG\_FREQ\_88KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aff685ebe62909eea8512b7deac0df409) = 0x09,

276

[ 278](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a79e7a473d3f7d6803f3b8b7843c40c60) [BT\_AUDIO\_CODEC\_CFG\_FREQ\_96KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a79e7a473d3f7d6803f3b8b7843c40c60) = 0x0a,

279

[ 281](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a85037a2eb4a64376a0a436ab43263126) [BT\_AUDIO\_CODEC\_CFG\_FREQ\_176KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a85037a2eb4a64376a0a436ab43263126) = 0x0b,

282

[ 284](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aa85a51db272ef019e5cce5ec3982f8c7) [BT\_AUDIO\_CODEC\_CFG\_FREQ\_192KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aa85a51db272ef019e5cce5ec3982f8c7) = 0x0c,

285

[ 287](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a44cccbd3e7afc25f964b3c2c571d4be4) [BT\_AUDIO\_CODEC\_CFG\_FREQ\_384KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a44cccbd3e7afc25f964b3c2c571d4be4) = 0x0d,

288};

289

[ 291](group__bt__audio.md#ga83701b5eadfcbc9b84dc0b1a85ebeb74)enum [bt\_audio\_codec\_cfg\_frame\_dur](group__bt__audio.md#ga83701b5eadfcbc9b84dc0b1a85ebeb74) {

[ 293](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ad2491c0ded7c7f489bdeffe024463272) [BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ad2491c0ded7c7f489bdeffe024463272) = 0x00,

294

[ 296](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ab6a0dd3bbe587ff5ba110675a01514a7) [BT\_AUDIO\_CODEC\_CFG\_DURATION\_10](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ab6a0dd3bbe587ff5ba110675a01514a7) = 0x01,

297};

298

[ 304](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3)enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) {

[ 306](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a3cfcfa76adc5effdc1aa95d75e5da37a) [BT\_AUDIO\_CONTEXT\_TYPE\_PROHIBITED](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a3cfcfa76adc5effdc1aa95d75e5da37a) = 0,

[ 311](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3aad96be1265bd1be4c937c687335e33f5) [BT\_AUDIO\_CONTEXT\_TYPE\_UNSPECIFIED](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3aad96be1265bd1be4c937c687335e33f5) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 316](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a8a6262c1cf4e4591a7b92b4f8f329f9e) [BT\_AUDIO\_CONTEXT\_TYPE\_CONVERSATIONAL](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a8a6262c1cf4e4591a7b92b4f8f329f9e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 318](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a43d67936976a5c041027d15d66c21a5e) [BT\_AUDIO\_CONTEXT\_TYPE\_MEDIA](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a43d67936976a5c041027d15d66c21a5e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 323](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a652ad83b9eb524c62933bf87a8ecb730) [BT\_AUDIO\_CONTEXT\_TYPE\_GAME](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a652ad83b9eb524c62933bf87a8ecb730) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

[ 325](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a2e3af6f4ca620f91d9266257f842ddd4) [BT\_AUDIO\_CONTEXT\_TYPE\_INSTRUCTIONAL](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a2e3af6f4ca620f91d9266257f842ddd4) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

[ 327](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a7e208290ddc2f92ac78ff4a22b20ca7e) [BT\_AUDIO\_CONTEXT\_TYPE\_VOICE\_ASSISTANTS](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a7e208290ddc2f92ac78ff4a22b20ca7e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

[ 332](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a42c80228bda513d5a59d4d836e73bd55) [BT\_AUDIO\_CONTEXT\_TYPE\_LIVE](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a42c80228bda513d5a59d4d836e73bd55) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6),

[ 337](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a6956a9e43433e2800fd36c7022e039d9) [BT\_AUDIO\_CONTEXT\_TYPE\_SOUND\_EFFECTS](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a6956a9e43433e2800fd36c7022e039d9) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7),

[ 342](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a06df6f713bb68b197be75bf821d5d377) [BT\_AUDIO\_CONTEXT\_TYPE\_NOTIFICATIONS](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a06df6f713bb68b197be75bf821d5d377) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8),

[ 347](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a422bb29f035583b7319456a679f880b3) [BT\_AUDIO\_CONTEXT\_TYPE\_RINGTONE](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a422bb29f035583b7319456a679f880b3) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9),

[ 352](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a915d05a728f3e083f290766a970dabb6) [BT\_AUDIO\_CONTEXT\_TYPE\_ALERTS](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a915d05a728f3e083f290766a970dabb6) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10),

[ 354](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a132abd2f9ac7be62d1306efc6bc8b7d1) [BT\_AUDIO\_CONTEXT\_TYPE\_EMERGENCY\_ALARM](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a132abd2f9ac7be62d1306efc6bc8b7d1) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11),

355};

356

[ 360](group__bt__audio.md#ga6320f86aab9b227385bdf52a9ff3985b)#define BT\_AUDIO\_CONTEXT\_TYPE\_ANY (BT\_AUDIO\_CONTEXT\_TYPE\_UNSPECIFIED | \

361 BT\_AUDIO\_CONTEXT\_TYPE\_CONVERSATIONAL | \

362 BT\_AUDIO\_CONTEXT\_TYPE\_MEDIA | \

363 BT\_AUDIO\_CONTEXT\_TYPE\_GAME | \

364 BT\_AUDIO\_CONTEXT\_TYPE\_INSTRUCTIONAL | \

365 BT\_AUDIO\_CONTEXT\_TYPE\_VOICE\_ASSISTANTS | \

366 BT\_AUDIO\_CONTEXT\_TYPE\_LIVE | \

367 BT\_AUDIO\_CONTEXT\_TYPE\_SOUND\_EFFECTS | \

368 BT\_AUDIO\_CONTEXT\_TYPE\_NOTIFICATIONS | \

369 BT\_AUDIO\_CONTEXT\_TYPE\_RINGTONE | \

370 BT\_AUDIO\_CONTEXT\_TYPE\_ALERTS | \

371 BT\_AUDIO\_CONTEXT\_TYPE\_EMERGENCY\_ALARM)

372

[ 379](group__bt__audio.md#ga6d4aff1f93dc0b902e4b5d1355f15760)enum [bt\_audio\_parental\_rating](group__bt__audio.md#ga6d4aff1f93dc0b902e4b5d1355f15760) {

[ 381](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760aecf628bbd76651215232c8bfed04aa2c) [BT\_AUDIO\_PARENTAL\_RATING\_NO\_RATING](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760aecf628bbd76651215232c8bfed04aa2c) = 0x00,

[ 383](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760ad6bba6a3b9537fcf913f798ab9a525f1) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_ANY](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760ad6bba6a3b9537fcf913f798ab9a525f1) = 0x01,

[ 385](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a8a8476abac3a569bd470a5237642c526) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_5\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a8a8476abac3a569bd470a5237642c526) = 0x02,

[ 387](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760accb959ba21c1238c70c594b5cdc3ebdc) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_6\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760accb959ba21c1238c70c594b5cdc3ebdc) = 0x03,

[ 389](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a69508e569059bde1fed1b3fb3db1547a) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_7\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a69508e569059bde1fed1b3fb3db1547a) = 0x04,

[ 391](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a9ed111f80d0671bb8b4e0a304ff0b0e4) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_8\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a9ed111f80d0671bb8b4e0a304ff0b0e4) = 0x05,

[ 393](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760aaabe26ebaa4b84684005440176ad86dd) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_9\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760aaabe26ebaa4b84684005440176ad86dd) = 0x06,

[ 395](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a4210d67d4506f8b9defb5fae32ae30d2) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_10\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a4210d67d4506f8b9defb5fae32ae30d2) = 0x07,

[ 397](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760ac402ee4c06b92f0cc36774cf409cbbd0) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_11\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760ac402ee4c06b92f0cc36774cf409cbbd0) = 0x08,

[ 399](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760ac68caf6719391afbef79e0c579dc96e7) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_12\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760ac68caf6719391afbef79e0c579dc96e7) = 0x09,

[ 401](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760aa680247699538d256111e18af1a2d15d) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_13\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760aa680247699538d256111e18af1a2d15d) = 0x0A,

[ 403](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760aef216d59983eccb86e90c493b8c17d86) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_14\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760aef216d59983eccb86e90c493b8c17d86) = 0x0B,

[ 405](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a3fe7bc3216a458ec3e5c6e177f43c077) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_15\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a3fe7bc3216a458ec3e5c6e177f43c077) = 0x0C,

[ 407](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a779c5dd14e5f88e8e6bb247dc66d9c92) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_16\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a779c5dd14e5f88e8e6bb247dc66d9c92) = 0x0D,

[ 409](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a7d0794fe6796f19ff7e58819728751ff) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_17\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a7d0794fe6796f19ff7e58819728751ff) = 0x0E,

[ 411](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a22167e0c033c176f592a447b14c30071) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_18\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a22167e0c033c176f592a447b14c30071) = 0x0F

412};

413

[ 415](group__bt__audio.md#ga16d403ec4db7be997682331ad365ff5f)enum [bt\_audio\_active\_state](group__bt__audio.md#ga16d403ec4db7be997682331ad365ff5f) {

[ 417](group__bt__audio.md#gga16d403ec4db7be997682331ad365ff5fade27604ea8fd592aa5d0958e2ccde4f3) [BT\_AUDIO\_ACTIVE\_STATE\_DISABLED](group__bt__audio.md#gga16d403ec4db7be997682331ad365ff5fade27604ea8fd592aa5d0958e2ccde4f3) = 0x00,

[ 419](group__bt__audio.md#gga16d403ec4db7be997682331ad365ff5fa6d062944e9c49001666769601ba1c940) [BT\_AUDIO\_ACTIVE\_STATE\_ENABLED](group__bt__audio.md#gga16d403ec4db7be997682331ad365ff5fa6d062944e9c49001666769601ba1c940) = 0x01,

420};

421

[ 427](group__bt__audio.md#gab53d0dd62bceff97cf8eed7d8cf80354)enum [bt\_audio\_metadata\_type](group__bt__audio.md#gab53d0dd62bceff97cf8eed7d8cf80354) {

[ 438](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354aac28d2a0dc883affa60b7a70f678ed9a) [BT\_AUDIO\_METADATA\_TYPE\_PREF\_CONTEXT](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354aac28d2a0dc883affa60b7a70f678ed9a) = 0x01,

439

[ 450](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a95f128b11584ee22100ae65ce751dbaa) [BT\_AUDIO\_METADATA\_TYPE\_STREAM\_CONTEXT](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a95f128b11584ee22100ae65ce751dbaa) = 0x02,

451

[ 453](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a02f91ea7fb6be631687d843ad7bf4ac7) [BT\_AUDIO\_METADATA\_TYPE\_PROGRAM\_INFO](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a02f91ea7fb6be631687d843ad7bf4ac7) = 0x03,

454

[ 461](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354af38d342d907c3903121a03bb8394efb1) [BT\_AUDIO\_METADATA\_TYPE\_LANG](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354af38d342d907c3903121a03bb8394efb1) = 0x04,

462

[ 464](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a37b5552e04734392dc6c6eb9e19b377b) [BT\_AUDIO\_METADATA\_TYPE\_CCID\_LIST](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a37b5552e04734392dc6c6eb9e19b377b) = 0x05,

465

[ 471](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a7a83f397dc5dbe6e6d60a994cccdc613) [BT\_AUDIO\_METADATA\_TYPE\_PARENTAL\_RATING](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a7a83f397dc5dbe6e6d60a994cccdc613) = 0x06,

472

[ 474](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a58971ea21b5045e56a0e1ca838358922) [BT\_AUDIO\_METADATA\_TYPE\_PROGRAM\_INFO\_URI](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a58971ea21b5045e56a0e1ca838358922) = 0x07,

475

[ 481](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354af220c40d351ec5e236cd41a5944da5fc) [BT\_AUDIO\_METADATA\_TYPE\_AUDIO\_STATE](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354af220c40d351ec5e236cd41a5944da5fc) = 0x08,

482

[ 484](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a4b9cc5b82a1dbfc3db69bb12747443f1) [BT\_AUDIO\_METADATA\_TYPE\_BROADCAST\_IMMEDIATE](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a4b9cc5b82a1dbfc3db69bb12747443f1) = 0x09,

485

[ 487](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a0b5a8cd34bad81ac53c657c3cd9ddb39) [BT\_AUDIO\_METADATA\_TYPE\_EXTENDED](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a0b5a8cd34bad81ac53c657c3cd9ddb39) = 0xFE,

488

[ 490](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a30fbc4a159e64174b22f195f29012286) [BT\_AUDIO\_METADATA\_TYPE\_VENDOR](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a30fbc4a159e64174b22f195f29012286) = 0xFF,

491};

492

[ 498](group__bt__audio.md#ga86a7e9ca661a3b13b7c59d41d206156e)#define BT\_AUDIO\_METADATA\_TYPE\_IS\_KNOWN(\_type) \

499 (IN\_RANGE((\_type), BT\_AUDIO\_METADATA\_TYPE\_PREF\_CONTEXT, \

500 BT\_AUDIO\_METADATA\_TYPE\_BROADCAST\_IMMEDIATE) || \

501 (\_type) == BT\_AUDIO\_METADATA\_TYPE\_EXTENDED || (\_type) == BT\_AUDIO\_METADATA\_TYPE\_VENDOR)

502

[ 508](group__bt__audio.md#ga41db714fa87e85896a52427399633bb4)#define BT\_AUDIO\_UNICAST\_ANNOUNCEMENT\_GENERAL 0x00

[ 510](group__bt__audio.md#ga56c14acb7f182a413fdecac4e271c5cc)#define BT\_AUDIO\_UNICAST\_ANNOUNCEMENT\_TARGETED 0x01

512

[ 521](group__bt__audio.md#gaddc49e39465798ae4c0cbe345e0b50d7)#define BT\_AUDIO\_CODEC\_DATA(\_type, \_bytes...) \

522 (sizeof((uint8\_t)\_type) + sizeof((uint8\_t[]){\_bytes})), (\_type), \_bytes

523

[ 533](group__bt__audio.md#gaefed7a013e282c63c9b5cbbdcdc67448)#define BT\_AUDIO\_CODEC\_CFG(\_id, \_cid, \_vid, \_data, \_meta) \

534 ((struct bt\_audio\_codec\_cfg){ \

535 /\* Use HCI data path as default, can be overwritten by application \*/ \

536 .path\_id = BT\_ISO\_DATA\_PATH\_HCI, \

537 .ctlr\_transcode = false, \

538 .id = \_id, \

539 .cid = \_cid, \

540 .vid = \_vid, \

541 .data\_len = sizeof((uint8\_t[])\_data), \

542 .data = \_data, \

543 .meta\_len = sizeof((uint8\_t[])\_meta), \

544 .meta = \_meta, \

545 })

546

[ 556](group__bt__audio.md#ga6b99f589f6cdcd9e48a83f729a7a4698)#define BT\_AUDIO\_CODEC\_CAP(\_id, \_cid, \_vid, \_data, \_meta) \

557 ((struct bt\_audio\_codec\_cap){ \

558 /\* Use HCI data path as default, can be overwritten by application \*/ \

559 .path\_id = BT\_ISO\_DATA\_PATH\_HCI, \

560 .ctlr\_transcode = false, \

561 .id = (\_id), \

562 .cid = (\_cid), \

563 .vid = (\_vid), \

564 .data\_len = sizeof((uint8\_t[])\_data), \

565 .data = \_data, \

566 .meta\_len = sizeof((uint8\_t[])\_meta), \

567 .meta = \_meta, \

568 })

569

[ 575](group__bt__audio.md#ga61230848c02098352320fe751332c4e8)enum [bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8) {

[ 577](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a8f476de613cdcb2f9f677d40291aa5df) [BT\_AUDIO\_LOCATION\_MONO\_AUDIO](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a8f476de613cdcb2f9f677d40291aa5df) = 0,

[ 579](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ac658188fa6f1b4f248a149d0bde1e41b) [BT\_AUDIO\_LOCATION\_FRONT\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ac658188fa6f1b4f248a149d0bde1e41b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 581](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a26d5ba460642bcf7fb2fc950082b70b3) [BT\_AUDIO\_LOCATION\_FRONT\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a26d5ba460642bcf7fb2fc950082b70b3) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 583](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a06b34e67c9931f8b26562218cba51337) [BT\_AUDIO\_LOCATION\_FRONT\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a06b34e67c9931f8b26562218cba51337) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 585](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ac4c09f948266f2c9c65b3bc16da2f3f6) [BT\_AUDIO\_LOCATION\_LOW\_FREQ\_EFFECTS\_1](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ac4c09f948266f2c9c65b3bc16da2f3f6) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

[ 587](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a96906ff7918b0a3e3e7efe73a08d9896) [BT\_AUDIO\_LOCATION\_BACK\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a96906ff7918b0a3e3e7efe73a08d9896) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

[ 589](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a43f5070c2b4d39c38fa7900595d9b1aa) [BT\_AUDIO\_LOCATION\_BACK\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a43f5070c2b4d39c38fa7900595d9b1aa) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

[ 591](group__bt__audio.md#gga61230848c02098352320fe751332c4e8af02a9d46877b742e8730bbf3dd6ad22e) [BT\_AUDIO\_LOCATION\_FRONT\_LEFT\_OF\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8af02a9d46877b742e8730bbf3dd6ad22e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6),

[ 593](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a725707ae4703a1f9b970de5b1e4e5692) [BT\_AUDIO\_LOCATION\_FRONT\_RIGHT\_OF\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a725707ae4703a1f9b970de5b1e4e5692) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7),

[ 595](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ae22cd1e458d8ff503741bf48262c7983) [BT\_AUDIO\_LOCATION\_BACK\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ae22cd1e458d8ff503741bf48262c7983) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8),

[ 597](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a0c304bdd529ad66acb71001caa1b361b) [BT\_AUDIO\_LOCATION\_LOW\_FREQ\_EFFECTS\_2](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a0c304bdd529ad66acb71001caa1b361b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9),

[ 599](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ab8e52c69b894e382f0f09cc370337064) [BT\_AUDIO\_LOCATION\_SIDE\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ab8e52c69b894e382f0f09cc370337064) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10),

[ 601](group__bt__audio.md#gga61230848c02098352320fe751332c4e8aa01ad94f71defd158d8cfe25936341cd) [BT\_AUDIO\_LOCATION\_SIDE\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8aa01ad94f71defd158d8cfe25936341cd) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11),

[ 603](group__bt__audio.md#gga61230848c02098352320fe751332c4e8aa093e6218e213eac5677766e01f5c1c9) [BT\_AUDIO\_LOCATION\_TOP\_FRONT\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8aa093e6218e213eac5677766e01f5c1c9) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12),

[ 605](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a60b154a216d8e029deac7305500eaf2d) [BT\_AUDIO\_LOCATION\_TOP\_FRONT\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a60b154a216d8e029deac7305500eaf2d) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13),

[ 607](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ac32ed6f456be2fb2d9af2c7b255f3a4e) [BT\_AUDIO\_LOCATION\_TOP\_FRONT\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ac32ed6f456be2fb2d9af2c7b255f3a4e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14),

[ 609](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a555361fafade3bfb27dc713666757a1f) [BT\_AUDIO\_LOCATION\_TOP\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a555361fafade3bfb27dc713666757a1f) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15),

[ 611](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a07e699c28bd847de3d85645dceb2ff06) [BT\_AUDIO\_LOCATION\_TOP\_BACK\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a07e699c28bd847de3d85645dceb2ff06) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(16),

[ 613](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a8e81b80f732b0037493712b4baa21a69) [BT\_AUDIO\_LOCATION\_TOP\_BACK\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a8e81b80f732b0037493712b4baa21a69) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(17),

[ 615](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ae846b2f4186b46d3690c71071c41c7d6) [BT\_AUDIO\_LOCATION\_TOP\_SIDE\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ae846b2f4186b46d3690c71071c41c7d6) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(18),

[ 617](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a1cf8dea66e42f75ca85ba55124829a59) [BT\_AUDIO\_LOCATION\_TOP\_SIDE\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a1cf8dea66e42f75ca85ba55124829a59) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(19),

[ 619](group__bt__audio.md#gga61230848c02098352320fe751332c4e8aebae1f0f2537a806672820fb74eba5dd) [BT\_AUDIO\_LOCATION\_TOP\_BACK\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8aebae1f0f2537a806672820fb74eba5dd) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(20),

[ 621](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ad0be8f720f03feb18a23e77f0eff6376) [BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ad0be8f720f03feb18a23e77f0eff6376) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(21),

[ 623](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ac1e355baee6ca0907356d72f0d4edb29) [BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ac1e355baee6ca0907356d72f0d4edb29) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(22),

[ 625](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a33d0f7c266f21fd086386f8c29ee31e8) [BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a33d0f7c266f21fd086386f8c29ee31e8) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(23),

[ 627](group__bt__audio.md#gga61230848c02098352320fe751332c4e8acba90183626ad85c21692b7edd87133d) [BT\_AUDIO\_LOCATION\_FRONT\_LEFT\_WIDE](group__bt__audio.md#gga61230848c02098352320fe751332c4e8acba90183626ad85c21692b7edd87133d) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(24),

[ 629](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a8649be1d5b7e8b312fc3374039cc0a71) [BT\_AUDIO\_LOCATION\_FRONT\_RIGHT\_WIDE](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a8649be1d5b7e8b312fc3374039cc0a71) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(25),

[ 631](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a568a581c0ad653177f5d148d04bef0b6) [BT\_AUDIO\_LOCATION\_LEFT\_SURROUND](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a568a581c0ad653177f5d148d04bef0b6) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(26),

[ 633](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a97954db823b6c6bed660ff2717600a5e) [BT\_AUDIO\_LOCATION\_RIGHT\_SURROUND](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a97954db823b6c6bed660ff2717600a5e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(27),

634};

635

[ 639](group__bt__audio.md#ga90688f158fe999ed3aa9c759c8245fcc)#define BT\_AUDIO\_LOCATION\_ANY (BT\_AUDIO\_LOCATION\_FRONT\_LEFT | \

640 BT\_AUDIO\_LOCATION\_FRONT\_RIGHT | \

641 BT\_AUDIO\_LOCATION\_FRONT\_CENTER | \

642 BT\_AUDIO\_LOCATION\_LOW\_FREQ\_EFFECTS\_1 | \

643 BT\_AUDIO\_LOCATION\_BACK\_LEFT | \

644 BT\_AUDIO\_LOCATION\_BACK\_RIGHT | \

645 BT\_AUDIO\_LOCATION\_FRONT\_LEFT\_OF\_CENTER | \

646 BT\_AUDIO\_LOCATION\_FRONT\_RIGHT\_OF\_CENTER | \

647 BT\_AUDIO\_LOCATION\_BACK\_CENTER | \

648 BT\_AUDIO\_LOCATION\_LOW\_FREQ\_EFFECTS\_2 | \

649 BT\_AUDIO\_LOCATION\_SIDE\_LEFT | \

650 BT\_AUDIO\_LOCATION\_SIDE\_RIGHT | \

651 BT\_AUDIO\_LOCATION\_TOP\_FRONT\_LEFT | \

652 BT\_AUDIO\_LOCATION\_TOP\_FRONT\_RIGHT | \

653 BT\_AUDIO\_LOCATION\_TOP\_FRONT\_CENTER | \

654 BT\_AUDIO\_LOCATION\_TOP\_CENTER | \

655 BT\_AUDIO\_LOCATION\_TOP\_BACK\_LEFT | \

656 BT\_AUDIO\_LOCATION\_TOP\_BACK\_RIGHT | \

657 BT\_AUDIO\_LOCATION\_TOP\_SIDE\_LEFT | \

658 BT\_AUDIO\_LOCATION\_TOP\_SIDE\_RIGHT | \

659 BT\_AUDIO\_LOCATION\_TOP\_BACK\_CENTER | \

660 BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_CENTER | \

661 BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_LEFT | \

662 BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_RIGHT | \

663 BT\_AUDIO\_LOCATION\_FRONT\_LEFT\_WIDE | \

664 BT\_AUDIO\_LOCATION\_FRONT\_RIGHT\_WIDE | \

665 BT\_AUDIO\_LOCATION\_LEFT\_SURROUND | \

666 BT\_AUDIO\_LOCATION\_RIGHT\_SURROUND)

667

[ 669](structbt__audio__codec__cap.md)struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) {

[ 675](structbt__audio__codec__cap.md#a822a06f815091cc580ca2e5bbb3126f7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [path\_id](structbt__audio__codec__cap.md#a822a06f815091cc580ca2e5bbb3126f7);

[ 681](structbt__audio__codec__cap.md#a900a77db09e72de61d4ff652c6dbb10b) bool [ctlr\_transcode](structbt__audio__codec__cap.md#a900a77db09e72de61d4ff652c6dbb10b);

[ 683](structbt__audio__codec__cap.md#ae3892731e7ca05f3ec426c70f0d9e1a9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [id](structbt__audio__codec__cap.md#ae3892731e7ca05f3ec426c70f0d9e1a9);

[ 685](structbt__audio__codec__cap.md#a763222d12a87958a5ba806303f98829a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [cid](structbt__audio__codec__cap.md#a763222d12a87958a5ba806303f98829a);

[ 687](structbt__audio__codec__cap.md#a3b91269e16a3d63b3128a527caa5e3ff) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [vid](structbt__audio__codec__cap.md#a3b91269e16a3d63b3128a527caa5e3ff);

688#if CONFIG\_BT\_AUDIO\_CODEC\_CAP\_MAX\_DATA\_SIZE > 0 || defined(\_\_DOXYGEN\_\_)

[ 690](structbt__audio__codec__cap.md#acf3e22c6db1533fff7015acbc7eca196) size\_t [data\_len](structbt__audio__codec__cap.md#acf3e22c6db1533fff7015acbc7eca196);

[ 692](structbt__audio__codec__cap.md#a455638aac9167d288a1e7a9fccabc49d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structbt__audio__codec__cap.md#a455638aac9167d288a1e7a9fccabc49d)[CONFIG\_BT\_AUDIO\_CODEC\_CAP\_MAX\_DATA\_SIZE];

693#endif /\* CONFIG\_BT\_AUDIO\_CODEC\_CAP\_MAX\_DATA\_SIZE > 0 \*/

694#if defined(CONFIG\_BT\_AUDIO\_CODEC\_CAP\_MAX\_METADATA\_SIZE) || defined(\_\_DOXYGEN\_\_)

[ 696](structbt__audio__codec__cap.md#afe806521d5aac36e9f6c6a0598500a8f) size\_t [meta\_len](structbt__audio__codec__cap.md#afe806521d5aac36e9f6c6a0598500a8f);

[ 698](structbt__audio__codec__cap.md#acec4f5e31752d81d4dbf441223e7f44c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [meta](structbt__audio__codec__cap.md#acec4f5e31752d81d4dbf441223e7f44c)[CONFIG\_BT\_AUDIO\_CODEC\_CAP\_MAX\_METADATA\_SIZE];

699#endif /\* CONFIG\_BT\_AUDIO\_CODEC\_CAP\_MAX\_METADATA\_SIZE \*/

700};

701

[ 703](structbt__audio__codec__cfg.md)struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) {

[ 709](structbt__audio__codec__cfg.md#a9386056bb02908407c9e3aad48abbd87) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [path\_id](structbt__audio__codec__cfg.md#a9386056bb02908407c9e3aad48abbd87);

[ 715](structbt__audio__codec__cfg.md#a9e2c8081950a0830ffc270245ab308c1) bool [ctlr\_transcode](structbt__audio__codec__cfg.md#a9e2c8081950a0830ffc270245ab308c1);

[ 717](structbt__audio__codec__cfg.md#aa2f99ec31ff3eb9b7b738bc8a1170f20) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [id](structbt__audio__codec__cfg.md#aa2f99ec31ff3eb9b7b738bc8a1170f20);

[ 719](structbt__audio__codec__cfg.md#a664e21bcd6002b21d4b1b53d866db32d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [cid](structbt__audio__codec__cfg.md#a664e21bcd6002b21d4b1b53d866db32d);

[ 721](structbt__audio__codec__cfg.md#a2996ab3f6ae1cab09ff5e3329b42468e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [vid](structbt__audio__codec__cfg.md#a2996ab3f6ae1cab09ff5e3329b42468e);

722#if CONFIG\_BT\_AUDIO\_CODEC\_CFG\_MAX\_DATA\_SIZE > 0 || defined(\_\_DOXYGEN\_\_)

[ 724](structbt__audio__codec__cfg.md#a8a5a789e9993a48ce4c83a2156c1f43c) size\_t [data\_len](structbt__audio__codec__cfg.md#a8a5a789e9993a48ce4c83a2156c1f43c);

[ 726](structbt__audio__codec__cfg.md#ad3709d5321f6faeb392452cb3b21023b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [data](structbt__audio__codec__cfg.md#ad3709d5321f6faeb392452cb3b21023b)[CONFIG\_BT\_AUDIO\_CODEC\_CFG\_MAX\_DATA\_SIZE];

727#endif /\* CONFIG\_BT\_AUDIO\_CODEC\_CFG\_MAX\_DATA\_SIZE > 0 \*/

728#if CONFIG\_BT\_AUDIO\_CODEC\_CFG\_MAX\_METADATA\_SIZE > 0 || defined(\_\_DOXYGEN\_\_)

[ 730](structbt__audio__codec__cfg.md#a1e69a5c017e9571b50aba721f86876fb) size\_t [meta\_len](structbt__audio__codec__cfg.md#a1e69a5c017e9571b50aba721f86876fb);

[ 732](structbt__audio__codec__cfg.md#a4f84974ea14b773ad8e2fd7c0ffa0c7f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [meta](structbt__audio__codec__cfg.md#a4f84974ea14b773ad8e2fd7c0ffa0c7f)[CONFIG\_BT\_AUDIO\_CODEC\_CFG\_MAX\_METADATA\_SIZE];

733#endif /\* CONFIG\_BT\_AUDIO\_CODEC\_CFG\_MAX\_METADATA\_SIZE > 0 \*/

734};

735

[ 750](group__bt__audio.md#gafd8574b16141162c95653f0aa2bf6ff7)int [bt\_audio\_data\_parse](group__bt__audio.md#gafd8574b16141162c95653f0aa2bf6ff7)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ltv[], size\_t size,

751 bool (\*func)(struct [bt\_data](structbt__data.md) \*data, void \*user\_data), void \*user\_data);

752

[ 760](group__bt__audio.md#ga87415f8dddd38b3f5641c96e9722a44a)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bt\_audio\_get\_chan\_count](group__bt__audio.md#ga87415f8dddd38b3f5641c96e9722a44a)(enum [bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8) chan\_allocation);

761

[ 763](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f)enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) {

[ 770](group__bt__audio.md#gga5bd899fb5e4d844058184913866e462fa2adba49daa32ac7b040c3294f047ceb8) [BT\_AUDIO\_DIR\_SINK](group__bt__audio.md#gga5bd899fb5e4d844058184913866e462fa2adba49daa32ac7b040c3294f047ceb8) = 0x01,

[ 777](group__bt__audio.md#gga5bd899fb5e4d844058184913866e462fa868695a31ebf95402a4bae2469f3aa6c) [BT\_AUDIO\_DIR\_SOURCE](group__bt__audio.md#gga5bd899fb5e4d844058184913866e462fa868695a31ebf95402a4bae2469f3aa6c) = 0x02,

778};

779

[ 791](group__bt__audio.md#ga13e5148d62cb364602f01c75a88b615b)#define BT\_AUDIO\_CODEC\_QOS(\_interval, \_framing, \_phy, \_sdu, \_rtn, \_latency, \_pd) \

792 ((struct bt\_audio\_codec\_qos){ \

793 .interval = \_interval, \

794 .framing = \_framing, \

795 .phy = \_phy, \

796 .sdu = \_sdu, \

797 .rtn = \_rtn, \

798 IF\_ENABLED(UTIL\_OR(IS\_ENABLED(CONFIG\_BT\_BAP\_BROADCAST\_SOURCE), \

799 IS\_ENABLED(CONFIG\_BT\_BAP\_UNICAST)), \

800 (.latency = \_latency,)) \

801 .pd = \_pd, \

802 })

803

[ 805](group__bt__audio.md#ga8cb1832a3ee38b1a151b702c5dee00d9)enum [bt\_audio\_codec\_qos\_framing](group__bt__audio.md#ga8cb1832a3ee38b1a151b702c5dee00d9) {

[ 807](group__bt__audio.md#gga8cb1832a3ee38b1a151b702c5dee00d9a426ad2fe26f69d135beff6a367ef872f) [BT\_AUDIO\_CODEC\_QOS\_FRAMING\_UNFRAMED](group__bt__audio.md#gga8cb1832a3ee38b1a151b702c5dee00d9a426ad2fe26f69d135beff6a367ef872f) = 0x00,

[ 809](group__bt__audio.md#gga8cb1832a3ee38b1a151b702c5dee00d9af7a4a07da9089c3afb248d63e3a9297a) [BT\_AUDIO\_CODEC\_QOS\_FRAMING\_FRAMED](group__bt__audio.md#gga8cb1832a3ee38b1a151b702c5dee00d9af7a4a07da9089c3afb248d63e3a9297a) = 0x01,

810};

811

813enum {

[ 815](group__bt__audio.md#ggaa69a4789478a1a0aa93451d294de7ad0ab387760c001ea6c81e889de55e74d5d5) [BT\_AUDIO\_CODEC\_QOS\_1M](group__bt__audio.md#ggaa69a4789478a1a0aa93451d294de7ad0ab387760c001ea6c81e889de55e74d5d5) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 817](group__bt__audio.md#ggaa69a4789478a1a0aa93451d294de7ad0ac81306188ed29b8fa17aa2afa878f297) [BT\_AUDIO\_CODEC\_QOS\_2M](group__bt__audio.md#ggaa69a4789478a1a0aa93451d294de7ad0ac81306188ed29b8fa17aa2afa878f297) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 819](group__bt__audio.md#ggaa69a4789478a1a0aa93451d294de7ad0a9789c1b6b319370a3b98ab37b61a86e0) [BT\_AUDIO\_CODEC\_QOS\_CODED](group__bt__audio.md#ggaa69a4789478a1a0aa93451d294de7ad0a9789c1b6b319370a3b98ab37b61a86e0) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

820};

821

[ 831](group__bt__audio.md#gadfc744b32a0b40da9377bb3668004bc2)#define BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(\_interval, \_sdu, \_rtn, \_latency, \_pd) \

832 BT\_AUDIO\_CODEC\_QOS(\_interval, BT\_AUDIO\_CODEC\_QOS\_FRAMING\_UNFRAMED, BT\_AUDIO\_CODEC\_QOS\_2M, \

833 \_sdu, \_rtn, \_latency, \_pd)

834

[ 844](group__bt__audio.md#gae2147bca922bf3effd072d67a6b5d635)#define BT\_AUDIO\_CODEC\_QOS\_FRAMED(\_interval, \_sdu, \_rtn, \_latency, \_pd) \

845 BT\_AUDIO\_CODEC\_QOS(\_interval, BT\_AUDIO\_CODEC\_QOS\_FRAMING\_FRAMED, BT\_AUDIO\_CODEC\_QOS\_2M, \

846 \_sdu, \_rtn, \_latency, \_pd)

847

[ 849](structbt__audio__codec__qos.md)struct [bt\_audio\_codec\_qos](structbt__audio__codec__qos.md) {

[ 860](structbt__audio__codec__qos.md#a28d87b06785e016fe7e12a0504f3b419) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pd](structbt__audio__codec__qos.md#a28d87b06785e016fe7e12a0504f3b419);

861

869 struct {

[ 871](structbt__audio__codec__qos.md#a4212bf93b65e0faa218a1e0d03ae0283) enum [bt\_audio\_codec\_qos\_framing](group__bt__audio.md#ga8cb1832a3ee38b1a151b702c5dee00d9) [framing](structbt__audio__codec__qos.md#a4212bf93b65e0faa218a1e0d03ae0283);

872

[ 879](structbt__audio__codec__qos.md#a8911b0b9db8e4de55b3c313e3ad7c502) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__audio__codec__qos.md#a8911b0b9db8e4de55b3c313e3ad7c502);

880

[ 887](structbt__audio__codec__qos.md#ab05af8d47df82d34921afdd557770dbd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rtn](structbt__audio__codec__qos.md#ab05af8d47df82d34921afdd557770dbd);

888

[ 894](structbt__audio__codec__qos.md#ae1a5adb80af9357fd6ee6532b0ba228e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sdu](structbt__audio__codec__qos.md#ae1a5adb80af9357fd6ee6532b0ba228e);

895

896#if defined(CONFIG\_BT\_BAP\_BROADCAST\_SOURCE) || defined(CONFIG\_BT\_BAP\_UNICAST) || \

897 defined(\_\_DOXYGEN\_\_)

[ 903](structbt__audio__codec__qos.md#acb0fb67ff7c24d6d00c318cccb6b6eb3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [latency](structbt__audio__codec__qos.md#acb0fb67ff7c24d6d00c318cccb6b6eb3);

904#endif /\* CONFIG\_BT\_BAP\_BROADCAST\_SOURCE || CONFIG\_BT\_BAP\_UNICAST \*/

905

[ 911](structbt__audio__codec__qos.md#ad906dc06624b0f80701d7ee92d849152) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [interval](structbt__audio__codec__qos.md#ad906dc06624b0f80701d7ee92d849152);

912

913#if defined(CONFIG\_BT\_ISO\_TEST\_PARAMS) || defined(\_\_DOXYGEN\_\_)

[ 925](structbt__audio__codec__qos.md#a98a5b8ba8ab2b2a289714916f38a1e27) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max\_pdu](structbt__audio__codec__qos.md#a98a5b8ba8ab2b2a289714916f38a1e27);

926

[ 932](structbt__audio__codec__qos.md#a42c025d09fb7f6ce8af136e01837e002) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [burst\_number](structbt__audio__codec__qos.md#a42c025d09fb7f6ce8af136e01837e002);

933

[ 941](structbt__audio__codec__qos.md#a7b66a27686feda162ea70fdc9ae17425) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_subevents](structbt__audio__codec__qos.md#a7b66a27686feda162ea70fdc9ae17425);

942#endif /\* CONFIG\_BT\_ISO\_TEST\_PARAMS \*/

943 };

944};

945

[ 958](group__bt__audio.md#gac48a47e5177754c2e6812eee440e6d42)#define BT\_AUDIO\_CODEC\_QOS\_PREF(\_unframed\_supported, \_phy, \_rtn, \_latency, \_pd\_min, \_pd\_max, \

959 \_pref\_pd\_min, \_pref\_pd\_max) \

960 { \

961 .unframed\_supported = \_unframed\_supported, \

962 .phy = \_phy, \

963 .rtn = \_rtn, \

964 .latency = \_latency, \

965 .pd\_min = \_pd\_min, \

966 .pd\_max = \_pd\_max, \

967 .pref\_pd\_min = \_pref\_pd\_min, \

968 .pref\_pd\_max = \_pref\_pd\_max, \

969 }

970

[ 972](structbt__audio__codec__qos__pref.md)struct [bt\_audio\_codec\_qos\_pref](structbt__audio__codec__qos__pref.md) {

[ 979](structbt__audio__codec__qos__pref.md#a3bdb319d2aa401102fb9e54f92993e83) bool [unframed\_supported](structbt__audio__codec__qos__pref.md#a3bdb319d2aa401102fb9e54f92993e83);

980

[ 982](structbt__audio__codec__qos__pref.md#a36fc375290b8f76c7278a236942db692) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__audio__codec__qos__pref.md#a36fc375290b8f76c7278a236942db692);

983

[ 985](structbt__audio__codec__qos__pref.md#abc2142ef5c8ad1744b829ae626a57e9d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rtn](structbt__audio__codec__qos__pref.md#abc2142ef5c8ad1744b829ae626a57e9d);

986

[ 988](structbt__audio__codec__qos__pref.md#a1d46cf0aa05cfb7c88446719e59e0011) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [latency](structbt__audio__codec__qos__pref.md#a1d46cf0aa05cfb7c88446719e59e0011);

989

[ 998](structbt__audio__codec__qos__pref.md#a7437273abb18ce93c15bb789eeeb65d3) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pd\_min](structbt__audio__codec__qos__pref.md#a7437273abb18ce93c15bb789eeeb65d3);

999

[ 1008](structbt__audio__codec__qos__pref.md#ab07f2245bfed3a1400b6a1e6eaad2735) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pd\_max](structbt__audio__codec__qos__pref.md#ab07f2245bfed3a1400b6a1e6eaad2735);

1009

[ 1015](structbt__audio__codec__qos__pref.md#ab38a4b98b47ab773f91873b42c69ed71) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pref\_pd\_min](structbt__audio__codec__qos__pref.md#ab38a4b98b47ab773f91873b42c69ed71);

1016

[ 1022](structbt__audio__codec__qos__pref.md#a5486cacf6cd5016e9b44b69e3da67d6d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pref\_pd\_max](structbt__audio__codec__qos__pref.md#a5486cacf6cd5016e9b44b69e3da67d6d);

1023};

1024

1033

[ 1042](group__bt__audio__codec__cfg.md#ga2e557fe726a49dc99754da16f7cc60af)int [bt\_audio\_codec\_cfg\_freq\_to\_freq\_hz](group__bt__audio__codec__cfg.md#ga2e557fe726a49dc99754da16f7cc60af)(enum [bt\_audio\_codec\_cfg\_freq](group__bt__audio.md#ga8e99fb678cc011bb8c9f6e1858bae0d7) freq);

1043

[ 1052](group__bt__audio__codec__cfg.md#ga99ab4f6d2a18f2a9b4e3da47f63fc9e0)int [bt\_audio\_codec\_cfg\_freq\_hz\_to\_freq](group__bt__audio__codec__cfg.md#ga99ab4f6d2a18f2a9b4e3da47f63fc9e0)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) freq\_hz);

1053

[ 1064](group__bt__audio__codec__cfg.md#gad8525a57d35e3e34ea591f7e20e2512d)int [bt\_audio\_codec\_cfg\_get\_freq](group__bt__audio__codec__cfg.md#gad8525a57d35e3e34ea591f7e20e2512d)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg);

1065

[ 1076](group__bt__audio__codec__cfg.md#gac119989d5dcfa36becf4edd0ae7c6138)int [bt\_audio\_codec\_cfg\_set\_freq](group__bt__audio__codec__cfg.md#gac119989d5dcfa36becf4edd0ae7c6138)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1077 enum [bt\_audio\_codec\_cfg\_freq](group__bt__audio.md#ga8e99fb678cc011bb8c9f6e1858bae0d7) freq);

1078

[ 1087](group__bt__audio__codec__cfg.md#ga225e05df1f0d1efb709c972187901495)int [bt\_audio\_codec\_cfg\_frame\_dur\_to\_frame\_dur\_us](group__bt__audio__codec__cfg.md#ga225e05df1f0d1efb709c972187901495)(enum [bt\_audio\_codec\_cfg\_frame\_dur](group__bt__audio.md#ga83701b5eadfcbc9b84dc0b1a85ebeb74) frame\_dur);

1088

[ 1097](group__bt__audio__codec__cfg.md#ga0782a3d9254fb76b441c6c2492571556)int [bt\_audio\_codec\_cfg\_frame\_dur\_us\_to\_frame\_dur](group__bt__audio__codec__cfg.md#ga0782a3d9254fb76b441c6c2492571556)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) frame\_dur\_us);

1098

[ 1109](group__bt__audio__codec__cfg.md#ga2dd3afe41b22e989fb46614f89550007)int [bt\_audio\_codec\_cfg\_get\_frame\_dur](group__bt__audio__codec__cfg.md#ga2dd3afe41b22e989fb46614f89550007)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg);

1110

[ 1121](group__bt__audio__codec__cfg.md#ga7d8306f98cb00f06e68a1df417825f0d)int [bt\_audio\_codec\_cfg\_set\_frame\_dur](group__bt__audio__codec__cfg.md#ga7d8306f98cb00f06e68a1df417825f0d)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1122 enum [bt\_audio\_codec\_cfg\_frame\_dur](group__bt__audio.md#ga83701b5eadfcbc9b84dc0b1a85ebeb74) frame\_dur);

1123

[ 1144](group__bt__audio__codec__cfg.md#gae712e0f8e84aeb4ad2528da34907e29d)int [bt\_audio\_codec\_cfg\_get\_chan\_allocation](group__bt__audio__codec__cfg.md#gae712e0f8e84aeb4ad2528da34907e29d)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1145 enum [bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8) \*chan\_allocation,

1146 bool fallback\_to\_default);

1147

[ 1158](group__bt__audio__codec__cfg.md#gafbbcd69fac18ed0201a5e0156209b049)int [bt\_audio\_codec\_cfg\_set\_chan\_allocation](group__bt__audio__codec__cfg.md#gafbbcd69fac18ed0201a5e0156209b049)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1159 enum [bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8) chan\_allocation);

1160

[ 1180](group__bt__audio__codec__cfg.md#ga503be053422217502d6108b045791e02)int [bt\_audio\_codec\_cfg\_get\_octets\_per\_frame](group__bt__audio__codec__cfg.md#ga503be053422217502d6108b045791e02)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg);

1181

[ 1192](group__bt__audio__codec__cfg.md#ga866cdec28194056dc9e274d0436b45c2)int [bt\_audio\_codec\_cfg\_set\_octets\_per\_frame](group__bt__audio__codec__cfg.md#ga866cdec28194056dc9e274d0436b45c2)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1193 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) octets\_per\_frame);

1194

[ 1215](group__bt__audio__codec__cfg.md#gadba0723f9d8a9546b659fba139051374)int [bt\_audio\_codec\_cfg\_get\_frame\_blocks\_per\_sdu](group__bt__audio__codec__cfg.md#gadba0723f9d8a9546b659fba139051374)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1216 bool fallback\_to\_default);

1217

[ 1228](group__bt__audio__codec__cfg.md#gac9cf20bafbe24b34034bfb6ee7aaf03e)int [bt\_audio\_codec\_cfg\_set\_frame\_blocks\_per\_sdu](group__bt__audio__codec__cfg.md#gac9cf20bafbe24b34034bfb6ee7aaf03e)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1229 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) frame\_blocks);

1230

[ 1242](group__bt__audio__codec__cfg.md#ga707c679db0193197b56acabfb08f8d1f)int [bt\_audio\_codec\_cfg\_get\_val](group__bt__audio__codec__cfg.md#ga707c679db0193197b56acabfb08f8d1f)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1243 enum [bt\_audio\_codec\_cfg\_type](group__bt__audio.md#ga9230ec4d7518bd243207ba2decb1a974) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*data);

1244

[ 1257](group__bt__audio__codec__cfg.md#gab10f22938780530b1d1b95695382902e)int [bt\_audio\_codec\_cfg\_set\_val](group__bt__audio__codec__cfg.md#gab10f22938780530b1d1b95695382902e)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1258 enum [bt\_audio\_codec\_cfg\_type](group__bt__audio.md#ga9230ec4d7518bd243207ba2decb1a974) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data,

1259 size\_t data\_len);

1260

[ 1272](group__bt__audio__codec__cfg.md#gad3857d0ca008854df5966501caa261ba)int [bt\_audio\_codec\_cfg\_unset\_val](group__bt__audio__codec__cfg.md#gad3857d0ca008854df5966501caa261ba)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1273 enum [bt\_audio\_codec\_cfg\_type](group__bt__audio.md#ga9230ec4d7518bd243207ba2decb1a974) type);

1274

[ 1287](group__bt__audio__codec__cfg.md#gae98335e87394a491b4a311d867a5e32d)int [bt\_audio\_codec\_cfg\_meta\_get\_val](group__bt__audio__codec__cfg.md#gae98335e87394a491b4a311d867a5e32d)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type,

1288 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*data);

1289

[ 1302](group__bt__audio__codec__cfg.md#ga3e24c2ba8de502600e647cb2f84e3ec4)int [bt\_audio\_codec\_cfg\_meta\_set\_val](group__bt__audio__codec__cfg.md#ga3e24c2ba8de502600e647cb2f84e3ec4)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1303 enum [bt\_audio\_metadata\_type](group__bt__audio.md#gab53d0dd62bceff97cf8eed7d8cf80354) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data,

1304 size\_t data\_len);

1305

[ 1317](group__bt__audio__codec__cfg.md#gab46f830daa1d9a907f47eb2a9eed7337)int [bt\_audio\_codec\_cfg\_meta\_unset\_val](group__bt__audio__codec__cfg.md#gab46f830daa1d9a907f47eb2a9eed7337)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1318 enum [bt\_audio\_metadata\_type](group__bt__audio.md#gab53d0dd62bceff97cf8eed7d8cf80354) type);

[ 1334](group__bt__audio__codec__cfg.md#gaea087663426a49bb6ff4859800aecb84)int [bt\_audio\_codec\_cfg\_meta\_get\_pref\_context](group__bt__audio__codec__cfg.md#gaea087663426a49bb6ff4859800aecb84)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1335 bool fallback\_to\_default);

1336

[ 1347](group__bt__audio__codec__cfg.md#gab40bad609f17d24e7e0e9ffcebe4e912)int [bt\_audio\_codec\_cfg\_meta\_set\_pref\_context](group__bt__audio__codec__cfg.md#gab40bad609f17d24e7e0e9ffcebe4e912)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1348 enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) ctx);

1349

[ 1362](group__bt__audio__codec__cfg.md#ga4cc4e1bb941206e7f1541a57fc92b8e9)int [bt\_audio\_codec\_cfg\_meta\_get\_stream\_context](group__bt__audio__codec__cfg.md#ga4cc4e1bb941206e7f1541a57fc92b8e9)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg);

1363

[ 1374](group__bt__audio__codec__cfg.md#ga5cd2af1bb44c6eb5bafe824f005a77f0)int [bt\_audio\_codec\_cfg\_meta\_set\_stream\_context](group__bt__audio__codec__cfg.md#ga5cd2af1bb44c6eb5bafe824f005a77f0)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1375 enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) ctx);

1376

[ 1389](group__bt__audio__codec__cfg.md#ga03284b8474d65443d7ecc8bdfc6f04c6)int [bt\_audio\_codec\_cfg\_meta\_get\_program\_info](group__bt__audio__codec__cfg.md#ga03284b8474d65443d7ecc8bdfc6f04c6)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1390 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*program\_info);

1391

[ 1403](group__bt__audio__codec__cfg.md#ga2ca9e616d20d7513c60ce905f046ac7b)int [bt\_audio\_codec\_cfg\_meta\_set\_program\_info](group__bt__audio__codec__cfg.md#ga2ca9e616d20d7513c60ce905f046ac7b)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1404 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*program\_info, size\_t program\_info\_len);

1405

[ 1419](group__bt__audio__codec__cfg.md#ga55e3cbaeacf15fcb1f24a16eb28db99c)int [bt\_audio\_codec\_cfg\_meta\_get\_lang](group__bt__audio__codec__cfg.md#ga55e3cbaeacf15fcb1f24a16eb28db99c)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1420 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*lang);

1421

[ 1432](group__bt__audio__codec__cfg.md#ga54b7eadf072c397879c1dababa2a3be0)int [bt\_audio\_codec\_cfg\_meta\_set\_lang](group__bt__audio__codec__cfg.md#ga54b7eadf072c397879c1dababa2a3be0)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1433 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) lang[[BT\_AUDIO\_LANG\_SIZE](group__bt__audio.md#gab6e5f793d514626deca21940d35d8f21)]);

1434

[ 1447](group__bt__audio__codec__cfg.md#gaa0f9b9f608c7af881d5a928a3ae397b2)int [bt\_audio\_codec\_cfg\_meta\_get\_ccid\_list](group__bt__audio__codec__cfg.md#gaa0f9b9f608c7af881d5a928a3ae397b2)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1448 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*ccid\_list);

1449

[ 1461](group__bt__audio__codec__cfg.md#ga59716b95fcea3404ff8c078564b0e29c)int [bt\_audio\_codec\_cfg\_meta\_set\_ccid\_list](group__bt__audio__codec__cfg.md#ga59716b95fcea3404ff8c078564b0e29c)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1462 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*ccid\_list, size\_t ccid\_list\_len);

1463

[ 1476](group__bt__audio__codec__cfg.md#gaf0eecb02a05f0cc2b75ae9fb32c03913)int [bt\_audio\_codec\_cfg\_meta\_get\_parental\_rating](group__bt__audio__codec__cfg.md#gaf0eecb02a05f0cc2b75ae9fb32c03913)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg);

1477

[ 1488](group__bt__audio__codec__cfg.md#gab5d8b5877de4fe16c0e06a1d4f0d15ce)int [bt\_audio\_codec\_cfg\_meta\_set\_parental\_rating](group__bt__audio__codec__cfg.md#gab5d8b5877de4fe16c0e06a1d4f0d15ce)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1489 enum [bt\_audio\_parental\_rating](group__bt__audio.md#ga6d4aff1f93dc0b902e4b5d1355f15760) parental\_rating);

1490

[ 1503](group__bt__audio__codec__cfg.md#ga6bdbc0a0b929fdbdc75db479aec858df)int [bt\_audio\_codec\_cfg\_meta\_get\_program\_info\_uri](group__bt__audio__codec__cfg.md#ga6bdbc0a0b929fdbdc75db479aec858df)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1504 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*program\_info\_uri);

1505

[ 1517](group__bt__audio__codec__cfg.md#ga99163729034e816eaef7195505d5ae20)int [bt\_audio\_codec\_cfg\_meta\_set\_program\_info\_uri](group__bt__audio__codec__cfg.md#ga99163729034e816eaef7195505d5ae20)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1518 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*program\_info\_uri,

1519 size\_t program\_info\_uri\_len);

1520

[ 1533](group__bt__audio__codec__cfg.md#ga0fd6e6baf1b4f22d60768aaed6f42e8e)int [bt\_audio\_codec\_cfg\_meta\_get\_audio\_active\_state](group__bt__audio__codec__cfg.md#ga0fd6e6baf1b4f22d60768aaed6f42e8e)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg);

1534

[ 1545](group__bt__audio__codec__cfg.md#gaf869e7ce0c9dd467fb03e8503d36c58a)int [bt\_audio\_codec\_cfg\_meta\_set\_audio\_active\_state](group__bt__audio__codec__cfg.md#gaf869e7ce0c9dd467fb03e8503d36c58a)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1546 enum [bt\_audio\_active\_state](group__bt__audio.md#ga16d403ec4db7be997682331ad365ff5f) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

1547

[ 1559](group__bt__audio__codec__cfg.md#ga66143aa7dcc726e06a12660b8f90fc5a)int [bt\_audio\_codec\_cfg\_meta\_get\_bcast\_audio\_immediate\_rend\_flag](group__bt__audio__codec__cfg.md#ga66143aa7dcc726e06a12660b8f90fc5a)(

1560 const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg);

1561

[ 1571](group__bt__audio__codec__cfg.md#gaede61b65d2037c7fbf6c4c4e090990be)int [bt\_audio\_codec\_cfg\_meta\_set\_bcast\_audio\_immediate\_rend\_flag](group__bt__audio__codec__cfg.md#gaede61b65d2037c7fbf6c4c4e090990be)(

1572 struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg);

1573

[ 1586](group__bt__audio__codec__cfg.md#ga1f76f82bff63b876eb761a0bf0377428)int [bt\_audio\_codec\_cfg\_meta\_get\_extended](group__bt__audio__codec__cfg.md#ga1f76f82bff63b876eb761a0bf0377428)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1587 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*extended\_meta);

1588

[ 1600](group__bt__audio__codec__cfg.md#gade9cb53287ab3356fb57ba8a454a3aad)int [bt\_audio\_codec\_cfg\_meta\_set\_extended](group__bt__audio__codec__cfg.md#gade9cb53287ab3356fb57ba8a454a3aad)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1601 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*extended\_meta, size\_t extended\_meta\_len);

1602

[ 1615](group__bt__audio__codec__cfg.md#ga4a4982e3bd0e8c944b584196ef146f6c)int [bt\_audio\_codec\_cfg\_meta\_get\_vendor](group__bt__audio__codec__cfg.md#ga4a4982e3bd0e8c944b584196ef146f6c)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1616 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*vendor\_meta);

1617

[ 1629](group__bt__audio__codec__cfg.md#ga6935d1c40b3178b0c8fa877ee93d1e53)int [bt\_audio\_codec\_cfg\_meta\_set\_vendor](group__bt__audio__codec__cfg.md#ga6935d1c40b3178b0c8fa877ee93d1e53)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1630 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*vendor\_meta, size\_t vendor\_meta\_len); /\* End of bt\_audio\_codec\_cfg \*/

1632

1642

[ 1654](group__bt__audio__codec__cap.md#gac3bf5dd414271bb1dcbc6590994cff6b)int [bt\_audio\_codec\_cap\_get\_val](group__bt__audio__codec__cap.md#gac3bf5dd414271bb1dcbc6590994cff6b)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1655 enum [bt\_audio\_codec\_cap\_type](group__bt__audio.md#gaf58823a56eb36cfd22e582ab1ea3d015) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*data);

1656

[ 1669](group__bt__audio__codec__cap.md#ga0c2c816b0b2b85aa5dd38f21caceea40)int [bt\_audio\_codec\_cap\_set\_val](group__bt__audio__codec__cap.md#ga0c2c816b0b2b85aa5dd38f21caceea40)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1670 enum [bt\_audio\_codec\_cap\_type](group__bt__audio.md#gaf58823a56eb36cfd22e582ab1ea3d015) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data,

1671 size\_t data\_len);

1672

[ 1684](group__bt__audio__codec__cap.md#gabc9962212ad65339ff02ba1389d5f9f8)int [bt\_audio\_codec\_cap\_unset\_val](group__bt__audio__codec__cap.md#gabc9962212ad65339ff02ba1389d5f9f8)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1685 enum [bt\_audio\_codec\_cap\_type](group__bt__audio.md#gaf58823a56eb36cfd22e582ab1ea3d015) type);

1686

[ 1697](group__bt__audio__codec__cap.md#gaa1dbf81c437c983af0144bf62433666c)int [bt\_audio\_codec\_cap\_get\_freq](group__bt__audio__codec__cap.md#gaa1dbf81c437c983af0144bf62433666c)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap);

1698

[ 1709](group__bt__audio__codec__cap.md#gac0655c0bd6552ab8a265076d7d0cd1b2)int [bt\_audio\_codec\_cap\_set\_freq](group__bt__audio__codec__cap.md#gac0655c0bd6552ab8a265076d7d0cd1b2)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1710 enum [bt\_audio\_codec\_cap\_freq](group__bt__audio.md#gaafc1106d5d305874ee2f540c850ff5b4) freq);

1711

[ 1722](group__bt__audio__codec__cap.md#ga12336de7d908bda94427caee4dc080e0)int [bt\_audio\_codec\_cap\_get\_frame\_dur](group__bt__audio__codec__cap.md#ga12336de7d908bda94427caee4dc080e0)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap);

1723

[ 1734](group__bt__audio__codec__cap.md#ga53e5df6cc4cfbed12b59a6a506657772)int [bt\_audio\_codec\_cap\_set\_frame\_dur](group__bt__audio__codec__cap.md#ga53e5df6cc4cfbed12b59a6a506657772)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1735 enum [bt\_audio\_codec\_cap\_frame\_dur](group__bt__audio.md#gaf37e8e19f956afb3c3a413cbaa1a21f5) frame\_dur);

1736

[ 1749](group__bt__audio__codec__cap.md#ga63d5e083f03ec06939ee1cd0355c8c2a)int [bt\_audio\_codec\_cap\_get\_supported\_audio\_chan\_counts](group__bt__audio__codec__cap.md#ga63d5e083f03ec06939ee1cd0355c8c2a)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1750 bool fallback\_to\_default);

1751

[ 1762](group__bt__audio__codec__cap.md#gaf6b2717823f9f3136237ed6a6515449e)int [bt\_audio\_codec\_cap\_set\_supported\_audio\_chan\_counts](group__bt__audio__codec__cap.md#gaf6b2717823f9f3136237ed6a6515449e)(

1763 struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, enum [bt\_audio\_codec\_cap\_chan\_count](group__bt__audio.md#gae695b5d17359967703f2509db1671fa5) chan\_count);

1764

[ 1776](group__bt__audio__codec__cap.md#gaa949089f2c6c143041e6cb61338e0ddc)int [bt\_audio\_codec\_cap\_get\_octets\_per\_frame](group__bt__audio__codec__cap.md#gaa949089f2c6c143041e6cb61338e0ddc)(

1777 const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1778 struct [bt\_audio\_codec\_octets\_per\_codec\_frame](structbt__audio__codec__octets__per__codec__frame.md) \*codec\_frame);

1779

[ 1790](group__bt__audio__codec__cap.md#gac1c42460cd3c55bbfbd467f84ab2d78d)int [bt\_audio\_codec\_cap\_set\_octets\_per\_frame](group__bt__audio__codec__cap.md#gac1c42460cd3c55bbfbd467f84ab2d78d)(

1791 struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1792 const struct [bt\_audio\_codec\_octets\_per\_codec\_frame](structbt__audio__codec__octets__per__codec__frame.md) \*codec\_frame);

1793

[ 1806](group__bt__audio__codec__cap.md#ga194d938896ee65601bdce96d68c84885)int [bt\_audio\_codec\_cap\_get\_max\_codec\_frames\_per\_sdu](group__bt__audio__codec__cap.md#ga194d938896ee65601bdce96d68c84885)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1807 bool fallback\_to\_default);

1808

[ 1819](group__bt__audio__codec__cap.md#ga3785bc41f56f8f2a09248396dadb31da)int [bt\_audio\_codec\_cap\_set\_max\_codec\_frames\_per\_sdu](group__bt__audio__codec__cap.md#ga3785bc41f56f8f2a09248396dadb31da)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1820 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) codec\_frames\_per\_sdu);

1821

[ 1833](group__bt__audio__codec__cap.md#ga5c2ecbb4d0cef26dd2cc5d023e70a163)int [bt\_audio\_codec\_cap\_meta\_get\_val](group__bt__audio__codec__cap.md#ga5c2ecbb4d0cef26dd2cc5d023e70a163)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type,

1834 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*data);

1835

[ 1848](group__bt__audio__codec__cap.md#ga1fdfd8c36f4131bcf4ffd2b7f176b631)int [bt\_audio\_codec\_cap\_meta\_set\_val](group__bt__audio__codec__cap.md#ga1fdfd8c36f4131bcf4ffd2b7f176b631)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1849 enum [bt\_audio\_metadata\_type](group__bt__audio.md#gab53d0dd62bceff97cf8eed7d8cf80354) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data,

1850 size\_t data\_len);

1851

[ 1863](group__bt__audio__codec__cap.md#ga40848f5375d1e58622c580112c282f2e)int [bt\_audio\_codec\_cap\_meta\_unset\_val](group__bt__audio__codec__cap.md#ga40848f5375d1e58622c580112c282f2e)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1864 enum [bt\_audio\_metadata\_type](group__bt__audio.md#gab53d0dd62bceff97cf8eed7d8cf80354) type);

1865

[ 1878](group__bt__audio__codec__cap.md#gaaa8c6783241b1b70349354b3e36c696c)int [bt\_audio\_codec\_cap\_meta\_get\_pref\_context](group__bt__audio__codec__cap.md#gaaa8c6783241b1b70349354b3e36c696c)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap);

1879

[ 1890](group__bt__audio__codec__cap.md#ga7fe0d4553d6accf5c89645cbf86149bf)int [bt\_audio\_codec\_cap\_meta\_set\_pref\_context](group__bt__audio__codec__cap.md#ga7fe0d4553d6accf5c89645cbf86149bf)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1891 enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) ctx);

1892

[ 1905](group__bt__audio__codec__cap.md#ga88ee657b5bd3f847bb75c9620ddb142f)int [bt\_audio\_codec\_cap\_meta\_get\_stream\_context](group__bt__audio__codec__cap.md#ga88ee657b5bd3f847bb75c9620ddb142f)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap);

1906

[ 1917](group__bt__audio__codec__cap.md#ga5cc7f360049c38c8de631ea33dbc44ab)int [bt\_audio\_codec\_cap\_meta\_set\_stream\_context](group__bt__audio__codec__cap.md#ga5cc7f360049c38c8de631ea33dbc44ab)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1918 enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) ctx);

1919

[ 1932](group__bt__audio__codec__cap.md#ga33725c3b2c06d6c22030bb5a77d702b0)int [bt\_audio\_codec\_cap\_meta\_get\_program\_info](group__bt__audio__codec__cap.md#ga33725c3b2c06d6c22030bb5a77d702b0)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1933 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*program\_info);

1934

[ 1946](group__bt__audio__codec__cap.md#ga43d2ec3a4d621c26843de82db7fd2189)int [bt\_audio\_codec\_cap\_meta\_set\_program\_info](group__bt__audio__codec__cap.md#ga43d2ec3a4d621c26843de82db7fd2189)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1947 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*program\_info, size\_t program\_info\_len);

1948

[ 1962](group__bt__audio__codec__cap.md#gafb631b55b69b256c60b9cf3c7f418ff8)int [bt\_audio\_codec\_cap\_meta\_get\_lang](group__bt__audio__codec__cap.md#gafb631b55b69b256c60b9cf3c7f418ff8)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1963 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*lang);

1964

[ 1975](group__bt__audio__codec__cap.md#ga8182b2bed20449b8581b89677893c130)int [bt\_audio\_codec\_cap\_meta\_set\_lang](group__bt__audio__codec__cap.md#ga8182b2bed20449b8581b89677893c130)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1976 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) lang[[BT\_AUDIO\_LANG\_SIZE](group__bt__audio.md#gab6e5f793d514626deca21940d35d8f21)]);

1977

[ 1990](group__bt__audio__codec__cap.md#ga3095dea36e60e75cbfe786d3c2f11866)int [bt\_audio\_codec\_cap\_meta\_get\_ccid\_list](group__bt__audio__codec__cap.md#ga3095dea36e60e75cbfe786d3c2f11866)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1991 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*ccid\_list);

1992

[ 2004](group__bt__audio__codec__cap.md#ga00a8ad22713dab761c81d1b8481c037d)int [bt\_audio\_codec\_cap\_meta\_set\_ccid\_list](group__bt__audio__codec__cap.md#ga00a8ad22713dab761c81d1b8481c037d)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

2005 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*ccid\_list, size\_t ccid\_list\_len);

2006

[ 2019](group__bt__audio__codec__cap.md#gab34d0369ce08efcd407d33956d32632e)int [bt\_audio\_codec\_cap\_meta\_get\_parental\_rating](group__bt__audio__codec__cap.md#gab34d0369ce08efcd407d33956d32632e)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap);

2020

[ 2031](group__bt__audio__codec__cap.md#ga5e267dfad978cd3d52be9c31a4fac0be)int [bt\_audio\_codec\_cap\_meta\_set\_parental\_rating](group__bt__audio__codec__cap.md#ga5e267dfad978cd3d52be9c31a4fac0be)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

2032 enum [bt\_audio\_parental\_rating](group__bt__audio.md#ga6d4aff1f93dc0b902e4b5d1355f15760) parental\_rating);

2033

[ 2046](group__bt__audio__codec__cap.md#gadb39b0ee1f65cdd2457fdf2c3142c040)int [bt\_audio\_codec\_cap\_meta\_get\_program\_info\_uri](group__bt__audio__codec__cap.md#gadb39b0ee1f65cdd2457fdf2c3142c040)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

2047 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*program\_info\_uri);

2048

[ 2060](group__bt__audio__codec__cap.md#gafbb0d6282d989e8bc70caada2845b337)int [bt\_audio\_codec\_cap\_meta\_set\_program\_info\_uri](group__bt__audio__codec__cap.md#gafbb0d6282d989e8bc70caada2845b337)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

2061 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*program\_info\_uri,

2062 size\_t program\_info\_uri\_len);

2063

[ 2076](group__bt__audio__codec__cap.md#ga88bb1da63b7ea0f95dd236aa1024cfb8)int [bt\_audio\_codec\_cap\_meta\_get\_audio\_active\_state](group__bt__audio__codec__cap.md#ga88bb1da63b7ea0f95dd236aa1024cfb8)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap);

2077

[ 2088](group__bt__audio__codec__cap.md#gacd3de0306a22d1a1d9ba09b4ac4f4e09)int [bt\_audio\_codec\_cap\_meta\_set\_audio\_active\_state](group__bt__audio__codec__cap.md#gacd3de0306a22d1a1d9ba09b4ac4f4e09)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

2089 enum [bt\_audio\_active\_state](group__bt__audio.md#ga16d403ec4db7be997682331ad365ff5f) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

2090

[ 2102](group__bt__audio__codec__cap.md#gab4ccc7cb7d779acb20185ae808dd8bbe)int [bt\_audio\_codec\_cap\_meta\_get\_bcast\_audio\_immediate\_rend\_flag](group__bt__audio__codec__cap.md#gab4ccc7cb7d779acb20185ae808dd8bbe)(

2103 const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap);

2104

[ 2114](group__bt__audio__codec__cap.md#gaa1d382b4fa53f7cbe8426df53a3317ce)int [bt\_audio\_codec\_cap\_meta\_set\_bcast\_audio\_immediate\_rend\_flag](group__bt__audio__codec__cap.md#gaa1d382b4fa53f7cbe8426df53a3317ce)(

2115 struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap);

2116

[ 2129](group__bt__audio__codec__cap.md#ga69aecd7e98f90a5162ff8ea3373b43d4)int [bt\_audio\_codec\_cap\_meta\_get\_extended](group__bt__audio__codec__cap.md#ga69aecd7e98f90a5162ff8ea3373b43d4)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

2130 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*extended\_meta);

2131

[ 2143](group__bt__audio__codec__cap.md#gac00aabc7329027852a7caf5cdff2bc26)int [bt\_audio\_codec\_cap\_meta\_set\_extended](group__bt__audio__codec__cap.md#gac00aabc7329027852a7caf5cdff2bc26)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

2144 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*extended\_meta, size\_t extended\_meta\_len);

2145

[ 2158](group__bt__audio__codec__cap.md#gab8c80a0f55041f026d453fd88cdeb727)int [bt\_audio\_codec\_cap\_meta\_get\_vendor](group__bt__audio__codec__cap.md#gab8c80a0f55041f026d453fd88cdeb727)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

2159 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*vendor\_meta);

2160

[ 2172](group__bt__audio__codec__cap.md#ga1f06789782541beab9aab4914f91bb57)int [bt\_audio\_codec\_cap\_meta\_set\_vendor](group__bt__audio__codec__cap.md#ga1f06789782541beab9aab4914f91bb57)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

2173 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*vendor\_meta, size\_t vendor\_meta\_len);

2174 /\* End of bt\_audio\_codec\_cap \*/

2176

2177#ifdef \_\_cplusplus

2178}

2179#endif

2180 /\* end of bt\_audio \*/

2182

2183#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_H\_ \*/

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

[bt\_audio\_codec\_cap\_meta\_get\_program\_info](group__bt__audio__codec__cap.md#ga33725c3b2c06d6c22030bb5a77d702b0)

int bt\_audio\_codec\_cap\_meta\_get\_program\_info(const struct bt\_audio\_codec\_cap \*codec\_cap, const uint8\_t \*\*program\_info)

Extract program info.

[bt\_audio\_codec\_cap\_set\_max\_codec\_frames\_per\_sdu](group__bt__audio__codec__cap.md#ga3785bc41f56f8f2a09248396dadb31da)

int bt\_audio\_codec\_cap\_set\_max\_codec\_frames\_per\_sdu(struct bt\_audio\_codec\_cap \*codec\_cap, uint8\_t codec\_frames\_per\_sdu)

Set the maximum codec frames per SDU of a codec capability.

[bt\_audio\_codec\_cap\_meta\_unset\_val](group__bt__audio__codec__cap.md#ga40848f5375d1e58622c580112c282f2e)

int bt\_audio\_codec\_cap\_meta\_unset\_val(struct bt\_audio\_codec\_cap \*codec\_cap, enum bt\_audio\_metadata\_type type)

Unset a specific codec capability metadata value.

[bt\_audio\_codec\_cap\_meta\_set\_program\_info](group__bt__audio__codec__cap.md#ga43d2ec3a4d621c26843de82db7fd2189)

int bt\_audio\_codec\_cap\_meta\_set\_program\_info(struct bt\_audio\_codec\_cap \*codec\_cap, const uint8\_t \*program\_info, size\_t program\_info\_len)

Set the program info of a codec capability metadata.

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

[bt\_audio\_codec\_cfg\_meta\_get\_bcast\_audio\_immediate\_rend\_flag](group__bt__audio__codec__cfg.md#ga66143aa7dcc726e06a12660b8f90fc5a)

int bt\_audio\_codec\_cfg\_meta\_get\_bcast\_audio\_immediate\_rend\_flag(const struct bt\_audio\_codec\_cfg \*codec\_cfg)

Extract broadcast audio immediate rendering flag.

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

[bt\_audio\_active\_state](group__bt__audio.md#ga16d403ec4db7be997682331ad365ff5f)

bt\_audio\_active\_state

Audio Active State defined by the Generic Audio assigned numbers (bluetooth.com).

**Definition** audio.h:415

[bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f)

bt\_audio\_dir

Audio direction from the perspective of the BAP Unicast Server / BAP Broadcast Sink.

**Definition** audio.h:763

[bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8)

bt\_audio\_location

Location values for BT Audio.

**Definition** audio.h:575

[bt\_audio\_parental\_rating](group__bt__audio.md#ga6d4aff1f93dc0b902e4b5d1355f15760)

bt\_audio\_parental\_rating

Parental rating defined by the Generic Audio assigned numbers (bluetooth.com).

**Definition** audio.h:379

[bt\_audio\_codec\_cfg\_frame\_dur](group__bt__audio.md#ga83701b5eadfcbc9b84dc0b1a85ebeb74)

bt\_audio\_codec\_cfg\_frame\_dur

Codec configuration frame duration.

**Definition** audio.h:291

[bt\_audio\_get\_chan\_count](group__bt__audio.md#ga87415f8dddd38b3f5641c96e9722a44a)

uint8\_t bt\_audio\_get\_chan\_count(enum bt\_audio\_location chan\_allocation)

Function to get the number of channels from the channel allocation.

[bt\_audio\_codec\_qos\_framing](group__bt__audio.md#ga8cb1832a3ee38b1a151b702c5dee00d9)

bt\_audio\_codec\_qos\_framing

Codec QoS Framing.

**Definition** audio.h:805

[bt\_audio\_codec\_cfg\_freq](group__bt__audio.md#ga8e99fb678cc011bb8c9f6e1858bae0d7)

bt\_audio\_codec\_cfg\_freq

Codec configuration sampling freqency.

**Definition** audio.h:249

[bt\_audio\_codec\_cfg\_type](group__bt__audio.md#ga9230ec4d7518bd243207ba2decb1a974)

bt\_audio\_codec\_cfg\_type

Codec configuration types.

**Definition** audio.h:231

[bt\_audio\_codec\_cap\_freq](group__bt__audio.md#gaafc1106d5d305874ee2f540c850ff5b4)

bt\_audio\_codec\_cap\_freq

Supported frequencies bitfield.

**Definition** audio.h:85

[bt\_audio\_metadata\_type](group__bt__audio.md#gab53d0dd62bceff97cf8eed7d8cf80354)

bt\_audio\_metadata\_type

Codec metadata type IDs.

**Definition** audio.h:427

[BT\_AUDIO\_LANG\_SIZE](group__bt__audio.md#gab6e5f793d514626deca21940d35d8f21)

#define BT\_AUDIO\_LANG\_SIZE

Size of the stream language value, e.g.

**Definition** audio.h:59

[bt\_audio\_codec\_cap\_chan\_count](group__bt__audio.md#gae695b5d17359967703f2509db1671fa5)

bt\_audio\_codec\_cap\_chan\_count

Supported audio capabilities channel count bitfield.

**Definition** audio.h:166

[bt\_audio\_codec\_cap\_frame\_dur](group__bt__audio.md#gaf37e8e19f956afb3c3a413cbaa1a21f5)

bt\_audio\_codec\_cap\_frame\_dur

Supported frame durations bitfield.

**Definition** audio.h:137

[bt\_audio\_codec\_cap\_type](group__bt__audio.md#gaf58823a56eb36cfd22e582ab1ea3d015)

bt\_audio\_codec\_cap\_type

Codec capability types.

**Definition** audio.h:67

[bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3)

bt\_audio\_context

Audio Context Type for Generic Audio.

**Definition** audio.h:304

[bt\_audio\_data\_parse](group__bt__audio.md#gafd8574b16141162c95653f0aa2bf6ff7)

int bt\_audio\_data\_parse(const uint8\_t ltv[], size\_t size, bool(\*func)(struct bt\_data \*data, void \*user\_data), void \*user\_data)

Helper for parsing length-type-value data.

[BT\_AUDIO\_ACTIVE\_STATE\_ENABLED](group__bt__audio.md#gga16d403ec4db7be997682331ad365ff5fa6d062944e9c49001666769601ba1c940)

@ BT\_AUDIO\_ACTIVE\_STATE\_ENABLED

Audio data is being transmitted.

**Definition** audio.h:419

[BT\_AUDIO\_ACTIVE\_STATE\_DISABLED](group__bt__audio.md#gga16d403ec4db7be997682331ad365ff5fade27604ea8fd592aa5d0958e2ccde4f3)

@ BT\_AUDIO\_ACTIVE\_STATE\_DISABLED

No audio data is being transmitted.

**Definition** audio.h:417

[BT\_AUDIO\_DIR\_SINK](group__bt__audio.md#gga5bd899fb5e4d844058184913866e462fa2adba49daa32ac7b040c3294f047ceb8)

@ BT\_AUDIO\_DIR\_SINK

Audio direction sink.

**Definition** audio.h:770

[BT\_AUDIO\_DIR\_SOURCE](group__bt__audio.md#gga5bd899fb5e4d844058184913866e462fa868695a31ebf95402a4bae2469f3aa6c)

@ BT\_AUDIO\_DIR\_SOURCE

Audio direction source.

**Definition** audio.h:777

[BT\_AUDIO\_LOCATION\_FRONT\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a06b34e67c9931f8b26562218cba51337)

@ BT\_AUDIO\_LOCATION\_FRONT\_CENTER

Front Center.

**Definition** audio.h:583

[BT\_AUDIO\_LOCATION\_TOP\_BACK\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a07e699c28bd847de3d85645dceb2ff06)

@ BT\_AUDIO\_LOCATION\_TOP\_BACK\_LEFT

Top Back Left.

**Definition** audio.h:611

[BT\_AUDIO\_LOCATION\_LOW\_FREQ\_EFFECTS\_2](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a0c304bdd529ad66acb71001caa1b361b)

@ BT\_AUDIO\_LOCATION\_LOW\_FREQ\_EFFECTS\_2

Low Frequency Effects 2.

**Definition** audio.h:597

[BT\_AUDIO\_LOCATION\_TOP\_SIDE\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a1cf8dea66e42f75ca85ba55124829a59)

@ BT\_AUDIO\_LOCATION\_TOP\_SIDE\_RIGHT

Top Side Right.

**Definition** audio.h:617

[BT\_AUDIO\_LOCATION\_FRONT\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a26d5ba460642bcf7fb2fc950082b70b3)

@ BT\_AUDIO\_LOCATION\_FRONT\_RIGHT

Front Right.

**Definition** audio.h:581

[BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a33d0f7c266f21fd086386f8c29ee31e8)

@ BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_RIGHT

Bottom Front Right.

**Definition** audio.h:625

[BT\_AUDIO\_LOCATION\_BACK\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a43f5070c2b4d39c38fa7900595d9b1aa)

@ BT\_AUDIO\_LOCATION\_BACK\_RIGHT

Back Right.

**Definition** audio.h:589

[BT\_AUDIO\_LOCATION\_TOP\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a555361fafade3bfb27dc713666757a1f)

@ BT\_AUDIO\_LOCATION\_TOP\_CENTER

Top Center.

**Definition** audio.h:609

[BT\_AUDIO\_LOCATION\_LEFT\_SURROUND](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a568a581c0ad653177f5d148d04bef0b6)

@ BT\_AUDIO\_LOCATION\_LEFT\_SURROUND

Left Surround.

**Definition** audio.h:631

[BT\_AUDIO\_LOCATION\_TOP\_FRONT\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a60b154a216d8e029deac7305500eaf2d)

@ BT\_AUDIO\_LOCATION\_TOP\_FRONT\_RIGHT

Top Front Right.

**Definition** audio.h:605

[BT\_AUDIO\_LOCATION\_FRONT\_RIGHT\_OF\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a725707ae4703a1f9b970de5b1e4e5692)

@ BT\_AUDIO\_LOCATION\_FRONT\_RIGHT\_OF\_CENTER

Front Right of Center.

**Definition** audio.h:593

[BT\_AUDIO\_LOCATION\_FRONT\_RIGHT\_WIDE](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a8649be1d5b7e8b312fc3374039cc0a71)

@ BT\_AUDIO\_LOCATION\_FRONT\_RIGHT\_WIDE

Front Right Wide.

**Definition** audio.h:629

[BT\_AUDIO\_LOCATION\_TOP\_BACK\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a8e81b80f732b0037493712b4baa21a69)

@ BT\_AUDIO\_LOCATION\_TOP\_BACK\_RIGHT

Top Back Right.

**Definition** audio.h:613

[BT\_AUDIO\_LOCATION\_MONO\_AUDIO](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a8f476de613cdcb2f9f677d40291aa5df)

@ BT\_AUDIO\_LOCATION\_MONO\_AUDIO

Mono Audio (no specified Audio Location).

**Definition** audio.h:577

[BT\_AUDIO\_LOCATION\_BACK\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a96906ff7918b0a3e3e7efe73a08d9896)

@ BT\_AUDIO\_LOCATION\_BACK\_LEFT

Back Left.

**Definition** audio.h:587

[BT\_AUDIO\_LOCATION\_RIGHT\_SURROUND](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a97954db823b6c6bed660ff2717600a5e)

@ BT\_AUDIO\_LOCATION\_RIGHT\_SURROUND

Right Surround.

**Definition** audio.h:633

[BT\_AUDIO\_LOCATION\_SIDE\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8aa01ad94f71defd158d8cfe25936341cd)

@ BT\_AUDIO\_LOCATION\_SIDE\_RIGHT

Side Right.

**Definition** audio.h:601

[BT\_AUDIO\_LOCATION\_TOP\_FRONT\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8aa093e6218e213eac5677766e01f5c1c9)

@ BT\_AUDIO\_LOCATION\_TOP\_FRONT\_LEFT

Top Front Left.

**Definition** audio.h:603

[BT\_AUDIO\_LOCATION\_SIDE\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ab8e52c69b894e382f0f09cc370337064)

@ BT\_AUDIO\_LOCATION\_SIDE\_LEFT

Side Left.

**Definition** audio.h:599

[BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ac1e355baee6ca0907356d72f0d4edb29)

@ BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_LEFT

Bottom Front Left.

**Definition** audio.h:623

[BT\_AUDIO\_LOCATION\_TOP\_FRONT\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ac32ed6f456be2fb2d9af2c7b255f3a4e)

@ BT\_AUDIO\_LOCATION\_TOP\_FRONT\_CENTER

Top Front Center.

**Definition** audio.h:607

[BT\_AUDIO\_LOCATION\_LOW\_FREQ\_EFFECTS\_1](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ac4c09f948266f2c9c65b3bc16da2f3f6)

@ BT\_AUDIO\_LOCATION\_LOW\_FREQ\_EFFECTS\_1

Low Frequency Effects 1.

**Definition** audio.h:585

[BT\_AUDIO\_LOCATION\_FRONT\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ac658188fa6f1b4f248a149d0bde1e41b)

@ BT\_AUDIO\_LOCATION\_FRONT\_LEFT

Front Left.

**Definition** audio.h:579

[BT\_AUDIO\_LOCATION\_FRONT\_LEFT\_WIDE](group__bt__audio.md#gga61230848c02098352320fe751332c4e8acba90183626ad85c21692b7edd87133d)

@ BT\_AUDIO\_LOCATION\_FRONT\_LEFT\_WIDE

Front Left Wide.

**Definition** audio.h:627

[BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ad0be8f720f03feb18a23e77f0eff6376)

@ BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_CENTER

Bottom Front Center.

**Definition** audio.h:621

[BT\_AUDIO\_LOCATION\_BACK\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ae22cd1e458d8ff503741bf48262c7983)

@ BT\_AUDIO\_LOCATION\_BACK\_CENTER

Back Center.

**Definition** audio.h:595

[BT\_AUDIO\_LOCATION\_TOP\_SIDE\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ae846b2f4186b46d3690c71071c41c7d6)

@ BT\_AUDIO\_LOCATION\_TOP\_SIDE\_LEFT

Top Side Left.

**Definition** audio.h:615

[BT\_AUDIO\_LOCATION\_TOP\_BACK\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8aebae1f0f2537a806672820fb74eba5dd)

@ BT\_AUDIO\_LOCATION\_TOP\_BACK\_CENTER

Top Back Center.

**Definition** audio.h:619

[BT\_AUDIO\_LOCATION\_FRONT\_LEFT\_OF\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8af02a9d46877b742e8730bbf3dd6ad22e)

@ BT\_AUDIO\_LOCATION\_FRONT\_LEFT\_OF\_CENTER

Front Left of Center.

**Definition** audio.h:591

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_18\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a22167e0c033c176f592a447b14c30071)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_18\_OR\_ABOVE

Recommended for listeners of age 18 and above.

**Definition** audio.h:411

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_15\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a3fe7bc3216a458ec3e5c6e177f43c077)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_15\_OR\_ABOVE

Recommended for listeners of age 15 and above.

**Definition** audio.h:405

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_10\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a4210d67d4506f8b9defb5fae32ae30d2)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_10\_OR\_ABOVE

Recommended for listeners of age 10 and above.

**Definition** audio.h:395

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_7\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a69508e569059bde1fed1b3fb3db1547a)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_7\_OR\_ABOVE

Recommended for listeners of age 7 and above.

**Definition** audio.h:389

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_16\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a779c5dd14e5f88e8e6bb247dc66d9c92)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_16\_OR\_ABOVE

Recommended for listeners of age 16 and above.

**Definition** audio.h:407

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_17\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a7d0794fe6796f19ff7e58819728751ff)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_17\_OR\_ABOVE

Recommended for listeners of age 17 and above.

**Definition** audio.h:409

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_5\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a8a8476abac3a569bd470a5237642c526)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_5\_OR\_ABOVE

Recommended for listeners of age 5 and above.

**Definition** audio.h:385

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_8\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a9ed111f80d0671bb8b4e0a304ff0b0e4)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_8\_OR\_ABOVE

Recommended for listeners of age 8 and above.

**Definition** audio.h:391

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_13\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760aa680247699538d256111e18af1a2d15d)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_13\_OR\_ABOVE

Recommended for listeners of age 13 and above.

**Definition** audio.h:401

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_9\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760aaabe26ebaa4b84684005440176ad86dd)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_9\_OR\_ABOVE

Recommended for listeners of age 9 and above.

**Definition** audio.h:393

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_11\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760ac402ee4c06b92f0cc36774cf409cbbd0)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_11\_OR\_ABOVE

Recommended for listeners of age 11 and above.

**Definition** audio.h:397

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_12\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760ac68caf6719391afbef79e0c579dc96e7)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_12\_OR\_ABOVE

Recommended for listeners of age 12 and above.

**Definition** audio.h:399

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_6\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760accb959ba21c1238c70c594b5cdc3ebdc)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_6\_OR\_ABOVE

Recommended for listeners of age 6 and above.

**Definition** audio.h:387

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_ANY](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760ad6bba6a3b9537fcf913f798ab9a525f1)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_ANY

For all ages.

**Definition** audio.h:383

[BT\_AUDIO\_PARENTAL\_RATING\_NO\_RATING](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760aecf628bbd76651215232c8bfed04aa2c)

@ BT\_AUDIO\_PARENTAL\_RATING\_NO\_RATING

No rating.

**Definition** audio.h:381

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_14\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760aef216d59983eccb86e90c493b8c17d86)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_14\_OR\_ABOVE

Recommended for listeners of age 14 and above.

**Definition** audio.h:403

[BT\_AUDIO\_CODEC\_CFG\_DURATION\_10](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ab6a0dd3bbe587ff5ba110675a01514a7)

@ BT\_AUDIO\_CODEC\_CFG\_DURATION\_10

10 msec Frame Duration configuration

**Definition** audio.h:296

[BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ad2491c0ded7c7f489bdeffe024463272)

@ BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5

7.5 msec Frame Duration configuration

**Definition** audio.h:293

[BT\_AUDIO\_CODEC\_QOS\_FRAMING\_UNFRAMED](group__bt__audio.md#gga8cb1832a3ee38b1a151b702c5dee00d9a426ad2fe26f69d135beff6a367ef872f)

@ BT\_AUDIO\_CODEC\_QOS\_FRAMING\_UNFRAMED

Packets may be framed or unframed.

**Definition** audio.h:807

[BT\_AUDIO\_CODEC\_QOS\_FRAMING\_FRAMED](group__bt__audio.md#gga8cb1832a3ee38b1a151b702c5dee00d9af7a4a07da9089c3afb248d63e3a9297a)

@ BT\_AUDIO\_CODEC\_QOS\_FRAMING\_FRAMED

Packets are always framed.

**Definition** audio.h:809

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_24KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a0d6d0f278628681f8ef5dc3797bf5275)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_24KHZ

24 Khz codec sampling frequency

**Definition** audio.h:263

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a2b7163ba4c486167d3e81c2aa4216f11)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ

48 Khz codec sampling frequency

**Definition** audio.h:272

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a3ce97404475ad182125ad64aba66077e)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ

32 Khz codec sampling frequency

**Definition** audio.h:266

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_384KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a44cccbd3e7afc25f964b3c2c571d4be4)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_384KHZ

384 Khz codec sampling frequency

**Definition** audio.h:287

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_22KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a68f8411a83f60ec4c6bb9fa65fdd7048)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_22KHZ

22.05 Khz codec sampling frequency

**Definition** audio.h:260

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_8KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a7018d3fb612d4730b880ef0bb2d20b9a)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_8KHZ

8 Khz codec sampling frequency

**Definition** audio.h:251

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_96KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a79e7a473d3f7d6803f3b8b7843c40c60)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_96KHZ

96 Khz codec sampling frequency

**Definition** audio.h:278

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_176KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a85037a2eb4a64376a0a436ab43263126)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_176KHZ

176.4 Khz codec sampling frequency

**Definition** audio.h:281

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_44KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aa701e855c950fdcdd66d4dbaaf75fb84)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_44KHZ

44.1 Khz codec sampling frequency

**Definition** audio.h:269

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_192KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aa85a51db272ef019e5cce5ec3982f8c7)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_192KHZ

192 Khz codec sampling frequency

**Definition** audio.h:284

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_11KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aa8d8018b050a8c029b4b60c706d771f8)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_11KHZ

11.025 Khz codec sampling frequency

**Definition** audio.h:254

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_16KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7ab097ae9f9ad963fee64e61eaf2663245)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_16KHZ

16 Khz codec sampling frequency

**Definition** audio.h:257

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_88KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aff685ebe62909eea8512b7deac0df409)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_88KHZ

88.2 Khz codec sampling frequency

**Definition** audio.h:275

[BT\_AUDIO\_CODEC\_CFG\_FREQ](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974a49849b389d553535ea222c9ae63bccc3)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ

Sampling frequency.

**Definition** audio.h:233

[BT\_AUDIO\_CODEC\_CFG\_FRAME\_LEN](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974a85d41856175c11b1193ebdd58b83d6e2)

@ BT\_AUDIO\_CODEC\_CFG\_FRAME\_LEN

Octets per codec frame.

**Definition** audio.h:242

[BT\_AUDIO\_CODEC\_CFG\_DURATION](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974a8e2fae97b1565b0fa0ff988a47928223)

@ BT\_AUDIO\_CODEC\_CFG\_DURATION

Frame duration.

**Definition** audio.h:236

[BT\_AUDIO\_CODEC\_CFG\_FRAME\_BLKS\_PER\_SDU](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974abbc2279f5d029278d9367f08a1152aa8)

@ BT\_AUDIO\_CODEC\_CFG\_FRAME\_BLKS\_PER\_SDU

Codec frame blocks per SDU.

**Definition** audio.h:245

[BT\_AUDIO\_CODEC\_CFG\_CHAN\_ALLOC](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974ad53deb048fb0ce4d4428df4f477718b2)

@ BT\_AUDIO\_CODEC\_CFG\_CHAN\_ALLOC

Audio channel allocation.

**Definition** audio.h:239

[BT\_AUDIO\_CODEC\_QOS\_CODED](group__bt__audio.md#ggaa69a4789478a1a0aa93451d294de7ad0a9789c1b6b319370a3b98ab37b61a86e0)

@ BT\_AUDIO\_CODEC\_QOS\_CODED

LE Coded PHY.

**Definition** audio.h:819

[BT\_AUDIO\_CODEC\_QOS\_1M](group__bt__audio.md#ggaa69a4789478a1a0aa93451d294de7ad0ab387760c001ea6c81e889de55e74d5d5)

@ BT\_AUDIO\_CODEC\_QOS\_1M

LE 1M PHY.

**Definition** audio.h:815

[BT\_AUDIO\_CODEC\_QOS\_2M](group__bt__audio.md#ggaa69a4789478a1a0aa93451d294de7ad0ac81306188ed29b8fa17aa2afa878f297)

@ BT\_AUDIO\_CODEC\_QOS\_2M

LE 2M PHY.

**Definition** audio.h:817

[BT\_AUDIO\_CODEC\_CAP\_FREQ\_176KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a031d159eadf7ea1ba6b00b03bef26d2b)

@ BT\_AUDIO\_CODEC\_CAP\_FREQ\_176KHZ

176.4 Khz sampling frequency

**Definition** audio.h:117

[BT\_AUDIO\_CODEC\_CAP\_FREQ\_192KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a0de8d0351153650c1b48934053e18890)

@ BT\_AUDIO\_CODEC\_CAP\_FREQ\_192KHZ

192 Khz sampling frequency

**Definition** audio.h:120

[BT\_AUDIO\_CODEC\_CAP\_FREQ\_88KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a25cc72bd630446f5154c54402058a211)

@ BT\_AUDIO\_CODEC\_CAP\_FREQ\_88KHZ

88.2 Khz sampling frequency

**Definition** audio.h:111

[BT\_AUDIO\_CODEC\_CAP\_FREQ\_8KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a3d821d03771805107707f47dcdb71f83)

@ BT\_AUDIO\_CODEC\_CAP\_FREQ\_8KHZ

8 Khz sampling frequency

**Definition** audio.h:87

[BT\_AUDIO\_CODEC\_CAP\_FREQ\_11KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a562c38a59cded025183a0f95d4a63c81)

@ BT\_AUDIO\_CODEC\_CAP\_FREQ\_11KHZ

11.025 Khz sampling frequency

**Definition** audio.h:90

[BT\_AUDIO\_CODEC\_CAP\_FREQ\_32KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a822ff105ab495c126c21d73bd90cbd9c)

@ BT\_AUDIO\_CODEC\_CAP\_FREQ\_32KHZ

32 Khz sampling frequency

**Definition** audio.h:102

[BT\_AUDIO\_CODEC\_CAP\_FREQ\_48KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a91ec17ee96b8e56e31ab545e5e8abe91)

@ BT\_AUDIO\_CODEC\_CAP\_FREQ\_48KHZ

48 Khz sampling frequency

**Definition** audio.h:108

[BT\_AUDIO\_CODEC\_CAP\_FREQ\_24KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4acf9ff8842d72d56d27eae692e4c4b956)

@ BT\_AUDIO\_CODEC\_CAP\_FREQ\_24KHZ

24 Khz sampling frequency

**Definition** audio.h:99

[BT\_AUDIO\_CODEC\_CAP\_FREQ\_16KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4acfef6825ac865b1e590e7959a9270361)

@ BT\_AUDIO\_CODEC\_CAP\_FREQ\_16KHZ

16 Khz sampling frequency

**Definition** audio.h:93

[BT\_AUDIO\_CODEC\_CAP\_FREQ\_44KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ad28396f4b5a71d7c196e1a27bd17f8c3)

@ BT\_AUDIO\_CODEC\_CAP\_FREQ\_44KHZ

44.1 Khz sampling frequency

**Definition** audio.h:105

[BT\_AUDIO\_CODEC\_CAP\_FREQ\_22KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ad7440157cf8864dfc5fd854482f3a982)

@ BT\_AUDIO\_CODEC\_CAP\_FREQ\_22KHZ

22.05 Khz sampling frequency

**Definition** audio.h:96

[BT\_AUDIO\_CODEC\_CAP\_FREQ\_ANY](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4adaaa42a6bb0c01d3819c604b6d5bbf02)

@ BT\_AUDIO\_CODEC\_CAP\_FREQ\_ANY

Any frequency capability.

**Definition** audio.h:126

[BT\_AUDIO\_CODEC\_CAP\_FREQ\_384KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ae5ddc4504b7077e90be56f34ad8647c2)

@ BT\_AUDIO\_CODEC\_CAP\_FREQ\_384KHZ

384 Khz sampling frequency

**Definition** audio.h:123

[BT\_AUDIO\_CODEC\_CAP\_FREQ\_96KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ae802fea402f207238613275917846663)

@ BT\_AUDIO\_CODEC\_CAP\_FREQ\_96KHZ

96 Khz sampling frequency

**Definition** audio.h:114

[BT\_AUDIO\_METADATA\_TYPE\_PROGRAM\_INFO](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a02f91ea7fb6be631687d843ad7bf4ac7)

@ BT\_AUDIO\_METADATA\_TYPE\_PROGRAM\_INFO

UTF-8 encoded title or summary of stream content.

**Definition** audio.h:453

[BT\_AUDIO\_METADATA\_TYPE\_EXTENDED](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a0b5a8cd34bad81ac53c657c3cd9ddb39)

@ BT\_AUDIO\_METADATA\_TYPE\_EXTENDED

Extended metadata.

**Definition** audio.h:487

[BT\_AUDIO\_METADATA\_TYPE\_VENDOR](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a30fbc4a159e64174b22f195f29012286)

@ BT\_AUDIO\_METADATA\_TYPE\_VENDOR

Vendor specific metadata.

**Definition** audio.h:490

[BT\_AUDIO\_METADATA\_TYPE\_CCID\_LIST](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a37b5552e04734392dc6c6eb9e19b377b)

@ BT\_AUDIO\_METADATA\_TYPE\_CCID\_LIST

Array of 8-bit CCID values.

**Definition** audio.h:464

[BT\_AUDIO\_METADATA\_TYPE\_BROADCAST\_IMMEDIATE](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a4b9cc5b82a1dbfc3db69bb12747443f1)

@ BT\_AUDIO\_METADATA\_TYPE\_BROADCAST\_IMMEDIATE

Broadcast Audio Immediate Rendering flag.

**Definition** audio.h:484

[BT\_AUDIO\_METADATA\_TYPE\_PROGRAM\_INFO\_URI](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a58971ea21b5045e56a0e1ca838358922)

@ BT\_AUDIO\_METADATA\_TYPE\_PROGRAM\_INFO\_URI

UTF-8 encoded URI for additional Program information.

**Definition** audio.h:474

[BT\_AUDIO\_METADATA\_TYPE\_PARENTAL\_RATING](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a7a83f397dc5dbe6e6d60a994cccdc613)

@ BT\_AUDIO\_METADATA\_TYPE\_PARENTAL\_RATING

Parental rating.

**Definition** audio.h:471

[BT\_AUDIO\_METADATA\_TYPE\_STREAM\_CONTEXT](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a95f128b11584ee22100ae65ce751dbaa)

@ BT\_AUDIO\_METADATA\_TYPE\_STREAM\_CONTEXT

Streaming audio context.

**Definition** audio.h:450

[BT\_AUDIO\_METADATA\_TYPE\_PREF\_CONTEXT](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354aac28d2a0dc883affa60b7a70f678ed9a)

@ BT\_AUDIO\_METADATA\_TYPE\_PREF\_CONTEXT

Preferred audio context.

**Definition** audio.h:438

[BT\_AUDIO\_METADATA\_TYPE\_AUDIO\_STATE](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354af220c40d351ec5e236cd41a5944da5fc)

@ BT\_AUDIO\_METADATA\_TYPE\_AUDIO\_STATE

Audio active state.

**Definition** audio.h:481

[BT\_AUDIO\_METADATA\_TYPE\_LANG](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354af38d342d907c3903121a03bb8394efb1)

@ BT\_AUDIO\_METADATA\_TYPE\_LANG

Language.

**Definition** audio.h:461

[BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_4](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a0fdfa6bf69b104f04d22e4f968969ac2)

@ BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_4

Supporting 4 channel.

**Definition** audio.h:177

[BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_2](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a13b236d93eb9c7516fdcf527313e16cd)

@ BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_2

Supporting 2 channel.

**Definition** audio.h:171

[BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_1](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a1558716b36042597515df18ff277f8bc)

@ BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_1

Supporting 1 channel.

**Definition** audio.h:168

[BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_3](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a17da27ec39a79c341c82549df891cb39)

@ BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_3

Supporting 3 channel.

**Definition** audio.h:174

[BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_8](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a50afa60bdd53172fab7a376ce374d943)

@ BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_8

Supporting 8 channel.

**Definition** audio.h:189

[BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_7](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a86ef227772c7751b4ae75529e2a57b82)

@ BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_7

Supporting 7 channel.

**Definition** audio.h:186

[BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_ANY](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5aaf6f7179310c64b93b300ecfc29e4219)

@ BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_ANY

Supporting all channels.

**Definition** audio.h:192

[BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_5](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5ad08bc2ea0347a1ee8fd411a023b7ca51)

@ BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_5

Supporting 5 channel.

**Definition** audio.h:180

[BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_6](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5af9f9dd0cac39793793e5c8c5e50b11b8)

@ BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_6

Supporting 6 channel.

**Definition** audio.h:183

[BT\_AUDIO\_CODEC\_CAP\_DURATION\_7\_5](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a340878058d0beabeade33e0f3893d441)

@ BT\_AUDIO\_CODEC\_CAP\_DURATION\_7\_5

7.5 msec frame duration capability

**Definition** audio.h:139

[BT\_AUDIO\_CODEC\_CAP\_DURATION\_PREFER\_7\_5](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a7ab1c63639cf93fdf2c2dfdf43424e91)

@ BT\_AUDIO\_CODEC\_CAP\_DURATION\_PREFER\_7\_5

7.5 msec preferred frame duration capability.

**Definition** audio.h:154

[BT\_AUDIO\_CODEC\_CAP\_DURATION\_ANY](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a81d28ce43d69d4625e9a73b37c70347a)

@ BT\_AUDIO\_CODEC\_CAP\_DURATION\_ANY

Any frame duration capability.

**Definition** audio.h:145

[BT\_AUDIO\_CODEC\_CAP\_DURATION\_PREFER\_10](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a9744473b3a29074c24cf0bbff35a5d8e)

@ BT\_AUDIO\_CODEC\_CAP\_DURATION\_PREFER\_10

10 msec preferred frame duration capability

**Definition** audio.h:162

[BT\_AUDIO\_CODEC\_CAP\_DURATION\_10](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5afd423ac4270ff0df8ca6df7f5e4c799b)

@ BT\_AUDIO\_CODEC\_CAP\_DURATION\_10

10 msec frame duration capability

**Definition** audio.h:142

[BT\_AUDIO\_CODEC\_CAP\_TYPE\_CHAN\_COUNT](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015a0cd3a3d31febc9e30137e9e21d4f7191)

@ BT\_AUDIO\_CODEC\_CAP\_TYPE\_CHAN\_COUNT

Supported audio channel counts.

**Definition** audio.h:75

[BT\_AUDIO\_CODEC\_CAP\_TYPE\_DURATION](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015a4a90a37cd6d8ca9d1ed984e4a122d510)

@ BT\_AUDIO\_CODEC\_CAP\_TYPE\_DURATION

Supported frame durations.

**Definition** audio.h:72

[BT\_AUDIO\_CODEC\_CAP\_TYPE\_FRAME\_COUNT](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015acba980896f080ac2ba81d1b66305bb41)

@ BT\_AUDIO\_CODEC\_CAP\_TYPE\_FRAME\_COUNT

Supported maximum codec frames per SDU.

**Definition** audio.h:81

[BT\_AUDIO\_CODEC\_CAP\_TYPE\_FRAME\_LEN](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015ad074bed5f79946e2388584336d30cf46)

@ BT\_AUDIO\_CODEC\_CAP\_TYPE\_FRAME\_LEN

Supported octets per codec frame.

**Definition** audio.h:78

[BT\_AUDIO\_CODEC\_CAP\_TYPE\_FREQ](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015af68f3f5665446de9b71c2f70e7aa762b)

@ BT\_AUDIO\_CODEC\_CAP\_TYPE\_FREQ

Supported sampling frequencies.

**Definition** audio.h:69

[BT\_AUDIO\_CONTEXT\_TYPE\_NOTIFICATIONS](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a06df6f713bb68b197be75bf821d5d377)

@ BT\_AUDIO\_CONTEXT\_TYPE\_NOTIFICATIONS

Notification and reminder sounds; attention-seeking audio, for example, in beeps signaling the arriva...

**Definition** audio.h:342

[BT\_AUDIO\_CONTEXT\_TYPE\_EMERGENCY\_ALARM](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a132abd2f9ac7be62d1306efc6bc8b7d1)

@ BT\_AUDIO\_CONTEXT\_TYPE\_EMERGENCY\_ALARM

Emergency alarm Emergency sounds, for example, fire alarms or other urgent alerts.

**Definition** audio.h:354

[BT\_AUDIO\_CONTEXT\_TYPE\_INSTRUCTIONAL](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a2e3af6f4ca620f91d9266257f842ddd4)

@ BT\_AUDIO\_CONTEXT\_TYPE\_INSTRUCTIONAL

Instructional audio, for example, in navigation, announcements, or user guidance.

**Definition** audio.h:325

[BT\_AUDIO\_CONTEXT\_TYPE\_PROHIBITED](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a3cfcfa76adc5effdc1aa95d75e5da37a)

@ BT\_AUDIO\_CONTEXT\_TYPE\_PROHIBITED

Prohibited.

**Definition** audio.h:306

[BT\_AUDIO\_CONTEXT\_TYPE\_RINGTONE](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a422bb29f035583b7319456a679f880b3)

@ BT\_AUDIO\_CONTEXT\_TYPE\_RINGTONE

Alerts the user to an incoming call, for example, an incoming telephony or video call,...

**Definition** audio.h:347

[BT\_AUDIO\_CONTEXT\_TYPE\_LIVE](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a42c80228bda513d5a59d4d836e73bd55)

@ BT\_AUDIO\_CONTEXT\_TYPE\_LIVE

Live audio, for example, from a microphone where audio is perceived both through a direct acoustic pa...

**Definition** audio.h:332

[BT\_AUDIO\_CONTEXT\_TYPE\_MEDIA](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a43d67936976a5c041027d15d66c21a5e)

@ BT\_AUDIO\_CONTEXT\_TYPE\_MEDIA

Media, for example, music playback, radio, podcast or movie soundtrack, or tv audio.

**Definition** audio.h:318

[BT\_AUDIO\_CONTEXT\_TYPE\_GAME](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a652ad83b9eb524c62933bf87a8ecb730)

@ BT\_AUDIO\_CONTEXT\_TYPE\_GAME

Audio associated with video gaming, for example gaming media; gaming effects; music and in-game voice...

**Definition** audio.h:323

[BT\_AUDIO\_CONTEXT\_TYPE\_SOUND\_EFFECTS](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a6956a9e43433e2800fd36c7022e039d9)

@ BT\_AUDIO\_CONTEXT\_TYPE\_SOUND\_EFFECTS

Sound effects including keyboard and touch feedback; menu and user interface sounds; and other system...

**Definition** audio.h:337

[BT\_AUDIO\_CONTEXT\_TYPE\_VOICE\_ASSISTANTS](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a7e208290ddc2f92ac78ff4a22b20ca7e)

@ BT\_AUDIO\_CONTEXT\_TYPE\_VOICE\_ASSISTANTS

Man-machine communication, for example, with voice recognition or virtual assistants.

**Definition** audio.h:327

[BT\_AUDIO\_CONTEXT\_TYPE\_CONVERSATIONAL](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a8a6262c1cf4e4591a7b92b4f8f329f9e)

@ BT\_AUDIO\_CONTEXT\_TYPE\_CONVERSATIONAL

Conversation between humans, for example, in telephony or video calls, including traditional cellular...

**Definition** audio.h:316

[BT\_AUDIO\_CONTEXT\_TYPE\_ALERTS](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a915d05a728f3e083f290766a970dabb6)

@ BT\_AUDIO\_CONTEXT\_TYPE\_ALERTS

Alarms and timers; immediate alerts, for example, in a critical battery alarm, timer expiry or alarm ...

**Definition** audio.h:352

[BT\_AUDIO\_CONTEXT\_TYPE\_UNSPECIFIED](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3aad96be1265bd1be4c937c687335e33f5)

@ BT\_AUDIO\_CONTEXT\_TYPE\_UNSPECIFIED

Identifies audio where the use case context does not match any other defined value,...

**Definition** audio.h:311

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

**Definition** audio.h:669

[bt\_audio\_codec\_cap::vid](structbt__audio__codec__cap.md#a3b91269e16a3d63b3128a527caa5e3ff)

uint16\_t vid

Codec Company Vendor ID.

**Definition** audio.h:687

[bt\_audio\_codec\_cap::data](structbt__audio__codec__cap.md#a455638aac9167d288a1e7a9fccabc49d)

uint8\_t data[CONFIG\_BT\_AUDIO\_CODEC\_CAP\_MAX\_DATA\_SIZE]

Codec Specific Capabilities Data.

**Definition** audio.h:692

[bt\_audio\_codec\_cap::cid](structbt__audio__codec__cap.md#a763222d12a87958a5ba806303f98829a)

uint16\_t cid

Codec Company ID.

**Definition** audio.h:685

[bt\_audio\_codec\_cap::path\_id](structbt__audio__codec__cap.md#a822a06f815091cc580ca2e5bbb3126f7)

uint8\_t path\_id

Data path ID.

**Definition** audio.h:675

[bt\_audio\_codec\_cap::ctlr\_transcode](structbt__audio__codec__cap.md#a900a77db09e72de61d4ff652c6dbb10b)

bool ctlr\_transcode

Whether or not the local controller should transcode.

**Definition** audio.h:681

[bt\_audio\_codec\_cap::meta](structbt__audio__codec__cap.md#acec4f5e31752d81d4dbf441223e7f44c)

uint8\_t meta[CONFIG\_BT\_AUDIO\_CODEC\_CAP\_MAX\_METADATA\_SIZE]

Codec Specific Capabilities Metadata.

**Definition** audio.h:698

[bt\_audio\_codec\_cap::data\_len](structbt__audio__codec__cap.md#acf3e22c6db1533fff7015acbc7eca196)

size\_t data\_len

Codec Specific Capabilities Data count.

**Definition** audio.h:690

[bt\_audio\_codec\_cap::id](structbt__audio__codec__cap.md#ae3892731e7ca05f3ec426c70f0d9e1a9)

uint8\_t id

Codec ID.

**Definition** audio.h:683

[bt\_audio\_codec\_cap::meta\_len](structbt__audio__codec__cap.md#afe806521d5aac36e9f6c6a0598500a8f)

size\_t meta\_len

Codec Specific Capabilities Metadata count.

**Definition** audio.h:696

[bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md)

Codec specific configuration structure.

**Definition** audio.h:703

[bt\_audio\_codec\_cfg::meta\_len](structbt__audio__codec__cfg.md#a1e69a5c017e9571b50aba721f86876fb)

size\_t meta\_len

Codec Specific Capabilities Metadata count.

**Definition** audio.h:730

[bt\_audio\_codec\_cfg::vid](structbt__audio__codec__cfg.md#a2996ab3f6ae1cab09ff5e3329b42468e)

uint16\_t vid

Codec Company Vendor ID.

**Definition** audio.h:721

[bt\_audio\_codec\_cfg::meta](structbt__audio__codec__cfg.md#a4f84974ea14b773ad8e2fd7c0ffa0c7f)

uint8\_t meta[CONFIG\_BT\_AUDIO\_CODEC\_CFG\_MAX\_METADATA\_SIZE]

Codec Specific Capabilities Metadata.

**Definition** audio.h:732

[bt\_audio\_codec\_cfg::cid](structbt__audio__codec__cfg.md#a664e21bcd6002b21d4b1b53d866db32d)

uint16\_t cid

Codec Company ID.

**Definition** audio.h:719

[bt\_audio\_codec\_cfg::data\_len](structbt__audio__codec__cfg.md#a8a5a789e9993a48ce4c83a2156c1f43c)

size\_t data\_len

Codec Specific Capabilities Data count.

**Definition** audio.h:724

[bt\_audio\_codec\_cfg::path\_id](structbt__audio__codec__cfg.md#a9386056bb02908407c9e3aad48abbd87)

uint8\_t path\_id

Data path ID.

**Definition** audio.h:709

[bt\_audio\_codec\_cfg::ctlr\_transcode](structbt__audio__codec__cfg.md#a9e2c8081950a0830ffc270245ab308c1)

bool ctlr\_transcode

Whether or not the local controller should transcode.

**Definition** audio.h:715

[bt\_audio\_codec\_cfg::id](structbt__audio__codec__cfg.md#aa2f99ec31ff3eb9b7b738bc8a1170f20)

uint8\_t id

Codec ID.

**Definition** audio.h:717

[bt\_audio\_codec\_cfg::data](structbt__audio__codec__cfg.md#ad3709d5321f6faeb392452cb3b21023b)

uint8\_t data[CONFIG\_BT\_AUDIO\_CODEC\_CFG\_MAX\_DATA\_SIZE]

Codec Specific Capabilities Data.

**Definition** audio.h:726

[bt\_audio\_codec\_octets\_per\_codec\_frame](structbt__audio__codec__octets__per__codec__frame.md)

struct to hold minimum and maximum supported codec frame sizes

**Definition** audio.h:218

[bt\_audio\_codec\_octets\_per\_codec\_frame::min](structbt__audio__codec__octets__per__codec__frame.md#aa8b234fa137273cd16230ebabc5f8ef4)

uint16\_t min

Minimum number of octets supported per codec frame.

**Definition** audio.h:220

[bt\_audio\_codec\_octets\_per\_codec\_frame::max](structbt__audio__codec__octets__per__codec__frame.md#ae09686799077b13e78b856b1e7e63b6a)

uint16\_t max

Maximum number of octets supported per codec frame.

**Definition** audio.h:222

[bt\_audio\_codec\_qos\_pref](structbt__audio__codec__qos__pref.md)

Audio Stream Quality of Service Preference structure.

**Definition** audio.h:972

[bt\_audio\_codec\_qos\_pref::latency](structbt__audio__codec__qos__pref.md#a1d46cf0aa05cfb7c88446719e59e0011)

uint16\_t latency

Preferred Transport Latency.

**Definition** audio.h:988

[bt\_audio\_codec\_qos\_pref::phy](structbt__audio__codec__qos__pref.md#a36fc375290b8f76c7278a236942db692)

uint8\_t phy

Preferred PHY.

**Definition** audio.h:982

[bt\_audio\_codec\_qos\_pref::unframed\_supported](structbt__audio__codec__qos__pref.md#a3bdb319d2aa401102fb9e54f92993e83)

bool unframed\_supported

Unframed PDUs supported.

**Definition** audio.h:979

[bt\_audio\_codec\_qos\_pref::pref\_pd\_max](structbt__audio__codec__qos__pref.md#a5486cacf6cd5016e9b44b69e3da67d6d)

uint32\_t pref\_pd\_max

Preferred maximum Presentation Delay.

**Definition** audio.h:1022

[bt\_audio\_codec\_qos\_pref::pd\_min](structbt__audio__codec__qos__pref.md#a7437273abb18ce93c15bb789eeeb65d3)

uint32\_t pd\_min

Minimum Presentation Delay in microseconds.

**Definition** audio.h:998

[bt\_audio\_codec\_qos\_pref::pd\_max](structbt__audio__codec__qos__pref.md#ab07f2245bfed3a1400b6a1e6eaad2735)

uint32\_t pd\_max

Maximum Presentation Delay.

**Definition** audio.h:1008

[bt\_audio\_codec\_qos\_pref::pref\_pd\_min](structbt__audio__codec__qos__pref.md#ab38a4b98b47ab773f91873b42c69ed71)

uint32\_t pref\_pd\_min

Preferred minimum Presentation Delay.

**Definition** audio.h:1015

[bt\_audio\_codec\_qos\_pref::rtn](structbt__audio__codec__qos__pref.md#abc2142ef5c8ad1744b829ae626a57e9d)

uint8\_t rtn

Preferred Retransmission Number.

**Definition** audio.h:985

[bt\_audio\_codec\_qos](structbt__audio__codec__qos.md)

Codec QoS structure.

**Definition** audio.h:849

[bt\_audio\_codec\_qos::pd](structbt__audio__codec__qos.md#a28d87b06785e016fe7e12a0504f3b419)

uint32\_t pd

Presentation Delay in microseconds.

**Definition** audio.h:860

[bt\_audio\_codec\_qos::framing](structbt__audio__codec__qos.md#a4212bf93b65e0faa218a1e0d03ae0283)

enum bt\_audio\_codec\_qos\_framing framing

QoS Framing.

**Definition** audio.h:871

[bt\_audio\_codec\_qos::burst\_number](structbt__audio__codec__qos.md#a42c025d09fb7f6ce8af136e01837e002)

uint8\_t burst\_number

Burst number.

**Definition** audio.h:932

[bt\_audio\_codec\_qos::num\_subevents](structbt__audio__codec__qos.md#a7b66a27686feda162ea70fdc9ae17425)

uint8\_t num\_subevents

Number of subevents.

**Definition** audio.h:941

[bt\_audio\_codec\_qos::phy](structbt__audio__codec__qos.md#a8911b0b9db8e4de55b3c313e3ad7c502)

uint8\_t phy

PHY.

**Definition** audio.h:879

[bt\_audio\_codec\_qos::max\_pdu](structbt__audio__codec__qos.md#a98a5b8ba8ab2b2a289714916f38a1e27)

uint16\_t max\_pdu

Maximum PDU size.

**Definition** audio.h:925

[bt\_audio\_codec\_qos::rtn](structbt__audio__codec__qos.md#ab05af8d47df82d34921afdd557770dbd)

uint8\_t rtn

Retransmission Number.

**Definition** audio.h:887

[bt\_audio\_codec\_qos::latency](structbt__audio__codec__qos.md#acb0fb67ff7c24d6d00c318cccb6b6eb3)

uint16\_t latency

Maximum Transport Latency.

**Definition** audio.h:903

[bt\_audio\_codec\_qos::interval](structbt__audio__codec__qos.md#ad906dc06624b0f80701d7ee92d849152)

uint32\_t interval

SDU Interval.

**Definition** audio.h:911

[bt\_audio\_codec\_qos::sdu](structbt__audio__codec__qos.md#ae1a5adb80af9357fd6ee6532b0ba228e)

uint16\_t sdu

Maximum SDU size.

**Definition** audio.h:894

[bt\_data](structbt__data.md)

Bluetooth data.

**Definition** bluetooth.h:454

[atomic.h](sys_2atomic_8h.md)

[util.h](util_8h.md)

Misc utilities.

[util\_macro.h](util__macro_8h.md)

Macro utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [audio.h](bluetooth_2audio_2audio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
