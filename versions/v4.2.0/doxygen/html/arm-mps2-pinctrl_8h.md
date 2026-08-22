---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/arm-mps2-pinctrl_8h.html
original_path: doxygen/html/arm-mps2-pinctrl_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arm-mps2-pinctrl.h File Reference

[Go to the source code of this file.](arm-mps2-pinctrl_8h_source.md)

| Macros | |
| --- | --- |
| #define | [MPS2\_ALT\_FUNC\_POS](#ad565796e43c28185243be8c71f910e3f)   0 |
| #define | [MPS2\_ALT\_FUNC\_MASK](#a6ba3abb5ab20065ea59cb44a2b12f09e)   0x3 |
| #define | [MPS2\_EXP\_NUM\_POS](#a8fc17b69bcffa4039b207b6a4ab7475d)   2 |
| #define | [MPS2\_EXP\_NUM\_MASK](#a98780dae8c8964bbcce2007cf5186b64)   0x3F |
| #define | [MPS2\_PINCTRL\_FUNC\_UART](#a793e19909cf9cdd9fb1aa0a34f835c65)   0 |
| #define | [MPS2\_PINCTRL\_FUNC\_GPIO](#af7cfe8556e424a3018d0e62e62f1b210)   1 |
| #define | [MPS2\_PINCTRL\_FUNC\_I2C](#a33857f12895ab4ffb8bac15a226d9e44)   2 |
| #define | [MPS2\_PINCTRL\_FUNC\_SPI](#a459cfc88b65ae738b2a94be1fbe6df46)   3 |
| #define | [MPS2\_PINMUX](#affba791a0c60352a28b3d8f122534540)(alt\_func, exp\_num) |
| #define | [UART3\_RXD\_EXP](#aad1ef19e8c46127baf5ddb680f4a9c2e)   [MPS2\_PINMUX](#affba791a0c60352a28b3d8f122534540)([MPS2\_PINCTRL\_FUNC\_UART](#a793e19909cf9cdd9fb1aa0a34f835c65), 0) |
| #define | [UART3\_TXD\_EXP](#aab7f8b8584aa06a033aa1e93200eb0d6)   [MPS2\_PINMUX](#affba791a0c60352a28b3d8f122534540)([MPS2\_PINCTRL\_FUNC\_UART](#a793e19909cf9cdd9fb1aa0a34f835c65), 4) |
| #define | [SBCON2\_SCL\_EXP](#a301bb93777a77d4fcbed8617edbe319a)   [MPS2\_PINMUX](#affba791a0c60352a28b3d8f122534540)([MPS2\_PINCTRL\_FUNC\_I2C](#a33857f12895ab4ffb8bac15a226d9e44), 5) |
| #define | [SBCON2\_SDA\_EXP](#a8c2f848c26c691ce333e05fe17c9341d)   [MPS2\_PINMUX](#affba791a0c60352a28b3d8f122534540)([MPS2\_PINCTRL\_FUNC\_I2C](#a33857f12895ab4ffb8bac15a226d9e44), 15) |
| #define | [SPI3\_SCK\_EXP](#ac3801e4481859951369757ac96612165)   [MPS2\_PINMUX](#affba791a0c60352a28b3d8f122534540)([MPS2\_PINCTRL\_FUNC\_SPI](#a459cfc88b65ae738b2a94be1fbe6df46), 11) |
| #define | [SPI3\_SS\_EXP](#ae1f9ab03b508c087a9190d742b67fc2a)   [MPS2\_PINMUX](#affba791a0c60352a28b3d8f122534540)([MPS2\_PINCTRL\_FUNC\_SPI](#a459cfc88b65ae738b2a94be1fbe6df46), 12) |
| #define | [SPI3\_MOSI\_EXP](#a95f2fe6603f5ab5de9c410dfaf87dc52)   [MPS2\_PINMUX](#affba791a0c60352a28b3d8f122534540)([MPS2\_PINCTRL\_FUNC\_SPI](#a459cfc88b65ae738b2a94be1fbe6df46), 13) |
| #define | [SPI3\_MISO\_EXP](#a14c932b34877e7b1f004bdf3edfdcd4b)   [MPS2\_PINMUX](#affba791a0c60352a28b3d8f122534540)([MPS2\_PINCTRL\_FUNC\_SPI](#a459cfc88b65ae738b2a94be1fbe6df46), 14) |
| #define | [SPI2\_SS\_EXP](#af8e71afd57806fbe85b504ac68879fa6)   [MPS2\_PINMUX](#affba791a0c60352a28b3d8f122534540)([MPS2\_PINCTRL\_FUNC\_SPI](#a459cfc88b65ae738b2a94be1fbe6df46), 16) |
| #define | [SPI2\_MISO\_EXP](#af0e38d71c2b6d7cb6f1238e17e8fff6f)   [MPS2\_PINMUX](#affba791a0c60352a28b3d8f122534540)([MPS2\_PINCTRL\_FUNC\_SPI](#a459cfc88b65ae738b2a94be1fbe6df46), 17) |
| #define | [SPI2\_MOSI\_EXP](#a32eff7bbffdfc00975ff1b5f3281eaa1)   [MPS2\_PINMUX](#affba791a0c60352a28b3d8f122534540)([MPS2\_PINCTRL\_FUNC\_SPI](#a459cfc88b65ae738b2a94be1fbe6df46), 18) |
| #define | [SPI2\_SCK\_EXP](#a6fbdf386063229b64599d3c2071ebffd)   [MPS2\_PINMUX](#affba791a0c60352a28b3d8f122534540)([MPS2\_PINCTRL\_FUNC\_SPI](#a459cfc88b65ae738b2a94be1fbe6df46), 19) |
| #define | [UART4\_RXD\_EXP](#a960b6b4bf5810595c274fab5842189e4)   [MPS2\_PINMUX](#affba791a0c60352a28b3d8f122534540)([MPS2\_PINCTRL\_FUNC\_UART](#a793e19909cf9cdd9fb1aa0a34f835c65), 26) |
| #define | [UART4\_TXD\_EXP](#a8f2f8e4cb191c641dad8dff6c4753e38)   [MPS2\_PINMUX](#affba791a0c60352a28b3d8f122534540)([MPS2\_PINCTRL\_FUNC\_UART](#a793e19909cf9cdd9fb1aa0a34f835c65), 30) |
| #define | [SBCON3\_SCL\_EXP](#a42708eb48f46a3dd04242b446389057b)   [MPS2\_PINMUX](#affba791a0c60352a28b3d8f122534540)([MPS2\_PINCTRL\_FUNC\_I2C](#a33857f12895ab4ffb8bac15a226d9e44), 31) |
| #define | [SBCON3\_SDA\_EXP](#a1f600b98990e17441e52f65cc0dabddb)   [MPS2\_PINMUX](#affba791a0c60352a28b3d8f122534540)([MPS2\_PINCTRL\_FUNC\_I2C](#a33857f12895ab4ffb8bac15a226d9e44), 41) |
| #define | [SPI4\_SS\_EXP](#a525321e1403275e09014f3ff1fa88d78)   [MPS2\_PINMUX](#affba791a0c60352a28b3d8f122534540)([MPS2\_PINCTRL\_FUNC\_SPI](#a459cfc88b65ae738b2a94be1fbe6df46), 38) |
| #define | [SPI4\_MOSI\_EXP](#aa73c8c56e661787cc05b131f86a8478c)   [MPS2\_PINMUX](#affba791a0c60352a28b3d8f122534540)([MPS2\_PINCTRL\_FUNC\_SPI](#a459cfc88b65ae738b2a94be1fbe6df46), 39) |
| #define | [SPI4\_MISO\_EXP](#a9709eee41e54142558c4930f1b034043)   [MPS2\_PINMUX](#affba791a0c60352a28b3d8f122534540)([MPS2\_PINCTRL\_FUNC\_SPI](#a459cfc88b65ae738b2a94be1fbe6df46), 40) |
| #define | [SPI4\_SCK\_EXP](#aa48a51e34a517797511e7214ad00b7de)   [MPS2\_PINMUX](#affba791a0c60352a28b3d8f122534540)([MPS2\_PINCTRL\_FUNC\_SPI](#a459cfc88b65ae738b2a94be1fbe6df46), 44) |

