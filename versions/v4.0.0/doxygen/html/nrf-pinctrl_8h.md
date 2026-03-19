---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/nrf-pinctrl_8h.html
original_path: doxygen/html/nrf-pinctrl_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nrf-pinctrl.h File Reference

[Go to the source code of this file.](nrf-pinctrl_8h_source.md)

| Macros | |
| --- | --- |
| #define | [NRF\_PSEL](#a43d0a0ad6e574456a2b69ab5354ccef4)(fun, port, pin) |
|  | Utility macro to build nRF psels property entry. |
| #define | [NRF\_PSEL\_DISCONNECTED](#a2e414bdc5912c0e0abc349d5362520bd)(fun) |
|  | Utility macro to build nRF psels property entry when a pin is disconnected. |
| nRF pin configuration bit field positions and masks. | |
| #define | [NRF\_FUN\_POS](#a10272aaefd0f103c15ae28ce8ef76987)   24U |
|  | Position of the function field. |
| #define | [NRF\_FUN\_MSK](#ae3f5b1848b0c00547eff520f22ede922)   0xFFU |
|  | Mask for the function field. |
| #define | [NRF\_GPD\_FAST\_ACTIVE1\_POS](#a9203c68fb293d5eec889a8729b5f52b3)   18U |
|  | Position of the GPD FAST ACTIVE1. |
| #define | [NRF\_GPD\_FAST\_ACTIVE1\_MSK](#a1211c8c57f411a7676023c61cc986095)   0x1U |
|  | Mask for the GPD FAST ACTIVE1. |
| #define | [NRF\_CLOCKPIN\_ENABLE\_POS](#a1ddd10f13ce7524c777f02a2d96ed727)   17U |
|  | Position of the clockpin enable field. |
| #define | [NRF\_CLOCKPIN\_ENABLE\_MSK](#af596f5bff44b420017fe9d0bb1260753)   0x1U |
|  | Mask for the clockpin enable field. |
| #define | [NRF\_INVERT\_POS](#aa13cd70c54db20407bfaef944ea10329)   16U |
|  | Position of the invert field. |
| #define | [NRF\_INVERT\_MSK](#a1a5cca24fa65f0ea64e8927e9d12ff43)   0x1U |
|  | Mask for the invert field. |
| #define | [NRF\_LP\_POS](#a97dce1e8b63e4054f23c1daa0ddd6327)   15U |
|  | Position of the low power field. |
| #define | [NRF\_LP\_MSK](#a67b7d47eed25086ebbe5db508c85ff7b)   0x1U |
|  | Mask for the low power field. |
| #define | [NRF\_DRIVE\_POS](#ae8b94074f18659a2767e0f7f1aa1c73f)   11U |
|  | Position of the drive configuration field. |
| #define | [NRF\_DRIVE\_MSK](#a86d4555acfb553f6bad1562743cf357c)   0xFU |
|  | Mask for the drive configuration field. |
| #define | [NRF\_PULL\_POS](#a0fac117bc7a2f45638ce462527cb8daa)   9U |
|  | Position of the pull configuration field. |
| #define | [NRF\_PULL\_MSK](#a3900fd72d44feeefef9aa73c909a2396)   0x3U |
|  | Mask for the pull configuration field. |
| #define | [NRF\_PIN\_POS](#aa057ad8de2dea12959f51a293a929367)   0U |
|  | Position of the pin field. |
| #define | [NRF\_PIN\_MSK](#a8f60ab83a5325691eb0d976ae1f70295)   0x1FFU |
|  | Mask for the pin field. |
| nRF pinctrl pin functions. | |
| #define | [NRF\_FUN\_UART\_TX](#a9550ec0625d3e702c41d79cdf633bf9b)   0U |
|  | UART TX. |
| #define | [NRF\_FUN\_UART\_RX](#ad7865c58ddd2d7686482fa2f92a330f8)   1U |
|  | UART RX. |
| #define | [NRF\_FUN\_UART\_RTS](#aa2ea1399ee3dff5019adf462b9cb09b8)   2U |
|  | UART RTS. |
| #define | [NRF\_FUN\_UART\_CTS](#a595b5f913921466ec87c58657709c800)   3U |
|  | UART CTS. |
| #define | [NRF\_FUN\_SPIM\_SCK](#a2594557c5e765d65ea7627c5c49e07d6)   4U |
|  | SPI master SCK. |
| #define | [NRF\_FUN\_SPIM\_MOSI](#a2e96ea48e6a9e707b76b846536a687cb)   5U |
|  | SPI master MOSI. |
| #define | [NRF\_FUN\_SPIM\_MISO](#afca36f99d1c1a9e17e4949f18206490a)   6U |
|  | SPI master MISO. |
| #define | [NRF\_FUN\_SPIS\_SCK](#a9906fedc9c9667be7a84c66443f01772)   7U |
|  | SPI slave SCK. |
| #define | [NRF\_FUN\_SPIS\_MOSI](#a016ffb10db008be19f494e7098096109)   8U |
|  | SPI slave MOSI. |
| #define | [NRF\_FUN\_SPIS\_MISO](#aa480a4b96df9c4521d744de7d9a72e1f)   9U |
|  | SPI slave MISO. |
| #define | [NRF\_FUN\_SPIS\_CSN](#a6591844a0ce9f0297f917abb2f87c259)   10U |
|  | SPI slave CSN. |
| #define | [NRF\_FUN\_TWIM\_SCL](#aa26e18840b9cc780f35a1c237f24f8f8)   11U |
|  | TWI master SCL. |
| #define | [NRF\_FUN\_TWIM\_SDA](#a7f0dcd38287a5e8c2e55145e43a57628)   12U |
|  | TWI master SDA. |
| #define | [NRF\_FUN\_I2S\_SCK\_M](#aae874d5eb9da322f9766c9546c565db2)   13U |
|  | I2S SCK in master mode. |
| #define | [NRF\_FUN\_I2S\_SCK\_S](#aa791b4bf51162aff1f6cfbc374af826b)   14U |
|  | I2S SCK in slave mode. |
| #define | [NRF\_FUN\_I2S\_LRCK\_M](#a8aeef372eba5608f6fa06c3e592bfe69)   15U |
|  | I2S LRCK in master mode. |
| #define | [NRF\_FUN\_I2S\_LRCK\_S](#aacf6b96aad472ee6423552c80936c375)   16U |
|  | I2S LRCK in slave mode. |
| #define | [NRF\_FUN\_I2S\_SDIN](#ad943106dbd772562b2cca1d063c10456)   17U |
|  | I2S SDIN. |
| #define | [NRF\_FUN\_I2S\_SDOUT](#af2966d1e579895b18331480c42145f2f)   18U |
|  | I2S SDOUT. |
| #define | [NRF\_FUN\_I2S\_MCK](#a6de3f8d978d2aa864c12410ff3a78741)   19U |
|  | I2S MCK. |
| #define | [NRF\_FUN\_PDM\_CLK](#a5ceee799b932f1b71366bda816cde19a)   20U |
|  | PDM CLK. |
| #define | [NRF\_FUN\_PDM\_DIN](#af8f0c9a76b28fe19a5c4552386b6cd30)   21U |
|  | PDM DIN. |
| #define | [NRF\_FUN\_PWM\_OUT0](#a9cf56eb616791c1bf79a15de6e11e270)   22U |
|  | PWM OUT0. |
| #define | [NRF\_FUN\_PWM\_OUT1](#a9668fd12e95380431659e5edaa62cf65)   23U |
|  | PWM OUT1. |
| #define | [NRF\_FUN\_PWM\_OUT2](#a4d9b8e2aba25457f1e688b71a8bcf235)   24U |
|  | PWM OUT2. |
| #define | [NRF\_FUN\_PWM\_OUT3](#a79e863ca96b4e14c6eb0367b7b50bd32)   25U |
|  | PWM OUT3. |
| #define | [NRF\_FUN\_QDEC\_A](#af07b0671c04b3318ad4f6e81f9b02f9b)   26U |
|  | QDEC A. |
| #define | [NRF\_FUN\_QDEC\_B](#a3da455a7ac5e260ff25e867212b4b026)   27U |
|  | QDEC B. |
| #define | [NRF\_FUN\_QDEC\_LED](#a0b4431b76b7c264167fe48294cb5eb3d)   28U |
|  | QDEC LED. |
| #define | [NRF\_FUN\_QSPI\_SCK](#a8504018d0dddd49c009ee8db7f6aa559)   29U |
|  | QSPI SCK. |
| #define | [NRF\_FUN\_QSPI\_CSN](#a2ec92b450cc6f75121879950a7a2f750)   30U |
|  | QSPI CSN. |
| #define | [NRF\_FUN\_QSPI\_IO0](#a97a03ba41e0a1bafe6d44868baf62b21)   31U |
|  | QSPI IO0. |
| #define | [NRF\_FUN\_QSPI\_IO1](#a4a87c54c51d9ab5e602a62f9ec70e98e)   32U |
|  | QSPI IO1. |
| #define | [NRF\_FUN\_QSPI\_IO2](#a0bd9c69689a0ec5c88eb4d50ff1c73dd)   33U |
|  | QSPI IO2. |
| #define | [NRF\_FUN\_QSPI\_IO3](#aaf2c957da80884f0a8d442da64da8b92)   34U |
|  | QSPI IO3. |
| #define | [NRF\_FUN\_EXMIF\_CK](#a9e02aa751912dd3e3ad3964bd2e92b1b)   35U |
|  | EXMIF CK. |
| #define | [NRF\_FUN\_EXMIF\_DQ0](#afe37cd483f85609e7f82044995c7245d)   36U |
|  | EXMIF DQ0. |
| #define | [NRF\_FUN\_EXMIF\_DQ1](#ab58883df980cf4e61b1d74a473a58563)   37U |
|  | EXMIF DQ1. |
| #define | [NRF\_FUN\_EXMIF\_DQ2](#ad358c9ec0f07e70cfc11313c4f09073c)   38U |
|  | EXMIF DQ2. |
| #define | [NRF\_FUN\_EXMIF\_DQ3](#ac7ef6d6a949d228bdaf5635ae5182262)   39U |
|  | EXMIF DQ3. |
| #define | [NRF\_FUN\_EXMIF\_DQ4](#ab74f922a6687ddc1fce33b8f508064b7)   40U |
|  | EXMIF DQ4. |
| #define | [NRF\_FUN\_EXMIF\_DQ5](#a144b60ce024fadb107e19de376f2077c)   41U |
|  | EXMIF DQ5. |
| #define | [NRF\_FUN\_EXMIF\_DQ6](#a8eb7a3680c93054ed76d1d6603ee9425)   42U |
|  | EXMIF DQ6. |
| #define | [NRF\_FUN\_EXMIF\_DQ7](#a8cc2db3d1d971145411645135a29bf18)   43U |
|  | EXMIF DQ7. |
| #define | [NRF\_FUN\_EXMIF\_CS0](#a25571f907b7d808c6d757c2b273287d3)   44U |
|  | EXMIF CS0. |
| #define | [NRF\_FUN\_EXMIF\_CS1](#aa80dee2db548ab0ba3de943046ff24af)   45U |
|  | EXMIF CS1. |
| #define | [NRF\_FUN\_CAN\_TX](#a34338fa4c8ab9e606bdc00d8cfe288ef)   46U |
|  | CAN TX. |
| #define | [NRF\_FUN\_CAN\_RX](#a55a2841880cd17f8d8a6ff5fb67ec71b)   47U |
|  | CAN RX. |
| nRF pinctrl output drive. | |
| #define | [NRF\_DRIVE\_S0S1](#a9a9ec0027e98f277a8ad72edc9783ca8)   0U |
|  | Standard '0', standard '1'. |
| #define | [NRF\_DRIVE\_H0S1](#a76555393e7124f333e0ec19414c2a6d5)   1U |
|  | High drive '0', standard '1'. |
| #define | [NRF\_DRIVE\_S0H1](#abc3f7122815fc04db4c4eede3cfd713c)   2U |
|  | Standard '0', high drive '1'. |
| #define | [NRF\_DRIVE\_H0H1](#a7f65712ab98608dbcdf438a57b651f4b)   3U |
|  | High drive '0', high drive '1'. |
| #define | [NRF\_DRIVE\_D0S1](#ac97de2448f9b56d04bfb07f57c86eee9)   4U |
|  | Disconnect '0' standard '1'. |
| #define | [NRF\_DRIVE\_D0H1](#a74f65220ebf6c8633b7023191bed55e8)   5U |
|  | Disconnect '0', high drive '1'. |
| #define | [NRF\_DRIVE\_S0D1](#aa12e26bef363bd9953791445bd2132d8)   6U |
|  | Standard '0', disconnect '1'. |
| #define | [NRF\_DRIVE\_H0D1](#ab83a7803e7f9155d31f9f3e4373de2c2)   7U |
|  | High drive '0', disconnect '1'. |
| #define | [NRF\_DRIVE\_E0E1](#a164af8cb0a188d21664987deec25946d)   8U |
|  | Extra high drive '0', extra high drive '1'. |
| nRF pinctrl pull-up/down. | |
| Note  Values match nrf\_gpio\_pin\_pull\_t constants. | |
| #define | [NRF\_PULL\_NONE](#ada4d270f356ec03b6686aeabdb71f860)   0U |
|  | Pull-up disabled. |
| #define | [NRF\_PULL\_DOWN](#aca067a8a69d212ccacd9482953fc2893)   1U |
|  | Pull-down enabled. |
| #define | [NRF\_PULL\_UP](#a60062185ecdd8b8552ae00398213c7f7)   3U |
|  | Pull-up enabled. |
| nRF pinctrl low power mode. | |
| #define | [NRF\_LP\_DISABLE](#aab29e9a98303f1d57c249362a4b062b0)   0U |
|  | Input. |
| #define | [NRF\_LP\_ENABLE](#a965ede26fa596ef7dd3ca62e0e9626a0)   1U |
|  | Output. |
| nRF pinctrl helpers to indicate disconnected pins. | |
| #define | [NRF\_PIN\_DISCONNECTED](#a1354873c8f0bcb226fc4d5fabb06b837)   [NRF\_PIN\_MSK](#a8f60ab83a5325691eb0d976ae1f70295) |
|  | Indicates that a pin is disconnected. |

