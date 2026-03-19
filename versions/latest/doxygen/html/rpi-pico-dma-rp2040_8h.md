---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/rpi-pico-dma-rp2040_8h.html
original_path: doxygen/html/rpi-pico-dma-rp2040_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rpi-pico-dma-rp2040.h File Reference

`#include "[rpi-pico-dma-common.h](rpi-pico-dma-common_8h_source.md)"`

[Go to the source code of this file.](rpi-pico-dma-rp2040_8h_source.md)

| Macros | |
| --- | --- |
| #define | [RPI\_PICO\_DMA\_SLOT\_SPI0\_TX](#ae18eed6d9f3a59b17d98e1d327d67cf7)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x10) |
| #define | [RPI\_PICO\_DMA\_SLOT\_SPI0\_RX](#aa955cbbf46c4c22ad7a57471aeed4344)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x11) |
| #define | [RPI\_PICO\_DMA\_SLOT\_SPI1\_TX](#a0076112cb2bb0ac30b53ba51b67cde13)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x12) |
| #define | [RPI\_PICO\_DMA\_SLOT\_SPI1\_RX](#a11b34c896fbb7993712f2a6228f0f470)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x13) |
| #define | [RPI\_PICO\_DMA\_SLOT\_UART0\_TX](#a8e4849d94891581e54c20f1ad3053e61)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x14) |
| #define | [RPI\_PICO\_DMA\_SLOT\_UART0\_RX](#a6c9dbf9ae4a775350dba0192d2d22ece)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x15) |
| #define | [RPI\_PICO\_DMA\_SLOT\_UART1\_TX](#ae3b608078bb7b0076565d6ba01b7f2db)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x16) |
| #define | [RPI\_PICO\_DMA\_SLOT\_UART1\_RX](#a867620802abfb1ea68f4de34bd9220c8)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x17) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP0](#aaf7f3a66c0e4bd1ba533c926e088bb72)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x18) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP1](#a4c4d3ebb5cb30a4af4289e72c74ac705)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x19) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP2](#a6807669224a777d8b8342d5a59b87370)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x1A) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP3](#a69039f5a94f8f30f46e488df743d8623)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x1B) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP4](#a16432ea7735d3d2b46696eb42c3a5a78)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x1C) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP5](#a262317a40c039af688969d08b734cb30)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x1D) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP6](#acc46df2f8f0ba68e155eb9dfb78d316b)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x1E) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP7](#acd268446715055b789d0b32527eaec18)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x1F) |
| #define | [RPI\_PICO\_DMA\_SLOT\_I2C0\_TX](#aeb3507fc3e3416b7bedfaebbfe8ba980)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x30) |
| #define | [RPI\_PICO\_DMA\_SLOT\_I2C0\_RX](#a22bdae09d66f57f0b2f26e6bd6b36f31)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x31) |
| #define | [RPI\_PICO\_DMA\_SLOT\_I2C1\_TX](#afa10629c69c563ca959fe692f40bc5bb)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x32) |
| #define | [RPI\_PICO\_DMA\_SLOT\_I2C1\_RX](#a0f6717d3026d1c19c30e84bd4f91511b)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x33) |
| #define | [RPI\_PICO\_DMA\_SLOT\_ADC](#ab9e20d2a674fa5d1947c01a5dc2fb359)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x34) |
| #define | [RPI\_PICO\_DMA\_SLOT\_XIP\_STREAM](#a831f08fba56848125d1e8773c05ac588)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x35) |
| #define | [RPI\_PICO\_DMA\_SLOT\_XIP\_SSITX](#a01f1ea52277e47bff8c3d76d6da7dab3)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x36) |
| #define | [RPI\_PICO\_DMA\_SLOT\_XIP\_SSIRX](#abdb688be5a52ddc5c3aacf2048096987)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x37) |

## Macro Definition Documentation

## [◆ ](#ab9e20d2a674fa5d1947c01a5dc2fb359)RPI\_PICO\_DMA\_SLOT\_ADC

| #define RPI\_PICO\_DMA\_SLOT\_ADC   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x34) |
| --- |

## [◆ ](#a22bdae09d66f57f0b2f26e6bd6b36f31)RPI\_PICO\_DMA\_SLOT\_I2C0\_RX

| #define RPI\_PICO\_DMA\_SLOT\_I2C0\_RX   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x31) |
| --- |

## [◆ ](#aeb3507fc3e3416b7bedfaebbfe8ba980)RPI\_PICO\_DMA\_SLOT\_I2C0\_TX

| #define RPI\_PICO\_DMA\_SLOT\_I2C0\_TX   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x30) |
| --- |

## [◆ ](#a0f6717d3026d1c19c30e84bd4f91511b)RPI\_PICO\_DMA\_SLOT\_I2C1\_RX

