---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/stm32-pinctrl_8h.html
original_path: doxygen/html/stm32-pinctrl_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stm32-pinctrl.h File Reference

`#include <[zephyr/dt-bindings/pinctrl/stm32-pinctrl-common.h](stm32-pinctrl-common_8h_source.md)>`

[Go to the source code of this file.](stm32-pinctrl_8h_source.md)

| Macros | |
| --- | --- |
| #define | [STM32\_AF0](#a856e7793927d195e31a0ab801d9320b1)   0x0 |
|  | Pin modes. |
| #define | [STM32\_AF1](#ac341ff4da52832f09596ddb8f66d0704)   0x1 |
| #define | [STM32\_AF2](#af6aa5ae98ba243f120737e8b0ad6644c)   0x2 |
| #define | [STM32\_AF3](#a3d65bb83c9f0515e218f300171a90b75)   0x3 |
| #define | [STM32\_AF4](#a286f6ec684e9c7297261f9ed7372e609)   0x4 |
| #define | [STM32\_AF5](#a9a48f460272ef966b8dd2ead78c8e8e9)   0x5 |
| #define | [STM32\_AF6](#a5c5b864b9d9d1431a8d905967cae69a4)   0x6 |
| #define | [STM32\_AF7](#ade35007347e4f04e0e7f2e4f87a4dec3)   0x7 |
| #define | [STM32\_AF8](#aef1775a7a3af9daed7d72c123db23f08)   0x8 |
| #define | [STM32\_AF9](#adeb65582e22de51dd619bfd7c49a0653)   0x9 |
| #define | [STM32\_AF10](#ad8732007cc06358d29379d025203df15)   0xa |
| #define | [STM32\_AF11](#ab7bb316e4f29094d7d7a8b08522eec69)   0xb |
| #define | [STM32\_AF12](#aaf99ab7b7abc0f5b211afba7dbc75dff)   0xc |
| #define | [STM32\_AF13](#a84a34bd261316ab1353d45bbd03437a5)   0xd |
| #define | [STM32\_AF14](#a5bc95c95792938f333095422499de8e6)   0xe |
| #define | [STM32\_AF15](#a2a2f2b85e7e92f1a7a7baa69ed8c4655)   0xf |
| #define | [STM32\_ANALOG](#a3cef198576d1117a64e34d3981ae69d2)   0x10 |
| #define | [STM32\_GPIO](#a6b8fe886fca3bab7d631a90cdfca6a0f)   0x11 |
| #define | [STM32\_MODE\_SHIFT](#a1b9d630e0c184195bfece6550ae74870)   0U |
|  | Macro to generate pinmux int using port, pin number and mode arguments This is inspired from Linux equivalent st,stm32f429-pinctrl binding. |
| #define | [STM32\_MODE\_MASK](#a12472016d6448c797707d2d062d6011d)   0x1FU |
| #define | [STM32\_LINE\_SHIFT](#a608cb76ac837e5b0b8ebbbc982ac1dc6)   5U |
| #define | [STM32\_LINE\_MASK](#a51d75677040be2ea1204ab667fd1d6f6)   0xFU |
| #define | [STM32\_PORT\_SHIFT](#a0fa09fe492147c76a6b2f191e39d3b9f)   9U |
| #define | [STM32\_PORT\_MASK](#ad7a035f83320bdf867b030bb0dac5221)   0x1FU |
| #define | [STM32\_PINMUX](#a0a29e4e3ef1b1e901bf203640bc84dd9)(port, line, mode) |
|  | Pin configuration configuration bit field. |
| #define | [STM32\_MODER\_INPUT\_MODE](#a90a61faade25953a971ea39959200da8)   (0x0 << [STM32\_MODER\_SHIFT](#a7384d84f720e2660ae4d8e1b7fa2d280)) |
|  | PIN configuration bitfield. |
| #define | [STM32\_MODER\_OUTPUT\_MODE](#af0c2579f30fd0c4c9908fa5d76a55aa5)   (0x1 << [STM32\_MODER\_SHIFT](#a7384d84f720e2660ae4d8e1b7fa2d280)) |
| #define | [STM32\_MODER\_ALT\_MODE](#a26d39411b37f40082178a0fe7a3b135f)   (0x2 << [STM32\_MODER\_SHIFT](#a7384d84f720e2660ae4d8e1b7fa2d280)) |
| #define | [STM32\_MODER\_ANALOG\_MODE](#a4507703ea2b3399214ff460fcd78cb91)   (0x3 << [STM32\_MODER\_SHIFT](#a7384d84f720e2660ae4d8e1b7fa2d280)) |
| #define | [STM32\_MODER\_MASK](#aa5f2e2e47c7915df1f36ce5bb3214a8e)   0x3 |
| #define | [STM32\_MODER\_SHIFT](#a7384d84f720e2660ae4d8e1b7fa2d280)   4 |
| #define | [STM32\_OTYPER\_PUSH\_PULL](#a1c2241544c16a546dd7716f9e1c79f4f)   (0x0 << [STM32\_OTYPER\_SHIFT](#a9f4ba8355e6794e8ea92387b3d07fe53)) |
| #define | [STM32\_OTYPER\_OPEN\_DRAIN](#a202967dcb384d745131708a5ff33f857)   (0x1 << [STM32\_OTYPER\_SHIFT](#a9f4ba8355e6794e8ea92387b3d07fe53)) |
| #define | [STM32\_OTYPER\_MASK](#a54ef12cf7862967900cd66bab6fbafb0)   0x1 |
| #define | [STM32\_OTYPER\_SHIFT](#a9f4ba8355e6794e8ea92387b3d07fe53)   6 |
| #define | [STM32\_OSPEEDR\_LOW\_SPEED](#a5297c898e88bb795d379b7d6179a2c77)   (0x0 << [STM32\_OSPEEDR\_SHIFT](#abbe5962daa9f7aaffc63ed5b28cca34c)) |
| #define | [STM32\_OSPEEDR\_MEDIUM\_SPEED](#a0f99d4fd8cb8821346caed2e8f4fbc8d)   (0x1 << [STM32\_OSPEEDR\_SHIFT](#abbe5962daa9f7aaffc63ed5b28cca34c)) |
| #define | [STM32\_OSPEEDR\_HIGH\_SPEED](#a1b9a5be0e0ea97b03f4b88c8dc11599c)   (0x2 << [STM32\_OSPEEDR\_SHIFT](#abbe5962daa9f7aaffc63ed5b28cca34c)) |
| #define | [STM32\_OSPEEDR\_VERY\_HIGH\_SPEED](#a51b0180d689496d60874b0a153d876fb)   (0x3 << [STM32\_OSPEEDR\_SHIFT](#abbe5962daa9f7aaffc63ed5b28cca34c)) |
| #define | [STM32\_OSPEEDR\_MASK](#a0e0319c5fc5b03907eecc9ac932a60a5)   0x3 |
| #define | [STM32\_OSPEEDR\_SHIFT](#abbe5962daa9f7aaffc63ed5b28cca34c)   7 |
| #define | [STM32\_PUPDR\_NO\_PULL](#ae597a50176d61956806f1d9ae5b66d6b)   (0x0 << [STM32\_PUPDR\_SHIFT](#a21164826201e6cdd17a59f2405f82208)) |
| #define | [STM32\_PUPDR\_PULL\_UP](#a5f5cf4b1701e7fbd3c4e50ea3d7717ed)   (0x1 << [STM32\_PUPDR\_SHIFT](#a21164826201e6cdd17a59f2405f82208)) |
| #define | [STM32\_PUPDR\_PULL\_DOWN](#a941f508cbf744960077d072b59118df8)   (0x2 << [STM32\_PUPDR\_SHIFT](#a21164826201e6cdd17a59f2405f82208)) |
| #define | [STM32\_PUPDR\_MASK](#a7d5d3673847fcb1680ea6c8ce1e58fa7)   0x3 |
| #define | [STM32\_PUPDR\_SHIFT](#a21164826201e6cdd17a59f2405f82208)   9 |
| #define | [STM32\_ODR\_0](#a48ba1ca7035db7a74e9a79ea4ec7e3a5)   (0x0 << [STM32\_ODR\_SHIFT](#a6ae722db87e6732c90c96dd85d5424b3)) |
| #define | [STM32\_ODR\_1](#ab705ff660828b74fe36bdb6584db4467)   (0x1 << [STM32\_ODR\_SHIFT](#a6ae722db87e6732c90c96dd85d5424b3)) |
| #define | [STM32\_ODR\_MASK](#a2228a72e108e811ee0f31092fa6f9dd9)   0x1 |
| #define | [STM32\_ODR\_SHIFT](#a6ae722db87e6732c90c96dd85d5424b3)   11 |

