---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/ene-kb1200-pinctrl_8h.html
original_path: doxygen/html/ene-kb1200-pinctrl_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ene-kb1200-pinctrl.h File Reference

`#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h_source.md)>`

[Go to the source code of this file.](ene-kb1200-pinctrl_8h_source.md)

| Macros | |
| --- | --- |
| #define | [PINMUX\_FUNC\_GPIO](#ab5585e56327f2b23ec89ba9debba0ee2)   0x00 |
| #define | [PINMUX\_FUNC\_A](#a98cfa6f81cd2d924b4b8410cc58dcced)   0x00 |
| #define | [PINMUX\_FUNC\_B](#a1f94697f2a9f866e751fad5fa50ac54a)   0x01 |
| #define | [PINMUX\_FUNC\_C](#ad65d0f30a98080f3e21e2db0d6f63e90)   0x02 |
| #define | [PINMUX\_FUNC\_D](#abcab76c799f9fefa55d8814c820f212a)   0x03 |
| #define | [PINMUX\_FUNC\_MAX](#a74d6d35ca16164b0a0b68ee271b16e0d)   0x04 |
| #define | [ENE\_KB1200\_NO\_PUD\_POS](#a4079f1e59701aa562027b6ad1656caad)   12 |
| #define | [ENE\_KB1200\_PD\_POS](#a49849bc4e85bd82ebc9bb4d14dd2668c)   13 |
| #define | [ENE\_KB1200\_PU\_POS](#af4297d42dd80877ce174a3d855df01b6)   14 |
| #define | [ENE\_KB1200\_PUSH\_PULL\_POS](#a2fd07082dd0f55f0fcb33847476d52b1)   15 |
| #define | [ENE\_KB1200\_OPEN\_DRAIN\_POS](#af0eeb505113d97cdbe2afa0436718829)   16 |
| #define | [ENE\_KB1200\_OUT\_DIS\_POS](#ae7915329e0bf4a3961fdcf3a3bd706ac)   17 |
| #define | [ENE\_KB1200\_OUT\_EN\_POS](#af87d58a86781f6db2b698aeb598d8f80)   18 |
| #define | [ENE\_KB1200\_OUT\_HI\_POS](#ae7289ea9757e87dba5eca26b0d8ea869)   19 |
| #define | [ENE\_KB1200\_OUT\_LO\_POS](#a31048a09bc76aa17796ac29093c94c17)   20 |
| #define | [ENE\_KB1200\_PIN\_LOW\_POWER\_POS](#ab68aefd0fa096ce5541f07d4b65881c0)   21 |
| #define | [ENE\_KB1200\_PINMUX\_PORT\_POS](#ade268ffe7669879fbef2c7bf4600ffc2)   5 |
| #define | [ENE\_KB1200\_PINMUX\_PORT\_MSK](#ad673befbb525dba683cc65b64fdd3abd)   0x7 |
| #define | [ENE\_KB1200\_PINMUX\_PIN\_POS](#abee9ef573bd89f90dc1bc2d65cfb2507)   0 |
| #define | [ENE\_KB1200\_PINMUX\_PIN\_MSK](#ac1666ff38512cea6f97afc30b22dda0f)   0x1f |
| #define | [ENE\_KB1200\_PINMUX\_FUNC\_POS](#aff29cfeb36d2bb8a9ac5792b30f6c627)   8 |
| #define | [ENE\_KB1200\_PINMUX\_FUNC\_MSK](#aa077424a43590e43f9067f3ab0a655ff)   0xf |
| #define | [ENE\_KB1200\_PINMUX](#a2c86608b7173b6e66f3e55015035a41b)(n, f) |

## Macro Definition Documentation

## [◆ ](#a4079f1e59701aa562027b6ad1656caad)ENE\_KB1200\_NO\_PUD\_POS

| #define ENE\_KB1200\_NO\_PUD\_POS   12 |
| --- |

## [◆ ](#af0eeb505113d97cdbe2afa0436718829)ENE\_KB1200\_OPEN\_DRAIN\_POS

| #define ENE\_KB1200\_OPEN\_DRAIN\_POS   16 |
| --- |

## [◆ ](#ae7915329e0bf4a3961fdcf3a3bd706ac)ENE\_KB1200\_OUT\_DIS\_POS

| #define ENE\_KB1200\_OUT\_DIS\_POS   17 |
| --- |

## [◆ ](#af87d58a86781f6db2b698aeb598d8f80)ENE\_KB1200\_OUT\_EN\_POS

| #define ENE\_KB1200\_OUT\_EN\_POS   18 |
| --- |

## [◆ ](#ae7289ea9757e87dba5eca26b0d8ea869)ENE\_KB1200\_OUT\_HI\_POS

| #define ENE\_KB1200\_OUT\_HI\_POS   19 |
| --- |

## [◆ ](#a31048a09bc76aa17796ac29093c94c17)ENE\_KB1200\_OUT\_LO\_POS

| #define ENE\_KB1200\_OUT\_LO\_POS   20 |
| --- |

## [◆ ](#a49849bc4e85bd82ebc9bb4d14dd2668c)ENE\_KB1200\_PD\_POS

