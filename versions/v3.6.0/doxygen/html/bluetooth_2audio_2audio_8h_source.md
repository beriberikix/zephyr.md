---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/bluetooth_2audio_2audio_8h_source.html
original_path: doxygen/html/bluetooth_2audio_2audio_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

audio.h

[Go to the documentation of this file.](bluetooth_2audio_2audio_8h.md)

1

4

5/\*

6 \* Copyright (c) 2020 Intel Corporation

7 \* Copyright (c) 2020-2023 Nordic Semiconductor ASA

8 \*

9 \* SPDX-License-Identifier: Apache-2.0

10 \*/

11#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_AUDIO\_H\_

12#define ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_AUDIO\_H\_

13

20

21#include <[zephyr/sys/atomic.h](atomic_8h.md)>

22#include <[zephyr/bluetooth/buf.h](bluetooth_2buf_8h.md)>

23#include <[zephyr/bluetooth/conn.h](conn_8h.md)>

24#include <[zephyr/bluetooth/hci.h](hci_8h.md)>

25#include <[zephyr/bluetooth/iso.h](iso_8h.md)>

26#include <[zephyr/bluetooth/gatt.h](gatt_8h.md)>

27#include <[zephyr/bluetooth/audio/lc3.h](lc3_8h.md)>

28

29

30#ifdef \_\_cplusplus

31extern "C" {

32#endif

33

[ 34](group__bt__audio.md#ga18dd9f4a4af7716dd01497309ff9c87c)#define BT\_AUDIO\_BROADCAST\_ID\_SIZE 3 /\* octets \*/

[ 36](group__bt__audio.md#ga3ed5ba09ab4c1ab7a59f8a1b4deee791)#define BT\_AUDIO\_BROADCAST\_ID\_MAX 0xFFFFFFU

[ 38](group__bt__audio.md#ga663ab7bf74d56f36ee6cc80b369cbc16)#define BT\_AUDIO\_PD\_PREF\_NONE 0x000000U

[ 40](group__bt__audio.md#gaaa0414a4baef5a867fd1c6b1865d2dbc)#define BT\_AUDIO\_PD\_MAX 0xFFFFFFU

41

[ 42](group__bt__audio.md#ga6eedc1f97491b38fe20b91688c62ffc0)#define BT\_AUDIO\_BROADCAST\_CODE\_SIZE 16

43

[ 50](group__bt__audio.md#gaf58823a56eb36cfd22e582ab1ea3d015)enum [bt\_audio\_codec\_cap\_type](group__bt__audio.md#gaf58823a56eb36cfd22e582ab1ea3d015) {

[ 52](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015af68f3f5665446de9b71c2f70e7aa762b) [BT\_AUDIO\_CODEC\_CAP\_TYPE\_FREQ](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015af68f3f5665446de9b71c2f70e7aa762b) = 0x01,

53

[ 55](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015a4a90a37cd6d8ca9d1ed984e4a122d510) [BT\_AUDIO\_CODEC\_CAP\_TYPE\_DURATION](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015a4a90a37cd6d8ca9d1ed984e4a122d510) = 0x02,

56

[ 58](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015a0cd3a3d31febc9e30137e9e21d4f7191) [BT\_AUDIO\_CODEC\_CAP\_TYPE\_CHAN\_COUNT](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015a0cd3a3d31febc9e30137e9e21d4f7191) = 0x03,

59

[ 61](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015ad074bed5f79946e2388584336d30cf46) [BT\_AUDIO\_CODEC\_CAP\_TYPE\_FRAME\_LEN](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015ad074bed5f79946e2388584336d30cf46) = 0x04,

62

[ 64](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015acba980896f080ac2ba81d1b66305bb41) [BT\_AUDIO\_CODEC\_CAP\_TYPE\_FRAME\_COUNT](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015acba980896f080ac2ba81d1b66305bb41) = 0x05,

65};

66

[ 68](group__bt__audio.md#gaafc1106d5d305874ee2f540c850ff5b4)enum [bt\_audio\_codec\_cap\_freq](group__bt__audio.md#gaafc1106d5d305874ee2f540c850ff5b4) {

[ 70](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a3d821d03771805107707f47dcdb71f83) [BT\_AUDIO\_CODEC\_CAP\_FREQ\_8KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a3d821d03771805107707f47dcdb71f83) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

71

[ 73](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a562c38a59cded025183a0f95d4a63c81) [BT\_AUDIO\_CODEC\_CAP\_FREQ\_11KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a562c38a59cded025183a0f95d4a63c81) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

74

[ 76](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4acfef6825ac865b1e590e7959a9270361) [BT\_AUDIO\_CODEC\_CAP\_FREQ\_16KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4acfef6825ac865b1e590e7959a9270361) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

77

[ 79](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ad7440157cf8864dfc5fd854482f3a982) [BT\_AUDIO\_CODEC\_CAP\_FREQ\_22KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ad7440157cf8864dfc5fd854482f3a982) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

80

[ 82](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4acf9ff8842d72d56d27eae692e4c4b956) [BT\_AUDIO\_CODEC\_CAP\_FREQ\_24KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4acf9ff8842d72d56d27eae692e4c4b956) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

83

[ 85](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a822ff105ab495c126c21d73bd90cbd9c) [BT\_AUDIO\_CODEC\_CAP\_FREQ\_32KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a822ff105ab495c126c21d73bd90cbd9c) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

86

[ 88](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ad28396f4b5a71d7c196e1a27bd17f8c3) [BT\_AUDIO\_CODEC\_CAP\_FREQ\_44KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ad28396f4b5a71d7c196e1a27bd17f8c3) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6),

89

[ 91](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a91ec17ee96b8e56e31ab545e5e8abe91) [BT\_AUDIO\_CODEC\_CAP\_FREQ\_48KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a91ec17ee96b8e56e31ab545e5e8abe91) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7),

92

[ 94](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a25cc72bd630446f5154c54402058a211) [BT\_AUDIO\_CODEC\_CAP\_FREQ\_88KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a25cc72bd630446f5154c54402058a211) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8),

95

[ 97](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ae802fea402f207238613275917846663) [BT\_AUDIO\_CODEC\_CAP\_FREQ\_96KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ae802fea402f207238613275917846663) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9),

98

[ 100](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a031d159eadf7ea1ba6b00b03bef26d2b) [BT\_AUDIO\_CODEC\_CAP\_FREQ\_176KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a031d159eadf7ea1ba6b00b03bef26d2b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10),

101

[ 103](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a0de8d0351153650c1b48934053e18890) [BT\_AUDIO\_CODEC\_CAP\_FREQ\_192KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a0de8d0351153650c1b48934053e18890) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11),

104

[ 106](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ae5ddc4504b7077e90be56f34ad8647c2) [BT\_AUDIO\_CODEC\_CAP\_FREQ\_384KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ae5ddc4504b7077e90be56f34ad8647c2) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12),

107

[ 109](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4adaaa42a6bb0c01d3819c604b6d5bbf02) [BT\_AUDIO\_CODEC\_CAP\_FREQ\_ANY](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4adaaa42a6bb0c01d3819c604b6d5bbf02) =

110 ([BT\_AUDIO\_CODEC\_CAP\_FREQ\_8KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a3d821d03771805107707f47dcdb71f83) | [BT\_AUDIO\_CODEC\_CAP\_FREQ\_11KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a562c38a59cded025183a0f95d4a63c81) |

111 [BT\_AUDIO\_CODEC\_CAP\_FREQ\_16KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4acfef6825ac865b1e590e7959a9270361) | [BT\_AUDIO\_CODEC\_CAP\_FREQ\_22KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ad7440157cf8864dfc5fd854482f3a982) |

112 [BT\_AUDIO\_CODEC\_CAP\_FREQ\_24KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4acf9ff8842d72d56d27eae692e4c4b956) | [BT\_AUDIO\_CODEC\_CAP\_FREQ\_32KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a822ff105ab495c126c21d73bd90cbd9c) |

113 [BT\_AUDIO\_CODEC\_CAP\_FREQ\_44KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ad28396f4b5a71d7c196e1a27bd17f8c3) | [BT\_AUDIO\_CODEC\_CAP\_FREQ\_48KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a91ec17ee96b8e56e31ab545e5e8abe91) |

114 [BT\_AUDIO\_CODEC\_CAP\_FREQ\_88KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a25cc72bd630446f5154c54402058a211) | [BT\_AUDIO\_CODEC\_CAP\_FREQ\_96KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ae802fea402f207238613275917846663) |

115 [BT\_AUDIO\_CODEC\_CAP\_FREQ\_176KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a031d159eadf7ea1ba6b00b03bef26d2b) | [BT\_AUDIO\_CODEC\_CAP\_FREQ\_192KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a0de8d0351153650c1b48934053e18890) |

116 [BT\_AUDIO\_CODEC\_CAP\_FREQ\_384KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ae5ddc4504b7077e90be56f34ad8647c2)),

117};

118

[ 120](group__bt__audio.md#gaf37e8e19f956afb3c3a413cbaa1a21f5)enum [bt\_audio\_codec\_cap\_frame\_dur](group__bt__audio.md#gaf37e8e19f956afb3c3a413cbaa1a21f5) {

[ 122](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a340878058d0beabeade33e0f3893d441) [BT\_AUDIO\_CODEC\_CAP\_DURATION\_7\_5](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a340878058d0beabeade33e0f3893d441) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

123

[ 125](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5afd423ac4270ff0df8ca6df7f5e4c799b) [BT\_AUDIO\_CODEC\_CAP\_DURATION\_10](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5afd423ac4270ff0df8ca6df7f5e4c799b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

126

[ 128](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a81d28ce43d69d4625e9a73b37c70347a) [BT\_AUDIO\_CODEC\_CAP\_DURATION\_ANY](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a81d28ce43d69d4625e9a73b37c70347a) =

129 ([BT\_AUDIO\_CODEC\_CAP\_DURATION\_7\_5](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a340878058d0beabeade33e0f3893d441) | [BT\_AUDIO\_CODEC\_CAP\_DURATION\_10](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5afd423ac4270ff0df8ca6df7f5e4c799b)),

130

[ 137](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a7ab1c63639cf93fdf2c2dfdf43424e91) [BT\_AUDIO\_CODEC\_CAP\_DURATION\_PREFER\_7\_5](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a7ab1c63639cf93fdf2c2dfdf43424e91) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

138

[ 145](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a9744473b3a29074c24cf0bbff35a5d8e) [BT\_AUDIO\_CODEC\_CAP\_DURATION\_PREFER\_10](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a9744473b3a29074c24cf0bbff35a5d8e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

146};

147

[ 148](group__bt__audio.md#gae695b5d17359967703f2509db1671fa5)enum [bt\_audio\_codec\_cap\_chan\_count](group__bt__audio.md#gae695b5d17359967703f2509db1671fa5) {

[ 150](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a1558716b36042597515df18ff277f8bc) [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_1](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a1558716b36042597515df18ff277f8bc) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

151

[ 153](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a13b236d93eb9c7516fdcf527313e16cd) [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_2](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a13b236d93eb9c7516fdcf527313e16cd) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

154

[ 156](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a17da27ec39a79c341c82549df891cb39) [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_3](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a17da27ec39a79c341c82549df891cb39) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

157

[ 159](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a0fdfa6bf69b104f04d22e4f968969ac2) [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_4](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a0fdfa6bf69b104f04d22e4f968969ac2) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

160

[ 162](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5ad08bc2ea0347a1ee8fd411a023b7ca51) [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_5](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5ad08bc2ea0347a1ee8fd411a023b7ca51) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

163

[ 165](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5af9f9dd0cac39793793e5c8c5e50b11b8) [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_6](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5af9f9dd0cac39793793e5c8c5e50b11b8) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

166

[ 168](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a86ef227772c7751b4ae75529e2a57b82) [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_7](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a86ef227772c7751b4ae75529e2a57b82) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6),

169

[ 171](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a50afa60bdd53172fab7a376ce374d943) [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_8](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a50afa60bdd53172fab7a376ce374d943) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7),

172

[ 174](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5aaf6f7179310c64b93b300ecfc29e4219) [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_ANY](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5aaf6f7179310c64b93b300ecfc29e4219) =

175 ([BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_1](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a1558716b36042597515df18ff277f8bc) | [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_2](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a13b236d93eb9c7516fdcf527313e16cd) |

176 [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_3](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a17da27ec39a79c341c82549df891cb39) | [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_4](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a0fdfa6bf69b104f04d22e4f968969ac2) |

177 [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_5](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5ad08bc2ea0347a1ee8fd411a023b7ca51) | [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_6](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5af9f9dd0cac39793793e5c8c5e50b11b8) |

178 [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_7](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a86ef227772c7751b4ae75529e2a57b82) | [BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_8](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a50afa60bdd53172fab7a376ce374d943)),

179};

180

