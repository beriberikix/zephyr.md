---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/stm32f1-pinctrl_8h.html
original_path: doxygen/html/stm32f1-pinctrl_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32f1-pinctrl.h File Reference

`#include <[zephyr/dt-bindings/pinctrl/stm32-pinctrl-common.h](stm32-pinctrl-common_8h_source.md)>`  
`#include <[zephyr/dt-bindings/pinctrl/stm32f1-afio.h](stm32f1-afio_8h_source.md)>`

[Go to the source code of this file.](stm32f1-pinctrl_8h_source.md)

| Macros | |
| --- | --- |
| #define | [STM32\_MODE\_SHIFT](#a1b9d630e0c184195bfece6550ae74870)   0U |
|  | Macro to generate pinmux int using port, pin number and mode arguments This is adapted from Linux equivalent st,stm32f429-pinctrl binding. |
| #define | [STM32\_MODE\_MASK](#a12472016d6448c797707d2d062d6011d)   0x3U |
| #define | [STM32\_LINE\_SHIFT](#a608cb76ac837e5b0b8ebbbc982ac1dc6)   2U |
| #define | [STM32\_LINE\_MASK](#a51d75677040be2ea1204ab667fd1d6f6)   0xFU |
| #define | [STM32\_PORT\_SHIFT](#a0fa09fe492147c76a6b2f191e39d3b9f)   6U |
| #define | [STM32\_PORT\_MASK](#ad7a035f83320bdf867b030bb0dac5221)   0xFU |
| #define | [STM32\_REMAP\_SHIFT](#ac805a8539bc58646fde819b259510f3c)   10U |
| #define | [STM32\_REMAP\_MASK](#a195e89eb01366f50937857a014a8c780)   0x3FFU |
| #define | [STM32F1\_PINMUX](#a66ff36e6fb75c1ebef645f7f8d89ace5)(port, line, mode, remap) |
|  | Pin configuration configuration bit field. |
| #define | [ALTERNATE](#ac7190c598c8618207180d135c0650dac)   0x0 /\* Alternate function output \*/ |
|  | Pin modes. |
| #define | [GPIO\_IN](#aa253a7f9c099890d2575f29dda32f154)   0x1 /\* Input \*/ |
| #define | [ANALOG](#ad42aa2404559d4a465d5d45e857f2881)   0x2 /\* Analog \*/ |
| #define | [GPIO\_OUT](#aa0d5e0e1b44c5015f31a44079fd2d9e6)   0x3 /\* Output \*/ |
| #define | [STM32\_MODE\_INPUT](#aa9844618e3818188246a2f0e63f912b6)   (0x0 << [STM32\_MODE\_INOUT\_SHIFT](#a0b6a084d6449a66092f2917fe97df807)) |
|  | PIN configuration bitfield. |
| #define | [STM32\_MODE\_OUTPUT](#acf96fd2b20693c4ca01c4a2ed63868fc)   (0x1 << [STM32\_MODE\_INOUT\_SHIFT](#a0b6a084d6449a66092f2917fe97df807)) |
| #define | [STM32\_MODE\_INOUT\_MASK](#a841c95812b5a687b1ff31f2d47400619)   0x1 |
| #define | [STM32\_MODE\_INOUT\_SHIFT](#a0b6a084d6449a66092f2917fe97df807)   0 |
| #define | [STM32\_CNF\_IN\_ANALOG](#a856018b58252b011a09e497476537792)   (0x0 << [STM32\_CNF\_IN\_SHIFT](#ab02cc6e05b7f86fe5751b4997090cf32)) |
| #define | [STM32\_CNF\_IN\_FLOAT](#a7c00df479b30101b86ac3b10edee754a)   (0x1 << [STM32\_CNF\_IN\_SHIFT](#ab02cc6e05b7f86fe5751b4997090cf32)) |
| #define | [STM32\_CNF\_IN\_PUPD](#ab7cd39547fa5551446d18f8177be0817)   (0x2 << [STM32\_CNF\_IN\_SHIFT](#ab02cc6e05b7f86fe5751b4997090cf32)) |
| #define | [STM32\_CNF\_IN\_MASK](#ad3a214e677771609666090119836b681)   0x3 |
| #define | [STM32\_CNF\_IN\_SHIFT](#ab02cc6e05b7f86fe5751b4997090cf32)   1 |
| #define | [STM32\_MODE\_OUTPUT\_MAX\_10](#a3785ba0db5f78b533cc6edf70f130d89)   (0x0 << [STM32\_MODE\_OSPEED\_SHIFT](#a8222a953484ca865a95621b67b477dff)) |
| #define | [STM32\_MODE\_OUTPUT\_MAX\_2](#aa785e1cfc212b7d6eee9b4c651f21fde)   (0x1 << [STM32\_MODE\_OSPEED\_SHIFT](#a8222a953484ca865a95621b67b477dff)) |
| #define | [STM32\_MODE\_OUTPUT\_MAX\_50](#a859c5c65cb08906b2e32cf5a913f2676)   (0x2 << [STM32\_MODE\_OSPEED\_SHIFT](#a8222a953484ca865a95621b67b477dff)) |
| #define | [STM32\_MODE\_OSPEED\_MASK](#af2eb3a3d0357ac7feaf6568e451e3a66)   0x3 |
| #define | [STM32\_MODE\_OSPEED\_SHIFT](#a8222a953484ca865a95621b67b477dff)   3 |
| #define | [STM32\_CNF\_PUSH\_PULL](#a31a0e44e3786b4964a378e40ac7e3039)   (0x0 << [STM32\_CNF\_OUT\_0\_SHIFT](#a0caefc9c2aac184c27fbc5bcd58c6507)) |
| #define | [STM32\_CNF\_OPEN\_DRAIN](#a93420385c3de44310b8afe9662c42b5f)   (0x1 << [STM32\_CNF\_OUT\_0\_SHIFT](#a0caefc9c2aac184c27fbc5bcd58c6507)) |
| #define | [STM32\_CNF\_OUT\_0\_MASK](#afbeddc9889f338ff54255b7790f8e3c2)   0x1 |
| #define | [STM32\_CNF\_OUT\_0\_SHIFT](#a0caefc9c2aac184c27fbc5bcd58c6507)   5 |
| #define | [STM32\_CNF\_GP\_OUTPUT](#a44801ba78bae673cb7ff40582065e307)   (0x0 << [STM32\_CNF\_OUT\_1\_SHIFT](#a3ae3d43708c37131013dfff3ad6dac65)) |
| #define | [STM32\_CNF\_ALT\_FUNC](#a8f9dee20ce6a566b1b513775be332557)   (0x1 << [STM32\_CNF\_OUT\_1\_SHIFT](#a3ae3d43708c37131013dfff3ad6dac65)) |
| #define | [STM32\_CNF\_OUT\_1\_MASK](#ae622832d07c96d971b2b19ee31d015d9)   0x1 |
| #define | [STM32\_CNF\_OUT\_1\_SHIFT](#a3ae3d43708c37131013dfff3ad6dac65)   6 |
| #define | [STM32\_PUPD\_NO\_PULL](#a63de2d9375292f21b01416a00ceae2e6)   (0x0 << [STM32\_PUPD\_SHIFT](#a66c8da0f11600f1e52df10c8a60816a4)) |
| #define | [STM32\_PUPD\_PULL\_UP](#a6b957a3e51de3ab1240683716ee4070a)   (0x1 << [STM32\_PUPD\_SHIFT](#a66c8da0f11600f1e52df10c8a60816a4)) |
| #define | [STM32\_PUPD\_PULL\_DOWN](#aec7ac04636b53a680170c34048ec4ede)   (0x2 << [STM32\_PUPD\_SHIFT](#a66c8da0f11600f1e52df10c8a60816a4)) |
| #define | [STM32\_PUPD\_MASK](#a64d43e1964d6ac8138030e5aace05b9a)   0x3 |
| #define | [STM32\_PUPD\_SHIFT](#a66c8da0f11600f1e52df10c8a60816a4)   7 |
| #define | [STM32\_ODR\_0](#a48ba1ca7035db7a74e9a79ea4ec7e3a5)   (0x0 << [STM32\_ODR\_SHIFT](#a6ae722db87e6732c90c96dd85d5424b3)) |
| #define | [STM32\_ODR\_1](#ab705ff660828b74fe36bdb6584db4467)   (0x1 << [STM32\_ODR\_SHIFT](#a6ae722db87e6732c90c96dd85d5424b3)) |
| #define | [STM32\_ODR\_MASK](#a2228a72e108e811ee0f31092fa6f9dd9)   0x1 |
| #define | [STM32\_ODR\_SHIFT](#a6ae722db87e6732c90c96dd85d5424b3)   9 |

