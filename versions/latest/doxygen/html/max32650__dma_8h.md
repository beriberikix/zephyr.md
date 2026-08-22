---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/max32650__dma_8h.html
original_path: doxygen/html/max32650__dma_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

max32650\_dma.h File Reference

[Go to the source code of this file.](max32650__dma_8h_source.md)

| Macros | |
| --- | --- |
| #define | [MAX32\_DMA\_SLOT\_MEMTOMEM](#a6e1ea6d5650545947928c83c71776c04)   0x00U |
| #define | [MAX32\_DMA\_SLOT\_SPI0\_RX](#ac505ee888a8cb52b03ac733a9b650097)   0x01U |
| #define | [MAX32\_DMA\_SLOT\_SPI1\_RX](#a0df8d71978ba7b5c5b6766c1cf28d00c)   0x02U |
| #define | [MAX32\_DMA\_SLOT\_SPI2\_RX](#afedfa23ede3c9817b4952311c3458ba0)   0x03U |
| #define | [MAX32\_DMA\_SLOT\_UART0\_RX](#ac823471b99eda7df54c2fce6eb923e96)   0x04U |
| #define | [MAX32\_DMA\_SLOT\_UART1\_RX](#ab7e79c3fa976243daa7ef5880f20fade)   0x05U |
| #define | [MAX32\_DMA\_SLOT\_I2C0\_RX](#a207563fbc9fb4110d78f92b1d2d4c423)   0x07U |
| #define | [MAX32\_DMA\_SLOT\_I2C1\_RX](#ad589918d7435fc9c74021d5ae1e5d5ca)   0x08U |
| #define | [MAX32\_DMA\_SLOT\_ADC](#adf6d862b295bc34de7b3c8334b6ad306)   0x09U |
| #define | [MAX32\_DMA\_SLOT\_UART2\_RX](#ac82aa4f9ad49e656963580bf297dcd26)   0x0EU |
| #define | [MAX32\_DMA\_SLOT\_SPI3\_RX](#a5314a7ed922831a39b6a025b4392ad06)   0x0FU |
| #define | [MAX32\_DMA\_SLOT\_SPI\_MSS\_RX](#a85a173b66c3ebc2768b5a8ad3514a83a)   0x10U |
| #define | [MAX32\_DMA\_SLOT\_USB\_RX1](#a0b75476dc07fbc9ec8ffb2e1e3a81981)   0x11U |
| #define | [MAX32\_DMA\_SLOT\_USB\_RX2](#a740ff452ee6d87e8294c20202e5a5eff)   0x12U |
| #define | [MAX32\_DMA\_SLOT\_USB\_RX3](#adce27b072546e820614976131f6e107a)   0x13U |
| #define | [MAX32\_DMA\_SLOT\_USB\_RX4](#a406cf4dd9f03849ae40057de5e7e1f01)   0x14U |
| #define | [MAX32\_DMA\_SLOT\_USB\_RX5](#a034c7228b0e23ef8d8df08f084b960ce)   0x15U |
| #define | [MAX32\_DMA\_SLOT\_USB\_RX6](#a2d38a4656f34282ab3d2766ee1a28429)   0x16U |
| #define | [MAX32\_DMA\_SLOT\_USB\_RX7](#a2f2e9d3c91ec5dda76f66099ff536725)   0x17U |
| #define | [MAX32\_DMA\_SLOT\_USB\_RX8](#a44c9abf42bedbf7a2459493a9a555b12)   0x18U |
| #define | [MAX32\_DMA\_SLOT\_USB\_RX9](#a41536d9831888832f4952fdf422864fa)   0x19U |
| #define | [MAX32\_DMA\_SLOT\_USB\_RX10](#a0c7485b0d883b3dab77565daa0bb4a74)   0x1AU |
| #define | [MAX32\_DMA\_SLOT\_USB\_RX11](#a1cd31446fe267673688df59af1f6f07d)   0x1BU |
| #define | [MAX32\_DMA\_SLOT\_SPI0\_TX](#a26f06363fd4639eaee5668450adaa1c3)   0x21U |
| #define | [MAX32\_DMA\_SLOT\_SPI1\_TX](#aa85105348eeb191fd2799d645aacc575)   0x22U |
| #define | [MAX32\_DMA\_SLOT\_SPI2\_TX](#a88067802f3a790268fcca78597551d80)   0x23U |
| #define | [MAX32\_DMA\_SLOT\_UART0\_TX](#a009a7e71c5fed2afa3d8907411c454e3)   0x24U |
| #define | [MAX32\_DMA\_SLOT\_UART1\_TX](#a5f8ba237de646a46c5584fe28fd05afa)   0x25U |
| #define | [MAX32\_DMA\_SLOT\_I2C0\_TX](#aee43cae318d6b70f9f2a7e6bd77e02dd)   0x27U |
| #define | [MAX32\_DMA\_SLOT\_I2C1\_TX](#a7a8535c65c0e3d286c0d26824ed37b0c)   0x28U |
| #define | [MAX32\_DMA\_SLOT\_UART2\_TX](#af2c822f39971c7bc6b8d58df6d139433)   0x2EU |
| #define | [MAX32\_DMA\_SLOT\_SPI3\_TX](#a051094c0cb0cfc3bd513cea484046601)   0x2FU |
| #define | [MAX32\_DMA\_SLOT\_SPI\_MSS\_TX](#ade3c6853ef7a5690d886903978b414f1)   0x30U |
| #define | [MAX32\_DMA\_SLOT\_USB\_TX1](#a0a3828eb499d5fa83acec4b4d0bb3f01)   0x31U |
| #define | [MAX32\_DMA\_SLOT\_USB\_TX2](#a7c7e6605fecf725fd9ba2fe6145a6038)   0x32U |
| #define | [MAX32\_DMA\_SLOT\_USB\_TX3](#a1d3020098dad909bc83ec30b25a6dcee)   0x33U |
| #define | [MAX32\_DMA\_SLOT\_USB\_TX4](#a11f32857847be0b0c4c71b8bd98f0227)   0x34U |
| #define | [MAX32\_DMA\_SLOT\_USB\_TX5](#ab6ff1b56cffd6c8f210db5fa2c67e862)   0x35U |
| #define | [MAX32\_DMA\_SLOT\_USB\_TX6](#aeb107c1e11d72e3cccc403c214ec1714)   0x36U |
| #define | [MAX32\_DMA\_SLOT\_USB\_TX7](#a21a7cec8333267f2bae73054500b2453)   0x37U |
| #define | [MAX32\_DMA\_SLOT\_USB\_TX8](#a273d7a9da9f57c5d8f3bdfbea2fd17e7)   0x38U |
| #define | [MAX32\_DMA\_SLOT\_USB\_TX9](#a7c323924a5cf297987b54211c2591283)   0x39U |
| #define | [MAX32\_DMA\_SLOT\_USB\_TX10](#ac64dc00771e5d66fe9946648958208dc)   0x3AU |
| #define | [MAX32\_DMA\_SLOT\_USB\_TX11](#a4643edd680c15f931e8185b7a216c1e4)   0x3BU |

