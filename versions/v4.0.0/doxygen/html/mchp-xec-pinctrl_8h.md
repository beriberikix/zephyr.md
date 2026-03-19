---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/mchp-xec-pinctrl_8h.html
original_path: doxygen/html/mchp-xec-pinctrl_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mchp-xec-pinctrl.h File Reference

`#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h_source.md)>`

[Go to the source code of this file.](mchp-xec-pinctrl_8h_source.md)

| Macros | |
| --- | --- |
| #define | [MCHP\_GPIO](#adbdaffd4bf6308e5e57f501313339871)   0x0 |
| #define | [MCHP\_AF0](#ae0c0be33001f69f4225644ab74f59078)   0x0 |
| #define | [MCHP\_AF1](#ad1d584cc5e02df71255e0608a04d019f)   0x1 |
| #define | [MCHP\_AF2](#ad1888b8f9e981d4a54534fca01aab1c4)   0x2 |
| #define | [MCHP\_AF3](#a9e4512829a2dba4904ab16718c2f54fd)   0x3 |
| #define | [MCHP\_AF4](#a68e1df87c0a06668cc3897fd8805bc16)   0x4 |
| #define | [MCHP\_AF5](#adb552a66660db8468dabfae0edcaba71)   0x5 |
| #define | [MCHP\_AF6](#a1b8833d1dee0e4c9ab63ffc50c8472a5)   0x6 |
| #define | [MCHP\_AF7](#a3ebbede5ab9560d1ed0889c488e5d658)   0x7 |
| #define | [MCHP\_AFMAX](#a57390da1563b872353fdec5d2ce039d0)   0x8 |
| #define | [MCHP\_XEC\_NO\_PUD\_POS](#a0a93d1975f3a17c0b9ef3a1d79f0b317)   12 |
| #define | [MCHP\_XEC\_PD\_POS](#a6ed13159931220304752a351806670f7)   13 |
| #define | [MCHP\_XEC\_PU\_POS](#adade4a3941f7c3d9aee288f8f5dd4296)   14 |
| #define | [MCHP\_XEC\_PUSH\_PULL\_POS](#a17adecf816e4f0fd7bb59be66e0701e8)   15 |
| #define | [MCHP\_XEC\_OPEN\_DRAIN\_POS](#a539983dc25059710c8286ed12e30449e)   16 |
| #define | [MCHP\_XEC\_OUT\_DIS\_POS](#ae7d712bf52abcb49e7f57ccef503c025)   17 |
| #define | [MCHP\_XEC\_OUT\_EN\_POS](#ababa1d9223423a8fad3264494f9c9e4a)   18 |
| #define | [MCHP\_XEC\_OUT\_HI\_POS](#ac396fb8f6698d9915f620eb59548a5aa)   19 |
| #define | [MCHP\_XEC\_OUT\_LO\_POS](#a6b4f5d75d5f9d3620fd60ec08926fbf6)   20 |
| #define | [MCHP\_XEC\_SLEW\_RATE\_POS](#aa10630a4dcb92b97e911ec9d38e15a82)   22 |
| #define | [MCHP\_XEC\_SLEW\_RATE\_MSK0](#ac916331403b2dfc814a67e541708558d)   0x3 |
| #define | [MCHP\_XEC\_SLEW\_RATE\_SLOW0](#a0d7c618b2bd4a89b24fb0ed3d92609c0)   0x1 |
| #define | [MCHP\_XEC\_SLEW\_RATE\_FAST0](#ad359dd0f6c31e1234f0a6cd8c269043e)   0x2 |
| #define | [MCHP\_XEC\_DRV\_STR\_POS](#a7e4732960045246965fcf13ef93542bc)   24 |
| #define | [MCHP\_XEC\_DRV\_STR\_MSK0](#ac740c2c3b0a7256f3ab485ba671bccce)   0x7 |
| #define | [MCHP\_XEC\_DRV\_STR0\_1X](#a77200792cd3b645a76e6e720bf386e2c)   0x1 /\* 2 or 4(PIO-24) mA \*/ |
| #define | [MCHP\_XEC\_DRV\_STR0\_2X](#a8e804be498ef9a9aa66df2ccf7e2e591)   0x2 /\* 4 or 8(PIO-24) mA \*/ |
| #define | [MCHP\_XEC\_DRV\_STR0\_4X](#a435fe00b4172ea7c0e43a6720933a09a)   0x3 /\* 8 or 16(PIO-24) mA \*/ |
| #define | [MCHP\_XEC\_DRV\_STR0\_6X](#a25e8e2002a525cb37ab412d46f71c61b)   0x4 /\* 12 or 24(PIO-24) mA \*/ |
| #define | [MCHP\_XEC\_PIN\_LOW\_POWER\_POS](#aec3b775918e3cf9e49275509d6cf18a7)   27 |
| #define | [MCHP\_XEC\_FUNC\_INV\_POS](#a78cd838c620e6f0af49a1765ad2843a9)   29 |
| #define | [MCHP\_XEC\_PINMUX\_PORT\_POS](#a7e0762ea1ba02d68a6c13c5d0805c60a)   0 |
| #define | [MCHP\_XEC\_PINMUX\_PORT\_MSK](#a27cbf07ff9a28f24d115d788de5567f2)   0xf |
| #define | [MCHP\_XEC\_PINMUX\_PIN\_POS](#a3504bf6d5897c23173f05009a4862c31)   4 |
| #define | [MCHP\_XEC\_PINMUX\_PIN\_MSK](#a8537436b6e3c94e965c0a27992b04d35)   0x1f |
| #define | [MCHP\_XEC\_PINMUX\_FUNC\_POS](#a4a8aea0c15ea3d89d4bac2629fa43c18)   9 |
| #define | [MCHP\_XEC\_PINMUX\_FUNC\_MSK](#ab39f30494ce30f88f18cbfdd835cbb6f)   0x7 |
| #define | [MCHP\_XEC\_PINMUX](#a9ce81e5379ef60140ed6251e30825fe9)(n, f) |
| #define | [MCHP\_XEC\_PINMUX\_PORT](#a04e9b92f5d748649eb516e628141d6f8)(p) |
| #define | [MCHP\_XEC\_PINMUX\_PIN](#a06fabe0e1bb56de3c56fc278d3f2da6f)(p) |
| #define | [MCHP\_XEC\_PINMUX\_FUNC](#a90649c60bd81e6cc2dca37ea32d8ad25)(p) |
| #define | [MEC\_XEC\_PINMUX\_PORT\_PIN](#a8f8edb939c9f5f9702253a24dc9bde3d)(p) |