## Macro Definition Documentation

## [◆ ](#af596f5bff44b420017fe9d0bb1260753)NRF\_CLOCKPIN\_ENABLE\_MSK

| #define NRF\_CLOCKPIN\_ENABLE\_MSK   0x1U |
| --- |

Mask for the clockpin enable field.

## [◆ ](#a1ddd10f13ce7524c777f02a2d96ed727)NRF\_CLOCKPIN\_ENABLE\_POS

| #define NRF\_CLOCKPIN\_ENABLE\_POS   17U |
| --- |

Position of the clockpin enable field.

## [◆ ](#a74f65220ebf6c8633b7023191bed55e8)NRF\_DRIVE\_D0H1

| #define NRF\_DRIVE\_D0H1   5U |
| --- |

Disconnect '0', high drive '1'.

## [◆ ](#ac97de2448f9b56d04bfb07f57c86eee9)NRF\_DRIVE\_D0S1

| #define NRF\_DRIVE\_D0S1   4U |
| --- |

Disconnect '0' standard '1'.

## [◆ ](#a164af8cb0a188d21664987deec25946d)NRF\_DRIVE\_E0E1

| #define NRF\_DRIVE\_E0E1   8U |
| --- |

Extra high drive '0', extra high drive '1'.

## [◆ ](#ab83a7803e7f9155d31f9f3e4373de2c2)NRF\_DRIVE\_H0D1

