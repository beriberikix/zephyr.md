---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/rpi__pico__dma_8h.html
original_path: doxygen/html/rpi__pico__dma_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rpi\_pico\_dma.h File Reference

[Go to the source code of this file.](rpi__pico__dma_8h_source.md)

| Macros | |
| --- | --- |
| #define | [RPI\_PICO\_DMA\_SLOT\_TO\_DREQ](#af17a4ab6d1b744cb7ba78185681f464b)([s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)) |
| #define | [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)   [RPI\_PICO\_DMA\_SLOT\_TO\_DREQ](#af17a4ab6d1b744cb7ba78185681f464b) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PIO0\_TX0](#ab4efb501d7d6acf7c4e320a992a736c9)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x00) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PIO0\_TX1](#ac83bcbc6b3716d947051d785f60447c1)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x01) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PIO0\_TX2](#ad2452d29f952c828fc38036d3fc8f7c7)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x02) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PIO0\_TX3](#a3be36155cb5c9faff83951e46e1ce6eb)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x03) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PIO0\_RX0](#a4931c164398407d3365d600d17110f95)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x04) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PIO0\_RX1](#a84583ff2852ec17e709f44cfe85a21d1)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x05) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PIO0\_RX2](#a7a30cab865790b3ff4c873cec1ae39a4)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x06) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PIO0\_RX3](#a131cdd1941010a43bebcda6fffd98016)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x07) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PIO1\_TX0](#a17f1642461493cde7e832a1ab78d9f69)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x08) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PIO1\_TX1](#a7a19561e334931146de9a56ce3214680)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x09) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PIO1\_TX2](#ae6f04b3ecc7adfa5bb4e070f6cc29780)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x0A) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PIO1\_TX3](#ab39ac333962fe0debca583061ba1b6cb)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x0B) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PIO1\_RX0](#a7eaaa6b0e6f80021364a66fd75450c0d)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x0C) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PIO1\_RX1](#a9963f9b698a5ffde3e3bcf9b4b43ed22)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x0D) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PIO1\_RX2](#ad1a63c332b00cf4442907a3a11d155d1)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x0E) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PIO1\_RX3](#a07eab28aade43838cf5580e0c0ea3bde)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x0F) |
| #define | [RPI\_PICO\_DMA\_SLOT\_SPI0\_TX](#ae18eed6d9f3a59b17d98e1d327d67cf7)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x10) |
| #define | [RPI\_PICO\_DMA\_SLOT\_SPI0\_RX](#aa955cbbf46c4c22ad7a57471aeed4344)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x11) |
| #define | [RPI\_PICO\_DMA\_SLOT\_SPI1\_TX](#a0076112cb2bb0ac30b53ba51b67cde13)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x12) |
| #define | [RPI\_PICO\_DMA\_SLOT\_SPI1\_RX](#a11b34c896fbb7993712f2a6228f0f470)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x13) |
| #define | [RPI\_PICO\_DMA\_SLOT\_UART0\_TX](#a8e4849d94891581e54c20f1ad3053e61)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x14) |
| #define | [RPI\_PICO\_DMA\_SLOT\_UART0\_RX](#a6c9dbf9ae4a775350dba0192d2d22ece)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x15) |
| #define | [RPI\_PICO\_DMA\_SLOT\_UART1\_TX](#ae3b608078bb7b0076565d6ba01b7f2db)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x16) |
| #define | [RPI\_PICO\_DMA\_SLOT\_UART1\_RX](#a867620802abfb1ea68f4de34bd9220c8)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x17) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP0](#aaf7f3a66c0e4bd1ba533c926e088bb72)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x18) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP1](#a4c4d3ebb5cb30a4af4289e72c74ac705)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x19) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP2](#a6807669224a777d8b8342d5a59b87370)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x1A) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP3](#a69039f5a94f8f30f46e488df743d8623)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x1B) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP4](#a16432ea7735d3d2b46696eb42c3a5a78)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x1C) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP5](#a262317a40c039af688969d08b734cb30)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x1D) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP6](#acc46df2f8f0ba68e155eb9dfb78d316b)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x1E) |
| #define | [RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP7](#acd268446715055b789d0b32527eaec18)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x1F) |
| #define | [RPI\_PICO\_DMA\_SLOT\_I2C0\_TX](#aeb3507fc3e3416b7bedfaebbfe8ba980)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x30) |
| #define | [RPI\_PICO\_DMA\_SLOT\_I2C0\_RX](#a22bdae09d66f57f0b2f26e6bd6b36f31)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x31) |
| #define | [RPI\_PICO\_DMA\_SLOT\_I2C1\_TX](#afa10629c69c563ca959fe692f40bc5bb)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x32) |
| #define | [RPI\_PICO\_DMA\_SLOT\_I2C1\_RX](#a0f6717d3026d1c19c30e84bd4f91511b)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x33) |
| #define | [RPI\_PICO\_DMA\_SLOT\_ADC](#ab9e20d2a674fa5d1947c01a5dc2fb359)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x34) |
| #define | [RPI\_PICO\_DMA\_SLOT\_XIP\_STREAM](#a831f08fba56848125d1e8773c05ac588)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x35) |
| #define | [RPI\_PICO\_DMA\_SLOT\_XIP\_SSITX](#a01f1ea52277e47bff8c3d76d6da7dab3)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x36) |
| #define | [RPI\_PICO\_DMA\_SLOT\_XIP\_SSIRX](#abdb688be5a52ddc5c3aacf2048096987)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x37) |
| #define | [RPI\_PICO\_DMA\_SLOT\_DMA\_TIMER0](#aac94fe3f6411cd4bad422974be560d92)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x3B) |
| #define | [RPI\_PICO\_DMA\_SLOT\_DMA\_TIMER1](#a864c5126bab363926d43b8d2a951a935)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x3C) |
| #define | [RPI\_PICO\_DMA\_SLOT\_DMA\_TIMER2](#a0b8c6347ccfe168d06851fdac5bfe470)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x3D) |
| #define | [RPI\_PICO\_DMA\_SLOT\_DMA\_TIMER3](#aa4cf3c65b88cf11aaadd685363695262)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x3E) |
| #define | [RPI\_PICO\_DMA\_SLOT\_FORCE](#a6571b7502d26dcb0011fa9c38f64f793)   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x3F) |

