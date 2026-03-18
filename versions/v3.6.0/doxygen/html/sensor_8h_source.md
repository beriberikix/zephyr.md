---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/sensor_8h_source.html
original_path: doxygen/html/sensor_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sensor.h

[Go to the documentation of this file.](sensor_8h.md)

1

6

7/\*

8 \* Copyright (c) 2016 Intel Corporation

9 \*

10 \* SPDX-License-Identifier: Apache-2.0

11 \*/

12#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_H\_

13#define ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_H\_

14

21

22#include <[errno.h](errno_8h.md)>

23#include <[stdlib.h](stdlib_8h.md)>

24

25#include <[zephyr/device.h](device_8h.md)>

26#include <[zephyr/drivers/sensor\_data\_types.h](sensor__data__types_8h.md)>

27#include <[zephyr/dsp/types.h](include_2zephyr_2dsp_2types_8h.md)>

28#include <[zephyr/rtio/rtio.h](rtio_8h.md)>

29#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

30#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

31

32#ifdef \_\_cplusplus

33extern "C" {

34#endif

35

[ 49](structsensor__value.md)struct [sensor\_value](structsensor__value.md) {

[ 51](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe);

[ 53](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b);

54};

55

[ 59](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934)enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) {

[ 61](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934afa9238082f000350530ca77b2f513d4c) [SENSOR\_CHAN\_ACCEL\_X](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934afa9238082f000350530ca77b2f513d4c),

[ 63](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a61c145468f01916c1a547fb38a1be9a8) [SENSOR\_CHAN\_ACCEL\_Y](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a61c145468f01916c1a547fb38a1be9a8),

[ 65](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a78e06bb48cfe06e42829816ad4cb5a0f) [SENSOR\_CHAN\_ACCEL\_Z](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a78e06bb48cfe06e42829816ad4cb5a0f),

[ 67](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a16c05784ae15a4952ea708c2f11a2ae9) [SENSOR\_CHAN\_ACCEL\_XYZ](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a16c05784ae15a4952ea708c2f11a2ae9),

[ 69](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac5709b77f0eb69972ccc055f927e5015) [SENSOR\_CHAN\_GYRO\_X](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac5709b77f0eb69972ccc055f927e5015),

[ 71](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a4a9533172105fd2e55d96e0122a48847) [SENSOR\_CHAN\_GYRO\_Y](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a4a9533172105fd2e55d96e0122a48847),

[ 73](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a9b6b9d13cd8d82449823d65779a87a39) [SENSOR\_CHAN\_GYRO\_Z](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a9b6b9d13cd8d82449823d65779a87a39),

[ 75](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a1d36b89ab3761e9bc86effc839f8db0e) [SENSOR\_CHAN\_GYRO\_XYZ](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a1d36b89ab3761e9bc86effc839f8db0e),

[ 77](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a171f37ba152d34f75ff745cb848b3240) [SENSOR\_CHAN\_MAGN\_X](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a171f37ba152d34f75ff745cb848b3240),

[ 79](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a2b4f1764f47428c528447347d7730942) [SENSOR\_CHAN\_MAGN\_Y](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a2b4f1764f47428c528447347d7730942),

[ 81](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a2a2115051ded019a57ece5a00f86ea61) [SENSOR\_CHAN\_MAGN\_Z](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a2a2115051ded019a57ece5a00f86ea61),

[ 83](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a5d1f48466f6f600503af18427fa3da32) [SENSOR\_CHAN\_MAGN\_XYZ](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a5d1f48466f6f600503af18427fa3da32),

[ 85](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a0a8828f51fe15335ad857d136f197ee1) [SENSOR\_CHAN\_DIE\_TEMP](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a0a8828f51fe15335ad857d136f197ee1),

[ 87](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a5bf9c4a677405c4a4df3bc3acd116c7c) [SENSOR\_CHAN\_AMBIENT\_TEMP](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a5bf9c4a677405c4a4df3bc3acd116c7c),

[ 89](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a14cd68844542e23d1b641a2bc54132a9) [SENSOR\_CHAN\_PRESS](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a14cd68844542e23d1b641a2bc54132a9),

[ 94](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934abaec2c1347ef0035221dd4d9c34a4774) [SENSOR\_CHAN\_PROX](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934abaec2c1347ef0035221dd4d9c34a4774),

[ 96](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ad08ddb6c9cd71c853a121f426fcea042) [SENSOR\_CHAN\_HUMIDITY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ad08ddb6c9cd71c853a121f426fcea042),

[ 98](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a6e91196c11d080c3f5df55fda190e19d) [SENSOR\_CHAN\_LIGHT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a6e91196c11d080c3f5df55fda190e19d),

[ 100](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ad725fe5778f000a17f93f83dab31132c) [SENSOR\_CHAN\_IR](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ad725fe5778f000a17f93f83dab31132c),

[ 102](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934af22c8ef66f4871efe5a22863d7f434aa) [SENSOR\_CHAN\_RED](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934af22c8ef66f4871efe5a22863d7f434aa),

[ 104](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a216a3b2b77d7a92f94547aeb889ae378) [SENSOR\_CHAN\_GREEN](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a216a3b2b77d7a92f94547aeb889ae378),

[ 106](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a6e66f95d73d05c2b3511e2db506844f5) [SENSOR\_CHAN\_BLUE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a6e66f95d73d05c2b3511e2db506844f5),

[ 108](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934af5ba63bfef1c64c8a96ae7fba4f35512) [SENSOR\_CHAN\_ALTITUDE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934af5ba63bfef1c64c8a96ae7fba4f35512),

109

[ 111](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a08f0c21c33008292b0b58defe5c06815) [SENSOR\_CHAN\_PM\_1\_0](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a08f0c21c33008292b0b58defe5c06815),

[ 113](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a3398fdc51964aa06c9a01096d2fac945) [SENSOR\_CHAN\_PM\_2\_5](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a3398fdc51964aa06c9a01096d2fac945),

[ 115](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aa450541bde278aefcc9b53bd0826e225) [SENSOR\_CHAN\_PM\_10](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aa450541bde278aefcc9b53bd0826e225),

[ 117](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ad46d1495990a86fa7e2ab5bbe5338e08) [SENSOR\_CHAN\_DISTANCE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ad46d1495990a86fa7e2ab5bbe5338e08),

118

[ 120](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a7a23e3e869c5e9a39f6a7bfa28737133) [SENSOR\_CHAN\_CO2](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a7a23e3e869c5e9a39f6a7bfa28737133),

[ 122](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934affee34c60c95398b67ec59644d647f8e) [SENSOR\_CHAN\_VOC](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934affee34c60c95398b67ec59644d647f8e),

[ 124](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934acf250a87d2d175f99179a5b54cb7ba01) [SENSOR\_CHAN\_GAS\_RES](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934acf250a87d2d175f99179a5b54cb7ba01),

125

[ 127](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a69dd8a737a0cb6f03fa5f60c92840e6d) [SENSOR\_CHAN\_VOLTAGE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a69dd8a737a0cb6f03fa5f60c92840e6d),

128

[ 130](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a1ea01c780995ad4539e9ffc2ca6102e9) [SENSOR\_CHAN\_VSHUNT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a1ea01c780995ad4539e9ffc2ca6102e9),

131

[ 133](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a1a001ba3ca5ad37308fb7be81f11c950) [SENSOR\_CHAN\_CURRENT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a1a001ba3ca5ad37308fb7be81f11c950),

[ 135](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a33607371060fca93c3555e8e10d5b177) [SENSOR\_CHAN\_POWER](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a33607371060fca93c3555e8e10d5b177),

136

[ 138](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a34ba555026ff976881142512cc8a616b) [SENSOR\_CHAN\_RESISTANCE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a34ba555026ff976881142512cc8a616b),

139

[ 141](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a551ffe08a9b1206e3c051f207b92aabf) [SENSOR\_CHAN\_ROTATION](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a551ffe08a9b1206e3c051f207b92aabf),

142

[ 144](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aa00b7a857e33c925c910661a91389517) [SENSOR\_CHAN\_POS\_DX](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aa00b7a857e33c925c910661a91389517),

[ 146](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a974327ca88ea6d22731cd03afeacef76) [SENSOR\_CHAN\_POS\_DY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a974327ca88ea6d22731cd03afeacef76),

[ 148](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aeaf49aa075947a160f21ae19cf8c39b9) [SENSOR\_CHAN\_POS\_DZ](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aeaf49aa075947a160f21ae19cf8c39b9),

149

[ 151](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a655a576a72cbd6641abc698a3f4304d1) [SENSOR\_CHAN\_RPM](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a655a576a72cbd6641abc698a3f4304d1),

152

[ 154](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ab942649ce1507fb081a77b4bcfc1a57d) [SENSOR\_CHAN\_GAUGE\_VOLTAGE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ab942649ce1507fb081a77b4bcfc1a57d),

[ 156](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a4272c1256cde47006d424c5523d26bf8) [SENSOR\_CHAN\_GAUGE\_AVG\_CURRENT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a4272c1256cde47006d424c5523d26bf8),

[ 158](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a5e6b87cacfe3e4703b963a2177d35cc8) [SENSOR\_CHAN\_GAUGE\_STDBY\_CURRENT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a5e6b87cacfe3e4703b963a2177d35cc8),

[ 160](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a603335f6a91846c5089a2a541d9053cf) [SENSOR\_CHAN\_GAUGE\_MAX\_LOAD\_CURRENT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a603335f6a91846c5089a2a541d9053cf),

[ 162](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a8cac65c812b3a1fcb55a53f18d827214) [SENSOR\_CHAN\_GAUGE\_TEMP](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a8cac65c812b3a1fcb55a53f18d827214),

[ 164](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a7d67d6842ee787fcc8a4d9ee2cbea139) [SENSOR\_CHAN\_GAUGE\_STATE\_OF\_CHARGE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a7d67d6842ee787fcc8a4d9ee2cbea139),

[ 166](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a54a6be68e09b9f8ca4d349e3d1445649) [SENSOR\_CHAN\_GAUGE\_FULL\_CHARGE\_CAPACITY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a54a6be68e09b9f8ca4d349e3d1445649),

[ 168](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aaaea6433c82f7b563f86fa53c95ad0ad) [SENSOR\_CHAN\_GAUGE\_REMAINING\_CHARGE\_CAPACITY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aaaea6433c82f7b563f86fa53c95ad0ad),

[ 170](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934af9b0ac69fd87a68e7e8d97e52b41304a) [SENSOR\_CHAN\_GAUGE\_NOM\_AVAIL\_CAPACITY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934af9b0ac69fd87a68e7e8d97e52b41304a),

[ 172](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a688287fa1587944424a2eda13b8d98e8) [SENSOR\_CHAN\_GAUGE\_FULL\_AVAIL\_CAPACITY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a688287fa1587944424a2eda13b8d98e8),

[ 174](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aa24f9e12f20a716dd152cf889cb51228) [SENSOR\_CHAN\_GAUGE\_AVG\_POWER](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aa24f9e12f20a716dd152cf889cb51228),

[ 176](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a0613c39397f06d11f4350f8cbcc24cf6) [SENSOR\_CHAN\_GAUGE\_STATE\_OF\_HEALTH](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a0613c39397f06d11f4350f8cbcc24cf6),

[ 178](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aa3755e9fcd8c90fef5185082edb29b65) [SENSOR\_CHAN\_GAUGE\_TIME\_TO\_EMPTY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aa3755e9fcd8c90fef5185082edb29b65),

[ 180](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a14d4c802805e1e07c9b4e47ccaff0eeb) [SENSOR\_CHAN\_GAUGE\_TIME\_TO\_FULL](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a14d4c802805e1e07c9b4e47ccaff0eeb),

[ 182](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a8834978858c2b62b5e923d06cfcb1a46) [SENSOR\_CHAN\_GAUGE\_CYCLE\_COUNT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a8834978858c2b62b5e923d06cfcb1a46),

[ 184](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a6f96ba4db6cf812b223f9a09f2a287d0) [SENSOR\_CHAN\_GAUGE\_DESIGN\_VOLTAGE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a6f96ba4db6cf812b223f9a09f2a287d0),

[ 186](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a2c33a7f11d5b3996e95167698a2056cf) [SENSOR\_CHAN\_GAUGE\_DESIRED\_VOLTAGE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a2c33a7f11d5b3996e95167698a2056cf),

[ 188](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a4aa8bba1b260e1994542383d8e2e908f) [SENSOR\_CHAN\_GAUGE\_DESIRED\_CHARGING\_CURRENT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a4aa8bba1b260e1994542383d8e2e908f),

189

[ 191](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ab275027eb550b2b075c44917634eca2c) [SENSOR\_CHAN\_ALL](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ab275027eb550b2b075c44917634eca2c),

192

[ 196](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934abb2893ccb71c9e1eeb155d7cbd539303) [SENSOR\_CHAN\_COMMON\_COUNT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934abb2893ccb71c9e1eeb155d7cbd539303),

197

[ 202](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12) [SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12) = [SENSOR\_CHAN\_COMMON\_COUNT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934abb2893ccb71c9e1eeb155d7cbd539303),

203

[ 207](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ad842035a01166417d90cd5d7630733b1) [SENSOR\_CHAN\_MAX](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ad842035a01166417d90cd5d7630733b1) = [INT16\_MAX](stdint_8h.md#ac58f2c111cc9989c86db2a7dc4fd84ca),

208};

209

[ 213](group__sensor__interface.md#ga08215279400e8c9eb05ce4e4f0898ffd)enum [sensor\_trigger\_type](group__sensor__interface.md#ga08215279400e8c9eb05ce4e4f0898ffd) {

[ 218](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdabf92b196394726ec90f1d61586a7f023) [SENSOR\_TRIG\_TIMER](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdabf92b196394726ec90f1d61586a7f023),

[ 220](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdaf7c161e309c267a7dd6daf2ad176f44f) [SENSOR\_TRIG\_DATA\_READY](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdaf7c161e309c267a7dd6daf2ad176f44f),

[ 229](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda3bb90a3334bcf613c9efbdf2ed05f855) [SENSOR\_TRIG\_DELTA](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda3bb90a3334bcf613c9efbdf2ed05f855),

[ 231](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda448226d83b28c2862c353a8cda7be0d5) [SENSOR\_TRIG\_NEAR\_FAR](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda448226d83b28c2862c353a8cda7be0d5),

[ 238](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda8f875f881b6540eebc28e3d6a7d46606) [SENSOR\_TRIG\_THRESHOLD](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda8f875f881b6540eebc28e3d6a7d46606),

239

[ 241](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdae49a25e6400f0753f6bac8a7d136200d) [SENSOR\_TRIG\_TAP](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdae49a25e6400f0753f6bac8a7d136200d),

242

[ 244](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdab95e52584a6bc3343181f495cd4cb2ef) [SENSOR\_TRIG\_DOUBLE\_TAP](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdab95e52584a6bc3343181f495cd4cb2ef),

245

[ 247](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda4943ffb4afaf4cbae39e85693bd4374c) [SENSOR\_TRIG\_FREEFALL](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda4943ffb4afaf4cbae39e85693bd4374c),

248

[ 250](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda7095387831b763b34171287945dae276) [SENSOR\_TRIG\_MOTION](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda7095387831b763b34171287945dae276),

251

[ 253](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda79e286ffced716e1076f56464ea47f5d) [SENSOR\_TRIG\_STATIONARY](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda79e286ffced716e1076f56464ea47f5d),

254

[ 256](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdac5d67fb4fb6206465b1b01dc78245fe4) [SENSOR\_TRIG\_FIFO\_WATERMARK](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdac5d67fb4fb6206465b1b01dc78245fe4),

257

[ 259](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda66f913f8751a77a6c16745e329c7315c) [SENSOR\_TRIG\_FIFO\_FULL](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda66f913f8751a77a6c16745e329c7315c),

[ 263](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda8d1f2621fad4fd685d56cca3f9b042f5) [SENSOR\_TRIG\_COMMON\_COUNT](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda8d1f2621fad4fd685d56cca3f9b042f5),

264

[ 269](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda5e1a94f21fee67ee98296153ea640921) [SENSOR\_TRIG\_PRIV\_START](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda5e1a94f21fee67ee98296153ea640921) = [SENSOR\_TRIG\_COMMON\_COUNT](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda8d1f2621fad4fd685d56cca3f9b042f5),

270

[ 274](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda9de566f44de519f94c59c58df1efc4c4) [SENSOR\_TRIG\_MAX](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda9de566f44de519f94c59c58df1efc4c4) = [INT16\_MAX](stdint_8h.md#ac58f2c111cc9989c86db2a7dc4fd84ca),

275};

276

[ 280](structsensor__trigger.md)struct [sensor\_trigger](structsensor__trigger.md) {

[ 282](structsensor__trigger.md#ac2cce1ec6ff82f95cb06d0dccafd7af0) enum [sensor\_trigger\_type](group__sensor__interface.md#ga08215279400e8c9eb05ce4e4f0898ffd) [type](structsensor__trigger.md#ac2cce1ec6ff82f95cb06d0dccafd7af0);

[ 284](structsensor__trigger.md#ae01f99b124aa99c59b9967818022e112) enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) [chan](structsensor__trigger.md#ae01f99b124aa99c59b9967818022e112);

285};

286

[ 290](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b)enum [sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b) {

[ 295](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bacb07e3508ea5503dbcdceee3f17d2291) [SENSOR\_ATTR\_SAMPLING\_FREQUENCY](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bacb07e3508ea5503dbcdceee3f17d2291),

[ 297](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940baee644485ab5f64e7c5273bbe562deaaa) [SENSOR\_ATTR\_LOWER\_THRESH](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940baee644485ab5f64e7c5273bbe562deaaa),

[ 299](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba5af51bd0640a87a94476eee112a4460b) [SENSOR\_ATTR\_UPPER\_THRESH](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba5af51bd0640a87a94476eee112a4460b),

[ 301](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bac4538665a244cb7f18fc053c40134302) [SENSOR\_ATTR\_SLOPE\_TH](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bac4538665a244cb7f18fc053c40134302),

[ 306](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940baf510b32b2e2395bbcf1c8fd7159ed2a1) [SENSOR\_ATTR\_SLOPE\_DUR](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940baf510b32b2e2395bbcf1c8fd7159ed2a1),

307 /\* Hysteresis for trigger thresholds. \*/

[ 308](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba044e67bfc04e8ddc2de7d2058fffbc94) [SENSOR\_ATTR\_HYSTERESIS](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba044e67bfc04e8ddc2de7d2058fffbc94),

[ 310](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba3d32987f75284d80d3f64bf44f5c6ccd) [SENSOR\_ATTR\_OVERSAMPLING](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba3d32987f75284d80d3f64bf44f5c6ccd),

[ 312](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bad30df3100fb6b285a6a786fdc77234d3) [SENSOR\_ATTR\_FULL\_SCALE](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bad30df3100fb6b285a6a786fdc77234d3),

[ 317](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba332935dcb6f7e228cb9c595a545079fd) [SENSOR\_ATTR\_OFFSET](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba332935dcb6f7e228cb9c595a545079fd),

[ 322](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba3043381b539610a8b424f12d76474bdf) [SENSOR\_ATTR\_CALIB\_TARGET](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba3043381b539610a8b424f12d76474bdf),

[ 324](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba75cd3aca26859fd7c10c83d86e3471e9) [SENSOR\_ATTR\_CONFIGURATION](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba75cd3aca26859fd7c10c83d86e3471e9),

[ 326](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba843d1e79573c634987e5e839ba9e965e) [SENSOR\_ATTR\_CALIBRATION](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba843d1e79573c634987e5e839ba9e965e),

[ 328](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba1f8d2242fa9d63a13c6a48fe3a1cbe52) [SENSOR\_ATTR\_FEATURE\_MASK](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba1f8d2242fa9d63a13c6a48fe3a1cbe52),

[ 330](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940baaedf76e63224adc3fa266d35666e0a3a) [SENSOR\_ATTR\_ALERT](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940baaedf76e63224adc3fa266d35666e0a3a),

[ 336](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba5a62ea6aa7e55efd62ab3f93dcb0593a) [SENSOR\_ATTR\_FF\_DUR](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba5a62ea6aa7e55efd62ab3f93dcb0593a),

337

[ 339](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba3b0cf69c77de55c92129e212bf5b8ced) [SENSOR\_ATTR\_BATCH\_DURATION](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba3b0cf69c77de55c92129e212bf5b8ced),

340

[ 344](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba99ceedef81217614ada0c8a469f91eb8) [SENSOR\_ATTR\_COMMON\_COUNT](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba99ceedef81217614ada0c8a469f91eb8),

345

[ 350](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3) [SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3) = [SENSOR\_ATTR\_COMMON\_COUNT](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba99ceedef81217614ada0c8a469f91eb8),

351

[ 355](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940baf6bd0b33ca2117ef329692c291f6384b) [SENSOR\_ATTR\_MAX](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940baf6bd0b33ca2117ef329692c291f6384b) = [INT16\_MAX](stdint_8h.md#ac58f2c111cc9989c86db2a7dc4fd84ca),

356};

357

[ 365](group__sensor__interface.md#ga890c1fb6d6974aea22a2d08829a75902)typedef void (\*[sensor\_trigger\_handler\_t](group__sensor__interface.md#ga890c1fb6d6974aea22a2d08829a75902))(const struct [device](structdevice.md) \*dev,

366 const struct [sensor\_trigger](structsensor__trigger.md) \*trigger);

367

[ 374](group__sensor__interface.md#ga38422ace4194a66a9a912a8ef1e088fb)typedef int (\*[sensor\_attr\_set\_t](group__sensor__interface.md#ga38422ace4194a66a9a912a8ef1e088fb))(const struct [device](structdevice.md) \*dev,

375 enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) chan,

376 enum [sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b) attr,

377 const struct [sensor\_value](structsensor__value.md) \*val);

378

[ 385](group__sensor__interface.md#ga00d05c82b46e56dca5f6e8f7f01c31b8)typedef int (\*[sensor\_attr\_get\_t](group__sensor__interface.md#ga00d05c82b46e56dca5f6e8f7f01c31b8))(const struct [device](structdevice.md) \*dev,

386 enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) chan,

387 enum [sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b) attr,

388 struct [sensor\_value](structsensor__value.md) \*val);

389

[ 396](group__sensor__interface.md#gad7f7a3d9e714cc16f23656ca06592aa4)typedef int (\*[sensor\_trigger\_set\_t](group__sensor__interface.md#gad7f7a3d9e714cc16f23656ca06592aa4))(const struct [device](structdevice.md) \*dev,

397 const struct [sensor\_trigger](structsensor__trigger.md) \*trig,

398 [sensor\_trigger\_handler\_t](group__sensor__interface.md#ga890c1fb6d6974aea22a2d08829a75902) handler);

[ 405](group__sensor__interface.md#gacae110a4edb6f29dfb457cb1ea8d68c1)typedef int (\*[sensor\_sample\_fetch\_t](group__sensor__interface.md#gacae110a4edb6f29dfb457cb1ea8d68c1))(const struct [device](structdevice.md) \*dev,

406 enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) chan);

[ 413](group__sensor__interface.md#ga5c9b5ed9097464562004b446856043fd)typedef int (\*[sensor\_channel\_get\_t](group__sensor__interface.md#ga5c9b5ed9097464562004b446856043fd))(const struct [device](structdevice.md) \*dev,

414 enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) chan,

415 struct [sensor\_value](structsensor__value.md) \*val);

416

[ 423](structsensor__decoder__api.md)struct [sensor\_decoder\_api](structsensor__decoder__api.md) {

[ 434](structsensor__decoder__api.md#ac8344c7849c9a7084788192fb4f691fc) int (\*[get\_frame\_count](structsensor__decoder__api.md#ac8344c7849c9a7084788192fb4f691fc))(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) channel,

435 size\_t channel\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*frame\_count);

436

[ 449](structsensor__decoder__api.md#a67db53773d768b160fb74ab72affee14) int (\*[get\_size\_info](structsensor__decoder__api.md#a67db53773d768b160fb74ab72affee14))(enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) channel, size\_t \*base\_size, size\_t \*frame\_size);

450

[ 477](structsensor__decoder__api.md#a6c910d525374987ae68da10d75f9766e) int (\*[decode](structsensor__decoder__api.md#a6c910d525374987ae68da10d75f9766e))(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) channel, size\_t channel\_idx,

478 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*fit, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) max\_count, void \*data\_out);

479

[ 487](structsensor__decoder__api.md#a78706bae0f1314615b5804736ef43493) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[has\_trigger](structsensor__decoder__api.md#a78706bae0f1314615b5804736ef43493))(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, enum [sensor\_trigger\_type](group__sensor__interface.md#ga08215279400e8c9eb05ce4e4f0898ffd) trigger);

488};

489

[ 514](structsensor__decode__context.md)struct [sensor\_decode\_context](structsensor__decode__context.md) {

[ 515](structsensor__decode__context.md#a1ac0773e83a086455371d108264ef4f6) const struct [sensor\_decoder\_api](structsensor__decoder__api.md) \*[decoder](structsensor__decode__context.md#a1ac0773e83a086455371d108264ef4f6);

[ 516](structsensor__decode__context.md#a23e27eb0687d722be78e1b89278613d1) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buffer](structsensor__decode__context.md#a23e27eb0687d722be78e1b89278613d1);

[ 517](structsensor__decode__context.md#a7eab1624b1136e07240d1f9c4d66d123) enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) [channel](structsensor__decode__context.md#a7eab1624b1136e07240d1f9c4d66d123);

[ 518](structsensor__decode__context.md#a69e74a3651f7a9adaf17b5038c660d77) size\_t [channel\_idx](structsensor__decode__context.md#a69e74a3651f7a9adaf17b5038c660d77);

[ 519](structsensor__decode__context.md#ada9e40625829093087886c41f2fb7350) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [fit](structsensor__decode__context.md#ada9e40625829093087886c41f2fb7350);

520};

521

[ 525](group__sensor__interface.md#gac537a3a64a2a67e1ae2bb70ada147b00)#define SENSOR\_DECODE\_CONTEXT\_INIT(decoder\_, buffer\_, channel\_, channel\_index\_) \

526 { \

527 .decoder = (decoder\_), \

528 .buffer = (buffer\_), \

529 .channel = (channel\_), \

530 .channel\_idx = (channel\_index\_), \

531 .fit = 0, \

532 }

533

[ 542](group__sensor__interface.md#ga018bca56056ae2558f9e45aeb2fa5f53)static inline int [sensor\_decode](group__sensor__interface.md#ga018bca56056ae2558f9e45aeb2fa5f53)(struct [sensor\_decode\_context](structsensor__decode__context.md) \*ctx, void \*out, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) max\_count)

543{

544 return ctx->[decoder](structsensor__decode__context.md#a1ac0773e83a086455371d108264ef4f6)->[decode](structsensor__decoder__api.md#a6c910d525374987ae68da10d75f9766e)(ctx->[buffer](structsensor__decode__context.md#a23e27eb0687d722be78e1b89278613d1), ctx->[channel](structsensor__decode__context.md#a7eab1624b1136e07240d1f9c4d66d123), ctx->[channel\_idx](structsensor__decode__context.md#a69e74a3651f7a9adaf17b5038c660d77), &ctx->[fit](structsensor__decode__context.md#ada9e40625829093087886c41f2fb7350),

545 max\_count, out);

546}

547

[ 548](group__sensor__interface.md#ga5d905ca03326972f3e08c92939c2a558)int [sensor\_natively\_supported\_channel\_size\_info](group__sensor__interface.md#ga5d905ca03326972f3e08c92939c2a558)(enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) channel, size\_t \*base\_size,

549 size\_t \*frame\_size);

550

[ 557](group__sensor__interface.md#ga21e407d552d140cfb6bfd0d9513c7d42)typedef int (\*[sensor\_get\_decoder\_t](group__sensor__interface.md#ga21e407d552d140cfb6bfd0d9513c7d42))(const struct [device](structdevice.md) \*dev,

558 const struct [sensor\_decoder\_api](structsensor__decoder__api.md) \*\*api);

559

[ 563](group__sensor__interface.md#ga8613a20521a37d40fd7371dc63ba2dac)enum [sensor\_stream\_data\_opt](group__sensor__interface.md#ga8613a20521a37d40fd7371dc63ba2dac) {

[ 565](group__sensor__interface.md#gga8613a20521a37d40fd7371dc63ba2daca2ba3554a08bf55b64da40900592be315) [SENSOR\_STREAM\_DATA\_INCLUDE](group__sensor__interface.md#gga8613a20521a37d40fd7371dc63ba2daca2ba3554a08bf55b64da40900592be315) = 0,

[ 567](group__sensor__interface.md#gga8613a20521a37d40fd7371dc63ba2daca7e897c6d1428ff50f98140ed4cd4d35d) [SENSOR\_STREAM\_DATA\_NOP](group__sensor__interface.md#gga8613a20521a37d40fd7371dc63ba2daca7e897c6d1428ff50f98140ed4cd4d35d) = 1,

[ 569](group__sensor__interface.md#gga8613a20521a37d40fd7371dc63ba2dacaa13c6d3bae87c16f9cd89e0fe7144f8e) [SENSOR\_STREAM\_DATA\_DROP](group__sensor__interface.md#gga8613a20521a37d40fd7371dc63ba2dacaa13c6d3bae87c16f9cd89e0fe7144f8e) = 2,

570};

571

[ 572](structsensor__stream__trigger.md)struct [sensor\_stream\_trigger](structsensor__stream__trigger.md) {

[ 573](structsensor__stream__trigger.md#a9a367e746764e68140ec9120f2a016e6) enum [sensor\_trigger\_type](group__sensor__interface.md#ga08215279400e8c9eb05ce4e4f0898ffd) [trigger](structsensor__stream__trigger.md#a9a367e746764e68140ec9120f2a016e6);

[ 574](structsensor__stream__trigger.md#a62ccdecf7253b1bfdff4f1d659563d76) enum [sensor\_stream\_data\_opt](group__sensor__interface.md#ga8613a20521a37d40fd7371dc63ba2dac) [opt](structsensor__stream__trigger.md#a62ccdecf7253b1bfdff4f1d659563d76);

575};

576

[ 577](group__sensor__interface.md#ga9b7b0db322121d220b126d2b5bb7eb73)#define SENSOR\_STREAM\_TRIGGER\_PREP(\_trigger, \_opt) \

578 { \

579 .trigger = (\_trigger), .opt = (\_opt), \

580 }

581/\*

582 \* Internal data structure used to store information about the IODevice for async reading and

583 \* streaming sensor data.

584 \*/

[ 585](structsensor__read__config.md)struct [sensor\_read\_config](structsensor__read__config.md) {

[ 586](structsensor__read__config.md#ad49d5ab5293017d1ad2cf60adc542090) const struct [device](structdevice.md) \*[sensor](structsensor__read__config.md#ad49d5ab5293017d1ad2cf60adc542090);

[ 587](structsensor__read__config.md#aca96de2c23fb63f887c4c40dcb272798) const bool [is\_streaming](structsensor__read__config.md#aca96de2c23fb63f887c4c40dcb272798);

588 union {

[ 589](structsensor__read__config.md#afd61f80d484e496cbdf1f48ceea3c657) enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) \*const [channels](structsensor__read__config.md#afd61f80d484e496cbdf1f48ceea3c657);

[ 590](structsensor__read__config.md#a6eaa6df7bc9378abe0f5b4b8c9a05909) struct [sensor\_stream\_trigger](structsensor__stream__trigger.md) \*const [triggers](structsensor__read__config.md#a6eaa6df7bc9378abe0f5b4b8c9a05909);

591 };

[ 592](structsensor__read__config.md#a5236049e0563ebba754994d70e22383a) size\_t [count](structsensor__read__config.md#a5236049e0563ebba754994d70e22383a);

[ 593](structsensor__read__config.md#aecb9c899e292fdb25c3c990bdaf1c76b) const size\_t [max](structsensor__read__config.md#aecb9c899e292fdb25c3c990bdaf1c76b);

594};

595

[ 610](group__sensor__interface.md#ga0cc1ee28114557e9e00257071c7dfa9f)#define SENSOR\_DT\_READ\_IODEV(name, dt\_node, ...) \

611 static enum sensor\_channel \_CONCAT(\_\_channel\_array\_, name)[] = {\_\_VA\_ARGS\_\_}; \

612 static struct sensor\_read\_config \_CONCAT(\_\_sensor\_read\_config\_, name) = { \

613 .sensor = DEVICE\_DT\_GET(dt\_node), \

614 .is\_streaming = false, \

615 .channels = \_CONCAT(\_\_channel\_array\_, name), \

616 .count = ARRAY\_SIZE(\_CONCAT(\_\_channel\_array\_, name)), \

617 .max = ARRAY\_SIZE(\_CONCAT(\_\_channel\_array\_, name)), \

618 }; \

619 RTIO\_IODEV\_DEFINE(name, &\_\_sensor\_iodev\_api, \_CONCAT(&\_\_sensor\_read\_config\_, name))

620

[ 640](group__sensor__interface.md#ga35211c4d908a26f98b1f8d925a9b1374)#define SENSOR\_DT\_STREAM\_IODEV(name, dt\_node, ...) \

641 static struct sensor\_stream\_trigger \_CONCAT(\_\_trigger\_array\_, name)[] = {\_\_VA\_ARGS\_\_}; \

642 static struct sensor\_read\_config \_CONCAT(\_\_sensor\_read\_config\_, name) = { \

643 .sensor = DEVICE\_DT\_GET(dt\_node), \

644 .is\_streaming = true, \

645 .triggers = \_CONCAT(\_\_trigger\_array\_, name), \

646 .count = ARRAY\_SIZE(\_CONCAT(\_\_trigger\_array\_, name)), \

647 .max = ARRAY\_SIZE(\_CONCAT(\_\_trigger\_array\_, name)), \

648 }; \

649 RTIO\_IODEV\_DEFINE(name, &\_\_sensor\_iodev\_api, &\_CONCAT(\_\_sensor\_read\_config\_, name))

650

651/\* Used to submit an RTIO sqe to the sensor's iodev \*/

[ 652](group__sensor__interface.md#gab8e7a28e19d596ddcbefeb34d84a2b3c)typedef int (\*[sensor\_submit\_t](group__sensor__interface.md#gab8e7a28e19d596ddcbefeb34d84a2b3c))(const struct [device](structdevice.md) \*sensor, struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b));

653

654/\* The default decoder API \*/

655extern const struct [sensor\_decoder\_api](structsensor__decoder__api.md) \_\_sensor\_default\_decoder;

656

657/\* The default sensor iodev API \*/

658extern const struct [rtio\_iodev\_api](structrtio__iodev__api.md) \_\_sensor\_iodev\_api;

659

[ 660](structsensor__driver__api.md)\_\_subsystem struct [sensor\_driver\_api](structsensor__driver__api.md) {

[ 661](structsensor__driver__api.md#a2d230a976b19a699d132034f58bb2b6a) [sensor\_attr\_set\_t](group__sensor__interface.md#ga38422ace4194a66a9a912a8ef1e088fb) [attr\_set](structsensor__driver__api.md#a2d230a976b19a699d132034f58bb2b6a);

[ 662](structsensor__driver__api.md#a3e28950f844c3f8b8da5ba9ff8052e46) [sensor\_attr\_get\_t](group__sensor__interface.md#ga00d05c82b46e56dca5f6e8f7f01c31b8) [attr\_get](structsensor__driver__api.md#a3e28950f844c3f8b8da5ba9ff8052e46);

[ 663](structsensor__driver__api.md#a4708070fd6654ecbbe631819aba319bd) [sensor\_trigger\_set\_t](group__sensor__interface.md#gad7f7a3d9e714cc16f23656ca06592aa4) [trigger\_set](structsensor__driver__api.md#a4708070fd6654ecbbe631819aba319bd);

[ 664](structsensor__driver__api.md#a4b40e25b81fe070e2f6bdcf7f8a4a31f) [sensor\_sample\_fetch\_t](group__sensor__interface.md#gacae110a4edb6f29dfb457cb1ea8d68c1) [sample\_fetch](structsensor__driver__api.md#a4b40e25b81fe070e2f6bdcf7f8a4a31f);

[ 665](structsensor__driver__api.md#a667b41bf51f2c7a6bb31713fbf889113) [sensor\_channel\_get\_t](group__sensor__interface.md#ga5c9b5ed9097464562004b446856043fd) [channel\_get](structsensor__driver__api.md#a667b41bf51f2c7a6bb31713fbf889113);

[ 666](structsensor__driver__api.md#a004f9d342805dc72249ab9b8c17a544b) [sensor\_get\_decoder\_t](group__sensor__interface.md#ga21e407d552d140cfb6bfd0d9513c7d42) [get\_decoder](structsensor__driver__api.md#a004f9d342805dc72249ab9b8c17a544b);

[ 667](structsensor__driver__api.md#ae3ba0adeba21351e8f660896e5a0e702) [sensor\_submit\_t](group__sensor__interface.md#gab8e7a28e19d596ddcbefeb34d84a2b3c) [submit](structsensor__driver__api.md#ae3ba0adeba21351e8f660896e5a0e702);

668};

669

[ 682](group__sensor__interface.md#gafbf65226a227e9f8824908bc38e336f5)\_\_syscall int [sensor\_attr\_set](group__sensor__interface.md#gafbf65226a227e9f8824908bc38e336f5)(const struct [device](structdevice.md) \*dev,

683 enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) chan,

684 enum [sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b) attr,

685 const struct [sensor\_value](structsensor__value.md) \*val);

686

687static inline int z\_impl\_sensor\_attr\_set(const struct [device](structdevice.md) \*dev,

688 enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) chan,

689 enum [sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b) attr,

690 const struct [sensor\_value](structsensor__value.md) \*val)

691{

692 const struct [sensor\_driver\_api](structsensor__driver__api.md) \*api =

693 (const struct [sensor\_driver\_api](structsensor__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

694

695 if (api->attr\_set == NULL) {

696 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

697 }

698

699 return api->attr\_set(dev, chan, attr, val);

700}

701

[ 714](group__sensor__interface.md#gaedfdfc71dce702dc1fb1c6e60ff0f73a)\_\_syscall int [sensor\_attr\_get](group__sensor__interface.md#gaedfdfc71dce702dc1fb1c6e60ff0f73a)(const struct [device](structdevice.md) \*dev,

715 enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) chan,

716 enum [sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b) attr,

717 struct [sensor\_value](structsensor__value.md) \*val);

718

719static inline int z\_impl\_sensor\_attr\_get(const struct [device](structdevice.md) \*dev,

720 enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) chan,

721 enum [sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b) attr,

722 struct [sensor\_value](structsensor__value.md) \*val)

723{

724 const struct [sensor\_driver\_api](structsensor__driver__api.md) \*api =

725 (const struct [sensor\_driver\_api](structsensor__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

726

727 if (api->attr\_get == NULL) {

728 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

729 }

730

731 return api->attr\_get(dev, chan, attr, val);

732}

733

[ 756](group__sensor__interface.md#ga7c72aca732e0641612d2f9437c2e41b7)static inline int [sensor\_trigger\_set](group__sensor__interface.md#ga7c72aca732e0641612d2f9437c2e41b7)(const struct [device](structdevice.md) \*dev,

757 const struct [sensor\_trigger](structsensor__trigger.md) \*trig,

758 [sensor\_trigger\_handler\_t](group__sensor__interface.md#ga890c1fb6d6974aea22a2d08829a75902) handler)

759{

760 const struct [sensor\_driver\_api](structsensor__driver__api.md) \*api =

761 (const struct [sensor\_driver\_api](structsensor__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

762

763 if (api->[trigger\_set](structsensor__driver__api.md#a4708070fd6654ecbbe631819aba319bd) == NULL) {

764 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

765 }

766

767 return api->[trigger\_set](structsensor__driver__api.md#a4708070fd6654ecbbe631819aba319bd)(dev, trig, handler);

768}

769

[ 788](group__sensor__interface.md#gaa75e25d93ee7cac0bf38399f3c006dff)\_\_syscall int [sensor\_sample\_fetch](group__sensor__interface.md#gaa75e25d93ee7cac0bf38399f3c006dff)(const struct [device](structdevice.md) \*dev);

789

790static inline int z\_impl\_sensor\_sample\_fetch(const struct [device](structdevice.md) \*dev)

791{

792 const struct [sensor\_driver\_api](structsensor__driver__api.md) \*api =

793 (const struct [sensor\_driver\_api](structsensor__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

794

795 return api->sample\_fetch(dev, [SENSOR\_CHAN\_ALL](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ab275027eb550b2b075c44917634eca2c));

796}

797

[ 819](group__sensor__interface.md#gac16192826432438a15274cf28d66e8a6)\_\_syscall int [sensor\_sample\_fetch\_chan](group__sensor__interface.md#gac16192826432438a15274cf28d66e8a6)(const struct [device](structdevice.md) \*dev,

820 enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) type);

821

822static inline int z\_impl\_sensor\_sample\_fetch\_chan(const struct [device](structdevice.md) \*dev,

823 enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) type)

824{

825 const struct [sensor\_driver\_api](structsensor__driver__api.md) \*api =

826 (const struct [sensor\_driver\_api](structsensor__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

827

828 return api->sample\_fetch(dev, type);

829}

830

[ 852](group__sensor__interface.md#ga9e0e6c1408d32c52267984bae7cb268d)\_\_syscall int [sensor\_channel\_get](group__sensor__interface.md#ga9e0e6c1408d32c52267984bae7cb268d)(const struct [device](structdevice.md) \*dev,

853 enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) chan,

854 struct [sensor\_value](structsensor__value.md) \*val);

855

856static inline int z\_impl\_sensor\_channel\_get(const struct [device](structdevice.md) \*dev,

857 enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) chan,

858 struct [sensor\_value](structsensor__value.md) \*val)

859{

860 const struct [sensor\_driver\_api](structsensor__driver__api.md) \*api =

861 (const struct [sensor\_driver\_api](structsensor__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

862

863 return api->channel\_get(dev, chan, val);

864}

865

866#if defined(CONFIG\_SENSOR\_ASYNC\_API) || defined(\_\_DOXYGEN\_\_)

867

868/\*

869 \* Generic data structure used for encoding the sample timestamp and number of channels sampled.

870 \*/

[ 871](structsensor__data__generic__header.md)struct \_\_attribute\_\_((\_\_packed\_\_)) [sensor\_data\_generic\_header](structsensor__data__generic__header.md) {

872 /\* The timestamp at which the data was collected from the sensor \*/

[ 873](structsensor__data__generic__header.md#a429e22b3191df271ccfe321b796e1ac9) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [timestamp\_ns](structsensor__data__generic__header.md#a429e22b3191df271ccfe321b796e1ac9);

874

875 /\*

876 \* The number of channels present in the frame. This will be the true number of elements in

877 \* channel\_info and in the q31 values that follow the header.

878 \*/

[ 879](structsensor__data__generic__header.md#a7edbe674f28c95f3aa40b1df84ca61fe) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [num\_channels](structsensor__data__generic__header.md#a7edbe674f28c95f3aa40b1df84ca61fe);

880

881 /\* Shift value for all samples in the frame \*/

[ 882](structsensor__data__generic__header.md#a68067521c1058b6802176e1d48fed788) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [shift](structsensor__data__generic__header.md#a68067521c1058b6802176e1d48fed788);

883

884 /\* This padding is needed to make sure that the 'channels' field is aligned \*/

885 [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) \_padding[sizeof(enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934)) - 1];

886

887 /\* Channels present in the frame \*/

[ 888](structsensor__data__generic__header.md#a14f5460f665c075d136eaa7b02c2e3c2) enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) [channels](structsensor__data__generic__header.md#a14f5460f665c075d136eaa7b02c2e3c2)[0];

889};

890

[ 899](group__sensor__interface.md#ga32f679a4004b5707b2de00eb580d0930)#define SENSOR\_CHANNEL\_3\_AXIS(chan) \

900 ((chan) == SENSOR\_CHAN\_ACCEL\_XYZ || (chan) == SENSOR\_CHAN\_GYRO\_XYZ || \

901 (chan) == SENSOR\_CHAN\_MAGN\_XYZ)

902

[ 911](group__sensor__interface.md#ga12db6fc43adce48d34c25c16fd2336a3)\_\_syscall int [sensor\_get\_decoder](group__sensor__interface.md#ga12db6fc43adce48d34c25c16fd2336a3)(const struct [device](structdevice.md) \*dev,

912 const struct [sensor\_decoder\_api](structsensor__decoder__api.md) \*\*decoder);

913

914static inline int z\_impl\_sensor\_get\_decoder(const struct [device](structdevice.md) \*dev,

915 const struct [sensor\_decoder\_api](structsensor__decoder__api.md) \*\*decoder)

916{

917 const struct [sensor\_driver\_api](structsensor__driver__api.md) \*api = (const struct [sensor\_driver\_api](structsensor__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

918

919 \_\_ASSERT\_NO\_MSG(api != NULL);

920

921 if (api->get\_decoder == NULL) {

922 \*decoder = &\_\_sensor\_default\_decoder;

923 return 0;

924 }

925

926 return api->get\_decoder(dev, decoder);

927}

928

[ 947](group__sensor__interface.md#ga949ab4cb1f0572d63eb439d34dad61cc)\_\_syscall int [sensor\_reconfigure\_read\_iodev](group__sensor__interface.md#ga949ab4cb1f0572d63eb439d34dad61cc)(struct [rtio\_iodev](structrtio__iodev.md) \*iodev, const struct [device](structdevice.md) \*sensor,

948 const enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) \*channels,

949 size\_t num\_channels);

950

951static inline int z\_impl\_sensor\_reconfigure\_read\_iodev(struct [rtio\_iodev](structrtio__iodev.md) \*iodev,

952 const struct [device](structdevice.md) \*sensor,

953 const enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) \*channels,

954 size\_t num\_channels)

955{

956 struct [sensor\_read\_config](structsensor__read__config.md) \*cfg = (struct [sensor\_read\_config](structsensor__read__config.md) \*)iodev->[data](structrtio__iodev.md#af0f3a27fe8dea2161c9a73cb838bdeec);

957

958 if (cfg->max < num\_channels || cfg->is\_streaming) {

959 return -[ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5);

960 }

961

962 cfg->sensor = [sensor](structsensor__read__config.md#ad49d5ab5293017d1ad2cf60adc542090);

963 [memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)(cfg->channels, [channels](structsensor__read__config.md#afd61f80d484e496cbdf1f48ceea3c657), num\_channels \* sizeof(enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934)));

964 cfg->count = num\_channels;

965 return 0;

966}

967

[ 968](group__sensor__interface.md#gac77fc83844935f61a2bf9ab2c38987b6)static inline int [sensor\_stream](group__sensor__interface.md#gac77fc83844935f61a2bf9ab2c38987b6)(struct [rtio\_iodev](structrtio__iodev.md) \*iodev, struct [rtio](structrtio.md) \*ctx, void \*userdata,

969 struct [rtio\_sqe](structrtio__sqe.md) \*\*handle)

970{

971 if ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_USERSPACE)) {

972 struct [rtio\_sqe](structrtio__sqe.md) sqe;

973

974 [rtio\_sqe\_prep\_read\_multishot](group__rtio.md#ga9803aa829f8c0eeee746ea7d872c20cc)(&sqe, [iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc), [RTIO\_PRIO\_NORM](group__rtio__sqe__prio.md#gab02e27e01b7dd4eb3439df557899ce92), [userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971));

975 [rtio\_sqe\_copy\_in\_get\_handles](group__rtio.md#ga830863e6c8d9b96f4c473a038cab8f8c)(ctx, &sqe, handle, 1);

976 } else {

977 struct [rtio\_sqe](structrtio__sqe.md) \*sqe = [rtio\_sqe\_acquire](group__rtio.md#ga8b47c954d15a334621def53acceb6799)(ctx);

978

979 if (sqe == NULL) {

980 return -[ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5);

981 }

982 if (handle != NULL) {

983 \*handle = sqe;

984 }

985 [rtio\_sqe\_prep\_read\_multishot](group__rtio.md#ga9803aa829f8c0eeee746ea7d872c20cc)(sqe, [iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc), [RTIO\_PRIO\_NORM](group__rtio__sqe__prio.md#gab02e27e01b7dd4eb3439df557899ce92), [userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971));

986 }

987 [rtio\_submit](group__rtio.md#gafee27c64a4a4989c4eb774addde8eb2e)(ctx, 0);

988 return 0;

989}

990

[ 1004](group__sensor__interface.md#ga385feca2a8b65cb6a24443a5d903ca8b)static inline int [sensor\_read](group__sensor__interface.md#ga385feca2a8b65cb6a24443a5d903ca8b)(struct [rtio\_iodev](structrtio__iodev.md) \*[iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc), struct [rtio](structrtio.md) \*ctx, void \*[userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971))

1005{

1006 if ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_USERSPACE)) {

1007 struct [rtio\_sqe](structrtio__sqe.md) sqe;

1008

1009 [rtio\_sqe\_prep\_read\_with\_pool](group__rtio.md#ga15c1f623658d27d300d1a31a6f3d6b9d)(&sqe, [iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc), [RTIO\_PRIO\_NORM](group__rtio__sqe__prio.md#gab02e27e01b7dd4eb3439df557899ce92), [userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971));

1010 [rtio\_sqe\_copy\_in](group__rtio.md#ga65e351af0a16dcf504a51ef4eb9316c7)(ctx, &sqe, 1);

1011 } else {

1012 struct [rtio\_sqe](structrtio__sqe.md) \*sqe = [rtio\_sqe\_acquire](group__rtio.md#ga8b47c954d15a334621def53acceb6799)(ctx);

1013

1014 if (sqe == NULL) {

1015 return -[ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5);

1016 }

1017 [rtio\_sqe\_prep\_read\_with\_pool](group__rtio.md#ga15c1f623658d27d300d1a31a6f3d6b9d)(sqe, [iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc), [RTIO\_PRIO\_NORM](group__rtio__sqe__prio.md#gab02e27e01b7dd4eb3439df557899ce92), [userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971));

1018 }

1019 [rtio\_submit](group__rtio.md#gafee27c64a4a4989c4eb774addde8eb2e)(ctx, 0);

1020 return 0;

1021}

1022

[ 1034](group__sensor__interface.md#gaa8cd6e4fadb5d69e59d101733b4fb462)typedef void (\*[sensor\_processing\_callback\_t](group__sensor__interface.md#gaa8cd6e4fadb5d69e59d101733b4fb462))(int result, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structrtio__sqe.md#a55e98f27b26393fee8e179b7bdb6a52e), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722),

1035 void \*[userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971));

1036

[ 1048](group__sensor__interface.md#gabb076531445e1b128d515b28c7cc9dc8)void [sensor\_processing\_with\_callback](group__sensor__interface.md#gabb076531445e1b128d515b28c7cc9dc8)(struct [rtio](structrtio.md) \*ctx, [sensor\_processing\_callback\_t](group__sensor__interface.md#gaa8cd6e4fadb5d69e59d101733b4fb462) cb);

1049

1050#endif /\* defined(CONFIG\_SENSOR\_ASYNC\_API) || defined(\_\_DOXYGEN\_\_) \*/

1051

[ 1055](group__sensor__interface.md#ga0066e049c4f084305ca2b978e5c7454d)#define SENSOR\_G 9806650LL

1056

[ 1060](group__sensor__interface.md#ga6ebdc2f6942334de3cc248a53db7df33)#define SENSOR\_PI 3141592LL

1061

[ 1070](group__sensor__interface.md#gab797f2f578b1c9cc44f54ab5d503bbf8)static inline [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [sensor\_ms2\_to\_g](group__sensor__interface.md#gab797f2f578b1c9cc44f54ab5d503bbf8)(const struct [sensor\_value](structsensor__value.md) \*ms2)

1071{

1072 [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) micro\_ms2 = ms2->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) \* 1000000LL + ms2->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b);

1073

1074 if (micro\_ms2 > 0) {

1075 return (micro\_ms2 + [SENSOR\_G](group__sensor__interface.md#ga0066e049c4f084305ca2b978e5c7454d) / 2) / [SENSOR\_G](group__sensor__interface.md#ga0066e049c4f084305ca2b978e5c7454d);

1076 } else {

1077 return (micro\_ms2 - [SENSOR\_G](group__sensor__interface.md#ga0066e049c4f084305ca2b978e5c7454d) / 2) / [SENSOR\_G](group__sensor__interface.md#ga0066e049c4f084305ca2b978e5c7454d);

1078 }

1079}

1080

[ 1087](group__sensor__interface.md#ga6ab9ce9c6ee2e52d197e5cb4ccd88979)static inline void [sensor\_g\_to\_ms2](group__sensor__interface.md#ga6ab9ce9c6ee2e52d197e5cb4ccd88979)([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) g, struct [sensor\_value](structsensor__value.md) \*ms2)

1088{

1089 ms2->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) = (([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))g \* [SENSOR\_G](group__sensor__interface.md#ga0066e049c4f084305ca2b978e5c7454d)) / 1000000LL;

1090 ms2->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b) = (([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))g \* [SENSOR\_G](group__sensor__interface.md#ga0066e049c4f084305ca2b978e5c7454d)) % 1000000LL;

1091}

1092

[ 1101](group__sensor__interface.md#ga3db980100e634310a0a1623136048742)static inline [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [sensor\_ms2\_to\_ug](group__sensor__interface.md#ga3db980100e634310a0a1623136048742)(const struct [sensor\_value](structsensor__value.md) \*ms2)

1102{

1103 [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) micro\_ms2 = (ms2->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) \* [INT64\_C](llvm_8h.md#a93d102802b35d3b8abae9bbe7f0fed75)(1000000)) + ms2->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b);

1104

1105 return (micro\_ms2 \* 1000000LL) / [SENSOR\_G](group__sensor__interface.md#ga0066e049c4f084305ca2b978e5c7454d);

1106}

1107

[ 1114](group__sensor__interface.md#ga28a1c6cf74a391712a4697792f759d62)static inline void [sensor\_ug\_to\_ms2](group__sensor__interface.md#ga28a1c6cf74a391712a4697792f759d62)([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) ug, struct [sensor\_value](structsensor__value.md) \*ms2)

1115{

1116 ms2->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) = (([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))ug \* [SENSOR\_G](group__sensor__interface.md#ga0066e049c4f084305ca2b978e5c7454d) / 1000000LL) / 1000000LL;

1117 ms2->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b) = (([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))ug \* [SENSOR\_G](group__sensor__interface.md#ga0066e049c4f084305ca2b978e5c7454d) / 1000000LL) % 1000000LL;

1118}

1119

[ 1127](group__sensor__interface.md#ga040a907c8934baab66d27b8dfb1ea220)static inline [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [sensor\_rad\_to\_degrees](group__sensor__interface.md#ga040a907c8934baab66d27b8dfb1ea220)(const struct [sensor\_value](structsensor__value.md) \*rad)

1128{

1129 [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) micro\_rad\_s = rad->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) \* 1000000LL + rad->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b);

1130

1131 if (micro\_rad\_s > 0) {

1132 return (micro\_rad\_s \* 180LL + [SENSOR\_PI](group__sensor__interface.md#ga6ebdc2f6942334de3cc248a53db7df33) / 2) / [SENSOR\_PI](group__sensor__interface.md#ga6ebdc2f6942334de3cc248a53db7df33);

1133 } else {

1134 return (micro\_rad\_s \* 180LL - [SENSOR\_PI](group__sensor__interface.md#ga6ebdc2f6942334de3cc248a53db7df33) / 2) / [SENSOR\_PI](group__sensor__interface.md#ga6ebdc2f6942334de3cc248a53db7df33);

1135 }

1136}

1137

[ 1144](group__sensor__interface.md#ga39d4b84f5d792e27b2d6d5eb6a2ccb0d)static inline void [sensor\_degrees\_to\_rad](group__sensor__interface.md#ga39d4b84f5d792e27b2d6d5eb6a2ccb0d)([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), struct [sensor\_value](structsensor__value.md) \*rad)

1145{

1146 rad->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) = (([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417) \* [SENSOR\_PI](group__sensor__interface.md#ga6ebdc2f6942334de3cc248a53db7df33) / 180LL) / 1000000LL;

1147 rad->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b) = (([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417) \* [SENSOR\_PI](group__sensor__interface.md#ga6ebdc2f6942334de3cc248a53db7df33) / 180LL) % 1000000LL;

1148}

1149

[ 1161](group__sensor__interface.md#gad80093a6cfe95428dd0ead85547838a6)static inline [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [sensor\_rad\_to\_10udegrees](group__sensor__interface.md#gad80093a6cfe95428dd0ead85547838a6)(const struct [sensor\_value](structsensor__value.md) \*rad)

1162{

1163 [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) micro\_rad\_s = rad->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) \* 1000000LL + rad->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b);

1164

1165 return (micro\_rad\_s \* 180LL \* 100000LL) / [SENSOR\_PI](group__sensor__interface.md#ga6ebdc2f6942334de3cc248a53db7df33);

1166}

1167

[ 1174](group__sensor__interface.md#gab53418e1eb164364663d3ec3f40399a4)static inline void [sensor\_10udegrees\_to\_rad](group__sensor__interface.md#gab53418e1eb164364663d3ec3f40399a4)([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), struct [sensor\_value](structsensor__value.md) \*rad)

1175{

1176 rad->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) = (([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417) \* [SENSOR\_PI](group__sensor__interface.md#ga6ebdc2f6942334de3cc248a53db7df33) / 180LL / 100000LL) / 1000000LL;

1177 rad->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b) = (([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417) \* [SENSOR\_PI](group__sensor__interface.md#ga6ebdc2f6942334de3cc248a53db7df33) / 180LL / 100000LL) % 1000000LL;

1178}

1179

[ 1186](group__sensor__interface.md#ga29223b754dc436ab1e97ce6209a3ea06)static inline double [sensor\_value\_to\_double](group__sensor__interface.md#ga29223b754dc436ab1e97ce6209a3ea06)(const struct [sensor\_value](structsensor__value.md) \*val)

1187{

1188 return (double)val->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) + (double)val->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b) / 1000000;

1189}

1190

[ 1197](group__sensor__interface.md#ga2ad1fc2abd1c8c38e7de6e99fa5c1f20)static inline float [sensor\_value\_to\_float](group__sensor__interface.md#ga2ad1fc2abd1c8c38e7de6e99fa5c1f20)(const struct [sensor\_value](structsensor__value.md) \*val)

1198{

1199 return (float)val->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) + (float)val->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b) / 1000000;

1200}

1201

[ 1209](group__sensor__interface.md#gaf01bbb251ad0c7f6c55c5b702e8a4048)static inline int [sensor\_value\_from\_double](group__sensor__interface.md#gaf01bbb251ad0c7f6c55c5b702e8a4048)(struct [sensor\_value](structsensor__value.md) \*val, double inp)

1210{

1211 if (inp < INT32\_MIN || inp > [INT32\_MAX](stdint_8h.md#a181807730d4a375f848ba139813ce04f)) {

1212 return -[ERANGE](group__system__errno.md#gaa1591a4f3a86360108de5b9ba34980ca);

1213 }

1214

1215 double val2 = (inp - ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))inp) \* 1000000.0;

1216

1217 if (val2 < INT32\_MIN || val2 > [INT32\_MAX](stdint_8h.md#a181807730d4a375f848ba139813ce04f)) {

1218 return -[ERANGE](group__system__errno.md#gaa1591a4f3a86360108de5b9ba34980ca);

1219 }

1220

1221 val->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) = ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))inp;

1222 val->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b) = ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))val2;

1223

1224 return 0;

1225}

1226

[ 1234](group__sensor__interface.md#ga64d5a1725eda200c80daf42b1067c46c)static inline int [sensor\_value\_from\_float](group__sensor__interface.md#ga64d5a1725eda200c80daf42b1067c46c)(struct [sensor\_value](structsensor__value.md) \*val, float inp)

1235{

1236 float val2 = (inp - ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))inp) \* 1000000.0f;

1237

1238 if (val2 < INT32\_MIN || val2 > (float)([INT32\_MAX](stdint_8h.md#a181807730d4a375f848ba139813ce04f) - 1)) {

1239 return -[ERANGE](group__system__errno.md#gaa1591a4f3a86360108de5b9ba34980ca);

1240 }

1241

1242 val->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) = ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))inp;

1243 val->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b) = ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))val2;

1244

1245 return 0;

1246}

1247

1248#ifdef CONFIG\_SENSOR\_INFO

1249

1250struct sensor\_info {

1251 const struct device \*dev;

1252 const char \*vendor;

1253 const char \*model;

1254 const char \*friendly\_name;

1255};

1256

1257#define SENSOR\_INFO\_INITIALIZER(\_dev, \_vendor, \_model, \_friendly\_name) \

1258 { \

1259 .dev = \_dev, \

1260 .vendor = \_vendor, \

1261 .model = \_model, \

1262 .friendly\_name = \_friendly\_name, \

1263 }

1264

1265#define SENSOR\_INFO\_DEFINE(name, ...) \

1266 static const STRUCT\_SECTION\_ITERABLE(sensor\_info, name) = \

1267 SENSOR\_INFO\_INITIALIZER(\_\_VA\_ARGS\_\_)

1268

1269#define SENSOR\_INFO\_DT\_NAME(node\_id) \

1270 \_CONCAT(\_\_sensor\_info, DEVICE\_DT\_NAME\_GET(node\_id))

1271

1272#define SENSOR\_INFO\_DT\_DEFINE(node\_id) \

1273 SENSOR\_INFO\_DEFINE(SENSOR\_INFO\_DT\_NAME(node\_id), \

1274 DEVICE\_DT\_GET(node\_id), \

1275 DT\_NODE\_VENDOR\_OR(node\_id, NULL), \

1276 DT\_NODE\_MODEL\_OR(node\_id, NULL), \

1277 DT\_PROP\_OR(node\_id, friendly\_name, NULL)) \

1278

1279#else

1280

[ 1281](group__sensor__interface.md#ga7467206da76c3704d2e491d1b1c0973a)#define SENSOR\_INFO\_DEFINE(name, ...)

[ 1282](group__sensor__interface.md#ga9e6acbc580e9223bfb86ee8919cdc778)#define SENSOR\_INFO\_DT\_DEFINE(node\_id)

1283

1284#endif /\* CONFIG\_SENSOR\_INFO \*/

1285

[ 1313](group__sensor__interface.md#gaa67ca630e3931a0c3821ba438c86690c)#define SENSOR\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm\_device, \

1314 data\_ptr, cfg\_ptr, level, prio, \

1315 api\_ptr, ...) \

1316 DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm\_device, \

1317 data\_ptr, cfg\_ptr, level, prio, \

1318 api\_ptr, \_\_VA\_ARGS\_\_); \

1319 \

1320 SENSOR\_INFO\_DT\_DEFINE(node\_id);

1321

[ 1331](group__sensor__interface.md#ga284dc3b9018f14161dc0a2b6bed9a37e)#define SENSOR\_DEVICE\_DT\_INST\_DEFINE(inst, ...) \

1332 SENSOR\_DEVICE\_DT\_DEFINE(DT\_DRV\_INST(inst), \_\_VA\_ARGS\_\_)

1333

[ 1340](group__sensor__interface.md#ga6d69a9644e08a9cd7773645fa11293e3)static inline [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [sensor\_value\_to\_milli](group__sensor__interface.md#ga6d69a9644e08a9cd7773645fa11293e3)(const struct [sensor\_value](structsensor__value.md) \*val)

1341{

1342 return (([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))val->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) \* 1000) + val->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b) / 1000;

1343}

1344

[ 1351](group__sensor__interface.md#ga9bf7faf60aa54a7540e9b73a61864e25)static inline [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [sensor\_value\_to\_micro](group__sensor__interface.md#ga9bf7faf60aa54a7540e9b73a61864e25)(const struct [sensor\_value](structsensor__value.md) \*val)

1352{

1353 return (([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))val->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) \* 1000000) + val->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b);

1354}

1355

[ 1363](group__sensor__interface.md#ga88b2605526e37420db871f066c5053b3)static inline int [sensor\_value\_from\_milli](group__sensor__interface.md#ga88b2605526e37420db871f066c5053b3)(struct [sensor\_value](structsensor__value.md) \*val, [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) milli)

1364{

1365 if (milli < (([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))[INT32\_MIN](stdint_8h.md#a688eb21a22db27c2b2bd5836943cdcbe) - 1) \* 1000LL ||

1366 milli > (([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))[INT32\_MAX](stdint_8h.md#a181807730d4a375f848ba139813ce04f) + 1) \* 1000LL) {

1367 return -[ERANGE](group__system__errno.md#gaa1591a4f3a86360108de5b9ba34980ca);

1368 }

1369

1370 val->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) = ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))(milli / 1000);

1371 val->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b) = ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))(milli % 1000) \* 1000;

1372

1373 return 0;

1374}

1375

[ 1383](group__sensor__interface.md#gabff019c63c89cbc546c0981819040c99)static inline int [sensor\_value\_from\_micro](group__sensor__interface.md#gabff019c63c89cbc546c0981819040c99)(struct [sensor\_value](structsensor__value.md) \*val, [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) micro)

1384{

1385 if (micro < (([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))[INT32\_MIN](stdint_8h.md#a688eb21a22db27c2b2bd5836943cdcbe) - 1) \* 1000000LL ||

1386 micro > (([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))[INT32\_MAX](stdint_8h.md#a181807730d4a375f848ba139813ce04f) + 1) \* 1000000LL) {

1387 return -[ERANGE](group__system__errno.md#gaa1591a4f3a86360108de5b9ba34980ca);

1388 }

1389

1390 val->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) = ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))(micro / 1000000LL);

1391 val->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b) = ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))(micro % 1000000LL);

1392

1393 return 0;

1394}

1395

1399

[ 1405](sensor_8h.md#a8d3434eb5860c2f2e6fe36b4de920c8c)#define SENSOR\_DECODER\_NAME() UTIL\_CAT(DT\_DRV\_COMPAT, \_\_decoder\_api)

1406

[ 1414](sensor_8h.md#a82da2432981c593ed638a21c51fb0873)#define SENSOR\_DECODER\_DT\_GET(node\_id) \

1415 &UTIL\_CAT(DT\_STRING\_TOKEN\_BY\_IDX(node\_id, compatible, 0), \_\_decoder\_api)

1416

[ 1432](sensor_8h.md#a78ad4b76be4a6f5347ba82b7db43b7c2)#define SENSOR\_DECODER\_API\_DT\_DEFINE() \

1433 COND\_CODE\_1(DT\_HAS\_COMPAT\_STATUS\_OKAY(DT\_DRV\_COMPAT), (), (static)) \

1434 const STRUCT\_SECTION\_ITERABLE(sensor\_decoder\_api, SENSOR\_DECODER\_NAME())

1435

1436#define Z\_MAYBE\_SENSOR\_DECODER\_DECLARE\_INTERNAL\_IDX(node\_id, prop, idx) \

1437 extern const struct sensor\_decoder\_api UTIL\_CAT( \

1438 DT\_STRING\_TOKEN\_BY\_IDX(node\_id, prop, idx), \_\_decoder\_api);

1439

1440#define Z\_MAYBE\_SENSOR\_DECODER\_DECLARE\_INTERNAL(node\_id) \

1441 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, compatible), \

1442 (DT\_FOREACH\_PROP\_ELEM(node\_id, compatible, \

1443 Z\_MAYBE\_SENSOR\_DECODER\_DECLARE\_INTERNAL\_IDX)), \

1444 ())

1445

1446[DT\_FOREACH\_STATUS\_OKAY\_NODE](group__devicetree-generic-foreach.md#ga926f68202042c9db05390e628787f916)(Z\_MAYBE\_SENSOR\_DECODER\_DECLARE\_INTERNAL)

1447

1448#ifdef \_\_cplusplus

1449}

1450#endif

1451

1452#include <syscalls/sensor.h>

1453

1454#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_H\_ \*/

[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)

irp nz macro MOVR cc d

**Definition** asm-macro-32-bit-gnu.h:11

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[DT\_FOREACH\_STATUS\_OKAY\_NODE](group__devicetree-generic-foreach.md#ga926f68202042c9db05390e628787f916)

#define DT\_FOREACH\_STATUS\_OKAY\_NODE(fn)

Invokes fn for every status okay node in the tree.

**Definition** devicetree.h:2671

[RTIO\_PRIO\_NORM](group__rtio__sqe__prio.md#gab02e27e01b7dd4eb3439df557899ce92)

#define RTIO\_PRIO\_NORM

Normal priority.

**Definition** rtio.h:68

[rtio\_sqe\_prep\_read\_with\_pool](group__rtio.md#ga15c1f623658d27d300d1a31a6f3d6b9d)

static void rtio\_sqe\_prep\_read\_with\_pool(struct rtio\_sqe \*sqe, const struct rtio\_iodev \*iodev, int8\_t prio, void \*userdata)

Prepare a read op submission with context's mempool.

**Definition** rtio.h:511

[rtio\_sqe\_copy\_in](group__rtio.md#ga65e351af0a16dcf504a51ef4eb9316c7)

static int rtio\_sqe\_copy\_in(struct rtio \*r, const struct rtio\_sqe \*sqes, size\_t sqe\_count)

Copy an array of SQEs into the queue.

**Definition** rtio.h:1359

[rtio\_sqe\_copy\_in\_get\_handles](group__rtio.md#ga830863e6c8d9b96f4c473a038cab8f8c)

int rtio\_sqe\_copy\_in\_get\_handles(struct rtio \*r, const struct rtio\_sqe \*sqes, struct rtio\_sqe \*\*handle, size\_t sqe\_count)

Copy an array of SQEs into the queue and get resulting handles back.

[rtio\_sqe\_acquire](group__rtio.md#ga8b47c954d15a334621def53acceb6799)

static struct rtio\_sqe \* rtio\_sqe\_acquire(struct rtio \*r)

Acquire a single submission queue event if available.

**Definition** rtio.h:895

[rtio\_sqe\_prep\_read\_multishot](group__rtio.md#ga9803aa829f8c0eeee746ea7d872c20cc)

static void rtio\_sqe\_prep\_read\_multishot(struct rtio\_sqe \*sqe, const struct rtio\_iodev \*iodev, int8\_t prio, void \*userdata)

**Definition** rtio.h:519

[rtio\_submit](group__rtio.md#gafee27c64a4a4989c4eb774addde8eb2e)

int rtio\_submit(struct rtio \*r, uint32\_t wait\_count)

Submit I/O requests to the underlying executor.

[SENSOR\_G](group__sensor__interface.md#ga0066e049c4f084305ca2b978e5c7454d)

#define SENSOR\_G

The value of gravitational constant in micro m/s^2.

**Definition** sensor.h:1055

[sensor\_attr\_get\_t](group__sensor__interface.md#ga00d05c82b46e56dca5f6e8f7f01c31b8)

int(\* sensor\_attr\_get\_t)(const struct device \*dev, enum sensor\_channel chan, enum sensor\_attribute attr, struct sensor\_value \*val)

Callback API upon getting a sensor's attributes.

**Definition** sensor.h:385

[sensor\_decode](group__sensor__interface.md#ga018bca56056ae2558f9e45aeb2fa5f53)

static int sensor\_decode(struct sensor\_decode\_context \*ctx, void \*out, uint16\_t max\_count)

Decode N frames using a sensor\_decode\_context.

**Definition** sensor.h:542

[sensor\_rad\_to\_degrees](group__sensor__interface.md#ga040a907c8934baab66d27b8dfb1ea220)

static int32\_t sensor\_rad\_to\_degrees(const struct sensor\_value \*rad)

Helper function for converting radians to degrees.

**Definition** sensor.h:1127

[sensor\_trigger\_type](group__sensor__interface.md#ga08215279400e8c9eb05ce4e4f0898ffd)

sensor\_trigger\_type

Sensor trigger types.

**Definition** sensor.h:213

[sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b)

sensor\_attribute

Sensor attribute types.

**Definition** sensor.h:290

[sensor\_get\_decoder](group__sensor__interface.md#ga12db6fc43adce48d34c25c16fd2336a3)

int sensor\_get\_decoder(const struct device \*dev, const struct sensor\_decoder\_api \*\*decoder)

Get the sensor's decoder API.

[sensor\_get\_decoder\_t](group__sensor__interface.md#ga21e407d552d140cfb6bfd0d9513c7d42)

int(\* sensor\_get\_decoder\_t)(const struct device \*dev, const struct sensor\_decoder\_api \*\*api)

Get the decoder associate with the given device.

**Definition** sensor.h:557

[sensor\_ug\_to\_ms2](group__sensor__interface.md#ga28a1c6cf74a391712a4697792f759d62)

static void sensor\_ug\_to\_ms2(int32\_t ug, struct sensor\_value \*ms2)

Helper function to convert acceleration from micro Gs to m/s^2.

**Definition** sensor.h:1114

[sensor\_value\_to\_double](group__sensor__interface.md#ga29223b754dc436ab1e97ce6209a3ea06)

static double sensor\_value\_to\_double(const struct sensor\_value \*val)

Helper function for converting struct sensor\_value to double.

**Definition** sensor.h:1186

[sensor\_value\_to\_float](group__sensor__interface.md#ga2ad1fc2abd1c8c38e7de6e99fa5c1f20)

static float sensor\_value\_to\_float(const struct sensor\_value \*val)

Helper function for converting struct sensor\_value to float.

**Definition** sensor.h:1197

[sensor\_attr\_set\_t](group__sensor__interface.md#ga38422ace4194a66a9a912a8ef1e088fb)

int(\* sensor\_attr\_set\_t)(const struct device \*dev, enum sensor\_channel chan, enum sensor\_attribute attr, const struct sensor\_value \*val)

Callback API upon setting a sensor's attributes.

**Definition** sensor.h:374

[sensor\_read](group__sensor__interface.md#ga385feca2a8b65cb6a24443a5d903ca8b)

static int sensor\_read(struct rtio\_iodev \*iodev, struct rtio \*ctx, void \*userdata)

Read data from a sensor.

**Definition** sensor.h:1004

[sensor\_degrees\_to\_rad](group__sensor__interface.md#ga39d4b84f5d792e27b2d6d5eb6a2ccb0d)

static void sensor\_degrees\_to\_rad(int32\_t d, struct sensor\_value \*rad)

Helper function for converting degrees to radians.

**Definition** sensor.h:1144

[sensor\_ms2\_to\_ug](group__sensor__interface.md#ga3db980100e634310a0a1623136048742)

static int32\_t sensor\_ms2\_to\_ug(const struct sensor\_value \*ms2)

Helper function to convert acceleration from m/s^2 to micro Gs.

**Definition** sensor.h:1101

[sensor\_channel\_get\_t](group__sensor__interface.md#ga5c9b5ed9097464562004b446856043fd)

int(\* sensor\_channel\_get\_t)(const struct device \*dev, enum sensor\_channel chan, struct sensor\_value \*val)

Callback API for getting a reading from a sensor.

**Definition** sensor.h:413

[sensor\_natively\_supported\_channel\_size\_info](group__sensor__interface.md#ga5d905ca03326972f3e08c92939c2a558)

int sensor\_natively\_supported\_channel\_size\_info(enum sensor\_channel channel, size\_t \*base\_size, size\_t \*frame\_size)

[sensor\_value\_from\_float](group__sensor__interface.md#ga64d5a1725eda200c80daf42b1067c46c)

static int sensor\_value\_from\_float(struct sensor\_value \*val, float inp)

Helper function for converting float to struct sensor\_value.

**Definition** sensor.h:1234

[sensor\_g\_to\_ms2](group__sensor__interface.md#ga6ab9ce9c6ee2e52d197e5cb4ccd88979)

static void sensor\_g\_to\_ms2(int32\_t g, struct sensor\_value \*ms2)

Helper function to convert acceleration from Gs to m/s^2.

**Definition** sensor.h:1087

[sensor\_value\_to\_milli](group__sensor__interface.md#ga6d69a9644e08a9cd7773645fa11293e3)

static int64\_t sensor\_value\_to\_milli(const struct sensor\_value \*val)

Helper function for converting struct sensor\_value to integer milli units.

**Definition** sensor.h:1340

[SENSOR\_PI](group__sensor__interface.md#ga6ebdc2f6942334de3cc248a53db7df33)

#define SENSOR\_PI

The value of constant PI in micros.

**Definition** sensor.h:1060

[sensor\_trigger\_set](group__sensor__interface.md#ga7c72aca732e0641612d2f9437c2e41b7)

static int sensor\_trigger\_set(const struct device \*dev, const struct sensor\_trigger \*trig, sensor\_trigger\_handler\_t handler)

Activate a sensor's trigger and set the trigger handler.

**Definition** sensor.h:756

[sensor\_stream\_data\_opt](group__sensor__interface.md#ga8613a20521a37d40fd7371dc63ba2dac)

sensor\_stream\_data\_opt

Options for what to do with the associated data when a trigger is consumed.

**Definition** sensor.h:563

[sensor\_value\_from\_milli](group__sensor__interface.md#ga88b2605526e37420db871f066c5053b3)

static int sensor\_value\_from\_milli(struct sensor\_value \*val, int64\_t milli)

Helper function for converting integer milli units to struct sensor\_value.

**Definition** sensor.h:1363

[sensor\_trigger\_handler\_t](group__sensor__interface.md#ga890c1fb6d6974aea22a2d08829a75902)

void(\* sensor\_trigger\_handler\_t)(const struct device \*dev, const struct sensor\_trigger \*trigger)

Callback API upon firing of a trigger.

**Definition** sensor.h:365

[sensor\_reconfigure\_read\_iodev](group__sensor__interface.md#ga949ab4cb1f0572d63eb439d34dad61cc)

int sensor\_reconfigure\_read\_iodev(struct rtio\_iodev \*iodev, const struct device \*sensor, const enum sensor\_channel \*channels, size\_t num\_channels)

Reconfigure a reading iodev.

[sensor\_value\_to\_micro](group__sensor__interface.md#ga9bf7faf60aa54a7540e9b73a61864e25)

static int64\_t sensor\_value\_to\_micro(const struct sensor\_value \*val)

Helper function for converting struct sensor\_value to integer micro units.

**Definition** sensor.h:1351

[sensor\_channel\_get](group__sensor__interface.md#ga9e0e6c1408d32c52267984bae7cb268d)

int sensor\_channel\_get(const struct device \*dev, enum sensor\_channel chan, struct sensor\_value \*val)

Get a reading from a sensor device.

[sensor\_sample\_fetch](group__sensor__interface.md#gaa75e25d93ee7cac0bf38399f3c006dff)

int sensor\_sample\_fetch(const struct device \*dev)

Fetch a sample from the sensor and store it in an internal driver buffer.

[sensor\_processing\_callback\_t](group__sensor__interface.md#gaa8cd6e4fadb5d69e59d101733b4fb462)

void(\* sensor\_processing\_callback\_t)(int result, uint8\_t \*buf, uint32\_t buf\_len, void \*userdata)

Callback function used with the helper processing function.

**Definition** sensor.h:1034

[sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934)

sensor\_channel

Sensor channels.

**Definition** sensor.h:59

[sensor\_10udegrees\_to\_rad](group__sensor__interface.md#gab53418e1eb164364663d3ec3f40399a4)

static void sensor\_10udegrees\_to\_rad(int32\_t d, struct sensor\_value \*rad)

Helper function for converting 10 micro degrees to radians.

**Definition** sensor.h:1174

[sensor\_ms2\_to\_g](group__sensor__interface.md#gab797f2f578b1c9cc44f54ab5d503bbf8)

static int32\_t sensor\_ms2\_to\_g(const struct sensor\_value \*ms2)

Helper function to convert acceleration from m/s^2 to Gs.

**Definition** sensor.h:1070

[sensor\_submit\_t](group__sensor__interface.md#gab8e7a28e19d596ddcbefeb34d84a2b3c)

int(\* sensor\_submit\_t)(const struct device \*sensor, struct rtio\_iodev\_sqe \*sqe)

**Definition** sensor.h:652

[sensor\_processing\_with\_callback](group__sensor__interface.md#gabb076531445e1b128d515b28c7cc9dc8)

void sensor\_processing\_with\_callback(struct rtio \*ctx, sensor\_processing\_callback\_t cb)

Helper function for common processing of sensor data.

[sensor\_value\_from\_micro](group__sensor__interface.md#gabff019c63c89cbc546c0981819040c99)

static int sensor\_value\_from\_micro(struct sensor\_value \*val, int64\_t micro)

Helper function for converting integer micro units to struct sensor\_value.

**Definition** sensor.h:1383

[sensor\_sample\_fetch\_chan](group__sensor__interface.md#gac16192826432438a15274cf28d66e8a6)

int sensor\_sample\_fetch\_chan(const struct device \*dev, enum sensor\_channel type)

Fetch a sample from the sensor and store it in an internal driver buffer.

[sensor\_stream](group__sensor__interface.md#gac77fc83844935f61a2bf9ab2c38987b6)

static int sensor\_stream(struct rtio\_iodev \*iodev, struct rtio \*ctx, void \*userdata, struct rtio\_sqe \*\*handle)

**Definition** sensor.h:968

[sensor\_sample\_fetch\_t](group__sensor__interface.md#gacae110a4edb6f29dfb457cb1ea8d68c1)

int(\* sensor\_sample\_fetch\_t)(const struct device \*dev, enum sensor\_channel chan)

Callback API for fetching data from a sensor.

**Definition** sensor.h:405

[sensor\_trigger\_set\_t](group__sensor__interface.md#gad7f7a3d9e714cc16f23656ca06592aa4)

int(\* sensor\_trigger\_set\_t)(const struct device \*dev, const struct sensor\_trigger \*trig, sensor\_trigger\_handler\_t handler)

Callback API for setting a sensor's trigger and handler.

**Definition** sensor.h:396

[sensor\_rad\_to\_10udegrees](group__sensor__interface.md#gad80093a6cfe95428dd0ead85547838a6)

static int32\_t sensor\_rad\_to\_10udegrees(const struct sensor\_value \*rad)

Helper function for converting radians to 10 micro degrees.

**Definition** sensor.h:1161

[sensor\_attr\_get](group__sensor__interface.md#gaedfdfc71dce702dc1fb1c6e60ff0f73a)

int sensor\_attr\_get(const struct device \*dev, enum sensor\_channel chan, enum sensor\_attribute attr, struct sensor\_value \*val)

Get an attribute for a sensor.

[sensor\_value\_from\_double](group__sensor__interface.md#gaf01bbb251ad0c7f6c55c5b702e8a4048)

static int sensor\_value\_from\_double(struct sensor\_value \*val, double inp)

Helper function for converting double to struct sensor\_value.

**Definition** sensor.h:1209

[sensor\_attr\_set](group__sensor__interface.md#gafbf65226a227e9f8824908bc38e336f5)

int sensor\_attr\_set(const struct device \*dev, enum sensor\_channel chan, enum sensor\_attribute attr, const struct sensor\_value \*val)

Set an attribute for a sensor.

[SENSOR\_TRIG\_DELTA](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda3bb90a3334bcf613c9efbdf2ed05f855)

@ SENSOR\_TRIG\_DELTA

Trigger fires when the selected channel varies significantly.

**Definition** sensor.h:229

[SENSOR\_TRIG\_NEAR\_FAR](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda448226d83b28c2862c353a8cda7be0d5)

@ SENSOR\_TRIG\_NEAR\_FAR

Trigger fires when a near/far event is detected.

**Definition** sensor.h:231

[SENSOR\_TRIG\_FREEFALL](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda4943ffb4afaf4cbae39e85693bd4374c)

@ SENSOR\_TRIG\_FREEFALL

Trigger fires when a free fall is detected.

**Definition** sensor.h:247

[SENSOR\_TRIG\_PRIV\_START](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda5e1a94f21fee67ee98296153ea640921)

@ SENSOR\_TRIG\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:269

[SENSOR\_TRIG\_FIFO\_FULL](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda66f913f8751a77a6c16745e329c7315c)

@ SENSOR\_TRIG\_FIFO\_FULL

Trigger fires when the FIFO becomes full.

**Definition** sensor.h:259

[SENSOR\_TRIG\_MOTION](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda7095387831b763b34171287945dae276)

@ SENSOR\_TRIG\_MOTION

Trigger fires when motion is detected.

**Definition** sensor.h:250

[SENSOR\_TRIG\_STATIONARY](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda79e286ffced716e1076f56464ea47f5d)

@ SENSOR\_TRIG\_STATIONARY

Trigger fires when no motion has been detected for a while.

**Definition** sensor.h:253

[SENSOR\_TRIG\_COMMON\_COUNT](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda8d1f2621fad4fd685d56cca3f9b042f5)

@ SENSOR\_TRIG\_COMMON\_COUNT

Number of all common sensor triggers.

**Definition** sensor.h:263

[SENSOR\_TRIG\_THRESHOLD](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda8f875f881b6540eebc28e3d6a7d46606)

@ SENSOR\_TRIG\_THRESHOLD

Trigger fires when channel reading transitions configured thresholds.

**Definition** sensor.h:238

[SENSOR\_TRIG\_MAX](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda9de566f44de519f94c59c58df1efc4c4)

@ SENSOR\_TRIG\_MAX

Maximum value describing a sensor trigger type.

**Definition** sensor.h:274

[SENSOR\_TRIG\_DOUBLE\_TAP](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdab95e52584a6bc3343181f495cd4cb2ef)

@ SENSOR\_TRIG\_DOUBLE\_TAP

Trigger fires when a double tap is detected.

**Definition** sensor.h:244

[SENSOR\_TRIG\_TIMER](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdabf92b196394726ec90f1d61586a7f023)

@ SENSOR\_TRIG\_TIMER

Timer-based trigger, useful when the sensor does not have an interrupt line.

**Definition** sensor.h:218

[SENSOR\_TRIG\_FIFO\_WATERMARK](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdac5d67fb4fb6206465b1b01dc78245fe4)

@ SENSOR\_TRIG\_FIFO\_WATERMARK

Trigger fires when the FIFO watermark has been reached.

**Definition** sensor.h:256

[SENSOR\_TRIG\_TAP](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdae49a25e6400f0753f6bac8a7d136200d)

@ SENSOR\_TRIG\_TAP

Trigger fires when a single tap is detected.

**Definition** sensor.h:241

[SENSOR\_TRIG\_DATA\_READY](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdaf7c161e309c267a7dd6daf2ad176f44f)

@ SENSOR\_TRIG\_DATA\_READY

Trigger fires whenever new data is ready.

**Definition** sensor.h:220

[SENSOR\_ATTR\_HYSTERESIS](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba044e67bfc04e8ddc2de7d2058fffbc94)

@ SENSOR\_ATTR\_HYSTERESIS

**Definition** sensor.h:308

[SENSOR\_ATTR\_FEATURE\_MASK](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba1f8d2242fa9d63a13c6a48fe3a1cbe52)

@ SENSOR\_ATTR\_FEATURE\_MASK

Enable/disable sensor features.

**Definition** sensor.h:328

[SENSOR\_ATTR\_CALIB\_TARGET](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba3043381b539610a8b424f12d76474bdf)

@ SENSOR\_ATTR\_CALIB\_TARGET

Calibration target.

**Definition** sensor.h:322

[SENSOR\_ATTR\_OFFSET](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba332935dcb6f7e228cb9c595a545079fd)

@ SENSOR\_ATTR\_OFFSET

The sensor value returned will be altered by the amount indicated by offset: final\_value = sensor\_val...

**Definition** sensor.h:317

[SENSOR\_ATTR\_BATCH\_DURATION](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba3b0cf69c77de55c92129e212bf5b8ced)

@ SENSOR\_ATTR\_BATCH\_DURATION

Hardware batch duration in ticks.

**Definition** sensor.h:339

[SENSOR\_ATTR\_OVERSAMPLING](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba3d32987f75284d80d3f64bf44f5c6ccd)

@ SENSOR\_ATTR\_OVERSAMPLING

Oversampling factor.

**Definition** sensor.h:310

[SENSOR\_ATTR\_FF\_DUR](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba5a62ea6aa7e55efd62ab3f93dcb0593a)

@ SENSOR\_ATTR\_FF\_DUR

Free-fall duration represented in milliseconds.

**Definition** sensor.h:336

[SENSOR\_ATTR\_UPPER\_THRESH](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba5af51bd0640a87a94476eee112a4460b)

@ SENSOR\_ATTR\_UPPER\_THRESH

Upper threshold for trigger.

**Definition** sensor.h:299

[SENSOR\_ATTR\_CONFIGURATION](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba75cd3aca26859fd7c10c83d86e3471e9)

@ SENSOR\_ATTR\_CONFIGURATION

Configure the operating modes of a sensor.

**Definition** sensor.h:324

[SENSOR\_ATTR\_CALIBRATION](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba843d1e79573c634987e5e839ba9e965e)

@ SENSOR\_ATTR\_CALIBRATION

Set a calibration value needed by a sensor.

**Definition** sensor.h:326

[SENSOR\_ATTR\_COMMON\_COUNT](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba99ceedef81217614ada0c8a469f91eb8)

@ SENSOR\_ATTR\_COMMON\_COUNT

Number of all common sensor attributes.

**Definition** sensor.h:344

[SENSOR\_ATTR\_ALERT](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940baaedf76e63224adc3fa266d35666e0a3a)

@ SENSOR\_ATTR\_ALERT

Alert threshold or alert enable/disable.

**Definition** sensor.h:330

[SENSOR\_ATTR\_SLOPE\_TH](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bac4538665a244cb7f18fc053c40134302)

@ SENSOR\_ATTR\_SLOPE\_TH

Threshold for any-motion (slope) trigger.

**Definition** sensor.h:301

[SENSOR\_ATTR\_SAMPLING\_FREQUENCY](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bacb07e3508ea5503dbcdceee3f17d2291)

@ SENSOR\_ATTR\_SAMPLING\_FREQUENCY

Sensor sampling frequency, i.e.

**Definition** sensor.h:295

[SENSOR\_ATTR\_FULL\_SCALE](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bad30df3100fb6b285a6a786fdc77234d3)

@ SENSOR\_ATTR\_FULL\_SCALE

Sensor range, in SI units.

**Definition** sensor.h:312

[SENSOR\_ATTR\_LOWER\_THRESH](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940baee644485ab5f64e7c5273bbe562deaaa)

@ SENSOR\_ATTR\_LOWER\_THRESH

Lower threshold for trigger.

**Definition** sensor.h:297

[SENSOR\_ATTR\_SLOPE\_DUR](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940baf510b32b2e2395bbcf1c8fd7159ed2a1)

@ SENSOR\_ATTR\_SLOPE\_DUR

Duration for which the slope values needs to be outside the threshold for the trigger to fire.

**Definition** sensor.h:306

[SENSOR\_ATTR\_MAX](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940baf6bd0b33ca2117ef329692c291f6384b)

@ SENSOR\_ATTR\_MAX

Maximum value describing a sensor attribute type.

**Definition** sensor.h:355

[SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)

@ SENSOR\_ATTR\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:350

[SENSOR\_STREAM\_DATA\_INCLUDE](group__sensor__interface.md#gga8613a20521a37d40fd7371dc63ba2daca2ba3554a08bf55b64da40900592be315)

@ SENSOR\_STREAM\_DATA\_INCLUDE

Include whatever data is associated with the trigger.

**Definition** sensor.h:565

[SENSOR\_STREAM\_DATA\_NOP](group__sensor__interface.md#gga8613a20521a37d40fd7371dc63ba2daca7e897c6d1428ff50f98140ed4cd4d35d)

@ SENSOR\_STREAM\_DATA\_NOP

Do nothing with the associated trigger data, it may be consumed later.

**Definition** sensor.h:567

[SENSOR\_STREAM\_DATA\_DROP](group__sensor__interface.md#gga8613a20521a37d40fd7371dc63ba2dacaa13c6d3bae87c16f9cd89e0fe7144f8e)

@ SENSOR\_STREAM\_DATA\_DROP

Flush/clear whatever data is associated with the trigger.

**Definition** sensor.h:569

[SENSOR\_CHAN\_GAUGE\_STATE\_OF\_HEALTH](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a0613c39397f06d11f4350f8cbcc24cf6)

@ SENSOR\_CHAN\_GAUGE\_STATE\_OF\_HEALTH

State of health measurement in %.

**Definition** sensor.h:176

[SENSOR\_CHAN\_PM\_1\_0](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a08f0c21c33008292b0b58defe5c06815)

@ SENSOR\_CHAN\_PM\_1\_0

1.0 micro-meters Particulate Matter, in ug/m^3

**Definition** sensor.h:111

[SENSOR\_CHAN\_DIE\_TEMP](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a0a8828f51fe15335ad857d136f197ee1)

@ SENSOR\_CHAN\_DIE\_TEMP

Device die temperature in degrees Celsius.

**Definition** sensor.h:85

[SENSOR\_CHAN\_PRESS](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a14cd68844542e23d1b641a2bc54132a9)

@ SENSOR\_CHAN\_PRESS

Pressure in kilopascal.

**Definition** sensor.h:89

[SENSOR\_CHAN\_GAUGE\_TIME\_TO\_FULL](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a14d4c802805e1e07c9b4e47ccaff0eeb)

@ SENSOR\_CHAN\_GAUGE\_TIME\_TO\_FULL

Time to full in minutes.

**Definition** sensor.h:180

[SENSOR\_CHAN\_ACCEL\_XYZ](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a16c05784ae15a4952ea708c2f11a2ae9)

@ SENSOR\_CHAN\_ACCEL\_XYZ

Acceleration on the X, Y and Z axes.

**Definition** sensor.h:67

[SENSOR\_CHAN\_MAGN\_X](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a171f37ba152d34f75ff745cb848b3240)

@ SENSOR\_CHAN\_MAGN\_X

Magnetic field on the X axis, in Gauss.

**Definition** sensor.h:77

[SENSOR\_CHAN\_CURRENT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a1a001ba3ca5ad37308fb7be81f11c950)

@ SENSOR\_CHAN\_CURRENT

Current, in amps.

**Definition** sensor.h:133

[SENSOR\_CHAN\_GYRO\_XYZ](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a1d36b89ab3761e9bc86effc839f8db0e)

@ SENSOR\_CHAN\_GYRO\_XYZ

Angular velocity around the X, Y and Z axes.

**Definition** sensor.h:75

[SENSOR\_CHAN\_VSHUNT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a1ea01c780995ad4539e9ffc2ca6102e9)

@ SENSOR\_CHAN\_VSHUNT

Current Shunt Voltage in milli-volts.

**Definition** sensor.h:130

[SENSOR\_CHAN\_GREEN](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a216a3b2b77d7a92f94547aeb889ae378)

@ SENSOR\_CHAN\_GREEN

Illuminance in green spectrum, in lux.

**Definition** sensor.h:104

[SENSOR\_CHAN\_MAGN\_Z](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a2a2115051ded019a57ece5a00f86ea61)

@ SENSOR\_CHAN\_MAGN\_Z

Magnetic field on the Z axis, in Gauss.

**Definition** sensor.h:81

[SENSOR\_CHAN\_MAGN\_Y](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a2b4f1764f47428c528447347d7730942)

@ SENSOR\_CHAN\_MAGN\_Y

Magnetic field on the Y axis, in Gauss.

**Definition** sensor.h:79

[SENSOR\_CHAN\_GAUGE\_DESIRED\_VOLTAGE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a2c33a7f11d5b3996e95167698a2056cf)

@ SENSOR\_CHAN\_GAUGE\_DESIRED\_VOLTAGE

Desired voltage of cell in V (nominal voltage).

**Definition** sensor.h:186

[SENSOR\_CHAN\_POWER](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a33607371060fca93c3555e8e10d5b177)

@ SENSOR\_CHAN\_POWER

Power in watts.

**Definition** sensor.h:135

[SENSOR\_CHAN\_PM\_2\_5](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a3398fdc51964aa06c9a01096d2fac945)

@ SENSOR\_CHAN\_PM\_2\_5

2.5 micro-meters Particulate Matter, in ug/m^3

**Definition** sensor.h:113

[SENSOR\_CHAN\_RESISTANCE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a34ba555026ff976881142512cc8a616b)

@ SENSOR\_CHAN\_RESISTANCE

Resistance , in Ohm.

**Definition** sensor.h:138

[SENSOR\_CHAN\_GAUGE\_AVG\_CURRENT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a4272c1256cde47006d424c5523d26bf8)

@ SENSOR\_CHAN\_GAUGE\_AVG\_CURRENT

Average current, in amps.

**Definition** sensor.h:156

[SENSOR\_CHAN\_GYRO\_Y](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a4a9533172105fd2e55d96e0122a48847)

@ SENSOR\_CHAN\_GYRO\_Y

Angular velocity around the Y axis, in radians/s.

**Definition** sensor.h:71

[SENSOR\_CHAN\_GAUGE\_DESIRED\_CHARGING\_CURRENT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a4aa8bba1b260e1994542383d8e2e908f)

@ SENSOR\_CHAN\_GAUGE\_DESIRED\_CHARGING\_CURRENT

Desired charging current in mA.

**Definition** sensor.h:188

[SENSOR\_CHAN\_GAUGE\_FULL\_CHARGE\_CAPACITY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a54a6be68e09b9f8ca4d349e3d1445649)

@ SENSOR\_CHAN\_GAUGE\_FULL\_CHARGE\_CAPACITY

Full Charge Capacity in mAh.

**Definition** sensor.h:166

[SENSOR\_CHAN\_ROTATION](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a551ffe08a9b1206e3c051f207b92aabf)

@ SENSOR\_CHAN\_ROTATION

Angular rotation, in degrees.

**Definition** sensor.h:141

[SENSOR\_CHAN\_AMBIENT\_TEMP](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a5bf9c4a677405c4a4df3bc3acd116c7c)

@ SENSOR\_CHAN\_AMBIENT\_TEMP

Ambient temperature in degrees Celsius.

**Definition** sensor.h:87

[SENSOR\_CHAN\_MAGN\_XYZ](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a5d1f48466f6f600503af18427fa3da32)

@ SENSOR\_CHAN\_MAGN\_XYZ

Magnetic field on the X, Y and Z axes.

**Definition** sensor.h:83

[SENSOR\_CHAN\_GAUGE\_STDBY\_CURRENT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a5e6b87cacfe3e4703b963a2177d35cc8)

@ SENSOR\_CHAN\_GAUGE\_STDBY\_CURRENT

Standby current, in amps.

**Definition** sensor.h:158

[SENSOR\_CHAN\_GAUGE\_MAX\_LOAD\_CURRENT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a603335f6a91846c5089a2a541d9053cf)

@ SENSOR\_CHAN\_GAUGE\_MAX\_LOAD\_CURRENT

Max load current, in amps.

**Definition** sensor.h:160

[SENSOR\_CHAN\_ACCEL\_Y](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a61c145468f01916c1a547fb38a1be9a8)

@ SENSOR\_CHAN\_ACCEL\_Y

Acceleration on the Y axis, in m/s^2.

**Definition** sensor.h:63

[SENSOR\_CHAN\_RPM](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a655a576a72cbd6641abc698a3f4304d1)

@ SENSOR\_CHAN\_RPM

Revolutions per minute, in RPM.

**Definition** sensor.h:151

[SENSOR\_CHAN\_GAUGE\_FULL\_AVAIL\_CAPACITY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a688287fa1587944424a2eda13b8d98e8)

@ SENSOR\_CHAN\_GAUGE\_FULL\_AVAIL\_CAPACITY

Full Available Capacity in mAh.

**Definition** sensor.h:172

[SENSOR\_CHAN\_VOLTAGE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a69dd8a737a0cb6f03fa5f60c92840e6d)

@ SENSOR\_CHAN\_VOLTAGE

Voltage, in volts.

**Definition** sensor.h:127

[SENSOR\_CHAN\_BLUE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a6e66f95d73d05c2b3511e2db506844f5)

@ SENSOR\_CHAN\_BLUE

Illuminance in blue spectrum, in lux.

**Definition** sensor.h:106

[SENSOR\_CHAN\_LIGHT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a6e91196c11d080c3f5df55fda190e19d)

@ SENSOR\_CHAN\_LIGHT

Illuminance in visible spectrum, in lux.

**Definition** sensor.h:98

[SENSOR\_CHAN\_GAUGE\_DESIGN\_VOLTAGE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a6f96ba4db6cf812b223f9a09f2a287d0)

@ SENSOR\_CHAN\_GAUGE\_DESIGN\_VOLTAGE

Design voltage of cell in V (max voltage).

**Definition** sensor.h:184

[SENSOR\_CHAN\_ACCEL\_Z](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a78e06bb48cfe06e42829816ad4cb5a0f)

@ SENSOR\_CHAN\_ACCEL\_Z

Acceleration on the Z axis, in m/s^2.

**Definition** sensor.h:65

[SENSOR\_CHAN\_CO2](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a7a23e3e869c5e9a39f6a7bfa28737133)

@ SENSOR\_CHAN\_CO2

CO2 level, in parts per million (ppm).

**Definition** sensor.h:120

[SENSOR\_CHAN\_GAUGE\_STATE\_OF\_CHARGE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a7d67d6842ee787fcc8a4d9ee2cbea139)

@ SENSOR\_CHAN\_GAUGE\_STATE\_OF\_CHARGE

State of charge measurement in %.

**Definition** sensor.h:164

[SENSOR\_CHAN\_GAUGE\_CYCLE\_COUNT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a8834978858c2b62b5e923d06cfcb1a46)

@ SENSOR\_CHAN\_GAUGE\_CYCLE\_COUNT

Cycle count (total number of charge/discharge cycles).

**Definition** sensor.h:182

[SENSOR\_CHAN\_GAUGE\_TEMP](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a8cac65c812b3a1fcb55a53f18d827214)

@ SENSOR\_CHAN\_GAUGE\_TEMP

Gauge temperature.

**Definition** sensor.h:162

[SENSOR\_CHAN\_POS\_DY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a974327ca88ea6d22731cd03afeacef76)

@ SENSOR\_CHAN\_POS\_DY

Position change on the Y axis, in points.

**Definition** sensor.h:146

[SENSOR\_CHAN\_GYRO\_Z](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a9b6b9d13cd8d82449823d65779a87a39)

@ SENSOR\_CHAN\_GYRO\_Z

Angular velocity around the Z axis, in radians/s.

**Definition** sensor.h:73

[SENSOR\_CHAN\_POS\_DX](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aa00b7a857e33c925c910661a91389517)

@ SENSOR\_CHAN\_POS\_DX

Position change on the X axis, in points.

**Definition** sensor.h:144

[SENSOR\_CHAN\_GAUGE\_AVG\_POWER](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aa24f9e12f20a716dd152cf889cb51228)

@ SENSOR\_CHAN\_GAUGE\_AVG\_POWER

Average power in mW.

**Definition** sensor.h:174

[SENSOR\_CHAN\_GAUGE\_TIME\_TO\_EMPTY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aa3755e9fcd8c90fef5185082edb29b65)

@ SENSOR\_CHAN\_GAUGE\_TIME\_TO\_EMPTY

Time to empty in minutes.

**Definition** sensor.h:178

[SENSOR\_CHAN\_PM\_10](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aa450541bde278aefcc9b53bd0826e225)

@ SENSOR\_CHAN\_PM\_10

10 micro-meters Particulate Matter, in ug/m^3

**Definition** sensor.h:115

[SENSOR\_CHAN\_GAUGE\_REMAINING\_CHARGE\_CAPACITY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aaaea6433c82f7b563f86fa53c95ad0ad)

@ SENSOR\_CHAN\_GAUGE\_REMAINING\_CHARGE\_CAPACITY

Remaining Charge Capacity in mAh.

**Definition** sensor.h:168

[SENSOR\_CHAN\_ALL](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ab275027eb550b2b075c44917634eca2c)

@ SENSOR\_CHAN\_ALL

All channels.

**Definition** sensor.h:191

[SENSOR\_CHAN\_GAUGE\_VOLTAGE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ab942649ce1507fb081a77b4bcfc1a57d)

@ SENSOR\_CHAN\_GAUGE\_VOLTAGE

Voltage, in volts.

**Definition** sensor.h:154

[SENSOR\_CHAN\_PROX](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934abaec2c1347ef0035221dd4d9c34a4774)

@ SENSOR\_CHAN\_PROX

Proximity.

**Definition** sensor.h:94

[SENSOR\_CHAN\_COMMON\_COUNT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934abb2893ccb71c9e1eeb155d7cbd539303)

@ SENSOR\_CHAN\_COMMON\_COUNT

Number of all common sensor channels.

**Definition** sensor.h:196

[SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12)

@ SENSOR\_CHAN\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:202

[SENSOR\_CHAN\_GYRO\_X](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac5709b77f0eb69972ccc055f927e5015)

@ SENSOR\_CHAN\_GYRO\_X

Angular velocity around the X axis, in radians/s.

**Definition** sensor.h:69

[SENSOR\_CHAN\_GAS\_RES](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934acf250a87d2d175f99179a5b54cb7ba01)

@ SENSOR\_CHAN\_GAS\_RES

Gas sensor resistance in ohms.

**Definition** sensor.h:124

[SENSOR\_CHAN\_HUMIDITY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ad08ddb6c9cd71c853a121f426fcea042)

@ SENSOR\_CHAN\_HUMIDITY

Humidity, in percent.

**Definition** sensor.h:96

[SENSOR\_CHAN\_DISTANCE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ad46d1495990a86fa7e2ab5bbe5338e08)

@ SENSOR\_CHAN\_DISTANCE

Distance.

**Definition** sensor.h:117

[SENSOR\_CHAN\_IR](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ad725fe5778f000a17f93f83dab31132c)

@ SENSOR\_CHAN\_IR

Illuminance in infra-red spectrum, in lux.

**Definition** sensor.h:100

[SENSOR\_CHAN\_MAX](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ad842035a01166417d90cd5d7630733b1)

@ SENSOR\_CHAN\_MAX

Maximum value describing a sensor channel type.

**Definition** sensor.h:207

[SENSOR\_CHAN\_POS\_DZ](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aeaf49aa075947a160f21ae19cf8c39b9)

@ SENSOR\_CHAN\_POS\_DZ

Position change on the Z axis, in points.

**Definition** sensor.h:148

[SENSOR\_CHAN\_RED](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934af22c8ef66f4871efe5a22863d7f434aa)

@ SENSOR\_CHAN\_RED

Illuminance in red spectrum, in lux.

**Definition** sensor.h:102

[SENSOR\_CHAN\_ALTITUDE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934af5ba63bfef1c64c8a96ae7fba4f35512)

@ SENSOR\_CHAN\_ALTITUDE

Altitude, in meters.

**Definition** sensor.h:108

[SENSOR\_CHAN\_GAUGE\_NOM\_AVAIL\_CAPACITY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934af9b0ac69fd87a68e7e8d97e52b41304a)

@ SENSOR\_CHAN\_GAUGE\_NOM\_AVAIL\_CAPACITY

Nominal Available Capacity in mAh.

**Definition** sensor.h:170

[SENSOR\_CHAN\_ACCEL\_X](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934afa9238082f000350530ca77b2f513d4c)

@ SENSOR\_CHAN\_ACCEL\_X

Acceleration on the X axis, in m/s^2.

**Definition** sensor.h:61

[SENSOR\_CHAN\_VOC](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934affee34c60c95398b67ec59644d647f8e)

@ SENSOR\_CHAN\_VOC

VOC level, in parts per billion (ppb).

**Definition** sensor.h:122

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:124

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:83

[ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5)

#define ENOMEM

Not enough core.

**Definition** errno.h:51

[ERANGE](group__system__errno.md#gaa1591a4f3a86360108de5b9ba34980ca)

#define ERANGE

Result too large.

**Definition** errno.h:73

[types.h](include_2zephyr_2dsp_2types_8h.md)

[types.h](include_2zephyr_2types_8h.md)

[INT64\_C](llvm_8h.md#a93d102802b35d3b8abae9bbe7f0fed75)

#define INT64\_C(x)

**Definition** llvm.h:86

[rtio.h](rtio_8h.md)

Real-Time IO device API for moving bytes with low effort.

[sensor\_data\_types.h](sensor__data__types_8h.md)

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[INT32\_MAX](stdint_8h.md#a181807730d4a375f848ba139813ce04f)

#define INT32\_MAX

**Definition** stdint.h:18

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[INT32\_MIN](stdint_8h.md#a688eb21a22db27c2b2bd5836943cdcbe)

#define INT32\_MIN

**Definition** stdint.h:24

[INT16\_MAX](stdint_8h.md#ac58f2c111cc9989c86db2a7dc4fd84ca)

#define INT16\_MAX

**Definition** stdint.h:17

[int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)

\_\_INT64\_TYPE\_\_ int64\_t

**Definition** stdint.h:75

[int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)

\_\_INT8\_TYPE\_\_ int8\_t

**Definition** stdint.h:72

[stdlib.h](stdlib_8h.md)

[memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)

void \* memcpy(void \*ZRESTRICT d, const void \*ZRESTRICT s, size\_t n)

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:393

[rtio\_iodev\_api](structrtio__iodev__api.md)

API that an RTIO IO device should implement.

**Definition** rtio.h:429

[rtio\_iodev\_sqe](structrtio__iodev__sqe.md)

Compute the mempool block index for a given pointer.

**Definition** rtio.h:419

[rtio\_iodev\_sqe::sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b)

struct rtio\_sqe sqe

**Definition** rtio.h:420

[rtio\_iodev](structrtio__iodev.md)

An IO device with a function table for submitting requests.

**Definition** rtio.h:444

[rtio\_iodev::data](structrtio__iodev.md#af0f3a27fe8dea2161c9a73cb838bdeec)

void \* data

**Definition** rtio.h:452

[rtio\_sqe](structrtio__sqe.md)

A submission queue event.

**Definition** rtio.h:230

[rtio\_sqe::userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971)

void \* userdata

User provided data which is returned upon operation completion.

**Definition** rtio.h:250

[rtio\_sqe::buf](structrtio__sqe.md#a55e98f27b26393fee8e179b7bdb6a52e)

uint8\_t \* buf

Buffer to use.

**Definition** rtio.h:257

[rtio\_sqe::buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722)

uint32\_t buf\_len

Length of buffer.

**Definition** rtio.h:256

[rtio\_sqe::iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc)

const struct rtio\_iodev \* iodev

Device to operation on.

**Definition** rtio.h:241

[rtio](structrtio.md)

An RTIO context containing what can be viewed as a pair of queues.

**Definition** rtio.h:323

[sensor\_data\_generic\_header](structsensor__data__generic__header.md)

**Definition** sensor.h:871

[sensor\_data\_generic\_header::channels](structsensor__data__generic__header.md#a14f5460f665c075d136eaa7b02c2e3c2)

enum sensor\_channel channels[0]

**Definition** sensor.h:888

[sensor\_data\_generic\_header::timestamp\_ns](structsensor__data__generic__header.md#a429e22b3191df271ccfe321b796e1ac9)

uint64\_t timestamp\_ns

**Definition** sensor.h:873

[sensor\_data\_generic\_header::shift](structsensor__data__generic__header.md#a68067521c1058b6802176e1d48fed788)

int8\_t shift

**Definition** sensor.h:882

[sensor\_data\_generic\_header::num\_channels](structsensor__data__generic__header.md#a7edbe674f28c95f3aa40b1df84ca61fe)

uint32\_t num\_channels

**Definition** sensor.h:879

[sensor\_decode\_context](structsensor__decode__context.md)

Used for iterating over the data frames via the sensor\_decoder\_api.

**Definition** sensor.h:514

[sensor\_decode\_context::decoder](structsensor__decode__context.md#a1ac0773e83a086455371d108264ef4f6)

const struct sensor\_decoder\_api \* decoder

**Definition** sensor.h:515

[sensor\_decode\_context::buffer](structsensor__decode__context.md#a23e27eb0687d722be78e1b89278613d1)

const uint8\_t \* buffer

**Definition** sensor.h:516

[sensor\_decode\_context::channel\_idx](structsensor__decode__context.md#a69e74a3651f7a9adaf17b5038c660d77)

size\_t channel\_idx

**Definition** sensor.h:518

[sensor\_decode\_context::channel](structsensor__decode__context.md#a7eab1624b1136e07240d1f9c4d66d123)

enum sensor\_channel channel

**Definition** sensor.h:517

[sensor\_decode\_context::fit](structsensor__decode__context.md#ada9e40625829093087886c41f2fb7350)

uint32\_t fit

**Definition** sensor.h:519

[sensor\_decoder\_api](structsensor__decoder__api.md)

Decodes a single raw data buffer.

**Definition** sensor.h:423

[sensor\_decoder\_api::get\_size\_info](structsensor__decoder__api.md#a67db53773d768b160fb74ab72affee14)

int(\* get\_size\_info)(enum sensor\_channel channel, size\_t \*base\_size, size\_t \*frame\_size)

Get the size required to decode a given channel.

**Definition** sensor.h:449

[sensor\_decoder\_api::decode](structsensor__decoder__api.md#a6c910d525374987ae68da10d75f9766e)

int(\* decode)(const uint8\_t \*buffer, enum sensor\_channel channel, size\_t channel\_idx, uint32\_t \*fit, uint16\_t max\_count, void \*data\_out)

Decode up to max\_count samples from the buffer.

**Definition** sensor.h:477

[sensor\_decoder\_api::has\_trigger](structsensor__decoder__api.md#a78706bae0f1314615b5804736ef43493)

bool(\* has\_trigger)(const uint8\_t \*buffer, enum sensor\_trigger\_type trigger)

Check if the given trigger type is present.

**Definition** sensor.h:487

[sensor\_decoder\_api::get\_frame\_count](structsensor__decoder__api.md#ac8344c7849c9a7084788192fb4f691fc)

int(\* get\_frame\_count)(const uint8\_t \*buffer, enum sensor\_channel channel, size\_t channel\_idx, uint16\_t \*frame\_count)

Get the number of frames in the current buffer.

**Definition** sensor.h:434

[sensor\_driver\_api](structsensor__driver__api.md)

**Definition** sensor.h:660

[sensor\_driver\_api::get\_decoder](structsensor__driver__api.md#a004f9d342805dc72249ab9b8c17a544b)

sensor\_get\_decoder\_t get\_decoder

**Definition** sensor.h:666

[sensor\_driver\_api::attr\_set](structsensor__driver__api.md#a2d230a976b19a699d132034f58bb2b6a)

sensor\_attr\_set\_t attr\_set

**Definition** sensor.h:661

[sensor\_driver\_api::attr\_get](structsensor__driver__api.md#a3e28950f844c3f8b8da5ba9ff8052e46)

sensor\_attr\_get\_t attr\_get

**Definition** sensor.h:662

[sensor\_driver\_api::trigger\_set](structsensor__driver__api.md#a4708070fd6654ecbbe631819aba319bd)

sensor\_trigger\_set\_t trigger\_set

**Definition** sensor.h:663

[sensor\_driver\_api::sample\_fetch](structsensor__driver__api.md#a4b40e25b81fe070e2f6bdcf7f8a4a31f)

sensor\_sample\_fetch\_t sample\_fetch

**Definition** sensor.h:664

[sensor\_driver\_api::channel\_get](structsensor__driver__api.md#a667b41bf51f2c7a6bb31713fbf889113)

sensor\_channel\_get\_t channel\_get

**Definition** sensor.h:665

[sensor\_driver\_api::submit](structsensor__driver__api.md#ae3ba0adeba21351e8f660896e5a0e702)

sensor\_submit\_t submit

**Definition** sensor.h:667

[sensor\_read\_config](structsensor__read__config.md)

**Definition** sensor.h:585

[sensor\_read\_config::count](structsensor__read__config.md#a5236049e0563ebba754994d70e22383a)

size\_t count

**Definition** sensor.h:592

[sensor\_read\_config::triggers](structsensor__read__config.md#a6eaa6df7bc9378abe0f5b4b8c9a05909)

struct sensor\_stream\_trigger \*const triggers

**Definition** sensor.h:590

[sensor\_read\_config::is\_streaming](structsensor__read__config.md#aca96de2c23fb63f887c4c40dcb272798)

const bool is\_streaming

**Definition** sensor.h:587

[sensor\_read\_config::sensor](structsensor__read__config.md#ad49d5ab5293017d1ad2cf60adc542090)

const struct device \* sensor

**Definition** sensor.h:586

[sensor\_read\_config::max](structsensor__read__config.md#aecb9c899e292fdb25c3c990bdaf1c76b)

const size\_t max

**Definition** sensor.h:593

[sensor\_read\_config::channels](structsensor__read__config.md#afd61f80d484e496cbdf1f48ceea3c657)

enum sensor\_channel \*const channels

**Definition** sensor.h:589

[sensor\_stream\_trigger](structsensor__stream__trigger.md)

**Definition** sensor.h:572

[sensor\_stream\_trigger::opt](structsensor__stream__trigger.md#a62ccdecf7253b1bfdff4f1d659563d76)

enum sensor\_stream\_data\_opt opt

**Definition** sensor.h:574

[sensor\_stream\_trigger::trigger](structsensor__stream__trigger.md#a9a367e746764e68140ec9120f2a016e6)

enum sensor\_trigger\_type trigger

**Definition** sensor.h:573

[sensor\_trigger](structsensor__trigger.md)

Sensor trigger spec.

**Definition** sensor.h:280

[sensor\_trigger::type](structsensor__trigger.md#ac2cce1ec6ff82f95cb06d0dccafd7af0)

enum sensor\_trigger\_type type

Trigger type.

**Definition** sensor.h:282

[sensor\_trigger::chan](structsensor__trigger.md#ae01f99b124aa99c59b9967818022e112)

enum sensor\_channel chan

Channel the trigger is set on.

**Definition** sensor.h:284

[sensor\_value](structsensor__value.md)

Representation of a sensor readout value.

**Definition** sensor.h:49

[sensor\_value::val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b)

int32\_t val2

Fractional part of the value (in one-millionth parts).

**Definition** sensor.h:53

[sensor\_value::val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe)

int32\_t val1

Integer part of the value.

**Definition** sensor.h:51

[iterable\_sections.h](sys_2iterable__sections_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor.h](sensor_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
