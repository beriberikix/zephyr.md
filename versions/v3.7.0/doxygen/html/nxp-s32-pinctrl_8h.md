---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/nxp-s32-pinctrl_8h.html
original_path: doxygen/html/nxp-s32-pinctrl_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nxp-s32-pinctrl.h File Reference

`#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h_source.md)>`

[Go to the source code of this file.](nxp-s32-pinctrl_8h_source.md)

| Macros | |
| --- | --- |
| #define | [NXP\_S32\_MSCR\_SSS\_SHIFT](#a2915bea966e78ea0875d00aed07cb4f6)   0U |
| #define | [NXP\_S32\_MSCR\_SSS\_MASK](#adc6d352496e379e60800d91a8e45885a)   [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(3) |
| #define | [NXP\_S32\_IMCR\_SSS\_SHIFT](#ab0a01e301ede34e769656f519b4a573a)   3U |
| #define | [NXP\_S32\_IMCR\_SSS\_MASK](#aa7b1d14b0d177551f76179d6a2f950f6)   [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(4) |
| #define | [NXP\_S32\_IMCR\_IDX\_SHIFT](#a7bcfc62953dea1ea593d2cc469f38d49)   7U |
| #define | [NXP\_S32\_IMCR\_IDX\_MASK](#a5f123343f14837fc00f6ae82050af000)   [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(9) |
| #define | [NXP\_S32\_MSCR\_IDX\_SHIFT](#a73bc3039d390d44ce9752053ad5bc7f2)   16U |
| #define | [NXP\_S32\_MSCR\_IDX\_MASK](#a24215e725f602151bf8085f3c951f704)   [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(9) |
| #define | [NXP\_S32\_SIUL2\_IDX\_SHIFT](#a08f75243446c15a7937bae2a2bbef58b)   25U |
| #define | [NXP\_S32\_SIUL2\_IDX\_MASK](#ad59950f8650e65f4d8be107f193ca423)   [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(3) |
| #define | [NXP\_S32\_PINMUX\_MSCR\_SSS](#a2edf4ccc26acaa5d553c40d406934fa9)(cfg) |
| #define | [NXP\_S32\_PINMUX\_IMCR\_SSS](#ac4a9d494c6dae04bbdf0cd76355b5d5e)(cfg) |
| #define | [NXP\_S32\_PINMUX\_IMCR\_IDX](#ac0cac289de975ecd3ffdcf696603c2fc)(cfg) |
| #define | [NXP\_S32\_PINMUX\_MSCR\_IDX](#ab6cb17e02b461e18fedc4bfe1cbc63d1)(cfg) |
| #define | [NXP\_S32\_PINMUX\_SIUL2\_IDX](#a841ea93977e7df9eb799b758ef2084d9)(cfg) |
| #define | [NXP\_S32\_PINMUX\_GET\_MSCR\_SSS](#a6e538ced36ab7da873e02a1b2a52a910)(cfg) |
| #define | [NXP\_S32\_PINMUX\_GET\_IMCR\_SSS](#a6ac30440c335d57ab1d5a3ec50bbc457)(cfg) |
| #define | [NXP\_S32\_PINMUX\_GET\_IMCR\_IDX](#ab4cd4a833393ea9aefa22efd7fcaf2b2)(cfg) |
| #define | [NXP\_S32\_PINMUX\_GET\_MSCR\_IDX](#a24d49cba327429b5abc3311bd1fe221f)(cfg) |
| #define | [NXP\_S32\_PINMUX\_GET\_SIUL2\_IDX](#a7dd79890341efa232612f1fd7538b561)(cfg) |
| #define | [NXP\_S32\_PINMUX](#a56420e905ab13c7a6ed8e1e88d8f06ff)(siul2\_idx, mscr\_idx, mscr\_sss, imcr\_idx, imcr\_sss) |
|  | Utility macro to build NXP S32 pinmux property for pinctrl nodes. |

## Macro Definition Documentation

## [◆ ](#a5f123343f14837fc00f6ae82050af000)NXP\_S32\_IMCR\_IDX\_MASK

| #define NXP\_S32\_IMCR\_IDX\_MASK   [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(9) |
| --- |

## [◆ ](#a7bcfc62953dea1ea593d2cc469f38d49)NXP\_S32\_IMCR\_IDX\_SHIFT

