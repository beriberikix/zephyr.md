---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/sensor_8h_source.html
original_path: doxygen/html/sensor_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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

[ 160](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a4b5a3a92ce610a2b3c9f113c93aef212) [SENSOR\_CHAN\_FREQUENCY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a4b5a3a92ce610a2b3c9f113c93aef212),

161

[ 163](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ab942649ce1507fb081a77b4bcfc1a57d) [SENSOR\_CHAN\_GAUGE\_VOLTAGE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ab942649ce1507fb081a77b4bcfc1a57d),

[ 165](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a4272c1256cde47006d424c5523d26bf8) [SENSOR\_CHAN\_GAUGE\_AVG\_CURRENT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a4272c1256cde47006d424c5523d26bf8),

[ 167](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a5e6b87cacfe3e4703b963a2177d35cc8) [SENSOR\_CHAN\_GAUGE\_STDBY\_CURRENT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a5e6b87cacfe3e4703b963a2177d35cc8),

[ 169](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a603335f6a91846c5089a2a541d9053cf) [SENSOR\_CHAN\_GAUGE\_MAX\_LOAD\_CURRENT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a603335f6a91846c5089a2a541d9053cf),

[ 171](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a8cac65c812b3a1fcb55a53f18d827214) [SENSOR\_CHAN\_GAUGE\_TEMP](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a8cac65c812b3a1fcb55a53f18d827214),

[ 173](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a7d67d6842ee787fcc8a4d9ee2cbea139) [SENSOR\_CHAN\_GAUGE\_STATE\_OF\_CHARGE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a7d67d6842ee787fcc8a4d9ee2cbea139),

[ 175](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a54a6be68e09b9f8ca4d349e3d1445649) [SENSOR\_CHAN\_GAUGE\_FULL\_CHARGE\_CAPACITY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a54a6be68e09b9f8ca4d349e3d1445649),

[ 177](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aaaea6433c82f7b563f86fa53c95ad0ad) [SENSOR\_CHAN\_GAUGE\_REMAINING\_CHARGE\_CAPACITY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aaaea6433c82f7b563f86fa53c95ad0ad),

[ 179](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934af9b0ac69fd87a68e7e8d97e52b41304a) [SENSOR\_CHAN\_GAUGE\_NOM\_AVAIL\_CAPACITY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934af9b0ac69fd87a68e7e8d97e52b41304a),

[ 181](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a688287fa1587944424a2eda13b8d98e8) [SENSOR\_CHAN\_GAUGE\_FULL\_AVAIL\_CAPACITY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a688287fa1587944424a2eda13b8d98e8),

[ 183](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aa24f9e12f20a716dd152cf889cb51228) [SENSOR\_CHAN\_GAUGE\_AVG\_POWER](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aa24f9e12f20a716dd152cf889cb51228),

[ 185](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a0613c39397f06d11f4350f8cbcc24cf6) [SENSOR\_CHAN\_GAUGE\_STATE\_OF\_HEALTH](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a0613c39397f06d11f4350f8cbcc24cf6),

[ 187](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aa3755e9fcd8c90fef5185082edb29b65) [SENSOR\_CHAN\_GAUGE\_TIME\_TO\_EMPTY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aa3755e9fcd8c90fef5185082edb29b65),

[ 189](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a14d4c802805e1e07c9b4e47ccaff0eeb) [SENSOR\_CHAN\_GAUGE\_TIME\_TO\_FULL](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a14d4c802805e1e07c9b4e47ccaff0eeb),

[ 191](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a8834978858c2b62b5e923d06cfcb1a46) [SENSOR\_CHAN\_GAUGE\_CYCLE\_COUNT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a8834978858c2b62b5e923d06cfcb1a46),

[ 193](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a6f96ba4db6cf812b223f9a09f2a287d0) [SENSOR\_CHAN\_GAUGE\_DESIGN\_VOLTAGE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a6f96ba4db6cf812b223f9a09f2a287d0),

[ 195](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a2c33a7f11d5b3996e95167698a2056cf) [SENSOR\_CHAN\_GAUGE\_DESIRED\_VOLTAGE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a2c33a7f11d5b3996e95167698a2056cf),

[ 197](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a4aa8bba1b260e1994542383d8e2e908f) [SENSOR\_CHAN\_GAUGE\_DESIRED\_CHARGING\_CURRENT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a4aa8bba1b260e1994542383d8e2e908f),

[ 199](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a3905467a96940ada0dbdef6ff8ee1a8a) [SENSOR\_CHAN\_GAME\_ROTATION\_VECTOR](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a3905467a96940ada0dbdef6ff8ee1a8a),

[ 201](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a26fe67f0313062c6bf841ff8b829f7ff) [SENSOR\_CHAN\_GRAVITY\_VECTOR](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a26fe67f0313062c6bf841ff8b829f7ff),

[ 203](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a88001b6464b2419dbf2aa4ad59556110) [SENSOR\_CHAN\_GBIAS\_XYZ](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a88001b6464b2419dbf2aa4ad59556110),

204

[ 206](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ab275027eb550b2b075c44917634eca2c) [SENSOR\_CHAN\_ALL](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ab275027eb550b2b075c44917634eca2c),

207

[ 211](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934abb2893ccb71c9e1eeb155d7cbd539303) [SENSOR\_CHAN\_COMMON\_COUNT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934abb2893ccb71c9e1eeb155d7cbd539303),

212

[ 217](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12) [SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12) = [SENSOR\_CHAN\_COMMON\_COUNT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934abb2893ccb71c9e1eeb155d7cbd539303),

218

[ 222](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ad842035a01166417d90cd5d7630733b1) [SENSOR\_CHAN\_MAX](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ad842035a01166417d90cd5d7630733b1) = [INT16\_MAX](stdint_8h.md#ac58f2c111cc9989c86db2a7dc4fd84ca),

223};

224