## Macro Definition Documentation

## [◆ ](#adf6d862b295bc34de7b3c8334b6ad306)MAX32\_DMA\_SLOT\_ADC

| #define MAX32\_DMA\_SLOT\_ADC   0x09U |
| --- |

## [◆ ](#a207563fbc9fb4110d78f92b1d2d4c423)MAX32\_DMA\_SLOT\_I2C0\_RX

| #define MAX32\_DMA\_SLOT\_I2C0\_RX   0x07U |
| --- |

## [◆ ](#aee43cae318d6b70f9f2a7e6bd77e02dd)MAX32\_DMA\_SLOT\_I2C0\_TX

| #define MAX32\_DMA\_SLOT\_I2C0\_TX   0x27U |
| --- |

## [◆ ](#ad589918d7435fc9c74021d5ae1e5d5ca)MAX32\_DMA\_SLOT\_I2C1\_RX

| #define MAX32\_DMA\_SLOT\_I2C1\_RX   0x08U |
| --- |

## [◆ ](#a7a8535c65c0e3d286c0d26824ed37b0c)MAX32\_DMA\_SLOT\_I2C1\_TX

| #define MAX32\_DMA\_SLOT\_I2C1\_TX   0x28U |
| --- |

## [◆ ](#a6e1ea6d5650545947928c83c71776c04)MAX32\_DMA\_SLOT\_MEMTOMEM

| #define MAX32\_DMA\_SLOT\_MEMTOMEM   0x00U |
| --- |

## [◆ ](#ac505ee888a8cb52b03ac733a9b650097)MAX32\_DMA\_SLOT\_SPI0\_RX

| #define MAX32\_DMA\_SLOT\_SPI0\_RX   0x01U |
| --- |

## [◆ ](#a26f06363fd4639eaee5668450adaa1c3)MAX32\_DMA\_SLOT\_SPI0\_TX