## Macro Definition Documentation

## [◆ ](#a856e7793927d195e31a0ab801d9320b1)STM32\_AF0

| #define STM32\_AF0   0x0 |
| --- |

Pin modes.

## [◆ ](#ac341ff4da52832f09596ddb8f66d0704)STM32\_AF1

| #define STM32\_AF1   0x1 |
| --- |

## [◆ ](#ad8732007cc06358d29379d025203df15)STM32\_AF10

| #define STM32\_AF10   0xa |
| --- |

## [◆ ](#ab7bb316e4f29094d7d7a8b08522eec69)STM32\_AF11

| #define STM32\_AF11   0xb |
| --- |

## [◆ ](#aaf99ab7b7abc0f5b211afba7dbc75dff)STM32\_AF12

| #define STM32\_AF12   0xc |
| --- |

## [◆ ](#a84a34bd261316ab1353d45bbd03437a5)STM32\_AF13

| #define STM32\_AF13   0xd |
| --- |

## [◆ ](#a5bc95c95792938f333095422499de8e6)STM32\_AF14

| #define STM32\_AF14   0xe |
| --- |

## [◆ ](#a2a2f2b85e7e92f1a7a7baa69ed8c4655)STM32\_AF15

| #define STM32\_AF15   0xf |
| --- |

