---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/mipi__display_8h_source.html
original_path: doxygen/html/mipi__display_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mipi\_display.h

[Go to the documentation of this file.](mipi__display_8h.md)

1/\*

2 \* Copyright 2023 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_DISPLAY\_MIPI\_DISPLAY\_H\_

13#define ZEPHYR\_INCLUDE\_DISPLAY\_MIPI\_DISPLAY\_H\_

14

21

22

23#ifdef \_\_cplusplus

24extern "C" {

25#endif

26

31

[ 32](group__mipi__interface.md#gadcaf06472d3e281e425bd2d71c5beaed)#define MIPI\_DCS\_NOP 0x00U

[ 33](group__mipi__interface.md#gab8c88ef2d316b783d5222a85d0e118ea)#define MIPI\_DCS\_SOFT\_RESET 0x01U

[ 34](group__mipi__interface.md#ga6d88c902f9d07c1fff0d1e92fe966fad)#define MIPI\_DCS\_GET\_COMPRESSION\_MODE 0x03U

[ 35](group__mipi__interface.md#ga94cb2e4ce1ae29871de780301d4d59d0)#define MIPI\_DCS\_GET\_DISPLAY\_ID 0x04U

[ 36](group__mipi__interface.md#ga5007b2e6e6e7750d13cb8421ff06d8e7)#define MIPI\_DCS\_GET\_RED\_CHANNEL 0x06U

[ 37](group__mipi__interface.md#gaa40f1c03dca04961a28dd19754212f06)#define MIPI\_DCS\_GET\_GREEN\_CHANNEL 0x07U

[ 38](group__mipi__interface.md#gaf1091bc7718eb7aa3a2c72c5c025ab4d)#define MIPI\_DCS\_GET\_BLUE\_CHANNEL 0x08U

[ 39](group__mipi__interface.md#gaca8b503fdca34456ca68ced074873424)#define MIPI\_DCS\_GET\_DISPLAY\_STATUS 0x09U

[ 40](group__mipi__interface.md#ga48669397e8ea5a7c6e0cb09ea9d4fd5c)#define MIPI\_DCS\_GET\_POWER\_MODE 0x0AU

[ 41](group__mipi__interface.md#ga9da041d715731d8d67caad967e5d6002)#define MIPI\_DCS\_GET\_ADDRESS\_MODE 0x0BU

[ 42](group__mipi__interface.md#gae7088fe2f1351d534262d111692a1bfa)#define MIPI\_DCS\_GET\_PIXEL\_FORMAT 0x0CU

[ 43](group__mipi__interface.md#gaf752f812f791e805fbfed0d3ab9b89de)#define MIPI\_DCS\_GET\_DISPLAY\_MODE 0x0DU

[ 44](group__mipi__interface.md#gaa80bc31f551b39eff6625e80c211f16a)#define MIPI\_DCS\_GET\_SIGNAL\_MODE 0x0EU

[ 45](group__mipi__interface.md#ga8ec1590be25764411567933943b77869)#define MIPI\_DCS\_GET\_DIAGNOSTIC\_RESULT 0x0FU

[ 46](group__mipi__interface.md#ga06f9b8e87b6f1f6f41a139db370f236b)#define MIPI\_DCS\_ENTER\_SLEEP\_MODE 0x10U

[ 47](group__mipi__interface.md#ga276231424603f027583ffd2a1bdd6089)#define MIPI\_DCS\_EXIT\_SLEEP\_MODE 0x11U

[ 48](group__mipi__interface.md#ga219bb0ba9e91812f4ab372adaa9afd07)#define MIPI\_DCS\_ENTER\_PARTIAL\_MODE 0x12U

[ 49](group__mipi__interface.md#gaedb3b5fa815593d3fa1ae247383d8a8e)#define MIPI\_DCS\_ENTER\_NORMAL\_MODE 0x13U

[ 50](group__mipi__interface.md#ga41a4fd226d8f86ba2efa34403b4033f8)#define MIPI\_DCS\_EXIT\_INVERT\_MODE 0x20U

[ 51](group__mipi__interface.md#gad1041d71940752f1c1121cf392a3b2d3)#define MIPI\_DCS\_ENTER\_INVERT\_MODE 0x21U

[ 52](group__mipi__interface.md#ga14771de93ba08dffabafffcedc85b54e)#define MIPI\_DCS\_SET\_GAMMA\_CURVE 0x26U

[ 53](group__mipi__interface.md#gaf50a5539c89552512ffcd04ece5b7fe0)#define MIPI\_DCS\_SET\_DISPLAY\_OFF 0x28U

[ 54](group__mipi__interface.md#gabdbee428ef6d48009a5795e384665c8f)#define MIPI\_DCS\_SET\_DISPLAY\_ON 0x29U

[ 55](group__mipi__interface.md#ga2d08791d990c2e4d9c6c9800ad2d8c1b)#define MIPI\_DCS\_SET\_COLUMN\_ADDRESS 0x2AU

[ 56](group__mipi__interface.md#ga63334f8e1458151197a35c7d5cf781a5)#define MIPI\_DCS\_SET\_PAGE\_ADDRESS 0x2BU

[ 57](group__mipi__interface.md#ga9a31b4772025e2046816057b74d2e7cd)#define MIPI\_DCS\_WRITE\_MEMORY\_START 0x2CU

[ 58](group__mipi__interface.md#ga6f94b4db07db5a287cd50ed87197a9c2)#define MIPI\_DCS\_WRITE\_LUT 0x2DU

[ 59](group__mipi__interface.md#ga860180f5477caadae3857b4c93f04281)#define MIPI\_DCS\_READ\_MEMORY\_START 0x2EU

[ 60](group__mipi__interface.md#ga18fe9e1cf30da71c18bebce1960095c3)#define MIPI\_DCS\_SET\_PARTIAL\_ROWS 0x30U

[ 61](group__mipi__interface.md#ga359a43a0bb277b8f09fa1120bb2c3b09)#define MIPI\_DCS\_SET\_PARTIAL\_COLUMNS 0x31U

[ 62](group__mipi__interface.md#ga36aa83afeed02df37cb2bb295915c92d)#define MIPI\_DCS\_SET\_SCROLL\_AREA 0x33U

[ 63](group__mipi__interface.md#gadcd4fd3ea6ccbb63ebecb290c00c660f)#define MIPI\_DCS\_SET\_TEAR\_OFF 0x34U

[ 64](group__mipi__interface.md#gad85387743db362579b788fd28ecd2fbf)#define MIPI\_DCS\_SET\_TEAR\_ON 0x35U

[ 65](group__mipi__interface.md#ga1d7e5a77666d13f4a8a435db202f4323)#define MIPI\_DCS\_SET\_ADDRESS\_MODE 0x36U

[ 66](group__mipi__interface.md#gaee29e37b0cb4b10920211048e0d95756)#define MIPI\_DCS\_SET\_SCROLL\_START 0x37U

[ 67](group__mipi__interface.md#gaf0a1f7ede08492751141cf52235808b3)#define MIPI\_DCS\_EXIT\_IDLE\_MODE 0x38U

[ 68](group__mipi__interface.md#ga7f1dfc0645ab456b38ac2caae783b709)#define MIPI\_DCS\_ENTER\_IDLE\_MODE 0x39U

[ 69](group__mipi__interface.md#ga1165d0835844eb0bd86fa6d30db7a84d)#define MIPI\_DCS\_SET\_PIXEL\_FORMAT 0x3AU

[ 70](group__mipi__interface.md#ga532122daccbd1370332fd9c26569c11f)#define MIPI\_DCS\_WRITE\_MEMORY\_CONTINUE 0x3CU

[ 71](group__mipi__interface.md#gaf9210d3033c2b09a7da608e9aeb88ad1)#define MIPI\_DCS\_SET\_3D\_CONTROL 0x3DU

[ 72](group__mipi__interface.md#ga6d3fcf5c050b45d8afe3af4ec98adadc)#define MIPI\_DCS\_READ\_MEMORY\_CONTINUE 0x3EU

[ 73](group__mipi__interface.md#gaace0882d961807760db2ed7693ab760a)#define MIPI\_DCS\_GET\_3D\_CONTROL 0x3FU

[ 74](group__mipi__interface.md#ga9597f72175b99376f7119b95cf425c1c)#define MIPI\_DCS\_SET\_VSYNC\_TIMING 0x40U

[ 75](group__mipi__interface.md#gaaac44d1367419dc395332712b0427458)#define MIPI\_DCS\_SET\_TEAR\_SCANLINE 0x44U

[ 76](group__mipi__interface.md#ga7933493853f9ef2dd28b31ea2fbb492f)#define MIPI\_DCS\_GET\_SCANLINE 0x45U

[ 77](group__mipi__interface.md#gac8dec8303a247b56a513628645d67f2b)#define MIPI\_DCS\_SET\_DISPLAY\_BRIGHTNESS 0x51U

[ 78](group__mipi__interface.md#ga4df917017e27912a343731b350e8d02e)#define MIPI\_DCS\_GET\_DISPLAY\_BRIGHTNESS 0x52U

[ 79](group__mipi__interface.md#gad47f873520b505e3463ad1f85d617787)#define MIPI\_DCS\_WRITE\_CONTROL\_DISPLAY 0x53U

[ 80](group__mipi__interface.md#ga9f83f0b2412084ab2ac3edd36b41fc11)#define MIPI\_DCS\_GET\_CONTROL\_DISPLAY 0x54U

[ 81](group__mipi__interface.md#ga2655d637a53b1b5e805ab3d69bc9fe9e)#define MIPI\_DCS\_WRITE\_POWER\_SAVE 0x55U

[ 82](group__mipi__interface.md#ga518ba3d308b6c453850e5168b26d1024)#define MIPI\_DCS\_GET\_POWER\_SAVE 0x56U

[ 83](group__mipi__interface.md#gab0d27051994aa70c8baf12a103080e80)#define MIPI\_DCS\_SET\_CABC\_MIN\_BRIGHTNESS 0x5EU

[ 84](group__mipi__interface.md#ga2d56066851a38acf38323cd2327820c4)#define MIPI\_DCS\_GET\_CABC\_MIN\_BRIGHTNESS 0x5FU

[ 85](group__mipi__interface.md#ga6cccd95a6bc9c007bb648b70d664c34d)#define MIPI\_DCS\_READ\_DDB\_START 0xA1U

[ 86](group__mipi__interface.md#ga26b4f0111aee93b8ad01448d7b4af368)#define MIPI\_DCS\_READ\_DDB\_CONTINUE 0xA8U

87

[ 88](group__mipi__interface.md#ga2772b5432484431573d092447c12e005)#define MIPI\_DCS\_PIXEL\_FORMAT\_24BIT 0x77

[ 89](group__mipi__interface.md#gab2d74d3cc0ce8036b57d5aec073b5b6b)#define MIPI\_DCS\_PIXEL\_FORMAT\_18BIT 0x66

[ 90](group__mipi__interface.md#ga171be8bd1a5551ffc129c14e0d829e61)#define MIPI\_DCS\_PIXEL\_FORMAT\_16BIT 0x55

[ 91](group__mipi__interface.md#ga77944b2fd7f59be6698bd414cbeedcac)#define MIPI\_DCS\_PIXEL\_FORMAT\_12BIT 0x33

[ 92](group__mipi__interface.md#gac3e18d2d9d4bcfb98d99518021bf98bd)#define MIPI\_DCS\_PIXEL\_FORMAT\_8BIT 0x22

[ 93](group__mipi__interface.md#ga5a14ff4ebc8e81b9bc92e87069ad7466)#define MIPI\_DCS\_PIXEL\_FORMAT\_3BIT 0x11

94

96

101

[ 102](group__mipi__interface.md#ga549bdf77bc40cc4a5cc81004b3f91775)#define MIPI\_DCS\_ADDRESS\_MODE\_MIRROR\_Y BIT(7)

[ 103](group__mipi__interface.md#gaa9c5f1e04806ef4dd672a6169136d07c)#define MIPI\_DCS\_ADDRESS\_MODE\_MIRROR\_X BIT(6)

[ 104](group__mipi__interface.md#gadfce4431c308f186479af4d15c83187b)#define MIPI\_DCS\_ADDRESS\_MODE\_SWAP\_XY BIT(5)

[ 105](group__mipi__interface.md#gad8591d77dafcb2d1ccc2ce971b012761)#define MIPI\_DCS\_ADDRESS\_MODE\_REFRESH\_BT BIT(4)

[ 106](group__mipi__interface.md#ga5320efc9a396b1cdfe89c5cfc87d8c11)#define MIPI\_DCS\_ADDRESS\_MODE\_BGR BIT(3)

[ 107](group__mipi__interface.md#gaa32acf97423f4491b27b2d9cb7d49a3c)#define MIPI\_DCS\_ADDRESS\_MODE\_LATCH\_RL BIT(2)

[ 108](group__mipi__interface.md#ga75df1e79cde793c01c47103bf683f3aa)#define MIPI\_DCS\_ADDRESS\_MODE\_FLIP\_X BIT(1)

[ 109](group__mipi__interface.md#ga72cf84630b55cd8dfe762eb84272692f)#define MIPI\_DCS\_ADDRESS\_MODE\_FLIP\_Y BIT(0)

110

112

117

[ 118](group__mipi__interface.md#gad58c27d600a73e38f33669a3ae743f01)#define MIPI\_DSI\_V\_SYNC\_START 0x01U

[ 119](group__mipi__interface.md#gaf85ef5c73d29fec41460de8b752cef39)#define MIPI\_DSI\_V\_SYNC\_END 0x11U

[ 120](group__mipi__interface.md#ga6852f3d6bfb77101d64b10a2b48a91c5)#define MIPI\_DSI\_H\_SYNC\_START 0x21U

[ 121](group__mipi__interface.md#gaa8cc494ce41880ec765701ee4beffe97)#define MIPI\_DSI\_H\_SYNC\_END 0x31U

[ 122](group__mipi__interface.md#gad713fb809d6012db370ef23601c81619)#define MIPI\_DSI\_COLOR\_MODE\_OFF 0x02U

[ 123](group__mipi__interface.md#ga1987975c9389ec9570c5ff05e3e1a9b1)#define MIPI\_DSI\_COLOR\_MODE\_ON 0x12U

[ 124](group__mipi__interface.md#gafac7d0f045d77fed0ff35f3a3503f6a5)#define MIPI\_DSI\_SHUTDOWN\_PERIPHERAL 0x22U

[ 125](group__mipi__interface.md#ga56292f7b60a0e7b55cd5118c1641c3ba)#define MIPI\_DSI\_TURN\_ON\_PERIPHERAL 0x32U

[ 126](group__mipi__interface.md#ga639170a23fa7b28e6bf3726c8d54ead0)#define MIPI\_DSI\_GENERIC\_SHORT\_WRITE\_0\_PARAM 0x03U

[ 127](group__mipi__interface.md#gaa0e596feb47e6eada0217fa7a81a0278)#define MIPI\_DSI\_GENERIC\_SHORT\_WRITE\_1\_PARAM 0x13U

[ 128](group__mipi__interface.md#gaea2acb4489552a159a19278018122ce6)#define MIPI\_DSI\_GENERIC\_SHORT\_WRITE\_2\_PARAM 0x23U

[ 129](group__mipi__interface.md#ga9d541d3e054b1fa75fd7f1b0ffa3883a)#define MIPI\_DSI\_GENERIC\_READ\_REQUEST\_0\_PARAM 0x04U

[ 130](group__mipi__interface.md#gabff929d8285415c0d3edb95748bf2686)#define MIPI\_DSI\_GENERIC\_READ\_REQUEST\_1\_PARAM 0x14U

[ 131](group__mipi__interface.md#ga9ea3c57a021879863097edc3f275ea60)#define MIPI\_DSI\_GENERIC\_READ\_REQUEST\_2\_PARAM 0x24U

[ 132](group__mipi__interface.md#ga51191c76ceca6f0e79cdb4f0e58013a3)#define MIPI\_DSI\_DCS\_SHORT\_WRITE 0x05U

[ 133](group__mipi__interface.md#ga5e0e1bf73a04668617e46cb0392bac8d)#define MIPI\_DSI\_DCS\_SHORT\_WRITE\_PARAM 0x15U

[ 134](group__mipi__interface.md#ga60acd68f9c3271b2cd306f6bb5e4af94)#define MIPI\_DSI\_DCS\_READ 0x06U

[ 135](group__mipi__interface.md#gab07bcea365f9835c5df3c37d15f3073c)#define MIPI\_DSI\_SET\_MAXIMUM\_RETURN\_PACKET\_SIZE 0x37U

[ 136](group__mipi__interface.md#ga575957d9fd4de559cd938b332f1eff05)#define MIPI\_DSI\_END\_OF\_TRANSMISSION 0x08U

[ 137](group__mipi__interface.md#gabcd142889c213edb8a7e7e95bb138b08)#define MIPI\_DSI\_NULL\_PACKET 0x09U

[ 138](group__mipi__interface.md#ga66550282423b364aed89c6ed2c202329)#define MIPI\_DSI\_BLANKING\_PACKET 0x19U

[ 139](group__mipi__interface.md#gadb6e6683462c4b8eaeda3a77b86f3e1d)#define MIPI\_DSI\_GENERIC\_LONG\_WRITE 0x29U

[ 140](group__mipi__interface.md#ga141eda8b32761dc7a275524c04e45535)#define MIPI\_DSI\_DCS\_LONG\_WRITE 0x39U

[ 141](group__mipi__interface.md#ga933521f6a7f2f8ebad1569a0e8320d41)#define MIPI\_DSI\_LOOSELY\_PACKED\_PIXEL\_STREAM\_YCBCR20 0x0CU

[ 142](group__mipi__interface.md#ga858695ed8e1f5234d25f44b59a4f270d)#define MIPI\_DSI\_PACKED\_PIXEL\_STREAM\_YCBCR24 0x1CU

[ 143](group__mipi__interface.md#ga928d1364d635cb892f5992f7cdda7905)#define MIPI\_DSI\_PACKED\_PIXEL\_STREAM\_YCBCR16 0x2CU

[ 144](group__mipi__interface.md#ga09da8d6976e18b7ac074f9e10cc8c52f)#define MIPI\_DSI\_PACKED\_PIXEL\_STREAM\_30 0x0DU

[ 145](group__mipi__interface.md#ga0015e0c7df4f3688e5567099f9d0ea11)#define MIPI\_DSI\_PACKED\_PIXEL\_STREAM\_36 0x1DU

[ 146](group__mipi__interface.md#ga999976bf03f40c56ccb9272f99334cdf)#define MIPI\_DSI\_PACKED\_PIXEL\_STREAM\_YCBCR12 0x3DU

[ 147](group__mipi__interface.md#ga93db7cc5b15cd5683ba8b9358731e151)#define MIPI\_DSI\_PACKED\_PIXEL\_STREAM\_16 0x0EU

[ 148](group__mipi__interface.md#ga3bf54b5ef30c94f863c353ac8a68f0f0)#define MIPI\_DSI\_PACKED\_PIXEL\_STREAM\_18 0x1EU

[ 149](group__mipi__interface.md#gaeee3817bcc554f3c04cb737e03649733)#define MIPI\_DSI\_PIXEL\_STREAM\_3BYTE\_18 0x2EU

[ 150](group__mipi__interface.md#ga0956384d8db5940cc6ffe3a4569a2fb2)#define MIPI\_DSI\_PACKED\_PIXEL\_STREAM\_24 0x3EU

151

153

154

155#ifdef \_\_cplusplus

156}

157#endif

158

162

163#endif /\* ZEPHYR\_INCLUDE\_DISPLAY\_MIPI\_DISPLAY\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [display](dir_dbe0bbdb2da2eed929c1e8ee8e4a99ef.md)
- [mipi\_display.h](mipi__display_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
