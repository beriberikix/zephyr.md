---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/renesas_00ra-sdram_8h.html
original_path: doxygen/html/renesas_00ra-sdram_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

renesas,ra-sdram.h File Reference

[Go to the source code of this file.](renesas_00ra-sdram_8h_source.md)

| Macros | |
| --- | --- |
| #define | [SDRAM\_TRAS\_1CYCLES](#a9b850c120726df7547a4391d7710e32c)   (1) |
| #define | [SDRAM\_TRAS\_2CYCLES](#ae56fe80b3a7cf24693cdd3a91062d5b0)   (2) |
| #define | [SDRAM\_TRAS\_3CYCLES](#a7db2b7e11b65b3884120afe29d2ea850)   (3) |
| #define | [SDRAM\_TRAS\_4CYCLES](#ac5e882089b27453f5abfb0300bc77fef)   (4) |
| #define | [SDRAM\_TRAS\_5CYCLES](#adc0f55360f454f71daba3504e710d381)   (5) |
| #define | [SDRAM\_TRAS\_6CYCLES](#a399fbd650bd1a42ba019df158859e177)   (6) |
| #define | [SDRAM\_TRAS\_7CYCLES](#a84b66fffb6cd59b46d1e768be3bb197d)   (7) |
| #define | [SDRAM\_TRCD\_1CYCLES](#ab5344383c093df789bf6de852dcf3bf4)   (1) |
| #define | [SDRAM\_TRCD\_2CYCLES](#a351a447807ba1c1a05b24e4387fbdb13)   (2) |
| #define | [SDRAM\_TRCD\_3CYCLES](#a430862adfb21a5f39fe4ed59773fb3de)   (3) |
| #define | [SDRAM\_TRCD\_4CYCLES](#a7a17a0b5ae2ac934701806376bd4e885)   (4) |
| #define | [SDRAM\_TRP\_1CYCLES](#a7da6a6f323234be8d004eb9f860c7fb4)   (1) |
| #define | [SDRAM\_TRP\_2CYCLES](#ab2ef4c3795e5ef8d439990e374af5d4b)   (2) |
| #define | [SDRAM\_TRP\_3CYCLES](#a8f91d45f142412d648b0b2a02a3783f6)   (3) |
| #define | [SDRAM\_TRP\_4CYCLES](#ab7adce344b910c0e7812b1f002277cf5)   (4) |
| #define | [SDRAM\_TRP\_5CYCLES](#ac9fd6953971b6f30c444b80e815ac897)   (5) |
| #define | [SDRAM\_TRP\_6CYCLES](#a5764bb6c6bc2f2fdf42a30f16e9db886)   (6) |
| #define | [SDRAM\_TRP\_7CYCLES](#a313aa75d58ba9a1090d7b4e56ac70af1)   (7) |
| #define | [SDRAM\_TRP\_8CYCLES](#a7d6dddf1b015e76561fa094adabd0deb)   (8) |
| #define | [SDRAM\_TWR\_1CYCLES](#a337ea5f0afbd100aff97272678b8e0f7)   (1) |
| #define | [SDRAM\_TWR\_2CYCLES](#ac42167d4a16b830bee12b16160030f6c)   (2) |
| #define | [SDRAM\_TCL\_1CYCLES](#a7d2ffd62d193559b88e0674d93f7eb9d)   (1) |
| #define | [SDRAM\_TCL\_2CYCLES](#abf6a85ad335bda51df3b473e85c37d4d)   (2) |
| #define | [SDRAM\_TCL\_3CYCLES](#a3a6ff6ff617d57bac16bed60b0414d39)   (3) |
| #define | [SDRAM\_TREFW\_1CYCLES](#aa341847901505e4c120d088f8cf81a6b)   (1) |
| #define | [SDRAM\_TREFW\_2CYCLES](#a42f64511938017f101ee1743dc468566)   (2) |
| #define | [SDRAM\_TREFW\_3CYCLES](#a76b3d7ec8db05603741ccfbd990206c5)   (3) |
| #define | [SDRAM\_TREFW\_4CYCLES](#aebc6f2e149e677324089f3e38dff66f8)   (4) |
| #define | [SDRAM\_TREFW\_5CYCLES](#a07a3097baffa217e1f1600115e5de771)   (5) |
| #define | [SDRAM\_TREFW\_6CYCLES](#a3d383cfff475bd6d5fc609b317d6a32e)   (6) |
| #define | [SDRAM\_TREFW\_7CYCLES](#ab7c186c764db327ab9d69a167705a51d)   (7) |
| #define | [SDRAM\_TREFW\_8CYCLES](#a382715f349c98e860464ab9462754a21)   (8) |
| #define | [SDRAM\_TREFW\_9CYCLES](#af7be8e3c325b79bed6efbe4f64b7956b)   (9) |
| #define | [SDRAM\_TREFW\_10CYCLES](#a69e476f723e7e10bd8482c07afdb27bd)   (10) |
| #define | [SDRAM\_TREFW\_11CYCLES](#aa91823a80305540801509177444889d7)   (11) |
| #define | [SDRAM\_TREFW\_12CYCLES](#aec07c7addb0a76a8a92108e256adea54)   (12) |
| #define | [SDRAM\_TREFW\_13CYCLES](#abd82d203d05abd0c987fd0d550e49918)   (13) |
| #define | [SDRAM\_TREFW\_14CYCLES](#a0a3e172b3b055f7ee285e307dadb6684)   (14) |
| #define | [SDRAM\_TREFW\_15CYCLES](#adb16e78cdd55fb24fa6b887cbedb7a68)   (15) |
| #define | [SDRAM\_TREFW\_16CYCLES](#a1311a16f4443baf064d4bcaa1f06cffe)   (16) |
| #define | [SDRAM\_AUTO\_REFREDSH\_INTERVEL\_3CYCLES](#abe06a5afd49ae6f5d24a7f526126ec27)   (3) |
| #define | [SDRAM\_AUTO\_REFREDSH\_INTERVEL\_4CYCLES](#a52d309aeaf962bd1d99784349a9e8208)   (4) |
| #define | [SDRAM\_AUTO\_REFREDSH\_INTERVEL\_5CYCLES](#af60b53acac99f2142c7cdbdeeefa5cf8)   (5) |
| #define | [SDRAM\_AUTO\_REFREDSH\_INTERVEL\_6CYCLES](#aeb47656cce233836e2e3a9459b8ac441)   (6) |
| #define | [SDRAM\_AUTO\_REFREDSH\_INTERVEL\_7CYCLES](#a6c485f55b5e9efdabfc2d926ea03b229)   (7) |
| #define | [SDRAM\_AUTO\_REFREDSH\_INTERVEL\_8CYCLES](#aedc59973ed65ef75e85aca2d41b2459e)   (8) |
| #define | [SDRAM\_AUTO\_REFREDSH\_INTERVEL\_9CYCLES](#a19d919e93afafcf6dea7bfc8a99805bd)   (9) |
| #define | [SDRAM\_AUTO\_REFREDSH\_INTERVEL\_10CYCLES](#a5da14b883478b20b9b4d3af60a202287)   (10) |
| #define | [SDRAM\_AUTO\_REFREDSH\_INTERVEL\_11CYCLES](#a4ebbafe112637a3aca637c458cecddc8)   (11) |
| #define | [SDRAM\_AUTO\_REFREDSH\_INTERVEL\_12CYCLES](#ab44e73d522dddb4ebf10626e8ce27493)   (12) |
| #define | [SDRAM\_AUTO\_REFREDSH\_INTERVEL\_13CYCLES](#a649e1edd30e2a910d9bb82d34dd1f322)   (13) |
| #define | [SDRAM\_AUTO\_REFREDSH\_INTERVEL\_14CYCLES](#a6c47375d3294b1e2c8e115a0e880de20)   (14) |
| #define | [SDRAM\_AUTO\_REFREDSH\_INTERVEL\_15CYCLES](#a8824e56809ca6885e9a5dd2833626737)   (15) |
| #define | [SDRAM\_AUTO\_REFREDSH\_INTERVEL\_16CYCLES](#a99f366ba2fa48e4030cc717a5735d872)   (16) |
| #define | [SDRAM\_AUTO\_REFREDSH\_INTERVEL\_17CYCLES](#ad49d1e400608ace52e06da95cae1a489)   (17) |
| #define | [SDRAM\_AUTO\_REFREDSH\_INTERVEL\_18CYCLES](#ab4d7084c29384c8c335daaefc4e7af7e)   (18) |
| #define | [SDRAM\_AUTO\_REFREDSH\_INTERVEL\_19CYCLES](#a320ae47ada592354aec26c9f6cfaa3b9)   (19) |
| #define | [SDRAM\_AUTO\_REFREDSH\_INTERVEL\_20CYCLES](#ae1f87478c97ea53a08c9d06ca170cff1)   (20) |
| #define | [SDRAM\_AUTO\_REFREDSH\_COUNT\_1TIMES](#a18aa86a53e70d2281f7de0e680586b49)   (1) |
| #define | [SDRAM\_AUTO\_REFREDSH\_COUNT\_2TIMES](#a4d6d65299224731da80251604d47e079)   (2) |
| #define | [SDRAM\_AUTO\_REFREDSH\_COUNT\_3TIMES](#af0d3fc2afe6b2cb328f5c653302688a9)   (3) |
| #define | [SDRAM\_AUTO\_REFREDSH\_COUNT\_4TIMES](#a533142aa5da537e10c0cbd0bee1018c5)   (4) |
| #define | [SDRAM\_AUTO\_REFREDSH\_COUNT\_5TIMES](#a38f05202792c8f82277083d322bd6d2f)   (5) |
| #define | [SDRAM\_AUTO\_REFREDSH\_COUNT\_6TIMES](#ab3857da549a872313285a289feef8fab)   (6) |
| #define | [SDRAM\_AUTO\_REFREDSH\_COUNT\_7TIMES](#a957d9d80aa82643717354fcef90f97a2)   (7) |
| #define | [SDRAM\_AUTO\_REFREDSH\_COUNT\_8TIMES](#aa43aad8cddcb412ba1075e08caf526e5)   (8) |
| #define | [SDRAM\_AUTO\_REFREDSH\_COUNT\_9TIMES](#af772446539500f0f790c72d84c8c0d34)   (9) |
| #define | [SDRAM\_AUTO\_REFREDSH\_COUNT\_10TIMES](#a8b12580225bc922cc453d2c87e4e3b26)   (10) |
| #define | [SDRAM\_AUTO\_REFREDSH\_COUNT\_11TIMES](#ab338fc16ab1083cef88de9e843ec36d5)   (11) |
| #define | [SDRAM\_AUTO\_REFREDSH\_COUNT\_12TIMES](#a92680601c62e08fbea88e0c503b13c46)   (12) |
| #define | [SDRAM\_AUTO\_REFREDSH\_COUNT\_13TIMES](#abc964a0f4ddf21a683bd4b9d62949b28)   (13) |
| #define | [SDRAM\_AUTO\_REFREDSH\_COUNT\_14TIMES](#a11b0c2995123682f07cafdcc4dd1b537)   (14) |
| #define | [SDRAM\_AUTO\_REFREDSH\_COUNT\_15TIMES](#ab46713ce532d63e0428c041e0d0cd71c)   (15) |
| #define | [SDRAM\_AUTO\_PRECHARGE\_CYCLE\_3CYCLES](#a406f57aa0281b0ce476ad5395f02d15b)   (3) |
| #define | [SDRAM\_AUTO\_PRECHARGE\_CYCLE\_4CYCLES](#a221ae04856f704891acfe619a9bdfc0b)   (4) |
| #define | [SDRAM\_AUTO\_PRECHARGE\_CYCLE\_5CYCLES](#a82d40091de1ecdec12401f6ebd3e013a)   (5) |
| #define | [SDRAM\_AUTO\_PRECHARGE\_CYCLE\_6CYCLES](#a623422304d18ec5514a1312aaad4635c)   (6) |
| #define | [SDRAM\_AUTO\_PRECHARGE\_CYCLE\_7CYCLES](#ab33684fc510a12a571d26ddf891eec0c)   (7) |
| #define | [SDRAM\_AUTO\_PRECHARGE\_CYCLE\_8CYCLES](#adbd5ea5398feee92dab73bfdf439c8f7)   (8) |
| #define | [SDRAM\_AUTO\_PRECHARGE\_CYCLE\_9CYCLES](#aa0c6b2c201a96a3507a2f1fe1d539dfd)   (9) |
| #define | [SDRAM\_AUTO\_PRECHARGE\_CYCLE\_10CYCLES](#a20a46130d1ac000ce379e40de015ef69)   (10) |

