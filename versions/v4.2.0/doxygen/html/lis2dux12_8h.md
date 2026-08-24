---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/lis2dux12_8h.html
original_path: doxygen/html/lis2dux12_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lis2dux12.h File Reference

`#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h_source.md)>`

[Go to the source code of this file.](lis2dux12_8h_source.md)

| Macros | |
| --- | --- |
| #define | [LIS2DUX12\_OPER\_MODE\_POWER\_DOWN](#a2319e5357a3b3933e46e0e445d8bb868)   0 |
| #define | [LIS2DUX12\_OPER\_MODE\_LOW\_POWER](#a03d276c97b5ee65f80ce301f78d8d620)   1 |
| #define | [LIS2DUX12\_OPER\_MODE\_HIGH\_PERFORMANCE](#ae08239e9d97ce581865d441faf13861b)   2 |
| #define | [LIS2DUX12\_OPER\_MODE\_SINGLE\_SHOT](#a1a6e9387e8b30d1c6ffcf0f02ca61000)   3 |
| #define | [LIS2DUX12\_DT\_ODR\_OFF](#a94ab30f7ef8aec193a84188ccf63a21d)   0 |
| #define | [LIS2DUX12\_DT\_ODR\_1Hz\_ULP](#ae8f5f4224653c75ba0343d13d0588910)   1 /\* available in ultra-low power mode \*/ |
| #define | [LIS2DUX12\_DT\_ODR\_3Hz\_ULP](#a4a85ef36d5836a6c216a36272c645cfb)   2 /\* available in ultra-low power mode \*/ |
| #define | [LIS2DUX12\_DT\_ODR\_25Hz\_ULP](#af649bb985c44d6631e6fd1a0a91fbf85)   3 /\* available in ultra-low power mode \*/ |
| #define | [LIS2DUX12\_DT\_ODR\_6Hz](#a7c83ff001a3ff25aaab5cbac32a56df0)   4 /\* available in LP and HP mode \*/ |
| #define | [LIS2DUX12\_DT\_ODR\_12Hz5](#a01ab37065a2bb53366adc7740af37d62)   5 /\* available in LP and HP mode \*/ |
| #define | [LIS2DUX12\_DT\_ODR\_25Hz](#a1daa6448cea439025041b74f5dc3e58f)   6 /\* available in LP and HP mode \*/ |
| #define | [LIS2DUX12\_DT\_ODR\_50Hz](#aea1f056b715ed59a38ddb4c8aac48804)   7 /\* available in LP and HP mode \*/ |
| #define | [LIS2DUX12\_DT\_ODR\_100Hz](#a3b40a334bea0de6546b783ab65e9f4dd)   8 /\* available in LP and HP mode \*/ |
| #define | [LIS2DUX12\_DT\_ODR\_200Hz](#a230b18cdf50c202d1bced583914332e1)   9 /\* available in LP and HP mode \*/ |
| #define | [LIS2DUX12\_DT\_ODR\_400Hz](#ae3dc67b51572e8f0c5d5ec3394d5d750)   10 /\* available in LP and HP mode \*/ |
| #define | [LIS2DUX12\_DT\_ODR\_800Hz](#a6a8105006b18fe6632fbce06c77bed52)   11 /\* available in LP and HP mode \*/ |
| #define | [LIS2DUX12\_DT\_ODR\_END](#a68214dc2825057ef3fa3e87a7ae1fcc1)   12 |
| #define | [LIS2DUX12\_DT\_FS\_2G](#a9793fcda818ea10e61e844a3b94cda62)   0 /\* 2g (0.061 mg/LSB) \*/ |
| #define | [LIS2DUX12\_DT\_FS\_4G](#ab50eb77d0d2bac9eb493ec0490f2b4f7)   1 /\* 4g (0.122 mg/LSB) \*/ |
| #define | [LIS2DUX12\_DT\_FS\_8G](#ad0119b9353cec4ff57ad4e6fe1c7c055)   2 /\* 8g (0.244 mg/LSB) \*/ |
| #define | [LIS2DUX12\_DT\_FS\_16G](#a6e29f5351f4eebe482648629024af77e)   3 /\* 16g (0.488 mg/LSB) \*/ |
| #define | [LIS2DUX12\_DT\_BDR\_XL\_ODR](#a3d4281053ce07bf0e2871180affd246a)   0x0 |
| #define | [LIS2DUX12\_DT\_BDR\_XL\_ODR\_DIV\_2](#a658039a66e163c5950d80eebd1b67f4a)   0x1 |
| #define | [LIS2DUX12\_DT\_BDR\_XL\_ODR\_DIV\_4](#a0b27bbf1af06f586a9f901d8603629b7)   0x2 |
| #define | [LIS2DUX12\_DT\_BDR\_XL\_ODR\_DIV\_8](#adf324739868e1fe7bc4b1128699e2223)   0x3 |
| #define | [LIS2DUX12\_DT\_BDR\_XL\_ODR\_DIV\_16](#a9560e4c28c1d4b50f273aab0c3274274)   0x4 |
| #define | [LIS2DUX12\_DT\_BDR\_XL\_ODR\_DIV\_32](#a03ef61baf524a38730341b3344cdc046)   0x5 |
| #define | [LIS2DUX12\_DT\_BDR\_XL\_ODR\_DIV\_64](#a73e547d7a3fd0436ee3c308d6f7c20f2)   0x6 |
| #define | [LIS2DUX12\_DT\_BDR\_XL\_ODR\_OFF](#afbbb48285a89128d313eeea2b7a1bbb1)   0x7 |
| #define | [LIS2DUX12\_DT\_DEC\_TS\_OFF](#a058e573325b65dde80dd3813984ac38a)   0x0 |
| #define | [LIS2DUX12\_DT\_DEC\_TS\_1](#a7520bcd1eae2b91bf068cdc1f6ae4487)   0x1 |
| #define | [LIS2DUX12\_DT\_DEC\_TS\_8](#a209de2a2bd10240767aa01c9d2f4d73d)   0x2 |
| #define | [LIS2DUX12\_DT\_DEC\_TS\_32](#a12c2234e04c51383868576fb82f8cecc)   0x3 |
| #define | [LIS2DUXXX\_FIFO\_EMPTY](#ab0f9df25d43e17fc210c63581a3abc0f)   0x0 |
| #define | [LIS2DUXXX\_XL\_TEMP\_TAG](#a26fc2cb8dbefd4995f47b0dd4b7d0652)   0x2 |
| #define | [LIS2DUXXX\_XL\_ONLY\_2X\_TAG](#a6540e92e3d71a254fbb5c6d13e0e707c)   0x3 |
| #define | [LIS2DUXXX\_TIMESTAMP\_TAG](#a4eb99cf7057a0688bc7289c3fbb05020)   0x4 |
| #define | [LIS2DUXXX\_STEP\_COUNTER\_TAG](#ad2648a4dd63e75dc6ec07fc7f5307ed8)   0x12 |
| #define | [LIS2DUXXX\_MLC\_RESULT\_TAG](#ab6e05aec8aec334546ef581b88f85741)   0x1A |
| #define | [LIS2DUXXX\_MLC\_FILTER\_TAG](#a9063c5ef1b246d7e859945aaa2832dd3)   0x1B |
| #define | [LIS2DUXXX\_MLC\_FEATURE](#a9ca64efe26ab1956ccffd4a921c0352c)   0x1C |
| #define | [LIS2DUXXX\_FSM\_RESULT\_TAG](#aa0b27f7c2bca8115c3026482aeaea324)   0x1D |
| #define | [LIS2DUXXX\_DT\_BYPASS\_MODE](#acc96a742af72f029a4b05ef67f99bb6d)   0x0 |
| #define | [LIS2DUXXX\_DT\_FIFO\_MODE](#a64c29d5624aac1eb64d5d38f3aa77f2b)   0x1 |
| #define | [LIS2DUXXX\_DT\_STREAM\_TO\_FIFO\_MODE](#ad0846e36da27873da048c8c44689f59e)   0x3 |
| #define | [LIS2DUXXX\_DT\_BYPASS\_TO\_STREAM\_MODE](#a2d1b9368d9bfcc55b93334fb13208b21)   0x4 |
| #define | [LIS2DUXXX\_DT\_STREAM\_MODE](#a62f6c22b8c4bdeb587a5262a727e4368)   0x6 |
| #define | [LIS2DUXXX\_DT\_BYPASS\_TO\_FIFO\_MODE](#a2ad4e4ad6c41d804db6a502f7863726a)   0x7 |
| #define | [LIS2DUXXX\_DT\_FIFO\_OFF](#a952127a0b7199066e7f3f0fa58fa2f95)   0x8 |
| #define | [LIS2DUXXX\_DT\_FIFO\_CTRL](#affa56c1d9471f5afbada2c14261f36a3)   0x15U |
| #define | [LIS2DUXXX\_DT\_STATUS](#ac4d1357af5ab51679f04a03a5396f76e)   0x25U |
| #define | [LIS2DUXXX\_DT\_FIFO\_STATUS1](#aeb7afe0eb54defa45b66a5726d51dec7)   0x26U |
| #define | [LIS2DUXXX\_DT\_OUTX\_L](#a7fd3f10740da5a54fdf18f37c9282f29)   0x28U |
| #define | [LIS2DUXXX\_DT\_FIFO\_DATA\_OUT\_TAG](#ad773a65749a20dd28e4e7b37cf8db62d)   0x40U |

