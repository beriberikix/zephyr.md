---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/gnss_8h_source.html
original_path: doxygen/html/gnss_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gnss.h

[Go to the documentation of this file.](gnss_8h.md)

1/\*

2 \* Copyright (c) 2023 Trackunit Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_GNSS\_H\_

13#define ZEPHYR\_INCLUDE\_DRIVERS\_GNSS\_H\_

14

23

24#include <[zephyr/kernel.h](kernel_8h.md)>

25#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

26#include <[zephyr/device.h](device_8h.md)>

27#include <[zephyr/data/navigation.h](navigation_8h.md)>

28#include <[errno.h](errno_8h.md)>

29

30#ifdef \_\_cplusplus

31extern "C" {

32#endif

33

[ 35](group__gnss__interface.md#ga2b43ac2fec33053a769b7070c4ed3263)enum [gnss\_pps\_mode](group__gnss__interface.md#ga2b43ac2fec33053a769b7070c4ed3263) {

[ 37](group__gnss__interface.md#gga2b43ac2fec33053a769b7070c4ed3263a5e9af4b08bd41a1aa1bf01c0e290d9fc) [GNSS\_PPS\_MODE\_DISABLED](group__gnss__interface.md#gga2b43ac2fec33053a769b7070c4ed3263a5e9af4b08bd41a1aa1bf01c0e290d9fc) = 0,

[ 39](group__gnss__interface.md#gga2b43ac2fec33053a769b7070c4ed3263a9cdbb144191c83f4a7a2cc27268eacfa) [GNSS\_PPS\_MODE\_ENABLED](group__gnss__interface.md#gga2b43ac2fec33053a769b7070c4ed3263a9cdbb144191c83f4a7a2cc27268eacfa) = 1,

[ 41](group__gnss__interface.md#gga2b43ac2fec33053a769b7070c4ed3263a2df416ad912a84135eff1e30977b4507) [GNSS\_PPS\_MODE\_ENABLED\_AFTER\_LOCK](group__gnss__interface.md#gga2b43ac2fec33053a769b7070c4ed3263a2df416ad912a84135eff1e30977b4507) = 2,

[ 43](group__gnss__interface.md#gga2b43ac2fec33053a769b7070c4ed3263afc82bd9ebcfd9d3b6111c9e82fc79ecc) [GNSS\_PPS\_MODE\_ENABLED\_WHILE\_LOCKED](group__gnss__interface.md#gga2b43ac2fec33053a769b7070c4ed3263afc82bd9ebcfd9d3b6111c9e82fc79ecc) = 3

44};

45

[ 47](group__gnss__interface.md#ga79e5975d5ec6c0557af4a71004a6da93)typedef int (\*[gnss\_set\_fix\_rate\_t](group__gnss__interface.md#ga79e5975d5ec6c0557af4a71004a6da93))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) fix\_interval\_ms);

48

[ 50](group__gnss__interface.md#ga63a98e08bc7e4b9c70a27de48dc9cd8c)typedef int (\*[gnss\_get\_fix\_rate\_t](group__gnss__interface.md#ga63a98e08bc7e4b9c70a27de48dc9cd8c))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*fix\_interval\_ms);

51

[ 53](group__gnss__interface.md#gadb734bb12433276d3014e08a1d21bb18)enum [gnss\_navigation\_mode](group__gnss__interface.md#gadb734bb12433276d3014e08a1d21bb18) {

[ 55](group__gnss__interface.md#ggadb734bb12433276d3014e08a1d21bb18a96f01438a205c0d557eb5ea4f80425ff) [GNSS\_NAVIGATION\_MODE\_ZERO\_DYNAMICS](group__gnss__interface.md#ggadb734bb12433276d3014e08a1d21bb18a96f01438a205c0d557eb5ea4f80425ff) = 0,

[ 57](group__gnss__interface.md#ggadb734bb12433276d3014e08a1d21bb18ac5f4b57f2b0f732f9ae8051cb8ac9453) [GNSS\_NAVIGATION\_MODE\_LOW\_DYNAMICS](group__gnss__interface.md#ggadb734bb12433276d3014e08a1d21bb18ac5f4b57f2b0f732f9ae8051cb8ac9453) = 1,

[ 59](group__gnss__interface.md#ggadb734bb12433276d3014e08a1d21bb18ab7fd6073a1e7d28ebf6ae9bc51ded88d) [GNSS\_NAVIGATION\_MODE\_BALANCED\_DYNAMICS](group__gnss__interface.md#ggadb734bb12433276d3014e08a1d21bb18ab7fd6073a1e7d28ebf6ae9bc51ded88d) = 2,

[ 61](group__gnss__interface.md#ggadb734bb12433276d3014e08a1d21bb18a5f57c5f13e22a94c003f582e8c41a27f) [GNSS\_NAVIGATION\_MODE\_HIGH\_DYNAMICS](group__gnss__interface.md#ggadb734bb12433276d3014e08a1d21bb18a5f57c5f13e22a94c003f582e8c41a27f) = 3

62};

63

[ 65](group__gnss__interface.md#gae946fce6ecced7c8fa09e06d75855abe)typedef int (\*[gnss\_set\_navigation\_mode\_t](group__gnss__interface.md#gae946fce6ecced7c8fa09e06d75855abe))(const struct [device](structdevice.md) \*dev,

66 enum [gnss\_navigation\_mode](group__gnss__interface.md#gadb734bb12433276d3014e08a1d21bb18) mode);

67

[ 69](group__gnss__interface.md#ga9705b36019161fde431e78d943eff604)typedef int (\*[gnss\_get\_navigation\_mode\_t](group__gnss__interface.md#ga9705b36019161fde431e78d943eff604))(const struct [device](structdevice.md) \*dev,

70 enum [gnss\_navigation\_mode](group__gnss__interface.md#gadb734bb12433276d3014e08a1d21bb18) \*mode);

71

[ 73](group__gnss__interface.md#ga928a05b4e820a9fcc8bc2db81f5f8c79)enum [gnss\_system](group__gnss__interface.md#ga928a05b4e820a9fcc8bc2db81f5f8c79) {

[ 75](group__gnss__interface.md#gga928a05b4e820a9fcc8bc2db81f5f8c79a84d3fc7ebefad4b20c58335bb7ca3e33) [GNSS\_SYSTEM\_GPS](group__gnss__interface.md#gga928a05b4e820a9fcc8bc2db81f5f8c79a84d3fc7ebefad4b20c58335bb7ca3e33) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 77](group__gnss__interface.md#gga928a05b4e820a9fcc8bc2db81f5f8c79a6f5a6de0d8196df55ade83d1f09de7dd) [GNSS\_SYSTEM\_GLONASS](group__gnss__interface.md#gga928a05b4e820a9fcc8bc2db81f5f8c79a6f5a6de0d8196df55ade83d1f09de7dd) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 79](group__gnss__interface.md#gga928a05b4e820a9fcc8bc2db81f5f8c79a1456923f0dd999b26e167fccc2461d5c) [GNSS\_SYSTEM\_GALILEO](group__gnss__interface.md#gga928a05b4e820a9fcc8bc2db81f5f8c79a1456923f0dd999b26e167fccc2461d5c) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 81](group__gnss__interface.md#gga928a05b4e820a9fcc8bc2db81f5f8c79a25a0162daa071267b63d2c7331a46c55) [GNSS\_SYSTEM\_BEIDOU](group__gnss__interface.md#gga928a05b4e820a9fcc8bc2db81f5f8c79a25a0162daa071267b63d2c7331a46c55) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

[ 83](group__gnss__interface.md#gga928a05b4e820a9fcc8bc2db81f5f8c79aac9ccafec388c071468ef16981679dff) [GNSS\_SYSTEM\_QZSS](group__gnss__interface.md#gga928a05b4e820a9fcc8bc2db81f5f8c79aac9ccafec388c071468ef16981679dff) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

[ 85](group__gnss__interface.md#gga928a05b4e820a9fcc8bc2db81f5f8c79a833e14eb77d70b3c5eb2843026b63242) [GNSS\_SYSTEM\_IRNSS](group__gnss__interface.md#gga928a05b4e820a9fcc8bc2db81f5f8c79a833e14eb77d70b3c5eb2843026b63242) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

[ 87](group__gnss__interface.md#gga928a05b4e820a9fcc8bc2db81f5f8c79a3e759b71b7e531d6c2c3068108e263dd) [GNSS\_SYSTEM\_SBAS](group__gnss__interface.md#gga928a05b4e820a9fcc8bc2db81f5f8c79a3e759b71b7e531d6c2c3068108e263dd) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6),

[ 89](group__gnss__interface.md#gga928a05b4e820a9fcc8bc2db81f5f8c79a6a216ab95d09806435af4257b4d189e9) [GNSS\_SYSTEM\_IMES](group__gnss__interface.md#gga928a05b4e820a9fcc8bc2db81f5f8c79a6a216ab95d09806435af4257b4d189e9) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7),

90};

91

[ 93](group__gnss__interface.md#ga731907f9ae501909bf26ecae5441a5ce)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [gnss\_systems\_t](group__gnss__interface.md#ga731907f9ae501909bf26ecae5441a5ce);

94

[ 96](group__gnss__interface.md#ga91948cc0567c343bee62b6c70a2f461d)typedef int (\*[gnss\_set\_enabled\_systems\_t](group__gnss__interface.md#ga91948cc0567c343bee62b6c70a2f461d))(const struct [device](structdevice.md) \*dev, [gnss\_systems\_t](group__gnss__interface.md#ga731907f9ae501909bf26ecae5441a5ce) systems);

97

[ 99](group__gnss__interface.md#gad87bd07c46ea1f79caf9a484c51ec0c9)typedef int (\*[gnss\_get\_enabled\_systems\_t](group__gnss__interface.md#gad87bd07c46ea1f79caf9a484c51ec0c9))(const struct [device](structdevice.md) \*dev, [gnss\_systems\_t](group__gnss__interface.md#ga731907f9ae501909bf26ecae5441a5ce) \*systems);

100

[ 102](group__gnss__interface.md#gaf52a65dee0d28286ac40e5c8bc86825a)typedef int (\*[gnss\_get\_supported\_systems\_t](group__gnss__interface.md#gaf52a65dee0d28286ac40e5c8bc86825a))(const struct [device](structdevice.md) \*dev, [gnss\_systems\_t](group__gnss__interface.md#ga731907f9ae501909bf26ecae5441a5ce) \*systems);

103

[ 105](group__gnss__interface.md#gaa482aa8a996b743aba7e68f36b4780a8)typedef int (\*[gnss\_get\_latest\_timepulse\_t](group__gnss__interface.md#gaa482aa8a996b743aba7e68f36b4780a8))(const struct [device](structdevice.md) \*dev, [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) \*timestamp);

106

[ 108](group__gnss__interface.md#ga15536308e2229a45493d06e8b61e63d9)enum [gnss\_fix\_status](group__gnss__interface.md#ga15536308e2229a45493d06e8b61e63d9) {

[ 110](group__gnss__interface.md#gga15536308e2229a45493d06e8b61e63d9a508bbeea1550d5020e579e6a311fbdbe) [GNSS\_FIX\_STATUS\_NO\_FIX](group__gnss__interface.md#gga15536308e2229a45493d06e8b61e63d9a508bbeea1550d5020e579e6a311fbdbe) = 0,

[ 112](group__gnss__interface.md#gga15536308e2229a45493d06e8b61e63d9a8ad1fb7bf9f4d2607cb86f40a901e343) [GNSS\_FIX\_STATUS\_GNSS\_FIX](group__gnss__interface.md#gga15536308e2229a45493d06e8b61e63d9a8ad1fb7bf9f4d2607cb86f40a901e343) = 1,

[ 114](group__gnss__interface.md#gga15536308e2229a45493d06e8b61e63d9a213553f5fa30cfa99317fcc28d0af1cc) [GNSS\_FIX\_STATUS\_DGNSS\_FIX](group__gnss__interface.md#gga15536308e2229a45493d06e8b61e63d9a213553f5fa30cfa99317fcc28d0af1cc) = 2,

[ 116](group__gnss__interface.md#gga15536308e2229a45493d06e8b61e63d9a19c4e932246f410ee702122d80fbfbeb) [GNSS\_FIX\_STATUS\_ESTIMATED\_FIX](group__gnss__interface.md#gga15536308e2229a45493d06e8b61e63d9a19c4e932246f410ee702122d80fbfbeb) = 3,

117};

118

[ 120](group__gnss__interface.md#gacf5a3464c487ae7609d526c73ccc758a)enum [gnss\_fix\_quality](group__gnss__interface.md#gacf5a3464c487ae7609d526c73ccc758a) {

[ 122](group__gnss__interface.md#ggacf5a3464c487ae7609d526c73ccc758aa67256fb63beab67ba6e7cbb63916af30) [GNSS\_FIX\_QUALITY\_INVALID](group__gnss__interface.md#ggacf5a3464c487ae7609d526c73ccc758aa67256fb63beab67ba6e7cbb63916af30) = 0,

[ 124](group__gnss__interface.md#ggacf5a3464c487ae7609d526c73ccc758aa316ea7e84abca8f04bbf95d3d73cea3f) [GNSS\_FIX\_QUALITY\_GNSS\_SPS](group__gnss__interface.md#ggacf5a3464c487ae7609d526c73ccc758aa316ea7e84abca8f04bbf95d3d73cea3f) = 1,

[ 126](group__gnss__interface.md#ggacf5a3464c487ae7609d526c73ccc758aa65df312eef5cd8b24384440629f534f8) [GNSS\_FIX\_QUALITY\_DGNSS](group__gnss__interface.md#ggacf5a3464c487ae7609d526c73ccc758aa65df312eef5cd8b24384440629f534f8) = 2,

[ 128](group__gnss__interface.md#ggacf5a3464c487ae7609d526c73ccc758aab4de07a3891e7c89d5bd23fec7add20f) [GNSS\_FIX\_QUALITY\_GNSS\_PPS](group__gnss__interface.md#ggacf5a3464c487ae7609d526c73ccc758aab4de07a3891e7c89d5bd23fec7add20f) = 3,

[ 130](group__gnss__interface.md#ggacf5a3464c487ae7609d526c73ccc758aa5256b22bb56e93c788d52a641c2a15a6) [GNSS\_FIX\_QUALITY\_RTK](group__gnss__interface.md#ggacf5a3464c487ae7609d526c73ccc758aa5256b22bb56e93c788d52a641c2a15a6) = 4,

[ 132](group__gnss__interface.md#ggacf5a3464c487ae7609d526c73ccc758aaedd76bb21200df49fd82243d4a394ac6) [GNSS\_FIX\_QUALITY\_FLOAT\_RTK](group__gnss__interface.md#ggacf5a3464c487ae7609d526c73ccc758aaedd76bb21200df49fd82243d4a394ac6) = 5,

[ 134](group__gnss__interface.md#ggacf5a3464c487ae7609d526c73ccc758aa851d88a47c1314eed8bc25e5cc7ba35a) [GNSS\_FIX\_QUALITY\_ESTIMATED](group__gnss__interface.md#ggacf5a3464c487ae7609d526c73ccc758aa851d88a47c1314eed8bc25e5cc7ba35a) = 6,

135};

136

[ 138](structgnss__info.md)struct [gnss\_info](structgnss__info.md) {

[ 140](structgnss__info.md#a81160955c4b9d3a746280d88a74f07eb) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [satellites\_cnt](structgnss__info.md#a81160955c4b9d3a746280d88a74f07eb);

[ 142](structgnss__info.md#a5de15dd2a9843c05b8805d4519b49a73) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [hdop](structgnss__info.md#a5de15dd2a9843c05b8805d4519b49a73);

[ 144](structgnss__info.md#a718e95833c4d07ad530669035ca21f8c) enum [gnss\_fix\_status](group__gnss__interface.md#ga15536308e2229a45493d06e8b61e63d9) [fix\_status](structgnss__info.md#a718e95833c4d07ad530669035ca21f8c);

[ 146](structgnss__info.md#a54396dd23fd05185bcb1104ee529984e) enum [gnss\_fix\_quality](group__gnss__interface.md#gacf5a3464c487ae7609d526c73ccc758a) [fix\_quality](structgnss__info.md#a54396dd23fd05185bcb1104ee529984e);

147};

148

[ 150](structgnss__time.md)struct [gnss\_time](structgnss__time.md) {

[ 152](structgnss__time.md#a5c8a280736741d8d07dacba30d48ed6f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [hour](structgnss__time.md#a5c8a280736741d8d07dacba30d48ed6f);

[ 154](structgnss__time.md#a3e8b96861e45cc2a6222961e92ab62f5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [minute](structgnss__time.md#a3e8b96861e45cc2a6222961e92ab62f5);

[ 156](structgnss__time.md#a2ab6b41452491ec34966fda0ddbdd9da) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [millisecond](structgnss__time.md#a2ab6b41452491ec34966fda0ddbdd9da);

[ 158](structgnss__time.md#a766744149009588f83cca930ef53ff10) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [month\_day](structgnss__time.md#a766744149009588f83cca930ef53ff10);

[ 160](structgnss__time.md#a1c6730dc08cd3dfb48aee08154f5f2de) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [month](structgnss__time.md#a1c6730dc08cd3dfb48aee08154f5f2de);

[ 162](structgnss__time.md#a4daa514f38a7b7d88bf49cb5d664b2ac) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [century\_year](structgnss__time.md#a4daa514f38a7b7d88bf49cb5d664b2ac);

163};

164

[ 166](structgnss__driver__api.md)\_\_subsystem struct [gnss\_driver\_api](structgnss__driver__api.md) {

[ 167](structgnss__driver__api.md#a0d79083d56a7a35c3a2c858e2c6627f5) [gnss\_set\_fix\_rate\_t](group__gnss__interface.md#ga79e5975d5ec6c0557af4a71004a6da93) [set\_fix\_rate](structgnss__driver__api.md#a0d79083d56a7a35c3a2c858e2c6627f5);

[ 168](structgnss__driver__api.md#abd0d989e810fa0bdffe0f68a10622bbf) [gnss\_get\_fix\_rate\_t](group__gnss__interface.md#ga63a98e08bc7e4b9c70a27de48dc9cd8c) [get\_fix\_rate](structgnss__driver__api.md#abd0d989e810fa0bdffe0f68a10622bbf);

[ 169](structgnss__driver__api.md#a7b77dbf9b49fec76dd9374b97a025b08) [gnss\_set\_navigation\_mode\_t](group__gnss__interface.md#gae946fce6ecced7c8fa09e06d75855abe) [set\_navigation\_mode](structgnss__driver__api.md#a7b77dbf9b49fec76dd9374b97a025b08);

[ 170](structgnss__driver__api.md#a77247b70ca41bea5b29f579e67c878a9) [gnss\_get\_navigation\_mode\_t](group__gnss__interface.md#ga9705b36019161fde431e78d943eff604) [get\_navigation\_mode](structgnss__driver__api.md#a77247b70ca41bea5b29f579e67c878a9);

[ 171](structgnss__driver__api.md#a1f4c78c928301ede626a9bcb92c5050d) [gnss\_set\_enabled\_systems\_t](group__gnss__interface.md#ga91948cc0567c343bee62b6c70a2f461d) [set\_enabled\_systems](structgnss__driver__api.md#a1f4c78c928301ede626a9bcb92c5050d);

[ 172](structgnss__driver__api.md#abc82a5f3ede200cd40982581ddf9d02f) [gnss\_get\_enabled\_systems\_t](group__gnss__interface.md#gad87bd07c46ea1f79caf9a484c51ec0c9) [get\_enabled\_systems](structgnss__driver__api.md#abc82a5f3ede200cd40982581ddf9d02f);

[ 173](structgnss__driver__api.md#af3ad59e6495183f9b45dfbfe0e54fbb6) [gnss\_get\_supported\_systems\_t](group__gnss__interface.md#gaf52a65dee0d28286ac40e5c8bc86825a) [get\_supported\_systems](structgnss__driver__api.md#af3ad59e6495183f9b45dfbfe0e54fbb6);

[ 174](structgnss__driver__api.md#a2a1604472e2a0249a766534b05a11133) [gnss\_get\_latest\_timepulse\_t](group__gnss__interface.md#gaa482aa8a996b743aba7e68f36b4780a8) [get\_latest\_timepulse](structgnss__driver__api.md#a2a1604472e2a0249a766534b05a11133);

175};

176

[ 178](structgnss__data.md)struct [gnss\_data](structgnss__data.md) {

[ 180](structgnss__data.md#a2470031921179cb30172441163d80052) struct [navigation\_data](structnavigation__data.md) [nav\_data](structgnss__data.md#a2470031921179cb30172441163d80052);

[ 182](structgnss__data.md#a78155e6d2c981b9121b2ee42c1700988) struct [gnss\_info](structgnss__info.md) [info](structgnss__data.md#a78155e6d2c981b9121b2ee42c1700988);

[ 184](structgnss__data.md#ae6bfc0c6a53901963a1d20bad025fb99) struct [gnss\_time](structgnss__time.md) [utc](structgnss__data.md#ae6bfc0c6a53901963a1d20bad025fb99);

185};

186

[ 188](group__gnss__interface.md#ga025c965369275ad8e5ab5ad44c14a23b)typedef void (\*[gnss\_data\_callback\_t](group__gnss__interface.md#ga025c965369275ad8e5ab5ad44c14a23b))(const struct [device](structdevice.md) \*dev, const struct [gnss\_data](structgnss__data.md) \*data);

189

[ 191](structgnss__data__callback.md)struct [gnss\_data\_callback](structgnss__data__callback.md) {

[ 193](structgnss__data__callback.md#afdf273ceed2d2038b6415840f9ecdd7b) const struct [device](structdevice.md) \*[dev](structgnss__data__callback.md#afdf273ceed2d2038b6415840f9ecdd7b);

[ 195](structgnss__data__callback.md#a07e9c7fd6192fd5b58ff37aabdbff11e) [gnss\_data\_callback\_t](group__gnss__interface.md#ga025c965369275ad8e5ab5ad44c14a23b) [callback](structgnss__data__callback.md#a07e9c7fd6192fd5b58ff37aabdbff11e);

196};

197

[ 199](structgnss__satellite.md)struct [gnss\_satellite](structgnss__satellite.md) {

[ 201](structgnss__satellite.md#a03543a7425f27c78e743b0ec180ccea7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [prn](structgnss__satellite.md#a03543a7425f27c78e743b0ec180ccea7);

[ 203](structgnss__satellite.md#a6818083aad878aa8b06d2cbeca53b1da) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [snr](structgnss__satellite.md#a6818083aad878aa8b06d2cbeca53b1da);

[ 205](structgnss__satellite.md#a3d99c5ad18242a42f95b5de496ca501d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [elevation](structgnss__satellite.md#a3d99c5ad18242a42f95b5de496ca501d);

[ 207](structgnss__satellite.md#a27a864422f5207b5d38efbd8b50893a3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [azimuth](structgnss__satellite.md#a27a864422f5207b5d38efbd8b50893a3);

[ 209](structgnss__satellite.md#ad9b31c85dd0e162979d384b049142549) enum [gnss\_system](group__gnss__interface.md#ga928a05b4e820a9fcc8bc2db81f5f8c79) [system](structgnss__satellite.md#ad9b31c85dd0e162979d384b049142549);

[ 211](structgnss__satellite.md#ae4c596c298ed158a188ea4a5fbd6181c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [is\_tracked](structgnss__satellite.md#ae4c596c298ed158a188ea4a5fbd6181c) : 1;

212};

213

[ 215](group__gnss__interface.md#ga80cf700468d1c942cfa064368e212e6f)typedef void (\*[gnss\_satellites\_callback\_t](group__gnss__interface.md#ga80cf700468d1c942cfa064368e212e6f))(const struct [device](structdevice.md) \*dev,

216 const struct [gnss\_satellite](structgnss__satellite.md) \*satellites,

217 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) size);

218

[ 220](structgnss__satellites__callback.md)struct [gnss\_satellites\_callback](structgnss__satellites__callback.md) {

[ 222](structgnss__satellites__callback.md#a19e64ff2450c00080ae39528f7d07b2b) const struct [device](structdevice.md) \*[dev](structgnss__satellites__callback.md#a19e64ff2450c00080ae39528f7d07b2b);

[ 224](structgnss__satellites__callback.md#af12fc64ff9c696b5862b5adfef31269b) [gnss\_satellites\_callback\_t](group__gnss__interface.md#ga80cf700468d1c942cfa064368e212e6f) [callback](structgnss__satellites__callback.md#af12fc64ff9c696b5862b5adfef31269b);

225};

226

[ 236](group__gnss__interface.md#ga16e8326737f114bd6017983812c7f28d)\_\_syscall int [gnss\_set\_fix\_rate](group__gnss__interface.md#ga16e8326737f114bd6017983812c7f28d)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) fix\_interval\_ms);

237

238static inline int z\_impl\_gnss\_set\_fix\_rate(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) fix\_interval\_ms)

239{

240 const struct [gnss\_driver\_api](structgnss__driver__api.md) \*api = (const struct [gnss\_driver\_api](structgnss__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

241

242 if (api->set\_fix\_rate == NULL) {

243 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

244 }

245

246 return api->set\_fix\_rate(dev, fix\_interval\_ms);

247}

248

[ 258](group__gnss__interface.md#ga8e625fb3f8758eab78c115d12bef6a72)\_\_syscall int [gnss\_get\_fix\_rate](group__gnss__interface.md#ga8e625fb3f8758eab78c115d12bef6a72)(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*fix\_interval\_ms);

259

260static inline int z\_impl\_gnss\_get\_fix\_rate(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*fix\_interval\_ms)

261{

262 const struct [gnss\_driver\_api](structgnss__driver__api.md) \*api = (const struct [gnss\_driver\_api](structgnss__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

263

264 if (api->get\_fix\_rate == NULL) {

265 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

266 }

267

268 return api->get\_fix\_rate(dev, fix\_interval\_ms);

269}

270

[ 280](group__gnss__interface.md#ga9d0347640e68d5702b1cb43ddf8380df)\_\_syscall int [gnss\_set\_navigation\_mode](group__gnss__interface.md#ga9d0347640e68d5702b1cb43ddf8380df)(const struct [device](structdevice.md) \*dev,

281 enum [gnss\_navigation\_mode](group__gnss__interface.md#gadb734bb12433276d3014e08a1d21bb18) mode);

282

283static inline int z\_impl\_gnss\_set\_navigation\_mode(const struct [device](structdevice.md) \*dev,

284 enum [gnss\_navigation\_mode](group__gnss__interface.md#gadb734bb12433276d3014e08a1d21bb18) mode)

285{

286 const struct [gnss\_driver\_api](structgnss__driver__api.md) \*api = (const struct [gnss\_driver\_api](structgnss__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

287

288 if (api->set\_navigation\_mode == NULL) {

289 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

290 }

291

292 return api->set\_navigation\_mode(dev, mode);

293}

294

[ 304](group__gnss__interface.md#gae5614f8125dad02a3ebd30400b575e6d)\_\_syscall int [gnss\_get\_navigation\_mode](group__gnss__interface.md#gae5614f8125dad02a3ebd30400b575e6d)(const struct [device](structdevice.md) \*dev,

305 enum [gnss\_navigation\_mode](group__gnss__interface.md#gadb734bb12433276d3014e08a1d21bb18) \*mode);

306

307static inline int z\_impl\_gnss\_get\_navigation\_mode(const struct [device](structdevice.md) \*dev,

308 enum [gnss\_navigation\_mode](group__gnss__interface.md#gadb734bb12433276d3014e08a1d21bb18) \*mode)

309{

310 const struct [gnss\_driver\_api](structgnss__driver__api.md) \*api = (const struct [gnss\_driver\_api](structgnss__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

311

312 if (api->get\_navigation\_mode == NULL) {

313 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

314 }

315

316 return api->get\_navigation\_mode(dev, mode);

317}

318

[ 328](group__gnss__interface.md#ga818e42c7a979623679eba26887662823)\_\_syscall int [gnss\_set\_enabled\_systems](group__gnss__interface.md#ga818e42c7a979623679eba26887662823)(const struct [device](structdevice.md) \*dev, [gnss\_systems\_t](group__gnss__interface.md#ga731907f9ae501909bf26ecae5441a5ce) systems);

329

330static inline int z\_impl\_gnss\_set\_enabled\_systems(const struct [device](structdevice.md) \*dev,

331 [gnss\_systems\_t](group__gnss__interface.md#ga731907f9ae501909bf26ecae5441a5ce) systems)

332{

333 const struct [gnss\_driver\_api](structgnss__driver__api.md) \*api = (const struct [gnss\_driver\_api](structgnss__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

334

335 if (api->set\_enabled\_systems == NULL) {

336 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

337 }

338

339 return api->set\_enabled\_systems(dev, systems);

340}

341

[ 351](group__gnss__interface.md#ga155126e113195c08158ef49e2a6b4f6a)\_\_syscall int [gnss\_get\_enabled\_systems](group__gnss__interface.md#ga155126e113195c08158ef49e2a6b4f6a)(const struct [device](structdevice.md) \*dev, [gnss\_systems\_t](group__gnss__interface.md#ga731907f9ae501909bf26ecae5441a5ce) \*systems);

352

353static inline int z\_impl\_gnss\_get\_enabled\_systems(const struct [device](structdevice.md) \*dev,

354 [gnss\_systems\_t](group__gnss__interface.md#ga731907f9ae501909bf26ecae5441a5ce) \*systems)

355{

356 const struct [gnss\_driver\_api](structgnss__driver__api.md) \*api = (const struct [gnss\_driver\_api](structgnss__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

357

358 if (api->get\_enabled\_systems == NULL) {

359 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

360 }

361

362 return api->get\_enabled\_systems(dev, systems);

363}

364

[ 374](group__gnss__interface.md#ga598609846ff196ff300fcad8237b2d51)\_\_syscall int [gnss\_get\_supported\_systems](group__gnss__interface.md#ga598609846ff196ff300fcad8237b2d51)(const struct [device](structdevice.md) \*dev, [gnss\_systems\_t](group__gnss__interface.md#ga731907f9ae501909bf26ecae5441a5ce) \*systems);

375

376static inline int z\_impl\_gnss\_get\_supported\_systems(const struct [device](structdevice.md) \*dev,

377 [gnss\_systems\_t](group__gnss__interface.md#ga731907f9ae501909bf26ecae5441a5ce) \*systems)

378{

379 const struct [gnss\_driver\_api](structgnss__driver__api.md) \*api = (const struct [gnss\_driver\_api](structgnss__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

380

381 if (api->get\_supported\_systems == NULL) {

382 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

383 }

384

385 return api->get\_supported\_systems(dev, systems);

386}

387

[ 401](group__gnss__interface.md#ga8eb37446d71c020e0517a406ea240fc2)\_\_syscall int [gnss\_get\_latest\_timepulse](group__gnss__interface.md#ga8eb37446d71c020e0517a406ea240fc2)(const struct [device](structdevice.md) \*dev, [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) \*timestamp);

402

403static inline int z\_impl\_gnss\_get\_latest\_timepulse(const struct [device](structdevice.md) \*dev,

404 [k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2) \*timestamp)

405{

406 const struct [gnss\_driver\_api](structgnss__driver__api.md) \*api = (const struct [gnss\_driver\_api](structgnss__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

407

408 if (api->get\_latest\_timepulse == NULL) {

409 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

410 }

411

412 return api->get\_latest\_timepulse(dev, timestamp);

413}

414

421#if CONFIG\_GNSS

422#define GNSS\_DATA\_CALLBACK\_DEFINE(\_dev, \_callback) \

423 static const STRUCT\_SECTION\_ITERABLE(gnss\_data\_callback, \

424 \_gnss\_data\_callback\_\_##\_callback) = { \

425 .dev = \_dev, \

426 .callback = \_callback, \

427 }

428#else

[ 429](group__gnss__interface.md#gae9c3fd5804bd6f8e6790cb1b7e47e4a6)#define GNSS\_DATA\_CALLBACK\_DEFINE(\_dev, \_callback)

430#endif

431

438#if CONFIG\_GNSS\_SATELLITES

439#define GNSS\_SATELLITES\_CALLBACK\_DEFINE(\_dev, \_callback) \

440 static const STRUCT\_SECTION\_ITERABLE(gnss\_satellites\_callback, \

441 \_gnss\_satellites\_callback\_\_##\_callback) = { \

442 .dev = \_dev, \

443 .callback = \_callback, \

444 }

445#else

[ 446](group__gnss__interface.md#ga414a414635e1cd00ef800edaf70bc234)#define GNSS\_SATELLITES\_CALLBACK\_DEFINE(\_dev, \_callback)

447#endif

448

452

453#ifdef \_\_cplusplus

454}

455#endif

456

457#include <zephyr/syscalls/gnss.h>

458

459#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_GNSS\_H\_ \*/

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[k\_ticks\_t](group__clock__apis.md#ga9832cb0adc2d1866420e5c370a0863e2)

uint32\_t k\_ticks\_t

Tick precision used in timeout APIs.

**Definition** sys\_clock.h:48

[gnss\_data\_callback\_t](group__gnss__interface.md#ga025c965369275ad8e5ab5ad44c14a23b)

void(\* gnss\_data\_callback\_t)(const struct device \*dev, const struct gnss\_data \*data)

Template for GNSS data callback.

**Definition** gnss.h:188

[gnss\_get\_enabled\_systems](group__gnss__interface.md#ga155126e113195c08158ef49e2a6b4f6a)

int gnss\_get\_enabled\_systems(const struct device \*dev, gnss\_systems\_t \*systems)

Get enabled GNSS systems.

[gnss\_fix\_status](group__gnss__interface.md#ga15536308e2229a45493d06e8b61e63d9)

gnss\_fix\_status

GNSS fix status.

**Definition** gnss.h:108

[gnss\_set\_fix\_rate](group__gnss__interface.md#ga16e8326737f114bd6017983812c7f28d)

int gnss\_set\_fix\_rate(const struct device \*dev, uint32\_t fix\_interval\_ms)

Set the GNSS fix rate.

[gnss\_pps\_mode](group__gnss__interface.md#ga2b43ac2fec33053a769b7070c4ed3263)

gnss\_pps\_mode

GNSS PPS modes.

**Definition** gnss.h:35

[gnss\_get\_supported\_systems](group__gnss__interface.md#ga598609846ff196ff300fcad8237b2d51)

int gnss\_get\_supported\_systems(const struct device \*dev, gnss\_systems\_t \*systems)

Get supported GNSS systems.

[gnss\_get\_fix\_rate\_t](group__gnss__interface.md#ga63a98e08bc7e4b9c70a27de48dc9cd8c)

int(\* gnss\_get\_fix\_rate\_t)(const struct device \*dev, uint32\_t \*fix\_interval\_ms)

API for getting fix rate.

**Definition** gnss.h:50

[gnss\_systems\_t](group__gnss__interface.md#ga731907f9ae501909bf26ecae5441a5ce)

uint32\_t gnss\_systems\_t

Type storing bitmask of GNSS systems.

**Definition** gnss.h:93

[gnss\_set\_fix\_rate\_t](group__gnss__interface.md#ga79e5975d5ec6c0557af4a71004a6da93)

int(\* gnss\_set\_fix\_rate\_t)(const struct device \*dev, uint32\_t fix\_interval\_ms)

API for setting fix rate.

**Definition** gnss.h:47

[gnss\_satellites\_callback\_t](group__gnss__interface.md#ga80cf700468d1c942cfa064368e212e6f)

void(\* gnss\_satellites\_callback\_t)(const struct device \*dev, const struct gnss\_satellite \*satellites, uint16\_t size)

Template for GNSS satellites callback.

**Definition** gnss.h:215

[gnss\_set\_enabled\_systems](group__gnss__interface.md#ga818e42c7a979623679eba26887662823)

int gnss\_set\_enabled\_systems(const struct device \*dev, gnss\_systems\_t systems)

Set enabled GNSS systems.

[gnss\_get\_fix\_rate](group__gnss__interface.md#ga8e625fb3f8758eab78c115d12bef6a72)

int gnss\_get\_fix\_rate(const struct device \*dev, uint32\_t \*fix\_interval\_ms)

Get the GNSS fix rate.

[gnss\_get\_latest\_timepulse](group__gnss__interface.md#ga8eb37446d71c020e0517a406ea240fc2)

int gnss\_get\_latest\_timepulse(const struct device \*dev, k\_ticks\_t \*timestamp)

Get the timestamp of the latest PPS timepulse.

[gnss\_set\_enabled\_systems\_t](group__gnss__interface.md#ga91948cc0567c343bee62b6c70a2f461d)

int(\* gnss\_set\_enabled\_systems\_t)(const struct device \*dev, gnss\_systems\_t systems)

API for enabling systems.

**Definition** gnss.h:96

[gnss\_system](group__gnss__interface.md#ga928a05b4e820a9fcc8bc2db81f5f8c79)

gnss\_system

Systems contained in gnss\_systems\_t.

**Definition** gnss.h:73

[gnss\_get\_navigation\_mode\_t](group__gnss__interface.md#ga9705b36019161fde431e78d943eff604)

int(\* gnss\_get\_navigation\_mode\_t)(const struct device \*dev, enum gnss\_navigation\_mode \*mode)

API for getting navigation mode.

**Definition** gnss.h:69

[gnss\_set\_navigation\_mode](group__gnss__interface.md#ga9d0347640e68d5702b1cb43ddf8380df)

int gnss\_set\_navigation\_mode(const struct device \*dev, enum gnss\_navigation\_mode mode)

Set the GNSS navigation mode.

[gnss\_get\_latest\_timepulse\_t](group__gnss__interface.md#gaa482aa8a996b743aba7e68f36b4780a8)

int(\* gnss\_get\_latest\_timepulse\_t)(const struct device \*dev, k\_ticks\_t \*timestamp)

API for getting timestamp of last PPS pulse.

**Definition** gnss.h:105

[gnss\_fix\_quality](group__gnss__interface.md#gacf5a3464c487ae7609d526c73ccc758a)

gnss\_fix\_quality

GNSS fix quality.

**Definition** gnss.h:120

[gnss\_get\_enabled\_systems\_t](group__gnss__interface.md#gad87bd07c46ea1f79caf9a484c51ec0c9)

int(\* gnss\_get\_enabled\_systems\_t)(const struct device \*dev, gnss\_systems\_t \*systems)

API for getting enabled systems.

**Definition** gnss.h:99

[gnss\_navigation\_mode](group__gnss__interface.md#gadb734bb12433276d3014e08a1d21bb18)

gnss\_navigation\_mode

GNSS navigation modes.

**Definition** gnss.h:53

[gnss\_get\_navigation\_mode](group__gnss__interface.md#gae5614f8125dad02a3ebd30400b575e6d)

int gnss\_get\_navigation\_mode(const struct device \*dev, enum gnss\_navigation\_mode \*mode)

Get the GNSS navigation mode.

[gnss\_set\_navigation\_mode\_t](group__gnss__interface.md#gae946fce6ecced7c8fa09e06d75855abe)

int(\* gnss\_set\_navigation\_mode\_t)(const struct device \*dev, enum gnss\_navigation\_mode mode)

API for setting navigation mode.

**Definition** gnss.h:65

[gnss\_get\_supported\_systems\_t](group__gnss__interface.md#gaf52a65dee0d28286ac40e5c8bc86825a)

int(\* gnss\_get\_supported\_systems\_t)(const struct device \*dev, gnss\_systems\_t \*systems)

API for getting enabled systems.

**Definition** gnss.h:102

[GNSS\_FIX\_STATUS\_ESTIMATED\_FIX](group__gnss__interface.md#gga15536308e2229a45493d06e8b61e63d9a19c4e932246f410ee702122d80fbfbeb)

@ GNSS\_FIX\_STATUS\_ESTIMATED\_FIX

Estimated fix acquired.

**Definition** gnss.h:116

[GNSS\_FIX\_STATUS\_DGNSS\_FIX](group__gnss__interface.md#gga15536308e2229a45493d06e8b61e63d9a213553f5fa30cfa99317fcc28d0af1cc)

@ GNSS\_FIX\_STATUS\_DGNSS\_FIX

Differential GNSS fix acquired.

**Definition** gnss.h:114

[GNSS\_FIX\_STATUS\_NO\_FIX](group__gnss__interface.md#gga15536308e2229a45493d06e8b61e63d9a508bbeea1550d5020e579e6a311fbdbe)

@ GNSS\_FIX\_STATUS\_NO\_FIX

No GNSS fix acquired.

**Definition** gnss.h:110

[GNSS\_FIX\_STATUS\_GNSS\_FIX](group__gnss__interface.md#gga15536308e2229a45493d06e8b61e63d9a8ad1fb7bf9f4d2607cb86f40a901e343)

@ GNSS\_FIX\_STATUS\_GNSS\_FIX

GNSS fix acquired.

**Definition** gnss.h:112

[GNSS\_PPS\_MODE\_ENABLED\_AFTER\_LOCK](group__gnss__interface.md#gga2b43ac2fec33053a769b7070c4ed3263a2df416ad912a84135eff1e30977b4507)

@ GNSS\_PPS\_MODE\_ENABLED\_AFTER\_LOCK

PPS output enabled from first lock.

**Definition** gnss.h:41

[GNSS\_PPS\_MODE\_DISABLED](group__gnss__interface.md#gga2b43ac2fec33053a769b7070c4ed3263a5e9af4b08bd41a1aa1bf01c0e290d9fc)

@ GNSS\_PPS\_MODE\_DISABLED

PPS output disabled.

**Definition** gnss.h:37

[GNSS\_PPS\_MODE\_ENABLED](group__gnss__interface.md#gga2b43ac2fec33053a769b7070c4ed3263a9cdbb144191c83f4a7a2cc27268eacfa)

@ GNSS\_PPS\_MODE\_ENABLED

PPS output always enabled.

**Definition** gnss.h:39

[GNSS\_PPS\_MODE\_ENABLED\_WHILE\_LOCKED](group__gnss__interface.md#gga2b43ac2fec33053a769b7070c4ed3263afc82bd9ebcfd9d3b6111c9e82fc79ecc)

@ GNSS\_PPS\_MODE\_ENABLED\_WHILE\_LOCKED

PPS output enabled while locked.

**Definition** gnss.h:43

[GNSS\_SYSTEM\_GALILEO](group__gnss__interface.md#gga928a05b4e820a9fcc8bc2db81f5f8c79a1456923f0dd999b26e167fccc2461d5c)

@ GNSS\_SYSTEM\_GALILEO

Galileo.

**Definition** gnss.h:79

[GNSS\_SYSTEM\_BEIDOU](group__gnss__interface.md#gga928a05b4e820a9fcc8bc2db81f5f8c79a25a0162daa071267b63d2c7331a46c55)

@ GNSS\_SYSTEM\_BEIDOU

BeiDou Navigation Satellite System.

**Definition** gnss.h:81

[GNSS\_SYSTEM\_SBAS](group__gnss__interface.md#gga928a05b4e820a9fcc8bc2db81f5f8c79a3e759b71b7e531d6c2c3068108e263dd)

@ GNSS\_SYSTEM\_SBAS

Satellite-Based Augmentation System (SBAS).

**Definition** gnss.h:87

[GNSS\_SYSTEM\_IMES](group__gnss__interface.md#gga928a05b4e820a9fcc8bc2db81f5f8c79a6a216ab95d09806435af4257b4d189e9)

@ GNSS\_SYSTEM\_IMES

Indoor Messaging System (IMES).

**Definition** gnss.h:89

[GNSS\_SYSTEM\_GLONASS](group__gnss__interface.md#gga928a05b4e820a9fcc8bc2db81f5f8c79a6f5a6de0d8196df55ade83d1f09de7dd)

@ GNSS\_SYSTEM\_GLONASS

GLObal NAvigation Satellite System (GLONASS).

**Definition** gnss.h:77

[GNSS\_SYSTEM\_IRNSS](group__gnss__interface.md#gga928a05b4e820a9fcc8bc2db81f5f8c79a833e14eb77d70b3c5eb2843026b63242)

@ GNSS\_SYSTEM\_IRNSS

Indian Regional Navigation Satellite System (IRNSS).

**Definition** gnss.h:85

[GNSS\_SYSTEM\_GPS](group__gnss__interface.md#gga928a05b4e820a9fcc8bc2db81f5f8c79a84d3fc7ebefad4b20c58335bb7ca3e33)

@ GNSS\_SYSTEM\_GPS

Global Positioning System (GPS).

**Definition** gnss.h:75

[GNSS\_SYSTEM\_QZSS](group__gnss__interface.md#gga928a05b4e820a9fcc8bc2db81f5f8c79aac9ccafec388c071468ef16981679dff)

@ GNSS\_SYSTEM\_QZSS

Quasi-Zenith Satellite System (QZSS).

**Definition** gnss.h:83

[GNSS\_FIX\_QUALITY\_GNSS\_SPS](group__gnss__interface.md#ggacf5a3464c487ae7609d526c73ccc758aa316ea7e84abca8f04bbf95d3d73cea3f)

@ GNSS\_FIX\_QUALITY\_GNSS\_SPS

Standard positioning service.

**Definition** gnss.h:124

[GNSS\_FIX\_QUALITY\_RTK](group__gnss__interface.md#ggacf5a3464c487ae7609d526c73ccc758aa5256b22bb56e93c788d52a641c2a15a6)

@ GNSS\_FIX\_QUALITY\_RTK

Real-time kinematic.

**Definition** gnss.h:130

[GNSS\_FIX\_QUALITY\_DGNSS](group__gnss__interface.md#ggacf5a3464c487ae7609d526c73ccc758aa65df312eef5cd8b24384440629f534f8)

@ GNSS\_FIX\_QUALITY\_DGNSS

Differential GNSS.

**Definition** gnss.h:126

[GNSS\_FIX\_QUALITY\_INVALID](group__gnss__interface.md#ggacf5a3464c487ae7609d526c73ccc758aa67256fb63beab67ba6e7cbb63916af30)

@ GNSS\_FIX\_QUALITY\_INVALID

Invalid fix.

**Definition** gnss.h:122

[GNSS\_FIX\_QUALITY\_ESTIMATED](group__gnss__interface.md#ggacf5a3464c487ae7609d526c73ccc758aa851d88a47c1314eed8bc25e5cc7ba35a)

@ GNSS\_FIX\_QUALITY\_ESTIMATED

Estimated fix.

**Definition** gnss.h:134

[GNSS\_FIX\_QUALITY\_GNSS\_PPS](group__gnss__interface.md#ggacf5a3464c487ae7609d526c73ccc758aab4de07a3891e7c89d5bd23fec7add20f)

@ GNSS\_FIX\_QUALITY\_GNSS\_PPS

Precise positioning service.

**Definition** gnss.h:128

[GNSS\_FIX\_QUALITY\_FLOAT\_RTK](group__gnss__interface.md#ggacf5a3464c487ae7609d526c73ccc758aaedd76bb21200df49fd82243d4a394ac6)

@ GNSS\_FIX\_QUALITY\_FLOAT\_RTK

Floating real-time kinematic.

**Definition** gnss.h:132

[GNSS\_NAVIGATION\_MODE\_HIGH\_DYNAMICS](group__gnss__interface.md#ggadb734bb12433276d3014e08a1d21bb18a5f57c5f13e22a94c003f582e8c41a27f)

@ GNSS\_NAVIGATION\_MODE\_HIGH\_DYNAMICS

High dynamics have higher impact on tracking.

**Definition** gnss.h:61

[GNSS\_NAVIGATION\_MODE\_ZERO\_DYNAMICS](group__gnss__interface.md#ggadb734bb12433276d3014e08a1d21bb18a96f01438a205c0d557eb5ea4f80425ff)

@ GNSS\_NAVIGATION\_MODE\_ZERO\_DYNAMICS

Dynamics have no impact on tracking.

**Definition** gnss.h:55

[GNSS\_NAVIGATION\_MODE\_BALANCED\_DYNAMICS](group__gnss__interface.md#ggadb734bb12433276d3014e08a1d21bb18ab7fd6073a1e7d28ebf6ae9bc51ded88d)

@ GNSS\_NAVIGATION\_MODE\_BALANCED\_DYNAMICS

Low and high dynamics have equal impact on tracking.

**Definition** gnss.h:59

[GNSS\_NAVIGATION\_MODE\_LOW\_DYNAMICS](group__gnss__interface.md#ggadb734bb12433276d3014e08a1d21bb18ac5f4b57f2b0f732f9ae8051cb8ac9453)

@ GNSS\_NAVIGATION\_MODE\_LOW\_DYNAMICS

Low dynamics have higher impact on tracking.

**Definition** gnss.h:57

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[types.h](include_2zephyr_2types_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[navigation.h](navigation_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:418

[gnss\_data\_callback](structgnss__data__callback.md)

GNSS callback structure.

**Definition** gnss.h:191

[gnss\_data\_callback::callback](structgnss__data__callback.md#a07e9c7fd6192fd5b58ff37aabdbff11e)

gnss\_data\_callback\_t callback

Callback called when GNSS data is published.

**Definition** gnss.h:195

[gnss\_data\_callback::dev](structgnss__data__callback.md#afdf273ceed2d2038b6415840f9ecdd7b)

const struct device \* dev

Filter callback to GNSS data from this device if not NULL.

**Definition** gnss.h:193

[gnss\_data](structgnss__data.md)

GNSS data structure.

**Definition** gnss.h:178

[gnss\_data::nav\_data](structgnss__data.md#a2470031921179cb30172441163d80052)

struct navigation\_data nav\_data

Navigation data acquired.

**Definition** gnss.h:180

[gnss\_data::info](structgnss__data.md#a78155e6d2c981b9121b2ee42c1700988)

struct gnss\_info info

GNSS info when navigation data was acquired.

**Definition** gnss.h:182

[gnss\_data::utc](structgnss__data.md#ae6bfc0c6a53901963a1d20bad025fb99)

struct gnss\_time utc

UTC time when data was acquired.

**Definition** gnss.h:184

[gnss\_driver\_api](structgnss__driver__api.md)

GNSS API structure.

**Definition** gnss.h:166

[gnss\_driver\_api::set\_fix\_rate](structgnss__driver__api.md#a0d79083d56a7a35c3a2c858e2c6627f5)

gnss\_set\_fix\_rate\_t set\_fix\_rate

**Definition** gnss.h:167

[gnss\_driver\_api::set\_enabled\_systems](structgnss__driver__api.md#a1f4c78c928301ede626a9bcb92c5050d)

gnss\_set\_enabled\_systems\_t set\_enabled\_systems

**Definition** gnss.h:171

[gnss\_driver\_api::get\_latest\_timepulse](structgnss__driver__api.md#a2a1604472e2a0249a766534b05a11133)

gnss\_get\_latest\_timepulse\_t get\_latest\_timepulse

**Definition** gnss.h:174

[gnss\_driver\_api::get\_navigation\_mode](structgnss__driver__api.md#a77247b70ca41bea5b29f579e67c878a9)

gnss\_get\_navigation\_mode\_t get\_navigation\_mode

**Definition** gnss.h:170

[gnss\_driver\_api::set\_navigation\_mode](structgnss__driver__api.md#a7b77dbf9b49fec76dd9374b97a025b08)

gnss\_set\_navigation\_mode\_t set\_navigation\_mode

**Definition** gnss.h:169

[gnss\_driver\_api::get\_enabled\_systems](structgnss__driver__api.md#abc82a5f3ede200cd40982581ddf9d02f)

gnss\_get\_enabled\_systems\_t get\_enabled\_systems

**Definition** gnss.h:172

[gnss\_driver\_api::get\_fix\_rate](structgnss__driver__api.md#abd0d989e810fa0bdffe0f68a10622bbf)

gnss\_get\_fix\_rate\_t get\_fix\_rate

**Definition** gnss.h:168

[gnss\_driver\_api::get\_supported\_systems](structgnss__driver__api.md#af3ad59e6495183f9b45dfbfe0e54fbb6)

gnss\_get\_supported\_systems\_t get\_supported\_systems

**Definition** gnss.h:173

[gnss\_info](structgnss__info.md)

GNSS info data structure.

**Definition** gnss.h:138

[gnss\_info::fix\_quality](structgnss__info.md#a54396dd23fd05185bcb1104ee529984e)

enum gnss\_fix\_quality fix\_quality

The fix quality.

**Definition** gnss.h:146

[gnss\_info::hdop](structgnss__info.md#a5de15dd2a9843c05b8805d4519b49a73)

uint32\_t hdop

Horizontal dilution of precision in 1/1000.

**Definition** gnss.h:142

[gnss\_info::fix\_status](structgnss__info.md#a718e95833c4d07ad530669035ca21f8c)

enum gnss\_fix\_status fix\_status

The fix status.

**Definition** gnss.h:144

[gnss\_info::satellites\_cnt](structgnss__info.md#a81160955c4b9d3a746280d88a74f07eb)

uint16\_t satellites\_cnt

Number of satellites being tracked.

**Definition** gnss.h:140

[gnss\_satellite](structgnss__satellite.md)

GNSS satellite structure.

**Definition** gnss.h:199

[gnss\_satellite::prn](structgnss__satellite.md#a03543a7425f27c78e743b0ec180ccea7)

uint8\_t prn

Pseudo-random noise sequence.

**Definition** gnss.h:201

[gnss\_satellite::azimuth](structgnss__satellite.md#a27a864422f5207b5d38efbd8b50893a3)

uint16\_t azimuth

Azimuth relative to True North in degrees [0, 359].

**Definition** gnss.h:207

[gnss\_satellite::elevation](structgnss__satellite.md#a3d99c5ad18242a42f95b5de496ca501d)

uint8\_t elevation

Elevation in degrees [0, 90].

**Definition** gnss.h:205

[gnss\_satellite::snr](structgnss__satellite.md#a6818083aad878aa8b06d2cbeca53b1da)

uint8\_t snr

Signal-to-noise ratio in dB.

**Definition** gnss.h:203

[gnss\_satellite::system](structgnss__satellite.md#ad9b31c85dd0e162979d384b049142549)

enum gnss\_system system

System of satellite.

**Definition** gnss.h:209

[gnss\_satellite::is\_tracked](structgnss__satellite.md#ae4c596c298ed158a188ea4a5fbd6181c)

uint8\_t is\_tracked

True if satellite is being tracked.

**Definition** gnss.h:211

[gnss\_satellites\_callback](structgnss__satellites__callback.md)

GNSS callback structure.

**Definition** gnss.h:220

[gnss\_satellites\_callback::dev](structgnss__satellites__callback.md#a19e64ff2450c00080ae39528f7d07b2b)

const struct device \* dev

Filter callback to GNSS data from this device if not NULL.

**Definition** gnss.h:222

[gnss\_satellites\_callback::callback](structgnss__satellites__callback.md#af12fc64ff9c696b5862b5adfef31269b)

gnss\_satellites\_callback\_t callback

Callback called when GNSS satellites is published.

**Definition** gnss.h:224

[gnss\_time](structgnss__time.md)

GNSS time data structure.

**Definition** gnss.h:150

[gnss\_time::month](structgnss__time.md#a1c6730dc08cd3dfb48aee08154f5f2de)

uint8\_t month

Month [1, 12].

**Definition** gnss.h:160

[gnss\_time::millisecond](structgnss__time.md#a2ab6b41452491ec34966fda0ddbdd9da)

uint16\_t millisecond

Millisecond [0, 60999].

**Definition** gnss.h:156

[gnss\_time::minute](structgnss__time.md#a3e8b96861e45cc2a6222961e92ab62f5)

uint8\_t minute

Minute [0, 59].

**Definition** gnss.h:154

[gnss\_time::century\_year](structgnss__time.md#a4daa514f38a7b7d88bf49cb5d664b2ac)

uint8\_t century\_year

Year [0, 99].

**Definition** gnss.h:162

[gnss\_time::hour](structgnss__time.md#a5c8a280736741d8d07dacba30d48ed6f)

uint8\_t hour

Hour [0, 23].

**Definition** gnss.h:152

[gnss\_time::month\_day](structgnss__time.md#a766744149009588f83cca930ef53ff10)

uint8\_t month\_day

Day of month [1, 31].

**Definition** gnss.h:158

[navigation\_data](structnavigation__data.md)

Navigation data structure.

**Definition** navigation.h:25

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [gnss.h](gnss_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
