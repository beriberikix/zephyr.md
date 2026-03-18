---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/health__faults_8h_source.html
original_path: doxygen/html/health__faults_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

health\_faults.h

[Go to the documentation of this file.](health__faults_8h.md)

1

4

5/\*

6 \* Copyright (c) 2019 Nordic Semiconductor ASA

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_HEALTH\_FAULTS\_H\_\_

11#define ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_HEALTH\_FAULTS\_H\_\_

12

19

[ 21](group__bt__mesh__health__faults.md#ga5fe6993bb219f6547b67e6720f7bf526)#define BT\_MESH\_HEALTH\_FAULT\_NO\_FAULT 0x00

22

[ 23](group__bt__mesh__health__faults.md#gaa75f0a4d758476e2fdeaa94b1ad98b55)#define BT\_MESH\_HEALTH\_FAULT\_BATTERY\_LOW\_WARNING 0x01

[ 24](group__bt__mesh__health__faults.md#gaaa682f49f35e6764af0429690aebf20e)#define BT\_MESH\_HEALTH\_FAULT\_BATTERY\_LOW\_ERROR 0x02

[ 25](group__bt__mesh__health__faults.md#ga0a77dbd3aa3bddeab0cbcf434d36f791)#define BT\_MESH\_HEALTH\_FAULT\_SUPPLY\_VOLTAGE\_TOO\_LOW\_WARNING 0x03

[ 26](group__bt__mesh__health__faults.md#gab64bbf32cda9d9cd8e82a05f7c9924a1)#define BT\_MESH\_HEALTH\_FAULT\_SUPPLY\_VOLTAGE\_TOO\_LOW\_ERROR 0x04

[ 27](group__bt__mesh__health__faults.md#ga7838991d14a19ef401a41d96bec76287)#define BT\_MESH\_HEALTH\_FAULT\_SUPPLY\_VOLTAGE\_TOO\_HIGH\_WARNING 0x05

[ 28](group__bt__mesh__health__faults.md#ga86d34960a167c0c3f8a1f320d1843702)#define BT\_MESH\_HEALTH\_FAULT\_SUPPLY\_VOLTAGE\_TOO\_HIGH\_ERROR 0x06

[ 29](group__bt__mesh__health__faults.md#ga326ce2242e409c9577d324388509b7b7)#define BT\_MESH\_HEALTH\_FAULT\_POWER\_SUPPLY\_INTERRUPTED\_WARNING 0x07

[ 30](group__bt__mesh__health__faults.md#gaf1fff982760290c80424b87a60bff822)#define BT\_MESH\_HEALTH\_FAULT\_POWER\_SUPPLY\_INTERRUPTED\_ERROR 0x08

[ 31](group__bt__mesh__health__faults.md#gab92ab13dbc9799476e6e627a81080e14)#define BT\_MESH\_HEALTH\_FAULT\_NO\_LOAD\_WARNING 0x09

[ 32](group__bt__mesh__health__faults.md#ga29b5e94269715a8301bc363cb66db370)#define BT\_MESH\_HEALTH\_FAULT\_NO\_LOAD\_ERROR 0x0A

[ 33](group__bt__mesh__health__faults.md#gacd14cc12794077cc517d5fefa748c9c6)#define BT\_MESH\_HEALTH\_FAULT\_OVERLOAD\_WARNING 0x0B

[ 34](group__bt__mesh__health__faults.md#gafafa715a04011e80944199d93ee6c51b)#define BT\_MESH\_HEALTH\_FAULT\_OVERLOAD\_ERROR 0x0C

[ 35](group__bt__mesh__health__faults.md#gac737fc53f2184bd1664f0da5388148ac)#define BT\_MESH\_HEALTH\_FAULT\_OVERHEAT\_WARNING 0x0D

[ 36](group__bt__mesh__health__faults.md#ga1c47ccb73f94cee4db7d300679972300)#define BT\_MESH\_HEALTH\_FAULT\_OVERHEAT\_ERROR 0x0E

[ 37](group__bt__mesh__health__faults.md#ga95fd40c6066a37417ebfc9916b06db7c)#define BT\_MESH\_HEALTH\_FAULT\_CONDENSATION\_WARNING 0x0F

[ 38](group__bt__mesh__health__faults.md#ga3da2c495908e3b4aac524e5d91c58189)#define BT\_MESH\_HEALTH\_FAULT\_CONDENSATION\_ERROR 0x10

[ 39](group__bt__mesh__health__faults.md#ga7fb07118fea783803bfa8f419441740f)#define BT\_MESH\_HEALTH\_FAULT\_VIBRATION\_WARNING 0x11

[ 40](group__bt__mesh__health__faults.md#ga1b9f51d2760530bc170a81ff29435cf3)#define BT\_MESH\_HEALTH\_FAULT\_VIBRATION\_ERROR 0x12

[ 41](group__bt__mesh__health__faults.md#ga4e46ae0ebd52722c1600f2025a2fb190)#define BT\_MESH\_HEALTH\_FAULT\_CONFIGURATION\_WARNING 0x13

[ 42](group__bt__mesh__health__faults.md#ga03ee761cb0a2d5cbf3509a719e658621)#define BT\_MESH\_HEALTH\_FAULT\_CONFIGURATION\_ERROR 0x14

[ 43](group__bt__mesh__health__faults.md#ga0e50ab22bffb357f02acf4860664d535)#define BT\_MESH\_HEALTH\_FAULT\_ELEMENT\_NOT\_CALIBRATED\_WARNING 0x15

[ 44](group__bt__mesh__health__faults.md#gaa612dbc60cc9ab0fe4978a0992499009)#define BT\_MESH\_HEALTH\_FAULT\_ELEMENT\_NOT\_CALIBRATED\_ERROR 0x16

[ 45](group__bt__mesh__health__faults.md#gabf766439091f937438a0e736ddc892b4)#define BT\_MESH\_HEALTH\_FAULT\_MEMORY\_WARNING 0x17

[ 46](group__bt__mesh__health__faults.md#ga358d3351b1935b3a4c259060902033db)#define BT\_MESH\_HEALTH\_FAULT\_MEMORY\_ERROR 0x18

[ 47](group__bt__mesh__health__faults.md#ga8d60f38c1560c269fdfd18de35daf5d6)#define BT\_MESH\_HEALTH\_FAULT\_SELF\_TEST\_WARNING 0x19

[ 48](group__bt__mesh__health__faults.md#ga75214891137e1045bcc83c4c54458e77)#define BT\_MESH\_HEALTH\_FAULT\_SELF\_TEST\_ERROR 0x1A

[ 49](group__bt__mesh__health__faults.md#ga124bb981c3ab2c41eda2ddf3bc85b5f2)#define BT\_MESH\_HEALTH\_FAULT\_INPUT\_TOO\_LOW\_WARNING 0x1B

[ 50](group__bt__mesh__health__faults.md#ga33c5b4f773c6afe73f64a14411033b3f)#define BT\_MESH\_HEALTH\_FAULT\_INPUT\_TOO\_LOW\_ERROR 0x1C

[ 51](group__bt__mesh__health__faults.md#gae3c188075202eeff7292ab56e03e31a9)#define BT\_MESH\_HEALTH\_FAULT\_INPUT\_TOO\_HIGH\_WARNING 0x1D

[ 52](group__bt__mesh__health__faults.md#gad42b0f690836deae1dcbb4757e885c02)#define BT\_MESH\_HEALTH\_FAULT\_INPUT\_TOO\_HIGH\_ERROR 0x1E

[ 53](group__bt__mesh__health__faults.md#ga5a1ba1561e93574e0d4598bd90c386b8)#define BT\_MESH\_HEALTH\_FAULT\_INPUT\_NO\_CHANGE\_WARNING 0x1F

[ 54](group__bt__mesh__health__faults.md#ga3789605186fe9c172d3320a22a21ead6)#define BT\_MESH\_HEALTH\_FAULT\_INPUT\_NO\_CHANGE\_ERROR 0x20

[ 55](group__bt__mesh__health__faults.md#gaf51ad764a78b425cda29720c4e063221)#define BT\_MESH\_HEALTH\_FAULT\_ACTUATOR\_BLOCKED\_WARNING 0x21

[ 56](group__bt__mesh__health__faults.md#ga0493f52939a375fcebe33d45451b618c)#define BT\_MESH\_HEALTH\_FAULT\_ACTUATOR\_BLOCKED\_ERROR 0x22

[ 57](group__bt__mesh__health__faults.md#ga03cfae918863f10dd5aaab6fd3a82b07)#define BT\_MESH\_HEALTH\_FAULT\_HOUSING\_OPENED\_WARNING 0x23

[ 58](group__bt__mesh__health__faults.md#ga7308395342cc226ef17584aebfa78d2c)#define BT\_MESH\_HEALTH\_FAULT\_HOUSING\_OPENED\_ERROR 0x24

[ 59](group__bt__mesh__health__faults.md#ga66d4e92380a42b0491848a261a36246b)#define BT\_MESH\_HEALTH\_FAULT\_TAMPER\_WARNING 0x25

[ 60](group__bt__mesh__health__faults.md#ga69b7755dd511f30864272ad1465f2965)#define BT\_MESH\_HEALTH\_FAULT\_TAMPER\_ERROR 0x26

[ 61](group__bt__mesh__health__faults.md#ga1494db7b9a0fbab15119a65da0b6b0d0)#define BT\_MESH\_HEALTH\_FAULT\_DEVICE\_MOVED\_WARNING 0x27

[ 62](group__bt__mesh__health__faults.md#ga482eb25cfcfd943342f8d30ed976bc24)#define BT\_MESH\_HEALTH\_FAULT\_DEVICE\_MOVED\_ERROR 0x28

[ 63](group__bt__mesh__health__faults.md#ga7f158981cf1282acaca0839244e3c6cb)#define BT\_MESH\_HEALTH\_FAULT\_DEVICE\_DROPPED\_WARNING 0x29

[ 64](group__bt__mesh__health__faults.md#ga2d0909640905067168ba45bea0523618)#define BT\_MESH\_HEALTH\_FAULT\_DEVICE\_DROPPED\_ERROR 0x2A

[ 65](group__bt__mesh__health__faults.md#ga95d30649750b543650c3a21cc8719c3e)#define BT\_MESH\_HEALTH\_FAULT\_OVERFLOW\_WARNING 0x2B

[ 66](group__bt__mesh__health__faults.md#ga63b9b85427e0efa31e8a1496065b3dc9)#define BT\_MESH\_HEALTH\_FAULT\_OVERFLOW\_ERROR 0x2C

[ 67](group__bt__mesh__health__faults.md#gada2400efbf70229ce8328a9ace7fcccf)#define BT\_MESH\_HEALTH\_FAULT\_EMPTY\_WARNING 0x2D

[ 68](group__bt__mesh__health__faults.md#ga0b0414621784d1a3c872077e0b578d0d)#define BT\_MESH\_HEALTH\_FAULT\_EMPTY\_ERROR 0x2E

[ 69](group__bt__mesh__health__faults.md#ga534b85b4f805b585c4c4d29e6abe782a)#define BT\_MESH\_HEALTH\_FAULT\_INTERNAL\_BUS\_WARNING 0x2F

[ 70](group__bt__mesh__health__faults.md#ga54b4657666c01dca9417d58e302ff738)#define BT\_MESH\_HEALTH\_FAULT\_INTERNAL\_BUS\_ERROR 0x30

[ 71](group__bt__mesh__health__faults.md#gae1113f6fcaae95b1a7cfe2dd95c287ab)#define BT\_MESH\_HEALTH\_FAULT\_MECHANISM\_JAMMED\_WARNING 0x31

[ 72](group__bt__mesh__health__faults.md#gaa6ccb4569d63b6eb0dc53ec7211f2f98)#define BT\_MESH\_HEALTH\_FAULT\_MECHANISM\_JAMMED\_ERROR 0x32

73

[ 79](group__bt__mesh__health__faults.md#gae0b8ecef9c11e17a02ede6a4b416c3b8)#define BT\_MESH\_HEALTH\_FAULT\_VENDOR\_SPECIFIC\_START 0x80

80

84

85#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_HEALTH\_FAULTS\_H\_\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [health\_faults.h](health__faults_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
