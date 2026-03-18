---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__mipi__interface.html
original_path: doxygen/html/group__mipi__interface.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

MIPI Display interface

[Device Driver APIs](group__io__interfaces.md)

MIPI Display definitions.
[More...](#details)

| MIPI-DSI DCS (Display Command Set) | |
| --- | --- |
| #define | [MIPI\_DCS\_NOP](#gadcaf06472d3e281e425bd2d71c5beaed)   0x00U |
| #define | [MIPI\_DCS\_SOFT\_RESET](#gab8c88ef2d316b783d5222a85d0e118ea)   0x01U |
| #define | [MIPI\_DCS\_GET\_COMPRESSION\_MODE](#ga6d88c902f9d07c1fff0d1e92fe966fad)   0x03U |
| #define | [MIPI\_DCS\_GET\_DISPLAY\_ID](#ga94cb2e4ce1ae29871de780301d4d59d0)   0x04U |
| #define | [MIPI\_DCS\_GET\_RED\_CHANNEL](#ga5007b2e6e6e7750d13cb8421ff06d8e7)   0x06U |
| #define | [MIPI\_DCS\_GET\_GREEN\_CHANNEL](#gaa40f1c03dca04961a28dd19754212f06)   0x07U |
| #define | [MIPI\_DCS\_GET\_BLUE\_CHANNEL](#gaf1091bc7718eb7aa3a2c72c5c025ab4d)   0x08U |
| #define | [MIPI\_DCS\_GET\_DISPLAY\_STATUS](#gaca8b503fdca34456ca68ced074873424)   0x09U |
| #define | [MIPI\_DCS\_GET\_POWER\_MODE](#ga48669397e8ea5a7c6e0cb09ea9d4fd5c)   0x0AU |
| #define | [MIPI\_DCS\_GET\_ADDRESS\_MODE](#ga9da041d715731d8d67caad967e5d6002)   0x0BU |
| #define | [MIPI\_DCS\_GET\_PIXEL\_FORMAT](#gae7088fe2f1351d534262d111692a1bfa)   0x0CU |
| #define | [MIPI\_DCS\_GET\_DISPLAY\_MODE](#gaf752f812f791e805fbfed0d3ab9b89de)   0x0DU |
| #define | [MIPI\_DCS\_GET\_SIGNAL\_MODE](#gaa80bc31f551b39eff6625e80c211f16a)   0x0EU |
| #define | [MIPI\_DCS\_GET\_DIAGNOSTIC\_RESULT](#ga8ec1590be25764411567933943b77869)   0x0FU |
| #define | [MIPI\_DCS\_ENTER\_SLEEP\_MODE](#ga06f9b8e87b6f1f6f41a139db370f236b)   0x10U |
| #define | [MIPI\_DCS\_EXIT\_SLEEP\_MODE](#ga276231424603f027583ffd2a1bdd6089)   0x11U |
| #define | [MIPI\_DCS\_ENTER\_PARTIAL\_MODE](#ga219bb0ba9e91812f4ab372adaa9afd07)   0x12U |
| #define | [MIPI\_DCS\_ENTER\_NORMAL\_MODE](#gaedb3b5fa815593d3fa1ae247383d8a8e)   0x13U |
| #define | [MIPI\_DCS\_EXIT\_INVERT\_MODE](#ga41a4fd226d8f86ba2efa34403b4033f8)   0x20U |
| #define | [MIPI\_DCS\_ENTER\_INVERT\_MODE](#gad1041d71940752f1c1121cf392a3b2d3)   0x21U |
| #define | [MIPI\_DCS\_SET\_GAMMA\_CURVE](#ga14771de93ba08dffabafffcedc85b54e)   0x26U |
| #define | [MIPI\_DCS\_SET\_DISPLAY\_OFF](#gaf50a5539c89552512ffcd04ece5b7fe0)   0x28U |
| #define | [MIPI\_DCS\_SET\_DISPLAY\_ON](#gabdbee428ef6d48009a5795e384665c8f)   0x29U |
| #define | [MIPI\_DCS\_SET\_COLUMN\_ADDRESS](#ga2d08791d990c2e4d9c6c9800ad2d8c1b)   0x2AU |
| #define | [MIPI\_DCS\_SET\_PAGE\_ADDRESS](#ga63334f8e1458151197a35c7d5cf781a5)   0x2BU |
| #define | [MIPI\_DCS\_WRITE\_MEMORY\_START](#ga9a31b4772025e2046816057b74d2e7cd)   0x2CU |
| #define | [MIPI\_DCS\_WRITE\_LUT](#ga6f94b4db07db5a287cd50ed87197a9c2)   0x2DU |
| #define | [MIPI\_DCS\_READ\_MEMORY\_START](#ga860180f5477caadae3857b4c93f04281)   0x2EU |
| #define | [MIPI\_DCS\_SET\_PARTIAL\_ROWS](#ga18fe9e1cf30da71c18bebce1960095c3)   0x30U |
| #define | [MIPI\_DCS\_SET\_PARTIAL\_COLUMNS](#ga359a43a0bb277b8f09fa1120bb2c3b09)   0x31U |
| #define | [MIPI\_DCS\_SET\_SCROLL\_AREA](#ga36aa83afeed02df37cb2bb295915c92d)   0x33U |
| #define | [MIPI\_DCS\_SET\_TEAR\_OFF](#gadcd4fd3ea6ccbb63ebecb290c00c660f)   0x34U |
| #define | [MIPI\_DCS\_SET\_TEAR\_ON](#gad85387743db362579b788fd28ecd2fbf)   0x35U |
| #define | [MIPI\_DCS\_SET\_ADDRESS\_MODE](#ga1d7e5a77666d13f4a8a435db202f4323)   0x36U |
| #define | [MIPI\_DCS\_SET\_SCROLL\_START](#gaee29e37b0cb4b10920211048e0d95756)   0x37U |
| #define | [MIPI\_DCS\_EXIT\_IDLE\_MODE](#gaf0a1f7ede08492751141cf52235808b3)   0x38U |
| #define | [MIPI\_DCS\_ENTER\_IDLE\_MODE](#ga7f1dfc0645ab456b38ac2caae783b709)   0x39U |
| #define | [MIPI\_DCS\_SET\_PIXEL\_FORMAT](#ga1165d0835844eb0bd86fa6d30db7a84d)   0x3AU |
| #define | [MIPI\_DCS\_WRITE\_MEMORY\_CONTINUE](#ga532122daccbd1370332fd9c26569c11f)   0x3CU |
| #define | [MIPI\_DCS\_SET\_3D\_CONTROL](#gaf9210d3033c2b09a7da608e9aeb88ad1)   0x3DU |
| #define | [MIPI\_DCS\_READ\_MEMORY\_CONTINUE](#ga6d3fcf5c050b45d8afe3af4ec98adadc)   0x3EU |
| #define | [MIPI\_DCS\_GET\_3D\_CONTROL](#gaace0882d961807760db2ed7693ab760a)   0x3FU |
| #define | [MIPI\_DCS\_SET\_VSYNC\_TIMING](#ga9597f72175b99376f7119b95cf425c1c)   0x40U |
| #define | [MIPI\_DCS\_SET\_TEAR\_SCANLINE](#gaaac44d1367419dc395332712b0427458)   0x44U |
| #define | [MIPI\_DCS\_GET\_SCANLINE](#ga7933493853f9ef2dd28b31ea2fbb492f)   0x45U |
| #define | [MIPI\_DCS\_SET\_DISPLAY\_BRIGHTNESS](#gac8dec8303a247b56a513628645d67f2b)   0x51U |
| #define | [MIPI\_DCS\_GET\_DISPLAY\_BRIGHTNESS](#ga4df917017e27912a343731b350e8d02e)   0x52U |
| #define | [MIPI\_DCS\_WRITE\_CONTROL\_DISPLAY](#gad47f873520b505e3463ad1f85d617787)   0x53U |
| #define | [MIPI\_DCS\_GET\_CONTROL\_DISPLAY](#ga9f83f0b2412084ab2ac3edd36b41fc11)   0x54U |
| #define | [MIPI\_DCS\_WRITE\_POWER\_SAVE](#ga2655d637a53b1b5e805ab3d69bc9fe9e)   0x55U |
| #define | [MIPI\_DCS\_GET\_POWER\_SAVE](#ga518ba3d308b6c453850e5168b26d1024)   0x56U |
| #define | [MIPI\_DCS\_SET\_CABC\_MIN\_BRIGHTNESS](#gab0d27051994aa70c8baf12a103080e80)   0x5EU |
| #define | [MIPI\_DCS\_GET\_CABC\_MIN\_BRIGHTNESS](#ga2d56066851a38acf38323cd2327820c4)   0x5FU |
| #define | [MIPI\_DCS\_READ\_DDB\_START](#ga6cccd95a6bc9c007bb648b70d664c34d)   0xA1U |
| #define | [MIPI\_DCS\_READ\_DDB\_CONTINUE](#ga26b4f0111aee93b8ad01448d7b4af368)   0xA8U |
| #define | [MIPI\_DCS\_PIXEL\_FORMAT\_24BIT](#ga2772b5432484431573d092447c12e005)   0x77 |
| #define | [MIPI\_DCS\_PIXEL\_FORMAT\_18BIT](#gab2d74d3cc0ce8036b57d5aec073b5b6b)   0x66 |
| #define | [MIPI\_DCS\_PIXEL\_FORMAT\_16BIT](#ga171be8bd1a5551ffc129c14e0d829e61)   0x55 |
| #define | [MIPI\_DCS\_PIXEL\_FORMAT\_12BIT](#ga77944b2fd7f59be6698bd414cbeedcac)   0x33 |
| #define | [MIPI\_DCS\_PIXEL\_FORMAT\_8BIT](#gac3e18d2d9d4bcfb98d99518021bf98bd)   0x22 |
| #define | [MIPI\_DCS\_PIXEL\_FORMAT\_3BIT](#ga5a14ff4ebc8e81b9bc92e87069ad7466)   0x11 |

| MIPI-DSI Address mode register fields. | |
| --- | --- |
| #define | [MIPI\_DCS\_ADDRESS\_MODE\_MIRROR\_Y](#ga549bdf77bc40cc4a5cc81004b3f91775)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| #define | [MIPI\_DCS\_ADDRESS\_MODE\_MIRROR\_X](#gaa9c5f1e04806ef4dd672a6169136d07c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| #define | [MIPI\_DCS\_ADDRESS\_MODE\_SWAP\_XY](#gadfce4431c308f186479af4d15c83187b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| #define | [MIPI\_DCS\_ADDRESS\_MODE\_REFRESH\_BT](#gad8591d77dafcb2d1ccc2ce971b012761)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| #define | [MIPI\_DCS\_ADDRESS\_MODE\_BGR](#ga5320efc9a396b1cdfe89c5cfc87d8c11)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [MIPI\_DCS\_ADDRESS\_MODE\_LATCH\_RL](#gaa32acf97423f4491b27b2d9cb7d49a3c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [MIPI\_DCS\_ADDRESS\_MODE\_FLIP\_X](#ga75df1e79cde793c01c47103bf683f3aa)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [MIPI\_DCS\_ADDRESS\_MODE\_FLIP\_Y](#ga72cf84630b55cd8dfe762eb84272692f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |

| MIPI-DSI Processor-to-Peripheral transaction types. | |
| --- | --- |
| #define | [MIPI\_DSI\_V\_SYNC\_START](#gad58c27d600a73e38f33669a3ae743f01)   0x01U |
| #define | [MIPI\_DSI\_V\_SYNC\_END](#gaf85ef5c73d29fec41460de8b752cef39)   0x11U |
| #define | [MIPI\_DSI\_H\_SYNC\_START](#ga6852f3d6bfb77101d64b10a2b48a91c5)   0x21U |
| #define | [MIPI\_DSI\_H\_SYNC\_END](#gaa8cc494ce41880ec765701ee4beffe97)   0x31U |
| #define | [MIPI\_DSI\_COLOR\_MODE\_OFF](#gad713fb809d6012db370ef23601c81619)   0x02U |
| #define | [MIPI\_DSI\_COLOR\_MODE\_ON](#ga1987975c9389ec9570c5ff05e3e1a9b1)   0x12U |
| #define | [MIPI\_DSI\_SHUTDOWN\_PERIPHERAL](#gafac7d0f045d77fed0ff35f3a3503f6a5)   0x22U |
| #define | [MIPI\_DSI\_TURN\_ON\_PERIPHERAL](#ga56292f7b60a0e7b55cd5118c1641c3ba)   0x32U |
| #define | [MIPI\_DSI\_GENERIC\_SHORT\_WRITE\_0\_PARAM](#ga639170a23fa7b28e6bf3726c8d54ead0)   0x03U |
| #define | [MIPI\_DSI\_GENERIC\_SHORT\_WRITE\_1\_PARAM](#gaa0e596feb47e6eada0217fa7a81a0278)   0x13U |
| #define | [MIPI\_DSI\_GENERIC\_SHORT\_WRITE\_2\_PARAM](#gaea2acb4489552a159a19278018122ce6)   0x23U |
| #define | [MIPI\_DSI\_GENERIC\_READ\_REQUEST\_0\_PARAM](#ga9d541d3e054b1fa75fd7f1b0ffa3883a)   0x04U |
| #define | [MIPI\_DSI\_GENERIC\_READ\_REQUEST\_1\_PARAM](#gabff929d8285415c0d3edb95748bf2686)   0x14U |
| #define | [MIPI\_DSI\_GENERIC\_READ\_REQUEST\_2\_PARAM](#ga9ea3c57a021879863097edc3f275ea60)   0x24U |
| #define | [MIPI\_DSI\_DCS\_SHORT\_WRITE](#ga51191c76ceca6f0e79cdb4f0e58013a3)   0x05U |
| #define | [MIPI\_DSI\_DCS\_SHORT\_WRITE\_PARAM](#ga5e0e1bf73a04668617e46cb0392bac8d)   0x15U |
| #define | [MIPI\_DSI\_DCS\_READ](#ga60acd68f9c3271b2cd306f6bb5e4af94)   0x06U |
| #define | [MIPI\_DSI\_SET\_MAXIMUM\_RETURN\_PACKET\_SIZE](#gab07bcea365f9835c5df3c37d15f3073c)   0x37U |
| #define | [MIPI\_DSI\_END\_OF\_TRANSMISSION](#ga575957d9fd4de559cd938b332f1eff05)   0x08U |
| #define | [MIPI\_DSI\_NULL\_PACKET](#gabcd142889c213edb8a7e7e95bb138b08)   0x09U |
| #define | [MIPI\_DSI\_BLANKING\_PACKET](#ga66550282423b364aed89c6ed2c202329)   0x19U |
| #define | [MIPI\_DSI\_GENERIC\_LONG\_WRITE](#gadb6e6683462c4b8eaeda3a77b86f3e1d)   0x29U |
| #define | [MIPI\_DSI\_DCS\_LONG\_WRITE](#ga141eda8b32761dc7a275524c04e45535)   0x39U |
| #define | [MIPI\_DSI\_LOOSELY\_PACKED\_PIXEL\_STREAM\_YCBCR20](#ga933521f6a7f2f8ebad1569a0e8320d41)   0x0CU |
| #define | [MIPI\_DSI\_PACKED\_PIXEL\_STREAM\_YCBCR24](#ga858695ed8e1f5234d25f44b59a4f270d)   0x1CU |
| #define | [MIPI\_DSI\_PACKED\_PIXEL\_STREAM\_YCBCR16](#ga928d1364d635cb892f5992f7cdda7905)   0x2CU |
| #define | [MIPI\_DSI\_PACKED\_PIXEL\_STREAM\_30](#ga09da8d6976e18b7ac074f9e10cc8c52f)   0x0DU |
| #define | [MIPI\_DSI\_PACKED\_PIXEL\_STREAM\_36](#ga0015e0c7df4f3688e5567099f9d0ea11)   0x1DU |
| #define | [MIPI\_DSI\_PACKED\_PIXEL\_STREAM\_YCBCR12](#ga999976bf03f40c56ccb9272f99334cdf)   0x3DU |
| #define | [MIPI\_DSI\_PACKED\_PIXEL\_STREAM\_16](#ga93db7cc5b15cd5683ba8b9358731e151)   0x0EU |
| #define | [MIPI\_DSI\_PACKED\_PIXEL\_STREAM\_18](#ga3bf54b5ef30c94f863c353ac8a68f0f0)   0x1EU |
| #define | [MIPI\_DSI\_PIXEL\_STREAM\_3BYTE\_18](#gaeee3817bcc554f3c04cb737e03649733)   0x2EU |
| #define | [MIPI\_DSI\_PACKED\_PIXEL\_STREAM\_24](#ga0956384d8db5940cc6ffe3a4569a2fb2)   0x3EU |

## Detailed Description

MIPI Display definitions.

## Macro Definition Documentation

## [◆ ](#ga5320efc9a396b1cdfe89c5cfc87d8c11)MIPI\_DCS\_ADDRESS\_MODE\_BGR

| #define MIPI\_DCS\_ADDRESS\_MODE\_BGR   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga75df1e79cde793c01c47103bf683f3aa)MIPI\_DCS\_ADDRESS\_MODE\_FLIP\_X

| #define MIPI\_DCS\_ADDRESS\_MODE\_FLIP\_X   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga72cf84630b55cd8dfe762eb84272692f)MIPI\_DCS\_ADDRESS\_MODE\_FLIP\_Y

| #define MIPI\_DCS\_ADDRESS\_MODE\_FLIP\_Y   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#gaa32acf97423f4491b27b2d9cb7d49a3c)MIPI\_DCS\_ADDRESS\_MODE\_LATCH\_RL

| #define MIPI\_DCS\_ADDRESS\_MODE\_LATCH\_RL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#gaa9c5f1e04806ef4dd672a6169136d07c)MIPI\_DCS\_ADDRESS\_MODE\_MIRROR\_X

| #define MIPI\_DCS\_ADDRESS\_MODE\_MIRROR\_X   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga549bdf77bc40cc4a5cc81004b3f91775)MIPI\_DCS\_ADDRESS\_MODE\_MIRROR\_Y

| #define MIPI\_DCS\_ADDRESS\_MODE\_MIRROR\_Y   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#gad8591d77dafcb2d1ccc2ce971b012761)MIPI\_DCS\_ADDRESS\_MODE\_REFRESH\_BT

| #define MIPI\_DCS\_ADDRESS\_MODE\_REFRESH\_BT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#gadfce4431c308f186479af4d15c83187b)MIPI\_DCS\_ADDRESS\_MODE\_SWAP\_XY

| #define MIPI\_DCS\_ADDRESS\_MODE\_SWAP\_XY   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga7f1dfc0645ab456b38ac2caae783b709)MIPI\_DCS\_ENTER\_IDLE\_MODE

| #define MIPI\_DCS\_ENTER\_IDLE\_MODE   0x39U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#gad1041d71940752f1c1121cf392a3b2d3)MIPI\_DCS\_ENTER\_INVERT\_MODE

| #define MIPI\_DCS\_ENTER\_INVERT\_MODE   0x21U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#gaedb3b5fa815593d3fa1ae247383d8a8e)MIPI\_DCS\_ENTER\_NORMAL\_MODE

| #define MIPI\_DCS\_ENTER\_NORMAL\_MODE   0x13U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga219bb0ba9e91812f4ab372adaa9afd07)MIPI\_DCS\_ENTER\_PARTIAL\_MODE

| #define MIPI\_DCS\_ENTER\_PARTIAL\_MODE   0x12U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga06f9b8e87b6f1f6f41a139db370f236b)MIPI\_DCS\_ENTER\_SLEEP\_MODE

| #define MIPI\_DCS\_ENTER\_SLEEP\_MODE   0x10U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#gaf0a1f7ede08492751141cf52235808b3)MIPI\_DCS\_EXIT\_IDLE\_MODE

| #define MIPI\_DCS\_EXIT\_IDLE\_MODE   0x38U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga41a4fd226d8f86ba2efa34403b4033f8)MIPI\_DCS\_EXIT\_INVERT\_MODE

| #define MIPI\_DCS\_EXIT\_INVERT\_MODE   0x20U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga276231424603f027583ffd2a1bdd6089)MIPI\_DCS\_EXIT\_SLEEP\_MODE

| #define MIPI\_DCS\_EXIT\_SLEEP\_MODE   0x11U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#gaace0882d961807760db2ed7693ab760a)MIPI\_DCS\_GET\_3D\_CONTROL

| #define MIPI\_DCS\_GET\_3D\_CONTROL   0x3FU |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga9da041d715731d8d67caad967e5d6002)MIPI\_DCS\_GET\_ADDRESS\_MODE

| #define MIPI\_DCS\_GET\_ADDRESS\_MODE   0x0BU |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#gaf1091bc7718eb7aa3a2c72c5c025ab4d)MIPI\_DCS\_GET\_BLUE\_CHANNEL

| #define MIPI\_DCS\_GET\_BLUE\_CHANNEL   0x08U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga2d56066851a38acf38323cd2327820c4)MIPI\_DCS\_GET\_CABC\_MIN\_BRIGHTNESS

| #define MIPI\_DCS\_GET\_CABC\_MIN\_BRIGHTNESS   0x5FU |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga6d88c902f9d07c1fff0d1e92fe966fad)MIPI\_DCS\_GET\_COMPRESSION\_MODE

| #define MIPI\_DCS\_GET\_COMPRESSION\_MODE   0x03U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga9f83f0b2412084ab2ac3edd36b41fc11)MIPI\_DCS\_GET\_CONTROL\_DISPLAY

| #define MIPI\_DCS\_GET\_CONTROL\_DISPLAY   0x54U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga8ec1590be25764411567933943b77869)MIPI\_DCS\_GET\_DIAGNOSTIC\_RESULT

| #define MIPI\_DCS\_GET\_DIAGNOSTIC\_RESULT   0x0FU |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga4df917017e27912a343731b350e8d02e)MIPI\_DCS\_GET\_DISPLAY\_BRIGHTNESS

| #define MIPI\_DCS\_GET\_DISPLAY\_BRIGHTNESS   0x52U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga94cb2e4ce1ae29871de780301d4d59d0)MIPI\_DCS\_GET\_DISPLAY\_ID

| #define MIPI\_DCS\_GET\_DISPLAY\_ID   0x04U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#gaf752f812f791e805fbfed0d3ab9b89de)MIPI\_DCS\_GET\_DISPLAY\_MODE

| #define MIPI\_DCS\_GET\_DISPLAY\_MODE   0x0DU |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#gaca8b503fdca34456ca68ced074873424)MIPI\_DCS\_GET\_DISPLAY\_STATUS

| #define MIPI\_DCS\_GET\_DISPLAY\_STATUS   0x09U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#gaa40f1c03dca04961a28dd19754212f06)MIPI\_DCS\_GET\_GREEN\_CHANNEL

| #define MIPI\_DCS\_GET\_GREEN\_CHANNEL   0x07U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#gae7088fe2f1351d534262d111692a1bfa)MIPI\_DCS\_GET\_PIXEL\_FORMAT

| #define MIPI\_DCS\_GET\_PIXEL\_FORMAT   0x0CU |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga48669397e8ea5a7c6e0cb09ea9d4fd5c)MIPI\_DCS\_GET\_POWER\_MODE

| #define MIPI\_DCS\_GET\_POWER\_MODE   0x0AU |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga518ba3d308b6c453850e5168b26d1024)MIPI\_DCS\_GET\_POWER\_SAVE

| #define MIPI\_DCS\_GET\_POWER\_SAVE   0x56U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga5007b2e6e6e7750d13cb8421ff06d8e7)MIPI\_DCS\_GET\_RED\_CHANNEL

| #define MIPI\_DCS\_GET\_RED\_CHANNEL   0x06U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga7933493853f9ef2dd28b31ea2fbb492f)MIPI\_DCS\_GET\_SCANLINE

| #define MIPI\_DCS\_GET\_SCANLINE   0x45U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#gaa80bc31f551b39eff6625e80c211f16a)MIPI\_DCS\_GET\_SIGNAL\_MODE

| #define MIPI\_DCS\_GET\_SIGNAL\_MODE   0x0EU |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#gadcaf06472d3e281e425bd2d71c5beaed)MIPI\_DCS\_NOP

| #define MIPI\_DCS\_NOP   0x00U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga77944b2fd7f59be6698bd414cbeedcac)MIPI\_DCS\_PIXEL\_FORMAT\_12BIT

| #define MIPI\_DCS\_PIXEL\_FORMAT\_12BIT   0x33 |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga171be8bd1a5551ffc129c14e0d829e61)MIPI\_DCS\_PIXEL\_FORMAT\_16BIT

| #define MIPI\_DCS\_PIXEL\_FORMAT\_16BIT   0x55 |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#gab2d74d3cc0ce8036b57d5aec073b5b6b)MIPI\_DCS\_PIXEL\_FORMAT\_18BIT

| #define MIPI\_DCS\_PIXEL\_FORMAT\_18BIT   0x66 |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga2772b5432484431573d092447c12e005)MIPI\_DCS\_PIXEL\_FORMAT\_24BIT

| #define MIPI\_DCS\_PIXEL\_FORMAT\_24BIT   0x77 |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga5a14ff4ebc8e81b9bc92e87069ad7466)MIPI\_DCS\_PIXEL\_FORMAT\_3BIT

| #define MIPI\_DCS\_PIXEL\_FORMAT\_3BIT   0x11 |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#gac3e18d2d9d4bcfb98d99518021bf98bd)MIPI\_DCS\_PIXEL\_FORMAT\_8BIT

| #define MIPI\_DCS\_PIXEL\_FORMAT\_8BIT   0x22 |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga26b4f0111aee93b8ad01448d7b4af368)MIPI\_DCS\_READ\_DDB\_CONTINUE

| #define MIPI\_DCS\_READ\_DDB\_CONTINUE   0xA8U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga6cccd95a6bc9c007bb648b70d664c34d)MIPI\_DCS\_READ\_DDB\_START

| #define MIPI\_DCS\_READ\_DDB\_START   0xA1U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga6d3fcf5c050b45d8afe3af4ec98adadc)MIPI\_DCS\_READ\_MEMORY\_CONTINUE

| #define MIPI\_DCS\_READ\_MEMORY\_CONTINUE   0x3EU |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga860180f5477caadae3857b4c93f04281)MIPI\_DCS\_READ\_MEMORY\_START

| #define MIPI\_DCS\_READ\_MEMORY\_START   0x2EU |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#gaf9210d3033c2b09a7da608e9aeb88ad1)MIPI\_DCS\_SET\_3D\_CONTROL

| #define MIPI\_DCS\_SET\_3D\_CONTROL   0x3DU |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga1d7e5a77666d13f4a8a435db202f4323)MIPI\_DCS\_SET\_ADDRESS\_MODE

| #define MIPI\_DCS\_SET\_ADDRESS\_MODE   0x36U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#gab0d27051994aa70c8baf12a103080e80)MIPI\_DCS\_SET\_CABC\_MIN\_BRIGHTNESS

| #define MIPI\_DCS\_SET\_CABC\_MIN\_BRIGHTNESS   0x5EU |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga2d08791d990c2e4d9c6c9800ad2d8c1b)MIPI\_DCS\_SET\_COLUMN\_ADDRESS

| #define MIPI\_DCS\_SET\_COLUMN\_ADDRESS   0x2AU |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#gac8dec8303a247b56a513628645d67f2b)MIPI\_DCS\_SET\_DISPLAY\_BRIGHTNESS

| #define MIPI\_DCS\_SET\_DISPLAY\_BRIGHTNESS   0x51U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#gaf50a5539c89552512ffcd04ece5b7fe0)MIPI\_DCS\_SET\_DISPLAY\_OFF

| #define MIPI\_DCS\_SET\_DISPLAY\_OFF   0x28U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#gabdbee428ef6d48009a5795e384665c8f)MIPI\_DCS\_SET\_DISPLAY\_ON

| #define MIPI\_DCS\_SET\_DISPLAY\_ON   0x29U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga14771de93ba08dffabafffcedc85b54e)MIPI\_DCS\_SET\_GAMMA\_CURVE

| #define MIPI\_DCS\_SET\_GAMMA\_CURVE   0x26U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga63334f8e1458151197a35c7d5cf781a5)MIPI\_DCS\_SET\_PAGE\_ADDRESS

| #define MIPI\_DCS\_SET\_PAGE\_ADDRESS   0x2BU |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga359a43a0bb277b8f09fa1120bb2c3b09)MIPI\_DCS\_SET\_PARTIAL\_COLUMNS

| #define MIPI\_DCS\_SET\_PARTIAL\_COLUMNS   0x31U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga18fe9e1cf30da71c18bebce1960095c3)MIPI\_DCS\_SET\_PARTIAL\_ROWS

| #define MIPI\_DCS\_SET\_PARTIAL\_ROWS   0x30U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga1165d0835844eb0bd86fa6d30db7a84d)MIPI\_DCS\_SET\_PIXEL\_FORMAT

| #define MIPI\_DCS\_SET\_PIXEL\_FORMAT   0x3AU |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga36aa83afeed02df37cb2bb295915c92d)MIPI\_DCS\_SET\_SCROLL\_AREA

| #define MIPI\_DCS\_SET\_SCROLL\_AREA   0x33U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#gaee29e37b0cb4b10920211048e0d95756)MIPI\_DCS\_SET\_SCROLL\_START

| #define MIPI\_DCS\_SET\_SCROLL\_START   0x37U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#gadcd4fd3ea6ccbb63ebecb290c00c660f)MIPI\_DCS\_SET\_TEAR\_OFF

| #define MIPI\_DCS\_SET\_TEAR\_OFF   0x34U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#gad85387743db362579b788fd28ecd2fbf)MIPI\_DCS\_SET\_TEAR\_ON

| #define MIPI\_DCS\_SET\_TEAR\_ON   0x35U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#gaaac44d1367419dc395332712b0427458)MIPI\_DCS\_SET\_TEAR\_SCANLINE

| #define MIPI\_DCS\_SET\_TEAR\_SCANLINE   0x44U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga9597f72175b99376f7119b95cf425c1c)MIPI\_DCS\_SET\_VSYNC\_TIMING

| #define MIPI\_DCS\_SET\_VSYNC\_TIMING   0x40U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#gab8c88ef2d316b783d5222a85d0e118ea)MIPI\_DCS\_SOFT\_RESET

| #define MIPI\_DCS\_SOFT\_RESET   0x01U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#gad47f873520b505e3463ad1f85d617787)MIPI\_DCS\_WRITE\_CONTROL\_DISPLAY

| #define MIPI\_DCS\_WRITE\_CONTROL\_DISPLAY   0x53U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga6f94b4db07db5a287cd50ed87197a9c2)MIPI\_DCS\_WRITE\_LUT

| #define MIPI\_DCS\_WRITE\_LUT   0x2DU |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga532122daccbd1370332fd9c26569c11f)MIPI\_DCS\_WRITE\_MEMORY\_CONTINUE

| #define MIPI\_DCS\_WRITE\_MEMORY\_CONTINUE   0x3CU |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga9a31b4772025e2046816057b74d2e7cd)MIPI\_DCS\_WRITE\_MEMORY\_START

| #define MIPI\_DCS\_WRITE\_MEMORY\_START   0x2CU |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga2655d637a53b1b5e805ab3d69bc9fe9e)MIPI\_DCS\_WRITE\_POWER\_SAVE

| #define MIPI\_DCS\_WRITE\_POWER\_SAVE   0x55U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga66550282423b364aed89c6ed2c202329)MIPI\_DSI\_BLANKING\_PACKET

| #define MIPI\_DSI\_BLANKING\_PACKET   0x19U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#gad713fb809d6012db370ef23601c81619)MIPI\_DSI\_COLOR\_MODE\_OFF

| #define MIPI\_DSI\_COLOR\_MODE\_OFF   0x02U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga1987975c9389ec9570c5ff05e3e1a9b1)MIPI\_DSI\_COLOR\_MODE\_ON

| #define MIPI\_DSI\_COLOR\_MODE\_ON   0x12U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga141eda8b32761dc7a275524c04e45535)MIPI\_DSI\_DCS\_LONG\_WRITE

| #define MIPI\_DSI\_DCS\_LONG\_WRITE   0x39U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga60acd68f9c3271b2cd306f6bb5e4af94)MIPI\_DSI\_DCS\_READ

| #define MIPI\_DSI\_DCS\_READ   0x06U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga51191c76ceca6f0e79cdb4f0e58013a3)MIPI\_DSI\_DCS\_SHORT\_WRITE

| #define MIPI\_DSI\_DCS\_SHORT\_WRITE   0x05U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga5e0e1bf73a04668617e46cb0392bac8d)MIPI\_DSI\_DCS\_SHORT\_WRITE\_PARAM

| #define MIPI\_DSI\_DCS\_SHORT\_WRITE\_PARAM   0x15U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga575957d9fd4de559cd938b332f1eff05)MIPI\_DSI\_END\_OF\_TRANSMISSION

| #define MIPI\_DSI\_END\_OF\_TRANSMISSION   0x08U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#gadb6e6683462c4b8eaeda3a77b86f3e1d)MIPI\_DSI\_GENERIC\_LONG\_WRITE

| #define MIPI\_DSI\_GENERIC\_LONG\_WRITE   0x29U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga9d541d3e054b1fa75fd7f1b0ffa3883a)MIPI\_DSI\_GENERIC\_READ\_REQUEST\_0\_PARAM

| #define MIPI\_DSI\_GENERIC\_READ\_REQUEST\_0\_PARAM   0x04U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#gabff929d8285415c0d3edb95748bf2686)MIPI\_DSI\_GENERIC\_READ\_REQUEST\_1\_PARAM

| #define MIPI\_DSI\_GENERIC\_READ\_REQUEST\_1\_PARAM   0x14U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga9ea3c57a021879863097edc3f275ea60)MIPI\_DSI\_GENERIC\_READ\_REQUEST\_2\_PARAM

| #define MIPI\_DSI\_GENERIC\_READ\_REQUEST\_2\_PARAM   0x24U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga639170a23fa7b28e6bf3726c8d54ead0)MIPI\_DSI\_GENERIC\_SHORT\_WRITE\_0\_PARAM

| #define MIPI\_DSI\_GENERIC\_SHORT\_WRITE\_0\_PARAM   0x03U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#gaa0e596feb47e6eada0217fa7a81a0278)MIPI\_DSI\_GENERIC\_SHORT\_WRITE\_1\_PARAM

| #define MIPI\_DSI\_GENERIC\_SHORT\_WRITE\_1\_PARAM   0x13U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#gaea2acb4489552a159a19278018122ce6)MIPI\_DSI\_GENERIC\_SHORT\_WRITE\_2\_PARAM

| #define MIPI\_DSI\_GENERIC\_SHORT\_WRITE\_2\_PARAM   0x23U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#gaa8cc494ce41880ec765701ee4beffe97)MIPI\_DSI\_H\_SYNC\_END

| #define MIPI\_DSI\_H\_SYNC\_END   0x31U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga6852f3d6bfb77101d64b10a2b48a91c5)MIPI\_DSI\_H\_SYNC\_START

| #define MIPI\_DSI\_H\_SYNC\_START   0x21U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga933521f6a7f2f8ebad1569a0e8320d41)MIPI\_DSI\_LOOSELY\_PACKED\_PIXEL\_STREAM\_YCBCR20

| #define MIPI\_DSI\_LOOSELY\_PACKED\_PIXEL\_STREAM\_YCBCR20   0x0CU |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#gabcd142889c213edb8a7e7e95bb138b08)MIPI\_DSI\_NULL\_PACKET

| #define MIPI\_DSI\_NULL\_PACKET   0x09U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga93db7cc5b15cd5683ba8b9358731e151)MIPI\_DSI\_PACKED\_PIXEL\_STREAM\_16

| #define MIPI\_DSI\_PACKED\_PIXEL\_STREAM\_16   0x0EU |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga3bf54b5ef30c94f863c353ac8a68f0f0)MIPI\_DSI\_PACKED\_PIXEL\_STREAM\_18

| #define MIPI\_DSI\_PACKED\_PIXEL\_STREAM\_18   0x1EU |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga0956384d8db5940cc6ffe3a4569a2fb2)MIPI\_DSI\_PACKED\_PIXEL\_STREAM\_24

| #define MIPI\_DSI\_PACKED\_PIXEL\_STREAM\_24   0x3EU |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga09da8d6976e18b7ac074f9e10cc8c52f)MIPI\_DSI\_PACKED\_PIXEL\_STREAM\_30

| #define MIPI\_DSI\_PACKED\_PIXEL\_STREAM\_30   0x0DU |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga0015e0c7df4f3688e5567099f9d0ea11)MIPI\_DSI\_PACKED\_PIXEL\_STREAM\_36

| #define MIPI\_DSI\_PACKED\_PIXEL\_STREAM\_36   0x1DU |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga999976bf03f40c56ccb9272f99334cdf)MIPI\_DSI\_PACKED\_PIXEL\_STREAM\_YCBCR12

| #define MIPI\_DSI\_PACKED\_PIXEL\_STREAM\_YCBCR12   0x3DU |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga928d1364d635cb892f5992f7cdda7905)MIPI\_DSI\_PACKED\_PIXEL\_STREAM\_YCBCR16

| #define MIPI\_DSI\_PACKED\_PIXEL\_STREAM\_YCBCR16   0x2CU |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga858695ed8e1f5234d25f44b59a4f270d)MIPI\_DSI\_PACKED\_PIXEL\_STREAM\_YCBCR24

| #define MIPI\_DSI\_PACKED\_PIXEL\_STREAM\_YCBCR24   0x1CU |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#gaeee3817bcc554f3c04cb737e03649733)MIPI\_DSI\_PIXEL\_STREAM\_3BYTE\_18

| #define MIPI\_DSI\_PIXEL\_STREAM\_3BYTE\_18   0x2EU |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#gab07bcea365f9835c5df3c37d15f3073c)MIPI\_DSI\_SET\_MAXIMUM\_RETURN\_PACKET\_SIZE

| #define MIPI\_DSI\_SET\_MAXIMUM\_RETURN\_PACKET\_SIZE   0x37U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#gafac7d0f045d77fed0ff35f3a3503f6a5)MIPI\_DSI\_SHUTDOWN\_PERIPHERAL

| #define MIPI\_DSI\_SHUTDOWN\_PERIPHERAL   0x22U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#ga56292f7b60a0e7b55cd5118c1641c3ba)MIPI\_DSI\_TURN\_ON\_PERIPHERAL

| #define MIPI\_DSI\_TURN\_ON\_PERIPHERAL   0x32U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#gaf85ef5c73d29fec41460de8b752cef39)MIPI\_DSI\_V\_SYNC\_END

| #define MIPI\_DSI\_V\_SYNC\_END   0x11U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

## [◆ ](#gad58c27d600a73e38f33669a3ae743f01)MIPI\_DSI\_V\_SYNC\_START

| #define MIPI\_DSI\_V\_SYNC\_START   0x01U |
| --- |

`#include <[mipi_display.h](mipi__display_8h.md)>`

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
