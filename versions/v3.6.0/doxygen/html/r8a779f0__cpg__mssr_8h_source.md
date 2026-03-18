---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/r8a779f0__cpg__mssr_8h_source.html
original_path: doxygen/html/r8a779f0__cpg__mssr_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

r8a779f0\_cpg\_mssr.h

[Go to the documentation of this file.](r8a779f0__cpg__mssr_8h.md)

1/\*

2 \* Copyright (c) 2023 IoT.bzh

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_RENESAS\_CLOCK\_R8A779F0\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_RENESAS\_CLOCK\_R8A779F0\_H\_

9

10#include "[renesas\_cpg\_mssr.h](dt-bindings_2clock_2renesas__cpg__mssr_8h.md)"

11

12/\* r8a779f0 CPG Core Clocks \*/

[ 13](r8a779f0__cpg__mssr_8h.md#abc3be8d319b77d137e15698ce4ec6816)#define R8A779F0\_CLK\_Z0 0

[ 14](r8a779f0__cpg__mssr_8h.md#a58a71802b95b1c82e4ffa90d18ca1a8a)#define R8A779F0\_CLK\_Z1 1

[ 15](r8a779f0__cpg__mssr_8h.md#a7bea0a74bec2641fb47ad0abdd16c03a)#define R8A779F0\_CLK\_ZR 2

[ 16](r8a779f0__cpg__mssr_8h.md#a77af2b33b2eeb197432c9373a13d9bb7)#define R8A779F0\_CLK\_ZX 3

[ 17](r8a779f0__cpg__mssr_8h.md#a37b79c999898d124b8d15aa396f394cb)#define R8A779F0\_CLK\_ZS 4

[ 18](r8a779f0__cpg__mssr_8h.md#a7357e4499fe58fb18c1e13e47960310b)#define R8A779F0\_CLK\_ZT 5

[ 19](r8a779f0__cpg__mssr_8h.md#aac193bbfa03cb6553fe780444f3e18f0)#define R8A779F0\_CLK\_ZTR 6

[ 20](r8a779f0__cpg__mssr_8h.md#acad7d7f64ca6f8074784391c617580a2)#define R8A779F0\_CLK\_S0D2 7

[ 21](r8a779f0__cpg__mssr_8h.md#a51367bf3cc3da59ffd95f013ae72f97d)#define R8A779F0\_CLK\_S0D3 8

[ 22](r8a779f0__cpg__mssr_8h.md#a9ff70a4d5a66da6133c552f10b7d782d)#define R8A779F0\_CLK\_S0D4 9

[ 23](r8a779f0__cpg__mssr_8h.md#ac7c8deb6d689b66b58d20ea2e2f7792a)#define R8A779F0\_CLK\_S0D2\_MM 10

[ 24](r8a779f0__cpg__mssr_8h.md#a63fdd4f4dd67455113a9fffada6b62f1)#define R8A779F0\_CLK\_S0D3\_MM 11

[ 25](r8a779f0__cpg__mssr_8h.md#a629696914317083bdcc450a2eb146a63)#define R8A779F0\_CLK\_S0D4\_MM 12

[ 26](r8a779f0__cpg__mssr_8h.md#a998c52482581c660501edaff04e92e60)#define R8A779F0\_CLK\_S0D2\_RT 13

[ 27](r8a779f0__cpg__mssr_8h.md#ab08009da20dbba7bdbf9e4c44c616491)#define R8A779F0\_CLK\_S0D3\_RT 14

[ 28](r8a779f0__cpg__mssr_8h.md#a2a983d2d3882206b952ddd1ff367980c)#define R8A779F0\_CLK\_S0D4\_RT 15

[ 29](r8a779f0__cpg__mssr_8h.md#ac147e12a244f14192e47c79243b617e7)#define R8A779F0\_CLK\_S0D6\_RT 16

[ 30](r8a779f0__cpg__mssr_8h.md#a4bdc5bc00199daf71558a7e5961b44f0)#define R8A779F0\_CLK\_S0D3\_PER 17

[ 31](r8a779f0__cpg__mssr_8h.md#a032a9ea3eaa6c885ee5a42cfcdcb9b93)#define R8A779F0\_CLK\_S0D6\_PER 18

[ 32](r8a779f0__cpg__mssr_8h.md#a9ff5a6188c09d562a49545f2e04ba7bd)#define R8A779F0\_CLK\_S0D12\_PER 19

[ 33](r8a779f0__cpg__mssr_8h.md#abfbcacc1efcf85b9948af3875f27584d)#define R8A779F0\_CLK\_S0D24\_PER 20

[ 34](r8a779f0__cpg__mssr_8h.md#adc4116c7b3620054f8d0a9931d81a8ce)#define R8A779F0\_CLK\_S0D2\_HSC 21

[ 35](r8a779f0__cpg__mssr_8h.md#af2c392c805ddc652df3f0bf250fd0cab)#define R8A779F0\_CLK\_S0D3\_HSC 22

[ 36](r8a779f0__cpg__mssr_8h.md#ab2da14debe9dde16622175be16c65d36)#define R8A779F0\_CLK\_S0D4\_HSC 23

[ 37](r8a779f0__cpg__mssr_8h.md#a61a850e9d318fe0369cf9183dbd2ccb9)#define R8A779F0\_CLK\_S0D6\_HSC 24

[ 38](r8a779f0__cpg__mssr_8h.md#a365df22690d0920a2cc2f8cb0baa2978)#define R8A779F0\_CLK\_S0D12\_HSC 25

[ 39](r8a779f0__cpg__mssr_8h.md#a86bc6ca1839080653590e48409266334)#define R8A779F0\_CLK\_S0D2\_CC 26

[ 40](r8a779f0__cpg__mssr_8h.md#a462f61c97f1214e538222c54e1ec344a)#define R8A779F0\_CLK\_CL 27

[ 41](r8a779f0__cpg__mssr_8h.md#a16a53521e26b017b716b513be5f7b466)#define R8A779F0\_CLK\_CL16M 28

[ 42](r8a779f0__cpg__mssr_8h.md#a74c05a5827865667bc4dae85839efc33)#define R8A779F0\_CLK\_CL16M\_MM 29

[ 43](r8a779f0__cpg__mssr_8h.md#a126cf32aba9f6ecb15210f288dbe382c)#define R8A779F0\_CLK\_CL16M\_RT 30

[ 44](r8a779f0__cpg__mssr_8h.md#a71f0683c5e9cab07b1bd52a4f3b1d90d)#define R8A779F0\_CLK\_CL16M\_PER 31

[ 45](r8a779f0__cpg__mssr_8h.md#abdb43c2674e30793691bac70af5cc22b)#define R8A779F0\_CLK\_CL16M\_HSC 32

[ 46](r8a779f0__cpg__mssr_8h.md#a2678c4a0b919a5584ee6e5b2ca561a24)#define R8A779F0\_CLK\_ZB3 33

[ 47](r8a779f0__cpg__mssr_8h.md#ae92fea018b78b5ccde9936fca7f2be74)#define R8A779F0\_CLK\_ZB3D2 34

[ 48](r8a779f0__cpg__mssr_8h.md#a848b8c6e2f21d7617ae8f53d76548077)#define R8A779F0\_CLK\_ZB3D4 35

[ 49](r8a779f0__cpg__mssr_8h.md#a1224270f68927302109975188c09fc80)#define R8A779F0\_CLK\_SD0H 36

[ 50](r8a779f0__cpg__mssr_8h.md#abc5ac7c0467c3d4cce4a9f1cc2130922)#define R8A779F0\_CLK\_SD0 37

[ 51](r8a779f0__cpg__mssr_8h.md#a994e15a0f845e480162608ceef6c7c4a)#define R8A779F0\_CLK\_RPC 38

[ 52](r8a779f0__cpg__mssr_8h.md#a79d19a050c94084baccb63324c2968a5)#define R8A779F0\_CLK\_RPCD2 39

[ 53](r8a779f0__cpg__mssr_8h.md#ae199f3bcb27e98b3cb41d9365f0cf5a5)#define R8A779F0\_CLK\_MSO 40

[ 54](r8a779f0__cpg__mssr_8h.md#a9d945df47947f90c1d3b4c6cb6f827d3)#define R8A779F0\_CLK\_POST 41

[ 55](r8a779f0__cpg__mssr_8h.md#a51e471d2ec589a9b499acfa2443b38b3)#define R8A779F0\_CLK\_POST2 42

[ 56](r8a779f0__cpg__mssr_8h.md#a205d268407b85388542261ec52fc6ced)#define R8A779F0\_CLK\_SASYNCRT 43

[ 57](r8a779f0__cpg__mssr_8h.md#aab42b07c83c8b163a27a0d03de7c1077)#define R8A779F0\_CLK\_SASYNCPERD1 44

[ 58](r8a779f0__cpg__mssr_8h.md#a45999f98f5b887266bfc8670d91c1346)#define R8A779F0\_CLK\_SASYNCPERD2 45

[ 59](r8a779f0__cpg__mssr_8h.md#a6f42e696bab079310ab39948d0c58ab8)#define R8A779F0\_CLK\_SASYNCPERD4 46

[ 60](r8a779f0__cpg__mssr_8h.md#a932b88945a23e7ca26ebfa397e289960)#define R8A779F0\_CLK\_DBGSOC\_HSC 47

[ 61](r8a779f0__cpg__mssr_8h.md#a632555abe41db51216098e511350e178)#define R8A779F0\_CLK\_RSW2 48

[ 62](r8a779f0__cpg__mssr_8h.md#a5f3b3ec6381c31c4d77bc49f9fae1654)#define R8A779F0\_CLK\_CPEX 49

[ 63](r8a779f0__cpg__mssr_8h.md#a93f9b6bd9030e6163a61cfa5010ae6c5)#define R8A779F0\_CLK\_CBFUSA 50

[ 64](r8a779f0__cpg__mssr_8h.md#a372aaef7a94c5d85f356f41340a6aab9)#define R8A779F0\_CLK\_R 51

[ 65](r8a779f0__cpg__mssr_8h.md#a98f1cace1a698c62aac1ab60d0f7e931)#define R8A779F0\_CLK\_OSC 52

66

67#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_CLOCK\_RENESAS\_CLOCK\_R8A779F0\_H\_ \*/

[renesas\_cpg\_mssr.h](dt-bindings_2clock_2renesas__cpg__mssr_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [r8a779f0\_cpg\_mssr.h](r8a779f0__cpg__mssr_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