| #define NRF\_DRIVE\_H0D1   7U |
| --- |

High drive '0', disconnect '1'.

## [◆ ](#a7f65712ab98608dbcdf438a57b651f4b)NRF\_DRIVE\_H0H1

| #define NRF\_DRIVE\_H0H1   3U |
| --- |

High drive '0', high drive '1'.

## [◆ ](#a76555393e7124f333e0ec19414c2a6d5)NRF\_DRIVE\_H0S1

| #define NRF\_DRIVE\_H0S1   1U |
| --- |

High drive '0', standard '1'.

## [◆ ](#a86d4555acfb553f6bad1562743cf357c)NRF\_DRIVE\_MSK

| #define NRF\_DRIVE\_MSK   0xFU |
| --- |

Mask for the drive configuration field.

## [◆ ](#ae8b94074f18659a2767e0f7f1aa1c73f)NRF\_DRIVE\_POS

| #define NRF\_DRIVE\_POS   11U |
| --- |

Position of the drive configuration field.

## [◆ ](#aa12e26bef363bd9953791445bd2132d8)NRF\_DRIVE\_S0D1

| #define NRF\_DRIVE\_S0D1   6U |
| --- |

Standard '0', disconnect '1'.

## [◆ ](#abc3f7122815fc04db4c4eede3cfd713c)NRF\_DRIVE\_S0H1

