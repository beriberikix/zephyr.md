---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/dt-bindings_2regulator_2npm1300_8h_source.html
original_path: doxygen/html/dt-bindings_2regulator_2npm1300_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

npm1300.h

[Go to the documentation of this file.](dt-bindings_2regulator_2npm1300_8h.md)

1/\*

2 \* Copyright (c) 2023 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_REGULATOR\_NPM1300\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_REGULATOR\_NPM1300\_H\_

9

15

20/\* Buck modes \*/

[ 21](group__regulator__npm1300.md#ga97496249f39cd06b128667806e4cc6d8)#define NPM1300\_BUCK\_MODE\_AUTO 0x00U

[ 22](group__regulator__npm1300.md#ga1b594bbfeeb7468283fd9195398cb63e)#define NPM1300\_BUCK\_MODE\_PWM 0x01U

[ 23](group__regulator__npm1300.md#gab6373bb0163cbc349c0c325de3cd91da)#define NPM1300\_BUCK\_MODE\_PFM 0x04U

24

25/\* LDSW / LDO modes \*/

[ 26](group__regulator__npm1300.md#gaa822bb8308819d27c6fcb50c77c02863)#define NPM1300\_LDSW\_MODE\_LDO 0x02U

[ 27](group__regulator__npm1300.md#ga32d21a1ebeda52b59eab5d410149536f)#define NPM1300\_LDSW\_MODE\_LDSW 0x03U

28

29/\* GPIO control configuration \*/

[ 30](group__regulator__npm1300.md#ga911e084475547f65f6a6b74edd030f23)#define NPM1300\_GPIO\_CHAN\_NONE 0x00U

[ 31](group__regulator__npm1300.md#ga7c59c9d2c404772621652d6b5a95d7f3)#define NPM1300\_GPIO\_CHAN\_0 0x01U

[ 32](group__regulator__npm1300.md#ga304b75dbfa7a3c3a2f1848aac765ec17)#define NPM1300\_GPIO\_CHAN\_1 0x02U

[ 33](group__regulator__npm1300.md#gac92e640bb3d7a751ec8276624260469a)#define NPM1300\_GPIO\_CHAN\_2 0x03U

[ 34](group__regulator__npm1300.md#ga4f7cfc353885cc1223a54ec30fe57137)#define NPM1300\_GPIO\_CHAN\_3 0x04U

[ 35](group__regulator__npm1300.md#gac016df7b6f7d356f3f0131a2c44776a6)#define NPM1300\_GPIO\_CHAN\_4 0x05U

36

38

40

41#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_REGULATOR\_NPM1300\_H\_\*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [regulator](dir_9ff35155c0210c7a7568a63cba064bf6.md)
- [npm1300.h](dt-bindings_2regulator_2npm1300_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