## Macro Definition Documentation

## [◆ ](#a108c9650b4eb398c9994d7c1683beaa8)RPI\_PICO\_DMA\_DREQ\_TO\_SLOT

| #define RPI\_PICO\_DMA\_DREQ\_TO\_SLOT   [RPI\_PICO\_DMA\_SLOT\_TO\_DREQ](#af17a4ab6d1b744cb7ba78185681f464b) |
| --- |

## [◆ ](#ab9e20d2a674fa5d1947c01a5dc2fb359)RPI\_PICO\_DMA\_SLOT\_ADC

| #define RPI\_PICO\_DMA\_SLOT\_ADC   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x34) |
| --- |

## [◆ ](#aac94fe3f6411cd4bad422974be560d92)RPI\_PICO\_DMA\_SLOT\_DMA\_TIMER0

| #define RPI\_PICO\_DMA\_SLOT\_DMA\_TIMER0   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x3B) |
| --- |

## [◆ ](#a864c5126bab363926d43b8d2a951a935)RPI\_PICO\_DMA\_SLOT\_DMA\_TIMER1

| #define RPI\_PICO\_DMA\_SLOT\_DMA\_TIMER1   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x3C) |
| --- |

## [◆ ](#a0b8c6347ccfe168d06851fdac5bfe470)RPI\_PICO\_DMA\_SLOT\_DMA\_TIMER2

| #define RPI\_PICO\_DMA\_SLOT\_DMA\_TIMER2   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x3D) |
| --- |

## [◆ ](#aa4cf3c65b88cf11aaadd685363695262)RPI\_PICO\_DMA\_SLOT\_DMA\_TIMER3

| #define RPI\_PICO\_DMA\_SLOT\_DMA\_TIMER3   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x3E) |
| --- |

## [◆ ](#a6571b7502d26dcb0011fa9c38f64f793)RPI\_PICO\_DMA\_SLOT\_FORCE

| #define RPI\_PICO\_DMA\_SLOT\_FORCE   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x3F) |
| --- |

## [◆ ](#a22bdae09d66f57f0b2f26e6bd6b36f31)RPI\_PICO\_DMA\_SLOT\_I2C0\_RX

| #define RPI\_PICO\_DMA\_SLOT\_I2C0\_RX   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x31) |
| --- |

## [◆ ](#aeb3507fc3e3416b7bedfaebbfe8ba980)RPI\_PICO\_DMA\_SLOT\_I2C0\_TX

| #define RPI\_PICO\_DMA\_SLOT\_I2C0\_TX   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x30) |
| --- |

## [◆ ](#a0f6717d3026d1c19c30e84bd4f91511b)RPI\_PICO\_DMA\_SLOT\_I2C1\_RX

| #define RPI\_PICO\_DMA\_SLOT\_I2C1\_RX   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x33) |
| --- |

## [◆ ](#afa10629c69c563ca959fe692f40bc5bb)RPI\_PICO\_DMA\_SLOT\_I2C1\_TX