## Macro Definition Documentation

## [◆ ](#a6ba3abb5ab20065ea59cb44a2b12f09e)MPS2\_ALT\_FUNC\_MASK

| #define MPS2\_ALT\_FUNC\_MASK   0x3 |
| --- |

## [◆ ](#ad565796e43c28185243be8c71f910e3f)MPS2\_ALT\_FUNC\_POS

| #define MPS2\_ALT\_FUNC\_POS   0 |
| --- |

## [◆ ](#a98780dae8c8964bbcce2007cf5186b64)MPS2\_EXP\_NUM\_MASK

| #define MPS2\_EXP\_NUM\_MASK   0x3F |
| --- |

## [◆ ](#a8fc17b69bcffa4039b207b6a4ab7475d)MPS2\_EXP\_NUM\_POS

| #define MPS2\_EXP\_NUM\_POS   2 |
| --- |

## [◆ ](#af7cfe8556e424a3018d0e62e62f1b210)MPS2\_PINCTRL\_FUNC\_GPIO

| #define MPS2\_PINCTRL\_FUNC\_GPIO   1 |
| --- |

## [◆ ](#a33857f12895ab4ffb8bac15a226d9e44)MPS2\_PINCTRL\_FUNC\_I2C

| #define MPS2\_PINCTRL\_FUNC\_I2C   2 |
| --- |