## Macro Definition Documentation

## [◆ ](#ae0c0be33001f69f4225644ab74f59078)MCHP\_AF0

| #define MCHP\_AF0   0x0 |
| --- |

## [◆ ](#ad1d584cc5e02df71255e0608a04d019f)MCHP\_AF1

| #define MCHP\_AF1   0x1 |
| --- |

## [◆ ](#ad1888b8f9e981d4a54534fca01aab1c4)MCHP\_AF2

| #define MCHP\_AF2   0x2 |
| --- |

## [◆ ](#a9e4512829a2dba4904ab16718c2f54fd)MCHP\_AF3

| #define MCHP\_AF3   0x3 |
| --- |

## [◆ ](#a68e1df87c0a06668cc3897fd8805bc16)MCHP\_AF4

| #define MCHP\_AF4   0x4 |
| --- |

## [◆ ](#adb552a66660db8468dabfae0edcaba71)MCHP\_AF5

| #define MCHP\_AF5   0x5 |
| --- |

## [◆ ](#a1b8833d1dee0e4c9ab63ffc50c8472a5)MCHP\_AF6

| #define MCHP\_AF6   0x6 |
| --- |

## [◆ ](#a3ebbede5ab9560d1ed0889c488e5d658)MCHP\_AF7

| #define MCHP\_AF7   0x7 |
| --- |