| #define NRF\_DRIVE\_S0H1   2U |
| --- |

Standard '0', high drive '1'.

## [◆ ](#a9a9ec0027e98f277a8ad72edc9783ca8)NRF\_DRIVE\_S0S1

| #define NRF\_DRIVE\_S0S1   0U |
| --- |

Standard '0', standard '1'.

## [◆ ](#a55a2841880cd17f8d8a6ff5fb67ec71b)NRF\_FUN\_CAN\_RX

| #define NRF\_FUN\_CAN\_RX   47U |
| --- |

CAN RX.

## [◆ ](#a34338fa4c8ab9e606bdc00d8cfe288ef)NRF\_FUN\_CAN\_TX

| #define NRF\_FUN\_CAN\_TX   46U |
| --- |

CAN TX.

## [◆ ](#a9e02aa751912dd3e3ad3964bd2e92b1b)NRF\_FUN\_EXMIF\_CK

| #define NRF\_FUN\_EXMIF\_CK   35U |
| --- |

EXMIF CK.

## [◆ ](#a25571f907b7d808c6d757c2b273287d3)NRF\_FUN\_EXMIF\_CS0

| #define NRF\_FUN\_EXMIF\_CS0   44U |
| --- |

EXMIF CS0.

## [◆ ](#aa80dee2db548ab0ba3de943046ff24af)NRF\_FUN\_EXMIF\_CS1

