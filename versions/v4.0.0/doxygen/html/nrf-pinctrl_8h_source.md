---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/nrf-pinctrl_8h_source.html
original_path: doxygen/html/nrf-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nrf-pinctrl.h

[Go to the documentation of this file.](nrf-pinctrl_8h.md)

1/\*

2 \* Copyright (c) 2021 Nordic Semiconductor ASA

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_NRF\_PINCTRL\_H\_

7#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_NRF\_PINCTRL\_H\_

8

9/\*

10 \* The whole nRF pin configuration information is encoded in a 32-bit bitfield

11 \* organized as follows:

12 \*

13 \* - 31..24: Pin function.

14 \* - 19-23: Reserved.

15 \* - 18: Associated peripheral belongs to GD FAST ACTIVE1 (nRF54H only)

16 \* - 17: Clockpin enable.

17 \* - 16: Pin inversion mode.

18 \* - 15: Pin low power mode.

19 \* - 14..11: Pin output drive configuration.

20 \* - 10..9: Pin pull configuration.

21 \* - 8..0: Pin number (combination of port and pin).

22 \*/

23

28

[ 30](nrf-pinctrl_8h.md#a10272aaefd0f103c15ae28ce8ef76987)#define NRF\_FUN\_POS 24U

[ 32](nrf-pinctrl_8h.md#ae3f5b1848b0c00547eff520f22ede922)#define NRF\_FUN\_MSK 0xFFU

[ 34](nrf-pinctrl_8h.md#a9203c68fb293d5eec889a8729b5f52b3)#define NRF\_GPD\_FAST\_ACTIVE1\_POS 18U

[ 36](nrf-pinctrl_8h.md#a1211c8c57f411a7676023c61cc986095)#define NRF\_GPD\_FAST\_ACTIVE1\_MSK 0x1U

[ 38](nrf-pinctrl_8h.md#a1ddd10f13ce7524c777f02a2d96ed727)#define NRF\_CLOCKPIN\_ENABLE\_POS 17U

[ 40](nrf-pinctrl_8h.md#af596f5bff44b420017fe9d0bb1260753)#define NRF\_CLOCKPIN\_ENABLE\_MSK 0x1U

[ 42](nrf-pinctrl_8h.md#aa13cd70c54db20407bfaef944ea10329)#define NRF\_INVERT\_POS 16U

[ 44](nrf-pinctrl_8h.md#a1a5cca24fa65f0ea64e8927e9d12ff43)#define NRF\_INVERT\_MSK 0x1U

[ 46](nrf-pinctrl_8h.md#a97dce1e8b63e4054f23c1daa0ddd6327)#define NRF\_LP\_POS 15U

[ 48](nrf-pinctrl_8h.md#a67b7d47eed25086ebbe5db508c85ff7b)#define NRF\_LP\_MSK 0x1U

[ 50](nrf-pinctrl_8h.md#ae8b94074f18659a2767e0f7f1aa1c73f)#define NRF\_DRIVE\_POS 11U

[ 52](nrf-pinctrl_8h.md#a86d4555acfb553f6bad1562743cf357c)#define NRF\_DRIVE\_MSK 0xFU

[ 54](nrf-pinctrl_8h.md#a0fac117bc7a2f45638ce462527cb8daa)#define NRF\_PULL\_POS 9U

[ 56](nrf-pinctrl_8h.md#a3900fd72d44feeefef9aa73c909a2396)#define NRF\_PULL\_MSK 0x3U

[ 58](nrf-pinctrl_8h.md#aa057ad8de2dea12959f51a293a929367)#define NRF\_PIN\_POS 0U

[ 60](nrf-pinctrl_8h.md#a8f60ab83a5325691eb0d976ae1f70295)#define NRF\_PIN\_MSK 0x1FFU

61

63

68

[ 70](nrf-pinctrl_8h.md#a9550ec0625d3e702c41d79cdf633bf9b)#define NRF\_FUN\_UART\_TX 0U

[ 72](nrf-pinctrl_8h.md#ad7865c58ddd2d7686482fa2f92a330f8)#define NRF\_FUN\_UART\_RX 1U

[ 74](nrf-pinctrl_8h.md#aa2ea1399ee3dff5019adf462b9cb09b8)#define NRF\_FUN\_UART\_RTS 2U

[ 76](nrf-pinctrl_8h.md#a595b5f913921466ec87c58657709c800)#define NRF\_FUN\_UART\_CTS 3U

[ 78](nrf-pinctrl_8h.md#a2594557c5e765d65ea7627c5c49e07d6)#define NRF\_FUN\_SPIM\_SCK 4U

[ 80](nrf-pinctrl_8h.md#a2e96ea48e6a9e707b76b846536a687cb)#define NRF\_FUN\_SPIM\_MOSI 5U

[ 82](nrf-pinctrl_8h.md#afca36f99d1c1a9e17e4949f18206490a)#define NRF\_FUN\_SPIM\_MISO 6U

[ 84](nrf-pinctrl_8h.md#a9906fedc9c9667be7a84c66443f01772)#define NRF\_FUN\_SPIS\_SCK 7U

[ 86](nrf-pinctrl_8h.md#a016ffb10db008be19f494e7098096109)#define NRF\_FUN\_SPIS\_MOSI 8U

[ 88](nrf-pinctrl_8h.md#aa480a4b96df9c4521d744de7d9a72e1f)#define NRF\_FUN\_SPIS\_MISO 9U

[ 90](nrf-pinctrl_8h.md#a6591844a0ce9f0297f917abb2f87c259)#define NRF\_FUN\_SPIS\_CSN 10U

[ 92](nrf-pinctrl_8h.md#aa26e18840b9cc780f35a1c237f24f8f8)#define NRF\_FUN\_TWIM\_SCL 11U

[ 94](nrf-pinctrl_8h.md#a7f0dcd38287a5e8c2e55145e43a57628)#define NRF\_FUN\_TWIM\_SDA 12U

[ 96](nrf-pinctrl_8h.md#aae874d5eb9da322f9766c9546c565db2)#define NRF\_FUN\_I2S\_SCK\_M 13U

[ 98](nrf-pinctrl_8h.md#aa791b4bf51162aff1f6cfbc374af826b)#define NRF\_FUN\_I2S\_SCK\_S 14U

[ 100](nrf-pinctrl_8h.md#a8aeef372eba5608f6fa06c3e592bfe69)#define NRF\_FUN\_I2S\_LRCK\_M 15U

[ 102](nrf-pinctrl_8h.md#aacf6b96aad472ee6423552c80936c375)#define NRF\_FUN\_I2S\_LRCK\_S 16U

[ 104](nrf-pinctrl_8h.md#ad943106dbd772562b2cca1d063c10456)#define NRF\_FUN\_I2S\_SDIN 17U

[ 106](nrf-pinctrl_8h.md#af2966d1e579895b18331480c42145f2f)#define NRF\_FUN\_I2S\_SDOUT 18U

[ 108](nrf-pinctrl_8h.md#a6de3f8d978d2aa864c12410ff3a78741)#define NRF\_FUN\_I2S\_MCK 19U

[ 110](nrf-pinctrl_8h.md#a5ceee799b932f1b71366bda816cde19a)#define NRF\_FUN\_PDM\_CLK 20U

[ 112](nrf-pinctrl_8h.md#af8f0c9a76b28fe19a5c4552386b6cd30)#define NRF\_FUN\_PDM\_DIN 21U

[ 114](nrf-pinctrl_8h.md#a9cf56eb616791c1bf79a15de6e11e270)#define NRF\_FUN\_PWM\_OUT0 22U

[ 116](nrf-pinctrl_8h.md#a9668fd12e95380431659e5edaa62cf65)#define NRF\_FUN\_PWM\_OUT1 23U

[ 118](nrf-pinctrl_8h.md#a4d9b8e2aba25457f1e688b71a8bcf235)#define NRF\_FUN\_PWM\_OUT2 24U

[ 120](nrf-pinctrl_8h.md#a79e863ca96b4e14c6eb0367b7b50bd32)#define NRF\_FUN\_PWM\_OUT3 25U

[ 122](nrf-pinctrl_8h.md#af07b0671c04b3318ad4f6e81f9b02f9b)#define NRF\_FUN\_QDEC\_A 26U

[ 124](nrf-pinctrl_8h.md#a3da455a7ac5e260ff25e867212b4b026)#define NRF\_FUN\_QDEC\_B 27U

[ 126](nrf-pinctrl_8h.md#a0b4431b76b7c264167fe48294cb5eb3d)#define NRF\_FUN\_QDEC\_LED 28U

[ 128](nrf-pinctrl_8h.md#a8504018d0dddd49c009ee8db7f6aa559)#define NRF\_FUN\_QSPI\_SCK 29U

[ 130](nrf-pinctrl_8h.md#a2ec92b450cc6f75121879950a7a2f750)#define NRF\_FUN\_QSPI\_CSN 30U

[ 132](nrf-pinctrl_8h.md#a97a03ba41e0a1bafe6d44868baf62b21)#define NRF\_FUN\_QSPI\_IO0 31U

[ 134](nrf-pinctrl_8h.md#a4a87c54c51d9ab5e602a62f9ec70e98e)#define NRF\_FUN\_QSPI\_IO1 32U

[ 136](nrf-pinctrl_8h.md#a0bd9c69689a0ec5c88eb4d50ff1c73dd)#define NRF\_FUN\_QSPI\_IO2 33U

[ 138](nrf-pinctrl_8h.md#aaf2c957da80884f0a8d442da64da8b92)#define NRF\_FUN\_QSPI\_IO3 34U

[ 140](nrf-pinctrl_8h.md#a9e02aa751912dd3e3ad3964bd2e92b1b)#define NRF\_FUN\_EXMIF\_CK 35U

[ 142](nrf-pinctrl_8h.md#afe37cd483f85609e7f82044995c7245d)#define NRF\_FUN\_EXMIF\_DQ0 36U

[ 144](nrf-pinctrl_8h.md#ab58883df980cf4e61b1d74a473a58563)#define NRF\_FUN\_EXMIF\_DQ1 37U

[ 146](nrf-pinctrl_8h.md#ad358c9ec0f07e70cfc11313c4f09073c)#define NRF\_FUN\_EXMIF\_DQ2 38U

[ 148](nrf-pinctrl_8h.md#ac7ef6d6a949d228bdaf5635ae5182262)#define NRF\_FUN\_EXMIF\_DQ3 39U

[ 150](nrf-pinctrl_8h.md#ab74f922a6687ddc1fce33b8f508064b7)#define NRF\_FUN\_EXMIF\_DQ4 40U

[ 152](nrf-pinctrl_8h.md#a144b60ce024fadb107e19de376f2077c)#define NRF\_FUN\_EXMIF\_DQ5 41U

[ 154](nrf-pinctrl_8h.md#a8eb7a3680c93054ed76d1d6603ee9425)#define NRF\_FUN\_EXMIF\_DQ6 42U

[ 156](nrf-pinctrl_8h.md#a8cc2db3d1d971145411645135a29bf18)#define NRF\_FUN\_EXMIF\_DQ7 43U

[ 158](nrf-pinctrl_8h.md#a25571f907b7d808c6d757c2b273287d3)#define NRF\_FUN\_EXMIF\_CS0 44U

[ 160](nrf-pinctrl_8h.md#aa80dee2db548ab0ba3de943046ff24af)#define NRF\_FUN\_EXMIF\_CS1 45U

[ 162](nrf-pinctrl_8h.md#a34338fa4c8ab9e606bdc00d8cfe288ef)#define NRF\_FUN\_CAN\_TX 46U

[ 164](nrf-pinctrl_8h.md#a55a2841880cd17f8d8a6ff5fb67ec71b)#define NRF\_FUN\_CAN\_RX 47U

165

167

172

[ 174](nrf-pinctrl_8h.md#a9a9ec0027e98f277a8ad72edc9783ca8)#define NRF\_DRIVE\_S0S1 0U

[ 176](nrf-pinctrl_8h.md#a76555393e7124f333e0ec19414c2a6d5)#define NRF\_DRIVE\_H0S1 1U

[ 178](nrf-pinctrl_8h.md#abc3f7122815fc04db4c4eede3cfd713c)#define NRF\_DRIVE\_S0H1 2U

[ 180](nrf-pinctrl_8h.md#a7f65712ab98608dbcdf438a57b651f4b)#define NRF\_DRIVE\_H0H1 3U

[ 182](nrf-pinctrl_8h.md#ac97de2448f9b56d04bfb07f57c86eee9)#define NRF\_DRIVE\_D0S1 4U

[ 184](nrf-pinctrl_8h.md#a74f65220ebf6c8633b7023191bed55e8)#define NRF\_DRIVE\_D0H1 5U

[ 186](nrf-pinctrl_8h.md#aa12e26bef363bd9953791445bd2132d8)#define NRF\_DRIVE\_S0D1 6U

[ 188](nrf-pinctrl_8h.md#ab83a7803e7f9155d31f9f3e4373de2c2)#define NRF\_DRIVE\_H0D1 7U

[ 190](nrf-pinctrl_8h.md#a164af8cb0a188d21664987deec25946d)#define NRF\_DRIVE\_E0E1 8U

191

193

199

[ 201](nrf-pinctrl_8h.md#ada4d270f356ec03b6686aeabdb71f860)#define NRF\_PULL\_NONE 0U

[ 203](nrf-pinctrl_8h.md#aca067a8a69d212ccacd9482953fc2893)#define NRF\_PULL\_DOWN 1U

[ 205](nrf-pinctrl_8h.md#a60062185ecdd8b8552ae00398213c7f7)#define NRF\_PULL\_UP 3U

206

208

213

[ 215](nrf-pinctrl_8h.md#aab29e9a98303f1d57c249362a4b062b0)#define NRF\_LP\_DISABLE 0U

[ 217](nrf-pinctrl_8h.md#a965ede26fa596ef7dd3ca62e0e9626a0)#define NRF\_LP\_ENABLE 1U

218

220

225

[ 227](nrf-pinctrl_8h.md#a1354873c8f0bcb226fc4d5fabb06b837)#define NRF\_PIN\_DISCONNECTED NRF\_PIN\_MSK

228

230

[ 238](nrf-pinctrl_8h.md#a43d0a0ad6e574456a2b69ab5354ccef4)#define NRF\_PSEL(fun, port, pin) \

239 ((((((port) \* 32U) + (pin)) & NRF\_PIN\_MSK) << NRF\_PIN\_POS) | \

240 ((NRF\_FUN\_ ## fun & NRF\_FUN\_MSK) << NRF\_FUN\_POS))

241

[ 250](nrf-pinctrl_8h.md#a2e414bdc5912c0e0abc349d5362520bd)#define NRF\_PSEL\_DISCONNECTED(fun) \

251 (NRF\_PIN\_DISCONNECTED | \

252 ((NRF\_FUN\_ ## fun & NRF\_FUN\_MSK) << NRF\_FUN\_POS))

253

254#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_NRF\_PINCTRL\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [nrf-pinctrl.h](nrf-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