| #define ENE\_KB1200\_PD\_POS   13 |
| --- |

## [◆ ](#ab68aefd0fa096ce5541f07d4b65881c0)ENE\_KB1200\_PIN\_LOW\_POWER\_POS

| #define ENE\_KB1200\_PIN\_LOW\_POWER\_POS   21 |
| --- |

## [◆ ](#a2c86608b7173b6e66f3e55015035a41b)ENE\_KB1200\_PINMUX

| #define ENE\_KB1200\_PINMUX | ( |  | *n*, |
| --- | --- | --- | --- |
|  |  |  | *f* ) |

**Value:**

(((((n) >> 5) & [ENE\_KB1200\_PINMUX\_PORT\_MSK](#ad673befbb525dba683cc65b64fdd3abd)) << [ENE\_KB1200\_PINMUX\_PORT\_POS](#ade268ffe7669879fbef2c7bf4600ffc2)) | \

(((n) & [ENE\_KB1200\_PINMUX\_PIN\_MSK](#ac1666ff38512cea6f97afc30b22dda0f)) << [ENE\_KB1200\_PINMUX\_PIN\_POS](#abee9ef573bd89f90dc1bc2d65cfb2507)) | \

(((f) & [ENE\_KB1200\_PINMUX\_FUNC\_MSK](#aa077424a43590e43f9067f3ab0a655ff)) << [ENE\_KB1200\_PINMUX\_FUNC\_POS](#aff29cfeb36d2bb8a9ac5792b30f6c627)))

[ENE\_KB1200\_PINMUX\_FUNC\_MSK](#aa077424a43590e43f9067f3ab0a655ff)

#define ENE\_KB1200\_PINMUX\_FUNC\_MSK

**Definition** ene-kb1200-pinctrl.h:35

[ENE\_KB1200\_PINMUX\_PIN\_POS](#abee9ef573bd89f90dc1bc2d65cfb2507)

#define ENE\_KB1200\_PINMUX\_PIN\_POS

**Definition** ene-kb1200-pinctrl.h:32

[ENE\_KB1200\_PINMUX\_PIN\_MSK](#ac1666ff38512cea6f97afc30b22dda0f)

#define ENE\_KB1200\_PINMUX\_PIN\_MSK

**Definition** ene-kb1200-pinctrl.h:33

[ENE\_KB1200\_PINMUX\_PORT\_MSK](#ad673befbb525dba683cc65b64fdd3abd)

#define ENE\_KB1200\_PINMUX\_PORT\_MSK

**Definition** ene-kb1200-pinctrl.h:31

[ENE\_KB1200\_PINMUX\_PORT\_POS](#ade268ffe7669879fbef2c7bf4600ffc2)

#define ENE\_KB1200\_PINMUX\_PORT\_POS

**Definition** ene-kb1200-pinctrl.h:30

[ENE\_KB1200\_PINMUX\_FUNC\_POS](#aff29cfeb36d2bb8a9ac5792b30f6c627)

#define ENE\_KB1200\_PINMUX\_FUNC\_POS

**Definition** ene-kb1200-pinctrl.h:34

## [◆ ](#aa077424a43590e43f9067f3ab0a655ff)ENE\_KB1200\_PINMUX\_FUNC\_MSK

| #define ENE\_KB1200\_PINMUX\_FUNC\_MSK   0xf |
| --- |

## [◆ ](#aff29cfeb36d2bb8a9ac5792b30f6c627)ENE\_KB1200\_PINMUX\_FUNC\_POS

| #define ENE\_KB1200\_PINMUX\_FUNC\_POS   8 |
| --- |

## [◆ ](#ac1666ff38512cea6f97afc30b22dda0f)ENE\_KB1200\_PINMUX\_PIN\_MSK

| #define ENE\_KB1200\_PINMUX\_PIN\_MSK   0x1f |
| --- |

## [◆ ](#abee9ef573bd89f90dc1bc2d65cfb2507)ENE\_KB1200\_PINMUX\_PIN\_POS

| #define ENE\_KB1200\_PINMUX\_PIN\_POS   0 |
| --- |

## [◆ ](#ad673befbb525dba683cc65b64fdd3abd)ENE\_KB1200\_PINMUX\_PORT\_MSK

| #define ENE\_KB1200\_PINMUX\_PORT\_MSK   0x7 |
| --- |

## [◆ ](#ade268ffe7669879fbef2c7bf4600ffc2)ENE\_KB1200\_PINMUX\_PORT\_POS

| #define ENE\_KB1200\_PINMUX\_PORT\_POS   5 |
| --- |

## [◆ ](#af4297d42dd80877ce174a3d855df01b6)ENE\_KB1200\_PU\_POS

| #define ENE\_KB1200\_PU\_POS   14 |
| --- |

## [◆ ](#a2fd07082dd0f55f0fcb33847476d52b1)ENE\_KB1200\_PUSH\_PULL\_POS

| #define ENE\_KB1200\_PUSH\_PULL\_POS   15 |
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
- [ene-kb1200-pinctrl.h](ene-kb1200-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