## Macro Definition Documentation

## [◆ ](#a3d4281053ce07bf0e2871180affd246a)LIS2DUX12\_DT\_BDR\_XL\_ODR

| #define LIS2DUX12\_DT\_BDR\_XL\_ODR   0x0 |
| --- |

## [◆ ](#a9560e4c28c1d4b50f273aab0c3274274)LIS2DUX12\_DT\_BDR\_XL\_ODR\_DIV\_16

| #define LIS2DUX12\_DT\_BDR\_XL\_ODR\_DIV\_16   0x4 |
| --- |

## [◆ ](#a658039a66e163c5950d80eebd1b67f4a)LIS2DUX12\_DT\_BDR\_XL\_ODR\_DIV\_2

| #define LIS2DUX12\_DT\_BDR\_XL\_ODR\_DIV\_2   0x1 |
| --- |

## [◆ ](#a03ef61baf524a38730341b3344cdc046)LIS2DUX12\_DT\_BDR\_XL\_ODR\_DIV\_32

| #define LIS2DUX12\_DT\_BDR\_XL\_ODR\_DIV\_32   0x5 |
| --- |

## [◆ ](#a0b27bbf1af06f586a9f901d8603629b7)LIS2DUX12\_DT\_BDR\_XL\_ODR\_DIV\_4

