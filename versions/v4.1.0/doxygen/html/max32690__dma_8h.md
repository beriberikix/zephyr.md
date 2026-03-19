---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/max32690__dma_8h.html
original_path: doxygen/html/max32690__dma_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

max32690\_dma.h File Reference

[Go to the source code of this file.](max32690__dma_8h_source.md)

| Macros | |
| --- | --- |
| #define | [MAX32\_DMA\_SLOT\_MEMTOMEM](#a6e1ea6d5650545947928c83c71776c04)   0x00U |
| #define | [MAX32\_DMA\_SLOT\_SPI0\_RX](#ac505ee888a8cb52b03ac733a9b650097)   0x01U |
| #define | [MAX32\_DMA\_SLOT\_SPI1\_RX](#a0df8d71978ba7b5c5b6766c1cf28d00c)   0x02U |
| #define | [MAX32\_DMA\_SLOT\_SPI2\_RX](#afedfa23ede3c9817b4952311c3458ba0)   0x03U |
| #define | [MAX32\_DMA\_SLOT\_UART0\_RX](#ac823471b99eda7df54c2fce6eb923e96)   0x04U |
| #define | [MAX32\_DMA\_SLOT\_UART1\_RX](#ab7e79c3fa976243daa7ef5880f20fade)   0x05U |
| #define | [MAX32\_DMA\_SLOT\_CAN0\_RX](#a05fffce0b3b48f9170223932559b8d41)   0x06U |
| #define | [MAX32\_DMA\_SLOT\_I2C0\_RX](#a207563fbc9fb4110d78f92b1d2d4c423)   0x07U |
| #define | [MAX32\_DMA\_SLOT\_I2C1\_RX](#ad589918d7435fc9c74021d5ae1e5d5ca)   0x08U |
| #define | [MAX32\_DMA\_SLOT\_ADC](#adf6d862b295bc34de7b3c8334b6ad306)   0x09U |
| #define | [MAX32\_DMA\_SLOT\_I2C2\_RX](#a640bd0651d35157bdd822b11e8b23274)   0x0AU |
| #define | [MAX32\_DMA\_SLOT\_UART2\_RX](#ac82aa4f9ad49e656963580bf297dcd26)   0x0EU |
| #define | [MAX32\_DMA\_SLOT\_SPI3\_RX](#a5314a7ed922831a39b6a025b4392ad06)   0x0FU |
| #define | [MAX32\_DMA\_SLOT\_SPI4\_RX](#a891ca72eda14d6331e78015f120dbb6a)   0x10U |
| #define | [MAX32\_DMA\_SLOT\_USB1\_IN](#a03f1f3ae4ed1f1338fd04fa067ad75e8)   0x11U |
| #define | [MAX32\_DMA\_SLOT\_USB2\_IN](#a64ae56f1a1e74e8b5215392833d5b32f)   0x12U |
| #define | [MAX32\_DMA\_SLOT\_USB3\_IN](#af408853da19bdfc6348ebfca9f868e35)   0x13U |
| #define | [MAX32\_DMA\_SLOT\_USB4\_IN](#a47f54cb1d33b89ee58e4bf11ed48a099)   0x14U |
| #define | [MAX32\_DMA\_SLOT\_USB5\_IN](#a7e2ae2470bd7133deba81786fa3f8112)   0x15U |
| #define | [MAX32\_DMA\_SLOT\_USB6\_IN](#a4c558e41238658fa93a7a1b94812ffe3)   0x16U |
| #define | [MAX32\_DMA\_SLOT\_USB7\_IN](#a856fece9c57666f58065ed62a8a4d895)   0x17U |
| #define | [MAX32\_DMA\_SLOT\_USB8\_IN](#a1539f829df18cf805b6e0dd904f67cba)   0x18U |
| #define | [MAX32\_DMA\_SLOT\_USB9\_IN](#a0f6099d8756b2752fd1b61f3367328be)   0x19U |
| #define | [MAX32\_DMA\_SLOT\_USB10\_IN](#ae4b1142f08cd54821757bca8c049ea52)   0x1AU |
| #define | [MAX32\_DMA\_SLOT\_USB11\_IN](#a9228600145736a5a2e6c68212207f70a)   0x1BU |
| #define | [MAX32\_DMA\_SLOT\_UART3\_RX](#a836e5ca3823f71e408ec8807c5bf1156)   0x1CU |
| #define | [MAX32\_DMA\_SLOT\_I2S\_RX](#a56646e3053fc8a76ef214adbd0ba5921)   0x1EU |
| #define | [MAX32\_DMA\_SLOT\_CAN1\_RX](#a8e50669ec54878ab00ad6eb848506d55)   0x1FU |
| #define | [MAX32\_DMA\_SLOT\_SPI0\_TX](#a26f06363fd4639eaee5668450adaa1c3)   0x21U |
| #define | [MAX32\_DMA\_SLOT\_SPI1\_TX](#aa85105348eeb191fd2799d645aacc575)   0x22U |
| #define | [MAX32\_DMA\_SLOT\_SPI2\_TX](#a88067802f3a790268fcca78597551d80)   0x23U |
| #define | [MAX32\_DMA\_SLOT\_UART0\_TX](#a009a7e71c5fed2afa3d8907411c454e3)   0x24U |
| #define | [MAX32\_DMA\_SLOT\_UART1\_TX](#a5f8ba237de646a46c5584fe28fd05afa)   0x25U |
| #define | [MAX32\_DMA\_SLOT\_CAN0\_TX](#ab6e6d113ddcf94477524929baec50efe)   0x26U |
| #define | [MAX32\_DMA\_SLOT\_I2C0\_TX](#aee43cae318d6b70f9f2a7e6bd77e02dd)   0x27U |
| #define | [MAX32\_DMA\_SLOT\_I2C1\_TX](#a7a8535c65c0e3d286c0d26824ed37b0c)   0x28U |
| #define | [MAX32\_DMA\_SLOT\_I2C2\_TX](#a8ae2d2fe05f0b1caea4b5c127fac3e11)   0x2AU |
| #define | [MAX32\_DMA\_SLOT\_UART2\_TX](#af2c822f39971c7bc6b8d58df6d139433)   0x2EU |
| #define | [MAX32\_DMA\_SLOT\_SPI3\_TX](#a051094c0cb0cfc3bd513cea484046601)   0x2FU |
| #define | [MAX32\_DMA\_SLOT\_SPI4\_TX](#a814c56475fe8b6ce2a6b6817032f2a87)   0x30U |
| #define | [MAX32\_DMA\_SLOT\_USB1\_OUT](#ab82dc978e78da71129ec21b08dc4c62f)   0x31U |
| #define | [MAX32\_DMA\_SLOT\_USB2\_OUT](#ad3f08940af7b9908c4376e87f73a4646)   0x32U |
| #define | [MAX32\_DMA\_SLOT\_USB3\_OUT](#affcdb959a2ce310a5745d623443ecf39)   0x33U |
| #define | [MAX32\_DMA\_SLOT\_USB4\_OUT](#aa10e5db19758fa2983c8e5c8dec1728e)   0x34U |
| #define | [MAX32\_DMA\_SLOT\_USB5\_OUT](#a3fdbec2e3910715b0505443a761d0199)   0x35U |
| #define | [MAX32\_DMA\_SLOT\_USB6\_OUT](#aaafe5f2dd2de43fd0df91383fef80888)   0x36U |
| #define | [MAX32\_DMA\_SLOT\_USB7\_OUT](#a7f83f6b1831f8d611d89bba5b85e3078)   0x37U |
| #define | [MAX32\_DMA\_SLOT\_USB8\_OUT](#a2c6fc053f7550264605e8e49a07ff4ee)   0x38U |
| #define | [MAX32\_DMA\_SLOT\_USB9\_OUT](#a85621d1cac930edf18367e3230514174)   0x39U |
| #define | [MAX32\_DMA\_SLOT\_USB10\_OUT](#a00aaf2c238cb9fa36b9ebb684fb0f4e9)   0x3AU |
| #define | [MAX32\_DMA\_SLOT\_USB11\_OUT](#abf6ee8392db788088caec873d6fe6ac7)   0x3BU |
| #define | [MAX32\_DMA\_SLOT\_UART3\_TX](#a7dbddaa644cdf31bc19cbcf638bec5a3)   0x3CU |
| #define | [MAX32\_DMA\_SLOT\_I2S\_TX](#a6ac25728509e7319f256fd02bb53f208)   0x3EU |
| #define | [MAX32\_DMA\_SLOT\_CAN1\_TX](#a39e447dd29c09caef38a8b516a432e9e)   0x3FU |