## Macro Definition Documentation

## [◆ ](#a20a46130d1ac000ce379e40de015ef69)SDRAM\_AUTO\_PRECHARGE\_CYCLE\_10CYCLES

| #define SDRAM\_AUTO\_PRECHARGE\_CYCLE\_10CYCLES   (10) |
| --- |

## [◆ ](#a406f57aa0281b0ce476ad5395f02d15b)SDRAM\_AUTO\_PRECHARGE\_CYCLE\_3CYCLES

| #define SDRAM\_AUTO\_PRECHARGE\_CYCLE\_3CYCLES   (3) |
| --- |

## [◆ ](#a221ae04856f704891acfe619a9bdfc0b)SDRAM\_AUTO\_PRECHARGE\_CYCLE\_4CYCLES

| #define SDRAM\_AUTO\_PRECHARGE\_CYCLE\_4CYCLES   (4) |
| --- |

## [◆ ](#a82d40091de1ecdec12401f6ebd3e013a)SDRAM\_AUTO\_PRECHARGE\_CYCLE\_5CYCLES

| #define SDRAM\_AUTO\_PRECHARGE\_CYCLE\_5CYCLES   (5) |
| --- |

## [◆ ](#a623422304d18ec5514a1312aaad4635c)SDRAM\_AUTO\_PRECHARGE\_CYCLE\_6CYCLES