| #define NRF\_FUN\_EXMIF\_CS1   45U |
| --- |

EXMIF CS1.

## [◆ ](#afe37cd483f85609e7f82044995c7245d)NRF\_FUN\_EXMIF\_DQ0

| #define NRF\_FUN\_EXMIF\_DQ0   36U |
| --- |

EXMIF DQ0.

## [◆ ](#ab58883df980cf4e61b1d74a473a58563)NRF\_FUN\_EXMIF\_DQ1

| #define NRF\_FUN\_EXMIF\_DQ1   37U |
| --- |

EXMIF DQ1.

## [◆ ](#ad358c9ec0f07e70cfc11313c4f09073c)NRF\_FUN\_EXMIF\_DQ2

| #define NRF\_FUN\_EXMIF\_DQ2   38U |
| --- |

EXMIF DQ2.

## [◆ ](#ac7ef6d6a949d228bdaf5635ae5182262)NRF\_FUN\_EXMIF\_DQ3

| #define NRF\_FUN\_EXMIF\_DQ3   39U |
| --- |

EXMIF DQ3.

## [◆ ](#ab74f922a6687ddc1fce33b8f508064b7)NRF\_FUN\_EXMIF\_DQ4

| #define NRF\_FUN\_EXMIF\_DQ4   40U |
| --- |

EXMIF DQ4.

## [◆ ](#a144b60ce024fadb107e19de376f2077c)NRF\_FUN\_EXMIF\_DQ5

| #define NRF\_FUN\_EXMIF\_DQ5   41U |
| --- |

EXMIF DQ5.

## [◆ ](#a8eb7a3680c93054ed76d1d6603ee9425)NRF\_FUN\_EXMIF\_DQ6

| #define NRF\_FUN\_EXMIF\_DQ6   42U |
| --- |

EXMIF DQ6.

## [◆ ](#a8cc2db3d1d971145411645135a29bf18)NRF\_FUN\_EXMIF\_DQ7

| #define NRF\_FUN\_EXMIF\_DQ7   43U |
| --- |

EXMIF DQ7.

## [◆ ](#a8aeef372eba5608f6fa06c3e592bfe69)NRF\_FUN\_I2S\_LRCK\_M

| #define NRF\_FUN\_I2S\_LRCK\_M   15U |
| --- |

I2S LRCK in master mode.

## [◆ ](#aacf6b96aad472ee6423552c80936c375)NRF\_FUN\_I2S\_LRCK\_S

| #define NRF\_FUN\_I2S\_LRCK\_S   16U |
| --- |

I2S LRCK in slave mode.

## [◆ ](#a6de3f8d978d2aa864c12410ff3a78741)NRF\_FUN\_I2S\_MCK

| #define NRF\_FUN\_I2S\_MCK   19U |
| --- |

I2S MCK.

## [◆ ](#aae874d5eb9da322f9766c9546c565db2)NRF\_FUN\_I2S\_SCK\_M

| #define NRF\_FUN\_I2S\_SCK\_M   13U |
| --- |

I2S SCK in master mode.

## [◆ ](#aa791b4bf51162aff1f6cfbc374af826b)NRF\_FUN\_I2S\_SCK\_S

| #define NRF\_FUN\_I2S\_SCK\_S   14U |
| --- |

I2S SCK in slave mode.

## [◆ ](#ad943106dbd772562b2cca1d063c10456)NRF\_FUN\_I2S\_SDIN

| #define NRF\_FUN\_I2S\_SDIN   17U |
| --- |

I2S SDIN.

## [◆ ](#af2966d1e579895b18331480c42145f2f)NRF\_FUN\_I2S\_SDOUT