## Macro Definition Documentation

## [◆ ](#ac7190c598c8618207180d135c0650dac)ALTERNATE

| #define ALTERNATE   0x0 /\* Alternate function output \*/ |
| --- |

Pin modes.

## [◆ ](#ad42aa2404559d4a465d5d45e857f2881)ANALOG

| #define ANALOG   0x2 /\* Analog \*/ |
| --- |

## [◆ ](#aa253a7f9c099890d2575f29dda32f154)GPIO\_IN

| #define GPIO\_IN   0x1 /\* Input \*/ |
| --- |

## [◆ ](#aa0d5e0e1b44c5015f31a44079fd2d9e6)GPIO\_OUT

| #define GPIO\_OUT   0x3 /\* Output \*/ |
| --- |

## [◆ ](#a8f9dee20ce6a566b1b513775be332557)STM32\_CNF\_ALT\_FUNC

| #define STM32\_CNF\_ALT\_FUNC   (0x1 << [STM32\_CNF\_OUT\_1\_SHIFT](#a3ae3d43708c37131013dfff3ad6dac65)) |
| --- |

## [◆ ](#a44801ba78bae673cb7ff40582065e307)STM32\_CNF\_GP\_OUTPUT

| #define STM32\_CNF\_GP\_OUTPUT   (0x0 << [STM32\_CNF\_OUT\_1\_SHIFT](#a3ae3d43708c37131013dfff3ad6dac65)) |
| --- |

