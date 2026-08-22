---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/mspm0-pinctrl_8h.html
original_path: doxygen/html/mspm0-pinctrl_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mspm0-pinctrl.h File Reference

[Go to the source code of this file.](mspm0-pinctrl_8h_source.md)

| Macros | |
| --- | --- |
| #define | [MSP\_PORT\_INDEX\_BY\_NAME](#a7bc7b96a754e425dd773b864eb0181be)(x) |
| #define | [MSPM0\_PIN\_FUNCTION\_ANALOG](#aed042e160fbf0499081e08f32b485ccc)   (0x00000000) |
| #define | [MSPM0\_PIN\_FUNCTION\_GPIO](#aafceb12e339618d1282aa7300507d9a5)   (0x00000001) |
| #define | [MSPM0\_PIN\_FUNCTION\_2](#a2d119d2da878acd9ebac10c6d0cc7c80)   (0x00000002) |
| #define | [MSPM0\_PIN\_FUNCTION\_3](#a4cdd8ded8a55c33f3b586152d64b2621)   (0x00000003) |
| #define | [MSPM0\_PIN\_FUNCTION\_4](#a897c32ff405a8c4eeaaffed7a6c69d5a)   (0x00000004) |
| #define | [MSPM0\_PIN\_FUNCTION\_5](#ab6ec2101ebc8d171852da5c72a9e6ff1)   (0x00000005) |
| #define | [MSPM0\_PIN\_FUNCTION\_6](#a4891b06c78d726a4806ea7f8c18d2bbc)   (0x00000006) |
| #define | [MSPM0\_PIN\_FUNCTION\_7](#af2b0ea70556adb258d70cbb7274dce12)   (0x00000007) |
| #define | [MSPM0\_PIN\_FUNCTION\_8](#a250cc53f70b280ed5a909f5b968f2c0b)   (0x00000008) |
| #define | [MSPM0\_PIN\_FUNCTION\_9](#affb9f84a279ac6ec00f153d024282b05)   (0x00000009) |
| #define | [MSPM0\_PIN\_FUNCTION\_10](#a974860da2ed7b0ad8835edf35fc3fa71)   (0x0000000A) |
| #define | [MSP\_PINMUX](#a6d8c1db9082542af49cc37dce3d02720)(pincm, function) |

## Macro Definition Documentation

## [◆ ](#a6d8c1db9082542af49cc37dce3d02720)MSP\_PINMUX

| #define MSP\_PINMUX | ( |  | *pincm*, |
| --- | --- | --- | --- |
|  |  |  | *function* ) |

**Value:**

(((pincm - 1) << 0x10) | function)

## [◆ ](#a7bc7b96a754e425dd773b864eb0181be)MSP\_PORT\_INDEX\_BY\_NAME

| #define MSP\_PORT\_INDEX\_BY\_NAME | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((x == "PORTA") ? 0 : 1)

## [◆ ](#a974860da2ed7b0ad8835edf35fc3fa71)MSPM0\_PIN\_FUNCTION\_10

| #define MSPM0\_PIN\_FUNCTION\_10   (0x0000000A) |
| --- |

## [◆ ](#a2d119d2da878acd9ebac10c6d0cc7c80)MSPM0\_PIN\_FUNCTION\_2

| #define MSPM0\_PIN\_FUNCTION\_2   (0x00000002) |
| --- |

## [◆ ](#a4cdd8ded8a55c33f3b586152d64b2621)MSPM0\_PIN\_FUNCTION\_3

| #define MSPM0\_PIN\_FUNCTION\_3   (0x00000003) |
| --- |

## [◆ ](#a897c32ff405a8c4eeaaffed7a6c69d5a)MSPM0\_PIN\_FUNCTION\_4

| #define MSPM0\_PIN\_FUNCTION\_4   (0x00000004) |
| --- |

## [◆ ](#ab6ec2101ebc8d171852da5c72a9e6ff1)MSPM0\_PIN\_FUNCTION\_5

| #define MSPM0\_PIN\_FUNCTION\_5   (0x00000005) |
| --- |

## [◆ ](#a4891b06c78d726a4806ea7f8c18d2bbc)MSPM0\_PIN\_FUNCTION\_6

| #define MSPM0\_PIN\_FUNCTION\_6   (0x00000006) |
| --- |

## [◆ ](#af2b0ea70556adb258d70cbb7274dce12)MSPM0\_PIN\_FUNCTION\_7

| #define MSPM0\_PIN\_FUNCTION\_7   (0x00000007) |
| --- |

## [◆ ](#a250cc53f70b280ed5a909f5b968f2c0b)MSPM0\_PIN\_FUNCTION\_8

| #define MSPM0\_PIN\_FUNCTION\_8   (0x00000008) |
| --- |

## [◆ ](#affb9f84a279ac6ec00f153d024282b05)MSPM0\_PIN\_FUNCTION\_9

| #define MSPM0\_PIN\_FUNCTION\_9   (0x00000009) |
| --- |

## [◆ ](#aed042e160fbf0499081e08f32b485ccc)MSPM0\_PIN\_FUNCTION\_ANALOG

| #define MSPM0\_PIN\_FUNCTION\_ANALOG   (0x00000000) |
| --- |

## [◆ ](#aafceb12e339618d1282aa7300507d9a5)MSPM0\_PIN\_FUNCTION\_GPIO

| #define MSPM0\_PIN\_FUNCTION\_GPIO   (0x00000001) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [mspm0-pinctrl.h](mspm0-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
