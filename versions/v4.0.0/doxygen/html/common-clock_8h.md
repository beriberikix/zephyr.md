---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/common-clock_8h.html
original_path: doxygen/html/common-clock_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

common-clock.h File Reference

[Go to the source code of this file.](common-clock_8h_source.md)

| Macros | |
| --- | --- |
| #define | [CLOCK\_BRANCH\_SYSCLK](#a9ae4718ce3eed8108bb86222d50e2098)   0 |
| #define | [CLOCK\_BRANCH\_HCLK](#a91972b1f1c8092580abbe30cfde99b2e)   1 |
| #define | [CLOCK\_BRANCH\_HCLKRADIO](#a84dc580deecd214156bb9d7b3d3c6b00)   2 |
| #define | [CLOCK\_BRANCH\_PCLK](#a8ae9a78ca89559a0c043cfbf7f4f0149)   3 |
| #define | [CLOCK\_BRANCH\_LSPCLK](#af47e31e42bff380a450374b997c9a62b)   4 |
| #define | [CLOCK\_BRANCH\_TRACECLK](#add6f564d9a54107b60f23e96650884bc)   5 |
| #define | [CLOCK\_BRANCH\_ADCCLK](#af76f7e0cd93d94fde5358ab2e8862e71)   6 |
| #define | [CLOCK\_BRANCH\_EXPORTCLK](#ac9b7d1af2508b712c3757745601d74d1)   7 |
| #define | [CLOCK\_BRANCH\_EM01GRPACLK](#a2288b081fb7811e461618a698cf2d68f)   8 |
| #define | [CLOCK\_BRANCH\_EM01GRPBCLK](#abbd5d61291505f2c78bc44ae3eadb5cb)   9 |
| #define | [CLOCK\_BRANCH\_EM01GRPCCLK](#a2f919498355d8112cfb0e20277863fca)   10 |
| #define | [CLOCK\_BRANCH\_EM01GRPDCLK](#a1999b720415f08a0115d61f2b081ca8f)   11 |
| #define | [CLOCK\_BRANCH\_EM23GRPACLK](#a69896c1bf0709d5b4f46d95645718076)   12 |
| #define | [CLOCK\_BRANCH\_EM4GRPACLK](#a791b0697adeddf7b424ffa2c31ebc794)   13 |
| #define | [CLOCK\_BRANCH\_QSPISYSCLK](#a2543cbe70d32186c539795fc7e3fb01a)   14 |
| #define | [CLOCK\_BRANCH\_IADCCLK](#aca2c7930c6f9f22d82a84d0d6b59fc02)   15 |
| #define | [CLOCK\_BRANCH\_WDOG0CLK](#a4ce1e4380d4f10200e8955fe1c4e0ec3)   16 |
| #define | [CLOCK\_BRANCH\_WDOG1CLK](#ae39802322698451abf5a6531157c7adc)   17 |
| #define | [CLOCK\_BRANCH\_RTCCCLK](#ab378f4ac4c47c3972d7ad21419fb569f)   18 |
| #define | [CLOCK\_BRANCH\_SYSRTCCLK](#afbf91ecb5f4d8d2ece258c4a28e012ed)   19 |
| #define | [CLOCK\_BRANCH\_EUART0CLK](#a17be2555fd6316645f596c4f8715d105)   20 |
| #define | [CLOCK\_BRANCH\_EUSART0CLK](#a9c788fabfbf9ca14c2e6a4d7e21f69df)   21 |
| #define | [CLOCK\_BRANCH\_DPLLREFCLK](#a5d16954e4cae59bba0411fcf4004c166)   22 |
| #define | [CLOCK\_BRANCH\_I2C0CLK](#afc4afa41743b9e8bd65f657469570cbf)   23 |
| #define | [CLOCK\_BRANCH\_LCDCLK](#a62c66b574633b7862d455ca92ecb7ca6)   24 |
| #define | [CLOCK\_BRANCH\_PIXELRZCLK](#ad9fc418b7b97d9691aa2dbed560c9d2d)   25 |
| #define | [CLOCK\_BRANCH\_PCNT0CLK](#afd28e8ca37027ae7211200072dedafcf)   26 |
| #define | [CLOCK\_BRANCH\_PRORTCCLK](#a28e66400d1616baa0afdd25d54283a2d)   27 |
| #define | [CLOCK\_BRANCH\_SYSTICKCLK](#a4be96634ea45a011a014480c9085df51)   28 |
| #define | [CLOCK\_BRANCH\_LESENSEHFCLK](#aa6229452489aaa2281b1627ef3a5a78c)   29 |
| #define | [CLOCK\_BRANCH\_VDAC0CLK](#a52cade1ae02584fb7d7d9cdc8dae0ac8)   30 |
| #define | [CLOCK\_BRANCH\_VDAC1CLK](#aebe06aa36e0952f79e76518ce8a29336)   31 |
| #define | [CLOCK\_BRANCH\_USB0CLK](#a60632170b51f5f443acf34fc76c9dea2)   32 |
| #define | [CLOCK\_BRANCH\_FLPLLREFCLK](#a274ca09dab6568f7142a2734ecdad428)   33 |
| #define | [CLOCK\_BRANCH\_INVALID](#a60be0eac710342c0175d620897b5a259)   34 |
| #define | [CLOCK\_BIT\_MASK](#a81609d56a415da8a22bd83d651cab503)   0x03FUL |
| #define | [CLOCK\_REG\_MASK](#adb54589c8ff63fe8dd82d1739fb4d256)   0x1C0UL |