| #define SDRAM\_AUTO\_PRECHARGE\_CYCLE\_6CYCLES   (6) |
| --- |

## [◆ ](#ab33684fc510a12a571d26ddf891eec0c)SDRAM\_AUTO\_PRECHARGE\_CYCLE\_7CYCLES

| #define SDRAM\_AUTO\_PRECHARGE\_CYCLE\_7CYCLES   (7) |
| --- |

## [◆ ](#adbd5ea5398feee92dab73bfdf439c8f7)SDRAM\_AUTO\_PRECHARGE\_CYCLE\_8CYCLES

| #define SDRAM\_AUTO\_PRECHARGE\_CYCLE\_8CYCLES   (8) |
| --- |

## [◆ ](#aa0c6b2c201a96a3507a2f1fe1d539dfd)SDRAM\_AUTO\_PRECHARGE\_CYCLE\_9CYCLES

| #define SDRAM\_AUTO\_PRECHARGE\_CYCLE\_9CYCLES   (9) |
| --- |

## [◆ ](#a8b12580225bc922cc453d2c87e4e3b26)SDRAM\_AUTO\_REFREDSH\_COUNT\_10TIMES

| #define SDRAM\_AUTO\_REFREDSH\_COUNT\_10TIMES   (10) |
| --- |

## [◆ ](#ab338fc16ab1083cef88de9e843ec36d5)SDRAM\_AUTO\_REFREDSH\_COUNT\_11TIMES

