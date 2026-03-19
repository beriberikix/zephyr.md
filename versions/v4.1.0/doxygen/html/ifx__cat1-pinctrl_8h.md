---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ifx__cat1-pinctrl_8h.html
original_path: doxygen/html/ifx__cat1-pinctrl_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ifx\_cat1-pinctrl.h File Reference

[Go to the source code of this file.](ifx__cat1-pinctrl_8h_source.md)

| Macros | |
| --- | --- |
| #define | [SOC\_PINMUX\_PORT\_POS](#a6ba3e93a5498c6c5bd5e8f3d0c00ac2a)   (0) |
|  | Pin control binding helper. |
| #define | [SOC\_PINMUX\_PORT\_MASK](#a4199ffda078d925e8dfb58194117de1a)   (0xFFul << [SOC\_PINMUX\_PORT\_POS](#a6ba3e93a5498c6c5bd5e8f3d0c00ac2a)) |
| #define | [SOC\_PINMUX\_PIN\_POS](#a5266efcdc6dbcd64d8fc61c814b37dc7)   (8) |
| #define | [SOC\_PINMUX\_PIN\_MASK](#a881a5ee83663d0eac3a2cfd530e23266)   (0xFFul << [SOC\_PINMUX\_PIN\_POS](#a5266efcdc6dbcd64d8fc61c814b37dc7)) |
| #define | [SOC\_PINMUX\_HSIOM\_FUNC\_POS](#a2af56d2b85a6e4ba3a2f1fdd191f8c98)   (16) |
| #define | [SOC\_PINMUX\_HSIOM\_MASK](#a6baa74b565ac921b7e3b8b5fc65327a6)   (0xFFul << [SOC\_PINMUX\_HSIOM\_FUNC\_POS](#a2af56d2b85a6e4ba3a2f1fdd191f8c98)) |
| #define | [SOC\_PINMUX\_SIGNAL\_POS](#a38673a696cc1caa97e13eb6ef937007a)   (24) |
| #define | [SOC\_PINMUX\_SIGNAL\_MASK](#aca26c39aa27a6520ea0f57b7ab058672)   (0xFFul << [SOC\_PINMUX\_SIGNAL\_POS](#a38673a696cc1caa97e13eb6ef937007a)) |
| #define | [HSIOM\_SEL\_GPIO](#ac0d2af1bfb229de155412af7f00e4fe0)   (0) |
|  | Functions are defined using HSIOM SEL. |
| #define | [HSIOM\_SEL\_GPIO\_DSI](#a441de7f56a1c7c75cdae4d9f93ccfade)   (1) |
| #define | [HSIOM\_SEL\_DSI\_DSI](#a959873e5156c6e3c24dd2773bb1ba516)   (2) |
| #define | [HSIOM\_SEL\_DSI\_GPIO](#a022f7af586ee9b46f689d187e8dd73d8)   (3) |
| #define | [HSIOM\_SEL\_AMUXA](#a8806729fcb666c9de823be5dd55c873d)   (4) |
| #define | [HSIOM\_SEL\_AMUXB](#a862eb93443c5c9575ff990b776b6203b)   (5) |
| #define | [HSIOM\_SEL\_AMUXA\_DSI](#a4ba8695f92c0f347dd25ef981d67d1b0)   (6) |
| #define | [HSIOM\_SEL\_AMUXB\_DSI](#af7a28a087a8867a14423e9ab471cce54)   (7) |
| #define | [HSIOM\_SEL\_ACT\_0](#a3080ad4afafa572482ea1a5b49f6a1ce)   (8) |
| #define | [HSIOM\_SEL\_ACT\_1](#a990e35fecfcc37ca08fe709eee746618)   (9) |
| #define | [HSIOM\_SEL\_ACT\_2](#a696aeb76109bf339ebf0fcd20979f211)   (10) |
| #define | [HSIOM\_SEL\_ACT\_3](#a25e956bc540c9570392a1722b7e94670)   (11) |
| #define | [HSIOM\_SEL\_DS\_0](#afb33417be16e7fa6423fadd2ef4a0f5b)   (12) |
| #define | [HSIOM\_SEL\_DS\_1](#aa06be65ae17fc2dc1861c2af2e364652)   (13) |
| #define | [HSIOM\_SEL\_DS\_2](#a07f591dc1f8a9f9eda13063d8c58c4eb)   (14) |
| #define | [HSIOM\_SEL\_DS\_3](#a157da2f7e72fa8f19dfd682ec4444319)   (15) |
| #define | [HSIOM\_SEL\_ACT\_4](#a3336f2e2d4886e0e46819ee4f4d96734)   (16) |
| #define | [HSIOM\_SEL\_ACT\_5](#a1040ff80864b6a1d85eb4c07f4278ea1)   (17) |
| #define | [HSIOM\_SEL\_ACT\_6](#a575188296b25564faa9b3a3b4817b5e4)   (18) |
| #define | [HSIOM\_SEL\_ACT\_7](#ae9c0f6360d56214106b09861eedb911a)   (19) |
| #define | [HSIOM\_SEL\_ACT\_8](#a8d36acbee0c4de7088ddc08a8b1c07a6)   (20) |
| #define | [HSIOM\_SEL\_ACT\_9](#aff276e6f5cdc671648a428c22fc2776e)   (21) |
| #define | [HSIOM\_SEL\_ACT\_10](#a42c5af47fba8b69dacb3064e332193fd)   (22) |
| #define | [HSIOM\_SEL\_ACT\_11](#a48052c8dd78b1403de4d675571b7e6e2)   (23) |
| #define | [HSIOM\_SEL\_ACT\_12](#a6fc1302224b4d7585c25c3dc2ea340e7)   (24) |
| #define | [HSIOM\_SEL\_ACT\_13](#ae4fb8f65206098cace15b3e0f1c12a3e)   (25) |
| #define | [HSIOM\_SEL\_ACT\_14](#a7c3ffb4e79372b4cc4d1a7b4554911d5)   (26) |
| #define | [HSIOM\_SEL\_ACT\_15](#ab3285eea99f44cbe985eb097d1166a3d)   (27) |
| #define | [HSIOM\_SEL\_DS\_4](#a0f134c65358e450ca55341bbfec1cd0e)   (28) |
| #define | [HSIOM\_SEL\_DS\_5](#a4208fc8f94abf237d943bc5e8ffe3080)   (29) |
| #define | [HSIOM\_SEL\_DS\_6](#ac0153eaa52ef010bf58304a44ecb1e9b)   (30) |
| #define | [HSIOM\_SEL\_DS\_7](#a8c067c1737f0f1573e056a384954fd81)   (31) |
| #define | [DT\_CAT1\_DRIVE\_MODE\_INFO](#ac58363c207e4f8ea82394859044b2690)(peripheral\_signal) |
|  | Macro to set drive mode. |
| #define | [DT\_CAT1\_PINMUX](#a33b355e05d5b955a6b8d48f3613c2d9a)(port, pin, hsiom) |
|  | Macro to set pin control information (from pinctrl node). |
| #define | [P0](#a1583b00a62bc1138f99bbfcd8ef81a6a)   CYHAL\_PORT\_0 |
| #define | [P1](#a6c2a9f7efd46f0160f3037869924d6ce)   CYHAL\_PORT\_1 |
| #define | [P2](#ae00a52dba55d31948c377fa85d385b87)   CYHAL\_PORT\_2 |
| #define | [P3](#a0707a89c2f63bd260108e9dbb669358e)   CYHAL\_PORT\_3 |
| #define | [P4](#acbc14a33d017f5f2dabce1cb0d85718e)   CYHAL\_PORT\_4 |
| #define | [P5](#a49ce5f7954a95865f12be8083ccb2719)   CYHAL\_PORT\_5 |
| #define | [P6](#ab276be36e56dfdd17d860fbc82c3a22d)   CYHAL\_PORT\_6 |
| #define | [P7](#a017ae5a42bc27ff7402656a779fec303)   CYHAL\_PORT\_7 |
| #define | [P8](#ae04365e5a91d08e332a28f00efe389fe)   CYHAL\_PORT\_8 |
| #define | [P9](#a8b201e09e2f1d58d8f3ad3a14c02b86b)   CYHAL\_PORT\_9 |
| #define | [P10](#a5bb9f89248afa8d7e5a821fd459b085f)   CYHAL\_PORT\_10 |
| #define | [P11](#aca6db006bc37d2b337fca225a79856c8)   CYHAL\_PORT\_11 |
| #define | [P12](#a20c70bba8105b63590b5a49d99f563b5)   CYHAL\_PORT\_12 |
| #define | [P13](#aa729f895b03c9230ebcf8c798f7bd1bb)   CYHAL\_PORT\_13 |
| #define | [P14](#af108487a116bc015d7abd21ee2ab374e)   CYHAL\_PORT\_14 |
| #define | [P15](#a3059522b4d1048ecf60259f3805147d6)   CYHAL\_PORT\_15 |
| #define | [P16](#a0f8aefca2c1a1d922ca9ecac68caa584)   CYHAL\_PORT\_16 |
| #define | [P17](#ac8f5bddb889a3da7918ae32ca6c5cc97)   CYHAL\_PORT\_17 |
| #define | [P18](#ae6f383959ce67f3403d4cf1e7aacb1cb)   CYHAL\_PORT\_18 |
| #define | [P19](#af04bd18711f898d17e1d28ac27b2064d)   CYHAL\_PORT\_19 |
| #define | [P20](#a33f788605a598e63ac41746fa80a2748)   CYHAL\_PORT\_20 |
| #define | [DT\_GET\_CYHAL\_GPIO\_FROM\_DT\_GPIOS](#a19da54df2a9e4e46dd945bdbb56f276c)(node, gpios\_prop) |