## [◆ ](#af6aa5ae98ba243f120737e8b0ad6644c)STM32\_AF2

| #define STM32\_AF2   0x2 |
| --- |

## [◆ ](#a3d65bb83c9f0515e218f300171a90b75)STM32\_AF3

| #define STM32\_AF3   0x3 |
| --- |

## [◆ ](#a286f6ec684e9c7297261f9ed7372e609)STM32\_AF4

| #define STM32\_AF4   0x4 |
| --- |

## [◆ ](#a9a48f460272ef966b8dd2ead78c8e8e9)STM32\_AF5

| #define STM32\_AF5   0x5 |
| --- |

## [◆ ](#a5c5b864b9d9d1431a8d905967cae69a4)STM32\_AF6

| #define STM32\_AF6   0x6 |
| --- |

## [◆ ](#ade35007347e4f04e0e7f2e4f87a4dec3)STM32\_AF7

| #define STM32\_AF7   0x7 |
| --- |

## [◆ ](#aef1775a7a3af9daed7d72c123db23f08)STM32\_AF8

| #define STM32\_AF8   0x8 |
| --- |

## [◆ ](#adeb65582e22de51dd619bfd7c49a0653)STM32\_AF9

| #define STM32\_AF9   0x9 |
| --- |

## [◆ ](#a3cef198576d1117a64e34d3981ae69d2)STM32\_ANALOG

| #define STM32\_ANALOG   0x10 |
| --- |

## [◆ ](#a6b8fe886fca3bab7d631a90cdfca6a0f)STM32\_GPIO

| #define STM32\_GPIO   0x11 |
| --- |

## [◆ ](#a51d75677040be2ea1204ab667fd1d6f6)STM32\_LINE\_MASK

| #define STM32\_LINE\_MASK   0xFU |
| --- |

## [◆ ](#a608cb76ac837e5b0b8ebbbc982ac1dc6)STM32\_LINE\_SHIFT

| #define STM32\_LINE\_SHIFT   5U |
| --- |

## [◆ ](#a12472016d6448c797707d2d062d6011d)STM32\_MODE\_MASK

| #define STM32\_MODE\_MASK   0x1FU |
| --- |

## [◆ ](#a1b9d630e0c184195bfece6550ae74870)STM32\_MODE\_SHIFT

| #define STM32\_MODE\_SHIFT   0U |
| --- |

Macro to generate pinmux int using port, pin number and mode arguments This is inspired from Linux equivalent st,stm32f429-pinctrl binding.

## [◆ ](#a26d39411b37f40082178a0fe7a3b135f)STM32\_MODER\_ALT\_MODE

| #define STM32\_MODER\_ALT\_MODE   (0x2 << [STM32\_MODER\_SHIFT](#a7384d84f720e2660ae4d8e1b7fa2d280)) |
| --- |

## [◆ ](#a4507703ea2b3399214ff460fcd78cb91)STM32\_MODER\_ANALOG\_MODE

| #define STM32\_MODER\_ANALOG\_MODE   (0x3 << [STM32\_MODER\_SHIFT](#a7384d84f720e2660ae4d8e1b7fa2d280)) |
| --- |