| #define SDRAM\_AUTO\_REFREDSH\_COUNT\_11TIMES   (11) |
| --- |

## [◆ ](#a92680601c62e08fbea88e0c503b13c46)SDRAM\_AUTO\_REFREDSH\_COUNT\_12TIMES

| #define SDRAM\_AUTO\_REFREDSH\_COUNT\_12TIMES   (12) |
| --- |

## [◆ ](#abc964a0f4ddf21a683bd4b9d62949b28)SDRAM\_AUTO\_REFREDSH\_COUNT\_13TIMES

| #define SDRAM\_AUTO\_REFREDSH\_COUNT\_13TIMES   (13) |
| --- |

## [◆ ](#a11b0c2995123682f07cafdcc4dd1b537)SDRAM\_AUTO\_REFREDSH\_COUNT\_14TIMES

| #define SDRAM\_AUTO\_REFREDSH\_COUNT\_14TIMES   (14) |
| --- |

## [◆ ](#ab46713ce532d63e0428c041e0d0cd71c)SDRAM\_AUTO\_REFREDSH\_COUNT\_15TIMES

| #define SDRAM\_AUTO\_REFREDSH\_COUNT\_15TIMES   (15) |
| --- |

## [◆ ](#a18aa86a53e70d2281f7de0e680586b49)SDRAM\_AUTO\_REFREDSH\_COUNT\_1TIMES