## Macro Definition Documentation

## [◆ ](#ac58363c207e4f8ea82394859044b2690)DT\_CAT1\_DRIVE\_MODE\_INFO

| #define DT\_CAT1\_DRIVE\_MODE\_INFO | ( |  | *peripheral\_signal* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

CAT1\_PIN\_MAP\_DRIVE\_MODE\_##peripheral\_signal

Macro to set drive mode.

## [◆ ](#a33b355e05d5b955a6b8d48f3613c2d9a)DT\_CAT1\_PINMUX

| #define DT\_CAT1\_PINMUX | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin*, |
|  |  |  | *hsiom* ) |

**Value:**

((port << [SOC\_PINMUX\_PORT\_POS](#a6ba3e93a5498c6c5bd5e8f3d0c00ac2a)) | \

(pin << [SOC\_PINMUX\_PIN\_POS](#a5266efcdc6dbcd64d8fc61c814b37dc7)) | \

(hsiom << [SOC\_PINMUX\_HSIOM\_FUNC\_POS](#a2af56d2b85a6e4ba3a2f1fdd191f8c98)))

[SOC\_PINMUX\_HSIOM\_FUNC\_POS](#a2af56d2b85a6e4ba3a2f1fdd191f8c98)

#define SOC\_PINMUX\_HSIOM\_FUNC\_POS

**Definition** ifx\_cat1-pinctrl.h:18

[SOC\_PINMUX\_PIN\_POS](#a5266efcdc6dbcd64d8fc61c814b37dc7)

#define SOC\_PINMUX\_PIN\_POS

**Definition** ifx\_cat1-pinctrl.h:16

[SOC\_PINMUX\_PORT\_POS](#a6ba3e93a5498c6c5bd5e8f3d0c00ac2a)

#define SOC\_PINMUX\_PORT\_POS

Pin control binding helper.

**Definition** ifx\_cat1-pinctrl.h:14

Macro to set pin control information (from pinctrl node).

## [◆ ](#a19da54df2a9e4e46dd945bdbb56f276c)DT\_GET\_CYHAL\_GPIO\_FROM\_DT\_GPIOS

| #define DT\_GET\_CYHAL\_GPIO\_FROM\_DT\_GPIOS | ( |  | *node*, |
| --- | --- | --- | --- |
|  |  |  | *gpios\_prop* ) |

**Value:**

CYHAL\_GET\_GPIO( \

([DT\_REG\_ADDR\_BY\_IDX](group__devicetree-reg-prop.md#gac540b00bb12d0662f6aefe6ac0cff243)([DT\_GPIO\_CTLR\_BY\_IDX](group__devicetree-gpio.md#ga97bd46d2ab88d392a3f336f4d23184eb)(node, gpios\_prop, 0), 0) - \

[DT\_REG\_ADDR\_BY\_IDX](group__devicetree-reg-prop.md#gac540b00bb12d0662f6aefe6ac0cff243)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(gpio\_prt0), 0)) / \

[DT\_REG\_ADDR\_BY\_IDX](group__devicetree-reg-prop.md#gac540b00bb12d0662f6aefe6ac0cff243)([DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(gpio\_prt0), 1), \

[DT\_PHA\_BY\_IDX](group__devicetree-generic-prop.md#ga118b63fd22c20ef940ac2fa073c126ed)(node, gpios\_prop, 0, pin) \

)

[DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)

#define DT\_NODELABEL(label)

Get a node identifier for a node label.

**Definition** devicetree.h:196

[DT\_PHA\_BY\_IDX](group__devicetree-generic-prop.md#ga118b63fd22c20ef940ac2fa073c126ed)

#define DT\_PHA\_BY\_IDX(node\_id, pha, idx, cell)

Get a phandle-array specifier cell value at an index.

**Definition** devicetree.h:1564

[DT\_GPIO\_CTLR\_BY\_IDX](group__devicetree-gpio.md#ga97bd46d2ab88d392a3f336f4d23184eb)

#define DT\_GPIO\_CTLR\_BY\_IDX(node\_id, gpio\_pha, idx)

Get the node identifier for the controller phandle from a gpio phandle-array property at an index.

**Definition** gpio.h:53

[DT\_REG\_ADDR\_BY\_IDX](group__devicetree-reg-prop.md#gac540b00bb12d0662f6aefe6ac0cff243)

#define DT\_REG\_ADDR\_BY\_IDX(node\_id, idx)

Get the base address of the register block at index idx.

**Definition** devicetree.h:2437

## [◆ ](#a3080ad4afafa572482ea1a5b49f6a1ce)HSIOM\_SEL\_ACT\_0

| #define HSIOM\_SEL\_ACT\_0   (8) |
| --- |

## [◆ ](#a990e35fecfcc37ca08fe709eee746618)HSIOM\_SEL\_ACT\_1

| #define HSIOM\_SEL\_ACT\_1   (9) |
| --- |

## [◆ ](#a42c5af47fba8b69dacb3064e332193fd)HSIOM\_SEL\_ACT\_10

| #define HSIOM\_SEL\_ACT\_10   (22) |
| --- |

## [◆ ](#a48052c8dd78b1403de4d675571b7e6e2)HSIOM\_SEL\_ACT\_11

| #define HSIOM\_SEL\_ACT\_11   (23) |
| --- |

## [◆ ](#a6fc1302224b4d7585c25c3dc2ea340e7)HSIOM\_SEL\_ACT\_12

| #define HSIOM\_SEL\_ACT\_12   (24) |
| --- |

## [◆ ](#ae4fb8f65206098cace15b3e0f1c12a3e)HSIOM\_SEL\_ACT\_13

| #define HSIOM\_SEL\_ACT\_13   (25) |
| --- |

## [◆ ](#a7c3ffb4e79372b4cc4d1a7b4554911d5)HSIOM\_SEL\_ACT\_14

| #define HSIOM\_SEL\_ACT\_14   (26) |
| --- |

## [◆ ](#ab3285eea99f44cbe985eb097d1166a3d)HSIOM\_SEL\_ACT\_15

| #define HSIOM\_SEL\_ACT\_15   (27) |
| --- |

## [◆ ](#a696aeb76109bf339ebf0fcd20979f211)HSIOM\_SEL\_ACT\_2

| #define HSIOM\_SEL\_ACT\_2   (10) |
| --- |

## [◆ ](#a25e956bc540c9570392a1722b7e94670)HSIOM\_SEL\_ACT\_3

| #define HSIOM\_SEL\_ACT\_3   (11) |
| --- |

## [◆ ](#a3336f2e2d4886e0e46819ee4f4d96734)HSIOM\_SEL\_ACT\_4

| #define HSIOM\_SEL\_ACT\_4   (16) |
| --- |

## [◆ ](#a1040ff80864b6a1d85eb4c07f4278ea1)HSIOM\_SEL\_ACT\_5

| #define HSIOM\_SEL\_ACT\_5   (17) |
| --- |

## [◆ ](#a575188296b25564faa9b3a3b4817b5e4)HSIOM\_SEL\_ACT\_6

| #define HSIOM\_SEL\_ACT\_6   (18) |
| --- |

## [◆ ](#ae9c0f6360d56214106b09861eedb911a)HSIOM\_SEL\_ACT\_7

| #define HSIOM\_SEL\_ACT\_7   (19) |
| --- |

## [◆ ](#a8d36acbee0c4de7088ddc08a8b1c07a6)HSIOM\_SEL\_ACT\_8

| #define HSIOM\_SEL\_ACT\_8   (20) |
| --- |

## [◆ ](#aff276e6f5cdc671648a428c22fc2776e)HSIOM\_SEL\_ACT\_9

| #define HSIOM\_SEL\_ACT\_9   (21) |
| --- |

## [◆ ](#a8806729fcb666c9de823be5dd55c873d)HSIOM\_SEL\_AMUXA

| #define HSIOM\_SEL\_AMUXA   (4) |
| --- |

## [◆ ](#a4ba8695f92c0f347dd25ef981d67d1b0)HSIOM\_SEL\_AMUXA\_DSI

| #define HSIOM\_SEL\_AMUXA\_DSI   (6) |
| --- |

## [◆ ](#a862eb93443c5c9575ff990b776b6203b)HSIOM\_SEL\_AMUXB

| #define HSIOM\_SEL\_AMUXB   (5) |
| --- |

## [◆ ](#af7a28a087a8867a14423e9ab471cce54)HSIOM\_SEL\_AMUXB\_DSI

| #define HSIOM\_SEL\_AMUXB\_DSI   (7) |
| --- |

## [◆ ](#afb33417be16e7fa6423fadd2ef4a0f5b)HSIOM\_SEL\_DS\_0

| #define HSIOM\_SEL\_DS\_0   (12) |
| --- |

## [◆ ](#aa06be65ae17fc2dc1861c2af2e364652)HSIOM\_SEL\_DS\_1

| #define HSIOM\_SEL\_DS\_1   (13) |
| --- |

## [◆ ](#a07f591dc1f8a9f9eda13063d8c58c4eb)HSIOM\_SEL\_DS\_2

| #define HSIOM\_SEL\_DS\_2   (14) |
| --- |

## [◆ ](#a157da2f7e72fa8f19dfd682ec4444319)HSIOM\_SEL\_DS\_3

| #define HSIOM\_SEL\_DS\_3   (15) |
| --- |

## [◆ ](#a0f134c65358e450ca55341bbfec1cd0e)HSIOM\_SEL\_DS\_4

| #define HSIOM\_SEL\_DS\_4   (28) |
| --- |

## [◆ ](#a4208fc8f94abf237d943bc5e8ffe3080)HSIOM\_SEL\_DS\_5

| #define HSIOM\_SEL\_DS\_5   (29) |
| --- |

## [◆ ](#ac0153eaa52ef010bf58304a44ecb1e9b)HSIOM\_SEL\_DS\_6

| #define HSIOM\_SEL\_DS\_6   (30) |
| --- |

## [◆ ](#a8c067c1737f0f1573e056a384954fd81)HSIOM\_SEL\_DS\_7

| #define HSIOM\_SEL\_DS\_7   (31) |
| --- |

## [◆ ](#a959873e5156c6e3c24dd2773bb1ba516)HSIOM\_SEL\_DSI\_DSI

| #define HSIOM\_SEL\_DSI\_DSI   (2) |
| --- |

## [◆ ](#a022f7af586ee9b46f689d187e8dd73d8)HSIOM\_SEL\_DSI\_GPIO

| #define HSIOM\_SEL\_DSI\_GPIO   (3) |
| --- |

## [◆ ](#ac0d2af1bfb229de155412af7f00e4fe0)HSIOM\_SEL\_GPIO

| #define HSIOM\_SEL\_GPIO   (0) |
| --- |

Functions are defined using HSIOM SEL.

## [◆ ](#a441de7f56a1c7c75cdae4d9f93ccfade)HSIOM\_SEL\_GPIO\_DSI

| #define HSIOM\_SEL\_GPIO\_DSI   (1) |
| --- |

## [◆ ](#a1583b00a62bc1138f99bbfcd8ef81a6a)P0

| #define P0   CYHAL\_PORT\_0 |
| --- |

## [◆ ](#a6c2a9f7efd46f0160f3037869924d6ce)P1

| #define P1   CYHAL\_PORT\_1 |
| --- |

## [◆ ](#a5bb9f89248afa8d7e5a821fd459b085f)P10

| #define P10   CYHAL\_PORT\_10 |
| --- |

## [◆ ](#aca6db006bc37d2b337fca225a79856c8)P11

| #define P11   CYHAL\_PORT\_11 |
| --- |

## [◆ ](#a20c70bba8105b63590b5a49d99f563b5)P12

| #define P12   CYHAL\_PORT\_12 |
| --- |

## [◆ ](#aa729f895b03c9230ebcf8c798f7bd1bb)P13

| #define P13   CYHAL\_PORT\_13 |
| --- |

## [◆ ](#af108487a116bc015d7abd21ee2ab374e)P14

| #define P14   CYHAL\_PORT\_14 |
| --- |

## [◆ ](#a3059522b4d1048ecf60259f3805147d6)P15

| #define P15   CYHAL\_PORT\_15 |
| --- |

## [◆ ](#a0f8aefca2c1a1d922ca9ecac68caa584)P16

| #define P16   CYHAL\_PORT\_16 |
| --- |

## [◆ ](#ac8f5bddb889a3da7918ae32ca6c5cc97)P17

| #define P17   CYHAL\_PORT\_17 |
| --- |

## [◆ ](#ae6f383959ce67f3403d4cf1e7aacb1cb)P18

| #define P18   CYHAL\_PORT\_18 |
| --- |

## [◆ ](#af04bd18711f898d17e1d28ac27b2064d)P19

| #define P19   CYHAL\_PORT\_19 |
| --- |

## [◆ ](#ae00a52dba55d31948c377fa85d385b87)P2

| #define P2   CYHAL\_PORT\_2 |
| --- |

## [◆ ](#a33f788605a598e63ac41746fa80a2748)P20

| #define P20   CYHAL\_PORT\_20 |
| --- |

## [◆ ](#a0707a89c2f63bd260108e9dbb669358e)P3

| #define P3   CYHAL\_PORT\_3 |
| --- |

## [◆ ](#acbc14a33d017f5f2dabce1cb0d85718e)P4

| #define P4   CYHAL\_PORT\_4 |
| --- |

## [◆ ](#a49ce5f7954a95865f12be8083ccb2719)P5

| #define P5   CYHAL\_PORT\_5 |
| --- |

## [◆ ](#ab276be36e56dfdd17d860fbc82c3a22d)P6

| #define P6   CYHAL\_PORT\_6 |
| --- |

## [◆ ](#a017ae5a42bc27ff7402656a779fec303)P7

| #define P7   CYHAL\_PORT\_7 |
| --- |

## [◆ ](#ae04365e5a91d08e332a28f00efe389fe)P8

| #define P8   CYHAL\_PORT\_8 |
| --- |

## [◆ ](#a8b201e09e2f1d58d8f3ad3a14c02b86b)P9

| #define P9   CYHAL\_PORT\_9 |
| --- |

## [◆ ](#a2af56d2b85a6e4ba3a2f1fdd191f8c98)SOC\_PINMUX\_HSIOM\_FUNC\_POS

| #define SOC\_PINMUX\_HSIOM\_FUNC\_POS   (16) |
| --- |

## [◆ ](#a6baa74b565ac921b7e3b8b5fc65327a6)SOC\_PINMUX\_HSIOM\_MASK

| #define SOC\_PINMUX\_HSIOM\_MASK   (0xFFul << [SOC\_PINMUX\_HSIOM\_FUNC\_POS](#a2af56d2b85a6e4ba3a2f1fdd191f8c98)) |
| --- |

## [◆ ](#a881a5ee83663d0eac3a2cfd530e23266)SOC\_PINMUX\_PIN\_MASK

| #define SOC\_PINMUX\_PIN\_MASK   (0xFFul << [SOC\_PINMUX\_PIN\_POS](#a5266efcdc6dbcd64d8fc61c814b37dc7)) |
| --- |

## [◆ ](#a5266efcdc6dbcd64d8fc61c814b37dc7)SOC\_PINMUX\_PIN\_POS

| #define SOC\_PINMUX\_PIN\_POS   (8) |
| --- |

## [◆ ](#a4199ffda078d925e8dfb58194117de1a)SOC\_PINMUX\_PORT\_MASK

| #define SOC\_PINMUX\_PORT\_MASK   (0xFFul << [SOC\_PINMUX\_PORT\_POS](#a6ba3e93a5498c6c5bd5e8f3d0c00ac2a)) |
| --- |

## [◆ ](#a6ba3e93a5498c6c5bd5e8f3d0c00ac2a)SOC\_PINMUX\_PORT\_POS

| #define SOC\_PINMUX\_PORT\_POS   (0) |
| --- |

Pin control binding helper.

Bit definition in PINMUX field

## [◆ ](#aca26c39aa27a6520ea0f57b7ab058672)SOC\_PINMUX\_SIGNAL\_MASK

| #define SOC\_PINMUX\_SIGNAL\_MASK   (0xFFul << [SOC\_PINMUX\_SIGNAL\_POS](#a38673a696cc1caa97e13eb6ef937007a)) |
| --- |

## [◆ ](#a38673a696cc1caa97e13eb6ef937007a)SOC\_PINMUX\_SIGNAL\_POS

| #define SOC\_PINMUX\_SIGNAL\_POS   (24) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [ifx\_cat1-pinctrl.h](ifx__cat1-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