| #define MAX32\_DMA\_SLOT\_SPI0\_TX   0x21U |
| --- |

## [◆ ](#a0df8d71978ba7b5c5b6766c1cf28d00c)MAX32\_DMA\_SLOT\_SPI1\_RX

| #define MAX32\_DMA\_SLOT\_SPI1\_RX   0x02U |
| --- |

## [◆ ](#aa85105348eeb191fd2799d645aacc575)MAX32\_DMA\_SLOT\_SPI1\_TX

| #define MAX32\_DMA\_SLOT\_SPI1\_TX   0x22U |
| --- |

## [◆ ](#afedfa23ede3c9817b4952311c3458ba0)MAX32\_DMA\_SLOT\_SPI2\_RX

| #define MAX32\_DMA\_SLOT\_SPI2\_RX   0x03U |
| --- |

## [◆ ](#a88067802f3a790268fcca78597551d80)MAX32\_DMA\_SLOT\_SPI2\_TX

| #define MAX32\_DMA\_SLOT\_SPI2\_TX   0x23U |
| --- |

## [◆ ](#a5314a7ed922831a39b6a025b4392ad06)MAX32\_DMA\_SLOT\_SPI3\_RX

| #define MAX32\_DMA\_SLOT\_SPI3\_RX   0x0FU |
| --- |

## [◆ ](#a051094c0cb0cfc3bd513cea484046601)MAX32\_DMA\_SLOT\_SPI3\_TX

| #define MAX32\_DMA\_SLOT\_SPI3\_TX   0x2FU |
| --- |

## [◆ ](#a85a173b66c3ebc2768b5a8ad3514a83a)MAX32\_DMA\_SLOT\_SPI\_MSS\_RX

| #define MAX32\_DMA\_SLOT\_SPI\_MSS\_RX   0x10U |
| --- |

## [◆ ](#ade3c6853ef7a5690d886903978b414f1)MAX32\_DMA\_SLOT\_SPI\_MSS\_TX

| #define MAX32\_DMA\_SLOT\_SPI\_MSS\_TX   0x30U |
| --- |

## [◆ ](#ac823471b99eda7df54c2fce6eb923e96)MAX32\_DMA\_SLOT\_UART0\_RX

| #define MAX32\_DMA\_SLOT\_UART0\_RX   0x04U |
| --- |

## [◆ ](#a009a7e71c5fed2afa3d8907411c454e3)MAX32\_DMA\_SLOT\_UART0\_TX

| #define MAX32\_DMA\_SLOT\_UART0\_TX   0x24U |
| --- |

## [◆ ](#ab7e79c3fa976243daa7ef5880f20fade)MAX32\_DMA\_SLOT\_UART1\_RX

| #define MAX32\_DMA\_SLOT\_UART1\_RX   0x05U |
| --- |

## [◆ ](#a5f8ba237de646a46c5584fe28fd05afa)MAX32\_DMA\_SLOT\_UART1\_TX

| #define MAX32\_DMA\_SLOT\_UART1\_TX   0x25U |
| --- |

## [◆ ](#ac82aa4f9ad49e656963580bf297dcd26)MAX32\_DMA\_SLOT\_UART2\_RX

| #define MAX32\_DMA\_SLOT\_UART2\_RX   0x0EU |
| --- |

## [◆ ](#af2c822f39971c7bc6b8d58df6d139433)MAX32\_DMA\_SLOT\_UART2\_TX

| #define MAX32\_DMA\_SLOT\_UART2\_TX   0x2EU |
| --- |

## [◆ ](#a0b75476dc07fbc9ec8ffb2e1e3a81981)MAX32\_DMA\_SLOT\_USB\_RX1

| #define MAX32\_DMA\_SLOT\_USB\_RX1   0x11U |
| --- |

## [◆ ](#a0c7485b0d883b3dab77565daa0bb4a74)MAX32\_DMA\_SLOT\_USB\_RX10

| #define MAX32\_DMA\_SLOT\_USB\_RX10   0x1AU |
| --- |

## [◆ ](#a1cd31446fe267673688df59af1f6f07d)MAX32\_DMA\_SLOT\_USB\_RX11

| #define MAX32\_DMA\_SLOT\_USB\_RX11   0x1BU |
| --- |

## [◆ ](#a740ff452ee6d87e8294c20202e5a5eff)MAX32\_DMA\_SLOT\_USB\_RX2