| #define NXP\_S32\_IMCR\_IDX\_SHIFT   7U |
| --- |

## [◆ ](#aa7b1d14b0d177551f76179d6a2f950f6)NXP\_S32\_IMCR\_SSS\_MASK

| #define NXP\_S32\_IMCR\_SSS\_MASK   [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(4) |
| --- |

## [◆ ](#ab0a01e301ede34e769656f519b4a573a)NXP\_S32\_IMCR\_SSS\_SHIFT

| #define NXP\_S32\_IMCR\_SSS\_SHIFT   3U |
| --- |

## [◆ ](#a24215e725f602151bf8085f3c951f704)NXP\_S32\_MSCR\_IDX\_MASK

| #define NXP\_S32\_MSCR\_IDX\_MASK   [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(9) |
| --- |

## [◆ ](#a73bc3039d390d44ce9752053ad5bc7f2)NXP\_S32\_MSCR\_IDX\_SHIFT

| #define NXP\_S32\_MSCR\_IDX\_SHIFT   16U |
| --- |

## [◆ ](#adc6d352496e379e60800d91a8e45885a)NXP\_S32\_MSCR\_SSS\_MASK

| #define NXP\_S32\_MSCR\_SSS\_MASK   [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(3) |
| --- |

## [◆ ](#a2915bea966e78ea0875d00aed07cb4f6)NXP\_S32\_MSCR\_SSS\_SHIFT

| #define NXP\_S32\_MSCR\_SSS\_SHIFT   0U |
| --- |

## [◆ ](#a56420e905ab13c7a6ed8e1e88d8f06ff)NXP\_S32\_PINMUX

| #define NXP\_S32\_PINMUX | ( |  | *siul2\_idx*, |
| --- | --- | --- | --- |
|  |  |  | *mscr\_idx*, |
|  |  |  | *mscr\_sss*, |
|  |  |  | *imcr\_idx*, |
|  |  |  | *imcr\_sss* ) |

**Value:**

