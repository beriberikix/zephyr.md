---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/imx8qxp-pinctrl_8h.html
original_path: doxygen/html/imx8qxp-pinctrl_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

imx8qxp-pinctrl.h File Reference

[Go to the source code of this file.](imx8qxp-pinctrl_8h_source.md)

| Macros | |
| --- | --- |
| #define | [SC\_P\_ESAI0\_FSR](#ab701a7700915e279fd94a55242271391)   55 |
| #define | [SC\_P\_ESAI0\_FST](#a5edfd221c1748aaebd1e7ca50bee160d)   56 |
| #define | [SC\_P\_ESAI0\_SCKR](#a7327c9ca8c3a7cf526af8fd06f49979a)   57 |
| #define | [SC\_P\_ESAI0\_SCKT](#a03d21c813e46bd8d0e559ab650cd51cf)   58 |
| #define | [SC\_P\_ESAI0\_TX0](#a47791f7f5bb5e5f5b0b4f3d141939613)   59 |
| #define | [SC\_P\_ESAI0\_TX1](#aae959f150f24fa5573c82673d2015191)   60 |
| #define | [SC\_P\_ESAI0\_TX2\_RX3](#a309087617f868dfc8dfa66431ffb722e)   61 |
| #define | [SC\_P\_ESAI0\_TX3\_RX2](#a9fbef245436e89128f04a293d3ce221d)   62 |
| #define | [SC\_P\_ESAI0\_TX4\_RX1](#ac19274d9c02ae4740501114d638d283a)   63 |
| #define | [SC\_P\_ESAI0\_TX5\_RX0](#a9b4e197a3fdd8d4d41d53cb0e56ce47f)   64 |
| #define | [SC\_P\_SAI1\_RXD](#aed4925b750ea0891fb3ba4a0fd8f764a)   86 |
| #define | [SC\_P\_SAI1\_RXC](#ac10ea2dbe0fe7573b504833ff2686abf)   87 |
| #define | [SC\_P\_SAI1\_RXFS](#acc9613444ebb12360d27006ec13fdc24)   88 |
| #define | [SC\_P\_SPI0\_CS1](#a87a3edc8ce026af85fadad64b3de8df4)   96 |
| #define | [SC\_P\_UART2\_TX](#a439d8a14a740c03a41d84a3f58d2d64f)   113 |
| #define | [SC\_P\_UART2\_RX](#a42bb2e2da91a5928dda46bba414ac396)   114 |
| #define | [IMX8QXP\_DMA\_LPUART2\_RX\_UART2\_RX](#a7b942182de88baca5cd8da3715048750)   0 /\* UART2\_RX ---> DMA\_LPUART2\_RX \*/ |
| #define | [IMX8QXP\_DMA\_LPUART2\_TX\_UART2\_TX](#ac3cca516631d1c243db966e16b4f7b3c)   0 /\* DMA\_LPUART2\_TX ---> UART2\_TX \*/ |
| #define | [IMX8QXP\_ADMA\_SAI1\_TXFS\_SAI1\_RXFS](#a27bf71ba10f35a11d1fd48b6bb7a68ce)   1 /\* ADMA\_SAI1\_TXFS <---> SAI1\_RXFS \*/ |
| #define | [IMX8QXP\_ADMA\_SAI1\_RXD\_SAI1\_RXD](#a365a0d17e3bc273abe7d2ea2fc895552)   0 /\* ADMA\_SAI1\_RXD <--- SAI1\_RXD \*/ |
| #define | [IMX8QXP\_ADMA\_SAI1\_TXC\_SAI1\_RXC](#a302270f6db91a71ecf3294653ee542d5)   1 /\* ADMA\_SAI1\_TXC <---> SAI1\_RXC \*/ |
| #define | [IMX8QXP\_ADMA\_SAI1\_TXD\_SPI0\_CS1](#a4e8796484812bbde8369067b9b232177)   2 /\* ADMA\_SAI1\_TXD ---> SPI0\_CS1 \*/ |
| #define | [IMX8QXP\_ADMA\_ESAI0\_FSR\_ESAI0\_FSR](#a962e53d832c142a0fd9cdef3f916b51d)   0 |
| #define | [IMX8QXP\_ADMA\_ESAI0\_FST\_ESAI0\_FST](#a8278312265ffa6e770ddbc285cc34bac)   0 |
| #define | [IMX8QXP\_ADMA\_ESAI0\_SCKR\_ESAI0\_SCKR](#ad70b586ebedc94f3d3e30d5f121b82ac)   0 |
| #define | [IMX8QXP\_ADMA\_ESAI0\_SCKT\_ESAI0\_SCKT](#a6d06f1e2f8c6c2935f2241114a9e16a5)   0 |
| #define | [IMX8QXP\_ADMA\_ESAI0\_TX0\_ESAI0\_TX0](#a00bb9f97c122aa04f16b025d43409da4)   0 |
| #define | [IMX8QXP\_ADMA\_ESAI0\_TX1\_ESAI0\_TX1](#a08bbf15b8a35868cf78879f84a913e36)   0 |
| #define | [IMX8QXP\_ADMA\_ESAI0\_TX2\_RX3\_ESAI0\_TX2\_RX3](#ad5eddfb8c65b08ea938a0e548fa0a787)   0 |
| #define | [IMX8QXP\_ADMA\_ESAI0\_TX3\_RX2\_ESAI0\_TX3\_RX2](#a2cbc1e5c3012d193e5d7c2395d985b5e)   0 |
| #define | [IMX8QXP\_ADMA\_ESAI0\_TX4\_RX1\_ESAI0\_TX4\_RX1](#a6ef5e2a862f0bf07726b456916a65e52)   0 |
| #define | [IMX8QXP\_ADMA\_ESAI0\_TX5\_RX0\_ESAI0\_TX5\_RX0](#afb4ff3c4a0f8ca346e41e5444a36f797)   0 |