| #define NRF\_FUN\_I2S\_SDOUT   18U |
| --- |

I2S SDOUT.

## [◆ ](#ae3f5b1848b0c00547eff520f22ede922)NRF\_FUN\_MSK

| #define NRF\_FUN\_MSK   0xFFU |
| --- |

Mask for the function field.

## [◆ ](#a5ceee799b932f1b71366bda816cde19a)NRF\_FUN\_PDM\_CLK

| #define NRF\_FUN\_PDM\_CLK   20U |
| --- |

PDM CLK.

## [◆ ](#af8f0c9a76b28fe19a5c4552386b6cd30)NRF\_FUN\_PDM\_DIN

| #define NRF\_FUN\_PDM\_DIN   21U |
| --- |

PDM DIN.

## [◆ ](#a10272aaefd0f103c15ae28ce8ef76987)NRF\_FUN\_POS

| #define NRF\_FUN\_POS   24U |
| --- |

Position of the function field.

## [◆ ](#a9cf56eb616791c1bf79a15de6e11e270)NRF\_FUN\_PWM\_OUT0

| #define NRF\_FUN\_PWM\_OUT0   22U |
| --- |

PWM OUT0.

## [◆ ](#a9668fd12e95380431659e5edaa62cf65)NRF\_FUN\_PWM\_OUT1

| #define NRF\_FUN\_PWM\_OUT1   23U |
| --- |

PWM OUT1.

## [◆ ](#a4d9b8e2aba25457f1e688b71a8bcf235)NRF\_FUN\_PWM\_OUT2

| #define NRF\_FUN\_PWM\_OUT2   24U |
| --- |

PWM OUT2.

## [◆ ](#a79e863ca96b4e14c6eb0367b7b50bd32)NRF\_FUN\_PWM\_OUT3

| #define NRF\_FUN\_PWM\_OUT3   25U |
| --- |

PWM OUT3.

## [◆ ](#af07b0671c04b3318ad4f6e81f9b02f9b)NRF\_FUN\_QDEC\_A

| #define NRF\_FUN\_QDEC\_A   26U |
| --- |

QDEC A.

## [◆ ](#a3da455a7ac5e260ff25e867212b4b026)NRF\_FUN\_QDEC\_B

| #define NRF\_FUN\_QDEC\_B   27U |
| --- |

QDEC B.

## [◆ ](#a0b4431b76b7c264167fe48294cb5eb3d)NRF\_FUN\_QDEC\_LED

| #define NRF\_FUN\_QDEC\_LED   28U |
| --- |

QDEC LED.

## [◆ ](#a2ec92b450cc6f75121879950a7a2f750)NRF\_FUN\_QSPI\_CSN

| #define NRF\_FUN\_QSPI\_CSN   30U |
| --- |

QSPI CSN.

## [◆ ](#a97a03ba41e0a1bafe6d44868baf62b21)NRF\_FUN\_QSPI\_IO0

| #define NRF\_FUN\_QSPI\_IO0   31U |
| --- |

QSPI IO0.

## [◆ ](#a4a87c54c51d9ab5e602a62f9ec70e98e)NRF\_FUN\_QSPI\_IO1

| #define NRF\_FUN\_QSPI\_IO1   32U |
| --- |

QSPI IO1.

## [◆ ](#a0bd9c69689a0ec5c88eb4d50ff1c73dd)NRF\_FUN\_QSPI\_IO2

| #define NRF\_FUN\_QSPI\_IO2   33U |
| --- |

QSPI IO2.

## [◆ ](#aaf2c957da80884f0a8d442da64da8b92)NRF\_FUN\_QSPI\_IO3

| #define NRF\_FUN\_QSPI\_IO3   34U |
| --- |

QSPI IO3.

## [◆ ](#a8504018d0dddd49c009ee8db7f6aa559)NRF\_FUN\_QSPI\_SCK

| #define NRF\_FUN\_QSPI\_SCK   29U |
| --- |

QSPI SCK.

## [◆ ](#afca36f99d1c1a9e17e4949f18206490a)NRF\_FUN\_SPIM\_MISO

| #define NRF\_FUN\_SPIM\_MISO   6U |
| --- |

SPI master MISO.

## [◆ ](#a2e96ea48e6a9e707b76b846536a687cb)NRF\_FUN\_SPIM\_MOSI

| #define NRF\_FUN\_SPIM\_MOSI   5U |
| --- |

SPI master MOSI.

## [◆ ](#a2594557c5e765d65ea7627c5c49e07d6)NRF\_FUN\_SPIM\_SCK