| #define LIS2DUX12\_DT\_BDR\_XL\_ODR\_DIV\_4   0x2 |
| --- |

## [◆ ](#a73e547d7a3fd0436ee3c308d6f7c20f2)LIS2DUX12\_DT\_BDR\_XL\_ODR\_DIV\_64

| #define LIS2DUX12\_DT\_BDR\_XL\_ODR\_DIV\_64   0x6 |
| --- |

## [◆ ](#adf324739868e1fe7bc4b1128699e2223)LIS2DUX12\_DT\_BDR\_XL\_ODR\_DIV\_8

| #define LIS2DUX12\_DT\_BDR\_XL\_ODR\_DIV\_8   0x3 |
| --- |

## [◆ ](#afbbb48285a89128d313eeea2b7a1bbb1)LIS2DUX12\_DT\_BDR\_XL\_ODR\_OFF

| #define LIS2DUX12\_DT\_BDR\_XL\_ODR\_OFF   0x7 |
| --- |

## [◆ ](#a7520bcd1eae2b91bf068cdc1f6ae4487)LIS2DUX12\_DT\_DEC\_TS\_1

| #define LIS2DUX12\_DT\_DEC\_TS\_1   0x1 |
| --- |

## [◆ ](#a12c2234e04c51383868576fb82f8cecc)LIS2DUX12\_DT\_DEC\_TS\_32