| #define SDRAM\_AUTO\_REFREDSH\_COUNT\_1TIMES   (1) |
| --- |

## [◆ ](#a4d6d65299224731da80251604d47e079)SDRAM\_AUTO\_REFREDSH\_COUNT\_2TIMES

| #define SDRAM\_AUTO\_REFREDSH\_COUNT\_2TIMES   (2) |
| --- |

## [◆ ](#af0d3fc2afe6b2cb328f5c653302688a9)SDRAM\_AUTO\_REFREDSH\_COUNT\_3TIMES

| #define SDRAM\_AUTO\_REFREDSH\_COUNT\_3TIMES   (3) |
| --- |

## [◆ ](#a533142aa5da537e10c0cbd0bee1018c5)SDRAM\_AUTO\_REFREDSH\_COUNT\_4TIMES

| #define SDRAM\_AUTO\_REFREDSH\_COUNT\_4TIMES   (4) |
| --- |

## [◆ ](#a38f05202792c8f82277083d322bd6d2f)SDRAM\_AUTO\_REFREDSH\_COUNT\_5TIMES

| #define SDRAM\_AUTO\_REFREDSH\_COUNT\_5TIMES   (5) |
| --- |

## [◆ ](#ab3857da549a872313285a289feef8fab)SDRAM\_AUTO\_REFREDSH\_COUNT\_6TIMES

| #define SDRAM\_AUTO\_REFREDSH\_COUNT\_6TIMES   (6) |
| --- |

## [◆ ](#a957d9d80aa82643717354fcef90f97a2)SDRAM\_AUTO\_REFREDSH\_COUNT\_7TIMES

| #define SDRAM\_AUTO\_REFREDSH\_COUNT\_7TIMES   (7) |
| --- |

## [◆ ](#aa43aad8cddcb412ba1075e08caf526e5)SDRAM\_AUTO\_REFREDSH\_COUNT\_8TIMES

| #define SDRAM\_AUTO\_REFREDSH\_COUNT\_8TIMES   (8) |
| --- |

## [◆ ](#af772446539500f0f790c72d84c8c0d34)SDRAM\_AUTO\_REFREDSH\_COUNT\_9TIMES

| #define SDRAM\_AUTO\_REFREDSH\_COUNT\_9TIMES   (9) |
| --- |

## [◆ ](#a5da14b883478b20b9b4d3af60a202287)SDRAM\_AUTO\_REFREDSH\_INTERVEL\_10CYCLES

| #define SDRAM\_AUTO\_REFREDSH\_INTERVEL\_10CYCLES   (10) |
| --- |

## [◆ ](#a4ebbafe112637a3aca637c458cecddc8)SDRAM\_AUTO\_REFREDSH\_INTERVEL\_11CYCLES

| #define SDRAM\_AUTO\_REFREDSH\_INTERVEL\_11CYCLES   (11) |
| --- |

## [◆ ](#ab44e73d522dddb4ebf10626e8ce27493)SDRAM\_AUTO\_REFREDSH\_INTERVEL\_12CYCLES

| #define SDRAM\_AUTO\_REFREDSH\_INTERVEL\_12CYCLES   (12) |
| --- |

## [◆ ](#a649e1edd30e2a910d9bb82d34dd1f322)SDRAM\_AUTO\_REFREDSH\_INTERVEL\_13CYCLES

| #define SDRAM\_AUTO\_REFREDSH\_INTERVEL\_13CYCLES   (13) |
| --- |

## [◆ ](#a6c47375d3294b1e2c8e115a0e880de20)SDRAM\_AUTO\_REFREDSH\_INTERVEL\_14CYCLES