## [◆ ](#a57390da1563b872353fdec5d2ce039d0)MCHP\_AFMAX

| #define MCHP\_AFMAX   0x8 |
| --- |

## [◆ ](#adbdaffd4bf6308e5e57f501313339871)MCHP\_GPIO

| #define MCHP\_GPIO   0x0 |
| --- |

## [◆ ](#a77200792cd3b645a76e6e720bf386e2c)MCHP\_XEC\_DRV\_STR0\_1X

| #define MCHP\_XEC\_DRV\_STR0\_1X   0x1 /\* 2 or 4(PIO-24) mA \*/ |
| --- |

## [◆ ](#a8e804be498ef9a9aa66df2ccf7e2e591)MCHP\_XEC\_DRV\_STR0\_2X

| #define MCHP\_XEC\_DRV\_STR0\_2X   0x2 /\* 4 or 8(PIO-24) mA \*/ |
| --- |

## [◆ ](#a435fe00b4172ea7c0e43a6720933a09a)MCHP\_XEC\_DRV\_STR0\_4X

| #define MCHP\_XEC\_DRV\_STR0\_4X   0x3 /\* 8 or 16(PIO-24) mA \*/ |
| --- |

## [◆ ](#a25e8e2002a525cb37ab412d46f71c61b)MCHP\_XEC\_DRV\_STR0\_6X

| #define MCHP\_XEC\_DRV\_STR0\_6X   0x4 /\* 12 or 24(PIO-24) mA \*/ |
| --- |

## [◆ ](#ac740c2c3b0a7256f3ab485ba671bccce)MCHP\_XEC\_DRV\_STR\_MSK0

| #define MCHP\_XEC\_DRV\_STR\_MSK0   0x7 |
| --- |

## [◆ ](#a7e4732960045246965fcf13ef93542bc)MCHP\_XEC\_DRV\_STR\_POS

| #define MCHP\_XEC\_DRV\_STR\_POS   24 |
| --- |

## [◆ ](#a78cd838c620e6f0af49a1765ad2843a9)MCHP\_XEC\_FUNC\_INV\_POS

| #define MCHP\_XEC\_FUNC\_INV\_POS   29 |
| --- |

## [◆ ](#a0a93d1975f3a17c0b9ef3a1d79f0b317)MCHP\_XEC\_NO\_PUD\_POS

| #define MCHP\_XEC\_NO\_PUD\_POS   12 |
| --- |

## [◆ ](#a539983dc25059710c8286ed12e30449e)MCHP\_XEC\_OPEN\_DRAIN\_POS

| #define MCHP\_XEC\_OPEN\_DRAIN\_POS   16 |
| --- |

## [◆ ](#ae7d712bf52abcb49e7f57ccef503c025)MCHP\_XEC\_OUT\_DIS\_POS

| #define MCHP\_XEC\_OUT\_DIS\_POS   17 |
| --- |

## [◆ ](#ababa1d9223423a8fad3264494f9c9e4a)MCHP\_XEC\_OUT\_EN\_POS

| #define MCHP\_XEC\_OUT\_EN\_POS   18 |
| --- |

## [◆ ](#ac396fb8f6698d9915f620eb59548a5aa)MCHP\_XEC\_OUT\_HI\_POS

| #define MCHP\_XEC\_OUT\_HI\_POS   19 |
| --- |

## [◆ ](#a6b4f5d75d5f9d3620fd60ec08926fbf6)MCHP\_XEC\_OUT\_LO\_POS

| #define MCHP\_XEC\_OUT\_LO\_POS   20 |
| --- |

## [◆ ](#a6ed13159931220304752a351806670f7)MCHP\_XEC\_PD\_POS

| #define MCHP\_XEC\_PD\_POS   13 |
| --- |

## [◆ ](#aec3b775918e3cf9e49275509d6cf18a7)MCHP\_XEC\_PIN\_LOW\_POWER\_POS

| #define MCHP\_XEC\_PIN\_LOW\_POWER\_POS   27 |
| --- |