| #define LIS2DUX12\_DT\_DEC\_TS\_32   0x3 |
| --- |

## [◆ ](#a209de2a2bd10240767aa01c9d2f4d73d)LIS2DUX12\_DT\_DEC\_TS\_8

| #define LIS2DUX12\_DT\_DEC\_TS\_8   0x2 |
| --- |

## [◆ ](#a058e573325b65dde80dd3813984ac38a)LIS2DUX12\_DT\_DEC\_TS\_OFF

| #define LIS2DUX12\_DT\_DEC\_TS\_OFF   0x0 |
| --- |

## [◆ ](#a6e29f5351f4eebe482648629024af77e)LIS2DUX12\_DT\_FS\_16G

| #define LIS2DUX12\_DT\_FS\_16G   3 /\* 16g (0.488 mg/LSB) \*/ |
| --- |

## [◆ ](#a9793fcda818ea10e61e844a3b94cda62)LIS2DUX12\_DT\_FS\_2G

| #define LIS2DUX12\_DT\_FS\_2G   0 /\* 2g (0.061 mg/LSB) \*/ |
| --- |

## [◆ ](#ab50eb77d0d2bac9eb493ec0490f2b4f7)LIS2DUX12\_DT\_FS\_4G

| #define LIS2DUX12\_DT\_FS\_4G   1 /\* 4g (0.122 mg/LSB) \*/ |
| --- |

## [◆ ](#ad0119b9353cec4ff57ad4e6fe1c7c055)LIS2DUX12\_DT\_FS\_8G

| #define LIS2DUX12\_DT\_FS\_8G   2 /\* 8g (0.244 mg/LSB) \*/ |
| --- |

## [◆ ](#a3b40a334bea0de6546b783ab65e9f4dd)LIS2DUX12\_DT\_ODR\_100Hz

| #define LIS2DUX12\_DT\_ODR\_100Hz   8 /\* available in LP and HP mode \*/ |
| --- |

## [◆ ](#a01ab37065a2bb53366adc7740af37d62)LIS2DUX12\_DT\_ODR\_12Hz5

| #define LIS2DUX12\_DT\_ODR\_12Hz5   5 /\* available in LP and HP mode \*/ |
| --- |

## [◆ ](#ae8f5f4224653c75ba0343d13d0588910)LIS2DUX12\_DT\_ODR\_1Hz\_ULP

| #define LIS2DUX12\_DT\_ODR\_1Hz\_ULP   1 /\* available in ultra-low power mode \*/ |
| --- |

## [◆ ](#a230b18cdf50c202d1bced583914332e1)LIS2DUX12\_DT\_ODR\_200Hz

| #define LIS2DUX12\_DT\_ODR\_200Hz   9 /\* available in LP and HP mode \*/ |
| --- |

## [◆ ](#a1daa6448cea439025041b74f5dc3e58f)LIS2DUX12\_DT\_ODR\_25Hz

| #define LIS2DUX12\_DT\_ODR\_25Hz   6 /\* available in LP and HP mode \*/ |
| --- |

## [◆ ](#af649bb985c44d6631e6fd1a0a91fbf85)LIS2DUX12\_DT\_ODR\_25Hz\_ULP

| #define LIS2DUX12\_DT\_ODR\_25Hz\_ULP   3 /\* available in ultra-low power mode \*/ |
| --- |

## [◆ ](#a4a85ef36d5836a6c216a36272c645cfb)LIS2DUX12\_DT\_ODR\_3Hz\_ULP

| #define LIS2DUX12\_DT\_ODR\_3Hz\_ULP   2 /\* available in ultra-low power mode \*/ |
| --- |