## Macro Definition Documentation

## [◆ ](#adf6d862b295bc34de7b3c8334b6ad306)MAX32\_DMA\_SLOT\_ADC

| #define MAX32\_DMA\_SLOT\_ADC   0x09U |
| --- |

## [◆ ](#a05fffce0b3b48f9170223932559b8d41)MAX32\_DMA\_SLOT\_CAN0\_RX

| #define MAX32\_DMA\_SLOT\_CAN0\_RX   0x06U |
| --- |

## [◆ ](#ab6e6d113ddcf94477524929baec50efe)MAX32\_DMA\_SLOT\_CAN0\_TX

| #define MAX32\_DMA\_SLOT\_CAN0\_TX   0x26U |
| --- |

## [◆ ](#a8e50669ec54878ab00ad6eb848506d55)MAX32\_DMA\_SLOT\_CAN1\_RX

| #define MAX32\_DMA\_SLOT\_CAN1\_RX   0x1FU |
| --- |

## [◆ ](#a39e447dd29c09caef38a8b516a432e9e)MAX32\_DMA\_SLOT\_CAN1\_TX

| #define MAX32\_DMA\_SLOT\_CAN1\_TX   0x3FU |
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

## [◆ ](#a640bd0651d35157bdd822b11e8b23274)MAX32\_DMA\_SLOT\_I2C2\_RX