## [◆ ](#a9ce81e5379ef60140ed6251e30825fe9)MCHP\_XEC\_PINMUX

| #define MCHP\_XEC\_PINMUX | ( |  | *n*, |
| --- | --- | --- | --- |
|  |  |  | *f* ) |

**Value:**

(((((n) >> 5) & [MCHP\_XEC\_PINMUX\_PORT\_MSK](#a27cbf07ff9a28f24d115d788de5567f2)) << [MCHP\_XEC\_PINMUX\_PORT\_POS](#a7e0762ea1ba02d68a6c13c5d0805c60a)) | \

(((n) & [MCHP\_XEC\_PINMUX\_PIN\_MSK](#a8537436b6e3c94e965c0a27992b04d35)) << [MCHP\_XEC\_PINMUX\_PIN\_POS](#a3504bf6d5897c23173f05009a4862c31)) | \

(((f) & [MCHP\_XEC\_PINMUX\_FUNC\_MSK](#ab39f30494ce30f88f18cbfdd835cbb6f)) << [MCHP\_XEC\_PINMUX\_FUNC\_POS](#a4a8aea0c15ea3d89d4bac2629fa43c18)))

[MCHP\_XEC\_PINMUX\_PORT\_MSK](#a27cbf07ff9a28f24d115d788de5567f2)

#define MCHP\_XEC\_PINMUX\_PORT\_MSK

**Definition** mchp-xec-pinctrl.h:47

[MCHP\_XEC\_PINMUX\_PIN\_POS](#a3504bf6d5897c23173f05009a4862c31)

#define MCHP\_XEC\_PINMUX\_PIN\_POS

**Definition** mchp-xec-pinctrl.h:48

[MCHP\_XEC\_PINMUX\_FUNC\_POS](#a4a8aea0c15ea3d89d4bac2629fa43c18)

#define MCHP\_XEC\_PINMUX\_FUNC\_POS

**Definition** mchp-xec-pinctrl.h:50

[MCHP\_XEC\_PINMUX\_PORT\_POS](#a7e0762ea1ba02d68a6c13c5d0805c60a)

#define MCHP\_XEC\_PINMUX\_PORT\_POS

**Definition** mchp-xec-pinctrl.h:46

[MCHP\_XEC\_PINMUX\_PIN\_MSK](#a8537436b6e3c94e965c0a27992b04d35)

#define MCHP\_XEC\_PINMUX\_PIN\_MSK

**Definition** mchp-xec-pinctrl.h:49

[MCHP\_XEC\_PINMUX\_FUNC\_MSK](#ab39f30494ce30f88f18cbfdd835cbb6f)

#define MCHP\_XEC\_PINMUX\_FUNC\_MSK

**Definition** mchp-xec-pinctrl.h:51

## [◆ ](#a90649c60bd81e6cc2dca37ea32d8ad25)MCHP\_XEC\_PINMUX\_FUNC

| #define MCHP\_XEC\_PINMUX\_FUNC | ( |  | *p* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((p) >> [MCHP\_XEC\_PINMUX\_FUNC\_POS](#a4a8aea0c15ea3d89d4bac2629fa43c18)) & [MCHP\_XEC\_PINMUX\_FUNC\_MSK](#ab39f30494ce30f88f18cbfdd835cbb6f))

## [◆ ](#ab39f30494ce30f88f18cbfdd835cbb6f)MCHP\_XEC\_PINMUX\_FUNC\_MSK

| #define MCHP\_XEC\_PINMUX\_FUNC\_MSK   0x7 |
| --- |

## [◆ ](#a4a8aea0c15ea3d89d4bac2629fa43c18)MCHP\_XEC\_PINMUX\_FUNC\_POS

| #define MCHP\_XEC\_PINMUX\_FUNC\_POS   9 |
| --- |

## [◆ ](#a06fabe0e1bb56de3c56fc278d3f2da6f)MCHP\_XEC\_PINMUX\_PIN

| #define MCHP\_XEC\_PINMUX\_PIN | ( |  | *p* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((p) >> [MCHP\_XEC\_PINMUX\_PIN\_POS](#a3504bf6d5897c23173f05009a4862c31)) & [MCHP\_XEC\_PINMUX\_PIN\_MSK](#a8537436b6e3c94e965c0a27992b04d35))

## [◆ ](#a8537436b6e3c94e965c0a27992b04d35)MCHP\_XEC\_PINMUX\_PIN\_MSK

| #define MCHP\_XEC\_PINMUX\_PIN\_MSK   0x1f |
| --- |

## [◆ ](#a3504bf6d5897c23173f05009a4862c31)MCHP\_XEC\_PINMUX\_PIN\_POS

| #define MCHP\_XEC\_PINMUX\_PIN\_POS   4 |
| --- |

## [◆ ](#a04e9b92f5d748649eb516e628141d6f8)MCHP\_XEC\_PINMUX\_PORT

| #define MCHP\_XEC\_PINMUX\_PORT | ( |  | *p* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((p) >> [MCHP\_XEC\_PINMUX\_PORT\_POS](#a7e0762ea1ba02d68a6c13c5d0805c60a)) & [MCHP\_XEC\_PINMUX\_PORT\_MSK](#a27cbf07ff9a28f24d115d788de5567f2))

## [◆ ](#a27cbf07ff9a28f24d115d788de5567f2)MCHP\_XEC\_PINMUX\_PORT\_MSK

| #define MCHP\_XEC\_PINMUX\_PORT\_MSK   0xf |
| --- |

## [◆ ](#a7e0762ea1ba02d68a6c13c5d0805c60a)MCHP\_XEC\_PINMUX\_PORT\_POS

| #define MCHP\_XEC\_PINMUX\_PORT\_POS   0 |
| --- |

## [◆ ](#adade4a3941f7c3d9aee288f8f5dd4296)MCHP\_XEC\_PU\_POS

| #define MCHP\_XEC\_PU\_POS   14 |
| --- |

## [◆ ](#a17adecf816e4f0fd7bb59be66e0701e8)MCHP\_XEC\_PUSH\_PULL\_POS

| #define MCHP\_XEC\_PUSH\_PULL\_POS   15 |
| --- |

## [◆ ](#ad359dd0f6c31e1234f0a6cd8c269043e)MCHP\_XEC\_SLEW\_RATE\_FAST0

| #define MCHP\_XEC\_SLEW\_RATE\_FAST0   0x2 |
| --- |

## [◆ ](#ac916331403b2dfc814a67e541708558d)MCHP\_XEC\_SLEW\_RATE\_MSK0

| #define MCHP\_XEC\_SLEW\_RATE\_MSK0   0x3 |
| --- |

## [◆ ](#aa10630a4dcb92b97e911ec9d38e15a82)MCHP\_XEC\_SLEW\_RATE\_POS

| #define MCHP\_XEC\_SLEW\_RATE\_POS   22 |
| --- |

## [◆ ](#a0d7c618b2bd4a89b24fb0ed3d92609c0)MCHP\_XEC\_SLEW\_RATE\_SLOW0

| #define MCHP\_XEC\_SLEW\_RATE\_SLOW0   0x1 |
| --- |

## [◆ ](#a8f8edb939c9f5f9702253a24dc9bde3d)MEC\_XEC\_PINMUX\_PORT\_PIN

| #define MEC\_XEC\_PINMUX\_PORT\_PIN | ( |  | *p* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((p) & (([MCHP\_XEC\_PINMUX\_PORT\_MSK](#a27cbf07ff9a28f24d115d788de5567f2) << [MCHP\_XEC\_PINMUX\_PORT\_POS](#a7e0762ea1ba02d68a6c13c5d0805c60a)) | \

([MCHP\_XEC\_PINMUX\_PIN\_MSK](#a8537436b6e3c94e965c0a27992b04d35) << [MCHP\_XEC\_PINMUX\_PIN\_POS](#a3504bf6d5897c23173f05009a4862c31))))

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [mchp-xec-pinctrl.h](mchp-xec-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