([NXP\_S32\_PINMUX\_SIUL2\_IDX](#a841ea93977e7df9eb799b758ef2084d9)(siul2\_idx) | [NXP\_S32\_PINMUX\_MSCR\_IDX](#ab6cb17e02b461e18fedc4bfe1cbc63d1)(mscr\_idx) \

| [NXP\_S32\_PINMUX\_MSCR\_SSS](#a2edf4ccc26acaa5d553c40d406934fa9)(mscr\_sss) | [NXP\_S32\_PINMUX\_IMCR\_IDX](#ac0cac289de975ecd3ffdcf696603c2fc)(imcr\_idx) \

| [NXP\_S32\_PINMUX\_IMCR\_SSS](#ac4a9d494c6dae04bbdf0cd76355b5d5e)(imcr\_sss))

[NXP\_S32\_PINMUX\_MSCR\_SSS](#a2edf4ccc26acaa5d553c40d406934fa9)

#define NXP\_S32\_PINMUX\_MSCR\_SSS(cfg)

**Definition** nxp-s32-pinctrl.h:33

[NXP\_S32\_PINMUX\_SIUL2\_IDX](#a841ea93977e7df9eb799b758ef2084d9)

#define NXP\_S32\_PINMUX\_SIUL2\_IDX(cfg)

**Definition** nxp-s32-pinctrl.h:45

[NXP\_S32\_PINMUX\_MSCR\_IDX](#ab6cb17e02b461e18fedc4bfe1cbc63d1)

#define NXP\_S32\_PINMUX\_MSCR\_IDX(cfg)

**Definition** nxp-s32-pinctrl.h:42

[NXP\_S32\_PINMUX\_IMCR\_IDX](#ac0cac289de975ecd3ffdcf696603c2fc)

#define NXP\_S32\_PINMUX\_IMCR\_IDX(cfg)

**Definition** nxp-s32-pinctrl.h:39

[NXP\_S32\_PINMUX\_IMCR\_SSS](#ac4a9d494c6dae04bbdf0cd76355b5d5e)

#define NXP\_S32\_PINMUX\_IMCR\_SSS(cfg)

**Definition** nxp-s32-pinctrl.h:36

Utility macro to build NXP S32 pinmux property for pinctrl nodes.

Parameters
:   | siul2\_idx | SIUL2 instance index |
    | --- | --- |
    | mscr\_idx | Multiplexed Signal Configuration Register (MSCR) index |
    | mscr\_sss | Output mux Source Signal Selection (MSCR.SSS) |
    | imcr\_idx | Input Multiplexed Signal Configuration Register (IMCR) index |
    | imcr\_sss | Input mux Source Signal Selection (IMCR.SSS) |

## [◆ ](#ab4cd4a833393ea9aefa22efd7fcaf2b2)NXP\_S32\_PINMUX\_GET\_IMCR\_IDX

| #define NXP\_S32\_PINMUX\_GET\_IMCR\_IDX | ( |  | *cfg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((cfg) >> [NXP\_S32\_IMCR\_IDX\_SHIFT](#a7bcfc62953dea1ea593d2cc469f38d49)) & [NXP\_S32\_IMCR\_IDX\_MASK](#a5f123343f14837fc00f6ae82050af000))

[NXP\_S32\_IMCR\_IDX\_MASK](#a5f123343f14837fc00f6ae82050af000)

#define NXP\_S32\_IMCR\_IDX\_MASK

**Definition** nxp-s32-pinctrl.h:27

[NXP\_S32\_IMCR\_IDX\_SHIFT](#a7bcfc62953dea1ea593d2cc469f38d49)

#define NXP\_S32\_IMCR\_IDX\_SHIFT

**Definition** nxp-s32-pinctrl.h:26

## [◆ ](#a6ac30440c335d57ab1d5a3ec50bbc457)NXP\_S32\_PINMUX\_GET\_IMCR\_SSS

| #define NXP\_S32\_PINMUX\_GET\_IMCR\_SSS | ( |  | *cfg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((cfg) >> [NXP\_S32\_IMCR\_SSS\_SHIFT](#ab0a01e301ede34e769656f519b4a573a)) & [NXP\_S32\_IMCR\_SSS\_MASK](#aa7b1d14b0d177551f76179d6a2f950f6))

[NXP\_S32\_IMCR\_SSS\_MASK](#aa7b1d14b0d177551f76179d6a2f950f6)

#define NXP\_S32\_IMCR\_SSS\_MASK

**Definition** nxp-s32-pinctrl.h:25

[NXP\_S32\_IMCR\_SSS\_SHIFT](#ab0a01e301ede34e769656f519b4a573a)

#define NXP\_S32\_IMCR\_SSS\_SHIFT

**Definition** nxp-s32-pinctrl.h:24

## [◆ ](#a24d49cba327429b5abc3311bd1fe221f)NXP\_S32\_PINMUX\_GET\_MSCR\_IDX

| #define NXP\_S32\_PINMUX\_GET\_MSCR\_IDX | ( |  | *cfg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((cfg) >> [NXP\_S32\_MSCR\_IDX\_SHIFT](#a73bc3039d390d44ce9752053ad5bc7f2)) & [NXP\_S32\_MSCR\_IDX\_MASK](#a24215e725f602151bf8085f3c951f704))

[NXP\_S32\_MSCR\_IDX\_MASK](#a24215e725f602151bf8085f3c951f704)

#define NXP\_S32\_MSCR\_IDX\_MASK

**Definition** nxp-s32-pinctrl.h:29

[NXP\_S32\_MSCR\_IDX\_SHIFT](#a73bc3039d390d44ce9752053ad5bc7f2)

#define NXP\_S32\_MSCR\_IDX\_SHIFT

**Definition** nxp-s32-pinctrl.h:28

## [◆ ](#a6e538ced36ab7da873e02a1b2a52a910)NXP\_S32\_PINMUX\_GET\_MSCR\_SSS

| #define NXP\_S32\_PINMUX\_GET\_MSCR\_SSS | ( |  | *cfg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((cfg) >> [NXP\_S32\_MSCR\_SSS\_SHIFT](#a2915bea966e78ea0875d00aed07cb4f6)) & [NXP\_S32\_MSCR\_SSS\_MASK](#adc6d352496e379e60800d91a8e45885a))

[NXP\_S32\_MSCR\_SSS\_SHIFT](#a2915bea966e78ea0875d00aed07cb4f6)

#define NXP\_S32\_MSCR\_SSS\_SHIFT

**Definition** nxp-s32-pinctrl.h:22

[NXP\_S32\_MSCR\_SSS\_MASK](#adc6d352496e379e60800d91a8e45885a)

#define NXP\_S32\_MSCR\_SSS\_MASK

**Definition** nxp-s32-pinctrl.h:23

## [◆ ](#a7dd79890341efa232612f1fd7538b561)NXP\_S32\_PINMUX\_GET\_SIUL2\_IDX

| #define NXP\_S32\_PINMUX\_GET\_SIUL2\_IDX | ( |  | *cfg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((cfg) >> [NXP\_S32\_SIUL2\_IDX\_SHIFT](#a08f75243446c15a7937bae2a2bbef58b)) & [NXP\_S32\_SIUL2\_IDX\_MASK](#ad59950f8650e65f4d8be107f193ca423))

[NXP\_S32\_SIUL2\_IDX\_SHIFT](#a08f75243446c15a7937bae2a2bbef58b)

#define NXP\_S32\_SIUL2\_IDX\_SHIFT

**Definition** nxp-s32-pinctrl.h:30

[NXP\_S32\_SIUL2\_IDX\_MASK](#ad59950f8650e65f4d8be107f193ca423)

#define NXP\_S32\_SIUL2\_IDX\_MASK

**Definition** nxp-s32-pinctrl.h:31

## [◆ ](#ac0cac289de975ecd3ffdcf696603c2fc)NXP\_S32\_PINMUX\_IMCR\_IDX

| #define NXP\_S32\_PINMUX\_IMCR\_IDX | ( |  | *cfg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((cfg) & [NXP\_S32\_IMCR\_IDX\_MASK](#a5f123343f14837fc00f6ae82050af000)) << [NXP\_S32\_IMCR\_IDX\_SHIFT](#a7bcfc62953dea1ea593d2cc469f38d49))

## [◆ ](#ac4a9d494c6dae04bbdf0cd76355b5d5e)NXP\_S32\_PINMUX\_IMCR\_SSS

| #define NXP\_S32\_PINMUX\_IMCR\_SSS | ( |  | *cfg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((cfg) & [NXP\_S32\_IMCR\_SSS\_MASK](#aa7b1d14b0d177551f76179d6a2f950f6)) << [NXP\_S32\_IMCR\_SSS\_SHIFT](#ab0a01e301ede34e769656f519b4a573a))

## [◆ ](#ab6cb17e02b461e18fedc4bfe1cbc63d1)NXP\_S32\_PINMUX\_MSCR\_IDX

| #define NXP\_S32\_PINMUX\_MSCR\_IDX | ( |  | *cfg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((cfg) & [NXP\_S32\_MSCR\_IDX\_MASK](#a24215e725f602151bf8085f3c951f704)) << [NXP\_S32\_MSCR\_IDX\_SHIFT](#a73bc3039d390d44ce9752053ad5bc7f2))

## [◆ ](#a2edf4ccc26acaa5d553c40d406934fa9)NXP\_S32\_PINMUX\_MSCR\_SSS

| #define NXP\_S32\_PINMUX\_MSCR\_SSS | ( |  | *cfg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((cfg) & [NXP\_S32\_MSCR\_SSS\_MASK](#adc6d352496e379e60800d91a8e45885a)) << [NXP\_S32\_MSCR\_SSS\_SHIFT](#a2915bea966e78ea0875d00aed07cb4f6))

## [◆ ](#a841ea93977e7df9eb799b758ef2084d9)NXP\_S32\_PINMUX\_SIUL2\_IDX

| #define NXP\_S32\_PINMUX\_SIUL2\_IDX | ( |  | *cfg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((cfg) & [NXP\_S32\_SIUL2\_IDX\_MASK](#ad59950f8650e65f4d8be107f193ca423)) << [NXP\_S32\_SIUL2\_IDX\_SHIFT](#a08f75243446c15a7937bae2a2bbef58b))

## [◆ ](#ad59950f8650e65f4d8be107f193ca423)NXP\_S32\_SIUL2\_IDX\_MASK

| #define NXP\_S32\_SIUL2\_IDX\_MASK   [BIT\_MASK](group__sys-util.md#ga3c12c6d36ad0aa481a3436923d21f4f8)(3) |
| --- |

## [◆ ](#a08f75243446c15a7937bae2a2bbef58b)NXP\_S32\_SIUL2\_IDX\_SHIFT

| #define NXP\_S32\_SIUL2\_IDX\_SHIFT   25U |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [nxp-s32-pinctrl.h](nxp-s32-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