## [◆ ](#a856018b58252b011a09e497476537792)STM32\_CNF\_IN\_ANALOG

| #define STM32\_CNF\_IN\_ANALOG   (0x0 << [STM32\_CNF\_IN\_SHIFT](#ab02cc6e05b7f86fe5751b4997090cf32)) |
| --- |

## [◆ ](#a7c00df479b30101b86ac3b10edee754a)STM32\_CNF\_IN\_FLOAT

| #define STM32\_CNF\_IN\_FLOAT   (0x1 << [STM32\_CNF\_IN\_SHIFT](#ab02cc6e05b7f86fe5751b4997090cf32)) |
| --- |

## [◆ ](#ad3a214e677771609666090119836b681)STM32\_CNF\_IN\_MASK

| #define STM32\_CNF\_IN\_MASK   0x3 |
| --- |

## [◆ ](#ab7cd39547fa5551446d18f8177be0817)STM32\_CNF\_IN\_PUPD

| #define STM32\_CNF\_IN\_PUPD   (0x2 << [STM32\_CNF\_IN\_SHIFT](#ab02cc6e05b7f86fe5751b4997090cf32)) |
| --- |

## [◆ ](#ab02cc6e05b7f86fe5751b4997090cf32)STM32\_CNF\_IN\_SHIFT

| #define STM32\_CNF\_IN\_SHIFT   1 |
| --- |

## [◆ ](#a93420385c3de44310b8afe9662c42b5f)STM32\_CNF\_OPEN\_DRAIN

| #define STM32\_CNF\_OPEN\_DRAIN   (0x1 << [STM32\_CNF\_OUT\_0\_SHIFT](#a0caefc9c2aac184c27fbc5bcd58c6507)) |
| --- |

