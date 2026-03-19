---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/renesas__rzg__clock_8h.html
original_path: doxygen/html/renesas__rzg__clock_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

renesas\_rzg\_clock.h File Reference

[Go to the source code of this file.](renesas__rzg__clock_8h_source.md)

| Macros | |
| --- | --- |
| #define | [RZ\_IP\_MASK](#af22fb58317528ced8ad8cdfc399ad2ac)   0xFF000000UL |
|  | RZ clock configuration values. |
| #define | [RZ\_IP\_SHIFT](#a0bfeafa5676753c0e6750a9c3c2f18f1)   24UL |
| #define | [RZ\_IP\_CH\_MASK](#a73baaadd858826d7b7e613120a9e4509)   0xFF0000UL |
| #define | [RZ\_IP\_CH\_SHIFT](#a4854f76eb8144726dcc49da30bb49494)   16UL |
| #define | [RZ\_CLOCK\_MASK](#a9712059a7005130fbeb48f2ce7f45f66)   0xFF00UL |
| #define | [RZ\_CLOCK\_SHIFT](#a0f4444cd8f843699d43be43968a76f60)   8UL |
| #define | [RZ\_CLOCK\_DIV\_MASK](#a68e6f2ee01f4ba23c076f5a0c3574ec3)   0xFFUL |
| #define | [RZ\_CLOCK\_DIV\_SHIFT](#a2a394bb9c50b68c2c0b4250d529e96fa)   0UL |
| #define | [RZ\_IP\_GTM](#a85c1cd03e46043357e15c2020cf8db25)   0UL /\* General Timer \*/ |
| #define | [RZ\_IP\_GPT](#a258d150ad8458cb580f823296dd4b863)   1UL /\* General PWM Timer \*/ |
| #define | [RZ\_IP\_SCIF](#a4d01bb6e25a7d8f0cc520efd1693f6b0)   2UL /\* Serial Communications Interface with FIFO \*/ |
| #define | [RZ\_IP\_RIIC](#a20be7b897467fae2e11d31b9404db77e)   3UL /\* I2C Bus Interface \*/ |
| #define | [RZ\_IP\_RSPI](#abe3258c6780f7e818d6a0bfa621c0c39)   4UL /\* Renesas Serial Peripheral Interface \*/ |
| #define | [RZ\_IP\_MHU](#a545f1dab775039d3e00320f4c2fa2266)   5UL /\* Message Handling Unit \*/ |
| #define | [RZ\_IP\_DMAC](#a6fb0a952bce1f87fdc485e3407885aab)   6UL /\* Direct Memory Access Controller \*/ |
| #define | [RZ\_IP\_CANFD](#a2a5b46c7954d9931d05ba9b78b6bfa92)   7UL /\* CANFD Interface (RS-CANFD) \*/ |
| #define | [RZ\_IP\_ADC](#ad6e07b47929a05a957f6685c8207a0d4)   8UL /\* A/D Converter \*/ |
| #define | [RZ\_CLOCK\_ICLK](#a244252c9570d2ce5142a1dacb71aca93)   0UL /\* Cortex-A55 Clock \*/ |
| #define | [RZ\_CLOCK\_I2CLK](#a9970fbd46cf921c331ad693053100e6f)   1UL /\* Cortex-M33 Clock \*/ |
| #define | [RZ\_CLOCK\_I3CLK](#a19ef59ea7eadc3ef12705e6bcd650cfc)   2UL /\* Cortex-M33 FPU Clock \*/ |
| #define | [RZ\_CLOCK\_S0CLK](#af7ba3a355a4c56b7c2700d4179bece3f)   3UL /\* DDR-PHY Clock \*/ |
| #define | [RZ\_CLOCK\_OC0CLK](#a8558bb747c644c3ba838d0b564fef57b)   4UL /\* OCTA0 Clock \*/ |
| #define | [RZ\_CLOCK\_OC1CLK](#abe1148e7058c4e6997c83e86470e1784)   5UL /\* OCTA1 Clock \*/ |
| #define | [RZ\_CLOCK\_SPI0CLK](#ab4e5d3a27f25df5591d3170f2e944e0f)   6UL /\* SPI0 Clock \*/ |
| #define | [RZ\_CLOCK\_SPI1CLK](#ab02c603153146d64db7a98b4f332a7d5)   7UL /\* SPI1 Clock \*/ |
| #define | [RZ\_CLOCK\_SD0CLK](#af49247c2ed779dc006ce90a7cdf3a8c1)   8UL /\* SDH0 Clock \*/ |
| #define | [RZ\_CLOCK\_SD1CLK](#a17b5762dca74eb50645508737085f6c1)   9UL /\* SDH1 Clock \*/ |
| #define | [RZ\_CLOCK\_SD2CLK](#a9b9efa69cb954f3bd2e590974f2f5b68)   10UL /\* SDH2 Clock \*/ |
| #define | [RZ\_CLOCK\_M0CLK](#ab42089566bde80f80a5a672c39f5f4a9)   11UL /\* VCP LCDC Clock \*/ |
| #define | [RZ\_CLOCK\_HPCLK](#a357ba27e1964a6f63d756d957213a94d)   12UL /\* Ethernet Clock \*/ |
| #define | [RZ\_CLOCK\_TSUCLK](#a622f3e70a5fe08a61474322492130319)   13UL /\* TSU Clock \*/ |
| #define | [RZ\_CLOCK\_ZTCLK](#a67327a7c0fcff2dc0374a0fbde6422c6)   14UL /\* JAUTH Clock \*/ |
| #define | [RZ\_CLOCK\_P0CLK](#a43f77faab57d93e59c93956572ed73a5)   15UL /\* APB-BUS Clock \*/ |
| #define | [RZ\_CLOCK\_P1CLK](#a960f074fd0a8e9ea8c5b02a4d6d977c9)   16UL /\* AXI-BUS Clock \*/ |
| #define | [RZ\_CLOCK\_P2CLK](#a794d8d5f1cb8a2df70ca2ab4caf2b049)   17UL /\* P2CLK \*/ |
| #define | [RZ\_CLOCK\_P3CLK](#a2dbb22921c00fb5398666f595da080d9)   18UL /\* P3CLK \*/ |
| #define | [RZ\_CLOCK\_P4CLK](#a3e09739b70bf6fbcd7cb3a72002c0339)   19UL /\* P4CLK \*/ |
| #define | [RZ\_CLOCK\_P5CLK](#a764d5d9af4b6ef76a903f93f15f53b74)   20UL /\* P5CLK \*/ |
| #define | [RZ\_CLOCK\_ATCLK](#a7b51d8e0e38165e26975696bf90d834b)   21UL /\* ATCLK \*/ |
| #define | [RZ\_CLOCK\_OSCCLK](#a800d72bacbe85d766ed0e027b28b36c8)   22UL /\* OSC Clock \*/ |
| #define | [RZ\_CLOCK\_OSCCLK2](#a4811a342819ebdb27d9ad77aa3bfc48e)   23UL /\* OSC2 Clock \*/ |
| #define | [RZ\_CLOCK](#af2b6678567dacec847501d2a634b7773)(IP, ch, clk, div) |
| #define | [RZ\_CLOCK\_SCIF](#ab5ba6102fd209a05b2a5cce69874594a)(ch) |
|  | Pack clock configurations in a 32-bit value as expected for the Device Tree clocks property on Renesas RZ/G. |
| #define | [RZ\_CLOCK\_GPT](#adda08ff063353c356bae99dada0352c8)(ch) |
| #define | [RZ\_CLOCK\_MHU](#ab7297a9bbf3181ab73f1ea0e2c67decd)(ch) |
| #define | [RZ\_CLOCK\_ADC](#aabe15d33711286e3c8a9a99774afffc4)(ch) |
| #define | [RZ\_CLOCK\_RIIC](#ae138403b21ab0a308312072d1ffa06f1)(ch) |
| #define | [RZ\_CLOCK\_GTM](#a435c6e38774d8d95067cb4e7513dd74d)(ch) |
| #define | [RZ\_CLOCK\_CANFD](#a637295af9157f6757bed145911ca2a3a)(ch) |
| #define | [RZ\_CLOCK\_RSPI](#a566a4e447745ff7d5ed3b4d0dd0fa666)(ch) |
| #define | [RZ\_CLOCK\_DMAC](#a3a3baef1dbd6eae8f7d54a0610521aa0)(ch) |