| #define SDRAM\_AUTO\_REFREDSH\_INTERVEL\_14CYCLES   (14) |
| --- |

## [◆ ](#a8824e56809ca6885e9a5dd2833626737)SDRAM\_AUTO\_REFREDSH\_INTERVEL\_15CYCLES

| #define SDRAM\_AUTO\_REFREDSH\_INTERVEL\_15CYCLES   (15) |
| --- |

## [◆ ](#a99f366ba2fa48e4030cc717a5735d872)SDRAM\_AUTO\_REFREDSH\_INTERVEL\_16CYCLES

| #define SDRAM\_AUTO\_REFREDSH\_INTERVEL\_16CYCLES   (16) |
| --- |

## [◆ ](#ad49d1e400608ace52e06da95cae1a489)SDRAM\_AUTO\_REFREDSH\_INTERVEL\_17CYCLES

| #define SDRAM\_AUTO\_REFREDSH\_INTERVEL\_17CYCLES   (17) |
| --- |

## [◆ ](#ab4d7084c29384c8c335daaefc4e7af7e)SDRAM\_AUTO\_REFREDSH\_INTERVEL\_18CYCLES

| #define SDRAM\_AUTO\_REFREDSH\_INTERVEL\_18CYCLES   (18) |
| --- |

## [◆ ](#a320ae47ada592354aec26c9f6cfaa3b9)SDRAM\_AUTO\_REFREDSH\_INTERVEL\_19CYCLES

| #define SDRAM\_AUTO\_REFREDSH\_INTERVEL\_19CYCLES   (19) |
| --- |

## [◆ ](#ae1f87478c97ea53a08c9d06ca170cff1)SDRAM\_AUTO\_REFREDSH\_INTERVEL\_20CYCLES

| #define SDRAM\_AUTO\_REFREDSH\_INTERVEL\_20CYCLES   (20) |
| --- |

## [◆ ](#abe06a5afd49ae6f5d24a7f526126ec27)SDRAM\_AUTO\_REFREDSH\_INTERVEL\_3CYCLES

| #define SDRAM\_AUTO\_REFREDSH\_INTERVEL\_3CYCLES   (3) |
| --- |

## [◆ ](#a52d309aeaf962bd1d99784349a9e8208)SDRAM\_AUTO\_REFREDSH\_INTERVEL\_4CYCLES

| #define SDRAM\_AUTO\_REFREDSH\_INTERVEL\_4CYCLES   (4) |
| --- |

## [◆ ](#af60b53acac99f2142c7cdbdeeefa5cf8)SDRAM\_AUTO\_REFREDSH\_INTERVEL\_5CYCLES

| #define SDRAM\_AUTO\_REFREDSH\_INTERVEL\_5CYCLES   (5) |
| --- |

## [◆ ](#aeb47656cce233836e2e3a9459b8ac441)SDRAM\_AUTO\_REFREDSH\_INTERVEL\_6CYCLES

| #define SDRAM\_AUTO\_REFREDSH\_INTERVEL\_6CYCLES   (6) |
| --- |

## [◆ ](#a6c485f55b5e9efdabfc2d926ea03b229)SDRAM\_AUTO\_REFREDSH\_INTERVEL\_7CYCLES

| #define SDRAM\_AUTO\_REFREDSH\_INTERVEL\_7CYCLES   (7) |
| --- |

## [◆ ](#aedc59973ed65ef75e85aca2d41b2459e)SDRAM\_AUTO\_REFREDSH\_INTERVEL\_8CYCLES

| #define SDRAM\_AUTO\_REFREDSH\_INTERVEL\_8CYCLES   (8) |
| --- |

## [◆ ](#a19d919e93afafcf6dea7bfc8a99805bd)SDRAM\_AUTO\_REFREDSH\_INTERVEL\_9CYCLES

| #define SDRAM\_AUTO\_REFREDSH\_INTERVEL\_9CYCLES   (9) |
| --- |

## [◆ ](#a7d2ffd62d193559b88e0674d93f7eb9d)SDRAM\_TCL\_1CYCLES

| #define SDRAM\_TCL\_1CYCLES   (1) |
| --- |