## [◆ ](#a459cfc88b65ae738b2a94be1fbe6df46)MPS2\_PINCTRL\_FUNC\_SPI

| #define MPS2\_PINCTRL\_FUNC\_SPI   3 |
| --- |

## [◆ ](#a793e19909cf9cdd9fb1aa0a34f835c65)MPS2\_PINCTRL\_FUNC\_UART

| #define MPS2\_PINCTRL\_FUNC\_UART   0 |
| --- |

## [◆ ](#affba791a0c60352a28b3d8f122534540)MPS2\_PINMUX

| #define MPS2\_PINMUX | ( |  | *alt\_func*, |
| --- | --- | --- | --- |
|  |  |  | *exp\_num* ) |

**Value:**

(exp\_num << [MPS2\_EXP\_NUM\_POS](#a8fc17b69bcffa4039b207b6a4ab7475d) | \

alt\_func << [MPS2\_ALT\_FUNC\_POS](#ad565796e43c28185243be8c71f910e3f))

[MPS2\_EXP\_NUM\_POS](#a8fc17b69bcffa4039b207b6a4ab7475d)

#define MPS2\_EXP\_NUM\_POS

**Definition** arm-mps2-pinctrl.h:10

[MPS2\_ALT\_FUNC\_POS](#ad565796e43c28185243be8c71f910e3f)

#define MPS2\_ALT\_FUNC\_POS

**Definition** arm-mps2-pinctrl.h:7

## [◆ ](#a301bb93777a77d4fcbed8617edbe319a)SBCON2\_SCL\_EXP

| #define SBCON2\_SCL\_EXP   [MPS2\_PINMUX](#affba791a0c60352a28b3d8f122534540)([MPS2\_PINCTRL\_FUNC\_I2C](#a33857f12895ab4ffb8bac15a226d9e44), 5) |
| --- |

## [◆ ](#a8c2f848c26c691ce333e05fe17c9341d)SBCON2\_SDA\_EXP

| #define SBCON2\_SDA\_EXP   [MPS2\_PINMUX](#affba791a0c60352a28b3d8f122534540)([MPS2\_PINCTRL\_FUNC\_I2C](#a33857f12895ab4ffb8bac15a226d9e44), 15) |
| --- |

## [◆ ](#a42708eb48f46a3dd04242b446389057b)SBCON3\_SCL\_EXP

| #define SBCON3\_SCL\_EXP   [MPS2\_PINMUX](#affba791a0c60352a28b3d8f122534540)([MPS2\_PINCTRL\_FUNC\_I2C](#a33857f12895ab4ffb8bac15a226d9e44), 31) |
| --- |

## [◆ ](#a1f600b98990e17441e52f65cc0dabddb)SBCON3\_SDA\_EXP

| #define SBCON3\_SDA\_EXP   [MPS2\_PINMUX](#affba791a0c60352a28b3d8f122534540)([MPS2\_PINCTRL\_FUNC\_I2C](#a33857f12895ab4ffb8bac15a226d9e44), 41) |
| --- |

## [◆ ](#af0e38d71c2b6d7cb6f1238e17e8fff6f)SPI2\_MISO\_EXP

| #define SPI2\_MISO\_EXP   [MPS2\_PINMUX](#affba791a0c60352a28b3d8f122534540)([MPS2\_PINCTRL\_FUNC\_SPI](#a459cfc88b65ae738b2a94be1fbe6df46), 17) |
| --- |

## [◆ ](#a32eff7bbffdfc00975ff1b5f3281eaa1)SPI2\_MOSI\_EXP

| #define SPI2\_MOSI\_EXP   [MPS2\_PINMUX](#affba791a0c60352a28b3d8f122534540)([MPS2\_PINCTRL\_FUNC\_SPI](#a459cfc88b65ae738b2a94be1fbe6df46), 18) |
| --- |

## [◆ ](#a6fbdf386063229b64599d3c2071ebffd)SPI2\_SCK\_EXP

| #define SPI2\_SCK\_EXP   [MPS2\_PINMUX](#affba791a0c60352a28b3d8f122534540)([MPS2\_PINCTRL\_FUNC\_SPI](#a459cfc88b65ae738b2a94be1fbe6df46), 19) |
| --- |

## [◆ ](#af8e71afd57806fbe85b504ac68879fa6)SPI2\_SS\_EXP

| #define SPI2\_SS\_EXP   [MPS2\_PINMUX](#affba791a0c60352a28b3d8f122534540)([MPS2\_PINCTRL\_FUNC\_SPI](#a459cfc88b65ae738b2a94be1fbe6df46), 16) |
| --- |

## [◆ ](#a14c932b34877e7b1f004bdf3edfdcd4b)SPI3\_MISO\_EXP

| #define SPI3\_MISO\_EXP   [MPS2\_PINMUX](#affba791a0c60352a28b3d8f122534540)([MPS2\_PINCTRL\_FUNC\_SPI](#a459cfc88b65ae738b2a94be1fbe6df46), 14) |
| --- |

## [◆ ](#a95f2fe6603f5ab5de9c410dfaf87dc52)SPI3\_MOSI\_EXP

| #define SPI3\_MOSI\_EXP   [MPS2\_PINMUX](#affba791a0c60352a28b3d8f122534540)([MPS2\_PINCTRL\_FUNC\_SPI](#a459cfc88b65ae738b2a94be1fbe6df46), 13) |
| --- |

## [◆ ](#ac3801e4481859951369757ac96612165)SPI3\_SCK\_EXP

| #define SPI3\_SCK\_EXP   [MPS2\_PINMUX](#affba791a0c60352a28b3d8f122534540)([MPS2\_PINCTRL\_FUNC\_SPI](#a459cfc88b65ae738b2a94be1fbe6df46), 11) |
| --- |

## [◆ ](#ae1f9ab03b508c087a9190d742b67fc2a)SPI3\_SS\_EXP

| #define SPI3\_SS\_EXP   [MPS2\_PINMUX](#affba791a0c60352a28b3d8f122534540)([MPS2\_PINCTRL\_FUNC\_SPI](#a459cfc88b65ae738b2a94be1fbe6df46), 12) |
| --- |

## [◆ ](#a9709eee41e54142558c4930f1b034043)SPI4\_MISO\_EXP

| #define SPI4\_MISO\_EXP   [MPS2\_PINMUX](#affba791a0c60352a28b3d8f122534540)([MPS2\_PINCTRL\_FUNC\_SPI](#a459cfc88b65ae738b2a94be1fbe6df46), 40) |
| --- |

## [◆ ](#aa73c8c56e661787cc05b131f86a8478c)SPI4\_MOSI\_EXP

| #define SPI4\_MOSI\_EXP   [MPS2\_PINMUX](#affba791a0c60352a28b3d8f122534540)([MPS2\_PINCTRL\_FUNC\_SPI](#a459cfc88b65ae738b2a94be1fbe6df46), 39) |
| --- |

## [◆ ](#aa48a51e34a517797511e7214ad00b7de)SPI4\_SCK\_EXP

| #define SPI4\_SCK\_EXP   [MPS2\_PINMUX](#affba791a0c60352a28b3d8f122534540)([MPS2\_PINCTRL\_FUNC\_SPI](#a459cfc88b65ae738b2a94be1fbe6df46), 44) |
| --- |

## [◆ ](#a525321e1403275e09014f3ff1fa88d78)SPI4\_SS\_EXP

| #define SPI4\_SS\_EXP   [MPS2\_PINMUX](#affba791a0c60352a28b3d8f122534540)([MPS2\_PINCTRL\_FUNC\_SPI](#a459cfc88b65ae738b2a94be1fbe6df46), 38) |
| --- |

## [◆ ](#aad1ef19e8c46127baf5ddb680f4a9c2e)UART3\_RXD\_EXP

| #define UART3\_RXD\_EXP   [MPS2\_PINMUX](#affba791a0c60352a28b3d8f122534540)([MPS2\_PINCTRL\_FUNC\_UART](#a793e19909cf9cdd9fb1aa0a34f835c65), 0) |
| --- |

## [◆ ](#aab7f8b8584aa06a033aa1e93200eb0d6)UART3\_TXD\_EXP

| #define UART3\_TXD\_EXP   [MPS2\_PINMUX](#affba791a0c60352a28b3d8f122534540)([MPS2\_PINCTRL\_FUNC\_UART](#a793e19909cf9cdd9fb1aa0a34f835c65), 4) |
| --- |

## [◆ ](#a960b6b4bf5810595c274fab5842189e4)UART4\_RXD\_EXP

| #define UART4\_RXD\_EXP   [MPS2\_PINMUX](#affba791a0c60352a28b3d8f122534540)([MPS2\_PINCTRL\_FUNC\_UART](#a793e19909cf9cdd9fb1aa0a34f835c65), 26) |
| --- |

## [◆ ](#a8f2f8e4cb191c641dad8dff6c4753e38)UART4\_TXD\_EXP

| #define UART4\_TXD\_EXP   [MPS2\_PINMUX](#affba791a0c60352a28b3d8f122534540)([MPS2\_PINCTRL\_FUNC\_UART](#a793e19909cf9cdd9fb1aa0a34f835c65), 30) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [arm-mps2-pinctrl.h](arm-mps2-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
