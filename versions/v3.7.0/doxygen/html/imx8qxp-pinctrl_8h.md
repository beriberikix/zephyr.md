---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/imx8qxp-pinctrl_8h.html
original_path: doxygen/html/imx8qxp-pinctrl_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

imx8qxp-pinctrl.h File Reference

[Go to the source code of this file.](imx8qxp-pinctrl_8h_source.md)

| Macros | |
| --- | --- |
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

## Macro Definition Documentation

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
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