## Macro Definition Documentation

## [◆ ](#a962e53d832c142a0fd9cdef3f916b51d)IMX8QXP\_ADMA\_ESAI0\_FSR\_ESAI0\_FSR

| #define IMX8QXP\_ADMA\_ESAI0\_FSR\_ESAI0\_FSR   0 |
| --- |

## [◆ ](#a8278312265ffa6e770ddbc285cc34bac)IMX8QXP\_ADMA\_ESAI0\_FST\_ESAI0\_FST

| #define IMX8QXP\_ADMA\_ESAI0\_FST\_ESAI0\_FST   0 |
| --- |

## [◆ ](#ad70b586ebedc94f3d3e30d5f121b82ac)IMX8QXP\_ADMA\_ESAI0\_SCKR\_ESAI0\_SCKR

| #define IMX8QXP\_ADMA\_ESAI0\_SCKR\_ESAI0\_SCKR   0 |
| --- |

## [◆ ](#a6d06f1e2f8c6c2935f2241114a9e16a5)IMX8QXP\_ADMA\_ESAI0\_SCKT\_ESAI0\_SCKT

| #define IMX8QXP\_ADMA\_ESAI0\_SCKT\_ESAI0\_SCKT   0 |
| --- |

## [◆ ](#a00bb9f97c122aa04f16b025d43409da4)IMX8QXP\_ADMA\_ESAI0\_TX0\_ESAI0\_TX0

| #define IMX8QXP\_ADMA\_ESAI0\_TX0\_ESAI0\_TX0   0 |
| --- |

## [◆ ](#a08bbf15b8a35868cf78879f84a913e36)IMX8QXP\_ADMA\_ESAI0\_TX1\_ESAI0\_TX1

| #define IMX8QXP\_ADMA\_ESAI0\_TX1\_ESAI0\_TX1   0 |
| --- |

## [◆ ](#ad5eddfb8c65b08ea938a0e548fa0a787)IMX8QXP\_ADMA\_ESAI0\_TX2\_RX3\_ESAI0\_TX2\_RX3

| #define IMX8QXP\_ADMA\_ESAI0\_TX2\_RX3\_ESAI0\_TX2\_RX3   0 |
| --- |

## [◆ ](#a2cbc1e5c3012d193e5d7c2395d985b5e)IMX8QXP\_ADMA\_ESAI0\_TX3\_RX2\_ESAI0\_TX3\_RX2

| #define IMX8QXP\_ADMA\_ESAI0\_TX3\_RX2\_ESAI0\_TX3\_RX2   0 |
| --- |

## [◆ ](#a6ef5e2a862f0bf07726b456916a65e52)IMX8QXP\_ADMA\_ESAI0\_TX4\_RX1\_ESAI0\_TX4\_RX1

| #define IMX8QXP\_ADMA\_ESAI0\_TX4\_RX1\_ESAI0\_TX4\_RX1   0 |
| --- |

## [◆ ](#afb4ff3c4a0f8ca346e41e5444a36f797)IMX8QXP\_ADMA\_ESAI0\_TX5\_RX0\_ESAI0\_TX5\_RX0

| #define IMX8QXP\_ADMA\_ESAI0\_TX5\_RX0\_ESAI0\_TX5\_RX0   0 |
| --- |

## [◆ ](#a365a0d17e3bc273abe7d2ea2fc895552)IMX8QXP\_ADMA\_SAI1\_RXD\_SAI1\_RXD

| #define IMX8QXP\_ADMA\_SAI1\_RXD\_SAI1\_RXD   0 /\* ADMA\_SAI1\_RXD <--- SAI1\_RXD \*/ |
| --- |

## [◆ ](#a302270f6db91a71ecf3294653ee542d5)IMX8QXP\_ADMA\_SAI1\_TXC\_SAI1\_RXC