| #define NRF\_FUN\_SPIM\_SCK   4U |
| --- |

SPI master SCK.

## [◆ ](#a6591844a0ce9f0297f917abb2f87c259)NRF\_FUN\_SPIS\_CSN

| #define NRF\_FUN\_SPIS\_CSN   10U |
| --- |

SPI slave CSN.

## [◆ ](#aa480a4b96df9c4521d744de7d9a72e1f)NRF\_FUN\_SPIS\_MISO

| #define NRF\_FUN\_SPIS\_MISO   9U |
| --- |

SPI slave MISO.

## [◆ ](#a016ffb10db008be19f494e7098096109)NRF\_FUN\_SPIS\_MOSI

| #define NRF\_FUN\_SPIS\_MOSI   8U |
| --- |

SPI slave MOSI.

## [◆ ](#a9906fedc9c9667be7a84c66443f01772)NRF\_FUN\_SPIS\_SCK

| #define NRF\_FUN\_SPIS\_SCK   7U |
| --- |

SPI slave SCK.

## [◆ ](#aa26e18840b9cc780f35a1c237f24f8f8)NRF\_FUN\_TWIM\_SCL

| #define NRF\_FUN\_TWIM\_SCL   11U |
| --- |

TWI master SCL.

## [◆ ](#a7f0dcd38287a5e8c2e55145e43a57628)NRF\_FUN\_TWIM\_SDA

| #define NRF\_FUN\_TWIM\_SDA   12U |
| --- |

TWI master SDA.

## [◆ ](#a595b5f913921466ec87c58657709c800)NRF\_FUN\_UART\_CTS

| #define NRF\_FUN\_UART\_CTS   3U |
| --- |

UART CTS.

## [◆ ](#aa2ea1399ee3dff5019adf462b9cb09b8)NRF\_FUN\_UART\_RTS

| #define NRF\_FUN\_UART\_RTS   2U |
| --- |

UART RTS.

## [◆ ](#ad7865c58ddd2d7686482fa2f92a330f8)NRF\_FUN\_UART\_RX

| #define NRF\_FUN\_UART\_RX   1U |
| --- |

UART RX.

## [◆ ](#a9550ec0625d3e702c41d79cdf633bf9b)NRF\_FUN\_UART\_TX

| #define NRF\_FUN\_UART\_TX   0U |
| --- |

UART TX.

## [◆ ](#a1211c8c57f411a7676023c61cc986095)NRF\_GPD\_FAST\_ACTIVE1\_MSK

| #define NRF\_GPD\_FAST\_ACTIVE1\_MSK   0x1U |
| --- |

Mask for the GPD FAST ACTIVE1.

## [◆ ](#a9203c68fb293d5eec889a8729b5f52b3)NRF\_GPD\_FAST\_ACTIVE1\_POS

| #define NRF\_GPD\_FAST\_ACTIVE1\_POS   18U |
| --- |

Position of the GPD FAST ACTIVE1.

## [◆ ](#a1a5cca24fa65f0ea64e8927e9d12ff43)NRF\_INVERT\_MSK

| #define NRF\_INVERT\_MSK   0x1U |
| --- |

Mask for the invert field.

## [◆ ](#aa13cd70c54db20407bfaef944ea10329)NRF\_INVERT\_POS

| #define NRF\_INVERT\_POS   16U |
| --- |

Position of the invert field.

## [◆ ](#aab29e9a98303f1d57c249362a4b062b0)NRF\_LP\_DISABLE

| #define NRF\_LP\_DISABLE   0U |
| --- |

Input.

## [◆ ](#a965ede26fa596ef7dd3ca62e0e9626a0)NRF\_LP\_ENABLE

| #define NRF\_LP\_ENABLE   1U |
| --- |

Output.

## [◆ ](#a67b7d47eed25086ebbe5db508c85ff7b)NRF\_LP\_MSK

| #define NRF\_LP\_MSK   0x1U |
| --- |

Mask for the low power field.

## [◆ ](#a97dce1e8b63e4054f23c1daa0ddd6327)NRF\_LP\_POS

| #define NRF\_LP\_POS   15U |
| --- |

Position of the low power field.

## [◆ ](#a1354873c8f0bcb226fc4d5fabb06b837)NRF\_PIN\_DISCONNECTED

| #define NRF\_PIN\_DISCONNECTED   [NRF\_PIN\_MSK](#a8f60ab83a5325691eb0d976ae1f70295) |
| --- |