## [◆ ](#ae3dc67b51572e8f0c5d5ec3394d5d750)LIS2DUX12\_DT\_ODR\_400Hz

| #define LIS2DUX12\_DT\_ODR\_400Hz   10 /\* available in LP and HP mode \*/ |
| --- |

## [◆ ](#aea1f056b715ed59a38ddb4c8aac48804)LIS2DUX12\_DT\_ODR\_50Hz

| #define LIS2DUX12\_DT\_ODR\_50Hz   7 /\* available in LP and HP mode \*/ |
| --- |

## [◆ ](#a7c83ff001a3ff25aaab5cbac32a56df0)LIS2DUX12\_DT\_ODR\_6Hz

| #define LIS2DUX12\_DT\_ODR\_6Hz   4 /\* available in LP and HP mode \*/ |
| --- |

## [◆ ](#a6a8105006b18fe6632fbce06c77bed52)LIS2DUX12\_DT\_ODR\_800Hz

| #define LIS2DUX12\_DT\_ODR\_800Hz   11 /\* available in LP and HP mode \*/ |
| --- |

## [◆ ](#a68214dc2825057ef3fa3e87a7ae1fcc1)LIS2DUX12\_DT\_ODR\_END

| #define LIS2DUX12\_DT\_ODR\_END   12 |
| --- |

## [◆ ](#a94ab30f7ef8aec193a84188ccf63a21d)LIS2DUX12\_DT\_ODR\_OFF

| #define LIS2DUX12\_DT\_ODR\_OFF   0 |
| --- |

## [◆ ](#ae08239e9d97ce581865d441faf13861b)LIS2DUX12\_OPER\_MODE\_HIGH\_PERFORMANCE

| #define LIS2DUX12\_OPER\_MODE\_HIGH\_PERFORMANCE   2 |
| --- |

## [◆ ](#a03d276c97b5ee65f80ce301f78d8d620)LIS2DUX12\_OPER\_MODE\_LOW\_POWER

| #define LIS2DUX12\_OPER\_MODE\_LOW\_POWER   1 |
| --- |

## [◆ ](#a2319e5357a3b3933e46e0e445d8bb868)LIS2DUX12\_OPER\_MODE\_POWER\_DOWN

| #define LIS2DUX12\_OPER\_MODE\_POWER\_DOWN   0 |
| --- |

## [◆ ](#a1a6e9387e8b30d1c6ffcf0f02ca61000)LIS2DUX12\_OPER\_MODE\_SINGLE\_SHOT

| #define LIS2DUX12\_OPER\_MODE\_SINGLE\_SHOT   3 |
| --- |

## [◆ ](#acc96a742af72f029a4b05ef67f99bb6d)LIS2DUXXX\_DT\_BYPASS\_MODE

| #define LIS2DUXXX\_DT\_BYPASS\_MODE   0x0 |
| --- |

## [◆ ](#a2ad4e4ad6c41d804db6a502f7863726a)LIS2DUXXX\_DT\_BYPASS\_TO\_FIFO\_MODE

| #define LIS2DUXXX\_DT\_BYPASS\_TO\_FIFO\_MODE   0x7 |
| --- |

## [◆ ](#a2d1b9368d9bfcc55b93334fb13208b21)LIS2DUXXX\_DT\_BYPASS\_TO\_STREAM\_MODE

| #define LIS2DUXXX\_DT\_BYPASS\_TO\_STREAM\_MODE   0x4 |
| --- |

## [◆ ](#affa56c1d9471f5afbada2c14261f36a3)LIS2DUXXX\_DT\_FIFO\_CTRL

| #define LIS2DUXXX\_DT\_FIFO\_CTRL   0x15U |
| --- |

## [◆ ](#ad773a65749a20dd28e4e7b37cf8db62d)LIS2DUXXX\_DT\_FIFO\_DATA\_OUT\_TAG

| #define LIS2DUXXX\_DT\_FIFO\_DATA\_OUT\_TAG   0x40U |
| --- |