[ 182](group__bt__audio.md#gac1251f8a35b5e343eeeff87f22f8ab10)#define BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_MIN 1

[ 184](group__bt__audio.md#gad91341739d394f92ffc4988b614f47b6)#define BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_MAX 8

185

[ 196](group__bt__audio.md#ga8f835266fabd6461216fe13e1b3b3a0f)#define BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_SUPPORT(...) \

197 ((enum bt\_audio\_codec\_cap\_chan\_count)((FOR\_EACH(BIT, (|), \_\_VA\_ARGS\_\_)) >> 1))

198

[ 199](structbt__audio__codec__octets__per__codec__frame.md)struct [bt\_audio\_codec\_octets\_per\_codec\_frame](structbt__audio__codec__octets__per__codec__frame.md) {

[ 201](structbt__audio__codec__octets__per__codec__frame.md#aa8b234fa137273cd16230ebabc5f8ef4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [min](structbt__audio__codec__octets__per__codec__frame.md#aa8b234fa137273cd16230ebabc5f8ef4);

[ 203](structbt__audio__codec__octets__per__codec__frame.md#ae09686799077b13e78b856b1e7e63b6a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [max](structbt__audio__codec__octets__per__codec__frame.md#ae09686799077b13e78b856b1e7e63b6a);

204};

205

[ 212](group__bt__audio.md#ga9230ec4d7518bd243207ba2decb1a974)enum [bt\_audio\_codec\_cfg\_type](group__bt__audio.md#ga9230ec4d7518bd243207ba2decb1a974) {

[ 214](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974a49849b389d553535ea222c9ae63bccc3) [BT\_AUDIO\_CODEC\_CFG\_FREQ](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974a49849b389d553535ea222c9ae63bccc3) = 0x01,

215

[ 217](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974a8e2fae97b1565b0fa0ff988a47928223) [BT\_AUDIO\_CODEC\_CFG\_DURATION](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974a8e2fae97b1565b0fa0ff988a47928223) = 0x02,

218

[ 220](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974ad53deb048fb0ce4d4428df4f477718b2) [BT\_AUDIO\_CODEC\_CFG\_CHAN\_ALLOC](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974ad53deb048fb0ce4d4428df4f477718b2) = 0x03,

221

[ 223](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974a85d41856175c11b1193ebdd58b83d6e2) [BT\_AUDIO\_CODEC\_CFG\_FRAME\_LEN](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974a85d41856175c11b1193ebdd58b83d6e2) = 0x04,

224

[ 226](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974abbc2279f5d029278d9367f08a1152aa8) [BT\_AUDIO\_CODEC\_CFG\_FRAME\_BLKS\_PER\_SDU](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974abbc2279f5d029278d9367f08a1152aa8) = 0x05,

227};

228

[ 229](group__bt__audio.md#ga8e99fb678cc011bb8c9f6e1858bae0d7)enum [bt\_audio\_codec\_cfg\_freq](group__bt__audio.md#ga8e99fb678cc011bb8c9f6e1858bae0d7) {

[ 231](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a7018d3fb612d4730b880ef0bb2d20b9a) [BT\_AUDIO\_CODEC\_CFG\_FREQ\_8KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a7018d3fb612d4730b880ef0bb2d20b9a) = 0x01,

232

[ 234](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aa8d8018b050a8c029b4b60c706d771f8) [BT\_AUDIO\_CODEC\_CFG\_FREQ\_11KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aa8d8018b050a8c029b4b60c706d771f8) = 0x02,

235

[ 237](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7ab097ae9f9ad963fee64e61eaf2663245) [BT\_AUDIO\_CODEC\_CFG\_FREQ\_16KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7ab097ae9f9ad963fee64e61eaf2663245) = 0x03,

238

[ 240](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a68f8411a83f60ec4c6bb9fa65fdd7048) [BT\_AUDIO\_CODEC\_CFG\_FREQ\_22KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a68f8411a83f60ec4c6bb9fa65fdd7048) = 0x04,

241

[ 243](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a0d6d0f278628681f8ef5dc3797bf5275) [BT\_AUDIO\_CODEC\_CFG\_FREQ\_24KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a0d6d0f278628681f8ef5dc3797bf5275) = 0x05,

244

[ 246](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a3ce97404475ad182125ad64aba66077e) [BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a3ce97404475ad182125ad64aba66077e) = 0x06,

247

[ 249](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aa701e855c950fdcdd66d4dbaaf75fb84) [BT\_AUDIO\_CODEC\_CFG\_FREQ\_44KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aa701e855c950fdcdd66d4dbaaf75fb84) = 0x07,

250

[ 252](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a2b7163ba4c486167d3e81c2aa4216f11) [BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a2b7163ba4c486167d3e81c2aa4216f11) = 0x08,

253

[ 255](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aff685ebe62909eea8512b7deac0df409) [BT\_AUDIO\_CODEC\_CFG\_FREQ\_88KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aff685ebe62909eea8512b7deac0df409) = 0x09,

256

[ 258](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a79e7a473d3f7d6803f3b8b7843c40c60) [BT\_AUDIO\_CODEC\_CFG\_FREQ\_96KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a79e7a473d3f7d6803f3b8b7843c40c60) = 0x0a,

259

[ 261](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a85037a2eb4a64376a0a436ab43263126) [BT\_AUDIO\_CODEC\_CFG\_FREQ\_176KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a85037a2eb4a64376a0a436ab43263126) = 0x0b,

262

[ 264](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aa85a51db272ef019e5cce5ec3982f8c7) [BT\_AUDIO\_CODEC\_CFG\_FREQ\_192KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aa85a51db272ef019e5cce5ec3982f8c7) = 0x0c,

265

[ 267](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a44cccbd3e7afc25f964b3c2c571d4be4) [BT\_AUDIO\_CODEC\_CFG\_FREQ\_384KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a44cccbd3e7afc25f964b3c2c571d4be4) = 0x0d,

268};

269

[ 270](group__bt__audio.md#ga83701b5eadfcbc9b84dc0b1a85ebeb74)enum [bt\_audio\_codec\_cfg\_frame\_dur](group__bt__audio.md#ga83701b5eadfcbc9b84dc0b1a85ebeb74) {

[ 272](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ad2491c0ded7c7f489bdeffe024463272) [BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ad2491c0ded7c7f489bdeffe024463272) = 0x00,

273

[ 275](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ab6a0dd3bbe587ff5ba110675a01514a7) [BT\_AUDIO\_CODEC\_CFG\_DURATION\_10](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ab6a0dd3bbe587ff5ba110675a01514a7) = 0x01,

276};

277

[ 282](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3)enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) {

[ 283](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a3cfcfa76adc5effdc1aa95d75e5da37a) [BT\_AUDIO\_CONTEXT\_TYPE\_PROHIBITED](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a3cfcfa76adc5effdc1aa95d75e5da37a) = 0,

[ 284](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3aad96be1265bd1be4c937c687335e33f5) [BT\_AUDIO\_CONTEXT\_TYPE\_UNSPECIFIED](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3aad96be1265bd1be4c937c687335e33f5) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 285](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a8a6262c1cf4e4591a7b92b4f8f329f9e) [BT\_AUDIO\_CONTEXT\_TYPE\_CONVERSATIONAL](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a8a6262c1cf4e4591a7b92b4f8f329f9e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 286](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a43d67936976a5c041027d15d66c21a5e) [BT\_AUDIO\_CONTEXT\_TYPE\_MEDIA](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a43d67936976a5c041027d15d66c21a5e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 287](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a652ad83b9eb524c62933bf87a8ecb730) [BT\_AUDIO\_CONTEXT\_TYPE\_GAME](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a652ad83b9eb524c62933bf87a8ecb730) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

[ 288](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a2e3af6f4ca620f91d9266257f842ddd4) [BT\_AUDIO\_CONTEXT\_TYPE\_INSTRUCTIONAL](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a2e3af6f4ca620f91d9266257f842ddd4) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

[ 289](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a7e208290ddc2f92ac78ff4a22b20ca7e) [BT\_AUDIO\_CONTEXT\_TYPE\_VOICE\_ASSISTANTS](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a7e208290ddc2f92ac78ff4a22b20ca7e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

[ 290](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a42c80228bda513d5a59d4d836e73bd55) [BT\_AUDIO\_CONTEXT\_TYPE\_LIVE](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a42c80228bda513d5a59d4d836e73bd55) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6),

[ 291](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a6956a9e43433e2800fd36c7022e039d9) [BT\_AUDIO\_CONTEXT\_TYPE\_SOUND\_EFFECTS](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a6956a9e43433e2800fd36c7022e039d9) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7),

[ 292](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a06df6f713bb68b197be75bf821d5d377) [BT\_AUDIO\_CONTEXT\_TYPE\_NOTIFICATIONS](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a06df6f713bb68b197be75bf821d5d377) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8),

[ 293](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a422bb29f035583b7319456a679f880b3) [BT\_AUDIO\_CONTEXT\_TYPE\_RINGTONE](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a422bb29f035583b7319456a679f880b3) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9),

[ 294](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a915d05a728f3e083f290766a970dabb6) [BT\_AUDIO\_CONTEXT\_TYPE\_ALERTS](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a915d05a728f3e083f290766a970dabb6) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10),

[ 295](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a132abd2f9ac7be62d1306efc6bc8b7d1) [BT\_AUDIO\_CONTEXT\_TYPE\_EMERGENCY\_ALARM](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a132abd2f9ac7be62d1306efc6bc8b7d1) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11),

296};

297

[ 301](group__bt__audio.md#ga6320f86aab9b227385bdf52a9ff3985b)#define BT\_AUDIO\_CONTEXT\_TYPE\_ANY (BT\_AUDIO\_CONTEXT\_TYPE\_UNSPECIFIED | \

302 BT\_AUDIO\_CONTEXT\_TYPE\_CONVERSATIONAL | \

303 BT\_AUDIO\_CONTEXT\_TYPE\_MEDIA | \

304 BT\_AUDIO\_CONTEXT\_TYPE\_GAME | \

305 BT\_AUDIO\_CONTEXT\_TYPE\_INSTRUCTIONAL | \

306 BT\_AUDIO\_CONTEXT\_TYPE\_VOICE\_ASSISTANTS | \

307 BT\_AUDIO\_CONTEXT\_TYPE\_LIVE | \

308 BT\_AUDIO\_CONTEXT\_TYPE\_SOUND\_EFFECTS | \

309 BT\_AUDIO\_CONTEXT\_TYPE\_NOTIFICATIONS | \

310 BT\_AUDIO\_CONTEXT\_TYPE\_RINGTONE | \

311 BT\_AUDIO\_CONTEXT\_TYPE\_ALERTS | \

312 BT\_AUDIO\_CONTEXT\_TYPE\_EMERGENCY\_ALARM)

313

[ 320](group__bt__audio.md#ga6d4aff1f93dc0b902e4b5d1355f15760)enum [bt\_audio\_parental\_rating](group__bt__audio.md#ga6d4aff1f93dc0b902e4b5d1355f15760) {

[ 321](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760aecf628bbd76651215232c8bfed04aa2c) [BT\_AUDIO\_PARENTAL\_RATING\_NO\_RATING](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760aecf628bbd76651215232c8bfed04aa2c) = 0x00,

[ 322](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760ad6bba6a3b9537fcf913f798ab9a525f1) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_ANY](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760ad6bba6a3b9537fcf913f798ab9a525f1) = 0x01,

[ 323](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a8a8476abac3a569bd470a5237642c526) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_5\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a8a8476abac3a569bd470a5237642c526) = 0x02,

[ 324](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760accb959ba21c1238c70c594b5cdc3ebdc) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_6\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760accb959ba21c1238c70c594b5cdc3ebdc) = 0x03,

[ 325](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a69508e569059bde1fed1b3fb3db1547a) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_7\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a69508e569059bde1fed1b3fb3db1547a) = 0x04,

[ 326](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a9ed111f80d0671bb8b4e0a304ff0b0e4) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_8\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a9ed111f80d0671bb8b4e0a304ff0b0e4) = 0x05,

[ 327](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760aaabe26ebaa4b84684005440176ad86dd) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_9\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760aaabe26ebaa4b84684005440176ad86dd) = 0x06,

[ 328](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a4210d67d4506f8b9defb5fae32ae30d2) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_10\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a4210d67d4506f8b9defb5fae32ae30d2) = 0x07,

[ 329](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760ac402ee4c06b92f0cc36774cf409cbbd0) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_11\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760ac402ee4c06b92f0cc36774cf409cbbd0) = 0x08,

[ 330](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760ac68caf6719391afbef79e0c579dc96e7) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_12\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760ac68caf6719391afbef79e0c579dc96e7) = 0x09,

[ 331](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760aa680247699538d256111e18af1a2d15d) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_13\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760aa680247699538d256111e18af1a2d15d) = 0x0A,

[ 332](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760aef216d59983eccb86e90c493b8c17d86) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_14\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760aef216d59983eccb86e90c493b8c17d86) = 0x0B,

[ 333](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a3fe7bc3216a458ec3e5c6e177f43c077) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_15\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a3fe7bc3216a458ec3e5c6e177f43c077) = 0x0C,

[ 334](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a779c5dd14e5f88e8e6bb247dc66d9c92) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_16\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a779c5dd14e5f88e8e6bb247dc66d9c92) = 0x0D,

[ 335](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a7d0794fe6796f19ff7e58819728751ff) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_17\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a7d0794fe6796f19ff7e58819728751ff) = 0x0E,

[ 336](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a22167e0c033c176f592a447b14c30071) [BT\_AUDIO\_PARENTAL\_RATING\_AGE\_18\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a22167e0c033c176f592a447b14c30071) = 0x0F

337};

338

