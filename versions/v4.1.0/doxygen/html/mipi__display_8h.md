---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/mipi__display_8h.html
original_path: doxygen/html/mipi__display_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mipi\_display.h File Reference

Display definitions for MIPI devices.
[More...](#details)

[Go to the source code of this file.](mipi__display_8h_source.md)

| Macros | |
| --- | --- |
| MIPI-DSI DCS (Display Command Set) | |
| #define | [MIPI\_DCS\_NOP](group__mipi__interface.md#gadcaf06472d3e281e425bd2d71c5beaed)   0x00U |
| #define | [MIPI\_DCS\_SOFT\_RESET](group__mipi__interface.md#gab8c88ef2d316b783d5222a85d0e118ea)   0x01U |
| #define | [MIPI\_DCS\_GET\_COMPRESSION\_MODE](group__mipi__interface.md#ga6d88c902f9d07c1fff0d1e92fe966fad)   0x03U |
| #define | [MIPI\_DCS\_GET\_DISPLAY\_ID](group__mipi__interface.md#ga94cb2e4ce1ae29871de780301d4d59d0)   0x04U |
| #define | [MIPI\_DCS\_GET\_RED\_CHANNEL](group__mipi__interface.md#ga5007b2e6e6e7750d13cb8421ff06d8e7)   0x06U |
| #define | [MIPI\_DCS\_GET\_GREEN\_CHANNEL](group__mipi__interface.md#gaa40f1c03dca04961a28dd19754212f06)   0x07U |
| #define | [MIPI\_DCS\_GET\_BLUE\_CHANNEL](group__mipi__interface.md#gaf1091bc7718eb7aa3a2c72c5c025ab4d)   0x08U |
| #define | [MIPI\_DCS\_GET\_DISPLAY\_STATUS](group__mipi__interface.md#gaca8b503fdca34456ca68ced074873424)   0x09U |
| #define | [MIPI\_DCS\_GET\_POWER\_MODE](group__mipi__interface.md#ga48669397e8ea5a7c6e0cb09ea9d4fd5c)   0x0AU |
| #define | [MIPI\_DCS\_GET\_ADDRESS\_MODE](group__mipi__interface.md#ga9da041d715731d8d67caad967e5d6002)   0x0BU |
| #define | [MIPI\_DCS\_GET\_PIXEL\_FORMAT](group__mipi__interface.md#gae7088fe2f1351d534262d111692a1bfa)   0x0CU |
| #define | [MIPI\_DCS\_GET\_DISPLAY\_MODE](group__mipi__interface.md#gaf752f812f791e805fbfed0d3ab9b89de)   0x0DU |
| #define | [MIPI\_DCS\_GET\_SIGNAL\_MODE](group__mipi__interface.md#gaa80bc31f551b39eff6625e80c211f16a)   0x0EU |
| #define | [MIPI\_DCS\_GET\_DIAGNOSTIC\_RESULT](group__mipi__interface.md#ga8ec1590be25764411567933943b77869)   0x0FU |
| #define | [MIPI\_DCS\_ENTER\_SLEEP\_MODE](group__mipi__interface.md#ga06f9b8e87b6f1f6f41a139db370f236b)   0x10U |
| #define | [MIPI\_DCS\_EXIT\_SLEEP\_MODE](group__mipi__interface.md#ga276231424603f027583ffd2a1bdd6089)   0x11U |
| #define | [MIPI\_DCS\_ENTER\_PARTIAL\_MODE](group__mipi__interface.md#ga219bb0ba9e91812f4ab372adaa9afd07)   0x12U |
| #define | [MIPI\_DCS\_ENTER\_NORMAL\_MODE](group__mipi__interface.md#gaedb3b5fa815593d3fa1ae247383d8a8e)   0x13U |
| #define | [MIPI\_DCS\_EXIT\_INVERT\_MODE](group__mipi__interface.md#ga41a4fd226d8f86ba2efa34403b4033f8)   0x20U |
| #define | [MIPI\_DCS\_ENTER\_INVERT\_MODE](group__mipi__interface.md#gad1041d71940752f1c1121cf392a3b2d3)   0x21U |
| #define | [MIPI\_DCS\_SET\_GAMMA\_CURVE](group__mipi__interface.md#ga14771de93ba08dffabafffcedc85b54e)   0x26U |
| #define | [MIPI\_DCS\_SET\_DISPLAY\_OFF](group__mipi__interface.md#gaf50a5539c89552512ffcd04ece5b7fe0)   0x28U |
| #define | [MIPI\_DCS\_SET\_DISPLAY\_ON](group__mipi__interface.md#gabdbee428ef6d48009a5795e384665c8f)   0x29U |
| #define | [MIPI\_DCS\_SET\_COLUMN\_ADDRESS](group__mipi__interface.md#ga2d08791d990c2e4d9c6c9800ad2d8c1b)   0x2AU |
| #define | [MIPI\_DCS\_SET\_PAGE\_ADDRESS](group__mipi__interface.md#ga63334f8e1458151197a35c7d5cf781a5)   0x2BU |
| #define | [MIPI\_DCS\_WRITE\_MEMORY\_START](group__mipi__interface.md#ga9a31b4772025e2046816057b74d2e7cd)   0x2CU |
| #define | [MIPI\_DCS\_WRITE\_LUT](group__mipi__interface.md#ga6f94b4db07db5a287cd50ed87197a9c2)   0x2DU |
| #define | [MIPI\_DCS\_READ\_MEMORY\_START](group__mipi__interface.md#ga860180f5477caadae3857b4c93f04281)   0x2EU |
| #define | [MIPI\_DCS\_SET\_PARTIAL\_ROWS](group__mipi__interface.md#ga18fe9e1cf30da71c18bebce1960095c3)   0x30U |
| #define | [MIPI\_DCS\_SET\_PARTIAL\_COLUMNS](group__mipi__interface.md#ga359a43a0bb277b8f09fa1120bb2c3b09)   0x31U |
| #define | [MIPI\_DCS\_SET\_SCROLL\_AREA](group__mipi__interface.md#ga36aa83afeed02df37cb2bb295915c92d)   0x33U |
| #define | [MIPI\_DCS\_SET\_TEAR\_OFF](group__mipi__interface.md#gadcd4fd3ea6ccbb63ebecb290c00c660f)   0x34U |
| #define | [MIPI\_DCS\_SET\_TEAR\_ON](group__mipi__interface.md#gad85387743db362579b788fd28ecd2fbf)   0x35U |
| #define | [MIPI\_DCS\_SET\_ADDRESS\_MODE](group__mipi__interface.md#ga1d7e5a77666d13f4a8a435db202f4323)   0x36U |
| #define | [MIPI\_DCS\_SET\_SCROLL\_START](group__mipi__interface.md#gaee29e37b0cb4b10920211048e0d95756)   0x37U |
| #define | [MIPI\_DCS\_EXIT\_IDLE\_MODE](group__mipi__interface.md#gaf0a1f7ede08492751141cf52235808b3)   0x38U |
| #define | [MIPI\_DCS\_ENTER\_IDLE\_MODE](group__mipi__interface.md#ga7f1dfc0645ab456b38ac2caae783b709)   0x39U |
| #define | [MIPI\_DCS\_SET\_PIXEL\_FORMAT](group__mipi__interface.md#ga1165d0835844eb0bd86fa6d30db7a84d)   0x3AU |
| #define | [MIPI\_DCS\_WRITE\_MEMORY\_CONTINUE](group__mipi__interface.md#ga532122daccbd1370332fd9c26569c11f)   0x3CU |
| #define | [MIPI\_DCS\_SET\_3D\_CONTROL](group__mipi__interface.md#gaf9210d3033c2b09a7da608e9aeb88ad1)   0x3DU |
| #define | [MIPI\_DCS\_READ\_MEMORY\_CONTINUE](group__mipi__interface.md#ga6d3fcf5c050b45d8afe3af4ec98adadc)   0x3EU |
| #define | [MIPI\_DCS\_GET\_3D\_CONTROL](group__mipi__interface.md#gaace0882d961807760db2ed7693ab760a)   0x3FU |
| #define | [MIPI\_DCS\_SET\_VSYNC\_TIMING](group__mipi__interface.md#ga9597f72175b99376f7119b95cf425c1c)   0x40U |
| #define | [MIPI\_DCS\_SET\_TEAR\_SCANLINE](group__mipi__interface.md#gaaac44d1367419dc395332712b0427458)   0x44U |
| #define | [MIPI\_DCS\_GET\_SCANLINE](group__mipi__interface.md#ga7933493853f9ef2dd28b31ea2fbb492f)   0x45U |
| #define | [MIPI\_DCS\_SET\_DISPLAY\_BRIGHTNESS](group__mipi__interface.md#gac8dec8303a247b56a513628645d67f2b)   0x51U |
| #define | [MIPI\_DCS\_GET\_DISPLAY\_BRIGHTNESS](group__mipi__interface.md#ga4df917017e27912a343731b350e8d02e)   0x52U |
| #define | [MIPI\_DCS\_WRITE\_CONTROL\_DISPLAY](group__mipi__interface.md#gad47f873520b505e3463ad1f85d617787)   0x53U |
| #define | [MIPI\_DCS\_GET\_CONTROL\_DISPLAY](group__mipi__interface.md#ga9f83f0b2412084ab2ac3edd36b41fc11)   0x54U |
| #define | [MIPI\_DCS\_WRITE\_POWER\_SAVE](group__mipi__interface.md#ga2655d637a53b1b5e805ab3d69bc9fe9e)   0x55U |
| #define | [MIPI\_DCS\_GET\_POWER\_SAVE](group__mipi__interface.md#ga518ba3d308b6c453850e5168b26d1024)   0x56U |
| #define | [MIPI\_DCS\_SET\_CABC\_MIN\_BRIGHTNESS](group__mipi__interface.md#gab0d27051994aa70c8baf12a103080e80)   0x5EU |
| #define | [MIPI\_DCS\_GET\_CABC\_MIN\_BRIGHTNESS](group__mipi__interface.md#ga2d56066851a38acf38323cd2327820c4)   0x5FU |
| #define | [MIPI\_DCS\_READ\_DDB\_START](group__mipi__interface.md#ga6cccd95a6bc9c007bb648b70d664c34d)   0xA1U |
| #define | [MIPI\_DCS\_READ\_DDB\_CONTINUE](group__mipi__interface.md#ga26b4f0111aee93b8ad01448d7b4af368)   0xA8U |
| #define | [MIPI\_DCS\_PIXEL\_FORMAT\_24BIT](group__mipi__interface.md#ga2772b5432484431573d092447c12e005)   0x77 |
| #define | [MIPI\_DCS\_PIXEL\_FORMAT\_18BIT](group__mipi__interface.md#gab2d74d3cc0ce8036b57d5aec073b5b6b)   0x66 |
| #define | [MIPI\_DCS\_PIXEL\_FORMAT\_16BIT](group__mipi__interface.md#ga171be8bd1a5551ffc129c14e0d829e61)   0x55 |
| #define | [MIPI\_DCS\_PIXEL\_FORMAT\_12BIT](group__mipi__interface.md#ga77944b2fd7f59be6698bd414cbeedcac)   0x33 |
| #define | [MIPI\_DCS\_PIXEL\_FORMAT\_8BIT](group__mipi__interface.md#gac3e18d2d9d4bcfb98d99518021bf98bd)   0x22 |
| #define | [MIPI\_DCS\_PIXEL\_FORMAT\_3BIT](group__mipi__interface.md#ga5a14ff4ebc8e81b9bc92e87069ad7466)   0x11 |
| MIPI-DSI Address mode register fields. | |
| #define | [MIPI\_DCS\_ADDRESS\_MODE\_MIRROR\_Y](group__mipi__interface.md#ga549bdf77bc40cc4a5cc81004b3f91775)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| #define | [MIPI\_DCS\_ADDRESS\_MODE\_MIRROR\_X](group__mipi__interface.md#gaa9c5f1e04806ef4dd672a6169136d07c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| #define | [MIPI\_DCS\_ADDRESS\_MODE\_SWAP\_XY](group__mipi__interface.md#gadfce4431c308f186479af4d15c83187b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| #define | [MIPI\_DCS\_ADDRESS\_MODE\_REFRESH\_BT](group__mipi__interface.md#gad8591d77dafcb2d1ccc2ce971b012761)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| #define | [MIPI\_DCS\_ADDRESS\_MODE\_BGR](group__mipi__interface.md#ga5320efc9a396b1cdfe89c5cfc87d8c11)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [MIPI\_DCS\_ADDRESS\_MODE\_LATCH\_RL](group__mipi__interface.md#gaa32acf97423f4491b27b2d9cb7d49a3c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [MIPI\_DCS\_ADDRESS\_MODE\_FLIP\_X](group__mipi__interface.md#ga75df1e79cde793c01c47103bf683f3aa)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [MIPI\_DCS\_ADDRESS\_MODE\_FLIP\_Y](group__mipi__interface.md#ga72cf84630b55cd8dfe762eb84272692f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| MIPI-DSI Processor-to-Peripheral transaction types. | |
| #define | [MIPI\_DSI\_V\_SYNC\_START](group__mipi__interface.md#gad58c27d600a73e38f33669a3ae743f01)   0x01U |
| #define | [MIPI\_DSI\_V\_SYNC\_END](group__mipi__interface.md#gaf85ef5c73d29fec41460de8b752cef39)   0x11U |
| #define | [MIPI\_DSI\_H\_SYNC\_START](group__mipi__interface.md#ga6852f3d6bfb77101d64b10a2b48a91c5)   0x21U |
| #define | [MIPI\_DSI\_H\_SYNC\_END](group__mipi__interface.md#gaa8cc494ce41880ec765701ee4beffe97)   0x31U |
| #define | [MIPI\_DSI\_COLOR\_MODE\_OFF](group__mipi__interface.md#gad713fb809d6012db370ef23601c81619)   0x02U |
| #define | [MIPI\_DSI\_COLOR\_MODE\_ON](group__mipi__interface.md#ga1987975c9389ec9570c5ff05e3e1a9b1)   0x12U |
| #define | [MIPI\_DSI\_SHUTDOWN\_PERIPHERAL](group__mipi__interface.md#gafac7d0f045d77fed0ff35f3a3503f6a5)   0x22U |
| #define | [MIPI\_DSI\_TURN\_ON\_PERIPHERAL](group__mipi__interface.md#ga56292f7b60a0e7b55cd5118c1641c3ba)   0x32U |
| #define | [MIPI\_DSI\_GENERIC\_SHORT\_WRITE\_0\_PARAM](group__mipi__interface.md#ga639170a23fa7b28e6bf3726c8d54ead0)   0x03U |
| #define | [MIPI\_DSI\_GENERIC\_SHORT\_WRITE\_1\_PARAM](group__mipi__interface.md#gaa0e596feb47e6eada0217fa7a81a0278)   0x13U |
| #define | [MIPI\_DSI\_GENERIC\_SHORT\_WRITE\_2\_PARAM](group__mipi__interface.md#gaea2acb4489552a159a19278018122ce6)   0x23U |
| #define | [MIPI\_DSI\_GENERIC\_READ\_REQUEST\_0\_PARAM](group__mipi__interface.md#ga9d541d3e054b1fa75fd7f1b0ffa3883a)   0x04U |
| #define | [MIPI\_DSI\_GENERIC\_READ\_REQUEST\_1\_PARAM](group__mipi__interface.md#gabff929d8285415c0d3edb95748bf2686)   0x14U |
| #define | [MIPI\_DSI\_GENERIC\_READ\_REQUEST\_2\_PARAM](group__mipi__interface.md#ga9ea3c57a021879863097edc3f275ea60)   0x24U |
| #define | [MIPI\_DSI\_DCS\_SHORT\_WRITE](group__mipi__interface.md#ga51191c76ceca6f0e79cdb4f0e58013a3)   0x05U |
| #define | [MIPI\_DSI\_DCS\_SHORT\_WRITE\_PARAM](group__mipi__interface.md#ga5e0e1bf73a04668617e46cb0392bac8d)   0x15U |
| #define | [MIPI\_DSI\_DCS\_READ](group__mipi__interface.md#ga60acd68f9c3271b2cd306f6bb5e4af94)   0x06U |
| #define | [MIPI\_DSI\_SET\_MAXIMUM\_RETURN\_PACKET\_SIZE](group__mipi__interface.md#gab07bcea365f9835c5df3c37d15f3073c)   0x37U |
| #define | [MIPI\_DSI\_END\_OF\_TRANSMISSION](group__mipi__interface.md#ga575957d9fd4de559cd938b332f1eff05)   0x08U |
| #define | [MIPI\_DSI\_NULL\_PACKET](group__mipi__interface.md#gabcd142889c213edb8a7e7e95bb138b08)   0x09U |
| #define | [MIPI\_DSI\_BLANKING\_PACKET](group__mipi__interface.md#ga66550282423b364aed89c6ed2c202329)   0x19U |
| #define | [MIPI\_DSI\_GENERIC\_LONG\_WRITE](group__mipi__interface.md#gadb6e6683462c4b8eaeda3a77b86f3e1d)   0x29U |
| #define | [MIPI\_DSI\_DCS\_LONG\_WRITE](group__mipi__interface.md#ga141eda8b32761dc7a275524c04e45535)   0x39U |
| #define | [MIPI\_DSI\_LOOSELY\_PACKED\_PIXEL\_STREAM\_YCBCR20](group__mipi__interface.md#ga933521f6a7f2f8ebad1569a0e8320d41)   0x0CU |
| #define | [MIPI\_DSI\_PACKED\_PIXEL\_STREAM\_YCBCR24](group__mipi__interface.md#ga858695ed8e1f5234d25f44b59a4f270d)   0x1CU |
| #define | [MIPI\_DSI\_PACKED\_PIXEL\_STREAM\_YCBCR16](group__mipi__interface.md#ga928d1364d635cb892f5992f7cdda7905)   0x2CU |
| #define | [MIPI\_DSI\_PACKED\_PIXEL\_STREAM\_30](group__mipi__interface.md#ga09da8d6976e18b7ac074f9e10cc8c52f)   0x0DU |
| #define | [MIPI\_DSI\_PACKED\_PIXEL\_STREAM\_36](group__mipi__interface.md#ga0015e0c7df4f3688e5567099f9d0ea11)   0x1DU |
| #define | [MIPI\_DSI\_PACKED\_PIXEL\_STREAM\_YCBCR12](group__mipi__interface.md#ga999976bf03f40c56ccb9272f99334cdf)   0x3DU |
| #define | [MIPI\_DSI\_PACKED\_PIXEL\_STREAM\_16](group__mipi__interface.md#ga93db7cc5b15cd5683ba8b9358731e151)   0x0EU |
| #define | [MIPI\_DSI\_PACKED\_PIXEL\_STREAM\_18](group__mipi__interface.md#ga3bf54b5ef30c94f863c353ac8a68f0f0)   0x1EU |
| #define | [MIPI\_DSI\_PIXEL\_STREAM\_3BYTE\_18](group__mipi__interface.md#gaeee3817bcc554f3c04cb737e03649733)   0x2EU |
| #define | [MIPI\_DSI\_PACKED\_PIXEL\_STREAM\_24](group__mipi__interface.md#ga0956384d8db5940cc6ffe3a4569a2fb2)   0x3EU |

## Detailed Description

Display definitions for MIPI devices.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [display](dir_dbe0bbdb2da2eed929c1e8ee8e4a99ef.md)
- [mipi\_display.h](mipi__display_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
