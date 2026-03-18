---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/r8a7795__cpg__mssr_8h_source.html
original_path: doxygen/html/r8a7795__cpg__mssr_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

r8a7795\_cpg\_mssr.h

[Go to the documentation of this file.](r8a7795__cpg__mssr_8h.md)

1/\*

2 \* Copyright (c) 2022 IoT.bzh

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_RENESAS\_CLOCK\_R8A7795\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_RENESAS\_CLOCK\_R8A7795\_H\_

9

10#include "[renesas\_cpg\_mssr.h](dt-bindings_2clock_2renesas__cpg__mssr_8h.md)"

11

12/\* r8a7795 CPG Core Clocks \*/

[ 13](r8a7795__cpg__mssr_8h.md#a791637471e9a1557349c6a1b10c520b2)#define R8A7795\_CLK\_Z 0

[ 14](r8a7795__cpg__mssr_8h.md#a2939ba8a3626c3e3bc9041e9b478d4ee)#define R8A7795\_CLK\_Z2 1

[ 15](r8a7795__cpg__mssr_8h.md#acba46ef45bda4cb6365fdb89d67e3e44)#define R8A7795\_CLK\_ZR 2

[ 16](r8a7795__cpg__mssr_8h.md#a8a8cbb2ab5dc1b34fd8c8e859fb2fa35)#define R8A7795\_CLK\_ZG 3

[ 17](r8a7795__cpg__mssr_8h.md#ab89160b83e87f2dd660e73651eb3a415)#define R8A7795\_CLK\_ZTR 4

[ 18](r8a7795__cpg__mssr_8h.md#af5b5eb9a60a798f22bd3b80d13d193e9)#define R8A7795\_CLK\_ZTRD2 5

[ 19](r8a7795__cpg__mssr_8h.md#a7d21c13a093aaf8d57a2ea7ab068eba5)#define R8A7795\_CLK\_ZT 6

[ 20](r8a7795__cpg__mssr_8h.md#a53b8c6eedcc398208bc8ec49a99a0ec8)#define R8A7795\_CLK\_ZX 7

[ 21](r8a7795__cpg__mssr_8h.md#ab14a90dbd88fd156cc8f9e78e1d22549)#define R8A7795\_CLK\_S0D1 8

[ 22](r8a7795__cpg__mssr_8h.md#a269643ef549e62aa5591da97c544c7ef)#define R8A7795\_CLK\_S0D4 9

[ 23](r8a7795__cpg__mssr_8h.md#aca4cf1624444c1ea2481c99f9d9632d1)#define R8A7795\_CLK\_S1D1 10

[ 24](r8a7795__cpg__mssr_8h.md#ad322249233f1ec83d12aa5aee87b920f)#define R8A7795\_CLK\_S1D2 11

[ 25](r8a7795__cpg__mssr_8h.md#a238fa0708ced8264ba52bab369234d6b)#define R8A7795\_CLK\_S1D4 12

[ 26](r8a7795__cpg__mssr_8h.md#a709c9d070899119f46716b2e089fa25d)#define R8A7795\_CLK\_S2D1 13

[ 27](r8a7795__cpg__mssr_8h.md#aa567bc0c6eb22279009529d7ab13ddf9)#define R8A7795\_CLK\_S2D2 14

[ 28](r8a7795__cpg__mssr_8h.md#a264b266e2509902004f38e843e7244bb)#define R8A7795\_CLK\_S2D4 15

[ 29](r8a7795__cpg__mssr_8h.md#ad927df9886612f8a98d9905676766c35)#define R8A7795\_CLK\_S3D1 16

[ 30](r8a7795__cpg__mssr_8h.md#ad11ed136c9ec09aafd338286ffbf22a5)#define R8A7795\_CLK\_S3D2 17

[ 31](r8a7795__cpg__mssr_8h.md#af8f6e89c25573b20b74396e3f3c43f2d)#define R8A7795\_CLK\_S3D4 18 /\* SCIF clock \*/

[ 32](r8a7795__cpg__mssr_8h.md#acdd1bb9c5ca6585c60aec776f195101a)#define R8A7795\_CLK\_LB 19

[ 33](r8a7795__cpg__mssr_8h.md#ad9f7a90a91738231153f1e44680dddc2)#define R8A7795\_CLK\_CL 20

[ 34](r8a7795__cpg__mssr_8h.md#a15ab3c3c6f295b9e46ff86980802c734)#define R8A7795\_CLK\_ZB3 21

[ 35](r8a7795__cpg__mssr_8h.md#a46c758617fc3566eb0b43185c621ca9b)#define R8A7795\_CLK\_ZB3D2 22

[ 36](r8a7795__cpg__mssr_8h.md#ab514dda758baadc4c9f8263d534c091b)#define R8A7795\_CLK\_CR 23

[ 37](r8a7795__cpg__mssr_8h.md#a9131eb62e177743859a612d48d206e1b)#define R8A7795\_CLK\_CRD2 24

[ 38](r8a7795__cpg__mssr_8h.md#a307aba919a11cdb5cf6ca285548fcc99)#define R8A7795\_CLK\_SD0H 25

[ 39](r8a7795__cpg__mssr_8h.md#ab5dba914038dfab3ddf1e28ffeb8c49e)#define R8A7795\_CLK\_SD0 26

[ 40](r8a7795__cpg__mssr_8h.md#acb99980ea38838c57bbc149998547fb6)#define R8A7795\_CLK\_SD1H 27

[ 41](r8a7795__cpg__mssr_8h.md#a7f1172e8eff7af14338ff21a5e714382)#define R8A7795\_CLK\_SD1 28

[ 42](r8a7795__cpg__mssr_8h.md#abf0e7520b5542c3b3fe2688131678f84)#define R8A7795\_CLK\_SD2H 29

[ 43](r8a7795__cpg__mssr_8h.md#a66f8cd659d06a60c67bb0ea07bb73fd5)#define R8A7795\_CLK\_SD2 30

[ 44](r8a7795__cpg__mssr_8h.md#a425a5f8361768cd75d8b19382f1e0223)#define R8A7795\_CLK\_SD3H 31

[ 45](r8a7795__cpg__mssr_8h.md#a15c4d55e7ddb1bd4b9729b24dc8a7f78)#define R8A7795\_CLK\_SD3 32

[ 46](r8a7795__cpg__mssr_8h.md#ac304d83d429fb398a31de2f3c17febda)#define R8A7795\_CLK\_SSP2 33

[ 47](r8a7795__cpg__mssr_8h.md#a6c3311a4095d32df4f962ee0f6c1d3ef)#define R8A7795\_CLK\_SSP1 34

[ 48](r8a7795__cpg__mssr_8h.md#a181121b1e08248f5837d4239dc50f8ec)#define R8A7795\_CLK\_SSPRS 35

[ 49](r8a7795__cpg__mssr_8h.md#a1b83fdfed567ad9a96f73a858e6bbeee)#define R8A7795\_CLK\_RPC 36

[ 50](r8a7795__cpg__mssr_8h.md#a8f264113c79d8d83465988474afbf11e)#define R8A7795\_CLK\_RPCD2 37

[ 51](r8a7795__cpg__mssr_8h.md#a1ce78418caaa586d8feb1f5e4e8bf516)#define R8A7795\_CLK\_MSO 38

[ 52](r8a7795__cpg__mssr_8h.md#ad2650c42301eba8e0405350fdc84e5ef)#define R8A7795\_CLK\_CANFD 39 /\* CANFD clock \*/

[ 53](r8a7795__cpg__mssr_8h.md#a7ba61021f2d2a0a0e485cb488f8e41b8)#define R8A7795\_CLK\_HDMI 40

[ 54](r8a7795__cpg__mssr_8h.md#a0a8d3ee85acb42f4c98f5aed56634d95)#define R8A7795\_CLK\_CSI0 41

55/\* CLK\_CSIREF was removed \*/

[ 56](r8a7795__cpg__mssr_8h.md#a035540e9632fddefdfd0621f477bba0a)#define R8A7795\_CLK\_CP 43

[ 57](r8a7795__cpg__mssr_8h.md#a874ec492aa6b8cf41f88f3695100b022)#define R8A7795\_CLK\_CPEX 44

[ 58](r8a7795__cpg__mssr_8h.md#a277ba0be094773d02ab3987d79e48fab)#define R8A7795\_CLK\_R 45

[ 59](r8a7795__cpg__mssr_8h.md#a40d639df5cc4f533637d033e13d9dff9)#define R8A7795\_CLK\_OSC 46

60

61/\* r8a7795 ES2.0 CPG Core Clocks \*/

[ 62](r8a7795__cpg__mssr_8h.md#a9b0475c30403b6a00c346b13577c077d)#define R8A7795\_CLK\_S0D2 47

[ 63](r8a7795__cpg__mssr_8h.md#ab80410f646a7807e166a0e5ae1453dbd)#define R8A7795\_CLK\_S0D3 48

[ 64](r8a7795__cpg__mssr_8h.md#a0ebd5fcae8b38a499c97df0b358617f0)#define R8A7795\_CLK\_S0D6 49

[ 65](r8a7795__cpg__mssr_8h.md#ad391f852747393ba5c7d66dec63d327d)#define R8A7795\_CLK\_S0D8 50

[ 66](r8a7795__cpg__mssr_8h.md#ab7e946d0f160786b5e0516417d007085)#define R8A7795\_CLK\_S0D12 51

67

68#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_RENESAS\_CLOCK\_R8A7795\_H\_ \*/

[renesas\_cpg\_mssr.h](dt-bindings_2clock_2renesas__cpg__mssr_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [r8a7795\_cpg\_mssr.h](r8a7795__cpg__mssr_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
