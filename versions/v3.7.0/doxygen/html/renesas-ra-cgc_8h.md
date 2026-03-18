---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/renesas-ra-cgc_8h.html
original_path: doxygen/html/renesas-ra-cgc_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

renesas-ra-cgc.h File Reference

[Go to the source code of this file.](renesas-ra-cgc_8h_source.md)

| Macros | |
| --- | --- |
| #define | [RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(grp, func, ch) |
| #define | [RA\_CLOCK\_GROUP](#ac6af2db5eb5e2826456e6e36ef78320b)(mod) |
| #define | [RA\_CLOCK\_BIT](#ad2d935ba5827105c9ac5b13a3a189ab0)(mod) |
| #define | [RA\_CLOCK\_DMAC](#ad4dfc984527e53e86162fd2f653768be)(channel) |
| #define | [RA\_CLOCK\_DTC](#a3ddb10bc4a6eed8a67a4bc2a373343c5)(channel) |
| #define | [RA\_CLOCK\_CAN](#aa6c6a052fa47101bc07b1cde7d0c8a9e)(channel) |
| #define | [RA\_CLOCK\_CEC](#a00974ed13a8ba59014206d622175903e)(channel) |
| #define | [RA\_CLOCK\_I3C](#a6724e283fa86f2a1a54e2f3b9be8bd3b)(channel) |
| #define | [RA\_CLOCK\_IRDA](#abc119ce6dc201c22f2c3984600716667)(channel) |
| #define | [RA\_CLOCK\_QSPI](#a4334a46b749963ef0ca7d1437acefc70)(channel) |
| #define | [RA\_CLOCK\_IIC](#abb191de59b4e661f23fa5b8bdc0e6735)(channel) |
| #define | [RA\_CLOCK\_USBFS](#a7601cf92d860ef7be29a7086e948c95f)(channel) |
| #define | [RA\_CLOCK\_USBHS](#ae19013bef5f3f49ac258f897baac8957)(channel) |
| #define | [RA\_CLOCK\_EPTPC](#ad6a3eb4b0a0fe5fdeb432d2aa30811f7)(channel) |
| #define | [RA\_CLOCK\_ETHER](#a1ff75408ca2eb508b42130c0c5b6167e)(channel) |
| #define | [RA\_CLOCK\_OSPI](#a2d1f85ce9073177e1e4c662a8fcea802)(channel) |
| #define | [RA\_CLOCK\_SPI](#a9907d81a9a8279782dbad1123ed9cabc)(channel) |
| #define | [RA\_CLOCK\_SCI](#a6e1e337469bda99de331098a3a75b57e)(channel) |
| #define | [RA\_CLOCK\_CAC](#a7c935768ee984933b2ecceb3d3c7b068)(channel) |
| #define | [RA\_CLOCK\_CRC](#a03eaba37f88043e0e18c8c184c5fa9ca)(channel) |
| #define | [RA\_CLOCK\_PDC](#a2268067bebcb6fc2504354a59a9d7b1f)(channel) |
| #define | [RA\_CLOCK\_CTSU](#ab1cc63937cef3f1eb0377b333b6ff2f4)(channel) |
| #define | [RA\_CLOCK\_SLCDC](#a238e1efc42e368172af9f5f9a50e7ae7)(channel) |
| #define | [RA\_CLOCK\_GLCDC](#a85533bf4da5b6f75aa16ce1cc7e4cbad)(channel) |
| #define | [RA\_CLOCK\_JPEG](#a7f6f30e7f3f1ce6fc1ae393dbe4060ac)(channel) |
| #define | [RA\_CLOCK\_DRW](#a2a4921ce74876f3f18d334e4def418b5)(channel) |
| #define | [RA\_CLOCK\_SSI](#ac0759645d4e2eee4818ef19fbbc2fcbf)(channel) |
| #define | [RA\_CLOCK\_SRC](#ab3382620555e10cd592efee37292529b)(channel) |
| #define | [RA\_CLOCK\_SDHIMMC](#a935564cc66df3b92c3a7ab57576c767a)(channel) |
| #define | [RA\_CLOCK\_DOC](#a5327566599aaac63d9efdd22ba9e1ab8)(channel) |
| #define | [RA\_CLOCK\_ELC](#a16a6667bd062060789a03a13bf53bef3)(channel) |
| #define | [RA\_CLOCK\_CEU](#a95cb45c4f05a85e2bf219f37e0adaf69)(channel) |
| #define | [RA\_CLOCK\_TFU](#a50855e5282bf718b6db83049bb6b7398)(channel) |
| #define | [RA\_CLOCK\_IIRFA](#add1f20a0973fe201ab9153e2ea7f20f9)(channel) |
| #define | [RA\_CLOCK\_CANFD](#a09d5b47c76c23d0250a2b06dfb076bc5)(channel) |
| #define | [RA\_CLOCK\_TRNG](#a38f3c27d996565d95ae1f6736208ddc6)(channel) |
| #define | [RA\_CLOCK\_SCE](#aa2a0c842cb4aa71966b1fb2c397aa924)(channel) |
| #define | [RA\_CLOCK\_AES](#a658efca6ca2f020ff8f98cb87d2d2520)(channel) |
| #define | [RA\_CLOCK\_POEG](#a35c288f044ae4ed5976d59641ab98836)(channel) |
| #define | [RA\_CLOCK\_ADC](#aac1fa19e11369a88fa4a829b8c879ce6)(channel) |
| #define | [RA\_CLOCK\_SDADC](#a168c711530cba89aec124560bed817bf)(channel) |
| #define | [RA\_CLOCK\_DAC8](#ad37fb3aa2527609a8b13084632662b34)(channel) |
| #define | [RA\_CLOCK\_DAC](#a67d7d9b9062858127aa056ce432cc0fe)(channel) |
| #define | [RA\_CLOCK\_TSN](#ab836d99882fd4aa5fd1ac36712e44877)(channel) |
| #define | [RA\_CLOCK\_ACMPHS](#ab7ef7f184b959df98de7d79297bb8550)(channel) |
| #define | [RA\_CLOCK\_ACMPLP](#aaa5130e00b4f8d00e45f65b969acf2d6)(channel) |
| #define | [RA\_CLOCK\_OPAMP](#a12564ad39a8eb4ee9821fb1f060702d6)(channel) |
| #define | [RA\_CLOCK\_AGT](#ac049286369b5979c85cedbab2a820096)(channel) |
| #define | [RA\_CLOCK\_KEY](#a8a76e240fbd3892ac80c21e5d6f0d53b)(channel) |
| #define | [RA\_CLOCK\_ULPT](#a157466252ee4cccc21c7ab70c25b4269)(channel) |
| #define | [RA\_CLOCK\_GPT](#a06453156b29ff923b7f12c01b7f57690)(channel) |

