---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/arm-mps4-pinctrl_8h.html
original_path: doxygen/html/arm-mps4-pinctrl_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arm-mps4-pinctrl.h File Reference

[Go to the source code of this file.](arm-mps4-pinctrl_8h_source.md)

| Macros | |
| --- | --- |
| #define | [MPS4\_ALT\_FUNC\_POS](#a8afa19b922051b18516de109ef91cfb2)   0 |
| #define | [MPS4\_ALT\_FUNC\_MASK](#a7499c07aa7f241ae37a8600ab3516025)   0x7 |
| #define | [MPS4\_EXP\_NUM\_POS](#a1b4bb85578599bcbe2d5abcd82ae5059)   3 |
| #define | [MPS4\_EXP\_NUM\_MASK](#a835b77789dd9e689e35f4fbdf8ae4b0c)   0x1F8 |
| #define | [MPS4\_PINCTRL\_FUNC\_UART](#aacc441eeb486384a97b6d495b7ede5b6)   0 |
| #define | [MPS4\_PINCTRL\_FUNC\_GPIO](#abce528e0feff0ea28504196171437878)   1 |
| #define | [MPS4\_PINCTRL\_FUNC\_I2C](#acd848d6b9cd67310c7678c9c814d019d)   2 |
| #define | [MPS4\_PINCTRL\_FUNC\_SPI](#af70280000f1f8d002f0eee7938595220)   3 |
| #define | [MPS4\_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)(alt\_func, exp\_num) |
| #define | [UART3\_RXD\_EXP](#aad1ef19e8c46127baf5ddb680f4a9c2e)   [MPS4\_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)([MPS4\_PINCTRL\_FUNC\_UART](#aacc441eeb486384a97b6d495b7ede5b6), 0) |
| #define | [UART3\_TXD\_EXP](#aab7f8b8584aa06a033aa1e93200eb0d6)   [MPS4\_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)([MPS4\_PINCTRL\_FUNC\_UART](#aacc441eeb486384a97b6d495b7ede5b6), 1) |
| #define | [SPI3\_SS\_EXP](#ae1f9ab03b508c087a9190d742b67fc2a)   [MPS4\_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)([MPS4\_PINCTRL\_FUNC\_SPI](#af70280000f1f8d002f0eee7938595220), 10) |
| #define | [SPI3\_MOSI\_EXP](#a95f2fe6603f5ab5de9c410dfaf87dc52)   [MPS4\_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)([MPS4\_PINCTRL\_FUNC\_SPI](#af70280000f1f8d002f0eee7938595220), 11) |
| #define | [SPI3\_MISO\_EXP](#a14c932b34877e7b1f004bdf3edfdcd4b)   [MPS4\_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)([MPS4\_PINCTRL\_FUNC\_SPI](#af70280000f1f8d002f0eee7938595220), 12) |
| #define | [SPI3\_SCK\_EXP](#ac3801e4481859951369757ac96612165)   [MPS4\_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)([MPS4\_PINCTRL\_FUNC\_SPI](#af70280000f1f8d002f0eee7938595220), 13) |
| #define | [SBCON2\_SDA\_EXP](#a8c2f848c26c691ce333e05fe17c9341d)   [MPS4\_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)([MPS4\_PINCTRL\_FUNC\_I2C](#acd848d6b9cd67310c7678c9c814d019d), 14) |
| #define | [SBCON2\_SCL\_EXP](#a301bb93777a77d4fcbed8617edbe319a)   [MPS4\_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)([MPS4\_PINCTRL\_FUNC\_I2C](#acd848d6b9cd67310c7678c9c814d019d), 15) |
| #define | [UART4\_RXD\_EXP](#a960b6b4bf5810595c274fab5842189e4)   [MPS4\_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)([MPS4\_PINCTRL\_FUNC\_UART](#aacc441eeb486384a97b6d495b7ede5b6), 16) |
| #define | [UART4\_TXD\_EXP](#a8f2f8e4cb191c641dad8dff6c4753e38)   [MPS4\_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)([MPS4\_PINCTRL\_FUNC\_UART](#aacc441eeb486384a97b6d495b7ede5b6), 17) |
| #define | [SPI4\_SS\_EXP](#a525321e1403275e09014f3ff1fa88d78)   [MPS4\_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)([MPS4\_PINCTRL\_FUNC\_SPI](#af70280000f1f8d002f0eee7938595220), 26) |
| #define | [SPI4\_MOSI\_EXP](#aa73c8c56e661787cc05b131f86a8478c)   [MPS4\_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)([MPS4\_PINCTRL\_FUNC\_SPI](#af70280000f1f8d002f0eee7938595220), 27) |
| #define | [SPI4\_MISO\_EXP](#a9709eee41e54142558c4930f1b034043)   [MPS4\_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)([MPS4\_PINCTRL\_FUNC\_SPI](#af70280000f1f8d002f0eee7938595220), 28) |
| #define | [SPI4\_SCK\_EXP](#aa48a51e34a517797511e7214ad00b7de)   [MPS4\_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)([MPS4\_PINCTRL\_FUNC\_SPI](#af70280000f1f8d002f0eee7938595220), 29) |
| #define | [SBCON3\_SDA\_EXP](#a1f600b98990e17441e52f65cc0dabddb)   [MPS4\_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)([MPS4\_PINCTRL\_FUNC\_I2C](#acd848d6b9cd67310c7678c9c814d019d), 30) |
| #define | [SBCON3\_SCL\_EXP](#a42708eb48f46a3dd04242b446389057b)   [MPS4\_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)([MPS4\_PINCTRL\_FUNC\_I2C](#acd848d6b9cd67310c7678c9c814d019d), 31) |