## [◆ ](#afbeddc9889f338ff54255b7790f8e3c2)STM32\_CNF\_OUT\_0\_MASK

| #define STM32\_CNF\_OUT\_0\_MASK   0x1 |
| --- |

## [◆ ](#a0caefc9c2aac184c27fbc5bcd58c6507)STM32\_CNF\_OUT\_0\_SHIFT

| #define STM32\_CNF\_OUT\_0\_SHIFT   5 |
| --- |

## [◆ ](#ae622832d07c96d971b2b19ee31d015d9)STM32\_CNF\_OUT\_1\_MASK

| #define STM32\_CNF\_OUT\_1\_MASK   0x1 |
| --- |

## [◆ ](#a3ae3d43708c37131013dfff3ad6dac65)STM32\_CNF\_OUT\_1\_SHIFT

| #define STM32\_CNF\_OUT\_1\_SHIFT   6 |
| --- |

## [◆ ](#a31a0e44e3786b4964a378e40ac7e3039)STM32\_CNF\_PUSH\_PULL

| #define STM32\_CNF\_PUSH\_PULL   (0x0 << [STM32\_CNF\_OUT\_0\_SHIFT](#a0caefc9c2aac184c27fbc5bcd58c6507)) |
| --- |

## [◆ ](#a51d75677040be2ea1204ab667fd1d6f6)STM32\_LINE\_MASK

| #define STM32\_LINE\_MASK   0xFU |
| --- |

## [◆ ](#a608cb76ac837e5b0b8ebbbc982ac1dc6)STM32\_LINE\_SHIFT

| #define STM32\_LINE\_SHIFT   2U |
| --- |

## [◆ ](#a841c95812b5a687b1ff31f2d47400619)STM32\_MODE\_INOUT\_MASK

| #define STM32\_MODE\_INOUT\_MASK   0x1 |
| --- |

## [◆ ](#a0b6a084d6449a66092f2917fe97df807)STM32\_MODE\_INOUT\_SHIFT

| #define STM32\_MODE\_INOUT\_SHIFT   0 |
| --- |

## [◆ ](#aa9844618e3818188246a2f0e63f912b6)STM32\_MODE\_INPUT

| #define STM32\_MODE\_INPUT   (0x0 << [STM32\_MODE\_INOUT\_SHIFT](#a0b6a084d6449a66092f2917fe97df807)) |
| --- |

PIN configuration bitfield.

Pin configuration is coded with the following fields GPIO I/O Mode [ 0 ] GPIO Input config [ 1 : 2 ] GPIO Output speed [ 3 : 4 ] GPIO Output PP/OD [ 5 ] GPIO Output AF/GP [ 6 ] GPIO PUPD Config [ 7 : 8 ] GPIO ODR [ 9 ]

Applicable to STM32F1 series

## [◆ ](#a12472016d6448c797707d2d062d6011d)STM32\_MODE\_MASK

| #define STM32\_MODE\_MASK   0x3U |
| --- |

## [◆ ](#af2eb3a3d0357ac7feaf6568e451e3a66)STM32\_MODE\_OSPEED\_MASK

| #define STM32\_MODE\_OSPEED\_MASK   0x3 |
| --- |

## [◆ ](#a8222a953484ca865a95621b67b477dff)STM32\_MODE\_OSPEED\_SHIFT

| #define STM32\_MODE\_OSPEED\_SHIFT   3 |
| --- |

## [◆ ](#acf96fd2b20693c4ca01c4a2ed63868fc)STM32\_MODE\_OUTPUT

| #define STM32\_MODE\_OUTPUT   (0x1 << [STM32\_MODE\_INOUT\_SHIFT](#a0b6a084d6449a66092f2917fe97df807)) |
| --- |

## [◆ ](#a3785ba0db5f78b533cc6edf70f130d89)STM32\_MODE\_OUTPUT\_MAX\_10

