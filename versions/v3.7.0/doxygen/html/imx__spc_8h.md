---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/imx__spc_8h.html
original_path: doxygen/html/imx__spc_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

imx\_spc.h File Reference

[Go to the source code of this file.](imx__spc_8h_source.md)

| Macros | |
| --- | --- |
| #define | [IMX\_GPC\_RUN](#a0346f0daeb276b819f045132114c74da)   0x0 |
| #define | [IMX\_GPC\_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)   0x1 |
| #define | [IMX\_GPC\_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)   0x2 |
| #define | [IMX\_GPC\_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)   0x3 |
| #define | [IMX\_SPC\_MASK](#ac16b45dfd6df94cad425dd8bf2eb0119)   0xF0 |
| #define | [IMX\_SPC\_SHIFT](#a626b183ac785be3b2cc9d2e8cbb841f4)   4 |
| #define | [IMX\_GPC\_MODE\_MASK](#a8468498e09c899056ea9f77e686c867a)   0xF |
| #define | [IMX\_SPC](#ada6ec38357d6bf3ce7f4102744e79bbc)(x) |
| #define | [IMX\_GPC\_MODE](#ae9feac62ff35ec0fef30e75ae0a88bee)(x) |
| #define | [IMX\_SPC\_0](#a2b91ceadf0b08f329ca48e459be4b8cf)   0x00 |
| #define | [IMX\_SPC\_1](#ac01b3b94d1a06a7870a48b3366edee55)   0x10 |
| #define | [IMX\_SPC\_2](#a214286102c951b04eb1a18aed412cd98)   0x20 |
| #define | [IMX\_SPC\_3](#af88f9b163c2a831198506bfc42455a54)   0x30 |
| #define | [IMX\_SPC\_4](#ac36951bfc1258656226275d6eb9bd7da)   0x40 |
| #define | [IMX\_SPC\_5](#a0ca2082bf7718bba8a4cbd3cae1e8491)   0x50 |
| #define | [IMX\_SPC\_6](#a97af1d082a356f5ac275fc84c0ca21c7)   0x60 |
| #define | [IMX\_SPC\_7](#ac73c19b933caae5626297572ee3ff022)   0x70 |
| #define | [IMX\_SPC\_8](#a1d8798b3f2081e9ff647b92e8515cd14)   0x80 |
| #define | [IMX\_SPC\_9](#a8cde5e61745d8e2b5641f50ab2ceed14)   0x90 |
| #define | [IMX\_SPC\_10](#a7b8f4911506984f1ac3fb2b91983a351)   0xA0 |
| #define | [IMX\_SPC\_11](#ac518e5c9a79447934ee3d0f35b3c334b)   0xB0 |
| #define | [IMX\_SPC\_12](#ab6ceb05e36ef4c24d3a776ddadf2a17b)   0xC0 |
| #define | [IMX\_SPC\_13](#a5bc88e7c7ec8e9bcda35ad60f671bef5)   0xD0 |
| #define | [IMX\_SPC\_14](#a11b0cee3cc0d34591c11e1da6aa3e586)   0xE0 |
| #define | [IMX\_SPC\_15](#a89c2348f26960a938b7126a631ff4440)   0xF0 |
| #define | [IMX\_SPC\_SET\_POINT\_0\_RUN](#a2513b235eb5c1d2eef874cde812d66e2)   ([IMX\_SPC\_0](#a2b91ceadf0b08f329ca48e459be4b8cf) | [IMX\_GPC\_RUN](#a0346f0daeb276b819f045132114c74da)) |
| #define | [IMX\_SPC\_SET\_POINT\_0\_WAIT](#a655eb9644e0f6edf17055c43beb8bc78)   ([IMX\_SPC\_0](#a2b91ceadf0b08f329ca48e459be4b8cf) | [IMX\_GPC\_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)) |
| #define | [IMX\_SPC\_SET\_POINT\_0\_STOP](#ac0bcab370462ec48cc65c2ad72673e25)   ([IMX\_SPC\_0](#a2b91ceadf0b08f329ca48e459be4b8cf) | [IMX\_GPC\_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)) |
| #define | [IMX\_SPC\_SET\_POINT\_0\_SUSPEND](#ad9a6bdc024c700869ba4b2a226449498)   ([IMX\_SPC\_0](#a2b91ceadf0b08f329ca48e459be4b8cf) | [IMX\_GPC\_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)) |
| #define | [IMX\_SPC\_SET\_POINT\_1\_RUN](#a675487df773ccd4a478c0ed74ffc1b8d)   ([IMX\_SPC\_1](#ac01b3b94d1a06a7870a48b3366edee55) | [IMX\_GPC\_RUN](#a0346f0daeb276b819f045132114c74da)) |
| #define | [IMX\_SPC\_SET\_POINT\_1\_WAIT](#ad70a5fc9fa6991d212e251223f69845c)   ([IMX\_SPC\_1](#ac01b3b94d1a06a7870a48b3366edee55) | [IMX\_GPC\_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)) |
| #define | [IMX\_SPC\_SET\_POINT\_1\_STOP](#abc74b52dbaec59ed1a437a6012737dcb)   ([IMX\_SPC\_1](#ac01b3b94d1a06a7870a48b3366edee55) | [IMX\_GPC\_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)) |
| #define | [IMX\_SPC\_SET\_POINT\_1\_SUSPEND](#a27bb5318452f3bdd359ea77a937ffe51)   ([IMX\_SPC\_1](#ac01b3b94d1a06a7870a48b3366edee55) | [IMX\_GPC\_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)) |
| #define | [IMX\_SPC\_SET\_POINT\_2\_RUN](#a212b8780e33e35edc68463cbbb656f47)   ([IMX\_SPC\_2](#a214286102c951b04eb1a18aed412cd98) | [IMX\_GPC\_RUN](#a0346f0daeb276b819f045132114c74da)) |
| #define | [IMX\_SPC\_SET\_POINT\_2\_WAIT](#a3e890fdf63a58fd42a0139812550d370)   ([IMX\_SPC\_2](#a214286102c951b04eb1a18aed412cd98) | [IMX\_GPC\_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)) |
| #define | [IMX\_SPC\_SET\_POINT\_2\_STOP](#aea99f181628c69b96ea093698b4c91fd)   ([IMX\_SPC\_2](#a214286102c951b04eb1a18aed412cd98) | [IMX\_GPC\_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)) |
| #define | [IMX\_SPC\_SET\_POINT\_2\_SUSPEND](#a0db51a91cb50008bbdc8baf9621ae55c)   ([IMX\_SPC\_2](#a214286102c951b04eb1a18aed412cd98) | [IMX\_GPC\_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)) |
| #define | [IMX\_SPC\_SET\_POINT\_3\_RUN](#a955a3993640e5f07be6dbdbac6b2887b)   ([IMX\_SPC\_3](#af88f9b163c2a831198506bfc42455a54) | [IMX\_GPC\_RUN](#a0346f0daeb276b819f045132114c74da)) |
| #define | [IMX\_SPC\_SET\_POINT\_3\_WAIT](#a77917334bf2072b01ee996b8b3cdbd0a)   ([IMX\_SPC\_3](#af88f9b163c2a831198506bfc42455a54) | [IMX\_GPC\_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)) |
| #define | [IMX\_SPC\_SET\_POINT\_3\_STOP](#a0fa20de0d1a6d4b59fb236467ed6eed8)   ([IMX\_SPC\_3](#af88f9b163c2a831198506bfc42455a54) | [IMX\_GPC\_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)) |
| #define | [IMX\_SPC\_SET\_POINT\_3\_SUSPEND](#a320b1171760941ca6220ae445027b2bb)   ([IMX\_SPC\_3](#af88f9b163c2a831198506bfc42455a54) | [IMX\_GPC\_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)) |
| #define | [IMX\_SPC\_SET\_POINT\_4\_RUN](#a3a875a06de64389b17942fe7096e533b)   ([IMX\_SPC\_4](#ac36951bfc1258656226275d6eb9bd7da) | [IMX\_GPC\_RUN](#a0346f0daeb276b819f045132114c74da)) |
| #define | [IMX\_SPC\_SET\_POINT\_4\_WAIT](#a53d8e05a6545202e55c12b9e19723141)   ([IMX\_SPC\_4](#ac36951bfc1258656226275d6eb9bd7da) | [IMX\_GPC\_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)) |
| #define | [IMX\_SPC\_SET\_POINT\_4\_STOP](#a6f2e970fea0a5b9713a98e6cb5b31060)   ([IMX\_SPC\_4](#ac36951bfc1258656226275d6eb9bd7da) | [IMX\_GPC\_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)) |
| #define | [IMX\_SPC\_SET\_POINT\_4\_SUSPEND](#a8b2c95d1accb75acb84d074c6f9554b4)   ([IMX\_SPC\_4](#ac36951bfc1258656226275d6eb9bd7da) | [IMX\_GPC\_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)) |
| #define | [IMX\_SPC\_SET\_POINT\_5\_RUN](#a08e368e7fbccdf9910ef41f8054e6ac7)   ([IMX\_SPC\_5](#a0ca2082bf7718bba8a4cbd3cae1e8491) | [IMX\_GPC\_RUN](#a0346f0daeb276b819f045132114c74da)) |
| #define | [IMX\_SPC\_SET\_POINT\_5\_WAIT](#ab8b90420137da04a8ce432c1b0385613)   ([IMX\_SPC\_5](#a0ca2082bf7718bba8a4cbd3cae1e8491) | [IMX\_GPC\_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)) |
| #define | [IMX\_SPC\_SET\_POINT\_5\_STOP](#a2111e4b8468791f5062bc1fafba1e871)   ([IMX\_SPC\_5](#a0ca2082bf7718bba8a4cbd3cae1e8491) | [IMX\_GPC\_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)) |
| #define | [IMX\_SPC\_SET\_POINT\_5\_SUSPEND](#a14047d119208c1c188d28e3fef2286cf)   ([IMX\_SPC\_5](#a0ca2082bf7718bba8a4cbd3cae1e8491) | [IMX\_GPC\_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)) |
| #define | [IMX\_SPC\_SET\_POINT\_6\_RUN](#ae667a3617c9389bef9d08f3d4a639731)   ([IMX\_SPC\_6](#a97af1d082a356f5ac275fc84c0ca21c7) | [IMX\_GPC\_RUN](#a0346f0daeb276b819f045132114c74da)) |
| #define | [IMX\_SPC\_SET\_POINT\_6\_WAIT](#aaf448cdd4b85f7c7417e5de766361035)   ([IMX\_SPC\_6](#a97af1d082a356f5ac275fc84c0ca21c7) | [IMX\_GPC\_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)) |
| #define | [IMX\_SPC\_SET\_POINT\_6\_STOP](#ab8f1fe76f07af84111d2532d4205a01c)   ([IMX\_SPC\_6](#a97af1d082a356f5ac275fc84c0ca21c7) | [IMX\_GPC\_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)) |
| #define | [IMX\_SPC\_SET\_POINT\_6\_SUSPEND](#ae977b643f59534d5df555e6aa283a82d)   ([IMX\_SPC\_6](#a97af1d082a356f5ac275fc84c0ca21c7) | [IMX\_GPC\_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)) |
| #define | [IMX\_SPC\_SET\_POINT\_7\_RUN](#a4edbee6f04031c2c8f2b835d0e100bf3)   ([IMX\_SPC\_7](#ac73c19b933caae5626297572ee3ff022) | [IMX\_GPC\_RUN](#a0346f0daeb276b819f045132114c74da)) |
| #define | [IMX\_SPC\_SET\_POINT\_7\_WAIT](#a78e453e0425752c8bb636cd45e9f66a5)   ([IMX\_SPC\_7](#ac73c19b933caae5626297572ee3ff022) | [IMX\_GPC\_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)) |
| #define | [IMX\_SPC\_SET\_POINT\_7\_STOP](#a996d39beaa9490adf49c602f325ebe04)   ([IMX\_SPC\_7](#ac73c19b933caae5626297572ee3ff022) | [IMX\_GPC\_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)) |
| #define | [IMX\_SPC\_SET\_POINT\_7\_SUSPEND](#a9b90dd5fd6f801e27a95e02f6e7614d7)   ([IMX\_SPC\_7](#ac73c19b933caae5626297572ee3ff022) | [IMX\_GPC\_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)) |
| #define | [IMX\_SPC\_SET\_POINT\_8\_RUN](#acbfdb5f70d7f4aee7435f5ca6d014596)   ([IMX\_SPC\_8](#a1d8798b3f2081e9ff647b92e8515cd14) | [IMX\_GPC\_RUN](#a0346f0daeb276b819f045132114c74da)) |
| #define | [IMX\_SPC\_SET\_POINT\_8\_WAIT](#a402e534a33588b1f3b31d0a7284d32ab)   ([IMX\_SPC\_8](#a1d8798b3f2081e9ff647b92e8515cd14) | [IMX\_GPC\_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)) |
| #define | [IMX\_SPC\_SET\_POINT\_8\_STOP](#a4f2f29f9e4bb420436d881b8233a43b5)   ([IMX\_SPC\_8](#a1d8798b3f2081e9ff647b92e8515cd14) | [IMX\_GPC\_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)) |
| #define | [IMX\_SPC\_SET\_POINT\_8\_SUSPEND](#a686e1a2d26bc3df4d465614da82bae08)   ([IMX\_SPC\_8](#a1d8798b3f2081e9ff647b92e8515cd14) | [IMX\_GPC\_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)) |
| #define | [IMX\_SPC\_SET\_POINT\_9\_RUN](#ab591869ecb6606cdf1e73cc3849f611d)   ([IMX\_SPC\_9](#a8cde5e61745d8e2b5641f50ab2ceed14) | [IMX\_GPC\_RUN](#a0346f0daeb276b819f045132114c74da)) |
| #define | [IMX\_SPC\_SET\_POINT\_9\_WAIT](#ad234e9dd6516742f9d8869fda039a5c1)   ([IMX\_SPC\_9](#a8cde5e61745d8e2b5641f50ab2ceed14) | [IMX\_GPC\_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)) |
| #define | [IMX\_SPC\_SET\_POINT\_9\_STOP](#a9696110f23d443b540cbfa8aedd25e9b)   ([IMX\_SPC\_9](#a8cde5e61745d8e2b5641f50ab2ceed14) | [IMX\_GPC\_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)) |
| #define | [IMX\_SPC\_SET\_POINT\_9\_SUSPEND](#a8e6427bd9509ffb3b51f18b62753340c)   ([IMX\_SPC\_9](#a8cde5e61745d8e2b5641f50ab2ceed14) | [IMX\_GPC\_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)) |
| #define | [IMX\_SPC\_SET\_POINT\_10\_RUN](#a7be6d85aa76e65805716c2bf20553fae)   ([IMX\_SPC\_10](#a7b8f4911506984f1ac3fb2b91983a351) | [IMX\_GPC\_RUN](#a0346f0daeb276b819f045132114c74da)) |
| #define | [IMX\_SPC\_SET\_POINT\_10\_WAIT](#a57e3cbbf5409c9b634a67d381f81b36c)   ([IMX\_SPC\_10](#a7b8f4911506984f1ac3fb2b91983a351) | [IMX\_GPC\_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)) |
| #define | [IMX\_SPC\_SET\_POINT\_10\_STOP](#a61e070d9c04cea7c4e0f7fb3ff703718)   ([IMX\_SPC\_10](#a7b8f4911506984f1ac3fb2b91983a351) | [IMX\_GPC\_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)) |
| #define | [IMX\_SPC\_SET\_POINT\_10\_SUSPEND](#a2d6aecb9ac2033ca89ca673c6786fe61)   ([IMX\_SPC\_10](#a7b8f4911506984f1ac3fb2b91983a351) | [IMX\_GPC\_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)) |
| #define | [IMX\_SPC\_SET\_POINT\_11\_RUN](#ade582b07da3be853835863e2c4efd1fe)   ([IMX\_SPC\_11](#ac518e5c9a79447934ee3d0f35b3c334b) | [IMX\_GPC\_RUN](#a0346f0daeb276b819f045132114c74da)) |
| #define | [IMX\_SPC\_SET\_POINT\_11\_WAIT](#ad81fd8b58c73dd88f869fbe99e45af62)   ([IMX\_SPC\_11](#ac518e5c9a79447934ee3d0f35b3c334b) | [IMX\_GPC\_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)) |
| #define | [IMX\_SPC\_SET\_POINT\_11\_STOP](#af328d05fc2f3084025426bcfa8e07acb)   ([IMX\_SPC\_11](#ac518e5c9a79447934ee3d0f35b3c334b) | [IMX\_GPC\_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)) |
| #define | [IMX\_SPC\_SET\_POINT\_11\_SUSPEND](#aa84a574b06d37679035c9e160794103b)   ([IMX\_SPC\_11](#ac518e5c9a79447934ee3d0f35b3c334b) | [IMX\_GPC\_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)) |
| #define | [IMX\_SPC\_SET\_POINT\_12\_RUN](#aa4b08d6e86e2a0786aa4b8467063e744)   ([IMX\_SPC\_12](#ab6ceb05e36ef4c24d3a776ddadf2a17b) | [IMX\_GPC\_RUN](#a0346f0daeb276b819f045132114c74da)) |
| #define | [IMX\_SPC\_SET\_POINT\_12\_WAIT](#a06f577fcd7a7039930f5cd60f10dbdbb)   ([IMX\_SPC\_12](#ab6ceb05e36ef4c24d3a776ddadf2a17b) | [IMX\_GPC\_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)) |
| #define | [IMX\_SPC\_SET\_POINT\_12\_STOP](#a82f472da9010bb1de1a74837d1b2eae7)   ([IMX\_SPC\_12](#ab6ceb05e36ef4c24d3a776ddadf2a17b) | [IMX\_GPC\_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)) |
| #define | [IMX\_SPC\_SET\_POINT\_12\_SUSPEND](#a393fdb54cd063085108b8d600653e3a3)   ([IMX\_SPC\_12](#ab6ceb05e36ef4c24d3a776ddadf2a17b) | [IMX\_GPC\_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)) |
| #define | [IMX\_SPC\_SET\_POINT\_13\_RUN](#aa62f55fa30c7fe258eb5bce336914b74)   ([IMX\_SPC\_13](#a5bc88e7c7ec8e9bcda35ad60f671bef5) | [IMX\_GPC\_RUN](#a0346f0daeb276b819f045132114c74da)) |
| #define | [IMX\_SPC\_SET\_POINT\_13\_WAIT](#a9603a1be5b8faf232c06f39526052992)   ([IMX\_SPC\_13](#a5bc88e7c7ec8e9bcda35ad60f671bef5) | [IMX\_GPC\_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)) |
| #define | [IMX\_SPC\_SET\_POINT\_13\_STOP](#a1c1e481a627910fee5786560815a7442)   ([IMX\_SPC\_13](#a5bc88e7c7ec8e9bcda35ad60f671bef5) | [IMX\_GPC\_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)) |
| #define | [IMX\_SPC\_SET\_POINT\_13\_SUSPEND](#a2e56fe135af350c5ebd92196cdca8067)   ([IMX\_SPC\_13](#a5bc88e7c7ec8e9bcda35ad60f671bef5) | [IMX\_GPC\_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)) |
| #define | [IMX\_SPC\_SET\_POINT\_14\_RUN](#a23f38fd1002d77d327a84ad8ca5e3d22)   ([IMX\_SPC\_14](#a11b0cee3cc0d34591c11e1da6aa3e586) | [IMX\_GPC\_RUN](#a0346f0daeb276b819f045132114c74da)) |
| #define | [IMX\_SPC\_SET\_POINT\_14\_WAIT](#abbda3ffc097e0cbba6f4a529215899f0)   ([IMX\_SPC\_14](#a11b0cee3cc0d34591c11e1da6aa3e586) | [IMX\_GPC\_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)) |
| #define | [IMX\_SPC\_SET\_POINT\_14\_STOP](#addc192b8864a96a935e983021fd6991b)   ([IMX\_SPC\_14](#a11b0cee3cc0d34591c11e1da6aa3e586) | [IMX\_GPC\_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)) |
| #define | [IMX\_SPC\_SET\_POINT\_14\_SUSPEND](#adabea62f128c40438f1edb29d597accd)   ([IMX\_SPC\_14](#a11b0cee3cc0d34591c11e1da6aa3e586) | [IMX\_GPC\_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)) |
| #define | [IMX\_SPC\_SET\_POINT\_15\_RUN](#a0efa4fa53bce64f0c89f9d4eb07ba27d)   ([IMX\_SPC\_15](#a89c2348f26960a938b7126a631ff4440) | [IMX\_GPC\_RUN](#a0346f0daeb276b819f045132114c74da)) |
| #define | [IMX\_SPC\_SET\_POINT\_15\_WAIT](#af691cffe687076e6ac2f03db06f9b48f)   ([IMX\_SPC\_15](#a89c2348f26960a938b7126a631ff4440) | [IMX\_GPC\_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)) |
| #define | [IMX\_SPC\_SET\_POINT\_15\_STOP](#a6a24e7b3e0e9e3a1ba0dd2984bd9fde6)   ([IMX\_SPC\_15](#a89c2348f26960a938b7126a631ff4440) | [IMX\_GPC\_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)) |
| #define | [IMX\_SPC\_SET\_POINT\_15\_SUSPEND](#a1eade5203e39d0892c2f9eba8fd023f9)   ([IMX\_SPC\_15](#a89c2348f26960a938b7126a631ff4440) | [IMX\_GPC\_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)) |