[ 228](group__sensor__interface.md#ga08215279400e8c9eb05ce4e4f0898ffd)enum [sensor\_trigger\_type](group__sensor__interface.md#ga08215279400e8c9eb05ce4e4f0898ffd) {

[ 233](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdabf92b196394726ec90f1d61586a7f023) [SENSOR\_TRIG\_TIMER](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdabf92b196394726ec90f1d61586a7f023),

[ 235](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdaf7c161e309c267a7dd6daf2ad176f44f) [SENSOR\_TRIG\_DATA\_READY](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdaf7c161e309c267a7dd6daf2ad176f44f),

[ 244](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda3bb90a3334bcf613c9efbdf2ed05f855) [SENSOR\_TRIG\_DELTA](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda3bb90a3334bcf613c9efbdf2ed05f855),

[ 246](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda448226d83b28c2862c353a8cda7be0d5) [SENSOR\_TRIG\_NEAR\_FAR](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda448226d83b28c2862c353a8cda7be0d5),

[ 253](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda8f875f881b6540eebc28e3d6a7d46606) [SENSOR\_TRIG\_THRESHOLD](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda8f875f881b6540eebc28e3d6a7d46606),

254

[ 256](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdae49a25e6400f0753f6bac8a7d136200d) [SENSOR\_TRIG\_TAP](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdae49a25e6400f0753f6bac8a7d136200d),

257

[ 259](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdab95e52584a6bc3343181f495cd4cb2ef) [SENSOR\_TRIG\_DOUBLE\_TAP](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdab95e52584a6bc3343181f495cd4cb2ef),

260

[ 262](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda4943ffb4afaf4cbae39e85693bd4374c) [SENSOR\_TRIG\_FREEFALL](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda4943ffb4afaf4cbae39e85693bd4374c),

263

[ 265](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda7095387831b763b34171287945dae276) [SENSOR\_TRIG\_MOTION](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda7095387831b763b34171287945dae276),

266

[ 268](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda79e286ffced716e1076f56464ea47f5d) [SENSOR\_TRIG\_STATIONARY](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda79e286ffced716e1076f56464ea47f5d),

269

[ 271](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdac5d67fb4fb6206465b1b01dc78245fe4) [SENSOR\_TRIG\_FIFO\_WATERMARK](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdac5d67fb4fb6206465b1b01dc78245fe4),

272

[ 274](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda66f913f8751a77a6c16745e329c7315c) [SENSOR\_TRIG\_FIFO\_FULL](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda66f913f8751a77a6c16745e329c7315c),

[ 278](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda8d1f2621fad4fd685d56cca3f9b042f5) [SENSOR\_TRIG\_COMMON\_COUNT](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda8d1f2621fad4fd685d56cca3f9b042f5),

279

[ 284](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda5e1a94f21fee67ee98296153ea640921) [SENSOR\_TRIG\_PRIV\_START](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda5e1a94f21fee67ee98296153ea640921) = [SENSOR\_TRIG\_COMMON\_COUNT](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda8d1f2621fad4fd685d56cca3f9b042f5),

285

[ 289](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda9de566f44de519f94c59c58df1efc4c4) [SENSOR\_TRIG\_MAX](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda9de566f44de519f94c59c58df1efc4c4) = [INT16\_MAX](stdint_8h.md#ac58f2c111cc9989c86db2a7dc4fd84ca),

290};

291

[ 295](structsensor__trigger.md)struct [sensor\_trigger](structsensor__trigger.md) {

[ 297](structsensor__trigger.md#ac2cce1ec6ff82f95cb06d0dccafd7af0) enum [sensor\_trigger\_type](group__sensor__interface.md#ga08215279400e8c9eb05ce4e4f0898ffd) [type](structsensor__trigger.md#ac2cce1ec6ff82f95cb06d0dccafd7af0);

[ 299](structsensor__trigger.md#ae01f99b124aa99c59b9967818022e112) enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) [chan](structsensor__trigger.md#ae01f99b124aa99c59b9967818022e112);

300};

301

[ 305](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b)enum [sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b) {

[ 310](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bacb07e3508ea5503dbcdceee3f17d2291) [SENSOR\_ATTR\_SAMPLING\_FREQUENCY](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bacb07e3508ea5503dbcdceee3f17d2291),

[ 312](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940baee644485ab5f64e7c5273bbe562deaaa) [SENSOR\_ATTR\_LOWER\_THRESH](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940baee644485ab5f64e7c5273bbe562deaaa),

[ 314](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba5af51bd0640a87a94476eee112a4460b) [SENSOR\_ATTR\_UPPER\_THRESH](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba5af51bd0640a87a94476eee112a4460b),

[ 316](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bac4538665a244cb7f18fc053c40134302) [SENSOR\_ATTR\_SLOPE\_TH](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bac4538665a244cb7f18fc053c40134302),

[ 321](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940baf510b32b2e2395bbcf1c8fd7159ed2a1) [SENSOR\_ATTR\_SLOPE\_DUR](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940baf510b32b2e2395bbcf1c8fd7159ed2a1),

322 /\* Hysteresis for trigger thresholds. \*/

[ 323](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba044e67bfc04e8ddc2de7d2058fffbc94) [SENSOR\_ATTR\_HYSTERESIS](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba044e67bfc04e8ddc2de7d2058fffbc94),

[ 325](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba3d32987f75284d80d3f64bf44f5c6ccd) [SENSOR\_ATTR\_OVERSAMPLING](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba3d32987f75284d80d3f64bf44f5c6ccd),

[ 327](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bad30df3100fb6b285a6a786fdc77234d3) [SENSOR\_ATTR\_FULL\_SCALE](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bad30df3100fb6b285a6a786fdc77234d3),

[ 332](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba332935dcb6f7e228cb9c595a545079fd) [SENSOR\_ATTR\_OFFSET](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba332935dcb6f7e228cb9c595a545079fd),

[ 337](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba3043381b539610a8b424f12d76474bdf) [SENSOR\_ATTR\_CALIB\_TARGET](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba3043381b539610a8b424f12d76474bdf),

[ 339](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba75cd3aca26859fd7c10c83d86e3471e9) [SENSOR\_ATTR\_CONFIGURATION](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba75cd3aca26859fd7c10c83d86e3471e9),

[ 341](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba843d1e79573c634987e5e839ba9e965e) [SENSOR\_ATTR\_CALIBRATION](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba843d1e79573c634987e5e839ba9e965e),

[ 343](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba1f8d2242fa9d63a13c6a48fe3a1cbe52) [SENSOR\_ATTR\_FEATURE\_MASK](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba1f8d2242fa9d63a13c6a48fe3a1cbe52),

[ 345](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940baaedf76e63224adc3fa266d35666e0a3a) [SENSOR\_ATTR\_ALERT](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940baaedf76e63224adc3fa266d35666e0a3a),

[ 351](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba5a62ea6aa7e55efd62ab3f93dcb0593a) [SENSOR\_ATTR\_FF\_DUR](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba5a62ea6aa7e55efd62ab3f93dcb0593a),

352

[ 354](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba3b0cf69c77de55c92129e212bf5b8ced) [SENSOR\_ATTR\_BATCH\_DURATION](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba3b0cf69c77de55c92129e212bf5b8ced),

355 /\* Configure the gain of a sensor. \*/

[ 356](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bac778fe666c284078117b2083779ba7a3) [SENSOR\_ATTR\_GAIN](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bac778fe666c284078117b2083779ba7a3),

357 /\* Configure the resolution of a sensor. \*/

[ 358](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba7f20835b052b1bd6374e56f66e0f285d) [SENSOR\_ATTR\_RESOLUTION](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba7f20835b052b1bd6374e56f66e0f285d),

[ 362](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba99ceedef81217614ada0c8a469f91eb8) [SENSOR\_ATTR\_COMMON\_COUNT](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba99ceedef81217614ada0c8a469f91eb8),

363

[ 368](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3) [SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3) = [SENSOR\_ATTR\_COMMON\_COUNT](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba99ceedef81217614ada0c8a469f91eb8),

369

[ 373](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940baf6bd0b33ca2117ef329692c291f6384b) [SENSOR\_ATTR\_MAX](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940baf6bd0b33ca2117ef329692c291f6384b) = [INT16\_MAX](stdint_8h.md#ac58f2c111cc9989c86db2a7dc4fd84ca),

374};

375

[ 383](group__sensor__interface.md#ga890c1fb6d6974aea22a2d08829a75902)typedef void (\*[sensor\_trigger\_handler\_t](group__sensor__interface.md#ga890c1fb6d6974aea22a2d08829a75902))(const struct [device](structdevice.md) \*dev,

384 const struct [sensor\_trigger](structsensor__trigger.md) \*trigger);

385

[ 392](group__sensor__interface.md#ga38422ace4194a66a9a912a8ef1e088fb)typedef int (\*[sensor\_attr\_set\_t](group__sensor__interface.md#ga38422ace4194a66a9a912a8ef1e088fb))(const struct [device](structdevice.md) \*dev,

393 enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) chan,

394 enum [sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b) attr,

395 const struct [sensor\_value](structsensor__value.md) \*val);

396

[ 403](group__sensor__interface.md#ga00d05c82b46e56dca5f6e8f7f01c31b8)typedef int (\*[sensor\_attr\_get\_t](group__sensor__interface.md#ga00d05c82b46e56dca5f6e8f7f01c31b8))(const struct [device](structdevice.md) \*dev,

404 enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) chan,

405 enum [sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b) attr,

406 struct [sensor\_value](structsensor__value.md) \*val);

407

[ 414](group__sensor__interface.md#gad7f7a3d9e714cc16f23656ca06592aa4)typedef int (\*[sensor\_trigger\_set\_t](group__sensor__interface.md#gad7f7a3d9e714cc16f23656ca06592aa4))(const struct [device](structdevice.md) \*dev,

415 const struct [sensor\_trigger](structsensor__trigger.md) \*trig,

416 [sensor\_trigger\_handler\_t](group__sensor__interface.md#ga890c1fb6d6974aea22a2d08829a75902) handler);

[ 423](group__sensor__interface.md#gacae110a4edb6f29dfb457cb1ea8d68c1)typedef int (\*[sensor\_sample\_fetch\_t](group__sensor__interface.md#gacae110a4edb6f29dfb457cb1ea8d68c1))(const struct [device](structdevice.md) \*dev,

424 enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) chan);

[ 431](group__sensor__interface.md#ga5c9b5ed9097464562004b446856043fd)typedef int (\*[sensor\_channel\_get\_t](group__sensor__interface.md#ga5c9b5ed9097464562004b446856043fd))(const struct [device](structdevice.md) \*dev,

432 enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) chan,

433 struct [sensor\_value](structsensor__value.md) \*val);

434

[ 443](structsensor__chan__spec.md)struct [sensor\_chan\_spec](structsensor__chan__spec.md) {

[ 444](structsensor__chan__spec.md#a1b2f0ecdc23e0d235536eb5fcdeeb63c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [chan\_type](structsensor__chan__spec.md#a1b2f0ecdc23e0d235536eb5fcdeeb63c);

[ 445](structsensor__chan__spec.md#a00d4a927cfeae33b2beea8cdc415dda1) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [chan\_idx](structsensor__chan__spec.md#a00d4a927cfeae33b2beea8cdc415dda1);

446};

447

449/\* Ensure sensor\_chan\_spec is sensibly sized to pass by value \*/

450BUILD\_ASSERT(sizeof(struct [sensor\_chan\_spec](structsensor__chan__spec.md)) <= sizeof([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)),

451 "sensor\_chan\_spec size should be equal or less than the size of a machine word");

453

[ 462](group__sensor__interface.md#gae95715ffea5da18a9593ec2add029824)static inline bool [sensor\_chan\_spec\_eq](group__sensor__interface.md#gae95715ffea5da18a9593ec2add029824)(struct [sensor\_chan\_spec](structsensor__chan__spec.md) chan\_spec0,

463 struct [sensor\_chan\_spec](structsensor__chan__spec.md) chan\_spec1)

464{

465 return chan\_spec0.[chan\_type](structsensor__chan__spec.md#a1b2f0ecdc23e0d235536eb5fcdeeb63c) == chan\_spec1.[chan\_type](structsensor__chan__spec.md#a1b2f0ecdc23e0d235536eb5fcdeeb63c) &&

466 chan\_spec0.[chan\_idx](structsensor__chan__spec.md#a00d4a927cfeae33b2beea8cdc415dda1) == chan\_spec1.[chan\_idx](structsensor__chan__spec.md#a00d4a927cfeae33b2beea8cdc415dda1);

467}

468

[ 475](structsensor__decoder__api.md)struct [sensor\_decoder\_api](structsensor__decoder__api.md) {

[ 485](structsensor__decoder__api.md#a16c0b0f1a3a13d037b9ffcbf348da1f5) int (\*[get\_frame\_count](structsensor__decoder__api.md#a16c0b0f1a3a13d037b9ffcbf348da1f5))(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, struct [sensor\_chan\_spec](structsensor__chan__spec.md) channel,

486 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*frame\_count);

487

[ 500](structsensor__decoder__api.md#a026be8086386e9eea0a1cb25c1cd602e) int (\*[get\_size\_info](structsensor__decoder__api.md#a026be8086386e9eea0a1cb25c1cd602e))(struct [sensor\_chan\_spec](structsensor__chan__spec.md) channel, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*base\_size,

501 size\_t \*frame\_size);

502

[ 528](structsensor__decoder__api.md#a1d24e69b5c2f0c41ce175de2aa2618db) int (\*[decode](structsensor__decoder__api.md#a1d24e69b5c2f0c41ce175de2aa2618db))(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, struct [sensor\_chan\_spec](structsensor__chan__spec.md) channel, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*fit,

529 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) max\_count, void \*data\_out);

530

[ 538](structsensor__decoder__api.md#a78706bae0f1314615b5804736ef43493) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[has\_trigger](structsensor__decoder__api.md#a78706bae0f1314615b5804736ef43493))(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, enum [sensor\_trigger\_type](group__sensor__interface.md#ga08215279400e8c9eb05ce4e4f0898ffd) trigger);

539};

540

[ 565](structsensor__decode__context.md)struct [sensor\_decode\_context](structsensor__decode__context.md) {

[ 566](structsensor__decode__context.md#a1ac0773e83a086455371d108264ef4f6) const struct [sensor\_decoder\_api](structsensor__decoder__api.md) \*[decoder](structsensor__decode__context.md#a1ac0773e83a086455371d108264ef4f6);

[ 567](structsensor__decode__context.md#a23e27eb0687d722be78e1b89278613d1) const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buffer](structsensor__decode__context.md#a23e27eb0687d722be78e1b89278613d1);

[ 568](structsensor__decode__context.md#a1c051bd8d0030f81cc561e32b2897d74) struct [sensor\_chan\_spec](structsensor__chan__spec.md) [channel](structsensor__decode__context.md#a1c051bd8d0030f81cc561e32b2897d74);

[ 569](structsensor__decode__context.md#ada9e40625829093087886c41f2fb7350) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [fit](structsensor__decode__context.md#ada9e40625829093087886c41f2fb7350);

570};

571

[ 575](group__sensor__interface.md#gae69ec503df53d2d5ee417e481f9ac9ea)#define SENSOR\_DECODE\_CONTEXT\_INIT(decoder\_, buffer\_, channel\_type\_, channel\_index\_) \

576 { \

577 .decoder = (decoder\_), \

578 .buffer = (buffer\_), \

579 .channel = {.chan\_type = (channel\_type\_), .chan\_idx = (channel\_index\_)}, \

580 .fit = 0, \

581 }

582

[ 591](group__sensor__interface.md#ga018bca56056ae2558f9e45aeb2fa5f53)static inline int [sensor\_decode](group__sensor__interface.md#ga018bca56056ae2558f9e45aeb2fa5f53)(struct [sensor\_decode\_context](structsensor__decode__context.md) \*ctx, void \*out, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) max\_count)

592{

593 return ctx->[decoder](structsensor__decode__context.md#a1ac0773e83a086455371d108264ef4f6)->[decode](structsensor__decoder__api.md#a1d24e69b5c2f0c41ce175de2aa2618db)(ctx->[buffer](structsensor__decode__context.md#a23e27eb0687d722be78e1b89278613d1), ctx->[channel](structsensor__decode__context.md#a1c051bd8d0030f81cc561e32b2897d74), &ctx->[fit](structsensor__decode__context.md#ada9e40625829093087886c41f2fb7350), max\_count, out);

594}

595

[ 596](group__sensor__interface.md#ga2b045cdbd4d1ca37beed69970093945b)int [sensor\_natively\_supported\_channel\_size\_info](group__sensor__interface.md#ga2b045cdbd4d1ca37beed69970093945b)(struct [sensor\_chan\_spec](structsensor__chan__spec.md) channel, size\_t \*base\_size,

597 size\_t \*frame\_size);

598

[ 605](group__sensor__interface.md#ga21e407d552d140cfb6bfd0d9513c7d42)typedef int (\*[sensor\_get\_decoder\_t](group__sensor__interface.md#ga21e407d552d140cfb6bfd0d9513c7d42))(const struct [device](structdevice.md) \*dev,

606 const struct [sensor\_decoder\_api](structsensor__decoder__api.md) \*\*api);

607

[ 611](group__sensor__interface.md#ga8613a20521a37d40fd7371dc63ba2dac)enum [sensor\_stream\_data\_opt](group__sensor__interface.md#ga8613a20521a37d40fd7371dc63ba2dac) {

[ 613](group__sensor__interface.md#gga8613a20521a37d40fd7371dc63ba2daca2ba3554a08bf55b64da40900592be315) [SENSOR\_STREAM\_DATA\_INCLUDE](group__sensor__interface.md#gga8613a20521a37d40fd7371dc63ba2daca2ba3554a08bf55b64da40900592be315) = 0,

[ 615](group__sensor__interface.md#gga8613a20521a37d40fd7371dc63ba2daca7e897c6d1428ff50f98140ed4cd4d35d) [SENSOR\_STREAM\_DATA\_NOP](group__sensor__interface.md#gga8613a20521a37d40fd7371dc63ba2daca7e897c6d1428ff50f98140ed4cd4d35d) = 1,

[ 617](group__sensor__interface.md#gga8613a20521a37d40fd7371dc63ba2dacaa13c6d3bae87c16f9cd89e0fe7144f8e) [SENSOR\_STREAM\_DATA\_DROP](group__sensor__interface.md#gga8613a20521a37d40fd7371dc63ba2dacaa13c6d3bae87c16f9cd89e0fe7144f8e) = 2,

618};

619

[ 620](structsensor__stream__trigger.md)struct [sensor\_stream\_trigger](structsensor__stream__trigger.md) {

[ 621](structsensor__stream__trigger.md#a9a367e746764e68140ec9120f2a016e6) enum [sensor\_trigger\_type](group__sensor__interface.md#ga08215279400e8c9eb05ce4e4f0898ffd) [trigger](structsensor__stream__trigger.md#a9a367e746764e68140ec9120f2a016e6);

[ 622](structsensor__stream__trigger.md#a62ccdecf7253b1bfdff4f1d659563d76) enum [sensor\_stream\_data\_opt](group__sensor__interface.md#ga8613a20521a37d40fd7371dc63ba2dac) [opt](structsensor__stream__trigger.md#a62ccdecf7253b1bfdff4f1d659563d76);

623};

624

[ 625](group__sensor__interface.md#ga9b7b0db322121d220b126d2b5bb7eb73)#define SENSOR\_STREAM\_TRIGGER\_PREP(\_trigger, \_opt) \

626 { \

627 .trigger = (\_trigger), .opt = (\_opt), \

628 }

629

630/\*

631 \* Internal data structure used to store information about the IODevice for async reading and

632 \* streaming sensor data.

633 \*/

[ 634](structsensor__read__config.md)struct [sensor\_read\_config](structsensor__read__config.md) {

[ 635](structsensor__read__config.md#ad49d5ab5293017d1ad2cf60adc542090) const struct [device](structdevice.md) \*[sensor](structsensor__read__config.md#ad49d5ab5293017d1ad2cf60adc542090);

[ 636](structsensor__read__config.md#aca96de2c23fb63f887c4c40dcb272798) const bool [is\_streaming](structsensor__read__config.md#aca96de2c23fb63f887c4c40dcb272798);

637 union {

[ 638](structsensor__read__config.md#a2aff44f02b25fd4ad1d4bc217800fad1) struct [sensor\_chan\_spec](structsensor__chan__spec.md) \*const [channels](structsensor__read__config.md#a2aff44f02b25fd4ad1d4bc217800fad1);

[ 639](structsensor__read__config.md#a6eaa6df7bc9378abe0f5b4b8c9a05909) struct [sensor\_stream\_trigger](structsensor__stream__trigger.md) \*const [triggers](structsensor__read__config.md#a6eaa6df7bc9378abe0f5b4b8c9a05909);

640 };

[ 641](structsensor__read__config.md#a5236049e0563ebba754994d70e22383a) size\_t [count](structsensor__read__config.md#a5236049e0563ebba754994d70e22383a);

[ 642](structsensor__read__config.md#aecb9c899e292fdb25c3c990bdaf1c76b) const size\_t [max](structsensor__read__config.md#aecb9c899e292fdb25c3c990bdaf1c76b);

643};

644

[ 660](group__sensor__interface.md#ga0cc1ee28114557e9e00257071c7dfa9f)#define SENSOR\_DT\_READ\_IODEV(name, dt\_node, ...) \

661 static struct sensor\_chan\_spec \_CONCAT(\_\_channel\_array\_, name)[] = {\_\_VA\_ARGS\_\_}; \

662 static struct sensor\_read\_config \_CONCAT(\_\_sensor\_read\_config\_, name) = { \

663 .sensor = DEVICE\_DT\_GET(dt\_node), \

664 .is\_streaming = false, \

665 .channels = \_CONCAT(\_\_channel\_array\_, name), \

666 .count = ARRAY\_SIZE(\_CONCAT(\_\_channel\_array\_, name)), \

667 .max = ARRAY\_SIZE(\_CONCAT(\_\_channel\_array\_, name)), \

668 }; \

669 RTIO\_IODEV\_DEFINE(name, &\_\_sensor\_iodev\_api, \_CONCAT(&\_\_sensor\_read\_config\_, name))

670

[ 690](group__sensor__interface.md#ga35211c4d908a26f98b1f8d925a9b1374)#define SENSOR\_DT\_STREAM\_IODEV(name, dt\_node, ...) \

691 static struct sensor\_stream\_trigger \_CONCAT(\_\_trigger\_array\_, name)[] = {\_\_VA\_ARGS\_\_}; \

692 static struct sensor\_read\_config \_CONCAT(\_\_sensor\_read\_config\_, name) = { \

693 .sensor = DEVICE\_DT\_GET(dt\_node), \

694 .is\_streaming = true, \

695 .triggers = \_CONCAT(\_\_trigger\_array\_, name), \

696 .count = ARRAY\_SIZE(\_CONCAT(\_\_trigger\_array\_, name)), \

697 .max = ARRAY\_SIZE(\_CONCAT(\_\_trigger\_array\_, name)), \

698 }; \

699 RTIO\_IODEV\_DEFINE(name, &\_\_sensor\_iodev\_api, &\_CONCAT(\_\_sensor\_read\_config\_, name))

700

701/\* Used to submit an RTIO sqe to the sensor's iodev \*/

[ 702](group__sensor__interface.md#gad77732c8f0ec5520cdd71c2829787981)typedef void (\*[sensor\_submit\_t](group__sensor__interface.md#gad77732c8f0ec5520cdd71c2829787981))(const struct [device](structdevice.md) \*sensor, struct [rtio\_iodev\_sqe](structrtio__iodev__sqe.md) \*[sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b));

703

704/\* The default decoder API \*/

705extern const struct [sensor\_decoder\_api](structsensor__decoder__api.md) \_\_sensor\_default\_decoder;

706

707/\* The default sensor iodev API \*/

708extern const struct [rtio\_iodev\_api](structrtio__iodev__api.md) \_\_sensor\_iodev\_api;

709

[ 710](structsensor__driver__api.md)\_\_subsystem struct [sensor\_driver\_api](structsensor__driver__api.md) {

[ 711](structsensor__driver__api.md#a2d230a976b19a699d132034f58bb2b6a) [sensor\_attr\_set\_t](group__sensor__interface.md#ga38422ace4194a66a9a912a8ef1e088fb) [attr\_set](structsensor__driver__api.md#a2d230a976b19a699d132034f58bb2b6a);

[ 712](structsensor__driver__api.md#a3e28950f844c3f8b8da5ba9ff8052e46) [sensor\_attr\_get\_t](group__sensor__interface.md#ga00d05c82b46e56dca5f6e8f7f01c31b8) [attr\_get](structsensor__driver__api.md#a3e28950f844c3f8b8da5ba9ff8052e46);

[ 713](structsensor__driver__api.md#a4708070fd6654ecbbe631819aba319bd) [sensor\_trigger\_set\_t](group__sensor__interface.md#gad7f7a3d9e714cc16f23656ca06592aa4) [trigger\_set](structsensor__driver__api.md#a4708070fd6654ecbbe631819aba319bd);

[ 714](structsensor__driver__api.md#a4b40e25b81fe070e2f6bdcf7f8a4a31f) [sensor\_sample\_fetch\_t](group__sensor__interface.md#gacae110a4edb6f29dfb457cb1ea8d68c1) [sample\_fetch](structsensor__driver__api.md#a4b40e25b81fe070e2f6bdcf7f8a4a31f);

[ 715](structsensor__driver__api.md#a667b41bf51f2c7a6bb31713fbf889113) [sensor\_channel\_get\_t](group__sensor__interface.md#ga5c9b5ed9097464562004b446856043fd) [channel\_get](structsensor__driver__api.md#a667b41bf51f2c7a6bb31713fbf889113);

[ 716](structsensor__driver__api.md#a004f9d342805dc72249ab9b8c17a544b) [sensor\_get\_decoder\_t](group__sensor__interface.md#ga21e407d552d140cfb6bfd0d9513c7d42) [get\_decoder](structsensor__driver__api.md#a004f9d342805dc72249ab9b8c17a544b);

[ 717](structsensor__driver__api.md#ae3ba0adeba21351e8f660896e5a0e702) [sensor\_submit\_t](group__sensor__interface.md#gad77732c8f0ec5520cdd71c2829787981) [submit](structsensor__driver__api.md#ae3ba0adeba21351e8f660896e5a0e702);

718};

719

[ 732](group__sensor__interface.md#gafbf65226a227e9f8824908bc38e336f5)\_\_syscall int [sensor\_attr\_set](group__sensor__interface.md#gafbf65226a227e9f8824908bc38e336f5)(const struct [device](structdevice.md) \*dev,

733 enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) chan,

734 enum [sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b) attr,

735 const struct [sensor\_value](structsensor__value.md) \*val);

736

737static inline int z\_impl\_sensor\_attr\_set(const struct [device](structdevice.md) \*dev,

738 enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) chan,

739 enum [sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b) attr,

740 const struct [sensor\_value](structsensor__value.md) \*val)

741{

742 const struct [sensor\_driver\_api](structsensor__driver__api.md) \*api =

743 (const struct [sensor\_driver\_api](structsensor__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

744

745 if (api->attr\_set == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

746 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

747 }

748

749 return api->attr\_set(dev, chan, attr, val);

750}

751

[ 764](group__sensor__interface.md#gaedfdfc71dce702dc1fb1c6e60ff0f73a)\_\_syscall int [sensor\_attr\_get](group__sensor__interface.md#gaedfdfc71dce702dc1fb1c6e60ff0f73a)(const struct [device](structdevice.md) \*dev,

765 enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) chan,

766 enum [sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b) attr,

767 struct [sensor\_value](structsensor__value.md) \*val);

768

769static inline int z\_impl\_sensor\_attr\_get(const struct [device](structdevice.md) \*dev,

770 enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) chan,

771 enum [sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b) attr,

772 struct [sensor\_value](structsensor__value.md) \*val)

773{

774 const struct [sensor\_driver\_api](structsensor__driver__api.md) \*api =

775 (const struct [sensor\_driver\_api](structsensor__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

776

777 if (api->attr\_get == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

778 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

779 }

780

781 return api->attr\_get(dev, chan, attr, val);

782}

783

[ 806](group__sensor__interface.md#ga7c72aca732e0641612d2f9437c2e41b7)static inline int [sensor\_trigger\_set](group__sensor__interface.md#ga7c72aca732e0641612d2f9437c2e41b7)(const struct [device](structdevice.md) \*dev,

807 const struct [sensor\_trigger](structsensor__trigger.md) \*trig,

808 [sensor\_trigger\_handler\_t](group__sensor__interface.md#ga890c1fb6d6974aea22a2d08829a75902) handler)

809{

810 const struct [sensor\_driver\_api](structsensor__driver__api.md) \*api =

811 (const struct [sensor\_driver\_api](structsensor__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

812

813 if (api->[trigger\_set](structsensor__driver__api.md#a4708070fd6654ecbbe631819aba319bd) == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

814 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

815 }

816

817 return api->[trigger\_set](structsensor__driver__api.md#a4708070fd6654ecbbe631819aba319bd)(dev, trig, handler);

818}

819

[ 838](group__sensor__interface.md#gaa75e25d93ee7cac0bf38399f3c006dff)\_\_syscall int [sensor\_sample\_fetch](group__sensor__interface.md#gaa75e25d93ee7cac0bf38399f3c006dff)(const struct [device](structdevice.md) \*dev);

839

840static inline int z\_impl\_sensor\_sample\_fetch(const struct [device](structdevice.md) \*dev)

841{

842 const struct [sensor\_driver\_api](structsensor__driver__api.md) \*api =

843 (const struct [sensor\_driver\_api](structsensor__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

844

845 return api->sample\_fetch(dev, [SENSOR\_CHAN\_ALL](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ab275027eb550b2b075c44917634eca2c));

846}

847

[ 869](group__sensor__interface.md#gac16192826432438a15274cf28d66e8a6)\_\_syscall int [sensor\_sample\_fetch\_chan](group__sensor__interface.md#gac16192826432438a15274cf28d66e8a6)(const struct [device](structdevice.md) \*dev,

870 enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) type);

871

872static inline int z\_impl\_sensor\_sample\_fetch\_chan(const struct [device](structdevice.md) \*dev,

873 enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) type)

874{

875 const struct [sensor\_driver\_api](structsensor__driver__api.md) \*api =

876 (const struct [sensor\_driver\_api](structsensor__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

877

878 return api->sample\_fetch(dev, type);

879}

880

[ 902](group__sensor__interface.md#ga9e0e6c1408d32c52267984bae7cb268d)\_\_syscall int [sensor\_channel\_get](group__sensor__interface.md#ga9e0e6c1408d32c52267984bae7cb268d)(const struct [device](structdevice.md) \*dev,

903 enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) chan,

904 struct [sensor\_value](structsensor__value.md) \*val);

905

906static inline int z\_impl\_sensor\_channel\_get(const struct [device](structdevice.md) \*dev,

907 enum [sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934) chan,

908 struct [sensor\_value](structsensor__value.md) \*val)

909{

910 const struct [sensor\_driver\_api](structsensor__driver__api.md) \*api =

911 (const struct [sensor\_driver\_api](structsensor__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

912

913 return api->channel\_get(dev, chan, val);

914}

915

916#if defined(CONFIG\_SENSOR\_ASYNC\_API) || defined(\_\_DOXYGEN\_\_)

917

918/\*

919 \* Generic data structure used for encoding the sample timestamp and number of channels sampled.

920 \*/

[ 921](structsensor__data__generic__header.md)struct \_\_attribute\_\_((\_\_packed\_\_)) [sensor\_data\_generic\_header](structsensor__data__generic__header.md) {

922 /\* The timestamp at which the data was collected from the sensor \*/

[ 923](structsensor__data__generic__header.md#a429e22b3191df271ccfe321b796e1ac9) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [timestamp\_ns](structsensor__data__generic__header.md#a429e22b3191df271ccfe321b796e1ac9);

924

925 /\*

926 \* The number of channels present in the frame. This will be the true number of elements in

927 \* channel\_info and in the q31 values that follow the header.

928 \*/

[ 929](structsensor__data__generic__header.md#a7edbe674f28c95f3aa40b1df84ca61fe) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [num\_channels](structsensor__data__generic__header.md#a7edbe674f28c95f3aa40b1df84ca61fe);

930

931 /\* Shift value for all samples in the frame \*/

[ 932](structsensor__data__generic__header.md#a68067521c1058b6802176e1d48fed788) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [shift](structsensor__data__generic__header.md#a68067521c1058b6802176e1d48fed788);

933

934 /\* This padding is needed to make sure that the 'channels' field is aligned \*/

935 [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) \_padding[sizeof(struct [sensor\_chan\_spec](structsensor__chan__spec.md)) - 1];

936

937 /\* Channels present in the frame \*/

[ 938](structsensor__data__generic__header.md#ac09f23959c66ff75b0854a95e8d4504b) struct [sensor\_chan\_spec](structsensor__chan__spec.md) [channels](structsensor__data__generic__header.md#ac09f23959c66ff75b0854a95e8d4504b)[0];

939};

940

[ 949](group__sensor__interface.md#ga32f679a4004b5707b2de00eb580d0930)#define SENSOR\_CHANNEL\_3\_AXIS(chan) \

950 ((chan) == SENSOR\_CHAN\_ACCEL\_XYZ || (chan) == SENSOR\_CHAN\_GYRO\_XYZ || \

951 (chan) == SENSOR\_CHAN\_MAGN\_XYZ || (chan) == SENSOR\_CHAN\_POS\_DXYZ)

952

[ 961](group__sensor__interface.md#ga8bec69db645c9f4d58b396f4d025d0d8)#define SENSOR\_CHANNEL\_IS\_ACCEL(chan) \

962 ((chan) == SENSOR\_CHAN\_ACCEL\_XYZ || (chan) == SENSOR\_CHAN\_ACCEL\_X || \

963 (chan) == SENSOR\_CHAN\_ACCEL\_Y || (chan) == SENSOR\_CHAN\_ACCEL\_Z)

964

[ 973](group__sensor__interface.md#gafac19bf89f1cca6f9a208676588184ae)#define SENSOR\_CHANNEL\_IS\_GYRO(chan) \

974 ((chan) == SENSOR\_CHAN\_GYRO\_XYZ || (chan) == SENSOR\_CHAN\_GYRO\_X || \

975 (chan) == SENSOR\_CHAN\_GYRO\_Y || (chan) == SENSOR\_CHAN\_GYRO\_Z)

976

[ 985](group__sensor__interface.md#ga12db6fc43adce48d34c25c16fd2336a3)\_\_syscall int [sensor\_get\_decoder](group__sensor__interface.md#ga12db6fc43adce48d34c25c16fd2336a3)(const struct [device](structdevice.md) \*dev,

986 const struct [sensor\_decoder\_api](structsensor__decoder__api.md) \*\*decoder);

987

988static inline int z\_impl\_sensor\_get\_decoder(const struct [device](structdevice.md) \*dev,

989 const struct [sensor\_decoder\_api](structsensor__decoder__api.md) \*\*decoder)

990{

991 const struct [sensor\_driver\_api](structsensor__driver__api.md) \*api = (const struct [sensor\_driver\_api](structsensor__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

992

993 \_\_ASSERT\_NO\_MSG(api != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4));

994

995 if (api->get\_decoder == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

996 \*decoder = &\_\_sensor\_default\_decoder;

997 return 0;

998 }

999

1000 return api->get\_decoder(dev, decoder);

1001}

1002

[ 1021](group__sensor__interface.md#gab854651e1b6c3206bf2b829ea5a6c420)\_\_syscall int [sensor\_reconfigure\_read\_iodev](group__sensor__interface.md#gab854651e1b6c3206bf2b829ea5a6c420)(struct [rtio\_iodev](structrtio__iodev.md) \*iodev, const struct [device](structdevice.md) \*sensor,

1022 const struct [sensor\_chan\_spec](structsensor__chan__spec.md) \*channels,

1023 size\_t num\_channels);

1024

1025static inline int z\_impl\_sensor\_reconfigure\_read\_iodev(struct [rtio\_iodev](structrtio__iodev.md) \*iodev,

1026 const struct [device](structdevice.md) \*sensor,

1027 const struct [sensor\_chan\_spec](structsensor__chan__spec.md) \*channels,

1028 size\_t num\_channels)

1029{

1030 struct [sensor\_read\_config](structsensor__read__config.md) \*cfg = (struct [sensor\_read\_config](structsensor__read__config.md) \*)iodev->[data](structrtio__iodev.md#af0f3a27fe8dea2161c9a73cb838bdeec);

1031

1032 if (cfg->max < num\_channels || cfg->is\_streaming) {

1033 return -[ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5);

1034 }

1035

1036 cfg->sensor = [sensor](structsensor__read__config.md#ad49d5ab5293017d1ad2cf60adc542090);

1037 [memcpy](string_8h.md#af0f01bffcd16daa9143f6014d10a25ad)(cfg->channels, [channels](structsensor__read__config.md#a2aff44f02b25fd4ad1d4bc217800fad1), num\_channels \* sizeof(struct [sensor\_chan\_spec](structsensor__chan__spec.md)));

1038 cfg->count = num\_channels;

1039 return 0;

1040}

1041

[ 1042](group__sensor__interface.md#gac77fc83844935f61a2bf9ab2c38987b6)static inline int [sensor\_stream](group__sensor__interface.md#gac77fc83844935f61a2bf9ab2c38987b6)(struct [rtio\_iodev](structrtio__iodev.md) \*iodev, struct [rtio](structrtio.md) \*ctx, void \*userdata,

1043 struct [rtio\_sqe](structrtio__sqe.md) \*\*handle)

1044{

1045 if ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_USERSPACE)) {

1046 struct [rtio\_sqe](structrtio__sqe.md) sqe;

1047

1048 [rtio\_sqe\_prep\_read\_multishot](group__rtio.md#ga9803aa829f8c0eeee746ea7d872c20cc)(&sqe, [iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc), [RTIO\_PRIO\_NORM](group__rtio__sqe__prio.md#gab02e27e01b7dd4eb3439df557899ce92), [userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971));

1049 [rtio\_sqe\_copy\_in\_get\_handles](group__rtio.md#ga830863e6c8d9b96f4c473a038cab8f8c)(ctx, &sqe, handle, 1);

1050 } else {

1051 struct [rtio\_sqe](structrtio__sqe.md) \*sqe = [rtio\_sqe\_acquire](group__rtio.md#ga8b47c954d15a334621def53acceb6799)(ctx);

1052

1053 if (sqe == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

1054 return -[ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5);

1055 }

1056 if (handle != [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

1057 \*handle = sqe;

1058 }

1059 [rtio\_sqe\_prep\_read\_multishot](group__rtio.md#ga9803aa829f8c0eeee746ea7d872c20cc)(sqe, [iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc), [RTIO\_PRIO\_NORM](group__rtio__sqe__prio.md#gab02e27e01b7dd4eb3439df557899ce92), [userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971));

1060 }

1061 [rtio\_submit](group__rtio.md#gafee27c64a4a4989c4eb774addde8eb2e)(ctx, 0);

1062 return 0;

1063}

1064

[ 1079](group__sensor__interface.md#ga1e77abad33cfd4b8330484cdc1354976)static inline int [sensor\_read](group__sensor__interface.md#ga1e77abad33cfd4b8330484cdc1354976)(struct [rtio\_iodev](structrtio__iodev.md) \*[iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc), struct [rtio](structrtio.md) \*ctx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structrtio__sqe.md#ab71176c084e8b8eb65dfeb3018ae2a49),

1080 size\_t [buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722))

1081{

1082 if ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_USERSPACE)) {

1083 struct [rtio\_sqe](structrtio__sqe.md) sqe;

1084

1085 [rtio\_sqe\_prep\_read](group__rtio.md#ga89c7cc2494e3dda50737f78f1a1376cf)(&sqe, [iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc), [RTIO\_PRIO\_NORM](group__rtio__sqe__prio.md#gab02e27e01b7dd4eb3439df557899ce92), [buf](structrtio__sqe.md#ab71176c084e8b8eb65dfeb3018ae2a49), [buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722), [buf](structrtio__sqe.md#ab71176c084e8b8eb65dfeb3018ae2a49));

1086 [rtio\_sqe\_copy\_in](group__rtio.md#ga65e351af0a16dcf504a51ef4eb9316c7)(ctx, &sqe, 1);

1087 } else {

1088 struct [rtio\_sqe](structrtio__sqe.md) \*sqe = [rtio\_sqe\_acquire](group__rtio.md#ga8b47c954d15a334621def53acceb6799)(ctx);

1089

1090 if (sqe == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

1091 return -[ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5);

1092 }

1093 [rtio\_sqe\_prep\_read](group__rtio.md#ga89c7cc2494e3dda50737f78f1a1376cf)(sqe, [iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc), [RTIO\_PRIO\_NORM](group__rtio__sqe__prio.md#gab02e27e01b7dd4eb3439df557899ce92), [buf](structrtio__sqe.md#ab71176c084e8b8eb65dfeb3018ae2a49), [buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722), [buf](structrtio__sqe.md#ab71176c084e8b8eb65dfeb3018ae2a49));

1094 }

1095 [rtio\_submit](group__rtio.md#gafee27c64a4a4989c4eb774addde8eb2e)(ctx, 0);

1096

1097 struct [rtio\_cqe](structrtio__cqe.md) \*cqe = [rtio\_cqe\_consume\_block](group__rtio.md#gaf617d05d9b59ce1f1d0697617ef6f249)(ctx);

1098 int res = cqe->[result](structrtio__cqe.md#acbe2e6607a752b676d9336b9ca6ce435);

1099

1100 \_\_ASSERT(cqe->[userdata](structrtio__cqe.md#a15128387ccbea55812ef229eab7241e7) == buf,

1101 "consumed non-matching completion for sensor read into buffer %p\n", buf);

1102

1103 [rtio\_cqe\_release](group__rtio.md#gaa0799a5f8ad98425d385a07c5d27d9cb)(ctx, cqe);

1104

1105 return res;

1106}

1107

[ 1121](group__sensor__interface.md#gab9eee9440b46b545b1faae224ae5949a)static inline int [sensor\_read\_async\_mempool](group__sensor__interface.md#gab9eee9440b46b545b1faae224ae5949a)(struct [rtio\_iodev](structrtio__iodev.md) \*iodev, struct [rtio](structrtio.md) \*ctx,

1122 void \*[userdata](structrtio__cqe.md#a15128387ccbea55812ef229eab7241e7))

1123{

1124 if ([IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(CONFIG\_USERSPACE)) {

1125 struct [rtio\_sqe](structrtio__sqe.md) sqe;

1126

1127 [rtio\_sqe\_prep\_read\_with\_pool](group__rtio.md#ga15c1f623658d27d300d1a31a6f3d6b9d)(&sqe, [iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc), [RTIO\_PRIO\_NORM](group__rtio__sqe__prio.md#gab02e27e01b7dd4eb3439df557899ce92), [userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971));

1128 [rtio\_sqe\_copy\_in](group__rtio.md#ga65e351af0a16dcf504a51ef4eb9316c7)(ctx, &sqe, 1);

1129 } else {

1130 struct [rtio\_sqe](structrtio__sqe.md) \*sqe = [rtio\_sqe\_acquire](group__rtio.md#ga8b47c954d15a334621def53acceb6799)(ctx);

1131

1132 if (sqe == [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)) {

1133 return -[ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5);

1134 }

1135 [rtio\_sqe\_prep\_read\_with\_pool](group__rtio.md#ga15c1f623658d27d300d1a31a6f3d6b9d)(sqe, [iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc), [RTIO\_PRIO\_NORM](group__rtio__sqe__prio.md#gab02e27e01b7dd4eb3439df557899ce92), [userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971));

1136 }

1137 [rtio\_submit](group__rtio.md#gafee27c64a4a4989c4eb774addde8eb2e)(ctx, 0);

1138 return 0;

1139}

1140

[ 1152](group__sensor__interface.md#gaa8cd6e4fadb5d69e59d101733b4fb462)typedef void (\*[sensor\_processing\_callback\_t](group__sensor__interface.md#gaa8cd6e4fadb5d69e59d101733b4fb462))(int result, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structrtio__sqe.md#ab71176c084e8b8eb65dfeb3018ae2a49), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722),

1153 void \*[userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971));

1154

[ 1166](group__sensor__interface.md#gabb076531445e1b128d515b28c7cc9dc8)void [sensor\_processing\_with\_callback](group__sensor__interface.md#gabb076531445e1b128d515b28c7cc9dc8)(struct [rtio](structrtio.md) \*ctx, [sensor\_processing\_callback\_t](group__sensor__interface.md#gaa8cd6e4fadb5d69e59d101733b4fb462) cb);

1167

1168#endif /\* defined(CONFIG\_SENSOR\_ASYNC\_API) || defined(\_\_DOXYGEN\_\_) \*/

1169

[ 1173](group__sensor__interface.md#ga0066e049c4f084305ca2b978e5c7454d)#define SENSOR\_G 9806650LL

1174

[ 1178](group__sensor__interface.md#ga6ebdc2f6942334de3cc248a53db7df33)#define SENSOR\_PI 3141592LL

1179

[ 1188](group__sensor__interface.md#gab797f2f578b1c9cc44f54ab5d503bbf8)static inline [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [sensor\_ms2\_to\_g](group__sensor__interface.md#gab797f2f578b1c9cc44f54ab5d503bbf8)(const struct [sensor\_value](structsensor__value.md) \*ms2)

1189{

1190 [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) micro\_ms2 = ms2->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) \* 1000000LL + ms2->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b);

1191

1192 if (micro\_ms2 > 0) {

1193 return (micro\_ms2 + [SENSOR\_G](group__sensor__interface.md#ga0066e049c4f084305ca2b978e5c7454d) / 2) / [SENSOR\_G](group__sensor__interface.md#ga0066e049c4f084305ca2b978e5c7454d);

1194 } else {

1195 return (micro\_ms2 - [SENSOR\_G](group__sensor__interface.md#ga0066e049c4f084305ca2b978e5c7454d) / 2) / [SENSOR\_G](group__sensor__interface.md#ga0066e049c4f084305ca2b978e5c7454d);

1196 }

1197}

1198

[ 1205](group__sensor__interface.md#ga6ab9ce9c6ee2e52d197e5cb4ccd88979)static inline void [sensor\_g\_to\_ms2](group__sensor__interface.md#ga6ab9ce9c6ee2e52d197e5cb4ccd88979)([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) g, struct [sensor\_value](structsensor__value.md) \*ms2)

1206{

1207 ms2->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) = (([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))g \* [SENSOR\_G](group__sensor__interface.md#ga0066e049c4f084305ca2b978e5c7454d)) / 1000000LL;

1208 ms2->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b) = (([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))g \* [SENSOR\_G](group__sensor__interface.md#ga0066e049c4f084305ca2b978e5c7454d)) % 1000000LL;

1209}

1210

[ 1219](group__sensor__interface.md#ga9e0fb14f84dca02497ce5bff10b51ab8)static inline [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [sensor\_ms2\_to\_mg](group__sensor__interface.md#ga9e0fb14f84dca02497ce5bff10b51ab8)(const struct [sensor\_value](structsensor__value.md) \*ms2)

1220{

1221 [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) nano\_ms2 = (ms2->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) \* 1000000LL + ms2->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b)) \* 1000LL;

1222

1223 if (nano\_ms2 > 0) {

1224 return (nano\_ms2 + [SENSOR\_G](group__sensor__interface.md#ga0066e049c4f084305ca2b978e5c7454d) / 2) / [SENSOR\_G](group__sensor__interface.md#ga0066e049c4f084305ca2b978e5c7454d);

1225 } else {

1226 return (nano\_ms2 - [SENSOR\_G](group__sensor__interface.md#ga0066e049c4f084305ca2b978e5c7454d) / 2) / [SENSOR\_G](group__sensor__interface.md#ga0066e049c4f084305ca2b978e5c7454d);

1227 }

1228}

1229

[ 1238](group__sensor__interface.md#ga3db980100e634310a0a1623136048742)static inline [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [sensor\_ms2\_to\_ug](group__sensor__interface.md#ga3db980100e634310a0a1623136048742)(const struct [sensor\_value](structsensor__value.md) \*ms2)

1239{

1240 [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) micro\_ms2 = (ms2->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) \* [INT64\_C](xcc_8h.md#a93d102802b35d3b8abae9bbe7f0fed75)(1000000)) + ms2->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b);

1241

1242 return (micro\_ms2 \* 1000000LL) / [SENSOR\_G](group__sensor__interface.md#ga0066e049c4f084305ca2b978e5c7454d);

1243}

1244

[ 1251](group__sensor__interface.md#ga28a1c6cf74a391712a4697792f759d62)static inline void [sensor\_ug\_to\_ms2](group__sensor__interface.md#ga28a1c6cf74a391712a4697792f759d62)([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) ug, struct [sensor\_value](structsensor__value.md) \*ms2)

1252{

1253 ms2->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) = (([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))ug \* [SENSOR\_G](group__sensor__interface.md#ga0066e049c4f084305ca2b978e5c7454d) / 1000000LL) / 1000000LL;

1254 ms2->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b) = (([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))ug \* [SENSOR\_G](group__sensor__interface.md#ga0066e049c4f084305ca2b978e5c7454d) / 1000000LL) % 1000000LL;

1255}

1256

[ 1264](group__sensor__interface.md#ga040a907c8934baab66d27b8dfb1ea220)static inline [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [sensor\_rad\_to\_degrees](group__sensor__interface.md#ga040a907c8934baab66d27b8dfb1ea220)(const struct [sensor\_value](structsensor__value.md) \*rad)

1265{

1266 [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) micro\_rad\_s = rad->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) \* 1000000LL + rad->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b);

1267

1268 if (micro\_rad\_s > 0) {

1269 return (micro\_rad\_s \* 180LL + [SENSOR\_PI](group__sensor__interface.md#ga6ebdc2f6942334de3cc248a53db7df33) / 2) / [SENSOR\_PI](group__sensor__interface.md#ga6ebdc2f6942334de3cc248a53db7df33);

1270 } else {

1271 return (micro\_rad\_s \* 180LL - [SENSOR\_PI](group__sensor__interface.md#ga6ebdc2f6942334de3cc248a53db7df33) / 2) / [SENSOR\_PI](group__sensor__interface.md#ga6ebdc2f6942334de3cc248a53db7df33);

1272 }

1273}

1274

[ 1281](group__sensor__interface.md#ga39d4b84f5d792e27b2d6d5eb6a2ccb0d)static inline void [sensor\_degrees\_to\_rad](group__sensor__interface.md#ga39d4b84f5d792e27b2d6d5eb6a2ccb0d)([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), struct [sensor\_value](structsensor__value.md) \*rad)

1282{

1283 rad->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) = (([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417) \* [SENSOR\_PI](group__sensor__interface.md#ga6ebdc2f6942334de3cc248a53db7df33) / 180LL) / 1000000LL;

1284 rad->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b) = (([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417) \* [SENSOR\_PI](group__sensor__interface.md#ga6ebdc2f6942334de3cc248a53db7df33) / 180LL) % 1000000LL;

1285}

1286

[ 1298](group__sensor__interface.md#gad80093a6cfe95428dd0ead85547838a6)static inline [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [sensor\_rad\_to\_10udegrees](group__sensor__interface.md#gad80093a6cfe95428dd0ead85547838a6)(const struct [sensor\_value](structsensor__value.md) \*rad)

1299{

1300 [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) micro\_rad\_s = rad->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) \* 1000000LL + rad->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b);

1301

1302 return (micro\_rad\_s \* 180LL \* 100000LL) / [SENSOR\_PI](group__sensor__interface.md#ga6ebdc2f6942334de3cc248a53db7df33);

1303}

1304

[ 1311](group__sensor__interface.md#gab53418e1eb164364663d3ec3f40399a4)static inline void [sensor\_10udegrees\_to\_rad](group__sensor__interface.md#gab53418e1eb164364663d3ec3f40399a4)([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), struct [sensor\_value](structsensor__value.md) \*rad)

1312{

1313 rad->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) = (([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417) \* [SENSOR\_PI](group__sensor__interface.md#ga6ebdc2f6942334de3cc248a53db7df33) / 180LL / 100000LL) / 1000000LL;

1314 rad->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b) = (([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417) \* [SENSOR\_PI](group__sensor__interface.md#ga6ebdc2f6942334de3cc248a53db7df33) / 180LL / 100000LL) % 1000000LL;

1315}

1316

[ 1323](group__sensor__interface.md#ga29223b754dc436ab1e97ce6209a3ea06)static inline double [sensor\_value\_to\_double](group__sensor__interface.md#ga29223b754dc436ab1e97ce6209a3ea06)(const struct [sensor\_value](structsensor__value.md) \*val)

1324{

1325 return (double)val->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) + (double)val->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b) / 1000000;

1326}

1327

[ 1334](group__sensor__interface.md#ga2ad1fc2abd1c8c38e7de6e99fa5c1f20)static inline float [sensor\_value\_to\_float](group__sensor__interface.md#ga2ad1fc2abd1c8c38e7de6e99fa5c1f20)(const struct [sensor\_value](structsensor__value.md) \*val)

1335{

1336 return (float)val->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) + (float)val->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b) / 1000000;

1337}

1338

[ 1346](group__sensor__interface.md#gaf01bbb251ad0c7f6c55c5b702e8a4048)static inline int [sensor\_value\_from\_double](group__sensor__interface.md#gaf01bbb251ad0c7f6c55c5b702e8a4048)(struct [sensor\_value](structsensor__value.md) \*val, double inp)

1347{

1348 if (inp < INT32\_MIN || inp > [INT32\_MAX](stdint_8h.md#a181807730d4a375f848ba139813ce04f)) {

1349 return -[ERANGE](group__system__errno.md#gaa1591a4f3a86360108de5b9ba34980ca);

1350 }

1351

1352 double val2 = (inp - ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))inp) \* 1000000.0;

1353

1354 if (val2 < INT32\_MIN || val2 > [INT32\_MAX](stdint_8h.md#a181807730d4a375f848ba139813ce04f)) {

1355 return -[ERANGE](group__system__errno.md#gaa1591a4f3a86360108de5b9ba34980ca);

1356 }

1357

1358 val->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) = ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))inp;

1359 val->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b) = ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))val2;

1360

1361 return 0;

1362}

1363

[ 1371](group__sensor__interface.md#ga64d5a1725eda200c80daf42b1067c46c)static inline int [sensor\_value\_from\_float](group__sensor__interface.md#ga64d5a1725eda200c80daf42b1067c46c)(struct [sensor\_value](structsensor__value.md) \*val, float inp)

1372{

1373 float val2 = (inp - ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))inp) \* 1000000.0f;

1374

1375 if (val2 < INT32\_MIN || val2 > (float)([INT32\_MAX](stdint_8h.md#a181807730d4a375f848ba139813ce04f) - 1)) {

1376 return -[ERANGE](group__system__errno.md#gaa1591a4f3a86360108de5b9ba34980ca);

1377 }

1378

1379 val->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) = ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))inp;

1380 val->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b) = ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))val2;

1381

1382 return 0;

1383}

1384

1385#ifdef CONFIG\_SENSOR\_INFO

1386

1387struct sensor\_info {

1388 const struct device \*dev;

1389 const char \*vendor;

1390 const char \*model;

1391 const char \*friendly\_name;

1392};

1393

1394#define SENSOR\_INFO\_INITIALIZER(\_dev, \_vendor, \_model, \_friendly\_name) \

1395 { \

1396 .dev = \_dev, \

1397 .vendor = \_vendor, \

1398 .model = \_model, \

1399 .friendly\_name = \_friendly\_name, \

1400 }

1401

1402#define SENSOR\_INFO\_DEFINE(name, ...) \

1403 static const STRUCT\_SECTION\_ITERABLE(sensor\_info, name) = \

1404 SENSOR\_INFO\_INITIALIZER(\_\_VA\_ARGS\_\_)

1405

1406#define SENSOR\_INFO\_DT\_NAME(node\_id) \

1407 \_CONCAT(\_\_sensor\_info, DEVICE\_DT\_NAME\_GET(node\_id))

1408

1409#define SENSOR\_INFO\_DT\_DEFINE(node\_id) \

1410 SENSOR\_INFO\_DEFINE(SENSOR\_INFO\_DT\_NAME(node\_id), \

1411 DEVICE\_DT\_GET(node\_id), \

1412 DT\_NODE\_VENDOR\_OR(node\_id, NULL), \

1413 DT\_NODE\_MODEL\_OR(node\_id, NULL), \

1414 DT\_PROP\_OR(node\_id, friendly\_name, NULL)) \

1415

1416#else

1417

[ 1418](group__sensor__interface.md#ga7467206da76c3704d2e491d1b1c0973a)#define SENSOR\_INFO\_DEFINE(name, ...)

[ 1419](group__sensor__interface.md#ga9e6acbc580e9223bfb86ee8919cdc778)#define SENSOR\_INFO\_DT\_DEFINE(node\_id)

1420

1421#endif /\* CONFIG\_SENSOR\_INFO \*/

1422

[ 1450](group__sensor__interface.md#gaa67ca630e3931a0c3821ba438c86690c)#define SENSOR\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm\_device, \

1451 data\_ptr, cfg\_ptr, level, prio, \

1452 api\_ptr, ...) \

1453 DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm\_device, \

1454 data\_ptr, cfg\_ptr, level, prio, \

1455 api\_ptr, \_\_VA\_ARGS\_\_); \

1456 \

1457 SENSOR\_INFO\_DT\_DEFINE(node\_id);

1458

[ 1468](group__sensor__interface.md#ga284dc3b9018f14161dc0a2b6bed9a37e)#define SENSOR\_DEVICE\_DT\_INST\_DEFINE(inst, ...) \

1469 SENSOR\_DEVICE\_DT\_DEFINE(DT\_DRV\_INST(inst), \_\_VA\_ARGS\_\_)

1470

[ 1477](group__sensor__interface.md#ga6d69a9644e08a9cd7773645fa11293e3)static inline [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [sensor\_value\_to\_milli](group__sensor__interface.md#ga6d69a9644e08a9cd7773645fa11293e3)(const struct [sensor\_value](structsensor__value.md) \*val)

1478{

1479 return (([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))val->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) \* 1000) + val->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b) / 1000;

1480}

1481

[ 1488](group__sensor__interface.md#ga9bf7faf60aa54a7540e9b73a61864e25)static inline [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) [sensor\_value\_to\_micro](group__sensor__interface.md#ga9bf7faf60aa54a7540e9b73a61864e25)(const struct [sensor\_value](structsensor__value.md) \*val)

1489{

1490 return (([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))val->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) \* 1000000) + val->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b);

1491}

1492

[ 1500](group__sensor__interface.md#ga88b2605526e37420db871f066c5053b3)static inline int [sensor\_value\_from\_milli](group__sensor__interface.md#ga88b2605526e37420db871f066c5053b3)(struct [sensor\_value](structsensor__value.md) \*val, [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) milli)

1501{

1502 if (milli < (([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))[INT32\_MIN](stdint_8h.md#a688eb21a22db27c2b2bd5836943cdcbe) - 1) \* 1000LL ||

1503 milli > (([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))[INT32\_MAX](stdint_8h.md#a181807730d4a375f848ba139813ce04f) + 1) \* 1000LL) {

1504 return -[ERANGE](group__system__errno.md#gaa1591a4f3a86360108de5b9ba34980ca);

1505 }

1506

1507 val->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) = ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))(milli / 1000);

1508 val->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b) = ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))(milli % 1000) \* 1000;

1509

1510 return 0;

1511}

1512

[ 1520](group__sensor__interface.md#gabff019c63c89cbc546c0981819040c99)static inline int [sensor\_value\_from\_micro](group__sensor__interface.md#gabff019c63c89cbc546c0981819040c99)(struct [sensor\_value](structsensor__value.md) \*val, [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) micro)

1521{

1522 if (micro < (([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))[INT32\_MIN](stdint_8h.md#a688eb21a22db27c2b2bd5836943cdcbe) - 1) \* 1000000LL ||

1523 micro > (([int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b))[INT32\_MAX](stdint_8h.md#a181807730d4a375f848ba139813ce04f) + 1) \* 1000000LL) {

1524 return -[ERANGE](group__system__errno.md#gaa1591a4f3a86360108de5b9ba34980ca);

1525 }

1526

1527 val->[val1](structsensor__value.md#af21dddb084da4c42a7e77b48edf26fbe) = ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))(micro / 1000000LL);

1528 val->[val2](structsensor__value.md#a91f81bd0f5da69084cf3c629fde68a1b) = ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2))(micro % 1000000LL);

1529

1530 return 0;

1531}

1532

1536

[ 1542](sensor_8h.md#a8d3434eb5860c2f2e6fe36b4de920c8c)#define SENSOR\_DECODER\_NAME() UTIL\_CAT(DT\_DRV\_COMPAT, \_\_decoder\_api)

1543

[ 1551](sensor_8h.md#a82da2432981c593ed638a21c51fb0873)#define SENSOR\_DECODER\_DT\_GET(node\_id) \

1552 &UTIL\_CAT(DT\_STRING\_TOKEN\_BY\_IDX(node\_id, compatible, 0), \_\_decoder\_api)

1553

[ 1569](sensor_8h.md#a78ad4b76be4a6f5347ba82b7db43b7c2)#define SENSOR\_DECODER\_API\_DT\_DEFINE() \

1570 COND\_CODE\_1(DT\_HAS\_COMPAT\_STATUS\_OKAY(DT\_DRV\_COMPAT), (), (static)) \

1571 const STRUCT\_SECTION\_ITERABLE(sensor\_decoder\_api, SENSOR\_DECODER\_NAME())

1572

1573#define Z\_MAYBE\_SENSOR\_DECODER\_DECLARE\_INTERNAL\_IDX(node\_id, prop, idx) \

1574 extern const struct sensor\_decoder\_api UTIL\_CAT( \

1575 DT\_STRING\_TOKEN\_BY\_IDX(node\_id, prop, idx), \_\_decoder\_api);

1576

1577#define Z\_MAYBE\_SENSOR\_DECODER\_DECLARE\_INTERNAL(node\_id) \

1578 COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, compatible), \

1579 (DT\_FOREACH\_PROP\_ELEM(node\_id, compatible, \

1580 Z\_MAYBE\_SENSOR\_DECODER\_DECLARE\_INTERNAL\_IDX)), \

1581 ())

1582

1583[DT\_FOREACH\_STATUS\_OKAY\_NODE](group__devicetree-generic-foreach.md#ga926f68202042c9db05390e628787f916)(Z\_MAYBE\_SENSOR\_DECODER\_DECLARE\_INTERNAL)

1584

1585#ifdef \_\_cplusplus

1586}

1587#endif

1588

1589#include <zephyr/syscalls/sensor.h>

1590

1591#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_SENSOR\_H\_ \*/

[d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417)

irp nz macro MOVR cc d

**Definition** asm-macro-32-bit-gnu.h:11

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[DT\_FOREACH\_STATUS\_OKAY\_NODE](group__devicetree-generic-foreach.md#ga926f68202042c9db05390e628787f916)

#define DT\_FOREACH\_STATUS\_OKAY\_NODE(fn)

Invokes fn for every status okay node in the tree.

**Definition** devicetree.h:3000

[RTIO\_PRIO\_NORM](group__rtio__sqe__prio.md#gab02e27e01b7dd4eb3439df557899ce92)

#define RTIO\_PRIO\_NORM

Normal priority.

**Definition** rtio.h:70

[rtio\_sqe\_prep\_read\_with\_pool](group__rtio.md#ga15c1f623658d27d300d1a31a6f3d6b9d)

static void rtio\_sqe\_prep\_read\_with\_pool(struct rtio\_sqe \*sqe, const struct rtio\_iodev \*iodev, int8\_t prio, void \*userdata)

Prepare a read op submission with context's mempool.

**Definition** rtio.h:595

[rtio\_sqe\_copy\_in](group__rtio.md#ga65e351af0a16dcf504a51ef4eb9316c7)

static int rtio\_sqe\_copy\_in(struct rtio \*r, const struct rtio\_sqe \*sqes, size\_t sqe\_count)

Copy an array of SQEs into the queue.

**Definition** rtio.h:1467

[rtio\_sqe\_copy\_in\_get\_handles](group__rtio.md#ga830863e6c8d9b96f4c473a038cab8f8c)

int rtio\_sqe\_copy\_in\_get\_handles(struct rtio \*r, const struct rtio\_sqe \*sqes, struct rtio\_sqe \*\*handle, size\_t sqe\_count)

Copy an array of SQEs into the queue and get resulting handles back.

[rtio\_sqe\_prep\_read](group__rtio.md#ga89c7cc2494e3dda50737f78f1a1376cf)

static void rtio\_sqe\_prep\_read(struct rtio\_sqe \*sqe, const struct rtio\_iodev \*iodev, int8\_t prio, uint8\_t \*buf, uint32\_t len, void \*userdata)

Prepare a read op submission.

**Definition** rtio.h:574

[rtio\_sqe\_acquire](group__rtio.md#ga8b47c954d15a334621def53acceb6799)

static struct rtio\_sqe \* rtio\_sqe\_acquire(struct rtio \*r)

Acquire a single submission queue event if available.

**Definition** rtio.h:1002

[rtio\_sqe\_prep\_read\_multishot](group__rtio.md#ga9803aa829f8c0eeee746ea7d872c20cc)

static void rtio\_sqe\_prep\_read\_multishot(struct rtio\_sqe \*sqe, const struct rtio\_iodev \*iodev, int8\_t prio, void \*userdata)

**Definition** rtio.h:603

[rtio\_cqe\_release](group__rtio.md#gaa0799a5f8ad98425d385a07c5d27d9cb)

static void rtio\_cqe\_release(struct rtio \*r, struct rtio\_cqe \*cqe)

Release consumed completion queue event.

**Definition** rtio.h:1121

[rtio\_cqe\_consume\_block](group__rtio.md#gaf617d05d9b59ce1f1d0697617ef6f249)

static struct rtio\_cqe \* rtio\_cqe\_consume\_block(struct rtio \*r)

Wait for and consume a single completion queue event.

**Definition** rtio.h:1097

[rtio\_submit](group__rtio.md#gafee27c64a4a4989c4eb774addde8eb2e)

int rtio\_submit(struct rtio \*r, uint32\_t wait\_count)

Submit I/O requests to the underlying executor.

[SENSOR\_G](group__sensor__interface.md#ga0066e049c4f084305ca2b978e5c7454d)

#define SENSOR\_G

The value of gravitational constant in micro m/s^2.

**Definition** sensor.h:1173

[sensor\_attr\_get\_t](group__sensor__interface.md#ga00d05c82b46e56dca5f6e8f7f01c31b8)

int(\* sensor\_attr\_get\_t)(const struct device \*dev, enum sensor\_channel chan, enum sensor\_attribute attr, struct sensor\_value \*val)

Callback API upon getting a sensor's attributes.

**Definition** sensor.h:403

[sensor\_decode](group__sensor__interface.md#ga018bca56056ae2558f9e45aeb2fa5f53)

static int sensor\_decode(struct sensor\_decode\_context \*ctx, void \*out, uint16\_t max\_count)

Decode N frames using a sensor\_decode\_context.

**Definition** sensor.h:591

[sensor\_rad\_to\_degrees](group__sensor__interface.md#ga040a907c8934baab66d27b8dfb1ea220)

static int32\_t sensor\_rad\_to\_degrees(const struct sensor\_value \*rad)

Helper function for converting radians to degrees.

**Definition** sensor.h:1264

[sensor\_trigger\_type](group__sensor__interface.md#ga08215279400e8c9eb05ce4e4f0898ffd)

sensor\_trigger\_type

Sensor trigger types.

**Definition** sensor.h:228

[sensor\_attribute](group__sensor__interface.md#ga0dcb6842bc969492bd1c9eb49708940b)

sensor\_attribute

Sensor attribute types.

**Definition** sensor.h:305

[sensor\_get\_decoder](group__sensor__interface.md#ga12db6fc43adce48d34c25c16fd2336a3)

int sensor\_get\_decoder(const struct device \*dev, const struct sensor\_decoder\_api \*\*decoder)

Get the sensor's decoder API.

[sensor\_read](group__sensor__interface.md#ga1e77abad33cfd4b8330484cdc1354976)

static int sensor\_read(struct rtio\_iodev \*iodev, struct rtio \*ctx, uint8\_t \*buf, size\_t buf\_len)

Blocking one shot read of samples from a sensor into a buffer.

**Definition** sensor.h:1079

[sensor\_get\_decoder\_t](group__sensor__interface.md#ga21e407d552d140cfb6bfd0d9513c7d42)

int(\* sensor\_get\_decoder\_t)(const struct device \*dev, const struct sensor\_decoder\_api \*\*api)

Get the decoder associate with the given device.

**Definition** sensor.h:605

[sensor\_ug\_to\_ms2](group__sensor__interface.md#ga28a1c6cf74a391712a4697792f759d62)

static void sensor\_ug\_to\_ms2(int32\_t ug, struct sensor\_value \*ms2)

Helper function to convert acceleration from micro Gs to m/s^2.

**Definition** sensor.h:1251

[sensor\_value\_to\_double](group__sensor__interface.md#ga29223b754dc436ab1e97ce6209a3ea06)

static double sensor\_value\_to\_double(const struct sensor\_value \*val)

Helper function for converting struct sensor\_value to double.

**Definition** sensor.h:1323

[sensor\_value\_to\_float](group__sensor__interface.md#ga2ad1fc2abd1c8c38e7de6e99fa5c1f20)

static float sensor\_value\_to\_float(const struct sensor\_value \*val)

Helper function for converting struct sensor\_value to float.

**Definition** sensor.h:1334

[sensor\_natively\_supported\_channel\_size\_info](group__sensor__interface.md#ga2b045cdbd4d1ca37beed69970093945b)

int sensor\_natively\_supported\_channel\_size\_info(struct sensor\_chan\_spec channel, size\_t \*base\_size, size\_t \*frame\_size)

[sensor\_attr\_set\_t](group__sensor__interface.md#ga38422ace4194a66a9a912a8ef1e088fb)

int(\* sensor\_attr\_set\_t)(const struct device \*dev, enum sensor\_channel chan, enum sensor\_attribute attr, const struct sensor\_value \*val)

Callback API upon setting a sensor's attributes.

**Definition** sensor.h:392

[sensor\_degrees\_to\_rad](group__sensor__interface.md#ga39d4b84f5d792e27b2d6d5eb6a2ccb0d)

static void sensor\_degrees\_to\_rad(int32\_t d, struct sensor\_value \*rad)

Helper function for converting degrees to radians.

**Definition** sensor.h:1281

[sensor\_ms2\_to\_ug](group__sensor__interface.md#ga3db980100e634310a0a1623136048742)

static int32\_t sensor\_ms2\_to\_ug(const struct sensor\_value \*ms2)

Helper function to convert acceleration from m/s^2 to micro Gs.

**Definition** sensor.h:1238

[sensor\_channel\_get\_t](group__sensor__interface.md#ga5c9b5ed9097464562004b446856043fd)

int(\* sensor\_channel\_get\_t)(const struct device \*dev, enum sensor\_channel chan, struct sensor\_value \*val)

Callback API for getting a reading from a sensor.

**Definition** sensor.h:431

[sensor\_value\_from\_float](group__sensor__interface.md#ga64d5a1725eda200c80daf42b1067c46c)

static int sensor\_value\_from\_float(struct sensor\_value \*val, float inp)

Helper function for converting float to struct sensor\_value.

**Definition** sensor.h:1371

[sensor\_g\_to\_ms2](group__sensor__interface.md#ga6ab9ce9c6ee2e52d197e5cb4ccd88979)

static void sensor\_g\_to\_ms2(int32\_t g, struct sensor\_value \*ms2)

Helper function to convert acceleration from Gs to m/s^2.

**Definition** sensor.h:1205

[sensor\_value\_to\_milli](group__sensor__interface.md#ga6d69a9644e08a9cd7773645fa11293e3)

static int64\_t sensor\_value\_to\_milli(const struct sensor\_value \*val)

Helper function for converting struct sensor\_value to integer milli units.

**Definition** sensor.h:1477

[SENSOR\_PI](group__sensor__interface.md#ga6ebdc2f6942334de3cc248a53db7df33)

#define SENSOR\_PI

The value of constant PI in micros.

**Definition** sensor.h:1178

[sensor\_trigger\_set](group__sensor__interface.md#ga7c72aca732e0641612d2f9437c2e41b7)

static int sensor\_trigger\_set(const struct device \*dev, const struct sensor\_trigger \*trig, sensor\_trigger\_handler\_t handler)

Activate a sensor's trigger and set the trigger handler.

**Definition** sensor.h:806

[sensor\_stream\_data\_opt](group__sensor__interface.md#ga8613a20521a37d40fd7371dc63ba2dac)

sensor\_stream\_data\_opt

Options for what to do with the associated data when a trigger is consumed.

**Definition** sensor.h:611

[sensor\_value\_from\_milli](group__sensor__interface.md#ga88b2605526e37420db871f066c5053b3)

static int sensor\_value\_from\_milli(struct sensor\_value \*val, int64\_t milli)

Helper function for converting integer milli units to struct sensor\_value.

**Definition** sensor.h:1500

[sensor\_trigger\_handler\_t](group__sensor__interface.md#ga890c1fb6d6974aea22a2d08829a75902)

void(\* sensor\_trigger\_handler\_t)(const struct device \*dev, const struct sensor\_trigger \*trigger)

Callback API upon firing of a trigger.

**Definition** sensor.h:383

[sensor\_value\_to\_micro](group__sensor__interface.md#ga9bf7faf60aa54a7540e9b73a61864e25)

static int64\_t sensor\_value\_to\_micro(const struct sensor\_value \*val)

Helper function for converting struct sensor\_value to integer micro units.

**Definition** sensor.h:1488

[sensor\_channel\_get](group__sensor__interface.md#ga9e0e6c1408d32c52267984bae7cb268d)

int sensor\_channel\_get(const struct device \*dev, enum sensor\_channel chan, struct sensor\_value \*val)

Get a reading from a sensor device.

[sensor\_ms2\_to\_mg](group__sensor__interface.md#ga9e0fb14f84dca02497ce5bff10b51ab8)

static int32\_t sensor\_ms2\_to\_mg(const struct sensor\_value \*ms2)

Helper function to convert acceleration from m/s^2 to milli Gs.

**Definition** sensor.h:1219

[sensor\_sample\_fetch](group__sensor__interface.md#gaa75e25d93ee7cac0bf38399f3c006dff)

int sensor\_sample\_fetch(const struct device \*dev)

Fetch a sample from the sensor and store it in an internal driver buffer.

[sensor\_processing\_callback\_t](group__sensor__interface.md#gaa8cd6e4fadb5d69e59d101733b4fb462)

void(\* sensor\_processing\_callback\_t)(int result, uint8\_t \*buf, uint32\_t buf\_len, void \*userdata)

Callback function used with the helper processing function.

**Definition** sensor.h:1152

[sensor\_channel](group__sensor__interface.md#gaaa1b502bc029b10d7b23b0a25ef4e934)

sensor\_channel

Sensor channels.

**Definition** sensor.h:61

[sensor\_10udegrees\_to\_rad](group__sensor__interface.md#gab53418e1eb164364663d3ec3f40399a4)

static void sensor\_10udegrees\_to\_rad(int32\_t d, struct sensor\_value \*rad)

Helper function for converting 10 micro degrees to radians.

**Definition** sensor.h:1311

[sensor\_ms2\_to\_g](group__sensor__interface.md#gab797f2f578b1c9cc44f54ab5d503bbf8)

static int32\_t sensor\_ms2\_to\_g(const struct sensor\_value \*ms2)

Helper function to convert acceleration from m/s^2 to Gs.

**Definition** sensor.h:1188

[sensor\_reconfigure\_read\_iodev](group__sensor__interface.md#gab854651e1b6c3206bf2b829ea5a6c420)

int sensor\_reconfigure\_read\_iodev(struct rtio\_iodev \*iodev, const struct device \*sensor, const struct sensor\_chan\_spec \*channels, size\_t num\_channels)

Reconfigure a reading iodev.

[sensor\_read\_async\_mempool](group__sensor__interface.md#gab9eee9440b46b545b1faae224ae5949a)

static int sensor\_read\_async\_mempool(struct rtio\_iodev \*iodev, struct rtio \*ctx, void \*userdata)

One shot non-blocking read with pool allocated buffer.

**Definition** sensor.h:1121

[sensor\_processing\_with\_callback](group__sensor__interface.md#gabb076531445e1b128d515b28c7cc9dc8)

void sensor\_processing\_with\_callback(struct rtio \*ctx, sensor\_processing\_callback\_t cb)

Helper function for common processing of sensor data.

[sensor\_value\_from\_micro](group__sensor__interface.md#gabff019c63c89cbc546c0981819040c99)

static int sensor\_value\_from\_micro(struct sensor\_value \*val, int64\_t micro)

Helper function for converting integer micro units to struct sensor\_value.

**Definition** sensor.h:1520

[sensor\_sample\_fetch\_chan](group__sensor__interface.md#gac16192826432438a15274cf28d66e8a6)

int sensor\_sample\_fetch\_chan(const struct device \*dev, enum sensor\_channel type)

Fetch a sample from the sensor and store it in an internal driver buffer.

[sensor\_stream](group__sensor__interface.md#gac77fc83844935f61a2bf9ab2c38987b6)

static int sensor\_stream(struct rtio\_iodev \*iodev, struct rtio \*ctx, void \*userdata, struct rtio\_sqe \*\*handle)

**Definition** sensor.h:1042

[sensor\_sample\_fetch\_t](group__sensor__interface.md#gacae110a4edb6f29dfb457cb1ea8d68c1)

int(\* sensor\_sample\_fetch\_t)(const struct device \*dev, enum sensor\_channel chan)

Callback API for fetching data from a sensor.

**Definition** sensor.h:423

[sensor\_submit\_t](group__sensor__interface.md#gad77732c8f0ec5520cdd71c2829787981)

void(\* sensor\_submit\_t)(const struct device \*sensor, struct rtio\_iodev\_sqe \*sqe)

**Definition** sensor.h:702

[sensor\_trigger\_set\_t](group__sensor__interface.md#gad7f7a3d9e714cc16f23656ca06592aa4)

int(\* sensor\_trigger\_set\_t)(const struct device \*dev, const struct sensor\_trigger \*trig, sensor\_trigger\_handler\_t handler)

Callback API for setting a sensor's trigger and handler.

**Definition** sensor.h:414

[sensor\_rad\_to\_10udegrees](group__sensor__interface.md#gad80093a6cfe95428dd0ead85547838a6)

static int32\_t sensor\_rad\_to\_10udegrees(const struct sensor\_value \*rad)

Helper function for converting radians to 10 micro degrees.

**Definition** sensor.h:1298

[sensor\_chan\_spec\_eq](group__sensor__interface.md#gae95715ffea5da18a9593ec2add029824)

static bool sensor\_chan\_spec\_eq(struct sensor\_chan\_spec chan\_spec0, struct sensor\_chan\_spec chan\_spec1)

Check if channel specs are equivalent.

**Definition** sensor.h:462

[sensor\_attr\_get](group__sensor__interface.md#gaedfdfc71dce702dc1fb1c6e60ff0f73a)

int sensor\_attr\_get(const struct device \*dev, enum sensor\_channel chan, enum sensor\_attribute attr, struct sensor\_value \*val)

Get an attribute for a sensor.

[sensor\_value\_from\_double](group__sensor__interface.md#gaf01bbb251ad0c7f6c55c5b702e8a4048)

static int sensor\_value\_from\_double(struct sensor\_value \*val, double inp)

Helper function for converting double to struct sensor\_value.

**Definition** sensor.h:1346

[sensor\_attr\_set](group__sensor__interface.md#gafbf65226a227e9f8824908bc38e336f5)

int sensor\_attr\_set(const struct device \*dev, enum sensor\_channel chan, enum sensor\_attribute attr, const struct sensor\_value \*val)

Set an attribute for a sensor.

[SENSOR\_TRIG\_DELTA](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda3bb90a3334bcf613c9efbdf2ed05f855)

@ SENSOR\_TRIG\_DELTA

Trigger fires when the selected channel varies significantly.

**Definition** sensor.h:244

[SENSOR\_TRIG\_NEAR\_FAR](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda448226d83b28c2862c353a8cda7be0d5)

@ SENSOR\_TRIG\_NEAR\_FAR

Trigger fires when a near/far event is detected.

**Definition** sensor.h:246

[SENSOR\_TRIG\_FREEFALL](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda4943ffb4afaf4cbae39e85693bd4374c)

@ SENSOR\_TRIG\_FREEFALL

Trigger fires when a free fall is detected.

**Definition** sensor.h:262

[SENSOR\_TRIG\_PRIV\_START](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda5e1a94f21fee67ee98296153ea640921)

@ SENSOR\_TRIG\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:284

[SENSOR\_TRIG\_FIFO\_FULL](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda66f913f8751a77a6c16745e329c7315c)

@ SENSOR\_TRIG\_FIFO\_FULL

Trigger fires when the FIFO becomes full.

**Definition** sensor.h:274

[SENSOR\_TRIG\_MOTION](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda7095387831b763b34171287945dae276)

@ SENSOR\_TRIG\_MOTION

Trigger fires when motion is detected.

**Definition** sensor.h:265

[SENSOR\_TRIG\_STATIONARY](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda79e286ffced716e1076f56464ea47f5d)

@ SENSOR\_TRIG\_STATIONARY

Trigger fires when no motion has been detected for a while.

**Definition** sensor.h:268

[SENSOR\_TRIG\_COMMON\_COUNT](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda8d1f2621fad4fd685d56cca3f9b042f5)

@ SENSOR\_TRIG\_COMMON\_COUNT

Number of all common sensor triggers.

**Definition** sensor.h:278

[SENSOR\_TRIG\_THRESHOLD](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda8f875f881b6540eebc28e3d6a7d46606)

@ SENSOR\_TRIG\_THRESHOLD

Trigger fires when channel reading transitions configured thresholds.

**Definition** sensor.h:253

[SENSOR\_TRIG\_MAX](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffda9de566f44de519f94c59c58df1efc4c4)

@ SENSOR\_TRIG\_MAX

Maximum value describing a sensor trigger type.

**Definition** sensor.h:289

[SENSOR\_TRIG\_DOUBLE\_TAP](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdab95e52584a6bc3343181f495cd4cb2ef)

@ SENSOR\_TRIG\_DOUBLE\_TAP

Trigger fires when a double tap is detected.

**Definition** sensor.h:259

[SENSOR\_TRIG\_TIMER](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdabf92b196394726ec90f1d61586a7f023)

@ SENSOR\_TRIG\_TIMER

Timer-based trigger, useful when the sensor does not have an interrupt line.

**Definition** sensor.h:233

[SENSOR\_TRIG\_FIFO\_WATERMARK](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdac5d67fb4fb6206465b1b01dc78245fe4)

@ SENSOR\_TRIG\_FIFO\_WATERMARK

Trigger fires when the FIFO watermark has been reached.

**Definition** sensor.h:271

[SENSOR\_TRIG\_TAP](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdae49a25e6400f0753f6bac8a7d136200d)

@ SENSOR\_TRIG\_TAP

Trigger fires when a single tap is detected.

**Definition** sensor.h:256

[SENSOR\_TRIG\_DATA\_READY](group__sensor__interface.md#gga08215279400e8c9eb05ce4e4f0898ffdaf7c161e309c267a7dd6daf2ad176f44f)

@ SENSOR\_TRIG\_DATA\_READY

Trigger fires whenever new data is ready.

**Definition** sensor.h:235

[SENSOR\_ATTR\_HYSTERESIS](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba044e67bfc04e8ddc2de7d2058fffbc94)

@ SENSOR\_ATTR\_HYSTERESIS

**Definition** sensor.h:323

[SENSOR\_ATTR\_FEATURE\_MASK](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba1f8d2242fa9d63a13c6a48fe3a1cbe52)

@ SENSOR\_ATTR\_FEATURE\_MASK

Enable/disable sensor features.

**Definition** sensor.h:343

[SENSOR\_ATTR\_CALIB\_TARGET](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba3043381b539610a8b424f12d76474bdf)

@ SENSOR\_ATTR\_CALIB\_TARGET

Calibration target.

**Definition** sensor.h:337

[SENSOR\_ATTR\_OFFSET](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba332935dcb6f7e228cb9c595a545079fd)

@ SENSOR\_ATTR\_OFFSET

The sensor value returned will be altered by the amount indicated by offset: final\_value = sensor\_val...

**Definition** sensor.h:332

[SENSOR\_ATTR\_BATCH\_DURATION](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba3b0cf69c77de55c92129e212bf5b8ced)

@ SENSOR\_ATTR\_BATCH\_DURATION

Hardware batch duration in ticks.

**Definition** sensor.h:354

[SENSOR\_ATTR\_OVERSAMPLING](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba3d32987f75284d80d3f64bf44f5c6ccd)

@ SENSOR\_ATTR\_OVERSAMPLING

Oversampling factor.

**Definition** sensor.h:325

[SENSOR\_ATTR\_FF\_DUR](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba5a62ea6aa7e55efd62ab3f93dcb0593a)

@ SENSOR\_ATTR\_FF\_DUR

Free-fall duration represented in milliseconds.

**Definition** sensor.h:351

[SENSOR\_ATTR\_UPPER\_THRESH](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba5af51bd0640a87a94476eee112a4460b)

@ SENSOR\_ATTR\_UPPER\_THRESH

Upper threshold for trigger.

**Definition** sensor.h:314

[SENSOR\_ATTR\_CONFIGURATION](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba75cd3aca26859fd7c10c83d86e3471e9)

@ SENSOR\_ATTR\_CONFIGURATION

Configure the operating modes of a sensor.

**Definition** sensor.h:339

[SENSOR\_ATTR\_RESOLUTION](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba7f20835b052b1bd6374e56f66e0f285d)

@ SENSOR\_ATTR\_RESOLUTION

**Definition** sensor.h:358

[SENSOR\_ATTR\_CALIBRATION](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba843d1e79573c634987e5e839ba9e965e)

@ SENSOR\_ATTR\_CALIBRATION

Set a calibration value needed by a sensor.

**Definition** sensor.h:341

[SENSOR\_ATTR\_COMMON\_COUNT](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940ba99ceedef81217614ada0c8a469f91eb8)

@ SENSOR\_ATTR\_COMMON\_COUNT

Number of all common sensor attributes.

**Definition** sensor.h:362

[SENSOR\_ATTR\_ALERT](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940baaedf76e63224adc3fa266d35666e0a3a)

@ SENSOR\_ATTR\_ALERT

Alert threshold or alert enable/disable.

**Definition** sensor.h:345

[SENSOR\_ATTR\_SLOPE\_TH](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bac4538665a244cb7f18fc053c40134302)

@ SENSOR\_ATTR\_SLOPE\_TH

Threshold for any-motion (slope) trigger.

**Definition** sensor.h:316

[SENSOR\_ATTR\_GAIN](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bac778fe666c284078117b2083779ba7a3)

@ SENSOR\_ATTR\_GAIN

**Definition** sensor.h:356

[SENSOR\_ATTR\_SAMPLING\_FREQUENCY](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bacb07e3508ea5503dbcdceee3f17d2291)

@ SENSOR\_ATTR\_SAMPLING\_FREQUENCY

Sensor sampling frequency, i.e.

**Definition** sensor.h:310

[SENSOR\_ATTR\_FULL\_SCALE](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bad30df3100fb6b285a6a786fdc77234d3)

@ SENSOR\_ATTR\_FULL\_SCALE

Sensor range, in SI units.

**Definition** sensor.h:327

[SENSOR\_ATTR\_LOWER\_THRESH](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940baee644485ab5f64e7c5273bbe562deaaa)

@ SENSOR\_ATTR\_LOWER\_THRESH

Lower threshold for trigger.

**Definition** sensor.h:312

[SENSOR\_ATTR\_SLOPE\_DUR](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940baf510b32b2e2395bbcf1c8fd7159ed2a1)

@ SENSOR\_ATTR\_SLOPE\_DUR

Duration for which the slope values needs to be outside the threshold for the trigger to fire.

**Definition** sensor.h:321

[SENSOR\_ATTR\_MAX](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940baf6bd0b33ca2117ef329692c291f6384b)

@ SENSOR\_ATTR\_MAX

Maximum value describing a sensor attribute type.

**Definition** sensor.h:373

[SENSOR\_ATTR\_PRIV\_START](group__sensor__interface.md#gga0dcb6842bc969492bd1c9eb49708940bafb4b5859bc369f817f60eaa161bcefc3)

@ SENSOR\_ATTR\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:368

[SENSOR\_STREAM\_DATA\_INCLUDE](group__sensor__interface.md#gga8613a20521a37d40fd7371dc63ba2daca2ba3554a08bf55b64da40900592be315)

@ SENSOR\_STREAM\_DATA\_INCLUDE

Include whatever data is associated with the trigger.

**Definition** sensor.h:613

[SENSOR\_STREAM\_DATA\_NOP](group__sensor__interface.md#gga8613a20521a37d40fd7371dc63ba2daca7e897c6d1428ff50f98140ed4cd4d35d)

@ SENSOR\_STREAM\_DATA\_NOP

Do nothing with the associated trigger data, it may be consumed later.

**Definition** sensor.h:615

[SENSOR\_STREAM\_DATA\_DROP](group__sensor__interface.md#gga8613a20521a37d40fd7371dc63ba2dacaa13c6d3bae87c16f9cd89e0fe7144f8e)

@ SENSOR\_STREAM\_DATA\_DROP

Flush/clear whatever data is associated with the trigger.

**Definition** sensor.h:617

[SENSOR\_CHAN\_GAUGE\_STATE\_OF\_HEALTH](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a0613c39397f06d11f4350f8cbcc24cf6)

@ SENSOR\_CHAN\_GAUGE\_STATE\_OF\_HEALTH

State of health measurement in %.

**Definition** sensor.h:185

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

**Definition** sensor.h:189

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

[SENSOR\_CHAN\_GRAVITY\_VECTOR](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a26fe67f0313062c6bf841ff8b829f7ff)

@ SENSOR\_CHAN\_GRAVITY\_VECTOR

Gravity Vector (X/Y/Z components in m/s^2).

**Definition** sensor.h:201

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

**Definition** sensor.h:195

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

[SENSOR\_CHAN\_GAME\_ROTATION\_VECTOR](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a3905467a96940ada0dbdef6ff8ee1a8a)

@ SENSOR\_CHAN\_GAME\_ROTATION\_VECTOR

Game Rotation Vector (unit quaternion components X/Y/Z/W).

**Definition** sensor.h:199

[SENSOR\_CHAN\_GAUGE\_AVG\_CURRENT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a4272c1256cde47006d424c5523d26bf8)

@ SENSOR\_CHAN\_GAUGE\_AVG\_CURRENT

Average current, in amps.

**Definition** sensor.h:165

[SENSOR\_CHAN\_GYRO\_Y](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a4a9533172105fd2e55d96e0122a48847)

@ SENSOR\_CHAN\_GYRO\_Y

Angular velocity around the Y axis, in radians/s.

**Definition** sensor.h:73

[SENSOR\_CHAN\_GAUGE\_DESIRED\_CHARGING\_CURRENT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a4aa8bba1b260e1994542383d8e2e908f)

@ SENSOR\_CHAN\_GAUGE\_DESIRED\_CHARGING\_CURRENT

Desired charging current in mA.

**Definition** sensor.h:197

[SENSOR\_CHAN\_FREQUENCY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a4b5a3a92ce610a2b3c9f113c93aef212)

@ SENSOR\_CHAN\_FREQUENCY

Frequency, in Hz.

**Definition** sensor.h:160

[SENSOR\_CHAN\_GAUGE\_FULL\_CHARGE\_CAPACITY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a54a6be68e09b9f8ca4d349e3d1445649)

@ SENSOR\_CHAN\_GAUGE\_FULL\_CHARGE\_CAPACITY

Full Charge Capacity in mAh.

**Definition** sensor.h:175

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

**Definition** sensor.h:167

[SENSOR\_CHAN\_GAUGE\_MAX\_LOAD\_CURRENT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a603335f6a91846c5089a2a541d9053cf)

@ SENSOR\_CHAN\_GAUGE\_MAX\_LOAD\_CURRENT

Max load current, in amps.

**Definition** sensor.h:169

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

**Definition** sensor.h:181

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

**Definition** sensor.h:193

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

**Definition** sensor.h:173

[SENSOR\_CHAN\_POS\_DXYZ](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a81fe5eca365c048c5a112071b7aca740)

@ SENSOR\_CHAN\_POS\_DXYZ

Position change on the X, Y and Z axis, in points.

**Definition** sensor.h:154

[SENSOR\_CHAN\_GBIAS\_XYZ](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a88001b6464b2419dbf2aa4ad59556110)

@ SENSOR\_CHAN\_GBIAS\_XYZ

Gyroscope bias (X/Y/Z components in radians/s).

**Definition** sensor.h:203

[SENSOR\_CHAN\_GAUGE\_CYCLE\_COUNT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a8834978858c2b62b5e923d06cfcb1a46)

@ SENSOR\_CHAN\_GAUGE\_CYCLE\_COUNT

Cycle count (total number of charge/discharge cycles).

**Definition** sensor.h:191

[SENSOR\_CHAN\_GAUGE\_TEMP](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934a8cac65c812b3a1fcb55a53f18d827214)

@ SENSOR\_CHAN\_GAUGE\_TEMP

Gauge temperature.

**Definition** sensor.h:171

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

**Definition** sensor.h:183

[SENSOR\_CHAN\_GAUGE\_TIME\_TO\_EMPTY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aa3755e9fcd8c90fef5185082edb29b65)

@ SENSOR\_CHAN\_GAUGE\_TIME\_TO\_EMPTY

Time to empty in minutes.

**Definition** sensor.h:187

[SENSOR\_CHAN\_PM\_10](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aa450541bde278aefcc9b53bd0826e225)

@ SENSOR\_CHAN\_PM\_10

10 micro-meters Particulate Matter, in ug/m^3

**Definition** sensor.h:117

[SENSOR\_CHAN\_GAUGE\_REMAINING\_CHARGE\_CAPACITY](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934aaaea6433c82f7b563f86fa53c95ad0ad)

@ SENSOR\_CHAN\_GAUGE\_REMAINING\_CHARGE\_CAPACITY

Remaining Charge Capacity in mAh.

**Definition** sensor.h:177

[SENSOR\_CHAN\_ALL](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ab275027eb550b2b075c44917634eca2c)

@ SENSOR\_CHAN\_ALL

All channels.

**Definition** sensor.h:206

[SENSOR\_CHAN\_GAUGE\_VOLTAGE](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ab942649ce1507fb081a77b4bcfc1a57d)

@ SENSOR\_CHAN\_GAUGE\_VOLTAGE

Voltage, in volts.

**Definition** sensor.h:163

[SENSOR\_CHAN\_PROX](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934abaec2c1347ef0035221dd4d9c34a4774)

@ SENSOR\_CHAN\_PROX

Proximity.

**Definition** sensor.h:96

[SENSOR\_CHAN\_COMMON\_COUNT](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934abb2893ccb71c9e1eeb155d7cbd539303)

@ SENSOR\_CHAN\_COMMON\_COUNT

Number of all common sensor channels.

**Definition** sensor.h:211

[SENSOR\_CHAN\_PRIV\_START](group__sensor__interface.md#ggaaa1b502bc029b10d7b23b0a25ef4e934ac1f260296289d93a13c5686ca11bdc12)

@ SENSOR\_CHAN\_PRIV\_START

This and higher values are sensor specific.

**Definition** sensor.h:217

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

**Definition** sensor.h:222

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

**Definition** sensor.h:179

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

**Definition** util\_macro.h:148

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

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

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

**Definition** device.h:453

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:459

[rtio\_cqe](structrtio__cqe.md)

A completion queue event.

**Definition** rtio.h:363

[rtio\_cqe::userdata](structrtio__cqe.md#a15128387ccbea55812ef229eab7241e7)

void \* userdata

Associated userdata with operation.

**Definition** rtio.h:367

[rtio\_cqe::result](structrtio__cqe.md#acbe2e6607a752b676d9336b9ca6ce435)

int32\_t result

Result from operation.

**Definition** rtio.h:366

[rtio\_iodev\_api](structrtio__iodev__api.md)

API that an RTIO IO device should implement.

**Definition** rtio.h:502

[rtio\_iodev\_sqe](structrtio__iodev__sqe.md)

Compute the mempool block index for a given pointer.

**Definition** rtio.h:492

[rtio\_iodev\_sqe::sqe](structrtio__iodev__sqe.md#a2bd98599678909c0ddb22f879affa12b)

struct rtio\_sqe sqe

**Definition** rtio.h:493

[rtio\_iodev](structrtio__iodev.md)

An IO device with a function table for submitting requests.

**Definition** rtio.h:517

[rtio\_iodev::data](structrtio__iodev.md#af0f3a27fe8dea2161c9a73cb838bdeec)

void \* data

**Definition** rtio.h:522

[rtio\_sqe](structrtio__sqe.md)

A submission queue event.

**Definition** rtio.h:286

[rtio\_sqe::userdata](structrtio__sqe.md#a0ed519ee0b5867ff73bdaf37f983c971)

void \* userdata

User provided data which is returned upon operation completion.

**Definition** rtio.h:304

[rtio\_sqe::buf\_len](structrtio__sqe.md#a67376f40a13960b152a23da250275722)

uint32\_t buf\_len

Length of buffer.

**Definition** rtio.h:310

[rtio\_sqe::iodev](structrtio__sqe.md#a6c784702f011592c84feacd57915bbfc)

const struct rtio\_iodev \* iodev

Device to operation on.

**Definition** rtio.h:295

[rtio\_sqe::buf](structrtio__sqe.md#ab71176c084e8b8eb65dfeb3018ae2a49)

const uint8\_t \* buf

Buffer to write from.

**Definition** rtio.h:311

[rtio](structrtio.md)

An RTIO context containing what can be viewed as a pair of queues.

**Definition** rtio.h:396

[sensor\_chan\_spec](structsensor__chan__spec.md)

Sensor Channel Specification.

**Definition** sensor.h:443

[sensor\_chan\_spec::chan\_idx](structsensor__chan__spec.md#a00d4a927cfeae33b2beea8cdc415dda1)

uint16\_t chan\_idx

A sensor channel index.

**Definition** sensor.h:445

[sensor\_chan\_spec::chan\_type](structsensor__chan__spec.md#a1b2f0ecdc23e0d235536eb5fcdeeb63c)

uint16\_t chan\_type

A sensor channel type.

**Definition** sensor.h:444

[sensor\_data\_generic\_header](structsensor__data__generic__header.md)

**Definition** sensor.h:921

[sensor\_data\_generic\_header::timestamp\_ns](structsensor__data__generic__header.md#a429e22b3191df271ccfe321b796e1ac9)

uint64\_t timestamp\_ns

**Definition** sensor.h:923

[sensor\_data\_generic\_header::shift](structsensor__data__generic__header.md#a68067521c1058b6802176e1d48fed788)

int8\_t shift

**Definition** sensor.h:932

[sensor\_data\_generic\_header::num\_channels](structsensor__data__generic__header.md#a7edbe674f28c95f3aa40b1df84ca61fe)

uint32\_t num\_channels

**Definition** sensor.h:929

[sensor\_data\_generic\_header::channels](structsensor__data__generic__header.md#ac09f23959c66ff75b0854a95e8d4504b)

struct sensor\_chan\_spec channels[0]

**Definition** sensor.h:938

[sensor\_decode\_context](structsensor__decode__context.md)

Used for iterating over the data frames via the sensor\_decoder\_api.

**Definition** sensor.h:565

[sensor\_decode\_context::decoder](structsensor__decode__context.md#a1ac0773e83a086455371d108264ef4f6)

const struct sensor\_decoder\_api \* decoder

**Definition** sensor.h:566

[sensor\_decode\_context::channel](structsensor__decode__context.md#a1c051bd8d0030f81cc561e32b2897d74)

struct sensor\_chan\_spec channel

**Definition** sensor.h:568

[sensor\_decode\_context::buffer](structsensor__decode__context.md#a23e27eb0687d722be78e1b89278613d1)

const uint8\_t \* buffer

**Definition** sensor.h:567

[sensor\_decode\_context::fit](structsensor__decode__context.md#ada9e40625829093087886c41f2fb7350)

uint32\_t fit

**Definition** sensor.h:569

[sensor\_decoder\_api](structsensor__decoder__api.md)

Decodes a single raw data buffer.

**Definition** sensor.h:475

[sensor\_decoder\_api::get\_size\_info](structsensor__decoder__api.md#a026be8086386e9eea0a1cb25c1cd602e)

int(\* get\_size\_info)(struct sensor\_chan\_spec channel, size\_t \*base\_size, size\_t \*frame\_size)

Get the size required to decode a given channel.

**Definition** sensor.h:500

[sensor\_decoder\_api::get\_frame\_count](structsensor__decoder__api.md#a16c0b0f1a3a13d037b9ffcbf348da1f5)

int(\* get\_frame\_count)(const uint8\_t \*buffer, struct sensor\_chan\_spec channel, uint16\_t \*frame\_count)

Get the number of frames in the current buffer.

**Definition** sensor.h:485

[sensor\_decoder\_api::decode](structsensor__decoder__api.md#a1d24e69b5c2f0c41ce175de2aa2618db)

int(\* decode)(const uint8\_t \*buffer, struct sensor\_chan\_spec channel, uint32\_t \*fit, uint16\_t max\_count, void \*data\_out)

Decode up to max\_count samples from the buffer.

**Definition** sensor.h:528

[sensor\_decoder\_api::has\_trigger](structsensor__decoder__api.md#a78706bae0f1314615b5804736ef43493)

bool(\* has\_trigger)(const uint8\_t \*buffer, enum sensor\_trigger\_type trigger)

Check if the given trigger type is present.

**Definition** sensor.h:538

[sensor\_driver\_api](structsensor__driver__api.md)

**Definition** sensor.h:710

[sensor\_driver\_api::get\_decoder](structsensor__driver__api.md#a004f9d342805dc72249ab9b8c17a544b)

sensor\_get\_decoder\_t get\_decoder

**Definition** sensor.h:716

[sensor\_driver\_api::attr\_set](structsensor__driver__api.md#a2d230a976b19a699d132034f58bb2b6a)

sensor\_attr\_set\_t attr\_set

**Definition** sensor.h:711

[sensor\_driver\_api::attr\_get](structsensor__driver__api.md#a3e28950f844c3f8b8da5ba9ff8052e46)

sensor\_attr\_get\_t attr\_get

**Definition** sensor.h:712

[sensor\_driver\_api::trigger\_set](structsensor__driver__api.md#a4708070fd6654ecbbe631819aba319bd)

sensor\_trigger\_set\_t trigger\_set

**Definition** sensor.h:713

[sensor\_driver\_api::sample\_fetch](structsensor__driver__api.md#a4b40e25b81fe070e2f6bdcf7f8a4a31f)

sensor\_sample\_fetch\_t sample\_fetch

**Definition** sensor.h:714

[sensor\_driver\_api::channel\_get](structsensor__driver__api.md#a667b41bf51f2c7a6bb31713fbf889113)

sensor\_channel\_get\_t channel\_get

**Definition** sensor.h:715

[sensor\_driver\_api::submit](structsensor__driver__api.md#ae3ba0adeba21351e8f660896e5a0e702)

sensor\_submit\_t submit

**Definition** sensor.h:717

[sensor\_read\_config](structsensor__read__config.md)

**Definition** sensor.h:634

[sensor\_read\_config::channels](structsensor__read__config.md#a2aff44f02b25fd4ad1d4bc217800fad1)

struct sensor\_chan\_spec \*const channels

**Definition** sensor.h:638

[sensor\_read\_config::count](structsensor__read__config.md#a5236049e0563ebba754994d70e22383a)

size\_t count

**Definition** sensor.h:641

[sensor\_read\_config::triggers](structsensor__read__config.md#a6eaa6df7bc9378abe0f5b4b8c9a05909)

struct sensor\_stream\_trigger \*const triggers

**Definition** sensor.h:639

[sensor\_read\_config::is\_streaming](structsensor__read__config.md#aca96de2c23fb63f887c4c40dcb272798)

const bool is\_streaming

**Definition** sensor.h:636

[sensor\_read\_config::sensor](structsensor__read__config.md#ad49d5ab5293017d1ad2cf60adc542090)

const struct device \* sensor

**Definition** sensor.h:635

[sensor\_read\_config::max](structsensor__read__config.md#aecb9c899e292fdb25c3c990bdaf1c76b)

const size\_t max

**Definition** sensor.h:642

[sensor\_stream\_trigger](structsensor__stream__trigger.md)

**Definition** sensor.h:620

[sensor\_stream\_trigger::opt](structsensor__stream__trigger.md#a62ccdecf7253b1bfdff4f1d659563d76)

enum sensor\_stream\_data\_opt opt

**Definition** sensor.h:622

[sensor\_stream\_trigger::trigger](structsensor__stream__trigger.md#a9a367e746764e68140ec9120f2a016e6)

enum sensor\_trigger\_type trigger

**Definition** sensor.h:621

[sensor\_trigger](structsensor__trigger.md)

Sensor trigger spec.

**Definition** sensor.h:295

[sensor\_trigger::type](structsensor__trigger.md#ac2cce1ec6ff82f95cb06d0dccafd7af0)

enum sensor\_trigger\_type type

Trigger type.

**Definition** sensor.h:297

[sensor\_trigger::chan](structsensor__trigger.md#ae01f99b124aa99c59b9967818022e112)

enum sensor\_channel chan

Channel the trigger is set on.

**Definition** sensor.h:299

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

**Definition** xcc.h:104

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sensor.h](sensor_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