## Macro Definition Documentation

## [◆ ](#a37dac2de2c6eeab25e2ed9de75edc4ba)RA\_CLOCK

| #define RA\_CLOCK | ( |  | *grp*, |
| --- | --- | --- | --- |
|  |  |  | *func*, |
|  |  |  | *ch* ) |

**Value:**

((grp << 28) | (func << 20) | ch)

## [◆ ](#ab7ef7f184b959df98de7d79297bb8550)RA\_CLOCK\_ACMPHS

| #define RA\_CLOCK\_ACMPHS | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(3, 28U, channel)

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)

#define RA\_CLOCK(grp, func, ch)

**Definition** renesas-ra-cgc.h:10

## [◆ ](#aaa5130e00b4f8d00e45f65b969acf2d6)RA\_CLOCK\_ACMPLP

| #define RA\_CLOCK\_ACMPLP | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(3, 29U, channel)

## [◆ ](#aac1fa19e11369a88fa4a829b8c879ce6)RA\_CLOCK\_ADC

| #define RA\_CLOCK\_ADC | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(3, 16U, channel)

## [◆ ](#a658efca6ca2f020ff8f98cb87d2d2520)RA\_CLOCK\_AES

| #define RA\_CLOCK\_AES | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(2, 31U, channel)

## [◆ ](#ac049286369b5979c85cedbab2a820096)RA\_CLOCK\_AGT

| #define RA\_CLOCK\_AGT | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(4, 3U, channel)

## [◆ ](#ad2d935ba5827105c9ac5b13a3a189ab0)RA\_CLOCK\_BIT

| #define RA\_CLOCK\_BIT | ( |  | *mod* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(((mod >> 20) & 0xFF) - ((mod >> 0) & 0xF))

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

## [◆ ](#a7c935768ee984933b2ecceb3d3c7b068)RA\_CLOCK\_CAC