## Macro Definition Documentation

## [◆ ](#ae9feac62ff35ec0fef30e75ae0a88bee)IMX\_GPC\_MODE

| #define IMX\_GPC\_MODE | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(x & [IMX\_GPC\_MODE\_MASK](#a8468498e09c899056ea9f77e686c867a))

[IMX\_GPC\_MODE\_MASK](#a8468498e09c899056ea9f77e686c867a)

#define IMX\_GPC\_MODE\_MASK

**Definition** imx\_spc.h:29

## [◆ ](#a8468498e09c899056ea9f77e686c867a)IMX\_GPC\_MODE\_MASK

| #define IMX\_GPC\_MODE\_MASK   0xF |
| --- |

## [◆ ](#a0346f0daeb276b819f045132114c74da)IMX\_GPC\_RUN

| #define IMX\_GPC\_RUN   0x0 |
| --- |

## [◆ ](#a0bd3da16de75240efaa9dbacc7abc1a9)IMX\_GPC\_STOP

| #define IMX\_GPC\_STOP   0x2 |
| --- |

## [◆ ](#a75a363ea77fdfa2a8f922869baf9cae5)IMX\_GPC\_SUSPEND

| #define IMX\_GPC\_SUSPEND   0x3 |
| --- |

## [◆ ](#a1f32dc4faba3158ab48cee77563a5a92)IMX\_GPC\_WAIT

| #define IMX\_GPC\_WAIT   0x1 |
| --- |

## [◆ ](#ada6ec38357d6bf3ce7f4102744e79bbc)IMX\_SPC

| #define IMX\_SPC | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((x & [IMX\_SPC\_MASK](#ac16b45dfd6df94cad425dd8bf2eb0119)) >> [IMX\_SPC\_SHIFT](#a626b183ac785be3b2cc9d2e8cbb841f4))

[IMX\_SPC\_SHIFT](#a626b183ac785be3b2cc9d2e8cbb841f4)

#define IMX\_SPC\_SHIFT

**Definition** imx\_spc.h:28

[IMX\_SPC\_MASK](#ac16b45dfd6df94cad425dd8bf2eb0119)

#define IMX\_SPC\_MASK

**Definition** imx\_spc.h:27

## [◆ ](#a2b91ceadf0b08f329ca48e459be4b8cf)IMX\_SPC\_0

| #define IMX\_SPC\_0   0x00 |
| --- |

## [◆ ](#ac01b3b94d1a06a7870a48b3366edee55)IMX\_SPC\_1

| #define IMX\_SPC\_1   0x10 |
| --- |

## [◆ ](#a7b8f4911506984f1ac3fb2b91983a351)IMX\_SPC\_10

| #define IMX\_SPC\_10   0xA0 |
| --- |

## [◆ ](#ac518e5c9a79447934ee3d0f35b3c334b)IMX\_SPC\_11

| #define IMX\_SPC\_11   0xB0 |
| --- |

## [◆ ](#ab6ceb05e36ef4c24d3a776ddadf2a17b)IMX\_SPC\_12

| #define IMX\_SPC\_12   0xC0 |
| --- |

## [◆ ](#a5bc88e7c7ec8e9bcda35ad60f671bef5)IMX\_SPC\_13

| #define IMX\_SPC\_13   0xD0 |
| --- |

## [◆ ](#a11b0cee3cc0d34591c11e1da6aa3e586)IMX\_SPC\_14

| #define IMX\_SPC\_14   0xE0 |
| --- |

## [◆ ](#a89c2348f26960a938b7126a631ff4440)IMX\_SPC\_15

| #define IMX\_SPC\_15   0xF0 |
| --- |

## [◆ ](#a214286102c951b04eb1a18aed412cd98)IMX\_SPC\_2

| #define IMX\_SPC\_2   0x20 |
| --- |

## [◆ ](#af88f9b163c2a831198506bfc42455a54)IMX\_SPC\_3

| #define IMX\_SPC\_3   0x30 |
| --- |

## [◆ ](#ac36951bfc1258656226275d6eb9bd7da)IMX\_SPC\_4

| #define IMX\_SPC\_4   0x40 |
| --- |

## [◆ ](#a0ca2082bf7718bba8a4cbd3cae1e8491)IMX\_SPC\_5

| #define IMX\_SPC\_5   0x50 |
| --- |

## [◆ ](#a97af1d082a356f5ac275fc84c0ca21c7)IMX\_SPC\_6

| #define IMX\_SPC\_6   0x60 |
| --- |

## [◆ ](#ac73c19b933caae5626297572ee3ff022)IMX\_SPC\_7

| #define IMX\_SPC\_7   0x70 |
| --- |

## [◆ ](#a1d8798b3f2081e9ff647b92e8515cd14)IMX\_SPC\_8

| #define IMX\_SPC\_8   0x80 |
| --- |

## [◆ ](#a8cde5e61745d8e2b5641f50ab2ceed14)IMX\_SPC\_9

| #define IMX\_SPC\_9   0x90 |
| --- |

## [◆ ](#ac16b45dfd6df94cad425dd8bf2eb0119)IMX\_SPC\_MASK

| #define IMX\_SPC\_MASK   0xF0 |
| --- |

## [◆ ](#a2513b235eb5c1d2eef874cde812d66e2)IMX\_SPC\_SET\_POINT\_0\_RUN

| #define IMX\_SPC\_SET\_POINT\_0\_RUN   ([IMX\_SPC\_0](#a2b91ceadf0b08f329ca48e459be4b8cf) | [IMX\_GPC\_RUN](#a0346f0daeb276b819f045132114c74da)) |
| --- |

## [◆ ](#ac0bcab370462ec48cc65c2ad72673e25)IMX\_SPC\_SET\_POINT\_0\_STOP

| #define IMX\_SPC\_SET\_POINT\_0\_STOP   ([IMX\_SPC\_0](#a2b91ceadf0b08f329ca48e459be4b8cf) | [IMX\_GPC\_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)) |
| --- |

## [◆ ](#ad9a6bdc024c700869ba4b2a226449498)IMX\_SPC\_SET\_POINT\_0\_SUSPEND

| #define IMX\_SPC\_SET\_POINT\_0\_SUSPEND   ([IMX\_SPC\_0](#a2b91ceadf0b08f329ca48e459be4b8cf) | [IMX\_GPC\_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)) |
| --- |

## [◆ ](#a655eb9644e0f6edf17055c43beb8bc78)IMX\_SPC\_SET\_POINT\_0\_WAIT

| #define IMX\_SPC\_SET\_POINT\_0\_WAIT   ([IMX\_SPC\_0](#a2b91ceadf0b08f329ca48e459be4b8cf) | [IMX\_GPC\_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)) |
| --- |

## [◆ ](#a7be6d85aa76e65805716c2bf20553fae)IMX\_SPC\_SET\_POINT\_10\_RUN

| #define IMX\_SPC\_SET\_POINT\_10\_RUN   ([IMX\_SPC\_10](#a7b8f4911506984f1ac3fb2b91983a351) | [IMX\_GPC\_RUN](#a0346f0daeb276b819f045132114c74da)) |
| --- |

## [◆ ](#a61e070d9c04cea7c4e0f7fb3ff703718)IMX\_SPC\_SET\_POINT\_10\_STOP

| #define IMX\_SPC\_SET\_POINT\_10\_STOP   ([IMX\_SPC\_10](#a7b8f4911506984f1ac3fb2b91983a351) | [IMX\_GPC\_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)) |
| --- |

## [◆ ](#a2d6aecb9ac2033ca89ca673c6786fe61)IMX\_SPC\_SET\_POINT\_10\_SUSPEND

| #define IMX\_SPC\_SET\_POINT\_10\_SUSPEND   ([IMX\_SPC\_10](#a7b8f4911506984f1ac3fb2b91983a351) | [IMX\_GPC\_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)) |
| --- |

## [◆ ](#a57e3cbbf5409c9b634a67d381f81b36c)IMX\_SPC\_SET\_POINT\_10\_WAIT

| #define IMX\_SPC\_SET\_POINT\_10\_WAIT   ([IMX\_SPC\_10](#a7b8f4911506984f1ac3fb2b91983a351) | [IMX\_GPC\_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)) |
| --- |

## [◆ ](#ade582b07da3be853835863e2c4efd1fe)IMX\_SPC\_SET\_POINT\_11\_RUN

| #define IMX\_SPC\_SET\_POINT\_11\_RUN   ([IMX\_SPC\_11](#ac518e5c9a79447934ee3d0f35b3c334b) | [IMX\_GPC\_RUN](#a0346f0daeb276b819f045132114c74da)) |
| --- |

## [◆ ](#af328d05fc2f3084025426bcfa8e07acb)IMX\_SPC\_SET\_POINT\_11\_STOP

| #define IMX\_SPC\_SET\_POINT\_11\_STOP   ([IMX\_SPC\_11](#ac518e5c9a79447934ee3d0f35b3c334b) | [IMX\_GPC\_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)) |
| --- |

## [◆ ](#aa84a574b06d37679035c9e160794103b)IMX\_SPC\_SET\_POINT\_11\_SUSPEND

| #define IMX\_SPC\_SET\_POINT\_11\_SUSPEND   ([IMX\_SPC\_11](#ac518e5c9a79447934ee3d0f35b3c334b) | [IMX\_GPC\_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)) |
| --- |

## [◆ ](#ad81fd8b58c73dd88f869fbe99e45af62)IMX\_SPC\_SET\_POINT\_11\_WAIT

| #define IMX\_SPC\_SET\_POINT\_11\_WAIT   ([IMX\_SPC\_11](#ac518e5c9a79447934ee3d0f35b3c334b) | [IMX\_GPC\_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)) |
| --- |

## [◆ ](#aa4b08d6e86e2a0786aa4b8467063e744)IMX\_SPC\_SET\_POINT\_12\_RUN

| #define IMX\_SPC\_SET\_POINT\_12\_RUN   ([IMX\_SPC\_12](#ab6ceb05e36ef4c24d3a776ddadf2a17b) | [IMX\_GPC\_RUN](#a0346f0daeb276b819f045132114c74da)) |
| --- |

## [◆ ](#a82f472da9010bb1de1a74837d1b2eae7)IMX\_SPC\_SET\_POINT\_12\_STOP

| #define IMX\_SPC\_SET\_POINT\_12\_STOP   ([IMX\_SPC\_12](#ab6ceb05e36ef4c24d3a776ddadf2a17b) | [IMX\_GPC\_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)) |
| --- |

## [◆ ](#a393fdb54cd063085108b8d600653e3a3)IMX\_SPC\_SET\_POINT\_12\_SUSPEND

| #define IMX\_SPC\_SET\_POINT\_12\_SUSPEND   ([IMX\_SPC\_12](#ab6ceb05e36ef4c24d3a776ddadf2a17b) | [IMX\_GPC\_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)) |
| --- |

## [◆ ](#a06f577fcd7a7039930f5cd60f10dbdbb)IMX\_SPC\_SET\_POINT\_12\_WAIT

| #define IMX\_SPC\_SET\_POINT\_12\_WAIT   ([IMX\_SPC\_12](#ab6ceb05e36ef4c24d3a776ddadf2a17b) | [IMX\_GPC\_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)) |
| --- |

## [◆ ](#aa62f55fa30c7fe258eb5bce336914b74)IMX\_SPC\_SET\_POINT\_13\_RUN

| #define IMX\_SPC\_SET\_POINT\_13\_RUN   ([IMX\_SPC\_13](#a5bc88e7c7ec8e9bcda35ad60f671bef5) | [IMX\_GPC\_RUN](#a0346f0daeb276b819f045132114c74da)) |
| --- |

## [◆ ](#a1c1e481a627910fee5786560815a7442)IMX\_SPC\_SET\_POINT\_13\_STOP

| #define IMX\_SPC\_SET\_POINT\_13\_STOP   ([IMX\_SPC\_13](#a5bc88e7c7ec8e9bcda35ad60f671bef5) | [IMX\_GPC\_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)) |
| --- |

## [◆ ](#a2e56fe135af350c5ebd92196cdca8067)IMX\_SPC\_SET\_POINT\_13\_SUSPEND

| #define IMX\_SPC\_SET\_POINT\_13\_SUSPEND   ([IMX\_SPC\_13](#a5bc88e7c7ec8e9bcda35ad60f671bef5) | [IMX\_GPC\_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)) |
| --- |

## [◆ ](#a9603a1be5b8faf232c06f39526052992)IMX\_SPC\_SET\_POINT\_13\_WAIT

| #define IMX\_SPC\_SET\_POINT\_13\_WAIT   ([IMX\_SPC\_13](#a5bc88e7c7ec8e9bcda35ad60f671bef5) | [IMX\_GPC\_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)) |
| --- |

## [◆ ](#a23f38fd1002d77d327a84ad8ca5e3d22)IMX\_SPC\_SET\_POINT\_14\_RUN

| #define IMX\_SPC\_SET\_POINT\_14\_RUN   ([IMX\_SPC\_14](#a11b0cee3cc0d34591c11e1da6aa3e586) | [IMX\_GPC\_RUN](#a0346f0daeb276b819f045132114c74da)) |
| --- |

## [◆ ](#addc192b8864a96a935e983021fd6991b)IMX\_SPC\_SET\_POINT\_14\_STOP

| #define IMX\_SPC\_SET\_POINT\_14\_STOP   ([IMX\_SPC\_14](#a11b0cee3cc0d34591c11e1da6aa3e586) | [IMX\_GPC\_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)) |
| --- |

## [◆ ](#adabea62f128c40438f1edb29d597accd)IMX\_SPC\_SET\_POINT\_14\_SUSPEND

| #define IMX\_SPC\_SET\_POINT\_14\_SUSPEND   ([IMX\_SPC\_14](#a11b0cee3cc0d34591c11e1da6aa3e586) | [IMX\_GPC\_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)) |
| --- |

## [◆ ](#abbda3ffc097e0cbba6f4a529215899f0)IMX\_SPC\_SET\_POINT\_14\_WAIT

| #define IMX\_SPC\_SET\_POINT\_14\_WAIT   ([IMX\_SPC\_14](#a11b0cee3cc0d34591c11e1da6aa3e586) | [IMX\_GPC\_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)) |
| --- |

## [◆ ](#a0efa4fa53bce64f0c89f9d4eb07ba27d)IMX\_SPC\_SET\_POINT\_15\_RUN

| #define IMX\_SPC\_SET\_POINT\_15\_RUN   ([IMX\_SPC\_15](#a89c2348f26960a938b7126a631ff4440) | [IMX\_GPC\_RUN](#a0346f0daeb276b819f045132114c74da)) |
| --- |

## [◆ ](#a6a24e7b3e0e9e3a1ba0dd2984bd9fde6)IMX\_SPC\_SET\_POINT\_15\_STOP

| #define IMX\_SPC\_SET\_POINT\_15\_STOP   ([IMX\_SPC\_15](#a89c2348f26960a938b7126a631ff4440) | [IMX\_GPC\_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)) |
| --- |

## [◆ ](#a1eade5203e39d0892c2f9eba8fd023f9)IMX\_SPC\_SET\_POINT\_15\_SUSPEND

| #define IMX\_SPC\_SET\_POINT\_15\_SUSPEND   ([IMX\_SPC\_15](#a89c2348f26960a938b7126a631ff4440) | [IMX\_GPC\_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)) |
| --- |

## [◆ ](#af691cffe687076e6ac2f03db06f9b48f)IMX\_SPC\_SET\_POINT\_15\_WAIT

| #define IMX\_SPC\_SET\_POINT\_15\_WAIT   ([IMX\_SPC\_15](#a89c2348f26960a938b7126a631ff4440) | [IMX\_GPC\_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)) |
| --- |

## [◆ ](#a675487df773ccd4a478c0ed74ffc1b8d)IMX\_SPC\_SET\_POINT\_1\_RUN

| #define IMX\_SPC\_SET\_POINT\_1\_RUN   ([IMX\_SPC\_1](#ac01b3b94d1a06a7870a48b3366edee55) | [IMX\_GPC\_RUN](#a0346f0daeb276b819f045132114c74da)) |
| --- |

## [◆ ](#abc74b52dbaec59ed1a437a6012737dcb)IMX\_SPC\_SET\_POINT\_1\_STOP

| #define IMX\_SPC\_SET\_POINT\_1\_STOP   ([IMX\_SPC\_1](#ac01b3b94d1a06a7870a48b3366edee55) | [IMX\_GPC\_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)) |
| --- |

## [◆ ](#a27bb5318452f3bdd359ea77a937ffe51)IMX\_SPC\_SET\_POINT\_1\_SUSPEND

| #define IMX\_SPC\_SET\_POINT\_1\_SUSPEND   ([IMX\_SPC\_1](#ac01b3b94d1a06a7870a48b3366edee55) | [IMX\_GPC\_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)) |
| --- |

## [◆ ](#ad70a5fc9fa6991d212e251223f69845c)IMX\_SPC\_SET\_POINT\_1\_WAIT

| #define IMX\_SPC\_SET\_POINT\_1\_WAIT   ([IMX\_SPC\_1](#ac01b3b94d1a06a7870a48b3366edee55) | [IMX\_GPC\_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)) |
| --- |

## [◆ ](#a212b8780e33e35edc68463cbbb656f47)IMX\_SPC\_SET\_POINT\_2\_RUN

| #define IMX\_SPC\_SET\_POINT\_2\_RUN   ([IMX\_SPC\_2](#a214286102c951b04eb1a18aed412cd98) | [IMX\_GPC\_RUN](#a0346f0daeb276b819f045132114c74da)) |
| --- |

## [◆ ](#aea99f181628c69b96ea093698b4c91fd)IMX\_SPC\_SET\_POINT\_2\_STOP

| #define IMX\_SPC\_SET\_POINT\_2\_STOP   ([IMX\_SPC\_2](#a214286102c951b04eb1a18aed412cd98) | [IMX\_GPC\_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)) |
| --- |

## [◆ ](#a0db51a91cb50008bbdc8baf9621ae55c)IMX\_SPC\_SET\_POINT\_2\_SUSPEND

| #define IMX\_SPC\_SET\_POINT\_2\_SUSPEND   ([IMX\_SPC\_2](#a214286102c951b04eb1a18aed412cd98) | [IMX\_GPC\_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)) |
| --- |

## [◆ ](#a3e890fdf63a58fd42a0139812550d370)IMX\_SPC\_SET\_POINT\_2\_WAIT

| #define IMX\_SPC\_SET\_POINT\_2\_WAIT   ([IMX\_SPC\_2](#a214286102c951b04eb1a18aed412cd98) | [IMX\_GPC\_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)) |
| --- |

## [◆ ](#a955a3993640e5f07be6dbdbac6b2887b)IMX\_SPC\_SET\_POINT\_3\_RUN

| #define IMX\_SPC\_SET\_POINT\_3\_RUN   ([IMX\_SPC\_3](#af88f9b163c2a831198506bfc42455a54) | [IMX\_GPC\_RUN](#a0346f0daeb276b819f045132114c74da)) |
| --- |

## [◆ ](#a0fa20de0d1a6d4b59fb236467ed6eed8)IMX\_SPC\_SET\_POINT\_3\_STOP

| #define IMX\_SPC\_SET\_POINT\_3\_STOP   ([IMX\_SPC\_3](#af88f9b163c2a831198506bfc42455a54) | [IMX\_GPC\_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)) |
| --- |

## [◆ ](#a320b1171760941ca6220ae445027b2bb)IMX\_SPC\_SET\_POINT\_3\_SUSPEND

| #define IMX\_SPC\_SET\_POINT\_3\_SUSPEND   ([IMX\_SPC\_3](#af88f9b163c2a831198506bfc42455a54) | [IMX\_GPC\_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)) |
| --- |

## [◆ ](#a77917334bf2072b01ee996b8b3cdbd0a)IMX\_SPC\_SET\_POINT\_3\_WAIT

| #define IMX\_SPC\_SET\_POINT\_3\_WAIT   ([IMX\_SPC\_3](#af88f9b163c2a831198506bfc42455a54) | [IMX\_GPC\_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)) |
| --- |

## [◆ ](#a3a875a06de64389b17942fe7096e533b)IMX\_SPC\_SET\_POINT\_4\_RUN

| #define IMX\_SPC\_SET\_POINT\_4\_RUN   ([IMX\_SPC\_4](#ac36951bfc1258656226275d6eb9bd7da) | [IMX\_GPC\_RUN](#a0346f0daeb276b819f045132114c74da)) |
| --- |

## [◆ ](#a6f2e970fea0a5b9713a98e6cb5b31060)IMX\_SPC\_SET\_POINT\_4\_STOP

| #define IMX\_SPC\_SET\_POINT\_4\_STOP   ([IMX\_SPC\_4](#ac36951bfc1258656226275d6eb9bd7da) | [IMX\_GPC\_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)) |
| --- |

## [◆ ](#a8b2c95d1accb75acb84d074c6f9554b4)IMX\_SPC\_SET\_POINT\_4\_SUSPEND

| #define IMX\_SPC\_SET\_POINT\_4\_SUSPEND   ([IMX\_SPC\_4](#ac36951bfc1258656226275d6eb9bd7da) | [IMX\_GPC\_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)) |
| --- |

## [◆ ](#a53d8e05a6545202e55c12b9e19723141)IMX\_SPC\_SET\_POINT\_4\_WAIT

| #define IMX\_SPC\_SET\_POINT\_4\_WAIT   ([IMX\_SPC\_4](#ac36951bfc1258656226275d6eb9bd7da) | [IMX\_GPC\_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)) |
| --- |

## [◆ ](#a08e368e7fbccdf9910ef41f8054e6ac7)IMX\_SPC\_SET\_POINT\_5\_RUN

| #define IMX\_SPC\_SET\_POINT\_5\_RUN   ([IMX\_SPC\_5](#a0ca2082bf7718bba8a4cbd3cae1e8491) | [IMX\_GPC\_RUN](#a0346f0daeb276b819f045132114c74da)) |
| --- |

## [◆ ](#a2111e4b8468791f5062bc1fafba1e871)IMX\_SPC\_SET\_POINT\_5\_STOP

| #define IMX\_SPC\_SET\_POINT\_5\_STOP   ([IMX\_SPC\_5](#a0ca2082bf7718bba8a4cbd3cae1e8491) | [IMX\_GPC\_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)) |
| --- |

## [◆ ](#a14047d119208c1c188d28e3fef2286cf)IMX\_SPC\_SET\_POINT\_5\_SUSPEND

| #define IMX\_SPC\_SET\_POINT\_5\_SUSPEND   ([IMX\_SPC\_5](#a0ca2082bf7718bba8a4cbd3cae1e8491) | [IMX\_GPC\_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)) |
| --- |

## [◆ ](#ab8b90420137da04a8ce432c1b0385613)IMX\_SPC\_SET\_POINT\_5\_WAIT

| #define IMX\_SPC\_SET\_POINT\_5\_WAIT   ([IMX\_SPC\_5](#a0ca2082bf7718bba8a4cbd3cae1e8491) | [IMX\_GPC\_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)) |
| --- |

## [◆ ](#ae667a3617c9389bef9d08f3d4a639731)IMX\_SPC\_SET\_POINT\_6\_RUN

| #define IMX\_SPC\_SET\_POINT\_6\_RUN   ([IMX\_SPC\_6](#a97af1d082a356f5ac275fc84c0ca21c7) | [IMX\_GPC\_RUN](#a0346f0daeb276b819f045132114c74da)) |
| --- |

## [◆ ](#ab8f1fe76f07af84111d2532d4205a01c)IMX\_SPC\_SET\_POINT\_6\_STOP

| #define IMX\_SPC\_SET\_POINT\_6\_STOP   ([IMX\_SPC\_6](#a97af1d082a356f5ac275fc84c0ca21c7) | [IMX\_GPC\_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)) |
| --- |

## [◆ ](#ae977b643f59534d5df555e6aa283a82d)IMX\_SPC\_SET\_POINT\_6\_SUSPEND

| #define IMX\_SPC\_SET\_POINT\_6\_SUSPEND   ([IMX\_SPC\_6](#a97af1d082a356f5ac275fc84c0ca21c7) | [IMX\_GPC\_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)) |
| --- |

## [◆ ](#aaf448cdd4b85f7c7417e5de766361035)IMX\_SPC\_SET\_POINT\_6\_WAIT

| #define IMX\_SPC\_SET\_POINT\_6\_WAIT   ([IMX\_SPC\_6](#a97af1d082a356f5ac275fc84c0ca21c7) | [IMX\_GPC\_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)) |
| --- |

## [◆ ](#a4edbee6f04031c2c8f2b835d0e100bf3)IMX\_SPC\_SET\_POINT\_7\_RUN

| #define IMX\_SPC\_SET\_POINT\_7\_RUN   ([IMX\_SPC\_7](#ac73c19b933caae5626297572ee3ff022) | [IMX\_GPC\_RUN](#a0346f0daeb276b819f045132114c74da)) |
| --- |

## [◆ ](#a996d39beaa9490adf49c602f325ebe04)IMX\_SPC\_SET\_POINT\_7\_STOP

| #define IMX\_SPC\_SET\_POINT\_7\_STOP   ([IMX\_SPC\_7](#ac73c19b933caae5626297572ee3ff022) | [IMX\_GPC\_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)) |
| --- |

## [◆ ](#a9b90dd5fd6f801e27a95e02f6e7614d7)IMX\_SPC\_SET\_POINT\_7\_SUSPEND

| #define IMX\_SPC\_SET\_POINT\_7\_SUSPEND   ([IMX\_SPC\_7](#ac73c19b933caae5626297572ee3ff022) | [IMX\_GPC\_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)) |
| --- |

## [◆ ](#a78e453e0425752c8bb636cd45e9f66a5)IMX\_SPC\_SET\_POINT\_7\_WAIT

| #define IMX\_SPC\_SET\_POINT\_7\_WAIT   ([IMX\_SPC\_7](#ac73c19b933caae5626297572ee3ff022) | [IMX\_GPC\_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)) |
| --- |

## [◆ ](#acbfdb5f70d7f4aee7435f5ca6d014596)IMX\_SPC\_SET\_POINT\_8\_RUN

| #define IMX\_SPC\_SET\_POINT\_8\_RUN   ([IMX\_SPC\_8](#a1d8798b3f2081e9ff647b92e8515cd14) | [IMX\_GPC\_RUN](#a0346f0daeb276b819f045132114c74da)) |
| --- |

## [◆ ](#a4f2f29f9e4bb420436d881b8233a43b5)IMX\_SPC\_SET\_POINT\_8\_STOP

| #define IMX\_SPC\_SET\_POINT\_8\_STOP   ([IMX\_SPC\_8](#a1d8798b3f2081e9ff647b92e8515cd14) | [IMX\_GPC\_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)) |
| --- |

## [◆ ](#a686e1a2d26bc3df4d465614da82bae08)IMX\_SPC\_SET\_POINT\_8\_SUSPEND

| #define IMX\_SPC\_SET\_POINT\_8\_SUSPEND   ([IMX\_SPC\_8](#a1d8798b3f2081e9ff647b92e8515cd14) | [IMX\_GPC\_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)) |
| --- |

## [◆ ](#a402e534a33588b1f3b31d0a7284d32ab)IMX\_SPC\_SET\_POINT\_8\_WAIT

| #define IMX\_SPC\_SET\_POINT\_8\_WAIT   ([IMX\_SPC\_8](#a1d8798b3f2081e9ff647b92e8515cd14) | [IMX\_GPC\_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)) |
| --- |

## [◆ ](#ab591869ecb6606cdf1e73cc3849f611d)IMX\_SPC\_SET\_POINT\_9\_RUN

| #define IMX\_SPC\_SET\_POINT\_9\_RUN   ([IMX\_SPC\_9](#a8cde5e61745d8e2b5641f50ab2ceed14) | [IMX\_GPC\_RUN](#a0346f0daeb276b819f045132114c74da)) |
| --- |

## [◆ ](#a9696110f23d443b540cbfa8aedd25e9b)IMX\_SPC\_SET\_POINT\_9\_STOP

| #define IMX\_SPC\_SET\_POINT\_9\_STOP   ([IMX\_SPC\_9](#a8cde5e61745d8e2b5641f50ab2ceed14) | [IMX\_GPC\_STOP](#a0bd3da16de75240efaa9dbacc7abc1a9)) |
| --- |

## [◆ ](#a8e6427bd9509ffb3b51f18b62753340c)IMX\_SPC\_SET\_POINT\_9\_SUSPEND

| #define IMX\_SPC\_SET\_POINT\_9\_SUSPEND   ([IMX\_SPC\_9](#a8cde5e61745d8e2b5641f50ab2ceed14) | [IMX\_GPC\_SUSPEND](#a75a363ea77fdfa2a8f922869baf9cae5)) |
| --- |

## [◆ ](#ad234e9dd6516742f9d8869fda039a5c1)IMX\_SPC\_SET\_POINT\_9\_WAIT

| #define IMX\_SPC\_SET\_POINT\_9\_WAIT   ([IMX\_SPC\_9](#a8cde5e61745d8e2b5641f50ab2ceed14) | [IMX\_GPC\_WAIT](#a1f32dc4faba3158ab48cee77563a5a92)) |
| --- |

## [◆ ](#a626b183ac785be3b2cc9d2e8cbb841f4)IMX\_SPC\_SHIFT

| #define IMX\_SPC\_SHIFT   4 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pm](dir_108d2a5c081446f0496ddf8d635df811.md)
- [imx\_spc.h](imx__spc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