| #define MAX32\_DMA\_SLOT\_I2C2\_RX   0x0AU |
| --- |

## [◆ ](#a8ae2d2fe05f0b1caea4b5c127fac3e11)MAX32\_DMA\_SLOT\_I2C2\_TX

| #define MAX32\_DMA\_SLOT\_I2C2\_TX   0x2AU |
| --- |

## [◆ ](#a56646e3053fc8a76ef214adbd0ba5921)MAX32\_DMA\_SLOT\_I2S\_RX

| #define MAX32\_DMA\_SLOT\_I2S\_RX   0x1EU |
| --- |

## [◆ ](#a6ac25728509e7319f256fd02bb53f208)MAX32\_DMA\_SLOT\_I2S\_TX

| #define MAX32\_DMA\_SLOT\_I2S\_TX   0x3EU |
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

## [◆ ](#a891ca72eda14d6331e78015f120dbb6a)MAX32\_DMA\_SLOT\_SPI4\_RX

| #define MAX32\_DMA\_SLOT\_SPI4\_RX   0x10U |
| --- |

## [◆ ](#a814c56475fe8b6ce2a6b6817032f2a87)MAX32\_DMA\_SLOT\_SPI4\_TX

| #define MAX32\_DMA\_SLOT\_SPI4\_TX   0x30U |
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

## [◆ ](#a836e5ca3823f71e408ec8807c5bf1156)MAX32\_DMA\_SLOT\_UART3\_RX

| #define MAX32\_DMA\_SLOT\_UART3\_RX   0x1CU |
| --- |

## [◆ ](#a7dbddaa644cdf31bc19cbcf638bec5a3)MAX32\_DMA\_SLOT\_UART3\_TX

| #define MAX32\_DMA\_SLOT\_UART3\_TX   0x3CU |
| --- |

## [◆ ](#ae4b1142f08cd54821757bca8c049ea52)MAX32\_DMA\_SLOT\_USB10\_IN

| #define MAX32\_DMA\_SLOT\_USB10\_IN   0x1AU |
| --- |

## [◆ ](#a00aaf2c238cb9fa36b9ebb684fb0f4e9)MAX32\_DMA\_SLOT\_USB10\_OUT

| #define MAX32\_DMA\_SLOT\_USB10\_OUT   0x3AU |
| --- |

## [◆ ](#a9228600145736a5a2e6c68212207f70a)MAX32\_DMA\_SLOT\_USB11\_IN

| #define MAX32\_DMA\_SLOT\_USB11\_IN   0x1BU |
| --- |

## [◆ ](#abf6ee8392db788088caec873d6fe6ac7)MAX32\_DMA\_SLOT\_USB11\_OUT

| #define MAX32\_DMA\_SLOT\_USB11\_OUT   0x3BU |
| --- |

## [◆ ](#a03f1f3ae4ed1f1338fd04fa067ad75e8)MAX32\_DMA\_SLOT\_USB1\_IN