| #define RPI\_PICO\_DMA\_SLOT\_I2C1\_TX   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x32) |
| --- |

## [◆ ](#a4931c164398407d3365d600d17110f95)RPI\_PICO\_DMA\_SLOT\_PIO0\_RX0

| #define RPI\_PICO\_DMA\_SLOT\_PIO0\_RX0   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x04) |
| --- |

## [◆ ](#a84583ff2852ec17e709f44cfe85a21d1)RPI\_PICO\_DMA\_SLOT\_PIO0\_RX1

| #define RPI\_PICO\_DMA\_SLOT\_PIO0\_RX1   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x05) |
| --- |

## [◆ ](#a7a30cab865790b3ff4c873cec1ae39a4)RPI\_PICO\_DMA\_SLOT\_PIO0\_RX2

| #define RPI\_PICO\_DMA\_SLOT\_PIO0\_RX2   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x06) |
| --- |

## [◆ ](#a131cdd1941010a43bebcda6fffd98016)RPI\_PICO\_DMA\_SLOT\_PIO0\_RX3

| #define RPI\_PICO\_DMA\_SLOT\_PIO0\_RX3   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x07) |
| --- |

## [◆ ](#ab4efb501d7d6acf7c4e320a992a736c9)RPI\_PICO\_DMA\_SLOT\_PIO0\_TX0

| #define RPI\_PICO\_DMA\_SLOT\_PIO0\_TX0   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x00) |
| --- |

## [◆ ](#ac83bcbc6b3716d947051d785f60447c1)RPI\_PICO\_DMA\_SLOT\_PIO0\_TX1

| #define RPI\_PICO\_DMA\_SLOT\_PIO0\_TX1   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x01) |
| --- |

## [◆ ](#ad2452d29f952c828fc38036d3fc8f7c7)RPI\_PICO\_DMA\_SLOT\_PIO0\_TX2

| #define RPI\_PICO\_DMA\_SLOT\_PIO0\_TX2   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x02) |
| --- |

## [◆ ](#a3be36155cb5c9faff83951e46e1ce6eb)RPI\_PICO\_DMA\_SLOT\_PIO0\_TX3

| #define RPI\_PICO\_DMA\_SLOT\_PIO0\_TX3   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x03) |
| --- |

## [◆ ](#a7eaaa6b0e6f80021364a66fd75450c0d)RPI\_PICO\_DMA\_SLOT\_PIO1\_RX0

| #define RPI\_PICO\_DMA\_SLOT\_PIO1\_RX0   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x0C) |
| --- |

## [◆ ](#a9963f9b698a5ffde3e3bcf9b4b43ed22)RPI\_PICO\_DMA\_SLOT\_PIO1\_RX1

| #define RPI\_PICO\_DMA\_SLOT\_PIO1\_RX1   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x0D) |
| --- |

## [◆ ](#ad1a63c332b00cf4442907a3a11d155d1)RPI\_PICO\_DMA\_SLOT\_PIO1\_RX2

| #define RPI\_PICO\_DMA\_SLOT\_PIO1\_RX2   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x0E) |
| --- |

## [◆ ](#a07eab28aade43838cf5580e0c0ea3bde)RPI\_PICO\_DMA\_SLOT\_PIO1\_RX3

| #define RPI\_PICO\_DMA\_SLOT\_PIO1\_RX3   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x0F) |
| --- |

## [◆ ](#a17f1642461493cde7e832a1ab78d9f69)RPI\_PICO\_DMA\_SLOT\_PIO1\_TX0

| #define RPI\_PICO\_DMA\_SLOT\_PIO1\_TX0   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x08) |
| --- |

## [◆ ](#a7a19561e334931146de9a56ce3214680)RPI\_PICO\_DMA\_SLOT\_PIO1\_TX1

| #define RPI\_PICO\_DMA\_SLOT\_PIO1\_TX1   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x09) |
| --- |

## [◆ ](#ae6f04b3ecc7adfa5bb4e070f6cc29780)RPI\_PICO\_DMA\_SLOT\_PIO1\_TX2

| #define RPI\_PICO\_DMA\_SLOT\_PIO1\_TX2   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x0A) |
| --- |

## [◆ ](#ab39ac333962fe0debca583061ba1b6cb)RPI\_PICO\_DMA\_SLOT\_PIO1\_TX3

| #define RPI\_PICO\_DMA\_SLOT\_PIO1\_TX3   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x0B) |
| --- |

## [◆ ](#aaf7f3a66c0e4bd1ba533c926e088bb72)RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP0

| #define RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP0   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x18) |
| --- |