| #define RA\_CLOCK\_CAC | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(2, 0U, channel)

## [◆ ](#aa6c6a052fa47101bc07b1cde7d0c8a9e)RA\_CLOCK\_CAN

| #define RA\_CLOCK\_CAN | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(1, 2, channel)

## [◆ ](#a09d5b47c76c23d0250a2b06dfb076bc5)RA\_CLOCK\_CANFD

| #define RA\_CLOCK\_CANFD | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(2, 27U, channel)

## [◆ ](#a00974ed13a8ba59014206d622175903e)RA\_CLOCK\_CEC

| #define RA\_CLOCK\_CEC | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(1, 3U, channel)

## [◆ ](#a95cb45c4f05a85e2bf219f37e0adaf69)RA\_CLOCK\_CEU

| #define RA\_CLOCK\_CEU | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(2, 16U, channel)

## [◆ ](#a03eaba37f88043e0e18c8c184c5fa9ca)RA\_CLOCK\_CRC

| #define RA\_CLOCK\_CRC | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(2, 1U, channel)

## [◆ ](#ab1cc63937cef3f1eb0377b333b6ff2f4)RA\_CLOCK\_CTSU

| #define RA\_CLOCK\_CTSU | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(2, 3U, channel)

## [◆ ](#a67d7d9b9062858127aa056ce432cc0fe)RA\_CLOCK\_DAC

| #define RA\_CLOCK\_DAC | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(3, 20U, channel)

## [◆ ](#ad37fb3aa2527609a8b13084632662b34)RA\_CLOCK\_DAC8

| #define RA\_CLOCK\_DAC8 | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(3, 19U, channel)

## [◆ ](#ad4dfc984527e53e86162fd2f653768be)RA\_CLOCK\_DMAC

| #define RA\_CLOCK\_DMAC | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(0, 22, channel)

## [◆ ](#a5327566599aaac63d9efdd22ba9e1ab8)RA\_CLOCK\_DOC

| #define RA\_CLOCK\_DOC | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(2, 13U, channel)

## [◆ ](#a2a4921ce74876f3f18d334e4def418b5)RA\_CLOCK\_DRW

| #define RA\_CLOCK\_DRW | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(2, 6U, channel)

## [◆ ](#a3ddb10bc4a6eed8a67a4bc2a373343c5)RA\_CLOCK\_DTC

| #define RA\_CLOCK\_DTC | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(0, 22, channel)

## [◆ ](#a16a6667bd062060789a03a13bf53bef3)RA\_CLOCK\_ELC

| #define RA\_CLOCK\_ELC | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(2, 14U, channel)

## [◆ ](#ad6a3eb4b0a0fe5fdeb432d2aa30811f7)RA\_CLOCK\_EPTPC

| #define RA\_CLOCK\_EPTPC | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(1, 13U, channel)

## [◆ ](#a1ff75408ca2eb508b42130c0c5b6167e)RA\_CLOCK\_ETHER

| #define RA\_CLOCK\_ETHER | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(1, 15U, channel)

## [◆ ](#a85533bf4da5b6f75aa16ce1cc7e4cbad)RA\_CLOCK\_GLCDC

| #define RA\_CLOCK\_GLCDC | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(2, 4U, channel)

## [◆ ](#a06453156b29ff923b7f12c01b7f57690)RA\_CLOCK\_GPT

| #define RA\_CLOCK\_GPT | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(5, 31U, channel)

## [◆ ](#ac6af2db5eb5e2826456e6e36ef78320b)RA\_CLOCK\_GROUP

| #define RA\_CLOCK\_GROUP | ( |  | *mod* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((mod >> 28) & 0xF) \* 4)

## [◆ ](#a6724e283fa86f2a1a54e2f3b9be8bd3b)RA\_CLOCK\_I3C

| #define RA\_CLOCK\_I3C | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(1, 4U, channel)

## [◆ ](#abb191de59b4e661f23fa5b8bdc0e6735)RA\_CLOCK\_IIC

| #define RA\_CLOCK\_IIC | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(1, 9U, channel)

## [◆ ](#add1f20a0973fe201ab9153e2ea7f20f9)RA\_CLOCK\_IIRFA

| #define RA\_CLOCK\_IIRFA | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(2, 21U, channel)

## [◆ ](#abc119ce6dc201c22f2c3984600716667)RA\_CLOCK\_IRDA

