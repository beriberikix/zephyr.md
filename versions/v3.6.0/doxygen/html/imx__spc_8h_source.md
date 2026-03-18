---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/imx__spc_8h_source.html
original_path: doxygen/html/imx__spc_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

imx\_spc.h

[Go to the documentation of this file.](imx__spc_8h.md)

1/\*

2 \* Copyright (c) 2021, NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7

8/\*

9 \* Setpoint definitions for IMX Set point controller. The SPC uses a series

10 \* of set points to determine the clock speeds and states of cores, as well

11 \* as which peripherals to gate clocks to. Higher values correspond to more

12 \* power saving. See your SOC's datasheet for specifics of what peripherals

13 \* have their clocks gated at each set point.

14 \*

15 \* Set point control is implemented at the soc level (see pm\_state\_set())

16 \*/

17

18#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PM\_IMX\_SPC\_H\_

19#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PM\_IMX\_SPC\_H\_

20

[ 21](imx__spc_8h.md#a0346f0daeb276b819f045132114c74da)#define IMX\_GPC\_RUN 0x0

[ 22](imx__spc_8h.md#a1f32dc4faba3158ab48cee77563a5a92)#define IMX\_GPC\_WAIT 0x1

[ 23](imx__spc_8h.md#a0bd3da16de75240efaa9dbacc7abc1a9)#define IMX\_GPC\_STOP 0x2

[ 24](imx__spc_8h.md#a75a363ea77fdfa2a8f922869baf9cae5)#define IMX\_GPC\_SUSPEND 0x3

25

26

[ 27](imx__spc_8h.md#ac16b45dfd6df94cad425dd8bf2eb0119)#define IMX\_SPC\_MASK 0xF0

[ 28](imx__spc_8h.md#a626b183ac785be3b2cc9d2e8cbb841f4)#define IMX\_SPC\_SHIFT 4

[ 29](imx__spc_8h.md#a8468498e09c899056ea9f77e686c867a)#define IMX\_GPC\_MODE\_MASK 0xF

30

[ 31](imx__spc_8h.md#ada6ec38357d6bf3ce7f4102744e79bbc)#define IMX\_SPC(x) ((x & IMX\_SPC\_MASK) >> IMX\_SPC\_SHIFT)

[ 32](imx__spc_8h.md#ae9feac62ff35ec0fef30e75ae0a88bee)#define IMX\_GPC\_MODE(x) (x & IMX\_GPC\_MODE\_MASK)

33

[ 34](imx__spc_8h.md#a2b91ceadf0b08f329ca48e459be4b8cf)#define IMX\_SPC\_0 0x00

[ 35](imx__spc_8h.md#ac01b3b94d1a06a7870a48b3366edee55)#define IMX\_SPC\_1 0x10

[ 36](imx__spc_8h.md#a214286102c951b04eb1a18aed412cd98)#define IMX\_SPC\_2 0x20

[ 37](imx__spc_8h.md#af88f9b163c2a831198506bfc42455a54)#define IMX\_SPC\_3 0x30

[ 38](imx__spc_8h.md#ac36951bfc1258656226275d6eb9bd7da)#define IMX\_SPC\_4 0x40

[ 39](imx__spc_8h.md#a0ca2082bf7718bba8a4cbd3cae1e8491)#define IMX\_SPC\_5 0x50

[ 40](imx__spc_8h.md#a97af1d082a356f5ac275fc84c0ca21c7)#define IMX\_SPC\_6 0x60

[ 41](imx__spc_8h.md#ac73c19b933caae5626297572ee3ff022)#define IMX\_SPC\_7 0x70

[ 42](imx__spc_8h.md#a1d8798b3f2081e9ff647b92e8515cd14)#define IMX\_SPC\_8 0x80

[ 43](imx__spc_8h.md#a8cde5e61745d8e2b5641f50ab2ceed14)#define IMX\_SPC\_9 0x90

[ 44](imx__spc_8h.md#a7b8f4911506984f1ac3fb2b91983a351)#define IMX\_SPC\_10 0xA0

[ 45](imx__spc_8h.md#ac518e5c9a79447934ee3d0f35b3c334b)#define IMX\_SPC\_11 0xB0

[ 46](imx__spc_8h.md#ab6ceb05e36ef4c24d3a776ddadf2a17b)#define IMX\_SPC\_12 0xC0

[ 47](imx__spc_8h.md#a5bc88e7c7ec8e9bcda35ad60f671bef5)#define IMX\_SPC\_13 0xD0

[ 48](imx__spc_8h.md#a11b0cee3cc0d34591c11e1da6aa3e586)#define IMX\_SPC\_14 0xE0

[ 49](imx__spc_8h.md#a89c2348f26960a938b7126a631ff4440)#define IMX\_SPC\_15 0xF0

50

51

[ 52](imx__spc_8h.md#a2513b235eb5c1d2eef874cde812d66e2)#define IMX\_SPC\_SET\_POINT\_0\_RUN (IMX\_SPC\_0 | IMX\_GPC\_RUN)

[ 53](imx__spc_8h.md#a655eb9644e0f6edf17055c43beb8bc78)#define IMX\_SPC\_SET\_POINT\_0\_WAIT (IMX\_SPC\_0 | IMX\_GPC\_WAIT)

[ 54](imx__spc_8h.md#ac0bcab370462ec48cc65c2ad72673e25)#define IMX\_SPC\_SET\_POINT\_0\_STOP (IMX\_SPC\_0 | IMX\_GPC\_STOP)

[ 55](imx__spc_8h.md#ad9a6bdc024c700869ba4b2a226449498)#define IMX\_SPC\_SET\_POINT\_0\_SUSPEND (IMX\_SPC\_0 | IMX\_GPC\_SUSPEND)

[ 56](imx__spc_8h.md#a675487df773ccd4a478c0ed74ffc1b8d)#define IMX\_SPC\_SET\_POINT\_1\_RUN (IMX\_SPC\_1 | IMX\_GPC\_RUN)

[ 57](imx__spc_8h.md#ad70a5fc9fa6991d212e251223f69845c)#define IMX\_SPC\_SET\_POINT\_1\_WAIT (IMX\_SPC\_1 | IMX\_GPC\_WAIT)

[ 58](imx__spc_8h.md#abc74b52dbaec59ed1a437a6012737dcb)#define IMX\_SPC\_SET\_POINT\_1\_STOP (IMX\_SPC\_1 | IMX\_GPC\_STOP)

[ 59](imx__spc_8h.md#a27bb5318452f3bdd359ea77a937ffe51)#define IMX\_SPC\_SET\_POINT\_1\_SUSPEND (IMX\_SPC\_1 | IMX\_GPC\_SUSPEND)

[ 60](imx__spc_8h.md#a212b8780e33e35edc68463cbbb656f47)#define IMX\_SPC\_SET\_POINT\_2\_RUN (IMX\_SPC\_2 | IMX\_GPC\_RUN)

[ 61](imx__spc_8h.md#a3e890fdf63a58fd42a0139812550d370)#define IMX\_SPC\_SET\_POINT\_2\_WAIT (IMX\_SPC\_2 | IMX\_GPC\_WAIT)

[ 62](imx__spc_8h.md#aea99f181628c69b96ea093698b4c91fd)#define IMX\_SPC\_SET\_POINT\_2\_STOP (IMX\_SPC\_2 | IMX\_GPC\_STOP)

[ 63](imx__spc_8h.md#a0db51a91cb50008bbdc8baf9621ae55c)#define IMX\_SPC\_SET\_POINT\_2\_SUSPEND (IMX\_SPC\_2 | IMX\_GPC\_SUSPEND)

[ 64](imx__spc_8h.md#a955a3993640e5f07be6dbdbac6b2887b)#define IMX\_SPC\_SET\_POINT\_3\_RUN (IMX\_SPC\_3 | IMX\_GPC\_RUN)

[ 65](imx__spc_8h.md#a77917334bf2072b01ee996b8b3cdbd0a)#define IMX\_SPC\_SET\_POINT\_3\_WAIT (IMX\_SPC\_3 | IMX\_GPC\_WAIT)

[ 66](imx__spc_8h.md#a0fa20de0d1a6d4b59fb236467ed6eed8)#define IMX\_SPC\_SET\_POINT\_3\_STOP (IMX\_SPC\_3 | IMX\_GPC\_STOP)

[ 67](imx__spc_8h.md#a320b1171760941ca6220ae445027b2bb)#define IMX\_SPC\_SET\_POINT\_3\_SUSPEND (IMX\_SPC\_3 | IMX\_GPC\_SUSPEND)

[ 68](imx__spc_8h.md#a3a875a06de64389b17942fe7096e533b)#define IMX\_SPC\_SET\_POINT\_4\_RUN (IMX\_SPC\_4 | IMX\_GPC\_RUN)

[ 69](imx__spc_8h.md#a53d8e05a6545202e55c12b9e19723141)#define IMX\_SPC\_SET\_POINT\_4\_WAIT (IMX\_SPC\_4 | IMX\_GPC\_WAIT)

[ 70](imx__spc_8h.md#a6f2e970fea0a5b9713a98e6cb5b31060)#define IMX\_SPC\_SET\_POINT\_4\_STOP (IMX\_SPC\_4 | IMX\_GPC\_STOP)

[ 71](imx__spc_8h.md#a8b2c95d1accb75acb84d074c6f9554b4)#define IMX\_SPC\_SET\_POINT\_4\_SUSPEND (IMX\_SPC\_4 | IMX\_GPC\_SUSPEND)

[ 72](imx__spc_8h.md#a08e368e7fbccdf9910ef41f8054e6ac7)#define IMX\_SPC\_SET\_POINT\_5\_RUN (IMX\_SPC\_5 | IMX\_GPC\_RUN)

[ 73](imx__spc_8h.md#ab8b90420137da04a8ce432c1b0385613)#define IMX\_SPC\_SET\_POINT\_5\_WAIT (IMX\_SPC\_5 | IMX\_GPC\_WAIT)

[ 74](imx__spc_8h.md#a2111e4b8468791f5062bc1fafba1e871)#define IMX\_SPC\_SET\_POINT\_5\_STOP (IMX\_SPC\_5 | IMX\_GPC\_STOP)

[ 75](imx__spc_8h.md#a14047d119208c1c188d28e3fef2286cf)#define IMX\_SPC\_SET\_POINT\_5\_SUSPEND (IMX\_SPC\_5 | IMX\_GPC\_SUSPEND)

[ 76](imx__spc_8h.md#ae667a3617c9389bef9d08f3d4a639731)#define IMX\_SPC\_SET\_POINT\_6\_RUN (IMX\_SPC\_6 | IMX\_GPC\_RUN)

[ 77](imx__spc_8h.md#aaf448cdd4b85f7c7417e5de766361035)#define IMX\_SPC\_SET\_POINT\_6\_WAIT (IMX\_SPC\_6 | IMX\_GPC\_WAIT)

[ 78](imx__spc_8h.md#ab8f1fe76f07af84111d2532d4205a01c)#define IMX\_SPC\_SET\_POINT\_6\_STOP (IMX\_SPC\_6 | IMX\_GPC\_STOP)

[ 79](imx__spc_8h.md#ae977b643f59534d5df555e6aa283a82d)#define IMX\_SPC\_SET\_POINT\_6\_SUSPEND (IMX\_SPC\_6 | IMX\_GPC\_SUSPEND)

[ 80](imx__spc_8h.md#a4edbee6f04031c2c8f2b835d0e100bf3)#define IMX\_SPC\_SET\_POINT\_7\_RUN (IMX\_SPC\_7 | IMX\_GPC\_RUN)

[ 81](imx__spc_8h.md#a78e453e0425752c8bb636cd45e9f66a5)#define IMX\_SPC\_SET\_POINT\_7\_WAIT (IMX\_SPC\_7 | IMX\_GPC\_WAIT)

[ 82](imx__spc_8h.md#a996d39beaa9490adf49c602f325ebe04)#define IMX\_SPC\_SET\_POINT\_7\_STOP (IMX\_SPC\_7 | IMX\_GPC\_STOP)

[ 83](imx__spc_8h.md#a9b90dd5fd6f801e27a95e02f6e7614d7)#define IMX\_SPC\_SET\_POINT\_7\_SUSPEND (IMX\_SPC\_7 | IMX\_GPC\_SUSPEND)

[ 84](imx__spc_8h.md#acbfdb5f70d7f4aee7435f5ca6d014596)#define IMX\_SPC\_SET\_POINT\_8\_RUN (IMX\_SPC\_8 | IMX\_GPC\_RUN)

[ 85](imx__spc_8h.md#a402e534a33588b1f3b31d0a7284d32ab)#define IMX\_SPC\_SET\_POINT\_8\_WAIT (IMX\_SPC\_8 | IMX\_GPC\_WAIT)

[ 86](imx__spc_8h.md#a4f2f29f9e4bb420436d881b8233a43b5)#define IMX\_SPC\_SET\_POINT\_8\_STOP (IMX\_SPC\_8 | IMX\_GPC\_STOP)

[ 87](imx__spc_8h.md#a686e1a2d26bc3df4d465614da82bae08)#define IMX\_SPC\_SET\_POINT\_8\_SUSPEND (IMX\_SPC\_8 | IMX\_GPC\_SUSPEND)

[ 88](imx__spc_8h.md#ab591869ecb6606cdf1e73cc3849f611d)#define IMX\_SPC\_SET\_POINT\_9\_RUN (IMX\_SPC\_9 | IMX\_GPC\_RUN)

[ 89](imx__spc_8h.md#ad234e9dd6516742f9d8869fda039a5c1)#define IMX\_SPC\_SET\_POINT\_9\_WAIT (IMX\_SPC\_9 | IMX\_GPC\_WAIT)

[ 90](imx__spc_8h.md#a9696110f23d443b540cbfa8aedd25e9b)#define IMX\_SPC\_SET\_POINT\_9\_STOP (IMX\_SPC\_9 | IMX\_GPC\_STOP)

[ 91](imx__spc_8h.md#a8e6427bd9509ffb3b51f18b62753340c)#define IMX\_SPC\_SET\_POINT\_9\_SUSPEND (IMX\_SPC\_9 | IMX\_GPC\_SUSPEND)

[ 92](imx__spc_8h.md#a7be6d85aa76e65805716c2bf20553fae)#define IMX\_SPC\_SET\_POINT\_10\_RUN (IMX\_SPC\_10 | IMX\_GPC\_RUN)

[ 93](imx__spc_8h.md#a57e3cbbf5409c9b634a67d381f81b36c)#define IMX\_SPC\_SET\_POINT\_10\_WAIT (IMX\_SPC\_10 | IMX\_GPC\_WAIT)

[ 94](imx__spc_8h.md#a61e070d9c04cea7c4e0f7fb3ff703718)#define IMX\_SPC\_SET\_POINT\_10\_STOP (IMX\_SPC\_10 | IMX\_GPC\_STOP)

[ 95](imx__spc_8h.md#a2d6aecb9ac2033ca89ca673c6786fe61)#define IMX\_SPC\_SET\_POINT\_10\_SUSPEND (IMX\_SPC\_10 | IMX\_GPC\_SUSPEND)

[ 96](imx__spc_8h.md#ade582b07da3be853835863e2c4efd1fe)#define IMX\_SPC\_SET\_POINT\_11\_RUN (IMX\_SPC\_11 | IMX\_GPC\_RUN)

[ 97](imx__spc_8h.md#ad81fd8b58c73dd88f869fbe99e45af62)#define IMX\_SPC\_SET\_POINT\_11\_WAIT (IMX\_SPC\_11 | IMX\_GPC\_WAIT)

[ 98](imx__spc_8h.md#af328d05fc2f3084025426bcfa8e07acb)#define IMX\_SPC\_SET\_POINT\_11\_STOP (IMX\_SPC\_11 | IMX\_GPC\_STOP)

[ 99](imx__spc_8h.md#aa84a574b06d37679035c9e160794103b)#define IMX\_SPC\_SET\_POINT\_11\_SUSPEND (IMX\_SPC\_11 | IMX\_GPC\_SUSPEND)

[ 100](imx__spc_8h.md#aa4b08d6e86e2a0786aa4b8467063e744)#define IMX\_SPC\_SET\_POINT\_12\_RUN (IMX\_SPC\_12 | IMX\_GPC\_RUN)

[ 101](imx__spc_8h.md#a06f577fcd7a7039930f5cd60f10dbdbb)#define IMX\_SPC\_SET\_POINT\_12\_WAIT (IMX\_SPC\_12 | IMX\_GPC\_WAIT)

[ 102](imx__spc_8h.md#a82f472da9010bb1de1a74837d1b2eae7)#define IMX\_SPC\_SET\_POINT\_12\_STOP (IMX\_SPC\_12 | IMX\_GPC\_STOP)

[ 103](imx__spc_8h.md#a393fdb54cd063085108b8d600653e3a3)#define IMX\_SPC\_SET\_POINT\_12\_SUSPEND (IMX\_SPC\_12 | IMX\_GPC\_SUSPEND)

[ 104](imx__spc_8h.md#aa62f55fa30c7fe258eb5bce336914b74)#define IMX\_SPC\_SET\_POINT\_13\_RUN (IMX\_SPC\_13 | IMX\_GPC\_RUN)

[ 105](imx__spc_8h.md#a9603a1be5b8faf232c06f39526052992)#define IMX\_SPC\_SET\_POINT\_13\_WAIT (IMX\_SPC\_13 | IMX\_GPC\_WAIT)

[ 106](imx__spc_8h.md#a1c1e481a627910fee5786560815a7442)#define IMX\_SPC\_SET\_POINT\_13\_STOP (IMX\_SPC\_13 | IMX\_GPC\_STOP)

[ 107](imx__spc_8h.md#a2e56fe135af350c5ebd92196cdca8067)#define IMX\_SPC\_SET\_POINT\_13\_SUSPEND (IMX\_SPC\_13 | IMX\_GPC\_SUSPEND)

[ 108](imx__spc_8h.md#a23f38fd1002d77d327a84ad8ca5e3d22)#define IMX\_SPC\_SET\_POINT\_14\_RUN (IMX\_SPC\_14 | IMX\_GPC\_RUN)

[ 109](imx__spc_8h.md#abbda3ffc097e0cbba6f4a529215899f0)#define IMX\_SPC\_SET\_POINT\_14\_WAIT (IMX\_SPC\_14 | IMX\_GPC\_WAIT)

[ 110](imx__spc_8h.md#addc192b8864a96a935e983021fd6991b)#define IMX\_SPC\_SET\_POINT\_14\_STOP (IMX\_SPC\_14 | IMX\_GPC\_STOP)

[ 111](imx__spc_8h.md#adabea62f128c40438f1edb29d597accd)#define IMX\_SPC\_SET\_POINT\_14\_SUSPEND (IMX\_SPC\_14 | IMX\_GPC\_SUSPEND)

[ 112](imx__spc_8h.md#a0efa4fa53bce64f0c89f9d4eb07ba27d)#define IMX\_SPC\_SET\_POINT\_15\_RUN (IMX\_SPC\_15 | IMX\_GPC\_RUN)

[ 113](imx__spc_8h.md#af691cffe687076e6ac2f03db06f9b48f)#define IMX\_SPC\_SET\_POINT\_15\_WAIT (IMX\_SPC\_15 | IMX\_GPC\_WAIT)

[ 114](imx__spc_8h.md#a6a24e7b3e0e9e3a1ba0dd2984bd9fde6)#define IMX\_SPC\_SET\_POINT\_15\_STOP (IMX\_SPC\_15 | IMX\_GPC\_STOP)

[ 115](imx__spc_8h.md#a1eade5203e39d0892c2f9eba8fd023f9)#define IMX\_SPC\_SET\_POINT\_15\_SUSPEND (IMX\_SPC\_15 | IMX\_GPC\_SUSPEND)

116

117

118#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PM\_IMX\_SPC\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pm](dir_108d2a5c081446f0496ddf8d635df811.md)
- [imx\_spc.h](imx__spc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
