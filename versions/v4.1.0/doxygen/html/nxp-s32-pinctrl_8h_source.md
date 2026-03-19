---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/nxp-s32-pinctrl_8h_source.html
original_path: doxygen/html/nxp-s32-pinctrl_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nxp-s32-pinctrl.h

[Go to the documentation of this file.](nxp-s32-pinctrl_8h.md)

1/\*

2 \* Copyright 2022, 2024 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_NXP\_S32\_PINCTRL\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_NXP\_S32\_PINCTRL\_H\_

9

10#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h.md)>

11

12/\*

13 \* The NXP S32 pinmux configuration is encoded in a 32-bit field value as follows:

14 \*

15 \* - 0..2: Output mux Source Signal Selection (MSCR.SSS)

16 \* - 3..6: Input mux Source Signal Selection (IMCR.SSS)

17 \* - 7..15: Input Multiplexed Signal Configuration Register (IMCR) index

18 \* - 16..24: Multiplexed Signal Configuration Register (MSCR) index

19 \* - 25..27: MSCR SIUL2 instance index (0..7)

20 \* - 28..30: IMCR SIUL2 instance index (0..7)

21 \* - 31: Reserved for future use

22 \*/

[ 23](nxp-s32-pinctrl_8h.md#a2915bea966e78ea0875d00aed07cb4f6)#define NXP\_S32\_MSCR\_SSS\_SHIFT 0U

[ 24](nxp-s32-pinctrl_8h.md#adc6d352496e379e60800d91a8e45885a)#define NXP\_S32\_MSCR\_SSS\_MASK BIT\_MASK(3)

[ 25](nxp-s32-pinctrl_8h.md#ab0a01e301ede34e769656f519b4a573a)#define NXP\_S32\_IMCR\_SSS\_SHIFT 3U

[ 26](nxp-s32-pinctrl_8h.md#aa7b1d14b0d177551f76179d6a2f950f6)#define NXP\_S32\_IMCR\_SSS\_MASK BIT\_MASK(4)

[ 27](nxp-s32-pinctrl_8h.md#a7bcfc62953dea1ea593d2cc469f38d49)#define NXP\_S32\_IMCR\_IDX\_SHIFT 7U

[ 28](nxp-s32-pinctrl_8h.md#a5f123343f14837fc00f6ae82050af000)#define NXP\_S32\_IMCR\_IDX\_MASK BIT\_MASK(9)

[ 29](nxp-s32-pinctrl_8h.md#a73bc3039d390d44ce9752053ad5bc7f2)#define NXP\_S32\_MSCR\_IDX\_SHIFT 16U

[ 30](nxp-s32-pinctrl_8h.md#a24215e725f602151bf8085f3c951f704)#define NXP\_S32\_MSCR\_IDX\_MASK BIT\_MASK(9)

[ 31](nxp-s32-pinctrl_8h.md#acda7ed56ba5298bc9e2dedbf41689217)#define NXP\_S32\_MSCR\_SIUL2\_IDX\_SHIFT 25U

[ 32](nxp-s32-pinctrl_8h.md#a45370f12eb59e87b296e0ab8ca75d9a1)#define NXP\_S32\_MSCR\_SIUL2\_IDX\_MASK BIT\_MASK(3)

[ 33](nxp-s32-pinctrl_8h.md#ae8b5532ac34a69b0e6af420b30b9f21c)#define NXP\_S32\_IMCR\_SIUL2\_IDX\_SHIFT 28U

[ 34](nxp-s32-pinctrl_8h.md#a20d83adf4f587ac553cd410ea4c1e470)#define NXP\_S32\_IMCR\_SIUL2\_IDX\_MASK BIT\_MASK(3)

35

[ 36](nxp-s32-pinctrl_8h.md#a2edf4ccc26acaa5d553c40d406934fa9)#define NXP\_S32\_PINMUX\_MSCR\_SSS(cfg) \

37 (((cfg) & NXP\_S32\_MSCR\_SSS\_MASK) << NXP\_S32\_MSCR\_SSS\_SHIFT)

38

[ 39](nxp-s32-pinctrl_8h.md#ac4a9d494c6dae04bbdf0cd76355b5d5e)#define NXP\_S32\_PINMUX\_IMCR\_SSS(cfg) \

40 (((cfg) & NXP\_S32\_IMCR\_SSS\_MASK) << NXP\_S32\_IMCR\_SSS\_SHIFT)

41

[ 42](nxp-s32-pinctrl_8h.md#ac0cac289de975ecd3ffdcf696603c2fc)#define NXP\_S32\_PINMUX\_IMCR\_IDX(cfg) \

43 (((cfg) & NXP\_S32\_IMCR\_IDX\_MASK) << NXP\_S32\_IMCR\_IDX\_SHIFT)

44

[ 45](nxp-s32-pinctrl_8h.md#ab6cb17e02b461e18fedc4bfe1cbc63d1)#define NXP\_S32\_PINMUX\_MSCR\_IDX(cfg) \

46 (((cfg) & NXP\_S32\_MSCR\_IDX\_MASK) << NXP\_S32\_MSCR\_IDX\_SHIFT)

47

[ 48](nxp-s32-pinctrl_8h.md#a0ddbf8d6fb6e1cd40aa7883fe5509ee6)#define NXP\_S32\_PINMUX\_MSCR\_SIUL2\_IDX(cfg) \

49 (((cfg) & NXP\_S32\_MSCR\_SIUL2\_IDX\_MASK) << NXP\_S32\_MSCR\_SIUL2\_IDX\_SHIFT)

50

[ 51](nxp-s32-pinctrl_8h.md#a1ec211308d697276bef1d69a7619bede)#define NXP\_S32\_PINMUX\_IMCR\_SIUL2\_IDX(cfg) \

52 (((cfg) & NXP\_S32\_IMCR\_SIUL2\_IDX\_MASK) << NXP\_S32\_IMCR\_SIUL2\_IDX\_SHIFT)

53

[ 54](nxp-s32-pinctrl_8h.md#a6e538ced36ab7da873e02a1b2a52a910)#define NXP\_S32\_PINMUX\_GET\_MSCR\_SSS(cfg) \

55 (((cfg) >> NXP\_S32\_MSCR\_SSS\_SHIFT) & NXP\_S32\_MSCR\_SSS\_MASK)

56

[ 57](nxp-s32-pinctrl_8h.md#a6ac30440c335d57ab1d5a3ec50bbc457)#define NXP\_S32\_PINMUX\_GET\_IMCR\_SSS(cfg) \

58 (((cfg) >> NXP\_S32\_IMCR\_SSS\_SHIFT) & NXP\_S32\_IMCR\_SSS\_MASK)

59

[ 60](nxp-s32-pinctrl_8h.md#ab4cd4a833393ea9aefa22efd7fcaf2b2)#define NXP\_S32\_PINMUX\_GET\_IMCR\_IDX(cfg) \

61 (((cfg) >> NXP\_S32\_IMCR\_IDX\_SHIFT) & NXP\_S32\_IMCR\_IDX\_MASK)

62

[ 63](nxp-s32-pinctrl_8h.md#a24d49cba327429b5abc3311bd1fe221f)#define NXP\_S32\_PINMUX\_GET\_MSCR\_IDX(cfg) \

64 (((cfg) >> NXP\_S32\_MSCR\_IDX\_SHIFT) & NXP\_S32\_MSCR\_IDX\_MASK)

65

[ 66](nxp-s32-pinctrl_8h.md#a10a5d08b6be11d50d535b269f62fcde8)#define NXP\_S32\_PINMUX\_GET\_MSCR\_SIUL2\_IDX(cfg) \

67 (((cfg) >> NXP\_S32\_MSCR\_SIUL2\_IDX\_SHIFT) & NXP\_S32\_MSCR\_SIUL2\_IDX\_MASK)

68

[ 69](nxp-s32-pinctrl_8h.md#ac21c656b243792b10af59199c00e1915)#define NXP\_S32\_PINMUX\_GET\_IMCR\_SIUL2\_IDX(cfg) \

70 (((cfg) >> NXP\_S32\_IMCR\_SIUL2\_IDX\_SHIFT) & NXP\_S32\_IMCR\_SIUL2\_IDX\_MASK)

71

[ 82](nxp-s32-pinctrl_8h.md#ab7ff4f1d2a05ec44c358ff52f13a5733)#define NXP\_S32\_PINMUX(mscr\_siul2\_idx, imcr\_siul2\_idx, mscr\_idx, mscr\_sss, imcr\_idx, imcr\_sss) \

83 (NXP\_S32\_PINMUX\_MSCR\_SIUL2\_IDX(mscr\_siul2\_idx) | \

84 NXP\_S32\_PINMUX\_IMCR\_SIUL2\_IDX(imcr\_siul2\_idx) | \

85 NXP\_S32\_PINMUX\_MSCR\_IDX(mscr\_idx) | \

86 NXP\_S32\_PINMUX\_MSCR\_SSS(mscr\_sss) | \

87 NXP\_S32\_PINMUX\_IMCR\_IDX(imcr\_idx) | \

88 NXP\_S32\_PINMUX\_IMCR\_SSS(imcr\_sss))

89

90#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PINCTRL\_NXP\_NXP\_S32\_PINCTRL\_H\_ \*/

[dt-util.h](dt-util_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [nxp-s32-pinctrl.h](nxp-s32-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