Indicates that a pin is disconnected.

## [◆ ](#a8f60ab83a5325691eb0d976ae1f70295)NRF\_PIN\_MSK

| #define NRF\_PIN\_MSK   0x1FFU |
| --- |

Mask for the pin field.

## [◆ ](#aa057ad8de2dea12959f51a293a929367)NRF\_PIN\_POS

| #define NRF\_PIN\_POS   0U |
| --- |

Position of the pin field.

## [◆ ](#a43d0a0ad6e574456a2b69ab5354ccef4)NRF\_PSEL

| #define NRF\_PSEL | ( |  | *fun*, |
| --- | --- | --- | --- |
|  |  |  | *port*, |
|  |  |  | *pin* ) |

**Value:**

((((((port) \* 32U) + (pin)) & [NRF\_PIN\_MSK](#a8f60ab83a5325691eb0d976ae1f70295)) << [NRF\_PIN\_POS](#aa057ad8de2dea12959f51a293a929367)) | \

((NRF\_FUN\_ ## fun & [NRF\_FUN\_MSK](#ae3f5b1848b0c00547eff520f22ede922)) << [NRF\_FUN\_POS](#a10272aaefd0f103c15ae28ce8ef76987)))

[NRF\_FUN\_POS](#a10272aaefd0f103c15ae28ce8ef76987)

#define NRF\_FUN\_POS

Position of the function field.

**Definition** nrf-pinctrl.h:30

[NRF\_PIN\_MSK](#a8f60ab83a5325691eb0d976ae1f70295)

#define NRF\_PIN\_MSK

Mask for the pin field.

**Definition** nrf-pinctrl.h:60

[NRF\_PIN\_POS](#aa057ad8de2dea12959f51a293a929367)

#define NRF\_PIN\_POS

Position of the pin field.

**Definition** nrf-pinctrl.h:58

[NRF\_FUN\_MSK](#ae3f5b1848b0c00547eff520f22ede922)

#define NRF\_FUN\_MSK

Mask for the function field.

**Definition** nrf-pinctrl.h:32

Utility macro to build nRF psels property entry.

Parameters
:   | fun | Pin function configuration (see NRF\_FUNC\_{name} macros). |
    | --- | --- |
    | port | Port (0 or 15). |
    | pin | Pin (0..31). |

## [◆ ](#a2e414bdc5912c0e0abc349d5362520bd)NRF\_PSEL\_DISCONNECTED

| #define NRF\_PSEL\_DISCONNECTED | ( |  | *fun* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

([NRF\_PIN\_DISCONNECTED](#a1354873c8f0bcb226fc4d5fabb06b837) | \

((NRF\_FUN\_ ## fun & [NRF\_FUN\_MSK](#ae3f5b1848b0c00547eff520f22ede922)) << [NRF\_FUN\_POS](#a10272aaefd0f103c15ae28ce8ef76987)))

[NRF\_PIN\_DISCONNECTED](#a1354873c8f0bcb226fc4d5fabb06b837)

#define NRF\_PIN\_DISCONNECTED

Indicates that a pin is disconnected.

**Definition** nrf-pinctrl.h:227

Utility macro to build nRF psels property entry when a pin is disconnected.

This can be useful in situations where code running before Zephyr, e.g. a bootloader configures pins that later needs to be disconnected.

Parameters
:   | fun | Pin function configuration (see NRF\_FUN\_{name} macros). |
    | --- | --- |

## [◆ ](#aca067a8a69d212ccacd9482953fc2893)NRF\_PULL\_DOWN

| #define NRF\_PULL\_DOWN   1U |
| --- |

Pull-down enabled.

## [◆ ](#a3900fd72d44feeefef9aa73c909a2396)NRF\_PULL\_MSK

| #define NRF\_PULL\_MSK   0x3U |
| --- |

Mask for the pull configuration field.

## [◆ ](#ada4d270f356ec03b6686aeabdb71f860)NRF\_PULL\_NONE

| #define NRF\_PULL\_NONE   0U |
| --- |

Pull-up disabled.

## [◆ ](#a0fac117bc7a2f45638ce462527cb8daa)NRF\_PULL\_POS

| #define NRF\_PULL\_POS   9U |
| --- |

Position of the pull configuration field.

## [◆ ](#a60062185ecdd8b8552ae00398213c7f7)NRF\_PULL\_UP

| #define NRF\_PULL\_UP   3U |
| --- |

Pull-up enabled.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [nrf-pinctrl.h](nrf-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