## [◆ ](#abf6a85ad335bda51df3b473e85c37d4d)SDRAM\_TCL\_2CYCLES

| #define SDRAM\_TCL\_2CYCLES   (2) |
| --- |

## [◆ ](#a3a6ff6ff617d57bac16bed60b0414d39)SDRAM\_TCL\_3CYCLES

| #define SDRAM\_TCL\_3CYCLES   (3) |
| --- |

## [◆ ](#a9b850c120726df7547a4391d7710e32c)SDRAM\_TRAS\_1CYCLES

| #define SDRAM\_TRAS\_1CYCLES   (1) |
| --- |

## [◆ ](#ae56fe80b3a7cf24693cdd3a91062d5b0)SDRAM\_TRAS\_2CYCLES

| #define SDRAM\_TRAS\_2CYCLES   (2) |
| --- |

## [◆ ](#a7db2b7e11b65b3884120afe29d2ea850)SDRAM\_TRAS\_3CYCLES

| #define SDRAM\_TRAS\_3CYCLES   (3) |
| --- |

## [◆ ](#ac5e882089b27453f5abfb0300bc77fef)SDRAM\_TRAS\_4CYCLES

| #define SDRAM\_TRAS\_4CYCLES   (4) |
| --- |

## [◆ ](#adc0f55360f454f71daba3504e710d381)SDRAM\_TRAS\_5CYCLES

| #define SDRAM\_TRAS\_5CYCLES   (5) |
| --- |

## [◆ ](#a399fbd650bd1a42ba019df158859e177)SDRAM\_TRAS\_6CYCLES

| #define SDRAM\_TRAS\_6CYCLES   (6) |
| --- |

## [◆ ](#a84b66fffb6cd59b46d1e768be3bb197d)SDRAM\_TRAS\_7CYCLES

| #define SDRAM\_TRAS\_7CYCLES   (7) |
| --- |

## [◆ ](#ab5344383c093df789bf6de852dcf3bf4)SDRAM\_TRCD\_1CYCLES

| #define SDRAM\_TRCD\_1CYCLES   (1) |
| --- |

## [◆ ](#a351a447807ba1c1a05b24e4387fbdb13)SDRAM\_TRCD\_2CYCLES

| #define SDRAM\_TRCD\_2CYCLES   (2) |
| --- |

## [◆ ](#a430862adfb21a5f39fe4ed59773fb3de)SDRAM\_TRCD\_3CYCLES

| #define SDRAM\_TRCD\_3CYCLES   (3) |
| --- |

## [◆ ](#a7a17a0b5ae2ac934701806376bd4e885)SDRAM\_TRCD\_4CYCLES

| #define SDRAM\_TRCD\_4CYCLES   (4) |
| --- |

## [◆ ](#a69e476f723e7e10bd8482c07afdb27bd)SDRAM\_TREFW\_10CYCLES

| #define SDRAM\_TREFW\_10CYCLES   (10) |
| --- |

## [◆ ](#aa91823a80305540801509177444889d7)SDRAM\_TREFW\_11CYCLES

| #define SDRAM\_TREFW\_11CYCLES   (11) |
| --- |

## [◆ ](#aec07c7addb0a76a8a92108e256adea54)SDRAM\_TREFW\_12CYCLES

| #define SDRAM\_TREFW\_12CYCLES   (12) |
| --- |

## [◆ ](#abd82d203d05abd0c987fd0d550e49918)SDRAM\_TREFW\_13CYCLES

| #define SDRAM\_TREFW\_13CYCLES   (13) |
| --- |

## [◆ ](#a0a3e172b3b055f7ee285e307dadb6684)SDRAM\_TREFW\_14CYCLES

| #define SDRAM\_TREFW\_14CYCLES   (14) |
| --- |

## [◆ ](#adb16e78cdd55fb24fa6b887cbedb7a68)SDRAM\_TREFW\_15CYCLES

| #define SDRAM\_TREFW\_15CYCLES   (15) |
| --- |

## [◆ ](#a1311a16f4443baf064d4bcaa1f06cffe)SDRAM\_TREFW\_16CYCLES

