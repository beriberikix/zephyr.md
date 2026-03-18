---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/sensor_8h_source.html
original_path: doxygen/html/sensor_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
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

23

24#include <[errno.h](errno_8h.md)>

25#include <[stdlib.h](stdlib_8h.md)>

26

27#include <[zephyr/device.h](device_8h.md)>

28#include <[zephyr/drivers/sensor\_data\_types.h](sensor__data__types_8h.md)>

29#include <[zephyr/dsp/types.h](include_2zephyr_2dsp_2types_8h.md)>

30#include <[zephyr/rtio/rtio.h](rtio_2rtio_8h.md)>

31#include <[zephyr/sys/iterable\_sections.h](sys_2iterable__sections_8h.md)>

32#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

33

34#ifdef \_\_cplusplus

35extern "C" {

36#endif

37

[ 51](structsensor__value.md)struct [sensor\_value](structsensor__value.md) {

[ 53](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe);

[ 55](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b) [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b);

56};

57

[ 61](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934)enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) {

[ 63](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934afa9238082f000350530ca77b2f513d4c) [SENSOR\_CHAN\_ACCEL\_X](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934afa9238082f000350530ca77b2f513d4c),

[ 65](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a61c145468f01916c1a547fb38a1be9a8) [SENSOR\_CHAN\_ACCEL\_Y](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a61c145468f01916c1a547fb38a1be9a8),

[ 67](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a78e06bb48cfe06e42829816ad4cb5a0f) [SENSOR\_CHAN\_ACCEL\_Z](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a78e06bb48cfe06e42829816ad4cb5a0f),

[ 69](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a16c05784ae15a4952ea708c2f11a2ae9) [SENSOR\_CHAN\_ACCEL\_XYZ](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a16c05784ae15a4952ea708c2f11a2ae9),

[ 71](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac5709b77f0eb69972ccc055f927e5015) [SENSOR\_CHAN\_GYRO\_X](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac5709b77f0eb69972ccc055f927e5015),

[ 73](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a4a9533172105fd2e55d96e0122a48847) [SENSOR\_CHAN\_GYRO\_Y](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a4a9533172105fd2e55d96e0122a48847),

[ 75](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a9b6b9d13cd8d82449823d65779a87a39) [SENSOR\_CHAN\_GYRO\_Z](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a9b6b9d13cd8d82449823d65779a87a39),

[ 77](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a1d36b89ab3761e9bc86effc839f8db0e) [SENSOR\_CHAN\_GYRO\_XYZ](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a1d36b89ab3761e9bc86effc839f8db0e),

[ 79](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a171f37ba152d34f75ff745cb848b3240) [SENSOR\_CHAN\_MAGN\_X](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a171f37ba152d34f75ff745cb848b3240),

[ 81](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a2b4f1764f47428c528447347d7730942) [SENSOR\_CHAN\_MAGN\_Y](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a2b4f1764f47428c528447347d7730942),

[ 83](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a2a2115051ded019a57ece5a00f86ea61) [SENSOR\_CHAN\_MAGN\_Z](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a2a2115051ded019a57ece5a00f86ea61),

[ 85](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a5d1f48466f6f600503af18427fa3da32) [SENSOR\_CHAN\_MAGN\_XYZ](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a5d1f48466f6f600503af18427fa3da32),

[ 87](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a0a8828f51fe15335ad857d136f197ee1) [SENSOR\_CHAN\_DIE\_TEMP](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a0a8828f51fe15335ad857d136f197ee1),

[ 89](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a5bf9c4a677405c4a4df3bc3acd116c7c) [SENSOR\_CHAN\_AMBIENT\_TEMP](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a5bf9c4a677405c4a4df3bc3acd116c7c),

[ 91](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a14cd68844542e23d1b641a2bc54132a9) [SENSOR\_CHAN\_PRESS](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a14cd68844542e23d1b641a2bc54132a9),

[ 96](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934abaec2c1347ef0035221dd4d9c34a4774) [SENSOR\_CHAN\_PROX](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934abaec2c1347ef0035221dd4d9c34a4774),

[ 98](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ad08ddb6c9cd71c853a121f426fcea042) [SENSOR\_CHAN\_HUMIDITY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ad08ddb6c9cd71c853a121f426fcea042),

[ 100](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a6e91196c11d080c3f5df55fda190e19d) [SENSOR\_CHAN\_LIGHT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a6e91196c11d080c3f5df55fda190e19d),

[ 102](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ad725fe5778f000a17f93f83dab31132c) [SENSOR\_CHAN\_IR](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ad725fe5778f000a17f93f83dab31132c),

[ 104](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934af22c8ef66f4871efe5a22863d7f434aa) [SENSOR\_CHAN\_RED](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934af22c8ef66f4871efe5a22863d7f434aa),

[ 106](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a216a3b2b77d7a92f94547aeb889ae378) [SENSOR\_CHAN\_GREEN](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a216a3b2b77d7a92f94547aeb889ae378),

[ 108](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a6e66f95d73d05c2b3511e2db506844f5) [SENSOR\_CHAN\_BLUE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a6e66f95d73d05c2b3511e2db506844f5),

[ 110](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934af5ba63bfef1c64c8a96ae7fba4f35512) [SENSOR\_CHAN\_ALTITUDE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934af5ba63bfef1c64c8a96ae7fba4f35512),

111

[ 113](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a08f0c21c33008292b0b58defe5c06815) [SENSOR\_CHAN\_PM\_1\_0](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a08f0c21c33008292b0b58defe5c06815),

[ 115](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a3398fdc51964aa06c9a01096d2fac945) [SENSOR\_CHAN\_PM\_2\_5](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a3398fdc51964aa06c9a01096d2fac945),

[ 117](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aa450541bde278aefcc9b53bd0826e225) [SENSOR\_CHAN\_PM\_10](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aa450541bde278aefcc9b53bd0826e225),

[ 119](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ad46d1495990a86fa7e2ab5bbe5338e08) [SENSOR\_CHAN\_DISTANCE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ad46d1495990a86fa7e2ab5bbe5338e08),

120

[ 122](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a7a23e3e869c5e9a39f6a7bfa28737133) [SENSOR\_CHAN\_CO2](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a7a23e3e869c5e9a39f6a7bfa28737133),

[ 124](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a17bcfa0e34eecf45e17988720471c8f9) [SENSOR\_CHAN\_O2](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a17bcfa0e34eecf45e17988720471c8f9),

[ 126](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934affee34c60c95398b67ec59644d647f8e) [SENSOR\_CHAN\_VOC](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934affee34c60c95398b67ec59644d647f8e),

[ 128](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934acf250a87d2d175f99179a5b54cb7ba01) [SENSOR\_CHAN\_GAS\_RES](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934acf250a87d2d175f99179a5b54cb7ba01),

129

[ 131](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a69dd8a737a0cb6f03fa5f60c92840e6d) [SENSOR\_CHAN\_VOLTAGE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a69dd8a737a0cb6f03fa5f60c92840e6d),

132

[ 134](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a1ea01c780995ad4539e9ffc2ca6102e9) [SENSOR\_CHAN\_VSHUNT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a1ea01c780995ad4539e9ffc2ca6102e9),

135

[ 137](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a1a001ba3ca5ad37308fb7be81f11c950) [SENSOR\_CHAN\_CURRENT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a1a001ba3ca5ad37308fb7be81f11c950),

[ 139](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a33607371060fca93c3555e8e10d5b177) [SENSOR\_CHAN\_POWER](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a33607371060fca93c3555e8e10d5b177),

140

[ 142](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a34ba555026ff976881142512cc8a616b) [SENSOR\_CHAN\_RESISTANCE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a34ba555026ff976881142512cc8a616b),

143

[ 145](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a551ffe08a9b1206e3c051f207b92aabf) [SENSOR\_CHAN\_ROTATION](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a551ffe08a9b1206e3c051f207b92aabf),

146

[ 148](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aa00b7a857e33c925c910661a91389517) [SENSOR\_CHAN\_POS\_DX](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aa00b7a857e33c925c910661a91389517),

[ 150](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a974327ca88ea6d22731cd03afeacef76) [SENSOR\_CHAN\_POS\_DY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a974327ca88ea6d22731cd03afeacef76),

[ 152](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aeaf49aa075947a160f21ae19cf8c39b9) [SENSOR\_CHAN\_POS\_DZ](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aeaf49aa075947a160f21ae19cf8c39b9),

[ 154](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a81fe5eca365c048c5a112071b7aca740) [SENSOR\_CHAN\_POS\_DXYZ](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a81fe5eca365c048c5a112071b7aca740),

155

[ 157](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a655a576a72cbd6641abc698a3f4304d1) [SENSOR\_CHAN\_RPM](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a655a576a72cbd6641abc698a3f4304d1),

158

[ 160](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ab942649ce1507fb081a77b4bcfc1a57d) [SENSOR\_CHAN\_GAUGE\_VOLTAGE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ab942649ce1507fb081a77b4bcfc1a57d),

[ 162](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a4272c1256cde47006d424c5523d26bf8) [SENSOR\_CHAN\_GAUGE\_AVG\_CURRENT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a4272c1256cde47006d424c5523d26bf8),

[ 164](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a5e6b87cacfe3e4703b963a2177d35cc8) [SENSOR\_CHAN\_GAUGE\_STDBY\_CURRENT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a5e6b87cacfe3e4703b963a2177d35cc8),

[ 166](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a603335f6a91846c5089a2a541d9053cf) [SENSOR\_CHAN\_GAUGE\_MAX\_LOAD\_CURRENT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a603335f6a91846c5089a2a541d9053cf),

[ 168](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a8cac65c812b3a1fcb55a53f18d827214) [SENSOR\_CHAN\_GAUGE\_TEMP](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a8cac65c812b3a1fcb55a53f18d827214),

[ 170](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a7d67d6842ee787fcc8a4d9ee2cbea139) [SENSOR\_CHAN\_GAUGE\_STATE\_OF\_CHARGE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a7d67d6842ee787fcc8a4d9ee2cbea139),

[ 172](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a54a6be68e09b9f8ca4d349e3d1445649) [SENSOR\_CHAN\_GAUGE\_FULL\_CHARGE\_CAPACITY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a54a6be68e09b9f8ca4d349e3d1445649),

[ 174](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aaaea6433c82f7b563f86fa53c95ad0ad) [SENSOR\_CHAN\_GAUGE\_REMAINING\_CHARGE\_CAPACITY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aaaea6433c82f7b563f86fa53c95ad0ad),

[ 176](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934af9b0ac69fd87a68e7e8d97e52b41304a) [SENSOR\_CHAN\_GAUGE\_NOM\_AVAIL\_CAPACITY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934af9b0ac69fd87a68e7e8d97e52b41304a),

[ 178](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a688287fa1587944424a2eda13b8d98e8) [SENSOR\_CHAN\_GAUGE\_FULL\_AVAIL\_CAPACITY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a688287fa1587944424a2eda13b8d98e8),

[ 180](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aa24f9e12f20a716dd152cf889cb51228) [SENSOR\_CHAN\_GAUGE\_AVG\_POWER](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aa24f9e12f20a716dd152cf889cb51228),

[ 182](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a0613c39397f06d11f4350f8cbcc24cf6) [SENSOR\_CHAN\_GAUGE\_STATE\_OF\_HEALTH](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a0613c39397f06d11f4350f8cbcc24cf6),

[ 184](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aa3755e9fcd8c90fef5185082edb29b65) [SENSOR\_CHAN\_GAUGE\_TIME\_TO\_EMPTY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aa3755e9fcd8c90fef5185082edb29b65),

[ 186](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a14d4c802805e1e07c9b4e47ccaff0eeb) [SENSOR\_CHAN\_GAUGE\_TIME\_TO\_FULL](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a14d4c802805e1e07c9b4e47ccaff0eeb),

[ 188](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a8834978858c2b62b5e923d06cfcb1a46) [SENSOR\_CHAN\_GAUGE\_CYCLE\_COUNT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a8834978858c2b62b5e923d06cfcb1a46),

[ 190](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a6f96ba4db6cf812b223f9a09f2a287d0) [SENSOR\_CHAN\_GAUGE\_DESIGN\_VOLTAGE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a6f96ba4db6cf812b223f9a09f2a287d0),

[ 192](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a2c33a7f11d5b3996e95167698a2056cf) [SENSOR\_CHAN\_GAUGE\_DESIRED\_VOLTAGE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a2c33a7f11d5b3996e95167698a2056cf),

[ 194](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a4aa8bba1b260e1994542383d8e2e908f) [SENSOR\_CHAN\_GAUGE\_DESIRED\_CHARGING\_CURRENT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a4aa8bba1b260e1994542383d8e2e908f),

195

[ 197](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ab275027eb550b2b075c44917634eca2c) [SENSOR\_CHAN\_ALL](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ab275027eb550b2b075c44917634eca2c),

198

[ 202](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934abb2893ccb71c9e1eeb155d7cbd539303) [SENSOR\_CHAN\_COMMON\_COUNT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934abb2893ccb71c9e1eeb155d7cbd539303),

203

[ 208](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12) [SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12) = [SENSOR\_CHAN\_COMMON\_COUNT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934abb2893ccb71c9e1eeb155d7cbd539303),

209

[ 213](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ad842035a01166417d90cd5d7630733b1) [SENSOR\_CHAN\_MAX](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ad842035a01166417d90cd5d7630733b1) = [INT16\_MAX](stdint_8h.md#ac58f2c111cc9989c86db2a7dc4fd84ca),

214};

215

[ 219](group__sensor__interface.md#ga08215279400e8c9eb05ce4e4f0898ffd)enum [sensor\_trigger\_type](group__sensor__interface.md#ga08215279400e8c9eb05ce4e4f0898ffd) {

[ 224](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdabf92b196394726ec90f1d61586a7f023) [SENSOR\_TRIG\_TIMER](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdabf92b196394726ec90f1d61586a7f023),

[ 226](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdaf7c161e309c267a7dd6daf2ad176f44f) [SENSOR\_TRIG\_DATA\_READY](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdaf7c161e309c267a7dd6daf2ad176f44f),

[ 235](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda3bb90a3334bcf613c9efbdf2ed05f855) [SENSOR\_TRIG\_DELTA](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda3bb90a3334bcf613c9efbdf2ed05f855),

[ 237](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda448226d83b28c2862c353a8cda7be0d5) [SENSOR\_TRIG\_NEAR\_FAR](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda448226d83b28c2862c353a8cda7be0d5),

[ 244](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda8f875f881b6540eebc28e3d6a7d46606) [SENSOR\_TRIG\_THRESHOLD](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda8f875f881b6540eebc28e3d6a7d46606),

245

[ 247](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdae49a25e6400f0753f6bac8a7d136200d) [SENSOR\_TRIG\_TAP](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdae49a25e6400f0753f6bac8a7d136200d),

248

[ 250](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdab95e52584a6bc3343181f495cd4cb2ef) [SENSOR\_TRIG\_DOUBLE\_TAP](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdab95e52584a6bc3343181f495cd4cb2ef),

251

[ 253](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda4943ffb4afaf4cbae39e85693bd4374c) [SENSOR\_TRIG\_FREEFALL](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda4943ffb4afaf4cbae39e85693bd4374c),

254

[ 256](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda7095387831b763b34171287945dae276) [SENSOR\_TRIG\_MOTION](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda7095387831b763b34171287945dae276),

257

[ 259](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda79e286ffced716e1076f56464ea47f5d) [SENSOR\_TRIG\_STATIONARY](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda79e286ffced716e1076f56464ea47f5d),

260

[ 262](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdac5d67fb4fb6206465b1b01dc78245fe4) [SENSOR\_TRIG\_FIFO\_WATERMARK](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdac5d67fb4fb6206465b1b01dc78245fe4),

263

[ 265](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda66f913f8751a77a6c16745e329c7315c) [SENSOR\_TRIG\_FIFO\_FULL](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda66f913f8751a77a6c16745e329c7315c),

[ 269](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda8d1f2621fad4fd685d56cca3f9b042f5) [SENSOR\_TRIG\_COMMON\_COUNT](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda8d1f2621fad4fd685d56cca3f9b042f5),

270

[ 275](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda5e1a94f21fee67ee98296153ea640921) [SENSOR\_TRIG\_PRIV\_START](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda5e1a94f21fee67ee98296153ea640921) = [SENSOR\_TRIG\_COMMON\_COUNT](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda8d1f2621fad4fd685d56cca3f9b042f5),

276

[ 280](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda9de566f44de519f94c59c58df1efc4c4) [SENSOR\_TRIG\_MAX](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda9de566f44de519f94c59c58df1efc4c4) = [INT16\_MAX](stdint_8h.md#ac58f2c111cc9989c86db2a7dc4fd84ca),

281};

282

[ 286](structsensor__trigger.md)struct [sensor\_trigger](structsensor__trigger.md) {

[ 288](structsensor__trigger.md#ac2cce1ec6ff82f95cb06d0dccafd7af0) enum [sensor\_trigger\_type](group__sensor__interface.md#ga08215279400e8c9eb05ce4e4f0898ffd) [type](structsensor__trigger.md#ac2cce1ec6ff82f95cb06d0dccafd7af0);

[ 290](structsensor__trigger.md#ae01f99b124aa99c59b9967818022e112) enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) [chan](structsensor__trigger.md#ae01f99b124aa99c59b9967818022e112);

291};

292

[ 296](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b)enum [sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b) {

[ 301](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bacb07e3508ea5503dbcdceee3f17d2291) [SENSOR\_ATTR\_SAMPLING\_FREQUENCY](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bacb07e3508ea5503dbcdceee3f17d2291),

[ 303](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940baee644485ab5f64e7c5273bbe562deaaa) [SENSOR\_ATTR\_LOWER\_THRESH](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940baee644485ab5f64e7c5273bbe562deaaa),

[ 305](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba5af51bd0640a87a94476eee112a4460b) [SENSOR\_ATTR\_UPPER\_THRESH](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba5af51bd0640a87a94476eee112a4460b),

[ 307](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bac4538665a244cb7f18fc053c40134302) [SENSOR\_ATTR\_SLOPE\_TH](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bac4538665a244cb7f18fc053c40134302),

[ 312](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940baf510b32b2e2395bbcf1c8fd7159ed2a1) [SENSOR\_ATTR\_SLOPE\_DUR](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940baf510b32b2e2395bbcf1c8fd7159ed2a1),

313 /\* Hysteresis for trigger thresholds. \*/

[ 314](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba044e67bfc04e8ddc2de7d2058fffbc94) [SENSOR\_ATTR\_HYSTERESIS](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba044e67bfc04e8ddc2de7d2058fffbc94),

[ 316](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba3d32987f75284d80d3f64bf44f5c6ccd) [SENSOR\_ATTR\_OVERSAMPLING](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba3d32987f75284d80d3f64bf44f5c6ccd),

[ 318](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bad30df3100fb6b285a6a786fdc77234d3) [SENSOR\_ATTR\_FULL\_SCALE](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bad30df3100fb6b285a6a786fdc77234d3),

[ 323](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba332935dcb6f7e228cb9c595a545079fd) [SENSOR\_ATTR\_OFFSET](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba332935dcb6f7e228cb9c595a545079fd),

[ 328](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba3043381b539610a8b424f12d76474bdf) [SENSOR\_ATTR\_CALIB\_TARGET](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba3043381b539610a8b424f12d76474bdf),

[ 330](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba75cd3aca26859fd7c10c83d86e3471e9) [SENSOR\_ATTR\_CONFIGURATION](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba75cd3aca26859fd7c10c83d86e3471e9),

[ 332](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba843d1e79573c634987e5e839ba9e965e) [SENSOR\_ATTR\_CALIBRATION](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba843d1e79573c634987e5e839ba9e965e),

[ 334](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba1f8d2242fa9d63a13c6a48fe3a1cbe52) [SENSOR\_ATTR\_FEATURE\_MASK](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba1f8d2242fa9d63a13c6a48fe3a1cbe52),

[ 336](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940baaedf76e63224adc3fa266d35666e0a3a) [SENSOR\_ATTR\_ALERT](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940baaedf76e63224adc3fa266d35666e0a3a),

[ 342](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba5a62ea6aa7e55efd62ab3f93dcb0593a) [SENSOR\_ATTR\_FF\_DUR](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba5a62ea6aa7e55efd62ab3f93dcb0593a),

343

[ 345](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba3b0cf69c77de55c92129e212bf5b8ced) [SENSOR\_ATTR\_BATCH\_DURATION](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba3b0cf69c77de55c92129e212bf5b8ced),

346

[ 350](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba99ceedef81217614ada0c8a469f91eb8) [SENSOR\_ATTR\_COMMON\_COUNT](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba99ceedef81217614ada0c8a469f91eb8),

351

[ 356](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3) [SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3) = [SENSOR\_ATTR\_COMMON\_COUNT](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba99ceedef81217614ada0c8a469f91eb8),

357

[ 361](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940baf6bd0b33ca2117ef329692c291f6384b) [SENSOR\_ATTR\_MAX](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940baf6bd0b33ca2117ef329692c291f6384b) = [INT16\_MAX](stdint_8h.md#ac58f2c111cc9989c86db2a7dc4fd84ca),

362};

363

[ 371](group__sensor__interface.md#ga890c1fb6d6974aea22a2d08829a75902)typedef void (\*[sensor\_trigger\_handler\_t](group__sensor__interface.md#ga890c1fb6d6974aea22a2d08829a75902))(const struct [device](structdevice.md) \*dev,

372 const struct [sensor\_trigger](structsensor__trigger.md) \*trigger);

373

[ 380](group__sensor__interface.md#ga38422ace4194a66a9a912a8ef1e088fb)typedef int (\*[sensor\_attr\_set\_t](group__sensor__interface.md#ga38422ace4194a66a9a912a8ef1e088fb))(const struct [device](structdevice.md) \*dev,

381 enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) chan,

382 enum [sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b) attr,

383 const struct [sensor\_value](structsensor__value.md) \*val);

384

[ 391](group__sensor__interface.md#ga00d05c82b46e56dca5f6e8f7f01c31b8)typedef int (\*[sensor\_attr\_get\_t](group__sensor__interface.md#ga00d05c82b46e56dca5f6e8f7f01c31b8))(const struct [device](structdevice.md) \*dev,

392 enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) chan,

393 enum [sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b) attr,

394 struct [sensor\_value](structsensor__value.md) \*val);

395

[ 402](group__sensor__interface.md#gad7f7a3d9e714cc16f23656ca06592aa4)typedef int (\*[sensor\_trigger\_set\_t](group__sensor__interface.md#gad7f7a3d9e714cc16f23656ca06592aa4))(const struct [device](structdevice.md) \*dev,

403 const struct [sensor\_trigger](structsensor__trigger.md) \*trig,

404 [sensor\_trigger\_handler\_t](group__sensor__interface.md#ga890c1fb6d6974aea22a2d08829a75902) handler);

[ 411](group__sensor__interface.md#gacae110a4edb6f29dfb457cb1ea8d68c1)typedef int (\*[sensor\_sample\_fetch\_t](group__sensor__interface.md#gacae110a4edb6f29dfb457cb1ea8d68c1))(const struct [device](structdevice.md) \*dev,

412 enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) chan);

[ 419](group__sensor__interface.md#ga5c9b5ed9097464562004b446856043fd)typedef int (\*[sensor\_channel\_get\_t](group__sensor__interface.md#ga5c9b5ed9097464562004b446856043fd))(const struct [device](structdevice.md) \*dev,

420 enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) chan,

421 struct [sensor\_value](structsensor__value.md) \*val);

422

[ 431](structsensor__chan__spec.md)struct [sensor\_chan\_spec](structsensor__chan__spec.md) {

[ 432](structsensor__chan__spec.md#a1b2f0ecdc23e0d235536eb5fcdeeb63c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [chan\_type](structsensor__chan__spec.md#a1b2f0ecdc23e0d235536eb5fcdeeb63c);

[ 433](structsensor__chan__spec.md#a00d4a927cfeae33b2beea8cdc415dda1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [chan\_idx](structsensor__chan__spec.md#a00d4a927cfeae33b2beea8cdc415dda1);

434};

435

437/\* Ensure sensor\_chan\_spec is sensibly sized to pass by value \*/

438BUILD\_ASSERT(sizeof(struct [sensor\_chan\_spec](structsensor__chan__spec.md)) <= sizeof([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)),

439 "sensor\_chan\_spec size should be equal or less than the size of a machine word");

441

[ 450](group__sensor__interface.md#gae95715ffea5da18a9593ec2add029824)static inline bool [sensor\_chan\_spec\_eq](group__sensor__interface.md#gae95715ffea5da18a9593ec2add029824)(struct [sensor\_chan\_spec](structsensor__chan__spec.md) chan\_spec0,

451 struct [sensor\_chan\_spec](structsensor__chan__spec.md) chan\_spec1)

452{

453 return chan\_spec0.[chan\_type](structsensor__chan__spec.md#a1b2f0ecdc23e0d235536eb5fcdeeb63c) == chan\_spec1.[chan\_type](structsensor__chan__spec.md#a1b2f0ecdc23e0d235536eb5fcdeeb63c) &&

454 chan\_spec0.[chan\_idx](structsensor__chan__spec.md#a00d4a927cfeae33b2beea8cdc415dda1) == chan\_spec1.[chan\_idx](structsensor__chan__spec.md#a00d4a927cfeae33b2beea8cdc415dda1);

455}

456

[ 463](structsensor__decoder__api.md)struct [sensor\_decoder\_api](structsensor__decoder__api.md) {

[ 473](structsensor__decoder__api.md#a16c0b0f1a3a13d037b9ffcbf348da1f5) int (\*[get\_frame\_count](structsensor__decoder__api.md#a16c0b0f1a3a13d037b9ffcbf348da1f5))(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, struct [sensor\_chan\_spec](structsensor__chan__spec.md) channel,

474 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*frame\_count);

475

[ 488](structsensor__decoder__api.md#a026be8086386e9eea0a1cb25c1cd602e) int (\*[get\_size\_info](structsensor__decoder__api.md#a026be8086386e9eea0a1cb25c1cd602e))(struct [sensor\_chan\_spec](structsensor__chan__spec.md) channel, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*base\_size,

489 size\_t \*frame\_size);

490

[ 516](structsensor__decoder__api.md#a1d24e69b5c2f0c41ce175de2aa2618db) int (\*[decode](structsensor__decoder__api.md#a1d24e69b5c2f0c41ce175de2aa2618db))(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, struct [sensor\_chan\_spec](structsensor__chan__spec.md) channel, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*fit,

517 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) max\_count, void \*data\_out);

518

[ 526](structsensor__decoder__api.md#a78706bae0f1314615b5804736ef43493) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[has\_trigger](structsensor__decoder__api.md#a78706bae0f1314615b5804736ef43493))(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, enum [sensor\_trigger\_type](group__sensor__interface.md#ga08215279400e8c9eb05ce4e4f0898ffd) trigger);

527};

528

[ 553](structsensor__decode__context.md)struct [sensor\_decode\_context](structsensor__decode__context.md) {

[ 554](structsensor__decode__context.md#a1ac0773e83a086455371d108264ef4f6) const struct [sensor\_decoder\_api](structsensor__decoder__api.md) \*[decoder](structsensor__decode__context.md#a1ac0773e83a086455371d108264ef4f6);

[ 555](structsensor__decode__context.md#a23e27eb0687d722be78e1b89278613d1) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buffer](structsensor__decode__context.md#a23e27eb0687d722be78e1b89278613d1);

[ 556](structsensor__decode__context.md#a1c051bd8d0030f81cc561e32b2897d74) struct [sensor\_chan\_spec](structsensor__chan__spec.md) [channel](structsensor__decode__context.md#a1c051bd8d0030f81cc561e32b2897d74);

[ 557](structsensor__decode__context.md#ada9e40625829093087886c41f2fb7350) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [fit](structsensor__decode__context.md#ada9e40625829093087886c41f2fb7350);

558};

559

[ 563](group__sensor__interface.md#gae69ec503df53d2d5ee417e481f9ac9ea)#define SENSOR\_DECODE\_CONTEXT\_INIT(decoder\_, buffer\_, channel\_type\_, channel\_index\_) \

564 { \

565 .decoder = (decoder\_), \

566 .buffer = (buffer\_), \

567 .channel = {.chan\_type = (channel\_type\_), .chan\_idx = (channel\_index\_)}, \

568 .fit = 0, \

569 }

570

[ 579](group__sensor__interface.md#ga018bca56056ae2558f9e45aeb2fa5f53)static inline int [sensor\_decode](group__sensor__interface.md#ga018bca56056ae2558f9e45aeb2fa5f53)(struct [sensor\_decode\_context](structsensor__decode__context.md) \*ctx, void \*out, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) max\_count)

580{

581 return ctx->[decoder](structsensor__decode__context.md#a1ac0773e83a086455371d108264ef4f6)->[decode](structsensor__decoder__api.md#a1d24e69b5c2f0c41ce175de2aa2618db)(ctx->[buffer](structsensor__decode__context.md#a23e27eb0687d722be78e1b89278613d1), ctx->[channel](structsensor__decode__context.md#a1c051bd8d0030f81cc561e32b2897d74), &ctx->[fit](structsensor__decode__context.md#ada9e40625829093087886c41f2fb7350), max\_count, out);

582}

583

[ 584](group__sensor__interface.md#ga2b045cdbd4d1ca37beed69970093945b)int [sensor\_natively\_supported\_channel\_size\_info](group__sensor__interface.md#ga2b045cdbd4d1ca37beed69970093945b)(struct [sensor\_chan\_spec](structsensor__chan__spec.md) channel, size\_t \*base\_size,

585 size\_t \*frame\_size);

586

[ 593](group__sensor__interface.md#ga21e407d552d140cfb6bfd0d9513c7d42)typedef int (\*[sensor\_get\_decoder\_t](group__sensor__interface.md#ga21e407d552d140cfb6bfd0d9513c7d42))(const struct [device](structdevice.md) \*dev,

594 const struct [sensor\_decoder\_api](structsensor__decoder__api.md) \*\*api);

595

[ 599](group__sensor__interface.md#ga8613a20521a37d40fd7371dc63ba2dac)enum [sensor\_stream\_data\_opt](group__sensor__interface.md#ga8613a20521a37d40fd7371dc63ba2dac) {

[ 601](group__sensor__interface.md#gga8613a20521a37d40fd7371dc63ba2daca2ba3554a08bf55b64da40900592be315) [SENSOR\_STREAM\_DATA\_INCLUDE](group__sensor__interface.md#gga8613a20521a37d40fd7371dc63ba2daca2ba3554a08bf55b64da40900592be315) = 0,

[ 603](group__sensor__interface.md#gga8613a20521a37d40fd7371dc63ba2daca7e897c6d1428ff50f98140ed4cd4d35d) [SENSOR\_STREAM\_DATA\_NOP](group__sensor__interface.md#gga8613a20521a37d40fd7371dc63ba2daca7e897c6d1428ff50f98140ed4cd4d35d) = 1,

[ 605](group__sensor__interface.md#gga8613a20521a37d40fd7371dc63ba2dacaa13c6d3bae87c16f9cd89e0fe7144f8e) [SENSOR\_STREAM\_DATA\_DROP](group__sensor__interface.md#gga8613a20521a37d40fd7371dc63ba2dacaa13c6d3bae87c16f9cd89e0fe7144f8e) = 2,

606};

607

[ 608](structsensor__stream__trigger.md)struct [sensor\_stream\_trigger](structsensor__stream__trigger.md) {

[ 609](structsensor__stream__trigger.md#a9a367e746764e68140ec9120f2a016e6) enum [sensor\_trigger\_type](group__sensor__interface.md#ga08215279400e8c9eb05ce4e4f0898ffd) [trigger](structsensor__stream__trigger.md#a9a367e746764e68140ec9120f2a016e6);

[ 610](structsensor__stream__trigger.md#a62ccdecf7253b1bfdff4f1d659563d76) enum [sensor\_stream\_data\_opt](group__sensor__interface.md#ga8613a20521a37d40fd7371dc63ba2dac) [opt](structsensor__stream__trigger.md#a62ccdecf7253b1bfdff4f1d659563d76);

611};

612

[ 613](group__sensor__interface.md#ga9b7b0db322121d220b126d2b5bb7eb73)#define SENSOR\_STREAM\_TRIGGER\_PREP(\_trigger, \_opt) \

614 { \

615 .trigger = (\_trigger), .opt = (\_opt), \

616 }

617

618/\*

619 \* Internal data structure used to store information about the IODevice for async reading and

620 \* streaming sensor data.

621 \*/

[ 622](structsensor__read__config.md)struct [sensor\_read\_config](structsensor__read__config.md) {

[ 623](structsensor__read__config.md#ad49d5ab5293017d1ad2cf60adc542090) const struct [device](structdevice.md) \*[sensor](structsensor__read__config.md#ad49d5ab5293017d1ad2cf60adc542090);

[ 624](structsensor__read__config.md#aca96de2c23fb63f887c4c40dcb272798) const bool [is\_streaming](structsensor__read__config.md#aca96de2c23fb63f887c4c40dcb272798);

625 union {

[ 626](structsensor__read__config.md#a2aff44f02b25fd4ad1d4bc217800fad1) struct [sensor\_chan\_spec](structsensor__chan__spec.md) \*const [channels](structsensor__read__config.md#a2aff44f02b25fd4ad1d4bc217800fad1);

[ 627](structsensor__read__config.md#a6eaa6df7bc9378abe0f5b4b8c9a05909) struct [sensor\_stream\_trigger](structsensor__stream__trigger.md) \*const [triggers](structsensor__read__config.md#a6eaa6df7bc9378abe0f5b4b8c9a05909);

628 };

[ 629](structsensor__read__config.md#a5236049e0563ebba754994d70e22383a) size\_t [count](structsensor__read__config.md#a5236049e0563ebba754994d70e22383a);

[ 630](structsensor__read__config.md#aecb9c899e292fdb25c3c990bdaf1c76b) const size\_t [max](structsensor__read__config.md#aecb9c899e292fdb25c3c990bdaf1c76b);

631};

632

[ 648](group__sensor__interface.md#ga0cc1ee28114557e9e00257071c7dfa9f)#define SENSOR\_DT\_READ\_IODEV(name, dt\_node, ...) \

649 static struct sensor\_chan\_spec \_CONCAT(\_\_channel\_array\_, name)[] = {\_\_VA\_ARGS\_\_}; \

650 static struct sensor\_read\_config \_CONCAT(\_\_sensor\_read\_config\_, name) = { \

651 .sensor = DEVICE\_DT\_GET(dt\_node), \

652 .is\_streaming = false, \

653 .channels = \_CONCAT(\_\_channel\_array\_, name), \

654 .count = ARRAY\_SIZE(\_CONCAT(\_\_channel\_array\_, name)), \

655 .max = ARRAY\_SIZE(\_CONCAT(\_\_channel\_array\_, name)), \

656 }; \

657 RTIO\_IODEV\_DEFINE(name, &\_\_sensor\_iodev\_api, \_CONCAT(&\_\_sensor\_read\_config\_, name))

658

[ 678](group__sensor__interface.md#ga35211c4d908a26f98b1f8d925a9b1374)#define SENSOR\_DT\_STREAM\_IODEV(name, dt\_node, ...) \

679 static struct sensor\_stream\_trigger \_CONCAT(\_\_trigger\_array\_, name)[] = {\_\_VA\_ARGS\_\_}; \

680 static struct sensor\_read\_config \_CONCAT(\_\_sensor\_read\_config\_, name) = { \

681 .sensor = DEVICE\_DT\_GET(dt\_node), \

682 .is\_streaming = true, \

683 .triggers = \_CONCAT(\_\_trigger\_array\_, name), \

684 .count = ARRAY\_SIZE(\_CONCAT(\_\_trigger\_array\_, name)), \

685 .max = ARRAY\_SIZE(\_CONCAT(\_\_trigger\_array\_, name)), \

686 }; \

687 RTIO\_IODEV\_DEFINE(name, &\_\_sensor\_iodev\_api, &\_CONCAT(\_\_sensor\_read\_config\_, name))

688

689/\* Used to submit an RTIO sqe to the sensor's iodev \*/

[ 690](group__sensor__interface.md#gad77732c8f0ec5520cdd71c2829787981)typedef void (\*[sensor\_submit\_t](group__sensor__interface.md#gad77732c8f0ec5520cdd71c2829787981))(const struct [device](structdevice.md) \*sensor, struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b));

691

692/\* The default decoder API \*/

693extern const struct [sensor\_decoder\_api](structsensor__decoder__api.md) \_\_sensor\_default\_decoder;

694

695/\* The default sensor iodev API \*/

696extern const struct [rtio\_iodev\_api](structrtio__iodev__api.md) \_\_sensor\_iodev\_api;

697

[ 698](structsensor__driver__api.md)\_\_subsystem struct [sensor\_driver\_api](structsensor__driver__api.md) {

[ 699](structsensor__driver__api.md#a2d230a976b19a699d132034f58bb2b6a) [sensor\_attr\_set\_t](group__sensor__interface.md#ga38422ace4194a66a9a912a8ef1e088fb) [attr\_set](structsensor__driver__api.md#a2d230a976b19a699d132034f58bb2b6a);

[ 700](structsensor__driver__api.md#a3e28950f844c3f8b8da5ba9ff8052e46) [sensor\_attr\_get\_t](group__sensor__interface.md#ga00d05c82b46e56dca5f6e8f7f01c31b8) [attr\_get](structsensor__driver__api.md#a3e28950f844c3f8b8da5ba9ff8052e46);

[ 701](structsensor__driver__api.md#a4708070fd6654ecbbe631819aba319bd) [sensor\_trigger\_set\_t](group__sensor__interface.md#gad7f7a3d9e714cc16f23656ca06592aa4) [trigger\_set](structsensor__driver__api.md#a4708070fd6654ecbbe631819aba319bd);

[ 702](structsensor__driver__api.md#a4b40e25b81fe070e2f6bdcf7f8a4a31f) [sensor\_sample\_fetch\_t](group__sensor__interface.md#gacae110a4edb6f29dfb457cb1ea8d68c1) [sample\_fetch](structsensor__driver__api.md#a4b40e25b81fe070e2f6bdcf7f8a4a31f);

[ 703](structsensor__driver__api.md#a667b41bf51f2c7a6bb31713fbf889113) [sensor\_channel\_get\_t](group__sensor__interface.md#ga5c9b5ed9097464562004b446856043fd) [channel\_get](structsensor__driver__api.md#a667b41bf51f2c7a6bb31713fbf889113);

[ 704](structsensor__driver__api.md#a004f9d342805dc72249ab9b8c17a544b) [sensor\_get\_decoder\_t](group__sensor__interface.md#ga21e407d552d140cfb6bfd0d9513c7d42) [get\_decoder](structsensor__driver__api.md#a004f9d342805dc72249ab9b8c17a544b);

[ 705](structsensor__driver__api.md#ae3ba0adeba21351e8f660896e5a0e702) [sensor\_submit\_t](group__sensor__interface.md#gad77732c8f0ec5520cdd71c2829787981) [submit](structsensor__driver__api.md#ae3ba0adeba21351e8f660896e5a0e702);

706};

707

[ 720](group__sensor__interface.md#gafbf65226a227e9f8824908bc38e336f5)\_\_syscall int [sensor\_attr\_set](group__sensor__interface.md#gafbf65226a227e9f8824908bc38e336f5)(const struct [device](structdevice.md) \*dev,

721 enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) chan,

722 enum [sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b) attr,

723 const struct [sensor\_value](structsensor__value.md) \*val);

724

725static inline int z\_impl\_sensor\_attr\_set(const struct [device](structdevice.md) \*dev,

726 enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) chan,

727 enum [sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b) attr,

728 const struct [sensor\_value](structsensor__value.md) \*val)

729{

730 const struct [sensor\_driver\_api](structsensor__driver__api.md) \*api =

731 (const struct [sensor\_driver\_api](structsensor__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

732

733 if (api->attr\_set == NULL) {

734 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

735 }

736

737 return api->attr\_set(dev, chan, attr, val);

738}

739

[ 752](group__sensor__interface.md#gaedfdfc71dce702dc1fb1c6e60ff0f73a)\_\_syscall int [sensor\_attr\_get](group__sensor__interface.md#gaedfdfc71dce702dc1fb1c6e60ff0f73a)(const struct [device](structdevice.md) \*dev,

753 enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) chan,

754 enum [sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b) attr,

755 struct [sensor\_value](structsensor__value.md) \*val);

756

757static inline int z\_impl\_sensor\_attr\_get(const struct [device](structdevice.md) \*dev,

758 enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) chan,

759 enum [sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b) attr,

760 struct [sensor\_value](structsensor__value.md) \*val)

761{

762 const struct [sensor\_driver\_api](structsensor__driver__api.md) \*api =

763 (const struct [sensor\_driver\_api](structsensor__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

764

765 if (api->attr\_get == NULL) {

766 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

767 }

768

769 return api->attr\_get(dev, chan, attr, val);

770}

771

[ 794](group__sensor__interface.md#ga7c72aca732e0641612d2f9437c2e41b7)static inline int [sensor\_trigger\_set](group__sensor__interface.md#ga7c72aca732e0641612d2f9437c2e41b7)(const struct [device](structdevice.md) \*dev,

795 const struct [sensor\_trigger](structsensor__trigger.md) \*trig,

796 [sensor\_trigger\_handler\_t](group__sensor__interface.md#ga890c1fb6d6974aea22a2d08829a75902) handler)

797{

798 const struct [sensor\_driver\_api](structsensor__driver__api.md) \*api =

799 (const struct [sensor\_driver\_api](structsensor__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

800

801 if (api->[trigger\_set](structsensor__driver__api.md#a4708070fd6654ecbbe631819aba319bd) == NULL) {

802 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

803 }

804

805 return api->[trigger\_set](structsensor__driver__api.md#a4708070fd6654ecbbe631819aba319bd)(dev, trig, handler);

806}

807

[ 826](group__sensor__interface.md#gaa75e25d93ee7cac0bf38399f3c006dff)\_\_syscall int [sensor\_sample\_fetch](group__sensor__interface.md#gaa75e25d93ee7cac0bf38399f3c006dff)(const struct [device](structdevice.md) \*dev);

827

828static inline int z\_impl\_sensor\_sample\_fetch(const struct [device](structdevice.md) \*dev)

829{

830 const struct [sensor\_driver\_api](structsensor__driver__api.md) \*api =

831 (const struct [sensor\_driver\_api](structsensor__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

832

833 return api->sample\_fetch(dev, [SENSOR\_CHAN\_ALL](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ab275027eb550b2b075c44917634eca2c));

834}

835

[ 857](group__sensor__interface.md#gac16192826432438a15274cf28d66e8a6)\_\_syscall int [sensor\_sample\_fetch\_chan](group__sensor__interface.md#gac16192826432438a15274cf28d66e8a6)(const struct [device](structdevice.md) \*dev,

858 enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) type);

859

860static inline int z\_impl\_sensor\_sample\_fetch\_chan(const struct [device](structdevice.md) \*dev,

861 enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) type)

862{

863 const struct [sensor\_driver\_api](structsensor__driver__api.md) \*api =

864 (const struct [sensor\_driver\_api](structsensor__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

865

866 return api->sample\_fetch(dev, type);

867}

868

[ 890](group__sensor__interface.md#ga9e0e6c1408d32c52267984bae7cb268d)\_\_syscall int [sensor\_channel\_get](group__sensor__interface.md#ga9e0e6c1408d32c52267984bae7cb268d)(const struct [device](structdevice.md) \*dev,

891 enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) chan,

892 struct [sensor\_value](structsensor__value.md) \*val);

893

894static inline int z\_impl\_sensor\_channel\_get(const struct [device](structdevice.md) \*dev,

895 enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) chan,

896 struct [sensor\_value](structsensor__value.md) \*val)

897{

898 const struct [sensor\_driver\_api](structsensor__driver__api.md) \*api =

899 (const struct [sensor\_driver\_api](structsensor__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

900

901 return api->channel\_get(dev, chan, val);

902}

903

904#if defined(CONFIG\_SENSOR\_ASYNC\_API) || defined(\_\_DOXYGEN\_\_)

905

906/\*

907 \* Generic data structure used for encoding the sample timestamp and number of channels sampled.

908 \*/

[ 909](structsensor__data__generic__header.md)struct \_\_attribute\_\_((\_\_packed\_\_)) [sensor\_data\_generic\_header](structsensor__data__generic__header.md) {

910 /\* The timestamp at which the data was collected from the sensor \*/

[ 911](structsensor__data__generic__header.md#a429e22b3191df271ccfe321b796e1ac9) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [timestamp\_ns](structsensor__data__generic__header.md#a429e22b3191df271ccfe321b796e1ac9);

912

913 /\*

914 \* The number of channels present in the frame. This will be the true number of elements in

915 \* channel\_info and in the q31 values that follow the header.

916 \*/

[ 917](structsensor__data__generic__header.md#a7edbe674f28c95f3aa40b1df84ca61fe) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [num\_channels](structsensor__data__generic__header.md#a7edbe674f28c95f3aa40b1df84ca61fe);

918

919 /\* Shift value for all samples in the frame \*/

[ 920](structsensor__data__generic__header.md#a68067521c1058b6802176e1d48fed788) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [shift](structsensor__data__generic__header.md#a68067521c1058b6802176e1d48fed788);

921

922 /\* This padding is needed to make sure that the 'channels' field is aligned \*/

923 [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) \_padding[sizeof(struct [sensor\_chan\_spec](structsensor__chan__spec.md)) - 1];

924

925 /\* Channels present in the frame \*/

[ 926](structsensor__data__generic__header.md#ac09f23959c66ff75b0854a95e8d4504b) struct [sensor\_chan\_spec](structsensor__chan__spec.md) [channels](structsensor__data__generic__header.md#ac09f23959c66ff75b0854a95e8d4504b)[0];

927};

928

[ 937](group__sensor__interface.md#ga32f679a4004b5707b2de00eb580d0930)#define SENSOR\_CHANNEL\_3\_AXIS(chan) \

938 ((chan) == SENSOR\_CHAN\_ACCEL\_XYZ || (chan) == SENSOR\_CHAN\_GYRO\_XYZ || \

939 (chan) == SENSOR\_CHAN\_MAGN\_XYZ || (chan) == SENSOR\_CHAN\_POS\_DXYZ)

940

[ 949](group__sensor__interface.md#ga12db6fc43adce48d34c25c16fd2336a3)\_\_syscall int [sensor\_get\_decoder](group__sensor__interface.md#ga12db6fc43adce48d34c25c16fd2336a3)(const struct [device](structdevice.md) \*dev,

950 const struct [sensor\_decoder\_api](structsensor__decoder__api.md) \*\*decoder);

951

952static inline int z\_impl\_sensor\_get\_decoder(const struct [device](structdevice.md) \*dev,

953 const struct [sensor\_decoder\_api](structsensor__decoder__api.md) \*\*decoder)

954{

955 const struct [sensor\_driver\_api](structsensor__driver__api.md) \*api = (const struct [sensor\_driver\_api](structsensor__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

956

957 \_\_ASSERT\_NO\_MSG(api != NULL);

958

959 if (api->get\_decoder == NULL) {

960 \*decoder = &\_\_sensor\_default\_decoder;

961 return 0;

962 }

963

964 return api->get\_decoder(dev, decoder);

965}

966

[ 985](group__sensor__interface.md#gab854651e1b6c3206bf2b829ea5a6c420)\_\_syscall int [sensor\_reconfigure\_read\_iodev](group__sensor__interface.md#gab854651e1b6c3206bf2b829ea5a6c420)(struct [rtio\_iodev](structrtio__iodev.md) \*iodev, const struct [device](structdevice.md) \*sensor,

986 const struct [sensor\_chan\_spec](structsensor__chan__spec.md) \*channels,

987 size\_t num\_channels);

988

989static inline int z\_impl\_sensor\_reconfigure\_read\_iodev(struct [rtio\_iodev](structrtio__iodev.md) \*iodev,

990 const struct [device](structdevice.md) \*sensor,

991 const struct [sensor\_chan\_spec](structsensor__chan__spec.md) \*channels,

992 size\_t num\_channels)

993{

994 struct [sensor\_read\_config](structsensor__read__config.md) \*cfg = (struct [sensor\_read\_config](structsensor__read__config.md) \*)iodev->[data](structrtio__iodev.md#af0f3a27fe8dea2161c9a73cb838bdeec);

995

996 if (cfg->max < num\_channels || cfg->is\_streaming) {

997 return -[ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5);

998 }

999

1000 cfg->sensor = [sensor](structsensor__read__config.md#ad49d5ab5293017d1ad2cf60adc542090);

1001 [memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)(cfg->channels, [channels](structsensor__read__config.md#a2aff44f02b25fd4ad1d4bc217800fad1), num\_channels \* sizeof(struct [sensor\_chan\_spec](structsensor__chan__spec.md)));

1002 cfg->count = num\_channels;

1003 return 0;

1004}

1005

[ 1006](group__sensor__interface.md#gac77fc83844935f61a2bf9ab2c38987b6)static inline int [sensor\_stream](group__sensor__interface.md#gac77fc83844935f61a2bf9ab2c38987b6)(struct [rtio\_iodev](structrtio__iodev.md) \*iodev, struct [rtio](structrtio.md) \*ctx, void \*userdata,

1007 struct [rtio\_sqe](structrtio__sqe.md) \*\*handle)

1008{

1009 if ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_USERSPACE)) {

1010 struct [rtio\_sqe](structrtio__sqe.md) sqe;

1011

1012 [rtio\_sqe\_prep\_read\_multishot](group__rtio.md#ga9803aa829f8c0eeee746ea7d872c20cc)(&sqe, [iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc), [RTIO\_PRIO\_NORM](group__rtio__sqe__prio.md#gab02e27e01b7dd4eb3439df557899ce92), [userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971));

1013 [rtio\_sqe\_copy\_in\_get\_handles](group__rtio.md#ga830863e6c8d9b96f4c473a038cab8f8c)(ctx, &sqe, handle, 1);

1014 } else {

1015 struct [rtio\_sqe](structrtio__sqe.md) \*sqe = [rtio\_sqe\_acquire](group__rtio.md#ga8b47c954d15a334621def53acceb6799)(ctx);

1016

1017 if (sqe == NULL) {

1018 return -[ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5);

1019 }

1020 if (handle != NULL) {

1021 \*handle = sqe;

1022 }

1023 [rtio\_sqe\_prep\_read\_multishot](group__rtio.md#ga9803aa829f8c0eeee746ea7d872c20cc)(sqe, [iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc), [RTIO\_PRIO\_NORM](group__rtio__sqe__prio.md#gab02e27e01b7dd4eb3439df557899ce92), [userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971));

1024 }

1025 [rtio\_submit](group__rtio.md#gafee27c64a4a4989c4eb774addde8eb2e)(ctx, 0);

1026 return 0;

1027}

1028

[ 1043](group__sensor__interface.md#ga1e77abad33cfd4b8330484cdc1354976)static inline int [sensor\_read](group__sensor__interface.md#ga1e77abad33cfd4b8330484cdc1354976)(struct [rtio\_iodev](structrtio__iodev.md) \*[iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc), struct [rtio](structrtio.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structrtio__sqe.md#a55e98f27b26393fee8e179b7bdb6a52e),

1044 size\_t [buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722))

1045{

1046 if ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_USERSPACE)) {

1047 struct [rtio\_sqe](structrtio__sqe.md) sqe;

1048

1049 [rtio\_sqe\_prep\_read](group__rtio.md#ga89c7cc2494e3dda50737f78f1a1376cf)(&sqe, [iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc), [RTIO\_PRIO\_NORM](group__rtio__sqe__prio.md#gab02e27e01b7dd4eb3439df557899ce92), [buf](structrtio__sqe.md#a55e98f27b26393fee8e179b7bdb6a52e), [buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722), [buf](structrtio__sqe.md#a55e98f27b26393fee8e179b7bdb6a52e));

1050 [rtio\_sqe\_copy\_in](group__rtio.md#ga65e351af0a16dcf504a51ef4eb9316c7)(ctx, &sqe, 1);

1051 } else {

1052 struct [rtio\_sqe](structrtio__sqe.md) \*sqe = [rtio\_sqe\_acquire](group__rtio.md#ga8b47c954d15a334621def53acceb6799)(ctx);

1053

1054 if (sqe == NULL) {

1055 return -[ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5);

1056 }

1057 [rtio\_sqe\_prep\_read](group__rtio.md#ga89c7cc2494e3dda50737f78f1a1376cf)(sqe, [iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc), [RTIO\_PRIO\_NORM](group__rtio__sqe__prio.md#gab02e27e01b7dd4eb3439df557899ce92), [buf](structrtio__sqe.md#a55e98f27b26393fee8e179b7bdb6a52e), [buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722), [buf](structrtio__sqe.md#a55e98f27b26393fee8e179b7bdb6a52e));

1058 }

1059 [rtio\_submit](group__rtio.md#gafee27c64a4a4989c4eb774addde8eb2e)(ctx, 0);

1060

1061 struct [rtio\_cqe](structrtio__cqe.md) \*cqe = [rtio\_cqe\_consume\_block](group__rtio.md#gaf617d05d9b59ce1f1d0697617ef6f249)(ctx);

1062 int res = cqe->[result](structrtio__cqe.md#acbe2e6607a752b676d9336b9ca6ce435);

1063

1064 \_\_ASSERT(cqe->[userdata](structrtio__cqe.md#a15128387ccbea55812ef229eab7241e7) != buf,

1065 "consumed non-matching completion for sensor read into buffer %p\n", buf);

1066

1067 [rtio\_cqe\_release](group__rtio.md#gaa0799a5f8ad98425d385a07c5d27d9cb)(ctx, cqe);

1068

1069 return res;

1070}

1071

[ 1085](group__sensor__interface.md#gab9eee9440b46b545b1faae224ae5949a)static inline int [sensor\_read\_async\_mempool](group__sensor__interface.md#gab9eee9440b46b545b1faae224ae5949a)(struct [rtio\_iodev](structrtio__iodev.md) \*iodev, struct [rtio](structrtio.md) \*ctx,

1086 void \*[userdata](structrtio__cqe.md#a15128387ccbea55812ef229eab7241e7))

1087{

1088 if ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_USERSPACE)) {

1089 struct [rtio\_sqe](structrtio__sqe.md) sqe;

1090

1091 [rtio\_sqe\_prep\_read\_with\_pool](group__rtio.md#ga15c1f623658d27d300d1a31a6f3d6b9d)(&sqe, [iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc), [RTIO\_PRIO\_NORM](group__rtio__sqe__prio.md#gab02e27e01b7dd4eb3439df557899ce92), [userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971));

1092 [rtio\_sqe\_copy\_in](group__rtio.md#ga65e351af0a16dcf504a51ef4eb9316c7)(ctx, &sqe, 1);

1093 } else {

1094 struct [rtio\_sqe](structrtio__sqe.md) \*sqe = [rtio\_sqe\_acquire](group__rtio.md#ga8b47c954d15a334621def53acceb6799)(ctx);

1095

1096 if (sqe == NULL) {

1097 return -[ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5);

1098 }

1099 [rtio\_sqe\_prep\_read\_with\_pool](group__rtio.md#ga15c1f623658d27d300d1a31a6f3d6b9d)(sqe, [iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc), [RTIO\_PRIO\_NORM](group__rtio__sqe__prio.md#gab02e27e01b7dd4eb3439df557899ce92), [userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971));

1100 }

1101 [rtio\_submit](group__rtio.md#gafee27c64a4a4989c4eb774addde8eb2e)(ctx, 0);

1102 return 0;

1103}

1104

[ 1116](group__sensor__interface.md#gaa8cd6e4fadb5d69e59d101733b4fb462)typedef void (\*[sensor\_processing\_callback\_t](group__sensor__interface.md#gaa8cd6e4fadb5d69e59d101733b4fb462))(int result, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structrtio__sqe.md#a55e98f27b26393fee8e179b7bdb6a52e), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722),

1117 void \*[userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971));

1118

[ 1130](group__sensor__interface.md#gabb076531445e1b128d515b28c7cc9dc8)void [sensor\_processing\_with\_callback](group__sensor__interface.md#gabb076531445e1b128d515b28c7cc9dc8)(struct [rtio](structrtio.md) \*ctx, [sensor\_processing\_callback\_t](group__sensor__interface.md#gaa8cd6e4fadb5d69e59d101733b4fb462) cb);

1131

1132#endif /\* defined(CONFIG\_SENSOR\_ASYNC\_API) || defined(\_\_DOXYGEN\_\_) \*/

1133

[ 1137](group__sensor__interface.md#ga0066e049c4f084305ca2b978e5c7454d)#define SENSOR\_G 9806650LL

1138

[ 1142](group__sensor__interface.md#ga6ebdc2f6942334de3cc248a53db7df33)#define SENSOR\_PI 3141592LL

1143

[ 1152](group__sensor__interface.md#gab797f2f578b1c9cc44f54ab5d503bbf8)static inline [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [sensor\_ms2\_to\_g](group__sensor__interface.md#gab797f2f578b1c9cc44f54ab5d503bbf8)(const struct [sensor\_value](structsensor__value.md) \*ms2)

1153{

1154 [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) micro\_ms2 = ms2->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) \* 1000000LL + ms2->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b);

1155

1156 if (micro\_ms2 > 0) {

1157 return (micro\_ms2 + [SENSOR\_G](group__sensor__interface.md#ga0066e049c4f084305ca2b978e5c7454d) / 2) / [SENSOR\_G](group__sensor__interface.md#ga0066e049c4f084305ca2b978e5c7454d);

1158 } else {

1159 return (micro\_ms2 - [SENSOR\_G](group__sensor__interface.md#ga0066e049c4f084305ca2b978e5c7454d) / 2) / [SENSOR\_G](group__sensor__interface.md#ga0066e049c4f084305ca2b978e5c7454d);

1160 }

1161}

1162

[ 1169](group__sensor__interface.md#ga6ab9ce9c6ee2e52d197e5cb4ccd88979)static inline void [sensor\_g\_to\_ms2](group__sensor__interface.md#ga6ab9ce9c6ee2e52d197e5cb4ccd88979)([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) g, struct [sensor\_value](structsensor__value.md) \*ms2)

1170{

1171 ms2->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) = (([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))g \* [SENSOR\_G](group__sensor__interface.md#ga0066e049c4f084305ca2b978e5c7454d)) / 1000000LL;

1172 ms2->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b) = (([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))g \* [SENSOR\_G](group__sensor__interface.md#ga0066e049c4f084305ca2b978e5c7454d)) % 1000000LL;

1173}

1174

[ 1183](group__sensor__interface.md#ga3db980100e634310a0a1623136048742)static inline [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [sensor\_ms2\_to\_ug](group__sensor__interface.md#ga3db980100e634310a0a1623136048742)(const struct [sensor\_value](structsensor__value.md) \*ms2)

1184{

1185 [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) micro\_ms2 = (ms2->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) \* [INT64\_C](xcc_8h.md#a93d102802b35d3b8abae9bbe7f0fed75)(1000000)) + ms2->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b);

1186

1187 return (micro\_ms2 \* 1000000LL) / [SENSOR\_G](group__sensor__interface.md#ga0066e049c4f084305ca2b978e5c7454d);

1188}

1189

[ 1196](group__sensor__interface.md#ga28a1c6cf74a391712a4697792f759d62)static inline void [sensor\_ug\_to\_ms2](group__sensor__interface.md#ga28a1c6cf74a391712a4697792f759d62)([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) ug, struct [sensor\_value](structsensor__value.md) \*ms2)

1197{

1198 ms2->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) = (([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))ug \* [SENSOR\_G](group__sensor__interface.md#ga0066e049c4f084305ca2b978e5c7454d) / 1000000LL) / 1000000LL;

1199 ms2->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b) = (([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))ug \* [SENSOR\_G](group__sensor__interface.md#ga0066e049c4f084305ca2b978e5c7454d) / 1000000LL) % 1000000LL;

1200}

1201

[ 1209](group__sensor__interface.md#ga040a907c8934baab66d27b8dfb1ea220)static inline [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [sensor\_rad\_to\_degrees](group__sensor__interface.md#ga040a907c8934baab66d27b8dfb1ea220)(const struct [sensor\_value](structsensor__value.md) \*rad)

1210{

1211 [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) micro\_rad\_s = rad->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) \* 1000000LL + rad->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b);

1212

1213 if (micro\_rad\_s > 0) {

1214 return (micro\_rad\_s \* 180LL + [SENSOR\_PI](group__sensor__interface.md#ga6ebdc2f6942334de3cc248a53db7df33) / 2) / [SENSOR\_PI](group__sensor__interface.md#ga6ebdc2f6942334de3cc248a53db7df33);

1215 } else {

1216 return (micro\_rad\_s \* 180LL - [SENSOR\_PI](group__sensor__interface.md#ga6ebdc2f6942334de3cc248a53db7df33) / 2) / [SENSOR\_PI](group__sensor__interface.md#ga6ebdc2f6942334de3cc248a53db7df33);

1217 }

1218}

1219

[ 1226](group__sensor__interface.md#ga39d4b84f5d792e27b2d6d5eb6a2ccb0d)static inline void [sensor\_degrees\_to\_rad](group__sensor__interface.md#ga39d4b84f5d792e27b2d6d5eb6a2ccb0d)([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), struct [sensor\_value](structsensor__value.md) \*rad)

1227{

1228 rad->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) = (([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417) \* [SENSOR\_PI](group__sensor__interface.md#ga6ebdc2f6942334de3cc248a53db7df33) / 180LL) / 1000000LL;

1229 rad->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b) = (([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417) \* [SENSOR\_PI](group__sensor__interface.md#ga6ebdc2f6942334de3cc248a53db7df33) / 180LL) % 1000000LL;

1230}

1231

[ 1243](group__sensor__interface.md#gad80093a6cfe95428dd0ead85547838a6)static inline [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [sensor\_rad\_to\_10udegrees](group__sensor__interface.md#gad80093a6cfe95428dd0ead85547838a6)(const struct [sensor\_value](structsensor__value.md) \*rad)

1244{

1245 [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) micro\_rad\_s = rad->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) \* 1000000LL + rad->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b);

1246

1247 return (micro\_rad\_s \* 180LL \* 100000LL) / [SENSOR\_PI](group__sensor__interface.md#ga6ebdc2f6942334de3cc248a53db7df33);

1248}

1249

[ 1256](group__sensor__interface.md#gab53418e1eb164364663d3ec3f40399a4)static inline void [sensor\_10udegrees\_to\_rad](group__sensor__interface.md#gab53418e1eb164364663d3ec3f40399a4)([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), struct [sensor\_value](structsensor__value.md) \*rad)

1257{

1258 rad->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) = (([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417) \* [SENSOR\_PI](group__sensor__interface.md#ga6ebdc2f6942334de3cc248a53db7df33) / 180LL / 100000LL) / 1000000LL;

1259 rad->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b) = (([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417) \* [SENSOR\_PI](group__sensor__interface.md#ga6ebdc2f6942334de3cc248a53db7df33) / 180LL / 100000LL) % 1000000LL;

1260}

1261

[ 1268](group__sensor__interface.md#ga29223b754dc436ab1e97ce6209a3ea06)static inline double [sensor\_value\_to\_double](group__sensor__interface.md#ga29223b754dc436ab1e97ce6209a3ea06)(const struct [sensor\_value](structsensor__value.md) \*val)

1269{

1270 return (double)val->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) + (double)val->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b) / 1000000;

1271}

1272

[ 1279](group__sensor__interface.md#ga2ad1fc2abd1c8c38e7de6e99fa5c1f20)static inline float [sensor\_value\_to\_float](group__sensor__interface.md#ga2ad1fc2abd1c8c38e7de6e99fa5c1f20)(const struct [sensor\_value](structsensor__value.md) \*val)

1280{

1281 return (float)val->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) + (float)val->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b) / 1000000;

1282}

1283

[ 1291](group__sensor__interface.md#gaf01bbb251ad0c7f6c55c5b702e8a4048)static inline int [sensor\_value\_from\_double](group__sensor__interface.md#gaf01bbb251ad0c7f6c55c5b702e8a4048)(struct [sensor\_value](structsensor__value.md) \*val, double inp)

1292{

1293 if (inp < INT32\_MIN || inp > [INT32\_MAX](stdint_8h.md#a181807730d4a375f848ba139813ce04f)) {

1294 return -[ERANGE](group__system__errno.md#gaa1591a4f3a86360108de5b9ba34980ca);

1295 }

1296

1297 double val2 = (inp - ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))inp) \* 1000000.0;

1298

1299 if (val2 < INT32\_MIN || val2 > [INT32\_MAX](stdint_8h.md#a181807730d4a375f848ba139813ce04f)) {

1300 return -[ERANGE](group__system__errno.md#gaa1591a4f3a86360108de5b9ba34980ca);

1301 }

1302

1303 val->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) = ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))inp;

1304 val->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b) = ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))val2;

1305

1306 return 0;

1307}

1308

[ 1316](group__sensor__interface.md#ga64d5a1725eda200c80daf42b1067c46c)static inline int [sensor\_value\_from\_float](group__sensor__interface.md#ga64d5a1725eda200c80daf42b1067c46c)(struct [sensor\_value](structsensor__value.md) \*val, float inp)

1317{

1318 float val2 = (inp - ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))inp) \* 1000000.0f;

1319

1320 if (val2 < INT32\_MIN || val2 > (float)([INT32\_MAX](stdint_8h.md#a181807730d4a375f848ba139813ce04f) - 1)) {

1321 return -[ERANGE](group__system__errno.md#gaa1591a4f3a86360108de5b9ba34980ca);

1322 }

1323

1324 val->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) = ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))inp;

1325 val->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b) = ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))val2;

1326

1327 return 0;

1328}

1329

1330#ifdef CONFIG\_SENSOR\_INFO

1331

1332struct sensor\_info {

1333 const struct device \*dev;

1334 const char \*vendor;

1335 const char \*model;

1336 const char \*friendly\_name;

1337};

1338

1339#define SENSOR\_INFO\_INITIALIZER(\_dev, \_vendor, \_model, \_friendly\_name) \

1340 { \

1341 .dev = \_dev, \

1342 .vendor = \_vendor, \

1343 .model = \_model, \

1344 .friendly\_name = \_friendly\_name, \

1345 }

1346

1347#define SENSOR\_INFO\_DEFINE(name, ...) \

1348 static const STRUCT\_SECTION\_ITERABLE(sensor\_info, name) = \

1349 SENSOR\_INFO\_INITIALIZER(\_\_VA\_ARGS\_\_)

1350

1351#define SENSOR\_INFO\_DT\_NAME(node\_id) \

1352 \_CONCAT(\_\_sensor\_info, DEVICE\_DT\_NAME\_GET(node\_id))

1353

1354#define SENSOR\_INFO\_DT\_DEFINE(node\_id) \

1355 SENSOR\_INFO\_DEFINE(SENSOR\_INFO\_DT\_NAME(node\_id), \

1356 DEVICE\_DT\_GET(node\_id), \

1357 DT\_NODE\_VENDOR\_OR(node\_id, NULL), \

1358 DT\_NODE\_MODEL\_OR(node\_id, NULL), \

1359 DT\_PROP\_OR(node\_id, friendly\_name, NULL)) \

1360

1361#else

1362

[ 1363](group__sensor__interface.md#ga7467206da76c3704d2e491d1b1c0973a)#define SENSOR\_INFO\_DEFINE(name, ...)

[ 1364](group__sensor__interface.md#ga9e6acbc580e9223bfb86ee8919cdc778)#define SENSOR\_INFO\_DT\_DEFINE(node\_id)

1365

1366#endif /\* CONFIG\_SENSOR\_INFO \*/

1367

[ 1395](group__sensor__interface.md#gaa67ca630e3931a0c3821ba438c86690c)#define SENSOR\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm\_device, \

1396 data\_ptr, cfg\_ptr, level, prio, \

1397 api\_ptr, ...) \

1398 DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm\_device, \

1399 data\_ptr, cfg\_ptr, level, prio, \

1400 api\_ptr, \_\_VA\_ARGS\_\_); \

1401 \

1402 SENSOR\_INFO\_DT\_DEFINE(node\_id);

1403

[ 1413](group__sensor__interface.md#ga284dc3b9018f14161dc0a2b6bed9a37e)#define SENSOR\_DEVICE\_DT\_INST\_DEFINE(inst, ...) \

1414 SENSOR\_DEVICE\_DT\_DEFINE(DT\_DRV\_INST(inst), \_\_VA\_ARGS\_\_)

1415

[ 1422](group__sensor__interface.md#ga6d69a9644e08a9cd7773645fa11293e3)static inline [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [sensor\_value\_to\_milli](group__sensor__interface.md#ga6d69a9644e08a9cd7773645fa11293e3)(const struct [sensor\_value](structsensor__value.md) \*val)

1423{

1424 return (([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))val->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) \* 1000) + val->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b) / 1000;

1425}

1426

[ 1433](group__sensor__interface.md#ga9bf7faf60aa54a7540e9b73a61864e25)static inline [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [sensor\_value\_to\_micro](group__sensor__interface.md#ga9bf7faf60aa54a7540e9b73a61864e25)(const struct [sensor\_value](structsensor__value.md) \*val)

1434{

1435 return (([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))val->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) \* 1000000) + val->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b);

1436}

1437

[ 1445](group__sensor__interface.md#ga88b2605526e37420db871f066c5053b3)static inline int [sensor\_value\_from\_milli](group__sensor__interface.md#ga88b2605526e37420db871f066c5053b3)(struct [sensor\_value](structsensor__value.md) \*val, [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) milli)

1446{

1447 if (milli < (([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))[INT32\_MIN](stdint_8h.md#a688eb21a22db27c2b2bd5836943cdcbe) - 1) \* 1000LL ||

1448 milli > (([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))[INT32\_MAX](stdint_8h.md#a181807730d4a375f848ba139813ce04f) + 1) \* 1000LL) {

1449 return -[ERANGE](group__system__errno.md#gaa1591a4f3a86360108de5b9ba34980ca);

1450 }

1451

1452 val->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) = ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))(milli / 1000);

1453 val->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b) = ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))(milli % 1000) \* 1000;

1454

1455 return 0;

1456}

1457

[ 1465](group__sensor__interface.md#gabff019c63c89cbc546c0981819040c99)static inline int [sensor\_value\_from\_micro](group__sensor__interface.md#gabff019c63c89cbc546c0981819040c99)(struct [sensor\_value](structsensor__value.md) \*val, [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) micro)

1466{

1467 if (micro < (([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))[INT32\_MIN](stdint_8h.md#a688eb21a22db27c2b2bd5836943cdcbe) - 1) \* 1000000LL ||

1468 micro > (([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))[INT32\_MAX](stdint_8h.md#a181807730d4a375f848ba139813ce04f) + 1) \* 1000000LL) {

1469 return -[ERANGE](group__system__errno.md#gaa1591a4f3a86360108de5b9ba34980ca);

1470 }

1471

1472 val->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) = ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))(micro / 1000000LL);

1473 val->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b) = ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))(micro % 1000000LL);

1474

1475 return 0;

1476}

1477

1481

[ 1487](sensor_8h.md#a8d3434eb5860c2f2e6fe36b4de920c8c)#define SENSOR\_DECODER\_NAME() UTIL\_CAT(DT\_DRV\_COMPAT, \_\_decoder\_api)

1488

[ 1496](sensor_8h.md#a82da2432981c593ed638a21c51fb0873)#define SENSOR\_DECODER\_DT\_GET(node\_id) \

1497 &UTIL\_CAT(DT\_STRING\_TOKEN\_BY\_IDX(node\_id, compatible, 0), \_\_decoder\_api)

1498

[ 1514](sensor_8h.md#a78ad4b76be4a6f5347ba82b7db43b7c2)#define SENSOR\_DECODER\_API\_DT\_DEFINE() \

1515 COND\_CODE\_1(DT\_HAS\_COMPAT\_STATUS\_OKAY(DT\_DRV\_COMPAT), (), (static)) \

1516 const STRUCT\_SECTION\_ITERABLE(sensor\_decoder\_api, SENSOR\_DECODER\_NAME())

1517

1518#define Z\_MAYBE\_SENSOR\_DECODER\_DECLARE\_INTERNAL\_IDX(node\_id, prop, idx) \

1519 extern const struct sensor\_decoder\_api UTIL\_CAT( \

1520 DT\_STRING\_TOKEN\_BY\_IDX(node\_id, prop, idx), \_\_decoder\_api);

1521

1522#define Z\_MAYBE\_SENSOR\_DECODER\_DECLARE\_INTERNAL(node\_id) \

1523 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, compatible), \

1524 (DT\_FOREACH\_PROP\_ELEM(node\_id, compatible, \

1525 Z\_MAYBE\_SENSOR\_DECODER\_DECLARE\_INTERNAL\_IDX)), \

1526 ())

1527

1528[DT\_FOREACH\_STATUS\_OKAY\_NODE](group__devicetree-generic-foreach.md#ga926f68202042c9db05390e628787f916)(Z\_MAYBE\_SENSOR\_DECODER\_DECLARE\_INTERNAL)

1529

1530#ifdef \_\_cplusplus

1531}

1532#endif

1533

1534#include <zephyr/syscalls/sensor.h>

1535

1536#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_H\_ \*/

[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)

irp nz macro MOVR cc d

**Definition** asm-macro-32-bit-gnu.h:11

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[DT\_FOREACH\_STATUS\_OKAY\_NODE](group__devicetree-generic-foreach.md#ga926f68202042c9db05390e628787f916)

#define DT\_FOREACH\_STATUS\_OKAY\_NODE(fn)

Invokes fn for every status okay node in the tree.

**Definition** devicetree.h:2785

[RTIO\_PRIO\_NORM](group__rtio__sqe__prio.md#gab02e27e01b7dd4eb3439df557899ce92)

#define RTIO\_PRIO\_NORM

Normal priority.

**Definition** rtio.h:70

[rtio\_sqe\_prep\_read\_with\_pool](group__rtio.md#ga15c1f623658d27d300d1a31a6f3d6b9d)

static void rtio\_sqe\_prep\_read\_with\_pool(struct rtio\_sqe \*sqe, const struct rtio\_iodev \*iodev, int8\_t prio, void \*userdata)

Prepare a read op submission with context's mempool.

**Definition** rtio.h:517

[rtio\_sqe\_copy\_in](group__rtio.md#ga65e351af0a16dcf504a51ef4eb9316c7)

static int rtio\_sqe\_copy\_in(struct rtio \*r, const struct rtio\_sqe \*sqes, size\_t sqe\_count)

Copy an array of SQEs into the queue.

**Definition** rtio.h:1347

[rtio\_sqe\_copy\_in\_get\_handles](group__rtio.md#ga830863e6c8d9b96f4c473a038cab8f8c)

int rtio\_sqe\_copy\_in\_get\_handles(struct rtio \*r, const struct rtio\_sqe \*sqes, struct rtio\_sqe \*\*handle, size\_t sqe\_count)

Copy an array of SQEs into the queue and get resulting handles back.

[rtio\_sqe\_prep\_read](group__rtio.md#ga89c7cc2494e3dda50737f78f1a1376cf)

static void rtio\_sqe\_prep\_read(struct rtio\_sqe \*sqe, const struct rtio\_iodev \*iodev, int8\_t prio, uint8\_t \*buf, uint32\_t len, void \*userdata)

Prepare a read op submission.

**Definition** rtio.h:496

[rtio\_sqe\_acquire](group__rtio.md#ga8b47c954d15a334621def53acceb6799)

static struct rtio\_sqe \* rtio\_sqe\_acquire(struct rtio \*r)

Acquire a single submission queue event if available.

**Definition** rtio.h:901

[rtio\_sqe\_prep\_read\_multishot](group__rtio.md#ga9803aa829f8c0eeee746ea7d872c20cc)

static void rtio\_sqe\_prep\_read\_multishot(struct rtio\_sqe \*sqe, const struct rtio\_iodev \*iodev, int8\_t prio, void \*userdata)

**Definition** rtio.h:525

[rtio\_cqe\_release](group__rtio.md#gaa0799a5f8ad98425d385a07c5d27d9cb)

static void rtio\_cqe\_release(struct rtio \*r, struct rtio\_cqe \*cqe)

Release consumed completion queue event.

**Definition** rtio.h:1020

[rtio\_cqe\_consume\_block](group__rtio.md#gaf617d05d9b59ce1f1d0697617ef6f249)

static struct rtio\_cqe \* rtio\_cqe\_consume\_block(struct rtio \*r)

Wait for and consume a single completion queue event.

**Definition** rtio.h:996

[rtio\_submit](group__rtio.md#gafee27c64a4a4989c4eb774addde8eb2e)

int rtio\_submit(struct rtio \*r, uint32\_t wait\_count)

Submit I/O requests to the underlying executor.

[SENSOR\_G](group__sensor__interface.md#ga0066e049c4f084305ca2b978e5c7454d)

#define SENSOR\_G

The value of gravitational constant in micro m/s^2.

**Definition** sensor.h:1137

[sensor\_attr\_get\_t](group__sensor__interface.md#ga00d05c82b46e56dca5f6e8f7f01c31b8)

int(\* sensor\_attr\_get\_t)(const struct device \*dev, enum sensor\_channel chan, enum sensor\_attribute attr, struct sensor\_value \*val)

Callback API upon getting a sensor's attributes.

**Definition** sensor.h:391

[sensor\_decode](group__sensor__interface.md#ga018bca56056ae2558f9e45aeb2fa5f53)

static int sensor\_decode(struct sensor\_decode\_context \*ctx, void \*out, uint16\_t max\_count)

Decode N frames using a sensor\_decode\_context.

**Definition** sensor.h:579

[sensor\_rad\_to\_degrees](group__sensor__interface.md#ga040a907c8934baab66d27b8dfb1ea220)

static int32\_t sensor\_rad\_to\_degrees(const struct sensor\_value \*rad)

Helper function for converting radians to degrees.

**Definition** sensor.h:1209

[sensor\_trigger\_type](group__sensor__interface.md#ga08215279400e8c9eb05ce4e4f0898ffd)

sensor\_trigger\_type

Sensor trigger types.

**Definition** sensor.h:219

[sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b)

sensor\_attribute

Sensor attribute types.

**Definition** sensor.h:296

[sensor\_get\_decoder](group__sensor__interface.md#ga12db6fc43adce48d34c25c16fd2336a3)

int sensor\_get\_decoder(const struct device \*dev, const struct sensor\_decoder\_api \*\*decoder)

Get the sensor's decoder API.

[sensor\_read](group__sensor__interface.md#ga1e77abad33cfd4b8330484cdc1354976)

static int sensor\_read(struct rtio\_iodev \*iodev, struct rtio \*ctx, uint8\_t \*buf, size\_t buf\_len)

Blocking one shot read of samples from a sensor into a buffer.

**Definition** sensor.h:1043

[sensor\_get\_decoder\_t](group__sensor__interface.md#ga21e407d552d140cfb6bfd0d9513c7d42)

int(\* sensor\_get\_decoder\_t)(const struct device \*dev, const struct sensor\_decoder\_api \*\*api)

Get the decoder associate with the given device.

**Definition** sensor.h:593

[sensor\_ug\_to\_ms2](group__sensor__interface.md#ga28a1c6cf74a391712a4697792f759d62)

static void sensor\_ug\_to\_ms2(int32\_t ug, struct sensor\_value \*ms2)

Helper function to convert acceleration from micro Gs to m/s^2.

**Definition** sensor.h:1196

[sensor\_value\_to\_double](group__sensor__interface.md#ga29223b754dc436ab1e97ce6209a3ea06)

static double sensor\_value\_to\_double(const struct sensor\_value \*val)

Helper function for converting struct sensor\_value to double.

**Definition** sensor.h:1268

[sensor\_value\_to\_float](group__sensor__interface.md#ga2ad1fc2abd1c8c38e7de6e99fa5c1f20)

static float sensor\_value\_to\_float(const struct sensor\_value \*val)

Helper function for converting struct sensor\_value to float.

**Definition** sensor.h:1279

[sensor\_natively\_supported\_channel\_size\_info](group__sensor__interface.md#ga2b045cdbd4d1ca37beed69970093945b)

int sensor\_natively\_supported\_channel\_size\_info(struct sensor\_chan\_spec channel, size\_t \*base\_size, size\_t \*frame\_size)

[sensor\_attr\_set\_t](group__sensor__interface.md#ga38422ace4194a66a9a912a8ef1e088fb)

int(\* sensor\_attr\_set\_t)(const struct device \*dev, enum sensor\_channel chan, enum sensor\_attribute attr, const struct sensor\_value \*val)

Callback API upon setting a sensor's attributes.

**Definition** sensor.h:380

[sensor\_degrees\_to\_rad](group__sensor__interface.md#ga39d4b84f5d792e27b2d6d5eb6a2ccb0d)

static void sensor\_degrees\_to\_rad(int32\_t d, struct sensor\_value \*rad)

Helper function for converting degrees to radians.

**Definition** sensor.h:1226

[sensor\_ms2\_to\_ug](group__sensor__interface.md#ga3db980100e634310a0a1623136048742)

static int32\_t sensor\_ms2\_to\_ug(const struct sensor\_value \*ms2)

Helper function to convert acceleration from m/s^2 to micro Gs.

**Definition** sensor.h:1183

[sensor\_channel\_get\_t](group__sensor__interface.md#ga5c9b5ed9097464562004b446856043fd)

int(\* sensor\_channel\_get\_t)(const struct device \*dev, enum sensor\_channel chan, struct sensor\_value \*val)

Callback API for getting a reading from a sensor.

**Definition** sensor.h:419

[sensor\_value\_from\_float](group__sensor__interface.md#ga64d5a1725eda200c80daf42b1067c46c)

static int sensor\_value\_from\_float(struct sensor\_value \*val, float inp)

Helper function for converting float to struct sensor\_value.

**Definition** sensor.h:1316

[sensor\_g\_to\_ms2](group__sensor__interface.md#ga6ab9ce9c6ee2e52d197e5cb4ccd88979)

static void sensor\_g\_to\_ms2(int32\_t g, struct sensor\_value \*ms2)

Helper function to convert acceleration from Gs to m/s^2.

**Definition** sensor.h:1169

[sensor\_value\_to\_milli](group__sensor__interface.md#ga6d69a9644e08a9cd7773645fa11293e3)

static int64\_t sensor\_value\_to\_milli(const struct sensor\_value \*val)

Helper function for converting struct sensor\_value to integer milli units.

**Definition** sensor.h:1422

[SENSOR\_PI](group__sensor__interface.md#ga6ebdc2f6942334de3cc248a53db7df33)

#define SENSOR\_PI

The value of constant PI in micros.

**Definition** sensor.h:1142

[sensor\_trigger\_set](group__sensor__interface.md#ga7c72aca732e0641612d2f9437c2e41b7)

static int sensor\_trigger\_set(const struct device \*dev, const struct sensor\_trigger \*trig, sensor\_trigger\_handler\_t handler)

Activate a sensor's trigger and set the trigger handler.

**Definition** sensor.h:794

[sensor\_stream\_data\_opt](group__sensor__interface.md#ga8613a20521a37d40fd7371dc63ba2dac)

sensor\_stream\_data\_opt

Options for what to do with the associated data when a trigger is consumed.

**Definition** sensor.h:599

[sensor\_value\_from\_milli](group__sensor__interface.md#ga88b2605526e37420db871f066c5053b3)

static int sensor\_value\_from\_milli(struct sensor\_value \*val, int64\_t milli)

Helper function for converting integer milli units to struct sensor\_value.

**Definition** sensor.h:1445

[sensor\_trigger\_handler\_t](group__sensor__interface.md#ga890c1fb6d6974aea22a2d08829a75902)

void(\* sensor\_trigger\_handler\_t)(const struct device \*dev, const struct sensor\_trigger \*trigger)

Callback API upon firing of a trigger.

**Definition** sensor.h:371

[sensor\_value\_to\_micro](group__sensor__interface.md#ga9bf7faf60aa54a7540e9b73a61864e25)

static int64\_t sensor\_value\_to\_micro(const struct sensor\_value \*val)

Helper function for converting struct sensor\_value to integer micro units.

**Definition** sensor.h:1433

[sensor\_channel\_get](group__sensor__interface.md#ga9e0e6c1408d32c52267984bae7cb268d)

int sensor\_channel\_get(const struct device \*dev, enum sensor\_channel chan, struct sensor\_value \*val)

Get a reading from a sensor device.

[sensor\_sample\_fetch](group__sensor__interface.md#gaa75e25d93ee7cac0bf38399f3c006dff)

int sensor\_sample\_fetch(const struct device \*dev)

Fetch a sample from the sensor and store it in an internal driver buffer.

[sensor\_processing\_callback\_t](group__sensor__interface.md#gaa8cd6e4fadb5d69e59d101733b4fb462)

void(\* sensor\_processing\_callback\_t)(int result, uint8\_t \*buf, uint32\_t buf\_len, void \*userdata)

Callback function used with the helper processing function.

**Definition** sensor.h:1116

[sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934)

sensor\_channel

Sensor channels.

**Definition** sensor.h:61

[sensor\_10udegrees\_to\_rad](group__sensor__interface.md#gab53418e1eb164364663d3ec3f40399a4)

static void sensor\_10udegrees\_to\_rad(int32\_t d, struct sensor\_value \*rad)

Helper function for converting 10 micro degrees to radians.

**Definition** sensor.h:1256

[sensor\_ms2\_to\_g](group__sensor__interface.md#gab797f2f578b1c9cc44f54ab5d503bbf8)

static int32\_t sensor\_ms2\_to\_g(const struct sensor\_value \*ms2)

Helper function to convert acceleration from m/s^2 to Gs.

**Definition** sensor.h:1152

[sensor\_reconfigure\_read\_iodev](group__sensor__interface.md#gab854651e1b6c3206bf2b829ea5a6c420)

int sensor\_reconfigure\_read\_iodev(struct rtio\_iodev \*iodev, const struct device \*sensor, const struct sensor\_chan\_spec \*channels, size\_t num\_channels)

Reconfigure a reading iodev.

[sensor\_read\_async\_mempool](group__sensor__interface.md#gab9eee9440b46b545b1faae224ae5949a)

static int sensor\_read\_async\_mempool(struct rtio\_iodev \*iodev, struct rtio \*ctx, void \*userdata)

One shot non-blocking read with pool allocated buffer.

**Definition** sensor.h:1085

[sensor\_processing\_with\_callback](group__sensor__interface.md#gabb076531445e1b128d515b28c7cc9dc8)

void sensor\_processing\_with\_callback(struct rtio \*ctx, sensor\_processing\_callback\_t cb)

Helper function for common processing of sensor data.

[sensor\_value\_from\_micro](group__sensor__interface.md#gabff019c63c89cbc546c0981819040c99)

static int sensor\_value\_from\_micro(struct sensor\_value \*val, int64\_t micro)

Helper function for converting integer micro units to struct sensor\_value.

**Definition** sensor.h:1465

[sensor\_sample\_fetch\_chan](group__sensor__interface.md#gac16192826432438a15274cf28d66e8a6)

int sensor\_sample\_fetch\_chan(const struct device \*dev, enum sensor\_channel type)

Fetch a sample from the sensor and store it in an internal driver buffer.

[sensor\_stream](group__sensor__interface.md#gac77fc83844935f61a2bf9ab2c38987b6)

static int sensor\_stream(struct rtio\_iodev \*iodev, struct rtio \*ctx, void \*userdata, struct rtio\_sqe \*\*handle)

**Definition** sensor.h:1006

[sensor\_sample\_fetch\_t](group__sensor__interface.md#gacae110a4edb6f29dfb457cb1ea8d68c1)

int(\* sensor\_sample\_fetch\_t)(const struct device \*dev, enum sensor\_channel chan)

Callback API for fetching data from a sensor.

**Definition** sensor.h:411

[sensor\_submit\_t](group__sensor__interface.md#gad77732c8f0ec5520cdd71c2829787981)

void(\* sensor\_submit\_t)(const struct device \*sensor, struct rtio\_iodev\_sqe \*sqe)

**Definition** sensor.h:690

[sensor\_trigger\_set\_t](group__sensor__interface.md#gad7f7a3d9e714cc16f23656ca06592aa4)

int(\* sensor\_trigger\_set\_t)(const struct device \*dev, const struct sensor\_trigger \*trig, sensor\_trigger\_handler\_t handler)

Callback API for setting a sensor's trigger and handler.

**Definition** sensor.h:402

[sensor\_rad\_to\_10udegrees](group__sensor__interface.md#gad80093a6cfe95428dd0ead85547838a6)

static int32\_t sensor\_rad\_to\_10udegrees(const struct sensor\_value \*rad)

Helper function for converting radians to 10 micro degrees.

**Definition** sensor.h:1243

[sensor\_chan\_spec\_eq](group__sensor__interface.md#gae95715ffea5da18a9593ec2add029824)

static bool sensor\_chan\_spec\_eq(struct sensor\_chan\_spec chan\_spec0, struct sensor\_chan\_spec chan\_spec1)

Check if channel specs are equivalent.

**Definition** sensor.h:450

[sensor\_attr\_get](group__sensor__interface.md#gaedfdfc71dce702dc1fb1c6e60ff0f73a)

int sensor\_attr\_get(const struct device \*dev, enum sensor\_channel chan, enum sensor\_attribute attr, struct sensor\_value \*val)

Get an attribute for a sensor.

[sensor\_value\_from\_double](group__sensor__interface.md#gaf01bbb251ad0c7f6c55c5b702e8a4048)

static int sensor\_value\_from\_double(struct sensor\_value \*val, double inp)

Helper function for converting double to struct sensor\_value.

**Definition** sensor.h:1291

[sensor\_attr\_set](group__sensor__interface.md#gafbf65226a227e9f8824908bc38e336f5)

int sensor\_attr\_set(const struct device \*dev, enum sensor\_channel chan, enum sensor\_attribute attr, const struct sensor\_value \*val)

Set an attribute for a sensor.

[SENSOR\_TRIG\_DELTA](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda3bb90a3334bcf613c9efbdf2ed05f855)

@ SENSOR\_TRIG\_DELTA

Trigger fires when the selected channel varies significantly.

**Definition** sensor.h:235

[SENSOR\_TRIG\_NEAR\_FAR](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda448226d83b28c2862c353a8cda7be0d5)

@ SENSOR\_TRIG\_NEAR\_FAR

Trigger fires when a near/far event is detected.

**Definition** sensor.h:237

[SENSOR\_TRIG\_FREEFALL](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda4943ffb4afaf4cbae39e85693bd4374c)

@ SENSOR\_TRIG\_FREEFALL

Trigger fires when a free fall is detected.

**Definition** sensor.h:253

[SENSOR\_TRIG\_PRIV\_START](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda5e1a94f21fee67ee98296153ea640921)

@ SENSOR\_TRIG\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:275

[SENSOR\_TRIG\_FIFO\_FULL](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda66f913f8751a77a6c16745e329c7315c)

@ SENSOR\_TRIG\_FIFO\_FULL

Trigger fires when the FIFO becomes full.

**Definition** sensor.h:265

[SENSOR\_TRIG\_MOTION](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda7095387831b763b34171287945dae276)

@ SENSOR\_TRIG\_MOTION

Trigger fires when motion is detected.

**Definition** sensor.h:256

[SENSOR\_TRIG\_STATIONARY](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda79e286ffced716e1076f56464ea47f5d)

@ SENSOR\_TRIG\_STATIONARY

Trigger fires when no motion has been detected for a while.

**Definition** sensor.h:259

[SENSOR\_TRIG\_COMMON\_COUNT](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda8d1f2621fad4fd685d56cca3f9b042f5)

@ SENSOR\_TRIG\_COMMON\_COUNT

Number of all common sensor triggers.

**Definition** sensor.h:269

[SENSOR\_TRIG\_THRESHOLD](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda8f875f881b6540eebc28e3d6a7d46606)

@ SENSOR\_TRIG\_THRESHOLD

Trigger fires when channel reading transitions configured thresholds.

**Definition** sensor.h:244

[SENSOR\_TRIG\_MAX](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda9de566f44de519f94c59c58df1efc4c4)

@ SENSOR\_TRIG\_MAX

Maximum value describing a sensor trigger type.

**Definition** sensor.h:280

[SENSOR\_TRIG\_DOUBLE\_TAP](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdab95e52584a6bc3343181f495cd4cb2ef)

@ SENSOR\_TRIG\_DOUBLE\_TAP

Trigger fires when a double tap is detected.

**Definition** sensor.h:250

[SENSOR\_TRIG\_TIMER](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdabf92b196394726ec90f1d61586a7f023)

@ SENSOR\_TRIG\_TIMER

Timer-based trigger, useful when the sensor does not have an interrupt line.

**Definition** sensor.h:224

[SENSOR\_TRIG\_FIFO\_WATERMARK](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdac5d67fb4fb6206465b1b01dc78245fe4)

@ SENSOR\_TRIG\_FIFO\_WATERMARK

Trigger fires when the FIFO watermark has been reached.

**Definition** sensor.h:262

[SENSOR\_TRIG\_TAP](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdae49a25e6400f0753f6bac8a7d136200d)

@ SENSOR\_TRIG\_TAP

Trigger fires when a single tap is detected.

**Definition** sensor.h:247

[SENSOR\_TRIG\_DATA\_READY](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdaf7c161e309c267a7dd6daf2ad176f44f)

@ SENSOR\_TRIG\_DATA\_READY

Trigger fires whenever new data is ready.

**Definition** sensor.h:226

[SENSOR\_ATTR\_HYSTERESIS](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba044e67bfc04e8ddc2de7d2058fffbc94)

@ SENSOR\_ATTR\_HYSTERESIS

**Definition** sensor.h:314

[SENSOR\_ATTR\_FEATURE\_MASK](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba1f8d2242fa9d63a13c6a48fe3a1cbe52)

@ SENSOR\_ATTR\_FEATURE\_MASK

Enable/disable sensor features.

**Definition** sensor.h:334

[SENSOR\_ATTR\_CALIB\_TARGET](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba3043381b539610a8b424f12d76474bdf)

@ SENSOR\_ATTR\_CALIB\_TARGET

Calibration target.

**Definition** sensor.h:328

[SENSOR\_ATTR\_OFFSET](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba332935dcb6f7e228cb9c595a545079fd)

@ SENSOR\_ATTR\_OFFSET

The sensor value returned will be altered by the amount indicated by offset: final\_value = sensor\_val...

**Definition** sensor.h:323

[SENSOR\_ATTR\_BATCH\_DURATION](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba3b0cf69c77de55c92129e212bf5b8ced)

@ SENSOR\_ATTR\_BATCH\_DURATION

Hardware batch duration in ticks.

**Definition** sensor.h:345

[SENSOR\_ATTR\_OVERSAMPLING](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba3d32987f75284d80d3f64bf44f5c6ccd)

@ SENSOR\_ATTR\_OVERSAMPLING

Oversampling factor.

**Definition** sensor.h:316

[SENSOR\_ATTR\_FF\_DUR](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba5a62ea6aa7e55efd62ab3f93dcb0593a)

@ SENSOR\_ATTR\_FF\_DUR

Free-fall duration represented in milliseconds.

**Definition** sensor.h:342

[SENSOR\_ATTR\_UPPER\_THRESH](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba5af51bd0640a87a94476eee112a4460b)

@ SENSOR\_ATTR\_UPPER\_THRESH

Upper threshold for trigger.

**Definition** sensor.h:305

[SENSOR\_ATTR\_CONFIGURATION](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba75cd3aca26859fd7c10c83d86e3471e9)

@ SENSOR\_ATTR\_CONFIGURATION

Configure the operating modes of a sensor.

**Definition** sensor.h:330

[SENSOR\_ATTR\_CALIBRATION](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba843d1e79573c634987e5e839ba9e965e)

@ SENSOR\_ATTR\_CALIBRATION

Set a calibration value needed by a sensor.

**Definition** sensor.h:332

[SENSOR\_ATTR\_COMMON\_COUNT](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba99ceedef81217614ada0c8a469f91eb8)

@ SENSOR\_ATTR\_COMMON\_COUNT

Number of all common sensor attributes.

**Definition** sensor.h:350

[SENSOR\_ATTR\_ALERT](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940baaedf76e63224adc3fa266d35666e0a3a)

@ SENSOR\_ATTR\_ALERT

Alert threshold or alert enable/disable.

**Definition** sensor.h:336

[SENSOR\_ATTR\_SLOPE\_TH](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bac4538665a244cb7f18fc053c40134302)

@ SENSOR\_ATTR\_SLOPE\_TH

Threshold for any-motion (slope) trigger.

**Definition** sensor.h:307

[SENSOR\_ATTR\_SAMPLING\_FREQUENCY](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bacb07e3508ea5503dbcdceee3f17d2291)

@ SENSOR\_ATTR\_SAMPLING\_FREQUENCY

Sensor sampling frequency, i.e.

**Definition** sensor.h:301

[SENSOR\_ATTR\_FULL\_SCALE](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bad30df3100fb6b285a6a786fdc77234d3)

@ SENSOR\_ATTR\_FULL\_SCALE

Sensor range, in SI units.

**Definition** sensor.h:318

[SENSOR\_ATTR\_LOWER\_THRESH](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940baee644485ab5f64e7c5273bbe562deaaa)

@ SENSOR\_ATTR\_LOWER\_THRESH

Lower threshold for trigger.

**Definition** sensor.h:303

[SENSOR\_ATTR\_SLOPE\_DUR](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940baf510b32b2e2395bbcf1c8fd7159ed2a1)

@ SENSOR\_ATTR\_SLOPE\_DUR

Duration for which the slope values needs to be outside the threshold for the trigger to fire.

**Definition** sensor.h:312

[SENSOR\_ATTR\_MAX](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940baf6bd0b33ca2117ef329692c291f6384b)

@ SENSOR\_ATTR\_MAX

Maximum value describing a sensor attribute type.

**Definition** sensor.h:361

[SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)

@ SENSOR\_ATTR\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:356

[SENSOR\_STREAM\_DATA\_INCLUDE](group__sensor__interface.md#gga8613a20521a37d40fd7371dc63ba2daca2ba3554a08bf55b64da40900592be315)

@ SENSOR\_STREAM\_DATA\_INCLUDE

Include whatever data is associated with the trigger.

**Definition** sensor.h:601

[SENSOR\_STREAM\_DATA\_NOP](group__sensor__interface.md#gga8613a20521a37d40fd7371dc63ba2daca7e897c6d1428ff50f98140ed4cd4d35d)

@ SENSOR\_STREAM\_DATA\_NOP

Do nothing with the associated trigger data, it may be consumed later.

**Definition** sensor.h:603

[SENSOR\_STREAM\_DATA\_DROP](group__sensor__interface.md#gga8613a20521a37d40fd7371dc63ba2dacaa13c6d3bae87c16f9cd89e0fe7144f8e)

@ SENSOR\_STREAM\_DATA\_DROP

Flush/clear whatever data is associated with the trigger.

**Definition** sensor.h:605

[SENSOR\_CHAN\_GAUGE\_STATE\_OF\_HEALTH](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a0613c39397f06d11f4350f8cbcc24cf6)

@ SENSOR\_CHAN\_GAUGE\_STATE\_OF\_HEALTH

State of health measurement in %.

**Definition** sensor.h:182

[SENSOR\_CHAN\_PM\_1\_0](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a08f0c21c33008292b0b58defe5c06815)

@ SENSOR\_CHAN\_PM\_1\_0

1.0 micro-meters Particulate Matter, in ug/m^3

**Definition** sensor.h:113

[SENSOR\_CHAN\_DIE\_TEMP](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a0a8828f51fe15335ad857d136f197ee1)

@ SENSOR\_CHAN\_DIE\_TEMP

Device die temperature in degrees Celsius.

**Definition** sensor.h:87

[SENSOR\_CHAN\_PRESS](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a14cd68844542e23d1b641a2bc54132a9)

@ SENSOR\_CHAN\_PRESS

Pressure in kilopascal.

**Definition** sensor.h:91

[SENSOR\_CHAN\_GAUGE\_TIME\_TO\_FULL](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a14d4c802805e1e07c9b4e47ccaff0eeb)

@ SENSOR\_CHAN\_GAUGE\_TIME\_TO\_FULL

Time to full in minutes.

**Definition** sensor.h:186

[SENSOR\_CHAN\_ACCEL\_XYZ](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a16c05784ae15a4952ea708c2f11a2ae9)

@ SENSOR\_CHAN\_ACCEL\_XYZ

Acceleration on the X, Y and Z axes.

**Definition** sensor.h:69

[SENSOR\_CHAN\_MAGN\_X](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a171f37ba152d34f75ff745cb848b3240)

@ SENSOR\_CHAN\_MAGN\_X

Magnetic field on the X axis, in Gauss.

**Definition** sensor.h:79

[SENSOR\_CHAN\_O2](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a17bcfa0e34eecf45e17988720471c8f9)

@ SENSOR\_CHAN\_O2

O2 level, in parts per million (ppm).

**Definition** sensor.h:124

[SENSOR\_CHAN\_CURRENT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a1a001ba3ca5ad37308fb7be81f11c950)

@ SENSOR\_CHAN\_CURRENT

Current, in amps.

**Definition** sensor.h:137

[SENSOR\_CHAN\_GYRO\_XYZ](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a1d36b89ab3761e9bc86effc839f8db0e)

@ SENSOR\_CHAN\_GYRO\_XYZ

Angular velocity around the X, Y and Z axes.

**Definition** sensor.h:77

[SENSOR\_CHAN\_VSHUNT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a1ea01c780995ad4539e9ffc2ca6102e9)

@ SENSOR\_CHAN\_VSHUNT

Current Shunt Voltage in milli-volts.

**Definition** sensor.h:134

[SENSOR\_CHAN\_GREEN](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a216a3b2b77d7a92f94547aeb889ae378)

@ SENSOR\_CHAN\_GREEN

Illuminance in green spectrum, in lux.

**Definition** sensor.h:106

[SENSOR\_CHAN\_MAGN\_Z](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a2a2115051ded019a57ece5a00f86ea61)

@ SENSOR\_CHAN\_MAGN\_Z

Magnetic field on the Z axis, in Gauss.

**Definition** sensor.h:83

[SENSOR\_CHAN\_MAGN\_Y](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a2b4f1764f47428c528447347d7730942)

@ SENSOR\_CHAN\_MAGN\_Y

Magnetic field on the Y axis, in Gauss.

**Definition** sensor.h:81

[SENSOR\_CHAN\_GAUGE\_DESIRED\_VOLTAGE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a2c33a7f11d5b3996e95167698a2056cf)

@ SENSOR\_CHAN\_GAUGE\_DESIRED\_VOLTAGE

Desired voltage of cell in V (nominal voltage).

**Definition** sensor.h:192

[SENSOR\_CHAN\_POWER](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a33607371060fca93c3555e8e10d5b177)

@ SENSOR\_CHAN\_POWER

Power in watts.

**Definition** sensor.h:139

[SENSOR\_CHAN\_PM\_2\_5](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a3398fdc51964aa06c9a01096d2fac945)

@ SENSOR\_CHAN\_PM\_2\_5

2.5 micro-meters Particulate Matter, in ug/m^3

**Definition** sensor.h:115

[SENSOR\_CHAN\_RESISTANCE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a34ba555026ff976881142512cc8a616b)

@ SENSOR\_CHAN\_RESISTANCE

Resistance , in Ohm.

**Definition** sensor.h:142

[SENSOR\_CHAN\_GAUGE\_AVG\_CURRENT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a4272c1256cde47006d424c5523d26bf8)

@ SENSOR\_CHAN\_GAUGE\_AVG\_CURRENT

Average current, in amps.

**Definition** sensor.h:162

[SENSOR\_CHAN\_GYRO\_Y](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a4a9533172105fd2e55d96e0122a48847)

@ SENSOR\_CHAN\_GYRO\_Y

Angular velocity around the Y axis, in radians/s.

**Definition** sensor.h:73

[SENSOR\_CHAN\_GAUGE\_DESIRED\_CHARGING\_CURRENT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a4aa8bba1b260e1994542383d8e2e908f)

@ SENSOR\_CHAN\_GAUGE\_DESIRED\_CHARGING\_CURRENT

Desired charging current in mA.

**Definition** sensor.h:194

[SENSOR\_CHAN\_GAUGE\_FULL\_CHARGE\_CAPACITY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a54a6be68e09b9f8ca4d349e3d1445649)

@ SENSOR\_CHAN\_GAUGE\_FULL\_CHARGE\_CAPACITY

Full Charge Capacity in mAh.

**Definition** sensor.h:172

[SENSOR\_CHAN\_ROTATION](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a551ffe08a9b1206e3c051f207b92aabf)

@ SENSOR\_CHAN\_ROTATION

Angular rotation, in degrees.

**Definition** sensor.h:145

[SENSOR\_CHAN\_AMBIENT\_TEMP](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a5bf9c4a677405c4a4df3bc3acd116c7c)

@ SENSOR\_CHAN\_AMBIENT\_TEMP

Ambient temperature in degrees Celsius.

**Definition** sensor.h:89

[SENSOR\_CHAN\_MAGN\_XYZ](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a5d1f48466f6f600503af18427fa3da32)

@ SENSOR\_CHAN\_MAGN\_XYZ

Magnetic field on the X, Y and Z axes.

**Definition** sensor.h:85

[SENSOR\_CHAN\_GAUGE\_STDBY\_CURRENT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a5e6b87cacfe3e4703b963a2177d35cc8)

@ SENSOR\_CHAN\_GAUGE\_STDBY\_CURRENT

Standby current, in amps.

**Definition** sensor.h:164

[SENSOR\_CHAN\_GAUGE\_MAX\_LOAD\_CURRENT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a603335f6a91846c5089a2a541d9053cf)

@ SENSOR\_CHAN\_GAUGE\_MAX\_LOAD\_CURRENT

Max load current, in amps.

**Definition** sensor.h:166

[SENSOR\_CHAN\_ACCEL\_Y](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a61c145468f01916c1a547fb38a1be9a8)

@ SENSOR\_CHAN\_ACCEL\_Y

Acceleration on the Y axis, in m/s^2.

**Definition** sensor.h:65

[SENSOR\_CHAN\_RPM](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a655a576a72cbd6641abc698a3f4304d1)

@ SENSOR\_CHAN\_RPM

Revolutions per minute, in RPM.

**Definition** sensor.h:157

[SENSOR\_CHAN\_GAUGE\_FULL\_AVAIL\_CAPACITY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a688287fa1587944424a2eda13b8d98e8)

@ SENSOR\_CHAN\_GAUGE\_FULL\_AVAIL\_CAPACITY

Full Available Capacity in mAh.

**Definition** sensor.h:178

[SENSOR\_CHAN\_VOLTAGE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a69dd8a737a0cb6f03fa5f60c92840e6d)

@ SENSOR\_CHAN\_VOLTAGE

Voltage, in volts.

**Definition** sensor.h:131

[SENSOR\_CHAN\_BLUE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a6e66f95d73d05c2b3511e2db506844f5)

@ SENSOR\_CHAN\_BLUE

Illuminance in blue spectrum, in lux.

**Definition** sensor.h:108

[SENSOR\_CHAN\_LIGHT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a6e91196c11d080c3f5df55fda190e19d)

@ SENSOR\_CHAN\_LIGHT

Illuminance in visible spectrum, in lux.

**Definition** sensor.h:100

[SENSOR\_CHAN\_GAUGE\_DESIGN\_VOLTAGE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a6f96ba4db6cf812b223f9a09f2a287d0)

@ SENSOR\_CHAN\_GAUGE\_DESIGN\_VOLTAGE

Design voltage of cell in V (max voltage).

**Definition** sensor.h:190

[SENSOR\_CHAN\_ACCEL\_Z](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a78e06bb48cfe06e42829816ad4cb5a0f)

@ SENSOR\_CHAN\_ACCEL\_Z

Acceleration on the Z axis, in m/s^2.

**Definition** sensor.h:67

[SENSOR\_CHAN\_CO2](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a7a23e3e869c5e9a39f6a7bfa28737133)

@ SENSOR\_CHAN\_CO2

CO2 level, in parts per million (ppm).

**Definition** sensor.h:122

[SENSOR\_CHAN\_GAUGE\_STATE\_OF\_CHARGE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a7d67d6842ee787fcc8a4d9ee2cbea139)

@ SENSOR\_CHAN\_GAUGE\_STATE\_OF\_CHARGE

State of charge measurement in %.

**Definition** sensor.h:170

[SENSOR\_CHAN\_POS\_DXYZ](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a81fe5eca365c048c5a112071b7aca740)

@ SENSOR\_CHAN\_POS\_DXYZ

Position change on the X, Y and Z axis, in points.

**Definition** sensor.h:154

[SENSOR\_CHAN\_GAUGE\_CYCLE\_COUNT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a8834978858c2b62b5e923d06cfcb1a46)

@ SENSOR\_CHAN\_GAUGE\_CYCLE\_COUNT

Cycle count (total number of charge/discharge cycles).

**Definition** sensor.h:188

[SENSOR\_CHAN\_GAUGE\_TEMP](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a8cac65c812b3a1fcb55a53f18d827214)

@ SENSOR\_CHAN\_GAUGE\_TEMP

Gauge temperature.

**Definition** sensor.h:168

[SENSOR\_CHAN\_POS\_DY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a974327ca88ea6d22731cd03afeacef76)

@ SENSOR\_CHAN\_POS\_DY

Position change on the Y axis, in points.

**Definition** sensor.h:150

[SENSOR\_CHAN\_GYRO\_Z](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a9b6b9d13cd8d82449823d65779a87a39)

@ SENSOR\_CHAN\_GYRO\_Z

Angular velocity around the Z axis, in radians/s.

**Definition** sensor.h:75

[SENSOR\_CHAN\_POS\_DX](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aa00b7a857e33c925c910661a91389517)

@ SENSOR\_CHAN\_POS\_DX

Position change on the X axis, in points.

**Definition** sensor.h:148

[SENSOR\_CHAN\_GAUGE\_AVG\_POWER](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aa24f9e12f20a716dd152cf889cb51228)

@ SENSOR\_CHAN\_GAUGE\_AVG\_POWER

Average power in mW.

**Definition** sensor.h:180

[SENSOR\_CHAN\_GAUGE\_TIME\_TO\_EMPTY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aa3755e9fcd8c90fef5185082edb29b65)

@ SENSOR\_CHAN\_GAUGE\_TIME\_TO\_EMPTY

Time to empty in minutes.

**Definition** sensor.h:184

[SENSOR\_CHAN\_PM\_10](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aa450541bde278aefcc9b53bd0826e225)

@ SENSOR\_CHAN\_PM\_10

10 micro-meters Particulate Matter, in ug/m^3

**Definition** sensor.h:117

[SENSOR\_CHAN\_GAUGE\_REMAINING\_CHARGE\_CAPACITY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aaaea6433c82f7b563f86fa53c95ad0ad)

@ SENSOR\_CHAN\_GAUGE\_REMAINING\_CHARGE\_CAPACITY

Remaining Charge Capacity in mAh.

**Definition** sensor.h:174

[SENSOR\_CHAN\_ALL](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ab275027eb550b2b075c44917634eca2c)

@ SENSOR\_CHAN\_ALL

All channels.

**Definition** sensor.h:197

[SENSOR\_CHAN\_GAUGE\_VOLTAGE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ab942649ce1507fb081a77b4bcfc1a57d)

@ SENSOR\_CHAN\_GAUGE\_VOLTAGE

Voltage, in volts.

**Definition** sensor.h:160

[SENSOR\_CHAN\_PROX](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934abaec2c1347ef0035221dd4d9c34a4774)

@ SENSOR\_CHAN\_PROX

Proximity.

**Definition** sensor.h:96

[SENSOR\_CHAN\_COMMON\_COUNT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934abb2893ccb71c9e1eeb155d7cbd539303)

@ SENSOR\_CHAN\_COMMON\_COUNT

Number of all common sensor channels.

**Definition** sensor.h:202

[SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12)

@ SENSOR\_CHAN\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:208

[SENSOR\_CHAN\_GYRO\_X](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac5709b77f0eb69972ccc055f927e5015)

@ SENSOR\_CHAN\_GYRO\_X

Angular velocity around the X axis, in radians/s.

**Definition** sensor.h:71

[SENSOR\_CHAN\_GAS\_RES](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934acf250a87d2d175f99179a5b54cb7ba01)

@ SENSOR\_CHAN\_GAS\_RES

Gas sensor resistance in ohms.

**Definition** sensor.h:128

[SENSOR\_CHAN\_HUMIDITY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ad08ddb6c9cd71c853a121f426fcea042)

@ SENSOR\_CHAN\_HUMIDITY

Humidity, in percent.

**Definition** sensor.h:98

[SENSOR\_CHAN\_DISTANCE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ad46d1495990a86fa7e2ab5bbe5338e08)

@ SENSOR\_CHAN\_DISTANCE

Distance.

**Definition** sensor.h:119

[SENSOR\_CHAN\_IR](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ad725fe5778f000a17f93f83dab31132c)

@ SENSOR\_CHAN\_IR

Illuminance in infra-red spectrum, in lux.

**Definition** sensor.h:102

[SENSOR\_CHAN\_MAX](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ad842035a01166417d90cd5d7630733b1)

@ SENSOR\_CHAN\_MAX

Maximum value describing a sensor channel type.

**Definition** sensor.h:213

[SENSOR\_CHAN\_POS\_DZ](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aeaf49aa075947a160f21ae19cf8c39b9)

@ SENSOR\_CHAN\_POS\_DZ

Position change on the Z axis, in points.

**Definition** sensor.h:152

[SENSOR\_CHAN\_RED](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934af22c8ef66f4871efe5a22863d7f434aa)

@ SENSOR\_CHAN\_RED

Illuminance in red spectrum, in lux.

**Definition** sensor.h:104

[SENSOR\_CHAN\_ALTITUDE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934af5ba63bfef1c64c8a96ae7fba4f35512)

@ SENSOR\_CHAN\_ALTITUDE

Altitude, in meters.

**Definition** sensor.h:110

[SENSOR\_CHAN\_GAUGE\_NOM\_AVAIL\_CAPACITY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934af9b0ac69fd87a68e7e8d97e52b41304a)

@ SENSOR\_CHAN\_GAUGE\_NOM\_AVAIL\_CAPACITY

Nominal Available Capacity in mAh.

**Definition** sensor.h:176

[SENSOR\_CHAN\_ACCEL\_X](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934afa9238082f000350530ca77b2f513d4c)

@ SENSOR\_CHAN\_ACCEL\_X

Acceleration on the X axis, in m/s^2.

**Definition** sensor.h:63

[SENSOR\_CHAN\_VOC](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934affee34c60c95398b67ec59644d647f8e)

@ SENSOR\_CHAN\_VOC

VOC level, in parts per billion (ppb).

**Definition** sensor.h:126

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:124

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5)

#define ENOMEM

Not enough core.

**Definition** errno.h:50

[ERANGE](group__system__errno.md#gaa1591a4f3a86360108de5b9ba34980ca)

#define ERANGE

Result too large.

**Definition** errno.h:72

[types.h](include_2zephyr_2dsp_2types_8h.md)

[types.h](include_2zephyr_2types_8h.md)

[size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9)

Size of off\_t must be equal or less than size of size\_t

**Definition** retained\_mem.h:28

[rtio.h](rtio_2rtio_8h.md)

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

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

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

**Definition** device.h:403

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:409

[rtio\_cqe](structrtio__cqe.md)

A completion queue event.

**Definition** rtio.h:294

[rtio\_cqe::userdata](structrtio__cqe.md#a15128387ccbea55812ef229eab7241e7)

void \* userdata

Associated userdata with operation.

**Definition** rtio.h:298

[rtio\_cqe::result](structrtio__cqe.md#acbe2e6607a752b676d9336b9ca6ce435)

int32\_t result

Result from operation.

**Definition** rtio.h:297

[rtio\_iodev\_api](structrtio__iodev__api.md)

API that an RTIO IO device should implement.

**Definition** rtio.h:433

[rtio\_iodev\_sqe](structrtio__iodev__sqe.md)

Compute the mempool block index for a given pointer.

**Definition** rtio.h:423

[rtio\_iodev\_sqe::sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b)

struct rtio\_sqe sqe

**Definition** rtio.h:424

[rtio\_iodev](structrtio__iodev.md)

An IO device with a function table for submitting requests.

**Definition** rtio.h:448

[rtio\_iodev::data](structrtio__iodev.md#af0f3a27fe8dea2161c9a73cb838bdeec)

void \* data

**Definition** rtio.h:453

[rtio\_sqe](structrtio__sqe.md)

A submission queue event.

**Definition** rtio.h:232

[rtio\_sqe::userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971)

void \* userdata

User provided data which is returned upon operation completion.

**Definition** rtio.h:252

[rtio\_sqe::buf](structrtio__sqe.md#a55e98f27b26393fee8e179b7bdb6a52e)

uint8\_t \* buf

Buffer to use.

**Definition** rtio.h:259

[rtio\_sqe::buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722)

uint32\_t buf\_len

Length of buffer.

**Definition** rtio.h:258

[rtio\_sqe::iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc)

const struct rtio\_iodev \* iodev

Device to operation on.

**Definition** rtio.h:243

[rtio](structrtio.md)

An RTIO context containing what can be viewed as a pair of queues.

**Definition** rtio.h:327

[sensor\_chan\_spec](structsensor__chan__spec.md)

Sensor Channel Specification.

**Definition** sensor.h:431

[sensor\_chan\_spec::chan\_idx](structsensor__chan__spec.md#a00d4a927cfeae33b2beea8cdc415dda1)

uint16\_t chan\_idx

A sensor channel index.

**Definition** sensor.h:433

[sensor\_chan\_spec::chan\_type](structsensor__chan__spec.md#a1b2f0ecdc23e0d235536eb5fcdeeb63c)

uint16\_t chan\_type

A sensor channel type.

**Definition** sensor.h:432

[sensor\_data\_generic\_header](structsensor__data__generic__header.md)

**Definition** sensor.h:909

[sensor\_data\_generic\_header::timestamp\_ns](structsensor__data__generic__header.md#a429e22b3191df271ccfe321b796e1ac9)

uint64\_t timestamp\_ns

**Definition** sensor.h:911

[sensor\_data\_generic\_header::shift](structsensor__data__generic__header.md#a68067521c1058b6802176e1d48fed788)

int8\_t shift

**Definition** sensor.h:920

[sensor\_data\_generic\_header::num\_channels](structsensor__data__generic__header.md#a7edbe674f28c95f3aa40b1df84ca61fe)

uint32\_t num\_channels

**Definition** sensor.h:917

[sensor\_data\_generic\_header::channels](structsensor__data__generic__header.md#ac09f23959c66ff75b0854a95e8d4504b)

struct sensor\_chan\_spec channels[0]

**Definition** sensor.h:926

[sensor\_decode\_context](structsensor__decode__context.md)

Used for iterating over the data frames via the sensor\_decoder\_api.

**Definition** sensor.h:553

[sensor\_decode\_context::decoder](structsensor__decode__context.md#a1ac0773e83a086455371d108264ef4f6)

const struct sensor\_decoder\_api \* decoder

**Definition** sensor.h:554

[sensor\_decode\_context::channel](structsensor__decode__context.md#a1c051bd8d0030f81cc561e32b2897d74)

struct sensor\_chan\_spec channel

**Definition** sensor.h:556

[sensor\_decode\_context::buffer](structsensor__decode__context.md#a23e27eb0687d722be78e1b89278613d1)

const uint8\_t \* buffer

**Definition** sensor.h:555

[sensor\_decode\_context::fit](structsensor__decode__context.md#ada9e40625829093087886c41f2fb7350)

uint32\_t fit

**Definition** sensor.h:557

[sensor\_decoder\_api](structsensor__decoder__api.md)

Decodes a single raw data buffer.

**Definition** sensor.h:463

[sensor\_decoder\_api::get\_size\_info](structsensor__decoder__api.md#a026be8086386e9eea0a1cb25c1cd602e)

int(\* get\_size\_info)(struct sensor\_chan\_spec channel, size\_t \*base\_size, size\_t \*frame\_size)

Get the size required to decode a given channel.

**Definition** sensor.h:488

[sensor\_decoder\_api::get\_frame\_count](structsensor__decoder__api.md#a16c0b0f1a3a13d037b9ffcbf348da1f5)

int(\* get\_frame\_count)(const uint8\_t \*buffer, struct sensor\_chan\_spec channel, uint16\_t \*frame\_count)

Get the number of frames in the current buffer.

**Definition** sensor.h:473

[sensor\_decoder\_api::decode](structsensor__decoder__api.md#a1d24e69b5c2f0c41ce175de2aa2618db)

int(\* decode)(const uint8\_t \*buffer, struct sensor\_chan\_spec channel, uint32\_t \*fit, uint16\_t max\_count, void \*data\_out)

Decode up to max\_count samples from the buffer.

**Definition** sensor.h:516

[sensor\_decoder\_api::has\_trigger](structsensor__decoder__api.md#a78706bae0f1314615b5804736ef43493)

bool(\* has\_trigger)(const uint8\_t \*buffer, enum sensor\_trigger\_type trigger)

Check if the given trigger type is present.

**Definition** sensor.h:526

[sensor\_driver\_api](structsensor__driver__api.md)

**Definition** sensor.h:698

[sensor\_driver\_api::get\_decoder](structsensor__driver__api.md#a004f9d342805dc72249ab9b8c17a544b)

sensor\_get\_decoder\_t get\_decoder

**Definition** sensor.h:704

[sensor\_driver\_api::attr\_set](structsensor__driver__api.md#a2d230a976b19a699d132034f58bb2b6a)

sensor\_attr\_set\_t attr\_set

**Definition** sensor.h:699

[sensor\_driver\_api::attr\_get](structsensor__driver__api.md#a3e28950f844c3f8b8da5ba9ff8052e46)

sensor\_attr\_get\_t attr\_get

**Definition** sensor.h:700

[sensor\_driver\_api::trigger\_set](structsensor__driver__api.md#a4708070fd6654ecbbe631819aba319bd)

sensor\_trigger\_set\_t trigger\_set

**Definition** sensor.h:701

[sensor\_driver\_api::sample\_fetch](structsensor__driver__api.md#a4b40e25b81fe070e2f6bdcf7f8a4a31f)

sensor\_sample\_fetch\_t sample\_fetch

**Definition** sensor.h:702

[sensor\_driver\_api::channel\_get](structsensor__driver__api.md#a667b41bf51f2c7a6bb31713fbf889113)

sensor\_channel\_get\_t channel\_get

**Definition** sensor.h:703

[sensor\_driver\_api::submit](structsensor__driver__api.md#ae3ba0adeba21351e8f660896e5a0e702)

sensor\_submit\_t submit

**Definition** sensor.h:705

[sensor\_read\_config](structsensor__read__config.md)

**Definition** sensor.h:622

[sensor\_read\_config::channels](structsensor__read__config.md#a2aff44f02b25fd4ad1d4bc217800fad1)

struct sensor\_chan\_spec \*const channels

**Definition** sensor.h:626

[sensor\_read\_config::count](structsensor__read__config.md#a5236049e0563ebba754994d70e22383a)

size\_t count

**Definition** sensor.h:629

[sensor\_read\_config::triggers](structsensor__read__config.md#a6eaa6df7bc9378abe0f5b4b8c9a05909)

struct sensor\_stream\_trigger \*const triggers

**Definition** sensor.h:627

[sensor\_read\_config::is\_streaming](structsensor__read__config.md#aca96de2c23fb63f887c4c40dcb272798)

const bool is\_streaming

**Definition** sensor.h:624

[sensor\_read\_config::sensor](structsensor__read__config.md#ad49d5ab5293017d1ad2cf60adc542090)

const struct device \* sensor

**Definition** sensor.h:623

[sensor\_read\_config::max](structsensor__read__config.md#aecb9c899e292fdb25c3c990bdaf1c76b)

const size\_t max

**Definition** sensor.h:630

[sensor\_stream\_trigger](structsensor__stream__trigger.md)

**Definition** sensor.h:608

[sensor\_stream\_trigger::opt](structsensor__stream__trigger.md#a62ccdecf7253b1bfdff4f1d659563d76)

enum sensor\_stream\_data\_opt opt

**Definition** sensor.h:610

[sensor\_stream\_trigger::trigger](structsensor__stream__trigger.md#a9a367e746764e68140ec9120f2a016e6)

enum sensor\_trigger\_type trigger

**Definition** sensor.h:609

[sensor\_trigger](structsensor__trigger.md)

Sensor trigger spec.

**Definition** sensor.h:286

[sensor\_trigger::type](structsensor__trigger.md#ac2cce1ec6ff82f95cb06d0dccafd7af0)

enum sensor\_trigger\_type type

Trigger type.

**Definition** sensor.h:288

[sensor\_trigger::chan](structsensor__trigger.md#ae01f99b124aa99c59b9967818022e112)

enum sensor\_channel chan

Channel the trigger is set on.

**Definition** sensor.h:290

[sensor\_value](structsensor__value.md)

Representation of a sensor readout value.

**Definition** sensor.h:51

[sensor\_value::val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b)

int32\_t val2

Fractional part of the value (in one-millionth parts).

**Definition** sensor.h:55

[sensor\_value::val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe)

int32\_t val1

Integer part of the value.

**Definition** sensor.h:53

[iterable\_sections.h](sys_2iterable__sections_8h.md)

[INT64\_C](xcc_8h.md#a93d102802b35d3b8abae9bbe7f0fed75)

#define INT64\_C(x)

**Definition** xcc.h:90

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor.h](sensor_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
