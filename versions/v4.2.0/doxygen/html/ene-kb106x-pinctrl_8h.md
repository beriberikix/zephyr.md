---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/ene-kb106x-pinctrl_8h.html
original_path: doxygen/html/ene-kb106x-pinctrl_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ene-kb106x-pinctrl.h File Reference

`#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h_source.md)>`

[Go to the source code of this file.](ene-kb106x-pinctrl_8h_source.md)

| Macros | |
| --- | --- |
| #define | [PINMUX\_FUNC\_GPIO](#ab5585e56327f2b23ec89ba9debba0ee2)   0x00 |
| #define | [PINMUX\_FUNC\_A](#a98cfa6f81cd2d924b4b8410cc58dcced)   0x00 |
| #define | [PINMUX\_FUNC\_B](#a1f94697f2a9f866e751fad5fa50ac54a)   0x01 |
| #define | [PINMUX\_FUNC\_C](#ad65d0f30a98080f3e21e2db0d6f63e90)   0x02 |
| #define | [PINMUX\_FUNC\_D](#abcab76c799f9fefa55d8814c820f212a)   0x03 |
| #define | [PINMUX\_FUNC\_MAX](#a74d6d35ca16164b0a0b68ee271b16e0d)   0x04 |
| #define | [ENE\_KB106X\_NO\_PUD\_POS](#abac4bfb212bc96557b44d5f912939202)   12 |
| #define | [ENE\_KB106X\_PD\_POS](#a3d996e8da6fd27b2e409f95d60c6d969)   13 |
| #define | [ENE\_KB106X\_PU\_POS](#ae8011d97ae2c4a1626a5c060c75be8da)   14 |
| #define | [ENE\_KB106X\_PUSH\_PULL\_POS](#a2ba1fa41dfd21090130f7ae0849ccb9a)   15 |
| #define | [ENE\_KB106X\_OPEN\_DRAIN\_POS](#a88576538346e2c249ef5307487619dce)   16 |
| #define | [ENE\_KB106X\_OUT\_DIS\_POS](#a969b0d246bc93d27662806924490134b)   17 |
| #define | [ENE\_KB106X\_OUT\_EN\_POS](#a57c26614d9fe66812dfdd6addc57e724)   18 |
| #define | [ENE\_KB106X\_OUT\_HI\_POS](#a5a6ed3b1af11083f5f424a47280369f5)   19 |
| #define | [ENE\_KB106X\_OUT\_LO\_POS](#a61b2e54a54dee416d674fb71fe450319)   20 |
| #define | [ENE\_KB106X\_PIN\_LOW\_POWER\_POS](#aad562cc00835aa70b1ebfc0d73cacb87)   21 |
| #define | [ENE\_KB106X\_IN\_DIS\_POS](#a040e843e147d311107bc2217440a3feb)   22 |
| #define | [ENE\_KB106X\_IN\_EN\_POS](#af66fd6f73d773180f6b4c2a5e55d2ee7)   23 |
| #define | [ENE\_KB106X\_DRIVING\_POS](#a7fda7bb531cdddc3c040352b33c6bc34)   31 |
| #define | [ENE\_KB106X\_PINMUX\_PORT\_POS](#a87c5ce1628625ff0bf8ab57e58c952a3)   5 |
| #define | [ENE\_KB106X\_PINMUX\_PORT\_MSK](#a14853b5c05a4c4d8a70ac2b257a0e2b2)   0x7 |
| #define | [ENE\_KB106X\_PINMUX\_PIN\_POS](#afe8dfa7a9f85d9bff0a3a066fbd5b4be)   0 |
| #define | [ENE\_KB106X\_PINMUX\_PIN\_MSK](#a48b9755d0765d1a78b259a7864e966f2)   0x1f |
| #define | [ENE\_KB106X\_PINMUX\_FUNC\_POS](#a02262fa6f75e8574b61f65cc94eaa233)   8 |
| #define | [ENE\_KB106X\_PINMUX\_FUNC\_MSK](#a744daeb1e891195cf3735ffb7440f746)   0xf |
| #define | [ENE\_KB106X\_EXTENDED\_BANK](#a346c95084c7edb51010f04201c298205)   0x80 |
| #define | [ENE\_KB106X\_PINMUX](#a2df12498c98fe54610bf619d68f76a55)(n, f) |

