---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/renesas_00ra-sdram_8h_source.html
original_path: doxygen/html/renesas_00ra-sdram_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

renesas,ra-sdram.h

[Go to the documentation of this file.](renesas_00ra-sdram_8h.md)

1/\*

2 \* Copyright (c) 2024 Renesas Electronics Corporation

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_MEMORY\_CONTROLLER\_RENESAS\_RA\_SDRAM\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_MEMORY\_CONTROLLER\_RENESAS\_RA\_SDRAM\_H\_

8

[ 9](renesas_00ra-sdram_8h.md#a9b850c120726df7547a4391d7710e32c)#define SDRAM\_TRAS\_1CYCLES (1)

[ 10](renesas_00ra-sdram_8h.md#ae56fe80b3a7cf24693cdd3a91062d5b0)#define SDRAM\_TRAS\_2CYCLES (2)

[ 11](renesas_00ra-sdram_8h.md#a7db2b7e11b65b3884120afe29d2ea850)#define SDRAM\_TRAS\_3CYCLES (3)

[ 12](renesas_00ra-sdram_8h.md#ac5e882089b27453f5abfb0300bc77fef)#define SDRAM\_TRAS\_4CYCLES (4)

[ 13](renesas_00ra-sdram_8h.md#adc0f55360f454f71daba3504e710d381)#define SDRAM\_TRAS\_5CYCLES (5)

[ 14](renesas_00ra-sdram_8h.md#a399fbd650bd1a42ba019df158859e177)#define SDRAM\_TRAS\_6CYCLES (6)

[ 15](renesas_00ra-sdram_8h.md#a84b66fffb6cd59b46d1e768be3bb197d)#define SDRAM\_TRAS\_7CYCLES (7)

16

[ 17](renesas_00ra-sdram_8h.md#ab5344383c093df789bf6de852dcf3bf4)#define SDRAM\_TRCD\_1CYCLES (1)

[ 18](renesas_00ra-sdram_8h.md#a351a447807ba1c1a05b24e4387fbdb13)#define SDRAM\_TRCD\_2CYCLES (2)

[ 19](renesas_00ra-sdram_8h.md#a430862adfb21a5f39fe4ed59773fb3de)#define SDRAM\_TRCD\_3CYCLES (3)

[ 20](renesas_00ra-sdram_8h.md#a7a17a0b5ae2ac934701806376bd4e885)#define SDRAM\_TRCD\_4CYCLES (4)

21

[ 22](renesas_00ra-sdram_8h.md#a7da6a6f323234be8d004eb9f860c7fb4)#define SDRAM\_TRP\_1CYCLES (1)

[ 23](renesas_00ra-sdram_8h.md#ab2ef4c3795e5ef8d439990e374af5d4b)#define SDRAM\_TRP\_2CYCLES (2)

[ 24](renesas_00ra-sdram_8h.md#a8f91d45f142412d648b0b2a02a3783f6)#define SDRAM\_TRP\_3CYCLES (3)

[ 25](renesas_00ra-sdram_8h.md#ab7adce344b910c0e7812b1f002277cf5)#define SDRAM\_TRP\_4CYCLES (4)

[ 26](renesas_00ra-sdram_8h.md#ac9fd6953971b6f30c444b80e815ac897)#define SDRAM\_TRP\_5CYCLES (5)

[ 27](renesas_00ra-sdram_8h.md#a5764bb6c6bc2f2fdf42a30f16e9db886)#define SDRAM\_TRP\_6CYCLES (6)

[ 28](renesas_00ra-sdram_8h.md#a313aa75d58ba9a1090d7b4e56ac70af1)#define SDRAM\_TRP\_7CYCLES (7)

[ 29](renesas_00ra-sdram_8h.md#a7d6dddf1b015e76561fa094adabd0deb)#define SDRAM\_TRP\_8CYCLES (8)

30

[ 31](renesas_00ra-sdram_8h.md#a337ea5f0afbd100aff97272678b8e0f7)#define SDRAM\_TWR\_1CYCLES (1)

[ 32](renesas_00ra-sdram_8h.md#ac42167d4a16b830bee12b16160030f6c)#define SDRAM\_TWR\_2CYCLES (2)

33

[ 34](renesas_00ra-sdram_8h.md#a7d2ffd62d193559b88e0674d93f7eb9d)#define SDRAM\_TCL\_1CYCLES (1)

[ 35](renesas_00ra-sdram_8h.md#abf6a85ad335bda51df3b473e85c37d4d)#define SDRAM\_TCL\_2CYCLES (2)

[ 36](renesas_00ra-sdram_8h.md#a3a6ff6ff617d57bac16bed60b0414d39)#define SDRAM\_TCL\_3CYCLES (3)

37

[ 38](renesas_00ra-sdram_8h.md#aa341847901505e4c120d088f8cf81a6b)#define SDRAM\_TREFW\_1CYCLES (1)

[ 39](renesas_00ra-sdram_8h.md#a42f64511938017f101ee1743dc468566)#define SDRAM\_TREFW\_2CYCLES (2)

[ 40](renesas_00ra-sdram_8h.md#a76b3d7ec8db05603741ccfbd990206c5)#define SDRAM\_TREFW\_3CYCLES (3)

[ 41](renesas_00ra-sdram_8h.md#aebc6f2e149e677324089f3e38dff66f8)#define SDRAM\_TREFW\_4CYCLES (4)

[ 42](renesas_00ra-sdram_8h.md#a07a3097baffa217e1f1600115e5de771)#define SDRAM\_TREFW\_5CYCLES (5)

[ 43](renesas_00ra-sdram_8h.md#a3d383cfff475bd6d5fc609b317d6a32e)#define SDRAM\_TREFW\_6CYCLES (6)

[ 44](renesas_00ra-sdram_8h.md#ab7c186c764db327ab9d69a167705a51d)#define SDRAM\_TREFW\_7CYCLES (7)

[ 45](renesas_00ra-sdram_8h.md#a382715f349c98e860464ab9462754a21)#define SDRAM\_TREFW\_8CYCLES (8)

[ 46](renesas_00ra-sdram_8h.md#af7be8e3c325b79bed6efbe4f64b7956b)#define SDRAM\_TREFW\_9CYCLES (9)

[ 47](renesas_00ra-sdram_8h.md#a69e476f723e7e10bd8482c07afdb27bd)#define SDRAM\_TREFW\_10CYCLES (10)

[ 48](renesas_00ra-sdram_8h.md#aa91823a80305540801509177444889d7)#define SDRAM\_TREFW\_11CYCLES (11)

[ 49](renesas_00ra-sdram_8h.md#aec07c7addb0a76a8a92108e256adea54)#define SDRAM\_TREFW\_12CYCLES (12)

[ 50](renesas_00ra-sdram_8h.md#abd82d203d05abd0c987fd0d550e49918)#define SDRAM\_TREFW\_13CYCLES (13)

[ 51](renesas_00ra-sdram_8h.md#a0a3e172b3b055f7ee285e307dadb6684)#define SDRAM\_TREFW\_14CYCLES (14)

[ 52](renesas_00ra-sdram_8h.md#adb16e78cdd55fb24fa6b887cbedb7a68)#define SDRAM\_TREFW\_15CYCLES (15)

[ 53](renesas_00ra-sdram_8h.md#a1311a16f4443baf064d4bcaa1f06cffe)#define SDRAM\_TREFW\_16CYCLES (16)

54

[ 55](renesas_00ra-sdram_8h.md#abe06a5afd49ae6f5d24a7f526126ec27)#define SDRAM\_AUTO\_REFREDSH\_INTERVEL\_3CYCLES (3)

[ 56](renesas_00ra-sdram_8h.md#a52d309aeaf962bd1d99784349a9e8208)#define SDRAM\_AUTO\_REFREDSH\_INTERVEL\_4CYCLES (4)

[ 57](renesas_00ra-sdram_8h.md#af60b53acac99f2142c7cdbdeeefa5cf8)#define SDRAM\_AUTO\_REFREDSH\_INTERVEL\_5CYCLES (5)

[ 58](renesas_00ra-sdram_8h.md#aeb47656cce233836e2e3a9459b8ac441)#define SDRAM\_AUTO\_REFREDSH\_INTERVEL\_6CYCLES (6)

[ 59](renesas_00ra-sdram_8h.md#a6c485f55b5e9efdabfc2d926ea03b229)#define SDRAM\_AUTO\_REFREDSH\_INTERVEL\_7CYCLES (7)

[ 60](renesas_00ra-sdram_8h.md#aedc59973ed65ef75e85aca2d41b2459e)#define SDRAM\_AUTO\_REFREDSH\_INTERVEL\_8CYCLES (8)

[ 61](renesas_00ra-sdram_8h.md#a19d919e93afafcf6dea7bfc8a99805bd)#define SDRAM\_AUTO\_REFREDSH\_INTERVEL\_9CYCLES (9)

[ 62](renesas_00ra-sdram_8h.md#a5da14b883478b20b9b4d3af60a202287)#define SDRAM\_AUTO\_REFREDSH\_INTERVEL\_10CYCLES (10)

[ 63](renesas_00ra-sdram_8h.md#a4ebbafe112637a3aca637c458cecddc8)#define SDRAM\_AUTO\_REFREDSH\_INTERVEL\_11CYCLES (11)

[ 64](renesas_00ra-sdram_8h.md#ab44e73d522dddb4ebf10626e8ce27493)#define SDRAM\_AUTO\_REFREDSH\_INTERVEL\_12CYCLES (12)

[ 65](renesas_00ra-sdram_8h.md#a649e1edd30e2a910d9bb82d34dd1f322)#define SDRAM\_AUTO\_REFREDSH\_INTERVEL\_13CYCLES (13)

[ 66](renesas_00ra-sdram_8h.md#a6c47375d3294b1e2c8e115a0e880de20)#define SDRAM\_AUTO\_REFREDSH\_INTERVEL\_14CYCLES (14)

[ 67](renesas_00ra-sdram_8h.md#a8824e56809ca6885e9a5dd2833626737)#define SDRAM\_AUTO\_REFREDSH\_INTERVEL\_15CYCLES (15)

[ 68](renesas_00ra-sdram_8h.md#a99f366ba2fa48e4030cc717a5735d872)#define SDRAM\_AUTO\_REFREDSH\_INTERVEL\_16CYCLES (16)

[ 69](renesas_00ra-sdram_8h.md#ad49d1e400608ace52e06da95cae1a489)#define SDRAM\_AUTO\_REFREDSH\_INTERVEL\_17CYCLES (17)

[ 70](renesas_00ra-sdram_8h.md#ab4d7084c29384c8c335daaefc4e7af7e)#define SDRAM\_AUTO\_REFREDSH\_INTERVEL\_18CYCLES (18)

[ 71](renesas_00ra-sdram_8h.md#a320ae47ada592354aec26c9f6cfaa3b9)#define SDRAM\_AUTO\_REFREDSH\_INTERVEL\_19CYCLES (19)

[ 72](renesas_00ra-sdram_8h.md#ae1f87478c97ea53a08c9d06ca170cff1)#define SDRAM\_AUTO\_REFREDSH\_INTERVEL\_20CYCLES (20)

73

[ 74](renesas_00ra-sdram_8h.md#a18aa86a53e70d2281f7de0e680586b49)#define SDRAM\_AUTO\_REFREDSH\_COUNT\_1TIMES (1)

[ 75](renesas_00ra-sdram_8h.md#a4d6d65299224731da80251604d47e079)#define SDRAM\_AUTO\_REFREDSH\_COUNT\_2TIMES (2)

[ 76](renesas_00ra-sdram_8h.md#af0d3fc2afe6b2cb328f5c653302688a9)#define SDRAM\_AUTO\_REFREDSH\_COUNT\_3TIMES (3)

[ 77](renesas_00ra-sdram_8h.md#a533142aa5da537e10c0cbd0bee1018c5)#define SDRAM\_AUTO\_REFREDSH\_COUNT\_4TIMES (4)

[ 78](renesas_00ra-sdram_8h.md#a38f05202792c8f82277083d322bd6d2f)#define SDRAM\_AUTO\_REFREDSH\_COUNT\_5TIMES (5)

[ 79](renesas_00ra-sdram_8h.md#ab3857da549a872313285a289feef8fab)#define SDRAM\_AUTO\_REFREDSH\_COUNT\_6TIMES (6)

[ 80](renesas_00ra-sdram_8h.md#a957d9d80aa82643717354fcef90f97a2)#define SDRAM\_AUTO\_REFREDSH\_COUNT\_7TIMES (7)

[ 81](renesas_00ra-sdram_8h.md#aa43aad8cddcb412ba1075e08caf526e5)#define SDRAM\_AUTO\_REFREDSH\_COUNT\_8TIMES (8)

[ 82](renesas_00ra-sdram_8h.md#af772446539500f0f790c72d84c8c0d34)#define SDRAM\_AUTO\_REFREDSH\_COUNT\_9TIMES (9)

[ 83](renesas_00ra-sdram_8h.md#a8b12580225bc922cc453d2c87e4e3b26)#define SDRAM\_AUTO\_REFREDSH\_COUNT\_10TIMES (10)

[ 84](renesas_00ra-sdram_8h.md#ab338fc16ab1083cef88de9e843ec36d5)#define SDRAM\_AUTO\_REFREDSH\_COUNT\_11TIMES (11)

[ 85](renesas_00ra-sdram_8h.md#a92680601c62e08fbea88e0c503b13c46)#define SDRAM\_AUTO\_REFREDSH\_COUNT\_12TIMES (12)

[ 86](renesas_00ra-sdram_8h.md#abc964a0f4ddf21a683bd4b9d62949b28)#define SDRAM\_AUTO\_REFREDSH\_COUNT\_13TIMES (13)

[ 87](renesas_00ra-sdram_8h.md#a11b0c2995123682f07cafdcc4dd1b537)#define SDRAM\_AUTO\_REFREDSH\_COUNT\_14TIMES (14)

[ 88](renesas_00ra-sdram_8h.md#ab46713ce532d63e0428c041e0d0cd71c)#define SDRAM\_AUTO\_REFREDSH\_COUNT\_15TIMES (15)

89

[ 90](renesas_00ra-sdram_8h.md#a406f57aa0281b0ce476ad5395f02d15b)#define SDRAM\_AUTO\_PRECHARGE\_CYCLE\_3CYCLES (3)

[ 91](renesas_00ra-sdram_8h.md#a221ae04856f704891acfe619a9bdfc0b)#define SDRAM\_AUTO\_PRECHARGE\_CYCLE\_4CYCLES (4)

[ 92](renesas_00ra-sdram_8h.md#a82d40091de1ecdec12401f6ebd3e013a)#define SDRAM\_AUTO\_PRECHARGE\_CYCLE\_5CYCLES (5)

[ 93](renesas_00ra-sdram_8h.md#a623422304d18ec5514a1312aaad4635c)#define SDRAM\_AUTO\_PRECHARGE\_CYCLE\_6CYCLES (6)

[ 94](renesas_00ra-sdram_8h.md#ab33684fc510a12a571d26ddf891eec0c)#define SDRAM\_AUTO\_PRECHARGE\_CYCLE\_7CYCLES (7)

[ 95](renesas_00ra-sdram_8h.md#adbd5ea5398feee92dab73bfdf439c8f7)#define SDRAM\_AUTO\_PRECHARGE\_CYCLE\_8CYCLES (8)

[ 96](renesas_00ra-sdram_8h.md#aa0c6b2c201a96a3507a2f1fe1d539dfd)#define SDRAM\_AUTO\_PRECHARGE\_CYCLE\_9CYCLES (9)

[ 97](renesas_00ra-sdram_8h.md#a20a46130d1ac000ce379e40de015ef69)#define SDRAM\_AUTO\_PRECHARGE\_CYCLE\_10CYCLES (10)

98

99#endif

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [memory-controller](dir_35d961eb615f3ea19ec1fece6b4faa4b.md)
- [renesas,ra-sdram.h](renesas_00ra-sdram_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