| #define MAX32\_DMA\_SLOT\_USB1\_IN   0x11U |
| --- |

## [◆ ](#ab82dc978e78da71129ec21b08dc4c62f)MAX32\_DMA\_SLOT\_USB1\_OUT

| #define MAX32\_DMA\_SLOT\_USB1\_OUT   0x31U |
| --- |

## [◆ ](#a64ae56f1a1e74e8b5215392833d5b32f)MAX32\_DMA\_SLOT\_USB2\_IN

| #define MAX32\_DMA\_SLOT\_USB2\_IN   0x12U |
| --- |

## [◆ ](#ad3f08940af7b9908c4376e87f73a4646)MAX32\_DMA\_SLOT\_USB2\_OUT

| #define MAX32\_DMA\_SLOT\_USB2\_OUT   0x32U |
| --- |

## [◆ ](#af408853da19bdfc6348ebfca9f868e35)MAX32\_DMA\_SLOT\_USB3\_IN

| #define MAX32\_DMA\_SLOT\_USB3\_IN   0x13U |
| --- |

## [◆ ](#affcdb959a2ce310a5745d623443ecf39)MAX32\_DMA\_SLOT\_USB3\_OUT

| #define MAX32\_DMA\_SLOT\_USB3\_OUT   0x33U |
| --- |

## [◆ ](#a47f54cb1d33b89ee58e4bf11ed48a099)MAX32\_DMA\_SLOT\_USB4\_IN

| #define MAX32\_DMA\_SLOT\_USB4\_IN   0x14U |
| --- |

## [◆ ](#aa10e5db19758fa2983c8e5c8dec1728e)MAX32\_DMA\_SLOT\_USB4\_OUT

| #define MAX32\_DMA\_SLOT\_USB4\_OUT   0x34U |
| --- |

## [◆ ](#a7e2ae2470bd7133deba81786fa3f8112)MAX32\_DMA\_SLOT\_USB5\_IN

| #define MAX32\_DMA\_SLOT\_USB5\_IN   0x15U |
| --- |

## [◆ ](#a3fdbec2e3910715b0505443a761d0199)MAX32\_DMA\_SLOT\_USB5\_OUT

| #define MAX32\_DMA\_SLOT\_USB5\_OUT   0x35U |
| --- |

## [◆ ](#a4c558e41238658fa93a7a1b94812ffe3)MAX32\_DMA\_SLOT\_USB6\_IN

| #define MAX32\_DMA\_SLOT\_USB6\_IN   0x16U |
| --- |

## [◆ ](#aaafe5f2dd2de43fd0df91383fef80888)MAX32\_DMA\_SLOT\_USB6\_OUT

| #define MAX32\_DMA\_SLOT\_USB6\_OUT   0x36U |
| --- |

## [◆ ](#a856fece9c57666f58065ed62a8a4d895)MAX32\_DMA\_SLOT\_USB7\_IN

| #define MAX32\_DMA\_SLOT\_USB7\_IN   0x17U |
| --- |

## [◆ ](#a7f83f6b1831f8d611d89bba5b85e3078)MAX32\_DMA\_SLOT\_USB7\_OUT

| #define MAX32\_DMA\_SLOT\_USB7\_OUT   0x37U |
| --- |

## [◆ ](#a1539f829df18cf805b6e0dd904f67cba)MAX32\_DMA\_SLOT\_USB8\_IN

| #define MAX32\_DMA\_SLOT\_USB8\_IN   0x18U |
| --- |

## [◆ ](#a2c6fc053f7550264605e8e49a07ff4ee)MAX32\_DMA\_SLOT\_USB8\_OUT

| #define MAX32\_DMA\_SLOT\_USB8\_OUT   0x38U |
| --- |

## [◆ ](#a0f6099d8756b2752fd1b61f3367328be)MAX32\_DMA\_SLOT\_USB9\_IN

| #define MAX32\_DMA\_SLOT\_USB9\_IN   0x19U |
| --- |

## [◆ ](#a85621d1cac930edf18367e3230514174)MAX32\_DMA\_SLOT\_USB9\_OUT

| #define MAX32\_DMA\_SLOT\_USB9\_OUT   0x39U |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [dma](dir_4af45c18fedc476f9a2ee26ec98f56f0.md)
- [max32690\_dma.h](max32690__dma_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