[ 340](group__bt__audio.md#ga16d403ec4db7be997682331ad365ff5f)enum [bt\_audio\_active\_state](group__bt__audio.md#ga16d403ec4db7be997682331ad365ff5f) {

[ 341](group__bt__audio.md#gga16d403ec4db7be997682331ad365ff5fade27604ea8fd592aa5d0958e2ccde4f3) [BT\_AUDIO\_ACTIVE\_STATE\_DISABLED](group__bt__audio.md#gga16d403ec4db7be997682331ad365ff5fade27604ea8fd592aa5d0958e2ccde4f3) = 0x00,

[ 342](group__bt__audio.md#gga16d403ec4db7be997682331ad365ff5fa6d062944e9c49001666769601ba1c940) [BT\_AUDIO\_ACTIVE\_STATE\_ENABLED](group__bt__audio.md#gga16d403ec4db7be997682331ad365ff5fa6d062944e9c49001666769601ba1c940) = 0x01,

343};

344

[ 350](group__bt__audio.md#gab53d0dd62bceff97cf8eed7d8cf80354)enum [bt\_audio\_metadata\_type](group__bt__audio.md#gab53d0dd62bceff97cf8eed7d8cf80354) {

[ 360](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354aac28d2a0dc883affa60b7a70f678ed9a) [BT\_AUDIO\_METADATA\_TYPE\_PREF\_CONTEXT](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354aac28d2a0dc883affa60b7a70f678ed9a) = 0x01,

361

[ 371](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a95f128b11584ee22100ae65ce751dbaa) [BT\_AUDIO\_METADATA\_TYPE\_STREAM\_CONTEXT](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a95f128b11584ee22100ae65ce751dbaa) = 0x02,

372

[ 374](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a02f91ea7fb6be631687d843ad7bf4ac7) [BT\_AUDIO\_METADATA\_TYPE\_PROGRAM\_INFO](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a02f91ea7fb6be631687d843ad7bf4ac7) = 0x03,

375

[ 380](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354ae98c430a422e3583d19d1b391b97edda) [BT\_AUDIO\_METADATA\_TYPE\_STREAM\_LANG](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354ae98c430a422e3583d19d1b391b97edda) = 0x04,

381

[ 383](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a37b5552e04734392dc6c6eb9e19b377b) [BT\_AUDIO\_METADATA\_TYPE\_CCID\_LIST](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a37b5552e04734392dc6c6eb9e19b377b) = 0x05,

384

[ 389](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a7a83f397dc5dbe6e6d60a994cccdc613) [BT\_AUDIO\_METADATA\_TYPE\_PARENTAL\_RATING](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a7a83f397dc5dbe6e6d60a994cccdc613) = 0x06,

390

[ 392](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a58971ea21b5045e56a0e1ca838358922) [BT\_AUDIO\_METADATA\_TYPE\_PROGRAM\_INFO\_URI](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a58971ea21b5045e56a0e1ca838358922) = 0x07,

393

[ 398](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354af220c40d351ec5e236cd41a5944da5fc) [BT\_AUDIO\_METADATA\_TYPE\_AUDIO\_STATE](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354af220c40d351ec5e236cd41a5944da5fc) = 0x08,

399

[ 401](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a4b9cc5b82a1dbfc3db69bb12747443f1) [BT\_AUDIO\_METADATA\_TYPE\_BROADCAST\_IMMEDIATE](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a4b9cc5b82a1dbfc3db69bb12747443f1) = 0x09,

402

[ 404](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a0b5a8cd34bad81ac53c657c3cd9ddb39) [BT\_AUDIO\_METADATA\_TYPE\_EXTENDED](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a0b5a8cd34bad81ac53c657c3cd9ddb39) = 0xFE,

405

[ 407](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a30fbc4a159e64174b22f195f29012286) [BT\_AUDIO\_METADATA\_TYPE\_VENDOR](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a30fbc4a159e64174b22f195f29012286) = 0xFF,

408};

409

[ 415](group__bt__audio.md#ga86a7e9ca661a3b13b7c59d41d206156e)#define BT\_AUDIO\_METADATA\_TYPE\_IS\_KNOWN(\_type) \

416 (IN\_RANGE((\_type), BT\_AUDIO\_METADATA\_TYPE\_PREF\_CONTEXT, \

417 BT\_AUDIO\_METADATA\_TYPE\_BROADCAST\_IMMEDIATE) || \

418 (\_type) == BT\_AUDIO\_METADATA\_TYPE\_EXTENDED || (\_type) == BT\_AUDIO\_METADATA\_TYPE\_VENDOR)

419

420/\* Unicast Announcement Type, Generic Audio \*/

[ 421](group__bt__audio.md#ga41db714fa87e85896a52427399633bb4)#define BT\_AUDIO\_UNICAST\_ANNOUNCEMENT\_GENERAL 0x00

[ 422](group__bt__audio.md#ga56c14acb7f182a413fdecac4e271c5cc)#define BT\_AUDIO\_UNICAST\_ANNOUNCEMENT\_TARGETED 0x01

423

[ 432](group__bt__audio.md#gaddc49e39465798ae4c0cbe345e0b50d7)#define BT\_AUDIO\_CODEC\_DATA(\_type, \_bytes...) \

433 (sizeof((uint8\_t)\_type) + sizeof((uint8\_t[]){\_bytes})), (\_type), \_bytes

434

[ 444](group__bt__audio.md#gaefed7a013e282c63c9b5cbbdcdc67448)#define BT\_AUDIO\_CODEC\_CFG(\_id, \_cid, \_vid, \_data, \_meta) \

445 ((struct bt\_audio\_codec\_cfg){ \

446 /\* Use HCI data path as default, can be overwritten by application \*/ \

447 .path\_id = BT\_ISO\_DATA\_PATH\_HCI, \

448 .ctlr\_transcode = false, \

449 .id = \_id, \

450 .cid = \_cid, \

451 .vid = \_vid, \

452 .data\_len = sizeof((uint8\_t[])\_data), \

453 .data = \_data, \

454 .meta\_len = sizeof((uint8\_t[])\_meta), \

455 .meta = \_meta, \

456 })

457

[ 467](group__bt__audio.md#ga6b99f589f6cdcd9e48a83f729a7a4698)#define BT\_AUDIO\_CODEC\_CAP(\_id, \_cid, \_vid, \_data, \_meta) \

468 ((struct bt\_audio\_codec\_cap){ \

469 /\* Use HCI data path as default, can be overwritten by application \*/ \

470 .path\_id = BT\_ISO\_DATA\_PATH\_HCI, \

471 .ctlr\_transcode = false, \

472 .id = (\_id), \

473 .cid = (\_cid), \

474 .vid = (\_vid), \

475 .data\_len = sizeof((uint8\_t[])\_data), \

476 .data = \_data, \

477 .meta\_len = sizeof((uint8\_t[])\_meta), \

478 .meta = \_meta, \

479 })

480

[ 485](group__bt__audio.md#ga61230848c02098352320fe751332c4e8)enum [bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8) {

[ 486](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a8f476de613cdcb2f9f677d40291aa5df) [BT\_AUDIO\_LOCATION\_MONO\_AUDIO](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a8f476de613cdcb2f9f677d40291aa5df) = 0,

[ 487](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ac658188fa6f1b4f248a149d0bde1e41b) [BT\_AUDIO\_LOCATION\_FRONT\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ac658188fa6f1b4f248a149d0bde1e41b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 488](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a26d5ba460642bcf7fb2fc950082b70b3) [BT\_AUDIO\_LOCATION\_FRONT\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a26d5ba460642bcf7fb2fc950082b70b3) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 489](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a06b34e67c9931f8b26562218cba51337) [BT\_AUDIO\_LOCATION\_FRONT\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a06b34e67c9931f8b26562218cba51337) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 490](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ac4c09f948266f2c9c65b3bc16da2f3f6) [BT\_AUDIO\_LOCATION\_LOW\_FREQ\_EFFECTS\_1](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ac4c09f948266f2c9c65b3bc16da2f3f6) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

[ 491](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a96906ff7918b0a3e3e7efe73a08d9896) [BT\_AUDIO\_LOCATION\_BACK\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a96906ff7918b0a3e3e7efe73a08d9896) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

[ 492](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a43f5070c2b4d39c38fa7900595d9b1aa) [BT\_AUDIO\_LOCATION\_BACK\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a43f5070c2b4d39c38fa7900595d9b1aa) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

[ 493](group__bt__audio.md#gga61230848c02098352320fe751332c4e8af02a9d46877b742e8730bbf3dd6ad22e) [BT\_AUDIO\_LOCATION\_FRONT\_LEFT\_OF\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8af02a9d46877b742e8730bbf3dd6ad22e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6),

[ 494](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a725707ae4703a1f9b970de5b1e4e5692) [BT\_AUDIO\_LOCATION\_FRONT\_RIGHT\_OF\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a725707ae4703a1f9b970de5b1e4e5692) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7),

[ 495](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ae22cd1e458d8ff503741bf48262c7983) [BT\_AUDIO\_LOCATION\_BACK\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ae22cd1e458d8ff503741bf48262c7983) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8),

[ 496](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a0c304bdd529ad66acb71001caa1b361b) [BT\_AUDIO\_LOCATION\_LOW\_FREQ\_EFFECTS\_2](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a0c304bdd529ad66acb71001caa1b361b) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9),

[ 497](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ab8e52c69b894e382f0f09cc370337064) [BT\_AUDIO\_LOCATION\_SIDE\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ab8e52c69b894e382f0f09cc370337064) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10),

[ 498](group__bt__audio.md#gga61230848c02098352320fe751332c4e8aa01ad94f71defd158d8cfe25936341cd) [BT\_AUDIO\_LOCATION\_SIDE\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8aa01ad94f71defd158d8cfe25936341cd) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11),

[ 499](group__bt__audio.md#gga61230848c02098352320fe751332c4e8aa093e6218e213eac5677766e01f5c1c9) [BT\_AUDIO\_LOCATION\_TOP\_FRONT\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8aa093e6218e213eac5677766e01f5c1c9) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12),

[ 500](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a60b154a216d8e029deac7305500eaf2d) [BT\_AUDIO\_LOCATION\_TOP\_FRONT\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a60b154a216d8e029deac7305500eaf2d) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13),

[ 501](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ac32ed6f456be2fb2d9af2c7b255f3a4e) [BT\_AUDIO\_LOCATION\_TOP\_FRONT\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ac32ed6f456be2fb2d9af2c7b255f3a4e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(14),

[ 502](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a555361fafade3bfb27dc713666757a1f) [BT\_AUDIO\_LOCATION\_TOP\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a555361fafade3bfb27dc713666757a1f) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(15),

[ 503](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a07e699c28bd847de3d85645dceb2ff06) [BT\_AUDIO\_LOCATION\_TOP\_BACK\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a07e699c28bd847de3d85645dceb2ff06) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(16),

[ 504](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a8e81b80f732b0037493712b4baa21a69) [BT\_AUDIO\_LOCATION\_TOP\_BACK\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a8e81b80f732b0037493712b4baa21a69) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(17),

[ 505](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ae846b2f4186b46d3690c71071c41c7d6) [BT\_AUDIO\_LOCATION\_TOP\_SIDE\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ae846b2f4186b46d3690c71071c41c7d6) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(18),

[ 506](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a1cf8dea66e42f75ca85ba55124829a59) [BT\_AUDIO\_LOCATION\_TOP\_SIDE\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a1cf8dea66e42f75ca85ba55124829a59) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(19),

[ 507](group__bt__audio.md#gga61230848c02098352320fe751332c4e8aebae1f0f2537a806672820fb74eba5dd) [BT\_AUDIO\_LOCATION\_TOP\_BACK\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8aebae1f0f2537a806672820fb74eba5dd) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(20),

[ 508](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ad0be8f720f03feb18a23e77f0eff6376) [BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ad0be8f720f03feb18a23e77f0eff6376) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(21),

[ 509](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ac1e355baee6ca0907356d72f0d4edb29) [BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ac1e355baee6ca0907356d72f0d4edb29) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(22),

[ 510](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a33d0f7c266f21fd086386f8c29ee31e8) [BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a33d0f7c266f21fd086386f8c29ee31e8) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(23),

[ 511](group__bt__audio.md#gga61230848c02098352320fe751332c4e8acba90183626ad85c21692b7edd87133d) [BT\_AUDIO\_LOCATION\_FRONT\_LEFT\_WIDE](group__bt__audio.md#gga61230848c02098352320fe751332c4e8acba90183626ad85c21692b7edd87133d) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(24),

[ 512](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a8649be1d5b7e8b312fc3374039cc0a71) [BT\_AUDIO\_LOCATION\_FRONT\_RIGHT\_WIDE](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a8649be1d5b7e8b312fc3374039cc0a71) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(25),

[ 513](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a568a581c0ad653177f5d148d04bef0b6) [BT\_AUDIO\_LOCATION\_LEFT\_SURROUND](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a568a581c0ad653177f5d148d04bef0b6) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(26),

[ 514](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a97954db823b6c6bed660ff2717600a5e) [BT\_AUDIO\_LOCATION\_RIGHT\_SURROUND](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a97954db823b6c6bed660ff2717600a5e) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(27),

515};

516

[ 520](group__bt__audio.md#ga90688f158fe999ed3aa9c759c8245fcc)#define BT\_AUDIO\_LOCATION\_ANY (BT\_AUDIO\_LOCATION\_FRONT\_LEFT | \

521 BT\_AUDIO\_LOCATION\_FRONT\_RIGHT | \

522 BT\_AUDIO\_LOCATION\_FRONT\_CENTER | \

523 BT\_AUDIO\_LOCATION\_LOW\_FREQ\_EFFECTS\_1 | \

524 BT\_AUDIO\_LOCATION\_BACK\_LEFT | \

525 BT\_AUDIO\_LOCATION\_BACK\_RIGHT | \

526 BT\_AUDIO\_LOCATION\_FRONT\_LEFT\_OF\_CENTER | \

527 BT\_AUDIO\_LOCATION\_FRONT\_RIGHT\_OF\_CENTER | \

528 BT\_AUDIO\_LOCATION\_BACK\_CENTER | \

529 BT\_AUDIO\_LOCATION\_LOW\_FREQ\_EFFECTS\_2 | \

530 BT\_AUDIO\_LOCATION\_SIDE\_LEFT | \

531 BT\_AUDIO\_LOCATION\_SIDE\_RIGHT | \

532 BT\_AUDIO\_LOCATION\_TOP\_FRONT\_LEFT | \

533 BT\_AUDIO\_LOCATION\_TOP\_FRONT\_RIGHT | \

534 BT\_AUDIO\_LOCATION\_TOP\_FRONT\_CENTER | \

535 BT\_AUDIO\_LOCATION\_TOP\_CENTER | \

536 BT\_AUDIO\_LOCATION\_TOP\_BACK\_LEFT | \

537 BT\_AUDIO\_LOCATION\_TOP\_BACK\_RIGHT | \

538 BT\_AUDIO\_LOCATION\_TOP\_SIDE\_LEFT | \

539 BT\_AUDIO\_LOCATION\_TOP\_SIDE\_RIGHT | \

540 BT\_AUDIO\_LOCATION\_TOP\_BACK\_CENTER | \

541 BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_CENTER | \

542 BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_LEFT | \

543 BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_RIGHT | \

544 BT\_AUDIO\_LOCATION\_FRONT\_LEFT\_WIDE | \

545 BT\_AUDIO\_LOCATION\_FRONT\_RIGHT\_WIDE | \

546 BT\_AUDIO\_LOCATION\_LEFT\_SURROUND | \

547 BT\_AUDIO\_LOCATION\_RIGHT\_SURROUND)

548

[ 550](structbt__audio__codec__cap.md)struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) {

[ 556](structbt__audio__codec__cap.md#a822a06f815091cc580ca2e5bbb3126f7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [path\_id](structbt__audio__codec__cap.md#a822a06f815091cc580ca2e5bbb3126f7);

[ 562](structbt__audio__codec__cap.md#a900a77db09e72de61d4ff652c6dbb10b) bool [ctlr\_transcode](structbt__audio__codec__cap.md#a900a77db09e72de61d4ff652c6dbb10b);

[ 564](structbt__audio__codec__cap.md#ae3892731e7ca05f3ec426c70f0d9e1a9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [id](structbt__audio__codec__cap.md#ae3892731e7ca05f3ec426c70f0d9e1a9);

[ 566](structbt__audio__codec__cap.md#a763222d12a87958a5ba806303f98829a) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [cid](structbt__audio__codec__cap.md#a763222d12a87958a5ba806303f98829a);

[ 568](structbt__audio__codec__cap.md#a3b91269e16a3d63b3128a527caa5e3ff) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [vid](structbt__audio__codec__cap.md#a3b91269e16a3d63b3128a527caa5e3ff);

569#if CONFIG\_BT\_AUDIO\_CODEC\_CAP\_MAX\_DATA\_SIZE > 0

571 size\_t data\_len;

573 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data[CONFIG\_BT\_AUDIO\_CODEC\_CAP\_MAX\_DATA\_SIZE];

574#endif /\* CONFIG\_BT\_AUDIO\_CODEC\_CAP\_MAX\_DATA\_SIZE > 0 \*/

575#if defined(CONFIG\_BT\_AUDIO\_CODEC\_CAP\_MAX\_METADATA\_SIZE)

577 size\_t meta\_len;

579 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) meta[CONFIG\_BT\_AUDIO\_CODEC\_CAP\_MAX\_METADATA\_SIZE];

580#endif /\* CONFIG\_BT\_AUDIO\_CODEC\_CAP\_MAX\_METADATA\_SIZE \*/

581};

582

[ 584](structbt__audio__codec__cfg.md)struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) {

[ 590](structbt__audio__codec__cfg.md#a9386056bb02908407c9e3aad48abbd87) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [path\_id](structbt__audio__codec__cfg.md#a9386056bb02908407c9e3aad48abbd87);

[ 596](structbt__audio__codec__cfg.md#a9e2c8081950a0830ffc270245ab308c1) bool [ctlr\_transcode](structbt__audio__codec__cfg.md#a9e2c8081950a0830ffc270245ab308c1);

[ 598](structbt__audio__codec__cfg.md#aa2f99ec31ff3eb9b7b738bc8a1170f20) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [id](structbt__audio__codec__cfg.md#aa2f99ec31ff3eb9b7b738bc8a1170f20);

[ 600](structbt__audio__codec__cfg.md#a664e21bcd6002b21d4b1b53d866db32d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [cid](structbt__audio__codec__cfg.md#a664e21bcd6002b21d4b1b53d866db32d);

[ 602](structbt__audio__codec__cfg.md#a2996ab3f6ae1cab09ff5e3329b42468e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [vid](structbt__audio__codec__cfg.md#a2996ab3f6ae1cab09ff5e3329b42468e);

603#if CONFIG\_BT\_AUDIO\_CODEC\_CFG\_MAX\_DATA\_SIZE > 0

605 size\_t data\_len;

607 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data[CONFIG\_BT\_AUDIO\_CODEC\_CFG\_MAX\_DATA\_SIZE];

608#endif /\* CONFIG\_BT\_AUDIO\_CODEC\_CFG\_MAX\_DATA\_SIZE > 0 \*/

609#if CONFIG\_BT\_AUDIO\_CODEC\_CFG\_MAX\_METADATA\_SIZE > 0

611 size\_t meta\_len;

613 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) meta[CONFIG\_BT\_AUDIO\_CODEC\_CFG\_MAX\_METADATA\_SIZE];

614#endif /\* CONFIG\_BT\_AUDIO\_CODEC\_CFG\_MAX\_METADATA\_SIZE > 0 \*/

615};

616

[ 631](group__bt__audio.md#gafd8574b16141162c95653f0aa2bf6ff7)int [bt\_audio\_data\_parse](group__bt__audio.md#gafd8574b16141162c95653f0aa2bf6ff7)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ltv[], size\_t size,

632 bool (\*func)(struct [bt\_data](structbt__data.md) \*data, void \*user\_data), void \*user\_data);

633

[ 635](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f)enum [bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f) {

[ 636](group__bt__audio.md#gga5bd899fb5e4d844058184913866e462fa2adba49daa32ac7b040c3294f047ceb8) [BT\_AUDIO\_DIR\_SINK](group__bt__audio.md#gga5bd899fb5e4d844058184913866e462fa2adba49daa32ac7b040c3294f047ceb8) = 0x01,

[ 637](group__bt__audio.md#gga5bd899fb5e4d844058184913866e462fa868695a31ebf95402a4bae2469f3aa6c) [BT\_AUDIO\_DIR\_SOURCE](group__bt__audio.md#gga5bd899fb5e4d844058184913866e462fa868695a31ebf95402a4bae2469f3aa6c) = 0x02,

638};

639

[ 651](group__bt__audio.md#ga13e5148d62cb364602f01c75a88b615b)#define BT\_AUDIO\_CODEC\_QOS(\_interval, \_framing, \_phy, \_sdu, \_rtn, \_latency, \_pd) \

652 ((struct bt\_audio\_codec\_qos){ \

653 .interval = \_interval, \

654 .framing = \_framing, \

655 .phy = \_phy, \

656 .sdu = \_sdu, \

657 .rtn = \_rtn, \

658 .latency = \_latency, \

659 .pd = \_pd, \

660 })

661

[ 663](group__bt__audio.md#ga8cb1832a3ee38b1a151b702c5dee00d9)enum [bt\_audio\_codec\_qos\_framing](group__bt__audio.md#ga8cb1832a3ee38b1a151b702c5dee00d9) {

[ 664](group__bt__audio.md#gga8cb1832a3ee38b1a151b702c5dee00d9a426ad2fe26f69d135beff6a367ef872f) [BT\_AUDIO\_CODEC\_QOS\_FRAMING\_UNFRAMED](group__bt__audio.md#gga8cb1832a3ee38b1a151b702c5dee00d9a426ad2fe26f69d135beff6a367ef872f) = 0x00,

[ 665](group__bt__audio.md#gga8cb1832a3ee38b1a151b702c5dee00d9af7a4a07da9089c3afb248d63e3a9297a) [BT\_AUDIO\_CODEC\_QOS\_FRAMING\_FRAMED](group__bt__audio.md#gga8cb1832a3ee38b1a151b702c5dee00d9af7a4a07da9089c3afb248d63e3a9297a) = 0x01,

666};

667

669enum {

[ 670](group__bt__audio.md#ggaa69a4789478a1a0aa93451d294de7ad0ab387760c001ea6c81e889de55e74d5d5) [BT\_AUDIO\_CODEC\_QOS\_1M](group__bt__audio.md#ggaa69a4789478a1a0aa93451d294de7ad0ab387760c001ea6c81e889de55e74d5d5) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 671](group__bt__audio.md#ggaa69a4789478a1a0aa93451d294de7ad0ac81306188ed29b8fa17aa2afa878f297) [BT\_AUDIO\_CODEC\_QOS\_2M](group__bt__audio.md#ggaa69a4789478a1a0aa93451d294de7ad0ac81306188ed29b8fa17aa2afa878f297) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 672](group__bt__audio.md#ggaa69a4789478a1a0aa93451d294de7ad0a9789c1b6b319370a3b98ab37b61a86e0) [BT\_AUDIO\_CODEC\_QOS\_CODED](group__bt__audio.md#ggaa69a4789478a1a0aa93451d294de7ad0a9789c1b6b319370a3b98ab37b61a86e0) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

673};

674

[ 684](group__bt__audio.md#gadfc744b32a0b40da9377bb3668004bc2)#define BT\_AUDIO\_CODEC\_QOS\_UNFRAMED(\_interval, \_sdu, \_rtn, \_latency, \_pd) \

685 BT\_AUDIO\_CODEC\_QOS(\_interval, BT\_AUDIO\_CODEC\_QOS\_FRAMING\_UNFRAMED, BT\_AUDIO\_CODEC\_QOS\_2M, \

686 \_sdu, \_rtn, \_latency, \_pd)

687

[ 697](group__bt__audio.md#gae2147bca922bf3effd072d67a6b5d635)#define BT\_AUDIO\_CODEC\_QOS\_FRAMED(\_interval, \_sdu, \_rtn, \_latency, \_pd) \

698 BT\_AUDIO\_CODEC\_QOS(\_interval, BT\_AUDIO\_CODEC\_QOS\_FRAMING\_FRAMED, BT\_AUDIO\_CODEC\_QOS\_2M, \

699 \_sdu, \_rtn, \_latency, \_pd)

700

[ 702](structbt__audio__codec__qos.md)struct [bt\_audio\_codec\_qos](structbt__audio__codec__qos.md) {

[ 704](structbt__audio__codec__qos.md#a8911b0b9db8e4de55b3c313e3ad7c502) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__audio__codec__qos.md#a8911b0b9db8e4de55b3c313e3ad7c502);

705

[ 707](structbt__audio__codec__qos.md#a4212bf93b65e0faa218a1e0d03ae0283) enum [bt\_audio\_codec\_qos\_framing](group__bt__audio.md#ga8cb1832a3ee38b1a151b702c5dee00d9) [framing](structbt__audio__codec__qos.md#a4212bf93b65e0faa218a1e0d03ae0283);

708

[ 710](structbt__audio__codec__qos.md#ab05af8d47df82d34921afdd557770dbd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rtn](structbt__audio__codec__qos.md#ab05af8d47df82d34921afdd557770dbd);

711

[ 713](structbt__audio__codec__qos.md#ae1a5adb80af9357fd6ee6532b0ba228e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [sdu](structbt__audio__codec__qos.md#ae1a5adb80af9357fd6ee6532b0ba228e);

714

715#if defined(CONFIG\_BT\_BAP\_BROADCAST\_SOURCE) || defined(CONFIG\_BT\_BAP\_UNICAST)

721 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) latency;

722#endif /\* CONFIG\_BT\_BAP\_BROADCAST\_SOURCE || CONFIG\_BT\_BAP\_UNICAST \*/

723

[ 725](structbt__audio__codec__qos.md#ad906dc06624b0f80701d7ee92d849152) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [interval](structbt__audio__codec__qos.md#ad906dc06624b0f80701d7ee92d849152);

726

[ 731](structbt__audio__codec__qos.md#a28d87b06785e016fe7e12a0504f3b419) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pd](structbt__audio__codec__qos.md#a28d87b06785e016fe7e12a0504f3b419);

732

733#if defined(CONFIG\_BT\_ISO\_TEST\_PARAMS)

741 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) max\_pdu;

742

747 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) burst\_number;

748

755 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_subevents;

756#endif /\* CONFIG\_BT\_ISO\_TEST\_PARAMS \*/

757};

758

[ 771](group__bt__audio.md#gac48a47e5177754c2e6812eee440e6d42)#define BT\_AUDIO\_CODEC\_QOS\_PREF(\_unframed\_supported, \_phy, \_rtn, \_latency, \_pd\_min, \_pd\_max, \

772 \_pref\_pd\_min, \_pref\_pd\_max) \

773 { \

774 .unframed\_supported = \_unframed\_supported, \

775 .phy = \_phy, \

776 .rtn = \_rtn, \

777 .latency = \_latency, \

778 .pd\_min = \_pd\_min, \

779 .pd\_max = \_pd\_max, \

780 .pref\_pd\_min = \_pref\_pd\_min, \

781 .pref\_pd\_max = \_pref\_pd\_max, \

782 }

783

[ 785](structbt__audio__codec__qos__pref.md)struct [bt\_audio\_codec\_qos\_pref](structbt__audio__codec__qos__pref.md) {

[ 791](structbt__audio__codec__qos__pref.md#a3bdb319d2aa401102fb9e54f92993e83) bool [unframed\_supported](structbt__audio__codec__qos__pref.md#a3bdb319d2aa401102fb9e54f92993e83);

792

[ 794](structbt__audio__codec__qos__pref.md#a36fc375290b8f76c7278a236942db692) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [phy](structbt__audio__codec__qos__pref.md#a36fc375290b8f76c7278a236942db692);

795

[ 797](structbt__audio__codec__qos__pref.md#abc2142ef5c8ad1744b829ae626a57e9d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rtn](structbt__audio__codec__qos__pref.md#abc2142ef5c8ad1744b829ae626a57e9d);

798

[ 800](structbt__audio__codec__qos__pref.md#a1d46cf0aa05cfb7c88446719e59e0011) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [latency](structbt__audio__codec__qos__pref.md#a1d46cf0aa05cfb7c88446719e59e0011);

801

[ 810](structbt__audio__codec__qos__pref.md#a7437273abb18ce93c15bb789eeeb65d3) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pd\_min](structbt__audio__codec__qos__pref.md#a7437273abb18ce93c15bb789eeeb65d3);

811

[ 820](structbt__audio__codec__qos__pref.md#ab07f2245bfed3a1400b6a1e6eaad2735) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pd\_max](structbt__audio__codec__qos__pref.md#ab07f2245bfed3a1400b6a1e6eaad2735);

821

[ 826](structbt__audio__codec__qos__pref.md#ab38a4b98b47ab773f91873b42c69ed71) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pref\_pd\_min](structbt__audio__codec__qos__pref.md#ab38a4b98b47ab773f91873b42c69ed71);

827

[ 832](structbt__audio__codec__qos__pref.md#a5486cacf6cd5016e9b44b69e3da67d6d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pref\_pd\_max](structbt__audio__codec__qos__pref.md#a5486cacf6cd5016e9b44b69e3da67d6d);

833};

834

843

[ 852](group__bt__audio__codec__cfg.md#ga2e557fe726a49dc99754da16f7cc60af)int [bt\_audio\_codec\_cfg\_freq\_to\_freq\_hz](group__bt__audio__codec__cfg.md#ga2e557fe726a49dc99754da16f7cc60af)(enum [bt\_audio\_codec\_cfg\_freq](group__bt__audio.md#ga8e99fb678cc011bb8c9f6e1858bae0d7) freq);

853

[ 862](group__bt__audio__codec__cfg.md#ga99ab4f6d2a18f2a9b4e3da47f63fc9e0)int [bt\_audio\_codec\_cfg\_freq\_hz\_to\_freq](group__bt__audio__codec__cfg.md#ga99ab4f6d2a18f2a9b4e3da47f63fc9e0)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) freq\_hz);

863

[ 873](group__bt__audio__codec__cfg.md#gad8525a57d35e3e34ea591f7e20e2512d)int [bt\_audio\_codec\_cfg\_get\_freq](group__bt__audio__codec__cfg.md#gad8525a57d35e3e34ea591f7e20e2512d)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg);

874

[ 885](group__bt__audio__codec__cfg.md#gac119989d5dcfa36becf4edd0ae7c6138)int [bt\_audio\_codec\_cfg\_set\_freq](group__bt__audio__codec__cfg.md#gac119989d5dcfa36becf4edd0ae7c6138)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

886 enum [bt\_audio\_codec\_cfg\_freq](group__bt__audio.md#ga8e99fb678cc011bb8c9f6e1858bae0d7) freq);

887

[ 896](group__bt__audio__codec__cfg.md#ga225e05df1f0d1efb709c972187901495)int [bt\_audio\_codec\_cfg\_frame\_dur\_to\_frame\_dur\_us](group__bt__audio__codec__cfg.md#ga225e05df1f0d1efb709c972187901495)(enum [bt\_audio\_codec\_cfg\_frame\_dur](group__bt__audio.md#ga83701b5eadfcbc9b84dc0b1a85ebeb74) frame\_dur);

897

[ 906](group__bt__audio__codec__cfg.md#ga0782a3d9254fb76b441c6c2492571556)int [bt\_audio\_codec\_cfg\_frame\_dur\_us\_to\_frame\_dur](group__bt__audio__codec__cfg.md#ga0782a3d9254fb76b441c6c2492571556)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) frame\_dur\_us);

907

[ 917](group__bt__audio__codec__cfg.md#ga2dd3afe41b22e989fb46614f89550007)int [bt\_audio\_codec\_cfg\_get\_frame\_dur](group__bt__audio__codec__cfg.md#ga2dd3afe41b22e989fb46614f89550007)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg);

918

[ 929](group__bt__audio__codec__cfg.md#ga7d8306f98cb00f06e68a1df417825f0d)int [bt\_audio\_codec\_cfg\_set\_frame\_dur](group__bt__audio__codec__cfg.md#ga7d8306f98cb00f06e68a1df417825f0d)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

930 enum [bt\_audio\_codec\_cfg\_frame\_dur](group__bt__audio.md#ga83701b5eadfcbc9b84dc0b1a85ebeb74) frame\_dur);

931

[ 948](group__bt__audio__codec__cfg.md#ga93949a1b06ed1cc306c455825ebd94bd)int [bt\_audio\_codec\_cfg\_get\_chan\_allocation](group__bt__audio__codec__cfg.md#ga93949a1b06ed1cc306c455825ebd94bd)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

949 enum [bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8) \*chan\_allocation);

950

[ 961](group__bt__audio__codec__cfg.md#gafbbcd69fac18ed0201a5e0156209b049)int [bt\_audio\_codec\_cfg\_set\_chan\_allocation](group__bt__audio__codec__cfg.md#gafbbcd69fac18ed0201a5e0156209b049)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

962 enum [bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8) chan\_allocation);

963

[ 982](group__bt__audio__codec__cfg.md#ga503be053422217502d6108b045791e02)int [bt\_audio\_codec\_cfg\_get\_octets\_per\_frame](group__bt__audio__codec__cfg.md#ga503be053422217502d6108b045791e02)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg);

983

[ 994](group__bt__audio__codec__cfg.md#ga866cdec28194056dc9e274d0436b45c2)int [bt\_audio\_codec\_cfg\_set\_octets\_per\_frame](group__bt__audio__codec__cfg.md#ga866cdec28194056dc9e274d0436b45c2)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

995 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) octets\_per\_frame);

996

[ 1018](group__bt__audio__codec__cfg.md#gadba0723f9d8a9546b659fba139051374)int [bt\_audio\_codec\_cfg\_get\_frame\_blocks\_per\_sdu](group__bt__audio__codec__cfg.md#gadba0723f9d8a9546b659fba139051374)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1019 bool fallback\_to\_default);

1020

[ 1031](group__bt__audio__codec__cfg.md#gac9cf20bafbe24b34034bfb6ee7aaf03e)int [bt\_audio\_codec\_cfg\_set\_frame\_blocks\_per\_sdu](group__bt__audio__codec__cfg.md#gac9cf20bafbe24b34034bfb6ee7aaf03e)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1032 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) frame\_blocks);

1033

[ 1044](group__bt__audio__codec__cfg.md#ga707c679db0193197b56acabfb08f8d1f)int [bt\_audio\_codec\_cfg\_get\_val](group__bt__audio__codec__cfg.md#ga707c679db0193197b56acabfb08f8d1f)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1045 enum [bt\_audio\_codec\_cfg\_type](group__bt__audio.md#ga9230ec4d7518bd243207ba2decb1a974) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*data);

1046

[ 1059](group__bt__audio__codec__cfg.md#gab10f22938780530b1d1b95695382902e)int [bt\_audio\_codec\_cfg\_set\_val](group__bt__audio__codec__cfg.md#gab10f22938780530b1d1b95695382902e)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1060 enum [bt\_audio\_codec\_cfg\_type](group__bt__audio.md#ga9230ec4d7518bd243207ba2decb1a974) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data,

1061 size\_t data\_len);

1062

[ 1074](group__bt__audio__codec__cfg.md#gad3857d0ca008854df5966501caa261ba)int [bt\_audio\_codec\_cfg\_unset\_val](group__bt__audio__codec__cfg.md#gad3857d0ca008854df5966501caa261ba)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1075 enum [bt\_audio\_codec\_cfg\_type](group__bt__audio.md#ga9230ec4d7518bd243207ba2decb1a974) type);

1076

[ 1088](group__bt__audio__codec__cfg.md#gae98335e87394a491b4a311d867a5e32d)int [bt\_audio\_codec\_cfg\_meta\_get\_val](group__bt__audio__codec__cfg.md#gae98335e87394a491b4a311d867a5e32d)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type,

1089 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*data);

1090

[ 1103](group__bt__audio__codec__cfg.md#ga3e24c2ba8de502600e647cb2f84e3ec4)int [bt\_audio\_codec\_cfg\_meta\_set\_val](group__bt__audio__codec__cfg.md#ga3e24c2ba8de502600e647cb2f84e3ec4)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1104 enum [bt\_audio\_metadata\_type](group__bt__audio.md#gab53d0dd62bceff97cf8eed7d8cf80354) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data,

1105 size\_t data\_len);

1106

[ 1118](group__bt__audio__codec__cfg.md#gab46f830daa1d9a907f47eb2a9eed7337)int [bt\_audio\_codec\_cfg\_meta\_unset\_val](group__bt__audio__codec__cfg.md#gab46f830daa1d9a907f47eb2a9eed7337)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1119 enum [bt\_audio\_metadata\_type](group__bt__audio.md#gab53d0dd62bceff97cf8eed7d8cf80354) type);

[ 1131](group__bt__audio__codec__cfg.md#ga5231504357bf52dda1912d3f065cc681)int [bt\_audio\_codec\_cfg\_meta\_get\_pref\_context](group__bt__audio__codec__cfg.md#ga5231504357bf52dda1912d3f065cc681)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg);

1132

[ 1143](group__bt__audio__codec__cfg.md#gab40bad609f17d24e7e0e9ffcebe4e912)int [bt\_audio\_codec\_cfg\_meta\_set\_pref\_context](group__bt__audio__codec__cfg.md#gab40bad609f17d24e7e0e9ffcebe4e912)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1144 enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) ctx);

1145

[ 1157](group__bt__audio__codec__cfg.md#ga4cc4e1bb941206e7f1541a57fc92b8e9)int [bt\_audio\_codec\_cfg\_meta\_get\_stream\_context](group__bt__audio__codec__cfg.md#ga4cc4e1bb941206e7f1541a57fc92b8e9)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg);

1158

[ 1169](group__bt__audio__codec__cfg.md#ga5cd2af1bb44c6eb5bafe824f005a77f0)int [bt\_audio\_codec\_cfg\_meta\_set\_stream\_context](group__bt__audio__codec__cfg.md#ga5cd2af1bb44c6eb5bafe824f005a77f0)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1170 enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) ctx);

1171

[ 1183](group__bt__audio__codec__cfg.md#ga03284b8474d65443d7ecc8bdfc6f04c6)int [bt\_audio\_codec\_cfg\_meta\_get\_program\_info](group__bt__audio__codec__cfg.md#ga03284b8474d65443d7ecc8bdfc6f04c6)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1184 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*program\_info);

1185

[ 1197](group__bt__audio__codec__cfg.md#ga2ca9e616d20d7513c60ce905f046ac7b)int [bt\_audio\_codec\_cfg\_meta\_set\_program\_info](group__bt__audio__codec__cfg.md#ga2ca9e616d20d7513c60ce905f046ac7b)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1198 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*program\_info, size\_t program\_info\_len);

1199

[ 1211](group__bt__audio__codec__cfg.md#ga18b76dba57879b16b24f23b5b62a425c)int [bt\_audio\_codec\_cfg\_meta\_get\_stream\_lang](group__bt__audio__codec__cfg.md#ga18b76dba57879b16b24f23b5b62a425c)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg);

1212

[ 1223](group__bt__audio__codec__cfg.md#gae2beb0c754a4956f04127aa353bb0949)int [bt\_audio\_codec\_cfg\_meta\_set\_stream\_lang](group__bt__audio__codec__cfg.md#gae2beb0c754a4956f04127aa353bb0949)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1224 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) stream\_lang);

1225

[ 1237](group__bt__audio__codec__cfg.md#gaa0f9b9f608c7af881d5a928a3ae397b2)int [bt\_audio\_codec\_cfg\_meta\_get\_ccid\_list](group__bt__audio__codec__cfg.md#gaa0f9b9f608c7af881d5a928a3ae397b2)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1238 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*ccid\_list);

1239

[ 1251](group__bt__audio__codec__cfg.md#ga59716b95fcea3404ff8c078564b0e29c)int [bt\_audio\_codec\_cfg\_meta\_set\_ccid\_list](group__bt__audio__codec__cfg.md#ga59716b95fcea3404ff8c078564b0e29c)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1252 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*ccid\_list, size\_t ccid\_list\_len);

1253

[ 1265](group__bt__audio__codec__cfg.md#gaf0eecb02a05f0cc2b75ae9fb32c03913)int [bt\_audio\_codec\_cfg\_meta\_get\_parental\_rating](group__bt__audio__codec__cfg.md#gaf0eecb02a05f0cc2b75ae9fb32c03913)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg);

1266

[ 1277](group__bt__audio__codec__cfg.md#gab5d8b5877de4fe16c0e06a1d4f0d15ce)int [bt\_audio\_codec\_cfg\_meta\_set\_parental\_rating](group__bt__audio__codec__cfg.md#gab5d8b5877de4fe16c0e06a1d4f0d15ce)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1278 enum [bt\_audio\_parental\_rating](group__bt__audio.md#ga6d4aff1f93dc0b902e4b5d1355f15760) parental\_rating);

1279

[ 1291](group__bt__audio__codec__cfg.md#ga6bdbc0a0b929fdbdc75db479aec858df)int [bt\_audio\_codec\_cfg\_meta\_get\_program\_info\_uri](group__bt__audio__codec__cfg.md#ga6bdbc0a0b929fdbdc75db479aec858df)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1292 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*program\_info\_uri);

1293

[ 1305](group__bt__audio__codec__cfg.md#ga99163729034e816eaef7195505d5ae20)int [bt\_audio\_codec\_cfg\_meta\_set\_program\_info\_uri](group__bt__audio__codec__cfg.md#ga99163729034e816eaef7195505d5ae20)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1306 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*program\_info\_uri,

1307 size\_t program\_info\_uri\_len);

1308

[ 1320](group__bt__audio__codec__cfg.md#ga0fd6e6baf1b4f22d60768aaed6f42e8e)int [bt\_audio\_codec\_cfg\_meta\_get\_audio\_active\_state](group__bt__audio__codec__cfg.md#ga0fd6e6baf1b4f22d60768aaed6f42e8e)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg);

1321

[ 1332](group__bt__audio__codec__cfg.md#gaf869e7ce0c9dd467fb03e8503d36c58a)int [bt\_audio\_codec\_cfg\_meta\_set\_audio\_active\_state](group__bt__audio__codec__cfg.md#gaf869e7ce0c9dd467fb03e8503d36c58a)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1333 enum [bt\_audio\_active\_state](group__bt__audio.md#ga16d403ec4db7be997682331ad365ff5f) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

1334

[ 1345](group__bt__audio__codec__cfg.md#ga66143aa7dcc726e06a12660b8f90fc5a)int [bt\_audio\_codec\_cfg\_meta\_get\_bcast\_audio\_immediate\_rend\_flag](group__bt__audio__codec__cfg.md#ga66143aa7dcc726e06a12660b8f90fc5a)(

1346 const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg);

1347

[ 1357](group__bt__audio__codec__cfg.md#gaede61b65d2037c7fbf6c4c4e090990be)int [bt\_audio\_codec\_cfg\_meta\_set\_bcast\_audio\_immediate\_rend\_flag](group__bt__audio__codec__cfg.md#gaede61b65d2037c7fbf6c4c4e090990be)(

1358 struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg);

1359

[ 1371](group__bt__audio__codec__cfg.md#ga1f76f82bff63b876eb761a0bf0377428)int [bt\_audio\_codec\_cfg\_meta\_get\_extended](group__bt__audio__codec__cfg.md#ga1f76f82bff63b876eb761a0bf0377428)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1372 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*extended\_meta);

1373

[ 1385](group__bt__audio__codec__cfg.md#gade9cb53287ab3356fb57ba8a454a3aad)int [bt\_audio\_codec\_cfg\_meta\_set\_extended](group__bt__audio__codec__cfg.md#gade9cb53287ab3356fb57ba8a454a3aad)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1386 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*extended\_meta, size\_t extended\_meta\_len);

1387

[ 1399](group__bt__audio__codec__cfg.md#ga4a4982e3bd0e8c944b584196ef146f6c)int [bt\_audio\_codec\_cfg\_meta\_get\_vendor](group__bt__audio__codec__cfg.md#ga4a4982e3bd0e8c944b584196ef146f6c)(const struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1400 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*vendor\_meta);

1401

[ 1413](group__bt__audio__codec__cfg.md#ga6935d1c40b3178b0c8fa877ee93d1e53)int [bt\_audio\_codec\_cfg\_meta\_set\_vendor](group__bt__audio__codec__cfg.md#ga6935d1c40b3178b0c8fa877ee93d1e53)(struct [bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md) \*codec\_cfg,

1414 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*vendor\_meta, size\_t vendor\_meta\_len); /\* End of bt\_audio\_codec\_cfg \*/

1416

1426

[ 1438](group__bt__audio__codec__cap.md#gac3bf5dd414271bb1dcbc6590994cff6b)int [bt\_audio\_codec\_cap\_get\_val](group__bt__audio__codec__cap.md#gac3bf5dd414271bb1dcbc6590994cff6b)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1439 enum [bt\_audio\_codec\_cap\_type](group__bt__audio.md#gaf58823a56eb36cfd22e582ab1ea3d015) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*data);

1440

[ 1453](group__bt__audio__codec__cap.md#ga0c2c816b0b2b85aa5dd38f21caceea40)int [bt\_audio\_codec\_cap\_set\_val](group__bt__audio__codec__cap.md#ga0c2c816b0b2b85aa5dd38f21caceea40)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1454 enum [bt\_audio\_codec\_cap\_type](group__bt__audio.md#gaf58823a56eb36cfd22e582ab1ea3d015) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data,

1455 size\_t data\_len);

1456

[ 1468](group__bt__audio__codec__cap.md#gabc9962212ad65339ff02ba1389d5f9f8)int [bt\_audio\_codec\_cap\_unset\_val](group__bt__audio__codec__cap.md#gabc9962212ad65339ff02ba1389d5f9f8)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1469 enum [bt\_audio\_codec\_cap\_type](group__bt__audio.md#gaf58823a56eb36cfd22e582ab1ea3d015) type);

1470

[ 1481](group__bt__audio__codec__cap.md#gaa1dbf81c437c983af0144bf62433666c)int [bt\_audio\_codec\_cap\_get\_freq](group__bt__audio__codec__cap.md#gaa1dbf81c437c983af0144bf62433666c)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap);

1482

[ 1493](group__bt__audio__codec__cap.md#gac0655c0bd6552ab8a265076d7d0cd1b2)int [bt\_audio\_codec\_cap\_set\_freq](group__bt__audio__codec__cap.md#gac0655c0bd6552ab8a265076d7d0cd1b2)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1494 enum [bt\_audio\_codec\_cap\_freq](group__bt__audio.md#gaafc1106d5d305874ee2f540c850ff5b4) freq);

1495

[ 1506](group__bt__audio__codec__cap.md#ga12336de7d908bda94427caee4dc080e0)int [bt\_audio\_codec\_cap\_get\_frame\_dur](group__bt__audio__codec__cap.md#ga12336de7d908bda94427caee4dc080e0)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap);

1507

[ 1518](group__bt__audio__codec__cap.md#ga53e5df6cc4cfbed12b59a6a506657772)int [bt\_audio\_codec\_cap\_set\_frame\_dur](group__bt__audio__codec__cap.md#ga53e5df6cc4cfbed12b59a6a506657772)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1519 enum [bt\_audio\_codec\_cap\_frame\_dur](group__bt__audio.md#gaf37e8e19f956afb3c3a413cbaa1a21f5) frame\_dur);

1520

[ 1531](group__bt__audio__codec__cap.md#ga7a4b34dced3c5d7e11a20611bf4dee28)int [bt\_audio\_codec\_cap\_get\_supported\_audio\_chan\_counts](group__bt__audio__codec__cap.md#ga7a4b34dced3c5d7e11a20611bf4dee28)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap);

1532

[ 1543](group__bt__audio__codec__cap.md#gaf6b2717823f9f3136237ed6a6515449e)int [bt\_audio\_codec\_cap\_set\_supported\_audio\_chan\_counts](group__bt__audio__codec__cap.md#gaf6b2717823f9f3136237ed6a6515449e)(

1544 struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, enum [bt\_audio\_codec\_cap\_chan\_count](group__bt__audio.md#gae695b5d17359967703f2509db1671fa5) chan\_count);

1545

[ 1557](group__bt__audio__codec__cap.md#gaa949089f2c6c143041e6cb61338e0ddc)int [bt\_audio\_codec\_cap\_get\_octets\_per\_frame](group__bt__audio__codec__cap.md#gaa949089f2c6c143041e6cb61338e0ddc)(

1558 const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1559 struct [bt\_audio\_codec\_octets\_per\_codec\_frame](structbt__audio__codec__octets__per__codec__frame.md) \*codec\_frame);

1560

[ 1571](group__bt__audio__codec__cap.md#gac1c42460cd3c55bbfbd467f84ab2d78d)int [bt\_audio\_codec\_cap\_set\_octets\_per\_frame](group__bt__audio__codec__cap.md#gac1c42460cd3c55bbfbd467f84ab2d78d)(

1572 struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1573 const struct [bt\_audio\_codec\_octets\_per\_codec\_frame](structbt__audio__codec__octets__per__codec__frame.md) \*codec\_frame);

1574

[ 1585](group__bt__audio__codec__cap.md#ga4904184e69994ebb4c5f8a39150fcaa1)int [bt\_audio\_codec\_cap\_get\_max\_codec\_frames\_per\_sdu](group__bt__audio__codec__cap.md#ga4904184e69994ebb4c5f8a39150fcaa1)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap);

1586

[ 1597](group__bt__audio__codec__cap.md#ga3785bc41f56f8f2a09248396dadb31da)int [bt\_audio\_codec\_cap\_set\_max\_codec\_frames\_per\_sdu](group__bt__audio__codec__cap.md#ga3785bc41f56f8f2a09248396dadb31da)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1598 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) codec\_frames\_per\_sdu);

1599

[ 1610](group__bt__audio__codec__cap.md#ga5c2ecbb4d0cef26dd2cc5d023e70a163)int [bt\_audio\_codec\_cap\_meta\_get\_val](group__bt__audio__codec__cap.md#ga5c2ecbb4d0cef26dd2cc5d023e70a163)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type,

1611 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*data);

1612

[ 1625](group__bt__audio__codec__cap.md#ga1fdfd8c36f4131bcf4ffd2b7f176b631)int [bt\_audio\_codec\_cap\_meta\_set\_val](group__bt__audio__codec__cap.md#ga1fdfd8c36f4131bcf4ffd2b7f176b631)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1626 enum [bt\_audio\_metadata\_type](group__bt__audio.md#gab53d0dd62bceff97cf8eed7d8cf80354) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data,

1627 size\_t data\_len);

1628

[ 1640](group__bt__audio__codec__cap.md#ga40848f5375d1e58622c580112c282f2e)int [bt\_audio\_codec\_cap\_meta\_unset\_val](group__bt__audio__codec__cap.md#ga40848f5375d1e58622c580112c282f2e)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1641 enum [bt\_audio\_metadata\_type](group__bt__audio.md#gab53d0dd62bceff97cf8eed7d8cf80354) type);

1642

[ 1654](group__bt__audio__codec__cap.md#gaaa8c6783241b1b70349354b3e36c696c)int [bt\_audio\_codec\_cap\_meta\_get\_pref\_context](group__bt__audio__codec__cap.md#gaaa8c6783241b1b70349354b3e36c696c)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap);

1655

[ 1666](group__bt__audio__codec__cap.md#ga7fe0d4553d6accf5c89645cbf86149bf)int [bt\_audio\_codec\_cap\_meta\_set\_pref\_context](group__bt__audio__codec__cap.md#ga7fe0d4553d6accf5c89645cbf86149bf)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1667 enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) ctx);

1668

[ 1680](group__bt__audio__codec__cap.md#ga88ee657b5bd3f847bb75c9620ddb142f)int [bt\_audio\_codec\_cap\_meta\_get\_stream\_context](group__bt__audio__codec__cap.md#ga88ee657b5bd3f847bb75c9620ddb142f)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap);

1681

[ 1692](group__bt__audio__codec__cap.md#ga5cc7f360049c38c8de631ea33dbc44ab)int [bt\_audio\_codec\_cap\_meta\_set\_stream\_context](group__bt__audio__codec__cap.md#ga5cc7f360049c38c8de631ea33dbc44ab)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1693 enum [bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3) ctx);

1694

[ 1706](group__bt__audio__codec__cap.md#ga33725c3b2c06d6c22030bb5a77d702b0)int [bt\_audio\_codec\_cap\_meta\_get\_program\_info](group__bt__audio__codec__cap.md#ga33725c3b2c06d6c22030bb5a77d702b0)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1707 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*program\_info);

1708

[ 1720](group__bt__audio__codec__cap.md#ga43d2ec3a4d621c26843de82db7fd2189)int [bt\_audio\_codec\_cap\_meta\_set\_program\_info](group__bt__audio__codec__cap.md#ga43d2ec3a4d621c26843de82db7fd2189)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1721 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*program\_info, size\_t program\_info\_len);

1722

[ 1734](group__bt__audio__codec__cap.md#gac78eba1117ba8ef0c2bb02c10c09b363)int [bt\_audio\_codec\_cap\_meta\_get\_stream\_lang](group__bt__audio__codec__cap.md#gac78eba1117ba8ef0c2bb02c10c09b363)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap);

1735

[ 1746](group__bt__audio__codec__cap.md#ga56ee81c8a9e0eaedb04a7b732d4b7a36)int [bt\_audio\_codec\_cap\_meta\_set\_stream\_lang](group__bt__audio__codec__cap.md#ga56ee81c8a9e0eaedb04a7b732d4b7a36)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1747 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) stream\_lang);

1748

[ 1760](group__bt__audio__codec__cap.md#ga3095dea36e60e75cbfe786d3c2f11866)int [bt\_audio\_codec\_cap\_meta\_get\_ccid\_list](group__bt__audio__codec__cap.md#ga3095dea36e60e75cbfe786d3c2f11866)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1761 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*ccid\_list);

1762

[ 1774](group__bt__audio__codec__cap.md#ga00a8ad22713dab761c81d1b8481c037d)int [bt\_audio\_codec\_cap\_meta\_set\_ccid\_list](group__bt__audio__codec__cap.md#ga00a8ad22713dab761c81d1b8481c037d)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1775 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*ccid\_list, size\_t ccid\_list\_len);

1776

[ 1788](group__bt__audio__codec__cap.md#gab34d0369ce08efcd407d33956d32632e)int [bt\_audio\_codec\_cap\_meta\_get\_parental\_rating](group__bt__audio__codec__cap.md#gab34d0369ce08efcd407d33956d32632e)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap);

1789

[ 1800](group__bt__audio__codec__cap.md#ga5e267dfad978cd3d52be9c31a4fac0be)int [bt\_audio\_codec\_cap\_meta\_set\_parental\_rating](group__bt__audio__codec__cap.md#ga5e267dfad978cd3d52be9c31a4fac0be)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1801 enum [bt\_audio\_parental\_rating](group__bt__audio.md#ga6d4aff1f93dc0b902e4b5d1355f15760) parental\_rating);

1802

[ 1814](group__bt__audio__codec__cap.md#gadb39b0ee1f65cdd2457fdf2c3142c040)int [bt\_audio\_codec\_cap\_meta\_get\_program\_info\_uri](group__bt__audio__codec__cap.md#gadb39b0ee1f65cdd2457fdf2c3142c040)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1815 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*program\_info\_uri);

1816

[ 1828](group__bt__audio__codec__cap.md#gafbb0d6282d989e8bc70caada2845b337)int [bt\_audio\_codec\_cap\_meta\_set\_program\_info\_uri](group__bt__audio__codec__cap.md#gafbb0d6282d989e8bc70caada2845b337)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1829 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*program\_info\_uri,

1830 size\_t program\_info\_uri\_len);

1831

[ 1843](group__bt__audio__codec__cap.md#ga88bb1da63b7ea0f95dd236aa1024cfb8)int [bt\_audio\_codec\_cap\_meta\_get\_audio\_active\_state](group__bt__audio__codec__cap.md#ga88bb1da63b7ea0f95dd236aa1024cfb8)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap);

1844

[ 1855](group__bt__audio__codec__cap.md#gacd3de0306a22d1a1d9ba09b4ac4f4e09)int [bt\_audio\_codec\_cap\_meta\_set\_audio\_active\_state](group__bt__audio__codec__cap.md#gacd3de0306a22d1a1d9ba09b4ac4f4e09)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1856 enum [bt\_audio\_active\_state](group__bt__audio.md#ga16d403ec4db7be997682331ad365ff5f) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

1857

[ 1868](group__bt__audio__codec__cap.md#gab4ccc7cb7d779acb20185ae808dd8bbe)int [bt\_audio\_codec\_cap\_meta\_get\_bcast\_audio\_immediate\_rend\_flag](group__bt__audio__codec__cap.md#gab4ccc7cb7d779acb20185ae808dd8bbe)(

1869 const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap);

1870

[ 1880](group__bt__audio__codec__cap.md#gaa1d382b4fa53f7cbe8426df53a3317ce)int [bt\_audio\_codec\_cap\_meta\_set\_bcast\_audio\_immediate\_rend\_flag](group__bt__audio__codec__cap.md#gaa1d382b4fa53f7cbe8426df53a3317ce)(

1881 struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap);

1882

[ 1894](group__bt__audio__codec__cap.md#ga69aecd7e98f90a5162ff8ea3373b43d4)int [bt\_audio\_codec\_cap\_meta\_get\_extended](group__bt__audio__codec__cap.md#ga69aecd7e98f90a5162ff8ea3373b43d4)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1895 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*extended\_meta);

1896

[ 1908](group__bt__audio__codec__cap.md#gac00aabc7329027852a7caf5cdff2bc26)int [bt\_audio\_codec\_cap\_meta\_set\_extended](group__bt__audio__codec__cap.md#gac00aabc7329027852a7caf5cdff2bc26)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1909 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*extended\_meta, size\_t extended\_meta\_len);

1910

[ 1922](group__bt__audio__codec__cap.md#gab8c80a0f55041f026d453fd88cdeb727)int [bt\_audio\_codec\_cap\_meta\_get\_vendor](group__bt__audio__codec__cap.md#gab8c80a0f55041f026d453fd88cdeb727)(const struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1923 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*vendor\_meta);

1924

[ 1936](group__bt__audio__codec__cap.md#ga1f06789782541beab9aab4914f91bb57)int [bt\_audio\_codec\_cap\_meta\_set\_vendor](group__bt__audio__codec__cap.md#ga1f06789782541beab9aab4914f91bb57)(struct [bt\_audio\_codec\_cap](structbt__audio__codec__cap.md) \*codec\_cap,

1937 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*vendor\_meta, size\_t vendor\_meta\_len);

1938 /\* End of bt\_audio\_codec\_cap \*/

1940

1941#ifdef \_\_cplusplus

1942}

1943#endif

1944 /\* end of bt\_audio \*/

1946

1947#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_AUDIO\_H\_ \*/

[atomic.h](atomic_8h.md)

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

[bt\_audio\_codec\_cap\_get\_max\_codec\_frames\_per\_sdu](group__bt__audio__codec__cap.md#ga4904184e69994ebb4c5f8a39150fcaa1)

int bt\_audio\_codec\_cap\_get\_max\_codec\_frames\_per\_sdu(const struct bt\_audio\_codec\_cap \*codec\_cap)

Extract the maximum codec frames per SDU from a codec capability.

[bt\_audio\_codec\_cap\_set\_frame\_dur](group__bt__audio__codec__cap.md#ga53e5df6cc4cfbed12b59a6a506657772)

int bt\_audio\_codec\_cap\_set\_frame\_dur(struct bt\_audio\_codec\_cap \*codec\_cap, enum bt\_audio\_codec\_cap\_frame\_dur frame\_dur)

Set the frame duration of a codec capability.

[bt\_audio\_codec\_cap\_meta\_set\_stream\_lang](group__bt__audio__codec__cap.md#ga56ee81c8a9e0eaedb04a7b732d4b7a36)

int bt\_audio\_codec\_cap\_meta\_set\_stream\_lang(struct bt\_audio\_codec\_cap \*codec\_cap, uint32\_t stream\_lang)

Set the stream language of a codec capability metadata.

[bt\_audio\_codec\_cap\_meta\_get\_val](group__bt__audio__codec__cap.md#ga5c2ecbb4d0cef26dd2cc5d023e70a163)

int bt\_audio\_codec\_cap\_meta\_get\_val(const struct bt\_audio\_codec\_cap \*codec\_cap, uint8\_t type, const uint8\_t \*\*data)

Lookup a specific metadata value based on type.

[bt\_audio\_codec\_cap\_meta\_set\_stream\_context](group__bt__audio__codec__cap.md#ga5cc7f360049c38c8de631ea33dbc44ab)

int bt\_audio\_codec\_cap\_meta\_set\_stream\_context(struct bt\_audio\_codec\_cap \*codec\_cap, enum bt\_audio\_context ctx)

Set the stream context of a codec capability metadata.

[bt\_audio\_codec\_cap\_meta\_set\_parental\_rating](group__bt__audio__codec__cap.md#ga5e267dfad978cd3d52be9c31a4fac0be)

int bt\_audio\_codec\_cap\_meta\_set\_parental\_rating(struct bt\_audio\_codec\_cap \*codec\_cap, enum bt\_audio\_parental\_rating parental\_rating)

Set the parental rating of a codec capability metadata.

[bt\_audio\_codec\_cap\_meta\_get\_extended](group__bt__audio__codec__cap.md#ga69aecd7e98f90a5162ff8ea3373b43d4)

int bt\_audio\_codec\_cap\_meta\_get\_extended(const struct bt\_audio\_codec\_cap \*codec\_cap, const uint8\_t \*\*extended\_meta)

Extract extended metadata.

[bt\_audio\_codec\_cap\_get\_supported\_audio\_chan\_counts](group__bt__audio__codec__cap.md#ga7a4b34dced3c5d7e11a20611bf4dee28)

int bt\_audio\_codec\_cap\_get\_supported\_audio\_chan\_counts(const struct bt\_audio\_codec\_cap \*codec\_cap)

Extract the frequency from a codec capability.

[bt\_audio\_codec\_cap\_meta\_set\_pref\_context](group__bt__audio__codec__cap.md#ga7fe0d4553d6accf5c89645cbf86149bf)

int bt\_audio\_codec\_cap\_meta\_set\_pref\_context(struct bt\_audio\_codec\_cap \*codec\_cap, enum bt\_audio\_context ctx)

Set the preferred context of a codec capability metadata.

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

[bt\_audio\_codec\_cap\_meta\_get\_stream\_lang](group__bt__audio__codec__cap.md#gac78eba1117ba8ef0c2bb02c10c09b363)

int bt\_audio\_codec\_cap\_meta\_get\_stream\_lang(const struct bt\_audio\_codec\_cap \*codec\_cap)

Extract stream language.

[bt\_audio\_codec\_cap\_meta\_set\_audio\_active\_state](group__bt__audio__codec__cap.md#gacd3de0306a22d1a1d9ba09b4ac4f4e09)

int bt\_audio\_codec\_cap\_meta\_set\_audio\_active\_state(struct bt\_audio\_codec\_cap \*codec\_cap, enum bt\_audio\_active\_state state)

Set the audio active state of a codec capability metadata.

[bt\_audio\_codec\_cap\_meta\_get\_program\_info\_uri](group__bt__audio__codec__cap.md#gadb39b0ee1f65cdd2457fdf2c3142c040)

int bt\_audio\_codec\_cap\_meta\_get\_program\_info\_uri(const struct bt\_audio\_codec\_cap \*codec\_cap, const uint8\_t \*\*program\_info\_uri)

Extract program info URI.

[bt\_audio\_codec\_cap\_set\_supported\_audio\_chan\_counts](group__bt__audio__codec__cap.md#gaf6b2717823f9f3136237ed6a6515449e)

int bt\_audio\_codec\_cap\_set\_supported\_audio\_chan\_counts(struct bt\_audio\_codec\_cap \*codec\_cap, enum bt\_audio\_codec\_cap\_chan\_count chan\_count)

Set the channel count of a codec capability.

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

[bt\_audio\_codec\_cfg\_meta\_get\_stream\_lang](group__bt__audio__codec__cfg.md#ga18b76dba57879b16b24f23b5b62a425c)

int bt\_audio\_codec\_cfg\_meta\_get\_stream\_lang(const struct bt\_audio\_codec\_cfg \*codec\_cfg)

Extract stream language.

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

[bt\_audio\_codec\_cfg\_meta\_get\_pref\_context](group__bt__audio__codec__cfg.md#ga5231504357bf52dda1912d3f065cc681)

int bt\_audio\_codec\_cfg\_meta\_get\_pref\_context(const struct bt\_audio\_codec\_cfg \*codec\_cfg)

Extract preferred contexts.

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

[bt\_audio\_codec\_cfg\_get\_chan\_allocation](group__bt__audio__codec__cfg.md#ga93949a1b06ed1cc306c455825ebd94bd)

int bt\_audio\_codec\_cfg\_get\_chan\_allocation(const struct bt\_audio\_codec\_cfg \*codec\_cfg, enum bt\_audio\_location \*chan\_allocation)

Extract channel allocation from BT codec config.

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

Extract number of audio frame blockss in each SDU from BT codec config.

[bt\_audio\_codec\_cfg\_meta\_set\_extended](group__bt__audio__codec__cfg.md#gade9cb53287ab3356fb57ba8a454a3aad)

int bt\_audio\_codec\_cfg\_meta\_set\_extended(struct bt\_audio\_codec\_cfg \*codec\_cfg, const uint8\_t \*extended\_meta, size\_t extended\_meta\_len)

Set the extended metadata of a codec configuration metadata.

[bt\_audio\_codec\_cfg\_meta\_set\_stream\_lang](group__bt__audio__codec__cfg.md#gae2beb0c754a4956f04127aa353bb0949)

int bt\_audio\_codec\_cfg\_meta\_set\_stream\_lang(struct bt\_audio\_codec\_cfg \*codec\_cfg, uint32\_t stream\_lang)

Set the stream language of a codec configuration metadata.

[bt\_audio\_codec\_cfg\_meta\_get\_val](group__bt__audio__codec__cfg.md#gae98335e87394a491b4a311d867a5e32d)

int bt\_audio\_codec\_cfg\_meta\_get\_val(const struct bt\_audio\_codec\_cfg \*codec\_cfg, uint8\_t type, const uint8\_t \*\*data)

Lookup a specific metadata value based on type.

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

**Definition** audio.h:340

[bt\_audio\_dir](group__bt__audio.md#ga5bd899fb5e4d844058184913866e462f)

bt\_audio\_dir

Audio Capability type.

**Definition** audio.h:635

[bt\_audio\_location](group__bt__audio.md#ga61230848c02098352320fe751332c4e8)

bt\_audio\_location

Location values for BT Audio.

**Definition** audio.h:485

[bt\_audio\_parental\_rating](group__bt__audio.md#ga6d4aff1f93dc0b902e4b5d1355f15760)

bt\_audio\_parental\_rating

Parental rating defined by the Generic Audio assigned numbers (bluetooth.com).

**Definition** audio.h:320

[bt\_audio\_codec\_cfg\_frame\_dur](group__bt__audio.md#ga83701b5eadfcbc9b84dc0b1a85ebeb74)

bt\_audio\_codec\_cfg\_frame\_dur

**Definition** audio.h:270

[bt\_audio\_codec\_qos\_framing](group__bt__audio.md#ga8cb1832a3ee38b1a151b702c5dee00d9)

bt\_audio\_codec\_qos\_framing

Codec QoS Framing.

**Definition** audio.h:663

[bt\_audio\_codec\_cfg\_freq](group__bt__audio.md#ga8e99fb678cc011bb8c9f6e1858bae0d7)

bt\_audio\_codec\_cfg\_freq

**Definition** audio.h:229

[bt\_audio\_codec\_cfg\_type](group__bt__audio.md#ga9230ec4d7518bd243207ba2decb1a974)

bt\_audio\_codec\_cfg\_type

Codec configuration types.

**Definition** audio.h:212

[bt\_audio\_codec\_cap\_freq](group__bt__audio.md#gaafc1106d5d305874ee2f540c850ff5b4)

bt\_audio\_codec\_cap\_freq

Supported frequencies bitfield.

**Definition** audio.h:68

[bt\_audio\_metadata\_type](group__bt__audio.md#gab53d0dd62bceff97cf8eed7d8cf80354)

bt\_audio\_metadata\_type

Codec metadata type IDs.

**Definition** audio.h:350

[bt\_audio\_codec\_cap\_chan\_count](group__bt__audio.md#gae695b5d17359967703f2509db1671fa5)

bt\_audio\_codec\_cap\_chan\_count

**Definition** audio.h:148

[bt\_audio\_codec\_cap\_frame\_dur](group__bt__audio.md#gaf37e8e19f956afb3c3a413cbaa1a21f5)

bt\_audio\_codec\_cap\_frame\_dur

Supported frame durations bitfield.

**Definition** audio.h:120

[bt\_audio\_codec\_cap\_type](group__bt__audio.md#gaf58823a56eb36cfd22e582ab1ea3d015)

bt\_audio\_codec\_cap\_type

Codec capability types.

**Definition** audio.h:50

[bt\_audio\_context](group__bt__audio.md#gafb379ffa88388cc1397960155bbb2ab3)

bt\_audio\_context

Audio Context Type for Generic Audio.

**Definition** audio.h:282

[bt\_audio\_data\_parse](group__bt__audio.md#gafd8574b16141162c95653f0aa2bf6ff7)

int bt\_audio\_data\_parse(const uint8\_t ltv[], size\_t size, bool(\*func)(struct bt\_data \*data, void \*user\_data), void \*user\_data)

Helper for parsing length-type-value data.

[BT\_AUDIO\_ACTIVE\_STATE\_ENABLED](group__bt__audio.md#gga16d403ec4db7be997682331ad365ff5fa6d062944e9c49001666769601ba1c940)

@ BT\_AUDIO\_ACTIVE\_STATE\_ENABLED

**Definition** audio.h:342

[BT\_AUDIO\_ACTIVE\_STATE\_DISABLED](group__bt__audio.md#gga16d403ec4db7be997682331ad365ff5fade27604ea8fd592aa5d0958e2ccde4f3)

@ BT\_AUDIO\_ACTIVE\_STATE\_DISABLED

**Definition** audio.h:341

[BT\_AUDIO\_DIR\_SINK](group__bt__audio.md#gga5bd899fb5e4d844058184913866e462fa2adba49daa32ac7b040c3294f047ceb8)

@ BT\_AUDIO\_DIR\_SINK

**Definition** audio.h:636

[BT\_AUDIO\_DIR\_SOURCE](group__bt__audio.md#gga5bd899fb5e4d844058184913866e462fa868695a31ebf95402a4bae2469f3aa6c)

@ BT\_AUDIO\_DIR\_SOURCE

**Definition** audio.h:637

[BT\_AUDIO\_LOCATION\_FRONT\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a06b34e67c9931f8b26562218cba51337)

@ BT\_AUDIO\_LOCATION\_FRONT\_CENTER

**Definition** audio.h:489

[BT\_AUDIO\_LOCATION\_TOP\_BACK\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a07e699c28bd847de3d85645dceb2ff06)

@ BT\_AUDIO\_LOCATION\_TOP\_BACK\_LEFT

**Definition** audio.h:503

[BT\_AUDIO\_LOCATION\_LOW\_FREQ\_EFFECTS\_2](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a0c304bdd529ad66acb71001caa1b361b)

@ BT\_AUDIO\_LOCATION\_LOW\_FREQ\_EFFECTS\_2

**Definition** audio.h:496

[BT\_AUDIO\_LOCATION\_TOP\_SIDE\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a1cf8dea66e42f75ca85ba55124829a59)

@ BT\_AUDIO\_LOCATION\_TOP\_SIDE\_RIGHT

**Definition** audio.h:506

[BT\_AUDIO\_LOCATION\_FRONT\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a26d5ba460642bcf7fb2fc950082b70b3)

@ BT\_AUDIO\_LOCATION\_FRONT\_RIGHT

**Definition** audio.h:488

[BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a33d0f7c266f21fd086386f8c29ee31e8)

@ BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_RIGHT

**Definition** audio.h:510

[BT\_AUDIO\_LOCATION\_BACK\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a43f5070c2b4d39c38fa7900595d9b1aa)

@ BT\_AUDIO\_LOCATION\_BACK\_RIGHT

**Definition** audio.h:492

[BT\_AUDIO\_LOCATION\_TOP\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a555361fafade3bfb27dc713666757a1f)

@ BT\_AUDIO\_LOCATION\_TOP\_CENTER

**Definition** audio.h:502

[BT\_AUDIO\_LOCATION\_LEFT\_SURROUND](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a568a581c0ad653177f5d148d04bef0b6)

@ BT\_AUDIO\_LOCATION\_LEFT\_SURROUND

**Definition** audio.h:513

[BT\_AUDIO\_LOCATION\_TOP\_FRONT\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a60b154a216d8e029deac7305500eaf2d)

@ BT\_AUDIO\_LOCATION\_TOP\_FRONT\_RIGHT

**Definition** audio.h:500

[BT\_AUDIO\_LOCATION\_FRONT\_RIGHT\_OF\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a725707ae4703a1f9b970de5b1e4e5692)

@ BT\_AUDIO\_LOCATION\_FRONT\_RIGHT\_OF\_CENTER

**Definition** audio.h:494

[BT\_AUDIO\_LOCATION\_FRONT\_RIGHT\_WIDE](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a8649be1d5b7e8b312fc3374039cc0a71)

@ BT\_AUDIO\_LOCATION\_FRONT\_RIGHT\_WIDE

**Definition** audio.h:512

[BT\_AUDIO\_LOCATION\_TOP\_BACK\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a8e81b80f732b0037493712b4baa21a69)

@ BT\_AUDIO\_LOCATION\_TOP\_BACK\_RIGHT

**Definition** audio.h:504

[BT\_AUDIO\_LOCATION\_MONO\_AUDIO](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a8f476de613cdcb2f9f677d40291aa5df)

@ BT\_AUDIO\_LOCATION\_MONO\_AUDIO

**Definition** audio.h:486

[BT\_AUDIO\_LOCATION\_BACK\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a96906ff7918b0a3e3e7efe73a08d9896)

@ BT\_AUDIO\_LOCATION\_BACK\_LEFT

**Definition** audio.h:491

[BT\_AUDIO\_LOCATION\_RIGHT\_SURROUND](group__bt__audio.md#gga61230848c02098352320fe751332c4e8a97954db823b6c6bed660ff2717600a5e)

@ BT\_AUDIO\_LOCATION\_RIGHT\_SURROUND

**Definition** audio.h:514

[BT\_AUDIO\_LOCATION\_SIDE\_RIGHT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8aa01ad94f71defd158d8cfe25936341cd)

@ BT\_AUDIO\_LOCATION\_SIDE\_RIGHT

**Definition** audio.h:498

[BT\_AUDIO\_LOCATION\_TOP\_FRONT\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8aa093e6218e213eac5677766e01f5c1c9)

@ BT\_AUDIO\_LOCATION\_TOP\_FRONT\_LEFT

**Definition** audio.h:499

[BT\_AUDIO\_LOCATION\_SIDE\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ab8e52c69b894e382f0f09cc370337064)

@ BT\_AUDIO\_LOCATION\_SIDE\_LEFT

**Definition** audio.h:497

[BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ac1e355baee6ca0907356d72f0d4edb29)

@ BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_LEFT

**Definition** audio.h:509

[BT\_AUDIO\_LOCATION\_TOP\_FRONT\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ac32ed6f456be2fb2d9af2c7b255f3a4e)

@ BT\_AUDIO\_LOCATION\_TOP\_FRONT\_CENTER

**Definition** audio.h:501

[BT\_AUDIO\_LOCATION\_LOW\_FREQ\_EFFECTS\_1](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ac4c09f948266f2c9c65b3bc16da2f3f6)

@ BT\_AUDIO\_LOCATION\_LOW\_FREQ\_EFFECTS\_1

**Definition** audio.h:490

[BT\_AUDIO\_LOCATION\_FRONT\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ac658188fa6f1b4f248a149d0bde1e41b)

@ BT\_AUDIO\_LOCATION\_FRONT\_LEFT

**Definition** audio.h:487

[BT\_AUDIO\_LOCATION\_FRONT\_LEFT\_WIDE](group__bt__audio.md#gga61230848c02098352320fe751332c4e8acba90183626ad85c21692b7edd87133d)

@ BT\_AUDIO\_LOCATION\_FRONT\_LEFT\_WIDE

**Definition** audio.h:511

[BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ad0be8f720f03feb18a23e77f0eff6376)

@ BT\_AUDIO\_LOCATION\_BOTTOM\_FRONT\_CENTER

**Definition** audio.h:508

[BT\_AUDIO\_LOCATION\_BACK\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ae22cd1e458d8ff503741bf48262c7983)

@ BT\_AUDIO\_LOCATION\_BACK\_CENTER

**Definition** audio.h:495

[BT\_AUDIO\_LOCATION\_TOP\_SIDE\_LEFT](group__bt__audio.md#gga61230848c02098352320fe751332c4e8ae846b2f4186b46d3690c71071c41c7d6)

@ BT\_AUDIO\_LOCATION\_TOP\_SIDE\_LEFT

**Definition** audio.h:505

[BT\_AUDIO\_LOCATION\_TOP\_BACK\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8aebae1f0f2537a806672820fb74eba5dd)

@ BT\_AUDIO\_LOCATION\_TOP\_BACK\_CENTER

**Definition** audio.h:507

[BT\_AUDIO\_LOCATION\_FRONT\_LEFT\_OF\_CENTER](group__bt__audio.md#gga61230848c02098352320fe751332c4e8af02a9d46877b742e8730bbf3dd6ad22e)

@ BT\_AUDIO\_LOCATION\_FRONT\_LEFT\_OF\_CENTER

**Definition** audio.h:493

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_18\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a22167e0c033c176f592a447b14c30071)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_18\_OR\_ABOVE

**Definition** audio.h:336

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_15\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a3fe7bc3216a458ec3e5c6e177f43c077)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_15\_OR\_ABOVE

**Definition** audio.h:333

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_10\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a4210d67d4506f8b9defb5fae32ae30d2)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_10\_OR\_ABOVE

**Definition** audio.h:328

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_7\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a69508e569059bde1fed1b3fb3db1547a)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_7\_OR\_ABOVE

**Definition** audio.h:325

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_16\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a779c5dd14e5f88e8e6bb247dc66d9c92)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_16\_OR\_ABOVE

**Definition** audio.h:334

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_17\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a7d0794fe6796f19ff7e58819728751ff)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_17\_OR\_ABOVE

**Definition** audio.h:335

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_5\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a8a8476abac3a569bd470a5237642c526)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_5\_OR\_ABOVE

**Definition** audio.h:323

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_8\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760a9ed111f80d0671bb8b4e0a304ff0b0e4)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_8\_OR\_ABOVE

**Definition** audio.h:326

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_13\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760aa680247699538d256111e18af1a2d15d)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_13\_OR\_ABOVE

**Definition** audio.h:331

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_9\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760aaabe26ebaa4b84684005440176ad86dd)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_9\_OR\_ABOVE

**Definition** audio.h:327

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_11\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760ac402ee4c06b92f0cc36774cf409cbbd0)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_11\_OR\_ABOVE

**Definition** audio.h:329

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_12\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760ac68caf6719391afbef79e0c579dc96e7)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_12\_OR\_ABOVE

**Definition** audio.h:330

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_6\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760accb959ba21c1238c70c594b5cdc3ebdc)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_6\_OR\_ABOVE

**Definition** audio.h:324

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_ANY](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760ad6bba6a3b9537fcf913f798ab9a525f1)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_ANY

**Definition** audio.h:322

[BT\_AUDIO\_PARENTAL\_RATING\_NO\_RATING](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760aecf628bbd76651215232c8bfed04aa2c)

@ BT\_AUDIO\_PARENTAL\_RATING\_NO\_RATING

**Definition** audio.h:321

[BT\_AUDIO\_PARENTAL\_RATING\_AGE\_14\_OR\_ABOVE](group__bt__audio.md#gga6d4aff1f93dc0b902e4b5d1355f15760aef216d59983eccb86e90c493b8c17d86)

@ BT\_AUDIO\_PARENTAL\_RATING\_AGE\_14\_OR\_ABOVE

**Definition** audio.h:332

[BT\_AUDIO\_CODEC\_CFG\_DURATION\_10](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ab6a0dd3bbe587ff5ba110675a01514a7)

@ BT\_AUDIO\_CODEC\_CFG\_DURATION\_10

10 msec Frame Duration configuration

**Definition** audio.h:275

[BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5](group__bt__audio.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ad2491c0ded7c7f489bdeffe024463272)

@ BT\_AUDIO\_CODEC\_CFG\_DURATION\_7\_5

7.5 msec Frame Duration configuration

**Definition** audio.h:272

[BT\_AUDIO\_CODEC\_QOS\_FRAMING\_UNFRAMED](group__bt__audio.md#gga8cb1832a3ee38b1a151b702c5dee00d9a426ad2fe26f69d135beff6a367ef872f)

@ BT\_AUDIO\_CODEC\_QOS\_FRAMING\_UNFRAMED

**Definition** audio.h:664

[BT\_AUDIO\_CODEC\_QOS\_FRAMING\_FRAMED](group__bt__audio.md#gga8cb1832a3ee38b1a151b702c5dee00d9af7a4a07da9089c3afb248d63e3a9297a)

@ BT\_AUDIO\_CODEC\_QOS\_FRAMING\_FRAMED

**Definition** audio.h:665

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_24KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a0d6d0f278628681f8ef5dc3797bf5275)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_24KHZ

24 Khz codec sampling frequency

**Definition** audio.h:243

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a2b7163ba4c486167d3e81c2aa4216f11)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_48KHZ

48 Khz codec sampling frequency

**Definition** audio.h:252

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a3ce97404475ad182125ad64aba66077e)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_32KHZ

32 Khz codec sampling frequency

**Definition** audio.h:246

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_384KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a44cccbd3e7afc25f964b3c2c571d4be4)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_384KHZ

384 Khz codec sampling frequency

**Definition** audio.h:267

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_22KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a68f8411a83f60ec4c6bb9fa65fdd7048)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_22KHZ

22.05 Khz codec sampling frequency

**Definition** audio.h:240

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_8KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a7018d3fb612d4730b880ef0bb2d20b9a)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_8KHZ

8 Khz codec sampling frequency

**Definition** audio.h:231

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_96KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a79e7a473d3f7d6803f3b8b7843c40c60)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_96KHZ

96 Khz codec sampling frequency

**Definition** audio.h:258

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_176KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a85037a2eb4a64376a0a436ab43263126)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_176KHZ

176.4 Khz codec sampling frequency

**Definition** audio.h:261

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_44KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aa701e855c950fdcdd66d4dbaaf75fb84)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_44KHZ

44.1 Khz codec sampling frequency

**Definition** audio.h:249

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_192KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aa85a51db272ef019e5cce5ec3982f8c7)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_192KHZ

192 Khz codec sampling frequency

**Definition** audio.h:264

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_11KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aa8d8018b050a8c029b4b60c706d771f8)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_11KHZ

11.025 Khz codec sampling frequency

**Definition** audio.h:234

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_16KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7ab097ae9f9ad963fee64e61eaf2663245)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_16KHZ

16 Khz codec sampling frequency

**Definition** audio.h:237

[BT\_AUDIO\_CODEC\_CFG\_FREQ\_88KHZ](group__bt__audio.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aff685ebe62909eea8512b7deac0df409)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ\_88KHZ

88.2 Khz codec sampling frequency

**Definition** audio.h:255

[BT\_AUDIO\_CODEC\_CFG\_FREQ](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974a49849b389d553535ea222c9ae63bccc3)

@ BT\_AUDIO\_CODEC\_CFG\_FREQ

Sampling frequency.

**Definition** audio.h:214

[BT\_AUDIO\_CODEC\_CFG\_FRAME\_LEN](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974a85d41856175c11b1193ebdd58b83d6e2)

@ BT\_AUDIO\_CODEC\_CFG\_FRAME\_LEN

Octets per codec frame.

**Definition** audio.h:223

[BT\_AUDIO\_CODEC\_CFG\_DURATION](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974a8e2fae97b1565b0fa0ff988a47928223)

@ BT\_AUDIO\_CODEC\_CFG\_DURATION

Frame duration.

**Definition** audio.h:217

[BT\_AUDIO\_CODEC\_CFG\_FRAME\_BLKS\_PER\_SDU](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974abbc2279f5d029278d9367f08a1152aa8)

@ BT\_AUDIO\_CODEC\_CFG\_FRAME\_BLKS\_PER\_SDU

Codec frame blocks per SDU.

**Definition** audio.h:226

[BT\_AUDIO\_CODEC\_CFG\_CHAN\_ALLOC](group__bt__audio.md#gga9230ec4d7518bd243207ba2decb1a974ad53deb048fb0ce4d4428df4f477718b2)

@ BT\_AUDIO\_CODEC\_CFG\_CHAN\_ALLOC

Audio channel allocation.

**Definition** audio.h:220

[BT\_AUDIO\_CODEC\_QOS\_CODED](group__bt__audio.md#ggaa69a4789478a1a0aa93451d294de7ad0a9789c1b6b319370a3b98ab37b61a86e0)

@ BT\_AUDIO\_CODEC\_QOS\_CODED

**Definition** audio.h:672

[BT\_AUDIO\_CODEC\_QOS\_1M](group__bt__audio.md#ggaa69a4789478a1a0aa93451d294de7ad0ab387760c001ea6c81e889de55e74d5d5)

@ BT\_AUDIO\_CODEC\_QOS\_1M

**Definition** audio.h:670

[BT\_AUDIO\_CODEC\_QOS\_2M](group__bt__audio.md#ggaa69a4789478a1a0aa93451d294de7ad0ac81306188ed29b8fa17aa2afa878f297)

@ BT\_AUDIO\_CODEC\_QOS\_2M

**Definition** audio.h:671

[BT\_AUDIO\_CODEC\_CAP\_FREQ\_176KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a031d159eadf7ea1ba6b00b03bef26d2b)

@ BT\_AUDIO\_CODEC\_CAP\_FREQ\_176KHZ

176.4 Khz sampling frequency

**Definition** audio.h:100

[BT\_AUDIO\_CODEC\_CAP\_FREQ\_192KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a0de8d0351153650c1b48934053e18890)

@ BT\_AUDIO\_CODEC\_CAP\_FREQ\_192KHZ

192 Khz sampling frequency

**Definition** audio.h:103

[BT\_AUDIO\_CODEC\_CAP\_FREQ\_88KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a25cc72bd630446f5154c54402058a211)

@ BT\_AUDIO\_CODEC\_CAP\_FREQ\_88KHZ

88.2 Khz sampling frequency

**Definition** audio.h:94

[BT\_AUDIO\_CODEC\_CAP\_FREQ\_8KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a3d821d03771805107707f47dcdb71f83)

@ BT\_AUDIO\_CODEC\_CAP\_FREQ\_8KHZ

8 Khz sampling frequency

**Definition** audio.h:70

[BT\_AUDIO\_CODEC\_CAP\_FREQ\_11KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a562c38a59cded025183a0f95d4a63c81)

@ BT\_AUDIO\_CODEC\_CAP\_FREQ\_11KHZ

11.025 Khz sampling frequency

**Definition** audio.h:73

[BT\_AUDIO\_CODEC\_CAP\_FREQ\_32KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a822ff105ab495c126c21d73bd90cbd9c)

@ BT\_AUDIO\_CODEC\_CAP\_FREQ\_32KHZ

32 Khz sampling frequency

**Definition** audio.h:85

[BT\_AUDIO\_CODEC\_CAP\_FREQ\_48KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4a91ec17ee96b8e56e31ab545e5e8abe91)

@ BT\_AUDIO\_CODEC\_CAP\_FREQ\_48KHZ

48 Khz sampling frequency

**Definition** audio.h:91

[BT\_AUDIO\_CODEC\_CAP\_FREQ\_24KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4acf9ff8842d72d56d27eae692e4c4b956)

@ BT\_AUDIO\_CODEC\_CAP\_FREQ\_24KHZ

24 Khz sampling frequency

**Definition** audio.h:82

[BT\_AUDIO\_CODEC\_CAP\_FREQ\_16KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4acfef6825ac865b1e590e7959a9270361)

@ BT\_AUDIO\_CODEC\_CAP\_FREQ\_16KHZ

16 Khz sampling frequency

**Definition** audio.h:76

[BT\_AUDIO\_CODEC\_CAP\_FREQ\_44KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ad28396f4b5a71d7c196e1a27bd17f8c3)

@ BT\_AUDIO\_CODEC\_CAP\_FREQ\_44KHZ

44.1 Khz sampling frequency

**Definition** audio.h:88

[BT\_AUDIO\_CODEC\_CAP\_FREQ\_22KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ad7440157cf8864dfc5fd854482f3a982)

@ BT\_AUDIO\_CODEC\_CAP\_FREQ\_22KHZ

22.05 Khz sampling frequency

**Definition** audio.h:79

[BT\_AUDIO\_CODEC\_CAP\_FREQ\_ANY](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4adaaa42a6bb0c01d3819c604b6d5bbf02)

@ BT\_AUDIO\_CODEC\_CAP\_FREQ\_ANY

Any frequency capability.

**Definition** audio.h:109

[BT\_AUDIO\_CODEC\_CAP\_FREQ\_384KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ae5ddc4504b7077e90be56f34ad8647c2)

@ BT\_AUDIO\_CODEC\_CAP\_FREQ\_384KHZ

384 Khz sampling frequency

**Definition** audio.h:106

[BT\_AUDIO\_CODEC\_CAP\_FREQ\_96KHZ](group__bt__audio.md#ggaafc1106d5d305874ee2f540c850ff5b4ae802fea402f207238613275917846663)

@ BT\_AUDIO\_CODEC\_CAP\_FREQ\_96KHZ

96 Khz sampling frequency

**Definition** audio.h:97

[BT\_AUDIO\_METADATA\_TYPE\_PROGRAM\_INFO](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a02f91ea7fb6be631687d843ad7bf4ac7)

@ BT\_AUDIO\_METADATA\_TYPE\_PROGRAM\_INFO

UTF-8 encoded title or summary of stream content.

**Definition** audio.h:374

[BT\_AUDIO\_METADATA\_TYPE\_EXTENDED](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a0b5a8cd34bad81ac53c657c3cd9ddb39)

@ BT\_AUDIO\_METADATA\_TYPE\_EXTENDED

Extended metadata.

**Definition** audio.h:404

[BT\_AUDIO\_METADATA\_TYPE\_VENDOR](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a30fbc4a159e64174b22f195f29012286)

@ BT\_AUDIO\_METADATA\_TYPE\_VENDOR

Vendor specific metadata.

**Definition** audio.h:407

[BT\_AUDIO\_METADATA\_TYPE\_CCID\_LIST](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a37b5552e04734392dc6c6eb9e19b377b)

@ BT\_AUDIO\_METADATA\_TYPE\_CCID\_LIST

Array of 8-bit CCID values.

**Definition** audio.h:383

[BT\_AUDIO\_METADATA\_TYPE\_BROADCAST\_IMMEDIATE](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a4b9cc5b82a1dbfc3db69bb12747443f1)

@ BT\_AUDIO\_METADATA\_TYPE\_BROADCAST\_IMMEDIATE

Broadcast Audio Immediate Rendering flag.

**Definition** audio.h:401

[BT\_AUDIO\_METADATA\_TYPE\_PROGRAM\_INFO\_URI](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a58971ea21b5045e56a0e1ca838358922)

@ BT\_AUDIO\_METADATA\_TYPE\_PROGRAM\_INFO\_URI

UTF-8 encoded URI for additional Program information.

**Definition** audio.h:392

[BT\_AUDIO\_METADATA\_TYPE\_PARENTAL\_RATING](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a7a83f397dc5dbe6e6d60a994cccdc613)

@ BT\_AUDIO\_METADATA\_TYPE\_PARENTAL\_RATING

Parental rating.

**Definition** audio.h:389

[BT\_AUDIO\_METADATA\_TYPE\_STREAM\_CONTEXT](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354a95f128b11584ee22100ae65ce751dbaa)

@ BT\_AUDIO\_METADATA\_TYPE\_STREAM\_CONTEXT

Streaming audio context.

**Definition** audio.h:371

[BT\_AUDIO\_METADATA\_TYPE\_PREF\_CONTEXT](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354aac28d2a0dc883affa60b7a70f678ed9a)

@ BT\_AUDIO\_METADATA\_TYPE\_PREF\_CONTEXT

Preferred audio context.

**Definition** audio.h:360

[BT\_AUDIO\_METADATA\_TYPE\_STREAM\_LANG](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354ae98c430a422e3583d19d1b391b97edda)

@ BT\_AUDIO\_METADATA\_TYPE\_STREAM\_LANG

Stream language.

**Definition** audio.h:380

[BT\_AUDIO\_METADATA\_TYPE\_AUDIO\_STATE](group__bt__audio.md#ggab53d0dd62bceff97cf8eed7d8cf80354af220c40d351ec5e236cd41a5944da5fc)

@ BT\_AUDIO\_METADATA\_TYPE\_AUDIO\_STATE

Audio active state.

**Definition** audio.h:398

[BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_4](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a0fdfa6bf69b104f04d22e4f968969ac2)

@ BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_4

Supporting 4 channel.

**Definition** audio.h:159

[BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_2](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a13b236d93eb9c7516fdcf527313e16cd)

@ BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_2

Supporting 2 channel.

**Definition** audio.h:153

[BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_1](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a1558716b36042597515df18ff277f8bc)

@ BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_1

Supporting 1 channel.

**Definition** audio.h:150

[BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_3](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a17da27ec39a79c341c82549df891cb39)

@ BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_3

Supporting 3 channel.

**Definition** audio.h:156

[BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_8](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a50afa60bdd53172fab7a376ce374d943)

@ BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_8

Supporting 8 channel.

**Definition** audio.h:171

[BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_7](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5a86ef227772c7751b4ae75529e2a57b82)

@ BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_7

Supporting 7 channel.

**Definition** audio.h:168

[BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_ANY](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5aaf6f7179310c64b93b300ecfc29e4219)

@ BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_ANY

Supporting all channels.

**Definition** audio.h:174

[BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_5](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5ad08bc2ea0347a1ee8fd411a023b7ca51)

@ BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_5

Supporting 5 channel.

**Definition** audio.h:162

[BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_6](group__bt__audio.md#ggae695b5d17359967703f2509db1671fa5af9f9dd0cac39793793e5c8c5e50b11b8)

@ BT\_AUDIO\_CODEC\_CAP\_CHAN\_COUNT\_6

Supporting 6 channel.

**Definition** audio.h:165

[BT\_AUDIO\_CODEC\_CAP\_DURATION\_7\_5](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a340878058d0beabeade33e0f3893d441)

@ BT\_AUDIO\_CODEC\_CAP\_DURATION\_7\_5

7.5 msec frame duration capability

**Definition** audio.h:122

[BT\_AUDIO\_CODEC\_CAP\_DURATION\_PREFER\_7\_5](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a7ab1c63639cf93fdf2c2dfdf43424e91)

@ BT\_AUDIO\_CODEC\_CAP\_DURATION\_PREFER\_7\_5

7.5 msec preferred frame duration capability.

**Definition** audio.h:137

[BT\_AUDIO\_CODEC\_CAP\_DURATION\_ANY](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a81d28ce43d69d4625e9a73b37c70347a)

@ BT\_AUDIO\_CODEC\_CAP\_DURATION\_ANY

Any frame duration capability.

**Definition** audio.h:128

[BT\_AUDIO\_CODEC\_CAP\_DURATION\_PREFER\_10](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a9744473b3a29074c24cf0bbff35a5d8e)

@ BT\_AUDIO\_CODEC\_CAP\_DURATION\_PREFER\_10

10 msec preferred frame duration capability

**Definition** audio.h:145

[BT\_AUDIO\_CODEC\_CAP\_DURATION\_10](group__bt__audio.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5afd423ac4270ff0df8ca6df7f5e4c799b)

@ BT\_AUDIO\_CODEC\_CAP\_DURATION\_10

10 msec frame duration capability

**Definition** audio.h:125

[BT\_AUDIO\_CODEC\_CAP\_TYPE\_CHAN\_COUNT](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015a0cd3a3d31febc9e30137e9e21d4f7191)

@ BT\_AUDIO\_CODEC\_CAP\_TYPE\_CHAN\_COUNT

Supported audio channel counts.

**Definition** audio.h:58

[BT\_AUDIO\_CODEC\_CAP\_TYPE\_DURATION](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015a4a90a37cd6d8ca9d1ed984e4a122d510)

@ BT\_AUDIO\_CODEC\_CAP\_TYPE\_DURATION

Supported frame durations.

**Definition** audio.h:55

[BT\_AUDIO\_CODEC\_CAP\_TYPE\_FRAME\_COUNT](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015acba980896f080ac2ba81d1b66305bb41)

@ BT\_AUDIO\_CODEC\_CAP\_TYPE\_FRAME\_COUNT

Supported maximum codec frames per SDU.

**Definition** audio.h:64

[BT\_AUDIO\_CODEC\_CAP\_TYPE\_FRAME\_LEN](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015ad074bed5f79946e2388584336d30cf46)

@ BT\_AUDIO\_CODEC\_CAP\_TYPE\_FRAME\_LEN

Supported octets per codec frame.

**Definition** audio.h:61

[BT\_AUDIO\_CODEC\_CAP\_TYPE\_FREQ](group__bt__audio.md#ggaf58823a56eb36cfd22e582ab1ea3d015af68f3f5665446de9b71c2f70e7aa762b)

@ BT\_AUDIO\_CODEC\_CAP\_TYPE\_FREQ

Supported sampling frequencies.

**Definition** audio.h:52

[BT\_AUDIO\_CONTEXT\_TYPE\_NOTIFICATIONS](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a06df6f713bb68b197be75bf821d5d377)

@ BT\_AUDIO\_CONTEXT\_TYPE\_NOTIFICATIONS

**Definition** audio.h:292

[BT\_AUDIO\_CONTEXT\_TYPE\_EMERGENCY\_ALARM](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a132abd2f9ac7be62d1306efc6bc8b7d1)

@ BT\_AUDIO\_CONTEXT\_TYPE\_EMERGENCY\_ALARM

**Definition** audio.h:295

[BT\_AUDIO\_CONTEXT\_TYPE\_INSTRUCTIONAL](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a2e3af6f4ca620f91d9266257f842ddd4)

@ BT\_AUDIO\_CONTEXT\_TYPE\_INSTRUCTIONAL

**Definition** audio.h:288

[BT\_AUDIO\_CONTEXT\_TYPE\_PROHIBITED](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a3cfcfa76adc5effdc1aa95d75e5da37a)

@ BT\_AUDIO\_CONTEXT\_TYPE\_PROHIBITED

**Definition** audio.h:283

[BT\_AUDIO\_CONTEXT\_TYPE\_RINGTONE](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a422bb29f035583b7319456a679f880b3)

@ BT\_AUDIO\_CONTEXT\_TYPE\_RINGTONE

**Definition** audio.h:293

[BT\_AUDIO\_CONTEXT\_TYPE\_LIVE](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a42c80228bda513d5a59d4d836e73bd55)

@ BT\_AUDIO\_CONTEXT\_TYPE\_LIVE

**Definition** audio.h:290

[BT\_AUDIO\_CONTEXT\_TYPE\_MEDIA](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a43d67936976a5c041027d15d66c21a5e)

@ BT\_AUDIO\_CONTEXT\_TYPE\_MEDIA

**Definition** audio.h:286

[BT\_AUDIO\_CONTEXT\_TYPE\_GAME](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a652ad83b9eb524c62933bf87a8ecb730)

@ BT\_AUDIO\_CONTEXT\_TYPE\_GAME

**Definition** audio.h:287

[BT\_AUDIO\_CONTEXT\_TYPE\_SOUND\_EFFECTS](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a6956a9e43433e2800fd36c7022e039d9)

@ BT\_AUDIO\_CONTEXT\_TYPE\_SOUND\_EFFECTS

**Definition** audio.h:291

[BT\_AUDIO\_CONTEXT\_TYPE\_VOICE\_ASSISTANTS](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a7e208290ddc2f92ac78ff4a22b20ca7e)

@ BT\_AUDIO\_CONTEXT\_TYPE\_VOICE\_ASSISTANTS

**Definition** audio.h:289

[BT\_AUDIO\_CONTEXT\_TYPE\_CONVERSATIONAL](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a8a6262c1cf4e4591a7b92b4f8f329f9e)

@ BT\_AUDIO\_CONTEXT\_TYPE\_CONVERSATIONAL

**Definition** audio.h:285

[BT\_AUDIO\_CONTEXT\_TYPE\_ALERTS](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3a915d05a728f3e083f290766a970dabb6)

@ BT\_AUDIO\_CONTEXT\_TYPE\_ALERTS

**Definition** audio.h:294

[BT\_AUDIO\_CONTEXT\_TYPE\_UNSPECIFIED](group__bt__audio.md#ggafb379ffa88388cc1397960155bbb2ab3aad96be1265bd1be4c937c687335e33f5)

@ BT\_AUDIO\_CONTEXT\_TYPE\_UNSPECIFIED

**Definition** audio.h:284

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

**Definition** audio.h:550

[bt\_audio\_codec\_cap::vid](structbt__audio__codec__cap.md#a3b91269e16a3d63b3128a527caa5e3ff)

uint16\_t vid

Codec Company Vendor ID.

**Definition** audio.h:568

[bt\_audio\_codec\_cap::cid](structbt__audio__codec__cap.md#a763222d12a87958a5ba806303f98829a)

uint16\_t cid

Codec Company ID.

**Definition** audio.h:566

[bt\_audio\_codec\_cap::path\_id](structbt__audio__codec__cap.md#a822a06f815091cc580ca2e5bbb3126f7)

uint8\_t path\_id

Data path ID.

**Definition** audio.h:556

[bt\_audio\_codec\_cap::ctlr\_transcode](structbt__audio__codec__cap.md#a900a77db09e72de61d4ff652c6dbb10b)

bool ctlr\_transcode

Whether or not the local controller should transcode.

**Definition** audio.h:562

[bt\_audio\_codec\_cap::id](structbt__audio__codec__cap.md#ae3892731e7ca05f3ec426c70f0d9e1a9)

uint8\_t id

Codec ID.

**Definition** audio.h:564

[bt\_audio\_codec\_cfg](structbt__audio__codec__cfg.md)

Codec specific configuration structure.

**Definition** audio.h:584

[bt\_audio\_codec\_cfg::vid](structbt__audio__codec__cfg.md#a2996ab3f6ae1cab09ff5e3329b42468e)

uint16\_t vid

Codec Company Vendor ID.

**Definition** audio.h:602

[bt\_audio\_codec\_cfg::cid](structbt__audio__codec__cfg.md#a664e21bcd6002b21d4b1b53d866db32d)

uint16\_t cid

Codec Company ID.

**Definition** audio.h:600

[bt\_audio\_codec\_cfg::path\_id](structbt__audio__codec__cfg.md#a9386056bb02908407c9e3aad48abbd87)

uint8\_t path\_id

Data path ID.

**Definition** audio.h:590

[bt\_audio\_codec\_cfg::ctlr\_transcode](structbt__audio__codec__cfg.md#a9e2c8081950a0830ffc270245ab308c1)

bool ctlr\_transcode

Whether or not the local controller should transcode.

**Definition** audio.h:596

[bt\_audio\_codec\_cfg::id](structbt__audio__codec__cfg.md#aa2f99ec31ff3eb9b7b738bc8a1170f20)

uint8\_t id

Codec ID.

**Definition** audio.h:598

[bt\_audio\_codec\_octets\_per\_codec\_frame](structbt__audio__codec__octets__per__codec__frame.md)

**Definition** audio.h:199

[bt\_audio\_codec\_octets\_per\_codec\_frame::min](structbt__audio__codec__octets__per__codec__frame.md#aa8b234fa137273cd16230ebabc5f8ef4)

uint16\_t min

Minimum number of octets supported per codec frame.

**Definition** audio.h:201

[bt\_audio\_codec\_octets\_per\_codec\_frame::max](structbt__audio__codec__octets__per__codec__frame.md#ae09686799077b13e78b856b1e7e63b6a)

uint16\_t max

Maximum number of octets supported per codec frame.

**Definition** audio.h:203

[bt\_audio\_codec\_qos\_pref](structbt__audio__codec__qos__pref.md)

Audio Stream Quality of Service Preference structure.

**Definition** audio.h:785

[bt\_audio\_codec\_qos\_pref::latency](structbt__audio__codec__qos__pref.md#a1d46cf0aa05cfb7c88446719e59e0011)

uint16\_t latency

Preferred Transport Latency.

**Definition** audio.h:800

[bt\_audio\_codec\_qos\_pref::phy](structbt__audio__codec__qos__pref.md#a36fc375290b8f76c7278a236942db692)

uint8\_t phy

Preferred PHY.

**Definition** audio.h:794

[bt\_audio\_codec\_qos\_pref::unframed\_supported](structbt__audio__codec__qos__pref.md#a3bdb319d2aa401102fb9e54f92993e83)

bool unframed\_supported

Unframed PDUs supported.

**Definition** audio.h:791

[bt\_audio\_codec\_qos\_pref::pref\_pd\_max](structbt__audio__codec__qos__pref.md#a5486cacf6cd5016e9b44b69e3da67d6d)

uint32\_t pref\_pd\_max

Preferred maximum Presentation Delay.

**Definition** audio.h:832

[bt\_audio\_codec\_qos\_pref::pd\_min](structbt__audio__codec__qos__pref.md#a7437273abb18ce93c15bb789eeeb65d3)

uint32\_t pd\_min

Minimum Presentation Delay in microseconds.

**Definition** audio.h:810

[bt\_audio\_codec\_qos\_pref::pd\_max](structbt__audio__codec__qos__pref.md#ab07f2245bfed3a1400b6a1e6eaad2735)

uint32\_t pd\_max

Maximum Presentation Delay.

**Definition** audio.h:820

[bt\_audio\_codec\_qos\_pref::pref\_pd\_min](structbt__audio__codec__qos__pref.md#ab38a4b98b47ab773f91873b42c69ed71)

uint32\_t pref\_pd\_min

Preferred minimum Presentation Delay.

**Definition** audio.h:826

[bt\_audio\_codec\_qos\_pref::rtn](structbt__audio__codec__qos__pref.md#abc2142ef5c8ad1744b829ae626a57e9d)

uint8\_t rtn

Preferred Retransmission Number.

**Definition** audio.h:797

[bt\_audio\_codec\_qos](structbt__audio__codec__qos.md)

Codec QoS structure.

**Definition** audio.h:702

[bt\_audio\_codec\_qos::pd](structbt__audio__codec__qos.md#a28d87b06785e016fe7e12a0504f3b419)

uint32\_t pd

QoS Presentation Delay in microseconds.

**Definition** audio.h:731

[bt\_audio\_codec\_qos::framing](structbt__audio__codec__qos.md#a4212bf93b65e0faa218a1e0d03ae0283)

enum bt\_audio\_codec\_qos\_framing framing

QoS Framing.

**Definition** audio.h:707

[bt\_audio\_codec\_qos::phy](structbt__audio__codec__qos.md#a8911b0b9db8e4de55b3c313e3ad7c502)

uint8\_t phy

QoS PHY.

**Definition** audio.h:704

[bt\_audio\_codec\_qos::rtn](structbt__audio__codec__qos.md#ab05af8d47df82d34921afdd557770dbd)

uint8\_t rtn

QoS Retransmission Number.

**Definition** audio.h:710

[bt\_audio\_codec\_qos::interval](structbt__audio__codec__qos.md#ad906dc06624b0f80701d7ee92d849152)

uint32\_t interval

QoS Frame Interval.

**Definition** audio.h:725

[bt\_audio\_codec\_qos::sdu](structbt__audio__codec__qos.md#ae1a5adb80af9357fd6ee6532b0ba228e)

uint16\_t sdu

QoS SDU.

**Definition** audio.h:713

[bt\_data](structbt__data.md)

Bluetooth data.

**Definition** bluetooth.h:439

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [audio.h](bluetooth_2audio_2audio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
