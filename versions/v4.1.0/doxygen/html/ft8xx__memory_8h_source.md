---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ft8xx__memory_8h_source.html
original_path: doxygen/html/ft8xx__memory_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ft8xx\_memory.h

[Go to the documentation of this file.](ft8xx__memory_8h.md)

1/\*

2 \* Copyright (c) 2020 Hubert Miś

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_DRIVERS\_MISC\_FT8XX\_FT8XX\_MEMORY\_H\_

13#define ZEPHYR\_DRIVERS\_MISC\_FT8XX\_FT8XX\_MEMORY\_H\_

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

25

[ 27](group__ft8xx__memory.md#ga91adc1665d20e88c087ddb10b5e5ef69)enum [ft800\_memory\_map\_t](group__ft8xx__memory.md#ga91adc1665d20e88c087ddb10b5e5ef69) {

[ 28](group__ft8xx__memory.md#gga91adc1665d20e88c087ddb10b5e5ef69a0f292b470f74c0c625292850d1f6d91c) [FT800\_RAM\_G](group__ft8xx__memory.md#gga91adc1665d20e88c087ddb10b5e5ef69a0f292b470f74c0c625292850d1f6d91c) = 0x000000,

[ 29](group__ft8xx__memory.md#gga91adc1665d20e88c087ddb10b5e5ef69ae186b0781a832f3adedb21e9d2e05300) [FT800\_ROM\_CHIPID](group__ft8xx__memory.md#gga91adc1665d20e88c087ddb10b5e5ef69ae186b0781a832f3adedb21e9d2e05300) = 0x0C0000,

[ 30](group__ft8xx__memory.md#gga91adc1665d20e88c087ddb10b5e5ef69a4f2b840d1343d34a13f5859f35241714) [FT800\_ROM\_FONT](group__ft8xx__memory.md#gga91adc1665d20e88c087ddb10b5e5ef69a4f2b840d1343d34a13f5859f35241714) = 0x0BB23C,

[ 31](group__ft8xx__memory.md#gga91adc1665d20e88c087ddb10b5e5ef69a0b846c1c3f54c88a66fee75ae1310893) [FT800\_ROM\_FONT\_ADDR](group__ft8xx__memory.md#gga91adc1665d20e88c087ddb10b5e5ef69a0b846c1c3f54c88a66fee75ae1310893) = 0x0FFFFC,

[ 32](group__ft8xx__memory.md#gga91adc1665d20e88c087ddb10b5e5ef69ad7f0dc26c1313aa315bbeba0b648a013) [FT800\_RAM\_DL](group__ft8xx__memory.md#gga91adc1665d20e88c087ddb10b5e5ef69ad7f0dc26c1313aa315bbeba0b648a013) = 0x100000,

[ 33](group__ft8xx__memory.md#gga91adc1665d20e88c087ddb10b5e5ef69a5a01dedda4d91a94bb7dd42eeef5f357) [FT800\_RAM\_PAL](group__ft8xx__memory.md#gga91adc1665d20e88c087ddb10b5e5ef69a5a01dedda4d91a94bb7dd42eeef5f357) = 0x102000,

[ 34](group__ft8xx__memory.md#gga91adc1665d20e88c087ddb10b5e5ef69a4a88dd5f6ec5d1adf451467db195604c) [FT800\_REG\_](group__ft8xx__memory.md#gga91adc1665d20e88c087ddb10b5e5ef69a4a88dd5f6ec5d1adf451467db195604c) = 0x102400,

[ 35](group__ft8xx__memory.md#gga91adc1665d20e88c087ddb10b5e5ef69a2c37aff19d6aa8801f257bc689428373) [FT800\_RAM\_CMD](group__ft8xx__memory.md#gga91adc1665d20e88c087ddb10b5e5ef69a2c37aff19d6aa8801f257bc689428373) = 0x108000

36};

37

[ 39](group__ft8xx__memory.md#ga6c8d08697812fb4e6292ff533e753aee)enum [ft810\_memory\_map\_t](group__ft8xx__memory.md#ga6c8d08697812fb4e6292ff533e753aee) {

[ 40](group__ft8xx__memory.md#gga6c8d08697812fb4e6292ff533e753aeeaa5619b0f2ba721cfc070ee09886af264) [FT810\_RAM\_G](group__ft8xx__memory.md#gga6c8d08697812fb4e6292ff533e753aeeaa5619b0f2ba721cfc070ee09886af264) = 0x000000,

[ 41](group__ft8xx__memory.md#gga6c8d08697812fb4e6292ff533e753aeea408b88147f94626dabe1e8b81f72b9ea) [FT810\_RAM\_DL](group__ft8xx__memory.md#gga6c8d08697812fb4e6292ff533e753aeea408b88147f94626dabe1e8b81f72b9ea) = 0x300000,

[ 42](group__ft8xx__memory.md#gga6c8d08697812fb4e6292ff533e753aeea0f483ff9a2c538fccc2326f431201a57) [FT810\_REG\_](group__ft8xx__memory.md#gga6c8d08697812fb4e6292ff533e753aeea0f483ff9a2c538fccc2326f431201a57) = 0x302000,

[ 43](group__ft8xx__memory.md#gga6c8d08697812fb4e6292ff533e753aeea06a9355b36b87b1b0fa79a6f468e46bb) [FT810\_RAM\_CMD](group__ft8xx__memory.md#gga6c8d08697812fb4e6292ff533e753aeea06a9355b36b87b1b0fa79a6f468e46bb) = 0x308000

44};

45

[ 47](group__ft8xx__memory.md#ga3c885b333acd851fed4d74886656d2c6)enum [ft800\_register\_address\_t](group__ft8xx__memory.md#ga3c885b333acd851fed4d74886656d2c6) {

[ 48](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a7946c63f4dd93692634c08ec0b4657e4) [FT800\_REG\_ID](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a7946c63f4dd93692634c08ec0b4657e4) = 0x102400,

[ 49](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aa45d948244f4decd8863f5def65a78db) [FT800\_REG\_FRAMES](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aa45d948244f4decd8863f5def65a78db) = 0x102404,

[ 50](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a46376ddea2bccf9e0af33d78a05f635a) [FT800\_REG\_CLOCK](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a46376ddea2bccf9e0af33d78a05f635a) = 0x102408,

[ 51](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a0a864b5230c4ed04ac4a18f7e9c85af5) [FT800\_REG\_FREQUENCY](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a0a864b5230c4ed04ac4a18f7e9c85af5) = 0x10240C,

[ 52](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a1ca1c284f1f3e2ae75c4874f0c569c7c) [FT800\_REG\_RENDERMODE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a1ca1c284f1f3e2ae75c4874f0c569c7c) = 0x102410,

[ 53](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a6bcedb4e986dba59c0c689356022d992) [FT800\_REG\_SNAPY](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a6bcedb4e986dba59c0c689356022d992) = 0x102414,

[ 54](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a382043bf7f2381a4fad71adeae73db2d) [FT800\_REG\_SNAPSHOT](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a382043bf7f2381a4fad71adeae73db2d) = 0x102418,

[ 55](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a4411395eca792d4d23f63242fea6307e) [FT800\_REG\_CPURESET](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a4411395eca792d4d23f63242fea6307e) = 0x10241C,

[ 56](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a2b36ffdd93c6f41bd08f732099608a99) [FT800\_REG\_TAP\_CRC](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a2b36ffdd93c6f41bd08f732099608a99) = 0x102420,

[ 57](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a3c6f1a0898055d4eec3ddfbde56f6a51) [FT800\_REG\_TAP\_MASK](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a3c6f1a0898055d4eec3ddfbde56f6a51) = 0x102424,

[ 58](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aa2b46aa7465a2e38a9947e0b5868f6c7) [FT800\_REG\_HCYCLE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aa2b46aa7465a2e38a9947e0b5868f6c7) = 0x102428,

[ 59](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a3179545d22570761b9bf0598ff24219a) [FT800\_REG\_HOFFSET](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a3179545d22570761b9bf0598ff24219a) = 0x10242C,

[ 60](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a7b46068735f066e0d2fa6a0ccb073001) [FT800\_REG\_HSIZE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a7b46068735f066e0d2fa6a0ccb073001) = 0x102430,

[ 61](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a5d365f03f5dcd630191f050963c4fc9c) [FT800\_REG\_HSYNC0](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a5d365f03f5dcd630191f050963c4fc9c) = 0x102434,

[ 62](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a7c4d1b3a4a5dc128d52fd91352342a70) [FT800\_REG\_HSYNC1](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a7c4d1b3a4a5dc128d52fd91352342a70) = 0x102438,

[ 63](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aaf8bdfc1924c2269c9db3933499cd23c) [FT800\_REG\_VCYCLE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aaf8bdfc1924c2269c9db3933499cd23c) = 0x10243C,

[ 64](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a7d9903cc3452f77287ce411c831e6567) [FT800\_REG\_VOFFSET](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a7d9903cc3452f77287ce411c831e6567) = 0x102440,

[ 65](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a2f17cc86a455d13b2f92ada17319a94e) [FT800\_REG\_VSIZE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a2f17cc86a455d13b2f92ada17319a94e) = 0x102444,

[ 66](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a0a6dcbe431ec103262ee805acaee9897) [FT800\_REG\_VSYNC0](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a0a6dcbe431ec103262ee805acaee9897) = 0x102448,

[ 67](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6abcd84b4d56e71b558a79f10d97b66ea1) [FT800\_REG\_VSYNC1](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6abcd84b4d56e71b558a79f10d97b66ea1) = 0x10244C,

[ 68](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a9f726cc401387bbe8aa3366047467688) [FT800\_REG\_DLSWAP](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a9f726cc401387bbe8aa3366047467688) = 0x102450,

[ 69](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ab9bf90e77f7946d4466e3b8d444d64e4) [FT800\_REG\_ROTATE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ab9bf90e77f7946d4466e3b8d444d64e4) = 0x102454,

[ 70](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a3d5e1b30a5d1889b14b77f8a4bfecf7b) [FT800\_REG\_OUTBITS](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a3d5e1b30a5d1889b14b77f8a4bfecf7b) = 0x102458,

[ 71](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a2ba06eef07c7b881c2b331aa090329ed) [FT800\_REG\_DITHER](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a2ba06eef07c7b881c2b331aa090329ed) = 0x10245C,

[ 72](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a161a252ef247cad31f812c88fbfcdf6f) [FT800\_REG\_SWIZZLE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a161a252ef247cad31f812c88fbfcdf6f) = 0x102460,

[ 73](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aaf65490a7a4b55309bc8943b065eef17) [FT800\_REG\_CSPREAD](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aaf65490a7a4b55309bc8943b065eef17) = 0x102464,

[ 74](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a9ded0eeda09a9cce3bf111c0a49dd391) [FT800\_REG\_PCLK\_POL](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a9ded0eeda09a9cce3bf111c0a49dd391) = 0x102468,

[ 75](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a8947fb21fa7a7fa4a26bdaea5dbe79c5) [FT800\_REG\_PCLK](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a8947fb21fa7a7fa4a26bdaea5dbe79c5) = 0x10246C,

[ 76](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a424e4e6fb301bb6833a46f813fc5895a) [FT800\_REG\_TAG\_X](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a424e4e6fb301bb6833a46f813fc5895a) = 0x102470,

[ 77](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a7f8c3d2a08a68b741ded594eafbfaae4) [FT800\_REG\_TAG\_Y](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a7f8c3d2a08a68b741ded594eafbfaae4) = 0x102474,

[ 78](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a83136b05a9a6f64867f39c50fb0079d2) [FT800\_REG\_TAG](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a83136b05a9a6f64867f39c50fb0079d2) = 0x102478,

[ 79](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a4f0e1449b7ab28bf29f52bf3544c442f) [FT800\_REG\_VOL\_PB](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a4f0e1449b7ab28bf29f52bf3544c442f) = 0x10247C,

[ 80](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a5672933c464d2408ad0a6a046fddc1d2) [FT800\_REG\_VOL\_SOUND](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a5672933c464d2408ad0a6a046fddc1d2) = 0x102480,

[ 81](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a2f0f00e3bbd1b9f9fb09c9d2b65382d7) [FT800\_REG\_SOUND](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a2f0f00e3bbd1b9f9fb09c9d2b65382d7) = 0x102484,

[ 82](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a0187a790b87eca35892431c600248e71) [FT800\_REG\_PLAY](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a0187a790b87eca35892431c600248e71) = 0x102488,

[ 83](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a2c4d02cf887f3ec87b99cd32ae8b355b) [FT800\_REG\_GPIO\_DIR](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a2c4d02cf887f3ec87b99cd32ae8b355b) = 0x10248C,

[ 84](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6af7d0154293ba1228a0e04bb923bf9b39) [FT800\_REG\_GPIO](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6af7d0154293ba1228a0e04bb923bf9b39) = 0x102490,

85

[ 86](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a4fbbc34adc25d9147f2a8007a537ddbd) [FT800\_REG\_INT\_FLAGS](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a4fbbc34adc25d9147f2a8007a537ddbd) = 0x102498,

[ 87](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aa31af794f56d1f4f831ef65c3daf1087) [FT800\_REG\_INT\_EN](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aa31af794f56d1f4f831ef65c3daf1087) = 0x10249C,

[ 88](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aa6461f2c17d723ecd672babedbb1e9fc) [FT800\_REG\_INT\_MASK](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aa6461f2c17d723ecd672babedbb1e9fc) = 0x1024A0,

[ 89](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ac159bfb8d704e46aa4be4859d1e476af) [FT800\_REG\_PLAYBACK\_START](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ac159bfb8d704e46aa4be4859d1e476af) = 0x1024A4,

[ 90](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a097806c1c7281e5cbaf0e992888c2e97) [FT800\_REG\_PLAYBACK\_LENGTH](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a097806c1c7281e5cbaf0e992888c2e97) = 0x1024A8,

[ 91](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aec4e118a3fe1cf3e1f2b5df6b376a651) [FT800\_REG\_PLAYBACK\_READPTR](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aec4e118a3fe1cf3e1f2b5df6b376a651) = 0x1024AC,

[ 92](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aa8c6fb57011ad08bf0a1d0b48eb5599a) [FT800\_REG\_PLAYBACK\_FREQ](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aa8c6fb57011ad08bf0a1d0b48eb5599a) = 0x1024B0,

[ 93](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a13f744aa7a089e177a36623239d12961) [FT800\_REG\_PLAYBACK\_FORMAT](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a13f744aa7a089e177a36623239d12961) = 0x1024B4,

[ 94](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ab62b5bbfdf948265ad10129ead4d8a63) [FT800\_REG\_PLAYBACK\_LOOP](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ab62b5bbfdf948265ad10129ead4d8a63) = 0x1024B8,

[ 95](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a15006a5d2ab004ca8b5a9a75be095b5b) [FT800\_REG\_PLAYBACK\_PLAY](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a15006a5d2ab004ca8b5a9a75be095b5b) = 0x1024BC,

[ 96](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ac321e2d68978123ab259a2d84d186719) [FT800\_REG\_PWM\_HZ](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ac321e2d68978123ab259a2d84d186719) = 0x1024C0,

[ 97](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ae14e09a184dbe44390ce7d5576b30d4c) [FT800\_REG\_PWM\_DUTY](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ae14e09a184dbe44390ce7d5576b30d4c) = 0x1024C4,

[ 98](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ae95328740c30d541b4dc79466734306c) [FT800\_REG\_MACRO\_0](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ae95328740c30d541b4dc79466734306c) = 0x1024C8,

[ 99](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a9bce17c193b9c809bef0770bc65b37cf) [FT800\_REG\_MACRO\_1](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a9bce17c193b9c809bef0770bc65b37cf) = 0x1024CC,

100

[ 101](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aa2cb7424ec77d9a35179824cd2fecb47) [FT800\_REG\_CMD\_READ](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aa2cb7424ec77d9a35179824cd2fecb47) = 0x1024E4,

[ 102](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a4911a990964958a6e2bf4842e87ab101) [FT800\_REG\_CMD\_WRITE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a4911a990964958a6e2bf4842e87ab101) = 0x1024E8,

[ 103](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a23f9fdc1d48d6410fc600359842b16ea) [FT800\_REG\_CMD\_DL](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a23f9fdc1d48d6410fc600359842b16ea) = 0x1024EC,

[ 104](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ada6b5afbed95413c1988131384c02b1b) [FT800\_REG\_TOUCH\_MODE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ada6b5afbed95413c1988131384c02b1b) = 0x1024F0,

[ 105](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a65b43042fe7dbc44bd15fb472bba33a4) [FT800\_REG\_TOUCH\_ADC\_MODE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a65b43042fe7dbc44bd15fb472bba33a4) = 0x1024F4,

[ 106](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a69b981de24b4da81175c9ac74c8454f5) [FT800\_REG\_TOUCH\_CHARGE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a69b981de24b4da81175c9ac74c8454f5) = 0x1024F8,

[ 107](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ae02db7afd08bd1c06f6e1f9e06e81d33) [FT800\_REG\_TOUCH\_SETTLE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ae02db7afd08bd1c06f6e1f9e06e81d33) = 0x1024FC,

[ 108](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a87e989861d85d683c95e8de44f74f58b) [FT800\_REG\_TOUCH\_OVERSAMPLE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a87e989861d85d683c95e8de44f74f58b) = 0x102500,

[ 109](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a70f721a708b36ef255270d02680e4e7f) [FT800\_REG\_TOUCH\_RZTHRESH](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a70f721a708b36ef255270d02680e4e7f) = 0x102504,

[ 110](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a8ef80aeaaffd974b2e246ad15c98f916) [FT800\_REG\_TOUCH\_RAW\_XY](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a8ef80aeaaffd974b2e246ad15c98f916) = 0x102508,

[ 111](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ab66136540b44e2f37a0f920fbd3cbcc4) [FT800\_REG\_TOUCH\_RZ](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ab66136540b44e2f37a0f920fbd3cbcc4) = 0x10250C,

[ 112](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a99fc0fc08ee942b7783951674837d57d) [FT800\_REG\_TOUCH\_SCREEN\_XY](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a99fc0fc08ee942b7783951674837d57d) = 0x102510,

[ 113](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a86ba740c280900a1dd4273422b9ca8b6) [FT800\_REG\_TOUCH\_TAG\_XY](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a86ba740c280900a1dd4273422b9ca8b6) = 0x102514,

[ 114](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a245e5594218702bc2c30c1b50ec44329) [FT800\_REG\_TOUCH\_TAG](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a245e5594218702bc2c30c1b50ec44329) = 0x102518,

[ 115](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a183fd00d406e113b8b72b8c5b5fc5880) [FT800\_REG\_TOUCH\_TRANSFORM\_A](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a183fd00d406e113b8b72b8c5b5fc5880) = 0x10251C,

[ 116](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6acd3161021e315e1a2f91f21ccdc48d8a) [FT800\_REG\_TOUCH\_TRANSFORM\_B](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6acd3161021e315e1a2f91f21ccdc48d8a) = 0x102520,

[ 117](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a4b3e903dfed68a7eb7f7734e18aca9e0) [FT800\_REG\_TOUCH\_TRANSFORM\_C](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a4b3e903dfed68a7eb7f7734e18aca9e0) = 0x102524,

[ 118](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a386a6293cd82485934b3865bd3f1956b) [FT800\_REG\_TOUCH\_TRANSFORM\_D](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a386a6293cd82485934b3865bd3f1956b) = 0x102528,

[ 119](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a4f188f88f9a032fdb6f3c87ed352d4bb) [FT800\_REG\_TOUCH\_TRANSFORM\_E](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a4f188f88f9a032fdb6f3c87ed352d4bb) = 0x10252C,

[ 120](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a1d01f5fe890a4d7670cf91a7cd48402f) [FT800\_REG\_TOUCH\_TRANSFORM\_F](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a1d01f5fe890a4d7670cf91a7cd48402f) = 0x102530,

121

[ 122](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a1745bb57bcf9872b308c49a151a43f1f) [FT800\_REG\_TOUCH\_DIRECT\_XY](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a1745bb57bcf9872b308c49a151a43f1f) = 0x102574,

[ 123](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a43bcc194c075b385073ed73a562b8cfa) [FT800\_REG\_TOUCH\_DIRECT\_Z1Z2](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a43bcc194c075b385073ed73a562b8cfa) = 0x102578,

124

[ 125](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a3397b2a86a97997d01780d52ec23b84c) [FT800\_REG\_TRACKER](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a3397b2a86a97997d01780d52ec23b84c) = 0x109000

126};

127

[ 129](group__ft8xx__memory.md#ga495a8c0706389e9b3677846d772eb352)enum [ft810\_register\_address\_t](group__ft8xx__memory.md#ga495a8c0706389e9b3677846d772eb352) {

[ 130](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ad35d6fc19bc4fe86802105c48489553e) [FT810\_REG\_TRIM](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ad35d6fc19bc4fe86802105c48489553e) = 0x10256C,

131

[ 132](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a8e81832420166c89993a4f0629d5765d) [FT810\_REG\_ID](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a8e81832420166c89993a4f0629d5765d) = 0x302000,

[ 133](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ab75607baa4c4121c34364f4118f990d2) [FT810\_REG\_FRAMES](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ab75607baa4c4121c34364f4118f990d2) = 0x302004,

[ 134](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a222e9d43895af76d103f9fbd09c40832) [FT810\_REG\_CLOCK](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a222e9d43895af76d103f9fbd09c40832) = 0x302008,

[ 135](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a3f09f2fd706996b97173f587637aee53) [FT810\_REG\_FREQUENCY](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a3f09f2fd706996b97173f587637aee53) = 0x30200C,

[ 136](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a32f5dfe4ebc13114ecf9336670f74a31) [FT810\_REG\_RENDERMODE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a32f5dfe4ebc13114ecf9336670f74a31) = 0x302010,

[ 137](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a1f9721ea190d82af17332d60cb8eb795) [FT810\_REG\_SNAPY](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a1f9721ea190d82af17332d60cb8eb795) = 0x302014,

[ 138](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a104e72273989d38213fc070b4fd4a676) [FT810\_REG\_SNAPSHOT](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a104e72273989d38213fc070b4fd4a676) = 0x302018,

[ 139](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ae2bae2d6191190c95a76e4cc1a6bc9d1) [FT810\_REG\_CPURESET](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ae2bae2d6191190c95a76e4cc1a6bc9d1) = 0x302020,

[ 140](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a6e302da1712f086b26d08e46f7a9f1d1) [FT810\_REG\_TAP\_CRC](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a6e302da1712f086b26d08e46f7a9f1d1) = 0x302020,

[ 141](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a369d654c43692ef193493063338888aa) [FT810\_REG\_TAP\_MASK](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a369d654c43692ef193493063338888aa) = 0x302024,

[ 142](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a68ae24f87a50c7790ac987c6e2ccab2b) [FT810\_REG\_HCYCLE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a68ae24f87a50c7790ac987c6e2ccab2b) = 0x30202C,

[ 143](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a95853b0fc36aca1c168611334a39037f) [FT810\_REG\_HOFFSET](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a95853b0fc36aca1c168611334a39037f) = 0x302030,

[ 144](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352af89832af70c53e320337f633985ce295) [FT810\_REG\_HSIZE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352af89832af70c53e320337f633985ce295) = 0x302034,

[ 145](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a086b28d18b9c49e51ef734c2f6e6ce21) [FT810\_REG\_HSYNC0](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a086b28d18b9c49e51ef734c2f6e6ce21) = 0x302038,

[ 146](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a533ec4682d3b9649a59e012a53ab55de) [FT810\_REG\_HSYNC1](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a533ec4682d3b9649a59e012a53ab55de) = 0x30203C,

[ 147](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a9e43b1a3872c21a26981a35c03fea93d) [FT810\_REG\_VCYCLE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a9e43b1a3872c21a26981a35c03fea93d) = 0x302040,

[ 148](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a2a155f858da556270114a3f9d989ef85) [FT810\_REG\_VOFFSET](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a2a155f858da556270114a3f9d989ef85) = 0x302044,

[ 149](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352acafecb336293cd24b363e33ca9fdce5a) [FT810\_REG\_VSIZE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352acafecb336293cd24b363e33ca9fdce5a) = 0x302048,

[ 150](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352afd3caed713df1d318d62cbd73fdfe3c6) [FT810\_REG\_VSYNC0](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352afd3caed713df1d318d62cbd73fdfe3c6) = 0x30204C,

[ 151](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a3deeabcda1f9453dc2d865e8b19715a8) [FT810\_REG\_VSYNC1](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a3deeabcda1f9453dc2d865e8b19715a8) = 0x302050,

[ 152](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352afb81eec26bd13732949ae8f8186fdd26) [FT810\_REG\_DLSWAP](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352afb81eec26bd13732949ae8f8186fdd26) = 0x302054,

[ 153](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a54935aeb6c13623f68c5c74c3db722ff) [FT810\_REG\_ROTATE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a54935aeb6c13623f68c5c74c3db722ff) = 0x302058,

[ 154](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aff30b9219c582c8ceac17f115a18375d) [FT810\_REG\_OUTBITS](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aff30b9219c582c8ceac17f115a18375d) = 0x30205C,

[ 155](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a61e1d7c2e2ed9a0ee4b372dd9c7df63a) [FT810\_REG\_DITHER](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a61e1d7c2e2ed9a0ee4b372dd9c7df63a) = 0x302060,

[ 156](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ad633919822dadc636420824948e75315) [FT810\_REG\_SWIZZLE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ad633919822dadc636420824948e75315) = 0x302064,

[ 157](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352abfa8c39566c4c41501588b815a5c52ad) [FT810\_REG\_CSPREAD](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352abfa8c39566c4c41501588b815a5c52ad) = 0x302068,

[ 158](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a83d5ff35dc2d6af8e461a45ea2239af6) [FT810\_REG\_PCLK\_POL](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a83d5ff35dc2d6af8e461a45ea2239af6) = 0x30206C,

[ 159](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aff03cfb6400f883999cc01c0cf832812) [FT810\_REG\_PCLK](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aff03cfb6400f883999cc01c0cf832812) = 0x302070,

[ 160](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ab45bcc55b80d016ef2ac8ea98ace2108) [FT810\_REG\_TAG\_X](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ab45bcc55b80d016ef2ac8ea98ace2108) = 0x302074,

[ 161](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a22089e51c2e0e4d373589c398a54ca05) [FT810\_REG\_TAG\_Y](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a22089e51c2e0e4d373589c398a54ca05) = 0x302078,

[ 162](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352af8919f80edc86615089d8bafd40f68fd) [FT810\_REG\_TAG](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352af8919f80edc86615089d8bafd40f68fd) = 0x30207C,

[ 163](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aade1a34c921a4d22fe87aa6575bef164) [FT810\_REG\_VOL\_PB](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aade1a34c921a4d22fe87aa6575bef164) = 0x302080,

[ 164](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a98246b3329620a8e252d7ee4a302783e) [FT810\_REG\_VOL\_SOUND](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a98246b3329620a8e252d7ee4a302783e) = 0x302084,

[ 165](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a5d019d200409c2dd4b57f727afedf815) [FT810\_REG\_SOUND](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a5d019d200409c2dd4b57f727afedf815) = 0x302088,

[ 166](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ab83798a30fa11e5e6d7f8e197b0327a4) [FT810\_REG\_PLAY](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ab83798a30fa11e5e6d7f8e197b0327a4) = 0x30208C,

[ 167](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aba2af4d5da3f34693261ef48710d22ee) [FT810\_REG\_GPIO\_DIR](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aba2af4d5da3f34693261ef48710d22ee) = 0x302090,

[ 168](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ab7400ab33f66708dd08fcf8ae543dba5) [FT810\_REG\_GPIO](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ab7400ab33f66708dd08fcf8ae543dba5) = 0x302094,

[ 169](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aec26223f49f0b0b2d418fb0f6a340f8b) [FT810\_REG\_GPIOX\_DIR](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aec26223f49f0b0b2d418fb0f6a340f8b) = 0x302098,

[ 170](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ae45783e98c43d87be2667155efbafbca) [FT810\_REG\_GPIOX](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ae45783e98c43d87be2667155efbafbca) = 0x30209C,

171

[ 172](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352afcc92c93fe9dd983cd13dd5beb91ee9f) [FT810\_REG\_INT\_FLAGS](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352afcc92c93fe9dd983cd13dd5beb91ee9f) = 0x3020A8,

[ 173](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a6ad1c0050228bfdfca87bca6a4a0a571) [FT810\_REG\_INT\_EN](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a6ad1c0050228bfdfca87bca6a4a0a571) = 0x3020AC,

[ 174](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a5a21ce38ac3699f4c9e5f8f0e7bc8555) [FT810\_REG\_INT\_MASK](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a5a21ce38ac3699f4c9e5f8f0e7bc8555) = 0x3020B0,

[ 175](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ab45c8dab2a9d9e7f2c02e40205b957fe) [FT810\_REG\_PLAYBACK\_START](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ab45c8dab2a9d9e7f2c02e40205b957fe) = 0x3020B4,

[ 176](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a206979e1f9edf49aca24f8afb07e7f48) [FT810\_REG\_PLAYBACK\_LENGTH](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a206979e1f9edf49aca24f8afb07e7f48) = 0x3020B8,

[ 177](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a60dd200c41f58057d20169ff833d4f82) [FT810\_REG\_PLAYBACK\_READPTR](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a60dd200c41f58057d20169ff833d4f82) = 0x3020BC,

[ 178](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a8f85d80231d8978144112e41b375ccc7) [FT810\_REG\_PLAYBACK\_FREQ](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a8f85d80231d8978144112e41b375ccc7) = 0x3020C0,

[ 179](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a304779eb0c7eca705a3c9fbf3d23fdb2) [FT810\_REG\_PLAYBACK\_FORMAT](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a304779eb0c7eca705a3c9fbf3d23fdb2) = 0x3020C4,

[ 180](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a0b2882f45164307c678cba35232bcbf9) [FT810\_REG\_PLAYBACK\_LOOP](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a0b2882f45164307c678cba35232bcbf9) = 0x3020C8,

[ 181](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aeba859d489260879a08e922c04e9ca8e) [FT810\_REG\_PLAYBACK\_PLAY](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aeba859d489260879a08e922c04e9ca8e) = 0x3020CC,

[ 182](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a75c68657acd7582c3028f0802d155771) [FT810\_REG\_PWM\_HZ](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a75c68657acd7582c3028f0802d155771) = 0x3020D0,

[ 183](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a0558ac04acd45a6bf1e9100ec3a0a278) [FT810\_REG\_PWM\_DUTY](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a0558ac04acd45a6bf1e9100ec3a0a278) = 0x3020D4,

184

[ 185](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a81b9c8fd550b60b9b4cd1aae7a97efb9) [FT810\_REG\_CMD\_READ](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a81b9c8fd550b60b9b4cd1aae7a97efb9) = 0x3020F8,

[ 186](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ae2b2865e053ed356d915a6f9afd62caf) [FT810\_REG\_CMD\_WRITE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ae2b2865e053ed356d915a6f9afd62caf) = 0x3020FC,

[ 187](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ae393b55425eb2f67bb289e0e2041649c) [FT810\_REG\_CMD\_DL](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ae393b55425eb2f67bb289e0e2041649c) = 0x302100,

[ 188](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a67e068b57d9917ba093bfb8b073cf712) [FT810\_REG\_TOUCH\_MODE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a67e068b57d9917ba093bfb8b073cf712) = 0x302104,

[ 189](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a2bb9ad22a0d93b7facb92f49be1ac63a) [FT810\_REG\_TOUCH\_ADC\_MODE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a2bb9ad22a0d93b7facb92f49be1ac63a) = 0x302108,

[ 190](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ae54293de74687bf2db5fdf9b0682ca44) [FT810\_REG\_TOUCH\_CHARGE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ae54293de74687bf2db5fdf9b0682ca44) = 0x30210C,

[ 191](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a0e712682bd8d083f0ee25b284c242cdf) [FT810\_REG\_TOUCH\_SETTLE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a0e712682bd8d083f0ee25b284c242cdf) = 0x302110,

[ 192](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a779e92fbc0655c0889a3760025f8880a) [FT810\_REG\_TOUCH\_OVERSAMPLE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a779e92fbc0655c0889a3760025f8880a) = 0x302114,

[ 193](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aa102086576124d6931a3a08673e8fc0d) [FT810\_REG\_TOUCH\_RZTHRESH](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aa102086576124d6931a3a08673e8fc0d) = 0x302118,

[ 194](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a359efc1f478e7653bb567fcfa20fb575) [FT810\_REG\_TOUCH\_RAW\_XY](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a359efc1f478e7653bb567fcfa20fb575) = 0x30211C,

[ 195](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a6a0dee898cc286ec6a2f91536fb0c8b4) [FT810\_REG\_TOUCH\_RZ](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a6a0dee898cc286ec6a2f91536fb0c8b4) = 0x302120,

[ 196](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352af62bbcce8fca40ef48253ed77959ff55) [FT810\_REG\_TOUCH\_SCREEN\_XY](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352af62bbcce8fca40ef48253ed77959ff55) = 0x302124,

[ 197](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a4e6013b98cf73db7e09b7952f1f29e5b) [FT810\_REG\_TOUCH\_TAG\_XY](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a4e6013b98cf73db7e09b7952f1f29e5b) = 0x302128,

[ 198](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a97ef048be3e5f39cc5ce6e7f12326a23) [FT810\_REG\_TOUCH\_TAG](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a97ef048be3e5f39cc5ce6e7f12326a23) = 0x30212C,

[ 199](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aa2341295c30b0121eeb8d117764a5baf) [FT810\_REG\_TOUCH\_TRANSFORM\_A](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aa2341295c30b0121eeb8d117764a5baf) = 0x302150,

[ 200](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aa25eab9796730236361b037fc522509d) [FT810\_REG\_TOUCH\_TRANSFORM\_B](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aa25eab9796730236361b037fc522509d) = 0x302154,

[ 201](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aaafde672b6470275a6055520a0534bb2) [FT810\_REG\_TOUCH\_TRANSFORM\_C](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aaafde672b6470275a6055520a0534bb2) = 0x302158,

[ 202](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a71f116560ffc21a45eece099f0155e52) [FT810\_REG\_TOUCH\_TRANSFORM\_D](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a71f116560ffc21a45eece099f0155e52) = 0x30215C,

[ 203](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aa61ca8fc286257f7f70057a5026b0867) [FT810\_REG\_TOUCH\_TRANSFORM\_E](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aa61ca8fc286257f7f70057a5026b0867) = 0x302160,

[ 204](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a03912bde6f4ad32381c50772b89ec2bc) [FT810\_REG\_TOUCH\_TRANSFORM\_F](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a03912bde6f4ad32381c50772b89ec2bc) = 0x302164,

[ 205](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a1190faa2c60e6a2dc8661eb7da7461c6) [FT810\_REG\_TOUCH\_CONFIG](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a1190faa2c60e6a2dc8661eb7da7461c6) = 0x302168,

206

[ 207](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a8366bdc17c88345c80aab6f061090312) [FT810\_REG\_SPI\_WIDTH](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a8366bdc17c88345c80aab6f061090312) = 0x302180,

208

[ 209](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a8807a786fb4c6d42e739a32b3f6078f8) [FT810\_REG\_TOUCH\_DIRECT\_XY](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a8807a786fb4c6d42e739a32b3f6078f8) = 0x30218C,

[ 210](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ad439205ca55294a850c88e9f87fb08b4) [FT810\_REG\_TOUCH\_DIRECT\_Z1Z2](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ad439205ca55294a850c88e9f87fb08b4) = 0x302190,

211

[ 212](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a85c5d599f609c97e80cf87fd0d922784) [FT810\_REG\_CMDB\_SPACE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a85c5d599f609c97e80cf87fd0d922784) = 0x302574,

[ 213](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aea1698cade20d8ab5807d60a7e4dbb3b) [FT810\_REG\_CMDB\_WRITE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aea1698cade20d8ab5807d60a7e4dbb3b) = 0x302578,

214

[ 215](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a43adc41a79ea8af3bbf769b796f7c223) [FT810\_REG\_TRACKER](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a43adc41a79ea8af3bbf769b796f7c223) = 0x309000,

[ 216](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aebe60fc86ac3088108447de01191bc4e) [FT810\_REG\_TRACKER1](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aebe60fc86ac3088108447de01191bc4e) = 0x309004,

[ 217](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352af6d6ece41191d230932dbfaae10c0762) [FT810\_REG\_TRACKER2](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352af6d6ece41191d230932dbfaae10c0762) = 0x309008,

[ 218](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a4449f285050e761b3fd78feebefe4335) [FT810\_REG\_TRACKER3](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a4449f285050e761b3fd78feebefe4335) = 0x30900C,

[ 219](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a9a887d54a3ba0dad157fafddc6573aed) [FT810\_REG\_TRACKER4](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a9a887d54a3ba0dad157fafddc6573aed) = 0x309010,

[ 220](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a8da19290bfcd66b76ff929bb9dd3e568) [FT810\_REG\_MEDIAFIFO\_READ](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a8da19290bfcd66b76ff929bb9dd3e568) = 0x309014,

[ 221](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aa905904989c14075318323a10fac0abe) [FT810\_REG\_MEDIAFIFO\_WRITE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aa905904989c14075318323a10fac0abe) = 0x309018,

222};

223

227

228#ifdef \_\_cplusplus

229}

230#endif

231

232#endif /\* ZEPHYR\_DRIVERS\_MISC\_FT8XX\_FT8XX\_MEMORY\_H\_ \*/

[ft800\_register\_address\_t](group__ft8xx__memory.md#ga3c885b333acd851fed4d74886656d2c6)

ft800\_register\_address\_t

FT800 register addresses.

**Definition** ft8xx\_memory.h:47

[ft810\_register\_address\_t](group__ft8xx__memory.md#ga495a8c0706389e9b3677846d772eb352)

ft810\_register\_address\_t

FT810 register addresses.

**Definition** ft8xx\_memory.h:129

[ft810\_memory\_map\_t](group__ft8xx__memory.md#ga6c8d08697812fb4e6292ff533e753aee)

ft810\_memory\_map\_t

Main parts of FT810 memory map.

**Definition** ft8xx\_memory.h:39

[ft800\_memory\_map\_t](group__ft8xx__memory.md#ga91adc1665d20e88c087ddb10b5e5ef69)

ft800\_memory\_map\_t

Main parts of FT800 memory map.

**Definition** ft8xx\_memory.h:27

[FT800\_REG\_PLAY](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a0187a790b87eca35892431c600248e71)

@ FT800\_REG\_PLAY

**Definition** ft8xx\_memory.h:82

[FT800\_REG\_PLAYBACK\_LENGTH](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a097806c1c7281e5cbaf0e992888c2e97)

@ FT800\_REG\_PLAYBACK\_LENGTH

**Definition** ft8xx\_memory.h:90

[FT800\_REG\_VSYNC0](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a0a6dcbe431ec103262ee805acaee9897)

@ FT800\_REG\_VSYNC0

**Definition** ft8xx\_memory.h:66

[FT800\_REG\_FREQUENCY](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a0a864b5230c4ed04ac4a18f7e9c85af5)

@ FT800\_REG\_FREQUENCY

**Definition** ft8xx\_memory.h:51

[FT800\_REG\_PLAYBACK\_FORMAT](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a13f744aa7a089e177a36623239d12961)

@ FT800\_REG\_PLAYBACK\_FORMAT

**Definition** ft8xx\_memory.h:93

[FT800\_REG\_PLAYBACK\_PLAY](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a15006a5d2ab004ca8b5a9a75be095b5b)

@ FT800\_REG\_PLAYBACK\_PLAY

**Definition** ft8xx\_memory.h:95

[FT800\_REG\_SWIZZLE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a161a252ef247cad31f812c88fbfcdf6f)

@ FT800\_REG\_SWIZZLE

**Definition** ft8xx\_memory.h:72

[FT800\_REG\_TOUCH\_DIRECT\_XY](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a1745bb57bcf9872b308c49a151a43f1f)

@ FT800\_REG\_TOUCH\_DIRECT\_XY

**Definition** ft8xx\_memory.h:122

[FT800\_REG\_TOUCH\_TRANSFORM\_A](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a183fd00d406e113b8b72b8c5b5fc5880)

@ FT800\_REG\_TOUCH\_TRANSFORM\_A

**Definition** ft8xx\_memory.h:115

[FT800\_REG\_RENDERMODE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a1ca1c284f1f3e2ae75c4874f0c569c7c)

@ FT800\_REG\_RENDERMODE

**Definition** ft8xx\_memory.h:52

[FT800\_REG\_TOUCH\_TRANSFORM\_F](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a1d01f5fe890a4d7670cf91a7cd48402f)

@ FT800\_REG\_TOUCH\_TRANSFORM\_F

**Definition** ft8xx\_memory.h:120

[FT800\_REG\_CMD\_DL](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a23f9fdc1d48d6410fc600359842b16ea)

@ FT800\_REG\_CMD\_DL

**Definition** ft8xx\_memory.h:103

[FT800\_REG\_TOUCH\_TAG](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a245e5594218702bc2c30c1b50ec44329)

@ FT800\_REG\_TOUCH\_TAG

**Definition** ft8xx\_memory.h:114

[FT800\_REG\_TAP\_CRC](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a2b36ffdd93c6f41bd08f732099608a99)

@ FT800\_REG\_TAP\_CRC

**Definition** ft8xx\_memory.h:56

[FT800\_REG\_DITHER](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a2ba06eef07c7b881c2b331aa090329ed)

@ FT800\_REG\_DITHER

**Definition** ft8xx\_memory.h:71

[FT800\_REG\_GPIO\_DIR](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a2c4d02cf887f3ec87b99cd32ae8b355b)

@ FT800\_REG\_GPIO\_DIR

**Definition** ft8xx\_memory.h:83

[FT800\_REG\_SOUND](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a2f0f00e3bbd1b9f9fb09c9d2b65382d7)

@ FT800\_REG\_SOUND

**Definition** ft8xx\_memory.h:81

[FT800\_REG\_VSIZE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a2f17cc86a455d13b2f92ada17319a94e)

@ FT800\_REG\_VSIZE

**Definition** ft8xx\_memory.h:65

[FT800\_REG\_HOFFSET](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a3179545d22570761b9bf0598ff24219a)

@ FT800\_REG\_HOFFSET

**Definition** ft8xx\_memory.h:59

[FT800\_REG\_TRACKER](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a3397b2a86a97997d01780d52ec23b84c)

@ FT800\_REG\_TRACKER

**Definition** ft8xx\_memory.h:125

[FT800\_REG\_SNAPSHOT](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a382043bf7f2381a4fad71adeae73db2d)

@ FT800\_REG\_SNAPSHOT

**Definition** ft8xx\_memory.h:54

[FT800\_REG\_TOUCH\_TRANSFORM\_D](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a386a6293cd82485934b3865bd3f1956b)

@ FT800\_REG\_TOUCH\_TRANSFORM\_D

**Definition** ft8xx\_memory.h:118

[FT800\_REG\_TAP\_MASK](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a3c6f1a0898055d4eec3ddfbde56f6a51)

@ FT800\_REG\_TAP\_MASK

**Definition** ft8xx\_memory.h:57

[FT800\_REG\_OUTBITS](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a3d5e1b30a5d1889b14b77f8a4bfecf7b)

@ FT800\_REG\_OUTBITS

**Definition** ft8xx\_memory.h:70

[FT800\_REG\_TAG\_X](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a424e4e6fb301bb6833a46f813fc5895a)

@ FT800\_REG\_TAG\_X

**Definition** ft8xx\_memory.h:76

[FT800\_REG\_TOUCH\_DIRECT\_Z1Z2](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a43bcc194c075b385073ed73a562b8cfa)

@ FT800\_REG\_TOUCH\_DIRECT\_Z1Z2

**Definition** ft8xx\_memory.h:123

[FT800\_REG\_CPURESET](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a4411395eca792d4d23f63242fea6307e)

@ FT800\_REG\_CPURESET

**Definition** ft8xx\_memory.h:55

[FT800\_REG\_CLOCK](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a46376ddea2bccf9e0af33d78a05f635a)

@ FT800\_REG\_CLOCK

**Definition** ft8xx\_memory.h:50

[FT800\_REG\_CMD\_WRITE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a4911a990964958a6e2bf4842e87ab101)

@ FT800\_REG\_CMD\_WRITE

**Definition** ft8xx\_memory.h:102

[FT800\_REG\_TOUCH\_TRANSFORM\_C](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a4b3e903dfed68a7eb7f7734e18aca9e0)

@ FT800\_REG\_TOUCH\_TRANSFORM\_C

**Definition** ft8xx\_memory.h:117

[FT800\_REG\_VOL\_PB](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a4f0e1449b7ab28bf29f52bf3544c442f)

@ FT800\_REG\_VOL\_PB

**Definition** ft8xx\_memory.h:79

[FT800\_REG\_TOUCH\_TRANSFORM\_E](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a4f188f88f9a032fdb6f3c87ed352d4bb)

@ FT800\_REG\_TOUCH\_TRANSFORM\_E

**Definition** ft8xx\_memory.h:119

[FT800\_REG\_INT\_FLAGS](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a4fbbc34adc25d9147f2a8007a537ddbd)

@ FT800\_REG\_INT\_FLAGS

**Definition** ft8xx\_memory.h:86

[FT800\_REG\_VOL\_SOUND](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a5672933c464d2408ad0a6a046fddc1d2)

@ FT800\_REG\_VOL\_SOUND

**Definition** ft8xx\_memory.h:80

[FT800\_REG\_HSYNC0](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a5d365f03f5dcd630191f050963c4fc9c)

@ FT800\_REG\_HSYNC0

**Definition** ft8xx\_memory.h:61

[FT800\_REG\_TOUCH\_ADC\_MODE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a65b43042fe7dbc44bd15fb472bba33a4)

@ FT800\_REG\_TOUCH\_ADC\_MODE

**Definition** ft8xx\_memory.h:105

[FT800\_REG\_TOUCH\_CHARGE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a69b981de24b4da81175c9ac74c8454f5)

@ FT800\_REG\_TOUCH\_CHARGE

**Definition** ft8xx\_memory.h:106

[FT800\_REG\_SNAPY](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a6bcedb4e986dba59c0c689356022d992)

@ FT800\_REG\_SNAPY

**Definition** ft8xx\_memory.h:53

[FT800\_REG\_TOUCH\_RZTHRESH](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a70f721a708b36ef255270d02680e4e7f)

@ FT800\_REG\_TOUCH\_RZTHRESH

**Definition** ft8xx\_memory.h:109

[FT800\_REG\_ID](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a7946c63f4dd93692634c08ec0b4657e4)

@ FT800\_REG\_ID

**Definition** ft8xx\_memory.h:48

[FT800\_REG\_HSIZE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a7b46068735f066e0d2fa6a0ccb073001)

@ FT800\_REG\_HSIZE

**Definition** ft8xx\_memory.h:60

[FT800\_REG\_HSYNC1](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a7c4d1b3a4a5dc128d52fd91352342a70)

@ FT800\_REG\_HSYNC1

**Definition** ft8xx\_memory.h:62

[FT800\_REG\_VOFFSET](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a7d9903cc3452f77287ce411c831e6567)

@ FT800\_REG\_VOFFSET

**Definition** ft8xx\_memory.h:64

[FT800\_REG\_TAG\_Y](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a7f8c3d2a08a68b741ded594eafbfaae4)

@ FT800\_REG\_TAG\_Y

**Definition** ft8xx\_memory.h:77

[FT800\_REG\_TAG](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a83136b05a9a6f64867f39c50fb0079d2)

@ FT800\_REG\_TAG

**Definition** ft8xx\_memory.h:78

[FT800\_REG\_TOUCH\_TAG\_XY](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a86ba740c280900a1dd4273422b9ca8b6)

@ FT800\_REG\_TOUCH\_TAG\_XY

**Definition** ft8xx\_memory.h:113

[FT800\_REG\_TOUCH\_OVERSAMPLE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a87e989861d85d683c95e8de44f74f58b)

@ FT800\_REG\_TOUCH\_OVERSAMPLE

**Definition** ft8xx\_memory.h:108

[FT800\_REG\_PCLK](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a8947fb21fa7a7fa4a26bdaea5dbe79c5)

@ FT800\_REG\_PCLK

**Definition** ft8xx\_memory.h:75

[FT800\_REG\_TOUCH\_RAW\_XY](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a8ef80aeaaffd974b2e246ad15c98f916)

@ FT800\_REG\_TOUCH\_RAW\_XY

**Definition** ft8xx\_memory.h:110

[FT800\_REG\_TOUCH\_SCREEN\_XY](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a99fc0fc08ee942b7783951674837d57d)

@ FT800\_REG\_TOUCH\_SCREEN\_XY

**Definition** ft8xx\_memory.h:112

[FT800\_REG\_MACRO\_1](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a9bce17c193b9c809bef0770bc65b37cf)

@ FT800\_REG\_MACRO\_1

**Definition** ft8xx\_memory.h:99

[FT800\_REG\_PCLK\_POL](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a9ded0eeda09a9cce3bf111c0a49dd391)

@ FT800\_REG\_PCLK\_POL

**Definition** ft8xx\_memory.h:74

[FT800\_REG\_DLSWAP](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a9f726cc401387bbe8aa3366047467688)

@ FT800\_REG\_DLSWAP

**Definition** ft8xx\_memory.h:68

[FT800\_REG\_HCYCLE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aa2b46aa7465a2e38a9947e0b5868f6c7)

@ FT800\_REG\_HCYCLE

**Definition** ft8xx\_memory.h:58

[FT800\_REG\_CMD\_READ](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aa2cb7424ec77d9a35179824cd2fecb47)

@ FT800\_REG\_CMD\_READ

**Definition** ft8xx\_memory.h:101

[FT800\_REG\_INT\_EN](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aa31af794f56d1f4f831ef65c3daf1087)

@ FT800\_REG\_INT\_EN

**Definition** ft8xx\_memory.h:87

[FT800\_REG\_FRAMES](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aa45d948244f4decd8863f5def65a78db)

@ FT800\_REG\_FRAMES

**Definition** ft8xx\_memory.h:49

[FT800\_REG\_INT\_MASK](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aa6461f2c17d723ecd672babedbb1e9fc)

@ FT800\_REG\_INT\_MASK

**Definition** ft8xx\_memory.h:88

[FT800\_REG\_PLAYBACK\_FREQ](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aa8c6fb57011ad08bf0a1d0b48eb5599a)

@ FT800\_REG\_PLAYBACK\_FREQ

**Definition** ft8xx\_memory.h:92

[FT800\_REG\_CSPREAD](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aaf65490a7a4b55309bc8943b065eef17)

@ FT800\_REG\_CSPREAD

**Definition** ft8xx\_memory.h:73

[FT800\_REG\_VCYCLE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aaf8bdfc1924c2269c9db3933499cd23c)

@ FT800\_REG\_VCYCLE

**Definition** ft8xx\_memory.h:63

[FT800\_REG\_PLAYBACK\_LOOP](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ab62b5bbfdf948265ad10129ead4d8a63)

@ FT800\_REG\_PLAYBACK\_LOOP

**Definition** ft8xx\_memory.h:94

[FT800\_REG\_TOUCH\_RZ](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ab66136540b44e2f37a0f920fbd3cbcc4)

@ FT800\_REG\_TOUCH\_RZ

**Definition** ft8xx\_memory.h:111

[FT800\_REG\_ROTATE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ab9bf90e77f7946d4466e3b8d444d64e4)

@ FT800\_REG\_ROTATE

**Definition** ft8xx\_memory.h:69

[FT800\_REG\_VSYNC1](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6abcd84b4d56e71b558a79f10d97b66ea1)

@ FT800\_REG\_VSYNC1

**Definition** ft8xx\_memory.h:67

[FT800\_REG\_PLAYBACK\_START](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ac159bfb8d704e46aa4be4859d1e476af)

@ FT800\_REG\_PLAYBACK\_START

**Definition** ft8xx\_memory.h:89

[FT800\_REG\_PWM\_HZ](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ac321e2d68978123ab259a2d84d186719)

@ FT800\_REG\_PWM\_HZ

**Definition** ft8xx\_memory.h:96

[FT800\_REG\_TOUCH\_TRANSFORM\_B](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6acd3161021e315e1a2f91f21ccdc48d8a)

@ FT800\_REG\_TOUCH\_TRANSFORM\_B

**Definition** ft8xx\_memory.h:116

[FT800\_REG\_TOUCH\_MODE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ada6b5afbed95413c1988131384c02b1b)

@ FT800\_REG\_TOUCH\_MODE

**Definition** ft8xx\_memory.h:104

[FT800\_REG\_TOUCH\_SETTLE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ae02db7afd08bd1c06f6e1f9e06e81d33)

@ FT800\_REG\_TOUCH\_SETTLE

**Definition** ft8xx\_memory.h:107

[FT800\_REG\_PWM\_DUTY](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ae14e09a184dbe44390ce7d5576b30d4c)

@ FT800\_REG\_PWM\_DUTY

**Definition** ft8xx\_memory.h:97

[FT800\_REG\_MACRO\_0](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ae95328740c30d541b4dc79466734306c)

@ FT800\_REG\_MACRO\_0

**Definition** ft8xx\_memory.h:98

[FT800\_REG\_PLAYBACK\_READPTR](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aec4e118a3fe1cf3e1f2b5df6b376a651)

@ FT800\_REG\_PLAYBACK\_READPTR

**Definition** ft8xx\_memory.h:91

[FT800\_REG\_GPIO](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6af7d0154293ba1228a0e04bb923bf9b39)

@ FT800\_REG\_GPIO

**Definition** ft8xx\_memory.h:84

[FT810\_REG\_TOUCH\_TRANSFORM\_F](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a03912bde6f4ad32381c50772b89ec2bc)

@ FT810\_REG\_TOUCH\_TRANSFORM\_F

**Definition** ft8xx\_memory.h:204

[FT810\_REG\_PWM\_DUTY](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a0558ac04acd45a6bf1e9100ec3a0a278)

@ FT810\_REG\_PWM\_DUTY

**Definition** ft8xx\_memory.h:183

[FT810\_REG\_HSYNC0](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a086b28d18b9c49e51ef734c2f6e6ce21)

@ FT810\_REG\_HSYNC0

**Definition** ft8xx\_memory.h:145

[FT810\_REG\_PLAYBACK\_LOOP](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a0b2882f45164307c678cba35232bcbf9)

@ FT810\_REG\_PLAYBACK\_LOOP

**Definition** ft8xx\_memory.h:180

[FT810\_REG\_TOUCH\_SETTLE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a0e712682bd8d083f0ee25b284c242cdf)

@ FT810\_REG\_TOUCH\_SETTLE

**Definition** ft8xx\_memory.h:191

[FT810\_REG\_SNAPSHOT](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a104e72273989d38213fc070b4fd4a676)

@ FT810\_REG\_SNAPSHOT

**Definition** ft8xx\_memory.h:138

[FT810\_REG\_TOUCH\_CONFIG](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a1190faa2c60e6a2dc8661eb7da7461c6)

@ FT810\_REG\_TOUCH\_CONFIG

**Definition** ft8xx\_memory.h:205

[FT810\_REG\_SNAPY](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a1f9721ea190d82af17332d60cb8eb795)

@ FT810\_REG\_SNAPY

**Definition** ft8xx\_memory.h:137

[FT810\_REG\_PLAYBACK\_LENGTH](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a206979e1f9edf49aca24f8afb07e7f48)

@ FT810\_REG\_PLAYBACK\_LENGTH

**Definition** ft8xx\_memory.h:176

[FT810\_REG\_TAG\_Y](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a22089e51c2e0e4d373589c398a54ca05)

@ FT810\_REG\_TAG\_Y

**Definition** ft8xx\_memory.h:161

[FT810\_REG\_CLOCK](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a222e9d43895af76d103f9fbd09c40832)

@ FT810\_REG\_CLOCK

**Definition** ft8xx\_memory.h:134

[FT810\_REG\_VOFFSET](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a2a155f858da556270114a3f9d989ef85)

@ FT810\_REG\_VOFFSET

**Definition** ft8xx\_memory.h:148

[FT810\_REG\_TOUCH\_ADC\_MODE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a2bb9ad22a0d93b7facb92f49be1ac63a)

@ FT810\_REG\_TOUCH\_ADC\_MODE

**Definition** ft8xx\_memory.h:189

[FT810\_REG\_PLAYBACK\_FORMAT](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a304779eb0c7eca705a3c9fbf3d23fdb2)

@ FT810\_REG\_PLAYBACK\_FORMAT

**Definition** ft8xx\_memory.h:179

[FT810\_REG\_RENDERMODE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a32f5dfe4ebc13114ecf9336670f74a31)

@ FT810\_REG\_RENDERMODE

**Definition** ft8xx\_memory.h:136

[FT810\_REG\_TOUCH\_RAW\_XY](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a359efc1f478e7653bb567fcfa20fb575)

@ FT810\_REG\_TOUCH\_RAW\_XY

**Definition** ft8xx\_memory.h:194

[FT810\_REG\_TAP\_MASK](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a369d654c43692ef193493063338888aa)

@ FT810\_REG\_TAP\_MASK

**Definition** ft8xx\_memory.h:141

[FT810\_REG\_VSYNC1](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a3deeabcda1f9453dc2d865e8b19715a8)

@ FT810\_REG\_VSYNC1

**Definition** ft8xx\_memory.h:151

[FT810\_REG\_FREQUENCY](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a3f09f2fd706996b97173f587637aee53)

@ FT810\_REG\_FREQUENCY

**Definition** ft8xx\_memory.h:135

[FT810\_REG\_TRACKER](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a43adc41a79ea8af3bbf769b796f7c223)

@ FT810\_REG\_TRACKER

**Definition** ft8xx\_memory.h:215

[FT810\_REG\_TRACKER3](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a4449f285050e761b3fd78feebefe4335)

@ FT810\_REG\_TRACKER3

**Definition** ft8xx\_memory.h:218

[FT810\_REG\_TOUCH\_TAG\_XY](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a4e6013b98cf73db7e09b7952f1f29e5b)

@ FT810\_REG\_TOUCH\_TAG\_XY

**Definition** ft8xx\_memory.h:197

[FT810\_REG\_HSYNC1](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a533ec4682d3b9649a59e012a53ab55de)

@ FT810\_REG\_HSYNC1

**Definition** ft8xx\_memory.h:146

[FT810\_REG\_ROTATE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a54935aeb6c13623f68c5c74c3db722ff)

@ FT810\_REG\_ROTATE

**Definition** ft8xx\_memory.h:153

[FT810\_REG\_INT\_MASK](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a5a21ce38ac3699f4c9e5f8f0e7bc8555)

@ FT810\_REG\_INT\_MASK

**Definition** ft8xx\_memory.h:174

[FT810\_REG\_SOUND](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a5d019d200409c2dd4b57f727afedf815)

@ FT810\_REG\_SOUND

**Definition** ft8xx\_memory.h:165

[FT810\_REG\_PLAYBACK\_READPTR](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a60dd200c41f58057d20169ff833d4f82)

@ FT810\_REG\_PLAYBACK\_READPTR

**Definition** ft8xx\_memory.h:177

[FT810\_REG\_DITHER](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a61e1d7c2e2ed9a0ee4b372dd9c7df63a)

@ FT810\_REG\_DITHER

**Definition** ft8xx\_memory.h:155

[FT810\_REG\_TOUCH\_MODE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a67e068b57d9917ba093bfb8b073cf712)

@ FT810\_REG\_TOUCH\_MODE

**Definition** ft8xx\_memory.h:188

[FT810\_REG\_HCYCLE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a68ae24f87a50c7790ac987c6e2ccab2b)

@ FT810\_REG\_HCYCLE

**Definition** ft8xx\_memory.h:142

[FT810\_REG\_TOUCH\_RZ](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a6a0dee898cc286ec6a2f91536fb0c8b4)

@ FT810\_REG\_TOUCH\_RZ

**Definition** ft8xx\_memory.h:195

[FT810\_REG\_INT\_EN](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a6ad1c0050228bfdfca87bca6a4a0a571)

@ FT810\_REG\_INT\_EN

**Definition** ft8xx\_memory.h:173

[FT810\_REG\_TAP\_CRC](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a6e302da1712f086b26d08e46f7a9f1d1)

@ FT810\_REG\_TAP\_CRC

**Definition** ft8xx\_memory.h:140

[FT810\_REG\_TOUCH\_TRANSFORM\_D](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a71f116560ffc21a45eece099f0155e52)

@ FT810\_REG\_TOUCH\_TRANSFORM\_D

**Definition** ft8xx\_memory.h:202

[FT810\_REG\_PWM\_HZ](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a75c68657acd7582c3028f0802d155771)

@ FT810\_REG\_PWM\_HZ

**Definition** ft8xx\_memory.h:182

[FT810\_REG\_TOUCH\_OVERSAMPLE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a779e92fbc0655c0889a3760025f8880a)

@ FT810\_REG\_TOUCH\_OVERSAMPLE

**Definition** ft8xx\_memory.h:192

[FT810\_REG\_CMD\_READ](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a81b9c8fd550b60b9b4cd1aae7a97efb9)

@ FT810\_REG\_CMD\_READ

**Definition** ft8xx\_memory.h:185

[FT810\_REG\_SPI\_WIDTH](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a8366bdc17c88345c80aab6f061090312)

@ FT810\_REG\_SPI\_WIDTH

**Definition** ft8xx\_memory.h:207

[FT810\_REG\_PCLK\_POL](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a83d5ff35dc2d6af8e461a45ea2239af6)

@ FT810\_REG\_PCLK\_POL

**Definition** ft8xx\_memory.h:158

[FT810\_REG\_CMDB\_SPACE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a85c5d599f609c97e80cf87fd0d922784)

@ FT810\_REG\_CMDB\_SPACE

**Definition** ft8xx\_memory.h:212

[FT810\_REG\_TOUCH\_DIRECT\_XY](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a8807a786fb4c6d42e739a32b3f6078f8)

@ FT810\_REG\_TOUCH\_DIRECT\_XY

**Definition** ft8xx\_memory.h:209

[FT810\_REG\_MEDIAFIFO\_READ](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a8da19290bfcd66b76ff929bb9dd3e568)

@ FT810\_REG\_MEDIAFIFO\_READ

**Definition** ft8xx\_memory.h:220

[FT810\_REG\_ID](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a8e81832420166c89993a4f0629d5765d)

@ FT810\_REG\_ID

**Definition** ft8xx\_memory.h:132

[FT810\_REG\_PLAYBACK\_FREQ](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a8f85d80231d8978144112e41b375ccc7)

@ FT810\_REG\_PLAYBACK\_FREQ

**Definition** ft8xx\_memory.h:178

[FT810\_REG\_HOFFSET](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a95853b0fc36aca1c168611334a39037f)

@ FT810\_REG\_HOFFSET

**Definition** ft8xx\_memory.h:143

[FT810\_REG\_TOUCH\_TAG](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a97ef048be3e5f39cc5ce6e7f12326a23)

@ FT810\_REG\_TOUCH\_TAG

**Definition** ft8xx\_memory.h:198

[FT810\_REG\_VOL\_SOUND](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a98246b3329620a8e252d7ee4a302783e)

@ FT810\_REG\_VOL\_SOUND

**Definition** ft8xx\_memory.h:164

[FT810\_REG\_TRACKER4](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a9a887d54a3ba0dad157fafddc6573aed)

@ FT810\_REG\_TRACKER4

**Definition** ft8xx\_memory.h:219

[FT810\_REG\_VCYCLE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a9e43b1a3872c21a26981a35c03fea93d)

@ FT810\_REG\_VCYCLE

**Definition** ft8xx\_memory.h:147

[FT810\_REG\_TOUCH\_RZTHRESH](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aa102086576124d6931a3a08673e8fc0d)

@ FT810\_REG\_TOUCH\_RZTHRESH

**Definition** ft8xx\_memory.h:193

[FT810\_REG\_TOUCH\_TRANSFORM\_A](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aa2341295c30b0121eeb8d117764a5baf)

@ FT810\_REG\_TOUCH\_TRANSFORM\_A

**Definition** ft8xx\_memory.h:199

[FT810\_REG\_TOUCH\_TRANSFORM\_B](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aa25eab9796730236361b037fc522509d)

@ FT810\_REG\_TOUCH\_TRANSFORM\_B

**Definition** ft8xx\_memory.h:200

[FT810\_REG\_TOUCH\_TRANSFORM\_E](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aa61ca8fc286257f7f70057a5026b0867)

@ FT810\_REG\_TOUCH\_TRANSFORM\_E

**Definition** ft8xx\_memory.h:203

[FT810\_REG\_MEDIAFIFO\_WRITE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aa905904989c14075318323a10fac0abe)

@ FT810\_REG\_MEDIAFIFO\_WRITE

**Definition** ft8xx\_memory.h:221

[FT810\_REG\_TOUCH\_TRANSFORM\_C](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aaafde672b6470275a6055520a0534bb2)

@ FT810\_REG\_TOUCH\_TRANSFORM\_C

**Definition** ft8xx\_memory.h:201

[FT810\_REG\_VOL\_PB](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aade1a34c921a4d22fe87aa6575bef164)

@ FT810\_REG\_VOL\_PB

**Definition** ft8xx\_memory.h:163

[FT810\_REG\_TAG\_X](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ab45bcc55b80d016ef2ac8ea98ace2108)

@ FT810\_REG\_TAG\_X

**Definition** ft8xx\_memory.h:160

[FT810\_REG\_PLAYBACK\_START](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ab45c8dab2a9d9e7f2c02e40205b957fe)

@ FT810\_REG\_PLAYBACK\_START

**Definition** ft8xx\_memory.h:175

[FT810\_REG\_GPIO](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ab7400ab33f66708dd08fcf8ae543dba5)

@ FT810\_REG\_GPIO

**Definition** ft8xx\_memory.h:168

[FT810\_REG\_FRAMES](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ab75607baa4c4121c34364f4118f990d2)

@ FT810\_REG\_FRAMES

**Definition** ft8xx\_memory.h:133

[FT810\_REG\_PLAY](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ab83798a30fa11e5e6d7f8e197b0327a4)

@ FT810\_REG\_PLAY

**Definition** ft8xx\_memory.h:166

[FT810\_REG\_GPIO\_DIR](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aba2af4d5da3f34693261ef48710d22ee)

@ FT810\_REG\_GPIO\_DIR

**Definition** ft8xx\_memory.h:167

[FT810\_REG\_CSPREAD](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352abfa8c39566c4c41501588b815a5c52ad)

@ FT810\_REG\_CSPREAD

**Definition** ft8xx\_memory.h:157

[FT810\_REG\_VSIZE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352acafecb336293cd24b363e33ca9fdce5a)

@ FT810\_REG\_VSIZE

**Definition** ft8xx\_memory.h:149

[FT810\_REG\_TRIM](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ad35d6fc19bc4fe86802105c48489553e)

@ FT810\_REG\_TRIM

**Definition** ft8xx\_memory.h:130

[FT810\_REG\_TOUCH\_DIRECT\_Z1Z2](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ad439205ca55294a850c88e9f87fb08b4)

@ FT810\_REG\_TOUCH\_DIRECT\_Z1Z2

**Definition** ft8xx\_memory.h:210

[FT810\_REG\_SWIZZLE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ad633919822dadc636420824948e75315)

@ FT810\_REG\_SWIZZLE

**Definition** ft8xx\_memory.h:156

[FT810\_REG\_CMD\_WRITE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ae2b2865e053ed356d915a6f9afd62caf)

@ FT810\_REG\_CMD\_WRITE

**Definition** ft8xx\_memory.h:186

[FT810\_REG\_CPURESET](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ae2bae2d6191190c95a76e4cc1a6bc9d1)

@ FT810\_REG\_CPURESET

**Definition** ft8xx\_memory.h:139

[FT810\_REG\_CMD\_DL](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ae393b55425eb2f67bb289e0e2041649c)

@ FT810\_REG\_CMD\_DL

**Definition** ft8xx\_memory.h:187

[FT810\_REG\_GPIOX](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ae45783e98c43d87be2667155efbafbca)

@ FT810\_REG\_GPIOX

**Definition** ft8xx\_memory.h:170

[FT810\_REG\_TOUCH\_CHARGE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ae54293de74687bf2db5fdf9b0682ca44)

@ FT810\_REG\_TOUCH\_CHARGE

**Definition** ft8xx\_memory.h:190

[FT810\_REG\_CMDB\_WRITE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aea1698cade20d8ab5807d60a7e4dbb3b)

@ FT810\_REG\_CMDB\_WRITE

**Definition** ft8xx\_memory.h:213

[FT810\_REG\_PLAYBACK\_PLAY](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aeba859d489260879a08e922c04e9ca8e)

@ FT810\_REG\_PLAYBACK\_PLAY

**Definition** ft8xx\_memory.h:181

[FT810\_REG\_TRACKER1](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aebe60fc86ac3088108447de01191bc4e)

@ FT810\_REG\_TRACKER1

**Definition** ft8xx\_memory.h:216

[FT810\_REG\_GPIOX\_DIR](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aec26223f49f0b0b2d418fb0f6a340f8b)

@ FT810\_REG\_GPIOX\_DIR

**Definition** ft8xx\_memory.h:169

[FT810\_REG\_TOUCH\_SCREEN\_XY](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352af62bbcce8fca40ef48253ed77959ff55)

@ FT810\_REG\_TOUCH\_SCREEN\_XY

**Definition** ft8xx\_memory.h:196

[FT810\_REG\_TRACKER2](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352af6d6ece41191d230932dbfaae10c0762)

@ FT810\_REG\_TRACKER2

**Definition** ft8xx\_memory.h:217

[FT810\_REG\_TAG](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352af8919f80edc86615089d8bafd40f68fd)

@ FT810\_REG\_TAG

**Definition** ft8xx\_memory.h:162

[FT810\_REG\_HSIZE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352af89832af70c53e320337f633985ce295)

@ FT810\_REG\_HSIZE

**Definition** ft8xx\_memory.h:144

[FT810\_REG\_DLSWAP](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352afb81eec26bd13732949ae8f8186fdd26)

@ FT810\_REG\_DLSWAP

**Definition** ft8xx\_memory.h:152

[FT810\_REG\_INT\_FLAGS](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352afcc92c93fe9dd983cd13dd5beb91ee9f)

@ FT810\_REG\_INT\_FLAGS

**Definition** ft8xx\_memory.h:172

[FT810\_REG\_VSYNC0](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352afd3caed713df1d318d62cbd73fdfe3c6)

@ FT810\_REG\_VSYNC0

**Definition** ft8xx\_memory.h:150

[FT810\_REG\_PCLK](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aff03cfb6400f883999cc01c0cf832812)

@ FT810\_REG\_PCLK

**Definition** ft8xx\_memory.h:159

[FT810\_REG\_OUTBITS](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aff30b9219c582c8ceac17f115a18375d)

@ FT810\_REG\_OUTBITS

**Definition** ft8xx\_memory.h:154

[FT810\_RAM\_CMD](group__ft8xx__memory.md#gga6c8d08697812fb4e6292ff533e753aeea06a9355b36b87b1b0fa79a6f468e46bb)

@ FT810\_RAM\_CMD

**Definition** ft8xx\_memory.h:43

[FT810\_REG\_](group__ft8xx__memory.md#gga6c8d08697812fb4e6292ff533e753aeea0f483ff9a2c538fccc2326f431201a57)

@ FT810\_REG\_

**Definition** ft8xx\_memory.h:42

[FT810\_RAM\_DL](group__ft8xx__memory.md#gga6c8d08697812fb4e6292ff533e753aeea408b88147f94626dabe1e8b81f72b9ea)

@ FT810\_RAM\_DL

**Definition** ft8xx\_memory.h:41

[FT810\_RAM\_G](group__ft8xx__memory.md#gga6c8d08697812fb4e6292ff533e753aeeaa5619b0f2ba721cfc070ee09886af264)

@ FT810\_RAM\_G

**Definition** ft8xx\_memory.h:40

[FT800\_ROM\_FONT\_ADDR](group__ft8xx__memory.md#gga91adc1665d20e88c087ddb10b5e5ef69a0b846c1c3f54c88a66fee75ae1310893)

@ FT800\_ROM\_FONT\_ADDR

**Definition** ft8xx\_memory.h:31

[FT800\_RAM\_G](group__ft8xx__memory.md#gga91adc1665d20e88c087ddb10b5e5ef69a0f292b470f74c0c625292850d1f6d91c)

@ FT800\_RAM\_G

**Definition** ft8xx\_memory.h:28

[FT800\_RAM\_CMD](group__ft8xx__memory.md#gga91adc1665d20e88c087ddb10b5e5ef69a2c37aff19d6aa8801f257bc689428373)

@ FT800\_RAM\_CMD

**Definition** ft8xx\_memory.h:35

[FT800\_REG\_](group__ft8xx__memory.md#gga91adc1665d20e88c087ddb10b5e5ef69a4a88dd5f6ec5d1adf451467db195604c)

@ FT800\_REG\_

**Definition** ft8xx\_memory.h:34

[FT800\_ROM\_FONT](group__ft8xx__memory.md#gga91adc1665d20e88c087ddb10b5e5ef69a4f2b840d1343d34a13f5859f35241714)

@ FT800\_ROM\_FONT

**Definition** ft8xx\_memory.h:30

[FT800\_RAM\_PAL](group__ft8xx__memory.md#gga91adc1665d20e88c087ddb10b5e5ef69a5a01dedda4d91a94bb7dd42eeef5f357)

@ FT800\_RAM\_PAL

**Definition** ft8xx\_memory.h:33

[FT800\_RAM\_DL](group__ft8xx__memory.md#gga91adc1665d20e88c087ddb10b5e5ef69ad7f0dc26c1313aa315bbeba0b648a013)

@ FT800\_RAM\_DL

**Definition** ft8xx\_memory.h:32

[FT800\_ROM\_CHIPID](group__ft8xx__memory.md#gga91adc1665d20e88c087ddb10b5e5ef69ae186b0781a832f3adedb21e9d2e05300)

@ FT800\_ROM\_CHIPID

**Definition** ft8xx\_memory.h:29

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [misc](dir_3d7f76f006150d60bf1fdbf1492e8004.md)
- [ft8xx](dir_2b36ac0e023aa45869ab11e4334d802b.md)
- [ft8xx\_memory.h](ft8xx__memory_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