## Macro Definition Documentation

## [◆ ](#a7fda7bb531cdddc3c040352b33c6bc34)ENE\_KB106X\_DRIVING\_POS

| #define ENE\_KB106X\_DRIVING\_POS   31 |
| --- |

## [◆ ](#a346c95084c7edb51010f04201c298205)ENE\_KB106X\_EXTENDED\_BANK

| #define ENE\_KB106X\_EXTENDED\_BANK   0x80 |
| --- |

## [◆ ](#a040e843e147d311107bc2217440a3feb)ENE\_KB106X\_IN\_DIS\_POS

| #define ENE\_KB106X\_IN\_DIS\_POS   22 |
| --- |

## [◆ ](#af66fd6f73d773180f6b4c2a5e55d2ee7)ENE\_KB106X\_IN\_EN\_POS

| #define ENE\_KB106X\_IN\_EN\_POS   23 |
| --- |

## [◆ ](#abac4bfb212bc96557b44d5f912939202)ENE\_KB106X\_NO\_PUD\_POS

| #define ENE\_KB106X\_NO\_PUD\_POS   12 |
| --- |

## [◆ ](#a88576538346e2c249ef5307487619dce)ENE\_KB106X\_OPEN\_DRAIN\_POS

| #define ENE\_KB106X\_OPEN\_DRAIN\_POS   16 |
| --- |

## [◆ ](#a969b0d246bc93d27662806924490134b)ENE\_KB106X\_OUT\_DIS\_POS

| #define ENE\_KB106X\_OUT\_DIS\_POS   17 |
| --- |

## [◆ ](#a57c26614d9fe66812dfdd6addc57e724)ENE\_KB106X\_OUT\_EN\_POS

| #define ENE\_KB106X\_OUT\_EN\_POS   18 |
| --- |

## [◆ ](#a5a6ed3b1af11083f5f424a47280369f5)ENE\_KB106X\_OUT\_HI\_POS

| #define ENE\_KB106X\_OUT\_HI\_POS   19 |
| --- |

## [◆ ](#a61b2e54a54dee416d674fb71fe450319)ENE\_KB106X\_OUT\_LO\_POS

| #define ENE\_KB106X\_OUT\_LO\_POS   20 |
| --- |

## [◆ ](#a3d996e8da6fd27b2e409f95d60c6d969)ENE\_KB106X\_PD\_POS

| #define ENE\_KB106X\_PD\_POS   13 |
| --- |

## [◆ ](#aad562cc00835aa70b1ebfc0d73cacb87)ENE\_KB106X\_PIN\_LOW\_POWER\_POS

| #define ENE\_KB106X\_PIN\_LOW\_POWER\_POS   21 |
| --- |

## [◆ ](#a2df12498c98fe54610bf619d68f76a55)ENE\_KB106X\_PINMUX

| #define ENE\_KB106X\_PINMUX | ( |  | *n*, |
| --- | --- | --- | --- |
|  |  |  | *f* ) |

**Value:**