| #define STM32\_MODE\_OUTPUT\_MAX\_10   (0x0 << [STM32\_MODE\_OSPEED\_SHIFT](#a8222a953484ca865a95621b67b477dff)) |
| --- |

## [◆ ](#aa785e1cfc212b7d6eee9b4c651f21fde)STM32\_MODE\_OUTPUT\_MAX\_2

| #define STM32\_MODE\_OUTPUT\_MAX\_2   (0x1 << [STM32\_MODE\_OSPEED\_SHIFT](#a8222a953484ca865a95621b67b477dff)) |
| --- |

## [◆ ](#a859c5c65cb08906b2e32cf5a913f2676)STM32\_MODE\_OUTPUT\_MAX\_50

| #define STM32\_MODE\_OUTPUT\_MAX\_50   (0x2 << [STM32\_MODE\_OSPEED\_SHIFT](#a8222a953484ca865a95621b67b477dff)) |
| --- |

## [◆ ](#a1b9d630e0c184195bfece6550ae74870)STM32\_MODE\_SHIFT

| #define STM32\_MODE\_SHIFT   0U |
| --- |

Macro to generate pinmux int using port, pin number and mode arguments This is adapted from Linux equivalent st,stm32f429-pinctrl binding.

## [◆ ](#a48ba1ca7035db7a74e9a79ea4ec7e3a5)STM32\_ODR\_0

| #define STM32\_ODR\_0   (0x0 << [STM32\_ODR\_SHIFT](#a6ae722db87e6732c90c96dd85d5424b3)) |
| --- |

## [◆ ](#ab705ff660828b74fe36bdb6584db4467)STM32\_ODR\_1

| #define STM32\_ODR\_1   (0x1 << [STM32\_ODR\_SHIFT](#a6ae722db87e6732c90c96dd85d5424b3)) |
| --- |

## [◆ ](#a2228a72e108e811ee0f31092fa6f9dd9)STM32\_ODR\_MASK

| #define STM32\_ODR\_MASK   0x1 |
| --- |

## [◆ ](#a6ae722db87e6732c90c96dd85d5424b3)STM32\_ODR\_SHIFT

| #define STM32\_ODR\_SHIFT   9 |
| --- |

## [◆ ](#ad7a035f83320bdf867b030bb0dac5221)STM32\_PORT\_MASK

| #define STM32\_PORT\_MASK   0xFU |
| --- |

## [◆ ](#a0fa09fe492147c76a6b2f191e39d3b9f)STM32\_PORT\_SHIFT

| #define STM32\_PORT\_SHIFT   6U |
| --- |

## [◆ ](#a64d43e1964d6ac8138030e5aace05b9a)STM32\_PUPD\_MASK

| #define STM32\_PUPD\_MASK   0x3 |
| --- |

## [◆ ](#a63de2d9375292f21b01416a00ceae2e6)STM32\_PUPD\_NO\_PULL

| #define STM32\_PUPD\_NO\_PULL   (0x0 << [STM32\_PUPD\_SHIFT](#a66c8da0f11600f1e52df10c8a60816a4)) |
| --- |

## [◆ ](#aec7ac04636b53a680170c34048ec4ede)STM32\_PUPD\_PULL\_DOWN

| #define STM32\_PUPD\_PULL\_DOWN   (0x2 << [STM32\_PUPD\_SHIFT](#a66c8da0f11600f1e52df10c8a60816a4)) |
| --- |

## [◆ ](#a6b957a3e51de3ab1240683716ee4070a)STM32\_PUPD\_PULL\_UP

| #define STM32\_PUPD\_PULL\_UP   (0x1 << [STM32\_PUPD\_SHIFT](#a66c8da0f11600f1e52df10c8a60816a4)) |
| --- |

## [◆ ](#a66c8da0f11600f1e52df10c8a60816a4)STM32\_PUPD\_SHIFT

| #define STM32\_PUPD\_SHIFT   7 |
| --- |

## [◆ ](#a195e89eb01366f50937857a014a8c780)STM32\_REMAP\_MASK

| #define STM32\_REMAP\_MASK   0x3FFU |
| --- |