## [◆ ](#a90a61faade25953a971ea39959200da8)STM32\_MODER\_INPUT\_MODE

| #define STM32\_MODER\_INPUT\_MODE   (0x0 << [STM32\_MODER\_SHIFT](#a7384d84f720e2660ae4d8e1b7fa2d280)) |
| --- |

PIN configuration bitfield.

Pin configuration is coded with the following fields Alternate Functions [ 0 : 3 ] GPIO Mode [ 4 : 5 ] GPIO Output type [ 6 ] GPIO Speed [ 7 : 8 ] GPIO PUPD config [ 9 : 10 ] GPIO Output data [ 11 ]

## [◆ ](#aa5f2e2e47c7915df1f36ce5bb3214a8e)STM32\_MODER\_MASK

| #define STM32\_MODER\_MASK   0x3 |
| --- |

## [◆ ](#af0c2579f30fd0c4c9908fa5d76a55aa5)STM32\_MODER\_OUTPUT\_MODE

| #define STM32\_MODER\_OUTPUT\_MODE   (0x1 << [STM32\_MODER\_SHIFT](#a7384d84f720e2660ae4d8e1b7fa2d280)) |
| --- |

## [◆ ](#a7384d84f720e2660ae4d8e1b7fa2d280)STM32\_MODER\_SHIFT

| #define STM32\_MODER\_SHIFT   4 |
| --- |

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

| #define STM32\_ODR\_SHIFT   11 |
| --- |

## [◆ ](#a1b9a5be0e0ea97b03f4b88c8dc11599c)STM32\_OSPEEDR\_HIGH\_SPEED

| #define STM32\_OSPEEDR\_HIGH\_SPEED   (0x2 << [STM32\_OSPEEDR\_SHIFT](#abbe5962daa9f7aaffc63ed5b28cca34c)) |
| --- |

## [◆ ](#a5297c898e88bb795d379b7d6179a2c77)STM32\_OSPEEDR\_LOW\_SPEED

| #define STM32\_OSPEEDR\_LOW\_SPEED   (0x0 << [STM32\_OSPEEDR\_SHIFT](#abbe5962daa9f7aaffc63ed5b28cca34c)) |
| --- |

## [◆ ](#a0e0319c5fc5b03907eecc9ac932a60a5)STM32\_OSPEEDR\_MASK

| #define STM32\_OSPEEDR\_MASK   0x3 |
| --- |

## [◆ ](#a0f99d4fd8cb8821346caed2e8f4fbc8d)STM32\_OSPEEDR\_MEDIUM\_SPEED

| #define STM32\_OSPEEDR\_MEDIUM\_SPEED   (0x1 << [STM32\_OSPEEDR\_SHIFT](#abbe5962daa9f7aaffc63ed5b28cca34c)) |
| --- |

## [◆ ](#abbe5962daa9f7aaffc63ed5b28cca34c)STM32\_OSPEEDR\_SHIFT

| #define STM32\_OSPEEDR\_SHIFT   7 |
| --- |

## [◆ ](#a51b0180d689496d60874b0a153d876fb)STM32\_OSPEEDR\_VERY\_HIGH\_SPEED

| #define STM32\_OSPEEDR\_VERY\_HIGH\_SPEED   (0x3 << [STM32\_OSPEEDR\_SHIFT](#abbe5962daa9f7aaffc63ed5b28cca34c)) |
| --- |

## [◆ ](#a54ef12cf7862967900cd66bab6fbafb0)STM32\_OTYPER\_MASK

| #define STM32\_OTYPER\_MASK   0x1 |
| --- |

## [◆ ](#a202967dcb384d745131708a5ff33f857)STM32\_OTYPER\_OPEN\_DRAIN

| #define STM32\_OTYPER\_OPEN\_DRAIN   (0x1 << [STM32\_OTYPER\_SHIFT](#a9f4ba8355e6794e8ea92387b3d07fe53)) |
| --- |

## [◆ ](#a1c2241544c16a546dd7716f9e1c79f4f)STM32\_OTYPER\_PUSH\_PULL

| #define STM32\_OTYPER\_PUSH\_PULL   (0x0 << [STM32\_OTYPER\_SHIFT](#a9f4ba8355e6794e8ea92387b3d07fe53)) |
| --- |

## [◆ ](#a9f4ba8355e6794e8ea92387b3d07fe53)STM32\_OTYPER\_SHIFT

