---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/infineon-xmc4xxx-gpio_8h.html
original_path: doxygen/html/infineon-xmc4xxx-gpio_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

infineon-xmc4xxx-gpio.h File Reference

[Go to the source code of this file.](infineon-xmc4xxx-gpio_8h_source.md)

| Macros | |
| --- | --- |
| #define | [XMC4XXX\_GPIO\_DS\_POS](#a0204cbd6c151fcea59199b1c4e007eaf)   9 |
| #define | [XMC4XXX\_GPIO\_DS\_MASK](#a766a7c07cd178b9373fec28745b1e077)   0xf |
| #define | [XMC4XXX\_GPIO\_DS\_STRONG\_SHARP\_EDGE](#ab820bfc6577c45c88b59260531d078d3)   (0x1 << [XMC4XXX\_GPIO\_DS\_POS](#a0204cbd6c151fcea59199b1c4e007eaf)) |
| #define | [XMC4XXX\_GPIO\_DS\_STRONG\_MEDIUM\_EDGE](#a6a21bcff48f4e8a4acede963a534fb95)   (0x2 << [XMC4XXX\_GPIO\_DS\_POS](#a0204cbd6c151fcea59199b1c4e007eaf)) |
| #define | [XMC4XXX\_GPIO\_DS\_STRONG\_SOFT\_EDGE](#a07e14898ba2a322edf9729054832c1a9)   (0x3 << [XMC4XXX\_GPIO\_DS\_POS](#a0204cbd6c151fcea59199b1c4e007eaf)) |
| #define | [XMC4XXX\_GPIO\_DS\_STRONG\_SLOW\_EDGE](#aa81ddd8894b2f3a1e991b5d95ac81a7f)   (0x4 << [XMC4XXX\_GPIO\_DS\_POS](#a0204cbd6c151fcea59199b1c4e007eaf)) |
| #define | [XMC4XXX\_GPIO\_DS\_MEDIUM](#af725ddf9a1dfaf02d478cdcf94132a24)   (0x5 << [XMC4XXX\_GPIO\_DS\_POS](#a0204cbd6c151fcea59199b1c4e007eaf)) |
| #define | [XMC4XXX\_GPIO\_DS\_WEAK](#a5c307c3181d3094cadb68766b318b3e5)   (0x8 << [XMC4XXX\_GPIO\_DS\_POS](#a0204cbd6c151fcea59199b1c4e007eaf)) |
| #define | [XMC4XXX\_GPIO\_GET\_DS](#a52bb9df6ed1e4ead550ceefe1b96a5b3)([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |

## Macro Definition Documentation

## [◆ ](#a766a7c07cd178b9373fec28745b1e077)XMC4XXX\_GPIO\_DS\_MASK

| #define XMC4XXX\_GPIO\_DS\_MASK   0xf |
| --- |

## [◆ ](#af725ddf9a1dfaf02d478cdcf94132a24)XMC4XXX\_GPIO\_DS\_MEDIUM

| #define XMC4XXX\_GPIO\_DS\_MEDIUM   (0x5 << [XMC4XXX\_GPIO\_DS\_POS](#a0204cbd6c151fcea59199b1c4e007eaf)) |
| --- |

## [◆ ](#a0204cbd6c151fcea59199b1c4e007eaf)XMC4XXX\_GPIO\_DS\_POS

| #define XMC4XXX\_GPIO\_DS\_POS   9 |
| --- |

## [◆ ](#a6a21bcff48f4e8a4acede963a534fb95)XMC4XXX\_GPIO\_DS\_STRONG\_MEDIUM\_EDGE

| #define XMC4XXX\_GPIO\_DS\_STRONG\_MEDIUM\_EDGE   (0x2 << [XMC4XXX\_GPIO\_DS\_POS](#a0204cbd6c151fcea59199b1c4e007eaf)) |
| --- |

## [◆ ](#ab820bfc6577c45c88b59260531d078d3)XMC4XXX\_GPIO\_DS\_STRONG\_SHARP\_EDGE

| #define XMC4XXX\_GPIO\_DS\_STRONG\_SHARP\_EDGE   (0x1 << [XMC4XXX\_GPIO\_DS\_POS](#a0204cbd6c151fcea59199b1c4e007eaf)) |
| --- |

## [◆ ](#aa81ddd8894b2f3a1e991b5d95ac81a7f)XMC4XXX\_GPIO\_DS\_STRONG\_SLOW\_EDGE

| #define XMC4XXX\_GPIO\_DS\_STRONG\_SLOW\_EDGE   (0x4 << [XMC4XXX\_GPIO\_DS\_POS](#a0204cbd6c151fcea59199b1c4e007eaf)) |
| --- |

## [◆ ](#a07e14898ba2a322edf9729054832c1a9)XMC4XXX\_GPIO\_DS\_STRONG\_SOFT\_EDGE

| #define XMC4XXX\_GPIO\_DS\_STRONG\_SOFT\_EDGE   (0x3 << [XMC4XXX\_GPIO\_DS\_POS](#a0204cbd6c151fcea59199b1c4e007eaf)) |
| --- |

## [◆ ](#a5c307c3181d3094cadb68766b318b3e5)XMC4XXX\_GPIO\_DS\_WEAK

| #define XMC4XXX\_GPIO\_DS\_WEAK   (0x8 << [XMC4XXX\_GPIO\_DS\_POS](#a0204cbd6c151fcea59199b1c4e007eaf)) |
| --- |

## [◆ ](#a52bb9df6ed1e4ead550ceefe1b96a5b3)XMC4XXX\_GPIO\_GET\_DS

| #define XMC4XXX\_GPIO\_GET\_DS | ( |  | *[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) >> [XMC4XXX\_GPIO\_DS\_POS](#a0204cbd6c151fcea59199b1c4e007eaf)) & [XMC4XXX\_GPIO\_DS\_MASK](#a766a7c07cd178b9373fec28745b1e077))

[XMC4XXX\_GPIO\_DS\_POS](#a0204cbd6c151fcea59199b1c4e007eaf)

#define XMC4XXX\_GPIO\_DS\_POS

**Definition** infineon-xmc4xxx-gpio.h:9

[XMC4XXX\_GPIO\_DS\_MASK](#a766a7c07cd178b9373fec28745b1e077)

#define XMC4XXX\_GPIO\_DS\_MASK

**Definition** infineon-xmc4xxx-gpio.h:10

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [gpio](dir_9486826309e816a7a1c2256ae23b5ea4.md)
- [infineon-xmc4xxx-gpio.h](infineon-xmc4xxx-gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