## [◆ ](#ac805a8539bc58646fde819b259510f3c)STM32\_REMAP\_SHIFT

| #define STM32\_REMAP\_SHIFT   10U |
| --- |

## [◆ ](#a66ff36e6fb75c1ebef645f7f8d89ace5)STM32F1\_PINMUX

| #define STM32F1\_PINMUX | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *line*, |
|  |  |  | *mode*, |
|  |  |  | *remap* ) |

**Value:**

(((((port) - 'A') & [STM32\_PORT\_MASK](stm32-pinctrl_8h.md#ad7a035f83320bdf867b030bb0dac5221)) << [STM32\_PORT\_SHIFT](stm32-pinctrl_8h.md#a0fa09fe492147c76a6b2f191e39d3b9f)) | \

(((line) & [STM32\_LINE\_MASK](stm32-pinctrl_8h.md#a51d75677040be2ea1204ab667fd1d6f6)) << [STM32\_LINE\_SHIFT](stm32-pinctrl_8h.md#a608cb76ac837e5b0b8ebbbc982ac1dc6)) | \

(((mode) & [STM32\_MODE\_MASK](stm32-pinctrl_8h.md#a12472016d6448c797707d2d062d6011d)) << [STM32\_MODE\_SHIFT](stm32-pinctrl_8h.md#a1b9d630e0c184195bfece6550ae74870)) | \

(((remap) & [STM32\_REMAP\_MASK](#a195e89eb01366f50937857a014a8c780)) << [STM32\_REMAP\_SHIFT](#ac805a8539bc58646fde819b259510f3c)))

[STM32\_PORT\_SHIFT](stm32-pinctrl_8h.md#a0fa09fe492147c76a6b2f191e39d3b9f)

#define STM32\_PORT\_SHIFT

**Definition** stm32-pinctrl.h:46

[STM32\_MODE\_MASK](stm32-pinctrl_8h.md#a12472016d6448c797707d2d062d6011d)

#define STM32\_MODE\_MASK

**Definition** stm32-pinctrl.h:43

[STM32\_MODE\_SHIFT](stm32-pinctrl_8h.md#a1b9d630e0c184195bfece6550ae74870)

#define STM32\_MODE\_SHIFT

Macro to generate pinmux int using port, pin number and mode arguments This is inspired from Linux eq...

**Definition** stm32-pinctrl.h:42

[STM32\_LINE\_MASK](stm32-pinctrl_8h.md#a51d75677040be2ea1204ab667fd1d6f6)

#define STM32\_LINE\_MASK

**Definition** stm32-pinctrl.h:45

[STM32\_LINE\_SHIFT](stm32-pinctrl_8h.md#a608cb76ac837e5b0b8ebbbc982ac1dc6)

#define STM32\_LINE\_SHIFT

**Definition** stm32-pinctrl.h:44

[STM32\_PORT\_MASK](stm32-pinctrl_8h.md#ad7a035f83320bdf867b030bb0dac5221)

#define STM32\_PORT\_MASK

**Definition** stm32-pinctrl.h:47

[STM32\_REMAP\_MASK](#a195e89eb01366f50937857a014a8c780)

#define STM32\_REMAP\_MASK

**Definition** stm32f1-pinctrl.h:27

[STM32\_REMAP\_SHIFT](#ac805a8539bc58646fde819b259510f3c)

#define STM32\_REMAP\_SHIFT

**Definition** stm32f1-pinctrl.h:26

Pin configuration configuration bit field.

Fields:

- mode [ 0 : 1 ]
- line [ 2 : 5 ]
- port [ 6 : 9 ]
- remap [ 10 : 19 ]

Parameters
:   | port | Port ('A'..'K') |
    | --- | --- |
    | line | Pin (0..15) |
    | mode | Pin mode (ANALOG, GPIO\_IN, ALTERNATE). |
    | remap | Pin remapping configuration (NO\_REMAP, REMAP\_1, ...) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [stm32f1-pinctrl.h](stm32f1-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