## [◆ ](#a64c29d5624aac1eb64d5d38f3aa77f2b)LIS2DUXXX\_DT\_FIFO\_MODE

| #define LIS2DUXXX\_DT\_FIFO\_MODE   0x1 |
| --- |

## [◆ ](#a952127a0b7199066e7f3f0fa58fa2f95)LIS2DUXXX\_DT\_FIFO\_OFF

| #define LIS2DUXXX\_DT\_FIFO\_OFF   0x8 |
| --- |

## [◆ ](#aeb7afe0eb54defa45b66a5726d51dec7)LIS2DUXXX\_DT\_FIFO\_STATUS1

| #define LIS2DUXXX\_DT\_FIFO\_STATUS1   0x26U |
| --- |

## [◆ ](#a7fd3f10740da5a54fdf18f37c9282f29)LIS2DUXXX\_DT\_OUTX\_L

| #define LIS2DUXXX\_DT\_OUTX\_L   0x28U |
| --- |

## [◆ ](#ac4d1357af5ab51679f04a03a5396f76e)LIS2DUXXX\_DT\_STATUS

| #define LIS2DUXXX\_DT\_STATUS   0x25U |
| --- |

## [◆ ](#a62f6c22b8c4bdeb587a5262a727e4368)LIS2DUXXX\_DT\_STREAM\_MODE

| #define LIS2DUXXX\_DT\_STREAM\_MODE   0x6 |
| --- |

## [◆ ](#ad0846e36da27873da048c8c44689f59e)LIS2DUXXX\_DT\_STREAM\_TO\_FIFO\_MODE

| #define LIS2DUXXX\_DT\_STREAM\_TO\_FIFO\_MODE   0x3 |
| --- |

## [◆ ](#ab0f9df25d43e17fc210c63581a3abc0f)LIS2DUXXX\_FIFO\_EMPTY

| #define LIS2DUXXX\_FIFO\_EMPTY   0x0 |
| --- |

## [◆ ](#aa0b27f7c2bca8115c3026482aeaea324)LIS2DUXXX\_FSM\_RESULT\_TAG

| #define LIS2DUXXX\_FSM\_RESULT\_TAG   0x1D |
| --- |

## [◆ ](#a9ca64efe26ab1956ccffd4a921c0352c)LIS2DUXXX\_MLC\_FEATURE

| #define LIS2DUXXX\_MLC\_FEATURE   0x1C |
| --- |

## [◆ ](#a9063c5ef1b246d7e859945aaa2832dd3)LIS2DUXXX\_MLC\_FILTER\_TAG

| #define LIS2DUXXX\_MLC\_FILTER\_TAG   0x1B |
| --- |

## [◆ ](#ab6e05aec8aec334546ef581b88f85741)LIS2DUXXX\_MLC\_RESULT\_TAG

| #define LIS2DUXXX\_MLC\_RESULT\_TAG   0x1A |
| --- |

## [◆ ](#ad2648a4dd63e75dc6ec07fc7f5307ed8)LIS2DUXXX\_STEP\_COUNTER\_TAG

| #define LIS2DUXXX\_STEP\_COUNTER\_TAG   0x12 |
| --- |

## [◆ ](#a4eb99cf7057a0688bc7289c3fbb05020)LIS2DUXXX\_TIMESTAMP\_TAG

| #define LIS2DUXXX\_TIMESTAMP\_TAG   0x4 |
| --- |

## [◆ ](#a6540e92e3d71a254fbb5c6d13e0e707c)LIS2DUXXX\_XL\_ONLY\_2X\_TAG

| #define LIS2DUXXX\_XL\_ONLY\_2X\_TAG   0x3 |
| --- |

## [◆ ](#a26fc2cb8dbefd4995f47b0dd4b7d0652)LIS2DUXXX\_XL\_TEMP\_TAG

| #define LIS2DUXXX\_XL\_TEMP\_TAG   0x2 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [sensor](dir_c9b2d7ff2bbb57ff9b1854f820609711.md)
- [lis2dux12.h](lis2dux12_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
