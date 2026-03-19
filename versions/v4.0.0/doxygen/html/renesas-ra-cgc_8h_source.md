---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/renesas-ra-cgc_8h_source.html
original_path: doxygen/html/renesas-ra-cgc_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

renesas-ra-cgc.h

[Go to the documentation of this file.](renesas-ra-cgc_8h.md)

1/\*

2 \* Copyright (c) 2023 TOKITA Hiroshi <tokita.hiroshi@fujitsu.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_DT\_BINDINGS\_CLOCK\_RENESAS\_RA\_CGC\_H\_

8#define ZEPHYR\_DT\_BINDINGS\_CLOCK\_RENESAS\_RA\_CGC\_H\_

9

[ 10](renesas-ra-cgc_8h.md#a37dac2de2c6eeab25e2ed9de75edc4ba)#define RA\_CLOCK(grp, func, ch) ((grp << 28) | (func << 20) | ch)

11

[ 12](renesas-ra-cgc_8h.md#ac6af2db5eb5e2826456e6e36ef78320b)#define RA\_CLOCK\_GROUP(mod) (((mod >> 28) & 0xF) \* 4)

[ 13](renesas-ra-cgc_8h.md#ad2d935ba5827105c9ac5b13a3a189ab0)#define RA\_CLOCK\_BIT(mod) BIT(((mod >> 20) & 0xFF) - ((mod >> 0) & 0xF))

14

[ 15](renesas-ra-cgc_8h.md#ad4dfc984527e53e86162fd2f653768be)#define RA\_CLOCK\_DMAC(channel) RA\_CLOCK(0, 22, channel)

[ 16](renesas-ra-cgc_8h.md#a3ddb10bc4a6eed8a67a4bc2a373343c5)#define RA\_CLOCK\_DTC(channel) RA\_CLOCK(0, 22, channel)

[ 17](renesas-ra-cgc_8h.md#aa6c6a052fa47101bc07b1cde7d0c8a9e)#define RA\_CLOCK\_CAN(channel) RA\_CLOCK(1, 2, channel)

[ 18](renesas-ra-cgc_8h.md#a00974ed13a8ba59014206d622175903e)#define RA\_CLOCK\_CEC(channel) RA\_CLOCK(1, 3U, channel)

[ 19](renesas-ra-cgc_8h.md#a6724e283fa86f2a1a54e2f3b9be8bd3b)#define RA\_CLOCK\_I3C(channel) RA\_CLOCK(1, 4U, channel)

[ 20](renesas-ra-cgc_8h.md#abc119ce6dc201c22f2c3984600716667)#define RA\_CLOCK\_IRDA(channel) RA\_CLOCK(1, 5U, channel)

[ 21](renesas-ra-cgc_8h.md#a4334a46b749963ef0ca7d1437acefc70)#define RA\_CLOCK\_QSPI(channel) RA\_CLOCK(1, 6U, channel)

[ 22](renesas-ra-cgc_8h.md#abb191de59b4e661f23fa5b8bdc0e6735)#define RA\_CLOCK\_IIC(channel) RA\_CLOCK(1, 9U, channel)

[ 23](renesas-ra-cgc_8h.md#a7601cf92d860ef7be29a7086e948c95f)#define RA\_CLOCK\_USBFS(channel) RA\_CLOCK(1, 11U, channel)

[ 24](renesas-ra-cgc_8h.md#ae19013bef5f3f49ac258f897baac8957)#define RA\_CLOCK\_USBHS(channel) RA\_CLOCK(1, 12U, channel)

[ 25](renesas-ra-cgc_8h.md#ad6a3eb4b0a0fe5fdeb432d2aa30811f7)#define RA\_CLOCK\_EPTPC(channel) RA\_CLOCK(1, 13U, channel)

[ 26](renesas-ra-cgc_8h.md#a1ff75408ca2eb508b42130c0c5b6167e)#define RA\_CLOCK\_ETHER(channel) RA\_CLOCK(1, 15U, channel)

[ 27](renesas-ra-cgc_8h.md#a2d1f85ce9073177e1e4c662a8fcea802)#define RA\_CLOCK\_OSPI(channel) RA\_CLOCK(1, 16U, channel)

[ 28](renesas-ra-cgc_8h.md#a9907d81a9a8279782dbad1123ed9cabc)#define RA\_CLOCK\_SPI(channel) RA\_CLOCK(1, 19U, channel)

[ 29](renesas-ra-cgc_8h.md#a6e1e337469bda99de331098a3a75b57e)#define RA\_CLOCK\_SCI(channel) RA\_CLOCK(1, 31U, channel)

[ 30](renesas-ra-cgc_8h.md#a7c935768ee984933b2ecceb3d3c7b068)#define RA\_CLOCK\_CAC(channel) RA\_CLOCK(2, 0U, channel)

[ 31](renesas-ra-cgc_8h.md#a03eaba37f88043e0e18c8c184c5fa9ca)#define RA\_CLOCK\_CRC(channel) RA\_CLOCK(2, 1U, channel)

[ 32](renesas-ra-cgc_8h.md#a2268067bebcb6fc2504354a59a9d7b1f)#define RA\_CLOCK\_PDC(channel) RA\_CLOCK(2, 2U, channel)

[ 33](renesas-ra-cgc_8h.md#ab1cc63937cef3f1eb0377b333b6ff2f4)#define RA\_CLOCK\_CTSU(channel) RA\_CLOCK(2, 3U, channel)

[ 34](renesas-ra-cgc_8h.md#a238e1efc42e368172af9f5f9a50e7ae7)#define RA\_CLOCK\_SLCDC(channel) RA\_CLOCK(2, 4U, channel)

[ 35](renesas-ra-cgc_8h.md#a85533bf4da5b6f75aa16ce1cc7e4cbad)#define RA\_CLOCK\_GLCDC(channel) RA\_CLOCK(2, 4U, channel)

[ 36](renesas-ra-cgc_8h.md#a7f6f30e7f3f1ce6fc1ae393dbe4060ac)#define RA\_CLOCK\_JPEG(channel) RA\_CLOCK(2, 5U, channel)

[ 37](renesas-ra-cgc_8h.md#a2a4921ce74876f3f18d334e4def418b5)#define RA\_CLOCK\_DRW(channel) RA\_CLOCK(2, 6U, channel)

[ 38](renesas-ra-cgc_8h.md#ac0759645d4e2eee4818ef19fbbc2fcbf)#define RA\_CLOCK\_SSI(channel) RA\_CLOCK(2, 8U, channel)

[ 39](renesas-ra-cgc_8h.md#ab3382620555e10cd592efee37292529b)#define RA\_CLOCK\_SRC(channel) RA\_CLOCK(2, 9U, channel)

[ 40](renesas-ra-cgc_8h.md#a935564cc66df3b92c3a7ab57576c767a)#define RA\_CLOCK\_SDHIMMC(channel) RA\_CLOCK(2, 12U, channel)

[ 41](renesas-ra-cgc_8h.md#a5327566599aaac63d9efdd22ba9e1ab8)#define RA\_CLOCK\_DOC(channel) RA\_CLOCK(2, 13U, channel)

[ 42](renesas-ra-cgc_8h.md#a16a6667bd062060789a03a13bf53bef3)#define RA\_CLOCK\_ELC(channel) RA\_CLOCK(2, 14U, channel)

[ 43](renesas-ra-cgc_8h.md#a95cb45c4f05a85e2bf219f37e0adaf69)#define RA\_CLOCK\_CEU(channel) RA\_CLOCK(2, 16U, channel)

[ 44](renesas-ra-cgc_8h.md#a50855e5282bf718b6db83049bb6b7398)#define RA\_CLOCK\_TFU(channel) RA\_CLOCK(2, 20U, channel)

[ 45](renesas-ra-cgc_8h.md#add1f20a0973fe201ab9153e2ea7f20f9)#define RA\_CLOCK\_IIRFA(channel) RA\_CLOCK(2, 21U, channel)

[ 46](renesas-ra-cgc_8h.md#a09d5b47c76c23d0250a2b06dfb076bc5)#define RA\_CLOCK\_CANFD(channel) RA\_CLOCK(2, 27U, channel)

[ 47](renesas-ra-cgc_8h.md#a38f3c27d996565d95ae1f6736208ddc6)#define RA\_CLOCK\_TRNG(channel) RA\_CLOCK(2, 28U, channel)

[ 48](renesas-ra-cgc_8h.md#aa2a0c842cb4aa71966b1fb2c397aa924)#define RA\_CLOCK\_SCE(channel) RA\_CLOCK(2, 31U, channel)

[ 49](renesas-ra-cgc_8h.md#a658efca6ca2f020ff8f98cb87d2d2520)#define RA\_CLOCK\_AES(channel) RA\_CLOCK(2, 31U, channel)

[ 50](renesas-ra-cgc_8h.md#a35c288f044ae4ed5976d59641ab98836)#define RA\_CLOCK\_POEG(channel) RA\_CLOCK(3, 14U, channel)

[ 51](renesas-ra-cgc_8h.md#aac1fa19e11369a88fa4a829b8c879ce6)#define RA\_CLOCK\_ADC(channel) RA\_CLOCK(3, 16U, channel)

[ 52](renesas-ra-cgc_8h.md#a168c711530cba89aec124560bed817bf)#define RA\_CLOCK\_SDADC(channel) RA\_CLOCK(3, 17U, channel)

[ 53](renesas-ra-cgc_8h.md#ad37fb3aa2527609a8b13084632662b34)#define RA\_CLOCK\_DAC8(channel) RA\_CLOCK(3, 19U, channel)

[ 54](renesas-ra-cgc_8h.md#a67d7d9b9062858127aa056ce432cc0fe)#define RA\_CLOCK\_DAC(channel) RA\_CLOCK(3, 20U, channel)

[ 55](renesas-ra-cgc_8h.md#ab836d99882fd4aa5fd1ac36712e44877)#define RA\_CLOCK\_TSN(channel) RA\_CLOCK(3, 22U, channel)

[ 56](renesas-ra-cgc_8h.md#ab7ef7f184b959df98de7d79297bb8550)#define RA\_CLOCK\_ACMPHS(channel) RA\_CLOCK(3, 28U, channel)

[ 57](renesas-ra-cgc_8h.md#aaa5130e00b4f8d00e45f65b969acf2d6)#define RA\_CLOCK\_ACMPLP(channel) RA\_CLOCK(3, 29U, channel)

[ 58](renesas-ra-cgc_8h.md#a12564ad39a8eb4ee9821fb1f060702d6)#define RA\_CLOCK\_OPAMP(channel) RA\_CLOCK(3, 31U, channel)

[ 59](renesas-ra-cgc_8h.md#ac049286369b5979c85cedbab2a820096)#define RA\_CLOCK\_AGT(channel) RA\_CLOCK(4, 3U, channel)

[ 60](renesas-ra-cgc_8h.md#a8a76e240fbd3892ac80c21e5d6f0d53b)#define RA\_CLOCK\_KEY(channel) RA\_CLOCK(4, 4U, channel)

[ 61](renesas-ra-cgc_8h.md#a157466252ee4cccc21c7ab70c25b4269)#define RA\_CLOCK\_ULPT(channel) RA\_CLOCK(4, 9U, channel)

[ 62](renesas-ra-cgc_8h.md#a06453156b29ff923b7f12c01b7f57690)#define RA\_CLOCK\_GPT(channel) RA\_CLOCK(5, 31U, channel)

63

64#endif /\* ZEPHYR\_DT\_BINDINGS\_CLOCK\_RENESAS\_RA\_CGC\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [renesas-ra-cgc.h](renesas-ra-cgc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