## Macro Definition Documentation

## [◆ ](#a81609d56a415da8a22bd83d651cab503)CLOCK\_BIT\_MASK

| #define CLOCK\_BIT\_MASK   0x03FUL |
| --- |

## [◆ ](#af76f7e0cd93d94fde5358ab2e8862e71)CLOCK\_BRANCH\_ADCCLK

| #define CLOCK\_BRANCH\_ADCCLK   6 |
| --- |

## [◆ ](#a5d16954e4cae59bba0411fcf4004c166)CLOCK\_BRANCH\_DPLLREFCLK

| #define CLOCK\_BRANCH\_DPLLREFCLK   22 |
| --- |

## [◆ ](#a2288b081fb7811e461618a698cf2d68f)CLOCK\_BRANCH\_EM01GRPACLK

| #define CLOCK\_BRANCH\_EM01GRPACLK   8 |
| --- |

## [◆ ](#abbd5d61291505f2c78bc44ae3eadb5cb)CLOCK\_BRANCH\_EM01GRPBCLK

| #define CLOCK\_BRANCH\_EM01GRPBCLK   9 |
| --- |

## [◆ ](#a2f919498355d8112cfb0e20277863fca)CLOCK\_BRANCH\_EM01GRPCCLK

| #define CLOCK\_BRANCH\_EM01GRPCCLK   10 |
| --- |

## [◆ ](#a1999b720415f08a0115d61f2b081ca8f)CLOCK\_BRANCH\_EM01GRPDCLK

| #define CLOCK\_BRANCH\_EM01GRPDCLK   11 |
| --- |

## [◆ ](#a69896c1bf0709d5b4f46d95645718076)CLOCK\_BRANCH\_EM23GRPACLK

| #define CLOCK\_BRANCH\_EM23GRPACLK   12 |
| --- |

## [◆ ](#a791b0697adeddf7b424ffa2c31ebc794)CLOCK\_BRANCH\_EM4GRPACLK

| #define CLOCK\_BRANCH\_EM4GRPACLK   13 |
| --- |

## [◆ ](#a17be2555fd6316645f596c4f8715d105)CLOCK\_BRANCH\_EUART0CLK

| #define CLOCK\_BRANCH\_EUART0CLK   20 |
| --- |

## [◆ ](#a9c788fabfbf9ca14c2e6a4d7e21f69df)CLOCK\_BRANCH\_EUSART0CLK

| #define CLOCK\_BRANCH\_EUSART0CLK   21 |
| --- |

## [◆ ](#ac9b7d1af2508b712c3757745601d74d1)CLOCK\_BRANCH\_EXPORTCLK

| #define CLOCK\_BRANCH\_EXPORTCLK   7 |
| --- |

## [◆ ](#a274ca09dab6568f7142a2734ecdad428)CLOCK\_BRANCH\_FLPLLREFCLK

| #define CLOCK\_BRANCH\_FLPLLREFCLK   33 |
| --- |

## [◆ ](#a91972b1f1c8092580abbe30cfde99b2e)CLOCK\_BRANCH\_HCLK

| #define CLOCK\_BRANCH\_HCLK   1 |
| --- |

## [◆ ](#a84dc580deecd214156bb9d7b3d3c6b00)CLOCK\_BRANCH\_HCLKRADIO

| #define CLOCK\_BRANCH\_HCLKRADIO   2 |
| --- |

## [◆ ](#afc4afa41743b9e8bd65f657469570cbf)CLOCK\_BRANCH\_I2C0CLK

| #define CLOCK\_BRANCH\_I2C0CLK   23 |
| --- |

## [◆ ](#aca2c7930c6f9f22d82a84d0d6b59fc02)CLOCK\_BRANCH\_IADCCLK