## Macro Definition Documentation

## [◆ ](#a7499c07aa7f241ae37a8600ab3516025)MPS4\_ALT\_FUNC\_MASK

| #define MPS4\_ALT\_FUNC\_MASK   0x7 |
| --- |

## [◆ ](#a8afa19b922051b18516de109ef91cfb2)MPS4\_ALT\_FUNC\_POS

| #define MPS4\_ALT\_FUNC\_POS   0 |
| --- |

## [◆ ](#a835b77789dd9e689e35f4fbdf8ae4b0c)MPS4\_EXP\_NUM\_MASK

| #define MPS4\_EXP\_NUM\_MASK   0x1F8 |
| --- |

## [◆ ](#a1b4bb85578599bcbe2d5abcd82ae5059)MPS4\_EXP\_NUM\_POS

| #define MPS4\_EXP\_NUM\_POS   3 |
| --- |

## [◆ ](#abce528e0feff0ea28504196171437878)MPS4\_PINCTRL\_FUNC\_GPIO

| #define MPS4\_PINCTRL\_FUNC\_GPIO   1 |
| --- |

## [◆ ](#acd848d6b9cd67310c7678c9c814d019d)MPS4\_PINCTRL\_FUNC\_I2C

| #define MPS4\_PINCTRL\_FUNC\_I2C   2 |
| --- |

## [◆ ](#af70280000f1f8d002f0eee7938595220)MPS4\_PINCTRL\_FUNC\_SPI

| #define MPS4\_PINCTRL\_FUNC\_SPI   3 |
| --- |

## [◆ ](#aacc441eeb486384a97b6d495b7ede5b6)MPS4\_PINCTRL\_FUNC\_UART

| #define MPS4\_PINCTRL\_FUNC\_UART   0 |
| --- |

## [◆ ](#aeea5b5140183c5d992cc3b786d43a9ba)MPS4\_PINMUX

| #define MPS4\_PINMUX | ( |  | *alt\_func*, |
| --- | --- | --- | --- |
|  |  |  | *exp\_num* ) |

**Value:**