| #define STM32\_OTYPER\_SHIFT   6 |
| --- |

## [◆ ](#a0a29e4e3ef1b1e901bf203640bc84dd9)STM32\_PINMUX

| #define STM32\_PINMUX | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *line*, |
|  |  |  | *mode* ) |

**Value:**

(((((port) - 'A') & [STM32\_PORT\_MASK](#ad7a035f83320bdf867b030bb0dac5221)) << [STM32\_PORT\_SHIFT](#a0fa09fe492147c76a6b2f191e39d3b9f)) | \

(((line) & [STM32\_LINE\_MASK](#a51d75677040be2ea1204ab667fd1d6f6)) << [STM32\_LINE\_SHIFT](#a608cb76ac837e5b0b8ebbbc982ac1dc6)) | \

(((STM32\_ ## mode) & [STM32\_MODE\_MASK](#a12472016d6448c797707d2d062d6011d)) << [STM32\_MODE\_SHIFT](#a1b9d630e0c184195bfece6550ae74870)))

[STM32\_PORT\_SHIFT](#a0fa09fe492147c76a6b2f191e39d3b9f)

#define STM32\_PORT\_SHIFT

**Definition** stm32-pinctrl.h:46

[STM32\_MODE\_MASK](#a12472016d6448c797707d2d062d6011d)

#define STM32\_MODE\_MASK

**Definition** stm32-pinctrl.h:43

[STM32\_MODE\_SHIFT](#a1b9d630e0c184195bfece6550ae74870)

#define STM32\_MODE\_SHIFT

Macro to generate pinmux int using port, pin number and mode arguments This is inspired from Linux eq...

**Definition** stm32-pinctrl.h:42

[STM32\_LINE\_MASK](#a51d75677040be2ea1204ab667fd1d6f6)

#define STM32\_LINE\_MASK

**Definition** stm32-pinctrl.h:45

[STM32\_LINE\_SHIFT](#a608cb76ac837e5b0b8ebbbc982ac1dc6)

#define STM32\_LINE\_SHIFT

**Definition** stm32-pinctrl.h:44

[STM32\_PORT\_MASK](#ad7a035f83320bdf867b030bb0dac5221)

#define STM32\_PORT\_MASK

**Definition** stm32-pinctrl.h:47

Pin configuration configuration bit field.

Fields:

- mode [ 0 : 4 ]
- line [ 5 : 8 ]
- port [ 9 : 13 ]

Parameters
:   | port | Port ('A'..'P') |
    | --- | --- |
    | line | Pin (0..15) |
    | mode | Mode (ANALOG, GPIO\_IN, ALTERNATE). |

## [◆ ](#ad7a035f83320bdf867b030bb0dac5221)STM32\_PORT\_MASK

| #define STM32\_PORT\_MASK   0x1FU |
| --- |

## [◆ ](#a0fa09fe492147c76a6b2f191e39d3b9f)STM32\_PORT\_SHIFT

| #define STM32\_PORT\_SHIFT   9U |
| --- |

## [◆ ](#a7d5d3673847fcb1680ea6c8ce1e58fa7)STM32\_PUPDR\_MASK

| #define STM32\_PUPDR\_MASK   0x3 |
| --- |

## [◆ ](#ae597a50176d61956806f1d9ae5b66d6b)STM32\_PUPDR\_NO\_PULL

| #define STM32\_PUPDR\_NO\_PULL   (0x0 << [STM32\_PUPDR\_SHIFT](#a21164826201e6cdd17a59f2405f82208)) |
| --- |

## [◆ ](#a941f508cbf744960077d072b59118df8)STM32\_PUPDR\_PULL\_DOWN

| #define STM32\_PUPDR\_PULL\_DOWN   (0x2 << [STM32\_PUPDR\_SHIFT](#a21164826201e6cdd17a59f2405f82208)) |
| --- |

## [◆ ](#a5f5cf4b1701e7fbd3c4e50ea3d7717ed)STM32\_PUPDR\_PULL\_UP

| #define STM32\_PUPDR\_PULL\_UP   (0x1 << [STM32\_PUPDR\_SHIFT](#a21164826201e6cdd17a59f2405f82208)) |
| --- |

## [◆ ](#a21164826201e6cdd17a59f2405f82208)STM32\_PUPDR\_SHIFT

| #define STM32\_PUPDR\_SHIFT   9 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [stm32-pinctrl.h](stm32-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