| #define RPI\_PICO\_DMA\_SLOT\_I2C1\_RX   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x33) |
| --- |

## [◆ ](#afa10629c69c563ca959fe692f40bc5bb)RPI\_PICO\_DMA\_SLOT\_I2C1\_TX

| #define RPI\_PICO\_DMA\_SLOT\_I2C1\_TX   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x32) |
| --- |

## [◆ ](#aaf7f3a66c0e4bd1ba533c926e088bb72)RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP0

| #define RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP0   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x18) |
| --- |

## [◆ ](#a4c4d3ebb5cb30a4af4289e72c74ac705)RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP1

| #define RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP1   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x19) |
| --- |

## [◆ ](#a6807669224a777d8b8342d5a59b87370)RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP2

| #define RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP2   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x1A) |
| --- |

## [◆ ](#a69039f5a94f8f30f46e488df743d8623)RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP3

| #define RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP3   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x1B) |
| --- |

## [◆ ](#a16432ea7735d3d2b46696eb42c3a5a78)RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP4

| #define RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP4   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x1C) |
| --- |

## [◆ ](#a262317a40c039af688969d08b734cb30)RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP5

| #define RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP5   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x1D) |
| --- |

## [◆ ](#acc46df2f8f0ba68e155eb9dfb78d316b)RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP6

| #define RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP6   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x1E) |
| --- |

## [◆ ](#acd268446715055b789d0b32527eaec18)RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP7

| #define RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP7   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x1F) |
| --- |

## [◆ ](#aa955cbbf46c4c22ad7a57471aeed4344)RPI\_PICO\_DMA\_SLOT\_SPI0\_RX

| #define RPI\_PICO\_DMA\_SLOT\_SPI0\_RX   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x11) |
| --- |

## [◆ ](#ae18eed6d9f3a59b17d98e1d327d67cf7)RPI\_PICO\_DMA\_SLOT\_SPI0\_TX

| #define RPI\_PICO\_DMA\_SLOT\_SPI0\_TX   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x10) |
| --- |

## [◆ ](#a11b34c896fbb7993712f2a6228f0f470)RPI\_PICO\_DMA\_SLOT\_SPI1\_RX

| #define RPI\_PICO\_DMA\_SLOT\_SPI1\_RX   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x13) |
| --- |

## [◆ ](#a0076112cb2bb0ac30b53ba51b67cde13)RPI\_PICO\_DMA\_SLOT\_SPI1\_TX

| #define RPI\_PICO\_DMA\_SLOT\_SPI1\_TX   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x12) |
| --- |

## [◆ ](#a6c9dbf9ae4a775350dba0192d2d22ece)RPI\_PICO\_DMA\_SLOT\_UART0\_RX

| #define RPI\_PICO\_DMA\_SLOT\_UART0\_RX   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x15) |
| --- |

## [◆ ](#a8e4849d94891581e54c20f1ad3053e61)RPI\_PICO\_DMA\_SLOT\_UART0\_TX

| #define RPI\_PICO\_DMA\_SLOT\_UART0\_TX   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x14) |
| --- |

## [◆ ](#a867620802abfb1ea68f4de34bd9220c8)RPI\_PICO\_DMA\_SLOT\_UART1\_RX

| #define RPI\_PICO\_DMA\_SLOT\_UART1\_RX   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x17) |
| --- |

## [◆ ](#ae3b608078bb7b0076565d6ba01b7f2db)RPI\_PICO\_DMA\_SLOT\_UART1\_TX

| #define RPI\_PICO\_DMA\_SLOT\_UART1\_TX   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x16) |
| --- |

## [◆ ](#abdb688be5a52ddc5c3aacf2048096987)RPI\_PICO\_DMA\_SLOT\_XIP\_SSIRX

| #define RPI\_PICO\_DMA\_SLOT\_XIP\_SSIRX   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x37) |
| --- |

## [◆ ](#a01f1ea52277e47bff8c3d76d6da7dab3)RPI\_PICO\_DMA\_SLOT\_XIP\_SSITX

| #define RPI\_PICO\_DMA\_SLOT\_XIP\_SSITX   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x36) |
| --- |

## [◆ ](#a831f08fba56848125d1e8773c05ac588)RPI\_PICO\_DMA\_SLOT\_XIP\_STREAM

| #define RPI\_PICO\_DMA\_SLOT\_XIP\_STREAM   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](rpi-pico-dma-common_8h.md#a108c9650b4eb398c9994d7c1683beaa8)(0x35) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [dma](dir_4af45c18fedc476f9a2ee26ec98f56f0.md)
- [rpi-pico-dma-rp2040.h](rpi-pico-dma-rp2040_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