| #define RA\_CLOCK\_IRDA | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(1, 5U, channel)

## [◆ ](#a7f6f30e7f3f1ce6fc1ae393dbe4060ac)RA\_CLOCK\_JPEG

| #define RA\_CLOCK\_JPEG | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(2, 5U, channel)

## [◆ ](#a8a76e240fbd3892ac80c21e5d6f0d53b)RA\_CLOCK\_KEY

| #define RA\_CLOCK\_KEY | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(4, 4U, channel)

## [◆ ](#a12564ad39a8eb4ee9821fb1f060702d6)RA\_CLOCK\_OPAMP

| #define RA\_CLOCK\_OPAMP | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(3, 31U, channel)

## [◆ ](#a2d1f85ce9073177e1e4c662a8fcea802)RA\_CLOCK\_OSPI

| #define RA\_CLOCK\_OSPI | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(1, 16U, channel)

## [◆ ](#a2268067bebcb6fc2504354a59a9d7b1f)RA\_CLOCK\_PDC

| #define RA\_CLOCK\_PDC | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(2, 2U, channel)

## [◆ ](#a35c288f044ae4ed5976d59641ab98836)RA\_CLOCK\_POEG

| #define RA\_CLOCK\_POEG | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(3, 14U, channel)

## [◆ ](#a4334a46b749963ef0ca7d1437acefc70)RA\_CLOCK\_QSPI

| #define RA\_CLOCK\_QSPI | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(1, 6U, channel)

## [◆ ](#aa2a0c842cb4aa71966b1fb2c397aa924)RA\_CLOCK\_SCE

| #define RA\_CLOCK\_SCE | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(2, 31U, channel)

## [◆ ](#a6e1e337469bda99de331098a3a75b57e)RA\_CLOCK\_SCI

| #define RA\_CLOCK\_SCI | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(1, 31U, channel)

## [◆ ](#a168c711530cba89aec124560bed817bf)RA\_CLOCK\_SDADC

| #define RA\_CLOCK\_SDADC | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(3, 17U, channel)

## [◆ ](#a935564cc66df3b92c3a7ab57576c767a)RA\_CLOCK\_SDHIMMC

| #define RA\_CLOCK\_SDHIMMC | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(2, 12U, channel)

## [◆ ](#a238e1efc42e368172af9f5f9a50e7ae7)RA\_CLOCK\_SLCDC

| #define RA\_CLOCK\_SLCDC | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(2, 4U, channel)

## [◆ ](#a9907d81a9a8279782dbad1123ed9cabc)RA\_CLOCK\_SPI

| #define RA\_CLOCK\_SPI | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(1, 19U, channel)

## [◆ ](#ab3382620555e10cd592efee37292529b)RA\_CLOCK\_SRC

| #define RA\_CLOCK\_SRC | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(2, 9U, channel)

## [◆ ](#ac0759645d4e2eee4818ef19fbbc2fcbf)RA\_CLOCK\_SSI

| #define RA\_CLOCK\_SSI | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(2, 8U, channel)

## [◆ ](#a50855e5282bf718b6db83049bb6b7398)RA\_CLOCK\_TFU

| #define RA\_CLOCK\_TFU | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(2, 20U, channel)

## [◆ ](#a38f3c27d996565d95ae1f6736208ddc6)RA\_CLOCK\_TRNG

| #define RA\_CLOCK\_TRNG | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(2, 28U, channel)

## [◆ ](#ab836d99882fd4aa5fd1ac36712e44877)RA\_CLOCK\_TSN

| #define RA\_CLOCK\_TSN | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(3, 22U, channel)

## [◆ ](#a157466252ee4cccc21c7ab70c25b4269)RA\_CLOCK\_ULPT

| #define RA\_CLOCK\_ULPT | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(4, 9U, channel)

## [◆ ](#a7601cf92d860ef7be29a7086e948c95f)RA\_CLOCK\_USBFS

| #define RA\_CLOCK\_USBFS | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(1, 11U, channel)

## [◆ ](#ae19013bef5f3f49ac258f897baac8957)RA\_CLOCK\_USBHS

| #define RA\_CLOCK\_USBHS | ( |  | *channel* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[RA\_CLOCK](#a37dac2de2c6eeab25e2ed9de75edc4ba)(1, 12U, channel)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [renesas-ra-cgc.h](renesas-ra-cgc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