(((((n) >> 5) & [ENE\_KB106X\_PINMUX\_PORT\_MSK](#a14853b5c05a4c4d8a70ac2b257a0e2b2)) << [ENE\_KB106X\_PINMUX\_PORT\_POS](#a87c5ce1628625ff0bf8ab57e58c952a3)) | \

(((n) & [ENE\_KB106X\_PINMUX\_PIN\_MSK](#a48b9755d0765d1a78b259a7864e966f2)) << [ENE\_KB106X\_PINMUX\_PIN\_POS](#afe8dfa7a9f85d9bff0a3a066fbd5b4be)) | \

(((f) & [ENE\_KB106X\_PINMUX\_FUNC\_MSK](#a744daeb1e891195cf3735ffb7440f746)) << [ENE\_KB106X\_PINMUX\_FUNC\_POS](#a02262fa6f75e8574b61f65cc94eaa233)))

[ENE\_KB106X\_PINMUX\_FUNC\_POS](#a02262fa6f75e8574b61f65cc94eaa233)

#define ENE\_KB106X\_PINMUX\_FUNC\_POS

**Definition** ene-kb106x-pinctrl.h:37

[ENE\_KB106X\_PINMUX\_PORT\_MSK](#a14853b5c05a4c4d8a70ac2b257a0e2b2)

#define ENE\_KB106X\_PINMUX\_PORT\_MSK

**Definition** ene-kb106x-pinctrl.h:34

[ENE\_KB106X\_PINMUX\_PIN\_MSK](#a48b9755d0765d1a78b259a7864e966f2)

#define ENE\_KB106X\_PINMUX\_PIN\_MSK

**Definition** ene-kb106x-pinctrl.h:36

[ENE\_KB106X\_PINMUX\_FUNC\_MSK](#a744daeb1e891195cf3735ffb7440f746)

#define ENE\_KB106X\_PINMUX\_FUNC\_MSK

**Definition** ene-kb106x-pinctrl.h:38

[ENE\_KB106X\_PINMUX\_PORT\_POS](#a87c5ce1628625ff0bf8ab57e58c952a3)

#define ENE\_KB106X\_PINMUX\_PORT\_POS

**Definition** ene-kb106x-pinctrl.h:33

[ENE\_KB106X\_PINMUX\_PIN\_POS](#afe8dfa7a9f85d9bff0a3a066fbd5b4be)

#define ENE\_KB106X\_PINMUX\_PIN\_POS

**Definition** ene-kb106x-pinctrl.h:35

## [◆ ](#a744daeb1e891195cf3735ffb7440f746)ENE\_KB106X\_PINMUX\_FUNC\_MSK

| #define ENE\_KB106X\_PINMUX\_FUNC\_MSK   0xf |
| --- |

## [◆ ](#a02262fa6f75e8574b61f65cc94eaa233)ENE\_KB106X\_PINMUX\_FUNC\_POS

| #define ENE\_KB106X\_PINMUX\_FUNC\_POS   8 |
| --- |

## [◆ ](#a48b9755d0765d1a78b259a7864e966f2)ENE\_KB106X\_PINMUX\_PIN\_MSK

| #define ENE\_KB106X\_PINMUX\_PIN\_MSK   0x1f |
| --- |

## [◆ ](#afe8dfa7a9f85d9bff0a3a066fbd5b4be)ENE\_KB106X\_PINMUX\_PIN\_POS

| #define ENE\_KB106X\_PINMUX\_PIN\_POS   0 |
| --- |

## [◆ ](#a14853b5c05a4c4d8a70ac2b257a0e2b2)ENE\_KB106X\_PINMUX\_PORT\_MSK

| #define ENE\_KB106X\_PINMUX\_PORT\_MSK   0x7 |
| --- |

## [◆ ](#a87c5ce1628625ff0bf8ab57e58c952a3)ENE\_KB106X\_PINMUX\_PORT\_POS

| #define ENE\_KB106X\_PINMUX\_PORT\_POS   5 |
| --- |

## [◆ ](#ae8011d97ae2c4a1626a5c060c75be8da)ENE\_KB106X\_PU\_POS

| #define ENE\_KB106X\_PU\_POS   14 |
| --- |

## [◆ ](#a2ba1fa41dfd21090130f7ae0849ccb9a)ENE\_KB106X\_PUSH\_PULL\_POS

| #define ENE\_KB106X\_PUSH\_PULL\_POS   15 |
| --- |

## [◆ ](#a98cfa6f81cd2d924b4b8410cc58dcced)PINMUX\_FUNC\_A

| #define PINMUX\_FUNC\_A   0x00 |
| --- |

## [◆ ](#a1f94697f2a9f866e751fad5fa50ac54a)PINMUX\_FUNC\_B

| #define PINMUX\_FUNC\_B   0x01 |
| --- |

## [◆ ](#ad65d0f30a98080f3e21e2db0d6f63e90)PINMUX\_FUNC\_C

| #define PINMUX\_FUNC\_C   0x02 |
| --- |

## [◆ ](#abcab76c799f9fefa55d8814c820f212a)PINMUX\_FUNC\_D

| #define PINMUX\_FUNC\_D   0x03 |
| --- |

## [◆ ](#ab5585e56327f2b23ec89ba9debba0ee2)PINMUX\_FUNC\_GPIO

| #define PINMUX\_FUNC\_GPIO   0x00 |
| --- |

## [◆ ](#a74d6d35ca16164b0a0b68ee271b16e0d)PINMUX\_FUNC\_MAX

| #define PINMUX\_FUNC\_MAX   0x04 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [ene-kb106x-pinctrl.h](ene-kb106x-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