| #define MAX32\_DMA\_SLOT\_USB\_RX2   0x12U |
| --- |

## [◆ ](#adce27b072546e820614976131f6e107a)MAX32\_DMA\_SLOT\_USB\_RX3

| #define MAX32\_DMA\_SLOT\_USB\_RX3   0x13U |
| --- |

## [◆ ](#a406cf4dd9f03849ae40057de5e7e1f01)MAX32\_DMA\_SLOT\_USB\_RX4

| #define MAX32\_DMA\_SLOT\_USB\_RX4   0x14U |
| --- |

## [◆ ](#a034c7228b0e23ef8d8df08f084b960ce)MAX32\_DMA\_SLOT\_USB\_RX5

| #define MAX32\_DMA\_SLOT\_USB\_RX5   0x15U |
| --- |

## [◆ ](#a2d38a4656f34282ab3d2766ee1a28429)MAX32\_DMA\_SLOT\_USB\_RX6

| #define MAX32\_DMA\_SLOT\_USB\_RX6   0x16U |
| --- |

## [◆ ](#a2f2e9d3c91ec5dda76f66099ff536725)MAX32\_DMA\_SLOT\_USB\_RX7

| #define MAX32\_DMA\_SLOT\_USB\_RX7   0x17U |
| --- |

## [◆ ](#a44c9abf42bedbf7a2459493a9a555b12)MAX32\_DMA\_SLOT\_USB\_RX8

| #define MAX32\_DMA\_SLOT\_USB\_RX8   0x18U |
| --- |

## [◆ ](#a41536d9831888832f4952fdf422864fa)MAX32\_DMA\_SLOT\_USB\_RX9

| #define MAX32\_DMA\_SLOT\_USB\_RX9   0x19U |
| --- |

## [◆ ](#a0a3828eb499d5fa83acec4b4d0bb3f01)MAX32\_DMA\_SLOT\_USB\_TX1

| #define MAX32\_DMA\_SLOT\_USB\_TX1   0x31U |
| --- |

## [◆ ](#ac64dc00771e5d66fe9946648958208dc)MAX32\_DMA\_SLOT\_USB\_TX10

| #define MAX32\_DMA\_SLOT\_USB\_TX10   0x3AU |
| --- |

## [◆ ](#a4643edd680c15f931e8185b7a216c1e4)MAX32\_DMA\_SLOT\_USB\_TX11

| #define MAX32\_DMA\_SLOT\_USB\_TX11   0x3BU |
| --- |

## [◆ ](#a7c7e6605fecf725fd9ba2fe6145a6038)MAX32\_DMA\_SLOT\_USB\_TX2

| #define MAX32\_DMA\_SLOT\_USB\_TX2   0x32U |
| --- |

## [◆ ](#a1d3020098dad909bc83ec30b25a6dcee)MAX32\_DMA\_SLOT\_USB\_TX3

| #define MAX32\_DMA\_SLOT\_USB\_TX3   0x33U |
| --- |

## [◆ ](#a11f32857847be0b0c4c71b8bd98f0227)MAX32\_DMA\_SLOT\_USB\_TX4

| #define MAX32\_DMA\_SLOT\_USB\_TX4   0x34U |
| --- |

## [◆ ](#ab6ff1b56cffd6c8f210db5fa2c67e862)MAX32\_DMA\_SLOT\_USB\_TX5

| #define MAX32\_DMA\_SLOT\_USB\_TX5   0x35U |
| --- |

## [◆ ](#aeb107c1e11d72e3cccc403c214ec1714)MAX32\_DMA\_SLOT\_USB\_TX6

| #define MAX32\_DMA\_SLOT\_USB\_TX6   0x36U |
| --- |

## [◆ ](#a21a7cec8333267f2bae73054500b2453)MAX32\_DMA\_SLOT\_USB\_TX7

| #define MAX32\_DMA\_SLOT\_USB\_TX7   0x37U |
| --- |

## [◆ ](#a273d7a9da9f57c5d8f3bdfbea2fd17e7)MAX32\_DMA\_SLOT\_USB\_TX8

| #define MAX32\_DMA\_SLOT\_USB\_TX8   0x38U |
| --- |

## [◆ ](#a7c323924a5cf297987b54211c2591283)MAX32\_DMA\_SLOT\_USB\_TX9

| #define MAX32\_DMA\_SLOT\_USB\_TX9   0x39U |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [dma](dir_4af45c18fedc476f9a2ee26ec98f56f0.md)
- [max32650\_dma.h](max32650__dma_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