(exp\_num << [MPS4\_EXP\_NUM\_POS](#a1b4bb85578599bcbe2d5abcd82ae5059) | \

alt\_func << [MPS4\_ALT\_FUNC\_POS](#a8afa19b922051b18516de109ef91cfb2))

[MPS4\_EXP\_NUM\_POS](#a1b4bb85578599bcbe2d5abcd82ae5059)

#define MPS4\_EXP\_NUM\_POS

**Definition** arm-mps4-pinctrl.h:10

[MPS4\_ALT\_FUNC\_POS](#a8afa19b922051b18516de109ef91cfb2)

#define MPS4\_ALT\_FUNC\_POS

**Definition** arm-mps4-pinctrl.h:7

## [◆ ](#a301bb93777a77d4fcbed8617edbe319a)SBCON2\_SCL\_EXP

| #define SBCON2\_SCL\_EXP   [MPS4\_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)([MPS4\_PINCTRL\_FUNC\_I2C](#acd848d6b9cd67310c7678c9c814d019d), 15) |
| --- |

## [◆ ](#a8c2f848c26c691ce333e05fe17c9341d)SBCON2\_SDA\_EXP

| #define SBCON2\_SDA\_EXP   [MPS4\_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)([MPS4\_PINCTRL\_FUNC\_I2C](#acd848d6b9cd67310c7678c9c814d019d), 14) |
| --- |

## [◆ ](#a42708eb48f46a3dd04242b446389057b)SBCON3\_SCL\_EXP

| #define SBCON3\_SCL\_EXP   [MPS4\_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)([MPS4\_PINCTRL\_FUNC\_I2C](#acd848d6b9cd67310c7678c9c814d019d), 31) |
| --- |

## [◆ ](#a1f600b98990e17441e52f65cc0dabddb)SBCON3\_SDA\_EXP

| #define SBCON3\_SDA\_EXP   [MPS4\_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)([MPS4\_PINCTRL\_FUNC\_I2C](#acd848d6b9cd67310c7678c9c814d019d), 30) |
| --- |

## [◆ ](#a14c932b34877e7b1f004bdf3edfdcd4b)SPI3\_MISO\_EXP

| #define SPI3\_MISO\_EXP   [MPS4\_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)([MPS4\_PINCTRL\_FUNC\_SPI](#af70280000f1f8d002f0eee7938595220), 12) |
| --- |

## [◆ ](#a95f2fe6603f5ab5de9c410dfaf87dc52)SPI3\_MOSI\_EXP

| #define SPI3\_MOSI\_EXP   [MPS4\_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)([MPS4\_PINCTRL\_FUNC\_SPI](#af70280000f1f8d002f0eee7938595220), 11) |
| --- |

## [◆ ](#ac3801e4481859951369757ac96612165)SPI3\_SCK\_EXP

| #define SPI3\_SCK\_EXP   [MPS4\_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)([MPS4\_PINCTRL\_FUNC\_SPI](#af70280000f1f8d002f0eee7938595220), 13) |
| --- |

## [◆ ](#ae1f9ab03b508c087a9190d742b67fc2a)SPI3\_SS\_EXP

| #define SPI3\_SS\_EXP   [MPS4\_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)([MPS4\_PINCTRL\_FUNC\_SPI](#af70280000f1f8d002f0eee7938595220), 10) |
| --- |

## [◆ ](#a9709eee41e54142558c4930f1b034043)SPI4\_MISO\_EXP

| #define SPI4\_MISO\_EXP   [MPS4\_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)([MPS4\_PINCTRL\_FUNC\_SPI](#af70280000f1f8d002f0eee7938595220), 28) |
| --- |

## [◆ ](#aa73c8c56e661787cc05b131f86a8478c)SPI4\_MOSI\_EXP

| #define SPI4\_MOSI\_EXP   [MPS4\_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)([MPS4\_PINCTRL\_FUNC\_SPI](#af70280000f1f8d002f0eee7938595220), 27) |
| --- |

## [◆ ](#aa48a51e34a517797511e7214ad00b7de)SPI4\_SCK\_EXP

| #define SPI4\_SCK\_EXP   [MPS4\_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)([MPS4\_PINCTRL\_FUNC\_SPI](#af70280000f1f8d002f0eee7938595220), 29) |
| --- |

## [◆ ](#a525321e1403275e09014f3ff1fa88d78)SPI4\_SS\_EXP

| #define SPI4\_SS\_EXP   [MPS4\_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)([MPS4\_PINCTRL\_FUNC\_SPI](#af70280000f1f8d002f0eee7938595220), 26) |
| --- |

## [◆ ](#aad1ef19e8c46127baf5ddb680f4a9c2e)UART3\_RXD\_EXP

| #define UART3\_RXD\_EXP   [MPS4\_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)([MPS4\_PINCTRL\_FUNC\_UART](#aacc441eeb486384a97b6d495b7ede5b6), 0) |
| --- |

## [◆ ](#aab7f8b8584aa06a033aa1e93200eb0d6)UART3\_TXD\_EXP

| #define UART3\_TXD\_EXP   [MPS4\_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)([MPS4\_PINCTRL\_FUNC\_UART](#aacc441eeb486384a97b6d495b7ede5b6), 1) |
| --- |

## [◆ ](#a960b6b4bf5810595c274fab5842189e4)UART4\_RXD\_EXP

| #define UART4\_RXD\_EXP   [MPS4\_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)([MPS4\_PINCTRL\_FUNC\_UART](#aacc441eeb486384a97b6d495b7ede5b6), 16) |
| --- |

## [◆ ](#a8f2f8e4cb191c641dad8dff6c4753e38)UART4\_TXD\_EXP

| #define UART4\_TXD\_EXP   [MPS4\_PINMUX](#aeea5b5140183c5d992cc3b786d43a9ba)([MPS4\_PINCTRL\_FUNC\_UART](#aacc441eeb486384a97b6d495b7ede5b6), 17) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [arm-mps4-pinctrl.h](arm-mps4-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