| #define IMX8QXP\_ADMA\_SAI1\_TXC\_SAI1\_RXC   1 /\* ADMA\_SAI1\_TXC <---> SAI1\_RXC \*/ |
| --- |

## [◆ ](#a4e8796484812bbde8369067b9b232177)IMX8QXP\_ADMA\_SAI1\_TXD\_SPI0\_CS1

| #define IMX8QXP\_ADMA\_SAI1\_TXD\_SPI0\_CS1   2 /\* ADMA\_SAI1\_TXD ---> SPI0\_CS1 \*/ |
| --- |

## [◆ ](#a27bf71ba10f35a11d1fd48b6bb7a68ce)IMX8QXP\_ADMA\_SAI1\_TXFS\_SAI1\_RXFS

| #define IMX8QXP\_ADMA\_SAI1\_TXFS\_SAI1\_RXFS   1 /\* ADMA\_SAI1\_TXFS <---> SAI1\_RXFS \*/ |
| --- |

## [◆ ](#a7b942182de88baca5cd8da3715048750)IMX8QXP\_DMA\_LPUART2\_RX\_UART2\_RX

| #define IMX8QXP\_DMA\_LPUART2\_RX\_UART2\_RX   0 /\* UART2\_RX ---> DMA\_LPUART2\_RX \*/ |
| --- |

## [◆ ](#ac3cca516631d1c243db966e16b4f7b3c)IMX8QXP\_DMA\_LPUART2\_TX\_UART2\_TX

| #define IMX8QXP\_DMA\_LPUART2\_TX\_UART2\_TX   0 /\* DMA\_LPUART2\_TX ---> UART2\_TX \*/ |
| --- |

## [◆ ](#ab701a7700915e279fd94a55242271391)SC\_P\_ESAI0\_FSR

| #define SC\_P\_ESAI0\_FSR   55 |
| --- |

## [◆ ](#a5edfd221c1748aaebd1e7ca50bee160d)SC\_P\_ESAI0\_FST

| #define SC\_P\_ESAI0\_FST   56 |
| --- |

## [◆ ](#a7327c9ca8c3a7cf526af8fd06f49979a)SC\_P\_ESAI0\_SCKR

| #define SC\_P\_ESAI0\_SCKR   57 |
| --- |

## [◆ ](#a03d21c813e46bd8d0e559ab650cd51cf)SC\_P\_ESAI0\_SCKT

| #define SC\_P\_ESAI0\_SCKT   58 |
| --- |

## [◆ ](#a47791f7f5bb5e5f5b0b4f3d141939613)SC\_P\_ESAI0\_TX0

| #define SC\_P\_ESAI0\_TX0   59 |
| --- |

## [◆ ](#aae959f150f24fa5573c82673d2015191)SC\_P\_ESAI0\_TX1

| #define SC\_P\_ESAI0\_TX1   60 |
| --- |

## [◆ ](#a309087617f868dfc8dfa66431ffb722e)SC\_P\_ESAI0\_TX2\_RX3

| #define SC\_P\_ESAI0\_TX2\_RX3   61 |
| --- |

## [◆ ](#a9fbef245436e89128f04a293d3ce221d)SC\_P\_ESAI0\_TX3\_RX2

| #define SC\_P\_ESAI0\_TX3\_RX2   62 |
| --- |

## [◆ ](#ac19274d9c02ae4740501114d638d283a)SC\_P\_ESAI0\_TX4\_RX1

| #define SC\_P\_ESAI0\_TX4\_RX1   63 |
| --- |

## [◆ ](#a9b4e197a3fdd8d4d41d53cb0e56ce47f)SC\_P\_ESAI0\_TX5\_RX0

| #define SC\_P\_ESAI0\_TX5\_RX0   64 |
| --- |

## [◆ ](#ac10ea2dbe0fe7573b504833ff2686abf)SC\_P\_SAI1\_RXC

| #define SC\_P\_SAI1\_RXC   87 |
| --- |

## [◆ ](#aed4925b750ea0891fb3ba4a0fd8f764a)SC\_P\_SAI1\_RXD

| #define SC\_P\_SAI1\_RXD   86 |
| --- |

## [◆ ](#acc9613444ebb12360d27006ec13fdc24)SC\_P\_SAI1\_RXFS

| #define SC\_P\_SAI1\_RXFS   88 |
| --- |

## [◆ ](#a87a3edc8ce026af85fadad64b3de8df4)SC\_P\_SPI0\_CS1

| #define SC\_P\_SPI0\_CS1   96 |
| --- |

## [◆ ](#a42bb2e2da91a5928dda46bba414ac396)SC\_P\_UART2\_RX

| #define SC\_P\_UART2\_RX   114 |
| --- |

## [◆ ](#a439d8a14a740c03a41d84a3f58d2d64f)SC\_P\_UART2\_TX

| #define SC\_P\_UART2\_TX   113 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [imx8qxp-pinctrl.h](imx8qxp-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