## Macro Definition Documentation

## [◆ ](#af2b6678567dacec847501d2a634b7773)RZ\_CLOCK

| #define RZ\_CLOCK | ( |  | *IP*, |
| --- | --- | --- | --- |
|  |  |  | *ch*, |
|  |  |  | *clk*, |
|  |  |  | *div* ) |

**Value:**

((RZ\_IP\_##IP << [RZ\_IP\_SHIFT](#a0bfeafa5676753c0e6750a9c3c2f18f1)) | ((ch) << [RZ\_IP\_CH\_SHIFT](#a4854f76eb8144726dcc49da30bb49494)) | ((clk) << [RZ\_CLOCK\_SHIFT](#a0f4444cd8f843699d43be43968a76f60)) | \

((div) << [RZ\_CLOCK\_DIV\_SHIFT](#a2a394bb9c50b68c2c0b4250d529e96fa)))

[RZ\_IP\_SHIFT](#a0bfeafa5676753c0e6750a9c3c2f18f1)

#define RZ\_IP\_SHIFT

**Definition** renesas\_rzg\_clock.h:12

[RZ\_CLOCK\_SHIFT](#a0f4444cd8f843699d43be43968a76f60)

#define RZ\_CLOCK\_SHIFT

**Definition** renesas\_rzg\_clock.h:16

[RZ\_CLOCK\_DIV\_SHIFT](#a2a394bb9c50b68c2c0b4250d529e96fa)

#define RZ\_CLOCK\_DIV\_SHIFT

**Definition** renesas\_rzg\_clock.h:18

[RZ\_IP\_CH\_SHIFT](#a4854f76eb8144726dcc49da30bb49494)

#define RZ\_IP\_CH\_SHIFT

**Definition** renesas\_rzg\_clock.h:14

## [◆ ](#aabe15d33711286e3c8a9a99774afffc4)RZ\_CLOCK\_ADC

| #define RZ\_CLOCK\_ADC | ( |  | *ch* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RZ\_CLOCK](#af2b6678567dacec847501d2a634b7773)(ADC, ch, [RZ\_CLOCK\_TSUCLK](#a622f3e70a5fe08a61474322492130319), 1)

[RZ\_CLOCK\_TSUCLK](#a622f3e70a5fe08a61474322492130319)

#define RZ\_CLOCK\_TSUCLK

**Definition** renesas\_rzg\_clock.h:43

[RZ\_CLOCK](#af2b6678567dacec847501d2a634b7773)

#define RZ\_CLOCK(IP, ch, clk, div)

**Definition** renesas\_rzg\_clock.h:55

## [◆ ](#a7b51d8e0e38165e26975696bf90d834b)RZ\_CLOCK\_ATCLK

| #define RZ\_CLOCK\_ATCLK   21UL /\* ATCLK \*/ |
| --- |

## [◆ ](#a637295af9157f6757bed145911ca2a3a)RZ\_CLOCK\_CANFD

| #define RZ\_CLOCK\_CANFD | ( |  | *ch* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RZ\_CLOCK](#af2b6678567dacec847501d2a634b7773)(CANFD, ch, [RZ\_CLOCK\_P4CLK](#a3e09739b70bf6fbcd7cb3a72002c0339), 2)

[RZ\_CLOCK\_P4CLK](#a3e09739b70bf6fbcd7cb3a72002c0339)

#define RZ\_CLOCK\_P4CLK

**Definition** renesas\_rzg\_clock.h:49

## [◆ ](#a68e6f2ee01f4ba23c076f5a0c3574ec3)RZ\_CLOCK\_DIV\_MASK

| #define RZ\_CLOCK\_DIV\_MASK   0xFFUL |
| --- |

## [◆ ](#a2a394bb9c50b68c2c0b4250d529e96fa)RZ\_CLOCK\_DIV\_SHIFT

| #define RZ\_CLOCK\_DIV\_SHIFT   0UL |
| --- |

## [◆ ](#a3a3baef1dbd6eae8f7d54a0610521aa0)RZ\_CLOCK\_DMAC

| #define RZ\_CLOCK\_DMAC | ( |  | *ch* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RZ\_CLOCK](#af2b6678567dacec847501d2a634b7773)(DMAC, ch, [RZ\_CLOCK\_P3CLK](#a2dbb22921c00fb5398666f595da080d9), 1)

[RZ\_CLOCK\_P3CLK](#a2dbb22921c00fb5398666f595da080d9)

#define RZ\_CLOCK\_P3CLK

**Definition** renesas\_rzg\_clock.h:48

## [◆ ](#adda08ff063353c356bae99dada0352c8)RZ\_CLOCK\_GPT

| #define RZ\_CLOCK\_GPT | ( |  | *ch* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RZ\_CLOCK](#af2b6678567dacec847501d2a634b7773)(GPT, ch, [RZ\_CLOCK\_P0CLK](#a43f77faab57d93e59c93956572ed73a5), 1)

[RZ\_CLOCK\_P0CLK](#a43f77faab57d93e59c93956572ed73a5)

#define RZ\_CLOCK\_P0CLK

**Definition** renesas\_rzg\_clock.h:45

## [◆ ](#a435c6e38774d8d95067cb4e7513dd74d)RZ\_CLOCK\_GTM

| #define RZ\_CLOCK\_GTM | ( |  | *ch* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RZ\_CLOCK](#af2b6678567dacec847501d2a634b7773)(GTM, ch, [RZ\_CLOCK\_P0CLK](#a43f77faab57d93e59c93956572ed73a5), 1)

## [◆ ](#a357ba27e1964a6f63d756d957213a94d)RZ\_CLOCK\_HPCLK

| #define RZ\_CLOCK\_HPCLK   12UL /\* Ethernet Clock \*/ |
| --- |

## [◆ ](#a9970fbd46cf921c331ad693053100e6f)RZ\_CLOCK\_I2CLK

| #define RZ\_CLOCK\_I2CLK   1UL /\* Cortex-M33 Clock \*/ |
| --- |

## [◆ ](#a19ef59ea7eadc3ef12705e6bcd650cfc)RZ\_CLOCK\_I3CLK

| #define RZ\_CLOCK\_I3CLK   2UL /\* Cortex-M33 FPU Clock \*/ |
| --- |

## [◆ ](#a244252c9570d2ce5142a1dacb71aca93)RZ\_CLOCK\_ICLK

| #define RZ\_CLOCK\_ICLK   0UL /\* Cortex-A55 Clock \*/ |
| --- |

## [◆ ](#ab42089566bde80f80a5a672c39f5f4a9)RZ\_CLOCK\_M0CLK

| #define RZ\_CLOCK\_M0CLK   11UL /\* VCP LCDC Clock \*/ |
| --- |

## [◆ ](#a9712059a7005130fbeb48f2ce7f45f66)RZ\_CLOCK\_MASK

| #define RZ\_CLOCK\_MASK   0xFF00UL |
| --- |

## [◆ ](#ab7297a9bbf3181ab73f1ea0e2c67decd)RZ\_CLOCK\_MHU

| #define RZ\_CLOCK\_MHU | ( |  | *ch* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RZ\_CLOCK](#af2b6678567dacec847501d2a634b7773)(MHU, ch, [RZ\_CLOCK\_P1CLK](#a960f074fd0a8e9ea8c5b02a4d6d977c9), 2)

[RZ\_CLOCK\_P1CLK](#a960f074fd0a8e9ea8c5b02a4d6d977c9)

#define RZ\_CLOCK\_P1CLK

**Definition** renesas\_rzg\_clock.h:46

## [◆ ](#a8558bb747c644c3ba838d0b564fef57b)RZ\_CLOCK\_OC0CLK

| #define RZ\_CLOCK\_OC0CLK   4UL /\* OCTA0 Clock \*/ |
| --- |

## [◆ ](#abe1148e7058c4e6997c83e86470e1784)RZ\_CLOCK\_OC1CLK

| #define RZ\_CLOCK\_OC1CLK   5UL /\* OCTA1 Clock \*/ |
| --- |

## [◆ ](#a800d72bacbe85d766ed0e027b28b36c8)RZ\_CLOCK\_OSCCLK

| #define RZ\_CLOCK\_OSCCLK   22UL /\* OSC Clock \*/ |
| --- |

## [◆ ](#a4811a342819ebdb27d9ad77aa3bfc48e)RZ\_CLOCK\_OSCCLK2

| #define RZ\_CLOCK\_OSCCLK2   23UL /\* OSC2 Clock \*/ |
| --- |

## [◆ ](#a43f77faab57d93e59c93956572ed73a5)RZ\_CLOCK\_P0CLK

| #define RZ\_CLOCK\_P0CLK   15UL /\* APB-BUS Clock \*/ |
| --- |

## [◆ ](#a960f074fd0a8e9ea8c5b02a4d6d977c9)RZ\_CLOCK\_P1CLK

| #define RZ\_CLOCK\_P1CLK   16UL /\* AXI-BUS Clock \*/ |
| --- |

## [◆ ](#a794d8d5f1cb8a2df70ca2ab4caf2b049)RZ\_CLOCK\_P2CLK

| #define RZ\_CLOCK\_P2CLK   17UL /\* P2CLK \*/ |
| --- |

## [◆ ](#a2dbb22921c00fb5398666f595da080d9)RZ\_CLOCK\_P3CLK

| #define RZ\_CLOCK\_P3CLK   18UL /\* P3CLK \*/ |
| --- |

## [◆ ](#a3e09739b70bf6fbcd7cb3a72002c0339)RZ\_CLOCK\_P4CLK

| #define RZ\_CLOCK\_P4CLK   19UL /\* P4CLK \*/ |
| --- |

## [◆ ](#a764d5d9af4b6ef76a903f93f15f53b74)RZ\_CLOCK\_P5CLK

| #define RZ\_CLOCK\_P5CLK   20UL /\* P5CLK \*/ |
| --- |

## [◆ ](#ae138403b21ab0a308312072d1ffa06f1)RZ\_CLOCK\_RIIC

| #define RZ\_CLOCK\_RIIC | ( |  | *ch* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RZ\_CLOCK](#af2b6678567dacec847501d2a634b7773)(RIIC, ch, [RZ\_CLOCK\_P0CLK](#a43f77faab57d93e59c93956572ed73a5), 1)

## [◆ ](#a566a4e447745ff7d5ed3b4d0dd0fa666)RZ\_CLOCK\_RSPI

| #define RZ\_CLOCK\_RSPI | ( |  | *ch* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RZ\_CLOCK](#af2b6678567dacec847501d2a634b7773)(RSPI, ch, [RZ\_CLOCK\_P0CLK](#a43f77faab57d93e59c93956572ed73a5), 1)

## [◆ ](#af7ba3a355a4c56b7c2700d4179bece3f)RZ\_CLOCK\_S0CLK

| #define RZ\_CLOCK\_S0CLK   3UL /\* DDR-PHY Clock \*/ |
| --- |

## [◆ ](#ab5ba6102fd209a05b2a5cce69874594a)RZ\_CLOCK\_SCIF

| #define RZ\_CLOCK\_SCIF | ( |  | *ch* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RZ\_CLOCK](#af2b6678567dacec847501d2a634b7773)(SCIF, ch, [RZ\_CLOCK\_P0CLK](#a43f77faab57d93e59c93956572ed73a5), 1)

Pack clock configurations in a 32-bit value as expected for the Device Tree clocks property on Renesas RZ/G.

Parameters
:   | ch | Peripheral channel/unit |
    | --- | --- |

## [◆ ](#af49247c2ed779dc006ce90a7cdf3a8c1)RZ\_CLOCK\_SD0CLK

| #define RZ\_CLOCK\_SD0CLK   8UL /\* SDH0 Clock \*/ |
| --- |

## [◆ ](#a17b5762dca74eb50645508737085f6c1)RZ\_CLOCK\_SD1CLK

| #define RZ\_CLOCK\_SD1CLK   9UL /\* SDH1 Clock \*/ |
| --- |

## [◆ ](#a9b9efa69cb954f3bd2e590974f2f5b68)RZ\_CLOCK\_SD2CLK

| #define RZ\_CLOCK\_SD2CLK   10UL /\* SDH2 Clock \*/ |
| --- |

## [◆ ](#a0f4444cd8f843699d43be43968a76f60)RZ\_CLOCK\_SHIFT

| #define RZ\_CLOCK\_SHIFT   8UL |
| --- |

## [◆ ](#ab4e5d3a27f25df5591d3170f2e944e0f)RZ\_CLOCK\_SPI0CLK

| #define RZ\_CLOCK\_SPI0CLK   6UL /\* SPI0 Clock \*/ |
| --- |

## [◆ ](#ab02c603153146d64db7a98b4f332a7d5)RZ\_CLOCK\_SPI1CLK

| #define RZ\_CLOCK\_SPI1CLK   7UL /\* SPI1 Clock \*/ |
| --- |

## [◆ ](#a622f3e70a5fe08a61474322492130319)RZ\_CLOCK\_TSUCLK

| #define RZ\_CLOCK\_TSUCLK   13UL /\* TSU Clock \*/ |
| --- |

## [◆ ](#a67327a7c0fcff2dc0374a0fbde6422c6)RZ\_CLOCK\_ZTCLK

| #define RZ\_CLOCK\_ZTCLK   14UL /\* JAUTH Clock \*/ |
| --- |

## [◆ ](#ad6e07b47929a05a957f6685c8207a0d4)RZ\_IP\_ADC

| #define RZ\_IP\_ADC   8UL /\* A/D Converter \*/ |
| --- |

## [◆ ](#a2a5b46c7954d9931d05ba9b78b6bfa92)RZ\_IP\_CANFD

| #define RZ\_IP\_CANFD   7UL /\* CANFD Interface (RS-CANFD) \*/ |
| --- |

## [◆ ](#a73baaadd858826d7b7e613120a9e4509)RZ\_IP\_CH\_MASK

| #define RZ\_IP\_CH\_MASK   0xFF0000UL |
| --- |

## [◆ ](#a4854f76eb8144726dcc49da30bb49494)RZ\_IP\_CH\_SHIFT

| #define RZ\_IP\_CH\_SHIFT   16UL |
| --- |

## [◆ ](#a6fb0a952bce1f87fdc485e3407885aab)RZ\_IP\_DMAC

| #define RZ\_IP\_DMAC   6UL /\* Direct Memory Access Controller \*/ |
| --- |

## [◆ ](#a258d150ad8458cb580f823296dd4b863)RZ\_IP\_GPT

| #define RZ\_IP\_GPT   1UL /\* General PWM Timer \*/ |
| --- |

## [◆ ](#a85c1cd03e46043357e15c2020cf8db25)RZ\_IP\_GTM

| #define RZ\_IP\_GTM   0UL /\* General Timer \*/ |
| --- |

## [◆ ](#af22fb58317528ced8ad8cdfc399ad2ac)RZ\_IP\_MASK

| #define RZ\_IP\_MASK   0xFF000000UL |
| --- |

RZ clock configuration values.

## [◆ ](#a545f1dab775039d3e00320f4c2fa2266)RZ\_IP\_MHU

| #define RZ\_IP\_MHU   5UL /\* Message Handling Unit \*/ |
| --- |

## [◆ ](#a20be7b897467fae2e11d31b9404db77e)RZ\_IP\_RIIC

| #define RZ\_IP\_RIIC   3UL /\* I2C Bus Interface \*/ |
| --- |

## [◆ ](#abe3258c6780f7e818d6a0bfa621c0c39)RZ\_IP\_RSPI

| #define RZ\_IP\_RSPI   4UL /\* Renesas Serial Peripheral Interface \*/ |
| --- |

## [◆ ](#a4d01bb6e25a7d8f0cc520efd1693f6b0)RZ\_IP\_SCIF

| #define RZ\_IP\_SCIF   2UL /\* Serial Communications Interface with FIFO \*/ |
| --- |

## [◆ ](#a0bfeafa5676753c0e6750a9c3c2f18f1)RZ\_IP\_SHIFT

| #define RZ\_IP\_SHIFT   24UL |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [renesas\_rzg\_clock.h](renesas__rzg__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