| #define CLOCK\_BRANCH\_IADCCLK   15 |
| --- |

## [◆ ](#a60be0eac710342c0175d620897b5a259)CLOCK\_BRANCH\_INVALID

| #define CLOCK\_BRANCH\_INVALID   34 |
| --- |

## [◆ ](#a62c66b574633b7862d455ca92ecb7ca6)CLOCK\_BRANCH\_LCDCLK

| #define CLOCK\_BRANCH\_LCDCLK   24 |
| --- |

## [◆ ](#aa6229452489aaa2281b1627ef3a5a78c)CLOCK\_BRANCH\_LESENSEHFCLK

| #define CLOCK\_BRANCH\_LESENSEHFCLK   29 |
| --- |

## [◆ ](#af47e31e42bff380a450374b997c9a62b)CLOCK\_BRANCH\_LSPCLK

| #define CLOCK\_BRANCH\_LSPCLK   4 |
| --- |

## [◆ ](#a8ae9a78ca89559a0c043cfbf7f4f0149)CLOCK\_BRANCH\_PCLK

| #define CLOCK\_BRANCH\_PCLK   3 |
| --- |

## [◆ ](#afd28e8ca37027ae7211200072dedafcf)CLOCK\_BRANCH\_PCNT0CLK

| #define CLOCK\_BRANCH\_PCNT0CLK   26 |
| --- |

## [◆ ](#ad9fc418b7b97d9691aa2dbed560c9d2d)CLOCK\_BRANCH\_PIXELRZCLK

| #define CLOCK\_BRANCH\_PIXELRZCLK   25 |
| --- |

## [◆ ](#a28e66400d1616baa0afdd25d54283a2d)CLOCK\_BRANCH\_PRORTCCLK

| #define CLOCK\_BRANCH\_PRORTCCLK   27 |
| --- |

## [◆ ](#a2543cbe70d32186c539795fc7e3fb01a)CLOCK\_BRANCH\_QSPISYSCLK

| #define CLOCK\_BRANCH\_QSPISYSCLK   14 |
| --- |

## [◆ ](#ab378f4ac4c47c3972d7ad21419fb569f)CLOCK\_BRANCH\_RTCCCLK

| #define CLOCK\_BRANCH\_RTCCCLK   18 |
| --- |

## [◆ ](#a9ae4718ce3eed8108bb86222d50e2098)CLOCK\_BRANCH\_SYSCLK

| #define CLOCK\_BRANCH\_SYSCLK   0 |
| --- |

## [◆ ](#afbf91ecb5f4d8d2ece258c4a28e012ed)CLOCK\_BRANCH\_SYSRTCCLK

| #define CLOCK\_BRANCH\_SYSRTCCLK   19 |
| --- |

## [◆ ](#a4be96634ea45a011a014480c9085df51)CLOCK\_BRANCH\_SYSTICKCLK

| #define CLOCK\_BRANCH\_SYSTICKCLK   28 |
| --- |

## [◆ ](#add6f564d9a54107b60f23e96650884bc)CLOCK\_BRANCH\_TRACECLK

| #define CLOCK\_BRANCH\_TRACECLK   5 |
| --- |

## [◆ ](#a60632170b51f5f443acf34fc76c9dea2)CLOCK\_BRANCH\_USB0CLK

| #define CLOCK\_BRANCH\_USB0CLK   32 |
| --- |

## [◆ ](#a52cade1ae02584fb7d7d9cdc8dae0ac8)CLOCK\_BRANCH\_VDAC0CLK

| #define CLOCK\_BRANCH\_VDAC0CLK   30 |
| --- |

## [◆ ](#aebe06aa36e0952f79e76518ce8a29336)CLOCK\_BRANCH\_VDAC1CLK

| #define CLOCK\_BRANCH\_VDAC1CLK   31 |
| --- |

## [◆ ](#a4ce1e4380d4f10200e8955fe1c4e0ec3)CLOCK\_BRANCH\_WDOG0CLK

| #define CLOCK\_BRANCH\_WDOG0CLK   16 |
| --- |

## [◆ ](#ae39802322698451abf5a6531157c7adc)CLOCK\_BRANCH\_WDOG1CLK

| #define CLOCK\_BRANCH\_WDOG1CLK   17 |
| --- |

## [◆ ](#adb54589c8ff63fe8dd82d1739fb4d256)CLOCK\_REG\_MASK

| #define CLOCK\_REG\_MASK   0x1C0UL |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [silabs](dir_9d9a53d793dad9345737df2b8d108293.md)
- [common-clock.h](common-clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