## [◆ ](#a4c4d3ebb5cb30a4af4289e72c74ac705)RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP1

| #define RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP1   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x19) |
| --- |

## [◆ ](#a6807669224a777d8b8342d5a59b87370)RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP2

| #define RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP2   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x1A) |
| --- |

## [◆ ](#a69039f5a94f8f30f46e488df743d8623)RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP3

| #define RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP3   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x1B) |
| --- |

## [◆ ](#a16432ea7735d3d2b46696eb42c3a5a78)RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP4

| #define RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP4   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x1C) |
| --- |

## [◆ ](#a262317a40c039af688969d08b734cb30)RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP5

| #define RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP5   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x1D) |
| --- |

## [◆ ](#acc46df2f8f0ba68e155eb9dfb78d316b)RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP6

| #define RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP6   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x1E) |
| --- |

## [◆ ](#acd268446715055b789d0b32527eaec18)RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP7

| #define RPI\_PICO\_DMA\_SLOT\_PWM\_WRAP7   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x1F) |
| --- |

## [◆ ](#aa955cbbf46c4c22ad7a57471aeed4344)RPI\_PICO\_DMA\_SLOT\_SPI0\_RX

| #define RPI\_PICO\_DMA\_SLOT\_SPI0\_RX   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x11) |
| --- |

## [◆ ](#ae18eed6d9f3a59b17d98e1d327d67cf7)RPI\_PICO\_DMA\_SLOT\_SPI0\_TX

| #define RPI\_PICO\_DMA\_SLOT\_SPI0\_TX   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x10) |
| --- |

## [◆ ](#a11b34c896fbb7993712f2a6228f0f470)RPI\_PICO\_DMA\_SLOT\_SPI1\_RX

| #define RPI\_PICO\_DMA\_SLOT\_SPI1\_RX   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x13) |
| --- |

## [◆ ](#a0076112cb2bb0ac30b53ba51b67cde13)RPI\_PICO\_DMA\_SLOT\_SPI1\_TX

| #define RPI\_PICO\_DMA\_SLOT\_SPI1\_TX   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x12) |
| --- |

## [◆ ](#af17a4ab6d1b744cb7ba78185681f464b)RPI\_PICO\_DMA\_SLOT\_TO\_DREQ

| #define RPI\_PICO\_DMA\_SLOT\_TO\_DREQ | ( |  | *[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(~([s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d))&0x3F)

[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)

irp nz macro MOVR cc s mov cc s endm endr irp aw macro LDR aa s

**Definition** asm-macro-32-bit-gnu.h:17

## [◆ ](#a6c9dbf9ae4a775350dba0192d2d22ece)RPI\_PICO\_DMA\_SLOT\_UART0\_RX

| #define RPI\_PICO\_DMA\_SLOT\_UART0\_RX   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x15) |
| --- |

## [◆ ](#a8e4849d94891581e54c20f1ad3053e61)RPI\_PICO\_DMA\_SLOT\_UART0\_TX

| #define RPI\_PICO\_DMA\_SLOT\_UART0\_TX   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x14) |
| --- |

## [◆ ](#a867620802abfb1ea68f4de34bd9220c8)RPI\_PICO\_DMA\_SLOT\_UART1\_RX

| #define RPI\_PICO\_DMA\_SLOT\_UART1\_RX   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x17) |
| --- |

## [◆ ](#ae3b608078bb7b0076565d6ba01b7f2db)RPI\_PICO\_DMA\_SLOT\_UART1\_TX

| #define RPI\_PICO\_DMA\_SLOT\_UART1\_TX   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x16) |
| --- |

## [◆ ](#abdb688be5a52ddc5c3aacf2048096987)RPI\_PICO\_DMA\_SLOT\_XIP\_SSIRX

| #define RPI\_PICO\_DMA\_SLOT\_XIP\_SSIRX   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x37) |
| --- |

## [◆ ](#a01f1ea52277e47bff8c3d76d6da7dab3)RPI\_PICO\_DMA\_SLOT\_XIP\_SSITX

| #define RPI\_PICO\_DMA\_SLOT\_XIP\_SSITX   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x36) |
| --- |

## [◆ ](#a831f08fba56848125d1e8773c05ac588)RPI\_PICO\_DMA\_SLOT\_XIP\_STREAM

| #define RPI\_PICO\_DMA\_SLOT\_XIP\_STREAM   [RPI\_PICO\_DMA\_DREQ\_TO\_SLOT](#a108c9650b4eb398c9994d7c1683beaa8)(0x35) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [dma](dir_4af45c18fedc476f9a2ee26ec98f56f0.md)
- [rpi\_pico\_dma.h](rpi__pico__dma_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
