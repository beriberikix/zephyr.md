---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/icm45686_8h_source.html
original_path: doxygen/html/icm45686_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

icm45686.h

[Go to the documentation of this file.](icm45686_8h.md)

1/\*

2 \* Copyright (c) 2024 Intel Corporation

3 \* Copyright (c) 2025 Croxel Inc.

4 \* Copyright (c) 2025 CogniPilot Foundation

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_TDK\_ICM45686\_H\_

9#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_TDK\_ICM45686\_H\_

10

16

[ 21](group__ICM45686__ACCEL__POWER__MODES.md#ga8b33a42ca2ee186c644481a20681599d)#define ICM45686\_DT\_ACCEL\_OFF 0

[ 22](group__ICM45686__ACCEL__POWER__MODES.md#gab87a06cbd382b4d3b781cb3d00907fa9)#define ICM45686\_DT\_ACCEL\_LP 2

[ 23](group__ICM45686__ACCEL__POWER__MODES.md#gaaef05bb2b940ce73d5afaf28ce14d9ce)#define ICM45686\_DT\_ACCEL\_LN 3

25

[ 30](group__ICM45686__GYRO__POWER__MODES.md#gade7adbaae8ac2eba67a8fa3f97ef0415)#define ICM45686\_DT\_GYRO\_OFF 0

[ 31](group__ICM45686__GYRO__POWER__MODES.md#gadae95f6a41154f1984da037fb83258d5)#define ICM45686\_DT\_GYRO\_STANDBY 1

[ 32](group__ICM45686__GYRO__POWER__MODES.md#gaee3b6201bb6d391c52f62d7b81e12fbc)#define ICM45686\_DT\_GYRO\_LP 2

[ 33](group__ICM45686__GYRO__POWER__MODES.md#gaa3cce06238e725b6aabe749cb9a9b0d4)#define ICM45686\_DT\_GYRO\_LN 3

35

[ 40](group__ICM45686__ACCEL__SCALE.md#gaf790544808b65f948d0b53cb0de7cb54)#define ICM45686\_DT\_ACCEL\_FS\_32 0

[ 41](group__ICM45686__ACCEL__SCALE.md#ga7690e5863f8437e6e30e8dd26f5d3dc1)#define ICM45686\_DT\_ACCEL\_FS\_16 1

[ 42](group__ICM45686__ACCEL__SCALE.md#ga1f2974e42fb6af6e2f94eeefaad8fdc2)#define ICM45686\_DT\_ACCEL\_FS\_8 2

[ 43](group__ICM45686__ACCEL__SCALE.md#ga5349fe55ec137b9eddb2e37454321486)#define ICM45686\_DT\_ACCEL\_FS\_4 3

[ 44](group__ICM45686__ACCEL__SCALE.md#gad37d83f116fde8bb5ba419e8db209ad1)#define ICM45686\_DT\_ACCEL\_FS\_2 4

46

[ 51](group__ICM45686__GYRO__SCALE.md#ga02e33c717d16c4f6e8ad39f41098a368)#define ICM45686\_DT\_GYRO\_FS\_4000 0

[ 52](group__ICM45686__GYRO__SCALE.md#ga7eada42888012443169b722b68590e30)#define ICM45686\_DT\_GYRO\_FS\_2000 1

[ 53](group__ICM45686__GYRO__SCALE.md#ga573e9a7c2517f47690a2bb57fa02e9e4)#define ICM45686\_DT\_GYRO\_FS\_1000 2

[ 54](group__ICM45686__GYRO__SCALE.md#gacd9c8c364e136f66e0dac901f5a8d470)#define ICM45686\_DT\_GYRO\_FS\_500 3

[ 55](group__ICM45686__GYRO__SCALE.md#gadc7a6ca2050179c0049f03797988d3e3)#define ICM45686\_DT\_GYRO\_FS\_250 4

[ 56](group__ICM45686__GYRO__SCALE.md#ga9cc1fe4f1738e8695c7e7e6fa7df44e9)#define ICM45686\_DT\_GYRO\_FS\_125 5

[ 57](group__ICM45686__GYRO__SCALE.md#ga27956d51388dea37fd9f1d8e4ca286b6)#define ICM45686\_DT\_GYRO\_FS\_62\_5 6

[ 58](group__ICM45686__GYRO__SCALE.md#ga2dfe38c6ebef4b45f95b9383450b6799)#define ICM45686\_DT\_GYRO\_FS\_31\_25 7

[ 59](group__ICM45686__GYRO__SCALE.md#gaef81e5104573864864de5781692df31d)#define ICM45686\_DT\_GYRO\_FS\_15\_625 8

61

[ 66](group__ICM45686__ACCEL__DATA__RATE.md#ga60693a4e030bca38e742735cd082a46e)#define ICM45686\_DT\_ACCEL\_ODR\_6400 3 /\* LN-mode only \*/

[ 67](group__ICM45686__ACCEL__DATA__RATE.md#gaf91570280567f8b094c10d665b32cdf8)#define ICM45686\_DT\_ACCEL\_ODR\_3200 4 /\* LN-mode only \*/

[ 68](group__ICM45686__ACCEL__DATA__RATE.md#gab22b9e6b25a80b5629536cb3014e1582)#define ICM45686\_DT\_ACCEL\_ODR\_1600 5 /\* LN-mode only \*/

[ 69](group__ICM45686__ACCEL__DATA__RATE.md#ga3ff3f2111a8ab2f4420aa31db8813da4)#define ICM45686\_DT\_ACCEL\_ODR\_800 6 /\* LN-mode only \*/

[ 70](group__ICM45686__ACCEL__DATA__RATE.md#ga7cb0cad42bb0eda5a694b195f49868b5)#define ICM45686\_DT\_ACCEL\_ODR\_400 7 /\* Both LN-mode and LP-mode \*/

[ 71](group__ICM45686__ACCEL__DATA__RATE.md#ga856edda34709d32f3c4e2738005cb263)#define ICM45686\_DT\_ACCEL\_ODR\_200 8 /\* Both LN-mode and LP-mode \*/

[ 72](group__ICM45686__ACCEL__DATA__RATE.md#ga54053977b70e2d369661f4de0614a512)#define ICM45686\_DT\_ACCEL\_ODR\_100 9 /\* Both LN-mode and LP-mode \*/

[ 73](group__ICM45686__ACCEL__DATA__RATE.md#ga5d5dc91e2993a0ec533e4e332740ada2)#define ICM45686\_DT\_ACCEL\_ODR\_50 10 /\* Both LN-mode and LP-mode \*/

[ 74](group__ICM45686__ACCEL__DATA__RATE.md#gab319d91b31ac5b09248d30042391c3ff)#define ICM45686\_DT\_ACCEL\_ODR\_25 11 /\* Both LN-mode and LP-mode \*/

[ 75](group__ICM45686__ACCEL__DATA__RATE.md#ga6c83ccbef5b5cb0dd6bf10eaa6ab5dc4)#define ICM45686\_DT\_ACCEL\_ODR\_12\_5 12 /\* Both LN-mode and LP-mode \*/

[ 76](group__ICM45686__ACCEL__DATA__RATE.md#gafd818ea53188619aab8e8b53c82bed75)#define ICM45686\_DT\_ACCEL\_ODR\_6\_25 13 /\* LP-mode only \*/

[ 77](group__ICM45686__ACCEL__DATA__RATE.md#gaeded0acef70490aaa122a54456c39c80)#define ICM45686\_DT\_ACCEL\_ODR\_3\_125 14 /\* LP-mode only \*/

[ 78](group__ICM45686__ACCEL__DATA__RATE.md#ga7fc1f9759a6b6ab9c287491f33673f5a)#define ICM45686\_DT\_ACCEL\_ODR\_1\_5625 15 /\* LP-mode only \*/

80

[ 85](group__ICM45686__GYRO__DATA__RATE.md#gab5eb26c981fbb104d368ef57371d8a7c)#define ICM45686\_DT\_GYRO\_ODR\_6400 3 /\* LN-mode only \*/

[ 86](group__ICM45686__GYRO__DATA__RATE.md#gab53b400f63aa733b790340a96b322885)#define ICM45686\_DT\_GYRO\_ODR\_3200 4 /\* LN-mode only \*/

[ 87](group__ICM45686__GYRO__DATA__RATE.md#gaa85269312c7a548aabe9f0da4ff2acac)#define ICM45686\_DT\_GYRO\_ODR\_1600 5 /\* LN-mode only \*/

[ 88](group__ICM45686__GYRO__DATA__RATE.md#ga1ac6b40e0b5416a31d08e7433c9228bd)#define ICM45686\_DT\_GYRO\_ODR\_800 6 /\* LN-mode only \*/

[ 89](group__ICM45686__GYRO__DATA__RATE.md#ga4364e0123afc4afde78a4a04b690ab16)#define ICM45686\_DT\_GYRO\_ODR\_400 7 /\* Both LN-mode and LP-mode \*/

[ 90](group__ICM45686__GYRO__DATA__RATE.md#ga79941259cc7ba89409b57a9d0f955881)#define ICM45686\_DT\_GYRO\_ODR\_200 8 /\* Both LN-mode and LP-mode \*/

[ 91](group__ICM45686__GYRO__DATA__RATE.md#gac0ed04fd24cccd6145629d9f967c7e1c)#define ICM45686\_DT\_GYRO\_ODR\_100 9 /\* Both LN-mode and LP-mode \*/

[ 92](group__ICM45686__GYRO__DATA__RATE.md#gafd69abea1b6667ce91ad0aa0cfd35ea7)#define ICM45686\_DT\_GYRO\_ODR\_50 10 /\* Both LN-mode and LP-mode \*/

[ 93](group__ICM45686__GYRO__DATA__RATE.md#gada0b64962561d0978a4d7eca1c953cf9)#define ICM45686\_DT\_GYRO\_ODR\_25 11 /\* Both LN-mode and LP-mode \*/

[ 94](group__ICM45686__GYRO__DATA__RATE.md#ga73f72b58714ea8ee5f16da67c19acebe)#define ICM45686\_DT\_GYRO\_ODR\_12\_5 12 /\* Both LN-mode and LP-mode \*/

[ 95](group__ICM45686__GYRO__DATA__RATE.md#ga80f01d68efff04a831d99f34cc7c4095)#define ICM45686\_DT\_GYRO\_ODR\_6\_25 13 /\* LP-mode only \*/

[ 96](group__ICM45686__GYRO__DATA__RATE.md#ga2e10d8ad52d7635f550d2ae99f522d58)#define ICM45686\_DT\_GYRO\_ODR\_3\_125 14 /\* LP-mode only \*/

[ 97](group__ICM45686__GYRO__DATA__RATE.md#ga416e6c246e18be3321d4070b10d704ff)#define ICM45686\_DT\_GYRO\_ODR\_1\_5625 15 /\* LP-mode only \*/

99

[ 104](group__ICM45686__GYRO__LPF.md#ga3e7966cdb32e1bf4b45284bdaa019aff)#define ICM45686\_DT\_GYRO\_LPF\_BW\_OFF 0

[ 105](group__ICM45686__GYRO__LPF.md#ga824b5b245825766b8e3e55337b563e00)#define ICM45686\_DT\_GYRO\_LPF\_BW\_1\_4 1

[ 106](group__ICM45686__GYRO__LPF.md#gaa6ab971581b350d6e39aafaeb2eb9224)#define ICM45686\_DT\_GYRO\_LPF\_BW\_1\_8 2

[ 107](group__ICM45686__GYRO__LPF.md#ga768aee240c0e30484ee2c51cd906bb32)#define ICM45686\_DT\_GYRO\_LPF\_BW\_1\_16 3

[ 108](group__ICM45686__GYRO__LPF.md#ga214dbae4eba8b982d3a64cffeaab5e74)#define ICM45686\_DT\_GYRO\_LPF\_BW\_1\_32 4

[ 109](group__ICM45686__GYRO__LPF.md#gaea4539a5b53911d62defcfda36321802)#define ICM45686\_DT\_GYRO\_LPF\_BW\_1\_64 5

[ 110](group__ICM45686__GYRO__LPF.md#gabb75aef9c5b0f814b6437c245837958a)#define ICM45686\_DT\_GYRO\_LPF\_BW\_1\_128 6

112

[ 117](group__ICM45686__ACCEL__LPF.md#ga5cd6f0bdb7bbe7c1bb2f9e894b503d32)#define ICM45686\_DT\_ACCEL\_LPF\_BW\_OFF 0

[ 118](group__ICM45686__ACCEL__LPF.md#gae1b58c4126f0270b4a29d3411bca8933)#define ICM45686\_DT\_ACCEL\_LPF\_BW\_1\_4 1

[ 119](group__ICM45686__ACCEL__LPF.md#ga9fb18995a51d3d3367d4daf289e63c85)#define ICM45686\_DT\_ACCEL\_LPF\_BW\_1\_8 2

[ 120](group__ICM45686__ACCEL__LPF.md#gae9411f41d66488dca5b7309c33b1413c)#define ICM45686\_DT\_ACCEL\_LPF\_BW\_1\_16 3

[ 121](group__ICM45686__ACCEL__LPF.md#ga48b322615cc68ce56944aaac54def755)#define ICM45686\_DT\_ACCEL\_LPF\_BW\_1\_32 4

[ 122](group__ICM45686__ACCEL__LPF.md#ga5e82ec391e86aeb1296b4ffae9401fac)#define ICM45686\_DT\_ACCEL\_LPF\_BW\_1\_64 5

[ 123](group__ICM45686__ACCEL__LPF.md#ga9473e299e65b1fe23e4dd987aae3554e)#define ICM45686\_DT\_ACCEL\_LPF\_BW\_1\_128 6

125

126

128

129#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_TDK\_ICM45686\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [sensor](dir_c9b2d7ff2bbb57ff9b1854f820609711.md)
- [icm45686.h](icm45686_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