| #define SDRAM\_TREFW\_16CYCLES   (16) |
| --- |

## [◆ ](#aa341847901505e4c120d088f8cf81a6b)SDRAM\_TREFW\_1CYCLES

| #define SDRAM\_TREFW\_1CYCLES   (1) |
| --- |

## [◆ ](#a42f64511938017f101ee1743dc468566)SDRAM\_TREFW\_2CYCLES

| #define SDRAM\_TREFW\_2CYCLES   (2) |
| --- |

## [◆ ](#a76b3d7ec8db05603741ccfbd990206c5)SDRAM\_TREFW\_3CYCLES

| #define SDRAM\_TREFW\_3CYCLES   (3) |
| --- |

## [◆ ](#aebc6f2e149e677324089f3e38dff66f8)SDRAM\_TREFW\_4CYCLES

| #define SDRAM\_TREFW\_4CYCLES   (4) |
| --- |

## [◆ ](#a07a3097baffa217e1f1600115e5de771)SDRAM\_TREFW\_5CYCLES

| #define SDRAM\_TREFW\_5CYCLES   (5) |
| --- |

## [◆ ](#a3d383cfff475bd6d5fc609b317d6a32e)SDRAM\_TREFW\_6CYCLES

| #define SDRAM\_TREFW\_6CYCLES   (6) |
| --- |

## [◆ ](#ab7c186c764db327ab9d69a167705a51d)SDRAM\_TREFW\_7CYCLES

| #define SDRAM\_TREFW\_7CYCLES   (7) |
| --- |

## [◆ ](#a382715f349c98e860464ab9462754a21)SDRAM\_TREFW\_8CYCLES

| #define SDRAM\_TREFW\_8CYCLES   (8) |
| --- |

## [◆ ](#af7be8e3c325b79bed6efbe4f64b7956b)SDRAM\_TREFW\_9CYCLES

| #define SDRAM\_TREFW\_9CYCLES   (9) |
| --- |

## [◆ ](#a7da6a6f323234be8d004eb9f860c7fb4)SDRAM\_TRP\_1CYCLES

| #define SDRAM\_TRP\_1CYCLES   (1) |
| --- |

## [◆ ](#ab2ef4c3795e5ef8d439990e374af5d4b)SDRAM\_TRP\_2CYCLES

| #define SDRAM\_TRP\_2CYCLES   (2) |
| --- |

## [◆ ](#a8f91d45f142412d648b0b2a02a3783f6)SDRAM\_TRP\_3CYCLES

| #define SDRAM\_TRP\_3CYCLES   (3) |
| --- |

## [◆ ](#ab7adce344b910c0e7812b1f002277cf5)SDRAM\_TRP\_4CYCLES

| #define SDRAM\_TRP\_4CYCLES   (4) |
| --- |

## [◆ ](#ac9fd6953971b6f30c444b80e815ac897)SDRAM\_TRP\_5CYCLES

| #define SDRAM\_TRP\_5CYCLES   (5) |
| --- |

## [◆ ](#a5764bb6c6bc2f2fdf42a30f16e9db886)SDRAM\_TRP\_6CYCLES

| #define SDRAM\_TRP\_6CYCLES   (6) |
| --- |

## [◆ ](#a313aa75d58ba9a1090d7b4e56ac70af1)SDRAM\_TRP\_7CYCLES

| #define SDRAM\_TRP\_7CYCLES   (7) |
| --- |

## [◆ ](#a7d6dddf1b015e76561fa094adabd0deb)SDRAM\_TRP\_8CYCLES

| #define SDRAM\_TRP\_8CYCLES   (8) |
| --- |

## [◆ ](#a337ea5f0afbd100aff97272678b8e0f7)SDRAM\_TWR\_1CYCLES

| #define SDRAM\_TWR\_1CYCLES   (1) |
| --- |

## [◆ ](#ac42167d4a16b830bee12b16160030f6c)SDRAM\_TWR\_2CYCLES

| #define SDRAM\_TWR\_2CYCLES   (2) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [memory-controller](dir_35d961eb615f3ea19ec1fece6b4faa4b.md)
- [renesas,ra-sdram.h](renesas_00ra-sdram_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
